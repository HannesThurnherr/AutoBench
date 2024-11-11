from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name
        super().__init__()

    @abstractmethod
    def generate(self, prompt: str, system_prompt: str, stop_strings: str, **kwargs) -> str:
        """
        Generate a response based on the input prompt, system_prompt, and stop_strings.

        :param prompt: The input text for the model.
        :param system_prompt: An system-level prompt that provides additional context.
        :param stop_strings: A string or list of strings that signal the end of a completion.
        :param kwargs: Additional keyword arguments for flexibility.
        :return: A string that is the model's generated response.
        """
        pass