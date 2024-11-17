# AutoBench: for Quick Automated Value Benchmarking of Language Models

### Motivation
Measuring a model’s values is essential to ensuring alignment, and benchmarks like Machiavelli exist to do just that. AutoBench aims to automate this process, creating benchmarks that provide quick insights into model value orientations.

### Overview
AutoBench provides an interface to generate questionnaires to measure a model's values. The approach involves:

1. Load a dataset of relevant questions and select interesting, competing answer categories (eg. optimist and pessimist).
2. Use an LLM to generate an answer option of each category for each question.
3. Present the generated questionnaire to various language models, prompting them to select an answer.
4. Compare the resulting answer distributions across the categories to assess relative values across models.
   
<div align="center">
    <img src="https://github.com/user-attachments/assets/180477e1-418b-48ee-984b-48466b014544" width="800" alt="Screenshot 2024-11-12 at 21 47 07">
</div>
For example, AutoBench can compare models by how often they produce utilitarian vs. deontological responses, or explore other axes like conservatism, optimism-pessimis, opinions about code, and more.

```bash
# 1. Clone the Repository
git clone git@github.com:HannesThurnherr/AutoBench.git
cd AutoBench

# 2. Set Up a Virtual Environment
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Run the Code
streamlit run autobench_app.py
```

### Results
The tool provides a distribution across chosen categories, making it easy to compare multiple language models on various moral or ideological dimensions. For instance, you could find that “Model A is 20% more utilitarian than Model B.”
<img width="2087" alt="Screenshot 2024-11-12 at 22 03 19" src="https://github.com/user-attachments/assets/9011b39d-e559-4cc8-80d1-586385bacb4a">

### Available Models
Currently, all models from OpenAI, Anthropic, and Xai are integrated. Additionally, many open-source models like the Llama series, Gemma 2, Qwen1.5 and 2, several models from Mistral, and some Nous-Hermes finetunes are supported using the [Llama API](https://www.llama-api.com/).

Models can easily be added by modifying the `models_config.json` file and, if necessary, implementing a new model class that inherits from the abstract `Model` class.

The respective API key can be entered in the terminal when necessary but it is recommended to configure the evironment variables `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `XAI_API_KEY` and `LLAMA_API_KEY` with the respective keys.
### Available Question-Datasets
Currently there are 6 datasets of questions available. The following four are all categories from the [SQUARE dataset](https://github.com/naver-ai/korean-safety-benchmarks/tree/main).
- Contentious questions
- Ethical questions
- Predictive Questions
- Etc Questions
- AITA Dilemmas
- CodeInsights samples

The first four datasets are all categories from the [SQUARE dataset](https://github.com/naver-ai/korean-safety-benchmarks/tree/main).
In addition to this there are also a set of social dilemmas of the form "Am I bad for X", with X being some controversial action. This data is taken from the [Scruples dataset](https://github.com/allenai/scruples) which pulls data from the "Am I the A-hole"-subreddit.
To analize technical tendencies there is also a set of short code samples from the [CodeInsights dataset](https://github.com/NathanaelBeau/CodeInsight/tree/main). This may allow evaluation alon axes like "how opinionated is the model about code formating". The questions always in the format:
```python
#Comment describing whats to be implemented
def foo():
    return code_implementing_task()

What do you think of this code?
```

Datasets can easily be added by placing a json file containing a list of strings (the questions) in the `datasets` folder.

