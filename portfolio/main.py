import os
import re
import win32crypt  # Requires pywin32 package

WORKBENCH_REGEX = re.compile('(?P<dbm>[A-z]+)@(?P<host>[A-z0-9._-]+):(?P<port>[0-9]+)\2(?P<user>[A-z0-9_-]+)\3(?P<password>.*)')

def read_workbench_user_data(file_path=None):
    if file_path is None:
        file_path = os.path.join(os.getenv('APPDATA'), 'MySQL/Workbench/workbench_user_data.dat')

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = win32crypt.CryptUnprotectData(encrypted_data, None, None, None, 0)
    decrypted_content = decrypted_data[1].decode('utf-8')
    return decrypted_content.split('\n')[:-1]

if __name__ == '__main__':
    for item in read_workbench_user_data():
        match = WORKBENCH_REGEX.match(item)

        print(f'{match.group("dbm")}:')
        print(f'\tHost: {match.group("host")}:{match.group("port")}')
        print(f'\tUsername: {match.group("user")}')
        print(f'\tPassword: {match.group("password")}')