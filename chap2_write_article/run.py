from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI

def ask_chatgpt(messages):
    response = OpenAI().chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
    )
    return response

prompt_role = "You are an assistant for journalists. \
    Your task is to write articles, based on the FACTS that are given to you. \
    You should respect the instructions: the TONE, the LENGTH, and the STYLE"

from typing import List
def assist_journalist(
    facts: List[str], tone: str, length_words: int, style: str
):
    facts = ", ".join(facts)
    prompt = f"{prompt_role} \
        FACTS: {facts} \
        TONE: {tone} \
        LENGTH: {length_words} words \
        STYLE: {style}"
    return ask_chatgpt([{"role": "user", "content": prompt}])

# print(
#     assist_journalist(
#         ["The sky is blue", "The grass is green"], "informal", 100, "blogpost"
#     )
# )

print(
    assist_journalist(
        facts=[
            "A book on ChatGPT has been published last week",
            "The title is Developing Apps with GPT-4 and ChatGPT",
            "The publisher is O'Reilly.",
        ],
        tone="excited",
        length_words=50,
        style="news flash",
    )
)