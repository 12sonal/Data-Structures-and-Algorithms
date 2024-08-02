#!/usr/bin/env python
# coding: utf-8

# # copyright: Jagadeesh Vasudevamurthy
# # Frie:  Friends.ipynb

# # WRITE CODE ONLY IN THIS CELL

# In[10]:


############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2023
###########################################################

############################################################
# All imports
###########################################################
##from Util import *

class Solution:
  def __init__(self,n:'int',a:'list of size 2'):
    self._n = n
    #a[0] = How many friends are there in n. Use _increment_number_of_friends to fill
    #a[1] = num_steps Use _increment_steps
    self._list = a
    ##YOU CAN HAVE ANY NUMBER OF DATA STRUCTURES HERE
    self._u = Util()

    

    ## NOTHING CAN BE CHANGED BELOW
    self._alg()

  def _increment_steps(self)->'none':
    self._list[1] = self._list[1] + 1

  def _increment_number_of_friends(self)->"int":
    self._list[0] = self._list[0] + 1
    return (self._list[0])


  ##Implement your code BELOW
  ##You can have any number of private variables and functions

  def find_factors(self, N):
    factors = [i for i in range(N)]
    prime_numbers = []
    for i in range(2, N):
        if factors[i] == i:
            prime_numbers.append(i)
            for j in range(i*2, N, i):
                factors[j] = i
    return factors

           
  def _alg(self):
    factor_sum = [0] * self._n
    factor_sum[1] = 1
    find_factors = self.find_factors(self._n)
    for i in range(2, self._n):
        self._increment_steps()
        num = i
        factor1 = find_factors[i]
        factor_count = 0
        while num % factor1 == 0:
            self._increment_steps()
            num = num // factor1
            factor_count += 1
        result = i // num
        factor_sum[i] = (result * factor1 - 1) // (factor1 - 1)
        factor_sum[i] *= factor_sum[num]
    pair_counter = 1
    for i in range(2, self._n):
        self._increment_steps()
        j = factor_sum[i] - i
        if j < self._n and j > i and factor_sum[j] - j == i:
            print(f"{pair_counter}. {i} {j}")
            pair_counter += 1
            self._increment_number_of_friends()

       





  

 


# # Some useful function 
# # Can use if required

# In[11]:


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


# # TEST BENCH
# # NOTHING CAN BE CHANGED BELOW

# In[13]:


############################################################
# Friends.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2023
###########################################################

############################################################
#           NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
#from Util import *
#from Solution import *


class Friends():
  def __init__(self):
    self._u = Util()
    self._testBench()

  def _testBench(self):
    self._tests()
    print("ALL TESTS PASSED")

  def _test1(self,n:'int',ans:'int'):
    print("-------------", n , "-------------------------")
    a = [0,0]
    t1_start = process_time()
    s = Solution(n,a) ##All action happens here
    t1_stop = process_time() 
    if (a[1] == 0):
        print("How did you solve the problem in 0 steps")
        print("when ever you loop call _increment_steps() ")
        assert(False)
    if (a[0] == 0):
        print("Number of friends is 0. How?")
        print("when ever you find friend call _increment_number_of_friends ")
        assert(False)
    d = t1_stop - t1_start; 
    print(n, " has ", a[0], " friends. Took", a[1], " steps to compute")
    print("Total CPU time in sec =",d)
    logn_base2 = self._u.log_lower_bound(n,2)
    nlogn = n * logn_base2
    w = a[1] / nlogn 
    print("n = ", n)
    print("logn ", logn_base2)
    print("nlogn ",nlogn)
    print("num_steps/nlogn", w)
    if (a[0] != ans):
      print(n," Has", ans, "Friends. But you are telling",a[0])
      assert(a[0] == ans)


  def _tests(self):
    n = 10000
    a = self._test1(n,5)

    n = 20000
    a = self._test1(n,8)

    n = 100000000 ## YOU CANNOT CHANGE THIS.
    a = self._test1(n,231)


############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
  print("Testing Friends.py Starts")
  s = Friends()
  print("Testing Friends.py ENDS")

############################################################
# Pthin calls this
###########################################################
if (__name__  == '__main__'):
  main()


# In[ ]:





# In[ ]:





# In[ ]:




