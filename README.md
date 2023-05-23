## Instructions

1. Create an OpenAI Account

Sign up at [the openai website](https://openai.com) and login to the [platform](https://platform.openai.com/)

2. Create an API key 

Go to ```Manage Account -> API Keys``` and generate one. Copy this key and store it in a ```.env``` file you create in the root directory of this repository

```.env

GPT_API_KEY=<your_api_key>

```

3. Create a virtual environment and install dependencies

First create a virtual environment in the root directory and activate it

```
# Create a virtual environment named venv
python3 -m venv venv

# Activate it
. ./venv/bin/activate
```

Now install your dependencies

```
pip3 install -r requirements.txt
```

4. Run the application

```
python3 app/main.py
```