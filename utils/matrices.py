import numpy as np

def similar(M):
    _, C = np.linalg.eig(M)
    return np.dot(np.linalg.inv(C), np.dot(M, C))

def minor(M, i, j):
    M = np.delete(M, i, axis=0)
    M = np.delete(M, j, axis=1)
    return M

def cofactor(M, i, j):
    '''
    This assumes that M is a determinant matrix.
    Use minor() if only the minor is required.
    '''
    M = minor(M, i, j)
    return (-1)**(i+j) * np.linalg.det(M)
