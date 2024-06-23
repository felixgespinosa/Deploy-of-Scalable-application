#!usr/bin/python3

import os

#Clonamos el repositorio para la práctica
os.system("sudo apt-get update")
os.system("sudo apt-get install -y git")
os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")

#Instalamos pip
os.system("sudo apt-get install -y python3-pip")

#Estas dependencias se cambian porque hay incompatibilidades entre librerias
#os.system("sed -i 's/chardet==3.0.4/chardet/g' practica_creativa2/bookinfo/src/productpage/requirements.txt")
#os.system("sed -i 's/gevent==1.4.0/gevent/g' practica_creativa2/bookinfo/src/productpage/requirements.txt")
#os.system("sed -i 's/greenlet==0.4.15/greenlet/g' practica_creativa2/bookinfo/src/productpage/requirements.txt")
#os.system("sed -i 's/urllib3==1.26.5/urllib3/g' practica_creativa2/bookinfo/src/productpage/requirements.txt")
#os.system("sed -i 's/requests==2.21.0/requests/g' practica_creativa2/bookinfo/src/productpage/requirements.txt")

#Instalamos las dependencias
os.system("sudo pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt")

#Creamos una variable de entorno con el número de grupo
os.environ["GRUPO_NUMERO"] = "07"

#Cambiamos el título de la página productpage para que muestre el número de grupo
numero_grupo = os.environ.get("GRUPO_NUMERO")

fin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r")
fout = open("productpage.html", "w")
for line in fin: 
  if "Simple Bookstore App" in line:
    fout.write("{% block title %}Simple Bookstore App Grupo:" + numero_grupo + "{% endblock %}")
  else: 
  	fout.write(line)
fin.close()
fout.close()
os.system("mv productpage.html practica_creativa2/bookinfo/src/productpage/templates/productpage.html")
#Se podría añadir para que al ejecutar el script se meta como parametro un puerto y si no, se lanza en predeterminado 9080

#Ejecutamos la aplicación en un puerto diferente al predeterminado, 8888
os.system("python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 8888")