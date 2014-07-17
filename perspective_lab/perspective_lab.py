from image_mat_util import *
from mat import Mat
from vec import Vec
from solver import solve
from matutil import *
## Task 1
def move2board(v): 
    '''
    Input:
        - v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
    Output:
        - A {'y1','y2','y3'}-vector z, the coordinate representation
          in whiteboard coordinates of the point p such that the line through the 
          origin and q intersects the whiteboard plane at p.
    '''
    
    return Vec({'y1','y2','y3'}, {k:val/v.f['y3'] for k,val in v.f.items()}  )

## Task 2
def make_equations(x1, x2, w1, w2): 
    '''
    Input:
        - x1 & x2: photo coordinates of a point on the board
        - y1 & y2: whiteboard coordinates of a point on the board
    Output:
        - List [u,v] where u*h = 0 and v*h = 0
    '''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    u = Vec(domain, {('y3','x1'):w1*x1,('y3','x2'):w1*x2,('y3','x3'):w1,('y1','x1'):-1*x1,('y1','x2'):-1*x2,('y1','x3'):-1 })
    v = Vec(domain, {('y3','x1'):w2*x1,('y3','x2'):w2*x2,('y3','x3'):w2,('y2','x1'):-1*x1,('y2','x2'):-1*x2,('y2','x3'):-1})
    return [u, v]


## Task 3

domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
H = Mat(({'y1','y2','y3'},{'x1','x2','x3'}), {('y3', 'x2'): -0.011690730864965316, ('y3', 'x1'): -0.721935681071003, ('y2', 'x1'): -0.38152131800543604, ('y2', 'x2'): 0.7378180860600994, ('y1', 'x1'): 1.0, ('y2', 'x3'): 110.02318074778253, ('y1', 'x3'): -359.860962566845, ('y1', 'x2'): 0.051693404634581386, ('y3', 'x3'): 669.4762699006177})

## Task 4
def mat_move2board(Y):
    '''
    Input:
        - Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector 
          giving the whiteboard coordinates of a point q.
    Output:
        - Mat instance, each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane 
          of the line through the origin and q).
    '''
    
    return coldict2mat({k:move2board(v) for k,v in mat2coldict(Y).items()})
    pass
