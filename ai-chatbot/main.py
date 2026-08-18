import os
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

load_dotenv()  # This specifically looks for a .env file and loads it

messages = []

API_KEY = os.environ.get("OPENAI_CHATBOT_KEY")
if not API_KEY:
    print("OPENAI_CHATBOT_KEY is not set. Check your .env file.")
    raise SystemExit(1)

client = OpenAI(api_key=API_KEY)

def completion(message):
    messages.append({
        "role": "user",
        "content": message,
    })

    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="gpt-4o",
        )
    except OpenAIError as e:
        messages.pop()  # roll back the user turn appended just above
        print(f"Request failed: {e}")
        return

    reply = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content,
    }

    messages.append(reply)
    print(f"ChatGPT: {reply['content']}")


if __name__ == "__main__":
    print("Hi, I am Joash, How may I help you?")
    while True:
        try:
            user_question = input()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye.")
            break

        cleaned = user_question.strip()
        if not cleaned:
            continue
        if cleaned.lower() in ("quit", "exit"):
            print("Goodbye.")
            break

        completion(user_question)