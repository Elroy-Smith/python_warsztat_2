from psycopg2 import connect

import config


def connection(database):
    cnx = connect(user=config.user,
                  password=config.password,
                  host=config.host,
                  database=database)
    cnx.autocommit = True
    return cnx
