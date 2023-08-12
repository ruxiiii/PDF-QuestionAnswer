# import os
# from chromadb.config import Settings
# import chromadb




# #define the chroma settings
# CHROMA_SETTINGS = Settings(
#     storage_backend= 'duckdb + parquet', #parquet is file format, duckdb make data analysis and searching of parquet better

#     storage_path= 'db',
#     anonymized_telemetry= False
# )

# client = chromadb.PeristentClient(path = 'db')
# CHROMA_SETTINGS = Settings(
#     anonymized_telemetry= False,
    
# )


import chromadb
from chromadb.config import Settings

CHROMA_SETTINGS = chromadb.PersistentClient(path = 'db', settings=Settings(anonymized_telemetry= False))

# CHROMA_SETTINGS = chromadb.Client(
#     Settings(
#         # chroma_db_impl='duckdb+parquet',
#         # persist_directory='db',
#         anonymized_telemetry=False,
        
#     )
# )
