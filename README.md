# Python-lift-chart
I couldn't find any python scirpts or modules to create and plot a simple lift chart (not to be confused with the ROC chart). So I made one using pandas, numpy and matplotlib.

## Prequisites
- Numpy
- Pandas
- Matplotlib (for visualisation)
    
## Parameters
- outcome: List or array containing the fact target variable
- model_proba: List or array containing the probability estimates of our model
- precision: Number of decimal places to round to
- vis: Display the resulting lift chart on a basic plt plot

## Resulting graph
![alt tag](https://imgur.com/a/5RVS5)

## On lift charts
https://en.wikipedia.org/wiki/Lift_(data_mining)
