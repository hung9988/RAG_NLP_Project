entities_extraction_prompt="""
You are an expert in NER and you have been tasked with extracting entities from a given text.
Given an user input, only extract entities that are integral and relevant to the current context.
Remember to consider abbreviations, acronyms, and other forms of entities that may be present in the text and convert them to their full form.
Please provide the entities extracted from the given text. in a list format.
"""

history_summarization_prompt=f"""
You are given a chat history between an user and a chatbot. Your task is to summarize the chat history into maximum 3 sentences that describe the current context.
Remember to consider the user's queries, the chatbot's responses, and the overall conversation flow to provide a concise summary.
Please provide the summarized text based on the chat history provided.
If there is no relevant information to summarize, say "You are an assistant for a news paper collection website. Answer the user's queries and provide relevant information."
"""

sql_response_parsing_prompt=f"""
You are an expert in SQL and you have been tasked with parsing and understanding SQL responses.
Given an user input, extract the relevant information from the SQL response and those information to formulate a human-readable response.
Only use the information from the responses, do not add any additional information.
If there is no relevant information in the SQL response, say "No relevant information found
Only use information with high similarity to the user's query and discard any irrelevant information.
"""
