# filter using 'AND'- '&'

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products.low_fats == 'Y') & (products.recyclable == 'Y')][['product_id']]

# amazon- 17
# google- 7
# adobe- 5
# facebook- 3
# apple- 3
# microsoft- 3
# bloomberg- 2
# yahoo- 2
