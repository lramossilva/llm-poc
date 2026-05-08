import requests
from llm.base import LLM

class LlamaLocal(LLM):
    def __init__(self, model: str = "llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def ask(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        response = requests.post(self.url, json=payload)
        response.raise_for_status()

        return response.json()["response"].strip()
