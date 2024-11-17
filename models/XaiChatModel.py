import os
import time
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

class XaiChatModel:
    def __init__(self, model_name: str):
        self.model_name = model_name

        # Check for API key in environment variables
        if "XAI_API_KEY" not in os.environ:
            os.environ["XAI_API_KEY"] = input("Please enter your xAI API key: ")

        self.api_key = os.environ["XAI_API_KEY"]
        self.client = Anthropic(
            api_key=self.api_key,
            base_url="https://api.x.ai",
        )

    def generate(self, prompt: str, system_prompt: str = None, max_tokens=None, **kwargs) -> str:
        try:
            # Validate or set max_tokens
            if max_tokens is None or max_tokens == "":
                max_tokens = 16
            elif not isinstance(max_tokens, int):
                try:
                    max_tokens = int(max_tokens)
                except ValueError:
                    raise ValueError(f"Invalid max_tokens value: {max_tokens}. It must be an integer.")

            # Build the conversation prompt
            conversation = ""
            if system_prompt:
                conversation += system_prompt + "\n\n"
            conversation += f"{HUMAN_PROMPT} {prompt}{AI_PROMPT}"

            response = self.client.completions.create(
                model=self.model_name,
                prompt=conversation,
                max_tokens_to_sample=max_tokens,
                **kwargs
            )
            out = response.completion.strip()
            #print(out)
            return out
        except ValueError as ve:
            print(f"Input error: {ve}")
            return ""
        except Exception as e:
            print(f"Error: {e}. Pausing for 60 seconds.")
            time.sleep(60)
            return self.generate(prompt, system_prompt, max_tokens, **kwargs)

    def set_api_key(self, key: str):
        os.environ["XAI_API_KEY"] = key
        self.client = Anthropic(
            api_key=key,
            base_url="https://api.x.ai",
        )
