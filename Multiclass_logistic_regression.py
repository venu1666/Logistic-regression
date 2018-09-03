import numpy as np
import matplotlib.pyplot as plt
import re

def load(data):
    k=[]
    labels=[]
    features=[]
    file=open(data)
    for line in file:
        k.append(line)
    del(k[-1])
    for line in k:
        b=[]
        a=line.strip('\n').split(',')
        if(a[-1]=='Iris-setosa'):
            labels.append([0])
        elif(a[-1]=='Iris-versicolor'):
            labels.append([1])
        elif(a[-1]=='Iris-virginica'):
            labels.append([2])
        a.pop()
        for x in a:
            b.append(float(x))
        features.append(b)
    features=np.array(features)
    targets=np.array(labels)
    return features,targets


def cal_gradient(features,target,w):
    a=0.001
    z=features.dot(w)
    hx=1/(1+np.exp(-z))
    w=w-a*((features.T).dot(hx-target))/len(target)
    return hx,w


def cal_cost(features,targets,w):
        z=features.dot(w)
        hx=1/(1+np.exp(-z))
        cost=-np.mean((targets*np.log(hx))+((1-targets)*(np.log(1-hx))))
        return cost
            
def predicting(features,w):
            z=features.dot(w)
            hx=1/(1+np.exp(-z))
            return hx
    

def main():
    features,targets=load('C:/Users/venu/Desktop/ml/datasets/iris.data')
    setosa=[]
    versicolor=[]
    verginica=[]
    for i in targets:
        if(i[0]==0):
            setosa.append([1])
        else:
            setosa.append([0])
    for m in targets:
        if(m[0]==1):
            versicolor.append([1])
        else:
            versicolor.append([0])
    for n in targets:
        if(n[0]==2):
            verginica.append([1])
        else:
            verginica.append([0])       
    setosa=np.array(setosa)
    versicolor=np.array(versicolor)
    verginica=np.array(verginica)
    w1=[]
    w2=[]
    w3=[]
    p=[]
    for k in range(len(features[1])):
        w1.append([0])
        w2.append([0])
        w3.append([0])
    w1=np.array(w1)
    w2=np.array(w2)
    w3=np.array(w3)
    for i in range(100000):
              hx1,w1=cal_gradient(features,setosa,w1)
              cost1=cal_cost(features,setosa,w1)
              hx2,w2=cal_gradient(features,versicolor,w2)
              cost2=cal_cost(features,versicolor,w2)
              hx3,w3=cal_gradient(features,verginica,w3)
              cost3=cal_cost(features,verginica,w3)
    predict=[]
    for i in range(len(hx1)):
        if(hx1[i]>hx2[i] and hx1[i]>hx3[i]):
            predict.append([0])
        elif(hx2[i]>hx1[i] and hx2[i]>hx3[i]):
            predict.append([1])
        elif(hx3[i]>hx1[i] and hx3[i]>hx2[i]):
            predict.append([2])
    predict=np.array(predict)
    count=0
    for i in range(len(targets)):
        if(predict[i][0]==targets[i][0]):
            count=count+1
    print(count/len(targets)*100)
    
    x=int(input('enter the number of predictions u want:'))
    for a in range(x):
        a=[6.8,2.8,4.8,1.4]
        '''for j in range(len(features[1])):
            a.append(float(input('enter the value:')))'''
    a=np.array(a)
    hx=predicting(a,w1)
    hx1=predicting(a,w2)
    hx2=predicting(a,w3)
    if(hx>hx1 and hx>hx2):
            print('setosa')
    elif(hx1>hx and hx1>hx2):
            print('versicolor')
    elif(hx2>hx and hx2>hx1):
            print('verginica')
    
    
            
        
            
        
        
    
            
            
    
    
main()