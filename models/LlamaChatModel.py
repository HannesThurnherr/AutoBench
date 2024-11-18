import os
import time
from openai import OpenAI
from abstract_model import Model

class LlamaChatModel(Model):
    def __init__(self, model_name: str):
        """
        Initialize the LlamaChatModel with a specific model name.
        :param model_name: The name of the model to use (e.g., 'llama3.2-11b-vision').
        """
        super().__init__(model_name)
        self.model_name = model_name

        # Check for API key in environment variables
        if "LLAMA_API_KEY" not in os.environ:
            os.environ["LLAMA_API_KEY"] = input("Please enter your Llama API key: ")

        self.api_key = os.environ["LLAMA_API_KEY"]

        # Initialize the OpenAI client for Llama API
        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.llama-api.com"
        )

    def generate(self, prompt: str, system_prompt: str = None, stop_strings=None, **kwargs) -> str:
        """
        Generates a response from the Llama API based on the provided prompts.
        :param prompt: User prompt to send to the model.
        :param system_prompt: Optional system prompt for context setting.
        :param stop_strings: Optional stop sequences to end the response.
        :param kwargs: Additional arguments for the API.
        :return: Generated text from the model.
        """
        try:
            # Construct the messages list
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})

            # Call the Llama API's chat completion method
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                **kwargs
            )

            # Debugging: Print full response (optional)
            # print(response.model_dump_json(indent=2))

            # Extract and return the content of the first choice
            print(response)
            return response.choices[0].message.content

        except Exception as e:
            print(f"Error occurred: {e}. Pausing for 60 seconds.")
            time.sleep(60)
            return self.generate(prompt, system_prompt, stop_strings, **kwargs)

    def set_api_key(self, key: str):
        """
        Sets a new API key for the Llama API client.
        :param key: New API key.
        """
        os.environ["LLAMA_API_KEY"] = key
        self.client = OpenAI(
            api_key=key,
            base_url="https://api.llama-api.com"
        )
