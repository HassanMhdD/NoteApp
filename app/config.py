import os

hostname = 'noteapp-db.cwtr407c812l.us-east-1.rds.amazonaws.com'
database = 'test'
username= 'hassan'
pwd = 'hello123'
port_id = 5432

url= f'postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}'
