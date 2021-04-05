import numpy as np
import pandas as pd
import yfinance as yf
import quandl
import lightgbm as lgb

from numpy import random
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from datetime import datetime, timedelta

import warnings
warnings.filterwarnings('ignore')

assets = ['bond_1', 'bond_2', 'commodity_1', 'commodity_2', 'currency_1', 
          'currency_2', 'stock_1', 'stock_2']

def preprocess(df2):
    # Create a categorical variable representing trade entry time 
    # (equivalently, trade duration)
    # apply inplace
    df = df2.copy()
    df['Entry'] = df["Position_Open"].apply(lambda x: x.split()[1])
    le = LabelEncoder()
    df['Entry'] = le.fit_transform(df['Entry'])
    df = df.drop(['Position_Close'], axis=1)

    #Remove %H:%M:%S component, to allow merging with external data later
    df['Position_Open'] = df["Position_Open"].apply(lambda x: x.split()[0])
    #Convert date into categorical features
    df['Position_Open'] = pd.to_datetime(df["Position_Open"])
    df["Year"] = df["Position_Open"].dt.year 
    df["Month"] = df["Position_Open"].dt.month
    df["Day"] = df["Position_Open"].dt.day

    df = df.rename({"Position_Open": "Date"}, axis = 1)
    return df

def get_quandl_data(symbols, key, path):
    # collect data from Quandl
    quandl.ApiConfig.api_key = key
    dfs = {}
    for x in symbols:
      temp = quandl.get(x[1])
      try:
        temp = temp[['Volume', 'Previous Day Open Interest','Open']]
      except:
        temp = temp[['Volume', 'Prev. Day Open Interest','Open']]
      temp['Volume'] = temp['Volume'].shift(1) 
      temp.columns = [f"{x[0]}-{c}" for c in temp.columns]
      
      dfs[x[0]] = temp
      dfs[x[0]].to_csv(f"{path}/{x[0]}.csv", index=True)
    return dfs

def get_y_finance_feats(tickers, path):
    # collect data from yfinance
    dfs = {}
    # VIX, SP500 from yahoo finance
    for x in tickers:
        dfs[x] = yf.Ticker(x).history(interval = '1d', start=datetime(2005, 1, 11), end=datetime(2021, 3, 31))
        dfs[x]['Close'] = dfs[x]['Close'].shift(1)
        dfs[x]['Rets'] = np.log(dfs[x]['Open']/dfs[x]['Close'])
        dfs[x] = dfs[x][['Open','Close','Rets']]
        dfs[x].columns=[f"{x}-{y}" for y in dfs[x].columns]
        dfs[x].to_csv(f"{path}/{x}.csv", index=True)
    return dfs

def split(df, drop_feats, train_start = 2006, train_end = 2015, val_start = 2016, 
    val_end = 2017, test_start = 2018, test_end =2019):
    #Split training set to evaluate model
    train = df[(df['Year'] >= train_start) & (df['Year'] <= train_end)].sort_values(by='Date')
    val = df[(df['Year'] >= val_start) & (df['Year'] <= val_end)].sort_values(by='Date')
    test = df[(df['Year'] >= test_start) & (df['Year'] <= test_end)].sort_values(by='Date')

    X_train, y_train = train.drop(drop_feats, axis= 1), train['Return']
    X_val, y_val = val.drop(drop_feats, axis= 1), val['Return']
    X_test, y_test = test.drop(drop_feats, axis= 1), test['Return']

    print(X_train.shape, y_train.shape)
    print(X_val.shape, y_val.shape)
    print(X_test.shape, y_test.shape, "\n")

    return (X_train, X_val, X_test, 
            y_train, y_val, y_test,
            train.index, val.index, test.index
            )

def split_by_asset(df):
    #Split dataframe by asset type
    df_bond = df.loc[df['Market'].isin(['bond_1', 'bond_2'])].copy()
    df_commodity = df.loc[df['Market'].isin(['commodity_1', 'commodity_2'])].copy()
    df_currency = df.loc[df['Market'].isin(['currency_1', 'currency_2'])].copy()
    df_stock = df.loc[df['Market'].isin(['stock_1', 'stock_2'])].copy()

    #Convert 'Market' into a categorical variable so it can be used as a feature
    convert_label = lambda x: 1 if x.endswith('1') else 2
    df_stock['Market'] = df_stock['Market'].apply(convert_label)
    df_currency['Market'] = df_currency['Market'].apply(convert_label)
    df_bond['Market'] = df_bond['Market'].apply(convert_label)
    df_commodity['Market'] = df_commodity['Market'].apply(convert_label)
    return df_bond, df_commodity, df_currency, df_bond
  

def long_only_sharpe(returns, predictions):  
    actions = []
    for i in range(len(returns)):
      if predictions[i] == 1:
        actions.append(returns[i])
      elif predictions[i] == -1:
        actions.append(-returns[i])
      else:
        actions.append(0)

    return sharpe(actions)


def no_hold_sharpe(returns, predictions):  
  #1 = long, 0 = short
  actions = []
  for i in range(len(returns)):
    if predictions[i] == 1:
        actions.append(returns[i])
    elif predictions[i] == 0:
        actions.append(-returns[i])
    else:
        actions.append(0)

  return sharpe(actions)

if __name__ == '__main__':
    assets = ['bond_1', 'bond_2', 'commodity_1', 'commodity_2', 'currency_1', 
              'currency_2', 'stock_1', 'stock_2']
    symbols = [("-TBond Futures", "CHRIS/CME_US1"), ("Crude Futures", "CHRIS/CME_CL1"), 
               ("Gold Futures", "CHRIS/CME_CL2"), ("USD Futures", "CHRIS/ICE_DX1"), 
               ("SP500 Futures","CHRIS/CME_SP1")]
    tickers = ["^VIX", "^GSPC","^FTSE"]

    #### join all provided data ####
    print("Joining all Data (Trade Returns)")
    df = pd.DataFrame()
    path = "data"
    for a in assets:
      try:
        temp = pd.read_csv(f"{path}/{a}.csv")
      except:
        try:
          temp = pd.read_csv(f"{a}.csv")
        except:
          pass
      if temp.shape[0] != 0: #if temp is non-empty
        try:
          df = pd.concat([df, temp], axis=0)
        except:
          print("Some error")

    df3 = preprocess(df)

    #### Comment these lines if running locally. ####
    # quandl_dfs = get_quandl_data(symbols, "pkLbjb4QQUmszgP48_jC", path)
    # dfs = get_y_finance_feats(tickers, path)

    #### Read in saved data, rather than using API ####
    print("Joining all Data (Exogenous Variables)")
    quandl_dfs = {}
    yf_dfs = {}
    for x in symbols:
        quandl_dfs[x[0]] = pd.read_csv(f"{path}/{x[0]}.csv")
    for x in tickers:
        yf_dfs[x[0]] = pd.read_csv(f"{path}/{x}.csv")

    us10yr = pd.read_csv(f"{path}/US 10 YR T-Note Futures Historical Data.csv")
    us10yr['Date'] = pd.to_datetime(us10yr["Date"])
    us10yr = us10yr[['Date','Open']]
    us10yr.columns = ["Date","US10Yr-Open"]

    df2  = df3.copy()
    for x in yf_dfs:
        yf_dfs[x]['Date'] = pd.to_datetime(yf_dfs[x]['Date'])
        df2 = pd.merge(df2, yf_dfs[x], on ='Date', how='left')

    for x in quandl_dfs:
        quandl_dfs[x]['Date'] = pd.to_datetime(quandl_dfs[x]['Date'])
        df2 = pd.merge(df2, quandl_dfs[x], on ='Date', how='left')

    df2 = pd.merge(df2, us10yr, how='left',on='Date')

    cat_feats =['Market']
    df2[cat_feats]  = df2[cat_feats].astype("category")

    #### Define Metrics and Position Sizing ####
    print("Training LGBM model")
    sharpe = lambda x: np.mean(x / np.std(x))
    # position sizing strategies
    identity = lambda p: p
    ls_pos = lambda p: 2 * p - 1 # scale prediction p so that it is between [-1, 1]
    hard_l = lambda p: p > 0.5 # hard boundary, so the signal is either [0, 1]
    hard_ls = lambda p: np.rint(2 * (p > 0.5) - 1) # hard boundary, the signal is either -1, 1

    drop_feats = ['Date','Year','Return']
    X_train, X_val, X_test, y_train, y_val, y_test, train_ind, val_ind, test_ind = split(df2, drop_feats = drop_feats)

    ### LightGBM Model ###
    train_data = lgb.Dataset(X_train, label = y_train > 0, categorical_feature = ['Market','Entry','Month','Day'])
    val_data = lgb.Dataset(X_val, label = y_val > 0,categorical_feature = ['Market','Entry','Month','Day'])

    SEED = random.randint(0, 999999)
    print("SEED", SEED, "\n")

    param = {"num_leaves": 64,
               "max_depth":8,
               "objective": "binary",
               "num_round": 500,
               "verbose": -1,
             "early_stopping_rounds":20,
               "seed": SEED}

    evals_result = {}
    bst = lgb.train(param, train_data, valid_sets=[val_data],evals_result=evals_result,verbose_eval=False)

    train_preds = bst.predict(X_train)
    val_preds = bst.predict(X_val)
    test_preds = bst.predict(X_test)

    #### Write Backtest Results ####
    print("Results")
    try:
        results = pd.read_csv(f"{path}/backtest_log.csv")
    except:
        baseline = [sharpe(y_train), sharpe(y_val), sharpe(y_test), 'always long']
        perfect = [sharpe(abs(y_train)), sharpe(abs(y_val)), sharpe(abs(y_test)), 'perfect sharpe']
        results = pd.DataFrame([baseline, perfect], columns=['train_sharpe','val_sharpe','test_sharpe','description'])

    for description, f in zip(["LGB Classification (probability)", "LGB Classification (2x - 1 scaling)", 
                  "LGB Hard Classification Long-only", "LGB Hard Classification Long-Short"], 
                 [identity, ls_pos, hard_l, hard_ls]):
      
        temp = pd.DataFrame([[sharpe(f(train_preds) * y_train), sharpe(f(val_preds) * y_val), 
                         sharpe(f(test_preds) * y_test), description, str(param)]])
        temp.columns = ['train_sharpe','val_sharpe','test_sharpe','description', 'hyperparameters']
        results = pd.concat([results, temp], axis = 0)

    results = results.drop_duplicates(subset=['train_sharpe','test_sharpe','val_sharpe'])
    results.to_csv(f"{path}/backtest_log.csv", index=False)
    print(f"See {path}/backtest_log.csv for backtest results")

    ### Example of how to create test predictions ####
    performance = df2.iloc[test_ind][['Date','Market','Return']]
    performance['prediction'] = bst.predict(df2.iloc[test_ind].drop(drop_feats, axis = 1))
    performance.to_csv(f"{path}/test_preds.csv")


