from retrieval.rag_orchestrator import answer_question

if __name__ == "__main__":
    question = "What are the latest news updates from India?"
    print("\nUser Question:", question)
    print("\n--- Answer ---\n")
    print(answer_question(question))
