pipeline {
    agent { docker { image 'python:3.10.0' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}