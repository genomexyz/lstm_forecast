#!/usr/bin/python3

from __future__ import absolute_import, division, print_function, unicode_literals
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from PyEMD import EMD
import tensorflow as tf
import numpy as np
import datetime


#read data
