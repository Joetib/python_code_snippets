# Use the 'whoosh' library to create a simple search engine
# Install whoosh using:
# >> pip install whoosh

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, KEYWORD, ID
from whoosh.qparser import QueryParser
# Define the schema for the search engine
schema = Schema(title=TEXT(stored=True), content=TEXT, path=ID(stored=True))
index_dir = "indexdir"
ix = create_in(index_dir, schema) # Create an index in a directory
writer = ix.writer() # Add documents to the index
writer.add_document(title="Document 1", content="This is the content of document 1")
writer.add_document(title="Document 2", content="Content for document 2")
writer.commit()

with ix.searcher() as searcher: # Search the index
    query = QueryParser("content", ix.schema).parse("search keywords")
    results = searcher.search(query)
    for result in results:
        print(result)
# Output
# >> <Hit {'title': 'Document 1'}>
# Please Like and Subscribe