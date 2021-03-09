#!/usr/bin/env python
# coding: utf-8

# 
# 
# 1.What are the difference between operators and values in the following?
# 
# *
# 'hello'
# -87.8
# -
# /
# +
# 6
# 
# sol:
# operators are used to perform the operations between the Mathematical expressions,where  *,-,/,+  are the operators that given in the question.
# 
# values are the data that assign to the particular variable it may be string,float,integer
# 'hello' is a string that which can be assigned to variable like
# A='hello'
# 
# -87.8 is float value which can be used as a value in particualr set of code.
# 
# 6 is a integer which can be also a value.
# 
# 
# 
# 
# 

# 2. What is the difference between string and variable?
#  spam
# 'spam'
# 
# variable  is said to be a storage of information where string is type of info or data that store in variable
# A string is enclosed in single quote('') or double quote("") or triple quote(""" """)
# 

# In[25]:



spam='spam'
spam
type(spam)

#where spam is a variable and 'spam' is a string.


# 3. Describe three different data forms.
# sol:
#     Numeric,sequence type and boolean are the three data forms in python
#     
#     ## Numeric data type
#     represents the numeric value as a data.it can be integer,floating number and even complex number.
#     The values are defined as int,float and complex in python
#     
#     integer:Integer may contains positive or negative numbers.In python there is no limit for length of the integer.
#     EX:2,4,-5,-9
#     
#     float:float class is a representation of real numbers with floating point.
#     EX:2.4,-4.6,-0.567
#     
#     complex numbers:complex numbers are the combination of real and imaginary numbers.
#     EX:2+3j,6+7j,-3-8j
#         
#         
#     ## Sequence type:
#     sequence type further divided into three data forms
#         they are string,tuple,list
#     
#     String:A string is a collection of one or more characters which incliuded whithin the single quote,double quote or triple
#         quote.there is no character datatype in python.A character is a string of length one and that is represented by str.
#     EX:"I NEURON","""SUNIL KUMAR""","34AF"
#         
#     Tuple:Python Tuple is used to store the sequence of immutable Python objects. The tuple is similar to lists since the value of 
#          the items stored in the list can be changed, whereas the tuple is immutable,and the value of the items stored in the tuple 
#          cannot be changed.
#     EX:
#         Creating a empty tuple
#         tuple=()
#         tuple1=(3,"numpy","scipy")
#     List:list is a data structure in python that is mutable,changeble,ordered sequence of elements.
#          Each element or value that is inside of a list is called an item.just as strings defined as characters between quotes.
#          list are defined by using []
#     EX:
#         list=[]
#         list1=[2,3,"assignment1"]
#         
#    ## Bollean
#     bollean data type is consits of two built in values True and False.In boolean datatype we can evaluate non-boolean objects 
#     as well which determined as True and False.It is denoted by the class bool.
#      In python True and False must have capital 'T' and 'F' othrrwise it throws an error.
#         
#      EX:type(True)
#         bool(2<4)
# 
#     
# 
#         
# 
# 
#         
# 
# 
#     
#     
#     

# 4. What makes up an expression? What are the functions of all expressions?
# 
# 
# sol:
#     Expressions are representations of value. They are different from statement in the fact that statements do something while 
#     expressions are representation of value. For example any string is also an expressions since it represents the value of the 
#     string as well.
#     Python has some advanced constructs through which you can represent values and hence these constructs are also called 
#     expressions.
#     Anything that does something is a statement.Any assignment to a variable or function call is a statement. 
#     Any value contained in that statement in an expression.
#     
#     Function is a combination of expression that which includes all the values and operators for the mathematical performance.    
# 
# 
# 

# #5. In this chapter, assignment statements such as spam = 10 were added. What difference between a declaration and an expression?
# 
# sol:
#     We have spam = 10,where spam is a variable and 10 is the value that assigned to the variable spam.
#     Here we declared the variable by assigning the value 10.So, it is called declaration.
#     An expression is a combination of declared variables which includes in the performance of operations. 

# In[3]:


spam=10
spam #declaration

#expression
exp=spam+10
exp


# In[8]:


"""
6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1  
"""
bacon=22
bacon +1
#after runnig this particular code we will get 23 as a output,because here we just added one to the bacon variable


# In[9]:


#if we run the bacon variable again we will get 22
bacon


# In[13]:


#7. What should the values of the following two terms be?

'spam' + 'spamspam'
#By running the above code we get addition of the strings i.e as fallows


# In[15]:


'spam' * 3
#since it is a mulptiplication operation so,the string spam is multiplies 3 times 


# #8. Why is it that eggs is a true variable name but 100 is not?
# 
# eggs is variable name which satisfies the rules to create a variable in python
# 
# rules for creating a variable in python
# 1.A variable name must be started with a letter or a underscore
# 2.it should not start with a number
# 3.A variable can only contain alpha-numeric characters and underscores(A-Z,0-9,-) and no special characters are entertained.
# 
# So,As per the rules 100 is digit which should not start with.so it is not a variable.
# 

# In[42]:


#9. Which of the following three functions may be used to convert a value to an integer, a floating-point number, or a string?

#float() will convert a integer to a floating point number and

print("integer to float:", float(3))
#float() will also convert a string which contains a integer into a floating point number.
print("string to float:", float("34"))
#int() will convert a floating point number to an integer
print("float point number to integer:", int(9.6))
#srt() will convert a integer or floating point to a string
a=2
str(a)
b=6.5
str(b)



# In[23]:


#10. What is the error caused by this expression? What would you do about it?

'I have eaten' + 99 + 'burritos'
#it is clear that  we can't able to concatenate both the strings and integers.


# In[43]:


#if we include that 99 in " "(quote),then it converts into string

'I have eaten' + '99' + 'burritos'


# In[ ]:




