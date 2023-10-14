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

