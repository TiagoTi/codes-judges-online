path_name=$(readlink -f ./..)
path_name=${path_name##*/}

sonar-scanner \
  -Dsonar.projectKey=$path_name \
  -Dsonar.sources=. \
  -Dsonar.host.url=$SONAR_URL \
  -Dsonar.login=$SONAR_LOGIN \
  -Dsonar.language=java
