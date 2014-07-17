# version code 761
# Please fill out this stencil and submit using the provided submission script.

from vec import *
## Problem 1
def vec_select(veclist, k): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    return [x for x in veclist if k not in x.f or x.f[k] == 0 ] 
    pass

def vec_sum(veclist, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    sumVec = Vec(D,{})
    for x in veclist:
        sumVec = add(x,sumVec)   
    return sumVec   
    pass

def vec_select_sum(veclist, k, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    sumVec = Vec(D,{})
    for x in veclist:
        if k not in x.f or x.f[k] == 0: 
            sumVec = add(x,sumVec)   
    return sumVec   
    pass

## Problem 2
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,3}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
    True
    '''
    modList = list()
    for index,vector in vecdict.items():
        tmpdict = dict()
        for key,value in vector.f.items():
            tmpdict[key] = value/index
        modList.append(Vec(vector.D,tmpdict))
    return modList                      
    pass

## Problem 3
def GF2_span(D, L):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
    >>> len(GF2_span(D, L))
    4
    >>> Vec(D, {}) in GF2_span(D, L)
    True
    >>> Vec(D, {'b': one}) in GF2_span(D, L)
    True
    >>> Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
    True
    >>> Vec(D, {x:one for x in D}) in GF2_span(D, L)
    True
    '''
    if len(L) == 0:
      return list()
    powerSet = list()
    for x in range(2**len(L)):
      powerSet.append(generateList(x,L))
    spanList = list()
    for x in powerSet:
      if len(x) == 0:
        spanList.append(Vec(D,dict()))
        continue
      sumVec = x[0]
      for i in range(1,len(x)):
        sumVec = add(sumVec,x[i])
      spanList.append(sumVec)  
    return spanList
    pass

def generateList(n, L):
    lst = list()
    counter = 0
    while n > 0:
      if n & 1 == 1:
        lst.append(L[counter])     
      n = n >> 1
      counter +=1
    return lst

## Problem 4
# Answer with a boolean, please.

is_it_a_vector_space_1 = True
is_it_a_vector_space_2 = False



## Problem 5
is_it_a_vector_space_3 = True
is_it_a_vector_space_4 = False


## Problem 6

is_it_a_vector_space_5 = True
is_it_a_vector_space_6 = False
