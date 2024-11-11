# AutoBench: Automated Value Benchmarking for Language Models

### Motivation
Measuring a model’s values is essential to ensuring alignment, and benchmarks like Machiavelli exist to do just that. AutoBench aims to automate this process, creating benchmarks that provide quick insights into model value orientations.

### Overview
AutoBench generates questionnaires to measure a model's alignment with specific value categories. The approach involves:

1. Prompting a Language Model with morally relevant questions.
2. Generating Categorical Responses by asking the model to produce answers aligned with predefined moral categories (e.g., utilitarian, deontological, amoral).
3. Comparing Distributions to reveal value-based differences among models.

For example, AutoBench can compare models by how often they produce utilitarian vs. deontological responses, or explore other axes like conservatism, youth alignment, and more.

### Quick Start

1. Clone this repo:
   `git clone git@github.com:HannesThurnherr/AutoBench.git`
   `cd AutoBench`
   
2. Set up dependencies:
   `pip install -r requirements.txt`

3. Run benchmark generation:
   `python generate_benchmark.py --categories "utilitarian,deontological,amoral"`

4. Evaluate a model's values:
   `python evaluate_model.py --model "MODEL_NAME"`

### Results
The tool provides a distribution across chosen categories, making it easy to compare multiple language models on various moral or ideological dimensions. For instance, you could find that “Model A is 20% more utilitarian than Model B.”
