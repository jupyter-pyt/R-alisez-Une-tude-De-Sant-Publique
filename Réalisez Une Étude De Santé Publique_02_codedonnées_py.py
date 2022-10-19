
############################################################ Version 1 ############################################################ 

import pyodbc, sqlalchemy, os
import pandas as pd 
import platform
import socket
from pathlib import Path

# Vérifier la Directory.
print()
retval = os.getcwdb()
print ("Current working directory %s" % retval)
print()

# Changement De La Directory
os.chdir(r"C:\Users\FURY\Desktop\Projet_3 SQL")
retval = os.getcwdb()
print("Directory changed successfully %s" % retval)

# Afficher Le Nom D'hôte (HostName)
print()
print(platform.node())
print()
print(socket.gethostname())

# Obtenir La Liste Des ODBC (Open Database Connectivity) Disponible :
print()
lst = pyodbc.drivers()
for i in lst :
    print(i)

# Obtenir La Liste Des Fichiers Disponible :
print()
for i in os.listdir():
    print(i)

# Établir La Connection Avec La Moteur De Base De Données (SGBD)
print()
conn = sqlalchemy.create_engine(f'mssql+pyodbc://{socket.gethostname()}/OpenClassrooms?trusted_connection=yes&driver=SQL SERVER')
print (conn)

# Choisir la méthode De Chargement Des Fichiers1
# 1 - Charger Tout Les fichiers
# 2 - Charger Un Fichier Spécéfique
print()
print('Veuillez Choisir Vôtre Mode De Chargement : ')
print('# 1 - Charger Tout Les fichiers')
print('# 2 - Charger Un Fichier Spécéfique')
print()
MDC = input()

if MDC == '1':
    for fl in os.listdir():
        # Obtenir Le Nom De Fichier Sans Extension À Partir Du Chemin En Utilisant La Méthode pathlib.path().stem
        file_path = fl
        file_name = Path(file_path).stem
        df = pd.read_csv(fl)
        df.to_sql(file_name, con = conn, if_exists ="append", index=False)
    print('Tout Les Fichiers Sont Chargés')
elif MDC == '2':
    print('''Veuillez Entrer Le Chemin D'accès Du Fichier : ''')
    CAF = input()
    df = pd.read_csv(CAF)
    df.to_sql("fr_population", con = conn, if_exists ="append", index=False)
    df = pd.read_sql(sql = "SELECT * FROM fr_population", con = conn)
    print(df)
else:
    print('Veuillez Entrer Le Bon Numéro')


############################################################ Version 2 ############################################################ 
import pyodbc 
import pandas as pd 

pyodbc.drivers()
print(pyodbc.drivers())
conx_string = "driver={SQL SERVER}; server=DESKTOP-BIJR7UP; database=OpenClassrooms; trusted_connection=YES;"
conx = pyodbc.connect(conx_string);

sql_insert = (r'''
        USE [OpenClassrooms]
        
        BULK INSERT [OpenClassrooms].[dbo].[fr_population]
            FROM 'C:\Users\FURY\Desktop\Projet_3 SQL\fr_population.csv'
            WITH
            (
            FORMAT = 'CSV',		
            FIRSTROW = 2,
            CODEPAGE = '65001',
            FIELDTERMINATOR = ',',  --CSV field delimiter
            ROWTERMINATOR = '0x0a',
            --ROWTERMINATOR = '\n',   --Use to shift the control to next row
            ERRORFILE = 'C:\Users\FURY\Desktop\Projet_3 SQL\fr_populationErrorRows.csv'
            )

        ''')
sql_insert_ = (r'''

       "SELECT * FROM [OpenClassrooms].[dbo].[fr_population]"

        ''')
cursor = conx.cursor();
cursor.execute(sql_insert);
#cursor.execute(sql_insert_);














