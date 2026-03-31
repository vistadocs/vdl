---
title: TBI Version 4.2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: TBI
app_name: "Registry: Traumatic Brain Injury"
section: CLI
app_status: active
pkg_ns: TBI
patch_ver: 4.2
patch_id: TBI*4.2
group_key: "TBI:TBI:4.2"
file_numbers: []
security_keys: []
menu_options: 0
description: The Presidential Task Force on Returning Global War on Terror Heroes, as stated in the Global War on Terror report (recommendation P-3) and Public Law 110-181 National Defense Authorization Act 2008 TBI Section 1704 created the requirement for the Traumatic Brain Injury (TBI) Registry. This registry
audience: 
keywords: 
  - table
  - contents
  - registry
  - release
  - enhancements
  - cube
  - view
  - strong
  - enhanced
  - notes
page_count: 0
word_count: 896
section_count: 8
table_count: 17
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 7
revision_newest: 11/1/2015
revision_oldest: 4/18/2012
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbirn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbirn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=198"
---

Traumatic Brain Injury Registry (TBI)Release Notes

![](tbi-version-4-2-release-notes/001.png)

Version 4.2November 2015

Office of Enterprise Development (OED)

Health Data Management Service (HDS)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
  - [Related Documents](#related-documents)
  - [Acronyms and Definitions](#acronyms-and-definitions)
- [User Release Notes](#user-release-notes)
  - [TBI Registry Enhancements INCR 1](#tbi-registry-enhancements-incr-1)
  - [Functional Performance](#functional-performance)
- [Technical Release Notes](#technical-release-notes)
  - [Data Dictionary Changes](#data-dictionary-changes)
| Version | Date  | Description                                                                                                         | Project Manager                | Author                         |
|-------------|-----------|-------------------------------------------------------------------------------------------------------------------------|------------------------------------|------------------------------------|
| 4.2         | 11/1/2015 | Removed reference to .NET 4.5.2, Updated Section 3.1 to include Data dictionary changes to Datamart_Registries Database | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 4.1         | 7/7/2015  | Updated for TBI Enhancements Increment 1 – sections 1.2 and 2.1                                                         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 4.1         | 5/7/2014  | Updated for Increment 5 Release                                                                                         | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 4.0         | 6/23/2012 | Reviewed and formatted                                                                                                  | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 3.0         | 4/26/2012 | Added Tracker 1524 and 1555 to the list of enhancements.                                                                | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 2.0         | 4/26/2012 | Updated the related user manual documents.                                                                              | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 1.0         | 4/18/2012 | Create Initial Draft Release Notes document                                                                             | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Presidential Task Force on Returning Global War on Terror Heroes, as stated in the Global War on Terror report (recommendation P-3) and Public Law 110-181 National Defense Authorization Act 2008 TBI Section 1704 created the requirement for the Traumatic Brain Injury (TBI) Registry. This registry promotes the delivery of quality care by ensuring Operation Enduring Freedom/Operation Iraqi Freedom (OEF/OIF) Veterans are screened for these injuries and that they receive timely follow up evaluations and ongoing treatment.

This release addresses the Traumatic Brain Injury (TBI) Enhancements Increment 1 business requirements to expand the current TBI Registry capabilities. Refer to section 2.1 below for these enhancements.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to identify and describe the changes in the TBI Registry software being deployed to the Converged Registries Solution (CRS) operational environment. It summarizes the features and enhancements for Increment 1 of the TBI Enhancements project.

The purpose of the TBI Registry is to facilitate screening, provide comprehensive follow up evaluations to positive screens, and to administer care to the current 615,000 and all future OEF, OIF and Operation New Dawn (OND) veterans through the use of TBI assessment tools, instruments and tracking modules.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of this release includes enhancements for the TBI Enhancements Project. Specifically, this release includes the following enhancements/changes:

- Migrated from MDWS to VIA for SOA calls.
- Migrated the reporting environment to Pyramid Analytics.
- Enhanced the Registry DataMart to include additional dimensions for use in the TBI Cube.
- Enhanced the TBI CUBE to allow more robust reporting and analysis of TBI Survey Data.
- Added the ability to view the Last 3 Instruments, and to view all instruments after correctly selecting the appropriate patient.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- TBI Installation Guide for Increment 2, Version 4.3, November 2015
- TBI Instruments User Manual for Increment 1, Version 5.4, November 2015
- TBI Polytrauma User Manual, Version 4.4, November 2015
- TBI Application User Manual, Version 1.5, November2015
- TBI System Management Guide, Version 4.2, July 2015
- HREG TBI Requirements Specification Document (RSD): <span class="mark">REDACTED</span>
- HREG TBI System Design Document (SDD): <span class="mark">REDACTED</span>

## *Acronyms and Definitions*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                                                                 |
|-------------|-----------------------------------------------------------------|
| Acronym | Description                                                 |
| CPRS        | Computerized Patient Record System                              |
| CRS         | Converged Registries Solution                                   |
| DEF         | Defect                                                          |
| INCR        | Increment                                                       |
| MDWS        | Medical Data Web Service                                        |
| OEF/OIF     | Operation Enduring Freedom/Operation Iraqi Freedom              |
| OND         | Operation New Dawn                                              |
| TBI         | Traumatic Brain Injury                                          |
| UAT         | User Acceptance Test                                            |
| VA          | Veterans Affairs                                                |
| VHA         | Veterans Health Administration                                  |
| VIA         | Veterans Integration Adapter                                    |
| VistA       | Veterans Health Information Systems and Technology Architecture |

# User Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## TBI Registry Enhancements INCR 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release addresses the TBI Enhancements Increment 1 business requirements to expand the current TBI Registry capability as follows:

1)  Exposed the Data Cube to Pyramid Analytics BIOXel to provide a consolidated, consistent source of TBI Instrument information that can be viewed for all reporting activities.
2)  Enhanced the Data Cube to provide the ability to view consolidated TBI Instrument information without manually merging tables.
3)  Enhanced the Data Cube so as new instrument packages are developed, the users have the ability to view their information as part of the consolidated source of Instrument information.
4)  Enhanced the Data Cube to provide the ability to view summary data elements and outcomes, for all standardized forms in the TBI Instruments package.
5)  Enhanced the Data Cube to provide the ability to view facility level summary data based on user’s preference for keyed variables. (I.E. date, location, gender, age etc.).
6)  The move to Pyramid Analytics allows users to save reports as templates for reuse.
7)  Enhanced the Data Cube to provide the ability to view each question within each instrument as a value for reporting.
8)  Enhanced the Data Cube to provide the ability to view information consolidated from multiple instruments into a single report.
9)  Enhanced the Data Cube to allow the selection of multiple instruments to report into a single report.
10) Provide the ability as new instrument packages are developed, to view their information as part of the Reporting Cube functionality.

## Functional Performance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no functional performance requirements for this increment.

# Technical Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Data Dictionary changes were limited to the DataMart_Registries database.

| <u>Name</u>           | DataMart_Registries.dbo.dimtime2                                                                                                                  |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <u>Dimension Type</u> | Type 0                                                                                                                                            |
| <u>Primary Key</u>    | DateKey                                                                                                                                           |
| <u>Source</u>         | DataMart_Registries.dbo.dimtime                                                                                                                   |
| <u>Description</u>    | The dimtime2 table is a subset of the dim time table with the addition of a surrogate key for use in the fact tables. It focuses on Fiscal dates. |

| <u>Column Name</u>       | <u>DataType</u> |
|------------------------------|---------------------|
| DateKey                      | int                 |
| PK_Date                      | datetime            |
| Date_Name                    | nvarchar(50)        |
| Year                         | datetime            |
| Year_Name                    | nvarchar(50)        |
| Quarter                      | datetime            |
| Quarter_Name                 | nvarchar(50)        |
| Month                        | datetime            |
| Month_Name                   | nvarchar(50)        |
| Day_Of_Year                  | int                 |
| Day_Of_Year_Name             | nvarchar(50)        |
| Day_Of_Quarter               | int                 |
| Day_Of_Quarter_Name          | nvarchar(50)        |
| Day_Of_Month                 | int                 |
| Day_Of_Month_Name            | nvarchar(50)        |
| Month_Of_Year                | int                 |
| Month_Of_Year_Name           | nvarchar(50)        |
| Month_Of_Quarter             | int                 |
| Month_Of_Quarter_Name        | nvarchar(50)        |
| Quarter_Of_Year              | int                 |
| Quarter_Of_Year_Name         | nvarchar(50)        |
| Fiscal_Year                  | datetime            |
| Fiscal_Year_Name             | nvarchar(50)        |
| Fiscal_Quarter               | datetime            |
| Fiscal_Quarter_Name          | nvarchar(50)        |
| Fiscal_Month                 | datetime            |
| Fiscal_Month_Name            | nvarchar(50)        |
| Fiscal_Day                   | datetime            |
| Fiscal_Day_Name              | nvarchar(50)        |
| Fiscal_Day_Of_Year           | int                 |
| Fiscal_Day_Of_Year_Name      | nvarchar(50)        |
| Fiscal_Day_Of_Quarter        | int                 |
| Fiscal_Day_Of_Quarter_Name   | nvarchar(50)        |
| Fiscal_Day_Of_Month          | int                 |
| Fiscal_Day_Of_Month_Name     | nvarchar(50)        |
| Fiscal_Month_Of_Year         | int                 |
| Fiscal_Month_Of_Year_Name    | nvarchar(50)        |
| Fiscal_Month_Of_Quarter      | int                 |
| Fiscal_Month_Of_Quarter_Name | nvarchar(50)        |
| Fiscal_Quarter_Of_Year       | int                 |
| Fiscal_Quarter_Of_Year_Name  | nvarchar(50)        |

| <u>Name</u>           | DataMart_Registries.dbo.dimAgeGroup                                                                                                             |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <u>Dimension Type</u> | Type 0                                                                                                                                          |
| <u>Primary Key</u>    | AgeGroupKey                                                                                                                                     |
| <u>Source</u>         | N/A                                                                                                                                             |
| <u>Description</u>    | The dimAgeGroup table was created and populated using values supplied by the RSD. It is used to group patients based on age at a point in time. |

| <u>Column Name</u> | <u>DataType</u>         |
|------------------------|-----------------------------|
| AgeGroupKey            | \[int\] IDENTITY(1000,1000) |
| Age_Group              | \[nchar\](10)               |

| <u>Name</u>           | DataMart_Registries.dbo.dimProvider                                                             |
|---------------------------|-------------------------------------------------------------------------------------------------|
| <u>Dimension Type</u> | Type 0                                                                                          |
| <u>Primary Key</u>    | Provider_id                                                                                     |
| <u>Source</u>         | Registry.dbo.Provider                                                                           |
| <u>Description</u>    | The dimProvider table is a subset of providers used to identify providers and authors of notes. |

| <u>Column Name</u> | <u>DataType</u> |
|------------------------|---------------------|
| PROVIDER_ID            | int                 |
| FIRST_NAME             | varchar(50)         |
| MIDDLE_NAME            | varchar(50)         |
| LAST_NAME              | varchar(50)         |
| ADDRESS_LINE1          | varchar(100)        |
| ADDRESS_LINE2          | varchar(100)        |
| ADDRESS_LINE3          | varchar(100)        |
| CITY                   | varchar(60)         |
| STATE                  | varchar(50)         |
| COUNTY                 | varchar(50)         |
| COUNTRY                | varchar(50)         |
| POSTAL_CODE            | varchar(20)         |
| ZIP_PLUS_4             | varchar(6)          |
| STA3N                  | smallint            |

| <u>Name</u>           | DataMart_Registries.TBICUBE.Patient                                                                            |
|---------------------------|----------------------------------------------------------------------------------------------------------------|
| <u>Dimension Type</u> | Type 2                                                                                                         |
| <u>Primary Key</u>    | Patient_Key                                                                                                    |
| <u>Source</u>         | Registry.dbo.patient                                                                                           |
| <u>Description</u>    | The patient table is a subset of the patient table used to identify demographic data for use in TBI analytics. |

| <u>Column Name</u>    | <u>DataType</u> |
|---------------------------|---------------------|
| Patient_Key               | int IDENTITY(1,1)   |
| PATIENT_ICN               | varchar(50)         |
| SSN                       | varchar(20)         |
| FIRST_NAME                | varchar(50)         |
| MIDDLE_NAME               | varchar(50)         |
| LAST_NAME                 | varchar(50)         |
| OEF_OIF_IND               | varchar(7)          |
| BIRTH_DATE                | datetime            |
| GENDER                    | varchar(100)        |
| OEF_OIF_LOCATION          | varchar(100)        |
| CURRENT_AGEGROUP          | varchar(5)          |
| SERVICE_BRANCH            | varchar(100)        |
| RACE_NAME                 | varchar(100)        |
| ETHNICITY_NAME            | varchar(100)        |
| MaritalStatus             | varchar(50)         |
| LastServiceSeparationDate | date                |
| ScdStatus                 | bit                 |
| ScdStartDate              | datetime            |
| ScdEndDate                | datetime            |

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><u>Name</u></strong></th>
<th>DataMart_Registries. TBICUBE.dimSurveyDetails</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>Dimension Type</u></strong></td>
<td>Type 2</td>
</tr>
<tr class="even">
<td><strong><u>Primary Key</u></strong></td>
<td>SurveyDetailsID</td>
</tr>
<tr class="odd">
<td><strong><u>Source</u></strong></td>
<td><p>Registry.dbo.STD_Survey_Type,</p>
<p>Registry.dbo.STD_Question,</p>
<p>Registry.dbo.STD_Question_Choice</p></td>
</tr>
<tr class="even">
<td><strong><u>Description</u></strong></td>
<td>The dimSurveyDetails table is a denormalized view of the Surveys/Instruments, each row contains the Survey, Question and Choice until all combinations are represented in the table.</td>
</tr>
</tbody>
</table>

| <u>Column Name</u> | <u>DataType</u>      |
|------------------------|--------------------------|
| SurveyDetailsID        | int                      |
| SurveyTypeID           | int                      |
| QuestionID             | int                      |
| QuestionChoiceID       | int                      |
| SurveyName             | varchar(100)             |
| QuestionNumber         | varchar(50)              |
| QuestionText           | varchar(950)             |
| QuestionSortOrder      | int                      |
| ChoiceName             | varchar(100)             |
| ChoiceText             | varchar(4000)            |
| ChoiceSortOrder        | int                      |
| ScdStatus              | bit DEFAULT ((0))        |
| ScdStartDate           | date DEFAULT (getdate()) |
| ScdEndDate             | date                     |

| <u>Name</u>           | DataMart_Registries.dbo.InstitutionOrganization                                                                                                                                                                                                                             |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <u>Dimension Type</u> | Type 2                                                                                                                                                                                                                                                                      |
| <u>Primary Key</u>    | Institution_Key                                                                                                                                                                                                                                                             |
| <u>Source</u>         | Registry.dbo.std_Institution, Registry.dbo.std_facility_type                                                                                                                                                                                                                |
| <u>Description</u>    | The InstitutionOrganization table is a subset of Institutions where the std_facility_type has the IsPatientTreating flag=1. It also has a self referencing key used in a parent child hierarchy in the cube database, the VISN parents have been validated with the client. |

| <u>Column Name</u>  | <u>DataType</u> |
|-------------------------|---------------------|
| Institution_Key         | int IDENTITY(1,1)   |
| Institution_id          | int                 |
| name                    | varchar(100)        |
| stationNumber           | varchar(10)         |
| VISTANAME               | varchar(50)         |
| STREETADDRESSLINE1      | varchar(100)        |
| STREETADDRESSLINE2      | varchar(100)        |
| STREETADDRESSLINE3      | varchar(100)        |
| STREETCITY              | varchar(50)         |
| STREETSTATE             | varchar(100)        |
| STREETPOSTALCODE        | varchar(50)         |
| parent_id               | int                 |
| VISN                    | varchar(100)        |
| FacilityTypeCode        | varchar(50)         |
| FacilityTypeName        | varchar(100)        |
| Institution_DisplayName | varchar(121)        |
| visn_id                 | int                 |
| ScdStatus               | bit                 |
| ScdStartDate            | datetime            |
| ScdEndDate              | datetime            |
|                         |                     |

| <u>Name</u>           | DataMart_Registries.dbo.SurveyType |
|---------------------------|------------------------------------|
| <u>Dimension Type</u> | Type 2                             |
| <u>Primary Key</u>    | SurveyTypeKey                      |
| <u>Source</u>         | Registry.dbo.STD_Survey_Type       |
| <u>Description</u>    |                                    |

| <u>Column Name</u> | <u>DataType</u> |
|------------------------|---------------------|
| SurveyTypeID           | Integer             |
| Survey_Name            | Varchar(100)        |
| Survey_Type_Abbr       | Varchar(15)         |
| Registry_ID            | Integer             |