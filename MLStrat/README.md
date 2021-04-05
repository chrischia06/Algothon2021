# Algothon 2021 - Machine Learning Strategy

For : [http://www.algothon.org/challenges.html](http://www.algothon.org/challenges.html)

Joint work between [Sanjit Neelam](https://github.com/sanj909), and [Chris Chia](https://github.com/chrischia06/)

## Running the script

First, install all the required packages by running `python3 -m pip install requirements.txt`. A script version of the strategy is provided as a file `ml_strat.py` here [here](ml_strat.py). A Jupyter Notebook `MLStratChallenge-Final.ipynb` is also provided [here](MLStratChallenge-Final.ipynb), and an online version as a Google Colab notebook is available here: [https://colab.research.google.com/drive/12fW0fXCSq7FMYfiaCoxUtUP5gYEudPZr](https://colab.research.google.com/drive/12fW0fXCSq7FMYfiaCoxUtUP5gYEudPZr).

The Jupyter Notebook / Google Colab versions are more interactive; they contain relevant visualisations and discussion as to the strategy and model. A sample of the results can be seen in either `MLStratChallenge-Final.html` or `MLStratChallenge-Final.pdf`. 

The script produces an output file `test_preds.csv`, but to obtain the relevant predictions for your desired test period, some edits to the script will be required.




## Data
May require downloading the data the organisers have provided ,[here](https://drive.google.com/drive/folders/180FaVThDIFtmrCZ2cGiYskvlyvyMv5Au), and adjusting the code in the notebook to account for your own path. We include several exogenous variables, obtained via the *Quandl API* and `yfinance` library, which are primarily futures and equity indices data. We have also included some sample data in the `data/` folder.


## Modelling

`MLStratChallenge.ipynb` contains the code for the strategy. We use Gradient boosted trees, specifically the LightGBM package `lightgbm` as a model to predict the *sign* of the trade returns, i.e. whether a trade will be profitable (assuming returns include transaction costs). 

We explore various position sizing strategies based on the prediction - hard classification 0/1 from the LGB prediction, scaling the prediction to be between [-1, 1] as well.





