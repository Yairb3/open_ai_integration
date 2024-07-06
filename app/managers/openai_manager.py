import os
from openai import OpenAI
from dotenv import load_dotenv

class OpenAIManager:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        self.client = OpenAI(api_key=self.api_key)

    async def get_answer(self, question: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": question},
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

