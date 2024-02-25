import os
from openai import OpenAI
import openai
os.environ['all_proxy'] = '127.0.0.1:7890'
openai.api_key = ('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'
)
def generator(input):
    messages = [
        {"role": "user",
         "content": """find all the colors in the given text' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = chat_completion = openai.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    reply = completion.choices[0].message.content
    return reply
