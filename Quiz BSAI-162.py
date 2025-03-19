#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


import re
nltk.download('punkt')


# # 1. Tokenize the paragraph into words and remove punctuation marks.

# In[3]:


from nltk.tokenize import word_tokenize
text = """Natural Language Processing (NLP) is a fascinating field of artificial intelligence that focuses on
the interaction between humans and computers using natural language. It involves various
techniques such as tokenization, stemming, lemmatization, and semantic analysis to process and
analyze textual data. For example, removing stopwords like 'the' and 'is' can help reduce noise in
the text, while tasks like named entity recognition (NER) identify important entities such as
'Google' or 'New York.' Dependency parsing further reveals the grammatical structure of sentences,
enabling deeper insights into relationships between words. NLP techniques are widely applied in
applications like chatbots, sentiment analysis, and machine translation. For instance, a chatbot
might process 1,000 user queries per day, while sentiment analysis can classify text into categories
like positive (e.g., +1), neutral (0), or negative (-1). Additionally, machine translation systems can
translate up to 10 million words daily across multiple languages."""
token = word_tokenize(text)
print(token)
print("cleaned data   :")
cleaned=re.sub(r'[^\w\s]', '', text)
print(cleaned)


# # 2. Write a function to filter out numbers and special characters.

# In[4]:


import re

def filter(text):
    filtered_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return filtered_text
text = """Natural Language Processing (NLP) is a fascinating field of artificial intelligence that focuses on
the interaction between humans and computers using natural language. It involves various
techniques such as tokenization, stemming, lemmatization, and semantic analysis to process and
analyze textual data. For example, removing stopwords like 'the' and 'is' can help reduce noise in
the text, while tasks like named entity recognition (NER) identify important entities such as
'Google' or 'New York.' Dependency parsing further reveals the grammatical structure of sentences,
enabling deeper insights into relationships between words. NLP techniques are widely applied in
applications like chatbots, sentiment analysis, and machine translation. For instance, a chatbot
might process 1,000 user queries per day, while sentiment analysis can classify text into categories
like positive (e.g., +1), neutral (0), or negative (-1). Additionally, machine translation systems can
translate up to 10 million words daily across multiple languages."""
cleaned = filter(text)
print(cleaned)


# In[14]:


pip install profanity


# # 3. Validate if the given text contains profanity using profanity-check.
# 

# In[16]:


from profanity import profanity

text = """Natural Language Processing (NLP) is a fascinating field of artificial intelligence that focuses on
the interaction between humans and computers using natural language. It involves various
techniques such as tokenization, stemming, lemmatization, and semantic analysis to process and
analyze textual data. For example, removing stopwords like 'the' and 'is' can help reduce noise in
the text, while tasks like named entity recognition (NER) identify important entities such as
'Google' or 'New York.' Dependency parsing further reveals the grammatical structure of sentences,
enabling deeper insights into relationships between words. NLP techniques are widely applied in
applications like chatbots, sentiment analysis, and machine translation. For instance, a chatbot
might process 1,000 user queries per day, while sentiment analysis can classify text into categories
like positive (e.g., +1), neutral (0), or negative (-1). Additionally, machine translation systems can
translate up to 10 million words daily across multiple languages."""
if profanity.contains_profanity(text):
    print("The text contains profanity.")
else:
    print("The text does not contain profanity.")


# # 4. Perform stemming on a given text using the Porter Stemmer algorithm.

# In[18]:


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
text = """Natural Language Processing (NLP) is a fascinating field of artificial intelligence that focuses on
the interaction between humans and computers using natural language. It involves various
techniques such as tokenization, stemming, lemmatization, and semantic analysis to process and
analyze textual data. For example, removing stopwords like 'the' and 'is' can help reduce noise in
the text, while tasks like named entity recognition (NER) identify important entities such as
'Google' or 'New York.' Dependency parsing further reveals the grammatical structure of sentences,
enabling deeper insights into relationships between words. NLP techniques are widely applied in
applications like chatbots, sentiment analysis, and machine translation. For instance, a chatbot
might process 1,000 user queries per day, while sentiment analysis can classify text into categories
like positive (e.g., +1), neutral (0), or negative (-1). Additionally, machine translation systems can
translate up to 10 million words daily across multiple languages."""
words = nltk.word_tokenize(text)
stemmed = [stemmer.stem(word) for word in words]
print("origional sentence:", words)
print("------------------------------------------------------------------------------------------------------------------")
print("stemmed sentence:", stemmed)


# In[ ]:




