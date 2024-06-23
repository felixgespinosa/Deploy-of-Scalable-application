#!usr/bin/python3
import os

#Instalamos docker y docker-compose
os.system('sudo apt-get remove docker docker-engine docker.io containerd runc')
os.system('sudo apt-get update')
os.system('sudo apt-get install -y ca-certificates curl gnupg lsb-release')
os.system('sudo apt install -y docker')
os.system('sudo apt install -y docker-compose')
os.system('sudo chmod +x /usr/local/bin/docker-compose')

#Importamos el repositorio github
os.system('sudo apt-get install -y git')
os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')

#Ejecutamos contenedor del gradle
os.chdir('practica_creativa2/bookinfo/src/reviews')
os.system('sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')

#Cambiamos al directorio de trabajo y levantamos el servicio
#os.chdir(os.path.expanduser("~/"))

#os.system('sudo docker-compose build')
#os.system('sudo docker-compose up')
