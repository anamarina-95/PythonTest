pipeline{
    
    agent any
    
    stages{
        
        stage ("Running something"){
            
            steps {
                sh '''
                    echo "Ola"
                '''
            }
            
        }
        
    }
}
