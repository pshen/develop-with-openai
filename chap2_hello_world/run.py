from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI


chat_completion = OpenAI().chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello World!"}],
)
# Extract the response
print(chat_completion)