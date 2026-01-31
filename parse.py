from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = (
    "You are tasked with extracting specific information from the following text content.\n\n"
    "CONTENT:\n{dom_content}\n\n"
    "INSTRUCTIONS:\n"
    "1. Extract ONLY information matching: {parse_description}\n"
    "2. Do not add explanations or comments.\n"
    "3. If nothing matches, return an empty string.\n"
    "4. Return only clean extracted data.\n"
)


model = OllamaLLM(model="llama3.1:latest")


def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    total = len(dom_chunks)

    for i, chunk in enumerate(dom_chunks, start=1):
        try:
            response = chain.invoke(
                {
                    "dom_content": chunk,
                    "parse_description": parse_description,
                }
            )

            print(f"Parsed batch {i}/{total}")
            parsed_results.append(response.strip())

        except Exception as e:
            print(f"Error parsing chunk {i}: {e}")

    return "\n".join(filter(None, parsed_results))
