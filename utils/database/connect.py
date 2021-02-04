import os
import psycopg2


def get_conn_and_cur():
    DATABASE_URL = os.environ["DATABASE_URL"]

    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cur = conn.cursor()
    return conn, cur
