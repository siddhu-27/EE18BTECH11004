import numpy as np
import matplotlib.pyplot as plt

P = np.array([2,-6])
Q = np.array([5,2])
R = np.array([-2,2])
W = np.array([2,2])
X = np.array([-0.6,-0.8]) 
Y = np.array([4.1369,-0.3013]) 
Z = np.array([2,0.5])

len = 10
lam_1 = np.linspace(0,1,len)

x_PQ = np.zeros((2,len))
x_QR = np.zeros((2,len))
x_RP= np.zeros((2,len))
x_PW = np.zeros((2,len))
x_QX = np.zeros((2,len))
x_RY = np.zeros((2,len))
for i in range(len):
	temp1 = P + lam_1[i]*(Q-P)
	x_PQ[:,i] = temp1.T
	temp2 = Q + lam_1[i]*(R-Q)
	x_QR[:,i] = temp2.T
	temp3 = R + lam_1[i]*(P-R)
	x_RP[:,i] = temp3.T
	temp4 = P + lam_1[i]*(W-P)
	x_PW[:,i] = temp4.T
	temp5 = Q + lam_1[i]*(X-Q)
	x_QX[:,i] = temp5.T
	temp6 = R + lam_1[i]*(Y-R)
	x_RY[:,i] = temp6.T
	
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')
plt.plot(x_PW[0,:],x_PW[1,:],label='$PW$')
plt.plot(x_QX[0,:],x_QX[1,:],label='$QX$')
plt.plot(x_RY[0,:],x_RY[1,:],label='$RY$')	

plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1 + 0.08),P[1]*(1 + 0.01), 'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1 + 0.02),Q[1]*(1 - 0.01), 'Q')
plt.plot(R[0],R[1],'o')
plt.text(R[0]*(1 + 0.1),R[1]*(1 - 0.2), 'R')
plt.plot(W[0],W[1],'o')
plt.text(W[0]*(1 + 0.1),W[1]*(1 - 0.1), 'W')
plt.plot(X[0],X[1],'o')
plt.text(X[0]*(1 + 0.1),X[1]*(1 - 0.3), 'X')
plt.plot(Y[0],Y[1],'o')
plt.text(Y[0]*(1 + 0.06),Y[1]*(1 - 0.1), 'Y')
plt.plot(Z[0],Z[1],'o')
plt.text(Z[0]*(1 + 0.06),Z[1]*(1 + 0.3), 'Z')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
