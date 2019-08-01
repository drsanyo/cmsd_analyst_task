﻿CREATE TABLE [dbo].[COMPANIES]
(
	[CMP_AUTO_KEY] INT NOT NULL PRIMARY KEY, 
    [COMPANY_NAME] VARCHAR(150) NOT NULL, 
    [COC_AUTO_KEY] INT NULL, 
    CONSTRAINT [FK_COMPANIES_COUNTRY_CODES] FOREIGN KEY ([COC_AUTO_KEY]) REFERENCES [dbo].[COUNTRY_CODES]([COC_AUTO_KEY])
)
