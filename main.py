import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
  request = input("\033[34mWhat is your question?\n\033[0m")

  if request.lower() == "exit":
    print("\033[31mGoodbye!\033[0m")
    break
  
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an helpful assistant.Answer the given questions, "},
      {"role": "user", "content": request}
    ]
  )

  print("\033[32m" + completion.choices[0].message.content + "\n")
