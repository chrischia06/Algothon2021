# Instructions

Aspect will provide a list of trades generated from a real production trading strategy, each trade has 3 fields: market / time-on / time-off (market is anonymised) and the pnl for each trade.

The challenge is to use all available market information prior to the trade to forecast the profitability of the trade.
Universe:

Liquid futures on: stock indices, FX, FI, Commodities
Each model should predict the return of each trade and return an action (-1,0,1)

+ 1 means implement the trade
+ 0 means do nothing
+ -1 means implement the opposite of the trade

## Evaluation criteria

The portfolio returns are calculated as the sum of returns for each trade, according to the recommended actions by the model.

We will then score the model using the sharpe ratio of the daily returns over a test period of 2 years.

## Data sources

Any market data up to the point of trade execution. (For example, intraday price of a futures contract, different realized vol estimators, implied volatility, volume etc etc. We don't want to put any constraints here, so use whatever you think your machine learning model will perform best with - time to be creative!).

+ **Train period**: 2006-2015 
+ **Validation period**: 2016-2017 
+ **Test period**: 2018-2019

**Tips**

> Avoid any look-ahead bias (don't use any data observed after the open-timestamp of the trade when predicting the action)

> Be imaginative with the data you use for forecasting. If you can't find any interesting forecasts from pure price data, try looking at volatility

> Make use of Python 3.7 + Tensorflow/Keras (if using neural networks) and include some instructions on how to run the model/reproduce results


>Hi Everyone,

> I hope you enjoyed Algothon Virtual and have managed to recover from the hectic weekend! We are really grateful for everyone for attending. However, we aren't quite finished yet.

> Aspect Capital's Volatility Research Team are running their ML challenge now on the full dataset. You can iterate on previous work, or start fresh if you wish.

> The deadline of Wednesday Midday is a soft deadline, if you are working on the challenge and you need more time please email Darius (cc'ed).

> All submissions will be reviewed manually so please leave clear instructions on how to run the model and reproduce results.
> Please can you also include a brief summary of your approach, a description of the model you're using, any assumptions you've made, which data
you've chosen etc just so we have context when reviewing the code.
> Please can you also download any data the model uses in csv files. External data APIs could be blocked on company machines.
> We use Python 3.7 and Tensorflow 2.4.1 so compatibility with these is preferable.
> If using Jupiter notebooks this is fine, but please also copy the code into a standard python project with a main.py we can run,
as this is much easier for us to integrate into other programs when testing.
> Any graphing/analytics to accompany the model will be beneficial - maybe you could reuse some features from the data-visualisation challenge!
> You can choose to continue working in the same team or continue individually. Each member of a winning team will receive an individual interview.
> Also note that multiple teams can be considered for interview, there doesn't necessarily have to be a single winner for this 🙂.
> The interview format will primarily be going through the code you submit and be quite informal, so be prepared to explain everything in detail!
> The aim of the internship will be to continue work on this model and ultimately deploy something in production and trade real money.
> I have asked the Algosoc team to distribute the full dataset for this next part. We trust you will avoid overfitting, but I think it's a more realistic research
exercise if you can decide your in/out of sample windows yourself.
> Final point: the original challenge specification mentions there's a trade-on timestamp and a trade-off timestamp, but I think there's only a single timestamp in the data files.
You can assume trade-off is 8pm each day (i.e this is a purely intraday strategy; you should never hold a position overnight).
> Please email all submissions to darius.horban@aspectcapital.com and CC team members as appropriate. Could all members of each team also apply to the research summer internship role on the aspect website and submit their CVs through there (for data privacy purposes)

> Please find the full dataset here: https://drive.google.com/drive/folders/17RLKKliRY-j6lQ4UK3rfsoNegxDHHibm

> If you have any questions, please reach out to Darius (cc'ed).

> Please find below the original scores from Algothon Virtual.

> Good luck with this challenge!

> Kind regards,
> Joe