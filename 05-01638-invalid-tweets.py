# return ids whose content length > 15
# use col.str.len() to compare length
# o/p only id col

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]

# yahoo- 2
# amazon- 2
# twitter- 1
