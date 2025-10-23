# MadGit - Supabase PostgreSQL Connection

This repository demonstrates how to connect to a Supabase PostgreSQL database.

## Prerequisites

- Python 3.7 or higher
- A Supabase account with a PostgreSQL database
- Your Supabase database password

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables**:
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and replace [YOUR_PASSWORD] with your actual Supabase password
   # The file should look like:
   # DATABASE_URL=postgresql://postgres:your_actual_password@db.ujxwaisatoycvrocchgw.supabase.co:5432/postgres
   ```

## Usage

### Connect to Supabase Database

Run the connection script to test your database connection:

```bash
python connect_supabase.py
```

This script will:
- Load your database credentials from the `.env` file
- Connect to your Supabase PostgreSQL database
- Display the PostgreSQL version
- Show the current database and user information
- Close the connection gracefully

### Example Output

```
============================================================
Supabase PostgreSQL Database Connection Test
============================================================
Connecting to Supabase PostgreSQL database...
✓ Successfully connected to Supabase!

PostgreSQL Version:
PostgreSQL 15.1 on x86_64-pc-linux-gnu...

Current Database: postgres
Current User: postgres

✓ Connection closed successfully.
============================================================
```

## Connection String Format

The Supabase PostgreSQL connection string follows this format:

```
postgresql://postgres:[YOUR_PASSWORD]@db.ujxwaisatoycvrocchgw.supabase.co:5432/postgres
```

Where:
- **postgres**: Default username
- **[YOUR_PASSWORD]**: Your Supabase database password
- **db.ujxwaisatoycvrocchgw.supabase.co**: Your Supabase database host
- **5432**: PostgreSQL default port
- **postgres**: Database name

## Security Notes

⚠️ **Important**: Never commit your `.env` file containing actual passwords to version control. The `.gitignore` file is configured to exclude it.

## Troubleshooting

### Connection Failed
- Verify your password is correct in the `.env` file
- Check that you've replaced `[YOUR_PASSWORD]` with your actual password
- Ensure your IP address is allowed in Supabase's network settings
- Verify the database host URL is correct

### Module Not Found
- Make sure you've installed the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Dependencies

- **psycopg2-binary**: PostgreSQL adapter for Python
- **python-dotenv**: Load environment variables from `.env` file

## License

This is a demonstration repository for learning purposes.
