import os
import google.generativeai as genai
from abstract_model import Model

class GeminiChatModel(Model):
    def __init__(self, model_name):
        super().__init__(model_name)
        self.model_name = model_name

        # Check if the API key is available in the environment
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            # Prompt for the key if not set in the environment
            api_key = input("Please enter your Gemini API key: ")
            os.environ["GEMINI_API_KEY"] = api_key  # Set it in the environment

        # Configure the API client with the retrieved key
        genai.configure(api_key=api_key)
        self.client = genai.GenerativeModel(model_name)

    def generate(self, prompt: str, system_prompt: str = None, stop_strings: list = None, **kwargs) -> str:
        # Prepare the messages structure as required by the API.
        messages = [{"role": "user", "content": prompt}]

        # Configure additional parameters if provided.
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        if not stop_strings:
            stop_strings = []

        # Prepare the request parameters.
        params = {
            "prompt": messages,
            "max_tokens": kwargs.get("max_tokens", 4096),
            "stop_sequences": stop_strings,
            # Add other parameters here as needed.
        }

        # Execute the request and handle the response.
        response = self.client.generate_content(prompt)

        # Extract the text from the response if available.
        if response and hasattr(response, 'text'):
            return response.text
        else:
            return ""
