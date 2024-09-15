#!/usr/bin/env python
from fastapi import FastAPI
from langserve import add_routes
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter
import os
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from prompts.example import example
from prompts.prompt import response_llm

load_dotenv()
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
DB_URI= os.getenv("DB_URI")

llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=OPENAI_API_KEY)
db = SQLDatabase.from_uri(DB_URI)

def clean_query(query):
    query=query.replace("SQLQuery:","").replace("```sql","").replace("```","")
    ### TODO: CHECK FOR VULNERABILITIES
    ### TODO: CHECK FOR SQL INJECTION
    return query


answer_prompt = PromptTemplate.from_template(response_llm)

query_executor = QuerySQLDataBaseTool(db=db)
query_generator = create_sql_query_chain(llm, db)
sql_response_translator = answer_prompt | llm | StrOutputParser()

chain=(
    RunnablePassthrough\
        .assign(query=query_generator | clean_query)\
        .assign(result=itemgetter("query") | query_executor)
    ) | sql_response_translator 


app = FastAPI(
    title="NLP4E",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)


add_routes(
    app,
    chain,
    path="/news_article",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the NLP4E API, please use the /news_article/playground endpoint to ask questions about the news article database"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)