---
title: STS Version 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: STS
app_name: Standards & Terminology Services
section: CLI
app_status: active
pkg_ns: STS
patch_ver: 1
patch_id: STS*1
group_key: "STS:STS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: Standards & Terminology Services (STS) is responsible for organizing, formalizing, and maintaining the terminology of the Veterans Health Administration (VHA). Currently, terminology is used in the Department of Veterans Affairs (VA) Electronic Medical Record (EMR) system known as Veterans Health In
audience: 
keywords: 
  - vista
  - table
  - class
  - strong
  - blockquote
  - contents
  - vhat
  - concept
  - style
  - width
page_count: 0
word_count: 7308
section_count: 8
table_count: 28
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Standards_and_Terminology_Services/sts_technical_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Standards_and_Terminology_Services/sts_technical_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=191"
---

# Standards & Terminology Service


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Standards & Terminology Service](#standards-terminology-service)
    - [VETS Deployment Services Production Release](#vets-deployment-services-production-release)
    - [Department of Veterans Affairs Office of Information and Technology Office of Enterprise Development](#department-of-veterans-affairs-office-of-information-and-technology-office-of-enterprise-development)
- [Introduction](#introduction)
- [Authoring VHAT](#authoring-vhat)
  - [Concepts](#concepts)
  - [Designations](#designations)
  - [Subsets](#subsets)
  - [Standardized Domains](#standardized-domains)
    - [Legacy Designations](#legacy-designations)
    - [Vitals](#vitals)
    - [Allergy](#allergy)
    - [National Drug File](#national-drug-file)
    - [Clinical Document Titles](#clinical-document-titles)
    - [Orders](#orders)
    - [Medication Routes](#medication-routes)
    - [Immunization](#immunization)
  - [Other issues related to Authoring VHAT](#other-issues-related-to-authoring-vhat)
    - [Issues Specific to VistA](#issues-specific-to-vista)
- [Standard Code Systems](#standard-code-systems)
- [Map Sets](#map-sets)
- [Configuration Files](#configuration-files)
  - [Terminology](#terminology)
  - [Browser](#browser)

### VETS Deployment Services Production Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Technical Manual*
![](sts-version-1-technical-manual/001.png)
> *Version 10*
> *December 2010*

### Department of Veterans Affairs Office of Information and Technology Office of Enterprise Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Revision History
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 56%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description of Change</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author Information</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Oct. 27, 2009</td>
<td>Inserted other doc text.</td>
<td>STS Technical Writer</td>
</tr>
<tr class="even">
<td>Oct. 28, 2009</td>
<td>Format in new template.</td>
<td>STS Technical Writer</td>
</tr>
<tr class="odd">
<td>Nov. 03, 2009</td>
<td>Incorporate review changes.</td>
<td>STS VETS Terminology Analysts, STS Technical Writer</td>
</tr>
<tr class="even">
<td>March 04,2010</td>
<td><mark>REDACTED</mark> changes, formatting.</td>
<td><blockquote>
<p>STS VETS Terminology Analysts, STS Technical Writer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>July 21, 2010</p>
<p>July 22, 2010</p>
<p>July 23, 2010</p></td>
<td>Analyst review changes added, and text edited and reformatted.</td>
<td>STS VETS Terminology Analysts, STS Technical Writer</td>
</tr>
<tr class="even">
<td>Dec. 2010</td>
<td>Analysts/Peer/SQA Review</td>
<td><p>STS VETS Terminology Analysts, STS VETS SQA Lead, STS</p>
<p>Technical Writer</p></td>
</tr>
<tr class="odd">
<td>Dec. 2010</td>
<td>Final for PDF</td>
<td>STS Technical Writer</td>
</tr>
</tbody>
</table>

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Standards & Terminology Services (STS) is responsible for organizing, formalizing, and maintaining the terminology of the Veterans Health Administration (VHA). Currently, terminology is used in the Department of Veterans Affairs (VA) Electronic Medical Record (EMR) system known as Veterans Health Information System and Technology Architecture (VistA). There are many implementations of VistA throughout the world. Each implementation has its own set of reference files that support clinical care of veterans. This reference information is non-uniform and can create a lot of confusion when comparing a patient’s medical record from one site to another. STS is making these files uniform throughout the enterprise, and is facilitating semantic and computational interoperability.

The processes of standardizing the terminology lead to the creation of the VHA Terminology (VHAT). VHAT encompasses reference information for many clinical domains including Vital Signs, Allergy, Text Integration Utility (TIU) document titles, Immunizations, and Medication Routes of administration. STS maintains VHAT through ongoing evaluation of feedback from domain experts. STS also sends regular updates to each VistA system.

# Authoring VHAT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The process of authoring concepts can be complicated with the best results coming when you can simultaneously think in two different contexts. The first context is the Terminology Deployment Services (TDS) application and the second is VistA. TDS was developed with the specific interests of VHAT in mind; it is the most straightforward representation of how terminology should appear. VistA, on the other hand, represents some domains in counter-intuitive ways, particularly the domain of Vital Signs.

This document focuses on points of modeling and of VistA. It is not a style guide for naming concepts, nor is it an exhaustive list of all the techniques and traps of terminology practice. The Technical Manual is a primer for understanding how modeling can assist VistA domains run smoothly.

## Concepts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The concept is the primary, abstract unit of thought. It is an abstract unit of meaning, independent of the language or any other method used to express the thought. A concept is not necessarily a simple thought -

\- it can be as simple or complex as necessary in order to stand for any part of the perceivable world. Concepts can have relationships with other concepts. They can also act as inputs to algorithms used to arrive at other concepts. You can organize them in many different ways according to your need.

The table depicts an enumeration of the attributes of concepts.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>VUID</th>
<th>The VA Unique Identifier</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Status</td>
<td>Indicates whether a concept is in use (Active) or has been removed from use (Inactive).</td>
</tr>
<tr class="even">
<td>Properties</td>
<td>All properties are assigned to concepts based on the requirements of the domain. See specific domain sections in this document.</td>
</tr>
<tr class="odd">
<td>Relationships</td>
<td><p>Relationships are assigned to concepts based on the requirements of the domain. See specific domain sections in this document.</p>
<p>Each concept (except for Vitals Qualifier concepts) has a has_parent relationship appropriate for its place in the taxonomy. The allowable values are:</p>
<p>DOCUMENT_TYPE [C]</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><p>DRUG CLASSES [C] DRUG INGREDIENT [C] NATURE OF ORDER [C] ORDER STATUS [C] REACTANTS [C] REACTIONS [C]</p>
<p>ROLE [C] SERVICE [C] SETTING [C]</p>
<p>SUBJECT MATTER DOMAIN (SMD) [C] TIU STATUS [C]</p>
<p>TIU TITLES [C]</p>
<p>VITALS QUALIFIER [C] VITALS TYPE [C]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Designations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Designations are the means by which you express concepts. There can be limitless designations for any one concept that can occur in any form. Designations modeled in VHAT at this time are textual terms; they are handles for concepts. Other than the immediate relationship with the concepts they represent, designations do not participate in relationships with other designations or concepts. Finally, designations can express concepts in different ways. Each concept has a designation that is considered its Preferred Name, and there are other designation types as well including Synonym and Abbreviation.

The table depicts an enumeration of the attributes of designations:

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>The text of the designation.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Type</td>
<td><p>Every concept should have one designation of type Preferred Name. Additional allowable values are Abbreviation, Synonym, and VistA Name. These additional values may be available as specified per domain.</p>
<blockquote>
<p>The designations that are destined for VistA are typically of type Preferred Name, but there may be reasons for using other types, such as VistA character length limitations. For example, the Allergy Reaction VistA Name designation of INCREASED SERUM CREATINE KINAS is deployed instead of the Preferred Name designation of INCREASED SERUM CREATINE KINASE.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VUID</td>
<td>The VA Unique Identifier that is assigned to the designation name</td>
</tr>
<tr class="odd">
<td>Status</td>
<td>Indicates whether a designation is in use (Active) or has been removed from use (Inactive).</td>
</tr>
<tr class="even">
<td>Properties</td>
<td>All properties are assigned to designations based on the requirements of the domain. See specific domain sections in this document.</td>
</tr>
<tr class="odd">
<td>Relationships</td>
<td>Designations are not involved in relationships.</td>
</tr>
</tbody>
</table>

## Subsets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subsets are not concepts, but exist behind the scenes for aggregating designations. Most subsets were created to represent the contents of the standardized files in VistA. The current list of subsets used in VHAT follows, grouped by the domains in which they appear:

- Allergy Subsets
  - Reactants
  - Reactions
- Immunization Subsets
  - Immunization Procedure
  - Skin Test
- National Drug File Subsets
  - Drug Class
  - Drug Ingredient
- Order Subsets
  - Nature of Order
  - Order Status
- Pharmacy Subsets
  - Medication Routes
- Text Integration Utility Subsets
  - TIU Doctype
  - TIU Role
  - TIU SMD
  - TIU Service
  - TIU Setting
  - TIU Status
  - TIU Titles
- Vitals Subsets
  - Vital Categories
  - Vital Qualifiers
  - Vital Types

## Standardized Domains

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each domain has a unique set of properties and relationships associated to a concept. The model for designations is generic and is the same for all domains. The following sections discuss the domains in order of their implementation and are prefaced with remarks about early approaches to non-standardized terms in standardized files. Steps to take to reactivate the terms are also discussed.

### Legacy Designations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vital Signs and Allergy were the first domains standardized. A list was made of all the terms found throughout VistA in these domains, and the standardized terms were made active and installed in every VistA system. The terms that were not included in the standardized list were reserved as a *Legacy Designation*, and were made inactive at whichever site had the term. Each of these legacy designations has a VA Unique Identifier (VUID). VUIDs are the same at every site.

Due to changes in practice or expanded clinical need, a legacy designation may be required. The legacy designations are made active and installed at all VistA sites.

Legacy designations exist in VHAT as designations only. Instead of each having a unique concept, they are aggregated to one of four legacy concepts. Legacy designations have the same attributes as Designations, with some following exceptions or specifications.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>The name of the designation as it is known in VistA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Type</td>
<td>All legacy designations have the type of VistA Name.</td>
</tr>
<tr class="even">
<td>Status</td>
<td>All legacy designations are Inactive.</td>
</tr>
<tr class="odd">
<td>VUID</td>
<td>The VA Unique Identifier</td>
</tr>
<tr class="even">
<td>Relationships</td>
<td><p>Legacy designations are not involved in relationships, just like other designations. The legacy designations, however, belong to one of the four following legacy concepts:</p>
<p>Legacy Allergy Reactants Legacy Allergy Reactions Legacy Vital Qualifiers</p>
<p>Legacy Vital Types</p></td>
</tr>
</tbody>
</table>

### Vitals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals Domain consists of three files that cover the wide range of all vital signs recorded in VistA, along with the appropriate modifiers. This domain is difficult to understand because its modeling in VistA is not intuitive. In VistA, the central file that organizes the domain is Vital Qualifier. Each Qualifier entry links to a couplet of a Vital Type and a Vital Category. To take an example from the domain, the Qualifier ADULT CUFF links to the Type of BLOOD PRESSURE and Category CUFF SIZE.

VistA has established a thorough set of steps to use following any deployed update. These steps check for possible dangling pointers between terms, and breaks links and inactivate terms as necessary. If modelers of Vitals terms are not careful, logical changes may be made in VistA that have not been considered in modeling. This will create mismatches between the model and VistA. These appear as checksum mismatches in TDS.

Updates to Vitals files are essentially permanent; it requires a patch to reverse any change. All modification to the Type file must be coordinated with the package developer, otherwise updated content may not be available to the package, or may even break it. In other words, resist changing this content for any reason. Make changes to the files only if necessary and as a final resort. Changes should only be made under the explicit direction of the package developer. The same prohibition is true for the Category file. The Qualifier file may be updated but only with certain changes.

- Qualifiers may be added to the file.
- Existing Qualifiers may be linked to Types.
- Qualifiers may be inactivated.
- No other change to the Qualifier file is permitted. VHAT Subset Name: Vital Types

VistA File Number: 120.51

VistA File Name: GMRV VITAL TYPE

> Properties

| VistA Field | VHAT Attribute or Property Name | Notes                         |
|-----------------|-------------------------------------|-----------------------------------|
| .01, NAME       | Designation Name                    | Required, must be 2-50 characters |

| 1, ABBREVIATION         | VistA_Short_Name           | Required, must be 1-5 characters, must be unique |
|-------------------------|----------------------------|--------------------------------------------------|
| 3, RATE                 | VistA_Type_Rate            | Set of {NO, YES}                                 |
| 4, RATE INPUT TRANSFORM | VistA_Rate_Input_Transform | Mumps code                                       |
| 5, RATE HELP            | VistA_Type_Rate_Help       | Must be 3-30 characters                          |
| 7, PCE ABBREVIATION     | VistA_PCE_Abbreviation     | Must be 1-10 characters, must be unique          |

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                   |
|-----------------|----------------------------|-------------------------------------------------------------|
| \<none\>        | has_parent                 | Every Type concept is the child of the concept Vital Types. |

A Type concept can also be the target of a Vital Qualifier concept’s has_qualifier relationship. VHAT Subset: Vital Qualifiers

VistA File Number: 120.52

VistA File Name: GMRV VITAL QUALIFIER

> Properties

| VistA Field | VHAT Attribute or Property Name | Notes                              |
|-----------------|-------------------------------------|----------------------------------------|
| .01, QUALIFIER  | Designation Name                    | Required, must be 2-50 characters      |
| .02, SYNONYM    | VistA_Short_Name                    | Must be 1-3 characters, must be unique |

> Relationships

| VistA Field         | VHAT Relationship Name | Notes                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 120.521,.01, VITAL TYPE | has_qualifier              | An instance of this relationship is required for each Vital Qualifier linked to a Vital Type. This relationship once pointed from the Type to the Qualifier in an earlier version of the model, but has changed direction to eliminate otherwise necessary transformations between the model and VistA. The name persists to minimize code changes to TDS or VistA. |
| 120.521,.02, CATEGORY   | has_VistA_category         | Each Qualifier has exactly one has_VistA_category relationship.                                                                                                                                                                                                                                                                                                     |
| \<none\>                | has_parent                 | Every Qualifier concept is the child of its Vital Category concept.                                                                                                                                                                                                                                                                                                 |

VHAT Subset Name: Vital Categories

VistA File Number: 120.53

VistA File Name: GMRV VITAL CATEGORY

> Properties

| VistA Field | VHAT Attribute or Property Name | Notes                         |
|-----------------|-------------------------------------|-----------------------------------|
| .01, CATEGORY   | Designation Name                    | Required, must be 2-40 characters |

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                            |
|-----------------|----------------------------|----------------------------------------------------------------------|
| \<none\>        | has_parent                 | Every Category concept is the child of the concept Vital Categories. |

A Category concept is also the target of a Vital Qualifier concept’s has_VistA_category relationship.

### Allergy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Allergy Domain is composed of two subsets:

- Reactants that contains the substances that cause adverse reactions
- Reactions that contains terms describing those adverse reactions VHAT Subset Name: Reactants

VistA File Number: 120.82

VistA File Name: GMR ALLERGIES

> Properties

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 29%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><strong>VHAT Attribute or Property Name</strong></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01, NAME</td>
<td>Designation Name</td>
<td>Required, must be 3 – 30 characters</td>
</tr>
<tr class="even">
<td>1, ALLERGY TYPE</td>
<td>Allergy_Type</td>
<td>Required, set of {drug, food, drug/food, other}</td>
</tr>
<tr class="odd">
<td>120.823, .01 SYNONYM</td>
<td>Search_Term</td>
<td>Must be 2 – 30 characters; there can be multiple Search_Term properties for one reactant</td>
</tr>
</tbody>
</table>

> Relationships

| VistA Field     | VHAT Relationship Name | Notes                                                                                                                                                                                                                 |
|---------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4, DRUG INGREDIENTS | has_drug_ingredient        | When present this relationship has as a target a concept in the Drug Ingredients hierarchy, which appears under the National Drug file concept; there can be multiple has_drug_ingredient relationships for one reactant. |
| 5, VA DRUG CLASSES  | has_drug_class             | When present this relationship                                                                                                                                                                                            |

|          |            | has as a target a concept in the Drug Classes hierarchy, which appears under the National Drug file concept; there can be multiple has_drug_class relationships for one reactant. |
|----------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \<none\> | has_parent | Every Reactants concept is the child of the concept Reactants.                                                                                                                    |

VHAT Subset Name: Reactions VistA File Number: 120.83

VistA File Name: SIGN/SYMPTOMS

> Properties

| VistA Field | VHAT Attribute or Property Name | Notes                                                                                 |
|-----------------|-------------------------------------|-------------------------------------------------------------------------------------------|
| .01, NAME       | Designation Name                    | Must be 3 – 30 characters                                                                 |
| 2, SYNONYM      | Search_Term                         | Must be 2 – 30 characters; there can be multiple Search_Term properties for one reaction. |

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                      |
|-----------------|----------------------------|----------------------------------------------------------------|
| \<none\>        | has_parent                 | Every Reactions concept is the child of the concept Reactions. |

### National Drug File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The National Drug File (NDF) Domain is composed of two files maintained by the Pharmacy team:

- Drug Ingredient
- Drug Class

STS does not deploy to these two files, but maintains relationships between these NDF files and Reactants. This allows for participation in order checking decision support in the Computerized Patient Record System (CPRS) when the Reactant’s Allergy Type is in {drug, drug/food}.

VHAT Subset Name: Drug Ingredient VistA File Number: 50.416

VistA File Name: DRUG INGREDIENTS

The model must accurately reflect the contents of the DRUG INGREDIENTS file. The Designation Name is the name of the Ingredient. The VUID for the designation comes from the VUID field of the DRUG INGREDIENTS file.

> Properties

Drug Ingredient concepts have no properties.

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                                   |
|-----------------|----------------------------|-----------------------------------------------------------------------------|
| \<none\>        | has_parent                 | Every Drug Ingredient concept is the child of the concept Drug Ingredients. |

A Drug Ingredient concept can also be the target of an Allergy Reactants concept’s has\_ drug_ingredient relationship.

VHAT Subset Name: Drug Class VistA File Number: 50.605

VistA File Name: VA DRUG CLASS

The model must accurately reflect the contents of the VA DRUG CLASS file. The Designation Name is the name of the Ingredient. The VUID for the designation comes from the VUID field of the DRUG CLASS file.

> Properties

Drug Class concepts have no properties.

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                          |
|-----------------|----------------------------|--------------------------------------------------------------------|
| \<none\>        | has_parent                 | Every Drug Class concept is the child of the concept Drug Classes. |

A Drug Class concept can also be the target of an Allergy Reactants concept’s has\_ drug_class relationship.

### Clinical Document Titles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The standardized domain of Clinical Document Titles consists of three parts:

- TIU Status (which does not receive NTRT deployments)
- TIU Axis files
- TIU Titles

There are at this time 3 levels of document titles in the VA:

- Local titles
- “National” titles
- Standard Titles

Both the Local titles and the “National” titles exist on local VistA systems. “National” titles are titles that were mandated by a VA Central Office or Program Office to have the same wording and exist on every local system throughout the enterprise. Local titles were created to support local workings, and may contain jargon not easily recognized beyond that system (or sometimes even at other departments within the same system). This is not to say that Local title names may not appear consistently between many individual systems, only that they have not been specifically mandated to be that way. The quotation marks that appear around the term “National” are there because the titles that they describe are often confused with Standard Titles that were created by STS. Standard Titles have been created to be mapping

targets for local titles, if they are nationally mandated or not, and to be the primary title currency in the HDR or in messaging to other agencies beyond the VA. It is therefore important to determine from requestors of new Standard Titles whether the desired title is meant to live on local systems or in the HDR, and whether the title is meant to conform to the model of Title Standardization or otherwise convey a different level of expressivity.

Each title has essentially two representations:

- A collection of axis terms
- A unique text string that reflects their concatenation in a pre-determined order The five Document Ontology axes (in their order of listing in a title) are:
- Subject Matter Domain
- Role
- Setting
- Service
- Document Type

The title string usually contains the Preferred Names of axis terms, but there are some axis terms that are represented by their abbreviations. These terms occur in VHAT with the Designation Type of Abbreviation and are never deployed, remaining in VHAT only for reference.

VHAT Subset Name: TIU Status VistA File Number: 8925.6 VistA File Name: TIU STATUS

Any addition of TIU Statuses to VistA requires software package changes. Without code changes, VistA users are not able to use a new TIU Status. Authoring changes should not be done on this file without coordinating with the TIU package developer.

> Properties

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 30%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><strong>VHAT Attribute or Property Name</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01, NAME</td>
<td>Designation Name</td>
<td>Required, must be 3 – 30 characters</td>
</tr>
<tr class="even">
<td>.02, SYMBOL</td>
<td>VistA_Abbreviation</td>
<td>Must be 1 – 3 characters</td>
</tr>
<tr class="odd">
<td>.04, APPLIES TO</td>
<td>VistA_Interaction</td>
<td><p>Set: Values of {document, document definition} correspond to values of</p>
<p>{DOCMT, DEF} in VistA</p></td>
</tr>
<tr class="even">
<td>1, DESCRIPTION</td>
<td>VistA_Description</td>
<td>Word processing field</td>
</tr>
</tbody>
</table>

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                        |
|-----------------|----------------------------|------------------------------------------------------------------|
| \<none\>        | has_parent                 | Every TIU Status concept is the child of the concept TIU Status. |

VHAT Subset Name: TIU Titles VistA File Number: 8926.1

VistA File Name: TIU VHA ENTERPRISE STANDARD TITLE

> **NOTE:** The author must make sure that the target concept for each relationship is of the proper type, because there is no system check of these constraints, other than later manual review.

> Properties

| VistA Field     | VHAT Attribute | Notes                           |
|---------------------|--------------------|-------------------------------------|
| .01, STANDARD TITLE | Designation Name   | Required, must be 3 – 90 characters |

> Relationships

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 30%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><strong>VHAT Relationship Name</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.04, SUBJECT MATTER DOMAIN</td>
<td>has_SMD</td>
<td><blockquote>
<p>Present 0 to 1 times</p>
</blockquote></td>
</tr>
<tr class="even">
<td>.05, ROLE</td>
<td>has_role</td>
<td>Present 0 to 1 times</td>
</tr>
<tr class="odd">
<td>.06, SETTING</td>
<td>has_setting</td>
<td>Present 0 to 1 times</td>
</tr>
<tr class="even">
<td>.07, SERVICE</td>
<td>has_service</td>
<td>Present 0 to 1 times</td>
</tr>
<tr class="odd">
<td>.08, DOCUMENT TYPE</td>
<td>has_doctype</td>
<td>Present exactly once</td>
</tr>
<tr class="even">
<td>&lt;none&gt;</td>
<td>has_parent</td>
<td>Every Titles concept is the child of the concept “TIU Titles.</td>
</tr>
</tbody>
</table>

VHAT Subset Name: TIU SMD VistA File Number: 8926.2

VistA File Name: TIU LOINC SUBJECT MATTER DOMAIN

Subject Matter Domain terms reflect the subject matter and/or discipline that is relevant to a particular document, e.g. Cardiology, Primary Care, Radiology, etc.

> Properties

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 26%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><strong>VHAT Attribute</strong></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01, SUBJECT MATTER DOMAIN</td>
<td>Designation Name</td>
<td><blockquote>
<p>Required, must be 3 – 90 characters</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                            |
|-----------------|----------------------------|----------------------------------------------------------------------|
| \<none\>        | has_parent                 | Every SMD concept is the child of the concept Subject Matter Domain. |

An SMD concept can also be the target of a TIU Titles concept’s has_SMD relationship. VHAT Subset Name: TIU Role

VistA File Number: 8926.3

VistA File Name: TIU LOINC ROLE

Role terms reflect the clinical role of the author of the document relative to the subject of the document,

e.g. Physician, Registered Nurse, Therapist, etc.

> Properties

| VistA Field | VHAT Attribute | Notes                           |
|-----------------|--------------------|-------------------------------------|
| .01, ROLE       | Designation Name   | Required, must be 2 – 90 characters |

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                            |
|-----------------|----------------------------|------------------------------------------------------|
| \<none\>        | has_parent                 | Every Role concept is the child of the concept Role. |

A Role concept can also be the target of a TIU Titles concept’s has_role relationship. VHAT Subset Name: TIU Setting

VistA File Number: 8926.4

VistA File Name: TIU LOINC SETTING

Setting terms reflect the place where the service occurred, e.g. Emergency Department, Critical Care Unit, Residential Facility, etc.

> Properties

| VistA Field | VHAT Attribute | Notes                           |
|-----------------|--------------------|-------------------------------------|
| .01, SETTING    | Designation Name   | Required, must be 2 – 90 characters |

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                  |
|-----------------|----------------------------|------------------------------------------------------------|
| \<none\>        | has_parent                 | Every Setting concept is the child of the concept Setting. |

A Setting concept can also be the target of a TIU Titles concept’s has_setting relationship. VHAT Subset Name: TIU Service

VistA File Number: 8926.5

VistA File Name: TIU LOINC SERVICE

Service terms reflect the type of service or activity that was provided to the patient or other recipient of the service, e.g. History and Physical, Evaluation and Management, Procedure, etc.

> Properties

| VistA Field | VHAT Attribute | Notes                           |
|-----------------|--------------------|-------------------------------------|
| .01, SERVICE    | Designation Name   | Required, must be 2 – 90 characters |

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                  |
|-----------------|----------------------------|------------------------------------------------------------|
| \<none\>        | has_parent                 | Every Service concept is the child of the concept Service. |

A Service concept can also be the target of a TIU Titles concept’s has_service relationship. VHAT Subset Name: TIU Doctype

VistA File Number: 8926.6

VistA File Name: TIU LOINC DOCUMENT TYPE

Document Type terms reflect the type and usage of the document, e.g. Note, Consent, Clinical Warning, etc.

> Properties

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 20%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><strong>VHAT Attribute</strong></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01, DOCUMENT TYPE</td>
<td>Designation Name</td>
<td><blockquote>
<p>Required, must be 2 – 90 characters</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                        |
|-----------------|----------------------------|------------------------------------------------------------------|
| \<none\>        | has_parent                 | Every Doctype concept is the child of the concept Document Type. |

A Doctype concept can also be the target of a TIU Titles concept’s has_doctype relationship.

### Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two files are standardized in the Orders Domain, which refers to orders clinicians give for patient. Order Status describes the position in clinical workflow that the order currently occupies. The Nature of Order determines the actions that are to be taken based on the origination of the order or a change to the order.

VHAT Subset Name: Order Status VistA File Number: 100.01

VistA File Name: ORDER STATUS

> **NOTE:** Any additions of Order Statuses to VistA require software package changes. Without code changes, VistA users are not able to use a new Order Status. Authoring changes should not be done on this file without coordinating with the Orders package developer.

> Properties

| VistA Field  | VHAT Attribute or Property Name | Notes                           |
|------------------|-------------------------------------|-------------------------------------|
| .01, NAME        | Designation Name                    | Required, must be 3 – 20 characters |
| .02, SHORT NAME  | VistA_Short_Name                    | Must be 1 – 4 characters            |
| .1, ABBREVIATION | VistA_Abbreviation                  | Must be 1 – 3 characters            |
| 2, DESCRIPTION   | VistA_Description                   | Word processing field               |

> Relationships

| VistA Field | VHAT Relationship Name | Notes |
|-----------------|----------------------------|-----------|

| \<none\> | has_parent | Every Order Status concept is the child of the concept Order Status. |
|----------|------------|----------------------------------------------------------------------|

VHAT Subset Name: Nature of Order VistA File Number: 100.02

VistA File Name: NATURE OF ORDER

Any additions of Natures of Order to VistA require software package changes. Without code changes, VistA users are not able to use a new Nature of Order. Authoring changes should not be done on this file without coordinating with the Orders package developer. Four additional fields in this file are not locked- down for national deployment, but are controlled locally via a VistA option. How these fields can be set must be part of the collaboration with the Orders package developer.

> Properties

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 26%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><strong>VHAT Attribute or Property Name</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01, NAME</td>
<td>Designation Name</td>
<td>Required, must be 3 – 30 characters</td>
</tr>
<tr class="even">
<td>.02, CODE</td>
<td>VistA_Abbreviation</td>
<td>Required, must be 1 – 3 characters</td>
</tr>
<tr class="odd">
<td>.03, NON- INTERACTIVE</td>
<td>VistA_Interaction</td>
<td>Set: Values of {INTERACTIVE, NON- INTERACTIVE} correspond to same values in VistA</td>
</tr>
<tr class="even">
<td>.05, FRONT/BACKDOOR</td>
<td>VistA_Door</td>
<td>Set: Values of {frontdoor, backdoor, both} correspond to same values in VistA</td>
</tr>
<tr class="odd">
<td>.06, DC ONLY</td>
<td>VistA_Discontinued</td>
<td>Set: Values of {YES, NO} correspond to same values in VistA</td>
</tr>
<tr class="even">
<td>.11, CREATE ACTION</td>
<td>VistA_Create_Action</td>
<td>Set: Values of {YES, NO} correspond to same values in VistA</td>
</tr>
<tr class="odd">
<td>.14, DEFAULT SIGNATURE STATUS</td>
<td>VistA_Signature_Status</td>
<td><p>Set: Values of {ON CHART w/written orders, ELECTRONIC, NOT SIGNED, NOT</p>
<p>REQUIRED, ON CHART w/printed orders, NOT REQUIRED due to cancel, SERVICE CORRECTION to signed order} correspond to same values in VistA</p></td>
</tr>
</tbody>
</table>

> Relationships

| VistA Field | VHAT Relationship Name | Notes                                                                  |
|-----------------|----------------------------|----------------------------------------------------------------------------|
| \<none\>        | has_parent                 | Every Nature of Order concept is the child of the concept Nature of Order. |

### Medication Routes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medication Routes domain consists of a single file that enumerates the many ways that medications can be administered to patients. It also references routes as used by First DataBank. Both the Pharmacy and Radiology packages point to this file.

VHAT Subset Name: Medication Routes VistA File Number: 51.23

VistA File Name: STANDARD MEDICATION ROUTES

> Properties

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 34%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><blockquote>
<p><strong>VHAT Attribute or Property Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01, NAME</td>
<td><blockquote>
<p>Designation Name</p>
</blockquote></td>
<td>Required, must be 3-50 characters</td>
</tr>
<tr class="even">
<td>1, FIRST DATABANK MED ROUTE</td>
<td><blockquote>
<p>FDB_Med_Route</p>
</blockquote></td>
<td><blockquote>
<p>Must be 3-30 characters</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Relationships

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 26%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><strong>VHAT Relationship Name</strong></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>99.97, REPLACED BY VHA STANDARD TERM</td>
<td>vista_replaced_by</td>
<td>This field is populated when one Term/Concept replaces another Term/Concept. This field is controlled by standardization and should only be changed by the standardization processes. This field contains a pointer to a VHA standard term that replaces this entry.</td>
</tr>
<tr class="even">
<td>&lt;none&gt;</td>
<td>has_parent</td>
<td><blockquote>
<p>Every Medication Routes concept is the child of the concept Medication Routes.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Immunization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Immunization standardization is based loosely on CVX codes published by the CDC. Some VistA packages that touch on these files include Pharmacy and Clinical Reminders.

VHAT Subset Name: Immunization Procedure VistA File Number: 9999999.14

VistA File Name: IMMUNIZATION

> Properties

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 34%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><blockquote>
<p><strong>VHAT Attribute or Property Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01, NAME</td>
<td><blockquote>
<p>Designation_Text</p>
</blockquote></td>
<td>Required, must be 3-150 characters</td>
</tr>
<tr class="even">
<td>.02, SHORT NAME</td>
<td><blockquote>
<p>VistA_Short_Name</p>
</blockquote></td>
<td><blockquote>
<p>Required, must be 2-60 characters</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Relationships

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 26%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><strong>VHAT Relationship Name</strong></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>99.97, REPLACED BY VHA STANDARD TERM</td>
<td>vista_replaced_by</td>
<td>This field is populated when one Term/Concept replaces another Term/Concept. This field is controlled by standardization and should only be changed by the standardization processes. This field contains a pointer to a VHA standard term that replaces this entry.</td>
</tr>
<tr class="even">
<td>&lt;none&gt;</td>
<td>has_parent</td>
<td><blockquote>
<p>Every Immunizations concept is the child of the concept Immunization Procedure.</p>
</blockquote></td>
</tr>
</tbody>
</table>

VHAT Subset Name: Skin Test VistA File Number: 9999999.28 VistA File Name: SKIN TEST Properties

| VistA Field | VHAT Attribute or Property Name | Notes                         |
|-----------------|-------------------------------------|-----------------------------------|
| .01, NAME       | Designation_Text                    | Required, must be 3-10 characters |

> Relationships

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 26%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Field</strong></th>
<th><strong>VHAT</strong> <strong>Relationship Name</strong></th>
<th><blockquote>
<p><strong>Notes</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>99.97, REPLACED BY VHA STANDARD TERM</td>
<td>vista_replaced_by</td>
<td>This field is populated when one Term/Concept replaces another Term/Concept. This field is controlled by standardization and should only be changed by the standardization processes. This field contains a pointer to a VHA standard term that replaces this entry.</td>
</tr>
<tr class="even">
<td>&lt;none&gt;</td>
<td>Has_parent</td>
<td><blockquote>
<p>Every Skin Test concept is the child of the concept Skin Test.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Other issues related to Authoring VHAT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since terminology content must pass through several systems, from authoring to updating files in VistA, some kludges were put in place to avoid damage from potential errors. The information below describes best practices you can use to avoid any potential errors:

- When using the relationship of VistA_replaced_by, in appropriate domains (see full enumeration of permissible relationships in above domain descriptions), it is important that the appropriate designation of the replacing concept has an active status and has already been sent to VistA before the replaced by concept relationship, and thus its designation, is sent. This can be accomplished in separate messages or even in the same message as long as the replacing designation appears earlier in the message than the update to the replaced by designation. The same-message scenario works only if the new designation comes alphabetically before the earlier designation.
- If you are logged in to TDS and navigate away from the website then attempt to get back to your session by clicking the browser Back button you are not required to reenter your user name and password, the session stays active. When you are not using the application, you should log out.
- When inactivating terms for VistA, the approach has been to inactivate the designation that participates in the appropriate subset. Other ways to accomplish a term inactivation in VistA is to remove the designation from the subset or to take the additional step of inactivating the concept to which the designation belongs. This latter approach may cause a discrepancy from the expected Discovery results for inactive concepts. The current recommendation is that concepts not be inactivated when the desired result is that a term be inactivated in VistA.
- When reactivating Legacy Designations remember that they already have VUIDs and should not have new ones generated by the system. Therefore, in the VHAT import process, it is important to use the existing VUID for both the CODE and VUID fields; otherwise, the system will create new VUIDs to fill in any blanks.
- As of TDS Version 8, there is the ability to kill concepts and designations that have not yet been deployed to any site, completely removing any trace of their existence from TDS. This practice is not commonly used, but can be quite helpful, for example, should concepts be created with errors in their names or should VUIDs have been assigned when some already existed (see reactivating Legacy Designations).
- Should new standardized domains be added to our portfolio, their descriptions (e.g., Reactants, TIU Status) cannot have any words with more than 20 characters, lest they be unwieldy to display in our applications, most notably in the Terminology Browser.
- Similarly, if domains will require new Property or Relationship Types that are currently not found in VHAT, they will need to first loaded into VHAT as empty types before they are instantiated in concepts.
- Always remember to check over any import files to make sure that there is not content being imported that has unmet dependencies. This is true for relationships in VHAT, as well as for Map Sets, which are described later.
- Remember that the VHAT XML export function will include Map Sets in its output. If you do not want to turn around and import Map Sets from an export file, then comment out these sections.

### Issues Specific to VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Be aware of characters that must be escaped in HL7 messages, especially when they are destined for Word Processing fields in VistA files. These characters are typically from this set of four:

> {~\|\\}. As a corollary, since escaped HL7 characters are translated again upon arrival at VistA, be aware of character combinations destined for Word Processing fields, e.g., \E\\ \T\\ \S\\ and

> \R\\ There is no absolute prohibition against such characters, but it is important to recognize when there could be translation errors either to or from HL7 that cause checksum mismatches, and to attempt to model terms away from such issues.

- VistA can accept only 8-bit ASCII characters, so it is very important to make sure that any values, particularly for properties, conform to this set. It can be difficult to tell when extended ASCII characters appear in snippets of text that might otherwise be copied and pasted into import files. To check this follow the steps below:
  - Copy the text destined for VistA into an application like MS Word.
  - Save the text to a text file and be sure to specify that the character encoding be limited to the 8-bit ASCII set. For example, US-ASCII encoding or MS-DOS encoding, followed by allowing character substitutions upon saving.
  - Close the text-writing application and open the text document.
  - The text that appears should be cleansed of extended characters. Use this for authoring.
- Note that for any updates of Allergy Reactants that have an allergy type of DRUG or DRUG,FOOD and have linkages to Drug Ingredients or Drug Classes, patient data in VistA will be updated as the Reactant file is updated.
- Similar to some updates to Allergy Reactants as mentioned above, should an Immunization term be inactivated and replaced by another any reminder definitions, terms, or dialogs that featured the previous term may be updated upon deployment.
- As of March 2010, VistA does not gracefully handle deployments to TIU Titles that cause no updates. Patch TIU\*1\*240 was created to fix this issue, but has never obtained sufficient test sites for release.

# Standard Code Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enhancements to the VETS infrastructure now permit Standard Code Systems (SCS) data such as SNOMED CT, LOINC, and ICD-9-CM to be imported into VETS repository. SCS data is retrieved from Standard Development Organizations (SDO), the authoritative source, and imported in its native format. This allows you to demonstrate source transparency to its source vocabulary. SCS data are not deployed to VistA. Therefore, they do not go through the same versioning (deployment-\>candidate version-

\>version) workflow as VHAT or Map Sets deployments. Authoring/Creating XML file s

SCS data is constructed into XML files and validated against the TerminologyData.xsd file. The xml schema defines the structure and the elements, attributes and data types for SCS. Below are some of the behaviors for a few data elements.

The Designation Type data element defines the designation types for a code system such as Fully Specified Name, Preferred Name, and synonym. The preferred designation type defines the designation type that is displayed in TDS and the Terminology Browser. For instance, the designation types for ICD- 9-CM code system are short and long descriptions with the preferred designation typeset to Long Description. Upon initial import of a SCS, designation types are required and must be defined in the XML file. Subsequent versions for that SCS do not require these specifications if there are no changes to designation types. However including them is not harmful, especially if there is any question whether they have been previously specified. Additionally in subsequent versions, the preferred designation type may be changed to an existing designation type, and new designation types may be added.

SCS include concepts, designations, properties, and relationships. Concept properties and relationships may be updated. Updates include a new property or relationship to be added, inactivated, or changed. If a change occurs for relationships then the import file will contain the old value and the new value.

Subsets may be created from an SDO’s data. Currently there is not a business need however; functionality is available when the business case arises. Each subset has a VUID and a status but is only viewable in VTS database.

Finally, one issue has been observed when creating SCS XML files. The Preferred Name for the SCS must not contain an ampersand (&) character.

Import

Upon import of the SCS xml file the system validates the structure against the TerminologyData.xsd file only and does not catch data errors. All data must go through a manual data quality review process in the Terminology Browser to ensure that transparency is achieved to its source vocabulary.

There are two ways to verify the standard code system data has been successfully imported:

- Go to the SCS/Manage and verify the entries imported. The entries imported are derived by counting each coded concept element that has any change to it or one of its children. So it is a count of the concepts in the last import for that version (including appends) that have any type of change to them.
- View the code system in the Terminology Browser and look for a specific change that was imported.
- Each update or new version of a Standard Code Systems will be brought into VETS. Steps for importing SNOMED CT data

The SNOMED import uses multiple files to import a single version of SNOMED. When importing SNOMED CT baseline January 2006 version and the all_relationships files a local person should do the import and copy the file to their local machine.

For the baseline January 2006 version, it must be imported with the baseline_ready_for_import file first, then the all_relationships file. Each file takes some time (between 20 minutes and 2 hours) to import. If an import takes much longer than 2 hours it is possible that some database maintenance needs to be done.

Ask the administrator of the database server to run statistics on the schema in order to improve performance.

For subsequent versions, 4 files for each version need to be imported in a predetermined order:

- Diff_new_concepts_and_status_changes
- Diff_desig_changes
- Diff_desig_adds
- Snomed_Relationship_diff

These imports should not take long compared to the baseline version.

SCS versions may be removed from VETS but only the most recent version and only if there is not a Map Set dependent on that version of the standard code system. If there is a Map Set in the system whose source or target code system specifies that version of the code system, then the Map Set must be removed before the system will allow the code system version to be removed.

SNOMED CT is comprised of codes, terms, and relationships and only the is-a relationship has been brought into VTS. Therefore, in the Terminology Browser on the Concept Details and History page the headings Properties, Parents, or Children are not shown because no data is available for those headings.

# Map Sets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enhancements to the VETS infrastructure now permit Map Sets such as SNOMED CT to ICD-9-CM to be imported into the VETS repository. Map Sets may be created internally or adopted from a SDO or other entity. Content can be created via import of an .XML file or authored in the Terminology Editor (TED). Map Sets may be deployed to VistA so they go through the same versioning (deployment-

\>candidate version-\>finalized version) workflow of VHAT deployments. This functionality has not yet been implemented in production VistA, so it should not be used there until such time as the function is enabled.

Working with XML file s

Map Sets data is constructed into xml files and must be validated against the TerminologyData.xsd schema. The xml schema defines the structure and the elements, attributes and data types for Map Sets. Below are some of the business rules or behaviors of specific data elements

- The source and target code systems and its version specified for that map set must be imported into the system before the map set is imported.
- The map set action type value set contains add, update, or none. Add is used for initial import of that Map Set, the update is used to update the metadata, and none is used for subsequent imports.
- Map Entry action type value set contains add or update. Add is used to add new map entries and the update is used to change the status or the Map Entry order.
- On creation of a new map set xml file, the version name data element must be unique.
- The Preferred Name of the Map Set may not contain the &.
- Map Set deployments and candidate version deployments may be removed. If a Map Set deployment is removed AND it has been deployed to VistA, the system does not remove the update made to VistA therefore causing a checksum mismatch. To ensure checksums match the user can remove the updates from VistA in the following ways:
  - If a status value was updated the user must capture the VUID for that map entry (s) add the VUID to the Import file if it did not exist on the initial import
  - If a new map entry was introduced the user must capture the VUID for that map entry (s) add the VUID and to the Import file and inactivate. Once the VUIDs have been added to the existing import file then the file can be re-imported. This must be done to obtain matching checksums.
- Checksum mismatch may be a result of a new entry to the mapping file in VistA or the deployment. Updates to a Map Set may be the result of:
  - A new version of SNOMED CT was released and the SNOMED CT concept (source code) was changed from an active status.
  - A new version of ICD-9-CM was released and the ICD-9-CM concept (target code) was changed from an active status.
  - A NTRT request for changing a map entry and the status or the map entry order was changed.
- Map Set can be inactivated at the map set level only if all the map entries are inactive first.
- Map Set data can be exported using TDS export functionality. This exports the data into a Comma-Separated Values (CSV) file. If the map set contains data that is from a standard code system that includes decimals in the code then the user must be aware of formatting the data correctly so leading and trailing zeros are not lost.
- Once a Map Set is versioned, its Preferred Name must not be changed.
- Any type of deployment should not mix subsets and Map Sets.
- Partial Deployments is not a use case for Map Sets.
- Map Set deployments of any type may contain one and only one Map Set.

# Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Terminology configuration file provides instructions to the terminology deployment service (TDS). It defines deployable and non-deployable subsets, converts the terminology model entities (subsets, concepts, designations, properties and relationships) into HL7 message, supports new domains, and specifies the deployment order and data validation. Since Version 9, subsets can be deployable or non- deployable subsets. To change a subset to non-deployable a new tag called Active has been added. In deployable subsets, the Active tag is set to True. In non-deployable subsets, the Active tag is set to False.

## Browser

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the Browser configuration file is to define the number of the results that are displayed to users after a search has been conducted. The maximum number of results has been set to 1000 for every tab, though this can be changed for any individual tab.