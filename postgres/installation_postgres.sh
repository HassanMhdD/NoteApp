#!/bin/bash


# This script will perform the following steps:
# 1. Verify privileges and run the script as a superuser
# 2. Install postresql
# 3. Configure
set -eu -o pipefail # if there is any errors, fail and exit # -u: if a variable doesn't exit, report the error and stop
                                                            # -e: terminate whenever an error occurs
                                                            # -o pipefail: if a sub-command fails, the entire pipeline command fails,terminating the script


sudo -n true # Run as superuser and don't ask for a password. #-n: Prevent sudo from prompting for a password. If one is required, sudo di     splays an error message and exits
                                                              #true: Builtin command that returns a succesful (zero) exit status

if [[ $? -eq 1 ]]
then
        echo "You should have sudo privilege to run this script"
else
    if ! dpkg -s postgresql >/dev/null 2>&1; then

        echo '-------------------------------'
        echo '###############################'
        echo 'POSTGRESQL IS NOT INSTALLED.'
        echo 'Update and Installation postgres'
        echo '###############################'
        echo '-------------------------------'
        echo 'UPDATING...'
        apt-get update
        echo 'INSTALLING POSTGRES...'
        apt-get install postgresql -y

        # Check installation status
        if dpkg -s postgresql >/dev/null 2>&1; then
            echo 'POSTGRESQL INSTALLATION SUCCESSFUL'
        else
            echo 'POSTGRESQL INSTALLATION FAILED'
            exit 1
        fi
    else
        echo 'POSTGRESQL IS ALREADY INSTALLED.'
    fi
        # $dbcript is the sql script for creating the PSQL user and creating a database.
        dbscript='/home/ubuntu/dbscript.sql'

        # The dbscript.sql is ran to create the user and  database.
        echo '-----------------'
        echo '#################'
        echo 'RUNNING SCRIPT...'
        echo '#################'
        echo '-----------------'
        sudo chmod 0751 /home/ubuntu
        sudo -u postgres psql -f $dbscript

        echo '-----------------------------'
        echo '#############################'
        echo 'MODIFYING POSTGRESQL.CONF ...'
        echo '#############################'
        echo '-----------------------------'
        sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" /etc/postgresql/14/main/postgresql.conf

        sleep 3

        echo '-----------------------------'
        echo '#############################'
        echo 'MODIFYING PG_HBA.CONF ...'
        echo '#############################'
        echo '-----------------------------'

        echo '# Allow client connections to all data bases and users' | sudo tee -a /etc/postgresql/14/main/pg_hba.conf >/dev/null
        echo 'host      all     all     0.0.0.0/0 md5' | sudo tee -a /etc/postgresql/14/main/pg_hba.conf >/dev/null

        sleep 3
        sudo systemctl restart postgresql
        echo 'Configuration completed'
fi
