## LOB market recreation using ODE RNN

This project aims to reproduce the top 5 level of the Limit Order Book market at anytime, using only the information about the top price and the trades. It implements a deep learning method from [Zijian Shi, Yu Chen, John Cartlidge](https://arxiv.org/abs/2103.01670).

## How to run

TODO

## Model used to predict it

[Zijian Shi, Yu Chen, John Cartlidge](https://arxiv.org/abs/2103.01670)

TODO

## Results

TODO

## Limitations

This method assumes that the prices at the top of the order book are densely distributed. Mathematically that means that the difference between the prices of two consecutive levels at the top of the LOB is equal to the tick size.

However this does not seem to be the case for the `AMZN` dataset from [Lobster](https://lobsterdata.com/info/DataSamples.php) so the dataset used in this repos is the `INTC` one where this assumption holds.