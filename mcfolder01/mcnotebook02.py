# Databricks notebook source
#import libraries
import numpy as np
import matplotlib.pyplot as plt

#define variables
x = np.arange(0.000,3*np.pi,0.001)
y = np.sin(x*np.pi)
z = np.cos(x*np.pi)

#plot function
plt.plot(x,y,x,z)

#add labels to plot
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Continuous Sin and Cosine functions')
plt.legend(['sin(x)', 'cos(x)'])

#show plot
plt.show()
