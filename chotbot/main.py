from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_KEY")
)

def chat_with_gpt(prompt):
    response = client.chatCompletion.create(
        model="gpt-3.0-turbo",
        messages=[
            {"role": "user", "content": "prompt"},
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"Bot: {response}")

