#coding: utf-8
import math
from scipy.spatial.distance import pdist
from numpy import array, vstack

def cos_similar(vector_A, vector_B): #cos類似度計算
    inner=0.0
    for (a, b) in zip(vector_A, vector_B):
        inner += a*b                        #内積
    for i in range(len(vector_A)):
        vector_A[i] = vector_A[i]**2
    for i in range(len(vector_B)):
        vector_B[i] = vector_B[i]**2
    norm_A = math.sqrt(sum(vector_A))       #ノルムA
    norm_B = math.sqrt(sum(vector_B))       #ノルムB
    return inner / (norm_A * norm_B)
def cos_distance(vector_A, vector_B):
    a = array(vector_A)
    b = array(vector_B)
    vector = vstack((a,b))
    return pdist(vector, 'cosine')

if __name__ == '__main__':
    a = [1,5]
    b = [2,7]
    
    print "scipy:cosine distance = " + str(cos_distance(a, b))
    print "my:cosine similarity = " + str(cos_similar(a, b))
    print "cos dis = 1 - cos sim"
    