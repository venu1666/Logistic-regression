import numpy as np
import matplotlib.pyplot as plt
import re
import math
from matplotlib import cm
def load(data):
    features=[]
    file=open(data)
    for line in file:
        lines=[float(j) for j in re.findall(r'[+\d.\d]+',line)]
        lines.insert(0,1)
        features.append(lines)
    target=[]
   
    for i in features:
        target.append([i.pop()])
    return features,target
 


       

def plot(data,target,w):
     z=data.dot(w)
     hx=hx=1/(1+(np.exp(-z)))
     plt.scatter(z,target)
     plt.scatter(z,hx)
     plt.show()

   
    
    
    
  
    
    
    
    #for i in range(len(data)):
        #if(data[i][-1]==)
    
     


def cal_cost(dataset,target,w):
    z=dataset.dot(w)
    hx=1/(1+(np.exp(-z)))
    #cost=(np.mean(target*(np.log(hx))+(1-target)*(np.log(1-hx))))
    cost=(sum(hx-target)**2)/(2*len(dataset))
    return cost


    
def gradient(dataset,target,w):
  
    a=0.001
    z=dataset.dot(w)
    #hx=1/(1+(np.exp(-z)))
    w=w-a*((dataset.T).dot((1/(1+(np.exp(-z))))-target))/len(target)
    return w

         
        
def plotcost(cost):
    d=range(50)
    x=d
    y=cost
    plt.plot(x,y)
    
def predict(data,w,target):
    l=[]
    z=data.dot(w)
    hx=1/(1+(np.exp(-z)))
    
    for i in hx:
        if(i<1.5):
            l.append(1.0)
        else:
            l.append(2.0)
   
    k=[]
    for j in range(len(target)):
        k.append(l)
        print(l)
    
        
    
             
def main():
    dataset,target=load('C:/Users/venu/Downloads/Skin_NonSkin.txt')
   
    #plot(dataset,target)

    dataset=np.array(dataset)
    
    target=np.array(target)
    w=[]
    for j in range(len(dataset[1])):
        w.append([0])
    
    for l in range(10):
          cost=cal_cost(dataset,target,w)
          w=gradient(dataset,target,w)
    plot(dataset,target,w)
    print(cost)
    predict(dataset,w,target)
    
    
    
main()