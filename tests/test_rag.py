from app.rag.qa_chain import ask_question

question = "What is Artificial Intelligence?"

answer = ask_question(question)

print(answer)