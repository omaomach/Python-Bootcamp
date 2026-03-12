import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # This specifically looks for a .env file and loads it

messages = []

client = OpenAI(
    api_key=os.environ.get("OPENAI_CHATBOT_KEY")
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message,
        },
    ),
    chat_completion = client.chat.completions.create( messages=messages,
                                                     model="gpt-4o"
                                                     )

    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }

    messages.append(message)
    print(f"Joash: {message['content']}")

if __name__ == "__main__":
    print(f"Hi, I am Joash, How may I help you?")
    while True:
        user_question = input()
        completion(user_question)