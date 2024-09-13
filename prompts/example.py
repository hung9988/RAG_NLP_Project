
example=[
   # {"input": "Cho toi bai bao ve dhbkhn", "output": "SELECT * FROM news_article WHERE title LIKE '%dhbkhn%'"},
 
    {"input": "các bài báo về 'khcn'", "query": "\n\nSELECT \"id\", \"title\", \"url\", \"description\", \"published_date\", \"author\" \nFROM \"News\" \nWHERE \"cat\" = 'KHCN' \nORDER BY \"published_date\" DESC \nLIMIT 5;\n"},
    {"input": "các bài báo về 'khoa học công nghệ'", "query": "\n\nSELECT \"id\", \"title\", \"url\", \"description\", \"published_date\", \"author\" \nFROM \"News\" \nWHERE \"cat\" = 'KHCN' \nORDER BY \"published_date\" DESC \nLIMIT 5;\n"},
    {"input": "các bài báo về 'khoa học'", "query": "\n\nSELECT \"id\", \"title\", \"url\", \"description\", \"published_date\", \"author\" \nFROM \"News\" \nWHERE \"cat\" = 'KHCN' \nORDER BY \"published_date\" DESC \nLIMIT 5;\n"},
    {"input": "các bài báo về 'công nghệ'", "query": "\n\nSELECT \"id\", \"title\", \"url\", \"description\", \"published_date\", \"author\" \nFROM \"News\" \nWHERE \"cat\" = 'KHCN' \nORDER BY \"published_date\" DESC \nLIMIT 5;\n"},
    {"input": "các bài báo về 'A' tháng 8", "query":"\n\nSELECT \"id\", \"title\", \"url\", \"description\", \"published_date\", \"author\" \nFROM \"News\" \nWHERE \"published_date\" LIKE '2024-08%' \nAND \"cat\" = 'A' \nORDER BY \"published_date\" DESC \nLIMIT 5;\n"  },
    {"input": "các bài báo về 'đại học bách khoa hà nội'", "query":"\n\nSELECT \"id\", \"title\", \"url\", \"description\", \"content\",\"published_date\", \"author\" \nFROM \"News\" \nWHERE \"title\" ILIKE '%Đại học Bách Khoa Hà Nội%' \nLIMIT 5;\n" }
]
from langchain_core.prompts import PromptTemplate
example_prompt = PromptTemplate.from_template("User input: {input}\nSQL query: {query}")