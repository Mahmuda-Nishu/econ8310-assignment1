import unittest
import patsy as pt
from pygam import LinearGAM, f, s, l
import numpy as np
import pandas as pd
import statsmodels as statsmodels
import pygam
from statsmodels.tsa.holtwinters import ExponentialSmoothing as ES
import prophet
import statsmodels.tsa.holtwinters as hw

# Import your code from parent directory
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from assignment1 import model, modelFit, pred

# Run the checks

class testCases(unittest.TestCase):
    def testFittedModel(self):
        if isinstance(modelFit, statsmodels.regression.linear_model.RegressionResultsWrapper) or isinstance(modelFit, statsmodels.tsa.arima.model.ARIMAResultsWrapper) or isinstance(modelFit, hw.results.HoltWintersResultsWrapper):
            self.assertTrue(True)
        elif hasattr(modelFit, '_is_fitted'):
            if modelFit._is_fitted:
                self.assertTrue(True)
        elif hasattr(modelFit, 'history'):
            self.assertTrue(bool(modelFit.history))
        else:
            print("Make sure that you store your fitted model in the variable 'modelFit'.")
            self.assertTrue(False)
            
