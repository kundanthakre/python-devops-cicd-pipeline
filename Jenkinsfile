pipeline {

```
agent any

environment {
    APP_SERVER = "172.31.45.171"
    APP_DIR = "/home/ubuntu/python-app"
}

stages {

    stage('Clone Repository') {
        steps {
            git branch: 'main',
            url: 'https://github.com/kundanthakre/python-devops-cicd-pipeline.git'
        }
    }

    stage('Run Tests') {
        steps {
            sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install -r app/requirements.txt
            pytest
            '''
        }
    }
}
```

}
