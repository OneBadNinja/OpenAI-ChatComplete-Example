import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

api_key = os.getenv("GPT_API_KEY")

openai.api_key = api_key

def get_system_message():
    return {"role": "system",
            "content": f"""You are an overly-friendly chatbot. You prefix all your answers with 'Yo broski'"""}

def get_user_message(prompt):
    return {"role": "user",
            "content": prompt}

def get_gpt3_response(prompt, history):

    system = get_system_message()

    messages = [system, *history, prompt]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        temperature=0,
        max_tokens=800,
        n = 1
    )

    return response

history = []

while True:
    prompt = input("Your prompt: ")
    prompt = get_user_message(prompt)
    response = get_gpt3_response(prompt, history)

    message_resp = response["choices"][0]["message"]
    print(f'Reply: {message_resp["content"]}')
    print(f'Usage: {response["usage"]}')
    print("\n\n")

    # Record history to persist context
    history.append(prompt)
    history.append(message_resp)

    # The above causes an issue however because once I exceed the maximum token size, it begins
    # to cut off the context, which includes the system message first!!!
