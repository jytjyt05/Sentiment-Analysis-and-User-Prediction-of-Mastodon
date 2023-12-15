# Sentiment Analysis and User Prediction of Mastodon
In this study, we analyzed and investigated the aftereffect of Twitter acquisition. We first use the sentiment analysis model investigate why people leave Twitter. Then we use the SIR compartmental model to model Mastodon users. Finally we use the Long Short-Term Memory(LSTM) model to
predict Mastodon's future user growth trend.


### Sample Data
sample_data directory is the csvs used for sentiment analysis under the twitter directory, the used mastodon data contains the csvs used for our SIR and LSTM models

### Get Tweets
get_Tweets.py is sentiment analysis script

### Mastodon Data and SIR Model
SIR_result.ipynb is the visualization of Mastodon Data used for our SIR and LSTM Models, as well as our implementation of the SIR model

### LSTM Model
lstm_result.py is the script for our lstm model for forecasting user counts of Mastodon
