---
title: PSO*7*294 Implementation Guide - Medication Reconciliation Tools
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: patch
doc_subject: Medication Reconciliation Tools
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*294
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: This product, Medication Reconciliation, represents the first class III to class I conversion. The software is a product initially developed at the Hines VA Hospital. The product utilizes Health Summary components and Text Integrated Utility (TIU) data objects to create a list of current medications
audience: 
keywords: 
  - summary
  - health
  - component
  - active
  - medications
  - remote
  - medication
  - object
  - components
  - print
page_count: 0
word_count: 9820
section_count: 17
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2008
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_img.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_img.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

![](pso-7-294-implementation-guide-medication-reconciliation-tools/001.png)

Medication Reconciliation

Tools

<span class="smallcaps">Implementation Guide</span>

May 2008

Veterans Health Information Technology

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Introduction](#introduction)
- [Tool \#1: Medication Reconciliation Profile Health Summaries](#tool-1-medication-reconciliation-profile-health-summaries)
  - [Creating the Health Summary Components](#creating-the-health-summary-components)
  - [Creating the Health Summary Type](#creating-the-health-summary-type)
  - [Adding the Health Summary to the CPRS Reports Tab](#adding-the-health-summary-to-the-cprs-reports-tab)
- [Tool \#2: Medication Worksheet](#tool-2-medication-worksheet)
  - [Creating the Health Summary Component](#creating-the-health-summary-component)
  - [Creating the Health Summary Type](#creating-the-health-summary-type-1)
  - [Adding the Health Summary to the CPRS Reports Tab](#adding-the-health-summary-to-the-cprs-reports-tab-1)
- [Tool \#3: Active/Pending/Expired Medications](#tool-3-activependingexpired-medications)
  - [Creating the TIU Data Objects](#creating-the-tiu-data-objects)
  - [Creating the Health Summary Component](#creating-the-health-summary-component-1)
  - [Creating the TIU Template (sample attached)](#creating-the-tiu-template-sample-attached)
- [Tool \#4: Remote Active Medications](#tool-4-remote-active-medications)
  - [Relevant Features of the Remote VA Medication Object](#relevant-features-of-the-remote-va-medication-object)
  - [Creating the Health Summary Components](#creating-the-health-summary-components-1)
  - [Creating the TIU Data Object](#creating-the-tiu-data-object)
- [Introduction](#introduction-1)
- [Step 1: Removing the PHARMACY SYSTEM File Parameter](#step-1-removing-the-pharmacy-system-file-parameter)
- [Step 2: Disabling the Menu Option that set the Parameter](#step-2-disabling-the-menu-option-that-set-the-parameter)
- [# Step 3: Redirecting the Health Summary Components and TIU Data Objects](#step-3-redirecting-the-health-summary-components-and-tiu-data-objects)
  - [Redirecting the Medication Reconciliation Health Summary](#redirecting-the-medication-reconciliation-health-summary)
    - [Redirecting the Health Summary Component](#redirecting-the-health-summary-component)
    - [Renaming the Health Summary Type](#renaming-the-health-summary-type)
  - [Redirecting the Medication Worksheet](#redirecting-the-medication-worksheet)
    - [Redirecting the Health Summary Component](#redirecting-the-health-summary-component-1)
    - [Renaming the Health Summary Type](#renaming-the-health-summary-type-1)
  - [Redirecting the Active/Pending/Expired Medications](#redirecting-the-activependingexpired-medications)
    - [Redirecting the TIU Data Object(s)](#redirecting-the-tiu-data-objects)
    - [Redirecting the Health Summary Component](#redirecting-the-health-summary-component-2)
  - [Redirecting Remote Active Medications](#redirecting-remote-active-medications)
    - [Redirecting the TIU Data Object](#redirecting-the-tiu-data-object)
    - [Redirecting the Health Summary Components](#redirecting-the-health-summary-components)
This guide refers to steps needed to set up components for Medication Reconciliation using routines introduced by patches PSO\*7\*294 and TIU\*1\*238. Please ensure that the patches have been installed prior to proceeding with the steps in the followings sections, as this guide is divided into two sections, assisting sites that are installing Medication Reconciliation for the first time and sites that are transitioning from the class III version to the class I version of Medication Reconciliation. Ensure you are using the correct section to implement Medication Reconciliation.
Table of Contents
<span id="_Toc183421465" class="anchor"></span>
Implementation (New Installation)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product, Medication Reconciliation, represents the first class III to class I conversion. The software is a product initially developed at the Hines VA Hospital. The product utilizes Health Summary components and Text Integrated Utility (TIU) data objects to create a list of current medications. Medication Reconciliation also leverages the Remote Data Interoperability (RDI) software to include medication data from other sites.

This Implementation section refers to steps needed to set up components for Medication Reconciliation using routines introduced by patches PSO\*7\*294 and TIU\*1\*238. Please ensure that the patches have been installed prior to proceeding with these steps.

Upon completion of the steps listed in this Implementation section, users will be able to retrieve reports useful for Medication Reconciliation by selecting the newly created Health Summaries on the CPRS Reports tab or by using the newly created TIU templates and objects (from the CPRS Notes tab templates drawer) and/or any progress note titles in which they have been embedded.

*Note: On occasion, the remote tools will need to be selected (clicked) twice, as it takes longer to retrieve the data than CPRS GUI waits for the report.*

# Tool \#1: Medication Reconciliation Profile Health Summaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medication Reconciliation Profiles are Health Summaries that provide an alphabetized list of patient medications from several sources, including outpatient prescriptions, unit dose medications, non-VA documented medications, and active remote VA medications and contain a section labeled “Other medications previously dispensed in the last year” for discontinued meds. While creating a list, a series of “order couplets” are generated that can be used to identify orders that should be added, discontinued, changed, or left as-is. These summaries are most commonly used at hospital admission and discharge, when the patient is transitioning between inpatient and outpatient status. The following is a list of routines used by this tool.

| Routine      | Description                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------|
| PSOQUAP/PSOQUAP2 | The main Health Summary drivers.                                                                  |
| PSOQ0076         | A specific utility library to calculate last fill dates.                                          |
| PSOQUTIL         | A utility library routine to format prescription SIGs.                                            |
| PSOQCF04         | Clinical reminder style computed finding to identify the last documentation date for Non-VA meds. |
| PSOQRART         | A Health Summary component for remote allergy/ADR data.                                           |

*Note: The remote data returned does NOT include any non-VA meds documentation from the other facilities, as that data is not stored in the Health Data Repository (HDR).*

## Creating the Health Summary Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps show how to create both of the Health Summary components. These steps may be performed by the IRM programmer who installed the patch routines or by a CAC/Health Summary Manager if they have the appropriate options.

*Note: The PRINT ROUTINE must be named accordingly for each Health Summary component and cannot vary. It is our recommendation that the other fields listed here be named accordingly when creating the Health Summary components.*Medication Reconciliation

- COMPONENT: Medication Reconciliation
- PRINT ROUTINE: EN;PSOQUAP2
- HEALTH SUMMARY COMPONENT ABBREVIATION: MRP
- DESCRIPTION: This component provides an alphabetized list of the patient's medications from several sources, including outpatient prescriptions, unit dose medications, non-VA documented medications, and active remote medications using the Remote Data Interoperability interface to the Health Data Repository.

.

Remote Allergy/ADR Data

- COMPONENT: Remote Allergy/ADR Data
- PRINT ROUTINE: ENHS;PSOQRART
- HEALTH SUMMARY COMPONENT ABBREVIATION: RART
- DESCRIPTION: This component displays remote allergy and adverse drug reaction information using the Remote Data Interoperability features of the Health Data Repository. Data is shown from other stations only and not the local station.

Follow these examples to create your Health Summary components.

Example: Medication Reconciliation

Select <u>Health Summary Overall Menu</u> Option: 4 Health Summary Maintenance Menu

Select Health Summary Maintenance Menu Option: 2 Create/Modify Health Summary Components

Select COMPONENT: Medication Reconciliation

Are you adding 'Medication Reconciliation' as

a new HEALTH SUMMARY COMPONENT? No// y (Yes)

HEALTH SUMMARY COMPONENT NUMBER: *578041*// \<Enter\>

HEALTH SUMMARY COMPONENT ABBREVIATION: MRP

Do you wish to duplicate an existing COMPONENT? YES// n NO

NAME: Medication Reconciliation Replace \<Enter\>

PRINT ROUTINE: EN;PSOQUAP2\<Enter\>

ABBREVIATION: MRP\<Enter\>

DESCRIPTION:

No existing text

Edit? NO// YES

-------------------------------------------------example continues--------------------------------------------------

==\[ WRAP \]==\[ INSERT \]=============\< DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

This component provides an alphabetized list of the patient's medications from several sources, including outpatient prescriptions, unit dose medications, non-VA documented medications, and active remote medications using the Remote Data Interoperability interface to the Health Data Repository.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: \<Enter\>

Select SELECTION FILE: \<Enter\>

ADD new Component to the AD HOC Health Summary? NO// YES \<Enter\>

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Select COMPONENT: Medication Reconciliation// \<Enter\>              

SUMMARY ORDER: 1705// \<Enter\> 1705 

HEADER NAME: \<Enter\>

Please hold on while I resequence the summary order.............................

................................................................................

\>\>\> Returning to Create/Modify Health Summary Component Option.

Example: Remote Allergy/ADR Data

Select COMPONENT: Remote Allergy/ADR Data

Are you adding 'Remote Allergy/ADR Data' as

a new HEALTH SUMMARY COMPONENT? No// y (Yes)

HEALTH SUMMARY COMPONENT NUMBER: *578042*//

HEALTH SUMMARY COMPONENT ABBREVIATION: RART

Do you wish to duplicate an existing COMPONENT? YES// n NO

NAME: Remote Allergy/ADR Data Replace

PRINT ROUTINE: ENHS;PSOQRART

ABBREVIATION: RART

DESCRIPTION:

No existing text

Edit? NO// YES

==\[ WRAP \]==\[ INSERT \]=============\< DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

This component displays remote allergy and adverse drug reaction information using the Remote Data Interoperability features of the Health Data Repository. Data is shown from other stations only and not the local station.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

-------------------------------------------------example continues--------------------------------------------------

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: \<Enter\>

Select SELECTION FILE: \<Enter\>

ADD new Component to the AD HOC Health Summary? NO// YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Select COMPONENT: Remote Allergy/ADR Data// \<Enter\>              

SUMMARY ORDER: 1710// \<Enter\> 1710 

HEADER NAME: \<Enter\>

Please hold on while I resequence the summary order.............................

................................................................................\>*\>\>*

Returning to Create/Modify Health Summary Component Option.

## Creating the Health Summary Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Summary type is the combination of Health Summary components that can be made available through CPRS on the Reports tab. Using the *Create/Modify Health Summary Type* \[GMTS TYPE ENTER/EDIT\] option, create a Health Summary named Medication Reconciliation and include components BADR (national component for local allergy/ADR data), RART (remote allergy/ADR data), and MRP (alphabetized Health Summary listing of all medications). Follow the example below to create your Health Summary type.

Select Health Summary Maintenance Menu Option: 6 Create/Modify Health Summary

Type

Select Health Summary Type: Medication Reconciliation

Are you adding 'Medication Reconciliation' as

a new HEALTH SUMMARY TYPE (the 63rd)? No// y YES

NAME: Medication Reconciliation Replace \<Enter\>

TITLE: Medication Reconciliation

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: y yes

SUPPRESS SENSITIVE PRINT DATA: ?

Answer with '9 DIGIT SSN', '4 DIGIT SSN', or, 'NO SSN'

Choose from:

0 9 DIGIT SSN

1 4 DIGIT SSN

2 NO SSN

SUPPRESS SENSITIVE PRINT DATA: NO SSN NO SSN

LOCK:

OWNER: USER//

-------------------------------------------------example continues--------------------------------------------------

Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO

Select COMPONENT: BADR  ADVERSE REACTIONS/ALLERG BRIEF BADR

SUMMARY ORDER: 5// \<Enter\> 5

HEADER NAME: Brief Adv React/All// \<Enter\>

Select COMPONENT: RART  Remote Allergy/ADR Data RART

SUMMARY ORDER: 10// \<Enter\> 10

HEADER NAME: \<Enter\>

Select COMPONENT: Medication Reconciliation   MRP

SUMMARY ORDER: 15// \<Enter\> 15

HEADER NAME: \<Enter\>

Select COMPONENT: \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// YES

HEALTH SUMMARY TYPE INQUIRY

Type Name: Medication Reconciliation

Title: Medication Reconciliation

Owner: USER

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes

SUPPRESS SENSITIVE PRINT DATA: NO SSN

                                   Max        Hos  ICD   Pro  CPT

Abb   Ord    Component Name        Occ  Time  Loc  Text  Nar  Mod  Selection

----------------------------------------------------------------------------

BADR  5       Brief Adv React/All                            

RART  10      Remote Allergy/ADR D                           

MRP   15      Medication Reconcili  

\* = Disabled Components

Select COMPONENT:

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Please hold on while I resequence the summary order...

## Adding the Health Summary to the CPRS Reports Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Note: It is important to note that this applies for only sites that do not use the parameter ORWRP HEALTH SUMMARY LIST ALL. If that parameter is set to ‘YES’ on a system, then the sequences listed here have no impact, and all Health Summaries in the database will be displayed and available in CPRS GUI on the Reports tab.*

This is one of many available methods for adding a Health Summary to the CPRS Reports tab. Follow these steps to add the Health Summary to the CPRS Reports tab.

1.  From the *CPRS MANAGER MENU* \[ORMGR\] menu, enter PE for CPRS Configuration (Clin Coord) ... \[OR PARAM COORDINATOR MENU\].
2.  Then, enter GP for GUI Parameters ... \[ORW PARAM GUI\] and proceed with the following steps. 

Select GUI Parameters Option: HS  GUI Health Summary Types

Allowable Health Summary Types may be set for the following:

     2   User          USR    \[choose from NEW PERSON\]

     4   System        SYS    \[HINES.MED.VA.GOV\]

Enter selection: 4  System   HINES.MED.VA.GOV

---- Setting Allowable Health Summary Types  for System: HINES.MED.VA.GOV ----

Select Sequence: ?

Sequence  Value

--------  -----

1         GMTS HS ADHOC OPTION

2         OUTPATIENT SUMMARY LIST

5         PATIENT EDUCATION

8         ORDERS SUMMARY

Select Sequence: 3

Are you adding 3 as a new Sequence? Yes// \<Enter\>  YES

Sequence: 3// \<Enter\>   3

Health Summary: Medication Reconciliation 

Please note that the Health Summary does not show immediately if you already have CPRS GUI open, but it will be present for all users the next time they start the program, as shown below.

![](pso-7-294-implementation-guide-medication-reconciliation-tools/002.png)

# Tool \#2: Medication Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medication Worksheet is a patient-friendly list of a patient’s outpatient prescriptions in a grid format. As a Health Summary, it is easily printed so that it can be given to the patient upon hospital discharge or when leaving a clinic visit.

The contents of the Medication Worksheet are limited to the VistA Outpatient Pharmacy prescriptions in active, suspended, or pending status. There are several known categories of orders that are not present in the current version of this tool. They include orders entered via the Inpatient Medication Orders for Outpatients (IMO) functionality, recently expired medications, or remote VA medications. Additionally, discontinued medications are not recorded on the Medication Worksheet, and medications with a status of “HOLD” are not clearly labeled to differentiate them from active medications. The following is a list of routines used by this tool.

| Routine | Description                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------|
| PSOQMCAL    | A newer version of Seattle/Puget Sound's original Medication Worksheet routine built to address the addition of pending meds. |
| PSOQ0076    | A utility to calculate last fill dates, refills remaining, and Rx expiration date.                                            |
| PSOQ0186    | A Health Summary stub for formatting.                                                                                         |

*Programmer NotesRoutine PSOQ0186 is a stub designed to format the output into a Health Summary. It has several options coded for the selection of pharmacy "division" (for name and phone number). A programmer at your site may want to swap which line is active by moving the ‘;’ (comment symbol) to the other line.*

## Creating the Health Summary Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps show how to create the Health Summary component. These steps may be performed by the IRM programmer who installed the patch routines or by a CAC/Health Summary Manager if they have the appropriate options.

*Note: The PRINT ROUTINE must be named accordingly for the Health Summary component and cannot vary. It is our recommendation that the other fields listed here be named accordingly when creating the Health Summary component.*Medication Reconciliation

- COMPONENT: Medication Worksheet
- PRINT ROUTINE: TASK2;PSOQ0186
- HEALTH SUMMARY COMPONENT ABBREVIATION: MWS
- DESCRIPTION: This component provides an alphabetized list of the patient's medications from several sources, including outpatient prescriptions, unit dose medications, non-VA documented medications, and active remote medications using the Remote Data Interoperability interface to the Health Data Repository.

Follow this example to create your Health Summary component.

Select Health Summary Maintenance Menu Option: 2 Create/Modify Health Summary Components

Select COMPONENT: Medication Worksheet

Are you adding 'Medication Worksheet' as

a new HEALTH SUMMARY COMPONENT? No// y (Yes)

HEALTH SUMMARY COMPONENT NUMBER: 500005// \<Enter\>

HEALTH SUMMARY COMPONENT ABBREVIATION: MWS \<Enter\>

Do you wish to duplicate an existing COMPONENT? YES// n NO

NAME: Medication Worksheet Replace \<Enter\>

PRINT ROUTINE: TASK2;PSOQ0186 \<Enter\>

ABBREVIATION: MWS// \<Enter\>

DESCRIPTION:

No existing text

Edit? NO// y YES

==\[ WRAP \]==\[ INSERT \]=============\< DESCRIPTION \>===========\[ \<PF1\>H=Help \]=== This component provides an alphabetized list of the patient's medications from several sources, including outpatient prescriptions, unit dose medications, non-VA documented medications, and active remote medications using the Remote Data Interoperability interface to the Health Data Repository.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: \<Enter\>

Select SELECTION FILE: \<Enter\>

ADD new Component to the AD HOC Health Summary? NO// y YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Select COMPONENT: Medication Worksheet// \<Enter\> MWS

SUMMARY ORDER: 1190// \<Enter\> 1190

HEADER NAME:

Please hold on while I resequence the summary order.............................

................................................................................

\>\>\> Returning to Create/Modify Health Summary Component Option.

## Creating the Health Summary Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Summary type is the combination of Health Summary components that can be made available through CPRS on the Reports tab. Follow this example to create your Health Summary type.

Select Health Summary Maintenance Menu Option: 6  Create/Modify Health Summary Type

Select Health Summary Type: Medication Worksheet

Are you adding 'Medication Worksheet' as

    a new HEALTH SUMMARY TYPE (the 64th)?   No// y  YES

-------------------------------------------------example continues--------------------------------------------------

NAME: Medication Worksheet  Replace \<Enter\>

TITLE: Medication Worksheet

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: y  yes

SUPPRESS SENSITIVE PRINT DATA: NO SSN

LOCK: \<Enter\>

OWNER: USER

Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO

Select COMPONENT: MWS  Medication Worksheet MWS

SUMMARY ORDER: 5// \<Enter\> 5

HEADER NAME: \<Enter\>

Select COMPONENT: \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Please hold on while I resequence the summary order.

## Adding the Health Summary to the CPRS Reports Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Note: It is also important to note that this applies for only sites that do not use the parameter ORWRP HEALTH SUMMARY LIST ALL. If that parameter is set to ‘YES’ on a system, then the sequences listed here have no impact, and all Health Summaries in the database will be displayed and available in CPRS GUI on the Reports tab.*

This is one of many available methods for adding a Health Summary to the CPRS Reports tab. Follow these steps to add the Health Summary to the CPRS Reports tab.

3.  From the *CPRS MANAGER MENU* \[ORMGR\] menu, enter PE for CPRS Configuration (Clin Coord) ... \[OR PARAM COORDINATOR MENU\].
4.  Then, enter GP for GUI Parameters ... \[ORW PARAM GUI\] and proceed with the following steps. 

Select GUI Parameters Option: HS  GUI Health Summary Types

Allowable Health Summary Types may be set for the following:

     2   User          USR    \[choose from NEW PERSON\]

     4   System        SYS    \[HINES.MED.VA.GOV\]

Enter selection: 4  System   HINES.MED.VA.GOV

---- Setting Allowable Health Summary Types  for System: HINES.MED.VA.GOV ----

Select Sequence: ?

Sequence  Value

--------  -----

1         GMTS HS ADHOC OPTION

2 OUTPATIENT SUMMARY LIST

3 Medication Reconciliation

5         PATIENT EDUCATION

8         ORDERS SUMMARY

Select Sequence: 4

Are you adding 4 as a new Sequence? Yes// \<Enter\>  YES

Sequence: 4// \<Enter\>   4

Health Summary: Medication Worksheet 

Please note that the Health Summary does not show immediately if you already have CPRS GUI open, but it will be present for all users the next time they start the program, as shown below.

> ![](pso-7-294-implementation-guide-medication-reconciliation-tools/003.png)

# Tool \#3: Active/Pending/Expired Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Active/Pending/Expired Medications has the following differences from the Medication Worksheet.

- As a TIU data object, it is accessed from the CPRS Notes Tab instead of the Reports tab.
- This data object includes the category Recently Expired Medications that is not present in the Medication Worksheet.

Also, please note that discontinued medications are explicitly excluded from the list of medications.

The following is a list of routines used by this tool.

| Routine | Description                                                                                                                   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------|
| TIULMED     | The TIU Data object for medications.                                                                                              |
| PSOQ0496    | A copy of class I routine PSOORRL to account for the changes being made in TIULMED so that they do not affect non-VA medications. |
| PSOQ0236    | A Health Summary component that calls the object.                                                                                 |

## Creating the TIU Data Objects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must be a member of the Clinical Coordinator user class and must have DUZ(0)=”@” to perform this procedure. The TIU data objects are driven by routine TIULMED, a class I routine that supports many kinds of medication objects. Upon installation of PSO\*7\*294, use of the variable TIUDATE will allow you to create an object which includes expired medications but not discontinued medications. The following examples show a recommended setting of 30 (days) for the value of TIUDATE, but you may adjust it in the OBJECT METHOD to a value between 1 and 180 days.

*Note: The OBJECT METHOD must be named accordingly for the TIU data objects and cannot vary. It is our recommendation that the NAME fields listed here be named accordingly when creating the TIU data objects.*Active/Pending/Expired Medications

- NAME: Active/Pending/Expired Medications
- OBJECT METHOD:

S TIUDATE=30 S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",,,3) K TIUDATE

> *Note: In the OBJECT METHOD, you can change the TIUDATE field value of 30 to any value between 1 and 180.*Active/Pending/Expired Medications (W/O Supplies)

- NAME: Active/Pending/Expired Medications (W/O Supplies)
- OBJECT METHOD:

S TIUDATE=30 S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",,,3,,,0) K TIUDATE

> *Note: In the OBJECT METHOD, you can change the TIUDATE field value of 30 to any value between 1 and 180.*

Follow these examples to create your TIU data objects.

  
Example: Active/Pending/Expired Medications

Select TIU Maintenance Menu Option: 2 Document Definitions (Manager)

Select Document Definitions (Manager) Option: 4 Create Objects

START DISPLAY WITH OBJECT: FIRST// .............................................

Select Action: Next Screen// CREATE Create

Enter the Name of a new Object: ACTIVE/PENDING/EXPIRED MEDICATIONS

CLASS OWNER: CLINICAL COORDINATOR Replace @

PERSONAL OWNER: USER RMS 11INF PHARMACIST

Entry added

Objects Feb 08, 2008@14:13:24 Page: 3 of 105

Objects

\+ Status

30 ACTIVE/PENDING/EXPIRED MEDICATIONS I

31 ADAC A

32 ADAM A

33 ADDICTION CLINIC A

34 ADDITIONAL VESSEL, INJECTION A

35 ADJUSTED CALCIUM WORKSHEET A

36 ADMDIAG A

37 ADMISSION DATE A

38 ADMTYPE A

39 ADRC A

40 ADRM A

41 AFB CULTURE & SMEAR A

42 AFP A

43 AGENT ORANGE EXAM DATE A

\+ ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\>

Change View Try Quit

Create Owner

Select Action: Next Screen// DET Detailed Display/Edit

Select Entry: (30-43): 30

Select Action: Quit// TECH Technical Fields

OBJECT METHOD: S TIUDATE=30 S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",,,3) K TIUDATE

Select Action: Next Screen// BAS Basics

NAME: ACTIVE/PENDING/EXPIRED MEDICATIONS Replace

ABBREVIATION:

PRINT NAME: ACTIVE/PENDING/EXPIRED MEDICATIONS Replace

PERSONAL OWNER: USER// USER

STATUS: (A/I): INACTIVE// A ACTIVE Entry Activated.

Select Action: Next Screen// QUIT Quit ......................................

Select Action: Next Screen// QUIT Quit

Select Document Definitions (Manager) Option:

  
Example: Active/Pending/Expired Medications (W/O Supplies)

Select TIU Maintenance Menu Option: 2 Document Definitions (Manager)

Select Document Definitions (Manager) Option: 4 Create Objects

START DISPLAY WITH OBJECT: FIRST// .............................................

Select Action: Next Screen// CREATE Create

Enter the Name of a new Object: ACTIVE/PENDING/EXPIRED MEDICATIONS (W/O Supplies)

CLASS OWNER: CLINICAL COORDINATOR Replace @

PERSONAL OWNER: USER RMS 11INF PHARMACIST

Entry added

Objects Feb 08, 2008@14:13:24 Page: 3 of 105

Objects

\+ Status

31 ACTIVE/PENDING/EXPIRED MEDICATIONS (W/O SUPPLIES) I

32 ADAC A

33 ADAM A

34 ADDICTION CLINIC A

35 ADDITIONAL VESSEL, INJECTION A

36 ADJUSTED CALCIUM WORKSHEET A

37 ADMDIAG A

38 ADMISSION DATE A

39 ADMTYPE A

40 ADRC A

41 ADRM A

42 AFB CULTURE & SMEAR A

43 AFP A

44 AGENT ORANGE EXAM DATE A

\+ ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\>

Change View Try Quit

Create Owner

Select Action: Next Screen// DET Detailed Display/Edit

Select Entry: (31-44): 31

Select Action: Quit// TECH Technical Fields

OBJECT METHOD: S TIUDATE=30 S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",,,3,,,0) K TIUDATE

Select Action: Next Screen// BAS Basics

NAME: ACTIVE/PENDING/EXPIRED MEDICATIONS (W/O SUPPLIES) Replace

ABBREVIATION:

PRINT NAME: ACTIVE/PENDING/EXPIRED MEDICATIONS (W/O SUPPLIES) Replace

PERSONAL OWNER: USER// USER

STATUS: (A/I): INACTIVE// A ACTIVE Entry Activated.

Select Action: Next Screen// QUIT Quit ......................................

Select Action: Next Screen// QUIT Quit

Select Document Definitions (Manager) Option:

## Creating the Health Summary Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Health Summary is for Active/Pending/Expired medications with supplies and is hardcoded as such. These steps show how to create the Health Summary component. These steps may be performed by the IRM programmer who installed the patch routines or by a CAC/Health Summary Manager if they have the appropriate options.

*Note: The PRINT ROUTINE must be named accordingly for the Health Summary component and cannot vary. It is our recommendation that the other fields listed here be named accordingly when creating the Health Summary component.*Active/Pending/Expired Meds

- COMPONENT: Active/Pending/Expired Meds
- PRINT ROUTINE: RPT;PSOQ0236
- HEALTH SUMMARY COMPONENT ABBREVIATION: PSO2
- DEFAULT HEADER NAME: Recent Rx Profile
- DESCRIPTION: This component provides a Health Summary equivalent to the new TIU object for ACTIVE/PENDING/EXPIRED MEDICATIONS. There are several parameters available with the basic object that have not been tested with this Health Summary component. It is hard-coded for up to 180 days of expired prescriptions to be included and includes supply items by design.

Follow this example to create your Health Summary component.

OPTION: GMTS IRM/ADPAC COMP EDIT Create/Modify Health Summary Components

Create/Modify Health Summary Components

Select COMPONENT: Active/Pending/Expired Meds

Are you adding 'Active/Pending/Expired Meds' as

a new HEALTH SUMMARY COMPONENT? No// y (Yes)

HEALTH SUMMARY COMPONENT NUMBER: 578052// \<Enter\>

HEALTH SUMMARY COMPONENT ABBREVIATION: PSO2

Do you wish to duplicate an existing COMPONENT? YES// n NO

NAME: Active/Pending/Expired Meds \<Enter\> Replace

PRINT ROUTINE: RPT;PSOQ0236

ABBREVIATION: PSO2// \<Enter\>

DESCRIPTION:

No existing text

Edit? NO// y YES

==\[ WRAP \]==\[ INSERT \]=============\< DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

This component provides a Health Summary equivalent to the new TIU object for ACTIVE/PENDING/EXPIRED MEDICATIONS. There are several parameters available with the basic object that have not been tested with this Health Summary component. It is hard-coded for up to 180 days of expired prescriptions to be included and includes supply items by design.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: Recent Rx Profile

Select SELECTION FILE: \<Enter\>

-------------------------------------------------example continues--------------------------------------------------

ADD new Component to the AD HOC Health Summary? NO// y YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Select COMPONENT: Active/Pending/Expired Meds// \<Enter\> PSO2

SUMMARY ORDER: 1715// \<Enter\> 1715

HEADER NAME:

Please hold on while I resequence the summary order.............................

................................................................................

\>\>\> Returning to Create/Modify Health Summary Component Option.

Select COMPONENT:

## Creating the TIU Template (sample attached)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Along with this documentation and the routines, a sample TIU TEMPLATE file (.txt format) has been distributed. It uses a locally created object, which is named “ACTIVE/PENDING/EXPIRED MEDICATIONS”.

![](pso-7-294-implementation-guide-medication-reconciliation-tools/004.png)

To use this format, install (import) the selected template to CPRS GUI and place it in the Shared Templates drawer in a commonly known location. The providers can right-click the template, select PRINT/PREVIEW, and choose the PRINT button to generate a list.

How to import the sample template found within this document:

1.  Open the TXT file (double-click). If it asks for a program selection, use Notepad.
2.  There, you will have a “SAVE AS” choice to save it to your desktop or file server.
3.  Then, you can use the CPRS GUI TIU template editor to Import it.
4.  The steps there are Notes Tab \> Options \> Edit Shared Templates \> Tools \> Import Template \> Browse for File \> OK. (It requires ASU of clinical coordinator for all the choices to appear.)

The template included above contains objects for the PATIENT ADDRESS and PATIENT PHONE. In case your site does not have suitable replacements for these objects, patch PSO\*7\*294 contains routine PSOQTIU4 that will allow you to create them.

NAME: PATIENT ADDRESS ABBREVIATION: PAD

TYPE: OBJECT STATUS: ACTIVE

OBJECT METHOD: S X=\$\$ADDRESS^PSOQTIU4(DFN,"^TMP(""PSOQADDR"",\$J)")

NAME: PATIENT PHONE ABBREVIATION: PPH

TYPE: OBJECT STATUS:ACTIVE

OBJECT METHOD: S X=\$\$PHONE^PSOQTIU4(DFN)

After creating Tool \#3, the Medication List for Patients is available, as shown below.

![](pso-7-294-implementation-guide-medication-reconciliation-tools/005.png)

# Tool \#4: Remote Active Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This tool comprises two standalone Health Summary components and TIU data objects that can be used various places within CPRS. One object/component retrieves active remote VA medications, and the other retrieves remote allergy/ADR information. Please note that Remote Active Medications stores only active and suspended medications and does not store discontinued medications. The following is a list of routines used by this tool.

| Routine | Description                                       |
|-------------|-------------------------------------------------------|
| PSOQ0595    | The Remote Medications TIU object and Health Summary. |
| PSOQRART    | The Remote Allergy/ADR data as Health Summary.        |
| PSOQUTIL    | The Utility Library.                                  |

## Relevant Features of the Remote VA Medication Object

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data will always be returned even when no medications are found. The following are possible headers.

- Remote Data from HDR not available
- No Remote Data available for this patient
- No Active Remote Medications for this patient
- Active Medications from Remote Data

SUSPENDED status RXS is included as part of the ACTIVE listing. The display of SUSPENDED status reads as ACTIVE/SUSPENDED to be consistent with CPRS displays.

## Creating the Health Summary Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps show how to create both of the Health Summary components. These steps may be performed by the IRM programmer who installed the patch routines or by a CAC/Health Summary Manager if they have the appropriate options.

*Note: The PRINT ROUTINE must be named accordingly for each Health Summary component and cannot vary. It is our recommendation that the other fields listed here be named accordingly when creating the Health Summary components.*Remote Active Medications

- COMPONENT: Remote Active Medications
- PRINT ROUTINE: ENHS;PSOQ0595
- HEALTH SUMMARY COMPONENT ABBREVIATION: RDIM
- DESCRIPTION: This component will display the details of a patient’s remote active outpatient medications using data from the Health Data Repository.

.

*Note: If you created the Remote Allergy/ADR Data Health Summary component in Tool \#1, you do not have to create it again.*Remote Allergy/ADR Data

- COMPONENT: Remote Allergy/ADR Data
- PRINT ROUTINE: ENHS;PSOQRART
- HEALTH SUMMARY COMPONENT ABBREVIATION: RART
- DESCRIPTION: This component displays remote allergy and adverse data information using the Remote Data Interoperability features of the Health Data Repository. Data is shown from other stations only and not the local station.

Follow these examples to create your Health Summary components.

Example: Remote Active Medications

Select OPTION NAME: GMTS MANAGER Health Summary Overall Menu

Select Health Summary Overall Menu Option: 4 Health Summary Maintenance Menu

Select Health Summary Maintenance Menu Option: 2

Create/Modify Health Summary Components

Select COMPONENT: Remote Active Medications

Are you adding 'Remote Active Medications' as

a new HEALTH SUMMARY COMPONENT? No// y (Yes)

HEALTH SUMMARY COMPONENT NUMBER: 500006// \<Enter\>

Do you wish to duplicate an existing COMPONENT? YES// n NO

NAME: Remote Active Medications \<Enter\> Replace

PRINT ROUTINE: ENHS;PSOQ0595

ABBREVIATION: RDIM

DESCRIPTION:

No existing text

Edit? NO// YES

==\[ WRAP \]==\[ INSERT \]=============\< DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

This component will display the details of a patient's remote active Outpatient medications using data from the Health Data Repository.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: \<Enter\>

Select SELECTION FILE: \<Enter\>

ADD new Component to the AD HOC Health Summary? NO// y YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Select COMPONENT: Remote Active Medications// \<Enter\> RDIM

SUMMARY ORDER: 1195// \<Enter\> 1195

HEADER NAME: \<Enter\>

Please hold on while I resequence the summary order.............................

................................................................................

\>\>\> Returning to Create/Modify Health Summary Component Option.

  
Example: Remote Allergy/ADR Data

Select COMPONENT: Remote Allergy/ADR Data

Are you adding 'Remote Allergy/ADR Data' as

a new HEALTH SUMMARY COMPONENT? No// y (Yes)

HEALTH SUMMARY COMPONENT NUMBER: *578042*//

HEALTH SUMMARY COMPONENT ABBREVIATION: RART

Do you wish to duplicate an existing COMPONENT? YES// n NO

NAME: Remote Allergy/ADR Data Replace

PRINT ROUTINE: ENHS;PSOQRART

ABBREVIATION: RART

DESCRIPTION:

No existing text

Edit? NO// YES

==\[ WRAP \]==\[ INSERT \]=============\< DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

This component displays remote allergy and adverse data information using the Remote Data Interoperability features of the Health Data Repository. Data is shown from other stations only and not the local station.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: \<Enter\>

Select SELECTION FILE: \<Enter\>

ADD new Component to the AD HOC Health Summary? NO// YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes//

Do you wish to review the Summary Type structure before continuing? NO//

Select COMPONENT: Remote Allergy/ADR Data//               

SUMMARY ORDER: 1710// \<Enter\> 1710 

HEADER NAME:

Please hold on while I resequence the summary order.............................

................................................................................\>*\>\>*

Returning to Create/Modify Health Summary Component Option.

## Creating the TIU Data Object

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must be a member of the Clinical Coordinator user class and must have DUZ(0)=”@” to perform this procedure.

To use Remote Allergy/ADR Data as a TIU object, create a TIU Health Summary object. Please refer to the TIU Technical Manual at <http://www.va.gov/vdl/application.asp?appid=65> for details.

*Note: The OBJECT METHOD must be named accordingly for the TIU data object and cannot vary. It is our recommendation that the NAME field listed here be named accordingly when creating the TIU data object.*Remote Active Medications

- NAME: Remote Active Medications
- OBJECT METHOD:

S X=\$\$RDI^PSOQ0595(DFN,"^TMP(\$J,""PSOQRDI"")")

Follow this example to create your TIU data object.

Select TIU Maintenance Menu Option: 2 Document Definitions (Manager)

Select Document Definitions (Manager) Option: 4 Create Objects

START DISPLAY WITH OBJECT: FIRST// .............................................

Select Action: Next Screen// CREATE Create

Enter the Name of a new Object: REMOTE ACTIVE MEDICATIONS

CLASS OWNER: CLINICAL COORDINATOR Replace @

PERSONAL OWNER: USER\<Enter\> RMS 11INF PHARMACIST

Entry added

Objects Feb 12, 2008@12:35:04 Page: 82 of 105

Objects

\+ Status

1140 REMOTE ACTIVE MEDICATIONS I

1141 RENAL IMAGING HS A

1142 RENAL LABS A

1143 RENAL LABS HS A

1144 RENAL-UA A

1145 RENIN A

1146 RESEARCH STUDY HISTORY A

1147 RESPIRATION A

1148 RETIC A

1149 RETICULOCYTE COUNT A

1150 RETICULOCYTE-AC A

1151 RHEUMATOID FACTOR A

1152 RHEUMATOID FACTOR, QUANT A

1153 ROOMBED A

\+ ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\>

Change View Try Quit

Create Owner

-------------------------------------------------example continues--------------------------------------------------

Select Action: Next Screen// DET Detailed Display/Edit

Select Entry: (1140-1153): 1140

Select Action: Quit// TECH Technical Fields

OBJECT METHOD: S X=\$\$RDI^PSOQ0595(DFN,"^TMP(\$J,""PSOQRDI"")")

Select Action: Next Screen// BAS Basics

NAME: REMOTE ACTIVE MEDICATIONS \<Enter\> Replace

ABBREVIATION: \<Enter\>

PRINT NAME: REMOTE ACTIVE MEDICATIONS \<Enter\> Replace

PERSONAL OWNER: USER// \<Enter\> USER

STATUS: (A/I): INACTIVE// A ACTIVE Entry Activated.

Select Action: Next Screen// QUIT Quit ......................................

Select Action: Next Screen// QUIT Quit

Select Document Definitions (Manager) Option:

After completing the implementation of Tool \#4, the following is an example of what you see from any TIU document that uses the created object.

![](pso-7-294-implementation-guide-medication-reconciliation-tools/006.png)

<span id="_Toc196278162" class="anchor"></span>Transition Guidance

(Class III to Class I)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product, Medication Reconciliation, represents the first class III to class I conversion. The software is a product initially developed at the Hines VA Hospital. The product utilizes Health Summary components and Text Integrated Utility (TIU) data objects to compile a list of current medications. Medication Reconciliation also leverages the Remote Data Interoperability (RDI) software to include medication data from other sites.

This document is intended to assist sites already using the class III version of the software so they will have a smooth transition to the released class I version. There are no intended functionality changes being added to the class I version. The sites that are already using the class III version of the software need to be aware that previously defined local names may vary, as the documentation is an example to follow.

This Transition Guidance section refers to steps needed to set up components for Medication Reconciliation using routines introduced by patches PSO\*7\*294 and TIU\*1\*238. Please ensure that the patches have been installed prior to proceeding with these steps.

Upon completion of the steps listed in this Transition Guidance section, users will be able to continue using the Medication Reconciliation tools that have previously been available within CPRS. The Health Summaries and TIU data objects will be using the class I routines to gather the patient information.

# Step 1: Removing the PHARMACY SYSTEM File Parameter 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During initial testing of the class I patch, a system parameter was introduced to control the ability for Medication Reconciliation software to access data from the Health Data Repository (HDR). That parameter is no longer necessary, and the data dictionary field can be removed from the PHARMACY SYSTEM file (#59.7) if it is present at your station.

From programmer mode, execute the following command.

S DIK="^DD(59.7,",DA=578100,DA(1)=59.7 D ^DIK

# Step 2: Disabling the Menu Option that set the Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the parameter has been removed in step 1, the option that was used to set it will no longer operate, but it is generally considered appropriate to mark the option as “Out-of-Order.” These steps show you how to perform that task.

Select OPTION NAME: EDIT OPTIONS XUEDITOPT Edit options

Select OPTION to edit: AJEY RDI USE IN MED REC

Enable/Disable RDI in Medication Reconciliation

NAME: AJEY RDI USE IN MED REC Replace \<Enter\>

MENU TEXT: Enable/Disable RDI in Medication Reconciliation

Replace \<Enter\>

PACKAGE: \<Enter\>

OUT OF ORDER MESSAGE: Parameter removed before PSO\*7\*294

LOCK: ^

# # Step 3: Redirecting the Health Summary Components and TIU Data Objects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This step redirects the Health Summary components and TIU data objects to class I released routines.

There are 4 sets of tools released with the Medication Reconciliation software. Each contains components and/or objects you need to redirect. The following sections step you through redirecting each.

## Redirecting the Medication Reconciliation Health Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Tool \#1 is the Medication Reconciliation Health Summary, which uses two Health Summary components. After the components have been redirected, rename the Health Summary type.

### Redirecting the Health Summary Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To locate the components, use the *Create/Modify Health Summary Components* \[GMTS IRM/ADPAC COMP EDIT\] option. An alternative method for finding the components is to perform a FileMan search of the HEALTH SUMMARY COMPONENT file (#142.1) for entries where the PRINT ROUTINE contains AJEY. For this tool, you are looking for the print routine(s) named AJEYUAP and/or AJEYUAP2.

*Note: The PRINT ROUTINE must be named accordingly for the Health Summary component and cannot vary. It is our recommendation that the other fields listed here be named accordingly when redirecting the Health Summary component.*Medication Reconciliation

- COMPONENT: Medication Reconciliation
- PRINT ROUTINE: EN;PSOQUAP2
- ABBREVIATION: MRP
- DESCRIPTION: This component provides an alphabetized list of the patient's medications from several sources, including outpatient prescriptions, unit dose medications, non-VA documented medications, and active remote medications using the Remote Data Interoperability interface to the Health Data Repository.

Once located, change the name, print routine, abbreviation, and description as shown in this example.

Select OPTION NAME: GMTS IRM/ADPAC COMP EDIT

Create/Modify Health Summary Components

Select COMPONENT: MED RECONCILIATION W/ REMOTE MRP2

NAME: MED RECONCILIATION W/ REMOTE Replace ... With Medication Reconciliation

Replace

Medication Reconciliation \<Enter\>

PRINT ROUTINE: EN;AJEYUAP2// EN;PSOQUAP2

ABBREVIATION: MRP2// MRP

DESCRIPTION:

Edit? NO// YES

-------------------------------------------------example continues--------------------------------------------------

==\[ WRAP \]==\[ INSERT \]===========\< DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

This component provides an alphabetized list of the patient's medicationsfrom several sources, including outpatient prescriptions, unit dosemedications, non-VA documented medications and active remote medicationsusing the Remote Data Interoperability interface to the Health DataRepository.

\<=======T=======T=======T======T=======T=======T=======T=======T=======T\>======

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: \<Enter\>

Select SELECTION FILE: \<Enter\>

ADD new Component to the AD HOC Health Summary? NO// YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: no// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Select COMPONENT: Medication Reconciliation// \<Enter\> MRP

Medication Reconciliation is already a component of this summary.

Select one of the following:

E Edit component parameters

D Delete component from summary

Select Action:

Please hold on while I resequence the summary order.................................................................................................................................................................

\>\>\> Returning to Create/Modify Health Summary Component Option.

Press RETURN to continue...

### Renaming the Health Summary Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Summary type is the combination of Health Summary components that can be made available through CPRS on the Reports tab. Follow the provided steps to rename the Health Summary type.

Select OPTION NAME: GMTS TYPE ENTER/EDIT

Create/Modify Health Summary Type

Select Health Summary Type: Med Reconciliation Profile+ Med Reconciliation Profile+

Med Reconciliation Profile+ (Med Reconciliation + Remote)

OK? YES// \<Enter\>

-------------------------------------------------example continues--------------------------------------------------

NAME: Med Reconciliation Profile+ Replace ... With Medication Reconciliation

Replace

Medication Reconciliation \<Enter\>

TITLE: Med Reconciliation + Remote Replace ... With Medication Reconciliation

Replace

Medication Reconciliation \<Enter\>

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// \<Enter\>

SUPPRESS SENSITIVE PRINT DATA: NO SSN NO SSN

LOCK: \<Enter\>

OWNER: USER// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// YES

HEALTH SUMMARY TYPE INQUIRY

Type Name: Medication Reconciliation

Title: Medication Reconciliation

Owner: USER

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes

SUPPRESS SENSITIVE PRINT DATA: NO SSN

Max Hos ICD Pro CPT

Abb Ord Component Name Occ Time Loc Text Nar Mod Selection

------------------------------------------------------------------------------

BADR 5 Brief Adv React/All

RART 10 Remote Allergy/ADR D

MRP 15 Medication Reconcili

\* = Disabled Components

Select COMPONENT:

## Redirecting the Medication Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Tool \#2 is the Medication Worksheet of outpatient prescriptions suitable for giving to the patient as they leave the hospital from an inpatient stay or a clinic visit. After redirecting the Health Summary component, rename the Health Summary type.

### Redirecting the Health Summary Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To locate the component, use the *Create/Modify Health Summary Components* \[GMTS IRM/ADPAC COMP EDIT\] option. An alternative method for finding the component is to perform a FileMan search of the HEALTH SUMMARY COMPONENT file (#142.1) for entries where the PRINT ROUTINE contains AJEY. For this tool, you are looking for a component with the print routine containing either AJEY0086 or AJEY0186.

*Note: The PRINT ROUTINE must be named accordingly for the Health Summary component and cannot vary. It is our recommendation that the other fields listed here be named accordingly when redirecting the Health Summary component.*Medication Worksheet

- COMPONENT: Medication Worksheet
- PRINT ROUTINE: TASK2;PSOQ0186
- ABBREVIATION: MWS
- DESCRIPTION: This component displays a list of the patient's active and pending outpatient prescriptions in a patient-friendly worksheet format with space intended for written notes by the patient, provider, or caregiver.

Once located, change the name, print routine, abbreviation, and description as shown in this example.

Select OPTION NAME: GMTS IRM/ADPAC COMP EDIT

Create/Modify Health Summary Components

Select COMPONENT: Med-Chart/Calendar/PMI MCAL

NAME: Med-Chart/Calendar/PMI Replace ... With Medication Worksheet

Replace

Medication Worksheet \<Enter\>

PRINT ROUTINE: TASK2;AJEY0186// TASK2;PSOQ0186

ABBREVIATION: MCAL// MWS

DESCRIPTION:

Edit? NO// YES

==\[ WRAP \]==\[ INSERT \]===========\< DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

This component displays a list of the patient's active and pendingoutpatient prescriptions in a patient-friendly worksheet format withspace intended for written notes by the patient, provider, or caregiver.

\<=======T=======T=======T======T=======T=======T=======T=======T=======T\>======

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: \<Enter\>

Select SELECTION FILE: \<Enter\>

ADD new Component to the AD HOC Health Summary? NO// YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: no// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Select COMPONENT: Medication Worksheet// \<Enter\> MWS

Medication Worksheet is already a component of this summary.

Select one of the following:

E Edit component parameters

D Delete component from summary

Select Action:

Please hold on while I resequence the summary order.................................................................................................................................................................

\>\>\> Returning to Create/Modify Health Summary Component Option.

Press RETURN to continue...

### Renaming the Health Summary Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Summary type is the combination of Health Summary components that can be made available through CPRS on the Reports tab. To rename the Health Summary type, you must perform a series of steps twice, as demonstrated below.

Renaming Health Summary Type: Part 1

Select OPTION NAME: GMTS TYPE ENTER/EDIT

Create/Modify Health Summary Type

Select Health Summary Type: Med-Chart

Med-Chart of Active RX'S

OK? YES// \<Enter\> Med-Chart of Active Rx's

> **WARNING:** You are about to edit a Health Summary Type that is being used

by a Health Summary Object. Changing the structure of this Health Summary

Type will alter how the Object will display.

Do want to continue? NO// y YES

NAME: Med-Chart of Active Rx's Replace ... With Medication Worksheet

Replace

Medication Worksheet \<Enter\>

TITLE: Medication Worksheet

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// \<Enter\>

SUPPRESS SENSITIVE PRINT DATA: NO SSN NO SSN

LOCK: \<Enter\>

OWNER: USER// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// y YES

HEALTH SUMMARY TYPE INQUIRY

Type Name:

Title:

Owner:

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA:

SUPPRESS SENSITIVE PRINT DATA: NO SSN

Max Hos ICD Pro CPT

Abb Ord Component Name Occ Time Loc Text Nar Mod Selection

------------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

\* = Disabled Components

Select COMPONENT:

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Please hold on while I resequence the summary order.

  
Renaming Health Summary Type: Part 2

Select OPTION NAME: GMTS TYPE ENTER/EDIT

Create/Modify Health Summary Type

Select Health Summary Type: Medication Worksheet

> **WARNING:** You are about to edit a Health Summary Type that is being used

by a Health Summary Object. Changing the structure of this Health Summary

Type will alter how the Object will display.

Do want to continue? NO// y YES

NAME: Medication Worksheet Replace \<Enter\>

TITLE: Medication Worksheet Replace \<Enter\>

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// \<Enter\>

SUPPRESS SENSITIVE PRINT DATA: NO SSN NO SSN

LOCK: \<Enter\>

OWNER: USER// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// y YES

HEALTH SUMMARY TYPE INQUIRY

Type Name: Medication Worksheet

Title: Medication Worksheet

Owner: USER

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes

SUPPRESS SENSITIVE PRINT DATA: NO SSN

Max Hos ICD Pro CPT

Abb Ord Component Name Occ Time Loc Text Nar Mod Selection

------------------------------------------------------------------------------

MWS 5 Medication Worksheet

\* = Disabled Components

Select COMPONENT:

Select Health Summary Type:

No Health Summary Type selected

## Redirecting the Active/Pending/Expired Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Tool \#3 is the TIU data object alternative for a list of medications to be given to the patient. After redirecting the TIU data object(s), redirect the Health Summary component.

### Redirecting the TIU Data Object(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Note:You must be the owner of the object to complete this procedure. If you are NOT the owner of this object or in the owner class for this object, before making changes, change yourself to be the owner of the object. There are three options on how to accomplish this: (1) add yourself to the owner class (2) remove the owner class and add yourself as the personal owner (3) replace the name of the personal owner with your name.*

To locate and edit this object, use the *Sort Document Definitions* \[TIUFA SORT DDEFS MGR\] option. Alternatively, you can search the TIU DOCUMENT DEFINITION file (#8925.1) for an entry where the object method contains the routine name TIULMED.

*Note: The OBJECT METHODS must be named accordingly for each TIU data object and cannot vary. It is our recommendation that the other fields listed here be named accordingly when redirecting the TIU data objects.*Active/Pending/Expired Medications

- NAME: Active/Pending/Expired Medications
- OBJECT METHOD:

S TIUDATE=30 S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",,,3) K TIUDATE

> *Note: In the OBJECT METHOD, you can change the TIUDATE field value of 30 to any value between 1 and 180.*Active/Pending/Expired Medications (W/O Supplies)

- NAME: Active/Pending/Expired Medications (W/O Supplies)
- OBJECT METHOD:

S TIUDATE=30 S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",,,3,,,0) K TIUDATE

> *Note: In the OBJECT METHOD, you can change the TIUDATE field value of 30 to any value between 1 and 180.*

Once located, change the name and object method as shown in this example.

Example:Active/Pending/Expired Medications

Select OPTION NAME: TIUFA SORT DDEFS MGR Sort Document Definitions

Sort Document Definitions

Select Attribute: (T/O/S/U/P/A): Owner// TYPE Type

Select TYPE: (CL/DC/TL/CO/O/N): OBJECT

START WITH DOCUMENT DEFINITION: FIRST// ACTIVE

GO TO DOCUMENT DEFINITION: LAST// ACTIVEZ....................

Sort by TYPE Jan 29, 2008@13:53:55 Page: 1 of 1

Entries of Type OBJECT from ACTIVE to ACTIVEZ

Name Type

1 ACTIVE INP MEDS O

2 ACTIVE MEDICATIONS O

3 ACTIVE MEDS COMBINED O

4 ACTIVE MEDS COMBINED W/O SUPPLIES O

5 ACTIVE MEDS COMBINED W/O SUPPLIES \[INCL. NON-VA\] O

6 ACTIVE MEDS COMBINED \[INCL. NON-VA\] O

7 ACTIVE MEDS O/P O

8 ACTIVE PROBLEMS O

9 ACTIVE/PENDING/EXPIRED MEDICATIONS O

10 ACTIVE/PENDING/EXPIRED MEDICATIONS (W/O SUPPLIES) O

?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\>

Select Action: Quit// DET Detailed Display/Edit

Select Entry: (1-10): 9

-------------------------------------------------example continues--------------------------------------------------

Detailed Display Jan 29, 2008@13:54:09 Page: 1 of 1

Object ACTIVE/PENDING/EXPIRED MEDICATIONS

Basics

Name: ACTIVE/PENDING/EXPIRED MEDICATIONS

VHA Enterprise

Standard Title:

Abbreviation:

Print Name:

Type: OBJECT

IFN: 3286

National

Standard: NO

Status: ACTIVE

Owner: CLINICAL COORDINATOR

Technical Fields

Object Method: S X=\$\$LIST^AJEY0495(DFN,"^TMP(""TIUMED"",\$J)",,,3)

? Help +, - Next, Previous Screen PS/PL

Basics Try Delete

Technical Fields Find Quit

Select Action: Quit// BAS Basics

Edit Owner and Status only; Entry not Inactive

CLASS OWNER: CLINICAL COORDINATOR Replace \<Enter\>

STATUS: (A/I): ACTIVE// I INACTIVE Inactivated

Detailed Display Jan 29, 2008@13:54:14 Page: 1 of 1

Object ACTIVE/PENDING/EXPIRED MEDICATIONS

Basics

Name: ACTIVE/PENDING/EXPIRED MEDICATIONS

VHA Enterprise

Standard Title:

Abbreviation:

Print Name:

Type: OBJECT

IFN: 3286

National

Standard: NO

Status: INACTIVE

Owner: CLINICAL COORDINATOR

Technical Fields

Object Method: S X=\$\$LIST^AJEY0495(DFN,"^TMP(""TIUMED"",\$J)",,,3)

? Help +, - Next, Previous Screen PS/PL

Basics Try Delete

Technical Fields Find Quit

Select Action: Quit// TECH Technical Fields

OBJECT METHOD: S X=\$\$LIST^AJEY0495(DFN,"^TMP(""TIUMED"",\$J)",,,3)

Replace ... With S TIUDATE=30 S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",,,3) K TIUDATE

Replace

S TIUDATE=30 S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",,,3) K TIUDATE

-------------------------------------------------example continues--------------------------------------------------

Select Action: Next Screen// BAS Basics

NAME: ACTIVE/PENDING/EXPIRED MEDICATIONS Replace \<Enter\>

ABBREVIATION: \<Enter\>

PRINT NAME: \<Enter\>

CLASS OWNER: CLINICAL COORDINATOR Replace \<Enter\>

STATUS: (A/I): INACTIVE// A ACTIVE Entry Activated.

Select Action: Next Screen// QUIT Quit ....................

Select Action: Quit// QUIT QUIT

This object method activates the properties unique to the Medication Reconciliation software by the presence of the TIUDATE variable. Set that number (shown here as ‘30’ to the number of days back to include expired medications).

You can also exclude supply items from the list by creating an object using the following method.

S TIUDATE=30 S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",,,3,,,0) K TIUDATE

### Redirecting the Health Summary Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To locate the components, use the *Create/Modify Health Summary Components* \[GMTS IRM/ADPAC COMP EDIT\] option. An alternative method for finding the components is to perform a FileMan search of the HEALTH SUMMARY COMPONENT file (#142.1) for entries where the PRINT ROUTINE contains AJEY. For this tool, you are looking for the print routine named AJEY0236.

*Note: The PRINT ROUTINE must be named accordingly for the Health Summary component and cannot vary. It is our recommendation that the other fields listed here be named accordingly when redirecting the Health Summary component.*Active/Pending/Expired Meds

- COMPONENT: Active/Pending/Expired Meds
- PRINT ROUTINE: RPT;PSOQ0236
- ABBREVIATION: PSO2
- DESCRIPTION: This component provides a Health Summary equivalent to the new TIU object for ACTIVE/PENDING/EXPIRED MEDICATIONS. There are several parameters with the basic object available that have not been tested with this Health Summary component. It is hard-coded for up to 180 days of expired prescriptions to be included and includes supply items by design.

Once located, change the name, print routine, abbreviation, and description as shown in this example.

Select Health Summary Maintenance Menu Option: 2 Create/Modify Health Summary Components

Select COMPONENT: AJEY RECENT RX LISTING PSO2

NAME: AJEY RECENT RX LISTING Replace ... With ACTIVE/PENDING/EXPIRED MEDS

Replace \<Enter\>

ACTIVE/PENDING/EXPIRED MEDS

-------------------------------------------------example continues--------------------------------------------------

PRINT ROUTINE: RPT;AJEY0236// RPT;PSOQ0236

ABBREVIATION: PSO2// \<Enter\>

DESCRIPTION:

This component provides a Health Summary equivalent to the new TIU object for ACTIVE/PENDING/EXPIRED MEDICATIONS. There are several parameters availablewith the basic object that have not been tested with this Health Summary component. It is hard-coded for up to 180 days of expired prescriptions to be included and includes supply items by design.

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: Recent Rx Profile// \<Enter\>

Select SELECTION FILE: \<Enter\>

ADD new Component to the AD HOC Health Summary? NO// YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: no// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Select COMPONENT: ACTIVE/PENDING/EXPIRED MEDS// \<Enter\> PSO2

ACTIVE/PENDING/EXPIRED MEDS is already a component of this summary.

Select one of the following:

E Edit component parameters

D Delete component from summary

Select Action: \<Enter\>

Please hold on while I resequence the summary order.............................

................................................................................

..........................................................

\>\>\> Returning to Create/Modify Health Summary Component Option.

Press RETURN to continue...

## Redirecting Remote Active Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Tool \#4 is the set of Health Summary components for active remote medications and remote allergy/adverse reaction data. After redirecting the TIU data object, redirect the Health Summary components.

### Redirecting the TIU Data Object

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Note:You must be the owner of the object to complete this procedure. If you are NOT the owner of this object or in the owner class for this object, before making changes, change yourself to be the owner of the object. There are three options on how to accomplish this: (1) add yourself to the owner class (2) remove the owner class and add yourself as the personal owner (3) replace the name of the personal owner with your name.*

To locate and edit this object, use the *Sort Document Definitions* \[TIUFA SORT DDEFS MGR\] option. Alternatively, you can search the TIU DOCUMENT DEFINITION file (#8925.1) for an entry where the object method contains the routine name PSOQ0595.

*Note: The OBJECT METHOD must be named accordingly for the TIU data object and cannot vary. It is our recommendation that the NAME field listed here be named accordingly when redirecting the TIU data object.*Remote Active Medications

- NAME: Remote Active Medications
- OBJECT METHOD:

S X=\$\$RDI^PSOQ0595(DFN,"^TMP(\$J,""PSOQRDI"")")

Once located, change the name and object method as shown in this example.

TIUFA SORT DDEFS MGR Sort Document Definitions

Sort Document Definitions

Select Attribute: (T/O/S/U/P/A): Owner// TYP Type

Select TYPE: (CL/DC/TL/CO/O/N): OB OBJECT

START WITH DOCUMENT DEFINITION: FIRST// REMOTE

GO TO DOCUMENT DEFINITION: LAST// REMOTEZ..

Sort by TYPE Feb 21, 2008@14:04:53 Page: 1 of 1

Entries of Type OBJECT from REMOTE to REMOTEZ

Name Type

1 REMOTE ACTIVE MEDICATIONS O

2 REMOTE ALLERGY/ADR O

?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\>

Change View... Detailed Display/Edit Delete

Create (Status...) Copy

Select Action: Quit// DET Detailed Display/Edit

Select Entry: (1-2): 1

Detailed Display Feb 21, 2008@14:05 Page: 1 of 1

Object REMOTE ACTIVE MEDICATIONS

Basics

Name: REMOTE ACTIVE MEDICATIONS

VHA Enterprise

Standard Title:

Abbreviation:

Print Name: REMOTE ACTIVE MEDICATIONS

Type: OBJECT

IFN: 3327

National

Standard: NO

Status: ACTIVE

Owner: USER

Technical Fields

Object Method: S X=\$\$RDI^AJEY0595(DFN,"^TMP(\$J,""AJEYRDI"")")

? Help +, - Next, Previous Screen PS/PL

Basics Try Delete

Technical Fields Find Quit

-------------------------------------------------example continues--------------------------------------------------

Select Action: Quit// BAS Basics

Edit Owner and Status only; Entry not Inactive

PERSONAL OWNER: USER// \<Enter\> USER

STATUS: (A/I): ACTIVE// I INACTIVE Inactivated

Select Action: Quit// TECH Technical Fields

OBJECT METHOD: S X=\$\$RDI^AJEY0595(DFN,"^TMP(\$J,""AJEYRDI"")")

Replace AJEY With PSOQ Replace AJEY With PSOQ

Replace \<Enter\>

S X=\$\$RDI^PSOQ0595(DFN,"^TMP(\$J,""PSOQRDI"")")

Select Action: Quit// BAS Basics

NAME: REMOTE ACTIVE MEDICATIONS \<Enter\> Replace

ABBREVIATION: \<Enter\>

PRINT NAME: REMOTE ACTIVE MEDICATIONS Replace \<Enter\>

PERSONAL OWNER: USER// \<Enter\> USER

STATUS: (A/I): INACTIVE// A ACTIVE Entry Activated.

Select Action: Quit// QUIT Quit ..

Select Action: Quit// QUIT QUIT

### Redirecting the Health Summary Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To locate the components, use the *Create/Modify Health Summary Components* \[GMTS IRM/ADPAC COMP EDIT\] option. An alternative method for finding the components is to perform a FileMan search of the HEALTH SUMMARY COMPONENT file (#142.1) for entries where the PRINT ROUTINE contains AJEY. The original class III components were pointed to routines named AJEYRART for the allergies and AJEY0595 for the medications.

*Note: The PRINT ROUTINES must be named accordingly for each Health Summary component and cannot vary. It is our recommendation that the other fields listed here be named accordingly when redirecting the Health Summary components.*Remote Allergy/ADR Data

- COMPONENT: Remote Allergy/ADR Data
- PRINT ROUTINE: ENHS;PSOQRART
- ABBREVIATION: RART
- DESCRIPTION: This component displays remote allergy and adverse data information using the Remote Data Interoperability features of the Health Data Repository. Data is only shown from other stations, not the local station.

Remote Active Medications

- COMPONENT: Remote Active Medications
- PRINT ROUTINE: ENHS;PSOQ0595
- ABBREVIATION: RDIM
- DESCRIPTION: This component will display the details of a patient's remote active outpatient medications using data from the Health Data Repository.

Once located, change the names, print routines, abbreviations, and descriptions as shown in these examples.

  
Example: Remote Allergy/ADR DataGMTS IRM/ADPAC COMP EDIT Create/Modify Health Summary Components

Create/Modify Health Summary Components

Select COMPONENT: Remote Allergy/ADR Data

NAME: Remote Allergy/ADR Data Replace \<Enter\>

PRINT ROUTINE: ENHS;AJEYRART// ENHS;PSOQRART

ABBREVIATION: RARI// RART

DESCRIPTION:

No existing text

Edit? NO// y YES

==\[ WRAP \]==\[ INSERT \]==========\< DESCRIPTION \>========\[ \<PF1\>H=Help \]====

This component displays remote allergy and adverse data information using the Remote Data Interoperability features of the Health Data Repository. Data is only shown from other stations, not the local station.

\<=======T=======T=======T=======T=======T=======T=======T=======T\>======

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: \<Enter\>

Select SELECTION FILE: \<Enter\>

ADD new Component to the AD HOC Health Summary? NO// y YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Select COMPONENT: Remote Allergy/ADR Data// \<Enter\> RART

SUMMARY ORDER: 1185// \<Enter\> 1185

HEADER NAME: \<Enter\>

Please hold on while I resequence the summary order...............................................................................................................................................

\>\>\> Returning to Create/Modify Health Summary Component Option.

Example: Remote Active MedicationsGMTS IRM/ADPAC COMP EDIT Create/Modify Health Summary Components

Create/Modify Health Summary Components

Select COMPONENT: Remote Active Medications HDRM

NAME: Remote Active Medications Replace \<Enter\>

PRINT ROUTINE: ENHS;AJEY0595// ENHS;PSOQ0595

ABBREVIATION: HDRM// RDIM

DESCRIPTION:

No existing text

Edit? NO// y YES

==\[ WRAP \]==\[ INSERT \]==========\< DESCRIPTION \>========\[ \<PF1\>H=Help \]====

This component will display the details of a patient's remote activeoutpatient medications using data from the Health Data Repository. \<=======T=======T=======T=======T=======T=======T=======T=======T\>======

-------------------------------------------------example continues--------------------------------------------------

TIME LIMITS APPLICABLE: \<Enter\>

MAXIMUM OCCURRENCES APPLICABLE: \<Enter\>

HOSPITAL LOCATION APPLICABLE: \<Enter\>

ICD TEXT APPLICABLE: \<Enter\>

PROVIDER NARRATIVE APPLICABLE: \<Enter\>

LOCK: \<Enter\>

DEFAULT HEADER NAME: \<Enter\>

Select SELECTION FILE: \<Enter\>

ADD new Component to the AD HOC Health Summary? NO// y YES

\>\>\> EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// \<Enter\>

Do you wish to review the Summary Type structure before continuing? NO// \<Enter\>

Select COMPONENT: Remote Active Medications// \<Enter\> RDIM

SUMMARY ORDER: 1195// \<Enter\> 1195

HEADER NAME: \<Enter\>

Please hold on while I resequence the summary order...............................................................................................................................................

\>\>\> Returning to Create/Modify Health Summary Component Option.