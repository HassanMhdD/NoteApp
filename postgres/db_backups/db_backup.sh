#!/bin/bash
DIR=`date +%d-%m-%y`
DEST=~/db_backups/$DIR
if [[ ! -d ~/db_backups ]]
then
        mkdir ~/db_backups
fi
if [[ ! -d $DEST ]]
then
        mkdir $DEST
fi

PGPASSWORD='hello123' pg_dump --inserts --column-inserts --username=hassan --host=172.31.95.134 --port=5432 test > $DEST/dbbackup.sql
