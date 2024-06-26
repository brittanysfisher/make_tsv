#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import os
import hashlib
import base64


# In[2]:


# Define constants - prefix and book directory
PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/'
BK_DIR = 'C:/Users/britt/OneDrive/Desktop/Cloud Computing/books/' 


# In[3]:


# Make md5 checksum function
def md5_checksum(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            md5_hash.update(chunk)
    return md5_hash.digest()


# In[4]:


# Define output file location/name
output_file = "C:/Users/britt/OneDrive/Desktop/Cloud Computing/books.tsv"


# In[5]:


#Write file
with open(output_file, mode='w') as tsv_file: 
    tsv_file.write("TsvHttpData-1.0\n") 
    for filename in os.listdir(BK_DIR): 
        if os.path.isfile(os.path.join(BK_DIR, filename)):  
            file_path = os.path.join(BK_DIR, filename) 
            file_size = os.path.getsize(file_path) 
            file_md5 = base64.b64encode(md5_checksum(file_path)) 
            file_url = f"{PREFIX}{filename}" 
            tsv_file.write(f"{file_url}\t{file_size}\t{file_md5}\n") 


# In[ ]:




