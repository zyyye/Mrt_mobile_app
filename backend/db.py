import sqlite3
from datetime import datetime

DB_NAME = "trips.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_station TEXT,
        end_station TEXT,
        fare REAL,
        distance REAL,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_trip(start, end, fare, distance):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO trips (start_station, end_station, fare, distance, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (start, end, fare, distance, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def get_trips_30_days():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM trips
    WHERE timestamp >= datetime('now', '-30 days')
    ORDER BY timestamp DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows