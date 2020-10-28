'''
Zachary Mollenhour
Stock Analysis Program
This program will predict stock closing prices by utilizing a simple machine learning model
Wihtin the program consists a GUI for the user to interact with
The algoirthm will pull the required data from Yahoo finance API
'''

from PyQt5 import QtCore, QtGui
from PyQt5.Qt import *
from yahoo_finance import Share
import datetime
import os
import pandas as pd
import numpy as np
import pandas_datareader.data as web 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import webbrowser


'''
Price Predictor Class 
'''

class PricePrediction:
    '''Analyze predictions for future closing price of a stock by performing
        Machine Learning against the acquired stock data
    '''
    #Init Function
    def __init__(self,start_Date, end_Date, train_Date, future_Date, future_num_days, pred_ticker):
        self.start_date = start_date
        self.end_date = end_date
        self.last_train_date = last_train_date
        self.future_dates = future_dates
        self.future_num_days = future_num_days
        self.pred_ticker = pred_ticker 
        self.results_df = pd.DataFrame({'Ticker' : [], 'Pred_ret' : [], 'Predicted_Date' : [], 'Days_Later': [], 'Act_ret' : [],
            'Act_Adj_Close' : [], 'Pred_Adj_Close' : [], 'Pct_Err' : [], 'Bench_PAC' : [], 'Bench_Pct_Err' : []})

    #Function to make a folder on the computer to store data
    def makeDirectory(self):
        '''Create a folder on the local machine to use for storing data gathered from Yahoo'''
        self.Yahoo_Folder = os.getcwd()+"\Yahoo_Downloads"

        #If the folder doesnt exist, make it
        if not os.path.exists(self.Yahoo_Folder):
            os.makedirs(self.Yahoo_Folder)