import argparse
import re
from typing import List

from openai import OpenAI

OPENAI_API_KEY = ""
MAX_INPUT_LENGTH = 32


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    if validate_length(user_input):
        generate_branding_snippet(user_input)
        generate_keywords(user_input)
    else:
        raise ValueError(f"Input length is too long. Myst be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}")


def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH


def generate_branding_snippet(prompt: str) -> str:
    client = OpenAI(
        api_key=OPENAI_API_KEY
    )
    enriched_branding_prompt = f"Generate upbeat branding snippet for {prompt}: "
    print(enriched_branding_prompt)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": enriched_branding_prompt,
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens=32,
    )

    # Extract output text and stripe whitespace.
    branding_text = chat_completion.choices[0].message.content.strip()
    last_char = branding_text[-1]

    # Add ... to truncated statements.
    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    print(f"Snippet: {branding_text}")
    return branding_text


def generate_keywords(prompt: str) -> List[str]:
    client = OpenAI(
        api_key=OPENAI_API_KEY
    )
    enriched_keywords_prompt = f"Generate related branding keywords for {prompt}: "
    print(enriched_keywords_prompt)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": enriched_keywords_prompt,
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens=32,
    )

    # Extract output text and stripe whitespace.
    keywords_txt = chat_completion.choices[0].message.content.strip().lower()
    keywords_array = re.split(",|\n|\*|-", keywords_txt)
    keywords_array = [k.strip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k) > 0]
    formatted_keywords = [re.sub(r'^\d+\.\s*', '', keyword) for keyword in keywords_array]

    print(f"Result: {formatted_keywords}")
    return formatted_keywords


if __name__ == "__main__":
    main()
