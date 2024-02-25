pipeline{
    
    agent any
    
    stages{
        
        stage ("Download repository"){
            
            steps {
                sh '''
                    cd $the_path
                    if not PythonTest:
                       git clone git@github.com:anamarina-95/PythonTest.git
                       cd /home/ana95/Picture/PythonTest
                    else:
                       cd /home/ana95/Picture/PythonTest
                       git checkout main
                       git pull origin main
                '''
            }
            
        }
        
        stage ("Move script to desktop") {
            steps {
                sh '''
                    mv myapp.py /home/ana95/Desktop
                '''
            }
            
        }
        
    }
}
