import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming."
        }
    ]
)
print(message.content)
