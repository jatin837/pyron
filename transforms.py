import numpy as np
def z_table(data):
    """
    PARAMETERS :
    ----------
    data as a numpy row vector
    RETURNS:
    --------
    z-transformed data as numpy row vector
    """
    mu = np.mean(data)
    sigma = np.std(data)
    res = (data - mu)/sigma
    return res

def min_max(data):
    """
    PARAMETERS :
    ----------
    non standardized numpy row vector
    RETURNS :
    -------
    standard numpy row vector between 0 and 1
    """
    minVal = np.min(data)
    maxVal = np.max(data)
    res = (data - minVal)/(data - maxVal)
    return res

def box_cox(data):
    """
    PARAMETERS:
    ----------
    non-normal numpy row vector 
    RETURNS:
    -------
    normal numpy row vector
    """
    pass

