import os

import sqlite3

DATABASE_NAME = "/data/lost_found.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            location TEXT NOT NULL,
            report_type TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open',
            contact TEXT NOT NULL,
            date_reported TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def insert_item(item_name, description, category, location, report_type, contact):
    connection = get_connection()

    connection.execute("""
        INSERT INTO items
        (item_name, description, category, location, report_type, contact)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (item_name, description, category, location, report_type, contact))

    connection.commit()
    connection.close()


def get_all_items():
    connection = get_connection()

    items = connection.execute("""
        SELECT * FROM items
        ORDER BY date_reported DESC
    """).fetchall()

    connection.close()

    return items


def get_dashboard_stats():
    connection = get_connection()

    total = connection.execute(
        "SELECT COUNT(*) FROM items"
    ).fetchone()[0]

    lost = connection.execute(
        "SELECT COUNT(*) FROM items WHERE report_type = 'Lost'"
    ).fetchone()[0]

    found = connection.execute(
        "SELECT COUNT(*) FROM items WHERE report_type = 'Found'"
    ).fetchone()[0]

    resolved = connection.execute(
        "SELECT COUNT(*) FROM items WHERE status = 'Resolved'"
    ).fetchone()[0]

    connection.close()

    return total, lost, found, resolved

def update_item_status(item_id, status):
    connection = get_connection()

    connection.execute("""
        UPDATE items
        SET status = ?
        WHERE id = ?
    """, (status, item_id))

    connection.commit()
    connection.close()
