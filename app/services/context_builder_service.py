def context_builder(results: list[dict]) -> str:
    res_chunk = []

    for result in results:
        source = result["source"]
        page = result["page"]
        chunk = result["text"]

        formatted_schunk = f"""Document::{source}
                            Page: {page}
                            {chunk}
                            """

        res_chunk.append(formatted_schunk)

        context = "\n\n----------------------------------------\n\n".join(res_chunk)

    return context
