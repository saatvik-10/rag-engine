from app.services.llm_service import generate_answer

prompt = """
You are a helpful assistant.

Question:
What is 2 + 2?

Answer:
"""

response = generate_answer(prompt)

print(response)