#!/usr/bin/env python
# coding: utf-8

# ## singly linked list
# ## Copyright: Jagadeesh Vasudevamurthy
# ## filename:slist.ipynb¶

# # All import here

# In[8]:


import sys # For getting Python Version
import random 
import math


# # ListNode class
# # NOTHING CAN BE CHANGED

# In[9]:


class ListNode:
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next


# # Slist class
# # WRITE CODE ONLY HERE

# In[10]:


############################################################
# Slist.py 
# SList oblect
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################

############################################################
#  All imports here
###########################################################
#from ListNode import *

############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        
    #############################
    # WRITE All public functtions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    def append(self, val):
        node = ListNode(val)
        if self._first is None:
            self._first = node
            return
        current = self._first
        while current.next:
            current = current.next
        current.next = node
        
    def prepend(self, val):
        node = ListNode(val)
        node.next= self._first
        self._first = node
        
    def find(self, element):
        current= self._first
        while current and current.val != element:
            current = current.next
        if current:
            return True
        return False
            
    def delete(self, element):
        current = self._first
        previous = None
        while current and current.val!= element:
            previous = current
            current= current.next
        if current is None:
            return False
        if previous is None:
            self._first = current.next
        else:
            previous.next = current.next
        return True
    
    def delete_front(self):
        if self._first:
            self._first = self._first.next
        
    def delete_last(self):
        if self._first is None:
            return
        if self._first.next is None:
            self._first = None
            return
        current = self._first
        while current.next.next:
            current = current.next
        current.next = None
        
    def build_slist_from_list(self,lst):
        for value in lst:
            self.append(value)
            
            
    def is_empty(self):
        if self._first is None:
            return True
        return False
    
    def reverse(self):
        current = self._first
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self._last = self._first
        self._first = previous
        
    def find_mid_point(self):
        if self.is_empty():
            return 0
        if self._first.next is None:
            return self._first.val
        count = 0
        current = self._first
        while current:
            count+=1
            current = current.next
        mid = ((count-1) //2 )
        return self.getI(mid)
    
    def getI(self, index):
        if index >= len(self):
            return None
        current = self._first
        for j in range(index):
            current = current.next
        return current.val
        
        
   
                
    #############################
    # All private functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    def __len__(self):
        count=0
        current = self._first
        while current:
            count+=1
            current= current.next
        return count
    
    def __str__(self):
        final = []
        current = self._first
        while current:
            final.append(str(current.val))
            current = current.next
        return "->".join(final)+ "->Null"
            


# # Util class
# # Nothing can be changed
# # No need to write any code here

# In[11]:


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
    def generate_n_numbers_in_desscending_order(self, n:int)->'List of integer':
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


# In[ ]:





# # Slist test class
# # NOTHING CAN BE CHANGED BELOW

# In[12]:


############################################################
# SlistTest.py 
# Test Bench for Slist
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################

############################################################
#  NOTHING CAN BE CHANGED IN THIS FILE
########################################################### 

############################################################
#  All imports here
###########################################################
import sys # For getting Python Version
#from ListNode import *
#from Slist import *
#from Util import *

############################################################
#  class  SlistTestAdd
###########################################################    
class SlistTestAdd():
    def __init__(self):
        self._add()

    def _add(self):
        print("------------  test append/prepend/find =================")
        s = Slist() 
        a = [1,2,3,4,5]
        s.build_slist_from_list(a)
        print(a,"is stored as",s);
        num = len(s)
        print("size of slist =",num)
        assert(num == len(a))
        b = [10,11,12]
        for i in b:
            s.prepend(i)
        print("After prepending",b,"s looks like",s);  
        num = len(s)
        print("size of slist =",num)
        assert(num == len(a) + len(b))
        for i in a:
            f = s.find(i)
            if (f == False):
                print(i,"is there in s, but you are telling not there")
                assert(False)
        for i in b:
            f = s.find(i)
            if (f == False):
                print(i,"is there in s, but you are telling not there")
                assert(False)
        print("Find if there passed")
        c = [6,7,8,9]
        for i in c:
            f = s.find(i)
            if (f == True):
                print(i,"is NOT there in s, but you are telling it is there")
                assert(False)
        print("Find if NOT there passed")

############################################################
#  class  SlistTestDelete
###########################################################    
class SlistTestDelete():
    def __init__(self):
        self._delete()

    def _delete(self):
        print("------------  test delete =================")
        s = Slist() 
        a = [1,2,3,4,5]
        s.build_slist_from_list(a)
        print(a,"is stored as",s);
        num = len(s);
        print("Size of s =",num)
        assert(num == len(a))
        x = 1
        s.delete(x)
        print("after removing",x, ":",s)
        num = len(s)
        assert(num == len(a)-1)
        x = 5
        s.delete(x)
        print("after removing",x, ":",s)
        num = len(s)
        assert(num == len(a)-2)
        x = 3
        s.delete(x)
        print("after removing",x, ":",s)
        num = len(s)
        assert(num == len(a)-3)
        x = 100
        f = s.delete(x)
        assert(f == False)
        print("Cannot Remove",x, "as it is not there",s)
        num = len(s)
        assert(num == len(a)-3)
        x = 2
        s.delete(x)
        print("after removing",x, ":",s)
        num = len(s)
        assert(num == len(a)-4)
        x = 4
        s.delete(x)
        print("after removing",x, ":",s)
        num = len(s)
        assert(num == len(a)-5)
        if (s.is_empty()):
            print("s is empty")
        assert(s.is_empty())
        
        ## TESTS delete_front
        print("-----------  Testing delete_front ---------------------")
        a = [1,2,3,4,5]
        lena = len(a)
        s.build_slist_from_list(a)
        print(a,"is stored as",s);
        num = len(s);
        print("Size of s =",num)
        assert(num == lena)
        j = lena ;
        for i in a:
            j = j - 1;
            s.delete_front()
            print("after removing",i, ":",s)
            num = len(s)
            assert(num == j )
            
        ## TESTS delete_front
        print("-----------  Testing delete_last ---------------------")
        a = [1,2,3,4,5]
        lena = len(a)
        s.build_slist_from_list(a)
        print(a,"is stored as",s);
        num = len(s);
        print("Size of s =",num)
        assert(num == lena)
        j = lena ;
        for i in reversed(a):
            j = j - 1;
            s.delete_last()
            print("after removing",i, ":",s)
            num = len(s)
            assert(num == j )

############################################################
#  class  Slist Reverse
###########################################################    
class SlistReverse():
    def __init__(self, recursive:'bool'):
        self._a = []
        self._reverse(self._a,recursive)
        self._a = [1]
        self._reverse(self._a,recursive)
        self._a = [1,2,3,4,5]
        self._reverse(self._a,recursive)
        N = 100
        self._a = []
        for i in range(N):
            self._a.append(i)
        self._reverse(self._a,recursive)

    def _reverse(self,a,recursive):
        if (recursive):
            print("------------  test recursive reverse =================")
            s = Slist() 
            lena = len(self._a)
            s.build_slist_from_list(self._a)
            print(a,"is stored as",s);
            num = len(s);
            print("Size of s =",num)
            assert(num == lena)
            s.reverse_recur()
            print("s after reverse_recur",s)
            num = len(s);
            assert(num == lena)
        else:
            print("------------  test reverse Iterative=================")
            s = Slist() 
            lena = len(self._a)
            s.build_slist_from_list(self._a)
            print(a,"is stored as",s);
            num = len(s);
            print("Size of s =",num)
            assert(num == lena)
            s.reverse()
            print("s after reverse",s)
            num = len(s);
            assert(num == lena)
        
############################################################
#  class  Slist Midpoint
###########################################################    
class SlistTestMidpoint():
    def __init__(self):
        self._a = []
        self._midpoint(self._a)
        self._a = [1]
        self._midpoint(self._a)
        self._a = [1,2]
        self._midpoint(self._a)
        self._a = [1,2,3]
        self._midpoint(self._a)
        self._a = [1,2,3,4]
        self._midpoint(self._a)
        self._a = [1,2,3,4,5]
        self._midpoint(self._a)
        self._a = [1,2,3,4,5,6]
        self._midpoint(self._a)
        N = 100
        self._a = []
        for i in range(N):
            self._a.append(i)
        self._midpoint(self._a)

    def _midpoint(self,a):
        print("------------  test midpoint using 2 pointers =================")
        s = Slist() 
        s.build_slist_from_list(self._a)
        print(a,"is stored as",s);
        num = len(s)
        print("size of slist =",num)
        assert(num == len(a))
        mval = s.find_mid_point()
        ans = 0
        if (num):
            mid = (0 + (num -1)) // 2
            ans = s.getI(mid)
        print("Mid point of s =",mval)
        print("Expected Mid point of s =",ans)
        assert(mval == ans)

class L0002Test():
    def __init__(self):
        self._show = True
        self._k = 0 
        self._assert_answers = True
        self._u = Util()
        self._testBench()

    #Private  function
    def _testBench(self):
        self._tests()
        self._testn()
        print("ALL TESTS PASSED")

    #Private sunction
    def _test1(self,a:'int',b:'int') -> None:
        if (self._show):
            self._k = self._k + 1             
            print("-------------PROBLEM",self._k,"---------------")
            print("a=",a)
            print("b=",b)
            print("answer must be =",a + b)
            print("Let us see your work")

        aslist = Slist()
        bslist = Slist()
        reverse = True
        aslist.build_slist_from_int(a,True)
        bslist.build_slist_from_int(b,True)
        cslist = aslist + bslist

        if (self._assert_answers or self._show):
            aval = aslist.get_value(reverse)
            bval = bslist.get_value(reverse)
            cval = cslist.get_value(reverse)

            if (self._show):
                print("aslist=",aslist,"The number is",aval)
                print("bslist=",bslist,"The number is",bval)
                print("cslist=",cslist,"The number is",cval)

            if (a != aval):
                print("aslist=",aslist)
                print("Given a = ",a, "But your value of aslist = ", aval)
                assert(False)
            if (b != bval):
                print("bslist=",bslist)
                print("Given c = ",a, "But your value of bslist = ", bval)
                assert(False)
            e = a + b ;
            if (cval != e):
                print("YOU CANNOT ADD",a , "+", b ,"=",e, "But your answer is",cval)
                print("cslist=",cslist)
                assert(False)

 
    #Private sunction
    def _tests(self):
        self._show = True
        self._assert_answers = True
        a = 342
        b = 465
        self._test1(a,b)
        
        a = 0
        b = 0
        self._test1(a,b)

        a = 9999999
        b = 9999
        self._test1(a,b)

        a = 3490529510847650949147849619903898133417764638493387843990820577
        b = 32769132993266709549961988190834461413177642967992942539798288533
        self._test1(a,b)


    #Private sunction
    def _testn(self):
        self._show = False
        self._assert_answers = True
        N = 10000
        K = 1000000
        print("________________________Testing ON", N, "random bumbers between 1 TO",K,"________________________")
        for i in range(0,N):
            a = self._u.generate_a_random_number(1,K)
            b = self._u.generate_a_random_number(1,K)
            self._test1(a,b)
        print("ALL ", N, "random tests passed")
        print("If you don't see this line means, you cannot add two numbers :-)")

############################################################
# TWO TESYS
###########################################################  
def test1():
    print("Basic slist test starts")
    print(sys.version)
    t = SlistTestAdd()
    t = SlistTestDelete()
    print("Basic slist test Passed. If you don't see this line means, you cannot write Slist")

def test2():
    recursive = False
    t = SlistReverse(recursive)
    #recursive = True
    ##t = SlistReverse(recursive)
    t = SlistTestMidpoint()
    #print("Testing L0002Test Starts")
    #s = L0002Test()
    #print("Testing L0002Test Ends")


# # main

# In[13]:


def main():
    test1()
    test2()
   


# In[14]:


main()


# In[ ]:





# In[ ]:




