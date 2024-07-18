# Glossary

- **transformer architecture** - what makes the transformer mechanism so effective is the **attention mechanism**, which narrows the model’s focus to the whole input sequence while it generates text one word at a time. these initial transformers were used for machine translation.
- original transformers had both an **encoder** for parsing text and a **decoder** for generating text. GPT only uses the decoder portion, which keeps the model simpler.
- autoregressive models
- emergent behaviors - these LLM models are powerful because they exhibit **emergent behaviors** like the capacity for translation—behaviors the LLMs haven’t been specifically trained to do.
- **tokenization** - the process of splitting text into individual tokens, which is a required preprocessing step for creating embeddings for an LLM
- **embedding** - converting data into a vector format—a mathematical model that a computer can use to do things with non-numerical, categorical data like text. Different data formats, like text, image, and music, require different embedding models. An embedding is a mapping from discrete objects to points in a continuous vector space. In an embedding, each token becomes a specific point in the continuous vector space.
- data sampling pipeline
- **RAG** - retrieval-augmented generation. An embedding model that embeds entire sentences or paragraphs to pull specific, detailed information when generating text.
- **special context tokens** - tokens that increase a model’s understanding of context or other relevant info in the text—markers for unknown words, document boundaries, etc. Common special context tokens include:
     - end of text
     - unknown words
     - beginning of sequence
     - end of sequence (basically, same as end of text tokens)
     - padding
Note that GPT tokenizers don’t use <unk> tokens for words outside the model’s vocabulary. Instead, they use byte pair encoding—breaking down individual words into sub-word units.
- **byte pair encoding** - a way of encoding an entire vocabulary out of small chunks of words—first letters, then common combinations of letters. This allows the encoder to encode even made-up words without having to resort to the <unk> special context token.
- **input-target pairs** -
- **PyTorch** - PyTorch has three components:
  1. tensor library - helps you use GPU acceleration for faster computations
  2. automatic differentiation engine - “autograd” - “provides functions to automatically compute gradients in dynamic computational graphs“
  3. neural network module - simplifies the implementation of neural networks. ChatGPT: “This module includes pre-defined layers (such as linear layers, convolutional layers, activation functions, etc.) and utilities for building and training neural networks. It allows you to define your neural network architecture as a sequence of layers and provides tools for managing parameters, computing losses, and optimizing models during training.”
- **tensor** - even after you have your encoding/decoding tokenizer, there’s still a need for representing words as *continuous valued vectors*. This is what tensors do (apparently). Sections 2.6 and A2.2 explain these things. Tensors are mathematical entities that “generalize vectors and matrices to potentially higher dimensions.” 
	- A *scalar* (just a single number) is a tensor of rank 0. 
	- A *vector* (single row or column of numbers) is a tensor of rank 1. 
	- A 2d matrix is a tensor of rank 2. 
Tensors are multi-dimensional data containers, with each dimension representing a different feature.

- **autograd** - “provides functions to automatically compute gradients in dynamic computational graphs“
- **computational graph** - “a directed graph that allows us to express and visualize mathematical expressions … lays out the sequence of calculations needed to compute the output of a neural netowrk.” e.g. computes the required gradients for backpropagation, the main training algorithm for neural networks. Per ChatGPT: “Computation graphs are like roadmaps that show how calculations flow from inputs to outputs in a model. The computation graph visually represents the flow of calculations in a machine learning model, including the forward pass in logistic regression.”
- **logistic regression forward pass** - Per ChatGPT: “Logistic regression is a type of algorithm used for binary classification, which means it predicts one of two outcomes (like yes/no, true/false). The goal is to find a line (or boundary) that separates the two classes based on the input data.” Logical regression algorithms have four elements:
	- inputs / features: the elements of data you have
	- weights / parameters: how important each feature is
	- bias / intercept: a baseline prediction that the model starts with
	- prediction: multiply the feature * weight, add the bias, then apply a **sigmoid function**, which gives you a probability score between 0 and 1.
- **sigmoid function** - a function (built into PyTorch, in this case) that allows you to compute the probability of a given output
