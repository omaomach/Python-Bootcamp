import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # This specifically looks for a .env file and loads it

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)