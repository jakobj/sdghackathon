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

import numpy as np
from sklearn.datasets import make_friedman2
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel

def plt_errorbar(ax, xplt,yplt,yerr,label=None,lw=2,c='steelblue',marker='',alpha=0.3,ls=None,offset=0,zorder=None,add_to_offset=True):
    # ax.plot(xplt,offset + yplt,lw=lw,c=c,marker=marker,ls=ls,label=label, alpha=alpha)
    # ax.fill_between(xplt,offset + yplt-yerr,yplt+yerr,color=c,alpha=alpha)
    if add_to_offset:
        # ax.plot(xplt, offset + yplt, color=c, alpha=alpha,zorder=-1)
        ax.fill_between(xplt, offset, offset + yplt, color=c, alpha=alpha, linewidth=0, zorder=-1)
    else:
        # ax.plot(xplt, yplt, color=c, alpha=alpha, zorder=-1)
        ax.fill_between(xplt, offset, yplt, color=c, alpha=alpha, linewidth=0, zorder=-1)

def fit_gp_and_predict(time,y,t_start,t_end,ax,fill_color,opa,dt,offset=0,zorder=None,add_to_offset=True):
    # fit GP
    kernel = DotProduct() + WhiteKernel()
    gpr = GaussianProcessRegressor(kernel=kernel,
                               random_state=0).fit(time.reshape([time.shape[0],1]), y)
    #create prediction
    t_pred = np.linspace(t_start-0.1,t_end,dt).reshape([dt,1])
    y_pred = gpr.sample_y(t_pred,n_samples=dt,random_state=0)
    y_mean = np.mean(y_pred,axis=1)
    y_mean = np.clip(y_mean, 0.0, np.inf)
    y_err = np.std(y_pred,axis=1)
    y_mean[0] = y[-1]  #smooth transition
    
    plt_errorbar(ax, t_pred.flatten(), y_mean, y_err,c=fill_color,alpha=opa,offset=offset,zorder=zorder,add_to_offset=add_to_offset)
    return y_mean
