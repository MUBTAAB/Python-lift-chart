def create_lift(outcome, model_proba, precision = 2, vis = False):
    """
    Returns series with the lift of the model. You may plot the results.
    
    Prequisites:
    - Numpy
    - Pandas
    - Matplotlib (for visualisation)
    
    Parameters:
    - outcome: List or array containing the fact target variable
    - model_proba: List or array containing the probability estimates of our model
    - precision: Number of decimal places to round to
    - vis: Display the resulting lift chart on a basic plt plot
    
    """
    import pandas as pd
    import numpy as np
    
    df_pred = pd.DataFrame({'outcome':outcome, 'model_proba':model_proba})
    df_pred['model_proba_pct'] = df_pred['model_proba'].rank(pct=True).round(precision)
    avgoutcome = np.mean(df_pred['outcome'])
    df_grp = df_pred.groupby('model_proba_pct')['outcome'].agg(['sum','count'])
    df_grp = df_grp.sort_index(ascending = False)
    
    df_grp['rate'] = (df_grp['sum'].cumsum()/df_grp['count'].cumsum())/avgoutcome
    
    if vis == True:
        import matplotlib.pyplot as plt
        plt.figure(figsize = (10,7.5))
        plt.plot(df_grp['rate'], linewidth = 3)
        df_grp['ref'] = 1
        plt.plot(df_grp['ref'], '--', linewidth = 3)
        plt.gca().invert_xaxis()
        plt.ylabel('Lift')
        plt.xlabel('Percentile of probability')
        plt.title('Lift Chart')
        plt.show()
    
    return(df_grp['rate'])
