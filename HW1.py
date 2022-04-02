#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.10


# In[2]:


d, u, v = xgcd (291, 252);


# In[3]:


print (d, u, v); # So, 291*13 - 252*15 = gcd (291, 252) = 3.


# In[4]:


d, u, v = xgcd (16261, 85652);


# In[5]:


print (d, u, v); # So, - 16261*79 + 85652*15 = gcd (16261, 85652) = 161.


# In[6]:


d, u, v = xgcd (139024789, 93278890);


# In[7]:


print (d, u, v); # So, 139024789*6944509 - 93278890*10350240 = gcd (139024789, 93278890) = 1.


# In[8]:


d, u, v = xgcd (16534528044, 8332745927);


# In[9]:


print (d, u, v); # So, 16534528044*81440996 - 8332745927*161602003 = gcd (16534528044, 8332745927) = 43.


# In[10]:


# 1.12


# In[11]:


def newxgcd1 (a,b):
    u = 1;
    g = a;
    x = 0;
    y = b;
    
    while y != 0:
        q = g // y;
        t = g % y;
        s = u - q * x;
        u = x;
        g = y;
        x = s;
        y = t;
    
    if y == 0:
        v = (g - a * u) / b;
        return (g,u,v);


# In[12]:


g, u, v = newxgcd1 (527, 1258);


# In[13]:


print (g, u, v);


# In[14]:


g, u, v = newxgcd1 (228, 1056);


# In[15]:


print (g, u, v);


# In[16]:


g, u, v = newxgcd1 (163961, 167181);


# In[17]:


print (g, u, v);


# In[18]:


g, u, v = newxgcd1 (3892394, 239847);


# In[19]:


print (g, u, v);


# In[20]:


def newxgcd2 (a,b):
    u = 1;
    g = a;
    x = 0;
    y = b;
    
    if b == 0:
        v = 0;
        return (g,u,v);
    
    while y != 0:
        q = g // y;
        t = g % y;
        s = u - q * x;
        u = x;
        g = y;
        x = s;
        y = t;
    
    if y == 0:
        v = (g - a * u) / b;
        return (g,u,v);


# In[21]:


def newxgcd3 (a,b):
    u = 1;
    g = a;
    x = 0;
    y = b;
    
    if b == 0:
        v = 0;
        return (g,u,v);
    
    while y != 0:
        q = g // y;
        t = g % y;
        s = u - q * x;
        u = x;
        g = y;
        x = s;
        y = t;
    
    if y == 0:
        v = (g - a * u) / b;
        
        u0 = u;
        v0 = v;
        k = 1;
        while u < 0:
            u = u0 + k * b / g;
            v = v0 - k * a / g;
            k = k + 1;
        return (g,u,v);


# In[22]:


# 1.26


# In[23]:


def squaremultiply (N, g, A):
    a = g;
    b = 1;
    while A > 0:
        if A % 2 == 1:
            b = (b * a) % N;
        a = (a * a) % N;
        A = A // 2;
    return b;


# In[24]:


result = squaremultiply (256, 17, 183);


# In[25]:


print (result);


# In[26]:


result = squaremultiply (1000, 2, 477);


# In[27]:


print (result);


# In[28]:


result = squaremultiply (1237, 11, 507);


# In[29]:


print (result);


# In[30]:


# 1.34


# In[31]:


def isPrimitiveRoot (a, p):
    r = primitive_root(p);
    
    i = 1;
    candidates = []
    while i < p - 1:
        if gcd (i, p-1) == 1:
            candidates.append(i);      
        i += 1;
        
    roots = [];
    for k in candidates:
        roots.append (r ** k % p);
    
    for r in roots:
        if r == a:
            return True;
    
    return False;


# In[32]:


a = isPrimitiveRoot (2, 13);
print (a);


# In[33]:


a = isPrimitiveRoot (2, 19);
print (a);


# In[34]:


a = isPrimitiveRoot (2, 23);
print (a);


# In[35]:


a = isPrimitiveRoot (3, 7);
print (a);


# In[36]:


a = isPrimitiveRoot (3, 11);
print (a);


# In[37]:


a = isPrimitiveRoot (3, 17);
print (a);


# In[38]:


root = primitive_root (23);
print (root);


# In[39]:


root = primitive_root (29);
print (root);


# In[40]:


root = primitive_root (41);
print (root);


# In[41]:


root = primitive_root (43);
print (root);


# In[42]:


def allPrimitiveRoots (p):
    r = primitive_root(p);
    
    i = 1;
    candidates = []
    while i < p - 1:
        if gcd (i, p-1) == 1:
            candidates.append(i);      
        i += 1;
        
    roots = [];
    for k in candidates:
        roots.append (r ** k % p);
    
    return roots;


# In[43]:


roots = allPrimitiveRoots (11);
print (roots); # φ(10) = 4


# In[44]:


roots = allPrimitiveRoots (229);
print (roots); # φ(228) = 72


# In[ ]:




