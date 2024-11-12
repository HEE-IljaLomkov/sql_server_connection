import pandas as pd
from src import PRIVATE, ssms_connection

if __name__ == '__main__':
    database_name = ""
    database_table = ""

    df = ssms_connection.Load_SSMS_Data(
        server=PRIVATE.SERVER,
        username=PRIVATE.USERNAME,
        database_name=database_name,
        database_table=database_table
    )

    print(df)
