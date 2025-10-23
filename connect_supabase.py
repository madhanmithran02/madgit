#!/usr/bin/env python3
"""
Supabase PostgreSQL Database Connection Script
This script connects to a Supabase PostgreSQL database using the connection string
provided in the environment variables.
"""

import os
import sys
import psycopg2
from dotenv import load_dotenv

def connect_to_supabase():
    """
    Connect to Supabase PostgreSQL database using environment variables.
    
    Returns:
        connection: psycopg2 connection object if successful, None otherwise
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Get database URL from environment
    database_url = os.getenv('DATABASE_URL')
    
    if not database_url:
        print("Error: DATABASE_URL not found in environment variables.")
        print("Please create a .env file based on .env.example and add your password.")
        return None
    
    # Check if password placeholder is still present
    if '[YOUR_PASSWORD]' in database_url:
        print("Error: Please replace [YOUR_PASSWORD] in your .env file with your actual Supabase password.")
        return None
    
    try:
        print("Connecting to Supabase PostgreSQL database...")
        connection = psycopg2.connect(database_url)
        print("✓ Successfully connected to Supabase!")
        return connection
    except psycopg2.Error as e:
        print(f"✗ Error connecting to database: {e}")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None

def test_connection(connection):
    """
    Test the database connection by running a simple query.
    
    Args:
        connection: psycopg2 connection object
    """
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        
        # Get PostgreSQL version
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"\nPostgreSQL Version:\n{version[0]}")
        
        # Get current database name
        cursor.execute("SELECT current_database();")
        db_name = cursor.fetchone()
        print(f"\nCurrent Database: {db_name[0]}")
        
        # Get current user
        cursor.execute("SELECT current_user;")
        user = cursor.fetchone()
        print(f"Current User: {user[0]}")
        
        cursor.close()
        
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """Main function to connect and test Supabase database."""
    print("=" * 60)
    print("Supabase PostgreSQL Database Connection Test")
    print("=" * 60)
    
    # Connect to database
    connection = connect_to_supabase()
    
    if connection:
        # Test the connection
        test_connection(connection)
        
        # Close connection
        connection.close()
        print("\n✓ Connection closed successfully.")
        print("=" * 60)
        return 0
    else:
        print("\n✗ Failed to connect to database.")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
