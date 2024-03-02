# filter using 'OR'- '|'

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
   return world[(world.area >= 3000000) | (world.population >= 25000000)][['name', 'population', 'area']]

# amazon- 2
# apple- 4
# google- 3
# bloomberg- 2
# adobe- 4
# facebook- 3
# yahoo- 3
