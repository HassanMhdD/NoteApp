import os

hostname = 'database'
database = 'test'
username= 'hassan'
pwd = 'hassan123'
port_id = 5432

url= f'postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}'
