import os

hostname = os.environ.get('HOSTNAMEPOSTGRE')
database = os.environ.get('POSTGRES_DB')
username= os.environ.get('POSTGRES_USER')
pwd = os.environ.get('POSTGRES_PASSWORD')
port_id = 5432

url= f'postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}'