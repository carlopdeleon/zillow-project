import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # import needed for the train, test, split functions.
from scipy import stats

# Scalers
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


#--------------------------------------------------------------------------------------------------

# Function for Training, Validating, and Testing the data. 
def split_data(df, target= 'enter target column here'):
    ''' 
        This function is the train, validate, test, function.
        1. First we create the TRAIN and TEST dataframes at an 0.80 train_size( or test_size 0.2).

        2. Second, use the newly created TRAIN dataframe and split that at a 0.70 train_size
        ( or test_size 0.3), which means 70% of the train dataframe, so 56% of all the data.

        Now we have a train, validate, and test dataframes

    '''
    train, test = train_test_split(df, train_size=0.8, random_state=123, stratify=df[target])
    train, validate = train_test_split(train, train_size = 0.7, random_state = 123, stratify=train[target])
    return train, validate, test

#--------------------------------------------------------------------------------------------------

# Function for Training, Validating, and Testing the data for continious data.
def split_data_continious(df):
    ''' 
        This function is the train, validate, test, function.
        1. First we create the TRAIN and TEST dataframes at an 0.80 train_size( or test_size 0.2).

        2. Second, use the newly created TRAIN dataframe and split that at a 0.70 train_size
        ( or test_size 0.3), which means 70% of the train dataframe, so 56% of all the data.

        Now we have a train, validate, and test dataframes

    '''
    train, test = train_test_split(df, train_size=0.8, random_state=123)
    train, validate = train_test_split(train, train_size = 0.7, random_state = 123)
    return train, validate, test

#--------------------------------------------------------------------------------------------------

# Function for returning scaled data
def get_scaled(train, validate, test):
    
    ''' 
    Creates dummies for FIPS column
    Scales the bedrooms, bathrooms, and sqft columns
    '''

    # Dummies
    scaled_train = pd.get_dummies(train, columns=['fips'])
    scaled_validate = pd.get_dummies(validate, columns=['fips'])
    scaled_test = pd.get_dummies(test, columns=['fips'])

    #Scaler Object
    mm_scaler = MinMaxScaler()

    # Fit the Scaler
    mm_scaler.fit(scaled_train[['bedrooms','bathrooms','sq_ft']])

    # Scaling Train, Validate, and Test
    scaled_train[['bedrooms','bathrooms','sq_ft']]\
        = mm_scaler.transform(scaled_train[['bedrooms','bathrooms','sq_ft']])

    scaled_validate[['bedrooms','bathrooms','sq_ft']]\
        = mm_scaler.transform(scaled_validate[['bedrooms','bathrooms','sq_ft']])

    scaled_test[['bedrooms','bathrooms','sq_ft']]\
        = mm_scaler.transform(scaled_test[['bedrooms','bathrooms','sq_ft']])
    

    return scaled_train, scaled_validate, scaled_test

#--------------------------------------------------------------------------------------------------

def scaled_dummies_base(train, validate, test):

    ''' 
    Creates dummies for FIPS column
    Scales the bedrooms, bathrooms, and sqft columns
    Adds baseline column with the mean of tax value from the train data set
    '''

    # Dummies
    scaled_train = pd.get_dummies(train, columns=['fips'])
    scaled_validate = pd.get_dummies(validate, columns=['fips'])
    scaled_test = pd.get_dummies(test, columns=['fips'])

    #Scaler Object
    mm_scaler = MinMaxScaler()

    # Fit the Scaler
    mm_scaler.fit(scaled_train[['bedrooms','bathrooms','sq_ft']])

    # Scaling Train, Validate, and Test
    scaled_train[['bedrooms','bathrooms','sq_ft']]\
        = mm_scaler.transform(scaled_train[['bedrooms','bathrooms','sq_ft']])

    scaled_validate[['bedrooms','bathrooms','sq_ft']]\
        = mm_scaler.transform(scaled_validate[['bedrooms','bathrooms','sq_ft']])

    scaled_test[['bedrooms','bathrooms','sq_ft']]\
        = mm_scaler.transform(scaled_test[['bedrooms','bathrooms','sq_ft']])

    # Adding Baseline Column
    scaled_train['baseline'] = scaled_train['tax_value'].mean()
    scaled_validate['baseline'] = scaled_train['tax_value'].mean()
    scaled_test['baseline'] = scaled_train['tax_value'].mean()

    return scaled_train, scaled_validate, scaled_test
    
#--------------------------------------------------------------------------------------------------

def xy_trains(train, val, test):

    '''
    Prepares X_train and y_train for modeling. 
    '''

    columns = ['tax_value', 'baseline']
    target = 'tax_value'


    X_train = train.drop(columns, axis=1)
    y_train = train[target]

    X_val = val.drop(columns, axis=1)
    y_val = val[target]

    X_test = test.drop(columns, axis=1)
    y_test = test[target]

    return X_train, y_train, X_val, y_val, X_test, y_test


def drop_outliers(df):

    '''
    Removes outliers. 
    Anything above 99th percentile for: sq_ft, tax_value, bedrooms, bathrooms
    Any homes that have no bedrooms or bathrooms
    '''
    # Dropping anything above 99th percentile for sq_ft and tax_value
    df = df[df['sq_ft'] < 5272]
    df = df[df['tax_value'] < 2146463]

    # Dropping any houses that do not have any bedrooms or bathrooms
    df = df[df['bedrooms'] >= 1]
    df = df[df['bathrooms'] >= 1]

    # Dropping anything above 99th percentile for bedrooms and bathrooms
    df = df[df['bedrooms'] <= 5]
    df = df[df['bathrooms'] <= 5]

    return df

#--------------------------------------------------------------------------------------------------

def pearsonr(df, x, y):

    '''
    Pearson R stats test. 
    '''

    corr , p = stats.pearsonr(df[x], df[y])

    print ('Results')
    print('--------')
    print(f'Correlation: {round(corr,4)}')
    print(f'P-value: {p}')

#--------------------------------------------------------------------------------------------------

def ttest(df):

    '''
    Independent T-test
    '''

    x = df[df['bedrooms'] <= 3]['bedrooms']
    y = df[df['bedrooms'] > 3]['bedrooms']

    t, p = stats.ttest_ind(x, y, equal_var=False)

    print ('Results')
    print('--------')
    print(f'Test statistic: {round(t,4)}')
    print(f'P-value: {p}')

#--------------------------------------------------------------------------------------------------

def ttest2(df):

    t, p = stats.ttest_ind(df['bathrooms'], df['tax_value'], equal_var=False)

    print ('Results')
    print('--------')
    print(f'Test statistic: {round(t,4)}')
    print(f'P-value: {p}')

#--------------------------------------------------------------------------------------------------

def ttest1samp(df):

    '''
    1-Sample T-test
    '''

    oc = df[df['fips'] == 6059]['tax_value']
    overall = df['tax_value']

    t,p = stats.ttest_1samp(oc, overall.mean())

    print ('Results')
    print('--------')
    print(f'Test statistic: {round(t,2)}')
    print(f'P-value: {p}')
