pipeline {
    agent {
        docker { image python:3.9-slim-buster }
    }

    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python -m unittest bisturi_test.py'
            }
        }
    }
}