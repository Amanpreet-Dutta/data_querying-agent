from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor, ZeroShotAgent
from langchain.tools import Tool
from langchain_community.utilities import SQLDatabase
from langchain.chains import LLMChain

def setup_agent(tools: list[Tool], google_api_key: str):
    """Sets up the LangChain ZeroShotAgent with tools and memory using Gemini."""
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=google_api_key, api_version="v1")
    memory = ConversationBufferMemory(memory_key="chat_history")

    tool_names = ", ".join([tool.name for tool in tools])
    tool_descriptions = "\n".join([f"{tool.name}: {tool.description}" for tool in tools])

    prefix = f"""You are a helpful AI agent that can answer questions about employee data.
The data is stored in a SQL database with a table named 'employees'.
The 'employees' table has the following columns: 'department', 'employee_id', and 'salary'.
You also have access to a Pandas DataFrame named 'df' containing the same employee data.

You have access to the following tools:
{tool_descriptions}

Use the following format:

Question: {{input}}
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the input question

Begin!

Question: {{input}}
{{agent_scratchpad}}"""

    prompt = PromptTemplate.from_template(prefix, template_format="jinja2")
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
    agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True, handle_parsing_errors="Check your output and try again.")
    return agent_executor

if __name__ == "__main__":
    from data_loader import load_data
    from tools import create_pandas_tool, create_sql_tool
    import os

    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        print("Please set the GOOGLE_API_KEY environment variable.")
    else:
        pandas_df, sql_engine, sql_conn = load_data()
        if pandas_df is not None:
            sql_db = SQLDatabase(sql_engine)
            pandas_tool = create_pandas_tool(pandas_df)
            sql_tool = create_sql_tool(sql_db)
            tools = [pandas_tool, sql_tool]
            agent = setup_agent(tools, google_api_key)
            print("LangChain ZeroShotAgent initialized with tools and memory using Gemini.")
            sql_conn.close()
        else:
            print("Failed to load data, agent not initialized.")
            