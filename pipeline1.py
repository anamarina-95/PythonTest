pipeline{
    
    agent any
    
    stages{
        
        stage ("Download repository"){
            
            steps {
                sh '''
                    cd $the_path
                    if [[ ! -d PythonTest ]]
                    then
                       git clone git@github.com:anamarina-95/PythonTest.git
                       cd PythonTest
                    else
                       cd PythonTest
                       git checkout main
                       git pull origin main
                    fi
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
