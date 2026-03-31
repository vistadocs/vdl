---
consolidated_title: "user guide"
app_code: MMRS
doc_type: user-manual
master_source: "MMRS*1*4 User Guide"
master_pub_date: April 2017
consolidated_from: 2 versions
prior_versions:
  - "MMRS*1*5 User Guide"
---

**VistA Lab Enhancements (VLE) – Microbiology**

# Releases: LR*5.2*463 and MMRS*1.0*4

# User Guide

<!-- image -->

**April 2017**

Document Version 1.1


Office of Information and Technology (OI&amp;T)

*.*

Revision History

| Date       |   Revision | Description           | Author   |
|------------|------------|-----------------------|----------|
| 04/12/2017 |        1.1 | Introduction updated. | REDACTED |
| 01/27/2017 |        1   | Document baselined.   | REDACTED |

**Table of Contents**

1.	Introduction	1

1.1.	Purpose	1

1.2.	Document Orientation	1

1.2.1.	Organization of the Manual	1

1.2.2.	Assumptions	1

1.2.3.	Coordination	1

1.2.4.	Disclaimers	2

1.2.4.1. Software Disclaimer	2

1.2.4.2. Documentation Disclaimer	2

1.2.5.	Documentation Conventions	2

1.2.6.	References and Resources	3

1.3.	National Service Desk and Organizational Contacts	3

2.	System Summary	4

2.1.	System Configuration	5

2.2.	User Access Levels	5

2.3.	Continuity of Operation	6

3.	Getting Started	6

3.1.	Logging On	6

3.2.	System Menu	6

3.3.	Changing User ID and Password	6

3.4.	Exit System	7

3.5.	Keyboard Conventions	7

4.	Using the Software	7

4.1.	Program Tools Setup Menu Options	7

4.1.1.	MDRO Tools Parameter Setup (Main)	8

4.2.	MDRO Tools Lab Parameter Setup Screen and Help Prompts	10

4.3.	MDRO Tools Lab Parameter Setup	11

4.3.1.	MDRO Tools Lab Parameter Setup for MRSA	11

4.3.2.	MDRO Tools Lab Parameter Setup for Carbapenem-Resistance	17

4.3.3.	MDRO Tools Lab Parameter Setup for Vancomycin-Resistant Enterococcus	19

4.3.4.	MDRO Tools Lab Parameter Setup for Clostridium difficile	22

4.3.5.	MDRO Tools Lab Parameter Setup for Extended-Spectrum Beta-Lactamase	25

4.3.6.	MDRO Tools Lab Parameter Setup: Deleting Information Previously Entered	29

4.4.	MRSA Tools Ward Mapping Setup	30

4.4.1.	Deleting a Geographical Unit	31

4.5.	MDRO Historical Days Edit	32

4.6.	CRE Tools Site Parameter Setup	33

4.7.	Isolation Orders Add/Edit	35

4.8.	MDRO Tools Reports Menu	36

4.8.1.	MRSA IPEC Report	37

4.8.1.1. Admission Report	39

4.8.1.2. Admission Summary Report	40

4.8.1.3. Discharge/Transmission Report	43

4.8.1.4. Discharge/Transmission Summary Report	45

4.8.2.	Print Isolation Report	47

4.8.3.	Print Nares Screen Compliance List	49

4.8.4.	Print CDI Report	51

4.8.4.1. Printing the CDI Report to a Printer	51

4.8.4.2. Displaying the CDI report to screen.	53

4.8.4.3. Importing the Delimited data into Excel™ Spreadsheet	55

4.8.5.	Print CRE Report	63

4.9.	Tasked Reports	67

4.9.1.	Print Isolation Report (Tasked)	67

4.9.2.	Print Nares Screen Compliance List (Tasked)	70

4.9.3.	MDRO Print CDI Report (Tasked)	72

4.9.4.	Obtaining a Division IEN	74

4.9.5.	Deleting a Variable Name	75

5.	Troubleshooting	76

5.1.	Warning Message that Lab Test or Etiology Parameters are not configured	76

5.2.	Warning Message that Etiology Parameter is not configured	76

5.3.	Warning Message that Specimen is not Configured	76

5.4.	Warning Message that Division(s) are not configured	77

5.5.	Warning Message that Chemistry Subscripted Tests are not configured	77

5.6.	Warning Message that the etiology Staphylococcus Aureus Methicillin Resistant (MRSA) has not been configured	77

5.7.	Warning Message that the Geographical Unit has not been configured	78

6.	Printing in Landscape	78

7.	MAS Movement	78

Glossary	85

List of Figures

Figure 1: Simplified Topology for one VA Medical Center.	5

Figure 2: MDRO Tools Setup Menu Options	7

Figure 3: MDRO Tools Parameter Setup	9

Figure 4: MDRO Tools Lab Parameter Setup Display	12

Figure 5: MDRO Tools Lab Parameter Display for MRSA	14

Figure 6: MDRO Tools Parameter Setup for MRSA Selected Etiology	15

Figure 7: MDRO Tools Parameter Setup for MRSA Antimicrobial Susceptibility	16

Figure 8: MDRO Bacteriology Report Remarks Display for MRSA	17

Figure 9: MDRO Tools Lab Parameter Display for CRB-R	18

Figure 10: MDRO Tools Parameter Setup for Selected Etiology	19

Figure 11: MDRO Tools Lab Parameter Display for VRE	20

Figure 12: MDRO Tools Parameter Setup for Selected Etiology	21

Figure 13: MDRO Tools Parameter Setup for Antimicrobial Susceptibility	22

Figure 14: MDRO Tools Lab Parameter Display for C. Diff	23

Figure 15: MDRO Tools Parameter Setup for Selected Etiology	24

Figure 16: MDRO Tools Lab Parameter Display for ESBL	26

Figure 17: MDRO Tools Parameter Setup for Selected Etiology	26

Figure 18: MDRO Tools Parameter Setup for Antimicrobial Susceptibility	27

Figure 19: Bacteriology Report Remarks	28

Figure 20: Deleting information from MDRO Tools Lab Parameters Setup	29

Figure 21: MDRO Tools Ward Mapping Setup	31

Figure 22: MDRO Tools Ward Mapping Setup:  Deleting a Geographical Unit	32

Figure 23: MDRO Historical Days Edit	33

Figure 24: CRE Tools Site Parameter Setup: Add a Specimen	34

Figure 25: CRE Tools Site Parameter Setup: Edit a Specimen	35

Figure 26: MDRO Tools Isolation Orders Setup	36

Figure 27: MDRO Tools Reports Menu	37

Figure 28: Print MRSA IPEC Report	38

Figure 29: Print MRSA IPEC Admission Report	39

Figure 30: MRSA IPEC Admission Summary Report	41

Figure 31: MRSA IPEC Discharge/Transmission Report	43

Figure 32: MRSA IPEC Discharge/Transmission Summary Report	46

Figure 33: Print Isolation Report Option	47

Figure 34: Isolation Report	48

Figure 35: Nares Screen Compliance List	49

Figure 36: Nares Swab Order List	50

Figure 37: Example of Printing the CDI Report for a Division	52

Figure 38: Rendition of Printing the CDI Report to a Printer	53

Figure 39: ReflectionTM Column Size	54

Figure 40: Displaying the CDI Report to Screen	55

Figure 41: ReflectionTM Column Size	56

Figure 42: Select A2 in CDI Reporting Tool	57

Figure 43: Importing Delimited Data, Import Wizard Step 1 of 3	58

Figure 44: Importing Delimited Data, Import Wizard Step 2 of 3	59

Figure 45: Importing Delimited Data, Import Wizard Step 3 of 3	60

Figure 46: CRE Print Detailed Report for All Divisions	64

Figure 47: Example of CRE Print Detail Report for All Divisions	64

Figure 48: Example of CRE Print Detail Report for a Single Division	65

Figure 49: Print Isolation Report (Tasked)	68

Figure 50: Print Isolation Report (Tasked) with Division 1 and Geographical Locations 3, 5	69

Figure 51: Print Isolation Report (Tasked) with Division 1 and All Geographical Locations	69

Figure 52: Print Nares Screen Compliance List (Tasked)	70

Figure 53: Print Nares Swab List (Tasked) with Division 1 and Geographical Locations 3, 5	71

Figure 54: Print Nares Swab List (Tasked) with Division 1 and All Geographical Locations	71

Figure 55: MDRO Print CDI Report (Tasked)	72

Figure 56: MDRO Print CDI Report (Tasked) Division 1 and Geographical Locations 3, 5	73

Figure 57: MDRO Print CDI Report (Tasked) with Division 1 and All Geographical Locations	74

Figure 58: Obtain MRSA Division IEN	74

Figure 59: Obtain Geographical Location IEN	75

Figure 60: Deleting a Variable Name	75

Figure 61: Warning Dialog regarding Lab Test/Etiology Configuration	76

Figure 62: Warning Dialog regarding Etiology Configuration	76

Figure 63: Warning Dialog regarding Specimen Configuration	76

Figure 64: Warning Dialog regarding Division Setup	77

Figure 65: Warning Dialog regarding Chemistry Subscripted Tests	77

Figure 66: Warning Dialog regarding Staphylococcus Aureus Methicillin Resistant etiology	77

Figure 67: Warning Dialog regarding Geographical Unit	78

Figure 68: Printing in Landscape	78

List of Tables

Table 1: Documentation Descriptions	2

Table 2: Tier Support Contact Information	4

Table 3: Business Rules for Nares Screening Compliance	8

Table 4: MDRO-PT Laboratory Parameter Options	10

Table 5: Descriptions for MRSA IPEC Admission Report	39

Table 6:  Descriptions for Prevalence Measures (Facility Wide)	41

Table 7: Descriptions for Prevalence Measures (Unit Specific)	42

Table 8: Descriptions for MRSA IPEC Discharge/Transmission Report	43

Table 9: Descriptions for Transmission Measures (Unit Specific)	46

Table 10: Descriptions for Census List and MDRO History	48

Table 11: Descriptions for Nares Screen Compliance List	50

Table 12: Descriptions for Excel™ spreadsheet CDI Reporting Tool	61

Table 13: CRE Print Descriptions	65

Table 14: MAS Movement Program Explanations	79

## Introduction

### Purpose

The Multi-Drug Resistant Organisms (MDRO) Program Tools (PT) application provides a method to extract data related to Methicillin-Resistant Staphylococcus aureus (MRSA), Carbapenem-Resistance (CRB-R), Vancomycin-Resistant Enterococcus (VRE), Clostridium difficile (C. diff), and Extended-spectrum beta-lactamase (ESBL).  MDRO-PT contains reports that will extract and consolidate required data for entry into the Inpatient Evaluation Center (IPEC) system.  Reports can also be generated to display real-time patient specific information, and can be used to identify patients that have a selected MDRO, and to identify patients who either received or did not receive a nares screening upon admission to the unit.

Patch LR*5.2*463 includes the necessary microbiology enhancements to allow Department of Veterans Affairs (VA) labs the ability to document and utilize standard data in VistA for Carbapenem Resistant Enterobacteriaceae (CRE) and other MDROs. In addition, it includes the ability to distribute nationally these microbiology enhancements and other MDRO standardized reporting etiologies without requiring each individual lab to update its own local files manually.

Patch MMRS*1.0*4 shall support the timely identification of MDROs, provide enhanced reporting capabilities for CRE and Clostridium Difficile Infection (CDI) positive cases, and streamline the MRSA initiative by updating the legacy MRSA Program Tools menu options and naming conventions to MDRO where applicable.

### Document Orientation

#### Organization of the Manual

This guide is arranged in a manner in which Laboratory Information Manager (LIM) and Automated Data Processing Application Coordinator (ADPAC) staff members who are well versed in the VistA Laboratory package and VistA’s roll-and-scroll functionality will utilize the software.

An explanation of the features and functions in the LR*5.2*463 and MMRS*1.0*4 releases are provided in this Guide.

#### Assumptions

This guide was written with the following assumed experience/skills of the audience:

User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).

- User has been provided the appropriate active roles, menus, and required security keys.
- User is familiar with the VistA Laboratory software package.

#### Coordination

The Microbiology initiative is a collaborative solution between the VistA Laboratory Enhancement (VLE) Team and Clinical Laboratory personnel. This solution provides Microbiology Laboratory Technologists a system that integrates with the existing VistA Microbiology system.

Deployment will be performed by Local Facility staff and supported by team members from one or more of the operations organizations: Enterprise Systems Engineering (ESE), Field Operations (FO), Enterprise Operations (EO), Lab SMEs and/or others.

#### Disclaimers

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain.  The VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. However, the VA would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the VA of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

#### Documentation Conventions

This section includes descriptions of any formatting or symbols and their meaning.

Various symbols are used throughout the documentation to alert the reader to special information. Table 1 gives a description of each of these symbols.

Table 1: Documentation Descriptions

| **Font**              | **Use**                              | **Example**                                                                                                               |
|-----------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined | Hyperlink to another document or URL | For further instructions, refer to the link: http://www.va.gov/vdl                                                        |
| Courier New           | Menu options                         | MDRO Tools Parameter Setup                                                                                                |
| Courier New           | Screen prompts                       | Want KIDS to INHIBIT LOGONs during the install? YES//                                                                     |
| Courier New           | VistA filenames                      | XYZ file #798.1                                                                                                           |
| Courier New           | VistA field names                    | “In the Indicator field, enter the logic that is to be used to determine if the test was positive for the selected MDRO.” |
| Courier New, bold     | User responses to screen prompts     | **NO**                                                                                                                    |
| Courier New, bold     | Keyboard keys                        | < F1 >, < Alt >, < L >, <Tab>, <Enter>                                                                                    |
| Courier New           | Report names                         | Procedures report                                                                                                         |
| Times New Roman       | Body text (Normal text)              | “There are no changes in the performance of the system once the installation process is complete.”                        |
| Times New Roman Bold  | Emphasis                             | **Note**  : You can also type the access code, followed by a semicolon, followed by the verify code.                      |

#### References and Resources

Documentation is also available on the VistA Document Library (VDL) The online versions will be updated as needed. Please look for the latest version on the VDL:

[http://www.va.gov/vdl](http://www.va.gov/vdl)

The following documents were used in preparation of this guide:

- LR*5.2*463 Patch Description. February 2016.
- MMRS*1.0*4 Patch Description. December 2016.
- Microbiology Systems Design Document (SDD). March 2016, version 0.6.
- MMRS*1.0*3 User Manual. July 2010, version 1.0
- MMRS*1.0*3 Technical Manual. July 2010, version 1.0.

### National Service Desk and Organizational Contacts

The four tiers of support documented herein are intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

The table below lists organizational contacts needed by site users for troubleshooting purposes. Support contacts are listed by name of service responsible to fix the problem, description of the incident escalation, associated tier level, and contact information.

Table 2: Tier Support Contact Information

| **Name**                                  | **Role**                   | **Organization**   | **Contact Information**             |
|-------------------------------------------|----------------------------|--------------------|-------------------------------------|
| Clinical Application Coordinator          | Tier 0 Support             | VHA                | To be determined (TBD).             |
| OI&T National Service Desk                | Tier 1 Support             | OI&T               | REDACTED                            |
| OI&T Local Support                        | Tier 2 Support             | OI&T               | REDACTED                            |
| Health Product Support                    | Tier 2 Support             | VHA                | REDACTED                            |
| OI&T System Admin/Field Operation Support | Tier 2 & 3 support         | OI&T               | REDACTED                            |
| VistA Patch Maintenance                   | Tier 3 Application Support | OI&T               | REDACTED                            |
| Enterprise Operations                     | Tier 3 & 4 Support         | OI&T               | OI&T Enterprise Operations Helpdesk |

## System Summary

After the LR*5.2*463 patch has been installed and post-installation procedures have been applied, the following organisms will be available for configuration and report generation purposes:

- KLEBSIELLA PNEUMONIAE, CARBAPENEM RESISTANT (CRE)
- KLEBSIELLA OXYTOCA, CARBAPENEM RESISTANT (CRE)
- ESCHERICHIA COLI, CARBAPENEM RESISTANT (CRE)
- ENTEROBACTER CLOACAE, CARBAPENEM RESISTANT (CRE)
- ENTEROBACTER SPP, CARBAPENEM RESISTANT (CRE)

The features and functionality provided in the MMRS*1.0*4 patch will provide technicians, MDRO Prevention Coordinators (MPCs) and Infection Prevention (IP) personnel automated tools thereby increasing efficiency and reducing the labor hours required previously with manual data mining.

In regards to enhanced reporting capabilities, the MMRS*1.0*4 patch shall provide the following new reporting capabilities:

- CDI reporting functionality shall capture positive cases for the wards of a particular facility.
- CRE reporting functionality shall capture positive cases within a facility.

**Note:** As indicated in the Installation Guide, it is required that patch LR*5.2*463 is installed prior to patch MMRS*1.0*4.

### System Configuration

The following diagram depicts the high-level network configuration for a Veteran Affairs Medical Center (VAMC).

Figure 1: Simplified Topology for one VA Medical Center.

<!-- image -->

### User Access Levels

The core intended user base include Information Resource Management (IRM), LIMs and MPCs.

IRM and MPC personnel will be responsible for assigning the MDRO Tools Setup Menu, the MDRO Tools Reports Menu *,* and the MMRS SETUP security key to the appropriate users.

IRM personnel, LIMs, and MPCs will be jointly responsible for setting up the parameter options in the MDRO Tools Setup Menu.

### Continuity of Operation

REDACTED

## Getting Started

This section provides a general walkthrough of the system from initiation through exit. The logical arrangement of the information shall enable the functional personnel to understand the sequence and flow of the system.

1. Obtain an access code and a verify code from your Clinical Coordinator.
2. Type in your access and verify codes when prompted.

**Note:** If the MMRS Setup Security key has not been assigned, the user will only have access to the MDRO Tools Reports Menu.

### Logging On

Before you can login, you will need to obtain an access code and a verify code. Typically, your Clinical Coordinator issues these codes.

**To login, follow these steps:**

1. Open/access the **VistA** instance on your desktop.

The VistA logo window and the VistA Sign-on dialog will appear.

2. If the Connect To dialog appears, click the **down-arrow** , select the appropriate account (if more than one exists), and click **OK** .

3. Type your access code into the Access Code field and press the **Tab** key.

4. Type the verify code into the verify code field and press the **Enter** key or click **OK** .

**Note** : You can also type the access code, followed by a semicolon, followed by the verify code. Once you have completed this process press the **Enter** key or click **OK** .

### System Menu

Various menu options are available to the user.  However, it should be noted that a user who does not have the MMRS Setup security key will only have access to the MDRO Tools Reports Menu.

### Changing User ID and Password

To change your access and verify codes, contact your Clinical Coordinator.

### Exit System

To exit or opt out of answering any question or prompt, enter the carat (^) and the &lt;ENTER&gt; key at the field prompt.

### Keyboard Conventions

Text centered between arrows represents a keyboard key that should be pressed in order for the system to capture a user response or to move the cursor to another field.  &lt;Enter&gt; indicates that the Enter key (or Return key on some keyboards) must be selected.  &lt;Tab&gt; indicates that the Tab key must be selected.  For information on the use of the keys is provided below.

- Use the &lt;Tab&gt; key to move the cursor to the next field.
- Use the &lt;Enter&gt; to select the default.

One, two, or three question marks can be entered at any of the prompts for online help.

| ?   | One question mark displays a brief statement of what information is appropriate for the prompt.             |
|-----|-------------------------------------------------------------------------------------------------------------|
| ??  | Two question marks provide more help, plus any hidden actions.                                              |
| ??? | Three question marks will provide more detailed help, including a list of possible answers, if appropriate. |

The caret (^) plus the &lt;Enter&gt; key can be used to exit the current option.

## Using the Software

### Program Tools Setup Menu Options

This section describes the parameters for the six options listed under the MDRO Program Tools Menu.  Included in this section are screen captures which contain examples with pre-populated fields.  In order to obtain access to the menu, the IRM will need to assign access rights to the MDRO Program Tools Menu and provide the MMRS SETUP key.

The MDRO Tools Setup Menu Options are illustrated in the screen capture below.

Figure 2: MDRO Tools Setup Menu Options

MMRS MDRO TOOLS SETUP MENU     MDRO Tools Setup Menu

1      MRSA Tools Site Parameter Setup 
   2      MDRO Tools Lab Parameter Setup 
   3      MRSA Tools Ward Mapping Setup 
   4      MDRO Historical Days Edit 
   5      CRE Tools Site Parameter Setup

6      Isolation Orders Add/Edit

#### MDRO Tools Parameter Setup (Main)

The MDRO Tools Parameter Setup menu allows the user(s) to setup the following:

- Divisions for their facility.
- Business rules for nares screening for each division.

When adding divisions, include the following facility areas:

- Acute care hospital(s)
- Community Living Centers

**Note:** When adding divisions, do not include Community Based Outreach Clinics (CBOC), behavioral/mental health facilities, domiciliary facilities, etc.

During parameter setup, the user will have to answer prompts regarding business rules for nares screening on transfer and discharge.  Based on the business rules at the facility enter either **YES** or **NO** in the prompts.

Business rules for nares screening on transfer and/or discharge instituted by facilities are listed in the table below.  Answer either **YES** or **NO** if the following prompt/statement is true for your facility.

After the parameters have been configured as directed in the sections that follow, the MDRO Tools parameters should not be changed except under one of the following five conditions:

1. Changes in business rules for nares screening upon transfer or discharge to ensure the program captures the most current practices.
2. Adding/Removing a ward/unit from the program.
3. Ward mapping.
4. A Lab changes how they report results for the specified MDROs.
5. Changes have been made to the orderable items used for isolation purposes.

**Note:** The MDRO-PT national package materials (i.e., IPEC Reports) should be reviewed periodically by the sites for data validation.

Table 3: Business Rules for Nares Screening Compliance

| Business Rules/Prompts                                            | Respond with: Yes                                                 | Respond with: Yes                                                                                 | Respond with: No                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Receiving unit screen on unit-to-unit transfers.                  | Receiving unit screen on unit-to-unit transfers.                  | The receiving unit is responsible for nares screening for unit-to-unit transfers.                 | Only the discharging/sending unit is responsible for screening for unit-to-unit transfers, and not the receiving unit.                                                                                                                                                                   |
| Discharging unit screen on unit-to-unit transfers.                | Discharging unit screen on unit-to-unit transfers.                | The discharging/sending unit is responsible for nares screening on unit-to-unit transfers.        | Only the receiving unit is responsible for nares screening on unit-to-unit transfers, and not the discharging unit.                                                                                                                                                                      |
| Screen patients with MRSA history on transfer-in.                 | Screen patients with MRSA history on transfer-in.                 | Patients are screened for MRSA on all transfer-ins, regardless of MRSA status.                    | Nares screens are not required for known MRSA positive patients (i.e., patients with a history of MRSA in the past year) for any transfer-in, via an inter-ward transfer.  To be considered ‘known positive’ the lab result must have been verified before the patient entered the unit. |
| Screen patient with MRSA history on discharge/death/transfer-out. | Screen patient with MRSA history on discharge/death/transfer-out. | Patients are screened for MRSA on all discharges/deaths/transfer-outs, regardless of MRSA status. | Nares screens are not required for known MRSA positive patients (i.e., patients with a history of MRSA in the past year) for any discharge, death, or transfer-out.  To be considered ‘known positive’ the lab result must have been verified before the patient left the unit.          |

Figure 3: MDRO Tools Parameter Setup

Select MDRO Tools Setup Menu Option: **MDRO Tools Parameter Setup**

Select MRSA SITE PARAMETERS DIVISION: **XXXXX VAMC**

Are you adding ‘XXXXX VAMC’ as

a new MRSA SITE PARAMETERS (the 1ST)? No// **Y** (Yes)

1. Receiving unit screen on unit-to-unit transfers: **YES**

2. Discharging unit screen on unit-to-unit transfers: **YES**

3. Screen patients with MRSA history on transfer-in: **YES**

4. Screen patients with MRSA history on discharge/death/transfer-out: **YES**

**Note:** There should never be a NO listed for both the Receiving unit screen on unit-to-unit transfers and Discharging unit screen on unit-to-unit transfers prompts.  This would indicate to the program that neither the receiving nor discharging unit is screening the patients on unit-to-unit transfers.

**Note:** It is required that business rules are added for each division.

### MDRO Tools Lab Parameter Setup Screen and Help Prompts

MDRO Tools Lab Parameter Setup option screen prompts and help prompts definitions are described in the table below.

Table 4: MDRO-PT Laboratory Parameter Options

| MDRO Tools Lab Parameter Setup Screen Prompt      | MDRO Tools Lab Parameter Setup Screen Help Prompt                                                                                                                                          |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Laboratory Tests(s)                               | Used only for Chemistry(CH) subscripted tests.  This is the test name to identify MRSA nares or CDI CH subscripted tests.  Select from the LABORATORY TEST file #60.                       |
| Indicator (for Laboratory Test(s) only)           | Select the code that will determine how to match lab results:  1 = Use Reference Ranges  2 = Contains  3 = Greater Than  4 = Less Than  5 = Equal To                                       |
| Value                                             | Enter POS, Positive, or 1.  This is a free text field that allows letters, numbers, punctuation, and spaces.  It is not case-sensitive.  Answers must be 1-30 characters in length.        |
| Selected Etiology                                 | Consider synonymous with organism, final microbial diagnosis/isolate.  Select from the ETIOLOGY FIELD file #61.2.                                                                          |
| Antimicrobial Susceptibility                      | Enter the antimicrobial that will be used in screening out sensitive Etiologies (e.g., “Oxacillin” for Staphylococcus aureus).  Select from the ANTIMICROBIAL SUSCEPTIBILITY file #62.06.  |
| Indicator (for Antimicrobial Susceptibility only) | Select the code that will determine how to match susceptibility interpretations:  1 = Contains  2 = Greater Than  3 = Less Than  4 = Equal To                                              |
| Indicated Value                                   | Choose a code to report susceptibility to antimicrobial agents:  For example:  - R for Resistant - S for Susceptible                                                                       |
| Include (for Bacteriology Report Remarks)         | Enter information pertaining to positive results.  This is a free text field that allows letters, numbers, punctuation, and spaces.  Answers must be 1-68 characters in length.            |
| Exclude (for Bacteriology Report Remarks)         | Enter reporting information pertaining to negative results.  This is a free text field that allows letters, numbers, punctuation, and spaces.   Answers must be 1-68 characters in length. |

### MDRO Tools Lab Parameter Setup

This option allows the user to enter laboratory parameters for historical reporting of the following multi-drug resistant organisms (MDROs):

- METHICILLIN-RESISTANT STAPHYLOCOCCUS AUREUS (MRSA)
- CARBAPENEM-RESISTANCE (CRB-R)
- VANCOMYCIN-RESISTANT ENTEROCOCCUS (VRE)
- CLOSTRIDIUM DIFFICILE (C. DIFF)
- EXTENDED-SPECTRUM BETA-LACTAMASE (ESBL)

**Note:** The user may choose to configure all five of the MDROs or may choose to define only the required MDROs; the required MDROs are MRSA and Clostridium difficile.  The other MDRO(s) are optional and will only need to be configured if the Print Isolation Report option will be utilized.

**Note:** The following Laboratory Tests do not need to be added to the laboratory parameters setup:  MRSA SURVL NARES DNA, MRSA SURVL NARES AGAR, MRSA SURVL OTHER DNA, and MRSA SURVL OTHER AGAR.

**Note:** Do not add STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT to the Selected Etiology section.  This information is already available in the program.

#### MDRO Tools Lab Parameter Setup for MRSA

Adding Methicillin-resistant Staphylococcus aureus to the MDRO Tools Lab Parameter Setup is mandatory .  The purpose of adding this pathogen to the parameter set-up is to identify prior history of MRSA (either by clinical culture or nares screen) based on laboratory reporting. If the facility fails to use the laboratory standards set forth, the program will be unable to generate accurate reports.

Methicillin (or oxacillin)-resistant Staphylococcus aureus (MRSA) is a pathogen of continuing importance for healthcare facilities.  It is a Gram-positive coccus that can be resistant to multiple antibiotics, causes serious disease, and is often difficult to treat.  It is the cause of healthcare-associated infections (HAIs), and is an emerging pathogen from community-associate sources. MRSA can be cultured from the nares and other sites in patients who are colonized or infected with the organism.  It is transmitted, in general, by contact with the hands of patients or health care workers or inanimate objects contaminated with MRSA.  Such transmission amplifies the number of patients who may become colonized and who are then at risk for clinical infection.

It is important to capture all positive tests for MRSA, both clinical cultures and surveillance screening tests (e.g., nares screens).  Any Staphylococcus aureus isolate that is resistant to Methicillin (or oxacillin) should be captured.   Veterans Health Administration (VHA) Laboratory Service must record results of MRSA tests performed using the following methodology:

- MI-subscripted tests will be used for clinical cultures only. STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA) is the only etiology that will be used to report positive clinical cultures.

- CH-subscripted tests will be used for MRSA nares screens or MRSA surveillance cultures. Laboratory is required to use the following test names: MRSA SURVL NARES DNA, MRSA SURVL OTHER DNA, MRSA SURVL NARES AGAR, MRSA SURVL OTHER AGAR.

**Note:** Refer to the "Laboratory Reporting of MRSA Test" for information on how to setup the standardized test names and etiologies.

This option allows the user to enter laboratory parameters for historical reporting of MRSA in the past 12 months.  The data entered in using this option will be used by the MRSA IPEC Reports and the MDRO Isolation Report to obtain laboratory information.

Figure 4: MDRO Tools Lab Parameter Setup Display

Select MDRO Tools Setup Menu Option: **MDRO Tools Lab Parameter Setup**

Select the Division: XXXXX VAMC

Select the MDRO: ?

Answer with MDRO TYPES NUMBER, or ABBREVIATION

Choose from:

1            MRSA      Methicillin-resistant Staphylococcus aureus

2            CRB-R     Carbapenem-Resistance

3            VRE       Vancomycin-Resistant Enterococcus

4            C. diff   Clostridium difficile

5            ESBL      Extended-spectrum beta-lactamase

Select the MDRO: **MRSA**

Do you want to see a description for MRSA? YES//

1. Enter the name of the division.  Press the **&lt;ENTER&gt;** key.

**Note:** If only one division has been set up at the site, this prompt will not be displayed.

1. Enter **MRSA** for Methicillin-resistant Staphylococcus aureus and press the **&lt;ENTER&gt;** key.
2. At the prompt, Do you want to see a description for C. diff?

1. To view the description, respond with **Y** and press the **&lt;ENTER&gt;** key twice to view the entire description.
2. Otherwise, respond with **N** and press the **&lt;ENTER&gt;** key.

3. In the Laboratory Test(s) field, enter **MRSA** and press the **&lt;TAB&gt;** key.
4. In the Indicator field, enter the logic that is to be used to determine if the test was positive.  As this field utilizes a set of codes, enter the code that will determine how to match susceptibility interpretations:

- **1** = Contains
- **2** = Greater Than
- **3** = Less Than
- **4** = Equal To

After entering the code, press the **&lt;TAB&gt;** key.

1. In the Value field, enter either **POS** , **Positive** , or **1** .  Press the **&lt;TAB&gt;** key.

**Note:** This is a free text field that allows letters, numbers, punctuation, and spaces.  It is not case-sensitive.  Answers must be 1-30 characters in length. Do not search for negative results.

Figure 5: MDRO Tools Lab Parameter Display for MRSA

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2

DIVISION: XXXXX VAMC                              MDRO: MRSA

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s)               Indicator                 Value

**MRSA (BY PCR) SCREEN		 Contains			POS**

Selected Etiology

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                               Press &lt;PF1&gt;H for help

1. Configure the MDRO by following the instructions below for either Chemistry (CH) subscripted tests or Microbiology (MI) subscripted tests:
    - 1.1. Select the CH-subscripted test from the LABORATORY TEST file (#60) and press the **&lt;TAB&gt;** key.

**Note:** The system will not let you choose a test with a subscript field (Field #4 in File #60) set to anything other than CH.  Laboratory is required to use the following test names: MRSA SURVL NARES DNA, MRSA SURVL OTHER DNA, MRSA SURVL NARES AGAR, MRSA SURVL OTHER AGAR.

- 0.1. For MI-subscripted tests, the Selected Etiology field will be used.  Select the etiology from the ETIOLOGY FIELD file (#61.2). For example, enter STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT and press the **&lt;TAB&gt;** key.

**Note:** STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA) is the only etiology that will be used to report positive clinical cultures.

**Note:** Refer to the "Laboratory Reporting of MRSA Test" for information on how to setup the standardized test names and etiology.

Figure 6: MDRO Tools Parameter Setup for MRSA Selected Etiology

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2

DIVISION: XXXXX VAMC                                                                MDRO: MRSA

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s)                    Indicator     Value

MRSA (BY PCR) SCREEN                  Contains      POS

Selected Etiology

**STAPHYLOCOCCUS AUREUS**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                                 Press &lt;PF1&gt;H for help

1. Enter the Antimicrobial Susceptibility for the organism and press the **&lt;TAB&gt;** key.

**Note:** Utilize the Susceptibility Template that is appropriate for the site.

**Note:** If an antimicrobial susceptibility is not entered, the program will consider the result positive. However, if an antimicrobial susceptibility is entered, the program will only consider the result positive if the organism meets the condition that is entered for one of the antimicrobials; for example, if Oxacillin Contains R (R for resistant) is entered in the Antimicrobial Susceptibility section for the Staphylococcus Aureus organism, then the test result will only be considered positive if it contains that organism, and it is Oxacillin Resistant.

If more than one antimicrobial susceptibility is entered, the program will consider the result positive if one of the antimicrobial susceptibilities entered matches the indicated value.

1. Enter the code for the Indicator field that will determine how to match susceptibility interpretations:

- **1** = Contains
- **2** = Greater Than
- **3** = Less Than
- **4** = Equal To

2. In the Indicated Value field, enter a code to report the susceptibility to antimicrobial agents and press the **&lt;ENTER&gt;** key:

- **R** for Resistant
- **S** for Susceptible

Figure 7: MDRO Tools Parameter Setup for MRSA Antimicrobial Susceptibility

| MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2  DIVISION: XXXXX VAMC                                                                MDRO: MRSA  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Laboratory Test(s)                         Indicator    Value  MRSA (BY PCR) SCREEN                       Contains     POS   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Selected Etiology  STAPHYLOCOCCUS AUREUS  ANTIMICROBIAL SUSCEPTIBILITY                                        INDICATOR    INDICATED VALUE      OXACILLIN                                                             Contains       R                                        COMMAND:                                                  Press &lt;PF1&gt;H for help                                                                                       |

1. If desired, enter information in the second page of the form for the Bacteriology Report Remarks.  Use discernment when entering information into the Bacteriology Report Remarks as it is a free text field and therefore introduces risk for entering information incorrectly which will adversely affect the results generated by the program.
    - 1.1. If desired, enter reporting information pertaining to positive results into the Include field.  This is a free text field that allows letters, numbers, punctuation, and spaces.  Answers must be 1-68 characters in length.
    - 1.2. If desired, enter reporting information pertaining to negative results into the Exclude field.  This is a free text field that allows letters, numbers, punctuation, and spaces.   Answers must be 1-68 characters in length.

**Note:** To include the positive results and exclude the negative results, use both the Include and the Exclude fields.  For example, for molecular based tests, the following two phrases are commonly used: MRSA DNA DETECTED for positive results and NO MRSA DNA DETECTED for negative results.  If NO MRSA DNA DETECTED has not been entered in the Exclude section, then a result that has the remark NO MRSA DNA DETECTED will be considered positive.

1. At the prompt, Save changes before leaving form (Y/N)?  Respond with **Y** and press the **&lt;ENTER&gt;** key.
2. At the Command prompt, enter **E** to exit the form(s).

Figure 8: MDRO Bacteriology Report Remarks Display for MRSA

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 2 of 2

DIVISION: XXXXX VAMC                              MDRO: MRSA

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

BACTERIOLOGY REPORT REMARKS

Include                                  Exclude

**MRSA DNA DETECTED                        NO MRSA DNA DETECTED**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit     Save     Next Page     Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

Save changes before leaving form (Y/N)?  Y           Press &lt;PF1&gt;H for help

#### MDRO Tools Lab Parameter Setup for Carbapenem-Resistance

Carbapenems are a class of beta-lactam antibiotics with a broad spectrum of antibacterial activity. These agents have the broadest antibacterial spectrum compared to other beta-lactam classes. They are active against both Gram positive and Gram negative bacteria, and can be used to treat nosocomial and mixed bacterial infections. Resistance to carbapenems is of importance because it limits therapeutic options.

**Note:** The purpose of adding carbapenem-resistant enterobacteriacea (CRE) etiologies to the MDRO Tools Lab Parameter Setup is to identify a patient's current or prior history of CRE based on laboratory reporting and the time frames that are entered to search for the patient's status. The result must occur as a CRE bacterial etiology and any result contained in a “free-text" section will not allow incorporation of the CRE into the MDRO Program Tools software.

**Note:** If desired, configure the Lab Parameter for CRE for multiple divisions.  Setup the divisions according to local facility policy.

1. Enter the name of the division.  Press the **&lt;ENTER&gt;** key.

**Note:** If only one division has been set up at the site, this prompt will not be displayed.

1. Enter **CRB-R** for Carbapenem-Resistance and press the **&lt;ENTER&gt;** key.
2. At the prompt, Do you want to see a description for CRB-R?
    - 2.1. To view the description, respond with **Y** and press the **&lt;ENTER&gt;** key twice to view the entire description.
    - 2.2. Otherwise, respond with **N** and press the **&lt;ENTER&gt;** key.

3. In the Laboratory Test(s) field, press the **&lt;TAB&gt;** key to leave the field blank.
4. In the Indicator field, press the **&lt;TAB&gt;** key to leave the field blank.
5. In the Value field, press the **&lt;TAB&gt;** key to leave the field blank.

Figure 9: MDRO Tools Lab Parameter Display for CRB-R

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2

DIVISION: XXXXX VAMC                              MDRO: CRB-R

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s)               Indicator                 Value

Selected Etiology

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                               Press &lt;PF1&gt;H for help

1. For MI-subscripted tests, the Selected Etiology field will be used.  Select the etiology from the ETIOLOGY FIELD file (#61.2) For example, enter part of the etiology name; for example, enter **kleb** to display a list associated with KLEBSIELLA.   Select the etiology from the list.  After the installation of patch LR*5.2*463, the following etiologies will be available for configuration:

- KLEBSIELLA PNEUMONIAE, CARBAPENEM RESISTANT (CRE)
- KLEBSIELLA OXYTOCA, CARBAPENEM RESISTANT (CRE)
- ESCHERICHIA COLI, CARBAPENEM RESISTANT (CRE)
- ENTEROBACTER CLOACAE, CARBAPENEM RESISTANT (CRE)
- ENTEROBACTER SPP, CARBAPENEM RESISTANT (CRE)
    - 1.1. Enter the name of each etiology from the Etiology Field File and press the **&lt;ENTER&gt;** key until all five of the etiologies listed above have been entered.

Figure 10: MDRO Tools Parameter Setup for Selected Etiology

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2

DIVISION: XXXXX VAMC                              MDRO: CRB-R

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s)                    Indicator     Value

Selected Etiology

**KLEBSIELLA PNEUMONIAE (CRE)**

**KLEBSIELLA OXYTOCA, CARBAPENEM RESISTANT (CRE)                       
ESCHERICHIA COLI, CARBAPENEM RESISTANT (CRE)                         
ENTEROBACTER CLOACAE, CARBAPENEM RESISTANT (CRE)                     
ENTEROBACTER SPP, CARBAPENEM RESISTANT (CRE)**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                                 Press &lt;PF1&gt;H for help

1. Do not enter the Antimicrobial Susceptibility for the organism. Select the **&lt;TAB&gt;** key to exit.

**Note:** When the antimicrobial susceptibility is not entered, the program will consider the result positive.  Only positive results will be obtained.

1. At the Command prompt, select the **&lt;ENTER&gt;** key to accept the default to close the form.
2. At the prompt, Save changes before leaving form (Y/N)?  Respond with **Y** and press the **&lt;ENTER&gt;** key.
3. At the Command prompt, enter **E** to exit the form(s).

#### MDRO Tools Lab Parameter Setup for Vancomycin-Resistant Enterococcus

Adding Vancomycin-resistant Enterococcus (VRE) to the MDRO Tools Lab Parameter Setup is optional.  The purpose of adding VRE to the parameter set-up is to identify a patient’s current or prior history of the MDRO.  This information can optionally be displayed on the Isolation Report and will include positive cultures for prevalence and surveillance review, with specimens of stool and rectal swabs.

VRE is a pathogen of increasing importance for healthcare facilities.  Enterococcus is a bacterium that lives in the intestinal tract and in the female genital tract.  Vancomycin is an antibiotic that is often used to treat infections caused by enterococci, and recently enterococci have become resistant to this drug.  Most VRE infections occur in the hospital.

**Note:** The laboratory parameter setup for the MDRO Program Tools should match the same parameter setup for the EPI (Emerging Pathogens Initiative).  If changes are made to how VRE is reported it should also be changed in EPI parameter setup.

1. Enter the name of the division.  Press the **&lt;ENTER&gt;** key.

**Note:** If only one division has been set up at the site, this prompt will not be displayed.

1. Enter **VRE** for Vancomycin-resistant Enterococcus and press the **&lt;ENTER&gt;** key.
2. At the prompt, Do you want to see a description for VRE?

1. To view the description, respond with **Y** and press the **&lt;ENTER&gt;** key twice to view the entire description.
    - 1.2. Otherwise, respond with **N** and press the **&lt;ENTER&gt;** key.

3. In the Laboratory Test(s) field, press the **&lt;TAB&gt;** key.
4. In the Indicator field, press the **&lt;TAB&gt;** key.
5. In the Value field, press the **&lt;TAB&gt;** key.

Figure 11: MDRO Tools Lab Parameter Display for VRE

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2

DIVISION: XXXXX VAMC                              MDRO: VRE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s)               Indicator                 Value

Selected Etiology

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                               Press &lt;PF1&gt;H for help

1. For MI-subscripted tests, the Selected Etiology field will be used.  Select the etiology from the ETIOLOGY FIELD file (#61.2). Enter the name of the etiology, for example, ENTEROCOCCUS, and press the **&lt;TAB&gt;** key.

Figure 12: MDRO Tools Parameter Setup for Selected Etiology

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2

DIVISION: XXXXX VAMC                              MDRO: VRE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s)                    Indicator     Value

Selected Etiology

**ENTEROCOCCUS**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                                 Press &lt;PF1&gt;H for help

1. Enter the code for the Indicator field that will determine how to match susceptibility interpretations:

- **1** = Contains
- **2** = Greater Than
- **3** = Less Than
- **4** = Equal To

2. In the Indicated Value field, enter a code to report the susceptibility to antimicrobial agents and press the **&lt;ENTER&gt;** key:

- **R** for Resistant
- **S** for Susceptible

3. At the prompt, Save changes before leaving form (Y/N)?  Respond with **Y** and press the **&lt;ENTER&gt;** key.
4. At the Command prompt, enter **E** to exit the form(s).

Figure 13: MDRO Tools Parameter Setup for Antimicrobial Susceptibility

| MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2  DIVISION: XXXXX VAMC                              MDRO: VRE  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Laboratory Test(s)                         Indicator    Value   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Selected  ENTEROCOCCUS  ANTIMICROBIAL SUSCEPTIBILITY                                        INDICATOR    INDICATED VALUE      VANCOMYCIN                                                         Contains       R                                        COMMAND:                                                  Press &lt;PF1&gt;H for help            |

#### MDRO Tools Lab Parameter Setup for Clostridium difficile

Clostridium difficile (C. difficile or C. diff) is a species of gram-positive bacteria. The disease is associated with the presence of Clostridium difficile enterotoxin, which can cause significant morbidity, as well as mortality. It is of importance, as its predominant acquisition appears to occur nosocomially and is the most serious cause of antibiotic-associated diarrhea. Presence of clostridium toxin (either enterotoxin or cytotoxin L) by assay (whether it be EIA, latex agglutination, cytotoxicity of cell culture neutralization, or culture of organism with subsequent colony testing) is the best indicator that an inflammatory diarrheal disease is due to presence of Clostridium difficile.

Laboratory services are quite varied as to how they identify the presence of Clostridium difficile. Some labs are set up to identify C. difficile as the final microbiological (bacterial) etiology of a culture, even if a culture method was not used. Other labs use a final etiology of "see comment" and then enter the results in a free text format. Still others enter the text under a hematology or chemistry format where a reference range and "positive" and "negative" result values can be entered.   Wherever the VHA Laboratory Service places the results, which are used to demonstrate the presence of toxin-producing C. difficile, should be accessible as a standardized field in order to allow the MDRO Programs Tool software to capture its presence.

**Note:** The purpose of adding Clostridium difficile to the MDRO Tools Lab Parameter Setup is to identify a patient's current or prior history of Clostridium difficile based on laboratory reporting and the time-frames that are entered to search for the patient's status.  The result must occur as a Clostridium difficile (a bacterial etiology) or as a retrievable “positive” result for a chemistry/serology laboratory test. Any results contained in a "Free-Text" section will not allow incorporation of Clostridium difficile into the MDRO Program Tools/Print CDI Report format.

1. Enter the name of the division.  Press the **&lt;ENTER&gt;** key.

**Note:** If only one division has been set up at the site, this prompt will not be displayed.

1. Enter **C. diff** for Clostridium difficile and press the **&lt;ENTER&gt;** key.
2. At the prompt, Do you want to see a description for C. diff?
    - 2.1. To view the description, respond with **Y** and press the **&lt;ENTER&gt;** key twice to view the entire description.
    - 2.2. Otherwise, respond with **N** and press the **&lt;ENTER&gt;** key.

**Note:** The instructions provided below are in regard to the configuration of Laboratory Tests and Etiologies.  Facilities have the option of configuring for Laboratory Tests only, Etiologies only, or for configuring for both Lab Tests and Etiologies.

1. In the Laboratory Test(s) field, enter the exact name of the C. diff toxin that has been configured, for example, **CLOSTRIDUM DIFFICILE TOXIN** .  Press the **&lt;TAB&gt;** key.
2. In the Indicator field, enter **Contains** and press the **&lt;TAB&gt;** key.
3. In the Value field, enter **POS** and press the **&lt;TAB&gt;** key.

**Note:** This is a free text field that allows letters, numbers, punctuation, and spaces; it is not case-sensitive.  Answers must be 1-30 characters in length. Do not search for negative results.

Figure 14: MDRO Tools Lab Parameter Display for C. Diff

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2

DIVISION: XXXXX VAMC                              MDRO: C. diff

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s)               Indicator                 Value

**CLOSTRIDUM DIFFICILE TOXIN       CONTAINS                  POS**

Selected Etiology

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                               Press &lt;PF1&gt;H for help

1. For MI-subscripted tests, the Selected Etiology field will be used.  Select **CLOSTRIDIUM DIFFICILE** from the ETIOLOGY FIELD file (#61.2).
2. Do not enter the Antimicrobial Susceptibility for the organism.  Select the **&lt;TAB&gt;** key to exit.

**Note:** When the antimicrobial susceptibility is not entered, the program will consider the result positive.  Only positive results will be obtained for C. diff.

1. At the command prompt, type **Close** and press the **&lt;ENTER&gt;** key.
2. Press the **&lt;TAB&gt;** key.
3. At the command prompt, type **S** to save the form and press the **&lt;ENTER&gt;** key.

1. At the command prompt, type **E** to exit and press the **&lt;ENTER&gt;** key.

**Note:** When the antimicrobial susceptibility is not entered, or the field is left blank, the program will consider the result positive .  Only positive results will be obtained for C. diff.

Figure 15: MDRO Tools Parameter Setup for Selected Etiology

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2

DIVISION: XXXXX VAMC                              MDRO: C. diff

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s)                    Indicator     Value

CLOSTRIDUM DIFFICILE TOXIN            CONTAINS      POS

Selected Etiology

**CLOSTRIDIUM DIFFICILE**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                                 Press &lt;PF1&gt;H for help

#### MDRO Tools Lab Parameter Setup for Extended-Spectrum Beta-Lactamase

Adding Extended-Spectrum Beta-Lactamase (ESBL) to the MDRO Tools Lab Parameter setup is optional.  The purpose of adding pathogens containing this form of antimicrobial resistance to the parameter set-up is to identify a patient’s current or prior history of ESBL. This information can optionally be displayed on the Isolation Report.  To find and display this information, enter information into the Bacteriology Report Remarks section.

ESBLs are enzymes that mediate resistance to extended-spectrum (third generation) cephalosporins (e.g., ceftazidime, cefotaxime, and ceftriaxone) and monobactams (e.g., aztreonam) but do not affect cephamycins (e.g., cefoxitin and cefotetan) or carbapenems (e.g., imipenem or meropenem).

ESBLs can be difficult to detect because they have different levels of activity against various cephalosporins.  It is critical to test the appropriate antimicrobial agent, thus an appropriate Committee on Laboratory Standards Institute (CLSI) testing schema should be utilized.  If an isolate is confirmed as an ESBL-producer by the CLSI-recommended phenotypic confirmatory test procedure, then all penicillins, cephalosporins and aztreonams should be reported as resistant.  Cephamycins should be reported according to their routine test results.

> **NOTE:** Any information contained in a free-text section will not allow incorporation of ESBL into the Isolation Report.

1. Enter the name of the division.  Press the **&lt;ENTER&gt;** key.

**Note:** If only one division has been set up at the site, this prompt will not be displayed.

1. Enter **ESBL** for Extended-Spectrum Beta-Lactamase and press the **&lt;ENTER&gt;** key.
2. At the prompt, Do you want to see a description for ESBL?
    - 2.1. To view the description, respond with **Y** and press the **&lt;ENTER&gt;** key twice to view the entire description.
    - 2.2. Otherwise, respond with **N** and press the **&lt;ENTER&gt;** key.
3. In the Laboratory Test(s) field, press the **&lt;TAB&gt;** key.
4. In the Indicator field, press the **&lt;TAB&gt;** key.
5. In the Value field, press the **&lt;TAB&gt;** key.

Figure 16: MDRO Tools Lab Parameter Display for ESBL

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2

DIVISION: XXXXX VAMC                              MDRO: ESBL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s)               Indicator                 Value

Selected Etiology

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                               Press &lt;PF1&gt;H for help

1. For MI-subscripted tests, the Selected Etiology field will be used.  Select the etiology from the ETIOLOGY FIELD file (#61.2).  In the example below, ESCHERICHIA COLI was entered. Enter the name of the etiology and press the **&lt;TAB&gt;** key.

Figure 17: MDRO Tools Parameter Setup for Selected Etiology

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2

DIVISION: XXXXX VAMC                              MDRO: ESBL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s)                    Indicator     Value

Selected Etiology

**ESCHERICHIA COLI**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                                 Press &lt;PF1&gt;H for help

1. Enter the Antimicrobial Susceptibility for the organism.

**Note:** If an antimicrobial susceptibility is not entered, the program will consider the result positive.  However, if an antimicrobial susceptibility is entered, the program will only consider the result positive if the organism meets the condition that is entered for one of the antimicrobials; for example, if Meropenem Contains R (R for resistant) is entered in the Antimicrobial Susceptibility section for the organism, then the test result will only be considered positive if it contains that organism, and it is Meropenem Resistant.

**Note:** If more than one antimicrobial susceptibility is entered, the program will consider the result positive if one of the antimicrobial susceptibilities entered matches the indicated value.

1. In the Indicator field, enter the logic that is to be used to determine if the test was positive.  As this field utilizes a set of codes, enter the code that will determine how to match susceptibility interpretations:

- **1** = Contains
- **2** = Greater Than
- **3** = Less Than
- **4** = Equal To

After entering the code, press the **&lt;TAB&gt;** key.

1. In the Indicated Value field, enter a code to report the susceptibility to antimicrobial agents and press the **&lt;ENTER&gt;** key:

- **R** for Resistant
- **S** for Susceptible

Figure 18: MDRO Tools Parameter Setup for Antimicrobial Susceptibility

| MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2  DIVISION: XXXXX VAMC                              MDRO: ESBL  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Laboratory Test(s)                         Indicator    Value   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Selected  ESCHERICHIA COLI  ANTIMICROBIAL SUSCEPTIBILITY                                        INDICATOR    INDICATED VALUE      CEFPODOXIME                                                       Contains       R                                        COMMAND:                                                  Press &lt;PF1&gt;H for help          |

1. If desired, enter information in the second page of the form for the Bacteriology Report Remarks.  Use discernment when entering information into the Bacteriology Report Remarks as it is a free text field and therefore introduces risk for entering information incorrectly which will adversely affect the results generated by the program.
    - 1.1. If desired, enter reporting information pertaining to positive results into the Include field.  This is a free text field that allows letters, numbers, punctuation, and spaces.  Answers must be 1-68 characters in length.
    - 1.2. If desired, enter reporting information pertaining to negative results into the Exclude field.  This is a free text field that allows letters, numbers, punctuation, and spaces.   Answers must be 1-68 characters in length.

**Note:** To include the positive results and exclude the negative results, use both the Include and the Exclude fields.  For example, for molecular based tests, the following two phrases are commonly used: ESBL POSITIVE for positive results and NOT ESBL POSITIVE for negative results.  If NOT ESBL POSITIVE has not been entered in the Exclude section, then a result that has the remark NOT ESBL POSITIVE will be considered positive.

1. At the prompt, Save changes before leaving form (Y/N)?  Respond with **Y** and press the **&lt;ENTER&gt;** key.
2. At the Command prompt, enter **E** to exit the form(s).

Figure 19: Bacteriology Report Remarks

MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 2 of 2

DIVISION: XXXXX VAMC                              MDRO: ESBL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

BACTERIOLOGY REPORT REMARKS

Include                                  Exclude

**ESBL POSITIVE                            NOT ESBL POSITIVE**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                           Press &lt;PF1&gt;H for help

#### MDRO Tools Lab Parameter Setup: Deleting Information  Previously Entered

Facilities may delete information that has been previously entered from the following fields:

- Laboratory Test
- Selected (Etiology)
- Antimicrobial Susceptibility
- Bacteriology Report Remarks

To delete information previously entered, perform the following steps:

1. Go to the field where the change needs to occur and place the **@** symbol in the field.
2. When prompted, Are you sure you want to delete this entire Subrecord (Y/N)?  respond with **Y** with the **&lt;ENTER&gt;** key to delete the information from the field.

Figure 20: Deleting information from MDRO Tools Lab Parameters Setup

| MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP    Page 1 of 2  DIVISION: XXXXX VAMC                                            MDRO: MRSA  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Laboratory Test(s)                         Indicator    Value  MRSA (BY PCR) SCREEN                       Contains     POS                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Selected  STAPHYLOCOCCUS AUREUS  ANTIMICROBIAL SUSCEPTIBILITY                                        INDICATOR    INDICATED VALUE      @                                                                                Contains       R                                        WARNING: DELETIONS ARE DONE IMMEDIATELY!  (EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)  Are you sure you want to delete this entire Subrecord (Y/N)?  Y |

### MRSA Tools Ward Mapping Setup

This option allows the user to define geographical units within each division for the purpose of running reports.  A geographical unit can consist of one or more wards listed in VistA, and for all intents and purposes is considered one unit.  Units may be mapped or grouped together for reporting purposes.  For example, one unit may be divided into Unit X Medicine and Unit X Surgery, but is one geographical unit.  By mapping the wards (e.g., Unit X Med-Surg), the report will consider all the wards mapped together as one location and all transfers between Unit X Medicine and Unit X Surgery will be ignored.

**Note:** Ward mappings must be configured for every unit for the purpose of running reports.

To configure the MRSA Tools Ward Mapping, perform the following steps:

1. When prompted, enter the name of the Unit to either create a new Geographical Unit or to edit an existing one.

**Note:** When adding a new location, use discretion and enter a descriptive name.

1. When prompted, enter the MRSA Ward Mappings Type and IPEC Unit ID.

**Note:** This information is required for the program to extract the data for upload to the IPEC website for data reporting purposes.

1. For the Location Type, choose from the following: **Acute Care (AC)** , **Community Living Center (CLC)** , **Observation (OBS)** , or Other (OT).
2. When prompted, enter the location’s IPEC Unit ID.

**Note:** This is the ID number that identifies this unit in IPEC which is only for Acute Care and CLC units reported to IPEC. Do not assign a Unit ID to any unit that is classified as OBS or Other. IPEC Unit IDs are available from the VHA MRSA Program Office and/or IPEC.

1. When prompted, enter the ward(s) in VistA to be included in the Geographical Unit.

**Note:** OBS patients should not be included in the number of admissions, discharges, and bed days of care that is reported to IPEC for the inpatient units; these patients are considered outpatients.  Therefore, sites should not generate a MRSA IPEC Report for any OBS units.  However, if desired, the site may run the Isolation Report or Nares Screen Compliance List for an OBS unit.

In order to prevent data from OBS wards erroneously reported to IPEC, sites should not map any OBS wards together with an inpatient ward (Acute Care or CLC). If the site desires the generation of the Isolation Report or Nares Screen Compliance List for an OBS unit, a separate Geographical Location should be utilized that includes the OBS ward only. For example, a site may have three wards in VistA entitled “4West Medicine”, “4West Surgery” and “4West OBS” and may desire to create a Geographical Location entitled “4West”; “4West” could consist of “4West Medicine” and “4West Surgery”.  In another scenario, a site may also wish to create a separate Geographical Location called “4West OBS” that could contain the “4West OBS” ward only.  However, in these examples, under no circumstances should the “4West OBS” ward be mapped together with the “4West Medicine” and “4West Surgery” wards under the same Geographical Location.

1. Enter the **&lt;TAB&gt;** key to get to the Command prompt.
2. At the command prompt, enter **S** and the **&lt;ENTER&gt;** key to save.
3. At the command prompt, enter **E** and the **&lt;ENTER&gt;** key to exit.
4. To return to the main menu, enter **^** and the **&lt;ENTER&gt;** key.

Figure 21: MDRO Tools Ward Mapping Setup

Select MDRO Tools Setup Menu Option: **MDRO Tools Ward Mapping Setup**

Select Geographical Unit: **11AB**

Are you adding '11AB' as a new MRSA WARD MAPPINGS (the 2ND)? No// **Y** (Yes)

MRSA WARD MAPPINGS TYPE: **ACUTE CARE**

MRSA WARD MAPPINGS IPEC UNIT ID: **999**

MDRO TOOLS WARD MAPPING SETUP

DIVISION: XXXXX VAMC

GEOGRAPHICAL UNIT: 11AB

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

WARD LOCATIONS:

**11AB**

**11ASURG**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                                Press &lt;PF1&gt;H for help

#### Deleting a Geographical Unit

To delete a Geographical Unit, perform the following steps:

1. Select the desired geographical unit.
2. Enter the **@** symbol and press the **&lt;ENTER&gt;** key.
3. When prompted, SURE YOU WANT TO DELETE THE ENTIRE ‘UNIT NAME’ MRSA WARD MAPPINGS? respond with **Y** and the **&lt;ENTER&gt;** key to delete the entire geographical unit from the setup.

he prograhe program will ask if the desired field  shoulto beuser can delete this information.  To do so,     Figure 22: MDRO Tools Ward Mapping Setup:  Deleting a Geographical Unit

Select MDRO Tools Setup Menu Option: **MDRO Tools Ward Mapping Setup**

DIVISION: XXXXX VAMC

SELECT GEOGRAPHICAL UNIT: PACU

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NAME:  PACU// **@**

SURE YOU WANT TO DELETE THE ENTIRE ‘PACU’ MRSA WARD MAPPINGS? **Y** (Yes)

### MDRO Historical Days Edit

This option allows the user to define the time frame selected for each MDRO defined in the MDRO Tools Lab Parameter Setup.  The information entered in this menu provides information for the Print Isolation Report option (the report displays patient’s historical lab data for certain MDROs).  The user will be asked to enter the number of historical days the program should search for a positive result for each MDRO.  This information can only be entered in days (e.g., 30 for 1 month; 90 for 1 quarter; 365 for 1 year). If no response is entered, the program will not display that MDRO on the Isolation Report.

**Note:** All sites must enter the following for MRSA in historical days: **365** ; this will ensure that the history of MRSA within the past year is identified for prevalence and transmission purposes.

For other MDROs selected, it is at the discretion of the facility to determine the time frame to search for the last positive MDRO result.

1. Select the division by entering it.  Press the **&lt;ENTER&gt;** key.  For a list of divisions, enter a ?
2. When prompted, enter the number of historical days the program should search for a positive result for each MDRO.

Figure 23: MDRO Historical Days Edit

Select MDRO Tools Setup Menu Option: **MDRO Historical Days Edit**

Select the Division: **XXXXX VAMC**

Enter the number of days to search for MRSA: **365**

Enter the number of days to search for IMP: **365**

Enter the number of days to search for VRE: **365**

Enter the number of days to search for C. diff: **28**

Enter the number of days to search for ESBL: **365**

### CRE Tools Site Parameter Setup

The CRE Tools Parameter Setup menu allows the user(s) to configure the CRE parameters for division(s) by either adding or editing specimens.

1. When prompted, enter the name of the division and press the **&lt;ENTER&gt;** key or press the **?** for a list of divisions and select the division from the list.
2. When prompted, select either Add to add a specimen for CRE Surveillance Screens or Edit to edit an existing specimen.
    - 2.1. If adding a specimen, type **Add** and press the **&lt;ENTER&gt;** key.  Enter the name of the specimen and press the **&lt;ENTER&gt;** key.
    - 2.2. If editing a specimen, type **Edit** and press the **&lt;ENTER&gt;** key.  Enter the name of the specimen and press the **&lt;ENTER&gt;** key.  To obtain a list of specimens, type **?** and the **&lt;ENTER&gt;** key.

Figure 24: CRE Tools Site Parameter Setup: Add a Specimen

Select MDRO Tools Setup Menu &lt;FACILITY ACCOUNT&gt; Option: 5  CRE Tools Site Parameter

Setup

Select CRE Site Parameters Division: ?

Answer with MDRO SITE PARAMETERS DIVISION

Choose from:

CASPER

CHEYENNE MOC

CHEYENNE VAMROC

FORT COLLINS

GREELEY

SIDNEY

You may enter a new MDRO SITE PARAMETERS, if you wish Enter the division the parameters are for.

Answer with MEDICAL CENTER DIVISION NUM, or NAME

Choose from:

1            CHEYENNE VAMROC     442

2            CASPER     442GA

3            FORT COLLINS     442GC

4            GREELEY     442GD

5            SIDNEY     442GB

6            CHEYENNE MOC     442HK

Select CRE Site Parameters Division: 1  CHEYENNE VAMROC     442

...OK? Yes//   (Yes)

Select one of the following:

A         ADD

E         EDIT

Do you want to Add or Edit specimen(s) for CRE Surveillance Screens: E// ADD

Select Specimen: FECES

Figure 25: CRE Tools Site Parameter Setup: Edit a Specimen

Select MDRO Tools Setup Menu &lt;FACILITY ACCOUNT&gt; Option: 5  CRE Tools Site Parameter

Setup

Select CRE Site Parameters Division: ?

Answer with MDRO SITE PARAMETERS DIVISION

Choose from:

CASPER

CHEYENNE MOC

CHEYENNE VAMROC

FORT COLLINS

GREELEY

SIDNEY

You may enter a new MDRO SITE PARAMETERS, if you wish Enter the division the parameters are for.

Answer with MEDICAL CENTER DIVISION NUM, or NAME

Choose from:

1            CHEYENNE VAMROC     442

2            CASPER     442GA

3            FORT COLLINS     442GC

4            GREELEY     442GD

5            SIDNEY     442GB

6            CHEYENNE MOC     442HK

Select CRE Site Parameters Division: 1  CHEYENNE VAMROC     442

...OK? Yes//   (Yes)

Select one of the following:

A         ADD

E         EDIT

Do you want to Add or Edit specimen(s) for CRE Surveillance Screens: E// EDIT

Select Specimen to delete: ?

Answer with SPECIMEN

Choose from:

FECES

SKIN

Enter the specimen you want to edit.

Select Specimen to delete: FECES

### Isolation Orders Add/Edit

The Isolation Orders Add/Edit option allows the user to enter the orderable item(s) at their site that are used for isolation purposes.  Each Isolation Order added must be mapped to one of the following Expanded Precaution Types: Contact Precautions, Contact Precautions Special, Airborne Infection, Droplet, Protective Environment, and Isolation Order.  The information entered will be used to populate the Print Isolation Report option.

**Note:** This option should only be used if the site uses orderable items when a patient is required to be in isolation.

1. Select the division.
2. At the Isolation Orders, enter an order and press &lt;TAB&gt;
3. At the Expanded Precaution Type, enter a precaution type and press **&lt;TAB&gt;** to return to the Isolation Orders field.
4. When finished, enter the **&lt;TAB&gt;** key at the Isolation Orders field.
5. At the Command prompt, enter **S** to save the form and press the **&lt;ENTER&gt;** key.
6. At the Command prompt, enter **E** to exit the form and press the **&lt;ENTER&gt;** key.

Figure 26: MDRO Tools Isolation Orders Setup

MDRO TOOLS ISOLATION ORDERS SETUP

DIVISION: XXXXX VAMC

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Isolation Orders				Expanded Precaution Type

**CONTACT PRECAUTIONS                CONTACT PRECAUTIONS**

**CONTACT PRECAUTIONS SPECIAL  	CONTACT PRECAUTIONS SPECIAL**

**AIRBORNE INFECTION ISOLATIOTI	AIRBORNE INFECTION**

**DROPLET PRECAUTIONS                DROPLET**

**PROTECTIVE ENVIRONMENT             PROTECTIVE ENVIRONMENT**

**ISOLATION ORDER                    ISOLATION ORDER**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                             Press &lt;PF1&gt;H for help

### MDRO Tools Reports Menu

After the five options in the MRSA Tools Setup Menu have been configured, reports may be printed for a particular Division and/or Unit from the MRSA Tools Reports Menu. The following options are available from the MRSA Tools Reports Menu:

- Print MRSA IPEC Report
- Print Isolation Report
- Print Nares Screen Compliance List
- Print CDI Report
- Print CRE Report

Figure 27: MDRO Tools Reports Menu

MDRO Tools Reports Menu

1      Print MRSA IPEC Report

2      Print Isolation Report

3      Print Nares Screen Compliance List

4      Print CDI Report

5      Print CRE Report

Select MDRO Tools Reports Menu &lt;TEST ACCOUNT&gt; Option:

#### MRSA IPEC Report

The MRSA IPEC Report is used to obtain all pertinent information for data entry into IPEC for Facility-Wide Prevalence Measures and Unit-Specific Prevalence and Transmission Measures.

The Admission Report uses unit admission dates, while the Discharge Report uses unit discharge dates.  For example, if the Admission Report is set to run for the CCU for the month of February 2017, it will display all patients admitted into the CCU during February 2017, regardless of when they were discharged from the unit (or if they still remain on the unit).  If the Discharge Report is run for February 2017, it will display all patients that were discharged from the CCU during February 2017, regardless of when they entered the unit. The Discharge report will also display all patients that were still on the unit at the end of February.

More information regarding the reports follow in this section.

**Note:** The MRSA IPEC Report should be run no earlier than 5 business days after the close of the month.  This allows the laboratory to complete testing and enter the results into VistA.  This is a suggested timeframe; it will be dependent on the laboratory practices at each facility.

**Note:** The MRSA IPEC Report should be run monthly to gather the required data for entry into IPEC.  The reports are not meant for daily monitoring.  Daily monitoring can be conducted using the Isolation Report and Nares Screen Compliance Report.

To generate the report, perform the following steps:

1. When prompted, select the report; choose either the Admission Report or Discharge/Transmission Report.
2. When prompted, enter a start date to run the report and an end date for the report.

**Note:** Reports should be run beginning with the first day of the month and should end with the last day of the month.

1. When prompted, enter the Geographical Locations for the report.

**Note:** The report can be run for one unit or all units.  Only Geographical Units created using the MRSA Tools Ward Mapping Setup option may be selected.  The report is designed for a 176 column format (landscape).

**Note:** Do not generate a MRSA IPEC Report for any Geographical Unit that is an OBS unit.

Figure 28: Print MRSA IPEC Report

Select MRSA Tools Reports Menu Option: **Print MRSA IPEC Report**

Select the Division: XXXXX VAMC

Select one of the following:

A         Admission Report

D         Discharge/Transmission Report

Run (A)dmission Or (D)ischarge/Transmission Report: Admission Report

Begin with ward admission date: **020117** (FEB 01, 2017)

End with ward admission date: **022817** (FEB 28, 2017)

Do you want to select all locations? NO//

Select Geographical Location: **11AB**

Select another Geographical Location:

Do you want to only print the summary report? NO//

This report is designed for a 176 column format (landscape).

DEVICE: HOME// **IDM1$PRT LANDSCAPE**

#### Admission Report

The Admission Report displays the listing of patients that have been admitted to the unit for the calendar month.  If a patient was admitted to the unit multiple times during the calendar month, then the patient will be displayed for each admission to the unit.

Figure 29: Print MRSA IPEC Admission Report

MRSA IPEC ADMISSION REPORT

GEOGRAPHICAL LOCATION:  11AB

Report period:  Oct 01, 2016 to Oct 31, 2016@24:00

Report printed on: Jan 16, 2017@14:07:26                                PAGE: 1

NARES   NARES   CULTURE

DATE                MAS MOVE      SCREEN  RESULT  RESULT   MRSA IN

WARD     PATIENT              SSN    ENTERED WARD   ADT  TYPE          24H     48H     48H      PAST YEAR

---------------------------------------------------------------------------------------------------------

11ABSURG *XXXXXXXXXXXXXXXXXX  XXXX   10/1/16@09:43  A    DIRECT        Y

11ABSURG  XXXXXXXXXXXXXXXXXX  XXXX   10/1/16@16:11  T    INTEWARD TRA  Y

11ABMED  *XXXXXXXXXXXXXXXXXX  XXXX   10/1/16@20:25  A    DIRECT        Y

11ABSURG *XXXXXXXXXXXXXXXXXX  XXXX   10/1/16@23:49  A    DIRECT        Y

11ABSURG *XXXXXXXXXXXXXXXXXX  XXXX   10/1/16@19:57  A    DIRECT

11ABMED  *XXXXXXXXXXXXXXXXXX  XXXX   10/1/16@11:01  A    DIRECT        Y

11ABSURG *XXXXXXXXXXXXXXXXXX  XXXX   10/13/16@13:42 A    DIRECT        Y        POS

11ABMED  *XXXXXXXXXXXXXXXXXX  XXXX   10/13/16@18:41 A    DIRECT        Y

11ABSURG  XXXXXXXXXXXXXXXXXX  XXXX   10/20/16@23:14 T    INTERWARD TRA Y

11ABMED   XXXXXXXXXXXXXXXXXX  XXXX   10/21/16@14:34 T    INTERWARD TRA Y        POS             POS

11ABSURG *XXXXXXXXXXXXXXXXXX  XXXX   10/23/16@01:19 A    DIRECT        Y        POS

11ABSURG *XXXXXXXXXXXXXXXXXX  XXXX   10/13/16@13:42 A    DIRECT        Y

A description for the headings from the report are outlined in the table below.

Table 5: Descriptions for MRSA IPEC Admission Report

| Heading            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WARD               | The patient was admitted or transferred into this Ward location.                                                                                                                                                                                                                                                                                                                                                                           |
| PATIENT            | The patient’s last name, followed by first name.  An asterisk (*) before the patient’s name denotes that the patient was indicated for a nasal screen upon admission to the unit based on the site’s business rules.                                                                                                                                                                                                                       |
| SSN                | The last 4 digits of the patient’s social security number                                                                                                                                                                                                                                                                                                                                                                                  |
| DATE ENTERED WARD  | The date patient was admitted or transferred into the unit.                                                                                                                                                                                                                                                                                                                                                                                |
| ADT                | How the patient entered the unit, either by: admission or transfer into the unit.                                                                                                                                                                                                                                                                                                                                                          |
| MAS MOVE TYPE      | The type of Medical Administration Service (MAS) movement.                                                                                                                                                                                                                                                                                                                                                                                 |
| NARES SCREEN 24H   | This will be a Y (yes) if the patient received a nares screen within 24 hours of arriving on the unit. Only tests that follow the new MRSA lab standards will be captured.  **Note:**  The test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA.                                                                                                                                                                        |
| NARES RESULT 48H   | This will be POS (positive) if the patient’s nares screen or surveillance culture was positive within 48 hours of admission/transfer into the unit. Only tests that follow the new MRSA lab standards will be captured.  **Note:**  For nares screens, the test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA; for surveillance cultures the test names must be called MRSA SURVL OTHER AGAR or MRSA SURVL OTHER DNA. |
| CULTURE RESULT 48H | This will be POS (positive) if the patient had a clinical culture and it was positive within 48 hours of admission/transfer-in to the unit. Only cultures that were reported using the new MRSA lab standards will be captured.  **Note:**  The site must report positives cultures using the Etiology STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA).                                                                                 |
| MRSA IN PAST YEAR  | The patient’s MRSA history going back one year prior to admission/transfer into the unit until the date/time of admission/transfer in.  It will display a POS, if the patient ever had a positive nares screen, surveillance culture or clinical culture for MRSA in the past year. The program will determine a MRSA positive based on the parameter setup and national standards for laboratory reporting of MRSA.                       |

#### Admission Summary Report

The Admission Summary Report displays all pertinent information to enter Prevalence Measure data into the Inpatient Evaluation Center (IPEC).  The report displays Facility-Wide and Unit-Specific information.

The report will print a summary report for each unit.  If multiple units were printed together, then an additional summary report will print which will contain a summary for all the units combined. This combined summary report can be useful to obtain the Facility-Wide prevalence measures that are required entries into IPEC, thereby eliminating the task of adding all the individual Facility wide measures together.

Figure 30: MRSA IPEC Admission Summary Report

MRSA IPEC ADMISSION SUMMARY REPORT

Geographical Location:  11AB

Report period:  Oct 01, 2016 to Oct 31, 2016@24:00

Report printed on:  Jan 16, 2017@14:07:26                                     PAGE: 2

Prevalence Measures (Facility Wide)

1. Number of Admissions to the facility:  31

2. Number of (1) who received MRSA nasal screening upon admission to facility:  28

3. Number of (1) positive for MRSA based on nasal screening upon admission to facility:  5

4. Number of those in (1) positive for MRSA based on clinical cultures upon admission to facility: 0

Prevalence Measures (Unit Specific)

1. Number of admissions (admissions + transfers in) to the unit for the month:  41

2. Number of (1) for whom nasal screening was indicated:  41

3. Number of (2) who received nasal screening upon admission to unit (within 24 hours):  38

4. Number of (1) positive for MRSA based on nasal screening upon admission to unit:  6

5. Number of (1) positive for MRSA based on clinical cultures upon admission to unit:  0

A description for the headings from the report are outlined in the tables below.

Table 6:  Descriptions for Prevalence Measures (Facility Wide)

| Heading                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of admissions to the facility                                                           | Direct admissions to the facility for the calendar month.  **Note:**  This includes all admissions (direct, non-service connected, etc.) and TO ASIH admissions; it does not include unit-to-unit transfers.                                                                                                                                                                                         |
| Number of (1) who received MRSA nasal screening upon admission to facility                     | Direct admissions who received a MRSA nasal screen within 24 hours of admission to the facility.                                                                                                                                                                                                                                                                                                     |
| Number of (1) positive for MRSA based on nasal screening upon admission to facility            | Direct admissions who received a MRSA nares screen or surveillance culture within 48 hours of arriving to the facility and results were positive for MRSA, plus those direct admissions that had a prior history of MRSA in the past 12 months based on nares screen or clinical culture. Patients who had a positive clinical culture within 48 hours of arriving to the facility will be excluded. |
| Number of those in (1) positive for MRSA based on clinical cultures upon admission to facility | Direct admissions that had a clinical culture upon admission to the facility and results were positive within 48 hours of admission.  **Note:**  If a patient has a positive nares screen or history of MRSA, and positive clinical culture, it is counted once under the clinical culture category.                                                                                                 |

Table 7: Descriptions for Prevalence Measures (Unit Specific)

| Heading                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of admissions (admissions + transfers) into the unit for the month                | Direct admissions plus transfers into the unit for the calendar month.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Number of (1) for whom nasal screening was indicated                                     | The number of admissions and transfers into the unit for the calendar month for whom a nasal screen was indicated.  The program will determine this information based on the site parameters entered during setup.  If the admitting unit at a site does not screen patients on unit-to-unit transfers, but the discharging unit does, then only Facility admissions will be indicated for a swab.  If a site does not screen patients with MRSA history on transfers into the unit, then a patient with a known MRSA history (within 365 days prior to entering the unit) will not be indicated for a swab on unit-to-unit transfers. To be considered “known positive” the lab result must have been verified before the patient entered the unit.  **Note:**  This is different from the column heading MRSA IN PAST YEAR, where the collection date, not the verification date, was used. |
| Number of (2) who received MRSA nasal screening upon admission to unit (within 24 hours) | Admissions and transfers into the unit for the calendar month that were indicated for a MRSA nares screen and who received a MRSA nasal screen within 24 hours of admission to the unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Number of (1) positive for MRSA based on nasal screening upon admission to unit          | Admissions and transfers into the unit for the calendar month who received a MRSA nares screen or surveillance culture within 48 hours of arriving to the unit and results were positive for MRSA, plus those admissions and transfers into the unit that had a prior history of MRSA in the past 12 months, either by nares screen or clinical culture. Patients who had a positive clinical culture within 48 hours of arriving to the unit will be excluded.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Number of (1) positive for MRSA based on clinical cultures upon admission to unit        | Admissions and transfers into the unit who had a clinical culture upon admission to the unit and results were positive within 48 hours of admission to unit.  **Note:**  If a patient has a positive nares screen or history of MRSA, and positive clinical culture, it is counted once under the clinical culture category.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

#### Discharge/Transmission Report

The Discharge/Transmission Report displays all discharges that occurred for the calendar month.  It also includes all patients that were still on the unit at the end of the calendar month.  If a patient was discharged from the unit more than once, they will show up multiple times.

Figure 31: MRSA IPEC Discharge/Transmission Report

**MRSA IPEC DISCHARGE/TRANSMISSION REPORT**

**Geographical Location: 11AB**

**Report period:  Oct 01, 2016 to Oct 31, 2016@24:00**

**Report printed on:  Jan 16, 2017#14:25:15                                                                                              PAGE: 1**

**ADM            NARES   NARES                                 DIS            NARES   NARES    MRSA**

**DATE            ADM  MAS MOVE       SCREEN  RESULT  MRSA IN  DATE            DIS  MAS MOVE       SCREEN  RESULT   IN CURR**

**WARD   PATIENT            SSN  ENTERED WARD    ADT  TYPE           24H     48H     PAST YR  LEFT WARD       ADT  TYPE           24H     48H      PRD      TRANS**

**---------------------------------------------------------------------------------------------------------------------------------------------------------------**

**11ABS   XXXXXXXXXXXXXXX   XXXX 9/7/16@17:51    T    INTERWARD TRA                  POS      10/27/16@18:20  D    NON-SERVICE C  Y**

**11ABM  *XXXXXXXXXXXXXXX   XXXX 9/26/16@18:17   A    DIRECT         Y       POS              10/12/16@15:24  D    MPM=SERVICE C**

**11ABS   XXXXXXXXXXXXXXX   XXXX 9/27/16@16:26   T    INTERWARD TRA  Y       POS     POS      10/1/16@12:07   T    INTERWARD TRA  Y       POS      POS**

**11ABM  *XXXXXXXXXXXXXXX   XXXX 9/28/16@19:58   A    DIRECT         Y                        10/2/16@21:22   D    MOM-SERVICE C**

**11ABS  *XXXXXXXXXXXXXXX   XXXX 9/28/16@20:03   A    DIRECT         Y                        10/2/16@21:12   D    TRANSFER OUR   Y**

**11ABS  *XXXXXXXXXXXXXXX   XXXX 9/28/16@22:11   A    DIRECT         Y                        10/1/16@16:40   D    NON-SERVICE C  Y**

**11ABM   XXXXXXXXXXXXXXX   XXXX 10/13/16@13:42  A    DIRECT         Y       POS     POS      10/14/16@23:57  D    IRREGULAR              POS**

**11ABS  *XXXXXXXXXXXXXXX   XXXX 10/14/16@15:11  A    DIRECT         Y                        10/26/16@17:21  D    NON-SERVICE C  Y**

**11ABS  *XXXXXXXXXXXXXXX   XXXX 10/16/16@11:05  T    INTERWARD TRA  Y                        10/18/16@19:50  T    INTEWARD TRA   Y**

**11ABS  *XXXXXXXXXXXXXXX   XXXX 10/16/16@17:35  A    DIRECT         Y                        10/20/16@13:10  D    NON-SERVICE C  Y       POS       POS      T**

**11ABS  *XXXXXXXXXXXXXXX   XXXX 10/17/16@17:00  A    DIRECT         Y                        10/17/16@22:19  T    INTERWARD TRA**

A description for the headings from the report are outlined in the table below.

Table 8: Descriptions for MRSA IPEC Discharge/Transmission Report

| Heading           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WARD              | The patient was admitted/transferred into this Ward location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PATIENT           | Patient’s last name, followed by first name.  An asterisk (*) before the patient’s name denotes that the patient was indicated for a nasal screen upon discharge from the unit based on the site’s business rules.                                                                                                                                                                                                                                                                                                                                                                                                           |
| SSN               | The last 4 digits of the patient’s social security number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DATE ENTERED WARD | The date patient was admitted or transferred into the unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADM ADT           | How the patient entered the ward, either by admission or transfer into the unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| MAS MOVE TYPE     | The type of Medical Administration Service (MAS) movement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| NARES SCREEN 24H  | This will be Y (yes) if the patient received a nares screen within 24 hours of arriving on the unit.  Only tests that follow the new MRSA laboratory standards will be captured.  **Note:**  The test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA.                                                                                                                                                                                                                                                                                                                                                    |
| NARES RESULT 48H  | This will be POS (positive) if the patient’s nares screen or surveillance culture was positive within 48 hours of admission to the unit. Only tests that follow the new MRSA lab standards will be captured.  **Note:**  For nares screens, the test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA; for surveillance cultures they must be called MRSA SURVL OTHER AGAR or MRSA SURVL OTHER DNA.                                                                                                                                                                                                        |
| MRSA IN PAST YEAR | The patient’s MRSA history going back one year prior to admission until 48 hours after admission.  It will display a POS, if the patient ever had a positive nares screen, surveillance culture or clinical culture for MRSA in the past year.  Begin time frame: (Admission – 365 days) or (report start date – 365 days); use the later timeframe.  End time frame: (Admission + 48 hours) or (report start date); use the later timeframe.  **Note:**  The program will determine a MRSA positive based on the parameter set-up (MDRO Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA. |
| DATE LEFT WARD    | Date the patient left the unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DIS ADT           | How the patient left the unit:  Discharge or Transfer-out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DIS MAS MOVE TYPE | Type of discharge movement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| NARES SCREEN 24H  | Y (yes) if the patient had a nares screen within 24 hours of being discharged from the unit. Only tests that follow the new MRSA lab standards will be captured.  **Note:**  The test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA.                                                                                                                                                                                                                                                                                                                                                                    |
| NARES RESULT 48H  | POS (positive) if the patient’s nares screen or surveillance culture was positive within 48 hours of exiting the unit.  Only tests that follow the new MRSA lab standards will be captured.  **Note:**  For nares screens, the test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA; for surveillance cultures they must be called MRSA SURVL OTHER AGAR or MRSA SURVL OTHER DNA.                                                                                                                                                                                                                         |
| MRSA IN CURR PRD  | POS (positive) if the patient had a positive MRSA nasal screen, surveillance culture or clinical culture during the current admission.  - Begin time frame: (Admission + 48 hours) or (Report start date); use the later timeframe.  - End time frame: (Discharge + 48 hours) or (Report end date); use the earlier timeframe.  **Note:**  The program will determine what’s considered a MRSA positive based on the parameter set-up (MDRO Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.                                                                                              |
| TRANS             | T if the patient had a transmission within the selected time range.  **Note:**  Transmission is defined as a patient with a negative nares screen within 48 hours of admission to the unit (NARES RESULT 48H) and no history of MRSA within the past 365 days (MRSA IN PAST YEAR).  In addition, on transfer and/or discharge from the unit the patient must have a positive nares screen (NARES RESULT 48H), or be positive for MRSA during the current admission (MRSA IN CURR PRD).                                                                                                                                       |

#### Discharge/Transmission Summary Report

The Discharge/Transmission Summary Report displays all pertinent information to enter Transmission Measure data into the Inpatient Evaluation Center (IPEC).  The report displays information for Unit-Specific data entry.

Figure 32: MRSA IPEC Discharge/Transmission Summary Report

MRSA IPEC DISCHARGE/TRANSMISSION SUMMARY REPORT

Geographical Location: SICU

Report period: Mar 01, 2017 to Mar 15, 2017@24:00                PAGE: 1

Transmission Measures (Unit Specific)

10. Number of bed days of care for the unit: 115

11. Number of exits (discharges + deaths + transfers out) from the unit:  33

12. Number of (11) for whom a discharge/transfer swab was indicated:  33

13. Number of (12) who received MRSA nasal screening upon exit from unit:  31

14. Number of MRSA transmissions on unit based on MRSA nasal screening or clinical cultures: 0

A description for the headings from the report are outlined in the table below.

**Table 9: Descriptions for Transmission Measures (Unit Specific)**

| Heading                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of bed days of care for the unit                                                 | Bed days of care for the unit for the calendar month.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Number of exits (discharges + deaths + transfers out) from the unit                     | The number of exits (discharges/deaths/transfers out) from the unit for the calendar month.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Number of (11) for whom a discharge/transfer swab was indicated                         | The number of discharges, deaths and transfer out from the unit for the calendar month, for whom a nasal screen was indicated.  The program will determine this information based on the site parameters entered during setup.  **Note:**  If the discharging unit at a site does not screen patients on unit-to-unit transfers (but the admitting unit does), then only facility discharge(s) or death will be indicated for a swab.  **Note:**  If a site does not screen patients with MRSA history on discharge/death/transfer-outs, then a patient with a known MRSA history (within 365 days prior to leaving the unit) will not be indicated for a swab. To be considered “known positive” the lab result must have been verified before the patient left the unit.  **Note:**  This is different than the column heading MRSA IN PAST YEAR, where the collection date (not verification date) was used. |
| Number of (12) who received MRSA nasal screening upon exit from the unit                | Those discharges, deaths and transfers out who were indicated for a MRSA nares screen and received a MRSA nares screen within 24 hours from exit from the unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Number of MRSA transmissions on unit based on MRSA nasal screening or clinical cultures | The number of transmissions on the units for the calendar month identified either by MRSA nares screen or clinical culture, while taking into account the patient’s history of MRSA in the past 12 months.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

#### Print Isolation Report

The Print Isolation Report is an optional report.  It can be used to print a ward census and will identify patients on the unit that have a selected MDRO (i.e., MRSA, CRB-R, VRE, C. diff, VRE, ESBL).  The report displays real-time unit-specific patient information and is based on the information entered in the parameter setup (MDRO and Historical Days, and Isolation Orders, if applicable).  The report will display the patient’s last known positive MDRO and active Isolation Orders if this information is used by the facility.

The report is designed for a 176 column (landscape) format.

Figure 33: Print Isolation Report Option

Select MRSA Tools Reports Menu Option: **Print Isolation Report**

Select the Division: **XXXXX VAMC**

Do you want to select all locations? NO//

Select Geographical Location: 11AB

Select another Location:

This report is designed for a 176 column format (landscape).

DEVICE: HOME// **IDM1$PRT LANDSCAPE**

The Print Isolation Report may be tasked to print to a specific unit at one or more specific times of day which will allow the unit to identify patients to be placed in contact precautions and to see if any Isolation Orders have been ordered for the patient.  See information regarding the Print Isolation Report (Tasked) for configuration instructions for this option.

Figure 34: Isolation Report

**CENSUS LIST AND MDRO HISTORY**

**Geographical location:  11AB**

**Report printed on: Mar 05, 2017@14:28:10                                                      PAGE: 1**

**LAST MRSA POS  LAST CRB-R POS  LAST ESBL POS    LAST VRE POS    LAST CDF POS**

**PATIENT              SSN    IN 365 DAYS    IN 365 DAYS     IN 356 DAYS      IN 365 DAYS     IN 28 DAYS     ISOLATION ORDER              START DATE**

**--------------------------------------------------------------------------------------------------------------------------------------------------**

**XXXXXXXXXXXXXXXXXXX  XXXX                                                                                  CONTACT PRECAUTIONS          3/1/16**

**XXXXXXXXXXXXXXXXXXX  XXXX**

**XXXXXXXXXXXXXXXXXXX  XXXX   2/28/16@17:00  6/1/16@13:30    5/13/16@15:15    6/5/16@13:30                   CONTACT PRECAUTIONS          2/27/16**

**XXXXXXXXXXXXXXXXXXX  XXXX   2/28/16@17:00  6/1/16@13:30    5/13/16@15:15    6/5/16@13:30                   CONTACT PRECAUTIONS          11/13/16**

**XXXXXXXXXXXXXXXXXXX  XXXX   10/7/16@21:57**

**XXXXXXXXXXXXXXXXXXX  XXXX**

**XXXXXXXXXXXXXXXXXXX  XXXX   2/25/16@15:05                                   5/14/16@20:01                  CONTACT PRECAUTIONS          2/25/16**

**XXXXXXXXXXXXXXXXXXX  XXXX**

**XXXXXXXXXXXXXXXXXXX  XXXX**

**XXXXXXXXXXXXXXXXXXX  XXXX   3/3/16@18:44                                                                   CONTACT PRECAUTIONS          3/4/16**

A description for the headings from the report are outlined in the table below.

Table 10: Descriptions for Census List and MDRO History

| Heading           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PATIENT           | The patient’s last name, followed by first name.                                                                                                                                                                                                                                                                                                                                                                                                           |
| SSN               | The last 4 digits of the patient’s social security number.                                                                                                                                                                                                                                                                                                                                                                                                 |
| MRSA IN 365 DAYS  | The last positive MRSA result (either by nares screen, surveillance culture or clinical culture) in the past 365 days.  **Note:**  The program will determine a MRSA positive based on the parameter setup (MDRO Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.                                                                                                                                                       |
| CRB-R IN XXX DAYS | The last positive CRB-R result in the past XXX day; it is optional.  It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).  **Note:**  The program will determine a CRB-R positive based on the parameter set-up (MDRO Tools Lab Parameter Setup).                                                                                           |
| ESBL IN XXX DAYS  | The last positive ESBL result in the past XXX days; it is optional.  It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).  **Note:**  The program will determine an ESBL positive based on the parameter set-up (MDRO Tools Lab Parameter Setup).                                                                                           |
| VRE IN XXX DAYS   | This will display the last positive VRE result in the past XXX days; it is optional.  It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).  **Note:**  The program will determine a VRE positive based on the parameter set-up (MDRO Tools Lab Parameter Setup).                                                                            |
| CDIFF IN XXX DAYS | Last positive C. difficile result in the past XXX days; it is optional.  It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).  **Note:**  The program will determine a C. diff positive based on the parameter set-up (MDRO Tools Lab Parameter Setup).                                                                                     |
| ISOLATION ORDER   | Type of Isolation Order the provider has ordered for the patient.  Note that the information will only be displayed if the site uses Isolation Orders; the information about Isolation Orders was added during the initial set-up (using option Isolation Orders Add/Edit).  If more than one Isolation Order has been ordered for the patient, then the patient will be listed multiple times on the report, dependent on the number of Isolation Orders. |
| START DATE        | Start Date for the Isolation Order that the provider ordered for the patient.  Note that the information will only be displayed if the site uses Isolation Orders, and information about Isolation Orders was added during the initial set-up (using option Isolation Orders Add/Edit).                                                                                                                                                                    |

#### Print Nares Screen Compliance List

The Print Nares Screen Compliance List is an optional report.  If desired, the report may be used to print a ward census and identify if a MRSA nares screen was ordered for the patient.  The report prints real-time patient information on the unit and is designed for a 132 column (compressed) format.

Figure 35: Nares Screen Compliance List

Select MRSA Tools Reports Menu Option: **Print Nares Screen Compliance List**

Select the Division: **XXXXX VAMC**

Do you want to select all locations? NO//

Select Geographical Location: 11AB

Select another Location:

This report is designed for a 132 column format (compressed).

DEVICE: HOME// **IDM1$PRT COMPRESSED**

Figure 36: Nares Swab Order List

NARES SWAB ORDER LIST

Geographical Location: 11AB

Report printed on: Mar 02, 2017@15:31:27                           PAGE: 1

DATE               MRSA IN   NARES                  LAB

PATIENT                  SSN   ENTERED WARD   ADT PAST YEAR ORDERED ORDER DATE     RECEIVED

-------------------------------------------------------------------------------------------

XXXXXXXXXXXXXXX          XXXX  2/27/17@19:13  T   POS       YES     2/27/17@18:53  YES

XXXXXXXXXXXXXXX          XXXX  2/27/17@19:37  A             YES     2/27/17@23:30  YES

XXXXXXXXXXXXXXX          XXXX  2/24/17@18:37  A   POS       YES     2/24/17@22:05  YES

XXXXXXXXXXXXXXX          XXXX  3/2/17@14:19   A

XXXXXXXXXXXXXXX          XXXX  3/2/17@02:48   A             YES     3/2/17@07:00   YES

XXXXXXXXXXXXXXX          XXXX  3/1/17@13:40   A             YES     3/1/17@14:15   YES

XXXXXXXXXXXXXXX          XXXX  2/22/17@11:02  T   POS       YES     2/22/17@01:48  YES

A description for each of the headings from the report are outlined in the table below.

Table 11: Descriptions for Nares Screen Compliance List

| Heading           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PATIENT           | Patient’s last name, first name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SSN               | Last 4 digits of the patient’s social security number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DATE ENTERED WARD | Date the patient was admitted to the unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ADT               | How the patient entered the ward:  Admission or Transfer-In to the unit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| MRSA IN PAST YEAR | POS (positive) if the patient had a positive MRSA result (either by nares screen or clinical culture).  **Note:**  The program will determine a MRSA positive based on the parameter set-up (MDRO Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.                                                                                                                                                                                                                                                                                      |
| NARES ORDERED     | If a nares screen was ordered for the patient, the report starts searching for a nares screen beginning 24 hours before admission – going forward. The first active or completed order it finds once it starts searching, is the order that gets displayed on the report. If there are no active or completed orders, then the first pending order within that time frame will be displayed.  **Note:**  Only orders for tests that follow the new MRSA lab standards will be picked up (the test names must be called ‘MRSA SURVL NARES AGAR’ or ‘MRSA SURVL NARES DNA’). |
| ORDER DATE        | Date the nares screen was ordered for the patient.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| LAB RECEIVED      | If the nares screen was received in the lab, labs received will be utilized during the search by the program.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

The Print Nares Screen Compliance List report can be tasked to print to a specific unit at one or more specified times of the day.  This allows the unit to determine if a patient did not have a nares screen upon admission and to obtain one, if needed.

**Note:** The Print Nares Screen Compliance List report is based on the laboratory standards for the following test names:  MRSA SURVL NARES DNA and MRSA SURVL NARES AGAR.  If the standards have not been implemented or have been set up incorrectly, then the report will not display accurate information.

#### Print CDI Report

#### Printing the CDI Report to a Printer

**Note:** Before running the report, ensure that the laboratory test(s), e.g., the Clostridium Difficile Etiology, are configured in the MDRO TOOLS LAB SEARCH/EXTRACT file (#104.1).  To configure the lab test(s), use the MDRO Tools Lab Parameter Setup option.

To generate the report, perform the following steps:

1. From the MDRO Tools Reports Menu, enter **4** for Print CDI Report and press the **&lt;ENTER&gt;** key.
2. At the Do you want to select all Divisions: NO// prompt, enter either **Yes** or **No** based on the following criteria:
    - 2.1. Entering **Yes** will obtain results for all divisions.
    - 2.2. Entering **No** will obtain results for a particular division or divisions.  After No is entered, a prompt will be displayed to enter the name of the division. Enter the name of the division and press the **&lt;ENTER&gt;** key.  If desired, enter additional divisions.

**Note** : The prompt will not display for a facility that is setup as a Single Division, it will only display for a Multi-Division Facility.

1. At the prompt, Beginning POS CDI Lab ID Event (Collection) Date: Nov 12, 2015// enter a start date to run the report or accept the default for 365 days.
2. At the prompt Ending POS CDI Lab ID Event (Collection) Date: enter an end date. **Note:** An end date must be entered to run the report.
3. At the prompt, Device: HOME//, enter the name of the printer.

**Note:** This report is designed for a 132 column format (compressed).

Figure 37: Example of Printing the CDI Report for a Division

Select MDRO Tools Reports Menu &lt;TEST ACCOUNT&gt; Option: 4  Print CDI Report

Do you want to select all divisions: NO// n NO

Select Division:      CHEYENNE VAMROC

Select another Division:

Beginning POS CDI Lab ID Event (Collection) Date: Jan 21, 2016//0811  (AUG 11, 2016)

Ending POS CDI Lab ID Event (Collection) Date: 0818  (AUG 18, 2016)

This report is designed for a 132 column format (compressed).

DEVICE: HOME// ;180;999  HOME  (CRT)

FACILITY CDI CASES REPORT

Division: CHEYENNE VAMROC

Geographical Location: C MEDICINE

Report printed on: Jan 19, 2017@11:38:37                      PAGE: 1

PATIENT                  SSN  DOB         CDI Event D/T               ADM D/T             LOCATION       DC D/T                   PREV CDI Event D/T

---------------------------------------------------------------------------------------------------------------------------------------------------------------

SQA,TESTPATIENTFOUR      5543 04/13/1969  8/14/16 08:00               8/13/16 00:39:23    C MEDICINE       8/13/16 17:31:37

FACILITY CDI CASES REPORT

Division: CHEYENNE VAMROC

Geographical Location: CHY ANTICOAG

Report printed on: Jan 19, 2017@11:38:37                      PAGE: 2

PATIENT                  SSN  DOB         CDI Event D/T               ADM D/T             LOCATION       DC D/T                   PREV CDI Event D/T

---------------------------------------------------------------------------------------------------------------------------------------------------------------

SQA,TESTPATIENTONE       0090 09/05/1989  8/13/16 08:00               CHY ANTICOAG

SQA,TESTPATIENTTWO       4412 07/30/1969  8/13/16 09:00               CHY ANTICOAG

FACILITY CDI CASES REPORT

Division: CHEYENNE VAMROC

Geographical Location: CLC

Report printed on: Jan 19, 2017@11:38:37                      PAGE: 3

PATIENT                  SSN  DOB         CDI Event D/T               ADM D/T             LOCATION       DC D/T                   PREV CDI Event D/T

---------------------------------------------------------------------------------------------------------------------------------------------------------------

SQA,TESTPATIENTFOUR      5543 04/13/1969  8/16/16 12:26:15            8/13/16 00:39:23    ICU-M                                   8/14/16 08:00

SQA,TESTPATIENTTHREE     2254 05/14/1977  8/13/16 17:25:25            8/13/16 00:36:44    ICU-M

SQA,TESTPATIENTTWO       4412 07/30/1969  8/14/16 22:25:16            8/14/16 22:06:52    ICU-M                                   8/13/16 09:00

SQA,TESTPATIENTTWO       4412 07/30/1969  8/16/16 12:37:27            8/14/16 22:06:52    ICU-M                                   8/16/16 10:45:11

**Figure 38: Rendition of Printing the CDI Report to a Printer**

FACILITY CDI CASES REPORT

Division: CASPER

Geographical Location: ICU-M

Report printed on: Dec 16, 2016@13:20:44                      PAGE: 1

PATIENT          SSN  DOB         CDI Event D/T     ADM D/T          LOCATION PREV CDI Event D/T

DC D/T

----------------------------------------------------------------------------

XXXXXXXXXXXXXXX  XXXX 04/13/1969  8/16/16 12:26:15  8/13/16 00:39:23 ICU-M    8/14/16 08:00

XXXXXXXXXXXXXXX  XXXX 05/14/1977  8/13/16 17:25:25  8/13/16 00:36:44 ICU-M    8/15/16 08:00

XXXXXXXXXXXXXXX  XXXX 07/30/1969  8/14/16 22:25:16  8/14/16 22:06:52 ICU-M    8/13/16 09:00

XXXXXXXXXXXXXXX  XXXX 07/30/1969  8/16/16 12:37:27  8/14/16 22:06:52 ICU-M    8/16/16 10:45:11

#### Displaying the CDI report to screen.

**Note:** Before running the report, ensure that the laboratory test(s), e.g., the Clostridium Difficile Etiology, are configured in the MDRO TOOLS LAB SEARCH/EXTRACT file (#104.1).  To configure the lab test(s), use the MDRO Tools Lab Parameter Setup option.

To generate the report, perform the following steps:

1. From the MDRO Tools Reports Menu, enter **4** for Print CDI Report and press the **&lt;ENTER&gt;** key.
2. At the Select Division: prompt, enter the name of the Division.
3. At the Do you want to select all Divisions: NO// prompt, enter either **Yes** or **No** based on the following criteria:
    - 3.1. Entering **Yes** will obtain results for all divisions.
    - 3.2. Entering **No** will obtain results for a particular division or divisions.  After No is entered, a prompt will be displayed to enter the name of the division. Enter the name of the division and press the **&lt;ENTER&gt;** key. If desired, enter additional divisions.

**Note** : The prompt will not display for a facility that is setup as a Single Division, it will only display for a Multi-Division Facility.

1. At the prompt, Beginning POS CDI Lab ID Event (Collection) Date: Nov 12, 2015// enter a start date to run the report or accept the default for 365 days.
2. At the prompt Ending POS CDI Lab ID Event (Collection) Date: enter an end date. **Note:** An end date must be entered to run the report.
3. At the prompt, Device: HOME//, press the **&lt;ENTER&gt;** key.
4. At the prompt, Print a delimited report to the screen? (Y/N): enter **Yes** and press the **&lt;ENTER&gt;** key.
5. Open Reflection™
6. Select **Setup** from the File Menu toolbar.
7. Select **Display** from Setup drop down.
8. From the Display window, Select the **Screen** tab.
9. Select **Auto Resize Screen** .
10. Enter **160** into the Columns box.  Press the **&lt;OK&gt;** button.

Figure 39: Reflection TM Column Size

1. In VistA, when prompted at Device: Home// enter the following: **;160;9999** and press the **&lt;ENTER&gt;** key.

Figure 40: Displaying the CDI Report to Screen

Print a delimited report to the screen? (Y/N): y  YES

Delimited Report will now be printed to the screen...

DEVICE: HOME// ;160;999  HOME  (CRT)

SQA,TESTPATIENTFOUR^5543^04/13/1969^8/14/16 08:00^8/13/16 00:39:23^C EDICINE^WARD^MEDICINE^13^^^8/13/16 17:31:37

SQA,TESTPATIENTONE^0090^09/05/1989^8/13/16 08:00^^CHY ANTICOAG^CLINIC^MEDICINE^161^^^

SQA,TESTPATIENTTWO^4412^07/30/1969^8/13/16 09:00^^CHY ANTICOAG^CLINIC^MEDICINE^161^^^

KORDISH,ELI SQAPATIENT^8397^05/13/1925^8/13/16 23:13:29^8/11/10 15:45:36^CLC^WARD^MEDICINE^13^^7/17/08 16:30^

SQA,TESTPATIENTFOUR^5543^04/13/1969^8/16/16 12:26:15^8/13/16 00:39:23^ICU-M^WARD^MEDICINE^13^^^8/14/16 08:00

SQA,TESTPATIENTTHREE^2254^05/14/1977^8/13/16 17:25:25^8/13/16 00:36:44^ICU-M^WARD^MEDICINE^13^^^

SQA,TESTPATIENTTWO^4412^07/30/1969^8/14/16 22:25:16^8/14/16 22:06:52^ICU-M^WARD^MEDICINE^13^^^8/13/16 09:00

SQA,TESTPATIENTTWO^4412^07/30/1969^8/16/16 12:37:27^8/14/16 22:06:52^ICU-M^WARD^MEDICINE^13^^^8/16/16 10:45:11

SQA,OUTPATIENTSIX^3876^03/18/1973^8/14/16 22:54:18^8/14/16 08:00^INTERMEDIATE MEDICINE^WARD^NONE^112^^^

SQA,TESTPATIENTSIX^8899^06/28/1968^8/13/16 17:31:57^8/13/16 00:24:38^INTERMEDIATE MEDICINE^WARD^NONE^112^^^

SQA,TESTPATIENTFIVE^3389^07/16/1972^8/16/16 10:27:39^8/13/16 00:14:13^TRANSITIONAL^WARD^^145^^^

END OF REPORT.

#### Importing the Delimited data into Excel™ Spreadsheet

An Excel™ spreadsheet has been developed entitled CDI Reporting Tool which can be utilized to determine how a case should be defined (e.g. duplicate, recurrent, incident, CO-, CO-CLC-Associated, CO-not-CLC-Associated, CLC Onset-CLC-Associated, etc.) for reporting to IPEC.  All CDI positive laboratory assays (obtained from inpatients as well as outpatients) should be captured each month in the CDI Reporting Tool.

**Note:** Before running the report, ensure that the laboratory test(s), e.g., the Clostridium Difficile Etiology, are configured in the MDRO TOOLS LAB SEARCH/EXTRACT file (#104.1).  To configure the lab test(s), use the MDRO Tools Lab Parameter Setup option.

To generate the report, perform the following steps:

1. From the MDRO Tools Reports Menu, enter **4** for Print CDI Report and press the **&lt;ENTER&gt;** key.
2. At the Do you want to select all Divisions: NO// prompt, enter either **Yes** or **No** based on the following criteria:
    - 2.1. Entering **Yes** will obtain results for all divisions.
    - 2.2. Entering **No** will obtain results for a particular division or divisions.  After No is entered, a prompt will be displayed to enter the name of the division. Enter the name of the division and press the **&lt;ENTER&gt;** key. If desired, enter additional divisions.

**Note** : The prompt will not display for a facility that is setup as a Single Division, it will only display for a Multi-Division Facility.

1. At the Beginning POS CDI LAB ID Event (Collection)Date: prompt, enter a begin date and press the **&lt;ENTER&gt;** key.
2. At the Ending POS CDI LAB ID Event (Collection)Date: prompt, enter an end date and press the **&lt;ENTER&gt;** key.
3. At the prompt, Device: HOME//, press the **&lt;ENTER&gt;** key.
4. At the prompt, Print a delimited report to the screen? (Y/N): enter **Yes** and press the **&lt;ENTER&gt;** key.
5. Open Reflection™
6. Select **Setup** from the File Menu toolbar.
7. Select **Display** from Setup drop down.
8. From the Display window, Select the **Screen** tab.
9. Select **Auto Resize Screen** .
10. Enter **160** into the Columns box.  Press the **&lt;OK&gt;** button.

Figure 41: Reflection TM Column Size

1. In VistA, when prompted at Device: Home// enter the following: **;160;9999** and press the **&lt;ENTER&gt;** key.
2. Select all of the delimited data when it is displayed.
3. Copy the selected delimited data.
4. Open the NotePad™ application.
5. Select **Paste** from the Menu toolbar.
6. Save the file as a Text file with a .TXT extension to either the desktop or network drive.  Note the location of the saved file.
7. Open the Excel™ spreadsheet CDI Reporting Tool.
8. Click once on the tab entitled Import VistA Report.
9. Select the cell A2 by placing the mouse in the cell and clicking once in the cell.

**Note:** The example shown below is the CDI Acute Care Reporting Tool.  Select the CDI Reporting Tool that is applicable, either CLC, Acute Care SCIU, or Acute Care.

Figure 42: Select A2 in CDI Reporting Tool

1. Select **Data** from the Excel™ Menu toolbar.
2. Select **From Text** to import data from the previously saved text file.
3. Navigate to the location of the previously saved Text file and select the **Import** button.
4. Select the **Delimited** button in the Text Import Wizard – Step 1 of 3 window.  See the figure shown below for more information.

Figure 43: Importing Delimited Data, Import Wizard Step 1 of 3

<!-- image -->

1. Select the **Next** button in the Text Import Wizard – Step 1 of 3 window.
2. In the Text Import Wizard – Step 1 of 2 window, deselect the Tab Delimiter by clicking once in the checkbox.
3. In the Text Import Wizard – Step 1 of 2 window, select the Other Delimiter by clicking once in the checkbox and placing the carat ^ symbol in the box.  See the figure shown below for more information.

Figure 44: Importing Delimited Data, Import Wizard Step 2 of 3

<!-- image -->

1. Select the **Next** button in the Text Import Wizard – Step 2 of 3 window.
2. Select the **Finish** button in the Text Import Wizard – Step 3 of 3 window.

Figure 45: Importing Delimited Data, Import Wizard Step 3 of 3

<!-- image -->

1. In the Import Data Window, select the **OK** button to accept the Existing Worksheet=$A$2. See the figure shown below for more information.
2. After importing the data, select **Save As** from the File Menu and save the worksheet to the local desktop or network drive.
3. Select all of the data imported in rows A through L by dragging the mouse across the data.
4. Select **Copy** from the Home menu.
5. Select the CDI Cases tab at the bottom of the Excel™ spreadsheet.
6. Click once into the A2 cell.
7. Select **Paste** from the Home menu **.**
8. Evaluate the data in cells F through I (regarding location) to determine a selection in cell J.  Select a Patient location when CDI LabID Event was collected from the drop down list in cell J.  Repeat this step for each patient.
9. Select **Save** from the File Menu to save the worksheet.

A description for the columns and headings from the report are outlined in the table below.

Table 12: Descriptions for Excel™ spreadsheet CDI Reporting Tool

| **Heading**                                                                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                                                                         | This field contains the patient’s name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| SSAN                                                                         | This field contains the last 4 numbers of the patient’s Social Security Account Number (SSAN).                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Birth date                                                                   | This field contains the patient’s birth date and may be useful as some patients have the same name and last 4 digits of the SSAN.  It is displayed in MM/DD/YY format.                                                                                                                                                                                                                                                                                                                                             |
| Date & time of CDI LabID Event                                               | This field contains the date and time that the  *C. difficile*  positive stool specimen for this episode was  collected  in MM/DD/YY HH:MM format.                                                                                                                                                                                                                                                                                                                                                                 |
| Date & time of admission associated with CDI LabID Event in Column D         | This field contains the date and time the patient was admitted to the CLC facility in MM/DD/YY HH:MM format.                                                                                                                                                                                                                                                                                                                                                                                                       |
| Location Name                                                                | Information shown in this column will enable the user to choose the appropriate Patient Location when CDI LabID Event was collected in Column J.                                                                                                                                                                                                                                                                                                                                                                   |
| Location Type                                                                | Information shown in this column will enable the user to choose the appropriate Patient Location when CDI LabID Event was collected in Column J.                                                                                                                                                                                                                                                                                                                                                                   |
| Location Service                                                             | Information shown in this column will enable the user to choose the appropriate Patient Location when CDI LabID Event was collected in Column J.                                                                                                                                                                                                                                                                                                                                                                   |
| Location Stop Code                                                           | Information shown in this column will enable the user to choose the appropriate Patient Location when CDI LabID Event was collected in Column J.                                                                                                                                                                                                                                                                                                                                                                   |
| Patient location when CDI LabID Event collected                              | Select either acute input, output/ED, SCIU, CLC, or mental health as appropriate from the drop-down box.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Date & time of most recent discharge from your inpt facility before Column E | This field contains the most recent discharge date &amp; time (MM/DD/YY HH:MM) if patient was discharged from the CLC facility at any time prior to the admission date in Column E;  Note: Mental health or observation discharges should not be included.                                                                                                                                                                                                                                                         |
| Date & time of most recent pos CDI LabID Event  before test in Column D      | If the patient had a previous CDI LabID Event, the date and time the most recent previous positive CDI LabID Event was collected (MM/DD/YY HH:MM) from any setting (acute inpatient, outpatient/ED, SCIU, CLC, or mental health) will be displayed.  A CDI LabID Event can be counted from an outside (either VA or non-VA) facility if there is documentation (e.g. a scanned report) in CPRS.                                                                                                                    |
| Duplicate case                                                               | This field is automatically calculated using the formula: (TRUE/FALSE) = number of days from previous positive CDI LabID Event to current positive CDI LabID Event ≤14 days.                                                                                                                                                                                                                                                                                                                                       |
| Recurrent case                                                               | This field is automatically calculated using the formula:  (TRUE/FALSE) = number of days from previous positive CDI LabID Event to current positive CDI LabID Event is >14 and ≤56.                                                                                                                                                                                                                                                                                                                                |
| Incident case                                                                | This field is automatically calculated using the formula:  (TRUE/FALSE) = number of days from previous positive CDI LabID Event to current positive CDI LabID Event is >56 or there was no positive stool specimen.                                                                                                                                                                                                                                                                                                |
| Pos CDI LabID Event collected upon admission                                 | This field is automatically calculated using the formula:  (TRUE/FALSE) = case where non-duplicate CDI LabID Event (Column D) was collected as an outpatient ≤24 hours before admission or as an inpatient ≤48 hours after the admission to your CLC facility listed in Column E.  This includes recurrent cases (non-duplicate CDI LabID Events where the second CDI LabID Event was collected >14 and ≤56 days after the first CDI LabID Event).                                                                 |
| Community-  Onset CDI (CO-CDI)                                               | This field is automatically calculated using the formula:  (TRUE/FALSE) = Patient admitted and a positive stool CDI LabID Event was collected as an outpatient ≤24 hours before admission or as an inpatient ≤48 hours after admission to your CLC facility AND non-duplicate/non-recurrent case AND patient location when the  CDI LabID Event was collected was “CLC”, “acute inpt,” “outpt/ED,” or “SCIU.”                                                                                                      |
| Community-Onset, CLC-Associated CDI (CO-CLC-Associated CDI)                  | This field is automatically calculated using the formula: (TRUE/FALSE) = Patient admitted and a positive stool CDI LabID Event was collected as an outpatient ≤24 hours before admission or as an inpatient ≤48 hours after admission to your CLC facility AND non-duplicate/non-recurrent case AND patient discharged from your CLC facility ≤28 days from date positive stool specimen was collected AND patient location when the CDI LabID Event was collected was “CLC”, “acute inpt,” “outpt/ED,” or “SCIU.” |
| CLC -Onset, CLC-Associated CDI case (CLC-Onset, CLC-Associated CDI)          | This field is automatically calculated using the formula: field (TRUE/FALSE) = Positive stool CDI LabID Event collected >48 hours after admission to your Community Living Center facility AND non-duplicate/non-recurrent case AND patient location when the CDI LabID Event was collected was “CLC”.                                                                                                                                                                                                             |
| Clinically Confirmed CLC-Onset-CLC-Associated CDI                            | From the drop-down menu, enter whether the patient  was a Clinically Confirmed CLC-Onset, CLC-Associated CDI case (i.e. a patient with a positive CDI LabID Event plus either 1) diarrhea or 2) colonoscopic or histopathologic findings of pseudomembranous colitis).  Enter “yes,” “no,” or “N/A” (not applicable) after chart review.                                                                                                                                                                           |
| Date for 30-day review                                                       | This field is automatically calculated using the formula:  when 30 days have passed since the positive laboratory CDI LabID Event in Column D.  **Note:**  This is the time to determine whether CDI complications occurred.                                                                                                                                                                                                                                                                                       |
| CDI Complications                                                            | From the drop-down menu, select any adverse outcomes associated with CDI: ICU admit, colectomy, death, or combinations of outcomes if known.                                                                                                                                                                                                                                                                                                                                                                       |
| Comments                                                                     | If desired, enter any relevant notes or clinical details related to the case.                                                                                                                                                                                                                                                                                                                                                                                                                                      |

#### Print CRE Report

1. From the MDRO Tools Reports Menu, enter **5** for Print CRE Report and press the **&lt;ENTER&gt;** key.
2. At the Do you want to select all Divisions: NO// prompt, enter either **Yes** or **No** based on the following criteria:
    - 2.1. Entering **Yes** will obtain results for all divisions.  See the figure below.
    - 2.2. Entering **No** will obtain results for a particular division or divisions.  After No is entered, a prompt will be displayed to enter the name of the division. Enter the name of the division and press the **&lt;ENTER&gt;** key. If desired, enter additional divisions.

**Note** : The prompt will not display for a facility that is setup as a Single Division, it will only display for a Multi-Division Facility.

1. At the Begin with facility admission date: prompt, enter a begin date and press the **&lt;ENTER&gt;** key.
2. At the End with facility admission date: prompt, enter an end date and press the **&lt;ENTER&gt;** key.
3. At the Do you want to only print the summary report? NO// prompt, enter either **Yes** or **No** based on the following criteria:
    - 3.1. Enter **No** and press the **&lt;ENTER&gt;** key to print the Detailed Report.
    - 3.2. Enter **Yes** and press the **&lt;ENTER&gt;** key to print the Summary Report.
4. At the Device: HOME// prompt, enter the name of the printer or format to print to screen by entering the following: **;160;999 HOME** and press the **&lt;ENTER&gt;** key.

Figure 46: CRE Print Detailed Report for All Divisions

Select MDRO Tools Reports Menu &lt;TEST ACCOUNT&gt; Option: 5  Print CRE Report

Do you want to select all divisions: NO// y  YES

Begin with facility admission date: 0911  (SEP 11, 2016)

End with facility admission date: 0918  (SEP 18, 2016)

Do you want to only print the summary report? NO//

This report is designed for a 176 column format (landscape).

DEVICE: HOME// ;160;999  HOME  (CRT)

Figure 47: Example of CRE Print Detail Report for All Divisions

CRE ACUTE CARE IPEC REPORT - DETAILED

Division: FORT COLLINS

Report period: Sep 11, 2016 to Sep 18, 2016@24:00

Report printed on: Nov 10, 2016@11:22:18                 PAGE: 1

Basic Measures and Device Days of Care

01 Total # of admissions to the acute care inpatient facility for the period: 8

02 Total # of bed days of care for acute care for the period: 0

Admission Prevalence Measures (Facility/Division Wide)

07 # of (01) with surveillance screens for CRE/CPE collected upon admission: 1

08 # of (07) that were positive for CRE/CPE based on surveillance screen: 1

09 # of (01) that were positive for CRE/CPE based on clinical cultures: 0

10 % of (01) that were positive for CRE/CPE based on surveillance screening: 100%

11 % of (01) that were positive for CRE/CPE based on clinical cultures: 0%

Incidence Measures: Healthcare-Associated Colonized Cases

12 # of patients with screens for CRE/CPE collected 3 or more days after admission: 4

13 # of (12) that were positive for CRE/CPE based on surveillance screen Collected 3 or more

days after admission: 2

14 # of patients with clinical cultures positive for CRE/CPE 3 or more days after admission:

2

15 Rate of healthcare-associated colonized cases: 0

Infection Prevention and Control Measures

33 # of cases with CRE/CPE for the period: 5

CRE ACUTE CARE IPEC REPORT - DETAILED

Division: FORT COLLINS

Report period: Sep 11, 2016 to Sep 18, 2016@24:00

Report printed on: Nov 10, 2016@11:22:18                 PAGE: 2

DATE MAS MOVE  SURVEILLANCE CLINICAL CULTURE

WARD  SERVICE  PATIENT  LAST4  ENTERED WARD ADT  TYPE  SOURCE  CULTURE  CULTURE  RESULT

---------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------

C MEDICINE GENERAL(ACUTE MEDICINE)  PATIENTONE   6612   Sep 12,2016@22:28 DIRECT ACTIVE SKIN  Y N POS

C MEDICINE GENERAL(ACUTE MEDICINE)  PATIENTTWO   1199   Sep 12,2016@23:00 DIRECT ACTIVE FECES N Y POS

ICU-S      SURGICAL ICU             PATIENTTHREE 6610   Sep 12, 2016@23:19 DIRECT ACTIVE SKIN Y N POS

ICU-M      MEDICAL ICU              PATIENTFOUR  7722   Sep 12, 2016@23:25 DIRECT ACTIVE FECES N Y POS

END OF REPORT

Figure 48: Example of CRE Print Detail Report for a Single Division

CRE ACUTE CARE IPEC REPORT - SUMMARY

Division: CHEYENNE VAMROC

Report period: Sep 08, 2016 to Sep 30, 2016@24:00

Report printed on: Nov 10, 2016@11:10:59                 PAGE: 1

Basic Measures and Device Days of Care

01 Total # of admissions to the acute care inpatient facility for the period:5

02 Total # of bed days of care for acute care for the period: 0

Admission Prevalence Measures (Facility/Division Wide)

07 # of (01) with surveillance screens for CRE/CPE collected upon admission: 4

08 # of (07) that were positive for CRE/CPE based on surveillance screen: 1

09 # of (01) that were positive for CRE/CPE based on clinical cultures: 0

10 % of (01) that were positive for CRE/CPE based on surveillance screening: 25%

11 % of (01) that were positive for CRE/CPE based on clinical cultures: 0%

Incidence Measures: Healthcare-Associated Colonized Cases

12 # of patients with screens for CRE/CPE collected 3 or more days after admission: 0

13 # of (12) that were positive for CRE/CPE based on surveillance screen collected 3 or more

days after admission: 0

14 # of patients with clinical cultures positive for CRE/CPE 3 or more days after admission:

0

15 Rate of healthcare-associated colonized cases: 0

Infection Prevention and Control Measures

33 # of cases with CRE/CPE for the period: 1

END OF REPORT

A description for the headings from the report are outlined in the table below.

Table 13: CRE Print Descriptions

| **Basic Measures and Device Days of Care**                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Header**                                                                                                        | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 01 Total # of admissions to the acute care inpatient facility for the period                                      | Total number of admissions (not patients) to all units (excluding mental health and observation) of the hospital for the calendar month.  In multi-division facilities transfers from one division to another are included as admissions (excluding in-hospital unit-to-unit transfers).  **Note:**  Some patients may be admitted more than once during the month.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 02 Total # of bed days of care for acute care for the period                                                      | The number of bed days of care for the acute care facility for the month.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Admission Prevalence Measures (Facility/Division Wide)**                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 07 # of (01) with surveillance screens for CRE/CPE collected upon admission                                       | The number of admissions (not patients) to all acute care units of the hospital for the calendar month who received surveillance screening for CRE/CPE on admission (days 1 or 2of admission) to the facility during the month.  **Note:**  This number may include patients determined by the facility to be high risk for CRE/CPE and others who received screening.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Admission Prevalence Measures (Facility/Division Wide)**                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| # of (07) positive for CRE/CPE based on surveillance screen                                                       | The number of surveillance screens on line (07) that were positive for CRE/CPE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| # of (01) positive for CRE/CPE based on clinical cultures                                                         | The number of admissions (not patients) to all acute care units (excluding mental health and observation) of the hospital for the calendar month with one or more clinical cultures positive for CRE/CPE upon admission during the month.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| % (01) positive for CRE/CPE based on surveillance screening.                                                      | This field is automatically calculated by using the formula: (line 8 / line 7) * 100).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| % (01) positive for CRE/CPE based on clinical cultures                                                            | This field is automatically calculated by using the formula: (line 9 / line 1) * 100).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Incidence Measures: Healthcare-Associated Colonized Cases**                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 12 # of patients with screens for CRE/CPE collected 3 or more days after admission                                | The date of the surveillance screen occurs greater than or equal to (≥) 3 calendar days after the date of admission where the date of admission is calendar day one.  The number of patients who had surveillance screens collected greater than or equal to (≥) 3 days after admission to determine presence of CRE/CPE.  This includes patients who are epidemiologically linked to other patient(s) positive for CRE/CPE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 13 # of (12) that were positive for CRE/CPE based on surveillance screen collected 3 or more days after admission | the number of patients with CRE/CPE positive surveillance screens collected ≥ 3 days after admission for the facility for the month.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 14 # of patients with clinical cultures positive for CRE/CPE 3 or more days after admission                       | These are cultures that do not fit the NHSN definition for infection (i.e., they are colonized).  Infections are defined using the current NHSN definitions. This is the number of patients with one or more clinical cultures positive for CRE/CPE that do not fit the NHSN definition for healthcare-associated infection (HAI) (those with actual infection should be counted for in lines 16 – 27).  This may indicate that the patient is colonized with CRE/CPE.  Each patient with a positive culture should only be counted once as patients may have more than one culture positive for CRE/CPE.  There is a note # 2 (circled in red above) at the left side of the data entry field stating that these are cultures that do not fit the NHSN definition for infection (i.e., they are colonized) and that cases with both a CRE/CPE positive clinical culture and surveillance specimen will be recorded ONLY as a clinical culture case. |
|                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Incidence Measures: Healthcare-Associated Colonized Cases**                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 15 Rate of healthcare-associated colonized cases                                                                  | This field is automatically calculated by using the formula:  ((line 13 + line 14) / line 2) * 1000).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Infection Prevention and Control Measures**                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 33 # of cases with CRE/CPE for the  period                                                                        | Total number of patients who were found to be positive for CRE/CPE on admission plus those found to have CRE/CPE colonization or infection after admission to the facility.  This includes all patients with a positive CRE/CPE screening or clinical culture throughout admission.  Although patients who are being screened should be placed in Contact Precautions awaiting the results of the screening, do not include those whose screens were negative on Line 33.  Do not include patients who have a prior history of CRE/CPE but do not have a positive CRE/CPE clinical culture or surveillance screen during this admission.                                                                                                                                                                                                                                                                                                             |

### Tasked Reports

The following reports can be set up in TaskMan to run automatically and print to a designated printer at specified frequencies during the day:

| MMRS ISOLATION REPORT (TASKED)   | Print Isolation Report (Tasked)    |
|----------------------------------|------------------------------------|
| MMRS NARES SWAB LIST (TASKED)    | Print Nares Screen Compliance List |
| MDRO PRINT CDI REPORT (TASKED)   | Print Facility CDI Report (Tasked) |

If the clinical staff desires to schedule any of the reports to automatically print to designated printers at specified times during the day, schedule these tasks in TaskMan.

#### Print Isolation Report (Tasked)

This option should not be run interactively.  It should be scheduled by IRM staff to run via TaskMan using option Schedule/Unschedule Options [XUTM SCHEDULE]; this option will print the Isolation Report at specified times.

Figure 49: Print Isolation Report (Tasked)

Select TaskMan Management Option: **Schedule/Unschedule Options**

Select OPTION to schedule or reschedule: **"MMRS ISOLATION REPORT (TASKED)"**

Are you adding 'MMRS ISOLATION REPORT (TASKED)' as

a new OPTION SCHEDULING (the 329TH)? No// **Y** (Yes)

Edit Option Schedule

Option Name: MMRS ISOLATION REPORT (TASKED

Menu Text: Print Isolation Report (Tasked)           TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: MAR 5,2017@15:50

DEVICE FOR QUEUED JOB OUTPUT: **IDM1$PRT LANDSCAPE;P-TCP LANDS**

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 12H

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                  Press &lt;PF1&gt;H for help

**Note:** In order for the report to run correctly, when the option is scheduled to run in TaskMan via the option Schedule / Unschedule Options [XUTM SCHEDULE], several variables need to be configured on the second page of the form as described below.

1. Add the Variable Name MMRSDIV and set the value of it to the Internal Entry Number (IEN) in File #104 for the applicable Division.

**Note:** See the Section entitled Obtaining a Division IEN Number for more information.

1. Setting the variables:
    - 1.1. To print the report for all locations or divisions, add the Variable Name. Set its value to **"ALL";** the quotations are required.
    - 1.2. To print for specific locations, add the Variable Name for each location.  For example: MMRSLOC(LOCIEN), where LOCIEN is the geographical unit IEN from File #104.3.  Set its value to **"".** Use the **&lt;TAB&gt;** key to enter each variable. **Note:** the two double quotes are required for the Value; do not leave the Value blank.

1. After configuring the variables, press the **&lt;ENTER&gt;** key.

1. At the command prompt, type **S** to save the form and press the **&lt;ENTER&gt;** key.

1. At the command prompt, type **E** to exit and press the **&lt;ENTER&gt;** key.

The figure below illustrates how to generate the option for Division 1 with geographical locations 3 and 5.

Figure 50: Print Isolation Report (Tasked) with Division 1 and Geographical Locations 3, 5

Edit Option Schedule

Option Name: MMRS ISOLATION REPORT (TASKED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USER TO RUN TASK:

VARIABLE NAME: MMRSDIV                  	VALUE: 1

VARIABLE NAME: MMRSLOC(3)               	VALUE: ""

VARIABLE NAME: MMRSLOC(5)               	VALUE: ""

VARIABLE NAME:                              VALUE:

COMMAND:                                  Press &lt;PF1&gt;H for help

The figure below illustrates how to generate the option for Division 1 with all Geographical Locations.

**Note:** When tasking options, ALL has to be in quotations (i.e., “ALL”).

Figure 51: Print Isolation Report (Tasked) with Division 1 and All Geographical Locations

Edit Option Schedule

Option Name: MMRS ISOLATION REPORT (TASKED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USER TO RUN TASK:

VARIABLE NAME: MMRSDIV                  	VALUE: 1

VARIABLE NAME: MMRSLOC               	      VALUE: "ALL"

VARIABLE NAME:                  	      VALUE:

VARIABLE NAME:                              VALUE:

VARIABLE NAME:                              VALUE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                  Press &lt;PF1&gt;H for help

**Note:** This option may be scheduled more than once.  For example, if the site wants to schedule the report to print at different printers for different locations, place the option name in quotes as it will allow for the scheduling of the option for more than a single time.

#### Print Nares Screen Compliance List (Tasked)

The Print Nares Screen Compliance List (Tasked) option should not be run interactively; it should only be scheduled by IRM staff to run via TaskMan using option Schedule/Unschedule Options [XUTM SCHEDULE]. This option will print the Nares Compliance List at specified times.

Figure 52: Print Nares Screen Compliance List (Tasked)

Select TaskMan Management Option: **Schedule/Unschedule Options**

Select OPTION to schedule or reschedule: **“MMRS NARES SWAB LIST (TASKED)”**

Are you adding ‘MMRS NARES SWAB LIST (TASKED)’ as

a new OPTION SCHEDULING (the 329TH)? No// **Y** (Yes)

Edit Option Schedule

Option Name: MMRS NARES SWAB LIST (TASKED

Menu Text: Print Nares Screen Compliance List (Tasked)           TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: MAR 5,2017@15:50

DEVICE FOR QUEUED JOB OUTPUT: IDM1$PRT LANDSCAPE;P-TCP LANDS

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 12H

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                  Press &lt;PF1&gt;H for help

**Note:** In order for the report to run correctly, when the option is scheduled to run in TaskMan via the option Schedule / Unschedule Options [XUTM SCHEDULE], several variables need to be configured on the second page of the form as described below.

1. Add the Variable Name MMRSDIV and set the value of it to the Internal Entry Number (IEN) in File #104 for the applicable Division.

**Note:** See the Section entitled Obtaining a Division IEN Number for more information.

1. Setting the variables:
    - 1.1. To print the report for all locations or divisions, add the Variable Name. Set its value to **"ALL";** the quotations are required.
    - 1.2. To print for specific locations, add the Variable Name for each location.  For example: MMRSLOC(LOCIEN), where LOCIEN is the geographical unit IEN from File #104.3.  Set its value to **"".** Use the **&lt;TAB&gt;** key to enter each variable. **Note:** the two double quotes are required for the Value; do not leave the Value blank.

1. After configuring the variables, press the **&lt;ENTER&gt;** key.

1. At the command prompt, type **S** to save the form and press the **&lt;ENTER&gt;** key.

1. At the command prompt, type **E** to exit and press the **&lt;ENTER&gt;** key.

The figure below illustrates how to generate the option for Division 1 with geographical locations 3 and 5.

Figure 53: Print Nares Swab List (Tasked) with Division 1 and Geographical Locations 3, 5

Edit Option Schedule

Option Name: MMRS NARES SWAB LIST (TASKED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USER TO RUN TASK:

VARIABLE NAME: MMRSDIV                  	VALUE: 1

VARIABLE NAME: MMRSLOC(3)               	VALUE: ""

VARIABLE NAME: MMRSLOC(5)               	VALUE: ""

VARIABLE NAME:                              VALUE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                  Press &lt;PF1&gt;H for help

The figure below illustrates how to generate the option for Division 1 and all Geographical Locations.

Figure 54: Print Nares Swab List (Tasked) with Division 1 and All Geographical Locations

Edit Option Schedule

Option Name: MMRS NARES SWAB LIST (TASKED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USER TO RUN TASK:

VARIABLE NAME: MMRSDIV                  	VALUE: 1

VARIABLE NAME: MMRSLOC               	VALUE: "ALL"

VARIABLE NAME:                	            VALUE:

VARIABLE NAME:                              VALUE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                  Press &lt;PF1&gt;H for help

#### MDRO Print CDI Report (Tasked)

The MDRO Print CDI Report (Tasked) option should not be run interactively.  It should only be scheduled by IRM staff to run via TaskMan using option Schedule/Unschedule Options [XUTM SCHEDULE or MAIN^MMRSCDI2]. This option will print the Facility CDI report at specified times utilizing the default date range of the previous month.

1. In TaskMan, Select the option Schedule/Unschedule and press the &lt;ENTER&gt; key.
2. When prompted, Select OPTION to schedule or reschedule:, enter **MDRO** and press the **&lt;ENTER&gt;** key.
3. When prompted, enter the option number for **MDRO PRINT CDI REPORT (TASKED)** and press the **&lt;ENTER&gt;** key.
4. When prompted, Are you adding 'MDRO PRINT CDI REPORT (TASKED)' as a new OPTION SCHEDULING (the 237TH)? No// Y respond Yes and press the **&lt;ENTER&gt;** key.

Figure 55: MDRO Print CDI Report (Tasked)

Select Taskman Management &lt;TEST ACCOUNT&gt; Option: Schedule/Unschedule Options

Select OPTION to schedule or reschedule: MDRO

1   MDRO PRINT CDI REPORT (TASKED) Print Facility CDI Report (Tasked)

2   MDRO HISTORICAL DAYS EDIT MMRS MDRO HIST DAYS EDIT MDRO Historical

Days Edit

3   MDRO TOOLS LAB PARAMETER SETUP MMRS MDRO LAB PARAMETER SETUP MDRO

Tools Lab Parameter Setup

CHOOSE 1-3: 1  MDRO PRINT CDI REPORT (TASKED)     Print Facility CDI Report (Tasked)

Are you adding 'MDRO PRINT CDI REPORT (TASKED)' as

a new OPTION SCHEDULING (the 237TH)? No// Y (Yes)

Edit Option Schedule

Option Name: MDRO Print CDI Report (TASKED

Menu Text: MDRO Print CDI Report (Tasked)           TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: JAN 5,2017@15:50

DEVICE FOR QUEUED JOB OUTPUT: IDM1$PRT LANDSCAPE;P-TCP LANDS

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                  Press &lt;PF1&gt;H for help

**Note:** In order for the report to run correctly, when the option is scheduled to run in TaskMan via the option Schedule / Unschedule Options [XUTM SCHEDULE], several variables need to be configured on the second page of the form as described below.

1. Add the Variable Name MMRSDIV and set the value of it to the Internal Entry Number (IEN) in File #104 for the applicable Division.

**Note:** See the Section entitled Obtaining a Division IEN Number for more information.

1. Setting the variables:
    - 1.1. To print the report for all locations or divisions, add the Variable Name. Set its value to **"ALL";** the quotations are required.
    - 1.2. To print for specific locations, add the Variable Name for each location.  For example: MMRSLOC(LOCIEN), where LOCIEN is the geographical unit IEN from File #104.3.  Set its value to **"".** Use the **&lt;TAB&gt;** key to enter each variable. **Note:** the two double quotes are required for the Value; do not leave the Value blank.

1. After configuring the variables, press the **&lt;ENTER&gt;** key.

1. At the command prompt, type **S** to save the form and press the **&lt;ENTER&gt;** key.

1. At the command prompt, type **E** to exit and press the **&lt;ENTER&gt;** key.

The figure below illustrates how to generate the option for Division 1 with geographical locations 3 and 5.

Figure 56: MDRO Print CDI Report (Tasked) Division 1 and Geographical Locations 3, 5

Edit Option Schedule

Option Name: MDRO PRINT CDI REPORT (TASKED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USER TO RUN TASK:

VARIABLE NAME: MMRSDIV                  	VALUE: 1

VARIABLE NAME: MMRSLOC(3)               	VALUE: ""

VARIABLE NAME: MMRSLOC(5)               	VALUE: ""

VARIABLE NAME:                              VALUE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                  Press &lt;PF1&gt;H for help

The figure below illustrates how to generate the option for Division 1 and all Geographical Locations.

Figure 57: MDRO Print CDI Report (Tasked) with Division 1 and All Geographical Locations

Edit Option Schedule

Option Name: MDRO PRINT CDI REPORT (TASKED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USER TO RUN TASK:

VARIABLE NAME: MMRSDIV                  	VALUE: 1

VARIABLE NAME: MMRSLOC               	VALUE: "ALL"

VARIABLE NAME:                	            VALUE:

VARIABLE NAME:                              VALUE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                  Press &lt;PF1&gt;H for help

#### Obtaining a Division IEN

To obtain a division IEN, follow the instructions below.

1. In FileMan, enter the option **INQUIRE TO FILE ENTRIES** and press the **&lt;ENTER&gt;** key.
2. When prompted, OUTPUT FROM WHAT FILE:, enter **MRSA SITE PARAMETERS** and press the **&lt;ENTER&gt;** key.
3. When prompted, Select MRSA SITE PARAMETERS DIVISION:, enter the division and press the **&lt;ENTER&gt;** key.

The figure below illustrates how to obtain the IEN for a Division. The number highlighted in yellow is the IEN.

Figure 58: Obtain MRSA Division IEN

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: **MRSA SITE PARAMETERS**

Select MRSA SITE PARAMETERS DIVISION: **XXXXX VAMC**

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes//   (Yes)

Include COMPUTED fields:  (N/Y/R/B): NO// **Record Number** (IEN)

NUMBER: 1                               DIVISION: XXXXX VAMC

RECEIVING UNIT SCREEN: YES                DISCHARGING UNIT SCREEN: YES

SCREEN POS ON TRANSFER IN: YES        SCREEN POS ON DISCHARGE: YES

To obtain a Geographical Location IEN, follow the instructions below

1. In FileMan, enter the option **INQUIRE TO FILE ENTRIES** and press the **&lt;ENTER&gt;** key.
2. When prompted, OUTPUT FROM WHAT FILE:, enter **MRSA WARD MAPPINGS** and press the **&lt;ENTER&gt;** key.
3. When prompted, Select MRSA WARD MAPPINGS NAME:, enter the ward and press the **&lt;ENTER&gt;** key.

The figure below illustrates how to obtain the IEN for a Geographical Location. The number highlighted in yellow is the IEN.

Figure 59: Obtain Geographical Location IEN

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: **MRSA WARD MAPPINGS**

Select MRSA WARD MAPPINGS NAME: **11AB**

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes//   (Yes)

Include COMPUTED fields:  (N/Y/R/B): NO// **Record Number** (IEN)

NUMBER: 5                               NAME: 11AB

DIVISION: XXXXX VAMC                  TYPE: ACUTE CARE

IPEC UNIT ID: 726

WARD LOCATION: 11AB

WARD LOCATION: 11ASURG

#### Deleting a Variable Name

To delete a variable name, follow the instructions below.

1. Select the desired variable.
2. Enter the **@** symbol and press the **&lt;ENTER&gt;** key.

Figure 60: Deleting a Variable Name

Edit Option Schedule

Option Name: MDRO PRINT CDI REPORT (TASKED)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

USER TO RUN TASK:

VARIABLE NAME: @                  	      VALUE: "ALL"

VARIABLE NAME:                                	      VALUE:

VARIABLE NAME:                	            VALUE:

VARIABLE NAME:                              VALUE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                  Press &lt;PF1&gt;H for help

1. When prompted, SURE YOU WANT TO DELETE This entire subrecord? respond with **Y** and the **&lt;ENTER&gt;** key to delete the entire geographical unit from the setup.

## Troubleshooting

This section describes warning messages that will be displayed if errors are encountered when generating a report.

### Warning Message that Lab Test or Etiology Parameters are not configured

If the Laboratory Test or Etiology parameters have not been configured, and a user attempts to generate the CDI Report, the following message will be displayed to the user:

Figure 61: Warning Dialog regarding Lab Test/Etiology Configuration

The report cannot be run because the Laboratory Test(s) or

the Etiology is not configured in the MDRO TOOLS LAB

SEARCH/EXTRACT file, (104.1).  Use the MDRO Tools Lab Parameter Setup option to configure.

Consult the on MDRO Tools Lab Parameter Setup for information on how to enter laboratory and/or etiology parameters for historical reporting of multi-drug resistant organisms (MDROs).

### Warning Message that Etiology Parameter is not configured

If the Etiology parameter has not been configured, and a user attempts to generate the CRE Report, the following message will be displayed to the user:

Figure 62: Warning Dialog regarding Etiology Configuration

The report cannot be run because the Etiology has not been

configured in the MDRO TOOLS LAB SEARCH/EXTRACT file,

(#104.1).  Use the MDRO Tools Lab Parameter Setup option to configure.

Correct the issue by configuring the etiology parameters.  Consult the section regarding MDRO Tools Lab Parameter Setup for more information.

### Warning Message that Specimen is not Configured

If a site has not configured specimen(s), and a user attempts to run the CRE Report, the following message will be displayed to the user:

Figure 63: Warning Dialog regarding Specimen Configuration

Make sure a division and/or a Surveillance specimen has been

setup using the option: 'CRE Tools Site Parameter Setup'

Consult the section regarding the CRE Tools Parameter Setup menu option on how to configure the CRE parameters for division(s).

### Warning Message that Division(s) are not configured

If divisions have not been configured, and the user attempts to generate a report without first defining a Division, a warning dialog will be displayed.

Figure 64: Warning Dialog regarding Division Setup

&gt;&gt;&gt; Make sure the division has been setup using option:

‘MDRO Tools Parameter Setup (Main)’

Correct the issue by configuring the division(s).  Consult the MDRO Tools Parameter Setup section for more information.

### Warning Message that Chemistry Subscripted Tests are not configured

If Chemistry subscripted tests (MRSA SURVL NARES DNA, MRSA SURVL NARES AGAR) have not been configured, and the user attempts to generate a report, a warning dialog will be displayed.

Figure 65: Warning Dialog regarding Chemistry Subscripted Tests

&gt;&gt;&gt; Make sure the MRSA Chemistry subscripted tests have been setup according to the National Guidelines.  Laboratory needs to setup at least one of the lab tests in the system before generating reports:

1. ‘MRSA SURVL NARES DNA’

2. ‘MRSA SURVL NARES AGAR’

Correct the issue by configuring the Chemistry subscripted tests.  Consult the MDRO Tools Parameter Setup section for more information.

### Warning Message that the etiology Staphylococcus Aureus Methicillin Resistant (MRSA) has not been configured

If the Staphylococcus Aureus Methicillin Resistant etiology has not been configured, and the user attempts to generate a report, a warning dialog will be displayed.

Figure 66: Warning Dialog regarding Staphylococcus Aureus Methicillin Resistant etiology

&gt;&gt;&gt; Make sure the Etiology has been setup according to the National Guidelines.  The following etiology must be added to the Etiology Field File (#61.2):

‘STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)’

Correct the issue by configuring the etiology parameters.  Consult the section regarding MDRO Tools Lab Parameter Setup for more information.

### Warning Message that the Geographical Unit has not been configured

If the Geographical Unit has not been configured, and the user attempts to generate a report, a warning dialog will be displayed.

Figure 67: Warning Dialog regarding Geographical Unit

&gt;&gt;&gt; Make sure the Ward Mappings for each Geographical Unit has been setup

Correct the issue by configuring the Geographical Unit.  Consult the section regarding MDRO Tools Ward Mapping Setup for more information.

## Printing in Landscape

The following is a sample Terminal Type for a landscape setup. Actual entries may vary depending on make and model of the printer.

Figure 68: Printing in Landscape

NAME: P-TCP LANDSCAPE                  RIGHT MARGIN: 176

FORM FEED: #                         PAGE LENGTH: 51

BACK SPACE: $C(8)

OPEN EXECUTE: W $C(27),"&amp;l1O",$C(27),"&amp;l7C",$C(27),"&amp;k2S",$C(27),"&amp;l2E"

CLOSE EXECUTE: W $C(27),"E" D CLOSE^NVSPRTU

## ## MAS Movement

This section describes how MDRO-PT handles or interprets Medical Administration Service (MAS) movements.

For example, for a transaction type of Specialty Transfer, the MAS movement is excluded as there was not a change to the patient’s room; there was only a change to the patient’s status or service.

In the scenario of patients who float between the CLC and acute care, theoretically, two movements are created: one for the actual Transfer and one for the Absent Sick in Hospital (ASIH); however, the program will ignore the ASIH.  The program will respond to the patient’s movement as a discharge from the CLC and an Admission back into the CLC.

The table below states how the MDRO-PT handles or interprets Medical Administration Service (MAS) movements.

Table 14: MAS Movement Program Explanations

| Name                                     | Description                                                                                                                                                                                                                 | Clinical Transaction Type   | Include/  Exclude   | MDRO-PT Program Response   |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|---------------------|----------------------------|
| AMBULATORY CARE (OPT-AC)                 | Admission to the VA facility from the Ambulatory Care (A/C) rolls.                                                                                                                                                          | Admission                   | Include             | Admission                  |
| DIRECT                                   | Direct admission to the VA facility for treatment.                                                                                                                                                                          | Admission                   | Include             | Admission                  |
| NON-SERVICE CONNECTED (OPT-NSC)          | Admission for inpatient treatment from the facility OPT-NSC program.                                                                                                                                                        | Admission                   | Include             | Admission                  |
| NON-VETERAN (OPT-NVE)                    | Admission of a patient who is not a veteran applicant for inpatient treatment.                                                                                                                                              | Admission                   | Include             | Admission                  |
| OPT-SC                                   | Admission for inpatient treatment from the facility OPT-SC program.                                                                                                                                                         | Admission                   | Include             | Admission                  |
| PRE-BED CARE (OPT-PBC)                   | Admission from the OPT-PBC program for inpatient treatment.                                                                                                                                                                 | Admission                   | Include             | Admission                  |
| READMISSION TO IMLTC/NHCU/DOMICILIARY    | Readmission to NHCU or Domiciliary within 30 days of last discharge from NHCU/Domiciliary.                                                                                                                                  | Admission                   | Include             | Admission                  |
| TO ASIH                                  | To the parent VA Hospital from the VANH or VAD in Absent Sick in Hospital (ASIH) status.  Does not cause discharge from sending facility.                                                                                   | Admission                   | Include             | Admission                  |
| TRANSFER IN                              | Transfer in (admission) from another VA facility to this VA facility.                                                                                                                                                       | Admission                   | Include             | Admission                  |
| WAITING LIST                             | Admission type to be used when admitting a patient from a waiting list.                                                                                                                                                     | Admission                   | Include             | Admission                  |
| CHECK-IN LODGER                          | Check a lodger into the VA facility without impacting census data.                                                                                                                                                          | Check-in lodger             | Exclude             | Excluded                   |
| CHECK-IN LODGER (OTHER FACILITY)         | Check a lodger into a non-VA facility such as a local hotel.                                                                                                                                                                | Check-in lodger             | Exclude             | Excluded                   |
| CHECK-OUT LODGER                         | Check a lodger out of lodger status from either VA or non-VA facility.                                                                                                                                                      | Check-out lodger            | Exclude             | Excluded                   |
| CONTINUED ASIH (OTHER FACILITY)          | Discharge from the parent facility to ASIH in another VA (or non-VA) facility.  Patient must have been sent to parent facility in ASIH status originally.                                                                   | Discharge                   | Exclude             | Excluded                   |
| DEATH                                    | Expired while in receipt of inpatient care either in VA facility or in non-VA facility under VA auspices.  Autopsy was NOT accomplished.                                                                                    | Discharge                   | Include             | Discharge                  |
| DEATH WITH AUTOPSY                       | Expired while in receipt of inpatient care either in VA facility or in non-VA facility under VA auspices.  Autopsy was accomplished.                                                                                        | Discharge                   | Include             | Discharge                  |
| DISCHARGE FROM IMLTC/NHCU/DOM WHILE ASIH | This movement type is used when discharging a patient from the NHCU/DOM ward prior to his hospital discharge and prior to 30 days.  Use this type when it is evident that the patient will not return to the NHCU/DOM ward. | Discharge                   | Exclude             | Excluded                   |
| DISCHARGE TO CNH                         | Discharge type for the AMIE package for use when discharging a patient to a community nursing home.                                                                                                                         | Discharge                   | Include             | Discharge                  |
| FROM ASIH                                | Discharge from VAH ASIH status with resumption of VANH/VAD episode of care.                                                                                                                                                 | Discharge                   | Include             | Discharge                  |
| IRREGULAR                                | Discharge from inpatient treatment against medical advice.                                                                                                                                                                  | Discharge                   | Include             | Discharge                  |
| NON-BED CARE                             | Discharge from inpatient treatment to the NBC (Non-bed care) rolls.                                                                                                                                                         | Discharge                   | Exclude             | Excluded                   |
| NON-SERVICE CONNECTED (OPT-NSC)          | Discharge from inpatient treatment to the facility OPT-NSC rolls.                                                                                                                                                           | Discharge                   | Include             | Discharge                  |
| NON-VETERAN                              | Discharge of a patient from inpatient care who was treated in a status other than as a veteran.                                                                                                                             | Discharge                   | Include             | Discharge                  |
| OPT-SC                                   | Discharge from inpatient treatment to the OPT-SC rolls.                                                                                                                                                                     | Discharge                   | Include             | Discharge                  |
| REGULAR                                  | Regular discharge from inpatient treatment.                                                                                                                                                                                 | Discharge                   | Include             | Discharge                  |
| TO DOM FROM HOSP                         | Discharge type created for the AMIE package to be used when discharging a hospital patient for admission to a domiciliary ward.                                                                                             | Discharge                   | Include             | Discharge                  |
| TO IMLTC/NHCU FROM DOM                   | Discharge type created for AMIE for use when discharging a patient from a ward for admission to a nursing home care unit.                                                                                                   | Discharge                   | Exclude             | Excluded                   |
| TO IMLTC/NHCU FROM HOSP                  | Discharge type created for the AMIE package used when discharging a hospital patient to the nursing home care unit.                                                                                                         | Discharge                   | Include             | Discharge                  |
| TRANSFER OUT                             | Transfer out (discharge) to another VA facility from this VA facility.                                                                                                                                                      | Discharge                   | Include             | Discharge                  |
| VA IMLTC/NHCU TO CNH                     | Discharge type added for the AMIE package to be used when discharging a patient from a VA nursing home care unit to a community nursing home.                                                                               | Discharge                   | Include             | Discharge                  |
| WHILE ASIH                               | Discharge from VAD/VANH while in an ASIH status at other facility either by termination of inpatient care or exceeding the 30-day ASIH period.                                                                              | Discharge                   | Exclude             | Excluded                   |
| PROVIDER/SPECIALTY CHANGE                | Change of provider and/or treating specialty without any other change in status,  *i.e.*  , ward, room remain same as prior to change.                                                                                      | Specialty transfer          | Exclude             | Excluded                   |
| AUTH ABSENCE 96 HOURS OR LESS            | Transfer to an absence (pass) of 96 hours or less.                                                                                                                                                                          | Transfer                    | Exclude             | Excluded                   |
| AUTHORIZED ABSENCE                       | To an authorized absence status of more than 96 hours but not greater than 7 days for hospital or 30 days for NHCU/Domiciliary.                                                                                             | Transfer                    | Include             | Discharge                  |
| CHANGE ASIH LOCATION (OTHER FACILITY)    | Continuation of ASIH status but to another VA or Non-VA facility at VA expense.  [Previously called CONTINUED ASIH (OTHER FACILITY)]                                                                                        | Transfer                    | Exclude             | Excluded                   |
| FROM ASIH (VAH)                          | Return to NHCU or Domiciliary within the 30-day timeframe from Absence Sick in Hospital status.                                                                                                                             | Transfer                    | Include             | Admission                  |
| FROM AUTH. ABSENCE OF 96 HOURS OR LESS   | Return from a pass status which didn't exceed 96 hours in duration.                                                                                                                                                         | Transfer                    | Exclude             | Excluded                   |
| FROM AUTHORIZED ABSENCE                  | Return from authorized absence which was scheduled for greater than 96 hours.                                                                                                                                               | Transfer                    | Include             | Admission                  |
| FROM AUTHORIZED TO UNAUTHORIZED ABSENCE  | Transfer from an authorized absence status to an unauthorized absence status.                                                                                                                                               | Transfer                    | Exclude             | Excluded                   |
| FROM UNAUTHORIZED ABSENCE                | Return from an unauthorized absence status within the 30-day limit (hospital) or 90-day limit (NHCU/Domiciliary).                                                                                                           | Transfer                    | Include             | Admission                  |
| FROM UNAUTHORIZED TO AUTHORIZED ABSENCE  | Transfer from unauthorized absence to authorized absence status.                                                                                                                                                            | Transfer                    | Exclude             | Excluded                   |
| INTERWARD TRANSFER                       | Transfer from one ward location in the VA facility to another.                                                                                                                                                              | Transfer                    | Include             | Transfer                   |
| RESUME ASIH IN PARENT FACILITY           | Return to the parent VAH to continue ASIH status after being ASIH in another VA or non-VA facility.  [Previously called CONTINUED ASIH]                                                                                     | Transfer                    | Include             | Admission                  |
| TO ASIH (OTHER FACILITY)                 | To Absent Sick in Hospital Status (ASIH) to somewhere other than the parent VA Hospital.                                                                                                                                    | Transfer                    | Include             | Discharge                  |
| TO ASIH (VAH)                            | Transfer from NHCU/Domiciliary to VA hospital for further care in Absent Sick in Hospital status.  Can't exceed 30 days in duration.                                                                                        | Transfer                    | Include             | Discharge                  |
| UNAUTHORIZED ABSENCE                     | To an unauthorized absence status of not more than 30 days for hospital or 90 days for NHCU/Domiciliary.                                                                                                                    | Transfer                    | Include             | Discharge                  |

## Glossary

| **Glossary of Terms**                                                   | **Definitions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access Code                                                             | A code that allows the computer to identify  a user authorized to gain access to the computer. The code is greater than six and less than twenty characters long; can be numeric, alphabetic, or a combination of both.  The code is usually assigned to a user by a site manager or application coordinator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADPAC                                                                   | Automated Data Processing Coordinator.  The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they run into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or Information Resource Management (IRM).                                                                                                                                                                                                                                                                                                                                                                                                                    |
| FileMan                                                                 | FileMan is a set of M or MUMPS utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.  FileMan’s first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.                                                                                                                                                                                                                                                                                                                                                                 |
| FORUM                                                                   | FORUM is the VA’s national-scale email system. FORUM uses the VistA mail software and provides an excellent interface for threaded messages that can take the form on ongoing discussions. The National Patch Module is a VistA application that helps developers to manage the numbering, inventory, and release of patches. Patches are developed in response to request submissions and an error reporting request system known as National Online Information Sharing. A process called the Kernel Installation Distribution System (KIDS) is used to roll up patches into text messages that can be sent to sites along with installation instructions. The patch builds are sent as text messages via email, and the recipient (e.g., a site administrator) can run a PackMan function to unpack the KIDS build and install the selected routines.                                                                                                       |
| File Transfer Protocol (FTP)                                            | A client-server protocol which allows a user on one computer to transfer files to and from another computer over a TCP/IP network. Also the client program the user executes to transfer files. It is defined in Internet Standard 9, Request for Comments 959.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Globals                                                                 | M uses globals or variables which are intrinsically stored in files and which persist beyond the program or process completion.  Globals appear as normal variables with the caret character in front of the name. For example, the M statement…  SET ^A(“first\_name”)=”Keeley”  …will result in a new record being created and inserted in the persistent just as a file persists in an operating system.  Globals are stored, naturally, in highly structured data files by the language and accessed only as M globals.  Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of M is based on its ability to handle all this flawlessly and invisibly to the programmer.  One of the most common M programs is a database management system; FileMan is an example.  M allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns. |
| Kernel                                                                  | The VistA software that enables VistA applications to coexist in a standard operating system independent computing environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Kernel Installation and Distribution System (KIDS)                      | KIDS provides a mechanism to create a distribution of packages and patches; allows distribution via a MailMan message or a host file; and allows queuing the installation of a distribution for off-hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| LIM                                                                     | Laboratory Information Manager.  The LIM manages the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other Computerized Patient Record System (CPRS) functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| M                                                                       | M is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. M data structures are sparse, using strings of characters as subscripts.  M was formerly (and is still commonly) called MUMPS, for Massachusetts General Hospital Utility Multiprogramming System.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Massachusetts General Hospital Utility Multi-Programming System (MUMPS) | See M                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MailMan                                                                 | MailMan is an electronic messaging system that transmits messages, computer programs, data dictionaries, and data between users and applications located at the same or at different facilities.  Network MailMan disseminates information across any communications medium.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MUMPS                                                                   | See M                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Namespace                                                               | A logical partition on a physical device that contains all the artifacts for a complete M system, including globals, routines, and libraries. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines.  In VistA, namespaces are usually dedicated to a particular function. The MMMS namespace, for example, is designed for use by MDRO-PT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PackMan                                                                 | A specific type of MailMan message used to distribute KIDS builds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| VAMC                                                                    | Department of Veterans Affairs Medical  Center.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## 9 

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MMRS*1*5 User Guide

### Dependencies

Release MMRS*1.0*5 includes the following dependencies:

- MMRS*1.0*4
- LR*5.2*463
- Remediation steps completed per the MMRS*1.0*4 *Post-Installation Remediation Guide* .  The guide is available on the Department of Veterans Affairs Software Document Library (VDL).

### Constraints

Security controls will be inherited from VistA and therefore will be fully compliant with National Institute of Standards and Technology (NIST) controls and in compliance with Directive 6500.  In addition, the MMRS*1.0*5 release will be 508 compliant and designed to ensure no performance impacts will be experienced in the production environments.
