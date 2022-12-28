import pymysql
from src.helpers.config_helpers import get_database_credentials
from src.configs.generic_configs import GenericConfigs

def read_from_db(sql):
    # connect to db
    db_credentials = get_database_credentials()
    connection = pymysql.connect(host=db_credentials['db_host'], port=db_credentials['db_port'],
                                user=db_credentials['db_user'], password=db_credentials['db_password'])

    # read from db
    try: 
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    # return the result
    return db_data

def get_order_from_db_by_order_nr(order_nr):
    schema = GenericConfigs.DATABASE_SCHEMA
    table_prefix = GenericConfigs.DATABASE_TABLE_PREFIX
    sql = f"SELECT * FROM {schema}.{table_prefix}posts WHERE ID = {order_nr} AND post_type = 'shop_order';"
    db_order = read_from_db(sql)
    return db_order

# get_order_from_db_by_order_nr(77)