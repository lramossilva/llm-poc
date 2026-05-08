from abc import ABC, abstractmethod

class LLM(ABC):
    @abstractmethod
    def ask(self, prompt: str) -> str:
        """Envia uma pergunta ao modelo e retorna a resposta"""
        pass