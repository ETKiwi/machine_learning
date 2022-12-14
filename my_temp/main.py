# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:09:02 2022

@author: BK
"""
import os
import glob
# import csv
# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from ML.pipeline.steps.preprocess import Preprocess
from ML.pipeline.steps.model import Model
from ML.pipeline.steps.utils import Utils
from ML.pipeline.steps.preflight import Preflight
from ML.pipeline.pipeline import Pipeline

def main():
    path = r'C:\Users\User'+'\\'
    os.chdir(path)
    
    inputs ={
        'path' : path,
        'files':glob.glob('*.csv'),
        'x':['x1','x2','X3','x4','x5'],
        'y':['y'],
        'column_duplicate':['x1'],
        'column_encoder': ['x1', 'x3']
        }
    
    
    steps = [
        Preflight(),
        Preprocess(),
        Model(),
        ]
    
    utils = Utils(path)
    p = Pipeline(steps)
    p.run(inputs, utils)
    
    
if __name__ == '__main__':
    main()





