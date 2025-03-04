#!/usr/bin/env python
# coding: utf-8

# In[11]:


words=[ 'This','is','a','sentence' ]
text=''.join(words)
print(text)


# In[16]:


Name="alice"
Age=30
Subject="nlp"
text="Name:{},Age:{},subject:{}".format(age,name,subject)
print(text)


# In[19]:


text="hello,World"
upper=text.upper()
lower=text.lower()
print(upper)
print(lower)


# In[22]:


pip install nltk


# In[25]:


import nltk

nltk.download('punkt')


# In[27]:


from nltk.tokenize import word_tokenize
text="tokenize is an important step in NLTK"


# In[28]:


tokens=word_tokenize(text)
print(tokens)


# In[34]:


import re
text="remove #special characters from the text!"
filtered_text=re.sub(r'[^a-zA-Z\s]','',text)
print(filtered_text)


# In[49]:


import re
text="remove #special characters from the text!"
filtered_text=re.sub(r'[*a-zA-Z\s]','',text)
print(filtered_text)


# In[47]:


import re
text="remove #special characters from the text!"
filtered_text=re.sub(r'[a-zA-Z\s]','1',text)
print(filtered_text)


# In[50]:


import re
text="please calll ma at 0304-123-4564"
filtered_text=re.findall(r'\d{3}-\d{3}-\d{4}',text)
print(filtered_text)


# In[55]:


import re
text="please calll ma at 92-051-920125"
filtered_text=re.findall(r'\d{2}-\d{3}-\d{6}',text)
print(filtered_text)


# In[54]:


import re
text = "please call me at +92-051-920125"
filtered_text = re.findall(r'\+\d{2}-\d{3}-\d{6}', text)
print(filtered_text)


# In[56]:


import re
text="please calll ma at +92-033-4217291"
filtered_text=re.findall(r'\+\d{2}-\d{3}-\d{7}',text)
print(filtered_text)


# In[59]:


from nltk.tokenize import word_tokenize

def is_english(text):
    try:
        words = word_tokenize(text)
        return all(word.isascii() for word in words)
    except UnicodeDecodeError:
        return False

text = "this is english"
print(is_english(text))

text = "这是英语"
print(is_english(text))


# In[ ]:




