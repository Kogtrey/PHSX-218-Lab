import numpy as np

def ruleOne(c,dA):
    return np.abs(c) * dA

def ruleTwo(c,m,A,dA):
    return np.abs(c * m * (A**(m-1))) * dA

def ruleThree(deltas):
    return np.sqrt(np.sum(deltas**2))


def ruleFour(Q,const,deltas,vals):
    return np.abs(Q) * np.sqrt(np.sum((const * deltas/vals)**2))
