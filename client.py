from socket import *
from datetime import datetime


def dt():
    curr_dt = datetime.now()
    return curr_dt


def main():
    while True:
        k = int(input(f'{dt()}\nIf you want to connect to server1 type 1\n'
                      'If you want to connect to server2 type 2\n'
                      'If you want to disconnect completely type 0\n'))
        if k == 1:
            client = socket(AF_INET, SOCK_STREAM)
            ip = '192.168.1.102'
            port = 1234
            client.connect((ip, port))
            while True:
                msg = client.recv(1024).decode('utf-8')
                print(f'\nSERVER MSG: {msg}')
                ans = str(input())
                if ans == 'no':
                    client.send(ans.encode('utf-8'))
                    break
                else:
                    client.send(ans.encode('utf-8'))

        elif k == 2:
            client = socket(AF_INET, SOCK_STREAM)
            ip = '192.168.1.102'
            port = 5678
            client.connect((ip, port))
            while True:
                msg = client.recv(1024).decode('utf-8')
                print(f'\nSERVER MSG: {msg}')
                ans = str(input())
                if ans == 'no':
                    client.send(ans.encode('utf-8'))
                    break
                else:
                    client.send(ans.encode('utf-8'))

        elif k == 0:
            break
        else:
            print(f'{dt()} Incorrect input! Try again\n')


if __name__ == "__main__":
    main()
