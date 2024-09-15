from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from .prompt import *
from .example import *

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

extraction_few_shot_example = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=extraction_examples,
)

summarize_few_shot_example = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=summarization_examples,
)

entites_extraction_template=ChatPromptTemplate.from_messages([
    ("system", entities_extraction_prompt),
    extraction_few_shot_example,
    ("human","Context: {context}"),
    ("human","Input: {input}")
])

history_summarization_template=ChatPromptTemplate.from_messages([
    ("system", history_summarization_prompt),
    summarize_few_shot_example,
    ("human","Chat history: {input}")
])

sql_response_parsing_template=ChatPromptTemplate.from_messages([
    ("system", sql_response_parsing_prompt),
    ("human","{input}")
])

