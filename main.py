#main.py
from data_loader import load_data
from tools import create_pandas_tool, create_sql_tool
from agent_setup import setup_agent
import os
from langchain_community.utilities import SQLDatabase

if __name__ == "__main__":
    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        print("Please set the GOOGLE_API_KEY environment variable.")
    else:
        pandas_df, sql_engine, sql_conn = load_data()
        if pandas_df is None:
            print("Error loading data. Exiting.")
            exit()

        sql_db = SQLDatabase(sql_engine)
        pandas_tool = create_pandas_tool(pandas_df)
        sql_tool = create_sql_tool(sql_db)
        tools = [pandas_tool, sql_tool]
        agent = setup_agent(tools, google_api_key)

        print("Welcome to the Data Querying AI Agent (using Gemini)!")
        while True:
            user_question = input("Ask a question about the data (or type 'exit'): ")
            if user_question.lower() == 'exit':
                break

            try:
                response = agent.invoke({"input": user_question})
                print("Answer:", response.get("output"))
                # If "output" doesn't work, try:
                # print("Answer:", response.get("answer"))
            except Exception as e:
                print(f"An error occurred: {e}")

        sql_conn.close()
        print("Goodbye!")