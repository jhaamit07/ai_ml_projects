import PySimpleGUI as sg
import sqlite3
import hashlib

# Create database
def setup_database():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords 
                     (id INTEGER PRIMARY KEY, website TEXT, username TEXT, password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS master 
                     (id INTEGER PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

# Check master password
def check_master_password(password):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('SELECT * FROM master WHERE password=?', (hashed,))
    result = cursor.fetchone()
    conn.close()
    return result

# Set master password (first time)
def set_master_password(password):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('INSERT INTO master (password) VALUES (?)', (hashed,))
    conn.commit()
    conn.close()

# Save password
def save_password(website, username, password):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)',
                   (website, username, password))
    conn.commit()
    conn.close()

# Get all passwords
def get_passwords():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('SELECT website, username, password FROM passwords')
    results = cursor.fetchall()
    conn.close()
    return results

# Delete a password entry
def delete_password(website, username):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM passwords WHERE website=? AND username=?', (website, username))
    conn.commit()
    conn.close()

# Main program
def main():
    setup_database()
    
    # Login window
    layout = [
        [sg.Text('Master Password:'), sg.Input(key='-MASTER-', password_char='*')],
        [sg.Button('Login'), sg.Button('Set Password')]
    ]
    
    window = sg.Window('Password Manager Login', layout)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Set Password':
            if values['-MASTER-']:
                set_master_password(values['-MASTER-'])
                sg.popup('Master password set!')
            else:
                sg.popup('Enter a password!')
        elif event == 'Login':
            if check_master_password(values['-MASTER-']):
                window.close()
                password_manager_window()
                break
            else:
                sg.popup('Wrong password!')
    
    window.close()

def password_manager_window():
    layout = [
        [sg.Text('Website:'), sg.Input(key='-WEBSITE-')],
        [sg.Text('Username:'), sg.Input(key='-USERNAME-')],
        [sg.Text('Password:'), sg.Input(key='-PASSWORD-')],
        [sg.Button('Save'), sg.Button('Show All'), sg.Button('Delete Password')],
        [sg.Multiline(key='-OUTPUT-', size=(50, 10))]
    ]
    
    window = sg.Window('Password Manager', layout)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Save':
            if values['-WEBSITE-'] and values['-USERNAME-'] and values['-PASSWORD-']:
                save_password(values['-WEBSITE-'], values['-USERNAME-'], values['-PASSWORD-'])
                sg.popup('Password saved!')
                window['-WEBSITE-'].update('')
                window['-USERNAME-'].update('')
                window['-PASSWORD-'].update('')
            else:
                sg.popup('Please fill all fields!')
        elif event == 'Show All':
            passwords = get_passwords()
            output = ''
            for website, username, password in passwords:
                output += f"Website: {website}\nUsername: {username}\nPassword: {password}\n\n"
            window['-OUTPUT-'].update(output)
        elif event == 'Delete Password':
            if values['-WEBSITE-'] and values['-USERNAME-']:
                delete_password(values['-WEBSITE-'], values['-USERNAME-'])
                sg.popup('Password deleted successfully!')
                # Optionally update displayed passwords automatically
                passwords = get_passwords()
                output = ''
                for website, username, password in passwords:
                    output += f"Website: {website}\nUsername: {username}\nPassword: {password}\n\n"
                window['-OUTPUT-'].update(output)
            else:
                sg.popup('Please enter Website and Username to delete.')
    
    window.close()

if __name__ == '__main__':
    main()
