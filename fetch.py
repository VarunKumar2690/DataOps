#pip install snowflake-connector-python
#Import the Snowflake Connector for Python
import snowflake.connector

# Set up Snowflake connection parameters
account = 'ml81433.central-india.azure'
user = 'VKUMAR50'
password = 'Gautam@2690'
database = 'DW_REFINED_PRD'
warehouse = 'COMPUTE_WH'

# Create a Snowflake connection
conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    database=database,
    warehouse=warehouse
)

# Execute a Snowflake query
cursor = conn.cursor()
# cursor.execute('USE WAREHOUSE ')
cursor.execute('SELECT * FROM DW_REFINED_PRD.MY_SCHEMA.CUSTOMERS')
result = cursor.fetchall()
print(result)

# Process the query result
# ... (perform your desired operations on the query result)

# Close the Snowflake connection
conn.close()

