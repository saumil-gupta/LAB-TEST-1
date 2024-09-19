#!/usr/bin/env python
# coding: utf-8

# In[89]:


import numpy as np
x=np.array([100,120,85,90,110,95])
y=np.array([80,75,60,95,85,90])
z=np.array([40,140,135,160,155,170])


# In[90]:


totalx=np.sum(x)
print("TOTAL RAINFALL IN CITY X IS ",totalx)
totaly=np.sum(y)
print("TOTAL RAINFALL IN CITY Y IS ",totaly)
totalz=np.sum(z)
print("TOTAL RAINFALL IN CITY Z IS ",totalz)

avgx=np.mean(x)
print("AVERAGE RAINFALL IN CITY X IS ",avgx)
avgy=np.mean(y)
print("AVERAGE RAINFALL IN CITY Y IS ",avgy)
avgz=np.mean(z)
print("AVERAGE RAINFALL IN CITY Z IS ",avgz)


# In[91]:


def totals(x):
    for i in range(0,len(x)):
        print("TOTAL RAINFALL IN MONTH ",i+1," IS",x[i]+y[i]+z[i])
    
def averages(x):
     for i in range(0,len(x)):
            print("TOTAL AVERAGE RAINFALL IN MONTH ",i+1," IS",(x[i]+y[i]+z[i])/3.0)
    
totals(x)
averages(x)


# In[92]:


import numpy as np
import matplotlib.pyplot as mpt
w=np.array(["Month-1","Month-2","Month-3","Month-4","Month-5","Month-6"])
aa=np.array(["City X","City Y","City Z"])
mpt.xlabel("Month")
mpt.ylabel("Rainfall")
mpt.title("City Variation")
mpt.plot(w,x,label="City 1")
mpt.plot(w,y,label="City 2")
mpt.legend()
mpt.show()


# In[93]:


print("DIFFERENCE BETWEEN MAX AND MIN RAINFALL IN CITY X IS ",np.max(x)-np.min(x))
print("DIFFERENCE BETWEEN MAX AND MIN RAINFALL IN CITY Y IS ",np.max(y)-np.min(y))
print("DIFFERENCE BETWEEN MAX AND MIN RAINFALL IN CITY Z IS ",np.max(z)-np.min(z))


# In[97]:


import numpy as np
import matplotlib.pyplot as mpt
f=np.array([np.max(x)-np.min(x),np.max(y)-np.min(y),np.max(z)-np.min(z)])
e=np.array(["City X","City Y","City Z"])
mpt.bar(e,f)
mpt.xlabel("City")
mpt.ylabel("Range of Rainfall")
mpt.title("Range Variation")
mpt.show()

