#!/usr/bin/env python
# coding: utf-8
r=int(input("enter the radius"))
area=3.14*(r**2)
print("the area of circle is",area)
# In[26]:


a=int(input("enter FIRST numbers"))
b=int(input("enter SECOND numbers"))
c=int(input("enter three numbers"))
if (a>b and a>c):
    print(f"{a} is the largest number")
elif (b>a and b>c):
    print(f"{b} is the largest number")
else:
    print(f"{c} is largest number")


# In[40]:


n=int(input("enter a number"))
p=n+(n*10+n)+(n*100+n*10+n)
print("the product is",p)


# In[48]:


import math
a=int(input("enter the first number"))
b=int(input("enter the second number"))    
gcd=math.gcd(a,b)
print(gcd)


# In[24]:


n = input("Enter a number n: ")
a=n
b=n*2
c=n*3
result = int(n) + int(n * 2) + int(n * 3)

print(f"The result of {a} + {b} + {c} is:", result)


# In[23]:


n=int(input("enter a number"))
p=str(n)+str(n*2)+str(n*3)
print("the product is",p)


# In[53]:


type("true")


# In[55]:


type(True)


# In[2]:


num=int(input("enter a number"))
result=num*2
print(result)


# In[13]:


p=10
q=20
p+=q
print(p)


# In[9]:


p=10
q=20
q-=p
print(q)


# In[11]:


p=10
q=20
p*=q
print(p)


# In[12]:


p=10
q=20
q+=p+q**2
print(q)


# In[14]:


l=[10,20,30,40,50]
print(l)
print(l[0])
print(l[0:3])
print(l[::-1])


# In[20]:


l=[]
n=int(input("enter the number of elements to be inserted"))
for i in range (n):
    ele=int(input("enter the elements"))
    l.append(ele)
print(l)


# In[22]:


l=[]
n=int(input("enter the number of days"))
for i in range (n):
    ele=input("enter the days")
    l.append(ele)
print(l[4])


# In[10]:


l=[]
n=int(input("enter the list of integers"))
for i in range (n):
    ele=int(input("enter the numbers"))
    if(ele%2!=0):
        l.append(ele)
if(len(l)>0):
    print("odd numbers",l)
else:
    print("no odd numbers")

    


# In[17]:


l=[]
n=int(input("enter the list of integers"))
for i in range (n):
    ele=int(input("enter the numbers"))
    l.append(ele)
print(l)
l1=[]
for ele in l:
    if(ele%2!=0):
        l1.append(ele)
if(len(l1)>0):
    print("odd numbers",l1)
else:
    print("no odd numbers")


# In[20]:


l=[]
n=int(input("enter the no of numbers to be inserted"))
for i in range (n):
    ele=int(input("enter the numbers"))
    if(ele>100):
        l.append("over")
    else:
        l.append(ele)
print(l)


# In[5]:


l1=[10,20,30,40]
l2=[1,2,3,4]
if(sum(l1)==sum(l2)):
    print(f"their sum of numbers is same{sum(l1),sum(l2)}")
else:
    print(f"their sums are not same{sum(l1),sum(l2)}")


# In[21]:


l1=[10,2,30,40]
l2=[1,73,4]
found=0
for i in l1:
    for j in l2:
        if(i==j):
            found=1
            break
    if(found==1):
        break
if(found==1):
    print("same number occured")
else:
    print("no number occured")
    


# In[1]:


def hello():
    print("hello world")
hello()


# In[3]:


n=int(input("enter a number:"))
nn=n*11
nnn=n*111
result=n+nn+nnn
print(f"{n}+{nn}+{nnn}=",result)


# In[8]:


def hello():
    name="Naveen"
    print(f"hello {name}")
hello()


# In[15]:


a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
def sum_pro():
    result=a+b+c
    print("sum of three numbers=",result)
    res_pro=a*b*c
    print("product of three numbers=",res_pro)
sum_pro()




# In[1]:


cur_year=int(input("enter the current year"))
last_year=int(input("enter the last year"))
year=[]
def leap_year():
    for i in range(cur_year,last_year+1):
        if(i%4==0 and i%100!=0)or(i%400==0):
            year.append(i)
    if(len(year)==0):
        print("no leap year")
    else:
        print(year)
leap_year()


# In[2]:


l1=[10,20,30,40]
l2=[1,2,3,4]
if set(l1).intersection(l2):
    print("number occured")
else:
    print("no number occured")


# In[19]:


a=[]
b=[]
n=int(input("enter the number of elements needed"))
for i in range(n):
    el=int(input("enter the numbers needed"))
    a.append(el)
for i in range(n):
    if a[i]>0:
        b.append(a[i])
print(b)        
        


# In[18]:


a = []
b = []
n = int(input("Enter the number of elements needed: "))

for i in range(n):
    el = int(input("Enter the number: "))
    a.append(el) # Added 'el' inside append()

for i in range(n): # Added parentheses around n
    if a[i] > 0:
        b.append(a[i]) # Used append() instead of index assignment

print("Positive numbers:", b)


# In[4]:


n=int(input("enter the number of elements needed"))
s=[x**2 for x in range(1,n+1)]
print(s)


# In[1]:


a=[-10,15,0,7,-3,22,-1]
pos=[n for n in a if n>0]
print(pos)


# In[18]:


n=input("enter a word:")
b="aeiouAEIOU"
s=[x for x in n if x in b]
print(s)


# In[9]:


n=input("enter a word")
s=[ord(x) for x in n]
print(s)


# In[19]:


l=["Naveen","Gautham","AAA"]
count_a=sum(x.lower().count('a') for x in l)
print(count_a)


# In[29]:


a=input("enter a word")
b=a[0]
p=a[1:].replace(a[0],'$')
print()


# In[34]:


a=input("enter a word")
n=len(a)
b=a[0]
p=a[1:].replace(a[0],a[n-1])
print(b+p)


# In[ ]:




