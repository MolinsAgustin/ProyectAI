from langchain_openai import ChatOpenAI
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
# Instanciamiento modelo OpenAI
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", api_key=openai_api_key)

# Start database
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

# Creo agente
agent_executor = create_sql_agent(llm=llm, db=db, agent_type="openai-tools", verbose=False)

def invocar_agente(entrada_usuario):
    return agent_executor.invoke(entrada_usuario)