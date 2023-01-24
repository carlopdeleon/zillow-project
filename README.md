# Zillow Project

# Project Description

### The Zillow Data Science Team is reaching out to data scientists around the nation in order to find the best and most optimized machine learning model that can predict a home's value. The homes that will be used for this process will be Single Family properties that were sold in 2017. These homes are located in three California counties: Los Angeles County, Orange County, Ventura County


# Business Goals

* Uncover drivers that influence a home's value
* Use machine learning algorythms with drivers to accurately predict a future home's value
* Develop an understanding on how the drivers influence a home's value

# Initial Thoughts

### My initial hypothesis is that a home's value is heavily influenced by its living area (square feet),  number of bedrooms, and number of bathrooms.

# The Plan

* Acquire data from Sequel Ace DB

* Prepare Data
    - Data processed for investingating:
    - Dropped 32 rows of duplicated data. About 0.05% of data
    - Dropped 557 rows that had missing data. About 1.0% of data.
    - Dropped year built column. Not being targreted as a driver.
    - Dropped tax amount column. Correlation value is too high. Would negatively impact model performance.
    - Dropped outliers:
        - Homes over 99th percentile in square feet, tax value, bedrooms, and bathrooms
        - Dropped any homes that were listed with 0 bedrooms or 0 bathrooms.
    - Created new column using existing data
        - FIPS
    - Create a train, validate, and test dataset with a split of about 56/24/20.
    
* Explore Data and uncover drivers
    - Is a home's value influenced by it's square feet?
    - Is a home's value influenced by the number of bedrooms it has?
    - Is a home's value influenced by the number of bathrooms it has?
    - Is a home's value influenced by its FIPS code?
 
* Develop machine learning models
    - Utilize drivers in various machine learning models
    - Evaluate and refine models on train and validate data sets
    - Select best performing models
    - Use test data set on best models


# Data Dictionary

| Feature | Definition |
| :-- | :-- |
| bedrooms | number of bedrooms |
| bathrooms | number of bathrooms |
| sq_ft | total square footage of home's living area<br>living area does not include basements, garages, or yards|
| tax_value | the house property value in USD | 
| fips | Federal Information Processing System<br>- fips 6037: Los Angeles County<br>- fips 6059: Orange County<br>- fips 6111: Ventura County |

# Steps to Reproduce

1. Clone this repo.
2. To acquire data, use your own env.py file to access MySql database and download data
3. Use functions in acquire.py to upload data
4. Use functions in prepare.py to clean and prep data.
5. Use functions in visual.py to plot the charts.
5. Use same configurations for models.
6. Use functions in evaluate.py to evaluate models.

# Conclusions

* Square feet, bedrooms, bathrooms, and fips were all considred drivers of tax value.
* For square feet, highest density of homes ranged from 1000-4000 sq. ft. with around 100k - 1.5mil dollars.
* For bedrooms, tax value increased as number of bedrooms increased.
* For bathrooms, tax value increased as number of bathrooms increased. Adding a half bath(powder room) drastically increased a home's tax value.
* For FIPS, depending on the county(fips code), a home's average price would be lower or higher. Orange County had the highest average, LA county had the second highest, and Ventura county had the lowest. 

# Recommendations

- I would recommending filling in missing data to minimize the need to drop rows.
- With more time given, I would explore how a home's lot size influences its value.
- I would also look into how a home's value is influence by the year it was built.




