# unpivot- use pd.melt()
# no null values needed in o/p so dropna()

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(products, id_vars = 'product_id', var_name = 'store', value_name = 'price').dropna()

# bloomberg- 2
# apple- 2
# amazon- 1
