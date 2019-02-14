import numpy as np
import matplotlib.pyplot as plt

def dir_vec(QR):
	return np.matmul(QR,dvec)
	
def ortocenterH1(QR,QP):	
	d1 = dir_vec(QR)
	d2 = dir_vec(RP)
	N1 = np.vstack((d1,d2))
	pa = np.zeros(2)
	pa[0] = np.matmul(d1,P)
	pa[1] = np.matmul(d2,Q)
	return np.matmul(np.linalg.inv(N1),pa)

def ortocenterH2(RP,PQ):
	d2 = dir_vec(RP)
	d3 = dir_vec(PQ	)
	N2 = np.vstack((d2,d3))
	pb = np.zeros(2)
	pb[0] = np.matmul(d2,Q)
	pb[1] = np.matmul(d3,R)
	return np.matmul(np.linalg.inv(N2),pb
	)
def ortocenterH3(PQ,QR):
    d3 = dir_vec(PQ)
	d1 = dir_vec(QR)
	N3 = np.vstack((d3,d1))
	pc = np.zeros(2)
	pc[0] = np.matmul(d3,R)
	pc[1] = np.matmul(d1,P)
	return np.matmul(np.linalg.inv(N3),pc)
		
P = np.array([2,-6])
Q = np.array([5,2])
R = np.array([-2,2])

PQ = np.vstack((P,Q)).T
QR = np.vstack((Q,R)).T
RP = np.vstack((R,P)).T
dvec = np.array([-1,1])

print(ortocenterH1(QR,RP))
print(ortocenterH2(RP,PQ))
print(ortocenterH3(PQ,QR))
