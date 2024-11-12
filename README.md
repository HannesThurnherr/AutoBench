# AutoBench: Automated Value Benchmarking for Language Models

### Motivation
Measuring a model’s values is essential to ensuring alignment, and benchmarks like Machiavelli exist to do just that. AutoBench aims to automate this process, creating benchmarks that provide quick insights into model value orientations.

### Overview
AutoBench generates questionnaires to measure a model's alignment with specific value categories. The approach involves:

1. Prompting a Language Model with morally relevant questions.
2. Generating Categorical Responses by asking the model to produce answers aligned with predefined moral categories (e.g., utilitarian, deontological, amoral).
3. Comparing Distributions to reveal value-based differences among models.
<img width="1778" alt="Screenshot 2024-11-12 at 21 45 21" src="https://github.com/user-attachments/assets/37010f84-b9c3-4273-98b0-9aa58a867be6">

For example, AutoBench can compare models by how often they produce utilitarian vs. deontological responses, or explore other axes like conservatism, youth alignment, and more.

### Quick Start

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
