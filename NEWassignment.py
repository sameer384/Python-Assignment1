#!/usr/bin/env python
# coding: utf-8

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line

# In[2]:


l=[]
for i in range(2000,3200) :
    if(i%7==0):
        l.append(i)
m=[]

for j in l:
    if(i%5==0):
        continue
    m.append(j)
print(m)


# Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name

# In[4]:


f= input("enter first name")
l = input("enter last name")

o = f[::-1]
p = l[::-1]
print(o+" "+p)


# 
#  Write a Python program to find the volume of a sphere with diameter 12 cm.  
#  
# Formula: V=4/3 * π * r 3 
#  

# In[10]:


d=12
r=d/2
pie= 3.14
V=4/3*pie*r*r*r
V


# Write a program which accepts a sequence of comma-separated numbers from console and generate a list. 

# In[1]:


v=input("list")


# In[4]:


list=v.split(",")


# In[5]:


list


# Create the below pattern using nested for loop in Python. 

# In[23]:


n=5
for i in range(n):
    for j in range(i):
        print('* ',end="")
    print('')
    
for i in range(5,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
    


# Write a Python program to reverse a word after accepting the input from the user

# In[2]:


a= input("enter a word ro reverse it")

o= a[::-1]
print(o)


# Write a Python Program to print the given string in the format specified in the ​sample output. 

# In[3]:


print("WE"+","+"THE PEOPLE OF INDIA"+","+"\n"+"\t"+" having solemnly resolved to constitute India into a SOVEREIGN"+","+"!"+"\n"+"\t"+"\t"+"SOCIALIST"+","+
      "SECULAR, DEMOCRATIC REPUBLIC"+"\n"+"\t"+"\t"+" "+"and to secure to all its citizens ")


# In[ ]:




