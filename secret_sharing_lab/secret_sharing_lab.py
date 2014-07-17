# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from hw5 import *


## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        u = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        if u* a0 == s and u * b0 == t:
            return u              
    pass

def random_select():
    while True:
     a1 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
     b1 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
     a2 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
     b2 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
     a3 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
     b3 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
     a4 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
     b4 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
     l1 = [a0,a1,a2,b0,b1,b2]
     l2 = [a0,a1,a3,b0,b1,b3]
     l3 = [a0,a1,a4,b0,b1,b4]
     l4 = [a0,a2,a3,b0,b2,b3]
     l5 = [a0,a2,a4,b0,b2,b4]
     l6 = [a0,a3,a4,b0,b3,b4]
     l7 = [a1,a2,a3,b1,b2,b3]
     l8 = [a1,a2,a4,b1,b2,b4]
     l9 = [a1,a3,a4,b1,b3,b4]
     l10 =[a2,a3,a4,b2,b3,b4]
     t1 = my_is_independent(l1);
     t2 = my_is_independent(l2);
     t3 = my_is_independent(l3);
     t4 = my_is_independent(l4);
     t5 = my_is_independent(l5);
     t6 = my_is_independent(l6);
     t7 = my_is_independent(l7);
     t8 = my_is_independent(l8);
     t9 = my_is_independent(l9);
     t10 = my_is_independent(l10);
     if t1 == True and t2 == True and t3 == True and t4 == True and t5 == True  and t6 == True and t7 == True and t8 ==True and t9 == True and t10 == True:
      return [a1,b1,a2,b2,a3,b3,a4,b4]
       
list_ab = random_select()


## Problem 2
# Give each vector as a Vec instance
secret_a0 = a0
secret_b0 = b0
secret_a1 = list_ab[0]
secret_b1 = list_ab[1]
secret_a2 = list_ab[2]
secret_b2 = list_ab[3]
secret_a3 = list_ab[4] 
secret_b3 = list_ab[5]
secret_a4 = list_ab[6]
secret_b4 = list_ab[7]

