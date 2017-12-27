#!/usr/bin/python3

''' Prints information stored at database to linux terminal '''

import sqlite3


class BaseGetterError(Exception):
    ''' Getter Error '''
    pass

class AuthError(BaseGetterError):
    ''' Basic Authentification Error '''
    pass

class Getter:
    ''' Get database info '''

    def __init__(self, login, password):
        ''' Attributes initialization '''

        self.login = login
        self.password = password
        self.connect = sqlite3.connect('database.sqlite3')
        self.cursor = self.connect.cursor()

    def credentials(self):
        ''' Sets which information show to which users '''

        if self.login == 'admin' and self.password == 'admin':
            getall = self.cursor.execute('''SELECT * FROM table''')
            for row in getall:
                print(row)

        elif self.login == 'test' and self.password == 'test':
            getall = self.cursor.execute('''SELECT row, row2 FROM table''')
            for row in getall:
                print(row)

        else:
            raise AuthError('Authentification failed')
