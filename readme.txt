The main.py file contains the graphs made for the intial analysis
    #debugging and new information 1
        that segment showed that within the churned people there was a age group completly cut out  
        meaning that one age group was not representated within the churned population but was evident within the nonchurned population

logistic.py is the logistic regression file. 

Independent observations: Each data point is assumed to be independent of the others means there should be no correlation or dependence between the input samples.
Binary dependent variables: It takes the assumption that the dependent variable must be binary, means it can take only two values. For more than two categories SoftMax functions are used.
Linearity relationship between independent variables and log odds: The model assumes a linear relationship between the independent variables and the log odds of the dependent variable which means the predictors affect the log odds in a linear way.
No outliers: The dataset should not contain extreme outliers as they can distort the estimation of the logistic regression coefficients.
Large sample size: It requires a sufficiently large sample size to produce reliable and stable results.

dataMath.py 
contains the data cleaning through z-score normalization and removal of the redundant column age
then creates the cleaned churn(containing only the churn values) and the cleanedNonC contains the cleaned data 

T 