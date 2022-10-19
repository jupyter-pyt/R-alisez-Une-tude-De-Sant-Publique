
import pandas as pd



########################################################################## Question 1 ##########################################################################
print("########################################################################## Question 1 ##########################################################################")
print("""
      """)

########--- Identification Des Possible Clés Primaires ---########
df = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_population.csv')
colonnes = ['Code Domaine', 'Domaine', 'Zone']
#colonnes = ['Code Domaine', 'Domaine']
def check_possible_primary_key(df, columns_pk): 
    if len(df) != len(df[columns_pk].drop_duplicates()): 
        raise Exception("{} can't be a primary key!".format(columns_pk))
    else :
        print("{} can be a primary key!".format(columns_pk))
check_possible_primary_key(df,colonnes)


########--- Détecter des éléments redondants ---########

def Detec_elem_redon():
    # ########--- Charger le Fichier fr_population.csv' ---########
    dataframe_fr_population = pd.read_csv(
        r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_population.csv')
    indexNames = dataframe_fr_population[dataframe_fr_population['Symbole'] == 'A'].index
    dataframe_fr_population = dataframe_fr_population.drop_duplicates()
    dataframe_fr_population.drop(indexNames, inplace=True)

    filtred_dataframe_fr_population = dataframe_fr_population
    return filtred_dataframe_fr_population


Detec_elem_redon()

########--- Selectionner les colonnes utile pour la Question 1 ---########
my_column = ['Zone', 'Unité', 'Valeur']
selected_column_dataframe_fr_population = Detec_elem_redon()[my_column]


def total_population_by_country():
    selected_column_dataframe_fr_population['total_population_by_country'] = selected_column_dataframe_fr_population.Valeur*1000

    ########--- Ajouter la colonne pour la population total par pays ---########
    # print('########--- Ajouter la colonne pour la population total par pays ---########')
    print('''
          ''')

    return selected_column_dataframe_fr_population


print('########--- lister de la population par pays ---########')
print(total_population_by_country())
print('''
      ''')
print('########--- Total de la population mondiale 2013 ---########')


def Word_population_2013():
    sum = total_population_by_country()['total_population_by_country'].sum()
    return sum


print('Le nombre d''habitans dans le monde en 2013 est de :',
      Word_population_2013(), 'Habitans')

################################################################################################################################################################
print("""
      """)
########################################################################## Question 2 ##########################################################################
print("########################################################################## Question 2 ##########################################################################")
print("""

      """)
print('                                                  ################### La Disponibilité ###################')
print(
      '''
     Les disponibilités comprennent l’ensemble des quantités domestiques de denrées alimentaires produites au cours de l’année, plus le volume des stocks disponibles en début d’année
     et les quantités de denrées alimentaires qui peuvent être acquises avec les revenus disponibles ou importés (FAO, 2001a). Elles permettent de déterminer le bilan alimentaire d’un
     pays à partir de l’agrégation des disponibilités des ménages.
      '''
)
print(
    '''
L'équation est la suivante :
---------------------------

    Disponibilité intérieure (kg/an) = + Production (kg/an) + Importations - Quantité (kg/an) + Variation de stock (kg/an)- Exportations 

                                                                <==>
                                                                
    Nourriture (kg/an) (Disponibilité alimentaire totale ) + Pertes (kg/an) + Semences (kg/an)

    Production (kg/an) = Semences (kg/an) + Traitement (kg/an)
'''
)

################################################################################################################################################################

print("""
      """)
########################################################################## Question 3 ##########################################################################
print("########################################################################## Question 3 ##########################################################################")
print("""
      """)

################## Utiliser le dataframe (Fichiers csv 'fr_animaux.csv' et 'fr_vegetaux.csv') ##################

df_dispo_alim_fr_animaux = pd.read_csv(
    r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_animaux.csv')
df_dispo_alim_fr_vegetaux = pd.read_csv(
    r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv')

df_dispo_alim_fr_animaux.Name = 'df_anim'
df_dispo_alim_fr_vegetaux.Name = 'df_vege'

list_Alim = [df_dispo_alim_fr_animaux, df_dispo_alim_fr_vegetaux]

str1 = 'Zone'
str2 = 'Produit'
str3 = 'Disponibilité alimentaire (Kcal/personne/jour)'
str4 = 'Disponibilité alimentaire en quantité (kg/personne/an)'
str5 = 'Disponibilité de protéines en quantité (g/personne/jour)'
colonnes = [str1, str2, str3, str4, str5]

def funct(dataframe):
    # Selecctionner les colonnes du dataframe disponibilité alimentaire protéine
    filtred_dataframe = dataframe[colonnes]
    ########--- Détecter des éléments redondants ---########
    filtred_dataframe = filtred_dataframe.drop_duplicates()
    indexNames = filtred_dataframe[filtred_dataframe['Zone'] == 'Chine'].index
    filtred_dataframe.drop(indexNames, inplace=True)
    return filtred_dataframe

for X in list_Alim:
    if X.Name == 'df_anim':
        df_anim_ = funct(X)
        print('''
              ''')
    elif X.Name == 'df_vege':
        df_vege_ = funct(X)

df_anim_ = pd.DataFrame(df_anim_)
df_vege_ = pd.DataFrame(df_vege_)
df_anim_['Index_Prot'] = 'Prot_Animal'
df_vege_['Index_Prot'] = 'Prot_Veget'

print('''
      ''')
#--- Concatener les deux dataframes ---#
dt_concat = pd.concat([df_anim_, df_vege_])

#dt_concat = dt_concat.groupby('Zone').sum()

str6 = 'Disponibilité Alimentaire (Kcal/Personne/ans)'
str7 = 'Disponibilité De Protéines (Kg/Personne/ans)'
str8 = 'total_population_by_country'
colonnes = [str6, str7]

dt_concat[str6] = dt_concat[str3] * 365
dt_concat[str7] = dt_concat[str5] * 365/1000
#dt_concat = dt_concat[colonnes]

# Appeler la fonction calculant la population totale par pays
df_total_population_by_country = total_population_by_country()
new_df_total_population_by_country = df_total_population_by_country.set_index(
    'Zone')
new_df_total_population_by_country = pd.DataFrame(
    new_df_total_population_by_country[str8])

# Réaliser un inner merge
dt_concat = dt_concat.set_index('Zone')
df_inner = dt_concat.merge(new_df_total_population_by_country,
                           how='inner', left_index=True, right_index=True)

# Mettre un nouvel Index
df_inner = df_inner.reset_index(drop=False)

str9 = 'Disponibilité Alimentaire Totale (Kcal/ans)'
str10 = 'Disponibilité De Protéines Totale (Kg/ans)'

df_inner[str9] = df_inner[str6] * df_inner[str8]
df_inner[str10] = df_inner[str7] * df_inner[str8]
print(df_inner)

print("""
      """)
################################################################################################################################################################
print("""
      """)
########################################################################## Question 4 ##########################################################################
print("########################################################################## Question 4 ##########################################################################")
print("""
      """)

dt_concat_q4 = pd.concat([df_anim_, df_vege_])
dt_concat_q4 = dt_concat_q4.reset_index(drop=True)

print("################### Ajouter la colonne Ratio (Kcal/kg) ###################")

str0 = 'Zone'
str1 = 'Produit'
str2 = 'Disponibilité alimentaire (Kcal/personne/jour)'
str3 = 'Disponibilité alimentaire en quantité (kg/personne/an)'
str4 = 'Disponibilité de protéines en quantité (g/personne/jour)'
str5 = 'Ratio (Kcal/KG)'
str6 = 'Ratio (Kcal/100g)'
str7 = 'Ratio (Poids Protéines/Poids Total)'
str8 = 'Ratio (Poids Protéines/100g De Produit)'
str9 = 'Index_Prot'

colonnes = [str0, str1, str2, str3, str4, str9]
dt_concat_q4 = dt_concat_q4[colonnes]

dt_concat_q4.insert(4, str5, dt_concat_q4[str2] * 365 / dt_concat_q4[str3])
dt_concat_q4.insert(5, str6, dt_concat_q4[str2] * 365 / 10 / dt_concat_q4[str3])
dt_concat_q4.insert(6, str7, dt_concat_q4[str4] * 365 / 1000 / dt_concat_q4[str3])
dt_concat_q4.insert(7, str8, dt_concat_q4[str4] * 365 / 1000 / dt_concat_q4[str3] * 100)

colonnes = [str0, str1, str5, str6, str7, str8, str9]
dt_concat_q4 = dt_concat_q4[colonnes]

# Supprimer les cellules vides et lès remplacer par 0
dt_concat_q4 = dt_concat_q4.fillna(0)
dt_concat_q4 = dt_concat_q4[~(dt_concat_q4[dt_concat_q4.columns[2:]] == 0).any(axis=1)]

# Vérifier les résultats avec par exemple : Avoine, Œufs, Viande de Volailles
print("""
      """)
print("################### Chercher le ratio Kcal/KG d'un produit ###################")
print("""
      """)
def Recherche_ratio_prot_produit(str_check):
    dt_concat_q4_avoine = dt_concat_q4[dt_concat_q4['Produit'] == str_check]
    return

str_check = "Avoine"
Recherche_ratio_prot_produit(str_check)

print('################### Calcul moyenne mondiale par produit et par pays du Ratio (Kcal/KG)  ###################')
print("""
      """)
dt_concat_q4 = dt_concat_q4.groupby(['Produit', 'Zone'], dropna=True).mean()
print(dt_concat_q4)

################################################################################################################################################################


print("""
      """)
########################################################################## Question 5 ##########################################################################
print("########################################################################## Question 5 ##########################################################################")
print("""
      """)
print('################### Citez 5 aliments parmi les 20 aliments les plus caloriques, en utilisant le ratio énergie/poids. ###################')
print("""
      """)
dt_concat_q5 = dt_concat_q4.groupby(['Produit'], dropna=True).mean()
str_q5_Kcal_KG = 'Ratio (Kcal/KG)'
dt_concat_q5 = dt_concat_q5.sort_values(
    by=str_q5_Kcal_KG, ascending=False).head(20)
print(dt_concat_q5)
print("""
      """)
print(dt_concat_q5[str_q5_Kcal_KG])

print("""
      """)
print("################### Citez 5 aliments parmi les 20 aliments les plus riches en protéines ###################")
print("""
      """)

dt_concat_q5 = dt_concat_q4.groupby(['Produit'], dropna=True).mean()
strq5_Prot_Poids = 'Ratio (Poids Protéines/100g De Produit)'
dt_concat_q5 = dt_concat_q5.sort_values(
    by=strq5_Prot_Poids, ascending=False).head(20)
print(dt_concat_q5)
print("""
      """)
print(dt_concat_q5[strq5_Prot_Poids])


################################################################################################################################################################


print("""
      """)
########################################################################## Question 6 ##########################################################################
print("########################################################################## Question 6 ##########################################################################")
print("""
      """)

print("################### Calculez, pour les produits végétaux uniquement, la disponibilité intérieure mondiale exprimée en kcal. ###################")
print("""
      """)
###### Charger le fichier fr_vegetaux.csv #######
df_vegetaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv')

# Filtrage des données
df_vegetaux = df_vegetaux.fillna(0)
df_vegetaux = df_vegetaux.drop_duplicates()
indexNames = df_vegetaux[df_vegetaux['Zone'] == 'Chine'].index
df_vegetaux.drop(indexNames, inplace=True)
print("""
      """)
print(
    "################### Partie 1 : Sélectionner les colonnes utiles et mettre [Produit] comme index ###################")
print("""
      """)
str_Zone = 'Zone'
str_prodduis = 'Produit'
str_dispo_inter_pays = 'Disponibilité intérieure (kg/an)'
colonnes = [str_prodduis, str_Zone, str_dispo_inter_pays]
df_vegetaux = df_vegetaux[colonnes]
df_vegetaux = df_vegetaux.groupby(['Produit', 'Zone'], dropna=True).mean()

print("""
      """)
print("################### Partie 2 Sélectionner les colonnes utiles et mettre [Produit] comme index : ###################")
print("""
      """)
dt_concat_q4 = dt_concat_q4.reset_index(drop=False)
dt_concat_q5 = dt_concat_q4[['Produit', 'Ratio (Kcal/KG)']].groupby(['Produit'], dropna=True).mean()

print("""
      """)
print("################### Partie 3 : merge ###################")
print("""
      """)
df_outer_vegetaux = df_vegetaux.merge(dt_concat_q5, how='outer', left_index=True, right_index=True)

str = 'Disponibilité Intérieure Exprimée En Kcal'
str1 = 'Disponibilité intérieure (kg/an)'
str2 = 'Ratio (Kcal/KG)'

new_df_inner_vegetaux_1 = pd.DataFrame(df_outer_vegetaux)
new_df_inner_vegetaux_2 = new_df_inner_vegetaux_1.reset_index(drop=False)

new_df_inner_vegetaux_2.insert(4, str, (new_df_inner_vegetaux_2[str1] * new_df_inner_vegetaux_2[str2]))
print('''    
      ''')
print("################### Partie 4 : Calcul du total ###################")
print('''    
      ''')
print(new_df_inner_vegetaux_2)

Total = (new_df_inner_vegetaux_2[str]).sum()
print('''    
      ''')
print('Total de la disponibilité intérieure mondiale exprimée en kcal = ', Total, 'Kcal/Ans')
print('''    
      ''')

################################################################################################################################################################


print("""
      """)
########################################################################## Question 7 ##########################################################################
print("########################################################################## Question 7 ##########################################################################")
print("""
      """)
print("################### Combien d'humains pourraient être nourris si toute la disponibilité intérieure mondiale de produits végétaux était utilisée pour de la nourriture ? ###################")


" Besoin ou apports calorifiques conseillés (Kcal par jour) : Adulte Homme : 3000 Kcal"
"                                                             Adulte Femme : 2000 Kcal"

" Avec une population mondiale qui s'approche des 50% d'homme et de 50% de femme, la moyenne des besoins par adulte est de : 2500 Kcal"

" Le nombre dhabitans dans le monde en 2013 est de : 6997326000 Habitans"

# Total de la disponibilité intérieure mondiale en végetaux exprimée en kcal = : 1.5792749227092222e+16 Kcal/Ans
# Besoins par adulte : 2500 Kcal
print("""
      """)
total_veg_kcal = Total
Nbr_hab_2013 = Word_population_2013()
print("Le nombre de personnes adulte qu'on peut nourrire avec tout les végetaux est de : ", total_veg_kcal/(2500*365))
print()
print("Exprimé en terme de % : ", ((total_veg_kcal / (2500 * 365))/Nbr_hab_2013) * 100, '%')
print("""
      """)


print("################### Donnez les résultats en termes de calories, puis de protéines, et exprimez ensuite ces 2 résultats en pourcentage de la population mondiale. ####################")
print("""
      """)
###### Charger le fichier fr_vegetaux.csv #######
df_vegetaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv')

# Filtrage des données
df_vegetaux = df_vegetaux.fillna(0)
df_vegetaux = df_vegetaux.drop_duplicates()
indexNames = df_vegetaux[df_vegetaux['Zone'] == 'Chine'].index
df_vegetaux.drop(indexNames, inplace=True)

str_dispo_alim_Kcal_pays = 'Disponibilité alimentaire (Kcal/personne/jour)'
str_dispo_alim_Kcal_pays_totale = 'Disponibilité alimentaire totale (Kcal/jour)'
str_dispo_alim_prot_pays = 'Disponibilité de protéines en quantité (g/personne/jour)'
str_dispo_alim_prot_pays_totale = 'Disponibilité de protéines total(g/jour)'
colonnes = [str_prodduis, str_Zone,
            str_dispo_alim_Kcal_pays, str_dispo_alim_prot_pays]
df_vegetaux = df_vegetaux[colonnes]
df_vegetaux = df_vegetaux.set_index('Zone')

###### effectuer le merge #######
print("""
      """)
X = total_population_by_country()[['Zone', 'total_population_by_country']]
X = X.set_index('Zone')
df_vegetaux = df_vegetaux.merge(
    X, how='outer', left_index=True, right_index=True)


###### insertion des colonne pour les totaux #######
print("""
      """)
df_vegetaux.insert(4, str_dispo_alim_Kcal_pays_totale, (df_vegetaux[str_dispo_alim_Kcal_pays] * X['total_population_by_country']))
df_vegetaux.insert(5, str_dispo_alim_prot_pays_totale, (df_vegetaux[str_dispo_alim_prot_pays] * X['total_population_by_country']))

colonnes = [str_prodduis, str_dispo_alim_Kcal_pays_totale, str_dispo_alim_prot_pays_totale]
df_vegetaux = df_vegetaux[colonnes]

print("""
      """)
###### Calcul des totaux #######
print("""
      """)
Total_kcal = (df_vegetaux[str_dispo_alim_Kcal_pays_totale]).sum()*365
print('La disponibilité alimentaire mondiale exprimée en kcal = ', Total_kcal, 'Kcal/Ans')
print('''    
      ''')
Total_prot_g_j = (df_vegetaux[str_dispo_alim_prot_pays_totale]).sum()
print('La disponibilité mondiale totale de protéines végétales exprimée en g/jour = ', Total_prot_g_j, 'g/jour')
print('''    
      ''')

" Besoin ou apports calorifiques conseillés (Kcal par jour) : Adulte Homme          : 3000 Kcal"
"                                                             Adulte Femme          : 2000 Kcal"
"                                                             Besoint par adulte    : 2500 Kcal"

" Avec une population mondiale qui s'approche des 50% d'homme et de 50% de femme, la moyenne des besoins par adulte est de : 2500 Kcal"

" Le poids moyen d'un humain est de : 65 kg"

" Le besoin moyen d'un humain est de : 0.9 g/j/kg"

" Le nombre dhabitans dans le monde en 2013 est de : 6997326000 Habitans"


Nbr_hab_2013 = Word_population_2013()
print("Le nombre de personnes adulte qu'on peut nourrire avec tout les végetaux est de (en termes de calories): ", Total_kcal/(2500*365), 'Personnes')
print("Exprimé en terme de % : ", ((Total_kcal / (2500 * 365))/Nbr_hab_2013) * 100, '%')
print("""
      """)
print("Le nombre de personnes adulte qu'on peut nourrire avec tout les végetaux est de (en termes de protéines): ", Total_prot_g_j/(0.9*65), 'Personnes')
print("Exprimé en terme de % : ", ((Total_prot_g_j/(0.9*65))/Nbr_hab_2013) * 100, '%')
print("""
      """)
################################################################################################################################################################
print("""
      
      """)
########################################################################## Question 8 ##########################################################################
print("########################################################################## Question 8 ##########################################################################")
print("""
      """)
print("####################### Calculez, pour les produits végétaux uniquement, la disponibilité intérieure mondiale exprimée en kcal. #######################")
print("""
      """)
###### Charger le fichier fr_vegetaux.csv #######
df_vegetaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv')

# Filtrage des données
df_vegetaux = df_vegetaux.fillna(0)
df_vegetaux = df_vegetaux.drop_duplicates()
indexNames = df_vegetaux[df_vegetaux['Zone'] == 'Chine'].index
df_vegetaux.drop(indexNames, inplace=True)
# print(df_vegetaux)
print("""
      """)
print(
    "####################### Partie 1 : Sélectionner les colonnes utiles et mettre [Produit] comme index #######################")
print("""
      """)
X = total_population_by_country()[['Zone', 'total_population_by_country']]
X = X.set_index('Zone')

str_Zone = 'Zone'
str_prodduis = 'Produit'
#str_dispo_inter_pays = 'Disponibilité intérieure (kg/an)'
str_dispo_alim_pays = 'Disponibilité alimentaire en quantité (kg/personne/an)'
str_dispo_alim_pays_totale = 'Disponibilité alimentaire totale (kg/an)'
str_dispo_alim_Kcal_pays = 'Disponibilité alimentaire (Kcal/personne/jour)'
str_dispo_alim_Kcal_pays_totale = 'Disponibilité alimentaire totale (Kcal/jour)'
str_dispo_alim_prot_pays = 'Disponibilité de protéines en quantité (g/personne/jour)'
str_dispo_alim_prot_pays_totale = 'Disponibilité de protéines total(g/jour)'
str_alim_anim_pays = 'Aliments pour animaux (kg/an)'
str_pertes = 'Pertes (kg/an)'
str_total_kg = 'Total Veg Kg/An'

colonnes = [str_prodduis, str_Zone, str_dispo_alim_pays, str_dispo_alim_Kcal_pays, str_dispo_alim_prot_pays, str_alim_anim_pays, str_pertes]
df_vegetaux = df_vegetaux[colonnes]
df_vegetaux = df_vegetaux.set_index('Zone')
df_vegetaux = pd.DataFrame(df_vegetaux)
print("""
      """)
print("####################### Partie 2 : merge #######################")
print("""
      """)
df_vegetaux = df_vegetaux.merge(X, how='outer', left_index=True, right_index=True)

df_vegetaux.insert(2, str_dispo_alim_pays_totale, (df_vegetaux[str_dispo_alim_pays] * X['total_population_by_country']))
df_vegetaux.insert(5, str_dispo_alim_Kcal_pays_totale, (df_vegetaux[str_dispo_alim_Kcal_pays] * X['total_population_by_country']))
df_vegetaux.insert(6, str_dispo_alim_prot_pays_totale, (df_vegetaux[str_dispo_alim_prot_pays] * X['total_population_by_country']))
df_vegetaux.insert(4, str_total_kg, (df_vegetaux[str_dispo_alim_pays_totale] + df_vegetaux[str_alim_anim_pays] + df_vegetaux[str_pertes]))

df_vegetaux = df_vegetaux.groupby(['Produit', 'Zone'], dropna=True).sum()
select_colonne = [str_dispo_alim_pays_totale, str_alim_anim_pays, str_pertes, str_total_kg, str_dispo_alim_Kcal_pays_totale, str_dispo_alim_prot_pays_totale]
print(df_vegetaux[select_colonne])

print('''   
      ''')
print("####################### Partie 3 : Calcul des totaux #######################")
print("""
      """)
Total_kcal = (df_vegetaux[str_dispo_alim_Kcal_pays_totale]).sum()*365
print('La disponibilité alimentaire mondiale exprimée en kcal = ', Total_kcal, 'Kcal/Ans')
print('''    
      ''')

Total_Kg = (df_vegetaux[str_total_kg]).sum()
print('La disponibilité mondiale totale des végétaux exprimée en Kg = ', Total_Kg, 'Kg/Ans')
print('''    
      ''')

Total_prot_g_j = (df_vegetaux[str_dispo_alim_prot_pays_totale]).sum()
print('La disponibilité mondiale totale de protéines végétales exprimée en g/jour = ', Total_prot_g_j, 'g/jour')
print('''    
      ''')

" Besoin ou apports calorifiques conseillés (Kcal par jour) : Adulte Homme          : 3000 Kcal"
"                                                             Adulte Femme          : 2000 Kcal"
"                                                             Besoint par adulte    : 2500 Kcal"

" Avec une population mondiale qui s'approche des 50% d'homme et de 50% de femme, la moyenne des besoins par adulte est de : 2500 Kcal"

" Le poids moyen d'un humain est de : 65 kg"

" Le besoin moyen d'un humain est de : 0.9 g/j/kg"

" Le nombre dhabitans dans le monde en 2013 est de : 6997326000 Habitans"

Nbr_hab_2013 = Word_population_2013()
print("Le nombre de personnes adulte qu'on peut nourrire avec tout les végetaux est de (en termes de calories): ", Total_kcal/(2500*365), 'Personnes')
print()
print("Exprimé en terme de % : ", ((Total_kcal / (2500 * 365))/Nbr_hab_2013) * 100, '%')
print("""
      """)
print("Le nombre de personnes adulte qu'on peut nourrire avec tout les végetaux est de (en termes de protéines): ", Total_prot_g_j/(0.9*65), 'Personnes')
print()
print("Exprimé en terme de % : ", ((Total_prot_g_j/(0.9*65))/Nbr_hab_2013) * 100, '%')
print("""
      """)
################################################################################################################################################################


print("""  
      """)
########################################################################## Question 9 ##########################################################################
print("########################################################################## Question 9 ##########################################################################")
print("""
      """)
#######################  Combien d'humains pourraient être nourris avec la disponibilité alimentaire mondiale ?. #######################

###### Charger le fichier fr_animaux.csv #######
df_animaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_animaux.csv')
df_animaux = df_animaux.fillna(0)
df_animaux = df_animaux.drop_duplicates()
indexNames = df_animaux[df_animaux['Zone'] == 'Chine'].index
df_animaux.drop(indexNames, inplace=True)

###### Charger le fichier fr_vegetaux.csv #######
df_vegetaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv')

###### Filtrage des données ###### 
df_vegetaux = df_vegetaux.fillna(0)
df_vegetaux = df_vegetaux.drop_duplicates()
indexNames = df_vegetaux[df_vegetaux['Zone'] == 'Chine'].index
df_vegetaux.drop(indexNames, inplace=True)

#######################  Donnez les résultats en termes de calories, puis de protéines, et exprimez ensuite ces 2 résultats en pourcentage de la population mondiale. #######################

dt_concat = pd.concat([df_animaux, df_vegetaux])

str_Zone = 'Zone'
str_produis = 'Produit'
str_dispo_alim_Kcal_pays = 'Disponibilité alimentaire (Kcal/personne/jour)'
str_dispo_alim_Kcal_pays_totale = 'Disponibilité alimentaire totale (Kcal/jour)'
str_dispo_alim_prot_pays = 'Disponibilité de protéines en quantité (g/personne/jour)'
str_dispo_alim_prot_pays_totale = 'Disponibilité de protéines total(g/jour)'
colonnes = [str_Zone, str_produis, str_dispo_alim_Kcal_pays, str_dispo_alim_prot_pays]
dt_concat = dt_concat[colonnes]
dt_concat = dt_concat.set_index('Zone')

X = total_population_by_country()[['Zone', 'total_population_by_country']]
X = X.set_index('Zone')

####################### merge #######################

dt_concat = dt_concat.merge(X, how='outer', left_index=True, right_index=True)

####################### Insertion des colonnes pour le calcul des totaux #######################

dt_concat.insert(4, str_dispo_alim_Kcal_pays_totale, (dt_concat[str_dispo_alim_Kcal_pays] * X['total_population_by_country']))
dt_concat.insert(5, str_dispo_alim_prot_pays_totale, (dt_concat[str_dispo_alim_prot_pays] * X['total_population_by_country']))

#dt_concat = dt_concat.groupby(['Produit', 'Zone'], dropna=True).sum()
colonnes = [str_produis, str_dispo_alim_Kcal_pays_totale, str_dispo_alim_prot_pays_totale]
#print(dt_concat[colonnes])

print("####################### Calcul des totaux #######################")
print("""
      """)
Total_kcal = (dt_concat[str_dispo_alim_Kcal_pays_totale]).sum()*365
print('La disponibilité alimentaire mondiale exprimée en kcal = ', Total_kcal, 'Kcal/Ans')
print()
Total_prot_g_j = (dt_concat[str_dispo_alim_prot_pays_totale]).sum()
print('La disponibilité mondiale totale de protéines exprimée en g/jour = ', Total_prot_g_j, 'g/jour')
print('''    
      ''')

" Besoin ou apports calorifiques conseillés (Kcal par jour) : Adulte Homme          : 3000 Kcal"
"                                                             Adulte Femme          : 2000 Kcal"
"                                                             Besoint par adulte    : 2500 Kcal"

" Avec une population mondiale qui s'approche des 50% d'homme et de 50% de femme, la moyenne des besoins par adulte est de : 2500 Kcal"

" Le poids moyen d'un humain est de : 65 kg"

" Le besoin moyen d'un humain est de : 0.9 g/j/kg"

" Le nombre dhabitans dans le monde en 2013 est de : 6997326000 Habitans"

Nbr_hab_2013 = Word_population_2013()
print("Le nombre de personnes adulte qu'on peut nourrire (en termes de calories): ", Total_kcal/(2500*365), 'Personnes')
print()
print("Exprimé en terme de % : ", ((Total_kcal / (2500 * 365))/Nbr_hab_2013) * 100, '%')
print("""
      """)
print("Le nombre de personnes adulte qu'on peut nourrire (en termes de protéines): ", Total_prot_g_j/(0.9*65), 'Personnes')
print()
print("Exprimé en terme de % : ", ((Total_prot_g_j/(0.9*65))/Nbr_hab_2013) * 100, '%')
print("""
      """)
################################################################################################################################################################


########################################################################## Question 10 ##########################################################################
print("########################################################################## Question 10 ##########################################################################")
print("""
      """)
print("#######################  Question 10 : A partir des données téléchargées qui concernent la sous-nutrition, répondez à cette question : Quelle proportion de la population mondiale est considérée comme étant en sous-nutrition ? #######################")


################### Charger le fichier fr_sousalimentation.csv ###################
df_sousalimentation = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_sousalimentation.csv')
df_sousalimentation.drop_duplicates()
print('''
      ''')
################### Selectionner les colonne qu'on va utiliser ###################
print('''    
      ''')
my_column = ['Zone', 'Année', 'Valeur']
df_sousalimentation = df_sousalimentation[my_column]

################### Filtrage ###################

df_sousalimentation['Valeur'] = df_sousalimentation['Valeur'].str.replace(r'<0.1', '0.1').astype('float')
indexNames = df_sousalimentation[df_sousalimentation['Zone'] == 'Chine'].index
df_sousalimentation.drop(indexNames, inplace=True)
#df_sousalimentation.style.set_properties(**{'text-align': 'left'})
print(df_sousalimentation)

print('''    
      ''')
################ Appliquer le mean() ################
print('''    
      ''')
################ Conversion de la colonne [Valeur] de Objet en float64 ################
df_sousalimentation['Valeur'] = df_sousalimentation['Valeur'].astype(float)
df_sousalim = df_sousalimentation.groupby(['Zone'])['Valeur'].mean()
df_sousalim = pd.DataFrame(df_sousalim)

#########--- Charger le Fichier fr_population.csv' ---########
df_fr_population = total_population_by_country()
my_column = ['Zone', 'total_population_by_country']
df_fr_population = df_fr_population[my_column]

#########--- Changer l'index et le mettre sur la colonne Zone ---########
df_fr_population = df_fr_population.set_index('Zone')

#########--- Effectuer un merge sur l'index Zone ---########
df_outer_sousalim = df_sousalim.merge(df_fr_population, how='outer', left_index=True, right_index=True)
print(df_outer_sousalim)

#########--- Filtrage des données ---########
df_outer_sousalim = df_outer_sousalim.fillna(0)
df_outer_sousalim = df_outer_sousalim.drop_duplicates()
df_outer_sousalim = df_outer_sousalim[~(df_outer_sousalim[df_outer_sousalim.columns[1:]] == 0).any(axis=1)]


str1 = 'Valeur'
str2 = 'total_population_by_country'
str3 = 'Pourcentage Sous-nutrition Par Pays'

df_outer_sousalim.insert(2, str3, df_outer_sousalim[str1] * 10**6 / df_outer_sousalim[str2] * 100)
df_outer_sousalim = pd.DataFrame(df_outer_sousalim)
print(df_outer_sousalim)
" Le nombre dhabitans dans le monde en 2013 est de : 6997326000 Habitans"
Nbr_hab_2013 = Word_population_2013()
print('''    
      ''')
print("La proportion de la population mondiale considérée comme étant en sous-nutrition est de : ", 10**6 * df_outer_sousalim['Valeur'].sum() / Nbr_hab_2013 * 100, '%')
print("""
      """)

print("####################### Établissez la liste des produits (ainsi que leur code) considérés comme des céréales selon la FAO.  #######################")
print("""
      """)
df_cereales = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_céréales.csv')
df_cereales.drop_duplicates()
df_cereales_Produit = df_cereales[['Produit', 'Code Produit']]
df_cereales_Produit = df_cereales_Produit.drop_duplicates()

print('liste des produits Céréales (ainsi que leur code) :')
print("""
      """)
print(df_cereales_Produit)
print("""
      """)
print(
    "####################### Repérez dans vos données les informations concernant les céréales (par exemple en créant une colonne de type booléen nommée [is_cereal]. #######################")
print("""
      """)
df_vegetaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv')
df_vegetaux.drop_duplicates()
df_vegetaux_Produit = df_vegetaux[['Produit']]
df_vegetaux_Produit = df_vegetaux_Produit.drop_duplicates()
print('liste des produits végétaux :')
print("""
      """)
print(df_vegetaux_Produit)

print("""
      """)
print('Reperer les produits Céréales dans le fichier végétaux (ainsi que leur code) :')
print("""
      """)
left_merge = pd.merge(df_vegetaux_Produit, df_cereales_Produit, on='Produit', how='left')
print(left_merge)
print("""
      """)
left_merge.loc[left_merge['Code Produit'].isna(), 'is_cereal'] = '0'
left_merge.loc[~left_merge['Code Produit'].isna(), 'is_cereal'] = '1'
print(left_merge)

################################################################################################################################################################

print("""
      """)
########################################################################## Question 11 ##########################################################################
print("########################################################################## Question 11 ##########################################################################")
print("""
      """)
####################### Partie 1 : Charger le fichier fr_céréales.csv et Selectionner les colonne qu'on va utiliser  #######################

###### Charger le fichier fr_céréales.csv #######
df_cereales = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_céréales.csv')
df_cereales.drop_duplicates()

my_column = ['Zone', 'Code Produit', 'Produit', 'Unité', 'Valeur']
df_cereales = df_cereales[my_column]

df_cereales_Produit = df_cereales['Produit']
df_cereales_Produit = df_cereales_Produit.drop_duplicates()
print(" La liste des céréales est : ")
print("""
      """)
print(df_cereales_Produit)

df_cereales_Produit = pd.DataFrame(df_cereales_Produit)

####################### Partie 2 : Charger le fichier fr_vegetaux.csv et Selectionner les colonne qu'on va utiliser  #######################

###### Charger le fichier fr_vegetaux.csv #######
df_vegetaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv')

###### Filtrage des données ###### 
df_vegetaux = df_vegetaux.fillna(0)
df_vegetaux = df_vegetaux.drop_duplicates()
indexNames = df_vegetaux[df_vegetaux['Zone'] == 'Chine'].index
df_vegetaux.drop(indexNames, inplace=True)

str_Zone = 'Zone'
str_prodduis = 'Produit'
str_alim_anim = 'Aliments pour animaux (kg/an)'
str_alim_pers_pays = 'Disponibilité alimentaire en quantité (kg/personne/an)'
str_total_cere_kg = 'Total Cereales Kg/An'

colonnes = [str_prodduis, str_Zone, str_alim_pers_pays, str_alim_anim]
df_vegetaux = df_vegetaux[colonnes]

df_merge_cereales_Produit = df_vegetaux.merge(df_cereales_Produit, left_on='Produit', right_on='Produit')

hab_pays_2013 = total_population_by_country()
hab_pays_2013 = hab_pays_2013[['Zone', 'total_population_by_country']]

df_merge_cereales_Produit = df_merge_cereales_Produit.merge(hab_pays_2013, left_on='Zone', right_on='Zone')

df_merge_cereales_Produit['total_population_by_country'] = df_merge_cereales_Produit['total_population_by_country'].astype(float)

df_merge_cereales_Produit.insert(5, str_total_cere_kg, df_merge_cereales_Produit['Disponibilité alimentaire en quantité (kg/personne/an)'] * df_merge_cereales_Produit['total_population_by_country'])

print("""
      """)
A = df_merge_cereales_Produit['Aliments pour animaux (kg/an)'].sum()
B = df_merge_cereales_Produit['Total Cereales Kg/An'].sum()

print("Poids total des Aliments pour animaux (kg/an) 2013 = ", A)
print()
print("Poids total des céréales dans le monde en 2013 = ", A+B)
print("""
      """)
print("Rapport poids Aliments pour animaux / Poids total des Cereales = ", A/(A+B))
print()
print("Exprimé en % = ", 100 * A/(A+B), '%')

print("""
      """)
print("########### Sélectionnez parmi les données des bilans alimentaires les informations relatives aux pays dans lesquels la FAO recense des personnes en sous-nutrition. ###########")
print("""
      """)
# La Sécurité Alimentaire et la Nutrition dans le Monde
# https://www.fao.org/state-of-food-security-nutrition/2018/fr/

# Ici on choisi 11 comme limite (Moyenne FAO Malnutrition dans le Monde 2013)
#df_outer_sousalim.sort_values(by='Pourcentage Sous-nutrition Par Pays', ascending=False).to_csv(r'/home/fury/Bureau/Test/df_outer_sousalim.csv')
#print(df_outer_sousalim.sort_values(by='Pourcentage Sous-nutrition Par Pays', ascending=False))
df_outer_sousalim_sort = df_outer_sousalim[df_outer_sousalim['Pourcentage Sous-nutrition Par Pays']> 0].sort_values(by='Pourcentage Sous-nutrition Par Pays', ascending=False)
my_column = ['Pourcentage Sous-nutrition Par Pays']
df_outer_sousalim_sort = df_outer_sousalim_sort[my_column]
df_outer_sousalim_sort = df_outer_sousalim_sort.reset_index()
print("""
      """)
print('Les pays en Sous-nutrition sont : ')
print("""
      """)
print(df_outer_sousalim_sort)
print("""
      """)
####################### Partie 1 : Charger les fichiers fr_vegetaux.csv, fr_animaux.csv, et  Selectionner les colonnes qu'on va utiliser  #######################

###### Charger le fichier fr_animaux.csv #######
df_animaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_animaux.csv')
df_animaux = df_animaux.fillna(0)
df_animaux = df_animaux.drop_duplicates()
indexNames = df_animaux[df_animaux['Zone'] == 'Chine'].index
df_animaux.drop(indexNames, inplace=True)


###### Charger le fichier fr_vegetaux.csv #######
df_vegetaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv')
# Filtrage des données
df_vegetaux = df_vegetaux.fillna(0)
df_vegetaux = df_vegetaux.drop_duplicates()
indexNames = df_vegetaux[df_vegetaux['Zone'] == 'Chine'].index
df_vegetaux.drop(indexNames, inplace=True)

#################################################################################################################################################################

df_concat_veg_anim = pd.concat([df_vegetaux, df_animaux])
df_concat_veg_anim = df_concat_veg_anim.set_index('Zone')

df_merge_sousalim_sort = df_outer_sousalim_sort.merge(df_concat_veg_anim, left_on='Zone', right_on='Zone')


print("""
      """)
print("########### Repérez les 15 produits les plus exportés par ce groupe de pays. ###########")
print("""
      """)

my_column = ['Zone', 'Produit', 'Exportations - Quantité (kg/an)', 'Autres utilisations (non alimentaire) (kg/an)',
             'Disponibilité intérieure (kg/an)', 'Aliments pour animaux (kg/an)', 'Disponibilité alimentaire en quantité (kg/personne/an)']
df_merge_sousalim_sort = df_merge_sousalim_sort[my_column]
df_merge_sousalim_sort = df_merge_sousalim_sort.groupby('Produit').sum().sort_values(by='Exportations - Quantité (kg/an)', ascending=False).head(15)
print("""
      """)
print("les 15 produits les plus exportés par ce groupe de pays : ")
print("""
      """)
print(df_merge_sousalim_sort['Exportations - Quantité (kg/an)'])

print("""
      """)
print("########### Parmi les données des bilans alimentaires au niveau mondial, sélectionnez les 200 plus grandes            ###########")
print("########### importations de ces produits (1 importation = une quantité d'un produit donné importée par un pays donné) ###########")
print("""
      """)


df_concat_veg_anim = pd.concat([df_vegetaux, df_animaux])
df_concat_veg_anim = df_concat_veg_anim.set_index('Produit')
my_column = ['Zone', 'Importations - Quantité (kg/an)']
df_concat_veg_anim = df_concat_veg_anim[my_column]
print(df_merge_sousalim_sort)
df_merge_sousalim_sort = df_merge_sousalim_sort.merge(df_concat_veg_anim, left_on='Produit', right_on='Produit')
df_merge_sousalim_sort = df_merge_sousalim_sort.reset_index()

print("les 200 plus grandes importations de ces produits : ")
print("""
      """)
print((df_merge_sousalim_sort[['Zone', 'Produit',  'Importations - Quantité (kg/an)']]).sort_values(by='Importations - Quantité (kg/an)', ascending=False).head(200))
#(df_merge_sousalim_sort[['Zone', 'Produit',  'Importations - Quantité (kg/an)']]).sort_values(by='Importations - Quantité (kg/an)', ascending=False).head(200).to_csv(r'/home/fury/Bureau/Test/df_merge_sousalim_sort1.csv')


print("""
      """)
print("########### Groupez ces importations par produit, afin d'avoir une table contenant 1 ligne pour chacun des 15 produits. ###########")
print("""
      """)

df_merge_sousalim_sort = df_merge_sousalim_sort[['Zone', 'Produit',  'Importations - Quantité (kg/an)']].groupby('Produit').sum()
print(df_merge_sousalim_sort)

print("""
      """)
################## le ratio entre la quantité destinés aux Autres utilisations (Other uses) et la disponibilité intérieure. ##################
print("""
      """)

X = total_population_by_country()[['Zone', 'total_population_by_country']]
X = X.set_index('Zone')

df_concat_veg_anim = pd.concat([df_vegetaux, df_animaux])
df_concat_veg_anim = df_concat_veg_anim.set_index('Zone')

df_concat_veg_anim = df_concat_veg_anim.merge(X, how='outer', left_index=True, right_index=True)
df_concat_veg_anim.insert(6, 'Disponibilité alimentaire (kg/an)', df_concat_veg_anim['Disponibilité alimentaire en quantité (kg/personne/an)'] * X['total_population_by_country'])

colonnes = ['Produit', 'Autres utilisations (non alimentaire) (kg/an)', 'Disponibilité intérieure (kg/an)', 'Aliments pour animaux (kg/an)', 'Disponibilité alimentaire (kg/an)']
df_concat_veg_anim = df_concat_veg_anim[colonnes]

list_of_values = df_merge_sousalim_sort.index.tolist()
df_concat_veg_anim = df_concat_veg_anim.loc[df_concat_veg_anim['Produit'].isin(list_of_values)]

df_concat_veg_anim = df_concat_veg_anim.groupby('Produit').sum()
#df_concat_veg_anim.to_csv(r'/home/fury/Bureau/Test/df_me.csv')

df_concat_veg_anim.insert(2, 'Ratio Autres utilisations/Disponibilité intérieure %', df_concat_veg_anim['Autres utilisations (non alimentaire) (kg/an)'] * 100 / df_concat_veg_anim['Disponibilité intérieure (kg/an)'])
df_concat_veg_anim = df_concat_veg_anim.reset_index()
print("Le ratio entre la quantité destinés aux Autres utilisations (Other uses) et la disponibilité intérieure (ratio exprimé en pourcentage '%'). :")
print("""
      """)
print(df_concat_veg_anim[['Produit', 'Ratio Autres utilisations/Disponibilité intérieure %']])
print()

print("""
      """)
######## le ratio entre la quantité destinée à la nourriture animale et la quantité destinée à la nourriture (animale + humaine) ########
df_concat_veg_anim.insert(5, 'Ratio Aliments pour animaux /Aliments pour animaux + Disponibilité alimentaire en %', df_concat_veg_anim['Aliments pour animaux (kg/an)'] * 100 / (df_concat_veg_anim['Aliments pour animaux (kg/an)']+df_concat_veg_anim['Disponibilité alimentaire (kg/an)']))
df_concat_veg_anim = df_concat_veg_anim.reset_index()
print("Le ratio entre la quantité destinée à la nourriture animale et la quantité destinée à la nourriture (animale + humaine) :")
print("""
      """)
print(df_concat_veg_anim[['Produit', 'Ratio Aliments pour animaux /Aliments pour animaux + Disponibilité alimentaire en %']])

print("""
      """)
########################################################################## Question 12 ##########################################################################
print("########################################################################## Question 12 ##########################################################################")
print("""
      """)
print('Donnez les 3 produits qui ont la plus grande valeur pour chacun des 2 ratios (vous aurez donc 6 produits à citer).')
print("""
      """)
################ Donnez les 3 produits qui ont la plus grande valeur pour chacun des 2 ratios (vous aurez donc 6 produits à citer). ################

str_A = 'Ratio Autres utilisations/Disponibilité intérieure %'
A = df_concat_veg_anim[['Produit', 'Ratio Autres utilisations/Disponibilité intérieure %']].sort_values(by=str_A, ascending=False).head(3)
print(A)

print("""
      """)
str_B = 'Ratio Aliments pour animaux /Aliments pour animaux + Disponibilité alimentaire en %'
B = df_concat_veg_anim[['Produit', 'Ratio Aliments pour animaux /Aliments pour animaux + Disponibilité alimentaire en %']].sort_values(by=str_B, ascending=False).head(3)
print(B)



################################################################################################################################################################


print("""
      """)
########################################################################## Question 13 ##########################################################################
print("########################################################################## Question 13 ##########################################################################")
print("""
      """)
################ Combien de tonnes de céréales pourraient être libérées si les USA diminuaient leur production de produits animaux de 10% ?. ################

###### Charger le fichier fr_céréales.csv #######
df_cereales = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_céréales.csv')
df_cereales.drop_duplicates()
str_usa = """États-Unis d'Amérique"""
indexNames = df_cereales[df_cereales['Zone'] != str_usa].index
df_cereales.drop(indexNames, inplace=True)
df_cereales = df_cereales[['Zone', 'Produit', 'Valeur']]
df_cereales.insert(3, 'Total Valeur en tonnes', df_cereales['Valeur'] * 1000)
print(df_cereales)
print("""
      """)
###### Charger le fichier fr_vegetaux.csv #######
df_vegetaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv')
# Filtrage des données
df_vegetaux = df_vegetaux.fillna(0)
df_vegetaux = df_vegetaux.drop_duplicates()
indexNames = df_vegetaux[df_vegetaux['Zone'] == 'Chine'].index
df_vegetaux.drop(indexNames, inplace=True)
indexNames = df_vegetaux[df_vegetaux['Zone'] != str_usa].index
df_vegetaux.drop(indexNames, inplace=True)


df_merge_usa = df_cereales.merge(df_vegetaux, left_on='Produit', right_on='Produit')
print(df_merge_usa)
df_merge_usa = df_merge_usa['Aliments pour animaux (kg/an)'].sum()
print(df_merge_usa)
print()
print('Le poids total des Aliments pour animaux (kg/an) au USA est de : ',df_merge_usa, 'Kg')
print()
print('10% du total =                                                   ',df_merge_usa/10, 'Kg')
print()
print('10% du total exprimé en tonnes =                                 ',df_merge_usa/(10*1000), 'Tonnes')

################################################################################################################################################################


print("""
      """)
########################################################################## Question 14 ##########################################################################
print("########################################################################## Question 14 ##########################################################################")
print("""
      """)
################ En Thaïlande, quelle proportion de manioc produit est exportée ? Quelle est la proportion de personnes en sous-nutrition ? ################

###### Charger le fichier fr_vegetaux.csv #######

df_vegetaux = pd.read_csv(r'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv')
# Filtrage des données
df_vegetaux = df_vegetaux.fillna(0)
df_vegetaux = df_vegetaux.drop_duplicates()
indexNames = df_vegetaux[df_vegetaux['Zone'] != 'Thaïlande'].index
df_vegetaux.drop(indexNames, inplace=True)
indexNames = df_vegetaux[df_vegetaux['Produit'] != 'Manioc'].index
df_vegetaux.drop(indexNames, inplace=True)

A = df_vegetaux['Exportations - Quantité (kg/an)'].sum()
B = df_vegetaux['Production (kg/an)'].sum()
print("En Thaïlande, la proportion de manioc produit et exportée ", A/B)
print()
print("Exprimé en %                                               ", 100*A/B, '%')
print("""
      """)
################################################################################################################################################################
