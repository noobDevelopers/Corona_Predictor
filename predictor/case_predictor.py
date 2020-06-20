import numpy as np
from datetime import datetime
def case_predictor(X):
    X = datetime.strptime(X, '%d/%m/%y')
    initial = datetime.strptime("30/01/20", '%d/%m/%y')
    X = (X-initial).days
    X = np.array([X])
    degree = 3
    out = np.zeros((X.shape[0],degree))
    for i in range(1,degree+1):
        out[:,i-1:i] = X**i
    
    x = out
    m = x.shape[0]
    on = np.ones((1,m))
    x = np.insert(x,0,on,axis=1)
    theta = np.array([[24.262031234015],[4.66632403328913],[-0.496408253816668],[0.00796655882799757]])
    ans = x@theta
    ans = round(ans[0,0])
    if ans < 0:
        ans = 0
    return f'Number of new Cases on this day:{ans}'

def death_predictor(X):
    X = datetime.strptime(X, '%d/%m/%y')
    initial = datetime.strptime("30/01/20", '%d/%m/%y')
    X = (X-initial).days
    X = np.array([X])
    degree = 2
    out = np.zeros((X.shape[0],degree))
    for i in range(1,degree+1):
        out[:,i-1:i] = X**i
    
    x = out
    m = x.shape[0]
    on = np.ones((1,m))
    x = np.insert(x,0,on,axis=1)
    theta = np.array([[40.3332349531563],[-3.77721926343234],[0.0470834667089071]])
    ans = x@theta
    ans = round(ans[0,0])
    if ans < 0:
        ans = 0
    return f'Number of Deaths on this day:{ans}'

def cured_predictor(X):
    X = datetime.strptime(X, '%d/%m/%y')
    initial = datetime.strptime("30/01/20", '%d/%m/%y')
    X = (X-initial).days
    X = np.array([X])
    degree = 3
    out = np.zeros((X.shape[0],degree))
    for i in range(1,degree+1):
        out[:,i-1:i] = X**i
    
    x = out
    m = x.shape[0]
    on = np.ones((1,m))
    x = np.insert(x,0,on,axis=1)
    theta = np.array([[-8.06484116e+01],[2.36212767e+01],[-8.78433085e-01],[8.07076317e-03]])
    ans = x@theta
    ans = round(ans[0,0])
    if ans < 0:
        ans = 0
    return f'Number of Patients Cured on this day:{ans}'

print(cured_predictor('19/06/20'))