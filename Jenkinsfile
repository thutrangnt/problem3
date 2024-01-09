pipeline {
    agent any
    
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage("Build"){
            steps{
                git branch: 'main', url: 'https://github.com/thutrangnt/problem3.git'
                bat 'python isValidString.py'
                
            }
        }
        
        stage("Test"){
            steps {
                echo 'Test'
            }
        }
    }
}
