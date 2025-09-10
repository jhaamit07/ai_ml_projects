# Local Password Manager

## Overview
This is a Python-based password manager with local storage using SQLite and a GUI developed with PySimpleGUI. It secures passwords with encryption and requires a master password for access.

## Features
- User authentication via master password
- Store website, username, and encrypted passwords locally
- Password encryption using Fernet symmetric encryption
- Simple and user-friendly PySimpleGUI interface
- Local SQLite database storage (passwords.db)
- Export/import features (optional)

## Setup

1. Install dependencies:
pip install PySimpleGUI cryptography

2. Run the app:
python password_manager.py


## Database
- Uses SQLite database `passwords.db`.
- Contains two tables: 
- `master_user` (stores hashed master password)
- `passwords` (stores encrypted password data)
- Database is created automatically upon first run.

## Security
- Master password is hashed with SHA-256.
- Stored passwords are encrypted with a key derived from the master password.
- Passwords can only be decrypted after successful login.

## Screenshots
- (Insert screenshots of GUI and DB Browser schema here)

## Usage
- Register a master password on first launch.
- Login with master password.
- Add, view, and manage your passwords securely.

---

