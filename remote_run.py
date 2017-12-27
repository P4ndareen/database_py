#!/usr/bin/python3

''' Remote version of programm '''

import paramiko


class Connection:
    ''' Establish connection with server to access database '''

    def __init__(self):
        ''' Attributes initialization '''

        self.LOGIN = input('Login: ')
        self.PASSWORD = input('Pasword: ')

    def serv_connect(self):
        ''' Establish connection to server '''

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Trying to connect to client
        client.connect(
            hostname='192.168.1.1',
            username=self.LOGIN,
            password=self.PASSWORD,
            port='22'
            )
        #command to execute, doesn't work with sudo... yet
        _, stdout, stderr = client.exec_command('path/to/run.py')
        data = stdout.read() + stderr.read()
        fxdata = data.decode().replace("'", '').replace(")", '').replace("(", '').replace(",", ':')
        print('\n%s' % fxdata)
        client.close()

with Connection().serv_connect() as start:
    start
