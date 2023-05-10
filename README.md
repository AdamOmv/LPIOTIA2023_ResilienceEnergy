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

## Architecture

### 1.Backend

* Mosquitto (MQTT)
* Node-Red
* InfluxDB
* Python
* Nginx
* Raspbian

### 2.Frontend

* Grafana

---------------------
## Materiels

* ShellyPlus 1PM * 2
* Panneau solaire
* Batterie
* Onduleur
* RaspBerry Pi3 model B
* Relais
* APS (Automatique Power Switch)
* Gestionnaire de Charge
* ET LE SOLEIL (ADAM)

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

* Sur le serveur Web des Shelly

1. Ajouter l'ip de la machine qui a le topic (ici un raspberry)
2. Ajouter le nom du Topic avec le port de NodeRed (1883)

Exemple :

```
XXX.XXX.XXX.XXX:1883
```

* On a deux Topic :

1. ```/home/shelly1/events/rpc```

```
object
  src: "Source Name"
  dst: "Destination"
  method: "NotifyStatus"
params: object
  ts: timestamp
switch:0: object
  id: 0
  apower: puissance
```

Exemple :

```
object
  src: "shellyplus1pm-083af201d8d8"
  dst: "/home/shelly1/events"
  method: "NotifyStatus"
params: object
  ts: 11554.94
switch:0: object
  id: 0
  apower: 11.4
```

A la place du apower il peut y avoir soit le courant (current), soit la tension (voltage) ou la puissance (apower).

2. ```/home/shelly2/events/rpc```

```
object
  src: "Source Name"
  dst: "Destination"
  method: "NotifyStatus"
params: object
  ts: timestamp
switch:0: object
  id: 0
  apower: puissance
```

Example : 

```
object
  src: "shellyplus1pm-083af201d8d8"
  dst: "/home/shelly1/events"
  method: "NotifyStatus"
params: object
  ts: 11554.94
switch:0: object
  id: 0
  apower: 11.4
```
A la place du apower il peut y avoir soit le courant (current), soit la tension (voltage) ou la puissance (apower).

---------------------

## Node-RED

Node-RED est un outil d'automation de flux vous permettant de contrôler et interconnecter des services cloud ou des objets connectés.

### Installation

* Installer Node.js et npm 

```
sudo apt-get install nodejs-legacy
sudo apt-get install npm
```

* Installer Node-RED

```
sudo npm install -g --unsafe-perm node-red node-red-admin
sudo ufw allow 1880
```

* Lancer Node-RED au demarrage du raspberry

```
sudo nano /etc/systemd/system/node-red.service

[Unit]
Description=Node-RED
After=syslog.target network.target

[Service]
ExecStart=/usr/local/bin/node-red-pi --max-old-space-size=128 -v
Restart=on-failure
KillSignal=SIGINT

# log output to syslog as 'node-red'
SyslogIdentifier=node-red
StandardOutput=syslog

# non-root user to run as
WorkingDirectory=/home/sammy/
User=sammy
Group=sammy

[Install]
WantedBy=multi-user.target
```

### Ajout MQTT Topic

* Adresse Serveur 
```http://localhost:1883```

* Topic
```/home/shelly(1/2)/events/rpc```

---------------------

## Docker

Docker est une plate-forme logicielle qui vous permet de concevoir, tester et déployer rapidement des applications à l'aide de conteneurs.  
On utilise docker pour installer des images InfluxDB et Grafana.

### Installation

1. Mise a jour apt

```sudo apt-get update```

2. Installer la dernier version de Docker

```sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin```

3. Verification

```sudo docker run hello-world```

### Docker-compose

Pour installer InfluxDB et Grafana on utilise un fichier docker-compose.yml.  
Ce fichier contient la configuration et les images a installer avec les ports.

* Utilisation

```docker compose up```

---------------------

## Influx Data

On utilise InfluxDB pour avoir des données avec des "time series", cela nous permet de créer des DashBoard simplement avec Grafana.

Pour la configuration il faut creer un Token et l'ajouter sur Node-RED et Grafana pour pouvoir interagir avec InfluxDB.

---------------------

## Grafana

Grafana est un outil open source de monitoring informatique orienté data visualistation.  
On l'utilise ici pour créer un DashBoard.

1. Il faut connecter InfluxDb a Grafana avec un Token
2. Creer un DashBoard avec un code en querry

Le code query et dans le fichier "InfluxDb query command.txt"

Exemple :

```
from(bucket: "consomation")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "current")
  |> filter(fn: (r) => r["_field"] == "value")
  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
  |> yield(name: "mean")
```

