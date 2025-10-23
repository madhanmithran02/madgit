# Quick Start Guide - Supabase PostgreSQL Connection

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure Your Database
```bash
# Copy the template
cp .env.example .env

# Edit .env and replace [YOUR_PASSWORD] with your actual password
```

### Step 3: Test Connection
```bash
# Test basic connection
python connect_supabase.py

# Try database operations (optional)
python example_operations.py
```

## 📝 What You Need

- Your Supabase database password
- Python 3.7+
- Network access to: `db.ujxwaisatoycvrocchgw.supabase.co`

## 🔒 Security Reminder

- Never commit `.env` file to git ✓ (already in .gitignore)
- Keep your database password secure
- Use environment variables for credentials

## 🆘 Common Issues

**"DATABASE_URL not found"**
→ Create `.env` file from `.env.example`

**"Please replace [YOUR_PASSWORD]"**
→ Edit `.env` and add your actual Supabase password

**"Error connecting to database"**
→ Check password, network connection, and Supabase IP allowlist

## 📚 Learn More

See [README.md](README.md) for detailed documentation.
