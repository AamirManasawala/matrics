from vec import Vec

def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]
    return M.f[k] if k in M.f else 0
    pass

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k] = val
    pass

def add(A, B):
    "Returns the sum of A and B"
    assert A.D == B.D
    addDict = dict()
    for key1,val in A.f.items():
        addDict[key1] = getitem(B,key1) + val
    for key2,val in B.f.items():
        if key2 not in A.f:
            addDict[key2] = val
    return Mat(A.D,addDict)

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M" 
    return Mat(M.D,{k:v*alpha for k,v in M.f.items()})
    pass

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    for key,value in A.f.items():
        if key in B.f and B.f[key] != value:
            return False
        elif key not in B.f and value != 0:
            return False
    for key,value in B.f.items():
        if key not in A.f and value != 0:
            return False
    return True

def transpose(M):
    "Returns the transpose of M"
    return Mat((M.D[1],M.D[0]), {(key[1],key[0]):value for key,value in M.f.items()} ) 
    pass

def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D
    resultVec = Vec(M.D[1],dict())
    for k in M.f.keys():
        resultVec[k[1]] +=  M[k[0],k[1]] * v[k[0]]
    return resultVec   
    pass

def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D
    resultVec = Vec(M.D[0],dict())
    for k in M.f.keys():
        if k[0] in resultVec.f:
            resultVec.f[k[0]] = resultVec.f[k[0]] + M[k[0],k[1]]*v[k[1]]
        else:
            resultVec.f[k[0]] = M[k[0],k[1]] * v[k[1]]
    return resultVec     
    pass

def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]
    productMat = Mat((A.D[0],B.D[1]) ,dict())
    for i,x in enumerate(A.D[0]):
        for j,y in enumerate(B.D[1]):
            for k,z in enumerate(A.D[1]):
                productMat[(x,y)] += A[x,z] * B[z,y]   
    return productMat
    pass

################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"
