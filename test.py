from llama_index.llms.llama_api import LlamaAPI
from llama_index.core.base.llms.types import ChatMessage
import os
print("imports done")
api_key = os.environ["LLAMA_API_KEY"]
client = LlamaAPI(api_key=api_key)
print("got api key")
messages = [
    ChatMessage(role="system", content="You are a helpful assistant."),
    ChatMessage(role="user", content="What is your name?"),
]
print("compiled messages")
response = client.chat(messages=messages, model="llama3.2-11b-vision")
print(f"Raw response: {response}")
