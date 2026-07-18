from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("Social_Network_Ads (1).csv") 

docs=loader.load()

print(len(docs))

print(docs[0])
