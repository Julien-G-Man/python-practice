import openai

openai.api_key = "API_KEY"

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain the history of the PayPal Mafia,"}
    ]
)

resp = response["choices"][0]["messages"]["content"]
print(resp)