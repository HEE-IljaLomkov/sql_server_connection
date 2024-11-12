import sqlalchemy
import pandas as pd

def Load_SSMS_Data(server: str, username: str, database: str, sql_query: str) -> pd.DataFrame:
    """
    Function to connect to SQL Server Management Studio (SSMS).
    Call this function when needing to connect to a new database.
    INPUTS:
        - server (type: string). Declare the SQL server to connect to.
        - username (type: string). Declare the login username.
        - database (type: string). Declare the name of the database to load data from.
        - database_table (type: string). Declare the login username.
        - sql_query (type: string). Declare the SQL query to load the table with.
    OUTPUTS:
        - dataframe (type: Pandas dataframe object).
    """

    AUTH_METHOD = "ActiveDirectoryInteractive"
    SQL_DRIVER = "{ODBC Driver 17 for SQL Server}"

    # https://stackoverflow.com/q/66751640
    # https://learn.microsoft.com/en-us/sql/connect/odbc/using-azure-active-directory?view=sql-server-2017#new-andor-modified-dsn-and-connection-string-keywords
    CONNECTION_STRING = (
        f"DRIVER={SQL_DRIVER};" +
        f"SERVER={server};" +
        f"DATABASE={database};" +
        f"UID={username};" +
        f"AUTHENTICATION={AUTH_METHOD}"
    )

    connection_url = sqlalchemy.engine.URL.create("mssql+pyodbc", query={"odbc_connect":CONNECTION_STRING})

    engine = sqlalchemy.create_engine(connection_url)

    with engine.connect() as connection:
        df = pd.read_sql(sql_query, connection)

    return (df)
