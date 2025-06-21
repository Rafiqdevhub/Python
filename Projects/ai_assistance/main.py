import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GOOGLE_API_KEY')  
genai.configure(api_key=API_KEY)

# Create the model
model = genai.GenerativeModel('gemini-2.0-flash')

def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to AI Assistant (powered by Gemini)!")
    print("Type 'quit' to exit")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        response = get_ai_response(user_input)
        print(f"\nAI: {response}")

if __name__ == "__main__":
    if not API_KEY:
        print("Error: Please set your GOOGLE_API_KEY in the .env file")
    else:
        main()