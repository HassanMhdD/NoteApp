import os

hostname = '172.31.95.134'
database = 'test'
username= 'hassan'
pwd = 'hello123'
port_id = 5432

url= f'postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}'
