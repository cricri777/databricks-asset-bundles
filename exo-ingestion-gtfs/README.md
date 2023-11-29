# A propos Du Projet
ingestion et processing des données gtfs et publique de la compagnie [Exo](https://exo.quebec/fr)
Ce pipeline tente de répondre aux questions suivante :
- Quels sont les horaires des bus et trains ?
- Quels sont les trajets des bus et trains ?

## Analyse de données pour GTFS de Exo
### 1 Lignes de train exo
Identifiant : 0bc4dc35-a12b-4695-8e0a-21b87c18d8a4  
Url : https://www.donneesquebec.ca/recherche/dataset/lignes-de-train-exo  
Source : https://exo.quebec/donnees_geomatiques/train_lignes_exo.geojson  
Type : GeoJSON  

Contenu :
- geometry - multilinestring coordonnées List(longitude, latitude)  
- id : id du train
- no_train : numéro du train
- nom_train : string nom du train
- coul_hex : string couleur hexadecimale de la ligne de train (i.e #f16179),
- date_maj_exo : ?? format %Y-%m-%d (i.e 2023-02-22)
- date_export : ?? format %Y-%m-%d

### 2 Gares de train exo
Identifiant : 95c99f50-d417-4932-9e9a-207b45b1b42a
Url : https://www.donneesquebec.ca/recherche/dataset/gares-de-train-exo  
Source : https://exo.quebec/donnees_geomatiques/train_gares_exo.geojson
Type : GeoJSON  

Contenu :  
- geometry - Point: coordonnées Tuple(longitude, latitude)
- id : id de la gare
- nom_gare : string nom de la gare
- nom_municipalite : string nom de la municipalité
- nom_train : string nom du train
- no_train : numéro du train,
- adresse_civique : string addresse civique
- a_un_stationnement : boolean si possède un stationnement
- date_maj_exo : ?? format %Y-%m-%d (i.e 2023-02-22)
- date_export : ?? format %Y-%m-%d

### 3 Territoire exo
Identifiant : 53f7c6ea-5b12-4688-a503-a901505242a1
Url : https://www.donneesquebec.ca/recherche/dataset/limites-du-territoire-exo  
Source : https://exo.quebec/donnees_geomatiques/territoire_exo.geojson  
Type : GeoJSON  

Contenu :  
- id : le id tu territoire
- date_maj_exo : ?? format %Y-%m-%d (i.e 2023-02-22)
- date_export : ?? format %Y-%m-%d
- geometry - Polygon : le territoire exo type polygon

### 4 Autobus - Secteur Sorel-Varennes - Horaires et parcours planifiés (GTFS)
Identifiant : 5a352b9d-44fc-4474-a537-e63444fab58e  
Url : https://www.donneesquebec.ca/recherche/dataset/sorel-varennes-gtfs  
Source : https://exo.quebec/xdata/citsv/google_transit.zip  
Type : GTFS


### 5 Trains - Exo - Horaires et parcours planifiés (GTFS)
Identifiant : add94538-0df0-447b-8ec8-18741a0b7736  
Url : https://www.donneesquebec.ca/recherche/dataset/exo-trains-gtfs  
Source : 	https://exo.quebec/xdata/trains/google_transit.zip  
Type : GTFS


### 6 Autobus - Secteur Sud-ouest - Horaires et parcours planifiés (GTFS)
Identifiant : 0c0bc533-f539-4ca8-92b4-2d521fd6542e  
Url : https://www.donneesquebec.ca/recherche/dataset/sud-ouest-gtfs  
Source : 	https://exo.quebec/xdata/citso/google_transit.zip  
Type : GTFS

### 7 Autobus - Secteur Laurentides - Horaires et parcours planifiés (GTFS) 
Identifiant : ca69f450-e24e-4666-aa61-be5d63fd0348  
Url : https://www.donneesquebec.ca/recherche/dataset/laurentides-gtfs  
Source : https://exo.quebec/xdata/citla/google_transit.zip  
Type : GTFS

### 8 Autobus - Secteur Vallée-du-Richelieu - Horaires et parcours planifiés (GTFS) 
Identifiant : 82275da4-83fd-4a1e-bbcd-d087d64154ac  
Url : https://www.donneesquebec.ca/recherche/dataset/vallee-du-richelieu-gtfs  
Source : https://exo.quebec/xdata/citvr/google_transit.zip  
Type : GTFS

### 9 Autobus - Secteur Terrebonne-Mascouche - Horaires et parcours planifiés (GTFS)
Identifiant : 17c7dacf-b491-44cd-ba47-eecea5efb334  
Url : https://www.donneesquebec.ca/recherche/dataset/terrebonne-mascouche-gtfs  
Source : https://exo.quebec/xdata/mrclm/google_transit.zip  
Type : GTFS

### 10 Autobus - Secteur Sainte-Julie - Horaires et parcours planifiés (GTFS) 
Identifiant : f298ba15-02cf-473f-aa88-49fcbb63b6a6  
Url : https://www.donneesquebec.ca/recherche/dataset/sainte-julie-gtfs  
Source : https://exo.quebec/xdata/omitsju/google_transit.zip  
Type : GTFS

### 11 Autobus - Secteur de La Presqu'île - Horaires et parcours planifiés (GTFS)
Identifiant : be1cca17-d9e8-45b8-b59b-be90c5f8602e
Url : https://www.donneesquebec.ca/recherche/dataset/presquile-gtfs  
Source : https://exo.quebec/xdata/citpi/google_transit.zip  
Type : GTFS

### 12 Autobus - Secteur Haut-Saint-Laurent - Horaires et parcours planifiés (GTFS)
Identifiant : 2cb1d60a-4410-4e05-a33d-5071bddcd031  
Url : https://www.donneesquebec.ca/recherche/dataset/haut-saint-laurent-gtfs  
Source : https://exo.quebec/xdata/cithsl/google_transit.zip    
Type : GTFS

### 13 Autobus - Secteur L'Assomption - Horaires et parcours planifiés (GTFS)
Identifiant : 5bf50944-0fc0-4f76-a96d-3f58314d940e  
Url : https://www.donneesquebec.ca/recherche/dataset/lassomption-gtfs    
Source : https://exo.quebec/xdata/mrclasso/google_transit.zip  
Type : GTFS

### 14 Autobus - Secteur Chambly-Richelieu-Carignan - Horaires et parcours planifiés (GTFS)
Identifiant : 5bf50944-0fc0-4f76-a96d-3f58314d940e  
Url : https://www.donneesquebec.ca/recherche/dataset/chambly-richelieu-carignan-gtfs  
Source : https://exo.quebec/xdata/citcrc/google_transit.zip  
Type : GTFS

# Pour commencer
## Excution local (databricks-connect)
### pré-requis 
- python > 3.10
- databricks cli > 0.205
- venv
- poetry > 1.7.1
- variable d'environnement :
  - DATABRICKS_CLUSTER_ID=1127-184500-z9lq82ws;
  - DATABRICKS_HOST=https://adb-7865087530835937.17.azuredatabricks.net/;
  - DATABRICKS_TOKEN=<ton_token_ici>

adb connector : /subscriptions/e921008b-db34-4fe4-8e81-5e87d56e1824/resourceGroups/cricri/providers/Microsoft.Databricks/accessConnectors/adbconnector
