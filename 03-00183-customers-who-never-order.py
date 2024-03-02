# '~' is used to negate the logic
# first, pull everything from orders, then negate it
# then pull only name and rename the column

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    not_in_orders = customers[~customers['id'].isin(orders['customerId'])]
    return not_in_orders[['name']].rename(columns = {'name' : 'Customers'})

#   OR
#   all in a single line
    return customers[~customers['id'].isin(orders['customerId'])][['name']].rename(columns = {'name' : 'Customers'})

# amazon- 3
# apple- 7
# bloomberg- 5
# adobe- 2
