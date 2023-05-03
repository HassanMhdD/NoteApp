pipeline {
    agent any
    stages{
        stage('Execute Ansible Playbook'){
            environment{
                // Définit les variables d'environnement pour l'utilisateur distant et les informations d'authentification SSH
                remoteUser = 'ubuntu'
                sshKey = credentials('2c2e5f7b-6aa6-49df-89e0-2819247e0ce6')
                }
                steps{
                    // Exécute les commandes Ansible pour déployer les playbooks sur l'agent distant
                    withEnv(["ANSIBLE_CONFIG=Ansible/ansible.cfg"]) {
                        sh "ansible-playbook -i inventory.yml --user='${remoteUser}' --private-key='${sshKey}' playbook_installation.yml"
                        }
                    }
        }
    }
}