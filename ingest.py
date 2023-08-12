from langchain.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

from langchain.vectorstores import Chroma

import os
from constants import CHROMA_SETTINGS
import chromadb


persist_directory = 'db'

def main():

    pdf_loaders = []
    
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('.pdf'):
                print(file)
                loader = PyPDFLoader(os.path.join(root,file))
                pdf_loaders.append(loader)


    documents = []

    #load the documents using all the loaders

    for loader in pdf_loaders:
        documents.extend(loader.load())


        
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0) 

    #splitting
    texts = text_splitter.split_documents(documents)

    #create embeddings here
    embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')


    #create vector store
    db = Chroma.from_documents(texts, 
                               embeddings
                            #    persist_directory=persist_directory,
                            #     client_settings=CHROMA_SETTINGS
                               )
    # db.persist()
    # db=None

if __name__ == '__main__':
    main()