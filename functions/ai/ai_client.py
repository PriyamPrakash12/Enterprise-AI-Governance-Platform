from abc import ABC, abstractmethod

class AIClient(ABC):
    @abstractmethod
    def classify(self, prompt: str):
        pass