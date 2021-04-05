"""

"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from joblib import dump, load

if __name__ == '__main__':
	# Read Data
	df = pd.read_csv(f"data/LatencyTraining.csv").iloc[:,1]
	temp = pd.DataFrame(df.copy())

	# Add Lags and create features and targets
	LAGS = 500
	for i in range(LAGS - 1):
	  temp2 = pd.DataFrame(df.shift(i + 1))
	  temp2.columns = [f'LogReturns_tm{i + 1}']
	  temp = pd.concat([temp, temp2],axis=1)

	X, y = temp.iloc[LAGS - 1:-1], df.shift(-1).iloc[LAGS-1:-1]
	X.to_csv("train.csv",index=False)
	y.to_csv("train_targets.csv",index=False)
	logit = LogisticRegression().fit(X, y > 0)
	print(",".join(map(str, logit.coef_[0])), logit.intercept_)
	dump(logit, 'latency_logit.joblib') 

