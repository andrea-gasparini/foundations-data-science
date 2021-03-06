import numpy as np
import math



# Compute the intersection distance between histograms x and y
# Return 1 - hist_intersection, so smaller values correspond to more similar histograms
# Check that the distance range in [0,1]

def dist_intersect(x,y):
    
    #... (your code here)
    
    q = 0
    v = 0
    qv = 0
    
    for i in range(len(y)):
        qv += min(x[i], y[i])
        q += x[i]
        v += y[i]
        
    intersect = (qv/q + qv/v)/2
    
    assert 0 <= intersect <= 1
    return 1 - intersect


# Compute the L2 distance between x and y histograms
# Check that the distance range in [0,sqrt(2)]

def dist_l2(x,y):
    
    
    assert 0 <= np.sum(np.square(x-y)) <= np.sqrt(2)
    
    return np.sum(np.square(x-y))



# Compute chi2 distance between x and y
# Check that the distance range in [0,Inf]
# Add a minimum score to each cell of the histograms (e.g. 1) to avoid division by 0

def dist_chi2(x,y):
    
    x = x + 1.0
    y = y + 1.0
    
    assert 0 <= np.sum(np.square(x-y)/(x+y)) <= np.inf
    return np.sum(np.square(x-y)/(x+y))


def get_dist_by_name(x, y, dist_name):
  if dist_name == 'chi2':
    return dist_chi2(x,y)
  elif dist_name == 'intersect':
    return dist_intersect(x,y)
  elif dist_name == 'l2':
    return dist_l2(x,y)
  else:
    assert False, 'unknown distance: %s'%dist_name
  




