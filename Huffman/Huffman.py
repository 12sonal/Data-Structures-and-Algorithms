#!/usr/bin/env python
# coding: utf-8

# ## Huffman Encoding and Decoding Algorithm
# ## Copyright: Jagadeesh Vasudevamurthy
# ## filename:Huffman.ipynb

# # All import here

# In[16]:


import sys # For getting Python Version
import random 
import math
import heapq


# # Node Class

# In[17]:


class Node():
    def __init__(self, freq, data, l = None, r = None):
        # Nothing can be added in class Node
        # Must use Node class.Hacker rank fails without this Node
        self.freq= freq #Note public
        self.data=data #Note public
        self.left = l #Note public
        self.right = r #Note public
    ## YOU CAN ADD ANY NUMBER OF PRIVATE FUNCTIONS ONLY
        self.code = ""
        
    def __repr__(self):
        return f"{self.data} {self.freq}"


# # Huffman  Class

# In[18]:


class Huffman():
    def __init__(self,show = False,f = None):
        ##Change this to the place where you write dot file
        self.base = "D:\\Output\\" 
        #Nothing can be changed or added below
        self._s = None
        self._show = show
        if (f):
            self._f = self.base + f
        self._f == None ;
        self._id = []
        ##YOU CAN ADD YOUR PRIVATE VARIABLE HERE
        self.encoder = {}
        self.decoder = {}
        self.temp = {}
        self.code_set = set()
        #self.root = None
        
    #############################################
    #  All public functions below
    #  NOTHING CAN BE CHANGED BELOW
    #############################################
    def encode(self, s:'str')->'str':
        self._s = s
        return self._encode()

    def decode(self,e:'str')->'str':
        return self._decode(e)


    #############################################
    #  WRITE YOUR CODE BELOW
    #  All private functions below
    #############################################
    def _encode(self)->'str':
        counter = self.frequencycheck()
        character = counter.keys()
        
        print("------ Step 1: Character Occurrence ------")
        for char in character:
            print(char, "occurs", counter.get(char), "times")
            
        nodes = []
        for char in character:
            nodes.append(Node(counter.get(char), char))
        nodes = sorted(nodes, key=lambda x: x.freq)
        print("\n------ Step 2: Tree Leaves build in this order ------")
        i = 1
        for j in nodes:
            print("Leaf node", i, j)
            i += 1
        
        print("\n------ Step 3: Internal Nodes of the Tree is build in this order ------")
        if len(nodes) > 1:
            while len(nodes) > 1:
                left = nodes[0]
                right = nodes[1]
                left.code = 0
                right.code = 1
                new_node = Node(left.freq + right.freq, left.data + right.data, left, right)
                nodes.remove(left)
                nodes.remove(right)
                nodes.append(new_node)
                nodes = sorted(nodes, key=lambda x: x.freq)
                print(f"Internal Node {i}: {new_node.data} {new_node.freq}")
                i += 1
        else:
            root = nodes[0]
            root.code = 0
            new_node = Node(root.freq, root.data, None, None)
            nodes.append(new_node)
            print(f"Internal Node {i}: {new_node.data} {new_node.freq}")
            i += 1
        print(f"Tree has {i-1} nodes")

        self.treeleveltraverse(nodes[0])
        encoded_str = ""
        for char in self._s:
            encoded_str += self.encoder[char]
            
        dotFile = self._f
        with open(dotFile, "w") as f:
                f.write("Digraph {\n")
                self._writeDot(nodes[0], f)
                f.write("}\n")
        print(f"\n------Step 4: Writing Dot file at Location------: {dotFile}")
        
        internal_nodes = [node for node in nodes if node.left or node.right]
        for i, node in enumerate(internal_nodes):
            pass
        print("\n------ Step 5: Code for each character is as follows -------")
        for char in character:
            print(f"{char} code is {self.encoder[char]}")
        print("\n------Step 6: Encoding-------")
        print("Encoded string:", encoded_str)
        return encoded_str   
              
    def frequencycheck(self):
        temp = {}
        for element in self._s:
            if element not in temp:
                temp[element] = 0
            temp[element] += 1
        
        return temp   
    
    def treeleveltraverse(self, node, val='', is_leaf=False, count=0):
        newVal = val + str(node.code)

        if node.left:
            count = self.treeleveltraverse(node.left, newVal, is_leaf=False, count=count)
        if node.right:
            count = self.treeleveltraverse(node.right, newVal, is_leaf=False, count=count)
        count += 1
        if not node.left and not node.right:
            self.encoder[node.data] = newVal
            self.decoder[newVal] = node.data
            self.code_set.add(newVal)
            is_leaf = True   
        if is_leaf:
            return count - 1
        else:
            return count
        
    def _writeDot(self, node, f):
        if node is None:
            return

        f.write('label="{}"\n'.format(self._s))

        if node.left:
            left_data = node.left.data
            left_freq = node.left.freq
            f.write('  "{}\\n{}" -> "{}\\n{}" [color=red];\n'.format(node.data, node.freq, left_data, left_freq))
            self._writeDot(node.left, f)

        if node.right:
            right_data = node.right.data
            right_freq = node.right.freq
            f.write('  "{}\\n{}" -> "{}\\n{}" [color=blue];\n'.format(node.data, node.freq, right_data, right_freq))
            self._writeDot(node.right, f)

    def _decode(self, e:'str')->'str':
        current_string = ""
        result = ""
        for i in e:
            current_string += i
            if current_string in self.code_set:
                result += self.decoder[current_string]
                current_string = "" 
        print("Decoded string:", result) 
        return result
    

          
############################################# 
##LEETCODE  
## https://leetcode.com/problems/encode-and-decode-tinyurl/
## Step1: Delete all code and comment in Leetcpde
## Step2: Cut and paste this file in Leetcode
## Step3: Make False to True
## All tests must pass in one shot.
## Post screen shot of Leetcode passed as pdf
#############################################
if (False):
    Codec = Huffman


# # Util class
# # Nothing can be changed
# # No need to write any code here

# In[19]:


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
 


# # Huffman test class
# # NOTHING CAN BE CHANGED BELOW

# In[20]:


############################################################
# HuffmanTest.py
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
##from Huffman import *
##from Util import *
##

class HuffmanTest():
    def __init__(self):
        #Nothing can be added here
        self.base = "C:\\scratch\\outputs\\huffmanpy\\"
        self.num = 1
        self._test_basic()
 
    ###########################################
    #           test1
    ############################################
    def _test1(self,s:'string',show:'bool',f:'string'):
        print("---- Problem",self.num,"s = ",s, "------  STARTS");
        h = Huffman(show,f)
        e = h.encode(s)
        d = h.decode(e)
        print("Original string:", s)
        print("Your     string:", d)
        if (s != d):
            assert(False)
        sl = len(s) * 8
        el = len(e)
        r = ((el - sl)/sl) * 100 ;
        print("% reduction =",r)

    ###########################################
    #           basic tests
    ############################################
    def _test_basic(self):
        show = True
        print("----------- Basic test Start --------------")
        self._test1("a",show,"1.dot");
        self._test1("aba",show,"2.dot");
        self._test1("aaabbggggghhhhaaaggggaaaaa_+@#",show,"3.dot");
        self._test1("A quick brown fox jumps over the lazy dog",show,"4.dot");
        self._test1("Pack my box with five dozen liquor jugs",show,"5.dot");
        self._test1("Long years ago we made a tryst with destiny, and now the time comes when we shall redeem our pledge, not wholly or in full measure, but very substantially.At the stroke of the midnight hour, when the world sleeps, India will awake to life and freedom. A moment comes, which comes but rarely in history, when we step out from the old to the new, when an age ends, and when the soul of a nation, long suppressed, finds utterance.",show,"6.dot");
        self._test1("Baa, baa, black sheep, have you any wool?",show,"7.dot");
        print("-----------Basic test Passed -------------------")


############################################################
# main 
# YOU CANNOT CHANGE ANYTHING BELOW
###########################################################
def main():
  print("Testing Huffman Starts")
  t = HuffmanTest()
  print("If you like my class, can uou please recommend on https://www.linkedin.com/in/jagadeesh-vasudevamurthy-6796591/")
  print("Testing Huffman Ends")

############################################################
# Real Main
###########################################################
if (__name__  == '__main__'):
  main()
  

