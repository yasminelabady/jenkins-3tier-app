pipeline {
    agent any

    stages {
        stage('Build Images') {
            steps {
                script {
                    sh 'docker compose build'
                }
            }
        }

        stage('Run Containers') {
            steps {
                script {
                    sh 'docker compose up -d'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

