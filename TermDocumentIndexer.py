from pathlib import Path
from documents import DocumentCorpus, DirectoryCorpus
from indexing import Index, TermDocumentIndex
from text import BasicTokenProcessor, EnglishTokenStream

"""This basic program builds a term-document matrix over the .txt files in 
the same directory as this file."""

def index_corpus(corpus : DocumentCorpus) -> Index:
    
    token_processor = BasicTokenProcessor()
    vocabulary = set()
    
    # First pass: Build vocabulary
    for d in corpus:
        print(f"Found document {d.title}")
        token_stream = EnglishTokenStream(d.get_content())
        for token in token_stream:
            processed_token = token_processor.process_token(token)
            vocabulary.add(processed_token)
    
    # Build index
    index = TermDocumentIndex(vocabulary, len(corpus))
    
    # Second pass: Index documents
    for d in corpus:
        token_stream = EnglishTokenStream(d.get_content())
        for token in token_stream:
            processed_token = token_processor.process_token(token)
            index.add_term(processed_token, d.id)
    
    return index

if __name__ == "__main__":
    corpus_path = Path("/Users/saqlainpatel/Downloads/SearchEngineTechnology/Moby Dick")
    d = DirectoryCorpus.load_text_directory(corpus_path, ".txt")

    # Build the index over this directory.
    index = index_corpus(d)


    while True:
            # Prompt the user for a term to search for
            term = input("Enter a term to search for (or type 'quit' to exit): ").strip().lower()

            # Check if the user wants to quit
            if term == 'quit':
                print("Exiting...")
                break

            # Search for the term in the index
            postings = list(index.get_postings(term))

            # Print the documents containing the term
            if postings:
                print(f"Documents containing '{term}':")
                for posting in postings:
                    doc = d.get_document(posting.doc_id)
                    print(f"- {doc.title}")
            else:
                print(f"No documents containing '{term}' found.")

    #print("In_main_method_")

    #query = "whale" # hard-coded search for "whale"
    #for p in index.get_postings(query):
    #    print(f"Document {d.get_document(p.doc_id)}")