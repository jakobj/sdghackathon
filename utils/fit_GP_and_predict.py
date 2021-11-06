# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:48:38 2021
Function producing a prediciton based on a fitted GP
Input:
    t ... times of shape n
    y  ... values for each time-point of shape n
    t_start ... starting point of prediction, integer
    t_end ... end point of prediction, integer
    dt ... bin size for intervall [t_start,t_end], integer
    ax ... figure to add prediction
    fill_color ... color to fill, string
    opa ... fill opacity, float between 0 and 1
    
@author: horvat
"""

from sklearn.datasets import make_friedman2
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel

def plt_errorbar(xplt,yplt,yerr,label=None,lw=2,c='steelblue',marker='',alpha=0.3,ls=None):
    ax.plot(xplt,yplt,lw=lw,c=c,marker=marker,ls=ls,label=label)
    ax.fill_between(xplt,yplt-yerr,yplt+yerr,color=c,alpha=alpha)

def fit_gp_and_predict(time,y,t_start,t_end,ax,fill_color,opa):
    # fit GP
    kernel = DotProduct() + WhiteKernel()
    gpr = GaussianProcessRegressor(kernel=kernel,
                               random_state=0).fit(dt.reshape([time.shape[0],1]), y)
    #create prediction
    t_pred = np.linspace(t_start,t_end,dt).reshape([dt,1])
    y_pred = gpr.sample_y(x_pred,n_samples=dt,random_state=0)
    y_mean = np.mean(y_pred,axis=0)
    y_err = np.std(y_pred,axis=0)
    y_mean[0] = y[-1]  #smooth transition
    
    plt_errorbar(np.linspace(t_start,t_end,dt), y_mean, y_err,c=fill_color,alpha=opa) 

