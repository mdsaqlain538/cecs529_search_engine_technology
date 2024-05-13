from .tokenprocessor import TokenProcessor
import re

class BasicTokenProcessor(TokenProcessor):
    """A BasicTokenProcessor creates terms from tokens by removing all non-alphanumeric characters 
    from the token, and converting it to all lowercase."""
    whitespace_re = re.compile(r"\W+")
    
    def process_token(self, token : str) -> str:
        # Remove non-alphanumeric characters and convert to lowercase.
        return re.sub(self.whitespace_re, "", token).lower()

    def normalize_type(self, type : str) -> str:
        # Don't do anything to normalize types.
        return type