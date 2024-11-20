from dotenv import load_dotenv
from swarm import Agent
import sqlite3
import os

load_dotenv()
model = os.getenv('LLM_MODEL', 'llama3.2:latest')

conn = sqlite3.connect('workout_data.db')
cursor = conn.cursor()

with open("db_structure.sql", "r") as table_schema_file:
    table_schemas = table_schema_file.read()

# Initialize session history
session_history = []

def add_to_history(agent_name, query, response):
    """Adds an interaction to the session history."""
    session_history.append({
        "agent": agent_name,
        "query": query,
        "response": response
    })

def display_session_history():
    """Displays the full session history."""
    for entry in session_history:
        print(f"Agent: {entry['agent']}\nQuery: {entry['query']}\nResponse: {entry['response']}\n")

def run_sql_select_statement(sql_statement, agent_name):
    """Executes a SQL SELECT statement and returns the results of running the SELECT."""
    connection = sqlite3.connect("workout_data.db")
    cursor = connection.cursor()
    
    try:
        print(f"Executing SQL statement: {sql_statement}")
        cursor.execute(sql_statement)
        records = cursor.fetchall()

        if not records:
            response = "No results found."
        else:
            # Handle COUNT queries specifically
            if "COUNT" in sql_statement.upper():
                count_result = records[0][0] if records else "No count result found."
                response = f"Count result: {count_result}"
            else:
                # Handle general SELECT queries
                column_names = [description[0] for description in cursor.description]
                col_widths = [len(name) for name in column_names]
                for row in records:
                    for i, value in enumerate(row):
                        col_widths[i] = max(col_widths[i], len(str(value)))

                result_str = ""
                header = " | ".join(name.ljust(width) for name, width in zip(column_names, col_widths))
                result_str += header + "\n"
                result_str += "-" * len(header) + "\n"
                
                for row in records:
                    row_str = " | ".join(str(value).ljust(width) for value, width in zip(row, col_widths))
                    result_str += row_str + "\n"
                
                response = result_str

        # Log to session history
        add_to_history(agent_name, sql_statement, response)
        
        return response
    
    except sqlite3.Error as e:
        response = f"An error occurred: {e}"
        add_to_history(agent_name, sql_statement, response)
        return response
    
    finally:
        cursor.close()
        connection.close()

def get_sql_router_agent_instructions():
    return """You are the orchestrator of specialized SQL agents, each of whom handles a specific data-related task. 
    Your job is to interpret the user’s request, identify the correct SQL expert agent to handle it, 
    and seamlessly pass the task to that agent. You do not respond to user queries directly; 
    instead, you ensure that the correct SQL expert agent receives and processes each request.
    
    Choose the best-suited agent based on the keywords, data topics, or context in the user's request 
    and transfer the task to that agent."""

def get_sql_agent_instructions():
    return f"""You are a specialized SQL expert. Your job is to process the user's request for database information, 
    construct a precise SQL SELECT query using the given table schemas, and execute the query to retrieve the requested data.
    
    Your tasks:
    - Carefully interpret each request to build accurate SQL queries.
    - Ensure each query aligns strictly with the table schemas below.
    - Avoid any assumptions beyond the information in these schemas.

    Here are the table schemas for the database you can query:
    
    {table_schemas}

    You are responsible for retrieving the correct data based on each query and delivering it to the user in a concise and accurate format.
    """

def get_diet_agent_instructions(goal, agent_name):
    return """You are a dietary guidance agent specializing in providing nutritional recommendations based on a user's personal goals. 
    Your task is to interpret the user's dietary needs, identify the relevant macros and micros, and offer tailored food suggestions to help them achieve their goals. 
    You respond specifically with dietary advice and do not address requests outside nutritional guidance.
    
    Analyze the user's goals, determine the appropriate nutrient intake based on their specific objectives (e.g., muscle gain, weight loss, maintenance), 
    and suggest relevant food items or daily intake recommendations that align with these targets.
    """

sql_router_agent = Agent(
    name="Router Agent",
    instructions=get_sql_router_agent_instructions(),
    model=model
)
rss_feed_agent = Agent(
    name="RSS Feed Agent",
    instructions=get_sql_agent_instructions() + "\n\nYou are an RSS Feed data expert. Respond enthusiastically and highlight the variety of RSS feeds available. Focus on delivering data specifically related to RSS feeds based on the user’s query.",
    functions=[lambda sql: run_sql_select_statement(sql, "RSS Feed Agent")],
    model=model
)
user_agent = Agent(
    name="User Agent",
    instructions=get_sql_agent_instructions() + "\n\nYou are a User Data expert. Your responses should focus exclusively on data related to users within the database. Always strive to be clear and accurate in fulfilling user data requests.",
    functions=[lambda sql: run_sql_select_statement(sql, "User Agent")],
    model=model
)
analytics_agent = Agent(
    name="Analytics Agent",
    instructions=get_sql_agent_instructions() + "\n\nYou are an Analytics Data expert. Your role is to help the user gain meaningful insights by analyzing data accurately. Pay close attention to numerical accuracy and, where relevant, cite data sources within the database.",
    functions=[lambda sql: run_sql_select_statement(sql, "Analytics Agent")],
    model=model
)
dietary_agent = Agent(
    name="Dietary Agent",
    instructions=get_sql_agent_instructions() + "\n\nYou are a Dietary Data expert. Your job is to provide dietary suggestions based on the user's goals. Focus on suggesting nutrients (macros and micros) tailored to specific user goals within the database.",
    functions=[lambda goal: get_diet_agent_instructions(goal, "Dietary Agent")],
    model=model
)

def transfer_back_to_router_agent(**kwargs):
    """Call this function if a user is asking about data that is not handled by the current agent."""
    return sql_router_agent

def transfer_to_rss_feeds_agent(**kwargs):
    return rss_feed_agent

def transfer_to_user_agent(**kwargs):
    return user_agent

def transfer_to_analytics_agent(**kwargs):
    return analytics_agent

def transfer_to_dietary_agent(goal):
    return dietary_agent.functions[0](goal)

sql_router_agent.functions = [transfer_to_rss_feeds_agent, transfer_to_user_agent, transfer_to_analytics_agent, transfer_to_dietary_agent]
rss_feed_agent.functions.append(transfer_back_to_router_agent)
user_agent.functions.append(transfer_back_to_router_agent)
analytics_agent.functions.append(transfer_back_to_router_agent)