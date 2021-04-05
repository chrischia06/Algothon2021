Note: SEED makes *zero* difference to model results.

---

# Results (no-hold): 
    param = {"num_leaves": 31,
             "objective": "binary",
             "num_round": 100,
             "verbose": -1,
             "seed": SEED})

## df_bond
Baseline train sharpe:  0.08179023515693262
Perfect train sharpe:  0.7124541882221715
train sharpe:  0.08179023515693275 

Baseline val sharpe:  0.011983028953476128
Perfect val sharpe:  0.8731552154143566
val sharpe:  0.011983028953476093 

Baseline test sharpe:  0.0032714647440287253
Perfect test sharpe:  0.5770417322698141
test sharpe:  0.0032714647440287457

## df_commodity
Baseline train sharpe:  0.10371467300400775
Perfect train sharpe:  0.7310770453037599
train sharpe:  0.13598793195863543 

Baseline val sharpe:  0.15829374235509622
Perfect val sharpe:  0.6745630579162148
val sharpe:  0.1489511289738109 

Baseline test sharpe:  0.0663774384877751
Perfect test sharpe:  0.7438510748987713
test sharpe:  0.10059105583250462

## df_currency
Baseline train sharpe:  0.05494746035891692
Perfect train sharpe:  0.729361247117214
train sharpe:  0.17751690078628754 

Baseline val sharpe:  -0.0019637180414150317
Perfect val sharpe:  0.596631212891202
val sharpe:  -0.024771611271621977 

Baseline test sharpe:  0.08538884320257148
Perfect test sharpe:  0.681285774023595
test sharpe:  0.05372424792299037

## df_stock

Baseline train sharpe:  0.10549310812809065
Perfect train sharpe:  0.676719455441265
train sharpe:  0.43789093377661464 

Baseline val sharpe:  0.1605220275034702
Perfect val sharpe:  0.877015328149025
val sharpe:  0.29974025909627877 

Baseline test sharpe:  0.13435442363038896
Perfect test sharpe:  0.5444696857905135
test sharpe:  0.23809603653985362  

---

# Results (long-only): 
    param = {"num_leaves": 31,
             "objective": "binary",
             "num_round": 100,
             "verbose": -1,
             "seed": SEED})

## df_bond
Baseline train sharpe:  0.08179023515693262
Perfect train sharpe:  0.7124541882221715
train sharpe:  0.08179023515693275 

Baseline val sharpe:  0.011983028953476128
Perfect val sharpe:  0.8731552154143566
val sharpe:  0.011983028953476093 

Baseline test sharpe:  0.0032714647440287253
Perfect test sharpe:  0.5770417322698141
test sharpe:  0.0032714647440287457

## df_commodity
Baseline train sharpe:  0.10371467300400775
Perfect train sharpe:  0.7310770453037599
train sharpe:  0.12524902621317133 

Baseline val sharpe:  0.15829374235509622
Perfect val sharpe:  0.6745630579162148
val sharpe:  0.1543979564947507 

Baseline test sharpe:  0.0663774384877751
Perfect test sharpe:  0.7438510748987713
test sharpe:  0.08882281296486302

## df_currency
Baseline train sharpe:  0.05494746035891692
Perfect train sharpe:  0.729361247117214
train sharpe:  0.16451663994323723 

Baseline val sharpe:  -0.0019637180414150317
Perfect val sharpe:  0.596631212891202
val sharpe:  -0.026587639241008924 

Baseline test sharpe:  0.08538884320257148
Perfect test sharpe:  0.681285774023595
test sharpe:  -0.02695018778243508

## df_stock

Baseline train sharpe:  0.10549310812809065,
Perfect train sharpe:  0.676719455441265,
train sharpe:  0.3176381257824255 

Baseline val sharpe:  0.1605220275034702,
Perfect val sharpe:  0.877015328149025,
val sharpe:  0.2842914453342108 

Baseline test sharpe:  0.13435442363038896,
Perfect test sharpe:  0.5444696857905135,
test sharpe:  0.2301397819735817 

---

+ bond_model buys all the time. Perhaps there's some outliers affecting the data?

+ Results for df_stock are pretty decent! 

+ For all models except the stock model, binary_logloss increases during training.