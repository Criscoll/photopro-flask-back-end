import os
import psycopg2


def get_conn_and_cur():
    host = os.environ["DATABASE_URL"]
    database_user = "cristiand2021@gmail.com"
    database_password = "Mella*Comy12"
    database_name = "DATABASE_URL"

    conn = psycopg2.connect(
        user=database_user,
        password=database_password,
        host=host,
        database=database_name,
    )
    cur = conn.cursor()
    return conn, cur
