
/*
/****** Question 15 : Proposez une clé primaire pertinente pour cette table.  ******/
*/

USE [Projet_3]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].[fr_population]

/****** Object:  Table [dbo].[fr_population]    Script Date: 14/11/2021 14:25:47 ******/
CREATE TABLE [dbo].[fr_population](
	[Code_Domaine] [nvarchar](50) NOT NULL,
	[Domaine] [nvarchar](100) NOT NULL,
	[Code_zone] [nvarchar](50) NOT NULL,
	[Zone] [nvarchar](50) NOT NULL,
	[Code_Élément] [int] NOT NULL,
	[Élément] [nvarchar](50) NOT NULL,
	[Code_Produit] [int] NOT NULL,
	[Produit] [nvarchar](50) NOT NULL,
	[Code_année] [int] NOT NULL,
	[Année] [int] NOT NULL,
	[Unité] [nvarchar](50) NOT NULL,
	[Valeur] [int] NOT NULL,
	[Symbole] [nvarchar](50) NULL,
	[Description_du_Symbole] [nvarchar](100) NOT NULL
) ON [PRIMARY]
GO


/****** Object:  Charger le fichier fr_population.csv la table Table  [dbo].[fr_population] ******/
BULK INSERT [dbo].[fr_population]
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
	GO

DELETE FROM [Projet_3].[dbo].[fr_population]

/****** La clé primaire pertinante est Zone.  ******/
ALTER TABLE [Projet_3].[dbo].[fr_population] ADD PRIMARY KEY ([Zone], [Année]);
ALTER TABLE [Projet_3].[dbo].[fr_population] ADD CONSTRAINT PK_pop_ann PRIMARY KEY ([Zone], [Année])


DELETE FROM [Projet_3].[dbo].[fr_population]
WHERE [Zone] = 'Chine'

UPDATE [Projet_3].[dbo].[fr_population]
SET [Valeur] = [Valeur]*1000

SELECT TOP (1000) 
	   [Zone] as [pays]
      ,[Code_zone] as [code_pays]
      ,[Année] as [annee]
      ,[Valeur] as [population] 
  FROM [Projet_3].[dbo].[fr_population]


-------------------------------------------------------------------------------------------------------------------------------------------------------
--###################################################################################################################################################--
-------------------------------------------------------------------------------------------------------------------------------------------------------
/*
/****** Question 16 : Proposez une clé primaire pertinente pour cette table.  ******/
*/

BULK INSERT [dbo].[fr_animaux]
    FROM 'C:\Users\FURY\Desktop\Projet_3 SQL\fr_animaux.csv'
    WITH
    (
	FORMAT = 'CSV',		
    FIRSTROW = 2,
	CODEPAGE = '65001',
    FIELDTERMINATOR = ',',  --CSV field delimiter
	ROWTERMINATOR = '0x0a',
    --ROWTERMINATOR = '\n',   --Use to shift the control to next row
    ERRORFILE = 'C:\Users\FURY\Desktop\Projet_3 SQL\fr_animauxErrorRows.csv'
    )
	GO

DELETE FROM [dbo].[fr_animaux]

BULK INSERT [dbo].[fr_vegetaux]
    FROM 'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetaux.csv'
    WITH
    (
	FORMAT = 'CSV',		
    FIRSTROW = 2,
	CODEPAGE = '65001',
    FIELDTERMINATOR = ',',  --CSV field delimiter
	ROWTERMINATOR = '0x0a',
    --ROWTERMINATOR = '\n',   --Use to shift the control to next row
    ERRORFILE = 'C:\Users\FURY\Desktop\Projet_3 SQL\fr_vegetauxErrorRows.csv'
    )
	GO

DELETE FROM [dbo].[fr_vegetaux]

DELETE FROM [Projet_3].[dbo].[fr_animaux]   
WHERE [Zone] = 'Chine'
DELETE FROM [Projet_3].[dbo].[fr_vegetaux]
WHERE [Zone] = 'Chine'

SELECT * FROM [dbo].[fr_animaux]
SELECT * FROM [dbo].[fr_vegetaux]


DELETE FROM [Projet_3].[dbo].[dispo_alim]
DELETE FROM [Projet_3].[dbo].[fr_animaux]
DELETE FROM [Projet_3].[dbo].[fr_vegetaux]
--------------------------------------------

ALTER TABLE [Projet_3].[dbo].[dispo_alim]
ADD [nature du produit] VARCHAR (255)

ALTER TABLE [Projet_3].[dbo].[fr_animaux]
ADD [nature du produit] VARCHAR (255)
CONSTRAINT valeur_par_defaut_ani DEFAULT 'animal'
WITH VALUES

ALTER TABLE [Projet_3].[dbo].[fr_vegetaux]
ADD [nature du produit] VARCHAR (255)
CONSTRAINT valeur_par_defaut_veg DEFAULT 'végétal'
WITH VALUES
--------------------------------------------

INSERT INTO [Projet_3].[dbo].[dispo_alim]
SELECT * FROM [Projet_3].[dbo].[fr_animaux]

INSERT INTO [Projet_3].[dbo].[dispo_alim]
SELECT * FROM [Projet_3].[dbo].[fr_vegetaux]
--------------------------------------------

ALTER TABLE [Projet_3].[dbo].[dispo_alim]
ALTER COLUMN [Disponibilité_alimentaire_en_quantité_kg_personne_an] FLOAT;
--------------------------------------------

UPDATE [Projet_3].[dbo].[dispo_alim]
SET [Disponibilité_alimentaire_en_quantité_kg_personne_an] = [Disponibilité_alimentaire_en_quantité_kg_personne_an]/1000
--------------------------------------------

ALTER TABLE [Projet_3].[dbo].[dispo_alim]
ADD [annee] INT 
CONSTRAINT valeur_par_defaut_annee DEFAULT 2013
WITH VALUES
--------------------------------------------

/****** La clé primaire pertinante est la clé composite ([Zone], [Produit]).  ******/
ALTER TABLE [Projet_3].[dbo].[dispo_alim] ADD PRIMARY KEY ([Zone], [Produit]);
ALTER TABLE [Projet_3].[dbo].[dispo_alim] ADD CONSTRAINT PK_dispo_alim PRIMARY KEY ([Zone], [Produit])
/****** Ici on crée un index unique à  la clé composite ([Zone], [Produit]).  ******/
--CREATE UNIQUE INDEX idx1 ON [Projet_3].[dbo].[dispo_alim] ([Zone], [Produit]);

ALTER TABLE [Projet_3].[dbo].[dispo_alim]
DROP CONSTRAINT [[PK__dispo_al__34B4370F5F692BA5]]
--------------------------------------------

SELECT * FROM [Projet_3].[dbo].[dispo_alim]
	  LEFT OUTER JOIN [Projet_3].[dbo].[fr_population] ON [Projet_3].[dbo].[dispo_alim].Zone = [Projet_3].[dbo].[fr_population].Zone
--------------------------------------------

SELECT *
FROM  [Projet_3].[dbo].[fr_vegetaux] AS V
LEFT OUTER JOIN [Projet_3].[dbo].[fr_population] AS P ON V.[Zone] = P.[Zone]
--------------------------------------------

SELECT 
	   P.[Zone] AS [pays]
	  ,P.[Code_zone] AS [Code_pays]
	  ,P.[Année] AS [annee]
      ,V.[Produit] AS [produit]
	  ,V.[nature du produit] AS [origin]
	  --,[Disponibilité_alimentaire_en_quantité_kg_personne_an]
	  ,[Disponibilité_alimentaire_en_quantité_kg_personne_an] * P.[Valeur] / 1000 AS [dispo_alim_tonnes]
	  ,[Disponibilité_alimentaire_Kcal_personne_jour] AS [dispo_alim_kcal_p_j]
	  ,[Disponibilité_de_protéines_en_quantité_g_personne_jour] AS [dispo_prot]
	  ,[Disponibilité_de_matière_grasse_en_quantité_g_personne_jour] AS [dispo_mat_gr]
	  ,[Valeur] AS [population]
FROM  [Projet_3].[dbo].[dispo_alim] AS V
LEFT OUTER JOIN [Projet_3].[dbo].[fr_population] AS P ON V.[Zone] = P.[Zone]



-------------------------------------------------------------------------------------------------------------------------------------------------------
--###################################################################################################################################################--
-------------------------------------------------------------------------------------------------------------------------------------------------------
/*
/****** Question 17 : Proposez une clé primaire pertinente pour cette table.  ******/
*/

USE [Projet_3]
GO

/****** Object:  Table [dbo].[equilibre_prod]    Script Date: 16/11/2021 15:11:22 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [Projet_3].[dbo].[equilibre_prod] (
	[Zone] [nvarchar](50) NOT NULL,
	[Code_zone] [int] NOT NULL,
	[Produit] [nvarchar](50) NOT NULL,
	[Aliments_pour_animaux_kg_an] [nvarchar](50) NULL,
	[Autres_utilisations_non_alimentaire_kg_an] [nvarchar](50) NULL,
	[Disponibilité_alimentaire_Kcal_personne_jour] [nvarchar](50) NULL,
	[Disponibilité_alimentaire_en_quantité_kg_personne_an] [float] NULL,
	[Disponibilité_de_matière_grasse_en_quantité_g_personne_jour] [nvarchar](50) NULL,
	[Disponibilité_de_protéines_en_quantité_g_personne_jour] [nvarchar](50) NULL,
	[Disponibilité_intérieure_kg_an] [nvarchar](50) NULL,
	[Exportations_Quantité_kg_an] [nvarchar](50) NULL,
	[Importations_Quantité_kg_an] [nvarchar](50) NULL,
	[Nourriture_kg_an] [nvarchar](50) NULL,
	[Pertes_kg_an] [nvarchar](50) NULL,
	[Production_kg_an] [nvarchar](50) NULL,
	[Semences_kg_an] [nvarchar](50) NULL,
	[Traitement_kg_an] [nvarchar](50) NULL,
	[Variation_de_stock_kg_an] [nvarchar](50) NULL,
	[nature du produit] [varchar](255) NULL,
	)
	GO

INSERT INTO [Projet_3].[dbo].[equilibre_prod]
SELECT * FROM [Projet_3].[dbo].[fr_animaux]

INSERT INTO [Projet_3].[dbo].[equilibre_prod]
SELECT * FROM [Projet_3].[dbo].[fr_vegetaux]

--------------------------------------------
DELETE FROM [Projet_3].[dbo].[equilibre_prod]
WHERE [Zone] = 'Chine'

SELECT *
  FROM [Projet_3].[dbo].[equilibre_prod] ORDER BY ZONE

ALTER TABLE [Projet_3].[dbo].[equilibre_prod]
ADD [annee] INT 
CONSTRAINT v_par_annee DEFAULT 2013
WITH VALUES

SELECT	 
		 [Zone] AS [pays]
		,[Code_zone] AS [code_pays]
		,[annee] AS [annee]
		,[Produit] AS [produit]
		,[nature du produit]AS [code_produit]
	    ,[Disponibilité_intérieure_kg_an]AS [dispo_int]		
		,[Aliments_pour_animaux_kg_an]AS [alim_ani]
		,[Pertes_kg_an]AS [pertes]
		,[Semences_kg_an] AS [semences]
		,[Autres_utilisations_non_alimentaire_kg_an]

  FROM [Projet_3].[dbo].[equilibre_prod]


/****** La clé primaire pertinante est la clé composite ([Zone], [Produit]).  ******/
/*
ALTER TABLE [Projet_3].[dbo].[equilibre_prod]
DROP CONSTRAINT [PK__dispo_al__34B4370F05E91970]
*/
--ALTER TABLE [Projet_3].[dbo].[equilibre_prod] ADD PRIMARY KEY ([Zone], [Produit]);
ALTER TABLE [Projet_3].[dbo].[equilibre_prod] ADD CONSTRAINT PK_equilibre_prod PRIMARY KEY ([Zone], [Produit])
/****** Ici on crée un index unique à  la clé composite ([Zone], [Produit]).  ******/
--CREATE UNIQUE INDEX idx1 ON [Projet_3].[dbo].[equilibre_prod] ([Zone], [Produit]);
--------------------------------------------


-------------------------------------------------------------------------------------------------------------------------------------------------------
--###################################################################################################################################################--
-------------------------------------------------------------------------------------------------------------------------------------------------------
/*
/****** Question 18 : Vous vous en doutez... proposez encore une fois une clé primaire pertinente pour cette table !  ******/
*/

USE [Projet_3]
GO

/****** Object:  Table [dbo].[fr_sousalimentation]    Script Date: 16/11/2021 16:32:24 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [Projet_3].[dbo].[sous_nutrition](
	[Code_Domaine] [nvarchar](50) NOT NULL,
	[Domaine] [nvarchar](50) NOT NULL,
	[Code_zone] [nvarchar](50) NOT NULL,
	[Zone] [nvarchar](50) NOT NULL,
	[Code_Élément] [int] NOT NULL,
	[Élément] [nvarchar](50) NOT NULL,
	[Code_Produit] [int] NOT NULL,
	[Produit] [nvarchar](100) NOT NULL,
	[Code_année] [int] NOT NULL,
	[Année] [nvarchar](50) NOT NULL,
	[Unité] [nvarchar](50) NOT NULL,
	[Valeur] [nvarchar](50) NULL,
	[Symbole] [nvarchar](50) NOT NULL,
	[Description_du_Symbole] [nvarchar](50) NOT NULL,
	[Note] [nvarchar](1) NULL
) ON [PRIMARY]
GO

--------------------------------------------

BULK INSERT [Projet_3].[dbo].[sous_nutrition]
    FROM 'C:\Users\FURY\Desktop\Projet_3 SQL\fr_sousalimentation.csv'
    WITH
    (
	FORMAT = 'CSV',		
    FIRSTROW = 2,
	CODEPAGE = '65001',
    FIELDTERMINATOR = ',',  --CSV field delimiter
	ROWTERMINATOR = '0x0a',
    --ROWTERMINATOR = '\n',   --Use to shift the control to next row
    ERRORFILE = 'C:\Users\FURY\Desktop\Projet_3 SQL\fr_sousalimentationErrorRows.csv'
    )
	GO
DELETE FROM [Projet_3].[dbo].[sous_nutrition]
--------------------------------------------

SELECT
       SN.[Zone]
      ,SN.[Code_année]
      ,SN.[Année]
      ,SN.[Unité]
	  ,SN.[Valeur]
      ,P.[Valeur]
FROM [Projet_3].[dbo].[sous_nutrition] AS SN
LEFT OUTER JOIN [Projet_3].[dbo].[fr_population] AS P ON SN.[Zone] = P.[Zone]
--------------------------------------------

/*
UPDATE [Projet_3].[dbo].[sous_nutrition]
ALTER TABLE [Projet_3].[dbo].[sous_nutrition]
ALTER COLUMN [Valeur] FLOAT;
SELECT CONVERT (FLOAT, A.Valeur) FROM [Projet_3].[dbo].[sous_nutrition] AS A; 
SELECT TRY_CONVERT (FLOAT, A.Valeur) FROM [Projet_3].[dbo].[sous_nutrition] AS A;
*/

UPDATE [Projet_3].[dbo].[sous_nutrition]
SET Valeur = TRY_CONVERT (FLOAT, Valeur)
ALTER TABLE [Projet_3].[dbo].[sous_nutrition] ALTER COLUMN [Valeur] FLOAT
--------------------------------------------

SELECT [Zone], AVG(A.Valeur * (POWER(10, 6))) AS Moyenne_Sous_Alimentation_Par
FROM [Projet_3].[dbo].[sous_nutrition] AS A
GROUP BY [Zone]
--------------------------------------------
/****** La clé primaire pertinante est la clé composite ([Zone], [Code_année]).  ******/
ALTER TABLE [Projet_3].[dbo].[sous_nutrition] ADD CONSTRAINT PK_sous_nutrition PRIMARY KEY ([Zone], [Code_année])

-------------------------------------------------------------------------------------------------------------------------------------------------------
--###################################################################################################################################################--
-------------------------------------------------------------------------------------------------------------------------------------------------------
/*
/****** Question 19 : Écrivez les requêtes SQL permettant de connaître…  ******/

1) Les 10 pays ayant le plus haut ratio disponibilité alimentaire/habitant en termes de protéines (en kg) par habitant, puis en termes de kcal par habitant.
2) Pour l'année 2013, les 10 pays ayant le plus faible ratio disponibilité alimentaire/habitant en termes de protéines (en kg) par habitant.
3) La quantité totale (en kg) de produits perdus par pays en 2013.
4) Les 10 pays pour lesquels la proportion de personnes sous-alimentées est la plus forte.
5) Les 10 produits pour lesquels le ratio Autres utilisations/Disponibilité intérieure est le plus élevé.
*/


/****** Question 19.1 : Les 10 pays ayant le plus haut ratio disponibilité alimentaire/habitant en termes de protéines (en kg) par habitant, puis en termes de kcal par habitant.  ******/
USE [Projet_3]
GO

/****** Object:  Table [dbo].[fr_sousalimentation]    Script Date: 16/11/2021 16:32:24 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE Question_19_1 (
	[Zone] [nvarchar](50) NOT NULL,
	[Code_zone] [nvarchar](50) NOT NULL,
	[Produit] [nvarchar](50) NOT NULL,
	[Aliments_pour_animaux_kg_an] [nvarchar](50) NULL,
	[Autres_utilisations_non_alimentaire_kg_an] [nvarchar](50) NULL,
	[Disponibilité_alimentaire_Kcal_personne_jour] [nvarchar](50) NULL,
	[Disponibilité_alimentaire_en_quantité_kg_personne_an] [nvarchar](50) NULL,
	[Disponibilité_de_matière_grasse_en_quantité_g_personne_jour] [nvarchar](50) NULL,
	[Disponibilité_de_protéines_en_quantité_g_personne_jour] [nvarchar](50) NULL,
	[Disponibilité_intérieure_kg_an] [nvarchar](50) NULL,
	[Exportations_Quantité_kg_an] [nvarchar](50) NULL,
	[Importations_Quantité_kg_an] [nvarchar](50) NULL,
	[Nourriture_kg_an] [nvarchar](50) NULL,
	[Pertes_kg_an] [nvarchar](50) NULL,
	[Production_kg_an] [nvarchar](50) NULL,
	[Semences_kg_an] [nvarchar](50) NULL,
	[Traitement_kg_an] [nvarchar](50) NULL,
	[Variation_de_stock_kg_an] [nvarchar](50) NULL,
	[nature du produit] [varchar](255) NULL
) ON [PRIMARY]
GO


INSERT INTO [Projet_3].[dbo].[Question_19_1]
SELECT * FROM [Projet_3].[dbo].[fr_animaux]

INSERT INTO [Projet_3].[dbo].[Question_19_1]
SELECT * FROM [Projet_3].[dbo].[fr_vegetaux]

DELETE FROM [Projet_3].[dbo].[Question_19_1]
WHERE [Zone] = 'Chine'


SELECT
	   [Zone]
      ,[Produit]
      ,[Disponibilité_alimentaire_Kcal_personne_jour]
      ,[Disponibilité_alimentaire_en_quantité_kg_personne_an]
      ,[Disponibilité_de_protéines_en_quantité_g_personne_jour]
      ,[Disponibilité_intérieure_kg_an]
      ,[nature du produit]
  FROM [Projet_3].[dbo].[Question_19_1]

/****** Question 19.1 : Les 10 pays ayant le plus haut ratio disponibilité alimentaire/habitant en termes de protéines (en kg) par habitant, puis en termes de kcal par habitant.  ******/

/****** Question 19.1 : Les 10 pays ayant le plus haut ratio disponibilité alimentaire/habitant en termes de protéines (en kg) par habitant ******/
SET ROWCOUNT 10
SELECT [Zone], AVG(TRY_CONVERT (FLOAT, A.Disponibilité_de_protéines_en_quantité_g_personne_jour)*65) AS Disponibilité_De_Protéines
FROM [Projet_3].[dbo].[Question_19_1] AS A
GROUP BY [Zone]
ORDER BY Disponibilité_De_Protéines ASC --DESC
SET ROWCOUNT 0

/****** Question 19.1 : Les 10 pays ayant le plus haut ratio disponibilité alimentaire/habitant en termes de kcal par habitant. ******/
SET ROWCOUNT 10
SELECT [Zone], AVG(TRY_CONVERT (FLOAT, A.[Disponibilité_alimentaire_Kcal_personne_jour])*65) AS Disponibilité_De_kcal_habitant
FROM [Projet_3].[dbo].[Question_19_1] AS A
GROUP BY [Zone]
ORDER BY Disponibilité_De_kcal_habitant DESC --ASC
SET ROWCOUNT 0

/****** Question 19.2 : Pour l'année 2013, les 10 pays ayant le plus faible ratio disponibilité alimentaire/habitant en termes de protéines (en kg) par habitant.  ******/
SET ROWCOUNT 10
SELECT [Zone], AVG(TRY_CONVERT (FLOAT, A.Disponibilité_de_protéines_en_quantité_g_personne_jour)) AS Disponibilité_De_Protéines
FROM [Projet_3].[dbo].[Question_19_1] AS A
GROUP BY [Zone]
ORDER BY Disponibilité_De_Protéines ASC
SET ROWCOUNT 0


SELECT TOP 10 [Zone], AVG(TRY_CONVERT (FLOAT, A.Disponibilité_de_protéines_en_quantité_g_personne_jour)) AS Disponibilité_De_Protéines
FROM [Projet_3].[dbo].[Question_19_1] AS A
GROUP BY [Zone]
ORDER BY Disponibilité_De_Protéines ASC

/****** Question 19.3 : La quantité totale (en kg) de produits perdus par pays en 2013.  ******/
SET ROWCOUNT 10
SELECT [Zone], SUM(TRY_CONVERT (FLOAT, A.Pertes_kg_an)) AS Pertes_kg_an
FROM [Projet_3].[dbo].[Question_19_1] AS A
GROUP BY [Zone]
ORDER BY Pertes_kg_an DESC --ASC
SET ROWCOUNT 0

/****** Question 19.4 : Les 10 pays pour lesquels la proportion de personnes sous-alimentées est la plus forte.  ******/

DELETE FROM [Projet_3].[dbo].[sous_nutrition]
WHERE [Zone] = 'Chine'

ALTER TABLE [Projet_3].[dbo].[sous_nutrition]
ADD [sous_alimentation_pays] FLOAT

ALTER TABLE [Projet_3].[dbo].[sous_nutrition]
DROP COLUMN [sous_alimentation_pays] 

SELECT
       SN.[Zone]
      ,SN.[Code_année]
      ,SN.[Année]
      ,SN.[Unité]
	  ,SN.[Valeur]
      ,P.[Valeur]
FROM [Projet_3].[dbo].[sous_nutrition] AS SN
LEFT OUTER JOIN [Projet_3].[dbo].[fr_population] AS P ON SN.[Zone] = P.[Zone]

UPDATE [Projet_3].[dbo].[sous_nutrition]
SET [Valeur] = [Valeur]*(POWER(10,6))

SET ROWCOUNT 10
SELECT
SN.[Zone], AVG(SN.[Valeur] * 100/P.[Valeur]) AS Ratio
FROM [Projet_3].[dbo].[sous_nutrition] AS SN
LEFT OUTER JOIN [Projet_3].[dbo].[fr_population] AS P ON SN.[Zone] = P.[Zone]
GROUP BY SN.[Zone]
ORDER BY Ratio DESC --ASC
SET ROWCOUNT 0


/****** Question 19.5 : Les 10 produits pour lesquels le ratio Autres utilisations/Disponibilité intérieure est le plus élevé.  ******/

UPDATE [Projet_3].[dbo].[dispo_alim]
SET Autres_utilisations_non_alimentaire_kg_an = TRY_CONVERT (FLOAT, Autres_utilisations_non_alimentaire_kg_an)
ALTER TABLE [Projet_3].[dbo].[dispo_alim] ALTER COLUMN [Autres_utilisations_non_alimentaire_kg_an] FLOAT

UPDATE [Projet_3].[dbo].[dispo_alim]
SET Disponibilité_intérieure_kg_an = TRY_CONVERT (FLOAT, Disponibilité_intérieure_kg_an)
ALTER TABLE [Projet_3].[dbo].[dispo_alim] ALTER COLUMN [Disponibilité_intérieure_kg_an] FLOAT

DELETE FROM [Projet_3].[dbo].[dispo_alim]  
WHERE [Autres_utilisations_non_alimentaire_kg_an] IS NULL

DELETE FROM [Projet_3].[dbo].[dispo_alim]  
WHERE [Disponibilité_intérieure_kg_an] = 0

SELECT  
	   SN.[Produit], AVG(SN.Autres_utilisations_non_alimentaire_kg_an / SN.Disponibilité_intérieure_kg_an) AS Ratio
      --,[Produit]
      --,[Autres_utilisations_non_alimentaire_kg_an]
      --,[Disponibilité_intérieure_kg_an]
  FROM [Projet_3].[dbo].[dispo_alim] AS SN
GROUP BY SN.[Produit]
ORDER BY [Ratio] DESC --ASC



-------------------------------------------------------------------------------------------------------------------------------------------------------
--###################################################################################################################################################--
-------------------------------------------------------------------------------------------------------------------------------------------------------
/*
/****** Question 20 : pour quelques-uns des produits identifiés dans cette dernière requête SQL, supposez quelles sont ces "autres utilisations" possibles (recherchez sur Internet !)  ******/




















