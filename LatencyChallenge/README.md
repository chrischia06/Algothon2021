# Algothon_TeamTBA

This is the github repo for TeamTBA during the Algothon 

Contains of a barebones classifier that predicts whether the next step log-return is positive $r_{t + 1} > 0$ based on the 500 previous log-returns $r_{t} , \ldots, r_{t - 499}$

+ `train_latency_classifier.py` - trains a Logistic Regression model on provided data `data/LatencyTraining.csv`
+ `latency_logit.joblib` - output of `train_latency_classifier.py`
+ `latency_predict.py` - import the classifier and use it to run predictions from command line

**Usage**

Run `make run`. For each line (observation), 500 numbers delimited by commas is expected; A prediction of 0 or 1 is returned for each line

**Tests**

To test, run `time make run < test_case{i}.txt` for the numpy version, and `time python latency_predict_old.py < test_case{i}.txt`

+ `test_case1.txt` - single line of input
+ `test_case2.txt` - multiple lines of input
+ `test_case3.txt` - original training data `LatencyTraining.csv`

**Benchmark**

*for 1 iteration of `time`*

| Method | test case | real | user | sys| n |
| -- | -- | -- | -- | -- | -- |
| weights only | test_case 1 | 0.287s |0.303s |0.067s | 1 | 
| weights only | test_case 2 | 0.237s | 0.283s | 0.053s | 5 |
| weights only | test_case 3 | 1.029s | 0.769s | 0.160s| 1328 |
| sklearn | test_case 1 | 0.815s | 0.843s | 0.150s| 1 | 
| sklearn | test_case 3 | 1.118s |0.907s |0.219s | 5 |
| sklearn | test_case 3 | |1.531s |1.409s |0.182s | 1328 |



