import os
from openai import OpenAI
from abstract_model import Model
import backoff
import tiktoken
from openai._exceptions import (
    APIConnectionError,
    RateLimitError,
)


class OpenAIChatModel(Model):
    def __init__(self, model_name: str):
        super().__init__(model_name)
        self.model_name = model_name

        # Check for API key in environment variables
        if "OPENAI_API_KEY" not in os.environ:
            os.environ["OPENAI_API_KEY"] = input("Please enter your OpenAI API key: ")

        if not "gpt-4o" in model_name:
            self.tokenizer = tiktoken.encoding_for_model(model_name)

    def generate(self, prompt: str, system_prompt: str | None, stop_strings, **kwargs) -> str:
        assert isinstance(prompt, str), "Prompt must be a string."
        if kwargs.get("prepend_completion", None):
            prompt += kwargs.pop("prepend_completion")
        params = {
            "prompt": prompt,
            "stop_strings": stop_strings,
        }
        if system_prompt is not None:
            params["system_prompt"] = system_prompt
        completion = self._call_gpt_api(**params, **kwargs)
        return completion

    @backoff.on_exception(
        backoff.expo,
        exception=(
            RateLimitError,
            APIConnectionError,
        ),
        max_value=60,
        factor=1.5,
    )
    def _call_gpt_api(self, prompt, stop_strings, system_prompt="", **kwargs) -> str:
        messages = [
            {"role": "user", "content": prompt},
        ]
        if system_prompt:
            messages = [{"role": "system", "content": system_prompt}] + messages
        response = OpenAI().chat.completions.create(model=self.model_name, messages=messages, **kwargs)
        return response.choices[0].message.content

    def set_api_key(self, key):
        os.environ["OPENAI_API_KEY"] = key
