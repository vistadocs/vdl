---
consolidated_title: "pharmacy data management technical manual/security guide"
app_code: PSS
doc_type: TM
master_source: "Pharmacy Data Management Version 1 Technical Manual/Security Guide (PSS*1*262)"
master_pub_date: June 2012
consolidated_from: 2 versions
prior_versions:
  - "Pharmacy Data Management Version 1 Technical Manual/Security Guide (updated PSS*1*252)"
---

# Pharmacy Data Management Technical Manual/Security Guide

<!-- image -->

June 2012

(Revised August 2025)


Office of Information and Technology

Revision History

| Date    | Revised Pages                     | Patch Number         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------|-----------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 08/2025 | 2, 5, 6, 13, 16, 31, 43, 47, 48   | PSS*1*262            | - Updated File List - Updated File Description with PSS*1*262 File Descriptions - Updated Menu Options added Check Drug Interaction and Check Pharmacogenomic Interaction - Updated Option Description Example - Updated XPAR Parameters section with PSS* 1*262.  - Added new routines, PSS262PO, PSS262PR PSSHDPG1,PSSP254A, PSSP254R, PSSP254U - PSSP254V, PSSPGX, PSSPGX1, PSSPGX2, PSSPGXOR, PSSPGXP2, PSSPGXPR , PSSPGXT1 - PSSPGXTS, PSSPGXU2, and PSSPGXUT to Routine List - Updated Standards and Convention Committee (SACC) Exemptions - Updated Table 7: PDM Files - Updated New Functionality - Updated Modified and New Routines for PSS*1*262 |
| 03/2024 | 1, 11, 15                         | PSS*1.0*259          | Added “Exclude Start/Stop override for ONE-TIME schedules” to the Option Descriptions and Menu/Options sections, and PSSEXLST to the Routines section  Fixed table accessibility issues, especially tables 4 and 5, and the Revision History table. Changed the Styles so that the document would conform to 508-accessibility standards.                                                                                                                                                                                                                                                                                                                    |
| 09/2022 | 4, 7                              | PSS*1.0*187          | Updated section 2.1.1 with list of new fields. Added Indication Usage Report to the Menu/Options section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 01/2022 | 15                                | PSS*1.0*252          | Added routine PSSNDCUT2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 07/2021 | i, 4, 10, 13                      | PSS*1.0*247          | - Replaced menu option, Manage Buprenorphine Tx of Pain Dosage Forms [PSS BUPRENORPHINE DOSAGE FORMS] with new option ‘Manage Buprenorphine Tx of Pain - VA Products’ [PSS BUPRENORPHINE VAPRODS]. - Added new XPAR Parameters section.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 08/2020 | Title, i,  5, 10, 11, 13, Footers | PSS*1.0*245          | - Added PSS MED INST MED ROUTE REPORT option for Medication Instruction Management - Added PSS MED INST MED ROUTE REPORT option for Medication Routes Management - Added the item PSS MED INST MED ROUTE REPORT - Added the item PSS MED INST MED ROUTE REPORT - Added routine - Updated Title page, Revision History, and Footers  REDACTED                                                                                                                                                                                                                                                                                                                 |
| 11/2018 | 3                                 | PSS*1.0*215          | Added Section 2.1.1  *Data Dictionary Changes*  to include information about the RX# UPPER BOUND WARNING LIMIT field (#48) added to the PHARMACY SYSTEM file (#59.7), and the CLINICAL ALERT multiple field (#109) added to the PHARMACY PATIENT file (#55).  REDACTED                                                                                                                                                                                                                                                                                                                                                                                       |
| 08/2018 | 12-13, 30                         | PSS*1.0*227          | Added XPAR Parameters section.  Added new routines PSSDEEA, PSSP227, and PSSPRICE to Routines List.  Added entry for PSS DEE AUDIT mail group.  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 8/2018  | 4, 9                              | PSS*1*219            | Added new menu option under the ‘Dosages’ menu [PSS DOSAGES MANAGEMENT[  Added new option ‘Manage Buprenorphine Tx of Pain Dosage Forms’ [PSS BUPRENORHINE DOSAGE FORMS].  Added missing options to item multiple under the ‘Dosages’ menu option [PSS DOSAGES MANAGEMENT].  REDACTED                                                                                                                                                                                                                                                                                                                                                                        |
| 06/2018 | 12-13                             | PSS*1*224            | Updated Routine List - adding new routines PSSDSEXF and PSS224PI  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 03/2018 | 2, 11                             | PSS*1.0*211          | Updated File List to include file #50.60699  Updated Routine List with PSSNDSU and PSS211PO  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 02/2018 | 12-13                             | PSS*1*178            | Updated Routine List  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 05/2017 | 2, 12, 34                         | PSS*1*201            | Updated File List  Updated Routine List  Added new routine PSSOAS  Updated File Security  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 10/2016 | 12  34-37                         | PSS*1*193            | Added new routine PSSHLDFS to the Routines section.  Added Appendix A for Pharmacy Interface Automation.  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 4/2016  | i-ii,  11-12, 22-23               | PSS*1*175            | Add 2 new Routines: PSSCKOS &amp; PSSDIUTX, Updated Additional Information section  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 3/2016  | i-ii,  11-12                      | PSS*1*191            | Updated Revision History  Added new routines to routine list:  PSS1P191, PSSHRHAI, PSSMRRDG, PSSMRRI  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 3/2014  | All  i - iii, 2, 7-13, 33, 37     | PSS*1*172            | Renumbered all pages.  Updated Revision History and Table of Contents.  Updated the Glossary section by putting definitions in a table format.  New menu, options, file and routines added.  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 9/2013  | i - iii, 3, 7 – 13a, 30, 34 - 35  | PSS*1*160            | Updated Revision History  Updated Table of Contents with Exported Options and Routines sections  Added Lookup Dosing Check Info for Drug [PSS DRUG DOSING LOOKUP] OPTION to the Dosages [PSS DOSAGES MANAGEMENT] MENU OPTION and Drug Names with Trailing Spaces Report  [PSS TRAILING SPACES REPORT].  Added PSS DOSING ORDER CHECKS option  Also added the following routines to the routine list:  PSS160EN  PSS160PO  PSSDRDOS  PSSFDBDI  PSSDSONF  Added Web Servers, Web Services, and Cache Class section  Added text to the Security Keys section  REDACTED                                                                                          |
| 01/2013 | i-iv, 3, 6-6b, 7, 10 - 13         | PSS*1*164  PSS*1*169 | Removed reference to patch PSS*1*146 in the menu options section  Added Print Interface Data File option to the Pharmacy Data Management [PSS MGR] menu  Added Check Drug Interaction option to the Pharmacy Data Management [PSS MGR] menu  Moved Menu/Option items from page 7 to page 6a  Added Print Interface Data File option to the PEPS Services menu under the Option Descriptions section  Added Check Drug Interaction option to the Option Descriptions section  Added routine PSSDIUTL  Added Find Unmapped Local Possible Dosages option to the Stand Alone Options section  REDACTED                                                          |
| 06/2012 | All                               | PSS*1*146            | Reissued document. Removed redundancies due to MOCHA V.1.0 incremental release; updated formatting and page numeration.  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

Table of Contents

Introduction	1

File List		2

File Descriptions	3

Menu / Options	6

Option Descriptions	11

Orderable Items Option	15

XPAR Parameters	15

Routines	16

Exported Options	19

Protocols	19

Bulletins		20

Web Servers	20

Web Services	20

Cache Class	20

HL7 Messaging with an External System	20

Data Archiving and Purging	29

Callable Routines / Entry Points / Application Program Interfaces (APIs)	29

Medication Routes	29

Administration Scheduling	30

External Relations	30

Internal Relations	30

Package-Wide Variables	30

Package Requirements	30

Additional Information	31

Security Management	38

Mail Groups	39

Alerts		39

Bulletins		39

Remote Systems	40

Archiving / Purging	40

Interfacing	40

Electronic Signatures	40

Locked Menu Options	40

Security Keys	40

File Security	42

References	44

Appendix A: Pharmacy Interface Automation	45

New Functionality	46

Options and Build Components	47

Modified and New Routines	48

Glossary	49

List of Tables

Table 1: HL7 Drug Message Segment Definition Table	20

Table 2: Segments Used in the Master File Update Message	24

Table 3: Package Requirements	30

Table 4: Waiver: OITIMB33554520 - Migration from M2J to VistA Web Services Client 	30

Table 5: Supporting Documentation for the Waiver	31

Table 6: Security Keys	39

Table 7: PDM FIles	41

Table 8: Non-PDM Files	42

Table 9: VistA Software	44

Table 10: Glossary	48

### Introduction

Pharmacy Data Management (PDM) provides tools for managing Pharmacy data. It includes tools for creating Pharmacy Orderable Items and maintaining files necessary for the Computer Patient Record System (CPRS). PDM consolidates tools for managing the various Pharmacy software products. It provides Pharmacy Supervisors, in one location, the capability to enter and edit data from the local DRUG file (#50) for all Pharmacy related packages.

The PDM Technical Manual is designed to acquaint the user with the various PDM options and offer specific guidance on the maintenance and use of the PDM package. Documentation concerning the PDM package, including any subsequent change pages affecting this documentation, can be found at the VistA Documentation Library (VDL) on the Veterans Administration Intranet.

Notations that will be used consistently throughout this PDM Technical Manual are outlined below.

Menu options will be italicized. **Example** : The *Drug Enter/Edit* option permits you to enter or edit a drug.

Screen prompts will be denoted with quotation marks around them. **Example** : the "SELECT DRUG" prompt will display next.

Responses in bold face indicate user input. **Example** : DRUG GENERIC NAME: **ACETA**

Text centered between bent parentheses represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field.

**&lt;Enter&gt;** indicates that the Enter key (or Return key on some keyboards) must be pressed.

**Example** : Type **Y** for Yes or **N** for No and press **&lt;Enter&gt;**

**&lt;Tab&gt;** indicates that the Tab key must be pressed.

**Example** :  Press **&lt;Tab&gt;** to move the cursor to the next field.

<!-- image -->

Indicates especially important or helpful information.

<!-- image -->

Options are locked with a particular security key.  The user must hold the particular security key to be able to perform the menu option.

<!-- image -->

**Example** :  Without the PSXCOMPMGR key, the Consolidated Mail Outpatient Pharmacy options cannot be accessed.

**?** , **??** , **???** One, two, or three question marks can be entered at any of the prompts for online help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions, and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

^ Up arrow (caret or a circumflex) and pressing **&lt;Enter&gt;** can be used to exit the present option.

#### File List

The following PDM files are exported with the PDM package.

**File#       NAME          	UPDATE 	DATA COMES    USER**

**DD	WITH FILE   OVERRIDE**

50          DRUG 	FULL	NO

50.4        DRUG ELECTROLYTES 	FULL	NO

50.606      DOSAGE FORM                  	FULL	YES (MERGE)	NO

50.60699    MASTER DOSAGE FORM	FULL	NO

50.7        PHARMACY ORDERABLE ITEM 	FULL	NO

51          MEDICATION INSTRUCTION        	FULL	NO

51.1        ADMINISTRATION SCHEDULE      	FULL	YES (MERGE)	YES

51.2        MEDICATION ROUTES           	FULL	YES (MERGE)	YES

51.23       STANDARD MEDICATION ROUTES          FULL	YES	NO

(OVERWRITE)

51.24       DOSE UNITS	FULL	YES	NO

(OVERWRITE)

51.25       DOSE UNIT CONVERSION	FULL	YES	NO

(OVERWRITE)

51.26       PHARMACOGENOMIC GENES		        FULL			YES	      YES

51.28       PHARMACOGENOMIC PHENOTYPES          FULL               YES         YES

51.29       PHARMACOGENOMIC EMAIL LOG	FULL	YES	NO

(OVERWRITE)

51.5        ORDER UNIT 	FULL	NO

51.7        DRUG TEXT	FULL	YES	YES

(OVERWRITE)

52.6        IV ADDITIVES 	FULL	NO

52.7        IV SOLUTIONS 	FULL	NO

53.47       INFUSION INSTRUCTIONS	FULL	NO

**File#       NAME          	UPDATE 	DATA COMES    USER**

**DD	WITH FILE   OVERRIDE**

54          RX CONSULT 	FULL (SCREEN)	NO

55          PHARMACY PATIENT (Partial DD)	PARTIAL	NO

59.7        PHARMACY SYSTEM 	FULL	NO

59.73        VENDOR DISABLE/ENABLE	FULL	NO

59.74        VENDOR INTERFACE DATA 	FULL	NO

The following non-PDM files are exported with the PDM package.

**File#	NAME	UPDATE 	DATA COMES    USER**

**DD	WITH FILE   OVERRIDE**

200	NEW PERSON (Partial DD)	PARTIAL	NO

9009032.3	APSP INTERVENTION TYPE	FULL	YES		NO

(OVERWRITE)

9009032.4	APSP INTERVENTION 	FULL	NO

9009032.5	APSP INTERVENTION RECOMMENDATION 	FULL	YES	NO

(OVERWRITE)

#### File Descriptions

This package requires the files listed below. Information about the files can be obtained by using the VA FileMan to generate a list of file attributes.

The Data Dictionaries (DDs) are considered part of the online documentation for this software application. Use the VA FileMan *List File Attributes* [DILIST] option *,* under the *Data Dictionary Utilities* [DI DDU] option, to view/print the DDs.

#### Data Dictionary Changes

Patch PSS*1.0*215 adds the RX# UPPER BOUND WARNING LIMIT field (#48) to the PHARMACY SYSTEM file (#59.7). The value stored in this field determines when an early warning message is sent to members of a new PHARMACY SUPERVISORS MailMan group.

This patch is a companion patch to PSO*7.0*452, which implements an early warning message to notify mail group recipients that one or more Outpatient Pharmacy sites are approaching the upper limit of the defined prescription numbering series. If  no custom value is entered in this field, then the message will be sent when 1000 numbers remain in the series, and again each time the associated background job runs and less than 1000 numbers remain in the series. Refer to the *Outpatient Pharmacy (PSO) Manager’s User Guide* for more information about the early warning functionality that uses this new field.

Patch PSS*1.0*215 also adds a CLINICAL ALERT multiple field (#109) to the PHARMACY PATIENT file (#55). This field stores the date and time of the Clinical Alert and provides a free-text field for the alert text, which is displayed when using certain Outpatient Pharmacy [PSO] options. Pharmacy Supervisors can use Clinical Alerts to make Pharmacy staff aware of information such as drug interactions or the patient’s participation in clinical trials. Refer to the *Outpatient Pharmacy (PSO) Manager’s User Guide* for more information about the Clinical Alert functionality that uses this new field.

<!-- image -->

**Note:** The Clinical Alert Enter/Edit [PSO CLINICAL ALERT ENTER/EDIT] option in the Outpatient Pharmacy package is used to add, modify, or delete Clinical Alerts.

Patch PSS*1*247 adds a new parameter, the PHARMACY OPERATING MODE field (#102) in the PHARMACY SYSTEM file (#59.7). This field may be set to "VAMC", for traditional VA Medical Center pharmacy mode, or "MBM", for Meds By Mail pharmacy mode. Only the Meds By Mail Pharmacy should set this parameter to “MBM”. If this parameter is left empty, it will default to “VAMC”.  Functionality is being released in patch PSO*7.0*630 that uses this parameter to help determine whether or not a provider's DEA related information may be edited at the facility. (see the PSO*7.0*630 patch description for more details).

Patch PSS*1.0*187 adds the following fields

- COPY INDICATION TO SIG (#96) to PHARMACY SYSTEM file (#59.7)

- INDICATION FOR USE (#141)  to PHARMACY PATIENT file (#55) UNIT DOSE subfile (#55.06)

- INDICATION FOR USE  (#156) to PHARMACY PATIENT file (#55) IV subfile (#55.01)

- INDICATION FOR USE  (#15) to PHARMACY PATIENT file (#55) NON-VA MEDS subfile (#55.05)

- SIG (#16) subfile (#55.516) to NON-VA MEDS subfile (#55.05) with the following fields
    - SIG (#.01)
    - SCHEDULE(#1)
    - DURATION(#2)
    - CONJUNCTION (#3)
    - DOSAGE(#4)

Patch PSS*1.0*187 modified the following fields

- INDICATIONS FOR USE subfile (#50.713) to PHARMACY ORDERABLE ITEMS file (#50.7) with the following field
    - INDICATIONS FOR USE (#.01) the length was modified from 30 to 40 characters

- OTHER LANGUAGE INDICATIONS subfile (#50.714) to PHARMACY ORDERABLE ITEMS file (#50.7) with the following field

- OTHER LANGUAGE INDICATIONS (#.01) the length was modified from 30 to 40 characters

Patch PSS*1.0*262 adds the following files:

- PHARMACOGENOMIC GENES (#51.26) – the file stores a list of standard genes used for Pharmacogenomic Order Checks.  The standard gene name will be mapped to the First Databank gene.
- PHARMACOGENOMIC PHENOTYPES (#51.28)- the file stores a list of standard phenotypes used for Pharmacogenomic Order Checks. The standard phenotype name will be mapped to the First Databank phenotype.
- PHARMACOGENOMIC EMAIL LOG (#51.29) - the file contains the log for whenever the VHA PBM CDS PGX Outlook email group is alerted about an HDR-retrieved gene or phenotype that cannot be mapped to the First Databank gene database. The file includes the patient’s Integrated Control Number (ICN) originating package for the order, unresolved term, the related genetic information, and the facility where the discrepancy was detected. If an order is entered or processed for a specific patient with the same unresolved gene or unresolved or null phenotype greater than 7 days from the last email log, the system will send notification to the VHA PBM CDS PGX Outlook email group again and new log will be added for that patient. The entries in this file will not be purged.

- VA PHARMACOGENOMICS URL field (#103) to PHARMACY SYSTEM file (#59.7) – the field is a free-text field with a character limit of 1 to 100 characters. The data in this new field will be referenced in the last line of every PGx order check displayed in the PSS CHECK PGX INTERACTION option.

Patch PSS*1.0*262 adds the following intervention types to the APSP INTERVENTION TYPE file (# 9009032.3):

- PHARMACOGENOMIC HIGH ORDER CHECK
- PHARMACOGENOMIC MEDIUM ORDER CHECK

Patch PSS*1*262 moved the Check Drug Interaction [PSS CHECK DRUG INTERACTION] option under the Order Check Management [PSS ORDER CHECK MANAGEMENT] and added the Check Pharmacogenomic Interaction [PSS CHECK PGX INTERACTION]

## Menu / Options

The PDM options listed below show the PSSw MGR Menu structure.

*Pharmacy Data Management* [PSS MGR] menu:

<!-- image -->

CMOP Mark/Unmark (Single drug)

[PSSXX MARK]

*Dosages…*

[PSS DOSAGES MANAGEMENT]

*Dosage Form File Enter/Edit*

[PSS DOSAGE FORM EDIT]

*Enter/Edit Dosages*

[PSS EDIT DOSAGES]

Most Common Dosages Report

[PSS COMMON DOSAGES]

Noun/Dosage Form Report

[PSS DOSE FORM/ NOUN REPORT]

Review Dosages Report

[PSS DOSAGE REVIEW REPORT]

Local Possible Dosages Report

[PSS LOCAL POSSIBLE DOSAGES]

Request Change to Dose Unit

[PSS DOSE UNIT REQUEST]

*Lookup Dosing Check Info for Drug*

[PSS DRUG DOSING LOOKUP]

*Drug Names with Trailing Spaces Report*

[PSS TRAILING SPACES REPORT]

*Manage Buprenorphine Tx of Pain - VA Products*

**[PSS BUPRENORPHINE VAPRODS]**

*Drug Enter/Edit*

[PSS DRUG ENTER/ EDIT]

*Order Check Management…*

[PSS ORDER CHECK MANAGEMENT]

*Check Drug Interaction*

[PSS CHECK DRUG INTERACTION]

*Check Pharmacogenomic Interaction*

[PSS CHECK PGX INTERACTION]

*Request Changes to Enhanced Order Check Database*

[PSS ORDER CHECK CHANGES]

*Report of Locally Entered Interactions*

*[PSS REPORT LOCAL INTERACTIONS]*

*Electrolyte File (IV)*

[PSSJI ELECTROLYTE FILE]

*Lookup into Dispense Drug File*

[PSS LOOK]

*Medication Instruction Management...*

[PSS MED INSTRUCTION MANAGEMENT]

*Medication Instruction File Add/Edit*

[PSSJU MI]

*Medication Instruction File Report*

[PSS MED INSTRUCTION REPORT]

*Med Instruction Med Term Route Report*

[PSS MED INST MED ROUTE REPORT]

*Medication Routes Management...*

[PSS MEDICATION ROUTES MGMT]

*Medication Route File Enter/Edit*

[PSS MEDICATION ROUTES EDIT]

*Medication Route Mapping Report*

[PSS MED ROUTE MAPPING REPORT]

*Medication Route Mapping History Report*

[PSS MED ROUTE MAPPING CHANGES]

*Med Instruction Med Term Route Report*

[PSS MED INST MED ROUTE REPORT]

*Request Change to Standard Medication Route*

[PSS MEDICATION ROUTE REQUEST]

*Default Med Route for OI Report*

[PSS DEF MED ROUTE OI RPT]

*Orderable Item Management…*

[PSS ORDERABLE ITEM MANAGEMENT]

*Edit Orderable Items*

[PSS EDIT ORDERABLE ITEMS]

*Dispense Drug/Orderable Item Maintenance*

[PSS MAINTAIN ORDERABLE ITEMS]

*Orderable Item/Dosages Report*

[PSS ORDERABLE ITEM DOSAGES]

*Patient Instructions Report*

[PSS INSTRUCTIONS/ ITEMS REPORT]

*Orderable Item Report*

[PSS ORDERABLE ITEM REPORT]

*Orderable Items that Require Removal Report*

[PSS MRR ORDERABLE ITEMS RPT]

*Orderable Items for High Risk\High Alert*

[PSS HR/HA ORDERABLE ITEMS RPT]

*Indication Usage Report* [PSS INDICATION USAGE REPORT]

*Formulary Information Report*

[PSSNFI]

*Drug Text Management...*

[PSS DRUG TEXT MANAGEMENT]

*Drug Text Enter/Edit*

[PSS EDIT TEXT]

*Drug Text File Report*

[PSS DRUG TEXT FILE REPORT]

*Pharmacy System Parameters Edit*

[PSS SYS EDIT]

*Standard Schedule Management...*

[PSS SCHEDULE MANAGEMENT]

*Standard Schedule Edit*

[PSS SCHEDULE EDIT]

*Administration Schedule File Report*

[PSS SCHEDULE REPORT]

*Exclude Start/Stop override for ONE-TIME schedules*

[PSS EXCLUDE 1TIME STRSTP MODS]

*Synonym Enter/Edit*

[PSS SYNONYM EDIT]

*Controlled Substances/PKI Reports…*

[PSS CS/PKI REPORTS]

*DEA Spec Hdlg &amp; CS Fed Sch Discrepancy*

[PSS DEA VS CS FED. SCH. DISCR.]

*Controlled Substances Not Matched to NDF*

[PSS CS NOT MATCHED TO NDF]

*CS (DRUGS) Inconsistent with DEA Spec Hdlg*

[PSS CS DRUGS INCON WITH DEA]

*CS (Ord. Item) Inconsistent with DEA Spec Hdlg*

[PSS CS (OI) INCON WITH DEA]

*Send Entire Drug File to External Interface*

[PSS MASTER FILE ALL]

*IV Additive/Solution …*

[PSS ADDITIVE/SOLUTION]

*IV Additive Report*

[PSS IV ADDITIVE REPORT]

*IV Solution Report*

[PSS IV SOLUTION REPORT]

*Mark PreMix Solutions*

[PSS MARK PREMIX SOLUTIONS]

*Warning Builder*

[PSS WARNING BUILDER]

*Warning Mapping*

[PSS WARNING MAPPING]

*PEPS Services…*

[PSS PEPS SERVICES]

*Check Vendor Database Link*

[PSS CHECK VENDOR DATABASE LINK]

*Check PEPS Services Setup*

[PSS CHECK PEPS SERVICES SETUP]

*Schedule/Reschedule Check PEPS Interface*

[PSS SCHEDULE PEPS INTERFACE CK]

*Print Interface Data File*

[PSS VENDOR INTERFACE REPORT]

*Inpatient Drug Management…*

[PSS INP MGR]

*ADditives File*

[PSSJI DRUG]

*Dispense Drug Fields*

[PSSJU DRG]

*Dispense Drug/ATC Set Up*

[PSSJU DRUG/ATC SET UP]

*Edit Cost Data*

[PSSJU DCC]

*EDit Drug Cost (IV)*

[PSSJI EDIT DRUG COST]

*MARk/Unmark Dispense Drugs For Unit Dose*

[PSSJU MARK UD ITEMS]

*PRimary Solution File (IV)*

[PSSJI SOLN]

*Infusion Instruction Management …*

[PSS INFINS MGR]

*Infusion Instructions Add/Edit*

[PSS INFINS ADED]

*Infusion Instruction Report*

[PSS INFINS RPT]

*Orders for MRRs With Removal Properties*

[PSS MRR ORDERS DIAGNOSTIC RPT]

<!-- image -->

Locked: PSXCMOPMGR

Without the PSXCMOPMGR key, =the *CMOP Mark/Unmark (Single drug)=* option will not appear on your menu.

### Option Descriptions

The option descriptions below were retrieved from VA FileMan and provide the PDM options following the initial installation of the PDM package.

PSS MGR Pharmacy Data Management

This menu contains the options necessary to build and maintain the PHARMACY ORDERABLE ITEM file (#50.7), and to also build and maintain the Med. Route/Instructions table.

ITEM: PSS DRUG ENTER/EDIT

ITEM: PSS LOOK

ITEM: PSSJI ELECTROLYTE FILE

ITEM: PSSXX MARK

ITEM: PSS SYS EDIT

ITEM: PSS ORDERABLE ITEM MANAGEMENT

ITEM: PSSNFI

ITEM: PSS SYNONYM EDIT

ITEM: PSS DOSAGES MANAGEMENT

ITEM: PSS CS/PKI REPORTS

ITEM: PSS MASTER FILE ALL

ITEM: PSS MEDICATION ROUTES MGMT

ITEM: PSS SCHEDULE MANAGEMENT

ITEM: PSS DRUG TEXT MANAGEMENT

ITEM: PSS MED INSTRUCTION MANAGEMENT

ITEM: PSS ORDER CHECK MANAGEMENT

ITEM: PSS ADDITIVE/SOLUTION

ITEM: PSS WARNING BUILDER

ITEM: PSS WARNING MAPPING

ITEM: PSS PEPS SERVICES

ITEM: PSS INP MGR

ITEM: PSS INFINS MGR

ITEM: PSS MRR ORDERS DIAGNOSTIC RPT

-----------------------------------------------------------------------------

PSS DRUG ENTER/EDIT
Drug Enter/Edit

This option allows the user to edit fields for ALL pharmacy packages if they possess the proper package key. It also will allow the user to match to NDF and Orderable Item.

TYPE: run routine   ROUTINE: PSSDEE

-----------------------------------------------------------------------------

PSS LOOK

Lookup into Dispense Drug File

This option provides a report of all information regarding the dispense drug.

TYPE: run routine   ROUTINE: PSSLOOK

-----------------------------------------------------------------------------

PSSJI ELECTROYLYTE FILE
Electrolyte File (IV)

This option will allow you to alter the contents of the DRUG ELECTORYLYTES file (#50.4). This is the file that is pointed to by the ELECTROLYTE field in both the IV ADDITIVES (#52.6) and IV SOLUTIONS (#52.7) files.

TYPE: run routine   ROUTINE: ELECTRO^PSSIVDRG

-----------------------------------------------------------------------------

PSSXX MARK

CMOP Mark/Unmark (Single drug)

This option allows the user to mark/unmark a single drug for transmission to the CMOP.

TYPE: run routine   ROUTINE: PSSMARK

-----------------------------------------------------------------------------

PSS SYS EDIT

Pharmacy System Parameters Edit

This option allows the user to edit the Pharmacy System parameters used in Pharmacy Data Management.

TYPE: run routine   ROUTINE: PSSYSP

-----------------------------------------------------------------------------

PSS ORDERABLE ITEM MANAGEMENT

Orderable Item Management

This is the sub-menu driver for Orderable Item maintenance.

ITEM: PSS MAINTAIN ORDERABLE ITEMS

ITEM: PSS EDIT ORDERABLE ITEMS

ITEM: PSS ORDERABLE ITEM DOSAGES

ITEM: PSS INSTRUCTIONS/ITEMS REPORT

ITEM: PSS ORDERABLE ITEM REPORT

TYPE: menu

-----------------------------------------------------------------------------

PSSNFI

Formulary Information Report

This option provides a listing of pertinent pharmacy formulary information.

TYPE: run routine   ROUTINE: PSSNFI

-----------------------------------------------------------------------------

PSS SYNONYM EDIT

Synonym Enter/Edit

The option provides easy access to update the synonym information for an entry in the local DRUG file.

TYPE: run routine   ROUTINE: PSSSEE

-----------------------------------------------------------------------------

PSS DOSAGES MANAGEMENT

Dosages

This menu option contains options that control the editing of dosages.

ITEM: PSS DOSAGE FORM EDIT

ITEM: PSS EDIT DOSAGES

ITEM: PSS COMMON DOSAGES

ITEM: PSS DOSE FORM/NOUN REPORT

ITEM: PSS DOSAGE REVIEW REPORT

ITEM: PSS LOCAL POSSIBLE DOSAGES

ITEM: PSS DOSE UNIT REQUEST

ITEM: PSS DRUG DOSING LOOKUP

ITEM: PSS TRAILING SPACES REPORT

ITEM: PSS BUPRENORPHINE VAPRODS

TYPE: menu

-----------------------------------------------------------------------------

PSS CS/PKI REPORTS

Controlled Substances/PKI Reports

PKI POST-INSTALL REPORTS PROVIDED AS OPTIONS.

ITEM: PSS DEA VS CS FED. SCH. DISCR.

ITEM: PSS CS NOT MATCHED TO NDF

ITEM: PSS CS DRUGS INCON WITH DEA

ITEM: PSS CS (OI) INCON WITH DEA

TYPE: menu

-----------------------------------------------------------------------------

PSS MASTER FILE ALL

Send Entire Drug File to External Interface

TYPE: run routine   ROUTINE: PSSMSTR

-----------------------------------------------------------------------------

PSS MEDICATION ROUTES MGMT

Medication Routes Management

This Sub-Menu contains options related to Medication Routes in both the MEDICATION ROUTES (#51.2) File and the STANDARD MEDICATION ROUTES (#51.23) File.

ITEM: PSS MEDICATION ROUTES EDIT

ITEM: PSS MED ROUTE MAPPING REPORT

ITEM: PSS MED ROUTE MAPPING CHANGES

ITEM: PSS MED INST MED ROUTE REPORT

ITEM: PSS MEDICATION ROUTE REQUEST

ITEM: PSS DEF MED ROUTE OI RPT

TYPE: menu

-----------------------------------------------------------------------------

PSS SCHEDULE MANAGEMENT

Standard Schedule Management

This Sub-Menu contains options needed for Schedule maintenance.

ITEM: PSS SCHEDULE EDIT

ITEM: PSS SCHEDULE REPORT
ITEM: PSS EXCLUDE 1TIME STRSTP MODS

TYPE: menu

-----------------------------------------------------------------------------

PSS DRUG TEXT MANAGEMENT

Drug Text Management

This Sub-Menu contains options concerning Drug Text.

ITEM: PSS EDIT TEXT

ITEM: PSS DRUG TEXT FILE REPORT

TYPE: menu

-----------------------------------------------------------------------------

PSS MED INSTRUCTION MANAGEMENT

Medication Instruction Management

The Sub-Menu contains options related to the MEDICATION INSTRUCTION (#51) File.

ITEM: PSSJU MI

ITEM: PSS MED INSTRUCTION REPORT

ITEM: PSS MED INST MED ROUTE REPORT

TYPE: menu

-----------------------------------------------------------------------------

PSS ORDER CHECK MANAGEMENT

Order Check Management

This is the sub-menu for functionality related to managing medication order checks.

ITEM: PSS CHECK DRUG INTERACTION

ITEM: PSS CHECK PGX INTERACTION

ITEM: PSS CHECK PGX INTERACTION

ITEM: PSS REPORT LOCAL INTERACTIONS

TYPE: menu

-----------------------------------------------------------------------------

PSS ADDITIVE/SOLUTION

IV Additive/Solution

This Sub-Menu contains options that can be used to run reports from the IV ADDITIVES (#52.6) File and the IV SOLUTIONS (#52.7) File. It also provides an option to edit the PREMIX (#18) Field in the IV SOLUTIONS (#52.7) File.

ITEM: PSS IV ADDITIVE REPORT

ITEM: PSS IV SOLUTION REPORT

ITEM: PSS MARK PREMIX SOLUTIONS

TYPE: menu

-----------------------------------------------------------------------------

PSS WARNING BUILDER

Warning Builder

This option will allow you to define a custom warning label list containing entries from both the new warning label source and the old Rx Consult file entries.

TYPE: run routine   ROUTINE: PSSWRNB

-----------------------------------------------------------------------------

PSS WARNING MAPPING

Warning Mapping

This option is used to match an entry from the old Rx Consult file to the new commercial data source warning file to aid in using the Warning Builder (to identify local warnings that do not have an equivalent entry in the new commercial data source). The user can also enter a Spanish translation for an Rx Consult file entry, if desired, but whenever possible, the new commercial data source's warnings (English or Spanish depending on the patient setting) should be used.

TYPE: run routine   ROUTINE: EDIT^PSSWMAP

-----------------------------------------------------------------------------

PSS PEPS SERVICES

PEPS

ITEM: PSS CHECK VENDOR DATABASE LINK

ITEM: PSS CHECK PEPS SERVICES SETUP

ITEM: PSS SCHEDULE PEPS INTERFACE CK

ITEM: PSS VENDOR INTERFACE REPORT

TYPE: menu

-----------------------------------------------------------------------------

PSS INP MGR

Inpatient Drug Management

This Sub-Menu contains options related to INPATIENT DRUG MANAGEMENT.

ITEM: PSSJI DRUG

ITEM: PSSJU DRG

ITEM: PSSJU DRUG/ATC SET UP

ITEM: PSSJU DCC

ITEM: PSSJI EDIT DRUG COST

ITEM: PSSJU MARK UD ITEMS

ITEM: PSSJI SOLN

TYPE: Menu

-----------------------------------------------------------------------------

TYPE: run routine ROUTINE: PSSDIUTL

PSS INFINS MGR

Infusion Instruction Management

Menu containing options related to the INFUSION INSTRUCTIONS (#53.47) file.

TYPE: menu

PSS INFINS ADED

Infusion Instructions Add/Edit

Allows users to enter and edit abbreviations and expansions in the INFUSION INSTRUCTIONS (#53.47) file.

TYPE: run routine  ROUTINE: ENII^PSSFILED

PSS INFINS RPT

Infusion Instructions Report

Provides a report of entries from the INFUSION INSTRUCTIONS(#53.47) file

TYPE: run routine ROUTINE: EN^PSSIIRPT

-----------------------------------------------------------------------------

PSS MRR ORDERS DIAGNOSTIC RPT

Orders for MRRs With Removal Properties

#### Orderable Items Option

This option enables you to determine which active orders contain Orderable Items that have the new "Prompt for Removal in BCMA" flag value set to 1, 2, or 3 that need to be discontinued and entered as New (not copied, edited or renewed) AFTER the installation of Pharmacy Inpatient.

Medications PSJ*5.0*315. Failure to re-create these orders could result in confusing information to display on the BCMA VDL if displayed alongside newer MRR orders that do have the updated removal information.

TYPE: run routine ROUTINE: EN^PSSMRRDG

#### XPAR Parameters

Patch PSS*1*227 adds XPAR parameter PSS DRUG AUDIT RETENTION MOS to the PARAMETER DEFINITION file (#8989.51). See the *Pharmacy Data Management Manager’s User Manual* for information on how this parameter is used. To set the parameter, follow the steps below. You must be a VistA programmer, Pharmacy Informaticist, Clinical Application Coordinator (CAC), or other user with access to the General Parameter Tools [XPAR MENU TOOLS] option in VistA.

Log in to VistA.

At the "Select OPTION NAME:" prompt, type **XPAR MENU TOOLS** and press **&lt;Enter&gt;** .

At the "Select General Parameter Tools Option:" prompt, type **EP** and press **&lt;Enter&gt;** .

At the "Select PARAMETER DEFINITION NAME:" prompt, type **PSS DRUG AUDIT RETENTION MOS** and then press **&lt;Enter&gt;** .

At the "Drug Audit Retention MOS:" prompt, type the number of retention months and press **&lt;Enter&gt;** .

Patch PSS*1*247 replaces the existing parameter, PSS BUPRENORPHINE PAIN DFS, with a new XPAR parameter PSS BUPRENORPHINE PAIN VAPRODS to the PARAMETER DEFINITION file (#8989.51). To set the parameter, follow the steps below. You must be a VistA programmer, Pharmacy Informaticist, Clinical Application Coordinator (CAC), or other user with access to the General Parameter Tools [XPAR MENU TOOLS] option in VistA.

1. Log in to VistA.
2. At the "Select OPTION NAME:" prompt, type **XPAR MENU TOOLS** and press **&lt;Enter&gt;** .
3. At the "Select General Parameter Tools Option:" prompt, type **EP** and press **&lt;Enter&gt;** .
4. At the "Select PARAMETER DEFINITION NAME:" prompt, type **PSS BUPRENORPHINE PAIN VAPRODS** and press **&lt;Enter&gt;** .
5. At the "Select Sequence:" prompt, type the sequence number and press **&lt;Enter&gt;** .

Patch PSS*1*247 automatically populated these products in XPAR “PSS BUPRENORPHINE PAIN VAPRODS” at the Package level during installation:

BUPRENORPHINE 10MCG/HR PATCH

BUPRENORPHINE 15MCG/HR PATCH

BUPRENORPHINE 20MCG/HR PATCH

BUPRENORPHINE 5MCG/HR PATCH

BUPRENORPHINE 7.5MCG/HR PATCH

BUPRENORPHINE 150MCG FILM,BUCCAL

BUPRENORPHINE 300MCG FILM,BUCCAL

BUPRENORPHINE 450MCG FILM,BUCCAL

BUPRENORPHINE 600MCG FILM,BUCCAL

BUPRENORPHINE 750MCG FILM,BUCCAL

BUPRENORPHINE 75MCG FILM,BUCCAL

BUPRENORPHINE 900MCG FILM,BUCCA

#### Routines

The following routines are used by the Pharmacy Data Management package.

- PSS0052
- PSS0093
- PSS0114
- PSS102RP
- PSS117EN
- PSS117PO
- PSS127PI
- PSS127PT
- PSS129EN
- PSS147EN
- PSS147PO
- PSS160EN
- PSS160PO
- PSS164P
- PSS172PO
- PSS1P178
- PSS1P201
- PSS1P23
- PSS1P43
- PSS208P
- PSS211PO
- PSS219PO
- PSS262PO
- PSS262PR
- PSS32P3
- PSS32P5
- PSS50
- PSS50A
- PSS50A1
- PSS50AQM
- PSS50ATC
- PSS50B
- PSS50B1
- PSS50B2
- PSS50C
- PSS50C1
- PSS50CMP
- PSS50D
- PSS50DAT
- PSS50DOS
- PSS50E
- PSS50F
- PSS50F1
- PSS50LAB
- PSS50NDF
- PSS50P4
- PSS50P66
- PSS50P7
- PSS50P7A
- PSS50TMP
- PSS50WS
- PSS51
- PSS51P1
- PSS51P15
- PSS51P1A
- PSS51P1B
- PSS51P1C
- PSS51P2
- PSS51P5
- PSS52P6
- PSS52P6A
- PSS52P6B
- PSS52P7
- PSS52P7A
- PSS54
- PSS55
- PSS551
- PSS55MIS
- PSS59P7
- PSS70UTL
- PSS781
- PSS90PI
- PSSADDIT
- PSSADRPT
- PSSAUTL
- PSSBPSUT
- PSSCHENV
- PSSCKOS
- PSSCLDRG
- PSSCLINR
- PSSCLOZ
- PSSCMOPE
- PSSCOMMN
- PSSCPRS
- PSSCPRS1
- PSSCREAT
- PSSCSPD
- PSSCUSRQ
- PSSDACS
- PSSDAWUT
- PSSDDUT
- PSSDDUT2
- PSSDDUT3
- PSSDEE
- PSSDEE1
- PSSDEE2
- PSSDEEA
- PSSDELOI
- PSSDENT
- PSSDFEE
- PSSDGUPD
- PSSDI
- PSSDIN
- PSSDINT
- PSSDIUTL
- PSSDIUTX
- PSSDOS
- PSSDOSED
- PSSDOSER
- PSSDOSLZ
- PSSDOSRP
- PSSDRDO2
- PSSDRDOS
- PSSDRINT
- PSSDSAPA
- PSSDSAPD
- PSSDSAPI
- PSSDSAPK
- PSSDSAPL
- PSSDSAPM
- PSSDSBBP
- PSSDSBDA
- PSSDSBDB
- PSSDSBPA
- PSSDSBPB
- PSSDSBPC
- PSSDSBPD
- PSSDSDAT
- PSSDSEXC
- PSSDSEXD
- PSSDSEXE
- PSSDSEXF
- PSSDSFDB
- PSSDSONF
- PSSDSPON
- PSSDSPOP
- PSSDSUTA
- PSSDSUTL
- PSSDTR
- PSSDVEN
- PSSEC119
- PSSEC123
- PSSENV
- PSSENVN
- PSSEXLST
- PSSFDBDI
- PSSFDBRT
- PSSFIL
- PSSFILED
- PSSFILES
- PSSGENM
- PSSGIU
- PSSGMI
- PSSGS0
- PSSGSGUI
- PSSGSH
- PSSHDPG1
- PSSHELP
- PSSHFREQ
- PSSHL1
- PSSHLDFS
- PSSHLSCH
- PSSHLU
- PSSHRCOM
- PSSHRENV
- PSSHREQ
- PSSHRHAI
- PSSHRIT
- PSSHRPST
- PSSHRQ2
- PSSHRQ21
- PSSHRQ22
- PSSHRQ23
- PSSHRQ24
- PSSHRQ25
- PSSHRQ2D
- PSSHRQ2O
- PSSHRVAL
- PSSHRVL1
- PSSHTTP
- PSSHUIDG
- PSSIIRPT
- PSSINSTR
- PSSJEEU
- PSSJORDF
- PSSJSPU
- PSSJSPU0
- PSSJSV
- PSSJSV0
- PSSJXR
- PSSJXR1
- PSSJXR10
- PSSJXR11
- PSSJXR12
- PSSJXR13
- PSSJXR14
- PSSJXR15
- PSSJXR16
- PSSJXR17
- PSSJXR18
- PSSJXR19
- PSSJXR2
- PSSJXR20
- PSSJXR21
- PSSJXR22
- PSSJXR23
- PSSJXR24
- PSSJXR25
- PSSJXR26
- PSSJXR27
- PSSJXR28
- PSSJXR29
- PSSJXR3
- PSSJXR30
- PSSJXR31
- PSSJXR32
- PSSJXR33
- PSSJXR34
- PSSJXR35
- PSSJXR36
- PSSJXR37
- PSSJXR38
- PSSJXR39
- PSSJXR4
- PSSJXR40
- PSSJXR41
- PSSJXR42
- PSSJXR5
- PSSJXR6
- PSSJXR7
- PSSJXR8
- PSSJXR9
- PSSLAB
- PSSLDALL
- PSSLDEDT
- PSSLDOSE
- PSSLOCK
- PSSLOOK
- PSSMARK
- PSSMATCH
- PSSMEDCH
- PSSMEDRQ
- PSSMEDRT
- PSSMEDX
- PSSMIRPT
- PSSMONT
- PSSMRRDG
- PSSMRRI
- PSSMRTUP
- PSSMRTUX
- PSSMSTR
- PSSNCPDP
- PSSNDCUT
- PSSNDCUT2
- PSSNDSU
- PSSNFI
- PSSNFIP
- PSSNOD2
- PSSNOUNR
- PSSOAS
- PSSOICT
- PSSOICT1
- PSSOIDOS
- PSSOPKI
- PSSOPKI1
- PSSORPH
- PSSORPH1
- PSSORPHZ
- PSSORUTE
- PSSORUTL
- PSSORUTZ
- PSSOUTSC
- PSSP110
- PSSP130
- PSSP134
- PSSP170
- PSSP191A
- PSSP194
- PSSP254A
- PSSP254R
- PSSP254U
- PSSP254V
- PSSPGX
- PSSPGX1
- PSSPGX2
- PSSPGXOR
- PSSPGXP2
- PSSPGXPR
- PSSPGXT1
- PSSPGXTS
- PSSPGXU2
- PSSPGXUT
- PSSPI89
- PSSPKIPI
- PSSPKIPR
- PSSPNSRP
- PSSPO129
- PSSPOI
- PSSPOIC
- PSSPOID1
- PSSPOID2
- PSSPOID3
- PSSPOIDT
- PSSPOIKA
- PSSPOIM
- PSSPOIM1
- PSSPOIM2
- PSSPOIM3
- PSSPOIMN
- PSSPOIMO
- PSSPOIMP
- PSSPOST2
- PSSPOST5
- PSSPOST6
- PSSPRE38
- PSSPRETR
- PSSPRICE
- PSSPRMIX
- PSSPRUTL
- PSSQOC
- PSSQORD
- PSSREF
- PSSREMCH
- PSSRXACT
- PSSSCHED
- PSSSCHMS
- PSSSCHRP
- PSSSEE
- PSSSOLI1
- PSSSOLIT
- PSSSPD
- PSSSUTIL
- PSSSXRD
- PSSSYN
- PSSTRENG
- PSSTXT
- PSSUNMSI
- PSSUTIL
- PSSUTIL1
- PSSUTIL3
- PSSUTLA1
- PSSUTLA2
- PSSUTLAZ
- PSSUTLPR
- PSSUTLPZ
- PSSVIDRG
- PSSVX6
- PSSVX61
- PSSVX62
- PSSVX63
- PSSVX64
- PSSVX65
- PSSVX66
- PSSWMAP
- PSSWRNA
- PSSWRNB
- PSSWRNC
- PSSWRNE
- PSSXDIC
- PSSXRF1
- PSSYSP

#### Exported Options

#### Stand-Alone Options

The following is a list of all stand-alone options that are **NOT** exported as part of the main PDM menu [PSS MGR]:

*Other Language Translation Setup*

[PSS OTHER LANGUAGE SETUP]

*Drug Inquiry (IV)*

[PSSJI DRUG INQUIRY]

*Electrolyte File (IV)*

[PSSJI ELECTROLYTE FILE]

*Enable/Disable Vendor Database Link*

[PSS ENABLE/DISABLE DB LINK]

*Add Default Med Route*

[PSS ADD DEFAULT MED ROUTE]

*Find Unmapped Local Possible Dosages*

[PSS LOCAL DOSAGES EDIT ALL]

<!-- image -->

The *Enable/Disable Vendor Database Link* option exists **ONLY** as a way for technical personnel to turn on/off the database connection if required for debugging. Normally, it is enabled and the Vendor Database updates are performed centrally on the MOCHA Servers, not at the individual sites. It is **NOT** exported as part of the main PDM menu [PSS MGR].

In the rare case where this option is used and the database link is disabled, NO drug-drug interaction, duplicate therapy, or dosing order checks will be performed in Pharmacy or in the Computerized Patient Record System (CPRS).

#### Protocols

NAME: PSS EXT MFU CLIENT 
DESCRIPTION: This protocol will be used as the ACK from the external interface for an MFN\_M01 message.

NAME: PSS EXT MFU SERVER 
DESCRIPTION: This protocol will be used to send event notification and data when new drugs are added to the DRUG file (#50) and when certain fields are  updated in the same file. This information will be sent to the automated  dispensing machines through HL7 V.2.4 formatted messages.

NAME: PSS HUI DRUG UPDATE 
DESCRIPTION: This protocol will be used to send event notification and data when new drugs are added to the Drug file (#50) and when certain fields are  updated in same file.

NAME: PSS MED ROUTE RECEIVE
DESCRIPTION: This protocol processes updates to the Standard Medication Routes (#51.23) File.

#### Bulletins

NAME: PSS FDB INTERFACE

SUBJECT: ORDER CHECK DATABASE DOWN

RETENTION DAYS: 3

PRIORITY?: YES

NAME: PSS FDB INTERFACE RESTORED

SUBJECT: ORDER CHECK DATABASE IS BACK UP

RETENTION DAYS: 3

PRIORITY?: YES

#### Web Servers

PEPS

#### Web Services

DOSING\_INFO

DRUG\_INFO

ORDER\_CHECKS

#### Cache Class

XMLHandler

#### HL7 Messaging with an External System

A protocol, PSS HUI DRUG UPDATE, is exported and has been created to generate HL7 messages when new drugs are added to the DRUG file (#50) and existing entries are updated. This protocol is exported with the text “DELETE ONLY TO SEND DRUG UPDATE MESSAGES” in the DISABLE field (#2) of the PROTOCOL file (#101). To activate the sending of these HL7 messages, the text from the DISABLE field (#2) of the PROTOCOL file (#101) must be deleted and at least one receiving protocol added as a subscriber. The drug data elements included in the HL7 message are defined in the following HL7 Drug Message Segment Definition table.

#### HL7 Drug Message Segment Definition Table

When the PSS HUI DRUG UPDATE protocol is enabled, the following table defines the data elements sent in each segment of the HL7 drug message.

Table 1: HL7 Drug Message Segment Definition Table

| Segment     |   Piece | Field Name                    | HL7 TBL # or Data Type   | Description                                    |
|-------------|---------|-------------------------------|--------------------------|------------------------------------------------|
| **MSH**     |       1 | &#124;                        | ST                       | Field Separator                                |
|             |       2 | ^~\&                          | ST                       | Encoding Characters                            |
|             |       3 | Pharmacy                      | No suggested value       | Sending Application                            |
|             |       9 | MFN                           | 0076                     | Message Type                                   |
| **MFI**     |       1 | 50^DRUG^99PSD                 | 0175                     | Master File ID                                 |
|             |       3 | UPD                           | 0178                     | File-Level Event Code                          |
|             |       6 | NE                            | 0179                     | Response Level Code                            |
| **MFA**     |       1 | MUP/MAD                       | 0180                     | UPDATE/ADD                                     |
| **MFE**     |       1 | MUP/MAD                       | 0180                     | UPDATE/ADD                                     |
|             |       4 | IEN^DRUG NAME^99PSD           |                          | File 50 Entry                                  |
| **ZPA**     |       1 | NDC                           | ST                       | National Drug Code                             |
|             |       2 | LOCAL NON-FORMULARY           | CE                       | If “1” true                                    |
|             |       3 | INACTIVE DATE                 | DT                       | HL7 Format (YYYYMMDD)                          |
|             |       4 | APPLICATION PACKAGE USE       | ST                       | Used by what packages                          |
|             |       5 | MESSAGE                       | ST                       | Info on drug                                   |
|             |       6 | VA CLASSIFICATION             | ST                       | VA Class                                       |
|             |       7 | DEA SPECIAL HDLG              | ST                       | How drug is dispense based on DEA codes        |
|             |       8 | FSN                           | ST                       | Federal Stock #                                |
|             |       9 | WARNING LABEL                 | ST                       | Drug Warnings for patient                      |
|             |      10 | VISN NON-FORMULAR             | CE                       | If ‘1’ true                                    |
| **ZPB**     |       1 | PHARMACY ORDERABLE ITEM       | CE                       | IEN^OI tied to dispense drug^PSD50.7           |
|             |       2 | DOSAGE FORM                   | ST                       | IEN^Dosage Form associated with OI^PSD50.606   |
|             |       3 | MEDICATION ROUTE              | ST                       | IEN^Med Route associated with OI^PSD51.2       |
|             |       4 | PSNDF VA PRODUCT NAME ENTRY   | CE                       | IEN^VA PRODUCT NAMES^PSD50.68                  |
|             |       5 | DISPENSE UNIT                 | ST                       | Dispense Unit for a drug                       |
|             |       6 | CMOP DISPENSE                 | CE                       | 1 or 0                                         |
|             |       7 | OP EXTERNAL DISPENSE          | CE                       | 1 or 0                                         |
|             |       8 | EXPIRATION DATE               | DT                       | HL7 Format (YYYYMMDD)                          |
|             |       9 | LAB TEST MONITOR              | CE                       | IEN^Lab Test^LAB60                             |
| **ZPC**     |       1 | SPECIMEN TYPE                 | CE                       | IEN^ SPECIMEN TYPE^LAB61                       |
|             |       2 | MONITOR ROUTINE               | ST                       | Program that runs to find lab test and results |
|             |       3 | LAB MONITOR MARK              | CE                       | If ‘1’ true                                    |
|             |       4 | STRENGTH                      | NM                       | Dose of drug                                   |
|             |       5 | UNIT                          | CE                       | IEN^Unit of measure^PSD50.607                  |
|             |       6 | PRICE PER ORDER UNIT          | NM                       |                                                |
|             |       7 | PRICE PER DISPENSE UNIT       | NM                       |                                                |
| **[{ZPD}]** |       1 | SYNONYM                       | ST                       | Trade Name                                     |
|             |       2 | NDC CODE                      | ST                       | National Drug Code                             |
|             |       3 | INTENDED USE                  | CE                       | CE^INTENTED USE                                |
|             |       4 | VSN                           | ST                       | Vendor Stock Number                            |
|             |       5 | ORDER UNIT                    | CE                       | IEN^ABBREVIATION^EXPANSION  ^PSD51.5           |
|             |       6 | PRICE PER ORDER UNIT          | NM                       |                                                |
|             |       7 | DISPENSE UNITS PER ORDER UNIT | NM                       |                                                |
|             |       8 | PRICE PER DISPENSE UNIT       | NM                       |                                                |
|             |       9 | VENDOR                        | ST                       | Vendor                                         |
| **[{ZPE}]** |       1 | ACTIVITY LOG                  | DT                       | HL7 Format YYYYMMDDHHMM[SS]-ZZZZ               |
|             |       2 | REASON                        | CE                       | E^EDIT                                         |
|             |       3 | INITIATOR OF ACTIVITY         | CE                       | IEN^NEW PERSON^VA200                           |
|             |       4 | FIELD EDITED                  | ST                       |                                                |
|             |       5 | NEW VALUE                     | ST                       |                                                |
|             |       6 | NDF UPDATE                    | ST                       |                                                |
| **[{ZPF}]** |       1 | DISPENSE UNITS PER DOSE       | NM                       |                                                |
|             |       2 | DOSE                          | NM                       |                                                |
|             |       3 | PACKAGE                       | CE                       | CE^PACKAGE(S)                                  |
|             |       4 | BCMA UNITS PER DOSE           | NM                       |                                                |
| **[{ZPG}]** |       1 | CLOZAPINE LAB TEST            | CE                       | IEN^LAB TEST^LAB60                             |
|             |       2 | MONITOR MAX DAYS              | NM                       |                                                |
|             |       3 | SPECIMEN TYPE                 | CE                       | IEN^ SPECIMEN TYPE^LAB61                       |
|             |       4 | TYPE OF TEST                  | CE                       | 1^WBC or 2^ANC                                 |
| **[{ZPH}]** |       1 | LOCAL POSSIBLE DOSAGE         | ST                       | FREE TEXT                                      |
|             |       2 | PACKAGE                       | CE                       | CE^PACKAGE(S)                                  |
|             |       3 | BCMA UNITS PER DOSE           | NM                       |                                                |

Two protocols, PSS EXT MFU CLIENT and PSS EXT MFU SERVER, are exported and have been created to generate HL7 messages when new drugs are added to the DRUG file (#50) and existing entries are updated. These protocols can only be activated by setting the following parameters in the OUTPATIENT SITE file (#59):

AUTOMATED DISPENSE field (#105) needs to be set to **2.4** .

ENABLE MASTER FILE UPDATE field (#105.2) needs to be set to **YES** .

LOGICAL LINK field (#2005) needs to be set to **PSO DISP** .

DISPENSE DNS NAME field (#2006) needs to be set to the dispensing system DNS name (for example, **dispensemachine1.vha.med.va.gov** ).

DISPENSE DNS PORT field (#2007) needs to be set to the dispensing system port number.

**Specific Transaction**

The Pharmacy/Treatment Encoded Order Message is as follows:

MFN	Master File Notification Message

MSH	Message Header

MFI	Master File Identifier

{MFE	Master File Entry

{{ZPA}	Drug File Information

{RXD}	Pharmacy/Treatment Dispense

{OBR}}	Observation Request

}

**Example:**

MSH|~^\&amp;|PSS VISTA|521~FO-BIRM.VHA.MED.VA.GOV~DNS|PSS DISPENSE|~DISPENSE1.VHA.MED.VA.GOV:9300~DNS|20030701||MFN~M01~MFN\_M01|10001|P|2.4|||AL|AL

MFI|50~DRUG~99PSD||UPD|||NE

MFE|MUP|||PROPANTHELINE 15MG TAB

ZPA|PROPANTHELINE 15MG TAB|N|LFN~Local Non-Formulary~Pharm Formulary Listing|20031226|Take with food|DE200|6|P|50~6505-00-960-8383~LPS50|8~NO ALCOHOL~LPS54|229~Bacitracin~LPSD50.7|3~CAP,ORAL~LPSD50.606|15~IV PUSH~LPSD51.2|3643~ATROPINE SO4 0.4MG TAB~LPSD50.68|OP~OP Dispense~99OP|20030830|9~Rubella~LLAB60|72~Hair of Scalp~LLAB61|PSOCLO1|N|100|20~MG~LPSD50.607|4.28&amp;USD~UP|15.64&amp;USD~UP|TAB|2|BLUE HOUSE VENDOR|0010-0501-33|TRADENAME

RXD||||1|||||1|||~P&amp;200&amp;LPSD50.0903||||||||||||O

OBR||||1102~ACETAZOLAMIDE~LLAB60|||||||||||70&amp;NECK&amp;LLAB61|||||||||WBC|||7

#### HL7 Drug Message Segment Definition Table

When the PSS EXT MFU SERVER protocol is enabled, the following table defines the data elements sent in each segment of the HL7 drug message.

Table 2: Segments Used in the Master File Update Message

| SEGMENT   |   SEQ# |   LEN | DT     | R/O   |   RP/# |   TBL# | ELEMENT NAME                                                 | EXAMPLE                                         |
|-----------|--------|-------|--------|-------|--------|--------|--------------------------------------------------------------|-------------------------------------------------|
| MSH       |      1 |     1 | ST     | R     |        |        | Field Separator                                              | &#124;                                          |
|           |      2 |     4 | ST     | R     |        |        | Encoding Characters                                          | ~^\&                                            |
|           |      3 |   180 | HD     | R     |        |   0361 | Sending Application                                          | PSS VISTA                                       |
|           |      4 |   180 | HD     | R     |        |   0362 | Sending Facility – station ID and station DNS name           | 521~FO-BIRM.MED.VA.GOV~DNS                      |
|           |      5 |   180 | HD     | R     |        |   0361 | Receiving Application                                        | PSS DISPENSE                                    |
|           |      6 |   180 | HD     | R     |        |   0362 | Receiving Facility – DNS name and port of dispensing machine | ~DISPENSE.VHA.MED.VA.GOV:9300~DNS               |
|           |      7 |    26 | TS     |       |        |        | Date/Time of Message                                         | 20040405152416                                  |
|           |      9 |    15 | CM     | R     |   0076 |        | Message Type                                                 | MFN_M01                                         |
|           |     10 |    20 | ST     | R     |        |        | Message Control ID                                           | 10001                                           |
|           |     11 |     3 | PT     | R     |   0103 |        | Processing ID                                                | P                                               |
|           |     12 |     3 | VID    | R     |   0104 |        | Version ID                                                   | 2.4                                             |
|           |     15 |     2 | ID     |       |        |   0155 | Accept Ack. Type                                             | AL                                              |
|           |     16 |     2 | ID     |       |        |   0155 | Application Ack Type                                         | AL                                              |
| MFI       |      1 |   250 | CE     | R     |        |   0175 | Master File Identifier                                       | 50^DRUG^99PSD                                   |
|           |      3 |     3 | ID     | R     |        |   0178 | File-Level Event Code                                        | UPD                                             |
|           |      6 |     2 | ID     | R     |        |   0179 | Response Level Code                                          | NE                                              |
| MFE       |      1 |     3 | ID     | R     |        |   0180 | Record-Level Event Code                                      | MUP                                             |
|           |      4 |   200 | Varies | R     |        |        | Primary Key Value – MFE                                      | PROPANTHELINE 15MG TAB                          |
| ZPA       |      1 |   200 | Varies | R     |        |        | Primary Key Value – ZPA                                      | PROPANTHELINE 15MG TAB                          |
|           |      2 |     1 | ID     | R     |        |   0136 | Is Synonym                                                   | N                                               |
|           |      3 |   200 | CE     | R     |        |        | Formulary Listing                                            | LFN~Local Non-Formulary~Pharm Formulary Listing |
|           |      4 |    10 | DT     | O     |        |        | Inactive Date                                                | 20031226                                        |
|           |      5 |   200 | ST     | O     |        |        | Drug Message                                                 | Take with Food                                  |
|           |      6 |    30 | ST     | O     |        |        | Drug Classification                                          | DE200                                           |
|           |      7 |    10 | ST     | O     |        |        | DEA-Schedule Code                                            | 6                                               |
|           |      8 |     1 | ST     | O     |        |        | DEA-Drug Type                                                | P                                               |
|           |      9 |   100 | CE     | R     |        |        | Stock Number                                                 | 50~6505-00-960-8383~LPS50                       |
|           |     10 |   100 | CE     | O     |        |        | Warning Label                                                | 8~NO ALCOHOL~LPS54                              |
|           |     11 |   100 | CE     | O     |        |        | Pharmacy Orderable Item                                      | 229~Bacitracin~LPSD50.7                         |
|           |     12 |   100 | CE     | O     |        |        | Dosage Form                                                  | 3~CAP,ORAL~LPSD50.606                           |
|           |     13 |   100 | CE     | O     |        |        | Medication Route                                             | 15~IV PUSH~LPSD51.2                             |
|           |     14 |   100 | CE     | O     |        |        | Drug Name Identifiers                                        | 3643~ATROPINE SO4 0.4MG TAB~LPSD50.68           |
|           |     15 |   100 | CE     | O     |        |        | Dispense Flags                                               | OP~OP Dispense~99OP                             |
|           |     16 |    15 | DT     | O     |        |        | Drug Expiration Date                                         | 20030830                                        |
|           |     17 |   100 | CE     | O     |        |        | Lab Test Monitor                                             | 9~Rubella~LLAB60                                |
|           |     18 |   100 | CE     | O     |        |        | Specimen Type                                                | 72~Hair of Scalp~LLAB61                         |
|           |     19 |    10 | CE     | O     |        |        | Monitor Routine                                              | PSOCLO1                                         |
|           |     20 |     1 | ID     | O     |        |        | Lab Monitor Mark                                             | N                                               |
|           |     21 |    50 | NM     | O     |        |        | Strength                                                     | 100                                             |
|           |     22 |   250 | CE     | R     |        |        | Unit                                                         | 20~MG~LPSD50.607                                |
|           |     23 |    50 | CP     | R     |        |        | Price Per Order Unit                                         | 4.28&USD~UP                                     |
|           |     24 |    50 | CP     | R     |        |        | Price Per Dispense Unit                                      | 15.64&USD~UP                                    |
|           |     25 |    25 | ST     | O     |        |        | Dispense Unit                                                | TAB                                             |
|           |     26 |    50 | NM     | O     |        |        | Dispense Units Per Order Unit                                | 2                                               |
|           |     27 |    50 | ST     | O     |        |        | Vendor                                                       | BLUE HOUSE VENDOR                               |
|           |     28 |    12 | ST     | O     |        |        | NDC Code                                                     | 0010-0501-33                                    |
|           |     29 |    25 | ST     | O     |        |        | Intended Use                                                 | TRADE NAME                                      |
| RXD       |      4 |    20 | NM     | R     |        |        | Actual Dispense Amount                                       | 1                                               |
|           |      8 |    20 | NM     | R     |        |        | Dispense Notes                                               | 1                                               |
|           |     12 |    10 | CQ     | O     |        |        | Total Daily Dose                                             | ~P&200&LPSD50.0903                              |
|           |     24 |     2 | ID     | R     |        |        | Dispense Package Method                                      | O                                               |
| OBR       |      4 |   250 | CE     | O     |        |        | Universal Service Identifier                                 | 1102~ACETAZOLAMIDE~LLAB60                       |
|           |     15 |   300 | CM     | O     |        |        | Specimen Source                                              | 70&NECK&LLAB61                                  |
|           |     24 |     3 | ID     | R     |        |        | Diagnostic Serv Sect ID                                      | WBC                                             |
|           |     27 |   200 | TQ     | O     |        |        | Quantity/Timing                                              | 7                                               |

Notes Pertaining to Some of the Data Elements:

[MSH-3] Sending Application is the station ID along with the DNS name of the sending facility.

[MSH-5] Receiving Application is the DNS name and DNS port number of the dispensing application.

[MSH-10] Message Control ID is the number that uniquely identifies the message. It is returned in MSA-2 of the dispense completion message.

[MFI-1] Master File Identifier is hard-coded to 50~DRUG~99PSD.

[MFE-1] Record-Level Event Code can be either MUP for Update or MAD for Add.

[MFE-4] Primary Key Value – MFE is the GENERIC NAME field (#.01) from the DRUG file (#50).

[ZPA-1] Primary Key Value – ZPA will be the generic name of the drug first and then all synonyms will follow in consecutive ZPA segments.

[ZPA-2] Is Synonym is set to Y or N depending on whether the primary key is a synonym.

[ZPA-3] Formulary Listing will contain LFN and/or VISN is the formulary is not to appear on the Local or VISN formulary.

[ZPA-9] Stock Number is the FSN field (#6) from the DRUG file (#50) or the VSN field (#400) from the SYNONYM subfile (#50.1) of the PRESCRIPTION file (#50).

[ZPA-15] Dispense Flags will indicate if this drug may be dispensed to an external interface and if it is marked to be dispensed at a Consolidated Outpatient Pharmacy (CMOP). If both are yes, the answer would be OP~OP Dispense~Pharm dispense^CMOP~CMOP dispense~Pharm dispense flag.

[ZPA-29] Intended User will be TRADE NAME, QUICK CODE, DRUG ACCOUNTABILITY or CONTROLLED SUBSTANCES.

[RXD-4] Actual Dispense Amount is the BCMA UNITS PER DOSE field (#3) from the POSSIBLE DOSAGES file (#50.0903).

[RXD-9] Dispense Notes is the DISPENSE UNITS PER DOSE field (#.01) from the POSSIBLE DOSAGES file (#50.0903).

[RXD-12] Total Daily Dose will be either P for Possible Dosages or LP for Local Possible Dosages.

[OBR-4] Universal Service Identifier is used for Clozapine Lab Test.

[OBR-15] Specimen Source is used for Clozapine Specimen Type.

[OBR-24] Diagnostic Serv Sect ID is used for Clozapine Type of Test.

[OBR-27] Quantity/Timing is used to encode Monitor Max days from the CLOZAPINE LAB TEST file (#50.02).

#### Data Archiving and Purging

There are no archiving and purging functions necessary with this release of the PDM package.

#### Callable Routines / Entry Points / Application Program Interfaces (APIs)

APIs, callable routines, and entry points can be viewed by first choosing the *DBA* menu option on FORUM and then choosing the *Integration Agreement* s *Menu* option:

IAs INTEGRATION CONTROL REGISTRATIONS ...

For detailed information on all supported Pharmacy Data Management APIs, see the *Pharmacy Re-Engineering (PRE) Application Program Interface (API) Manual* posted on the VistA Documentation Library (VDL).

#### Medication Routes

The following paragraphs provide an explanation of medication route information.

**For Outpatient Pharmacy &amp; Inpatient Medication Unit Dose Orders** :

The Default med route will be returned from the DEFAULT MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) if it is populated, or from the POSSIBLE MED ROUTES multiple (#50.711) of the PHARMACY ORDERABLE ITEM file (#50.7) if it is populated with a single entry and the USE DOSAGE FORM MED ROUTE LIST field (#10) is set to "NO." The med route selection list will be returned with entries from the POSSIBLE MED ROUTES multiple (#50.711) if the USE DOSAGE FORM MED ROUTE LIST field (#10) is set to "NO." Otherwise, the med routes associated with the orderable item's dosage form, MED ROUTE FOR DOSAGE FORM multiple (#50.6061) of the DOSAGE FORM file (#50.606), will be returned.

**For IV Fluids Orders** :

If there is only one orderable item in the IV order request, the same logic as defined above under ‘For Outpatient Pharmacy &amp; Inpatient Medication Unit Dose Orders’ will be used to return the default med route from the DEFAULT MED ROUTE field (#.06) and the med route selection list from the PHARMACY ORDERABLE ITEM file (#50.7).

If there is more than one orderable item on the IV order request, the PHARMACY ORDERABLE ITEM file (#50.7) will be checked for each orderable item for the default med route and med route selection list as defined above under ‘For Outpatient Pharmacy &amp; Inpatient Medication Unit Dose Orders.’ If there is a default med route common with every orderable item, that default med route will be returned. Similarly, the list of possible med routes that are common with every orderable item will be returned.

#### Administration Scheduling

The following rules apply to administration scheduling.

If there is a duplicate schedule, and if one of them contains ward-specific administration times for the ward location of the patient, the schedule returned for inclusion in the array of selectable schedules in CPRS will be the one with the ward-specific administration times.

If no duplicate has ward-specific administration times for the ward location of the patient, the schedule with the lowest IEN number will be returned. If both (or more than one) duplicate schedules have ward-specific administration times for the ward location of the patient, the schedule with the lowest IEN number in the ADMINISTRATION SCHEDULE file #51.1 will be the schedule in the array returned to CPRS.

#### External Relations

**Integration Agreements**

IAs can be viewed by first choosing the *DBA* option on FORUM and then the *Integration Agreement* s *Menu* option.

**Example: DBA Option**

Select Primary Menu Option: DBA

Select DBA Option: INTEGration Agreements Menu

Select Integration Agreements Menu Option:  Custodial Package Menu

Select Custodial Package Menu Option:  ACTIVE by Custodial Package

Select PACKAGE NAME: PHARMACY DATA MANAGEMENT     PSS

DEVICE: HOME//

#### Internal Relations

All PDM options can function independently.

#### Package-Wide Variables

There are no package-wide variables for this version.

### Package Requirements

The PDM module relies on, at least, the following external packages to run effectively.

Table 3: Package Requirements

| Package                               | Minimum version needed   |
|---------------------------------------|--------------------------|
| National Drug File                    | V. 4.0                   |
| Outpatient Pharmacy                   | V. 7.0                   |
| Inpatient Medications                 | V. 5.0                   |
| Kernel                                | V. 8.0                   |
| VA FileMan                            | V. 22.0                  |
| HealtheVet Web Services Client (HWSC) | V. 1.0                   |
| VistALink                             | V. 1.6                   |

#### Additional Information

#### Standards and Conventions Committee (SACC) Exemptions

The following PSS routines will generate errors reported in the XINDEX utility from using non-standard M syntax, due to the need to consume external web services.

PSSFDBDI

PSSFDBRT

PSSHRPST

PSSHTTP

PSS262PO

PSSHDPG1

PSSPGX2

The following waiver permits the use of this non-standard M syntax to allow the use of Cache features to consume external web services. This waiver is located in the HealtheVet Web Services Client (HWSC) Developer Guide.

Table 4: Waiver: OITIMB33554520 - Migration from M2J to VistA Web Services Client (VWSC)

| **Keywords**             | M2J,VWSC,J2EE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Decision Date**        | 12/1/2006                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Decision Type**        | Architecture                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Decision Making Body** | HPMO CCB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Description**          | On December 1, 2006, the HPMO Change Control Board voted to accept the migration of VistA from the current M2J solution to the VistA Web Services Client (VWSC). This decision was made for a number of reasons, in particular the fact that the existing 12-year-old M standard has been surpassed by evolving technologies and can no longer address today’s requirements. Additionally, we are no longer required to support DSM, previously the primary VistA/M hosting environment. Today, all sites are standardized on Caché 5.0 systems. As such, approvals were granted as follows: Waiver of the requirement to adhere to the existing 1995 M standard (that does not address the implementation of web services); Implementation of an industry standard such as web services for VistA/M to J2EE calls using Caché’s built in HTTP and web service client feature; Use of VWSC as an interim solution that ensures continuity of integration between VistA/M applications and migrated J2EE applications as HealtheVet evolves by enabling the consumption of external web services by legacy VistA applications; and Deprecation of the original M2J approach. |
| **Rationale**            | This architectural change allows for a number of improvements, including better scalability, resilience, and performance. Deployment and configuration are far less complicated for administrators, and the APIs can be used by a variety of clients rather than solely M-based. It also places responsibility for support, maintenance, etc. with the vendor rather than OI&T.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Record Type**          | TDR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **State**                | Approved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Date Submitted**       | 2/14/2007 8:37:24 AM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

Table 5: Supporting Documentation for the Waiver

| **Link**   | **Document Title**                                                        | **Description**                                           | **Date**   |
|------------|---------------------------------------------------------------------------|-----------------------------------------------------------|------------|
| Download   | Migration from M2J to VistA Web Services Client (VWSC) Email Notification | Email notification alerting of the decision               | 2/13/2007  |
| Download   | VWSC Architecture                                                         | Proposed architecture view of VWSC                        | 12/1/2006  |
| Download   | VWSC Proposed View                                                        | Proposed logical view of VistA Web Services Client (VWSC) | 12/1/2006  |

#### Cross-Reference Logic to Keep Orderable Items Up To Date

With the introduction of PSS*1*38, a new process for keeping Orderable Items updated was implemented. The process is explained in detail in the section below.

Anytime specific fields are edited, or a pointer to the PHARMACY ORDERABLE ITEM file (#50.7) changes, the Orderable Item (OI) must be updated and sent to CPRS. Two different situations can precipitate these changes. Both situations are explained in detail here.

The first situation occurs when a field is edited that can possibly affect the status of the Orderable Item, but no Orderable Item pointers change. In this situation, the old Orderable Item is the same as the new Orderable Item. In these cases, the kill logic will be the same as the set logic. The kill and set logic will simply pass in the Orderable Item to the routine that checks all IV Additives/IV Solutions/Dispense Drugs matched to the Orderable Item, does all the necessary updates (Inactivation date, Supply flag, Non-formulary, Base, Additive), and then sends the Master File Update to CPRS on that Orderable Item. This type of update occurs when the fields listed below are edited.

File 50: DEA Special Hdlg

File 50: Inactivation Date

File 50: Application Packages’ Use

File 50: Local Non-Formulary

File 50.7: Inactivation Date

File 52.6: Inactivation Date

File 52.6: Used in IV Fluid Order Entry

File 52.7: Inactivation Date

File 52.7: Used in IV Fluid Order Entry

The second situation occurs when pointers to the PHARMACY ORDERABLE ITEM file (#50.7) are changed. IV Additives, IV Solutions and the Dispense Drug always point to the same Orderable Item. That Orderable Item is, in turn, pointed to by the IV Additive or IV Solution. So, the fields that may be affected include the Orderable Item pointer in the DRUG file (#50) and the Generic Drug pointer in the IV ADDITIVES file (#52.6) and the IV SOLUTIONS file (#52.7).

File 50: Orderable Item Pointer

File 52.6: Generic Drug Pointer

File 52.7: Generic Drug Pointer

The initial change is to make the Orderable Item pointers in the IV ADDITIVES file (#52.6) and the IV SOLUTIONS file (#52.7) uneditable. The software will now control those pointers.

**Scenario 1: The Orderable Item Pointer Is Changed For A Dispense Drug**

In Example 1, the Orderable Item pointer is changed for a Dispense Drug. In this case, any Orderable Item pointers must be updated for entries in the IV ADDITIVES file (#52.6) and the IV SOLUTIONS file (#52.7) that point to that Dispense Drug. After these pointers have been updated, the Orderable Item must be updated for the old Orderable Item with what will point to it after the matching. The Orderable Item must also be updated for the new Orderable Item after the matching. And these pharmacy Orderable Item updates must be sent to CPRS as part of the Master File Update. To accomplish this, the following steps must be completed:

1. Add a Cross-Reference on the Orderable Item pointer in the DRUG file (#50) that will hard set one Cross-Reference in the ORDERABLE ITEM file (#50.7) and two Cross-References in the DRUG file (#50) as follows.

Orderable Item:	^PS(50.7,"A50",Orderable Item IEN, Dispense Drug IEN)=""

Drug file:	^PSDRUG("A526", Dispense Drug IEN, Additive IEN,)=""

Drug file:	^PSDRUG("A527", Dispense Drug IEN, Solution IEN,)=""

The Orderable Item Cross-Reference allows access to Dispense Drugs matched to an Orderable Item.  The two DRUG file (#50) Cross-References allow access to Solutions and Additives linked to Dispense Drugs. An "A50" Cross-Reference will also be added on the NAME field (# .01) of the PHARMACY ORDERABLE ITEM file (#50.7) containing a "Quit" command for the set and kill logic for documentation purposes only.

When the Orderable Item pointer of a Dispense Drug changes, only one Cross-Reference is needed on that field to perform the following actions:

**Kill Logic:** This command performs a hard kill of the "A50" Cross-Reference in the PHARMACY ORDERABLE ITEM file (#50.7) for that Dispense Drug using old value (X) and DA, where X equals the OI IEN and DA equals the Dispense Drug IEN. The two DRUG file (#50) Cross-References will not change.

After the hard kill is completed, a Master File Update is performed for the old Orderable Item. The logic for all Dispense Drugs/IV Additives/IV Solutions matched to the Orderable item is executed by looping the three Cross-References to find all entries in all three files matched to the Orderable Item. Also in the Kill logic, the Orderable Item pointer is set to null and the Orderable Item pointer Cross-Reference is killed for any IV Additives or IV Solutions matched to the Dispense Drug.

**Set Logic:** Using the New Value (X), where X equals the OI IEN, the "A50" Cross-Reference is hard set in the PHARMACY ORDERABLE ITEM file (#50.7). The Master File Update is then performed for the new Orderable Item. The logic for all Dispense Drugs/IV Additives/IV Solutions matched to the Orderable Item is executed by looping on the three Cross-References to find all entries in all three files matched to the Orderable Item. The Orderable Item pointer and the Orderable Item pointer Cross-References are then hard set for all IV Additives and IV Solutions that have been matched to the Dispense Drug with new value (X).

**Example 1:**

**Additives/Solution	Dispense Drugs:	Orderable Item:**

IEN 3 	points to =&gt;	IEN 100	points to =&gt;	500

IEN 4	points to =&gt;	IEN 100	points to =&gt;	500

IEN 5	points to =&gt; 	IEN 100	points to =&gt;	500

IEN 10 	points to =&gt;	IEN 200	points to =&gt;	500

**Cross-References are:** ^PS(50.7,"A50",500,100)=""

^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,3)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

Orderable Item 500 is pointed to by Dispense Drugs 100 and 200, and by IV Additives 3, 4, and 5, and IV Solution 10.

(If the LOCAL NON-FORMULARY field (#51) in the DRUG file (#50) is edited, the software will obtain the OI pointer 500 and execute the OI logic by looping on 500 in the "A50" Cross-Reference of the PHARMACY ORDERABLE ITEM file (#50.7). As it references each entry, the OI logic is executed by looping on the “A526” and “A527” Cross-references on the DRUG file (#50) before going to the next Orderable Item pointer in the "A50" Cross-reference in the PHARMACY ORDERABLE ITEM file (#50.7). For Example 1 above, the software will find in the first "A50" Cross-Reference for OI 500, Dispense Drug 100. The software will then loop through all the “A526” and “A527” Cross-References in the DRUG file (#50) to find the IV Additives 3, 4 and 5. In the second “A50” Cross-Reference for OI 500, Dispense Drug 200 is identified.  The software will again loop through any existing “A526” and “A527” Cross-references in the DRUG file (#50) to find IV Solution 10.

If the Orderable Item pointer for Dispense Drug 100 is edited from 500 to 600, the Cross-Reference in the DRUG file (#50) the following logic will be performed.

**Kill Logic**

Kill the Cross-Reference ^PS(50.7,"A50",500,100) using DA and old value (X=500), where DA equals the IEN of the Dispense Drug and X equals the IEN of the Orderable Item

The Cross References would now be as follows.

^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,3)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

The ‘A50” and “A527” Cross-references now identify Orderable Item 500 to be pointed to by Dispense Drug 200 and IV Solution 10. The Orderable Item update for OI 500 is then performed for Dispense Drug 200 and IV solution 10.

While still in the Kill logic, the PHARMACY ORDERABLE ITEM field (#15) in the IV ADDITIVES file (#52.6) is set to null for IV Additives 3, 4, and 5. This action results in the deletion of Cross-References on the PHARMACY ORDERABLE ITEM field (#15) of the IV ADDITIVES file (#52.6).

**Set Logic**

The “A50” Cross-Reference in the PHARMACY ORDERABLE ITEM file (#50.7) for the new Orderable Item 600 is set as follows.

^PS(50.7,"A50",500,200)=""

^PS(50.7,"A50",600,100)=""

^PSDRUG("A526",100,3)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

The Orderable Item logic is executed on the new OI 600 by looping on the "A50" Cross-Reference, to get the Dispense Drug pointer of 100. The software then loops through any existing “A526” and “A527” Cross-References to get IV Additives 3, 4 and 5.

The value of the PHARMACY ORDERABLE ITEM (#15) field in the IV ADDITIVES file (#52.6) for IV Additives 3, 4, and 5 is set to 600. Existing Cross-References are also set to reflect this change.

**Scenario 2: The Dispense Drug Pointer Is Edited For An IV Additive Or IV Solution**

If the Dispense Drug is changed for an IV Additive or IV Solution, the Cross-References on the PHARMACY ORDERABLE ITEM field in the IV ADDITIVES file (#52.6) and IV SOLUTION file (#52.7) will perform the following set and kill logic.

**Kill Logic**

First, the "A526" or "A527" Cross-References in the DRUG file (#50) will be killed. Then, using DA, which is equal to the Orderable Item IEN, the software will get the old Orderable Item pointer value and perform the Orderable Item logic on the old Orderable Item. Subsequently, the value in the PHARMACY ORDERABLE ITEM field for the IV Additive and/or IV Solution will be set to null and the existing Cross-References on this field will be killed.

**Set Logic**

First, the "A526" or "A527" Cross-References in the DRUG file (#50) will be set. Then Using X, which is equal to the Dispense Drug IEN, the software will identify the new Orderable Item in the DRUG file (#50) and perform the OI logic on that Orderable Item. The PHARMACY ORDERABLE ITEM field in the IV ADDITIVES file (#52.6) and IV SOLUTION file (#52.7) will be set to the new value and existing Cross-References will be also set.

<!-- image -->

Users can first check the new Dispense Drug, and if the Orderable Item does not change by rematching the Additive/Solution to the new Dispense Drug, they can choose the QUIT command.

**Example 2:**

**IV Additives/IV Solution	Dispense Drugs	Orderable Item**

IEN 3	points to =&gt;	IEN 100	points to =&gt;	500

IEN 4	points to =&gt;	IEN 100	points to =&gt;	500

IEN 5	points to =&gt;	IEN 100	points to =&gt;	500

IEN 10	points to =&gt;	IEN 200	points to =&gt;	500

**Cross-References** ^PS(50.7,"A50",500,100)=""

^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,3)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

For example, the USED IN IV FLUID ORDER ENTRY field (#17) in the IV ADDITIVES file (#52.6) for IV Additive 3 could be edited. The Orderable Item that the IV Additive points to in this case, is 500. Both the Kill and Set logic (same logic) for the OI 500 is updated by looping through the "A50" Cross-Reference in the PHARMACY ORDERABLE ITEM file (#50.7), finding each Dispense Drug IEN, and going through the "A526" and  "A527" Cross-References in the DRUG file (#50) for that Dispense Drug. This process is then repeated for the next Dispense drug identified in the “A50” Cross-Reference

If the DRUG file (#50) pointer for IV Additive 3 were changed from Dispense Drug 100 to Dispense Drug 900, the Cross-Reference on the Dispense Drug Pointer would be killed.

**Kill Logic**

Using old value of X, which equals the Dispense Drug 100 and DA, which equals the IV ADDITIVE 3, the software would kill Cross-Reference  ^PSDRUG("A526",100,3) with the following Cross-References remaining.

^PS(50.7,"A50",500,100)=""

^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

Using DA, the software would get the old Orderable Item pointer of 500 and execute the Orderable Item logic for Dispense Drugs 100, IV Additives 4 and 5, Dispense Drug 200, and IV Solution 10.

The value for the PHARMACY ORDERABLE ITEM field (#15) in the IV ADDITIVES file (#52.6) would be set to null and Cross-References on this field would be deleted.

**Set Logic**

Using new value X, where X equals the Dispense Drug 900, the software would set the new "A526" Cross Reference as ^PSDRUG("A526",900,3)="", The updated Cross-References are as follows

^PS(50.7,"A50",500,100)=""

^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A526",900,3)=""

^PSDRUG("A527",200,10)=""

Using new value of X, where X equals the Dispense Drug 900, the software gets the Orderable Item pointer for Dispense Drug 900, in this example, Orderable Item 2000. The applicable Cross-References would be the following.

^PS(50.7,"A50",500,100)=""

^PS(50.7,"A50",500,200)=""

^PS(50.7,"A50",2000,900)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A526",900,3)=""

^PSDRUG("A527",200,10)=""

The software performs the OI update for Orderable Item 2000, with Dispense Drug 900 and IV Additive 3. The PHARMACY ORDERABLE ITEM field (#15) value in the IV ADDITIVES file (#52.6) is set to 2000. The corresponding Cross-References on this field are also set.

### Security Management

The PDM package does not contain any VA FileMan security codes except for programmer security (@) on the data dictionaries for the PDM files. Security with respect to standard options in the module is implemented by carefully assigning options to users and by the use of security keys.

#### Mail Groups

Patch PSS*1*147 creates a new mail group called PSS ORDER CHECKS. The mail group description below was retrieved from VA FileMan. The IRM Pharmacy support and Pharmacy ADPACs (and backups) should at a minimum be added to this mail group.

**NAME: PSS ORDER CHECKS**

TYPE: public

DESCRIPTION:   Members of this mail group will receive various notifications

that impact Enhanced Order Checks (drug-drug interactions, duplicate therapy

and dosing checks) introduced with PRE V. 0.5 utilizing a COTS database.

Patch PSS*1*227 creates a new mail group called PSS DEE AUDIT. The mail group description below was retrieved from VA FileMan. This mail group should include anyone who should be notified when changes are made to the DRUG file (#50). For more information on this mail group, refer to the *Pharmacy Data Management Manager’s User Manual* .

**NAME: PSS DEE AUDIT**

TYPE: public

DESCRIPTION:   Members of this mail group will receive audit notifications

when certain fields are viewed or changed in the DRUG file (#50).

#### Alerts

There are no alerts in the PDM package.

#### Bulletins

Bulletins are 'Super' messages. Each Bulletin has a text and a subject just like a normal message. But embedded within either the subject or the text can be variable fields that can be filled in with parameters. There is also a standard set of recipients in the form of a Mail Group that is associated with the bulletin.

Bulletins are processed by MailMan either because of either a special type of cross reference or a direct call in a routine. The interface for the direct call is described in the documentation on programmer entry points. FileMan sets up code that will issue a bulletin automatically when the special cross reference type is created. In either case the parameters that go into the text and/or the subject make each bulletin unique.

NAME: PSS FDB INTERFACE

SUBJECT: ORDER CHECK DATABASE DOWN

RETENTION DAYS: 3

PRIORITY?: YES

NAME: PSS FDB INTERFACE RESTORED

SUBJECT: ORDER CHECK DATABASE IS BACK UP

RETENTION DAYS: 3

PRIORITY?: YES

#### Remote Systems

PDM does not transmit data to any remote system or facility.

#### Archiving / Purging

There are no archiving and purging functions necessary with the PDM package.

#### Contingency Planning

Sites utilizing the PDM package should develop a local contingency plan to be used in the event of product problems in a live environment. The facility contingency plan must identify the procedure for maintaining functionality provided by this package in the event of system outage. Field station Information Security Officers (ISOs) may obtain assistance from their Regional Information Security Officer (RISO).

#### Interfacing

There are no specialized products embedded within or required by the PDM package.

#### Electronic Signatures

No electronic signatures are utilized in the PDM package.

#### Locked Menu Options

This section relates only to options that are locked. For a complete listing of The PDM options listed in the PSS MGR Menu structure, refer to the Menu/Options section of this document.

<!-- image -->

**Locked: PSXCMOPMGR**

Without the PSXCMOPMGR key the *CMOP Mark/Unmark (Single drug)* option will not appear on your menu.

#### Security Keys

The PSS ORDER CHECKS security key is used to control access to the Enable/Disable Dosing Order Checks [PSS DOSING ORDER CHECKS] option.

In order to mark or edit package specific fields in a DRUG file (#50) entry, the user must hold the corresponding package key. The keys are assigned for the individual packages. PDM does not export any of these keys.

Table 6: Security Keys

| Package                                 | Keys       |
|-----------------------------------------|------------|
| Outpatient Pharmacy                     | PSORPH     |
| Inpatient Medications                   | PSJU MGR   |
| Inpatient Medications                   | PSJI MGR   |
| Automatic Replenishment/Ward Stock      | PSGWMGR    |
| Drug Accountability/Inventory Interface | PSAMGR     |
| Drug Accountability/Inventory Interface | PSA ORDERS |
| Controlled Substances                   | PSDMGR     |
| National Drug File                      | PSNMGR     |
| Consolidated Mail Outpatient Pharmacy   | PSXCMOPMGR |

Patch PSS*1*147 exports the following four security keys, that will be used by the Pharmacy Enterprise Customization System (PECS) application. Only a few users who will be granted access to the PECS application will need one or more keys assigned based on their role. Assignment of these keys should be by request only. The security key descriptions were retrieved from VA FileMan.

NAME: PSS\_CUSTOM\_TABLES\_ADMIN

DESCRIPTIVE NAME: ADMINISTRATOR

DESCRIPTION:  This key is used by the Pharmacy Enterprise Customization System (PECS) web application. Holders of this key will have the ability to perform configuration and administrative tasks for the application. They will also have querying capabilities.

NAME: PSS\_CUSTOM\_TABLES\_APPROVER

DESCRIPTIVE NAME: APPROVER

DESCRIPTION:  This key is used by the Pharmacy Enterprise Customization System (PECS) web application.  Holders of this key will have the same privileges as those with the PSS CUSTOM TABLES REQUESTOR key. Additional capabilities will be to review, approve, delete or reject customization requests and to view and generate reports.

NAME: PSS\_CUSTOM\_TABLES\_REL\_MAN

DESCRIPTIVE NAME: RELEASE MANAGER

DESCRIPTION:  This key is used by the Pharmacy Enterprise Customization System (PECS) web application. Holders of this key will have the ability to create file updates for FDB database tables to be applied at local facilities. They will also have querying capabilities.

NAME: PSS\_CUSTOM\_TABLES\_REQUESTOR

DESCRIPTIVE NAME: REQUESTOR

DESCRIPTION:  This key is used by the Pharmacy Enterprise Customization System (PECS) web application.  Holders of this key will be allowed to enter customization requests, display and view the status of their own requests. They will also have limited querying capabilities

Five security keys were introduced with Patch PSS*1*167 that will be used to authenticate users accessing the Pharmacy Product System-National (PPS-N) using Kernel Authentication and Authorization for J2EE (KAAJEE).  Users requiring access to the Pharmacy Product System-National should be assigned these keys as appropriate to their level of approved access.  PPS-N is a reengineered product that will replace the National Drug File Management System (NDFMS).  Site users may be assigned the PSS\_PPSN\_VIEWER key only.  The other four security keys are only to be assigned to members of the National NDF Management Group.

NAME: PSS\_PPSN\_MANAGER

DESCRIPTIVE NAME: PPS-National Manager

DESCRIPTION:   This role can perform the operational functions in PPS-N but doesn't have the administrative rights of the PPS-N National Supervisor.

NAME: PSS\_PPSN\_MIGRATOR

DESCRIPTIVE NAME: PPS-National Migration User

DESCRIPTION:   This role has the ability to run the PPS-N Migration.

NAME: PSS\_PPSN\_SECOND\_APPROVER

DESCRIPTIVE NAME: PPS-National Second Approver

DESCRIPTION:   This role has the ability to do a second approval on items that are in the pending second approval state.

NAME: PSS\_PPSN\_SUPERVISOR

DESCRIPTIVE NAME: PPS-National Supervisor

DESCRIPTION:   This role has the ability to perform all actions in the PPS-N application, including Administration and Configuration.

NAME: PSS\_PPSN\_VIEWER

DESCRIPTIVE NAME: PPS-National Viewer

DESCRIPTION:   This role has the ability to log in and view items in the PPS-N Application but cannot modify any of the items.

#### File Security

Information about all files, including these, can be obtained by using the VA FileMan to generate a list of file attributes.

#### PDM Files

Table 7: PDM Files

|   ## File Numbers | File Names                    | DD   | RD   | WR   | DEL   | LAYGO   |
|-------------------|-------------------------------|------|------|------|-------|---------|
|            50     | DRUG                          | @    |      |      |       |         |
|            50.4   | DRUG ELECTROLYTES             | @    |      |      |       |         |
|            50.606 | DOSAGE FORM                   | @    |      | @    | @     | @       |
|            50.7   | PHARMACY ORDERABLE ITEM       | @    |      |      |       |         |
|            51     | MEDICATION INSTRUCTION        | @    |      |      |       |         |
|            51.1   | ADMINISTRATION SCHEDULE       | @    |      |      |       |         |
|            51.2   | MEDICATION ROUTES             | @    |      |      |       |         |
|            51.23  | STANDARD MEDICATION ROUTES    | @    | Pp   | @    | @     | @       |
|            51.24  | DOSE UNITS                    | @    | Pp   | @    | @     | @       |
|            51.25  | DOSE UNIT CONVERSION          | @    | Pp   | @    | @     | @       |
|            51.26  | PHARMACOGENOMIC GENES         | @    | Pp   | @    | @     | @       |
|            51.28  | PHARMACOGENOMIC PHENOTYPES    | @    | Pp   | @    | @     | @       |
|            51.29  | PHARMACOGENOMIC EMAIL LOG     | @    | Pp   | @    | @     | @       |
|            51.5   | ORDER UNIT                    |      |      |      |       |         |
|            51.7   | DRUG TEXT                     | @    |      |      |       |         |
|            52.6   | IV ADDITIVES                  | @    |      |      |       |         |
|            52.7   | IV SOLUTIONS                  | @    |      |      |       |         |
|            53.47  | INFUSION INSTRUCTIONS         |      |      |      |       |         |
|            54     | RX CONSULT                    |      |      |      |       |         |
|            55     | PHARMACY PATIENT (Partial DD) | @    | P    |      |       |         |
|            59.7   | PHARMACY SYSTEM               | ^    |      | ^    | ^     | ^       |
|            59.73  | VENDOR DISABLE/ENABLE         | @    | @    | @    | @     | @       |
|            59.74  | VENDOR INTERFACE DATA         | @    | @    | @    | @     | @       |

#### Non-PDM Files

Table 8: Non-PDM Files

|   File Numbers | File Names                       | DD   | RD   | WR   | DEL   | LAYGO   |
|----------------|----------------------------------|------|------|------|-------|---------|
|  200           | NEW PERSON (Partial DD)          | #    | #    | #    | #     | #       |
|    9.00903e+06 | APSP INTERVENTION TYPE           |      |      |      |       |         |
|    9.00903e+06 | APSP INTERVENTION                |      |      |      |       |         |
|    9.00903e+06 | APSP INTERVENTION RECOMMENDATION |      |      |      |       |         |

<!-- image -->

Please refer to the "Sending Security Codes." section of the Kernel V. 8.0 Systems Manual for more information concerning installation of security codes.

#### References

There are no regulations or directives related to the Pharmacy Data Management package. Additional manuals related to the Pharmacy Data Management package can be found at the VistA Documentation Library (VDL) on the Internet.

### Appendix A: Pharmacy Interface Automation

Introduction appendix provides a brief description of the new features and functions of the Pharmacy Interface Automation project. This projects consist of multiple patches, which must be installed for the functionality to perform.

The Clinical Ancillary Services (CAS) Development Delivery of Pharmacy enhancements (DDPE) Pharmacy Interface Automation project supports the initiative to create an automated interface between the Pharmacy Automated Dispensing Equipment (PADE) used in the inpatient and outpatient care settings and VistA Pharmacy and Admission Discharge Transfer (ADT) applications. This will allow VA health care users the ability to access, transmit, receive alerts, and generate reports on medication transactions.

Pharmacy Interface Automation is a vital enhancement to the medication transaction functions of the PADE.  It allows pharmacists to access dispensing equipment remotely; keep a perpetual inventory of all medication received, dispensed, and wasted; alert the pharmacy of medication removed from the devices without orders; and establishes monitors for potentially inappropriate electronic pharmacy transactions.

This product shall run on standard hardware platforms used by the Department of Veterans Affairs (VA) Healthcare facilities.

The minimum required VistA software is:

Table 9: VistA Software

| Package                                            |   Minimum Version Needed |
|----------------------------------------------------|--------------------------|
| Adverse Reaction Tracking (ART)                    |                      4   |
| BCMA                                               |                      3   |
| Computerized Patient Record System (CPRS)          |                      3   |
| Controlled Substance                               |                      3   |
| Drug Accountability                                |                      3   |
| VA FileMan                                         |                     22   |
| HL7                                                |                      2.4 |
| Inpatient Medications (IP)                         |                      5   |
| Kernel                                             |                      8   |
| MailMan                                            |                      7.1 |
| Master Patient Index/Patient Demographics (MPI/PD) |                      1   |
| National Drug File (NDF)                           |                      4   |
| Nursing Service                                    |                      4   |
| Order Entry/Results Reporting (OERR)               |                      3   |
| Registration                                       |                      5.3 |
| Pharmacy Data Management (PDM)                     |                      1   |
| Remote Procedure Call (RPC) Broker                 |                      1.1 |
| Scheduling                                         |                      5.3 |

#### New Functionality

A new automated bidirectional interface between VistA and PADE has been designed and developed utilizing VIE as the middleware component for communication of HL7 messages and error handling.  The added functional components are:

Provide pharmacists the capability to remotely access dispensing equipment to provide the pharmacist the status of drugs:  whether they have been dispensed, or in the queue or some error condition that may have been encountered by the dispensing equipment.

Provide PADE the capability to transmit dispensing information to VistA Pharmacy to keep a perpetual inventory of all drugs/medications received, dispensed, and wasted.

Provide PADE the capability to alert VistA Pharmacy of medication removal from PADE without orders.

Establish monitors of all potentially inappropriate electronic pharmacy transactions.  Implement trending reports in order to address and detect potentially inappropriate pharmacy transactions, such as drug diversion. For example, reports include the ability to sort transactions by nursing, user, drug, etc., and from the VA-side of the interface.

Refer to the following Pharmacy Interface Automation documents for additional information:

Pharmacy Interface Automation Installation Guide

Pharmacy Interface Automation User Guide

Pharmacy Interface Automation System Design Document

Pharmacy Interface Automation Data Dictionary

A new Pharmacogenomic order checking is added to medication orders entered through Inpatient Medications, Outpatient Pharmacy and Computerized Patient Record System (CPRS). Refer to the following documents for additional information:

PSO\_7\_0\_P737\_MAN\_UM

PSJ\_5\_0\_P447\_PHAR\_UM

PSJ\_5\_0\_P447\_NURSE\_UM

CPRS User Guide\_GUI Version

#### Options and Build Components

The following are the options and build components for Pharmacy Interface Automation for PSS*1.0*193:

Select OPTION NAME:    XPD PRINT BUILD     Build File Print

Build File Print

Select BUILD NAME: PSS*1.0*193       PHARMACY DATA MANAGEMENT

DEVICE: HOME// ;;99999  SSH VIRTUAL TERMINAL

PACKAGE: PSS*1.0*193     Nov 25, 2015 10:27 am                           PAGE 1

-------------------------------------------------------------------------------SINGLE PACKAGE                               TRACK NATIONALLY: YES

NATIONAL PACKAGE: PHARMACY DATA MANAGEMENT       ALPHA/BETA TESTING: NO

As part of this patch PSS*1*193, the following enhancements were made:

1. Two new protocols PSS MFNM01 CLIENT and PSS MFNM01 SERVER were added to facilitate sending MFN HL7 drug messages to PADE.

The Send Entire Drug File to External Interface [PSS MASTER FILE ALL]  option was modified to allow transmission of the drug file to an Inpatient Interface (PADE) depending on the PADE setup. It also provides the flexibility of sending all drugs marked for Unit Dose, IV or Ward Stock or send selected drugs to PADE.

Since this option now allows to send all or selected drugs to PADE, the option name "Send Entire Drug File to External Interface" was changed   to "Send Drug File Entries to External Interface"

A new PSS PADE INIT security key was added so that holders of this key can only send "all" drugs to PADE noted in item 2.

Option Drug Enter/Edit [PSS DRUG ENTER/EDIT] was modified to send an addition/update/both or none to PADE provided it is set up to receive such updates.

ENVIRONMENT CHECK:                               DELETE ENV ROUTINE:

PRE-INIT ROUTINE:                          DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE:                         DELETE POST-INIT ROUTINE:

PRE-TRANSPORT RTN:

ROUTINE:                                       ACTION:

PSSDEE                                         SEND TO SITE

PSSHLDFS                                       SEND TO SITE

PSSMSTR                                        SEND TO SITE

OPTION:                                        ACTION:

PSS MASTER FILE ALL                            SEND TO SITE

SECURITY KEY:                                  ACTION:

PSS PADE INIT                                  SEND TO SITE

PROTOCOL:                                      ACTION:

PSS MFNM01 CLIENT                              SEND TO SITE

PSS MFNM01 SERVER                              SEND TO SITE

REQUIRED BUILDS:                               ACTION:

PSS*1.0*180                                    Don't install, leave global

CDEVISC1A2:DVA&gt;

#### Modified and New Routines

The following routines are for PSS*1*193:

PSSDEE

PSSHLDFS

PSSMSTR

The following routines are added for PSS*1*262

PSS262PO

PSS262PR

PSSHDPG1

PSSPGX

PSSPGX1

PSSPGX2

PSSPGXOR

PSSPGXP2

PSSPGXPR

PSSPGXT1

PSSPGXTS

PSSPGXU2

PSSPGXUT

The following routines are modified for PSS*1*262

PSSDSFDB

PSSHRIT

PSSHRVL1

PSSLOOK

### Glossary

Table 10: Glossary

| Term                            | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Administration Schedule File    | The ADMINISTRATION SCHEDULE file (#51.1) contains administration schedule names and standard dosage administration times. The name is a common abbreviation for an administration schedule (e.g., QID, Q4H, PRN). The administration time is entered in military time.                                                                                                                                                                                                                                                                                                                                              |
| CPRS                            | A VistA computer software package called Computerized Patient Record System. CPRS is an application in VistA that allows the user to enter all necessary orders for a patient in different packages from a single application.                                                                                                                                                                                                                                                                                                                                                                                      |
| DATUP                           | Functionality that allows the Pharmacy Enterprise Customization System (PECS) to send out custom and standard commercial-off-the-shelf (COTS) vendor database changes to update the two centralized databases at Austin and Martinsburg.                                                                                                                                                                                                                                                                                                                                                                            |
| Dispense Drug                   | The Dispense Drug is pulled from DRUG file (#50) and usually has the strength attached to it (e.g., Acetaminophen 325 mg). Usually, the name alone without a strength attached is the Pharmacy Orderable Item name.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Dosage Form File                | The DOSAGE FORM file (#50.606) contains all dosage forms and associated data that are used by Pharmacy packages and CPRS. The dosage form is used in SIG construction, default values and in the determination of the type of each dosage created for each application.                                                                                                                                                                                                                                                                                                                                             |
| Dose Unit Conversion File       | The DOSE UNIT CONVERSION file (#51.25) was created to convert one dose unit to another using a conversion factor so that a comparison can be made between two dose units when they are not equivalent. The dose unit used for the Dosing Order Check may not be the same dose unit First Databank (FDB) returns with the Dosing Order Check results.                                                                                                                                                                                                                                                                |
| Dose Unit File                  | The DOSE UNIT file (#51.24) was created to accomplish the mapping to First Data Bank (FDB). All entries in this file have been mapped to an FDB Dose Unit. Although this file has not yet been standardized by Standards and Terminology Services (STS), no local editing will be allowed. When populating the Dose Unit field for a Local Possible Dosage in the DRUG file (#50), selection will be from this new file.                                                                                                                                                                                            |
| Drug Electrolytes File          | The DRUG ELECTROLYTES file (#50.4) contains the names of anions/cations, and their cations and concentration units.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Drug File                       | The DRUG file (#50) holds the information related to each drug that can be used to fill a prescription or medication order. It is pointed to from several other files and should be handled carefully, usually only by special individuals in the Pharmacy Service. Entries are not typically deleted, but rather made inactive by entering an inactive date.                                                                                                                                                                                                                                                       |
| Drug Text File                  | The DRUG TEXT file (#51.7) stores rapidly changing drug restrictions, guidelines, and protocols to help assure medications are being used according to defined specifications.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Infusion Instructions File      | The INFUSION INSTRUCTIONS file (#53.47) holds abbreviations used when entering the Infusion Rate (#.08) field in the IV (#100) multiple of the PHARMACY PATIENT (#55) FILE, AND THE infusion rate (#59) FIELD IN THE non-verified orders (#53.1) file. Each record holds an expansion of the abbreviation which replaces the abbreviation in the Infusion Rate at the time the IV order is created.                                                                                                                                                                                                                 |
| IV Additives File               | The IV ADDITIVES file (#52.6) contains drugs that are used as Additives in the IV room. Data entered includes drug generic name, print name, drug information, synonym(s), dispensing units, cost per unit, days for IV order, usual IV schedule, administration times, electrolytes, and quick code information.                                                                                                                                                                                                                                                                                                   |
| IV Solutions File               | The IV SOLUTIONS file (#52.7) contains drugs that are used as primary solutions in the IV room. The solution must already exist in the Drug file (#50) to be selected. Data in this file includes: drug generic name, print name, status, drug information, synonym(s), volume, and electrolytes.                                                                                                                                                                                                                                                                                                                   |
| Local Possible Dosages          | Local Possible Dosages are free text dosages that are associated with drugs that do not meet all of the criteria for Possible Dosages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Medication Instruction File     | The MEDICATION INSTRUCTION file (#51) is used by Unit Dose and Outpatient Pharmacy. It contains the medication instruction name, expansion and intended use.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Medication Routes File          | The MEDICATION ROUTES file (#51.2) contains medication route names. The user can enter an abbreviation for each route to be used at their site. The abbreviation will most likely be the Latin abbreviation for the term.                                                                                                                                                                                                                                                                                                                                                                                           |
| Medication Routes/Abbreviations | The Medication RouteS file (#51.2) contains the medication routes and abbreviations, which are selected by each Department of Veterans Affairs Medical Centers (VAMC). The abbreviation cannot be longer than five characters to fit on labels and the Medical Administration Record (MAR). The user can add new routes and abbreviations as appropriate.                                                                                                                                                                                                                                                           |
| MOCHA                           | Medication Order Check Healthcare Application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| National Drug File              | The National Drug File provides standardization of the local drug files in all VA medical facilities. Standardization includes the adoption of new drug nomenclature and drug classification and links the local drug file entries to data in the National Drug File. For drugs approved by the Food and Drug Administration (FDA), VA medical facilities have access to information concerning dosage form, strength and unit; package size and type; manufacturer’s trade name; and National Drug Code (NDC). The NDF software lays the foundation for sharing prescription information among medical facilities. |
| Non-Formulary Drugs             | Drugs that are not available for use by all providers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Orderable Item                  | An Orderable Item is pulled from the PHARMACY ORDERABLE ITEM file (#50.7) and usually has no strength attached to it (e.g., Acetaminophen). The name, with a strength attached, is the Dispense Drug name (e.g., Acetaminophen 325mg).                                                                                                                                                                                                                                                                                                                                                                              |
| Orderable Item File             | The ORDERABLE ITEM file (#101.43) is a CPRS file that provides the Orderable Items for selection within CPRS. Pharmacy Orderable Items are a subset of this file.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PECS                            | Pharmacy Enterprise Customization System. A Graphical User Interface (GUI) web-based application used to research, update via DATUP, maintain, and report VA customizations of the commercial-off-the-shelf (COTS) vendor database used to perform Pharmacy order checks such as drug-drug interactions, duplicate therapy, dosing, and pharmacogenomics.                                                                                                                                                                                                                                                           |
| PEPS                            | Pharmacy Enterprise Product System. A re-engineering of pharmacy data and its management practices developed to use a commercial off-the-shelf (COTS) drug database, currently First DataBank (FDB) MedKnowledge, to provide the latest identification and safety information on medications.                                                                                                                                                                                                                                                                                                                       |
| Pending Order                   | A pending order is one that has been entered by a provider through CPRS without Pharmacy finishing the order. Once Pharmacy has finished (and verified for Unit Dose only) the order, it will become active.                                                                                                                                                                                                                                                                                                                                                                                                        |
| Pharmacy Orderable Item         | The Pharmacy Orderable Item is used through CPRS to order Inpatient Medications and Outpatient Pharmacy prescriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Pharmacy Orderable Item File    | The PHARMACY ORDERABLE ITEM file (#50.7) contains the Order Entry name for items that can be ordered in the Inpatient Medications and Outpatient Pharmacy packages.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Possible Dosages                | Dosages that have a numeric dosage and numeric Dispense Units Per Dose appropriate for administration.  For a drug to have possible dosages, it must be a single ingredient product that is matched to VA PRODUCT file (#50.68). The VA PRODUCT file (#50.68) entry must have a numeric strength and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.                                                                                                                                                                           |
| Prompt                          | A point at which the system questions the user and waits for a response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Standard Medication Route File  | The STANDARD MEDICATION ROUTE file (#51.23) was created to map Local Medication Routes in VistA to an FDB Route in order to perform dosage checks in PRE V.0.5.  This file has been standardized by Standards and Terminology Service (STS) and is mapped to an FDB Route. It cannot be edited locally.                                                                                                                                                                                                                                                                                                             |
| Standard Schedule               | Standard medication administration schedules are stored in the Administration Schedule file (#51.1).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Units Per Dose                  | The Units Per Dose is the number of Units (tablets, capsules, etc.) to be dispensed as a dose for an order. Fractional numbers will be accepted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| VA Drug Class Code              | A drug classification system used by VA that separates drugs into different categories based upon their characteristics. Some cost reports can be run for VA Drug Class Codes.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| VA Product File                 | The VA PRODUCT file (#50.68) contains a list of available drug products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Pharmacy Data Management Version 1 Technical Manual/Security Guide (updated PSS*1*252)

## File List

The following PDM files are exported with the PDM package.

**File#       NAME          	UPDATE 	DATA COMES    USER**

**DD	WITH FILE   OVERRIDE**

50          DRUG 	FULL	NO

50.4        DRUG ELECTROLYTES 	FULL	NO

50.606      DOSAGE FORM                  	FULL	YES (MERGE)	NO

50.60699    MASTER DOSAGE FORM	FULL	NO

50.7        PHARMACY ORDERABLE ITEM 	FULL	NO

51          MEDICATION INSTRUCTION        	FULL	NO

51.1        ADMINISTRATION SCHEDULE      	FULL	YES (MERGE)	YES

51.2        MEDICATION ROUTES           	FULL	YES (MERGE)	YES

51.23       STANDARD MEDICATION ROUTES          FULL	YES	NO

(OVERWRITE)

51.24       DOSE UNITS	FULL	YES	NO

(OVERWRITE)

51.25       DOSE UNIT CONVERSION	FULL	YES	NO

(OVERWRITE)

51.5        ORDER UNIT 	FULL	NO

51.7        DRUG TEXT	FULL	YES	YES

(OVERWRITE)

52.6        IV ADDITIVES 	FULL	NO

52.7        IV SOLUTIONS 	FULL	NO

53.47       INFUSION INSTRUCTIONS	FULL	NO

54          RX CONSULT 	FULL (SCREEN)	NO

55          PHARMACY PATIENT (Partial DD)	PARTIAL	NO

59.7        PHARMACY SYSTEM 	FULL	NO

59.73        VENDOR DISABLE/ENABLE	FULL	NO

59.74        VENDOR INTERFACE DATA 	FULL	NO

The following non-PDM files are exported with the PDM package.

**File#	NAME	UPDATE 	DATA COMES    USER**

**DD	WITH FILE   OVERRIDE**

200	NEW PERSON (Partial DD)	PARTIAL	NO

9009032.3	APSP INTERVENTION TYPE	FULL	YES		NO

(OVERWRITE)

9009032.4	APSP INTERVENTION 	FULL	NO

9009032.5	APSP INTERVENTION RECOMMENDATION 	FULL	YES	NO

(OVERWRITE)

### File Descriptions

This package requires the files listed below. Information about the files can be obtained by using the VA FileMan to generate a list of file attributes.

The Data Dictionaries (DDs) are considered part of the online documentation for this software application. Use the VA FileMan *List File Attributes* [DILIST] option *,* under the *Data Dictionary Utilities* [DI DDU] option, to view/print the DDs.

#### Data Dictionary Changes

Patch PSS*1.0*215 adds the RX# UPPER BOUND WARNING LIMIT field (#48) to the PHARMACY SYSTEM file (#59.7). The value stored in this field determines when an early warning message is sent to members of a new PHARMACY SUPERVISORS MailMan group.

This patch is a companion patch to PSO*7.0*452, which implements an early warning message to notify mail group recipients that one or more Outpatient Pharmacy sites are approaching the upper limit of the defined prescription numbering series. If  no custom value is entered in this field, then the message will be sent when 1000 numbers remain in the series, and again each time the associated background job runs and less than 1000 numbers remain in the series. Refer to the *Outpatient Pharmacy (PSO) Manager’s User Guide* for more information about the early warning functionality that uses this new field.

Patch PSS*1.0*215 also adds a CLINICAL ALERT multiple field (#109) to the PHARMACY PATIENT file (#55). This field stores the date and time of the Clinical Alert and provides a free-text field for the alert text, which is displayed when using certain Outpatient Pharmacy [PSO] options. Pharmacy Supervisors can use Clinical Alerts to make Pharmacy staff aware of information such as drug interactions or the patient’s participation in clinical trials. Refer to the *Outpatient Pharmacy (PSO) Manager’s User Guide* for more information about the Clinical Alert functionality that uses this new field.

<!-- image -->

**Note:** The Clinical Alert Enter/Edit [PSO CLINICAL ALERT ENTER/EDIT] option in the Outpatient Pharmacy package is used to add, modify, or delete Clinical Alerts.

Patch PSS*1*247 adds a new parameter, the PHARMACY OPERATING MODE field (#102) in the PHARMACY SYSTEM file (#59.7).  This field may be set to "VAMC", for traditional VA Medical Center pharmacy mode, or "MBM", for Meds By Mail pharmacy mode.  Only the Meds By Mail Pharmacy should set this parameter to “MBM”.  If this parameter is left empty, it will default to “VAMC”.  Functionality is being released in patch PSO*7.0*630 that uses this parameter to help determine whether or not a provider's DEA related information may be edited at the facility. (see the PSO*7.0*630 patch description for more details).

### Menu / Options

The PDM options listed below show the PSS MGR Menu structure.

*Pharmacy Data Management* [PSS MGR] menu:

<!-- image -->

CMOP Mark/Unmark (Single drug)

[PSSXX MARK]

*Dosages…*

[PSS DOSAGES MANAGEMENT]

*Dosage Form File Enter/Edit*

[PSS DOSAGE FORM EDIT]

*Enter/Edit Dosages*

[PSS EDIT DOSAGES]

Most Common Dosages Report

[PSS COMMON DOSAGES]

Noun/Dosage Form Report

[PSS DOSE FORM/ NOUN REPORT]

Review Dosages Report

[PSS DOSAGE REVIEW REPORT]

Local Possible Dosages Report

[PSS LOCAL POSSIBLE DOSAGES]

Request Change to Dose Unit

[PSS DOSE UNIT REQUEST]

*Lookup Dosing Check Info for Drug*

[PSS DRUG DOSING LOOKUP]

*Drug Names with Trailing Spaces Report*

[PSS TRAILING SPACES REPORT]

*Manage Buprenorphine Tx of Pain - VA Products*

**[PSS BUPRENORPHINE VAPRODS]**

*Drug Enter/Edit*

[PSS DRUG ENTER/ EDIT]

*Order Check Management…*

[PSS ORDER CHECK MANAGEMENT]

*Request Changes to Enhanced Order Check Database*

[PSS ORDER CHECK CHANGES]

*Report of Locally Entered Interactions*

[PSS REPORT LOCAL INTERACTIONS]

*Electrolyte File (IV)*

[PSSJI ELECTROLYTE FILE]

*Lookup into Dispense Drug File*

[PSS LOOK]

*Medication Instruction Management...*

[PSS MED INSTRUCTION MANAGEMENT]

*Medication Instruction File Add/Edit*

[PSSJU MI]

*Medication Instruction File Report*

[PSS MED INSTRUCTION REPORT]

*Med Instruction Med Term Route Report*

[PSS MED INST MED ROUTE REPORT]

*Medication Routes Management...*

[PSS MEDICATION ROUTES MGMT]

*Medication Route File Enter/Edit*

[PSS MEDICATION ROUTES EDIT]

*Medication Route Mapping Report*

[PSS MED ROUTE MAPPING REPORT]

*Medication Route Mapping History Report*

[PSS MED ROUTE MAPPING CHANGES]

*Med Instruction Med Term Route Report*

[PSS MED INST MED ROUTE REPORT]

*Request Change to Standard Medication Route*

[PSS MEDICATION ROUTE REQUEST]

*Default Med Route for OI Report*

[PSS DEF MED ROUTE OI RPT]

*Orderable Item Management…*

[PSS ORDERABLE ITEM MANAGEMENT]

*Edit Orderable Items*

[PSS EDIT ORDERABLE ITEMS]

*Dispense Drug/Orderable Item Maintenance*

[PSS MAINTAIN ORDERABLE ITEMS]

*Orderable Item/Dosages Report*

[PSS ORDERABLE ITEM DOSAGES]

*Patient Instructions Report*

[PSS INSTRUCTIONS/ ITEMS REPORT]

*Orderable Item Report*

[PSS ORDERABLE ITEM REPORT]

*Orderable Items that Require Removal Report*

[PSS MRR ORDERABLE ITEMS RPT]

*Orderable Items for High Risk\High Alert*

[PSS HR/HA ORDERABLE ITEMS RPT]

*Formulary Information Report*

[PSSNFI]

*Drug Text Management...*

[PSS DRUG TEXT MANAGEMENT]

*Drug Text Enter/Edit*

[PSS EDIT TEXT]

*Drug Text File Report*

[PSS DRUG TEXT FILE REPORT]

*Pharmacy System Parameters Edit*

[PSS SYS EDIT]

*Standard Schedule Management...*

[PSS SCHEDULE MANAGEMENT]

*Standard Schedule Edit*

[PSS SCHEDULE EDIT]

*Administration Schedule File Report*

[PSS SCHEDULE REPORT]

*Synonym Enter/Edit*

[PSS SYNONYM EDIT]

*Controlled Substances/PKI Reports…*

[PSS CS/PKI REPORTS]

*DEA Spec Hdlg &amp; CS Fed Sch Discrepancy*

[PSS DEA VS CS FED. SCH. DISCR.]

*Controlled Substances Not Matched to NDF*

[PSS CS NOT MATCHED TO NDF]

*CS (DRUGS) Inconsistent with DEA Spec Hdlg*

[PSS CS DRUGS INCON WITH DEA]

*CS (Ord. Item) Inconsistent with DEA Spec Hdlg*

[PSS CS (OI) INCON WITH DEA]

*Send Entire Drug File to External Interface*

[PSS MASTER FILE ALL]

*IV Additive/Solution …*

[PSS ADDITIVE/SOLUTION]

*IV Additive Report*

[PSS IV ADDITIVE REPORT]

*IV Solution Report*

[PSS IV SOLUTION REPORT]

*Mark PreMix Solutions*

[PSS MARK PREMIX SOLUTIONS]

*Warning Builder*

[PSS WARNING BUILDER]

*Warning Mapping*

[PSS WARNING MAPPING]

*PEPS Services…*

[PSS PEPS SERVICES]

*Check Vendor Database Link*

[PSS CHECK VENDOR DATABASE LINK]

*Check PEPS Services Setup*

[PSS CHECK PEPS SERVICES SETUP]

*Schedule/Reschedule Check PEPS Interface*

[PSS SCHEDULE PEPS INTERFACE CK]

*Print Interface Data File*

[PSS VENDOR INTERFACE REPORT]

*Inpatient Drug Management…*

[PSS INP MGR]

*ADditives File*

[PSSJI DRUG]

*Dispense Drug Fields*

[PSSJU DRG]

*Dispense Drug/ATC Set Up*

[PSSJU DRUG/ATC SET UP]

*Edit Cost Data*

[PSSJU DCC]

*EDit Drug Cost (IV)*

[PSSJI EDIT DRUG COST]

*MARk/Unmark Dispense Drugs For Unit Dose*

[PSSJU MARK UD ITEMS]

*PRimary Solution File (IV)*

[PSSJI SOLN]

*Check Drug Interaction*

[PSS CHECK DRUG INTERACTION]

*Infusion Instruction Management …*

[PSS INFINS MGR]

*Infusion Instructions Add/Edit*

[PSS INFINS ADED]

*Infusion Instruction Report*

[PSS INFINS RPT]

*Orders for MRRs With Removal Properties*

[PSS MRR ORDERS DIAGNOSTIC RPT]

<!-- image -->

Locked: PSXCMOPMGR

Without the PSXCMOPMGR key, =the *CMOP Mark/Unmark (Single drug)=* option will not appear on your menu.

### Orderable Items Option

This option enables you to determine which active orders contain Orderable Items that have the new "Prompt for Removal in BCMA" flag value set to 1, 2 or 3 that need to be discontinued and entered as New (not copied, edited or renewed) AFTER the installation of Pharmacy Inpatient

Medications PSJ*5.0*315. Failure to re-create these orders could result in confusing information to display on the BCMA VDL if displayed alongside newer MRR orders that do have the updated removal information.

TYPE: run routine ROUTINE: EN^PSSMRRDG

### XPAR Parameters

Patch PSS*1*227 adds XPAR parameter PSS DRUG AUDIT RETENTION MOS to the PARAMETER DEFINITION file (#8989.51). See the *Pharmacy Data Management Manager’s User Manual* for information on how this parameter is used. To set the parameter, follow the steps below. You must be a VistA programmer, Pharmacy Informaticist, Clinical Application Coordinator (CAC), or other user with access to the General Parameter Tools [XPAR MENU TOOLS] option in VistA.

Log in to VistA.

At the "Select OPTION NAME:" prompt, type XPAR MENU TOOLS and then press Enter.

At the "Select General Parameter Tools Option:" prompt, type EP and then press Enter.

At the "Select PARAMETER DEFINITION NAME:" prompt, type PSS DRUG AUDIT RETENTION MOS and then press Enter.

At the "Drug Audit Retention MOS:" prompt, type the number of retention months and then press Enter.

Patch PSS*1*247 replaces the existing parameter, PSS BUPRENORPHINE PAIN DFS, with a new XPAR parameter PSS BUPRENORPHINE PAIN VAPRODS to the PARAMETER DEFINITION file (#8989.51). To set the parameter, follow the steps below. You must be a VistA programmer, Pharmacy Informaticist, Clinical Application Coordinator (CAC), or other user with access to the General Parameter Tools [XPAR MENU TOOLS] option in VistA.

1. Log in to VistA.
2. At the "Select OPTION NAME:" prompt, type XPAR MENU TOOLS and then press Enter.
3. At the "Select General Parameter Tools Option:" prompt, type EP and then press Enter.
4. At the "Select PARAMETER DEFINITION NAME:" prompt, type PSS BUPRENORPHINE PAIN VAPRODS and then press Enter.
5. At the "Select Sequence:" prompt, type the sequence number and then press Enter.

Patch PSS*1*247 automatically populuated these products in XPAR “PSS BUPRENORPHINE PAIN VAPRODS” at the Package level during installation:

BUPRENORPHINE 10MCG/HR PATCH

BUPRENORPHINE 15MCG/HR PATCH

BUPRENORPHINE 20MCG/HR PATCH

BUPRENORPHINE 5MCG/HR PATCH

BUPRENORPHINE 7.5MCG/HR PATCH

BUPRENORPHINE 150MCG FILM,BUCCAL

BUPRENORPHINE 300MCG FILM,BUCCAL

BUPRENORPHINE 450MCG FILM,BUCCAL

BUPRENORPHINE 600MCG FILM,BUCCAL

BUPRENORPHINE 750MCG FILM,BUCCAL

BUPRENORPHINE 75MCG FILM,BUCCAL

BUPRENORPHINE 900MCG FILM,BUCCAL

### Routines

The following routines are used by the Pharmacy Data Management package.

- PSS0052
- PSS0093
- PSS0114
- PSS102RP
- PSS117EN
- PSS117PO
- PSS127PI
- PSS127PT
- PSS129EN
- PSS147EN
- PSS147PO
- PSS160EN
- PSS160PO
- PSS164P
- PSS172PO
- PSS1P178
- PSS1P201
- PSS1P23
- PSS1P43
- PSS208P
- PSS211PO
- PSS219PO
- PSS32P3
- PSS32P5
- PSS50
- PSS50A
- PSS50A1
- PSS50AQM
- PSS50ATC
- PSS50B
- PSS50B1
- PSS50B2
- PSS50C
- PSS50C1
- PSS50CMP
- PSS50D
- PSS50DAT
- PSS50DOS
- PSS50E
- PSS50F
- PSS50F1
- PSS50LAB
- PSS50NDF
- PSS50P4
- PSS50P66
- PSS50P7
- PSS50P7A
- PSS50TMP
- PSS50WS
- PSS51
- PSS51P1
- PSS51P15
- PSS51P1A
- PSS51P1B
- PSS51P1C
- PSS51P2
- PSS51P5
- PSS52P6
- PSS52P6A
- PSS52P6B
- PSS52P7
- PSS52P7A
- PSS54
- PSS55
- PSS551
- PSS55MIS
- PSS59P7
- PSS70UTL
- PSS781
- PSS90PI
- PSSADDIT
- PSSADRPT
- PSSAUTL
- PSSBPSUT
- PSSCHENV
- PSSCKOS
- PSSCLDRG
- PSSCLINR
- PSSCLOZ
- PSSCMOPE
- PSSCOMMN
- PSSCPRS
- PSSCPRS1
- PSSCREAT
- PSSCSPD
- PSSCUSRQ
- PSSDACS
- PSSDAWUT
- PSSDDUT
- PSSDDUT2
- PSSDDUT3
- PSSDEE
- PSSDEE1
- PSSDEE2
- PSSDEEA
- PSSDELOI
- PSSDENT
- PSSDFEE
- PSSDGUPD
- PSSDI
- PSSDIN
- PSSDINT
- PSSDIUTL
- PSSDIUTX
- PSSDOS
- PSSDOSED
- PSSDOSER
- PSSDOSLZ
- PSSDOSRP
- PSSDRDO2
- PSSDRDOS
- PSSDRINT
- PSSDSAPA
- PSSDSAPD
- PSSDSAPI
- PSSDSAPK
- PSSDSAPL
- PSSDSAPM
- PSSDSBBP
- PSSDSBDA
- PSSDSBDB
- PSSDSBPA
- PSSDSBPB
- PSSDSBPC
- PSSDSBPD
- PSSDSDAT
- PSSDSEXC
- PSSDSEXD
- PSSDSEXE
- PSSDSEXF
- PSSDSFDB
- PSSDSONF
- PSSDSPON
- PSSDSPOP
- PSSDSUTA
- PSSDSUTL
- PSSDTR
- PSSDVEN
- PSSEC119
- PSSEC123
- PSSENV
- PSSENVN
- PSSFDBDI
- PSSFDBRT
- PSSFIL
- PSSFILED
- PSSFILES
- PSSGENM
- PSSGIU
- PSSGMI
- PSSGS0
- PSSGSGUI
- PSSGSH
- PSSHELP
- PSSHFREQ
- PSSHL1
- PSSHLDFS
- PSSHLSCH
- PSSHLU
- PSSHRCOM
- PSSHRENV
- PSSHREQ
- PSSHRHAI
- PSSHRIT
- PSSHRPST
- PSSHRQ2
- PSSHRQ21
- PSSHRQ22
- PSSHRQ23
- PSSHRQ24
- PSSHRQ25
- PSSHRQ2D
- PSSHRQ2O
- PSSHRVAL
- PSSHRVL1
- PSSHTTP
- PSSHUIDG
- PSSIIRPT
- PSSINSTR
- PSSJEEU
- PSSJORDF
- PSSJSPU
- PSSJSPU0
- PSSJSV
- PSSJSV0
- PSSJXR
- PSSJXR1
- PSSJXR10
- PSSJXR11
- PSSJXR12
- PSSJXR13
- PSSJXR14
- PSSJXR15
- PSSJXR16
- PSSJXR17
- PSSJXR18
- PSSJXR19
- PSSJXR2
- PSSJXR20
- PSSJXR21
- PSSJXR22
- PSSJXR23
- PSSJXR24
- PSSJXR25
- PSSJXR26
- PSSJXR27
- PSSJXR28
- PSSJXR29
- PSSJXR3
- PSSJXR30
- PSSJXR31
- PSSJXR32
- PSSJXR33
- PSSJXR34
- PSSJXR35
- PSSJXR36
- PSSJXR37
- PSSJXR38
- PSSJXR39
- PSSJXR4
- PSSJXR40
- PSSJXR41
- PSSJXR42
- PSSJXR5
- PSSJXR6
- PSSJXR7
- PSSJXR8
- PSSJXR9
- PSSLAB
- PSSLDALL
- PSSLDEDT
- PSSLDOSE
- PSSLOCK
- PSSLOOK
- PSSMARK
- PSSMATCH
- PSSMEDCH
- PSSMEDRQ
- PSSMEDRT
- PSSMEDX
- PSSMIRPT
- PSSMONT
- PSSMRRDG
- PSSMRRI
- PSSMRTUP
- PSSMRTUX
- PSSMSTR
- PSSNCPDP
- PSSNDCUT
- PSSNDCUT2
- PSSNDSU
- PSSNFI
- PSSNFIP
- PSSNOD2
- PSSNOUNR
- PSSOAS
- PSSOICT
- PSSOICT1
- PSSOIDOS
- PSSOPKI
- PSSOPKI1
- PSSORPH
- PSSORPH1
- PSSORPHZ
- PSSORUTE
- PSSORUTL
- PSSORUTZ
- PSSOUTSC
- PSSP110
- PSSP130
- PSSP134
- PSSP170
- PSSP191A
- PSSP194
- PSSPI89
- PSSPKIPI
- PSSPKIPR
- PSSPNSRP
- PSSPO129
- PSSPOI
- PSSPOIC
- PSSPOID1
- PSSPOID2
- PSSPOID3
- PSSPOIDT
- PSSPOIKA
- PSSPOIM
- PSSPOIM1
- PSSPOIM2
- PSSPOIM3
- PSSPOIMN
- PSSPOIMO
- PSSPOIMP
- PSSPOST2
- PSSPOST5
- PSSPOST6
- PSSPRE38
- PSSPRETR
- PSSPRICE
- PSSPRMIX
- PSSPRUTL
- PSSQOC
- PSSQORD
- PSSREF
- PSSREMCH
- PSSRXACT
- PSSSCHED
- PSSSCHMS
- PSSSCHRP
- PSSSEE
- PSSSOLI1
- PSSSOLIT
- PSSSPD
- PSSSUTIL
- PSSSXRD
- PSSSYN
- PSSTRENG
- PSSTXT
- PSSUNMSI
- PSSUTIL
- PSSUTIL1
- PSSUTIL3
- PSSUTLA1
- PSSUTLA2
- PSSUTLAZ
- PSSUTLPR
- PSSUTLPZ
- PSSVIDRG
- PSSVX6
- PSSVX61
- PSSVX62
- PSSVX63
- PSSVX64
- PSSVX65
- PSSVX66
- PSSWMAP
- PSSWRNA
- PSSWRNB
- PSSWRNC
- PSSWRNE
- PSSXDIC
- PSSXRF1
- PSSYSP

### Exported Options

#### Stand-Alone Options

The following is a list of all stand-alone options that are **NOT** exported as part of the main PDM menu [PSS MGR]:

*Other Language Translation Setup*

[PSS OTHER LANGUAGE SETUP]

*Drug Inquiry (IV)*

[PSSJI DRUG INQUIRY]

*Electrolyte File (IV)*

[PSSJI ELECTROLYTE FILE]

*Enable/Disable Vendor Database Link*

[PSS ENABLE/DISABLE DB LINK]

*Add Default Med Route*

[PSS ADD DEFAULT MED ROUTE]

*Find Unmapped Local Possible Dosages*

[PSS LOCAL DOSAGES EDIT ALL]

<!-- image -->

The *Enable/Disable Vendor Database Link* option exists **ONLY** as a way for technical personnel to turn on/off the database connection if required for debugging. Normally, it is enabled and the Vendor Database updates are performed centrally on the MOCHA Servers, not at the individual sites. It is **NOT** exported as part of the main PDM menu [PSS MGR].

In the rare case where this option is used and the database link is disabled, NO drug-drug interaction, duplicate therapy, or dosing order checks will be performed in Pharmacy or in the Computerized Patient Record System (CPRS).

### Protocols

NAME: PSS EXT MFU CLIENT 
DESCRIPTION: This protocol will be used as the ACK from the external interface for a MFN\_M01 message.

NAME: PSS EXT MFU SERVER 
DESCRIPTION: This protocol will be used to send event notification and data when new drugs are added to the DRUG file (#50) and when certain fields are  updated in the same file. This information will be sent to the automated  dispensing machines through HL7 V.2.4 formatted messages.

NAME: PSS HUI DRUG UPDATE 
DESCRIPTION: This protocol will be used to send event notification and data when new drugs are added to the Drug file (#50) and when certain fields are  updated in same file.

NAME: PSS MED ROUTE RECEIVE
DESCRIPTION: This protocol processes updates to the Standard Medication Routes (#51.23) File.

### Bulletins

NAME: PSS FDB INTERFACE

SUBJECT: ORDER CHECK DATABASE DOWN

RETENTION DAYS: 3

PRIORITY?: YES

NAME: PSS FDB INTERFACE RESTORED

SUBJECT: ORDER CHECK DATABASE IS BACK UP

RETENTION DAYS: 3

PRIORITY?: YES

### Web Servers

PEPS

### Web Services

DOSING\_INFO

DRUG\_INFO

ORDER\_CHECKS

### Cache Class

XMLHandler

### HL7 Messaging with an External System

A protocol, PSS HUI DRUG UPDATE, is exported and has been created to generate HL7 messages when new drugs are added to the DRUG file (#50) and existing entries are updated. This protocol is exported with the text “DELETE ONLY TO SEND DRUG UPDATE MESSAGES” in the DISABLE field (#2) of the PROTOCOL file (#101). To activate the sending of these HL7 messages, the text from the DISABLE field (#2) of the PROTOCOL file (#101) must be deleted and at least one receiving protocol added as a subscriber. The drug data elements included in the HL7 message are defined in the following HL7 Drug Message Segment Definition table.

#### HL7 Drug Message Segment Definition Table

When the PSS HUI DRUG UPDATE protocol is enabled, the following table defines the data elements sent in each segment of the HL7 drug message.

Table 1: HL7 Drug Message Segment Definition Table

| Segment     |   Piece | Field Name                    | HL7 TBL # or Data Type   | Description                                    |
|-------------|---------|-------------------------------|--------------------------|------------------------------------------------|
| **MSH**     |       1 | &#124;                        | ST                       | Field Separator                                |
|             |       2 | ^~\&                          | ST                       | Encoding Characters                            |
|             |       3 | Pharmacy                      | No suggested value       | Sending Application                            |
|             |       9 | MFN                           | 0076                     | Message Type                                   |
| **MFI**     |       1 | 50^DRUG^99PSD                 | 0175                     | Master File ID                                 |
|             |       3 | UPD                           | 0178                     | File-Level Event Code                          |
|             |       6 | NE                            | 0179                     | Response Level Code                            |
| **MFA**     |       1 | MUP/MAD                       | 0180                     | UPDATE/ADD                                     |
| **MFE**     |       1 | MUP/MAD                       | 0180                     | UPDATE/ADD                                     |
|             |       4 | IEN^DRUG NAME^99PSD           |                          | File 50 Entry                                  |
| **ZPA**     |       1 | NDC                           | ST                       | National Drug Code                             |
|             |       2 | LOCAL NON-FORMULARY           | CE                       | If “1” true                                    |
|             |       3 | INACTIVE DATE                 | DT                       | HL7 Format (YYYYMMDD)                          |
|             |       4 | APPLICATION PACKAGE USE       | ST                       | Used by what packages                          |
|             |       5 | MESSAGE                       | ST                       | Info on drug                                   |
|             |       6 | VA CLASSIFICATION             | ST                       | VA Class                                       |
|             |       7 | DEA SPECIAL HDLG              | ST                       | How drug is dispense based on DEA codes        |
|             |       8 | FSN                           | ST                       | Federal Stock #                                |
|             |       9 | WARNING LABEL                 | ST                       | Drug Warnings for patient                      |
|             |      10 | VISN NON-FORMULAR             | CE                       | If ‘1’ true                                    |
| **ZPB**     |       1 | PHARMACY ORDERABLE ITEM       | CE                       | IEN^OI tied to dispense drug^PSD50.7           |
|             |       2 | DOSAGE FORM                   | ST                       | IEN^Dosage Form associated with OI^PSD50.606   |
|             |       3 | MEDICATION ROUTE              | ST                       | IEN^Med Route associated with OI^PSD51.2       |
|             |       4 | PSNDF VA PRODUCT NAME ENTRY   | CE                       | IEN^VA PRODUCT NAMES^PSD50.68                  |
|             |       5 | DISPENSE UNIT                 | ST                       | Dispense Unit for a drug                       |
|             |       6 | CMOP DISPENSE                 | CE                       | 1 or 0                                         |
|             |       7 | OP EXTERNAL DISPENSE          | CE                       | 1 or 0                                         |
|             |       8 | EXPIRATION DATE               | DT                       | HL7 Format (YYYYMMDD)                          |
|             |       9 | LAB TEST MONITOR              | CE                       | IEN^Lab Test^LAB60                             |
| **ZPC**     |       1 | SPECIMEN TYPE                 | CE                       | IEN^ SPECIMEN TYPE^LAB61                       |
|             |       2 | MONITOR ROUTINE               | ST                       | Program that runs to find lab test and results |
|             |       3 | LAB MONITOR MARK              | CE                       | If ‘1’ true                                    |
|             |       4 | STRENGTH                      | NM                       | Dose of drug                                   |
|             |       5 | UNIT                          | CE                       | IEN^Unit of measure^PSD50.607                  |
|             |       6 | PRICE PER ORDER UNIT          | NM                       |                                                |
|             |       7 | PRICE PER DISPENSE UNIT       | NM                       |                                                |
| **[{ZPD}]** |       1 | SYNONYM                       | ST                       | Trade Name                                     |
|             |       2 | NDC CODE                      | ST                       | National Drug Code                             |
|             |       3 | INTENDED USE                  | CE                       | CE^INTENTED USE                                |
|             |       4 | VSN                           | ST                       | Vendor Stock Number                            |
|             |       5 | ORDER UNIT                    | CE                       | IEN^ABBREVIATION^EXPANSION  ^PSD51.5           |
|             |       6 | PRICE PER ORDER UNIT          | NM                       |                                                |
|             |       7 | DISPENSE UNITS PER ORDER UNIT | NM                       |                                                |
|             |       8 | PRICE PER DISPENSE UNIT       | NM                       |                                                |
|             |       9 | VENDOR                        | ST                       | Vendor                                         |
| **[{ZPE}]** |       1 | ACTIVITY LOG                  | DT                       | HL7 Format YYYYMMDDHHMM[SS]-ZZZZ               |
|             |       2 | REASON                        | CE                       | E^EDIT                                         |
|             |       3 | INITIATOR OF ACTIVITY         | CE                       | IEN^NEW PERSON^VA200                           |
|             |       4 | FIELD EDITED                  | ST                       |                                                |
|             |       5 | NEW VALUE                     | ST                       |                                                |
|             |       6 | NDF UPDATE                    | ST                       |                                                |
| **[{ZPF}]** |       1 | DISPENSE UNITS PER DOSE       | NM                       |                                                |
|             |       2 | DOSE                          | NM                       |                                                |
|             |       3 | PACKAGE                       | CE                       | CE^PACKAGE(S)                                  |
|             |       4 | BCMA UNITS PER DOSE           | NM                       |                                                |
| **[{ZPG}]** |       1 | CLOZAPINE LAB TEST            | CE                       | IEN^LAB TEST^LAB60                             |
|             |       2 | MONITOR MAX DAYS              | NM                       |                                                |
|             |       3 | SPECIMEN TYPE                 | CE                       | IEN^ SPECIMEN TYPE^LAB61                       |
|             |       4 | TYPE OF TEST                  | CE                       | 1^WBC or 2^ANC                                 |
| **[{ZPH}]** |       1 | LOCAL POSSIBLE DOSAGE         | ST                       | FREE TEXT                                      |
|             |       2 | PACKAGE                       | CE                       | CE^PACKAGE(S)                                  |
|             |       3 | BCMA UNITS PER DOSE           | NM                       |                                                |

Two protocols, PSS EXT MFU CLIENT and PSS EXT MFU SERVER, are exported and have been created to generate HL7 messages when new drugs are added to the DRUG file (#50) and existing entries are updated. These protocols can only be activated by setting the following parameters in the OUTPATIENT SITE file (#59):

AUTOMATED DISPENSE field (#105) needs to be set to **2.4** .

ENABLE MASTER FILE UPDATE field (#105.2) needs to be set to **YES** .

LOGICAL LINK field (#2005) needs to be set to **PSO DISP** .

DISPENSE DNS NAME field (#2006) needs to be set to the dispensing system DNS name (for example, **dispensemachine1.vha.med.va.gov** ).

DISPENSE DNS PORT field (#2007) needs to be set to the dispensing system port number.

**Specific Transaction**

The Pharmacy/Treatment Encoded Order Message is as follows:

MFN	Master File Notification Message

MSH	Message Header

MFI	Master File Identifier

{MFE	Master File Entry

{{ZPA}	Drug File Information

{RXD}	Pharmacy/Treatment Dispense

{OBR}}	Observation Request

}

**Example:**

MSH|~^\&amp;|PSS VISTA|521~FO-BIRM.VHA.MED.VA.GOV~DNS|PSS DISPENSE|~DISPENSE1.VHA.MED.VA.GOV:9300~DNS|20030701||MFN~M01~MFN\_M01|10001|P|2.4|||AL|AL

MFI|50~DRUG~99PSD||UPD|||NE

MFE|MUP|||PROPANTHELINE 15MG TAB

ZPA|PROPANTHELINE 15MG TAB|N|LFN~Local Non-Formulary~Pharm Formulary Listing|20031226|Take with food|DE200|6|P|50~6505-00-960-8383~LPS50|8~NO ALCOHOL~LPS54|229~Bacitracin~LPSD50.7|3~CAP,ORAL~LPSD50.606|15~IV PUSH~LPSD51.2|3643~ATROPINE SO4 0.4MG TAB~LPSD50.68|OP~OP Dispense~99OP|20030830|9~Rubella~LLAB60|72~Hair of Scalp~LLAB61|PSOCLO1|N|100|20~MG~LPSD50.607|4.28&amp;USD~UP|15.64&amp;USD~UP|TAB|2|BLUE HOUSE VENDOR|0010-0501-33|TRADENAME

RXD||||1|||||1|||~P&amp;200&amp;LPSD50.0903||||||||||||O

OBR||||1102~ACETAZOLAMIDE~LLAB60|||||||||||70&amp;NECK&amp;LLAB61|||||||||WBC|||7

#### HL7 Drug Message Segment Definition Table

When the PSS EXT MFU SERVER protocol is enabled, the following table defines the data elements sent in each segment of the HL7 drug message.

Table 2: Segments Used in the Master File Update Message

| SEGMENT   |   SEQ# |   LEN | DT     | R/O   |   RP/# |   TBL# | ELEMENT NAME                                                 | EXAMPLE                                         |
|-----------|--------|-------|--------|-------|--------|--------|--------------------------------------------------------------|-------------------------------------------------|
| MSH       |      1 |     1 | ST     | R     |        |        | Field Separator                                              | &#124;                                          |
| MSH       |      2 |     4 | ST     | R     |        |        | Encoding Characters                                          | ~^\&                                            |
| MSH       |      3 |   180 | HD     | R     |        |   0361 | Sending Application                                          | PSS VISTA                                       |
| MSH       |      4 |   180 | HD     | R     |        |   0362 | Sending Facility – station ID and station DNS name           | 521~FO-BIRM.MED.VA.GOV~DNS                      |
| MSH       |      5 |   180 | HD     | R     |        |   0361 | Receiving Application                                        | PSS DISPENSE                                    |
| MSH       |      6 |   180 | HD     | R     |        |   0362 | Receiving Facility – DNS name and port of dispensing machine | ~DISPENSE.VHA.MED.VA.GOV:9300~DNS               |
| MSH       |      7 |    26 | TS     |       |        |        | Date/Time of Message                                         | 20040405152416                                  |
| MSH       |      9 |    15 | CM     | R     |   0076 |        | Message Type                                                 | MFN_M01                                         |
| MSH       |     10 |    20 | ST     | R     |        |        | Message Control ID                                           | 10001                                           |
| MSH       |     11 |     3 | PT     | R     |   0103 |        | Processing ID                                                | P                                               |
| MSH       |     12 |     3 | VID    | R     |   0104 |        | Version ID                                                   | 2.4                                             |
| MSH       |     15 |     2 | ID     |       |        |   0155 | Accept Ack. Type                                             | AL                                              |
| MSH       |     16 |     2 | ID     |       |        |   0155 | Application Ack Type                                         | AL                                              |
| MFI       |      1 |   250 | CE     | R     |        |   0175 | Master File Identifier                                       | 50^DRUG^99PSD                                   |
| MFI       |      3 |     3 | ID     | R     |        |   0178 | File-Level Event Code                                        | UPD                                             |
| MFI       |      6 |     2 | ID     | R     |        |   0179 | Response Level Code                                          | NE                                              |
| MFE       |      1 |     3 | ID     | R     |        |   0180 | Record-Level Event Code                                      | MUP                                             |
| MFE       |      4 |   200 | Varies | R     |        |        | Primary Key Value – MFE                                      | PROPANTHELINE 15MG TAB                          |
| ZPA       |      1 |   200 | Varies | R     |        |        | Primary Key Value – ZPA                                      | PROPANTHELINE 15MG TAB                          |
| ZPA       |      2 |     1 | ID     | R     |        |   0136 | Is Synonym                                                   | N                                               |
| ZPA       |      3 |   200 | CE     | R     |        |        | Formulary Listing                                            | LFN~Local Non-Formulary~Pharm Formulary Listing |
| ZPA       |      4 |    10 | DT     | O     |        |        | Inactive Date                                                | 20031226                                        |
| ZPA       |      5 |   200 | ST     | O     |        |        | Drug Message                                                 | Take with Food                                  |
| ZPA       |      6 |    30 | ST     | O     |        |        | Drug Classification                                          | DE200                                           |
| ZPA       |      7 |    10 | ST     | O     |        |        | DEA-Schedule Code                                            | 6                                               |
| ZPA       |      8 |     1 | ST     | O     |        |        | DEA-Drug Type                                                | P                                               |
| ZPA       |      9 |   100 | CE     | R     |        |        | Stock Number                                                 | 50~6505-00-960-8383~LPS50                       |
| ZPA       |     10 |   100 | CE     | O     |        |        | Warning Label                                                | 8~NO ALCOHOL~LPS54                              |
| ZPA       |     11 |   100 | CE     | O     |        |        | Pharmacy Orderable Item                                      | 229~Bacitracin~LPSD50.7                         |
| ZPA       |     12 |   100 | CE     | O     |        |        | Dosage Form                                                  | 3~CAP,ORAL~LPSD50.606                           |
| ZPA       |     13 |   100 | CE     | O     |        |        | Medication Route                                             | 15~IV PUSH~LPSD51.2                             |
| ZPA       |     14 |   100 | CE     | O     |        |        | Drug Name Identifiers                                        | 3643~ATROPINE SO4 0.4MG TAB~LPSD50.68           |
| ZPA       |     15 |   100 | CE     | O     |        |        | Dispense Flags                                               | OP~OP Dispense~99OP                             |
| ZPA       |     16 |    15 | DT     | O     |        |        | Drug Expiration Date                                         | 20030830                                        |
| ZPA       |     17 |   100 | CE     | O     |        |        | Lab Test Monitor                                             | 9~Rubella~LLAB60                                |
| ZPA       |     18 |   100 | CE     | O     |        |        | Specimen Type                                                | 72~Hair of Scalp~LLAB61                         |
| ZPA       |     19 |    10 | CE     | O     |        |        | Monitor Routine                                              | PSOCLO1                                         |
| ZPA       |     20 |     1 | ID     | O     |        |        | Lab Monitor Mark                                             | N                                               |
| ZPA       |     21 |    50 | NM     | O     |        |        | Strength                                                     | 100                                             |
| ZPA       |     22 |   250 | CE     | R     |        |        | Unit                                                         | 20~MG~LPSD50.607                                |
| ZPA       |     23 |    50 | CP     | R     |        |        | Price Per Order Unit                                         | 4.28&USD~UP                                     |
| ZPA       |     24 |    50 | CP     | R     |        |        | Price Per Dispense Unit                                      | 15.64&USD~UP                                    |
| ZPA       |     25 |    25 | ST     | O     |        |        | Dispense Unit                                                | TAB                                             |
| ZPA       |     26 |    50 | NM     | O     |        |        | Dispense Units Per Order Unit                                | 2                                               |
| ZPA       |     27 |    50 | ST     | O     |        |        | Vendor                                                       | BLUE HOUSE VENDOR                               |
| ZPA       |     28 |    12 | ST     | O     |        |        | NDC Code                                                     | 0010-0501-33                                    |
| ZPA       |     29 |    25 | ST     | O     |        |        | Intended Use                                                 | TRADE NAME                                      |
| RXD       |      4 |    20 | NM     | R     |        |        | Actual Dispense Amount                                       | 1                                               |
| RXD       |      8 |    20 | NM     | R     |        |        | Dispense Notes                                               | 1                                               |
| RXD       |     12 |    10 | CQ     | O     |        |        | Total Daily Dose                                             | ~P&200&LPSD50.0903                              |
| RXD       |     24 |     2 | ID     | R     |        |        | Dispense Package Method                                      | O                                               |
| OBR       |      4 |   250 | CE     | O     |        |        | Universal Service Identifier                                 | 1102~ACETAZOLAMIDE~LLAB60                       |
| OBR       |     15 |   300 | CM     | O     |        |        | Specimen Source                                              | 70&NECK&LLAB61                                  |
| OBR       |     24 |     3 | ID     | R     |        |        | Diagnostic Serv Sect ID                                      | WBC                                             |
| OBR       |     27 |   200 | TQ     | O     |        |        | Quantity/Timing                                              | 7                                               |

Notes Pertaining to Some of the Data Elements:

[MSH-3] Sending Application is the station ID along with the DNS name of the sending facility.

[MSH-5] Receiving Application is the DNS name and DNS port number of the dispensing application.

[MSH-10] Message Control ID is the number that uniquely identifies the message. It is returned in MSA-2 of the dispense completion message.

[MFI-1] Master File Identifier is hard-coded to 50~DRUG~99PSD.

[MFE-1] Record-Level Event Code can be either MUP for Update or MAD for Add.

[MFE-4] Primary Key Value – MFE is the GENERIC NAME field (#.01) from the DRUG file (#50).

[ZPA-1] Primary Key Value – ZPA will be the generic name of the drug first and then all synonyms will follow in consecutive ZPA segments.

[ZPA-2] Is Synonym is set to Y or N depending on whether the primary key is a synonym.

[ZPA-3] Formulary Listing will contain LFN and/or VISN is the formulary is not to appear on the Local or VISN formulary.

[ZPA-9] Stock Number is the FSN field (#6) from the DRUG file (#50) or the VSN field (#400) from the SYNONYM subfile (#50.1) of the PRESCRIPTION file (#50).

[ZPA-15] Dispense Flags will indicate if this drug may be dispensed to an external interface and if it is marked to be dispensed at a Consolidated Outpatient Pharmacy (CMOP). If both are yes, the answer would be OP~OP Dispense~Pharm dispense^CMOP~CMOP dispense~Pharm dispense flag.

[ZPA-29] Intended User will be TRADE NAME, QUICK CODE, DRUG ACCOUNTABILITY or CONTROLLED SUBSTANCES.

[RXD-4] Actual Dispense Amount is the BCMA UNITS PER DOSE field (#3) from the POSSIBLE DOSAGES file (#50.0903).

[RXD-9] Dispense Notes is the DISPENSE UNITS PER DOSE field (#.01) from the POSSIBLE DOSAGES file (#50.0903).

[RXD-12] Total Daily Dose will be either P for Possible Dosages or LP for Local Possible Dosages.

[OBR-4] Universal Service Identifier is used for Clozapine Lab Test.

[OBR-15] Specimen Source is used for Clozapine Specimen Type.

[OBR-24] Diagnostic Serv Sect ID is used for Clozapine Type of Test.

[OBR-27] Quantity/Timing is used to encode Monitor Max days from the CLOZAPINE LAB TEST file (#50.02).

### Data Archiving and Purging

There are no archiving and purging functions necessary with this release of the PDM package.

### Callable Routines / Entry Points / Application Program Interfaces (APIs)

APIs, callable routines, and entry points can be viewed by first choosing the *DBA* menu option on FORUM and then choosing the *Integration Agreement* s *Menu* option:

IAs INTEGRATION CONTROL REGISTRATIONS ...

For detailed information on all supported Pharmacy Data Management APIs, see the *Pharmacy Re-Engineering (PRE) Application Program Interface (API) Manual* posted on the VistA Documentation Library (VDL).

### Medication Routes

The following paragraphs provide an explanation of medication route information.

**For Outpatient Pharmacy &amp; Inpatient Medication Unit Dose Orders** :

The Default med route will be returned from the DEFAULT MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) if it is populated, or from the POSSIBLE MED ROUTES multiple (#50.711) of the PHARMACY ORDERABLE ITEM file (#50.7) if it is populated with a single entry and the USE DOSAGE FORM MED ROUTE LIST field (#10) is set to "NO." The med route selection list will be returned with entries from the POSSIBLE MED ROUTES multiple (#50.711) if the USE DOSAGE FORM MED ROUTE LIST field (#10) is set to "NO." Otherwise, the med routes associated with the orderable item's dosage form, MED ROUTE FOR DOSAGE FORM multiple (#50.6061) of the DOSAGE FORM file (#50.606), will be returned.

**For IV Fluids Orders** :

If there is only one orderable item in the IV order request, the same logic as defined above under ‘For Outpatient Pharmacy &amp; Inpatient Medication Unit Dose Orders’ will be used to return the default med route from the DEFAULT MED ROUTE field (#.06) and the med route selection list from the PHARMACY ORDERABLE ITEM file (#50.7).

If there is more than one orderable item on the IV order request, the PHARMACY ORDERABLE ITEM file (#50.7) will be checked for each orderable item for the default med route and med route selection list as defined above under ‘For Outpatient Pharmacy &amp; Inpatient Medication Unit Dose Orders.’ If there is a default med route common with every orderable item, that default med route will be returned. Similarly, the list of possible med routes that are common with every orderable item will be returned.

### Administration Scheduling

The following rules apply to administration scheduling.

If there is a duplicate schedule, and if one of them contains ward-specific administration times for the ward location of the patient, the schedule returned for inclusion in the array of selectable schedules in CPRS will be the one with the ward-specific administration times.

If no duplicate has ward-specific administration times for the ward location of the patient, the schedule with the lowest IEN number will be returned. If both (or more than one) duplicate schedules have ward-specific administration times for the ward location of the patient, the schedule with the lowest IEN number in the ADMINISTRATION SCHEDULE file #51.1 will be the schedule in the array returned to CPRS.

### External Relations

**Integration Agreements**

IAs can be viewed by first choosing the *DBA* option on FORUM and then the *Integration Agreement* s *Menu* option.

**Example: DBA Option**

Select Primary Menu Option: DBA

Select DBA Option: INTEGration Agreements Menu

Select Integration Agreements Menu Option:  Custodial Package Menu

Select Custodial Package Menu Option:  ACTIVE by Custodial Package

Select PACKAGE NAME: PHARMACY DATA MANAGEMENT     PSS

DEVICE: HOME//

### Internal Relations

All PDM options can function independently.

### Package-Wide Variables

There are no package-wide variables for this version.

### Additional Information

#### Standards and Conventions Committee (SACC) Exemptions

The following PSS routines will generate errors reported in the XINDEX utility from using non-standard M syntax, due to the need to consume external web services.

PSSFDBDI

PSSFDBRT

PSSHRPST

PSSHTTP

The following waiver permits the use of this non-standard M syntax to allow the use of Cache features to consume external web services. This waiver is located in the HealtheVet Web Services Client (HWSC) Developer Guide.

Table 4: Waiver

| **OITIMB33554520 - Migration from M2J to VistA Web Services Client (VWSC)**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Keywords**                                                                  | M2J,VWSC,J2EE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Decision Date**                                                             | 12/1/2006                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Decision Type**                                                             | Architecture                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Decision Making Body**                                                      | HPMO CCB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Description**                                                               | On December 1, 2006, the HPMO Change Control Board voted to accept the migration of VistA from the current M2J solution to the VistA Web Services Client (VWSC). This decision was made for a number of reasons, in particular the fact that the existing 12-year-old M standard has been surpassed by evolving technologies and can no longer address today’s requirements. Additionally, we are no longer required to support DSM, previously the primary VistA/M hosting environment. Today, all sites are standardized on Caché 5.0 systems. As such, approvals were granted as follows: Waiver of the requirement to adhere to the existing 1995 M standard (that does not address the implementation of web services); Implementation of an industry standard such as web services for VistA/M to J2EE calls using Caché’s built in HTTP and web service client feature; Use of VWSC as an interim solution that ensures continuity of integration between VistA/M applications and migrated J2EE applications as HealtheVet evolves by enabling the consumption of external web services by legacy VistA applications; and Deprecation of the original M2J approach. |
| **Rationale**                                                                 | This architectural change allows for a number of improvements, including better scalability, resilience, and performance. Deployment and configuration is far less complicated for administrators, and the APIs can be used by a variety of clients rather than solely M-based. It also places responsibility for support, maintenance, etc. with the vendor rather than OI&T.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Record Type**                                                               | TDR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **State**                                                                     | Approved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Date Submitted**                                                            | 2/14/2007 8:37:24 AM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

**Supporting Documentation**

| Link     | Document Title                                                            | Description                                               | Date      |
|----------|---------------------------------------------------------------------------|-----------------------------------------------------------|-----------|
| Download | Migration from M2J to VistA Web Services Client (VWSC) Email Notification | Email notification alerting of the decision               | 2/13/2007 |
| Download | VWSC Architecture                                                         | Proposed architecture view of VWSC                        | 12/1/2006 |
| Download | VWSC Proposed View                                                        | Proposed logical view of VistA Web Services Client (VWSC) | 12/1/2006 |

#### Cross-Reference Logic to Keep Orderable Items Up To Date

With the introduction of PSS*1*38, a new process for keeping Orderable Items updated was implemented. The process is explained in detail in the section below.

Anytime specific fields are edited, or a pointer to the PHARMACY ORDERABLE ITEM file (#50.7) changes, the Orderable Item (OI) must be updated and sent to CPRS. Two different situations can precipitate these changes. Both situations are explained in detail here.

The first situation occurs when a field is edited that can possibly affect the status of the Orderable Item, but no Orderable Item pointers change. In this situation, the old Orderable Item is the same as the new Orderable Item. In these cases, the kill logic will be the same as the set logic. The kill and set logic will simply pass in the Orderable Item to the routine that checks all IV Additives/IV Solutions/Dispense Drugs matched to the Orderable Item, does all the necessary updates (Inactivation date, Supply flag, Non-formulary, Base, Additive), and then sends the Master File Update to CPRS on that Orderable Item. This type of update occurs when the fields listed below are edited.

File 50: DEA Special Hdlg

File 50: Inactivation Date

File 50: Application Packages’ Use

File 50: Local Non-Formulary

File 50.7: Inactivation Date

File 52.6: Inactivation Date

File 52.6: Used in IV Fluid Order Entry

File 52.7: Inactivation Date

File 52.7: Used in IV Fluid Order Entry

The second situation occurs when pointers to the PHARMACY ORDERABLE ITEM file (#50.7) are changed. IV Additives, IV Solutions and the Dispense Drug always point to the same Orderable Item. That Orderable Item is, in turn, pointed to by the IV Additive or IV Solution. So, the fields that may be affected include the Orderable Item pointer in the DRUG file (#50) and the Generic Drug pointer in the IV ADDITIVES file (#52.6) and the IV SOLUTIONS file (#52.7).

File 50: Orderable Item Pointer

File 52.6: Generic Drug Pointer

File 52.7: Generic Drug Pointer

The initial change is to make the Orderable Item pointers in the IV ADDITIVES file (#52.6) and the IV SOLUTIONS file (#52.7) uneditable. The software will now control those pointers.

**Scenario 1: The Orderable Item Pointer Is Changed For A Dispense Drug**

In Example 1, the Orderable Item pointer is changed for a Dispense Drug. In this case, any Orderable Item pointers must be updated for entries in the IV ADDITIVES file (#52.6) and the IV SOLUTIONS file (#52.7) that point to that Dispense Drug. After these pointers have been updated, the Orderable Item must be updated for the old Orderable Item with what will point to it after the matching. The Orderable Item must also be updated for the new Orderable Item after the matching. And these pharmacy Orderable Item updates must be sent to CPRS as part of the Master File Update. To accomplish this, the following steps must be completed:

1. Add a Cross-Reference on the Orderable Item pointer in the DRUG file (#50) that will hard set one Cross-Reference in the ORDERABLE ITEM file (#50.7) and two Cross-References in the DRUG file (#50) as follows.

Orderable Item:	^PS(50.7,"A50",Orderable Item IEN, Dispense Drug IEN)=""

Drug file:	^PSDRUG("A526", Dispense Drug IEN, Additive IEN,)=""

Drug file:	^PSDRUG("A527", Dispense Drug IEN, Solution IEN,)=""

The Orderable Item Cross-Reference allows access to Dispense Drugs matched to an Orderable Item.  The two DRUG file (#50) Cross-References allow access to Solutions and Additives linked to Dispense Drugs. An "A50" Cross-Reference will also be added on the NAME field (# .01) of the PHARMACY ORDERABLE ITEM file (#50.7) containing a "Quit" command for the set and kill logic for documentation purposes only.

When the Orderable Item pointer of a Dispense Drug changes, only one Cross-Reference is needed on that field to perform the following actions:

**Kill Logic:** This command performs a hard kill of the "A50" Cross-Reference in the PHARMACY ORDERABLE ITEM file (#50.7) for that Dispense Drug using old value (X) and DA, where X equals the OI IEN and DA equals the Dispense Drug IEN. The two DRUG file (#50) Cross-References will not change.

After the hard kill is completed, a Master File Update is performed for the old Orderable Item. The logic for all Dispense Drugs/IV Additives/IV Solutions matched to the Orderable item is executed by looping the three Cross-References to find all entries in all three files matched to the Orderable Item. Also in the Kill logic, the Orderable Item pointer is set to null and the Orderable Item pointer Cross-Reference is killed for any IV Additives or IV Solutions matched to the Dispense Drug.

**Set Logic:** Using the New Value (X), where X equals the OI IEN, the "A50" Cross-Reference is hard set in the PHARMACY ORDERABLE ITEM file (#50.7). The Master File Update is then performed for the new Orderable Item. The logic for all Dispense Drugs/IV Additives/IV Solutions matched to the Orderable Item is executed by looping on the three Cross-References to find all entries in all three files matched to the Orderable Item. The Orderable Item pointer and the Orderable Item pointer Cross-References are then hard set for all IV Additives and IV Solutions that have been matched to the Dispense Drug with new value (X).

**Example 1:**

**Additives/Solution	Dispense Drugs:	Orderable Item:**

IEN 3 	points to =&gt;	IEN 100	points to =&gt;	500

IEN 4	points to =&gt;	IEN 100	points to =&gt;	500

IEN 5	points to =&gt; 	IEN 100	points to =&gt;	500

IEN 10 	points to =&gt;	IEN 200	points to =&gt;	500

**Cross-References are:** ^PS(50.7,"A50",500,100)=""

^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,3)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

Orderable Item 500 is pointed to by Dispense Drugs 100 and 200, and by IV Additives 3, 4, and 5, and IV Solution 10.

(If the LOCAL NON-FORMULARY field (#51) in the DRUG file (#50) is edited, the software will obtain the OI pointer 500 and execute the OI logic by looping on 500 in the "A50" Cross-Reference of the PHARMACY ORDERABLE ITEM file (#50.7). As it references each entry, the OI logic is executed by looping on the “A526” and “A527” Cross-references on the DRUG file (#50) before going to the next Orderable Item pointer in the "A50" Cross-reference in the PHARMACY ORDERABLE ITEM file (#50.7). For Example 1 above, the software will find in the first "A50" Cross-Reference for OI 500, Dispense Drug 100. The software will then loop through all the “A526” and “A527” Cross-References in the DRUG file (#50) to find the IV Additives 3, 4 and 5. In the second “A50” Cross-Reference for OI 500, Dispense Drug 200 is identified.  The software will again loop through any existing “A526” and “A527” Cross-references in the DRUG file (#50) to find IV Solution 10.

If the Orderable Item pointer for Dispense Drug 100 is edited from 500 to 600, the Cross-Reference in the DRUG file (#50) the following logic will be performed.

**Kill Logic**

Kill the Cross-Reference ^PS(50.7,"A50",500,100) using DA and old value (X=500), where DA equals the IEN of the Dispense Drug and X equals the IEN of the Orderable Item

The Cross-References would now be as follows.

^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,3)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

The ‘A50” and “A527” Cross-references now identify Orderable Item 500 to be pointed to by Dispense Drug 200 and IV Solution 10. The Orderable Item update for OI 500 is then performed for Dispense Drug 200 and IV solution 10.

While still in the Kill logic, the PHARMACY ORDERABLE ITEM field (#15) in the IV ADDITIVES file (#52.6) is set to null for IV Additives 3, 4, and 5. This action results in the deletion of Cross-References on the PHARMACY ORDERABLE ITEM field (#15) of the IV ADDITIVES file (#52.6).

**Set Logic**

The “A50” Cross-Reference in the PHARMACY ORDERABLE ITEM file (#50.7) for the new Orderable Item 600 is set as follows.

^PS(50.7,"A50",500,200)=""

^PS(50.7,"A50",600,100)=""

^PSDRUG("A526",100,3)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

The Orderable Item logic is executed on the new OI 600 by looping on the "A50" Cross-Reference, to get the Dispense Drug pointer of 100. The software then loops through any existing “A526” and “A527” Cross-References to get IV Additives 3, 4 and 5.

The value of the PHARMACY ORDERABLE ITEM (#15) field in the IV ADDITIVES file (#52.6) for IV Additives 3, 4, and 5 is set to 600. Existing Cross-References are also set to reflect this change.

**Scenario 2: The Dispense Drug Pointer Is Edited For An IV Additive Or IV Solution**

If the Dispense Drug is changed for an IV Additive or IV Solution, the Cross-References on the PHARMACY ORDERABLE ITEM field in the IV ADDITIVES file (#52.6) and IV SOLUTION file (#52.7) will perform the following set and kill logic.

**Kill Logic**

First, the "A526" or "A527" Cross-References in the DRUG file (#50) will be killed. Then, using DA, which is equal to the Orderable Item IEN, the software will get the old Orderable Item pointer value and perform the Orderable Item logic on the old Orderable Item. Subsequently, the value in the PHARMACY ORDERABLE ITEM field for the IV Additive and/or IV Solution will be set to null and the existing Cross-References on this field will be killed.

**Set Logic**

First, the "A526" or "A527" Cross-References in the DRUG file (#50) will be set. Then Using X, which is equal to the Dispense Drug IEN, the software will identify the new Orderable Item in the DRUG file (#50) and perform the OI logic on that Orderable Item. The PHARMACY ORDERABLE ITEM field in the IV ADDITIVES file (#52.6) and IV SOLUTION file (#52.7) will be set to the new value and existing Cross-References will be also set.

<!-- image -->

Users can first check the new Dispense Drug, and if the Orderable Item does not change by rematching the Additive/Solution to the new Dispense Drug, they can choose the QUIT command.

**Example 2:**

**IV Additives/IV Solution	Dispense Drugs	Orderable Item**

IEN 3	points to =&gt;	IEN 100	points to =&gt;	500

IEN 4	points to =&gt;	IEN 100	points to =&gt;	500

IEN 5	points to =&gt;	IEN 100	points to =&gt;	500

IEN 10	points to =&gt;	IEN 200	points to =&gt;	500

**Cross-References** ^PS(50.7,"A50",500,100)=""

^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,3)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

For example, the USED IN IV FLUID ORDER ENTRY field (#17) in the IV ADDITIVES file (#52.6) for IV Additive 3 could be edited. The Orderable Item that the IV Additive points to in this case, is 500. Both the Kill and Set logic (same logic) for the OI 500 is updated by looping through the "A50" Cross-Reference in the PHARMACY ORDERABLE ITEM file (#50.7), finding each Dispense Drug IEN, and going through the "A526" and  "A527" Cross-References in the DRUG file (#50) for that Dispense Drug. This process is then repeated for the next Dispense drug identified in the “A50” Cross-Reference

If the DRUG file (#50) pointer for IV Additive 3 were changed from Dispense Drug 100 to Dispense Drug 900, the Cross-Reference on the Dispense Drug Pointer would be killed.

**Kill Logic**

Using old value of X, which equals the Dispense Drug 100 and DA, which equals the IV ADDITIVE 3, the software would kill Cross-Reference  ^PSDRUG("A526",100,3) with the following Cross-References remaining.

^PS(50.7,"A50",500,100)=""

^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

Using DA, the software would get the old Orderable Item pointer of 500 and execute the Orderable Item logic for Dispense Drugs 100, IV Additives 4 and 5, Dispense Drug 200, and IV Solution 10.

The value for the PHARMACY ORDERABLE ITEM field (#15) in the IV ADDITIVES file (#52.6) would be set to null and Cross-References on this field would be deleted.

**Set Logic**

Using new value X, where X equals the Dispense Drug 900, the software would set the new "A526" Cross Reference as ^PSDRUG("A526",900,3)="", The updated Cross-References are as follows

^PS(50.7,"A50",500,100)=""

^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A526",900,3)=""

^PSDRUG("A527",200,10)=""

Using new value of X, where X equals the Dispense Drug 900, the software gets the Orderable Item pointer for Dispense Drug 900, in this example, Orderable Item 2000. The applicable Cross-References would be the following.

^PS(50.7,"A50",500,100)=""

^PS(50.7,"A50",500,200)=""

^PS(50.7,"A50",2000,900)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A526",900,3)=""

^PSDRUG("A527",200,10)=""

The software performs the OI update for Orderable Item 2000, with Dispense Drug 900 and IV Additive 3. The PHARMACY ORDERABLE ITEM field (#15) value in the IV ADDITIVES file (#52.6) is set to 2000. The corresponding Cross-References on this field are also set.

### Mail Groups

Patch PSS*1*147 creates a new mail group called PSS ORDER CHECKS. The mail group description below was retrieved from VA FileMan. The IRM Pharmacy support and Pharmacy ADPACs (and backups) should at a minimum be added to this mail group.

**NAME: PSS ORDER CHECKS**

TYPE: public

DESCRIPTION:   Members of this mail group will receive various notifications

that impact Enhanced Order Checks (drug-drug interactions, duplicate therapy

and dosing checks) introduced with PRE V. 0.5 utilizing a COTS database.

Patch PSS*1*227 creates a new mail group called PSS DEE AUDIT. The mail group description below was retrieved from VA FileMan. This mail group should include anyone who should be notified when changes are made to the DRUG file (#50). For more information on this mail group, refer to the *Pharmacy Data Management Manager’s User Manual* .

**NAME: PSS DEE AUDIT**

TYPE: public

DESCRIPTION:   Members of this mail group will receive audit notifications

when certain fields are viewed or changed in the DRUG file (#50).

### Alerts

There are no alerts in the PDM package.

### Bulletins

Bulletins are 'Super' messages. Each Bulletin has a text and a subject just like a normal message. But embedded within either the subject or the text can be variable fields that can be filled in with parameters. There is also a standard set of recipients in the form of a Mail Group that is associated with the bulletin.

Bulletins are processed by MailMan either because of either a special type of cross reference or a direct call in a routine. The interface for the direct call is described in the documentation on programmer entry points. FileMan sets up code that will issue a bulletin automatically when the special cross reference type is created.  In either case the parameters that go into the text and/or the subject make each bulletin unique.

NAME: PSS FDB INTERFACE

SUBJECT: ORDER CHECK DATABASE DOWN

RETENTION DAYS: 3

PRIORITY?: YES

NAME: PSS FDB INTERFACE RESTORED

SUBJECT: ORDER CHECK DATABASE IS BACK UP

RETENTION DAYS: 3

PRIORITY?: YES

### Remote Systems

PDM does not transmit data to any remote system or facility.

### Archiving / Purging

There are no archiving and purging functions necessary with the PDM package.

### Contingency Planning

Sites utilizing the PDM package should develop a local contingency plan to be used in the event of product problems in a live environment. The facility contingency plan must identify the procedure for maintaining functionality provided by this package in the event of system outage. Field station Information Security Officers (ISOs) may obtain assistance from their Regional Information Security Officer (RISO).

### Interfacing

There are no specialized products embedded within or required by the PDM package.

### Electronic Signatures

No electronic signatures are utilized in the PDM package.

### Locked Menu Options

This section relates only to options that are locked. For a complete listing of The PDM options listed in the PSS MGR Menu structure, refer to the Menu/Options section of this document.

<!-- image -->

**Locked: PSXCMOPMGR**

Without the PSXCMOPMGR key the *CMOP Mark/Unmark (Single drug)* option will not appear on your menu.

### Security Keys

The PSS ORDER CHECKS security key is used to control access to the Enable/Disable Dosing Order Checks [PSS DOSING ORDER CHECKS] option.

In order to mark or edit package specific fields in a DRUG file (#50) entry, the user must hold the corresponding package key. The keys are assigned for the individual packages. PDM does not export any of these keys.

Table 5: Security Keys

| Package                                 | Keys       |
|-----------------------------------------|------------|
| Outpatient Pharmacy                     | PSORPH     |
| Inpatient Medications                   | PSJU MGR   |
| Inpatient Medications                   | PSJI MGR   |
| Automatic Replenishment/Ward Stock      | PSGWMGR    |
| Drug Accountability/Inventory Interface | PSAMGR     |
| Drug Accountability/Inventory Interface | PSA ORDERS |
| Controlled Substances                   | PSDMGR     |
| National Drug File                      | PSNMGR     |
| Consolidated Mail Outpatient Pharmacy   | PSXCMOPMGR |

Patch PSS*1*147 exports the following four security keys, that will be used by the Pharmacy Enterprise Customization System (PECS) application. Only a few users who will be granted access to the PECS application will need one or more keys assigned based on their role. Assignment of these keys should be by request only. The security key descriptions were retrieved from VA FileMan.

NAME: PSS\_CUSTOM\_TABLES\_ADMIN

DESCRIPTIVE NAME: ADMINISTRATOR

DESCRIPTION:  This key is used by the Pharmacy Enterprise Customization System (PECS) web application. Holders of this key will have the ability to perform configuration and administrative tasks for the application. They will also have querying capabilities.

NAME: PSS\_CUSTOM\_TABLES\_APPROVER

DESCRIPTIVE NAME: APPROVER

DESCRIPTION:  This key is used by the Pharmacy Enterprise Customization System (PECS) web application.  Holders of this key will have the same privileges as those with the PSS CUSTOM TABLES REQUESTOR key. Additional capabilities will be to review, approve, delete or reject customization requests and to view and generate reports.

NAME: PSS\_CUSTOM\_TABLES\_REL\_MAN

DESCRIPTIVE NAME: RELEASE MANAGER

DESCRIPTION:  This key is used by the Pharmacy Enterprise Customization System (PECS) web application. Holders of this key will have the ability to create file updates for FDB database tables to be applied at local facilities. They will also have querying capabilities.

NAME: PSS\_CUSTOM\_TABLES\_REQUESTOR

DESCRIPTIVE NAME: REQUESTOR

DESCRIPTION:  This key is used by the Pharmacy Enterprise Customization System (PECS) web application.  Holders of this key will be allowed to enter customization requests, display and view the status of their own requests. They will also have limited querying capabilities

Five security keys were introduced with Patch PSS*1*167 that will be used to authenticate users accessing the Pharmacy Product System-National (PPS-N) using Kernel Authentication and Authorization for J2EE (KAAJEE).  Users requiring access to the Pharmacy Product System-National should be assigned these keys as appropriate to their level of approved access.  PPS-N is a reengineered product that will replace the National Drug File Management System (NDFMS).  Site users may be assigned the PSS\_PPSN\_VIEWER key only.  The other four security keys are only to be assigned to members of the National NDF Management Group.

NAME: PSS\_PPSN\_MANAGER

DESCRIPTIVE NAME: PPS-National Manager

DESCRIPTION:   This role can perform the operational functions in PPS-N but doesn't have the administrative rights of the PPS-N National Supervisor.

NAME: PSS\_PPSN\_MIGRATOR

DESCRIPTIVE NAME: PPS-National Migration User

DESCRIPTION:   This role has the ability to run the PPS-N Migration.

NAME: PSS\_PPSN\_SECOND\_APPROVER

DESCRIPTIVE NAME: PPS-National Second Approver

DESCRIPTION:   This role has the ability to do a second approval on items that are in the pending second approval state.

NAME: PSS\_PPSN\_SUPERVISOR

DESCRIPTIVE NAME: PPS-National Supervisor

DESCRIPTION:   This role has the ability to perform all actions in the PPS-N application, including Administration and Configuration.

NAME: PSS\_PPSN\_VIEWER

DESCRIPTIVE NAME: PPS-National Viewer

DESCRIPTION:   This role has the ability to log in and view items in the PPS-N Application but cannot modify any of the items.

### File Security

Information about all files, including these, can be obtained by using the VA FileMan to generate a list of file attributes.

#### PDM Files

Table 6: PDM FIles

|   File Numbers | File Names                    | DD   | RD   | WR   | DEL   | LAYGO   |
|----------------|-------------------------------|------|------|------|-------|---------|
|         50     | DRUG                          | @    |      |      |       |         |
|         50.4   | DRUG ELECTROLYTES             | @    |      |      |       |         |
|         50.606 | DOSAGE FORM                   | @    |      | @    | @     | @       |
|         50.7   | PHARMACY ORDERABLE ITEM       | @    |      |      |       |         |
|         51     | MEDICATION INSTRUCTION        | @    |      |      |       |         |
|         51.1   | ADMINISTRATION SCHEDULE       | @    |      |      |       |         |
|         51.2   | MEDICATION ROUTES             | @    |      |      |       |         |
|         51.23  | STANDARD MEDICATION ROUTES    | @    | Pp   | @    | @     | @       |
|         51.24  | DOSE UNITS                    | @    | Pp   | @    | @     | @       |
|         51.25  | DOSE UNIT CONVERSION          | @    | Pp   | @    | @     | @       |
|         51.5   | ORDER UNIT                    |      |      |      |       |         |
|         51.7   | DRUG TEXT                     | @    |      |      |       |         |
|         52.6   | IV ADDITIVES                  | @    |      |      |       |         |
|         52.7   | IV SOLUTIONS                  | @    |      |      |       |         |
|         53.47  | INFUSION INSTRUCTIONS         |      |      |      |       |         |
|         54     | RX CONSULT                    |      |      |      |       |         |
|         55     | PHARMACY PATIENT (Partial DD) | @    | P    |      |       |         |
|         59.7   | PHARMACY SYSTEM               | ^    |      | ^    | ^     | ^       |
|         59.73  | VENDOR DISABLE/ENABLE         | @    | @    | @    | @     | @       |
|         59.74  | VENDOR INTERFACE DATA         | @    | @    | @    | @     | @       |

#### Non-PDM Files

Table 7: Non-PDM Files

|   File Numbers | File Names                       | DD   | RD   | WR   | DEL   | LAYGO   |
|----------------|----------------------------------|------|------|------|-------|---------|
|  200           | NEW PERSON (Partial DD)          | #    | #    | #    | #     | #       |
|    9.00903e+06 | APSP INTERVENTION TYPE           |      |      |      |       |         |
|    9.00903e+06 | APSP INTERVENTION                |      |      |      |       |         |
|    9.00903e+06 | APSP INTERVENTION RECOMMENDATION |      |      |      |       |         |

<!-- image -->

Please refer to the "Sending Security Codes." section of the Kernel V. 8.0 Systems Manual for more information concerning installation of security codes.

### References

There are no regulations or directives related to the Pharmacy Data Management package. Additional manuals related to the Pharmacy Data Management package can be found at the VistA Documentation Library (VDL) on the Internet.

### New Functionality

A new automated bidirectional interface between VistA and PADE has been designed and developed utilizing VIE as the middleware component for communication of HL7 messages and error handling.  The added functional components are:

Provide pharmacists the capability to remotely access dispensing equipment to provide the pharmacist the status of drugs:  whether they have been dispensed, or in the queue or some error condition that may have been encountered by the dispensing equipment.

Provide PADE the capability to transmit dispensing information to VistA Pharmacy to keep a perpetual inventory of all drugs/medications received, dispensed, and wasted.

Provide PADE the capability to alert VistA Pharmacy of medication removal from PADE without orders.

Establish monitors of all potentially inappropriate electronic pharmacy transactions.  Implement trending reports in order to address and detect potentially inappropriate pharmacy transactions, such as drug diversion.  For example, reports include the ability to sort transactions by nursing, user, drug, etc., and from the VA-side of the interface.

Refer to the following Pharmacy Interface Automation documents for additional information:

Pharmacy Interface Automation Installation Guide

Pharmacy Interface Automation User Guide

Pharmacy Interface Automation System Design Document

Pharmacy Interface Automation Data Dictionary

### Options and Build Components

The following are the options and build components for Pharmacy Interface Automation for PSS*1.0*193:

Select OPTION NAME:    XPD PRINT BUILD     Build File Print

Build File Print

Select BUILD NAME: PSS*1.0*193       PHARMACY DATA MANAGEMENT

DEVICE: HOME// ;;99999  SSH VIRTUAL TERMINAL

PACKAGE: PSS*1.0*193     Nov 25, 2015 10:27 am                           PAGE 1

-------------------------------------------------------------------------------SINGLE PACKAGE                               TRACK NATIONALLY: YES

NATIONAL PACKAGE: PHARMACY DATA MANAGEMENT       ALPHA/BETA TESTING: NO

As part of this patch PSS*1*193, the following enhancements were made:

1. Two new protocols PSS MFNM01 CLIENT and PSS MFNM01 SERVER were added to facilitate sending MFN HL7 drug messages to PADE.

The Send Entire Drug File to External Interface [PSS MASTER FILE ALL]  option was modified to allow transmission of the drug file to an Inpatient Interface (PADE) depending on the PADE setup. It also provides the flexibility of sending all drugs marked for Unit Dose, IV or Ward Stock or send selected drugs to PADE.

Since this option now allows to send all or selected drugs to PADE, the option name "Send Entire Drug File to External Interface" was changed   to "Send Drug File Entries to External Interface"

A new PSS PADE INIT security key was added so that holders of this key can only send "all" drugs to PADE noted in item 2.

Option Drug Enter/Edit [PSS DRUG ENTER/EDIT] was modified to send an addition/update/both or none to PADE provided it is setup to receive such updates.

ENVIRONMENT CHECK:                               DELETE ENV ROUTINE:

PRE-INIT ROUTINE:                          DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE:                         DELETE POST-INIT ROUTINE:

PRE-TRANSPORT RTN:

ROUTINE:                                       ACTION:

PSSDEE                                         SEND TO SITE

PSSHLDFS                                       SEND TO SITE

PSSMSTR                                        SEND TO SITE

OPTION:                                        ACTION:

PSS MASTER FILE ALL                            SEND TO SITE

SECURITY KEY:                                  ACTION:

PSS PADE INIT                                  SEND TO SITE

PROTOCOL:                                      ACTION:

PSS MFNM01 CLIENT                              SEND TO SITE

PSS MFNM01 SERVER                              SEND TO SITE

REQUIRED BUILDS:                               ACTION:

PSS*1.0*180                                    Don't install, leave global

CDEVISC1A2:DVA&gt;

### Modified and New Routines

The following routines are for PSS*1*193:

PSSDEE

PSSHLDFS

PSSMSTR
