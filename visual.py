import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pydataset import data
from scipy import stats

#--------------------------------------------------------------------------------------------------

def scatter(x_str, y_str, datasource):
    '''
    Intakes x and y axis data values and plots it into a scatter plot.
    '''

    plt.title('Square Feet and Tax Value')
    # scatter plot
    sns.scatterplot(x=x_str, y=y_str, data=datasource)

    plt.xlabel('Square Feet')
    plt.ylabel('Tax Value')

    plt.show()

#--------------------------------------------------------------------------------------------------

def barplot(x_str, y_str, datasource):
    '''
        Intakes x and y axis data values and plots it into a bar plot.
    '''
    plt.title(' Bedrooms and Tax Value')
    sns.barplot(x=x_str, y=y_str, data=datasource)
    plt.xlabel('Bedrooms')
    plt.ylabel('Tax Value')
    plt.show()

#--------------------------------------------------------------------------------------------------

def boxplot(x_str, y_str, datasource):
    '''
    Intakes x and y axis data values and plots it into a box plot
    '''

    sns.boxplot(x=x_str, y=y_str, data=datasource)
    plt.show()

#--------------------------------------------------------------------------------------------------

def subplots(df):


    plt.subplot(131)
    sns.barplot(x='bedrooms', y='tax_value', data=df)
    plt.xlabel('Bedrooms')
    plt.ylabel('Tax Value')

    plt.subplot(133)
    sns.boxplot(x='bedrooms', y='tax_value', data=df)
    plt.xlabel('Bedrooms')
    plt.ylabel('Tax Value')

    plt.show()

#--------------------------------------------------------------------------------------------------

def barplot2(df):
    '''
        Intakes x and y axis data values and plots it into a bar plot.
    '''
    plt.title(' Bathrooms and Tax Value')
    sns.barplot(x='bathrooms', y='tax_value', data=df)
    plt.xlabel('Bathrooms')
    plt.ylabel('Tax Value')
    plt.show()

#--------------------------------------------------------------------------------------------------

def barplot3(df):

    ax = sns.barplot(x='fips', y='tax_value', data=df)
    ax.set_xticklabels(['LA (6037)','Orange (6059)','Ventura (6111)'])
    plt.xlabel('FIPS')
    plt.ylabel('Tax Value')
    plt.title('County(FIPS) and Tax Value')
    plt.show()