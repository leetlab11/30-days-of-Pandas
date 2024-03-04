# question asks to delete duplicates in place and not return any value
# we sort the table because we want to keep the email with smappest id
# sorting will bring smallest id before larger ids
# then we drop duplicates and keep the first values

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by = 'id', inplace = True)
    person.drop_duplicates(subset = 'email', keep = 'first', inplace = True)


# apple- 2
# oracle- 2
# amazon- 6
# uber- 2
