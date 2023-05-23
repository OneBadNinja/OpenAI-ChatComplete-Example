import openai
import os
import lorem
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

api_key = os.getenv("GPT_API_KEY")

openai.api_key = api_key

def get_system_message():
    return {"role": "system",
            "content": f"""You are an overly-friendly chatbot. You always reply in English Pirate!"""}

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

    try:
        response = get_gpt3_response(prompt, history)

        message_resp = list(response["choices"])[0].to_dict()["message"]
        print(f'Reply: {message_resp["content"]}')
        print(f'Usage: {response["usage"]}')
        print("\n\n")

        # Record history to persist context
        history.append(prompt)
        history.append(message_resp)
    except (openai.error.InvalidRequestError, openai.error.RateLimitError) as e:
        if(isinstance(e, openai.error.RateLimitError)):
            print("Rate limit exceeded. You are allowed 3 messages/min. Please try again in a few seconds")
        elif(isinstance(e, openai.error.InvalidRequestError)):
            print("Maximum token size exceeded for the API call (4097 tokens for gpt-3.5-turbo). Trimming the earliest message and attempting again.")
            history = history[1:] # Trim the first message

