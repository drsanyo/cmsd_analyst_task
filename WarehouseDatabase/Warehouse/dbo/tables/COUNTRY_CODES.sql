﻿CREATE TABLE [dbo].[COUNTRY_CODES]
(
	[COC_AUTO_KEY] INT NOT NULL PRIMARY KEY, 
    [CODE] VARCHAR(50) NOT NULL, 
    [COUNTRY_NAME] VARCHAR(50) NOT NULL, 
    [SDF_COC_002] VARCHAR(50) NULL, 
    [SDF_COC_003] VARCHAR(50) NULL
)
