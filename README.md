Markdown

# Data Querying AI Agent (using Gemini)

This project is a Python-based AI agent that allows you to ask questions about a structured dataset (currently loaded into a Pandas DataFrame and an in-memory SQLite database) using natural language. It leverages the power of the Google Gemini language model through LangChain to understand your queries and interact with the data using either Pandas operations or SQL queries.

**Important Note:** This application runs entirely within your **terminal or command line interface**. There is **no graphical user interface (frontend)** for this project. All interaction with the agent happens through text input and output in the terminal.

## Overview

The agent is designed to:

1.  **Load Data:** Reads data from a (currently dummy) CSV file into a Pandas DataFrame and an in-memory SQLite database.
2.  **Understand Questions:** Uses the Google Gemini model to interpret user questions.
3.  **Choose the Right Tool:** Decides whether to use Pandas (for complex data manipulation and analysis) or SQL (for querying and filtering) to answer the question.
4.  **Execute Operations:** Runs the appropriate Python code (Pandas) or SQL queries.
5.  **Provide Answers:** Returns the results of the data operations in a user-friendly format **directly in the terminal**.
6.  **Maintain Conversation History:** Remembers previous questions and answers to provide more contextual responses **within the same terminal session**.

## Setup

Follow these steps to get the project running:

1.  **Clone the Repository (if you've pushed it to Git):**
    ```bash
    git clone <your_repository_url>
    cd data-querying-agent
    ```

2.  **Create a Virtual Environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS and Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (This assumes you have a `requirements.txt` file with the necessary libraries. If not, create one with `langchain`, `pandas`, `sqlalchemy`, `sqlite3`, `google-generativeai`, `langchain-google-genai`, `langchain-community`, and `jinja2`).

4.  **Set the Google API Key:**
    You need a Google Cloud API key with access to the Gemini API.
    * Go to the [Google Cloud Console](https://console.cloud.google.com/).
    * Create a project or select an existing one.
    * Enable the Gemini API.
    * Create API credentials.
    * Set the `GOOGLE_API_KEY` environment variable:
        ```bash
        # For current terminal session (replace with your actual key)
        export GOOGLE_API_KEY="YOUR_API_KEY"  # macOS/Linux
        set GOOGLE_API_KEY="YOUR_API_KEY"     # Windows (Command Prompt)
        $env:GOOGLE_API_KEY="YOUR_API_KEY"    # Windows (PowerShell)
        ```
        For permanent setting, refer to your operating system's instructions for environment variables.

## Running the Agent

1.  **Navigate to the project directory in your terminal.**
2.  **Ensure your virtual environment is activated.**
3.  **Run the `main.py` script:**
    ```bash
    python main.py
    ```

4.  **Interact with the Agent (in the terminal):** The agent will prompt you to ask questions about the data **directly in the terminal**. Type your questions in natural language and press Enter. The agent's responses will also appear **in the terminal**. Type `exit` to end the conversation.

    ```
    Welcome to the Data Querying AI Agent (using Gemini)!
    Ask a question about the data (or type 'exit'): What is the average salary?
    Answer: ... (The agent's response will be here)
    Ask a question about the data (or type 'exit'):
    ```

## Example Questions

Based on the current dummy data (employees table with 'department', 'employee_id', 'salary' columns):

* What is the average salary?
* Show all departments.
* How many employees are in the Sales department?
* What are the employee IDs?
* What is the highest salary in the Finance department?

You can also try more complex questions that might involve Pandas:

* What is the average salary for each department?

**Remember, all interaction happens directly within your terminal.**

