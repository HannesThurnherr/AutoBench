import google.generativeai as genai
from abstract_model import Model

class GeminiChatModel(Model):
    def __init__(self, model_name):
        super().__init__(model_name)
        self.model_name = model_name
        genai.configure(api_key=input("your Gemini API key: "))
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
