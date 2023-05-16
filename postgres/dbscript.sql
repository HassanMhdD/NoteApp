CREATE ROLE hassan with login;
ALTER ROLE hassan with ENCRYPTED PASSWORD 'hassan123';
ALTER ROLE hassan CREATEDB;
CREATE DATABASE test with OWNER hassan;
