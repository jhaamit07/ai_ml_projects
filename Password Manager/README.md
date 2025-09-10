# Local Password Manager

## Overview
This is a simple Python-based password manager application. It stores your website login credentials securely in a local SQLite database and requires a master password for access.

This repository includes:
- Python source code (`password_manager.py`)
- Windows executable (`password_manager.exe`) in the `dist` folder
- SQLite database (`passwords.db`) created automatically on first run

---

## Features
- Set and verify a master password
- Save website, username, and password securely
- View all saved password entries
- Delete saved entries
- Local storage with SQLite database

---

## Installation

### Running the Python Script
1. Ensure you have [Python 3.x](https://www.python.org/downloads/) installed.
2. Install required libraries:
pip install PySimpleGUI
3. Run the password manager script:
python password_manager.py


### Running the Windows Executable
- Navigate to the `dist` folder.
- Run `password_manager.exe`.
- No need to install Python or dependencies.

---

## How to Use

1. **Launch the app** (via `.exe` or Python script).
2. **Set a master password** (first time only).
3. **Login** with your master password.
4. Use the GUI to:
- Add new passwords (Website, Username, Password)
- View all saved passwords by clicking "Show All"
- Delete any password by entering the Website and Username, then clicking "Delete Password"

---

## Security Notes
- Master password is hashed securely.
- Passwords are saved locally; no data is sent online.
- Use a strong master password to protect your database.

---

## Screenshots
![Image 1](https://github.com/user-attachments/assets/2d385b85-806a-46a6-8c6b-c65e0e48a894)

![Image 2](https://github.com/user-attachments/assets/5190674d-9f42-4cb5-942e-2df74c4914d5)

![Image 3](https://github.com/user-attachments/assets/a47c036c-f4e4-4f84-b5a5-4ab0e7f03ed2)

---

## License
This project is free to use for learning and personal purposes.

---

