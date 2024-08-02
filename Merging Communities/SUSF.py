#!/usr/bin/env python
# coding: utf-8

# ## Smart Union Smart Find
# ## Copyright: Jagadeesh Vasudevamurthy
# ## filename:SUSF.ipynb

# # All import here

# In[51]:


import sys # For getting Python Version
import random 
import math


# # SUSF class

# In[52]:


############################################################
# SUSF.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2022
###########################################################

############################################################
# All imports
# Comment all these imports in jupyter note book

#from Util import *
###########################################################
class SUSF():
    def __init__(self,n:'int'):
        #Nothing can be changed here
        self._n = n
        self._id = []
        self._numUnion = 0 
        self._numFind = 0 
        self._maxHeight = 0
        #he true identity of parent is in a node that has negative weight
        for i in range(n):
            self._id.append(-1)

    #############################################
    #  All public functions below
    #############################################
    def P(self):
        #NOTHING CAN BE CHANGED
        if (self._n < 20):
            u = Util()
            u.print_index(self._n)
            u.print_list(self._id)
        print("U = ",self._numUnion,"F = ",self._numFind, "H = ",self._maxHeight) ;

    def H(self):
        #NOTHING CAN BE CHANGED
        return self._maxHeight

    #############################################
    # NOTHING CAN BE CHANGED BELOW
    # At the end find the max height
    # Find the owner of each pbject
    # The max HOP will be reorded in self._maxHeight
    #############################################
    def max_height(self)->int:
        for i in range(self._n):
            self.F1(i)
        return self.H()

    #############################################
    #  Number of element in group a
    #############################################
    def num(self,a:'int')->'int':
        #print("WRITE CODE. HOW many elements a has")
        val = self.F1(a)
        if val <= 0:
            raise ValueError("Invalid index")
        count = self._id[val]
        return -count

         
    #############################################
    #  Smart Find
    #  Who is the parent of a
    #############################################
    def F1(self,a:'int')->'int':  
        #print("WRITE CODE. Who is the parent of a")
        #print("Mange number of hops and update self._maxHeight ONLY in this routine")
        temp = [0]
        check = self._hops(a, temp)
        if (temp[0] > self._maxHeight):
            self._maxHeight = temp[0]
        return check
        

    #############################################
    #  Smart Find
    #  is a conneccted to b
    #  Almost constant
    #############################################
    def F2(self,a:'int',b:'int')->'bool':
        #print("WRITE CODE. Is a connected to b. Hint: Use F1")
        root_a = self.F1(a)
        root_b = self.F1(b)
        if root_a < 0 or root_b < 0:
            return False
        return root_a == root_b

    #############################################
    # Smart Union
    # Make union of a and b  if not connected
    # union by size
    # Almost constant
    #############################################
    def U(self,a:'int',b:'int')->'bool':
        x = self.F2(a,b)
        y = self.F2(b,a)
        assert(x == y)
        if (x == False):
            root_b = self.F1(b)
            if (self._id[root_b] < 0):
                root_a= self.F1(a) 
                if (self._id[root_a] < 0 or root_b != root_a):
                    self._numUnion += 1
                    if self._id[root_b] < self._id[root_a]:
                        self._id[root_b] += self._id[root_a]
                        self._id[root_a] = root_b
                    else:
                        self._id[root_a] += self._id[root_b]
                        self._id[root_b] = root_a
                    return True
                else:
                    return False
      

    #############################################
    #  All private functions below
    #############################################
    def _hops(self, a, temp):
        if (self._id[a] < 0):
            return a
        self._numFind +=1
        temp[0]+=1
        self._id[a]= self._hops(self._id[a], temp)
        return self._id[a]
    
    


# ## https://www.hackerrank.com/challenges/merging-communities/problem?isFullScreen=true
# ## UNCOMMENT THE CODE and paste in Hacker Rank
# ## YOU MUST USE ONLY THIS CODE FOR FULL GRADE

# In[53]:


# [N,Q]=[int(x) for x in input().split()]
# ds = [[i,1] for i in range(0,N+1)]
# s = SUSF(N)
# for q in range(Q):
#     inp = input().split()
#     if inp[0] == 'M':
#         a = int(inp[1])
#         b = int(inp[2])
#         s.U(a,b)
#     else:
#         a = int(inp[1])
#         print(s.num(a))


# # Util class
# # Nothing can be changed
# # No need to write any code here

# In[54]:


############################################################
# Util.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################

############################################################
# NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
import sys # For getting Python Version
import random 
import math
from time import process_time 

class Util():
  pass

  ############################################
  # generate_random_number start to end INCLUDED 
  # start to end INCLUDED
  #########################################
  def generate_a_random_number(self,start:int,end:int)->'int':
    v = random.randrange(start,end+1);
    return v

  ############################################
  # generate_random_number GENERATES  N random numbers betweem 
  # start to end INCLUDED
  # if onlypositive is False, generates both pos and negative number
  #  randrange(beg, end, step) :- 
  #  beginning number (included in generation), 
  #  last number (excluded in generation) a
  #  nd step ( to skip numbers in range while selecting).
  #########################################
  def generate_random_number(self, N:int, onlypositive:bool, start:int, end:int)->'List of integer':
    a = []
    for i in range(N):
      v = self.generate_a_random_number(start,end);
      if (onlypositive == False):
        if ((i % 2) == 0): ##//Even. Half are positive, Half are negative
          v = -v ;
      a.append(v)
    return a

  ############################################
  # swap
  #########################################
  def swap(self,a:'List of integer', i:'int', j:'int'):
    t = a[i]
    a[i] = a[j]
    a[j] = t

  ############################################
  # generate shuffled number between 0 to n
  # n-1 not encluded
  #########################################
  def generate_suffled_number_between_1_to_n(self, n:int)->'List of integer':
    a = []
    for i in range(n):
      a.append(i)

    for i in range(n):
      j = self.generate_a_random_number(0,n-1);
      k = self.generate_a_random_number(0,n-1);
      self.swap(a,j,k)
    return a

  ############################################
  # generate shuffled number between 0 to n
  # n-1 not encluded
  #########################################
  def generate_duplicated_number_between_1_to_n(self, n:int)->'List of integer':
    a = []
    for i in range(n):
      a.append(i)

    for i in range(n):
      j = self.generate_a_random_number(0,n-1);
      k = self.generate_a_random_number(0,n-1);
      a[k] = a[j]
    return a

  ############################################
  # generate n numbers in ascending order from 0 to n-1
  #########################################
  def generate_n_numbers_in_ascending_order(self, n:int)->'List of integer':
    a = []
    for i in range(n):
      a.append(i)
    return a

  ############################################
  # generate n numbers in descending order from n-1 to 0
  #########################################
  def generate_n_numbers_in_descending_order(self, n:int)->'List of integer':
    a = []
    for i in range(n-1,-1,-1):
      a.append(i)
    return a

  ############################################
  # generate n same k number
  #########################################
  def generate_n_same_k_number(self, n:int,k:'int')->'List of integer':
    a = []
    for i in range(n):
      a.append(k)
    return a

  ############################################
  # print_index(10)
  #    0   1   2   3   4   5   6   7   8   9
  #########################################
  def print_index(self, n:int):
    for i in range(n):
      print("{:4d}".format(i),end="")
    print()

  ############################################
  # a = [7,8,9, 23, 100]
  # print_list(a)
  # 7   8   9  23 100
  #########################################
  def print_list(self, a:'list'):
    for i in range(len(a)):
      print("{:4d}".format(a[i]),end="")
    print()

  ############################################
  # a = [7,8,9, 1, 100]
  # crash
  #########################################
  def assert_ascending_range(self, a:'list',start:int, includingend:int):
    t = a[start]
    for i in range(start+1,includingend):
      if (a[i] < t):
        assert(False)
      t = a[i]

  ############################################
  # a = [7,8,9, 1, 100]
  # crash
  #########################################
  def assert_ascending(self, a:'list'):
    if (len(a)):
      self.assert_ascending_range(a,0,len(a)) 

  ############################################
  # a = [1,2,3, 3, 4]
  # return True
  #########################################
  def is_ascending_order_has_duplicates(self,a:'list')->'bool':
    if (len(a)):
        t = a[0]
        for i in range(1,len(a)):
          if (a[i] <= t):
            return True
          t = a[i]
    return False

  ############################################
  # log to the next possible integer
  #########################################
  def log_upper_bound(self, n:'int', b:'int')->'int':
    f = math.log(n,b)
    c = math.ceil(f)
    return c 

  ############################################
  # log to the smallest possible integer
  #########################################
  def log_lower_bound(self, n:'int', b:'int')->'int':
    f = math.log(n,b)
    c = math.floor(f)
    return c 

  ############################################
  # sqrt to the next possible integer
  #########################################
  def sqrt_upper_bound(self, n:'int')->'int':
    f = math.sqrt(n)
    c = math.ceil(f)
    return c 

  ############################################
  # sqrt to the smallest possible integer
  #########################################
  def sqrt_lower_bound(self, n:'int')->'int':
    f = math.sqrt(n)
    c = math.floor(f)
    return c 
 


# # SUSF test class
# # NOTHING CAN BE CHANGED BELOW

# In[55]:


############################################################
# SUSFTest.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2022
###########################################################

############################################################
#           NOTHING CAN BE CHANGED BELOW
###########################################################

############################################################
# All imports
# Comment all these imports in jupyter note book
###########################################################
##
##from SUSF import *
##from Util import *
##

class SUSFTest():
    def __init__(self):
        #Nothing can be added here
        self._test_basic()
        self._hacker_1()
        self._test1(1000)
        self._test2(1000)
        self._testRandom(100000)

    ###########################################
    #           basic tests
    ############################################
    def _test_basic(self):
        print("----------- Basic test Start --------------")
        N = 10
        s = SUSF(N)
        e1 = [ [4,3], [3,8],[6,5],[9,4],[2,1] ]
        e2 = [ [5,0], [7,2],[6,1],[7,3] ]
        
        for e in e1:
           s.P()
           s.U(e[0],e[1])
        assert(s.F2(8,9))
        assert(s.F2(5,4) == False)

        for e in e2:
           s.U(e[0],e[1])
        s.P()
        h = s.H()
        if (h != 2):
            print("Height for this must be 2. But your height is",h)
            assert(False)
        print("-----------Basic test Passed -------------------")

    ###########################################
    #           test 1
    ############################################
    def _test1(self,n:'int'):
        print("----------- Test1 Start ------------")
        s = SUSF(n+1)
        for i in range(n):
            s.U(i,i+1)
        s.P()
        h = s.max_height()
        s.P()
        if (h != 1):
            print("Height for this must be 1. But your height is",h)
            assert(False)
        print("----------- Test1 Passed ------------")

    ###########################################
    #           test hacker
    ############################################
    def _hacker_1(self):
        print("-----------  hacker_1 Start -------------")
        n = 17
        s = SUSF(n)
        for i in range(1,16,2):
            s.U(i,i+1)
        for i in range(1,14,4):
            s.U(i,i+2)
        s.U(1,5)
        s.U(11,13)
        s.U(1,10)
        s.P()
        print("num(2)",s.num(2)) ##CHANGE TO 2
        print("num(9)",s.num(9))
        s.P()
        h = s.max_height()
        s.P()
        if (h != 2):
            print("Height for this must be 2. But your height is",h)
            assert(False)
        print("-----------  hacker_1 passed -------------")

    ###########################################
    #           test 2
    ############################################
    def _test2(self,n:'int'):
        print("-------- Test2 Start  -------------")
        s = SUSF(n)
        s.U(0,1)
        for i in range(2, n):
            s.U(i,0)
        s.P()
        h = s.max_height()
        s.P()
        if (h != 1):
            print("Height for this must be 1. But your height is",h)
            assert(False)
        print("-------- Test2 Passed  -------------")

    ###########################################
    #           test Random
    ############################################
    def _testRandom(self,n:'int'):
        print("------ Test Random Start -----------")
        u = Util()
        k = n * 10
        print("Union on",n,"Random data performed",k,"times")
        s = SUSF(n+1)
        for i in range(k):
            v1 = u.generate_a_random_number(0,n)
            v2 = u.generate_a_random_number(0,n)
            if (v1 != v2):
                s.U(v1,v2)

        s.P()
        h = s.max_height()
        s.P()
        if (h > 6):
            print("Height for this must be <= 6. But your height is",h)
            assert(False)
        print("------ Test Random Passed -----------")

############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
  print("Testing SFSU Starts")
  t = SUSFTest()
  print("Testing SFSU Ends")

############################################################
# Real Main
###########################################################
if (__name__  == '__main__'):
  main()
  

