#tools.py

from langchain.tools import Tool
import pandas as pd
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase

def create_pandas_tool(df: pd.DataFrame):
    """Creates a LangChain tool for querying a Pandas DataFrame."""
    def run_pandas_code(query: str) -> str:
        try:
            local_namespace = {"df": df}
            result = eval(query, globals(), local_namespace)
            return str(result)
        except Exception as e:
            return f"Error executing Pandas query: {e}"

    return Tool(
        name="pandas_data_analysis",
        func=run_pandas_code,
        description="Useful for performing operations and queries on the pandas DataFrame.",
    )

def create_sql_tool(db: SQLDatabase):
    """Creates a LangChain tool for querying a SQL database."""
    def run_sql(query: str) -> str:
        try:
            result = db.run(query)
            return result
        except Exception as e:
            return f"Error executing SQL query: {e}"

    return Tool(
        name="sql_query",
        func=run_sql,
        description="Useful for querying the SQL database.",
    )

if __name__ == "__main__":
    from data_loader import load_data
    pandas_df, sql_engine, sql_conn = load_data()
    pandas_tool = create_pandas_tool(pandas_df)
    sql_db = SQLDatabase(sql_engine)
    sql_tool = create_sql_tool(sql_db)

    print("Pandas Tool:", pandas_tool.name)
    print("SQL Tool:", sql_tool.name)
    sql_conn.close()