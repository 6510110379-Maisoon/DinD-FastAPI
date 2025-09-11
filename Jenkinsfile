pipeline {
    agent {
        docker {
            image 'python-java-docker:3.11'
            args '-v /var/run/docker.sock:/var/run/docker.sock' // DinD
        }
    }

    environment {
        SONARQUBE = credentials('sonar-token')
        IMAGE_NAME = "psu6510110379/fastapi-app"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/6510110379-Maisoon/DinD-FastAPI.git'
            }
        }

        stage('Setup venv') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh 'venv/bin/pytest --maxfail=1 --disable-warnings -q --cov=app --cov-report=xml'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    script {
                        def scannerHome = tool 'sonar-scanner'
                        sh """
                        ${scannerHome}/bin/sonar-scanner \
                          -Dsonar.projectKey=fastapi-clean-demo \
                          -Dsonar.sources=app \
                          -Dsonar.python.coverage.reportPaths=coverage.xml
                        """
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f fastapi-app || true
                docker run -d -p 8000:8000 --name fastapi-app ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Push to Registry') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-cred',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}
