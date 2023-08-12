from langchain.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

import os
from constants import CHROMA_SETTINGS


def main():
    embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')

    sentences = ["Hello, how are you?", "I am fine, thank you!"]
    sentence_embeddings = embeddings.encode_kwargs(sentences)

    # Access the embeddings
    for sentence, embedding in zip(sentences, sentence_embeddings):
        print(f"Sentence: {sentence}")
        print(f"Embedding: {embedding}")
        print()


if __name__ == '__main__':
    main()
