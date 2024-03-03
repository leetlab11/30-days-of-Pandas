# first, filter rows
# pull only required column
# rename the col
# remove duplicates from the col
# sort the col

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    return views[(views['author_id'] == views['viewer_id'])][['author_id']].rename(columns = {'author_id' : 'id'}).drop_duplicates().sort_values(by = ['id'])

#   OR
#   first, filter rows
#   sort values by author_id
#   rename that col
#   pull only that col
#   remove duplicates
  
    return views[(views['author_id'] == views['viewer_id'])].sort_values(by = ['author_id']).rename(columns = {'author_id' : 'id'})[['id']].drop_duplicates()
  
  
# bloomberg- 4
# amazon- 3
# adobe- 2
# yahoo- 4
# google- 3
# uber- 2
# apple- 2
# liniedin- 1


