from langchain.llms import Bedrock

class ArchitectureAgent:

    def __init__(self):
        self.llm = Bedrock(
            model_id="anthropic.claude-v2"
        )

    def ask_architecture_question(self, question):
        prompt = f"""
        You are an enterprise architecture advisor.

        Answer the following architecture question:

        {question}
        """

        response = self.llm(prompt)
        return response


if __name__ == "__main__":

    agent = ArchitectureAgent()

    question = "What is a good AWS microservices architecture?"

    answer = agent.ask_architecture_question(question)

    print(answer)
