import os
from openai import OpenAI

client = OpenAI(
  base_url='http://10014343-0.local:1337/v1',
  api_key='not uise'
)

model = "gemma-2-2b-it"

prompt = input('prompt:')

completion = client.chat.completions.create(
  model=model,
  messages=[
    {"role": "system", "content": "日本語で答えてください。"},
    {"role": "user", "content": prompt},
  ],
  temperature=0.7,
  max_completion_tokens=1000,
)

print(completion.choices[0].messages.content)
