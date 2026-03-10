import os

from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-5.4",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)