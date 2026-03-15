# Simple AWS Agentic AI demo
# This example shows how an AI agent might call an LLM
# using AWS Bedrock and LangChain.

from langchain.llms import Bedrock

def architecture_advisor(question):
    # Initialize Bedrock LLM
    llm = Bedrock(model_id="anthropic.claude-v2")

    # Ask the model for architecture advice
    response = llm(question)

    return response

if __name__ == "__main__":
    question = "What is a good AWS microservices architecture?"
    answer = architecture_advisor(question)
    print(answer)
