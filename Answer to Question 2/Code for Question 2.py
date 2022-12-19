'''
Question 8.2
'''

import math
import numpy as np
import matplotlib.pyplot as plt

## set up for initial parameters
k1 = 100
k2 = 600
k3 = 150

## define four functions of rate of changes of E, S ES and P
def fun_E (E, S, ES, P):
    return -k1*E*S + (k2+k3)*ES

def fun_S (E, S, ES, P):
    return -k1*E*S + k2*ES

def fun_ES (E, S, ES, P):
    return k1*E*S - (k2+k3)*ES

def fun_P (E, S, ES, P):
    return k3*ES
    
## Solve funtions using RK4 method:
def rk4_function (E, S, ES, P, n):
    E_list = [E]
    S_list = [S]
    ES_list = [ES]
    P_list = [P]
    L = [0]
    h = 0.0001
    t = 0
        
    while t < n:
        t = t + h
        L.append(t)
        
        ## first step:
        E1 = fun_E(E, S, ES, P)
        S1 = fun_S(E, S, ES, P)
        P1 = fun_P(E, S, ES, P)
        ES1 = fun_ES(E, S, ES, P)
        
        ## second step:
        e2 = E + E1*h/2
        s2 = S + S1*h/2
        es2 = ES + ES1*h/2
        p2 = P + P1*h/2
        E2 = fun_E(e2, s2, es2, p2)
        S2 = fun_S(e2, s2, es2, p2)
        ES2 = fun_ES(e2, s2, es2, p2)
        P2 = fun_P(e2, s2, es2, p2)
        
        ## third step:
        e3 = E + E2*h/2
        s3 = S + S2*h/2
        es3 = ES + ES2*h/2
        p3 = P + P2*h/2
        E3 = fun_E(e3, s3, es3, p3)
        S3 = fun_S(e3, s3, es3, p3)
        ES3 = fun_ES(e3, s3, es3, p3)
        P3 = fun_P(e3, s3, es3, p3)
        
        ## forth step:
        e4 = E + E3*h/2
        s4 = S + S3*h/2
        es4 = ES + ES3*h/2
        p4 = P + P3*h/2
        E4 = fun_E(e4, s4, es4, p4)
        S4 = fun_S(e4, s4, es4, p4)
        ES4 = fun_ES(e4, s4, es4, p4)
        P4 = fun_P(e4, s4, es4, p4)        
        
        E = E + (E1 + 2*E2 + 2*E3 + E4)* h/6
        S = S + (S1 + 2*S2 + 2*S3 + S4)* h/6
        ES = ES + (ES1 + 2*ES2 + 2*ES3 + ES4)* h/6
        P = P + (P1 + 2*P2 + 2*P3 + P4)* h/6
        E_list.append(E)
        S_list.append(S)
        ES_list.append(ES)
        P_list.append(P)
        
    return (E_list, S_list, ES_list, P_list, L)

## the inital parameters are given following:
E0 = 1
S0 = 10
ES0 = 0
P0 = 0
n = 0.35

## we can get the result as following:
results = rk4_function (E0, S0, ES0, P0, n)

## Plot the result:
E_result = results[0]
S_result = results[1]
ES_result = results[2]
P_result = results[3]
T = results[4]
plt.figure()
plt.plot(T, E_result, label = "[E]")
plt.plot(T, S_result, label = "[S]")
plt.plot(T, ES_result, label = "[ES]")
plt.plot(T, P_result, label = "[P]")
plt.title("Rate of Changes of E, S, ES, and P")
plt.legend()
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.show()

'''
Question 8.3
'''
## The velocity of the enzymatic reaction 
V = []
k3 = 150
for i in ES_result:
    v = i*k3
    V.append (v) 
S = S_result

## To show the result of Vmax
print(max(V))

## Plot the result
plt.figure()
plt.plot(S, V)
plt.xlabel("Concentration of S")
plt.ylabel("Velocity V")
plt.show()    