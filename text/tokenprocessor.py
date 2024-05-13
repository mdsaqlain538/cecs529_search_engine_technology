from abc import ABC, abstractmethod

class TokenProcessor(ABC):
    """A TokenProcessor applies some rules of text processing and normalization to 
    to transform tokens into types and terms."""

    @abstractmethod
    def process_token(self, token : str) -> str:
        """Processes a token into a type."""
        pass
    
    @abstractmethod
    def normalize_type(self, type : str) -> str:
        """Normalizes a type into a term."""
        pass