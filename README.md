# ```Setup```
### VPN
Do not forget to connect to the VPN.

### Libraries
The following libraries are required, and can be installed using conda, or pip.

```conda install <package_name>```:

##### 1.) ```pandas```

##### 2.) ```sqlalchemy```

It is recommended to create a new Conda environment, and install these packages there.

### Configuration
Prior to execution, the Python script must be configured.

The following must be modified in the PRIVATE.py Python file:

#### 1.) ```SERVER```

This is the connection address of the SQL Server.

#### 2.) ```USERNAME```

This is the username that is used to connect to the SQL Server - typically the user's email address.

The following must be modified in the sql_server_connection.ipynb file:

#### 1.) ```database_name```

This is the name of the database to connect to.

#### 2.) ```database_table```

This is the name of the table to connect to.

#### 3.) ```sql_query```

This is the SQL Query to query the database with.

# ```Limitations```
SQLAlchemy does not support the creation of Local, or Global, temporary tables.

