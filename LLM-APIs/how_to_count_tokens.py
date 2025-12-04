import tiktoken

enc = tiktoken.encoding_for_model("gpt-4.1-mini")

text = "Julien is building AI systems in Africa."
tokens = enc.encode(text)

print(f"Number of tokens: {len(tokens)}")
