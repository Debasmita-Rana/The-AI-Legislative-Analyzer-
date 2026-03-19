# The-AI-Legislative-Analyzer-
Team - Code Synth 

Citizen’s Dashboard – AI Powered Policy Simplifier
📌 Project Overview

Indian laws and parliamentary bills are often very long, complex, and difficult for the average citizen to understand. Reading these documents requires time, technical knowledge, and legal understanding. At the same time, running Large Language Models (LLMs) directly on such large documents consumes a huge number of tokens, which increases energy usage and computational cost.

This project builds a Citizen’s Dashboard that simplifies government policies and legal documents into easy-to-understand summaries using token compression + AI summarization.

The system first reduces the size of large policy documents using a lightweight token compression layer. Then, it generates a simplified citizen-friendly summary from the compressed text. This approach improves information density (value per token) while reducing computational cost and energy usage.

🎯 Problem Statement

Build a "Citizen's Dashboard" that provides real-time, simplified summaries of new government policies and legal documents while reducing token usage through token compression.

💡 Solution Approach

The system follows a simple and efficient pipeline:

Input Policy Document
A large government policy or legal document is provided as input.

Token Compression Layer
The system reduces the size of the document by removing unnecessary or repetitive content while keeping the important information.

AI-Based Summarization
The compressed document is passed to an AI model to generate a simplified summary that is easy for citizens to understand.

Citizen-Friendly Output
The final result is a short, clear, and readable version of the policy.

🧠 Key Features

Simplifies complex legal documents

Reduces token usage using compression

Improves information density (more value per token)

Citizen-friendly output

Lightweight and easy to run

Fallback mechanism to avoid API failures

⚙️ Tech Stack

Programming Language

Python 3

Libraries Used

requests – for API communication

os and sys – for file and path handling

AI Tools

Scaledown API (for AI-based compression)

Gemini API (for AI-based summarization)

Token Compression (custom lightweight implementation)

Project Structure

Modular Python architecture (compression.py, pipeline.py, summarizer_api.py)

Text-based input system (policy.txt)

Project Architecture

Policy Text
     ↓
     
Token Compression Layer
     ↓
     
AI Summarization (Gemini API)
     ↓
     
Citizen-Friendly Output

How to Run the Project

1.Install Python 3

2.Install the requirements 

pip install requirements.txt
