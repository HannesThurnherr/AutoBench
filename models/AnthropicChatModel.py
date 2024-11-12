import time
from abstract_model import Model
import anthropic
import os

class AnthropicChatModel(Model):
    def __init__(self, model_name: str):
        super().__init__(model_name)
        self.model_name = model_name

        # Check for API key in environment variables
        if "ANTHROPIC_API_KEY" not in os.environ:
            os.environ["ANTHROPIC_API_KEY"] = input("Please enter your Anthropic API key: ")

        self.api_key = os.environ["ANTHROPIC_API_KEY"]
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate(self, prompt: str, system_prompt: str, stop_strings: str, **kwargs) -> str:
        try:
            messages = [{"role": "user", "content": prompt}]
            params = {
                "model": self.model_name,
                "messages": messages,
                "max_tokens": 4096,
                "stop_sequences": [],
            }
            if system_prompt is not None:
                params["system"] = system_prompt
            completion = self.client.messages.create(**params)
            if len(completion.content) == 0:
                return ""
            return completion.content[0].text
        except:
            print("pausing for 60 seconds")
            time.sleep(60)
            return self.generate(prompt, system_prompt, stop_strings, **kwargs)

    def set_api_key(self, key):
        os.environ["ANTHROPIC_API_KEY"] = key
        self.client = anthropic.Anthropic(api_key=key)