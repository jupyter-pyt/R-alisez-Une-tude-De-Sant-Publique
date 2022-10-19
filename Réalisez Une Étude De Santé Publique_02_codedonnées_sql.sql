

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




-------------------------------------------------------------------------------------------------------------------------------------------------------
--###################################################################################################################################################--
-------------------------------------------------------------------------------------------------------------------------------------------------------
/*
/****** fr_animaux & fr_vegetaux  ******/
*/

/****** Object:  Charger le fichier fr_animaux.csv la table Table  [dbo].[fr_animaux] ******/

USE [Projet_3]
GO

/****** Object:  Table [dbo].[fr_animaux]    Script Date: 14/11/2021 14:28:40 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].[fr_animaux]

CREATE TABLE [dbo].[fr_animaux](
	[Zone] [nvarchar](50) NOT NULL,
	[Code_zone] [nvarchar](50) NOT NULL,
	[Produit] [nvarchar](50) NOT NULL,
	[Aliments_pour_animaux_kg_an] [nvarchar](50) NULL,
	[Autres_utilisations_non_alimentaire_kg_an] [nvarchar](50) NULL,
	[Disponibilité_alimentaire_Kcal_personne_jour] [nvarchar](50) NULL,
	[Disponibilité_alimentaire_en_quantité_kg_personne_an] [nvarchar](50) NULL,
	[Disponibilité_de_matière_grasse_en_quantité_g_personne_jour] [nvarchar](50) NULL,
	[Disponibilité_de_protéines_en_quantité_g_personne_jour] [nvarchar](50) NULL,
	[Disponibilité_intérieure_kg_an] [nvarchar](50) NOT NULL,
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

/****** Object:  Charger le fichier fr_vegetaux.csv la table Table  [dbo].[fr_vegetaux] ******/

USE [Projet_3]
GO

/****** Object:  Table [dbo].[fr_vegetaux]    Script Date: 14/11/2021 14:30:14 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].[fr_vegetaux]

CREATE TABLE [dbo].[fr_vegetaux](
	[Zone] [nvarchar](50) NOT NULL,
	[Code_zone] [int] NOT NULL,
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


