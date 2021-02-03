import psycopg2


def get_conn_and_cur():
    host = "postgres://iglwjbwrhnmhev:4f289a07ddcc5452f9a785f89a769c3817661465a15e46e733f8c2bba78518fe@ec2-52-72-162-207.compute-1.amazonaws.com:5432/d8ek2he65l0bdh"
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
