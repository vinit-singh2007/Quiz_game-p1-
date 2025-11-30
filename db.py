import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()   

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),  # password hidden
        database="quiz_game"
    )

def save_score_mysql(name, score):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO scores (name, score) VALUES (%s, %s)"
    values = (name, score)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
