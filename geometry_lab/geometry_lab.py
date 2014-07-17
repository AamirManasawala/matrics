from mat import Mat
import math
from math import *

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat(({i for i in labels},{j for j in labels}), {(k1,k2):1 for k1 in labels for k2 in labels if k1==k2} )
    pass

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):1,('y','y'):1,('u','u'):1,('x','u'):x,('y','u'):y}) 
    pass

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):a,('y','y'):b,('u','u'):1}) 
    pass

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):cos(angle),('y','y'):cos(angle),('x','y'):-1 * sin(angle),('y','x'):sin(angle),('u','u'):1}) 
    pass

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y) * rotation(angle) * translation(-x,-y)
    pass

def sparcify(M):
    return Mat(M.D,{(key,value) for key,value in M.f.items() if value != 0})

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    return scale(-1,1)
    pass

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    return scale(1,-1)
    pass
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    return Mat(({'r','g','b'},{'g','r','b'}),{('r','r'):scale_r,('g','g'):scale_g,('b','b'):scale_b})
    pass

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    r = 77/256
    g = 151/256
    b = 28/256

    dic =  {('r','r'):r,('g','g'):g,('b','b'):b,('r','g'):g,('r','b'):b,('b','r'):r,('b','g'):g,('g','b'):b,('g','r'):r} 
    return Mat(({'r','g','b'},{'g','r','b'}),dic)
    pass   

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


