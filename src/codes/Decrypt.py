#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
from Crypto.Cipher import AES
from Crypto.Hash import SHA256


# In[43]:


password = "9UoZdcaw@keyE8c="
hash_obj = SHA256.new(password.encode('utf-8'))
hkey = hash_obj.digest()


# In[44]:


def encrypt(info):
    msg = info
    BLOCK_SIZE = 16
    PAD = "{"
    padding = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PAD
    cipher = AES.new(hkey, AES.MODE_ECB)
    result = cipher.encrypt(padding(msg).encode('utf-8'))
    return result 


# In[45]:


msg = "c3VwZXJ1c2VyOnN1cGVyc2VjcmV0"
cipher_text = encrypt(msg)
print(cipher_text)


# In[46]:


file1 = open("out5.txt","wb")
file1.write(cipher_text)
file1.close()
file2 = open("cert.txt","w")
file2.write(password);
file2.close()
with open("out2.txt", "w") as text_file:
    print(cipher_text, file=text_file)


# In[47]:


def decrypt(info):
    #password = "dcaw@key"
    file2 = open("cert.txt","r")
    cert = file2.read()
    hash_obj = SHA256.new(cert.encode('utf-8'))
    BLOCK_SIZE = 16
    hkey = hash_obj.digest()
    msg1 = info
    PAD = "{"
    decipher = AES.new(hkey, AES.MODE_ECB)
    pt = decipher.decrypt((msg1)).decode('utf-8')
    pad_index = pt.find(PAD)
    result = pt[: pad_index]
    return result


# In[48]:


file1 = open("out5.txt","rb")
content1 = file1.read()
print(content1)


# In[49]:


plaintext = decrypt(content1)
print(plaintext)
if msg==plaintext:
    print("Valid")
else:
    print("Invalid")


# In[ 0]:




