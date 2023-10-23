## Oct. 22nd Notes
Created a quick example of using LlamaIndex to do source-based chat, and it works quite well. 

To run it:
1. Fill in "openai.api_key" in `ask_about_papers.py`.
2. Run `python scripts/ask_about_papers.py`. It by default uses the two papers under `hallucinations_papers_subset` as references.

To include more relevant papers into consideration, run `python scripts/download_papers.py`, which will extract all the mentioned papers and download them into `hallucination_papers`.

Here is an example where I asked it about specific details in the paper, and asked it for advice. They were accurate and decent.
```text
=========================
User: Please give me a summary of the paper "A Token-level Reference-free Hallucination Detection Benchmark for Free-form Text Generation"
=========================
Agent: 
The paper "A Token-level Reference-free Hallucination Detection Benchmark for Free-form Text Generation" presents a new benchmark for hallucination detection in free-form text generation. Hallucination, in this context, refers to the generation of text that is fluent and grammatically correct but factually incorrect or not grounded in the source text. The authors propose a token-level, reference-free approach to hallucination detection, which does not rely on a reference text for comparison. They also introduce a new dataset for this task, which includes annotations at the token level. The paper discusses the challenges of hallucination detection, the design of the new benchmark, and the performance of several models on this task. The authors hope that their work will stimulate further research in this area.
=========================
User: Who are the authors of the paper?
=========================
Agent: 
The authors of the paper "A Token-level Reference-free Hallucination Detection Benchmark for Free-form Text Generation" are Tianyu Liu, Yizhe Zhang, Chris Brockett, Yi Mao, Zhifang Sui, Weizhu Chen, and Bill Dolan.
=========================
User: Which organizations or institutes do they work at?
=========================
Agent: 
The authors of the paper "A Token-level Reference-free Hallucination Detection Benchmark for Free-form Text Generation" are affiliated with Peking University, Tencent Cloud Xiaowei, Meta AI, and Microsoft Corporation.
=========================
User: Can you help me match each author with the organization?
=========================
Agent: 
Sure, here are the affiliations of each author:

- Tianyu Liu is affiliated with Peking University and Tencent Cloud Xiaowei.
- Yizhe Zhang is associated with Meta AI.
- Chris Brockett, Yi Mao, Weizhu Chen, and Bill Dolan are all from Microsoft Corporation.
- Zhifang Sui is from Peking University.
=========================
User: Neat! Which models did they use as baseline when evaluating on the benchmark?
=========================
Agent: 
The authors of the paper used both feature-based models and pretrained transformer models as baselines when evaluating on the benchmark.
=========================
User: What specific pretrained transformer models did they use?
=========================
Agent: 
The authors used a variety of pretrained transformer models, including BERT-large, GPT2-medium, XLNet-large, and RoBERTa-large.
=========================
User: If I want to compare whether a model's hallucination is reduced by RAG technique (Retrieval Augmented Generation), is their benchmark a good choice? What are some pros and cons?
=========================
Agent: 
Yes, their benchmark could be a good choice for comparing whether a model's hallucination is reduced by the RAG (Retrieval Augmented Generation) technique. 

Pros:
1. **Token-level Analysis**: Their benchmark provides a token-level, reference-free approach to hallucination detection. This means it can provide a more granular analysis of where and how hallucinations occur in the generated text.
2. **New Dataset**: They introduce a new dataset for this task, which includes annotations at the token level. This dataset could be useful for training and testing models.
3. **Model Comparison**: The benchmark has been used to evaluate several models, which could provide a basis for comparison.

Cons:
1. **Limited Scope**: The benchmark is designed specifically for hallucination detection in free-form text generation. If your model or the RAG technique has other aspects that need to be evaluated, this benchmark might not cover them.
2. **Annotation Bias**: The dataset used in the benchmark is annotated by humans, which could introduce bias or inconsistency.
3. **Complex Evaluation**: Depending on the complexity of your model and the RAG technique, evaluating them on this benchmark could be computationally intensive or challenging. 

Remember, the choice of benchmark depends on the specific requirements and constraints of your project. It's always a good idea to consider multiple benchmarks and choose the one that best fits your needs.
=========================
```