#!/usr/bin/env python3
"""
Example script demonstrating basic database operations with Supabase PostgreSQL.
This script shows how to create tables, insert data, and query data.
"""

import os
import sys
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

def get_connection():
    """Get a connection to the Supabase database."""
    load_dotenv()
    database_url = os.getenv('DATABASE_URL')
    
    if not database_url or '[YOUR_PASSWORD]' in database_url:
        print("Error: Please configure DATABASE_URL in your .env file")
        return None
    
    try:
        return psycopg2.connect(database_url)
    except Exception as e:
        print(f"Error connecting: {e}")
        return None

def create_sample_table(connection):
    """Create a sample table for demonstration."""
    try:
        cursor = connection.cursor()
        
        # Create a sample users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sample_users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        connection.commit()
        print("✓ Sample table 'sample_users' created successfully")
        cursor.close()
        
    except Exception as e:
        print(f"Error creating table: {e}")
        connection.rollback()

def insert_sample_data(connection):
    """Insert sample data into the table."""
    try:
        cursor = connection.cursor()
        
        # Insert sample users
        sample_users = [
            ('john_doe', 'john@example.com'),
            ('jane_smith', 'jane@example.com'),
            ('bob_wilson', 'bob@example.com')
        ]
        
        for username, email in sample_users:
            cursor.execute(
                "INSERT INTO sample_users (username, email) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING",
                (username, email)
            )
        
        connection.commit()
        print(f"✓ Inserted {cursor.rowcount} sample records")
        cursor.close()
        
    except Exception as e:
        print(f"Error inserting data: {e}")
        connection.rollback()

def query_data(connection):
    """Query and display data from the table."""
    try:
        cursor = connection.cursor()
        
        cursor.execute("SELECT id, username, email, created_at FROM sample_users ORDER BY id")
        rows = cursor.fetchall()
        
        print("\nSample Users:")
        print("-" * 80)
        print(f"{'ID':<5} {'Username':<20} {'Email':<30} {'Created At':<25}")
        print("-" * 80)
        
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<30} {str(row[3]):<25}")
        
        print("-" * 80)
        cursor.close()
        
    except Exception as e:
        print(f"Error querying data: {e}")

def cleanup_table(connection):
    """Drop the sample table (optional cleanup)."""
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS sample_users")
        connection.commit()
        print("\n✓ Sample table dropped (cleanup complete)")
        cursor.close()
        
    except Exception as e:
        print(f"Error dropping table: {e}")
        connection.rollback()

def main():
    """Main function demonstrating database operations."""
    print("=" * 80)
    print("Supabase PostgreSQL - Database Operations Example")
    print("=" * 80)
    
    connection = get_connection()
    if not connection:
        return 1
    
    try:
        # Demonstrate various database operations
        create_sample_table(connection)
        insert_sample_data(connection)
        query_data(connection)
        
        # Ask user if they want to cleanup
        print("\nNote: This example created a table 'sample_users' in your database.")
        cleanup = input("Would you like to drop this table? (y/n): ").lower().strip()
        
        if cleanup == 'y':
            cleanup_table(connection)
        else:
            print("\nTable 'sample_users' kept in database.")
        
    finally:
        connection.close()
        print("\n✓ Connection closed")
        print("=" * 80)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
