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

### Autobus - Secteur Sorel-Varennes - Horaires et parcours planifiés (GTFS)
Identifiant : 5a352b9d-44fc-4474-a537-e63444fab58e  
Url : https://www.donneesquebec.ca/recherche/dataset/sorel-varennes-gtfs  
Source : 	https://exo.quebec/xdata/citsv/google_transit.zip  
Type : GTFS


### Trains - Exo - Horaires et parcours planifiés (GTFS)
Identifiant : add94538-0df0-447b-8ec8-18741a0b7736  
Url : https://www.donneesquebec.ca/recherche/dataset/exo-trains-gtfs  
Source : 	https://exo.quebec/xdata/trains/google_transit.zip  
Type : GTFS


### Autobus - Secteur Sud-ouest - Horaires et parcours planifiés (GTFS) 

### Autobus - Secteur Laurentides - Horaires et parcours planifiés (GTFS) 

### Autobus - Secteur Vallée-du-Richelieu - Horaires et parcours planifiés (GTFS) 

### Autobus - Secteur Terrebonne-Mascouche - Horaires et parcours planifiés (GTFS)

### Autobus - Secteur Sainte-Julie - Horaires et parcours planifiés (GTFS) 

### Autobus - Secteur de La Presqu'île - Horaires et parcours planifiés (GTFS)

### Autobus - Secteur Haut-Saint-Laurent - Horaires et parcours planifiés (GTFS)

### Autobus - Secteur L'Assomption - Horaires et parcours planifiés (GTFS)

### Autobus - Secteur Chambly-Richelieu-Carignan - Horaires et parcours planifiés (GTFS)