# config.py
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5433, 
        database="restaurant_db",  
        user="postgres",           
        password="noha"   
    )
    return conn
