from datetime import datetime


def log_query(
    query: str,
    results: list[dict],
    context_chars: int,
    prompt_chars: int,
    model: str,
    prompt_tokens: int,
    completion_tokens: int,
    total_tokens: int,
    cost: float,
    latency: float,
    answer: str,
):
    print("\n" + "=" * 60)
    print(f"RAG QUERY LOG | {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 60)

    print(f"Query: {query}")

    print("\nRetrieved Chunks:")
    for result in results:
        print(
            f"• {result['source']} | "
            f"Page {result['page']} | "
            f"Score: {result['score']:.3f}"
        )

    print("\nContext")
    print(f"Characters: {context_chars}")

    print("\nPrompt")
    print(f"Characters: {prompt_chars}")

    print("\nLLM")
    print(f"Model: {model}")
    print(f"Prompt Tokens: {prompt_tokens}")
    print(f"Completion Tokens: {completion_tokens}")
    print(f"Total Tokens: {total_tokens}")
    print(f"Cost: ${cost:.8f}")

    print("\nPerformance")
    print(f"Latency: {latency:.2f}s")

    print("\nAnswer")
    print(answer)

    print("=" * 60 + "\n")
