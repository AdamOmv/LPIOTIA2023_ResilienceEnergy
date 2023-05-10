# LPIOTIA2023_ResilienceEnergy

* Oumarov Adam, 22001137, oumarov.adam@gmail.com
* Billebault Baptiste 22005584 billebaultbaptiste@gmail.com

---------------------
## Git Procedure

When you work in one non development file do git lock  

```bash
For lock :  
git lfs lock "file name"
For look locks files :  
git lfs locks
For unlock : 
git lfs unlock "file name"
```

---------------------
## Draw.io Procedure
 
1. pull the file (git pull)  
2. next lock the file (git lfs lock Project-Resilience_Energetique.drawio)  
3. after you open it on
4. add the the modification (git add .)  
5. then commit (git commit -m "")  
6. and then unlock the file (git lfs unlock Project-Resilience_Energetique.drawio)  

---------------------
## MQTT Procedure
 
* Mosquitto est un serveur MQTT open-source qui permet d'utiliser simplement le protocole MQTT entre différents appareils connectés au même réseau.

* Le protocole MQTT (Message Queue Telemetry Transport) est un protocole de communication spécifié pour des échanges de données de petite taille sur des réseaux avec beaucoup de délais et une faible bande passante.  

### Installation sur Linux  

```bash
sudo apt-get update
sudo apt-get install mosquitto mosquitto-client
```

* Une fois le service installé, il est possible de le gérer avec les commanndes suivantes.  

```bash
sudo systemctl stop mosquitto   #arrêter
sudo systemctl start mosquitto  #démarrer
sudo systemctl restart mosquitto #redémarrer
sudo systemctl status mosquitto #connaitre le status
```

* Vous pouvez egalement le confugurer  

```
sudo nano /etc/mosquitto/mosquitto.conf
sudo nano /etc/mosquitto/conf.d/default.conf
```

* Il est possible d'utiliser mosquitto directement en ligne de commande. Dans un terminal.  

```
mosquitto_sub -h localhost -t test_topic
mosquitto_sub -h localhost -t test_topic
```

---------------------
## MQTT Contract
 
1. pull the file (git pull)  
2. next lock the file (git lfs lock Project-Resilience_Energetique.drawio)  
3. after you open it on
4. add the the modification (git add .)  
5. then commit (git commit -m "")  
6. and then unlock the file (git lfs unlock Project-Resilience_Energetique.drawio) 

---------------------

## Architecture

### 1.Backend

* Mosquitto (MQTT)
* Node-Red
* InfluxDB
* Python

### 2.Frontend

* Grafana

---------------------
## Sensor
