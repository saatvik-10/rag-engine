def prompt_builder(question: str, context: str) -> str:
    prompt = f"""
    You are a helpful AI assistant.
    
    Answer the user's question only using the provided context.
    
    If the answer cannot be found in the provided context, respond with "I don't know based on the provided context."
    
    Do not make up information.
    
    If relevant, mention the document name and page number in your answer.
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:
    """

    return prompt
