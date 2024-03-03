# return tweetids where content length > 15
# use col.str.len()

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]

# yahoo- 3
# amazon- 2
# twitter- 1
