---
consolidated_title: "emergency dept integration software gui (edis) technical manual"
app_code: EDIS
doc_type: technical-manual
master_source: "Emergency Dept Integration Software GUI (EDIS) Version 2.1.2 Technical Manual"
master_pub_date: July 2013
consolidated_from: 2 versions
prior_versions:
  - "Emergency Dept Integration Software GUI (EDIS) Version 2.2.1 Technical Manual"
---

# Emergency Department Integration Software (EDIS)

# Technical Manual

<!-- image -->

VistA EDP*2.0*2

GUI EDIS Version 2.1.2


July 2013

Department of Veteran Affairs (VA)

Office of Information and Technology (OIT)

Product Development

**Revision History**

| Date        |   Version | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Author                        |
|-------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| 5/2018      |      2.11 | Patch EDP*2.0*9  Updated the Discharge Diagnosis Files  Removed reference of $$ICDONE^LEXU  and corrected ICD9 CODE to remove the 9  Updated title page and footers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | HPS Clinical Sustainment Team |
| 11/2014     |      2.1  | Patch EDP*2.0*2, GUI 2.1.2:  Updated title page, headers, and footers.  Corrected table formatting throughout document.  Reformatted all headings to replace manual Table of Contents with automated one.  Added alt text to Figure 1.  Updated Sections 1.3 and 1.4 for EDIS v.2.1.2/EDP*2.0*2.  Updated EDIS URLs in Section 2.1.3 (new URLs for EDIS v.2.1.2/EDP*2.0*2).  Updated Section 4 Routines for EDIS v.2.1.2/EDP*2.0*2.  Removed Provider Report:  Deleted EDPRPT6 from Section 4.1 EDIS Routines and from Index; Deleted EDPR PROVIDER Security Key from Section 8.3 and from Index.  Corrected description for CPE Role (#232.5), Field .03 XML ABBREVIATION, in Table 26.  Added notes to Sections 3.1, 7.1, 8.3, 9.1, and 10.1 about EDPF BIGBOARD KIOSKS option/parameter/list template no longer being used as of EDIS v.2.1.1/EDP*2.0*6. | REDACTED                      |
| August 2014 |      2.9  | Patch EDP*2*2, GUI 2.1.1-ICD-10  Added information on EDPLEX routine (p. 12)  Updated to ICD-10 reference (p. 13)  Added and updated routine names and checksums (p.16).  Updated to reference ICD-10 codes and text in the Discharge Diagnosis Files (p. 30)  Updated to reference ICD-10 codes and text in the Tracking Area File (p. 47)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                      |
| 07/17/2013  |      2.8  | Update to remove zip reference                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ProdDev                       |
| 07/10/2013  |      2.7  | Updated checksum value for EDPLOGA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED                      |
| 07/10/2013  |      2.7  | Technical Edits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                      |
| 06/20/2013  |      2.6  | Incorporate Product Support updates                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Prod Development              |
| 06/20/2013  |      2.6  | Updated footer , TOC, and addressed text styles for 508 compliance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED                      |
| 05/12/2013  |      2.5  | Final review prior to submission                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED                      |
| 05/11/2013  |      2.5  | Updated cover page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED                      |
| 5/10/2013   |      2.5  | Additional technical reviews                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | REDACTED                      |
| 2/20/2013   |      2.4  | Updated URLs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | REDACTED                      |
| 1/14/2013   |      2.3  | Incorporate Product Support Feedback                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | REDACTED                      |
| 1/10/13     |      2.2  | Edited file to reflect changes from a patch to a host file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                      |
| 01/04/2013  |      2.1  | Final review prior to submission                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED                      |
| 01/03/2013  |      2.1  | Addressed Product Support Feedback                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | EDIS Team                     |
| 11/30/2012  |      2    | Final review prior to submission                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED                      |
| 11/29/2012  |      2    | Updated footer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED                      |
| 10/30/2012  |      1.9  | Made updates (incorporated edits from [T.S.])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED                      |
| 10/26/2012  |      1.8  | Updated links within document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED                      |
| 09/28/2012  |      1.7  | Additional technical reviews                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | REDACTED                      |
| 09/05/2012  |      1.6  | Final review prior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED                      |
| 9/04/2012   |      1.6  | Review & edits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED                      |
| 8/30/2012   |      1.6  | Technical Edits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                      |
| 6/22/2012   |      1.5  | Technical Edits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                      |
| 6/22/2012   |      1.5  | Review                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED                      |
| 5/21/2012   |      1.4  | Final Review prior to submission                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED                      |
| 05/15/2012  |      1.4  | Technical Edits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                      |
| 5/15/2012   |      1.4  | Review                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED                      |
| 03/04/2012  |      1.3  | Final review prior to submission                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED                      |
| 03/03/2012  |      1.3  | Technical Edits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                      |
| 03/01/2012  |      1.3  | Technical edits and additions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED                      |
| 01/11/2012  |      1.2  | Final review prior to submission                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED                      |
| 01/08/2012  |      1.2  | Technical Edits                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                      |
| 01/07/2012  |      1.1  | Technical Review                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED                      |
| 01/06/2012  |      1    | Draft                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED                      |

**Table of Contents**

1.	Product Description	1

1.1.	About this Guide	1

1.2.	Section 508 of the Rehabilitation Act of 1973	1

1.3.	Referenced Documents and Files	1

1.4.	File Retrieval	2

1.5.	Document Conventions	3

2.	General Information	4

2.1.	Architectural Scope	4

2.1.1.	Web Application	4

2.1.2.	EDIS Display Boards	4

2.1.3.	URLs	4

2.1.3.1.	EDIS in Production Accounts	4

2.1.3.2.	EDIS in Test Accounts	4

2.2.	System Performance	5

2.2.1.	Scaling Guide: Memory and CPU	5

2.2.2.	Disk Space	6

2.3.	EDIS KIDS Install	6

2.3.1.	Retrieve patch EDP*2*2	6

2.3.2.	Install patch EDP*2*2	6

3.	Parameters	8

3.1.	EDIS (EDPF) Parameters	8

3.1.1.	Setting Up Synchronization with Patient Care Encounters	9

4.	Routines	11

4.1.	EDIS Routines	11

4.2.	EDIS Checksums	16

5.	Files and Globals	20

5.1.	Globals	20

5.2.	Files	21

5.2.1.	File Descriptions	21

5.2.1.1.	ED Log (#230)	21

5.2.1.2.	Discharge Diagnosis 230.04	30

5.2.1.3.	Orders 230.08	31

5.2.1.4.	Record Indices for File #230	32

5.2.1.5.	ED Log History (230.1)	34

5.2.1.6.	Record Indices for File (230.1)	38

5.2.1.7.	Tracking Staff (231.7)	38

5.2.1.8.	Record Indices for File (231.7)	39

5.2.1.9.	Tracking Room-Bed (#231.8)	40

5.2.1.10.	Record Indices for (#231.8)	43

5.2.1.11.	Tracking Area (#231.9)	43

5.2.1.12.	Display Board Configuration Subfile (231.94)	46

5.2.1.13.	Tracking Code (233.1)	47

5.2.1.14.	Tracking Code File Indices (#233.1)	48

5.2.1.15.	Tracking Code Set (#233.2)	49

5.2.1.16.	Codes (233.21)	49

5.2.1.17.	CPE Role (#232.5)	50

5.2.1.18.	EDP Worksheet Specification (#232.6)	52

5.2.1.19.	Subfile: Sections (#232.62)	53

5.2.1.20.	Subfile: Components (#232.622)	54

5.2.1.21.	Subfile: Roles (#232.63)	55

5.2.1.22.	EDP Worksheet Section (#232.71)	55

5.2.1.23.	Subfile: Components (#232.711)	56

5.2.1.24.	Subfile: Roles (#232.712)	56

5.2.1.25.	EDP Worksheet Component (#232.72)	57

5.2.1.26.	Subfile: Parameters (#232.725)	58

5.2.1.27.	Subfile: Components (#232.727)	59

5.2.1.28.	Subfile: Roles (#232.728)	59

5.2.1.29.	Subfile: Validator (#232.729)	59

5.2.1.30.	EDP Worksheet Component Type (#232.73)	60

5.2.1.31.	NHAMCS Reason for Visit (#233.8)	60

5.2.1.32.	NHAMCS Reason for Visit Display (#233.81)	61

5.2.1.33.	ED Complaint (#233.82)	61

5.2.1.34.	Attribute (233.821)	62

5.2.1.35.	Possible Value (#233.8211)	62

5.2.1.36.	Associated Symptom (#233.822)	63

5.2.1.37.	Clinical Events (#234)	63

5.2.1.38.	EDP Report Template (#232.1)	65

5.2.1.39.	Subfile: Sequence (#232.12)	65

5.2.1.40.	Subfile: Roles (#232.13)	65

5.2.1.41.	EDP Report Elements (#232.11)	65

6.	Exported Remote Procedure Calls	67

6.1.	EDIS Remote Procedure Calls	67

6.1.1.	EDPCBRD RPC	67

6.1.2.	EDPCTRL RPC	67

6.1.3.	EDPGLOB RPC	67

7.	Exported Options	68

7.1.	EDIS Options	68

7.2.	Include EDIS Options in Users’ Menu Trees	70

7.2.1.	Assign EDIS Views to Users	70

8.	Security	72

8.1.	KAAJEE	72

8.2.	Secure Sockets Layer	72

8.2.1.	PKI Encryption Basics	72

8.3.	Security Keys	73

*8.3.1.	EDPF KIOSKS	73*

8.3.2.	EDPR EXPORT	73

8.3.3.	EDPF WORKSHEETS	73

8.3.4.	EDPR ADHOC	73

8.3.5.	EDPR XREF	73

8.3.6.	Assign Keys for Emergency Department Users	73

9.	Protocols	75

9.1.	EDIS Protocols	75

9.2.	Other Protocols	76

10.	List Templates	77

10.1.	EDIS List Templates	77

11.	Troubleshooting	77

11.1.	Check-in via Scheduling	77

11.2.	Blank View	77

11.3.	PCE Visits	77

11.3.1.	Check the EDPF LOCATION Parameter	77

11.3.2.	Check for Active Person Class	77

11.4.	Nurse Assignments	78

11.5.	Intermittent Login Difficulties	78

12.	Index	79

**List of Tables**

Table 1: Anonymous Software Directories	2

Table 2: Document Files	2

Table 3: Adobe Flash Minimum Hardware Requirements	5

Table 4:  Optimal Viewing Requirements	5

Table 5: Parameters	8

Table 6: EDIS Routine Checksums	16

Table 7: Global Placement and Protection	20

Table 8: XE Files	21

Table 9: File Descriptions	22

Table 10: Subfile – Discharge Diagnosis Files	31

Table 11: Subfile – XE Orders	31

Table 12: Record Indices for File #230	33

Table 13: XE ED Log History Files (#230.1)	34

Table 14: XE File Record Indices (230.1)	38

Table 15: XE Files – Tracking Staff (#231.7)	38

Table 16: XE Files Record Indices (231.7)	39

Table 17: XE Files – Tracking Room Bed (#231.8)	40

Table 18: XE Files – Record Indices (#231.8)	43

Table 19: XE Files – Tracking Area (#231.9)	43

Table 20: XE Files Display Board Configuration Subfile	46

Table 21: Files and Fields that Point to Tracking Code File	47

Table 22: Tracking Code (#233.1)	48

Table 23: Tracking Code File Indices (#233.1)	48

Table 24: Tracking Code Set (#233.2)	49

Table 25: Subfile – Tracking Code Set File – Codes (#233.21)	49

Table 26: CPE Role (#232.5)	50

Table 27: EDP Worksheet Specification (#232.6)	52

Table 28: Subfile – Sections (#232.62)	53

Table 29: Subfile – Components (#232.622)	54

Table 30: Subfile – Roles (#232.63)	55

Table 31: EDP Worksheet Section (#232.71)	55

Table 32: Subfile – Components (#232.711)	56

Table 33: Subfile – Roles (#232.712)	57

Table 34: EDP Worksheet Component (#232.72)	57

Table 35: Subfile – Parameters (#232.725)	59

Table 36: Subfile – Components (#232.727)	59

Table 37: Subfile – Roles (#232.728)	59

Table 38: Subfile – Validator (#232.729)	59

Table 39: EDP Worksheet Component Type (#232.73)	60

Table 40: NHAMCS Reason for Visit (#233.8)	60

Table 41: NHAMCS Reason for Visit Display (#233.81)	61

Table 42: ED Complaint (#233.82)	61

Table 43: Attribute (#233.821)	62

Table 44: Possible Value (#233.8211)	62

Table 45: Associated Symptom (#233.822)	63

Table 46: Clinical Events (#234)	63

Table 47: EDP Report Template (#232.1)	65

Table 48: Subfile – Sequence (#232.12)	65

Table 49: Subfile – Roles (#232.13)	65

Table 50: EDP Report Elements (#232.11)	66

Table 51: EDIS Options	68

**List of Figures**

Figure 1: The EDIS Topology	5

## Product Description

Emergency Department Integration Software (EDIS) incorporates several Web-based views that extend the current Computerized Patient Record System (CPRS) to help healthcare professionals track and manage the flow of patient care in the emergency - department setting. EDIS views are based on a class-three application developed by the Upstate New York Veterans Health Care Network —or Veterans Integrated Services Network (VISN) 2. Most views are site-configurable. EDIS enables you to:

- Add emergency-department patients to the application’s electronic whiteboard—or big board—display
- View information about patients on the display board
- Edit patient information
- Remove patients from the display board
- Create administrative and operational reports

The application also includes views for entering patients’ dispositions and configuring the display board.

### About this Guide

*Emergency Department Integration Software Technical Manual* provides technical information for configuring, managing, and troubleshooting local (M Server) components of the EDIS application.  This guide is specific to EDIS v2.1.2/EDP*2.0*2.

### Section 508 of the Rehabilitation Act of 1973

Section 508 Compliance Testing is required for an application utilizing a Graphical User Interface (GUI), such as CPRS or BCMA. Roll and scroll VistA Legacy applications written in MUMPS need not comply with Section 508 Compliance requirements.

**NOTE:** EDIS received a 508 exception on 12/17/2012.

### Referenced Documents and Files

The following documents and files are available on the Anonymous software directories identified in the table below.

- EDIS v.2.1.2 Server and Client Installation Guide
- EDIS v.2.1.2 Big Board Installation Guide
- EDIS v.2.1.2 Release Notes
- EDIS v.2.1.2 Technical Manual
- EDIS v.2.1.2 User Guide
- EDIS Glossary
- EDIS Installation Zip File (contains Launch\_EDIS.bat and edisautologon.reg)

The documents (except the zip file) are also available on the VistA Documentation Library (VDL), which is located at [http://www.va.gov/vdl/application.asp?appid=179](http://www.va.gov/vdl/application.asp?appid=179) .

### File Retrieval

Files are available on the Anonymous software directories identified in the table below.

Table 1: Anonymous Software Directories

| OI&T Field Office   | FTP Address   | Directory   |
|---------------------|---------------|-------------|
| Albany              | REDACTED      | REDACTED    |
| Hines               | REDACTED      | REDACTED    |
| Salt Lake City      | REDACTED      | REDACTED    |
| VistA Download Site | REDACTED      | REDACTED    |

The documents appear on the Anonymous software directories under the file names listed in the table below.

Table 2: Document Files

| File Name                                                                                                                                                                                                                                                                                           | Title                                                                                        | FTP Mode   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------|
| EDIS_2_1_2_IG.PDF                                                                                                                                                                                                                                                                                   | Emergency Department Integration Software Version 2.1.2 Server and Client Installation Guide | Binary     |
| EDIS_2_1_2_BigBrd_IG.PDF                                                                                                                                                                                                                                                                            | Emergency Department Integration Software Version 2.1.2 Big Board Installation Guide         | Binary     |
| EDIS_2_1_2_RN.PDF                                                                                                                                                                                                                                                                                   | Emergency Department Integration Software Version 2.1.2 Release Notes                        | Binary     |
| EDIS_2_1_2_TM.PDF                                                                                                                                                                                                                                                                                   | Emergency Department Integration Software Version 2.1.2 Technical Manual                     | Binary     |
| EDIS_2_1_2_UG.PDF                                                                                                                                                                                                                                                                                   | Emergency Department Integration Software Version 2.1.2 User Guide                           | Binary     |
| EDIS_2_1_2_Glossary.PDF                                                                                                                                                                                                                                                                             | Emergency Department Integration Software Glossary                                           | Binary     |
| EDP2\_1\_1.zip  **NOTE:**  The zip file and its contents have NOT been updated for the EDIS v.2.1.2/EDP*2.0*2 release.  The file is included with the latest release documentation for ease of reference but is still named for the release in which it was last modified (EDIS v.2.1.1/EDP*2.0*6). | Emergency Department Integration Software Installation Package Zip File                      | Binary     |

### Document Conventions

**Bold type** indicates application elements (views, panes, links, buttons, text boxes, and so forth) and key names.

Key names appear in angle brackets &lt;&gt;.

*Italicized text* indicates special emphasis or user responses. ALL CAPS indicates M routines and options.

… (Ellipses) indicate omitted text.

## General Information

### Architectural Scope

EDIS runs as a Web application on a centrally located Oracle WebLogic server that contains program logic and operational emergency-department data in its Java middle tier. (Refer to **Figure 1** .) The presentation tier is a Flash Player application. The data tier encompasses local sites’ Veterans Health Information Systems and Technology Architecture (VistA) systems and a centrally located relational database management system (RDMS) data store containing Standard Data Services (SDS) tables.

The application uses remote procedure calls (RPCs) from local VistA implementations to populate patient - and provider-selection lists, provide limited data synchronization between EDIS and CPRS, and determine users’ access levels.

#### Web Application

The application’s presentation tier runs in users’ Web browsers via Adobe Flash Player. The VA’s Kernel Authentication and Authorization for Java 2 Enterprise Edition (KAAJEE) provides end-user authentication.

#### EDIS Display Boards

Sites can configure one or more electronic whiteboard—or big board—displays. Display boards run in their own browser-based instances of Flash Player.

#### URLs

#### EDIS in Production Accounts

When EDIS is running in your site’s production account, use [https://vaww.edisprod2.med.va.gov/main](https://vaww.edisprod2.med.va.gov/main) for user access to the main application and [https://vaww.edisprod2.med.va.gov/main/board.html](https://vaww.edisprod2.med.va.gov/main/board.html) for your main big-board display.

For secondary big-board displays, append the following argument: board=your\_secondary\_board\_name.  Your institution must be placed in the sitecode parameter.  For example, if your site has a secondary display board named *Lab;* its URL would be: [https://vaww.edisprod2.med.va.gov/main/board.html?sitecode=442&amp;board=Lab](https://vaww.edisprod2.med.va.gov/main/board.html?sitecode=442&board=Lab) .

#### EDIS in Test Accounts

When EDIS is running in your site’s test account, use [https://preprod.edispreprod2.med.va.gov/main](https://preprod.edispreprod2.med.va.gov/main) for user access to the main application.

<!-- image -->

Figure : The EDIS Topology

### System Performance

#### Scaling Guide: Memory and CPU

Workstations should comply with VA Desktop Minimum Acceptable Configurations ( [http://vaww. vairm. vaco.va. go v/VADesktop](http://vaww.vairm.vaco.va.gov/VADesktop) ). In addition, users’ workstations should meet the minimum hardware requirements for running Adobe Flash Player; see table below.

Table : Adobe Flash Minimum Hardware Requirements

| Platform   | CPU                                                                                                                | RAM    |
|------------|--------------------------------------------------------------------------------------------------------------------|--------|
| Windows    | Intel Pentium II 450MHz or faster processor (or equivalent), AMD Athlon 600MHz or faster processor (or equivalent) | 128 MB |
| Macintosh  | PowerPC G3 500MHz or faster processor or Intel Core Duo 1.33GHz or faster processor                                | 128 MB |

See table below for Optimal Viewing Requirements.

Table :  Optimal Viewing Requirements

| Resolution                                    | CPU                                                | RAM                        |
|-----------------------------------------------|----------------------------------------------------|----------------------------|
| 852 x 480 (480 p), 24 frames per second (fps) | Intel Pentium 4 2.33 GHz processor (or equivalent) | 256 MB RAM with 64 MB VRAM |
| 1280 x 720 (720 p), 24–30  fps                | Intel Pentium 4 3 GHz processor (or equivalent)    | 128 MB RAM with 64 MB VRAM |
| 1920 x 1080 (1080 p) 24 fps                   | Intel Core Duo 1.8 GHz processor (or equivalent)   | 128 MB RAM with 64 MB VRAM |

#### Disk Space

EDIS installation creates files in two global: ^EDP and ^EDPB.

- You can expect ^EDP to grow at the following yearly rate: 2,000 bytes multiplied by the number of emergency-department visits per year. For example, if your emergency department responds to an average of 12,000 visits every year, you can expect ^EDP to grow at a yearly rate of 24 MB. You should place this global in a volume with sufficient space to manage this growth.
- You can expect ^EDPB to remain small. (It is currently about 50 K.)

### EDIS KIDS Install

For more information, refer to the EDIS v.2.1.2 Server and Client Installation Guide (see Section 1.4 above).

#### Retrieve patch EDP*2*2

**NOTE:** The EDP .ear file for the Graphical User Interface will show a version of 2.1.2, while patch 2 for VistA will show a version of 2.0. This is alright and should not be a reason for concern. The application guides will appear with version 2.1.2.

EDP*2*2 is a FORUM patch and will be pushed to the IRM’s by product support. Once you have been notified that the patch has been pushed, you can retrieve and extract the patch from Mail Manager.

#### Install patch EDP*2*2

Follow these instructions to install EDIS v2.1.2 (EDP*2.0*2).  This patch should be installed during a period of low system activity with EDIS users off the system.  No options need to be placed out of service.  Installation time is expected to be less than 5 minutes.

**NOTE:** Coordination of the M server installation must be synchronized with the update of the EDIS URLs, which are used on the desktop client and the Big Board monitor.  For more information, refer to the EDIS v.2.1.2 Server and Client Installation Guide and the EDIS v.2.1.2 Big Board Installation Guide (see Section 1.4 above).

1. Choose the PackMan message containing this patch.
2. Choose the INSTALL/CHECK MESSAGE PackMan option.
3. From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation Menu.  From this menu, you may elect to use the following option.  When prompted for the INSTALL enter the patch #(ex.EDP*2.0*2):

1. Backup a Transport Global - This option will create a backup message of any routines exported with this patch.  It will not backup any other changes such as DDs or templates.
2. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed.  It compares all components of this patch (routines, DDs, templates, etc.).
3. Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

4. From the Installation Menu, select the Install Package(s) option and choose the patch to install.  Enter EDP*2.0*2.
5. If prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer ‘NO’.
6. When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer ‘NO’.
7. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer ‘NO’.
8. If prompted “Delay Install (Minutes): (0 – 60): 0//’, respond ‘0’.

## Parameters

### EDIS (EDPF) Parameters

Table : Parameters

| EDPF Parameter Name     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EDPF BIGBOARD KIOSKS    | NOTE: This parameter is no longer used as of EDIS v.2.1.1/EDP*2.0*6.  This parameter maps fully qualified computer names to display board names. Sites must add or change values for this parameter via the EDPF BIGBOARD KIOSKS option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| EDPF DEBUG START TIME   | This parameter sets a $H timestamp to signal that EDIS should log out its RPCs for 30 minutes following the debug time stamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| EDPF LOCATION           | This parameter holds one or more entries from the Hospital Location (#44) file. Entries correspond to hospital locations that the emergency department uses. With this parameter, VistA prompts sites for a time range or sequence. If sites have multiple Hospital Location file entries, they have two choices when responding to the Time Range or Sequence prompt: they can enter a time range or a sequence.  Entering a time range allows EDIS to map Hospital Location entries by time of day. EDIS uses this mapping when users create encounters in the Patient Care Encounters (PCE) package: it matches the Hospital Location entry based on the current time of day. The parameter accepts ranges in military time.  Entering a sequence allows sites to map Hospital Location entries in order of preference. When users create encounters in PCE, EDIS uses the entry with the lowest sequence number to create visits.  When users create appointments by checking in patients via the Scheduling package, any matches on this parameter’s list of locations (be they time- or sequence-based) cause EDIS to add the checked-in patient to the display board. |
| EDPF NURSE STAFF SCREEN | This parameter allows sites to select the type of filtering upon which EDIS bases its nurse-selection list. It applies filtering—or screening— to the New Person file (#200). By default, EDIS allows selections from all entries in the New Person file. Other screening options include the following:  - Allow only persons holding the ORELSE key - Allow only persons holding the PSJ RNURSE key - Allow only persons who are present and active in the Nurse Staff file (#210)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| EDPF SCHEDULING TRIGGER | This parameter allows sites to specify which Scheduling package event, triggers EDIS to automatically add patients to the board. Sites can choose from one of the following two selections:  1: Patient will be added to the board when an appointment is made  4: Patient will be added to the board when checked in  Sites can set this parameter at the package, system, or division level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| EDPF SCREEN SIZES       | This parameter contains a list of selectable screen sizes for sites’ EDIS display boards. The parameter generally lists large-display LCD or plasma screen sizes. Add screen sizes to this parameter using the following format: WxH (width multiplied by height). You can set this parameter at the package, system, or division level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| EDP APP COUNTDOWN       | This parameter contains the number of countdown seconds before the application closes. Once the timeout is met, this is the number that the counter will start with as it begins countdown for closure. If this parameter is set at 15, after the timeout has occurred, the user will be given 15 seconds to respond to a dialog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| EDP APP TIMEOUT         | This holds the number of seconds until the application times out. If set, this value over rides the user’s DTIME value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

#### Setting Up Synchronization with Patient Care Encounters

The EDPF LOCATION parameter should contain the hospital location or locations that your emergency department uses. If yours is a multi -division site, make an entry for each division.

- 3.1.1.1. Log in to VistA.
- 3.1.1.2. At the Select **OPTION NAME** prompt, type *xpar menu* (for **XPAR MENU TOOLS** ) and then press the &lt; **Enter** &gt; key.
- 3.1.1.3. At the Select **General Parameter Tools** option prompt, type *ep* (for **Edit**

**Parameter Values** ) and then press the &lt; **Enter** &gt; key.

- 3.1.1.1. At the Select **PARAMETER DEFINITION NAME** prompt, type *edpf l* (for

**EDPF LOCATION** ) *,* and then press the &lt; **Enter** &gt; key.

- 3.1.1.1. At the Select **INSTITUTION NAME** prompt, type the name or station number of your institution and then press the &lt; **Enter** &gt; key.
- 3.1.1.2. At the Select **Time Range (ex. 0800-1200) or Sequence** prompt, type the time range during which the clinic location you are about to select functions as your site’s emergency department. Use military time. For example, if the location serves as your site’s emergency department 24 hours a day, type *0001-2400* Alternately, type a number that represents the location’s preference rating (the number *1* represents the most-preferred location). Press the &lt; **Enter** &gt; key. When users create a PCE encounter, EDIS uses time-of-day-based or preference-based criteria to determine the encounter’s location.

**NOTE:** When selecting time ranges, take care to account for all hours of emergency-department operation. EDIS does not create PCE appointments for patients whom users add during times that you don’t include in the EDPF LOCATION parameter. For example, suppose you set the parameter to use Clinic A from 0700 to 0800 hours and Clinic B from 0900 to 1200 hours. If a user then adds a patient at 0830 hours, EDIS will not create a PCE appointment for the patient. Also, take care not to overlap hours. In cases where hours overlap, EDIS always creates the patient’s PCE appointment for the first clinic.

- 3.1.1.1. At the **Are you adding [** ***your time range or sequence*** **] as a new Time Range or Sequence? Yes//** prompt, press the &lt; **Enter** &gt; key to accept the time range or sequence—or, if you’ve made a mistake, type the letter *n* (for *No* ) and press the &lt; **Enter** &gt; key.
- 3.1.1.2. VistA displays a confirmation: **Time Range (ex. 0800-1200) or Sequence [** ***your time range or sequence*** **]//.** Press the &lt; **Enter** &gt; key to acknowledge this confirmation.
- 3.1.1.3. At the **ED LOCATION** prompt, type the name of the location that serves as your site’s emergency department during this time range (or for this preference rating) and press the &lt; **Enter** &gt; key.
- 3.1.1.4. Repeat steps 6 through 9 for additional emergency-department locations.

## Routines

### EDIS Routines

### EDIS Checksums

The following table contains routine names with before and after EDIS v.2.1.2/EDP*2.0*2 checksums:

Table 6: EDIS Routine Checksums

| Updated with EDIS v2.1.2/ EDP*2.0*2   | Routine Name   | Before Checksum   |   After Checksum |
|---------------------------------------|----------------|-------------------|------------------|
| X                                     | EDP22PST       | N/A               |           737172 |
|                                       | EDP2ENV        | 653636            |           653636 |
|                                       | EDP2PRE        | 852824            |           852824 |
|                                       | EDP2PST        | 10565179          |         10565179 |
|                                       | EDPARPT        | 95079217          |         95079217 |
|                                       | EDPARPT1       | 17834740          |         17834740 |
|                                       | EDPBCF         | 26108693          |         26108693 |
|                                       | EDPBCM         | 17332251          |         17332251 |
|                                       | EDPBDL         | 11063047          |         11063047 |
|                                       | EDPBKS         | 15371728          |         15371728 |
|                                       | EDPBLK         | 7330093           |          7330093 |
|                                       | EDPBPM         | 6261242           |          6261242 |
|                                       | EDPBRM         | 26325333          |         26325333 |
|                                       | EDPBRS         | 19233483          |         19233483 |
|                                       | EDPBSL         | 20029785          |         20029785 |
|                                       | EDPBST         | 9812007           |          9812007 |
|                                       | EDPBWS         | 229022529         |        229022529 |
|                                       | EDPCBRD        | 4768831           |          4768831 |
|                                       | EDPCDBG        | 4038807           |          4038807 |
| X                                     | EDPCONV        | 69787121          |         70928886 |
|                                       | EDPCONV1       | 10237522          |         10237522 |
|                                       | EDPCSV         | 1174493           |          1174493 |
|                                       | EDPCTRL        | 89022760          |         89022760 |
|                                       | EDPDD          | 1577854           |          1577854 |
|                                       | EDPDTL         | 80102068          |         80102068 |
| X                                     | EDPFAA         | 36904209          |         37763699 |
| X                                     | EDPFLEX        | 1745474           |         10693270 |
|                                       | EDPFMON        | 26481799          |         26481799 |
|                                       | EDPFMOVE       | 44917407          |         44917407 |
|                                       | EDPFPER        | 4359382           |          4359382 |
|                                       | EDPFPTC        | 19115099          |         19115099 |
|                                       | EDPFPTL        | 4915038           |          4915038 |
|                                       | EDPFX233       | 2082229           |          2082229 |
|                                       | EDPGLOB        | 4109172           |          4109172 |
|                                       | EDPHIST        | 59451957          |         59451957 |
|                                       | EDPLAB         | 51111821          |         51111821 |
| X                                     | EDPLEX         | N/A               |         11049187 |
| X                                     | EDPLOG         | 58048189          |         64279489 |
|                                       | EDPLOG1        | 2583250           |          2583250 |
|                                       | EDPLOGA        | 12583805          |         12583805 |
|                                       | EDPLOGH        | 12593326          |         12593326 |
| X                                     | EDPLPCE        | 32808524          |         39952113 |
|                                       | EDPMAIL        | 7450955           |          7450955 |
|                                       | EDPMED         | 4429388           |          4429388 |
|                                       | EDPQAR         | 7638401           |          7638401 |
|                                       | EDPQDB         | 56093021          |         56093021 |
|                                       | EDPQDBS        | 7446153           |          7446153 |
| X                                     | EDPQLE         | 43232281          |         55054483 |
|                                       | EDPQLE1        | 11912520          |         11912520 |
|                                       | EDPQLP         | 12368052          |         12368052 |
|                                       | EDPQLW         | 6750208           |          6750208 |
| X                                     | EDPQPCE        | 3317665           |          6816999 |
|                                       | EDPQPP         | 92368102          |         92368102 |
|                                       | EDPQPPS        | 4046541           |          4046541 |
|                                       | EDPRPT         | 25243776          |         25243776 |
| X                                     | EDPRPT1        | 50357723          |         51586751 |
| X                                     | EDPRPT10       | 30220543          |         32122849 |
|                                       | EDPRPT11       | 8059237           |          8059237 |
|                                       | EDPRPT12       | 8703521           |          8703521 |
|                                       | EDPRPT13       | 7846285           |          7846285 |
| X                                     | EDPRPT2        | 24332800          |         26475007 |
|                                       | EDPRPT3        | 14278258          |         14278258 |
|                                       | EDPRPT4        | 32540898          |         32540898 |
|                                       | EDPRPT5        | 52072453          |         52072453 |
|                                       | EDPRPT6        | 9636184           |          9636184 |
| X                                     | EDPRPT7        | 20666458          |         23000869 |
| X                                     | EDPRPT7C       | 22153636          |         24197469 |
|                                       | EDPRPT8        | 15923220          |         15923220 |
|                                       | EDPRPT9        | 1597193           |          1597193 |
| X                                     | EDPRPTBV       | 28273730          |         30889629 |
|                                       | EDPUPD         | 6705060           |          6705060 |
|                                       | EDPVIT         | 32884634          |         32884634 |
|                                       | EDPWS          | 17524272          |         17524272 |
|                                       | EDPWSL         | 7192929           |          7192929 |
|                                       | EDPWSLM        | 3855274           |          3855274 |
|                                       | EDPWSP         | 7526722           |          7526722 |
| X                                     | EDPX           | 12709600          |         16354064 |
|                                       | EDPXML         | 13678293          |         13678293 |
|                                       | EDPYCHK        | 1074868           |          1074868 |
|                                       | EDPYP2         | 8435306           |          8435306 |
|                                       | EDPYPRE        | 13981628          |         13981628 |
|                                       | EDPYPST        | 35872203          |         35872203 |

## Files and Globals

### Globals

- **[Updated with EDP*2.0*2]** EDP22PST - Post-init for facility install.

- EDP2PST – Post-init for facility install.

- EDPARPT - This routine handles the following functions
    - Saving/Modifying report templates
    - Building new report templates
    - Executing existing report templates as well as ad-hoc reports (fully custom unsaved reports).
- EDPARPT1 – Ad Hoc Reports.

- EDPBCF loads and saves display-board configuration settings—including column values, color maps, room and area values, parameter settings, and screen-size settings. It also loads a list of display boards and their specifications.

- EDPBCM creates and saves configuration settings for color maps. It creates color-map elements, closing tags, map elements for standard urgencies, and single map elements. It also builds color-map selection lists.

- EDPBDL deletes or inactivates configuration entries. It deletes rooms or beds if the application’s log entries are not referencing them; otherwise, it inactivates the rooms or beds.

- EDPBKS supports a list template that maps fully qualified machine names to the names of EDIS big-board displays; this routine enables sites to add, change, and delete large displays that run in kiosk mode.

- EDPBLK handles locking and unlocking for configuration settings. It displays one of three error messages when one user attempts to make or save configuration changes while another user is also making or saving changes.

- EDPBPM loads current and saves updated **Configuration** view parameter settings (diagnosis required, coded diagnosis required, disposition required, reason for delay required, number of minutes before reason for delay is required, shift start time and duration, include residents, default room or area, and arriving-ambulance area). It also saves time zone differences (in minutes) and sets the fail node.

- EDPBRM loads a list of all rooms and beds in sequence, builds an XML output file containing this list, and keeps the list updated. It also adds and updates room-and-area records, loads multi-assignment areas and choice lists (display-when, single- and multiple-patient assignments, and so forth).

- EDPBRS sets and resets display-board specifications (default-board specifications, display width, scroll-delay time, column size, column headers and size, font size, row colors, baseline rooms, and baseline parameters).

- EDPBSL loads selection lists (acuity, status, mode of arrival, disposition, and reason for delay) and builds XML output files for them. It also saves selection-list changes; creates new code sets; clears codes from, and adds new codes to, the CODES multiple; and updates existing codes in, and adds new codes to, the Tracking Code file (#233.1).

- EDPBST returns a list of staffing matches from VistA’s New Person file (#200). For each of the following three roles, it builds a list of staff members who have an active person class: resident, physician, and nurse. It also saves updated staff members and creates and updates records in the Tracking Staff file (#231.7).

- EDPBWS is the main routine for processing, building, retrieving, and modifying worksheets for the EDIS User Interface.

- EDPCBRD is the controller for the EDIS display board. It processes requests via remote procedure calls (RPCs) and also supports a Caché Server Pages (CSP) mode for processing requests via CSP.

- EDPCDBG is the debugging routine for the display-board controller. It turns debugging on and off, enables the EDIS debugging log, logs debugging activities for 30 minutes after the debugging start time, records debugging start and stop times, and saves debugging requests and XML results.

- **[Updated with EDP*2.0*2]** EDPCONV processes incoming mail to convert emergency-department visits from Syracuse class-three application files to EDIS class-one files. It stores conversion data in the Tracking Code file (#233.1), Tracking Room/Bed file (#231.8), ED Log file (#230), and ED Log History file (#230.1).

- EDPCONV1 converts configuration data from Syracuse class-three application files to EDIS class-one files. It stores converted data in the Tracking Area file (#231.9).

- EDPCSV is a comma-separated-value (CSV) utility that provides a controller for HyperText Transfer Protocol (HTTP) requests.

- EDPCTRL is the controller for EDIS. It processes requests via remote procedure calls (RPCs) and also supports Caché Server Pages (CSP) mode for processing requests via CSP.

- EDPDD provides a test update log.

- **[Updated with EDP*2.0*2 (internal operations to update ICD-10 activation date)]** EDPFAA provides RPC calls to the local facility. It also sets up EDIS sessions and returns role-based views for users. (EDPFAA code enabled VHA eHealth University [VeHU] training.)

- **[Updated with EDP*2.0*2]** EDPFLEX provides Lexicon-package utilities: it returns matches from the Lexicon package when users type in dispositions.

- EDPFMON monitors Health Level 7 (HL7) VistA event messages at the facility. It adds new orders to patients’ log entries based on visit-related information from the following packages: Radiology, Laboratory, Pharmacy, Consults, Procedures, Dietetics, and Order Entry. It also updates orders’ statuses and removes orders from patients’ log entries.

- EDPFMOVE is part of the conversion routine. It moves local emergency-department visits to EDIS and provides conversion-related messages—“Visit conversion has completed,” for example. This routine also provides users with several conversion-related options—such as the option to convert Syracuse class-three configuration data (in addition to patient data).

- EDPFPER looks up emergency-department staff (providers, residents, and nurses) in VistA’s New Person file (#200). The routine adds people who match its screening criteria to EDIS staffing lists.

- EDPFPTC performs patient-selection checks. For example, this routine checks to see if selected patients are already on the **Active Patients** list, have patient records that are marked sensitive (in which case the routine displays a warning), are deceased, or have identifiers that are similar to the identifiers of one or more patients who are already on the **Active Patients** list. (Patients on the **Active Patients** list are ipso facto on the display board.) This routine also gets patient record flags (PRFs) for display within EDIS and makes security-log entries when users access records marked sensitive.

- EDPFPTL accepts as its input patient names and social security numbers (including last four social security numbers and last-name initials concatenated with last four social security numbers) and returns from the local VistA system a list of possible matches.

- EDPGLOB – This routine is used to return a global array. If the amount of data is too large, store errors can occur in VistA. Using the EDPGLOB RPC fixes these errors and utilizes global arrays to store and send back the data.

- **[Updated with EDP*2.0*2]** EDPLEX provides API wrappers for calls to the Lexicon. Used by other EDIS routines.

- EDPLOG updates the EDIS log in response to timestamp changes. It also processes diagnoses and checks for the presence of data in required fields before letting users remove patients from the system.

- EDPLOG1 validates record entries and returns error messages for invalid entries.

- EDPLOGA adds log records for new patients. It sets up patient fields, adds default values to stub entries, creates current log records, and creates initial log-history entries. This routine also deletes the initial history-log stub entry.

- EDPLOGH adds new log-history entries and saves new entries for changed fields. This routine also checks timestamps in the ED Log History file (#230.1) for possible data-entry collisions and displays a warning message—“Since you loaded this entry, changes have been made by someone else”—when collisions are imminent. Similarly, when users update data and select a different view before saving their updates, this routine warns them that they will lose their changes if they exit the view without first saving their changes. Finally, this routine notifies users when their bed choices are no longer available.

- **[Updated with EDP*2.0*2]** EDPLPCE creates a visit in the CPRS Patient Care Encounters (PCE) package when users select a provider, resident, nurse, or diagnosis in EDIS. It updates diagnoses for emergency-department visits in EDIS if users enter the diagnoses in CPRS, and in CPRS if users enter the diagnoses in EDIS. This routine also coordinates primary providers between CPRS and EDIS.

- EDPMAIL parses and processes incoming VA MailMan messages from SEND^EDPFMON, which monitors order-related events such as new orders, order changes, deleted orders, and so forth. EDPMAIL also parses and processes patient check-in events.

- EDPQAR logs area information. It returns site-configurable parameters and default areas, and adds default areas in cases where no default areas are assigned.

- EDPQDB displays active log entries on the EDIS display board. It gets display-board data—a list of all beds in sequence for a given area, patient data, and so forth—computes order statuses, and formats data for display.

- EDPQDBS gets display-board specifications for room, area, and staff color configurations.

- **[Updated with EDP*2.0*2]** EDPQLE retrieves log entries by request and returns XML-formatted log entries for patient demographics, diagnoses (ICD-10-CM coded), fields required for closing entries (delay reasons, physician assignments, and so forth), and time stamps.

- EDPQLE1 retrieves supporting information—such as staff and other selection items—and adds the information to XML pick lists. It also builds nodes for code sets.

- EDPQLP returns lists for the log-entry edit context. It also builds duplicate-name and last- four-Social-Security-number lists for counters.

- **[Updated with EDP*2.0*2]** EDPQPCE retrieves PCE information such as diagnoses (including primary and free-text diagnoses) for emergency-department visits.

- EDPQPPS – routine to handle display board specifications.

- EDPRPT gets data for reports by site and date range. This routine turns on switches that determine the beginning and ending points of the report date range and the report type. It also returns timestamp-related data—such as the times acuities were first assigned, the times patients left the waiting area, the times admitting decisions were entered, and so forth.

- **[Updated with EDP*2.0*2]** EDPRPT1 gets data for the Activity report based on site and date range. It gets report headers (CSV), calculates times and averages for column values, initializes counters and sums, returns external values for codes, and includes a list of assigned providers.

- **[Updated with EDP*2.0*2]** EDPRPT10 gets data for the Admissions report based on site and date range. This routine initializes counters and sums, gets report headers (CSV), calculates times and averages, initializes counters and sums, and returns external values for codes.

- EDPRPT11 gets data for the Patient Intake report based on site and date range. This routine initializes counters and sums, gets report headers, returns counts and averages, performs rounding computations, returns hours (24-hour—or military—clock format), and returns name-of-day (Monday, Tuesday, and so forth).

- EDPRPT12 gets data for the Orders by Acuity report based on site and date range. It gets report headers and returns an acuity-based count of lab, imaging, medication, consult, and other orders.

- **[Updated with EDP*2.0*2]** EDPRPT2 gets data for the Delay report based on site and date range. It initializes counters and sums, returns counts and averages, and gets column headers. The routine also returns disposition indicators for VA admissions and external values for codes.

- EDPRPT3 gets data for the Missed Opportunities report based on site and date range. It initializes counters and returns a **1** (one) or **0** (zero) to indicate missed opportunities. The routine also gets column headers, initializes counters, calculates times, and returns totals as CSV- or XML-formatted data.

- EDPRPT4 gets data for the Delay Summary report based on site and date range. It initializes counters and sums and returns counts and averages as CSV- or XML-formatted data. This routine also returns external values for acuity and other codes, and codes ( **1** or **0** ) for IEN statuses that indicate observation.

- EDPRPT5 returns data for the Shift report based on site and day. It initializes counters and sums, calculates the number of visits that carried over, and returns the following: column information (headers, counts and averages—as CSV- and XML-formatted data), the names of shifts (one, two, three, and so forth—based on shift times), and external values for acuity codes.

- **[Updated with EDP*2.0*2]** EDPRPT7 gets data for the Exposure report based on site and the infected person’s time in and time out of the emergency department. It returns a list of patients who were in the waiting room and treatment rooms during the infected patient’s stay (adding a row for each room the infected patient used —including laboratory and x-ray). It also returns on-duty staff assignments. EDPRPT7 returns external values for codes.

- **[Updated with EDP*2.0*2]** EDPRPT7C gets data for the Exposure report in CSV format.

- EDPRPT8 gets data for the Acuity report based on site and date range. It initializes counters and sums and returns external values for acuity codes. The routine returns counts and averages for acuity-based entries, all admissions, and VA admissions.

- EDPRPT9 gets data for the Patient Cross Reference (XRef) report based on site and date range. It uses the ED Log file (#230) to provide information about patients’ identities.

- **[Updated with EDP*2.0*2]** EDPRPTBV gets data for the BVAC report based on site and date range. This routine initializes counters and sums, gets column headers, calculates sums and averages, and returns external values for codes.

- **[Updated with EDP*2.0*2]** EDPX provides a group of common utilities that includes the following: ESC (X), escape for XML transmission; UES (X), unescape XML; UESREQ (REQ), unescape HTTP post; VAL (X,R), returns parameter value or null; NVPARSE (LST, IN), parses tab and delimited name-value pairs into an array; XMLS (TAG, DATA, LBL), returns an XML node as &lt;TAG data=“9” label=“XXX” /&gt;; XMLA (TAG, ATT, END), returns an XML node as &lt;TAG att1=“a” att2=“b”… /&gt;; SMLE (SRC), appends lists to XML arrays as elements; XML (X), adds the line of XML that is to be returned; CODE (X), returns internal values for codes; MSG (MSG), writes out error messages.

- EDPYCHK performs a pre-installation environment check.

- EDPYPRE is the pre-initialization routine.

- EDPYPST is the post initialization routine.

EDIS uses the following globals:

^EDP

^EDPB

The ^EDP global holds a list of patients who are currently checked in at the emergency-department (that is, the list of active patients). The ^EDPB global holds a comprehensive list of emergency-department activities.

Table : Global Placement and Protection

| Global   | Type    | Placement                                                                                                               | Journal   | Protection   |
|----------|---------|-------------------------------------------------------------------------------------------------------------------------|-----------|--------------|
| ^EDP     | Dynamic | Place this global in a volume set that can accommodate the following yearly growth rate:  2,000 bytes * visits per year | Yes       | RWP or D     |
| ^EDPB    | Static  | No recommendation (this global should remain small)                                                                     | Yes       | RWP or D     |

### Files

Table : XE Files

|   File # | File Name                       | Root Global   | Global Protection   |
|----------|---------------------------------|---------------|---------------------|
|   230    | ED LOG                          | ^EDPB(230)    | @                   |
|   230.1  | ED LOG HISTORY                  | ^EDP(230.1)   | @                   |
|   231.6  | TRACKING BOARD                  | ^EDPB(231.6)  | @                   |
|   231.7  | TRACKING STAFF                  | ^EDPB(231.7)  | @                   |
|   231.8  | TRACKING ROOM- BED              | ^EDPB(231.8)  | @                   |
|   231.9  | TRACKING AREA                   | ^EDPB(231.9)  | @                   |
|   232.1  | EDP REPORT TEMPLATE             | ^EDPB(232.1)  | @                   |
|   232.11 | EDP REPORT ELEMENTS             | ^EDPB(232.11) | @                   |
|   232.5  | CPE ROLE                        | ^EDPB(232.5)  | @                   |
|   232.6  | EDP WORKSHEET SPECIFICATION     | ^EDPB(232.6)  | @                   |
|   232.71 | EDP WORKSHEET SECTION           | ^EDPB(232.71) | @                   |
|   232.72 | EDP WORKSHEET COMPONENT         | ^EDPB(232.72  | @                   |
|   232.74 | EDP COMPONENT VALIDATORS        | ^EDPB(232.74) | @                   |
|   233.1  | TRACKING CODE                   | ^EDPB(233.1)  | @                   |
|   233.2  | TRACKING CODE SET               | ^EDPB(233.2)  | @                   |
|   233.8  | NHAMCS REASON FOR VISIT         | ^EDPB(233.8)  | @                   |
|   233.81 | NHAMCS REASON FOR VISIT DISPLAY | ^EDPB(233.81) | @                   |
|   233.82 | ED COMPLAINT                    | ^EDPB(233.82) | @                   |
|   234    | CLINICAL EVENTS                 | ^EDP(234)     | @                   |

#### File Descriptions

#### ED Log (#230)

The ED Log file serves as the log of emergency -department visits and as EDIS’s key source of information for display -board data. EDIS refreshes the display board every 30 seconds, and many of the indices in this file assist in making the application’s refresh code as efficient as possible.

The file works together with the ED Log History file (#230.1) to track activities associated with typical emergency -department visits from beginning to end. The log records key clinical events —triage and disposition, for example. It also records where each patient went after his or her emergency - department visit, and who was responsible for the patient.

Table : File Descriptions

|   Field Number | Field Name            | Pointers                                                                           | Cross References and Record Indices                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------|-----------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          0.01  | LOG ENTRY TIME        | The Log Entry field (.01) of the ED Log History file (230.1)  points to this field | 230^B  AC (#787)  ADUP1 (#788)  ADUP2 (#789)  AL (#790)  AN (#791)  AO (#784)  AP (#792)  APA (#806)  AS (#793)  ATI (#794)  ATO (#795)  PDFN (#801)  PN (#796)              | Date-and-time field (required):  Contains the date and time EDIS added this log record to the file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|          0.02  | INSTITUTION           | Pointer to the Institution file (#4)                                               | AC (#787)  ADUP1 (#788)  ADUP2 (#789)  AL (#790)  AN (#791)  AP (#792)  AS (#793)  ATO (#795)  PN (#796)  PDFN (#801)                                                        | Free-text field (required): This field allows EDIS to associate log entries with  the stations that originated  the entries; it allows the same EDIS system to serve multiple institutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|          0.03  | AREA                  | Pointer to the Tracking Area file (#231.9)                                         | AC (#787)  ADUP1 (#788)  ADUP2 (#789)  AL (#790)  AN (#791)  AP (#792)  AS (#793)  PN (#796)  PDFN (#801)                                                                    | Pointer field: Points to the hospital area to which records apply – initially only to the site’s emergency-department locations; will allow users to expand EDIS’s use to other departments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|          0.04  | PATIENT NAME          |                                                                                    |                                                                                                                                                                              | Free-text field: Contains the patient’s name. Allows sites to enter patients’ names in cases of humanitarian intervention or where patients do not yet have entries in VistA.  Assists in checking for duplicate names and similar names on the display.  This field is set to the following value in cases where  ambulances are arriving and the names of the patients are unknown: (ambulance enroute)  When patients are added to VistA during their ED visits, their names in VistA replace clerk-entered names.  When users select patients from VistA, the software gets the patients’ VistA names and places them in this field.  The field uses this format: Surname,Firstname Names must be between 3 to 30 characters in length. |
|          0.05  | PATIENT SSN           |                                                                                    | AS (#793)                                                                                                                                                                    | Free-text field: Contains the patient’s Social Security Number.  Allows sites to enter patients’ Social Security Numbers in cases of humanitarian care or when patients do not yet have entries in VistA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|          0.06  | PATIENT ID            | Pointer to Patient file (#2)                                                       | AP (#792)  APA (#806)  PDFN (#801)                                                                                                                                           | Pointer field:  Points to the patient’s data file number (the DFN is the IEN in the Patient file).  Contains the patients in VistA for whom EDIS is creating its log entries; entries may be absent in cases where ambulances are arriving with unknown patients and where sites are rendering humanitarian aid to non- VA patients.                                                                                                                                                                                                                                                                                                                                                                                                        |
|          0.07  | CLOSED                |                                                                                    | AC (#787)  ADUP1 (#788)  ADUP2 (#789)  AL (#790)  AN (#791)  AP (#792)  AS (#793)  APA (#806)  Triggers CLOSED DATE/TIME (.071)                                              | A setting:  - 1 (Yes) - 0 (No)  EDIS sets this flag to  *1*  when users remove properly disposed patients from the area (emergency department); closed entries no longer appear on the display board.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|          0.071 | CLOSED DATE/TIME      | Date/Time                                                                          | Triggered by the CLOSED field (.07)                                                                                                                                          | Date-and-time field:  Contains the date/time when the log entry was ‘closed’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|          0.072 | CLOSED BY             | Pointer to New Person file (#200)                                                  |                                                                                                                                                                              | Pointer field:  Contains the IEN of the user who closed the log entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|          0.073 | REMOVED IN ERROR      | Set of Codes                                                                       |                                                                                                                                                                              | Set of codes: 1 (Yes)  This field indicates whether or not this patient was ‘removed in error’. 1 will indicate that the patient was removed in error. Null indicates not removed in error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|          0.074 | RESTORED BY           | Pointer to New Person file (#200)                                                  | Triggers RESTORED BY DATE/TIME                                                                                                                                               | Pointer field:  Contains the IEN of the user who restored the patient to the board. This only occurs if a patient has been removed in error and has been restored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|          0.075 | RESTORED BY DATE/TIME | Date/Time                                                                          | ARIE (#886)  Triggered by ‘RESTORED BY’ field (.074)                                                                                                                         | Date/Time:  This holds the date/time when the patient was ‘restored’ to the board.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|          0.08  | TIME IN               |                                                                                    | ATI (#794)                                                                                                                                                                   | Date-and-time field: Contains the time and date when the patient actually arrived at the emergency department. EDIS measures patients’ length of visit from this date and time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|          0.09  | TIME OUT              |                                                                                    | ATO (#795)                                                                                                                                                                   | Date-and-time field: Contains the patient’s discharge time and date.  EDIS prompts users for delay reasons based on the difference between time- in and time-out entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|          0.1   | ARRIVAL MODE          | Pointer to the Tracking Code file (#233.1)                                         |                                                                                                                                                                              | Pointer field: Points to the source of the patient’s visit.  Currently applies only to the sources of emergency-department visits, e.g. nursing homes or clinics.  Values are associated with the <stn>.arrival and edp.arrival code sets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|          0.11  | PATIENT BRIEF ID      |                                                                                    | ADUP2 (#789)                                                                                                                                                                 | Free-text field:  Contains the patient’s display-board identifier; can store identifiers for patients who are arriving by ambulance and for non-VA patients; the identifier should be in the X9999 format.  When VistA patients are selected, the field stores X9999-formatted identifiers that the application constructs from the Patient file (#2); this allows the application to indicate on the display board patients who have identical X9999-formatted identifiers.                                                                                                                                                                                                                                                                |
|          0.12  | VISIT                 | Pointer to the Visit file (#9000010)                                               | 230^AVISIT^MUMPS  (increments and decrements the dependency counter in the Visit file [#9000010])  230^V  (PCE uses this cross reference to help identify dependent entries) | Pointer field: Points to the visit associated with this  emergency-department encounter.  Because emergency departments don’t normally use appointments, EDIS records patient visits in this field; EDIS can then create visits in PCE so subsequent caregivers can associate orders and progress notes with the same visit; EDIS creates this visit when it collects data for any PCE-related field, allowing it to call DATA2PCE; triage nurses usually enter this data.                                                                                                                                                                                                                                                                  |
|          0.13  | CREATION SOURCE       |                                                                                    |                                                                                                                                                                              | A setting to identify the visit-creation source:  - 0 (EDIS) - 1 (Scheduling) - 2 (CPRS)  EDIS generally populates the VISIT field by calling DATA2PCE; users can also create visits by entering emergency-department appointments or writing progress notes for emergency-department locations; this field records the mechanism responsible for creating the entry in the Visit file (#9000010).                                                                                                                                                                                                                                                                                                                                          |
|          0.14  | CLINIC                | Pointer to the Hospital Location file (#44)                                        |                                                                                                                                                                              | Pointer field: Holds a pointer to the specific emergency-department clinic that EDIS will associate with the patient’s visit. When users check in patients through the Scheduling package, EDIS stores a pointer to the clinic they select here until it creates a visit. When the application creates the visit, it uses the location stored in this field.                                                                                                                                                                                                                                                                                                                                                                                |
|          1.1   | COMPLAINT             |                                                                                    |                                                                                                                                                                              | Free-text field: Contains the complaint with which the patient presented; sites can include this complaint on the display board, so it should be brief enough to fit within a display-board column; this field accepts 1–50 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|          1.2   | DISPOSITION           | Pointer to the Tracking Code file (#233.1)                                         |                                                                                                                                                                              | Pointer field: Points to the patient’s end-of-visit disposition; values for this field are associated with the <stn>.disposition and edp.disposition code sets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|          1.3   | DISPOSITION TIME      |                                                                                    |                                                                                                                                                                              | Time-and-date field: Contains the time and date of the patient’s most recent disposition-field update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|          1.4   | DIAGNOSIS TIME        |                                                                                    |                                                                                                                                                                              | Time-and-date field: Contains the date and time of the patient’s last diagnosis-field update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|          1.5   | DELAY REASON          | Pointer to the Tracking Code file (#233.1)                                         |                                                                                                                                                                              | Pointer field: Points to the reason for delay (for patient stays that exceed the maximum length of stay); associated with the <stn>.delay and edp.delay code sets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|          2     | COMPLAINT (LONG)      |                                                                                    |                                                                                                                                                                              | Free-text field: The patient’s long complaint (free text); an optional field that allows staff to enter complaints in a longer form than EDIS allows for its display-board complaint; this field holds from 1 to 220 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|          3.2   | STATUS                | Pointer to the Tracking Code file (#233.1)                                         |                                                                                                                                                                              | Pointer field:  Points to the record of a patient’s statuses during the course of his or her emergency-department visit (awaiting triage, ED patient, and so forth); associated with the &lt;stn&gt;.status and edp.status code sets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|          3.3   | ACUITY                | Pointer to the Tracking Code file (#233.1)                                         |                                                                                                                                                                              | Pointer field:  Points to the patient’s acuity level, which is based on the Emergency Severity Index (ESI) algorithm (acuity levels 1-5); associated with the edp.acuity code set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|          3.4   | LOC                   | Pointer to the Tracking Room-Bed file (#231.8)                                     | AL (#790)                                                                                                                                                                    | Pointer field:  Points to the patient’s current location; locations can be a specific room or bed, or a conceptual area (such as the hallway, parking lot, or radiology department); locations need not be physical locations; this field allows checking for unoccupied beds or areas.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|          3.5   | MD ASSIGNED           | Pointer to the New Person file (#200)                                              |                                                                                                                                                                              | Pointer field:  Points to the patient’s current physician (provider) assignment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|          3.6   | NURSE ASSIGNED        | Pointer to the New Person file (#200)                                              |                                                                                                                                                                              | Pointer field:  Points to the patient’s current nurse assignment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|          3.7   | RESIDENT ASSIGNED     | Pointer to the New Person file (#200)                                              |                                                                                                                                                                              | Pointer field:  Points to the patient’s current resident assignment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|          3.8   | COMMENT               |                                                                                    |                                                                                                                                                                              | Free-text field (optional): Contains comments associated with the patient’s emergency-department stay; users can enter and update this field for patients’ current visits; sites can optionally include comments on the display board; this field accepts 1–80 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|          4     | DISCHARGE DIAGNOSIS   | Multiple (230.4)                                                                   |                                                                                                                                                                              | Contains the patient’s diagnosis or diagnoses for this emergency- department visit; when sites have enabled free-text diagnoses, EDIS stores patients’ diagnoses lists in this field; when sites have enabled coded diagnoses, this field holds patients’ diagnoses until their PCE visits become available, after which EDIS transfers their diagnoses lists to PCE; in this latter case, PCE becomes the real holder of patients’ diagnoses lists; however, the lists remain synchronized with EDIS to cover rare cases in which sites change parameter settings to allow free-text diagnoses; the parameter that controls diagnoses lists is in the Tracking Area file (#231.9).                                                         |
|          8     | ORDERS                | Multiple (230.08)                                                                  |                                                                                                                                                                              | Tracks orders during the course of the patient’s emergency-department visit; an order-entry event monitor populates this multiple and identifies orders that are related to patients’ current emergency-department visits; the event monitor enables EDIS display boards to offer up-to-date order-related information with every display-board refresh; it also allows reports to track the history of orders related to emergency-department visits.                                                                                                                                                                                                                                                                                      |

#### Discharge Diagnosis 230.04

Sites have the option to synchronize patients’ diagnoses with PCE. If diagnoses are synchronized, every time a diagnosis changes in EDIS, the application passes the change to PCE. If sites do not synchronize patients’ diagnoses with PCE, EDIS simply keeps patient-diagnoses lists in this file. Clinical staff can later access the file’s contents and enter patients’ diagnoses into PCE.

Table : Subfile – Discharge Diagnosis Files

|   Field Number | Field Name          | Pointers                                | Cross References and Record Indices   | Description                                                                                                                                                                                                                                                                                                                                                   |
|----------------|---------------------|-----------------------------------------|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | DISCHARGE DIAGNOSIS |                                         | 230.04^B                              | Free-text field (multiply asked):  Contains the free text entries of the patient’s discharge diagnoses for the visit.  If sites set EDIS parameters to require coded diagnoses, the text in this field will match either ICD-9-CM or ICD-10-CM (after ICD-10 activation date) text from Clinical Lexicon entries; some entries map to more than one ICD code. |
|           0.02 | ICD CODE            | Pointer to the ICD Diagnosis file (#80) |                                       | Pointer field: This is the ICD code for the diagnosis.  Clinical Lexicon utilities are used by the application to look up diagnoses.  Some Clinical Lexicon entries map to more than one ICD code.                                                                                                                                                            |
|           0.03 | PRIMARY             |                                         |                                       | A setting:  1. No (secondary) 2. Yes (primary)  This setting indicates which diagnosis is the primary diagnosis.                                                                                                                                                                                                                                              |

#### Orders 230.08

The order-entry event monitor identifies orders that are related to patients’ current emergency-department visits and populates this multiple with these orders. This subfile enables EDIS to quickly update display boards (which EDIS refreshes every few seconds to provide up -to-date order-status information). It also allows EDIS reporting functionality to track the history of orders that are related to patients’ emergency-department visits.

Table : Subfile – XE Orders

|   Field Number | Field Name   | Pointers   | Cross References and Record Indices   | Description                                                                                                                                                                                                                                                       |
|----------------|--------------|------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | ORDER        |            | 230.08^B AO (#784)                    | Free-text field (multiply asked):  Contains order IDs for patients’ emergency- department-related orders (order IEN); EDIS uses this field to locate orders when the event monitor needs to update them                                                           |
|           0.02 | SERVICE      |            | 230.08^AC                             | A setting:  - M (medication) - L (lab) - R (radiology) - C (consult) - A (all others)  Provides a general identification of the service to which orders are related and allows quick checks for orders associated with the patient’s emergency- department visit. |
|           0.03 | STATUS       |            |                                       | A setting:  - N (new) - A (active) - C (complete)  Provides the general status of orders; sites can use order status to highlight orders on the display board, enabling sites to monitor the board for orders that have been outstanding for too long.            |
|           0.04 | STAT         |            |                                       | A setting:  - 1 (STAT) - 0 (not STAT)  A setting of  *1*  indicates stat orders; sites can optionally use colors to highlight stat orders on the display board.                                                                                                   |
|           0.05 | RELEASE TIME |            |                                       | Date-and-time field: Contains the date and time of an order’s release to its service; allows sites to monitor orders for delay.                                                                                                                                   |

#### Record Indices for File #230

Table : Record Indices for File #230

| Record Index   | Indexed Fields                                   | Description                                                                                                                                                                                                                                                                                         |
|----------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC (#787)      | SITE, AREA, IEN  (active entries only)           | EDIS uses this index to list patients with currently active entries on the display board                                                                                                                                                                                                            |
| ADUP1 (#788)   | SITE, AREA, LASTNAME, IEN  (active entries only) | EDIS uses this index to contribute patients’ last names to the ADUP cross reference, which helps identify patients with similar names or similar brief identities (X9999 formatted identifiers)                                                                                                     |
| ADUP2 (#789)   | SITE, AREA,  LAST4, IEN (active entries only)    | EDIS uses this index to contribute patients’ identifiers in X9999 format                                                                                                                                                                                                                            |
| AL (#790)      | SITE, AREA, LOC,  IEN (active entries only)      | EDIS uses this index to check for beds and areas that are currently occupied                                                                                                                                                                                                                        |
| AN (#791)      | SITE, AREA, PTNAME, IEN  (active entries only)   | EDIS uses this index to check patients’ active statuses in cases where patients do not have DFNs (as is the case with humanitarian interventions); the application references this index before adding patients to the display board to determine whether or not patients are already on the board  |
| AP (#792)      | SITE, AREA, DFN,  IEN (active entries only)      | EDIS uses this index to test for duplicate entries when users select patients who have DFNs (that is, VistA patients) for addition to the display board                                                                                                                                             |
| ARIE (#886)    | RESTORED DATE/TIME,IEN                           | EDIS uses this index to search for patients who were removed in error.                                                                                                                                                                                                                              |
| AS (#793)      | SITE, AREA, SSN,  IEN (active entries only)      | EDIS uses this index to see if patients are already on the display board in cases where patients don’t have DFNs and users are identifying these patients by their SSNs                                                                                                                             |
| ATI (#794)     | SITE, TIME IN (for  reports)                     | EDIS uses this index to get a range of visits within a user-specified time range                                                                                                                                                                                                                    |
| ATO (#795)     | SITE, TIME OUT  (for reports)                    | EDIS uses this index to get a range of visits that were closed within a user- specified time span                                                                                                                                                                                                   |
| PDFN (#801)    | SITE, AREA, DFN,  IEN (for all patients)         | This index organizes all entries by patient DFN. When EDIS performs special lookups against the patient file (by SSN, for example), the lookup service returns a DFN; this index allows EDIS to find visits that correspond to these DFNs; the index contains all visit entries (closed and active) |
| PN (#796)      | SITE, AREA, PTNAME, IEN (for  all patients)      | EDIS uses this index of  *all*  patient names—including the names of patients who do not have DFNs—for selecting patients when visits (closed or otherwise) need to be corrected.                                                                                                                   |

#### ED Log History (230.1)

The ED Log History file provides a forward - and reverse-chronological list of updates to each emergency-department log record. The times tamps contained in this file make it possible to generate a variety of reports.

Table : XE ED Log History Files (#230.1)

|   Field Number | Field Name            | Pointers                                       | Cross References and Record Indices      | Description                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------|-----------------------|------------------------------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         0.01   | LOG ENTRY             | Pointer to the ED Log file (#230)              | 230.1^B ADF (#797)                       | Pointer field:  Points to an entry in the ED Log file; file entries record modifications (updates) to entries in the ED Log file                                                                                                                                                                                                                                                                   |
|         0.02   | TIME                  |                                                | ADF (#797)                               | Time-and-date field: Contains the time and date of the log record’s last  modification (if the  patient’s log record was modified)                                                                                                                                                                                                                                                                 |
|         0.03   | ENTERED BY            | Pointer to the New Person file (#200)          |                                          | Pointer field:  Contains the identities of users who have updated log data                                                                                                                                                                                                                                                                                                                         |
|         0.04   | PATIENT NAME          |                                                |                                          | Free-text field:  The updated value of the patient’s name (if updated)                                                                                                                                                                                                                                                                                                                             |
|         0.05   | PATIENT SSN           |                                                |                                          | Free-text field:  Contains the updated value of the patient’s social security number (if updated)  The class-three product recorded Social Security numbers when patients without DFNs came to the emergency room; EDIS is not currently using this field; the field is present for the sake of compatibility with the class-three version  Patients’ DFNs are their IENs in the Patient file (#2) |
|         0.06   | PATIENT ID            | Pointer to the Patient file (#2)               |                                          | Pointer field:  Points to the updated value of the patient’s DFN (if updated)                                                                                                                                                                                                                                                                                                                      |
|         0.07   | COMPLAINT             |                                                |                                          | Free-text field:  Contains the updated value of the patient’s display- board complaint (if updated)                                                                                                                                                                                                                                                                                                |
|         0.0701 | CLOSED                |                                                |                                          | Set of codes:  1 (Yes)  0 (No)                                                                                                                                                                                                                                                                                                                                                                     |
|         0.071  | CLOSED DATE/TIME      |                                                | Triggered by the CLOSED field (.07)      | Date-and-time field:  Contains the date/time when the log entry was ‘closed’.                                                                                                                                                                                                                                                                                                                      |
|         0.072  | CLOSED BY             | Pointer to New Person file (#200)              |                                          | Pointer field:  Contains the IEN of the user who closed the log entry.                                                                                                                                                                                                                                                                                                                             |
|         0.073  | REMOVED IN ERROR      |                                                |                                          | Set of codes: 1 (Yes)  This field indicates whether or not this patient was ‘removed in error’. 1 will indicate that the patient was removed in error. Null indicates not removed in error.                                                                                                                                                                                                        |
|         0.074  | RESTORED BY           | Pointer to New Person file (#200)              | Triggers RESTORED BY DATE/TIME           | Pointer field:  Contains the IEN of the user who restored the patient to the board. This only occurs if a patient has been removed in error and has been restored.                                                                                                                                                                                                                                 |
|         0.075  | RESTORED BY DATE/TIME |                                                | Triggered by ‘RESTORED BY’  field (.074) | Date/Time:  This holds the date/time when the patient was ‘restored’ to the board.                                                                                                                                                                                                                                                                                                                 |
|         0.08   | TIME IN               |                                                |                                          | Time-and-date field: Contains the updated value of the patient’s arrival time  (if updated)                                                                                                                                                                                                                                                                                                        |
|         0.09   | TIME OUT              |                                                |                                          | Time-and-date field: Contains the updated value of the patient’s departure  time (if updated)                                                                                                                                                                                                                                                                                                      |
|         0.1    | ARRIVAL MODE          | Pointer to the Tracking Code file (#233.1)     |                                          | Pointer field:  Points to the updated value of the source of the patient’s visit (a nursing home or hospital ward, for example—if updated)                                                                                                                                                                                                                                                         |
|         0.11   | DISPOSITION           | Pointer to the Tracking Code file (#233.1)     |                                          | Pointer field:  Points to the updated value of the patient’s disposition (if updated)                                                                                                                                                                                                                                                                                                              |
|         0.12   | DELAY                 | Pointer to the Tracking Code file (#233.1)     |                                          | Pointer field:  Points to the updated reason that the patient’s stay exceeded the maximum stay limit (if updated)                                                                                                                                                                                                                                                                                  |
|         0.14   | CLINIC                | Pointer to the Hospital Location file (#44)    |                                          | Pointer field:  Points to the updated value of the clinic location (if updated)                                                                                                                                                                                                                                                                                                                    |
|         2      | COMPLAINT (LONG)      |                                                |                                          | Free-text field:  Contains the updated value of the patient’s long complaint (if updated)                                                                                                                                                                                                                                                                                                          |
|         3.2    | STATUS                | Pointer to the Tracking Code file (#233.1)     |                                          | Pointer field:  Points to the updated value of the patient’s status (if updated)                                                                                                                                                                                                                                                                                                                   |
|         3.3    | ACUITY                | Pointer to the Tracking Code file (#233.1)     |                                          | Pointer field:  Points to the updated value of the patient’s acuity (if updated)                                                                                                                                                                                                                                                                                                                   |
|         3.4    | LOC                   | Pointer to the Tracking Room-Bed file (#231.8) |                                          | Pointer field:  Points to the updated value of the patient’s room, bed, or area assignment (if updated)                                                                                                                                                                                                                                                                                            |
|         3.5    | MD ASSIGNED           | Pointer to the New Person file (#200)          |                                          | Pointer field:  Points to the identity of the patient’s updated emergency-department physician assignment (if updated)                                                                                                                                                                                                                                                                             |
|         3.6    | NURSE ASSIGNED        | Pointer to the New Person file (#200)          |                                          | Pointer field:  Points to the patient’s updated nurse assignment (if updated)                                                                                                                                                                                                                                                                                                                      |
|         3.7    | RESIDENT ASSIGNED     | Pointer to the New Person file (#200)          |                                          | Pointer field:  Points to the patient’s updated resident assignment (if updated)                                                                                                                                                                                                                                                                                                                   |
|         3.8    | COMMENT               |                                                |                                          | Free-text field Contains updated  comments associated with  the patient’s emergency- department visit (if any— comments are optional)                                                                                                                                                                                                                                                              |
|         9.1    | MODIFIED FIELDS       |                                                |                                          | Free text field:  Contains a list of fields that users modified in the corresponding ED LOG record at the time of the update; the list contains field numbers and is semicolon delimited                                                                                                                                                                                                           |

#### Record Indices for File (230.1)

Table : XE File Record Indices (230.1)

| Record Index   | Indexed Fields   | Description                                                                                                          |
|----------------|------------------|----------------------------------------------------------------------------------------------------------------------|
| ADF (#797)     | LOG, TIME, IEN   | This index provides a forward- chronological list of updates to the log record of a single entry in the ED Log file. |

#### Tracking Staff (231.7)

The Tracking Staff file contains staff assignments for particular areas (currently sites’ emergency departments). It allows for concise staff -selection lists and enables sites to associate colors with staff members so that emergency-department personnel can more easily tell which staff members are assigned to which patients.

Table : XE Files – Tracking Staff (#231.7)

|   Field Number | Field Name   | Pointers                                     | Cross Reference      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|--------------|----------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | PERSON       | Pointer to the New Person file (#200)        | 231.7^B AD (#807)    | Pointer field:  Points to the identity of a person who is assigned to work as staff in the emergency department (required)                                                                                                                                                                                                                                                                                                                                     |
|           0.02 | INSTITUTION  | Pointer to the Institution file (#4)         | AC (#800)  AD (#807) | Pointer field:  Points to entries in the Institution file (#4); allows each station to have its own set of staff assignments                                                                                                                                                                                                                                                                                                                                   |
|           0.03 | AREA         | Pointer to the Tracking Area file (#231.9)   | AC (#800)  AD (#807) | Pointer field:  Points to the area to which the person is  assigned as staff  EDIS currently supports only emergency departments but is capable of supporting other areas in the future                                                                                                                                                                                                                                                                        |
|           0.04 | INACTIVE     |                                              | AD (#800)            | A setting: 0 (active)  1 (inactive)  A setting of  *1*  indicates that the person is no longer an active staff member in the associated area                                                                                                                                                                                                                                                                                                                   |
|           0.05 | LOCAL ID     |                                              |                      | Free-text                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|           0.06 | ROLE         | Pointer to the TRACKING  STAFF file (#232.5) | AC(#873)             | Pointer field:  Points to the role in the CPE ROLE file.                                                                                                                                                                                                                                                                                                                                                                                                       |
|           0.07 | INITIALS     |                                              |                      | Free-text:  This is the user’s initials.                                                                                                                                                                                                                                                                                                                                                                                                                       |
|           0.08 | COLOR        |                                              |                      | Free-text field:  Contains red-green-blue (RGB) values for the  foreground and  background colors (if any) that sites have used to highlight the staff member’s identifier on the display board  Colors are hexadecimal; this field accepts values having the following format: &lt;use color&gt;,&lt;foreground color&gt;,&lt;background color&gt; (for example, the following entry specifies a red foreground and a white background: 1, 0xff0000,0xffffff) |

#### Record Indices for File (231.7)

Table : XE Files Record Indices (231.7)

| Record Index   | Indexed Fields        | Description                                                                                                                                                                                                                                                                             |
|----------------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC (#871)      | SITE, AREA, ROLE, IEN | This cross reference supports constructing a list of currently active staff for a particular role.                                                                                                                                                                                      |
| AD (#872)      | SITE, AREA, DUZ, IEN  | This cross reference allows searching the file for an entry matching a particular DUZ (say, to look up a color map). Since a person may work as staff in multiple areas, this cross reference allows finding the staff record that applies to the person's activity in a specific area. |

#### Tracking Room-Bed (#231.8)

As patients progress through their visits, they may stop at a number of areas. The Tracking Room-Bed file allows sites to set up these areas in EDIS so that they can track patients throughout their visits. Areas can be physical or conceptual, and may include specific beds, waiting areas, and other areas of the hospital (radiology, exam rooms, and so forth).

Table : XE Files – Tracking Room Bed (#231.8)

|   Field Number | Field Name      | Pointers                                   | Cross References and Record Indices   | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------|-----------------|--------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | NAME            |                                            | 231.8^B                               | Free-text field (required): The internal name of the room, bed, or area that the patient is occupying at this stage of his visit                                                                                                                                                                                                                                                                                                        |
|           0.02 | INSTITUTION     | Pointer to Institution file (#4)           | AC (#802)  C (#803)                   | Pointer field:  Allows each station (division, for example) to manage its own set of rooms, beds, and areas                                                                                                                                                                                                                                                                                                                             |
|           0.03 | AREA            | Pointer to the Tracking Area file (#231.9) |                                       | Pointer field:  Points to the hospital area associated with this room, bed, or area; EDIS currently supports only the emergency department, but will probably support additional areas in the future  Trainers can use this field to set up separate areas for each trainee, allowing each trainee to configure his or her own set of rooms and beds                                                                                    |
|           0.04 | INACTIVE        |                                            |                                       | A setting:  - 0 (active) - 1 (inactive)  A setting of  *1*  makes the associated room or area unavailable for selection in EDIS; however, inactive rooms and areas still appear on reports and in views for previous entries                                                                                                                                                                                                            |
|           0.05 | SEQUENCE        |                                            |                                       | A number:  Represents the sequential order in which EDIS should display the associated room or area on the big-board display; the field accepts numbers from one (1) to 9999                                                                                                                                                                                                                                                            |
|           0.06 | DISPLAY NAME    |                                            | AC (#802)                             | Free-text field:  Contains the name of the room or area as it should appear on the big-board display; display names should be concise to save display-board space; supports names from 1–30 characters in length                                                                                                                                                                                                                        |
|           0.07 | DISPLAY WHEN    |                                            |                                       | A setting:  - 0 (occupied) - 1 (always) - (never)  A setting of 0, 1, or 2 determines whether EDIS should display the associated room or area when occupied, always, or never, respectively                                                                                                                                                                                                                                             |
|           0.08 | DEFAULT STATUS  | Pointer to the Tracking Code file (#233.1) |                                       | Pointer field:  Points to the default status (if any) of the room, bed, or area; when sites select a default status for a room, bed, or area, EDIS automatically assigns this default status to patients who are occupying the room, bed, or area                                                                                                                                                                                       |
|           0.09 | MULTIPLE ASSIGN |                                            |                                       | A setting:  - 0 (single—accepts one patient assignment at a time) - 1 (multiple—accepts multiple simultaneous patient assignments) - 2 (waiting—a special case of the multiple-assignments designation for reporting) - 3 (single, non-ED—single- assignment designation in an area outside the emergency department) - 4 (multiple, non-ED— multiple-assignment designation in an area outside the emergency department)               |
|           0.1  | SHARED NAME     |                                            |                                       | Free-text field:  Contains a common name for several beds or areas that share the same physical space; using a shared name in such cases allows sites to run reports that identify patients and staff who are at risk for exposure to contagious organisms                                                                                                                                                                              |
|           0.11 | BOARD           |                                            |                                       | Free-text field:  Contains the name of the particular display board on which the room or area is to appear                                                                                                                                                                                                                                                                                                                              |
|           0.12 | COLOR           |                                            |                                       | Free-text field:  Contains values for colors; allows sites to map specific rooms and areas to particular foreground and background colors for use with the display-board’s room-bed-area list; this field accepts values that have the following format: &lt;use color&gt;,&lt;foreground color&gt;,&lt;background color&gt; (for example, the following entry specifies a red foreground and a white background: 1, 0xff0000,0xffffff) |
|           0.13 | PRIMARY         |                                            |                                       | Set of codes:  - ‘1’ – Primary - ‘2’ – Secondary                                                                                                                                                                                                                                                                                                                                                                                        |

#### Record Indices for (#231.8)

Table : XE Files – Record Indices (#231.8)

| Record Index   | Indexed Fields               | Description                                                                                                                  |
|----------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| AC (#873)      | SITE, AREA, DISPLAYNAME, IEN | Allows looking for a room with a specific abbreviation, such as AMBU or WAIT (when setting baseline parameters for example). |
| C (#874)       | INSTITUTION, AREA            | Allows collecting all of the rooms for a specific area within a division (station number).                                   |

#### Tracking Area (#231.9)

This file contains parameters that control EDIS’s tracking behavior. It also contains XML descriptions that client software uses to control display -board column appearance, row content, and cell color. The AREA field (#.03) of the ED Log files (#230) points to this file.

Table : XE Files – Tracking Area (#231.9)

|   Field Number | Field Name           | Pointers                                   | Cross References and Record Indices   | Description                                                                                                                                                                                                                                                                                                                                      |
|----------------|----------------------|--------------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | NAME                 |                                            | 231.9^B                               | Free-text field  Contains the name of an area within the hospital; EDIS currently supports only sites’ emergency department areas                                                                                                                                                                                                                |
|           0.02 | INSTITUTION          | Pointer to Institution file (#4)           | 231.9^C                               | A pointer field:  Allows each station within a given VistA system to have its own set of areas                                                                                                                                                                                                                                                   |
|           0.03 | LAST UPDATE          |                                            |                                       | Date-and-time field: Contains the date and time that the site last updated the display-board configuration; this helps client software determine if it is necessary to reload configuration parameters                                                                                                                                           |
|           1.1  | DIAGNOSIS REQUIRED   |                                            |                                       | A setting:  - 0 (no) - 1 (yes)  A setting of  *1*  indicates that users must enter diagnoses before removing patients from the display board                                                                                                                                                                                                     |
|           1.11 | AMBULANCE            | Pointer to Tracking Room-Bed file (#231.8) |                                       | Pointer field:  Points to the entry in the Tracking Room-Bed file that represents an arriving ambulance                                                                                                                                                                                                                                          |
|           1.12 | INITIAL ROOM         | Pointer to Tracking Room-Bed file (231.8)  |                                       | Pointer field:  Points to the tracking-file entry that specifies the default room or area (often the waiting room) to which patients are first assigned                                                                                                                                                                                          |
|           1.2  | CODED DIAGNOSIS      |                                            |                                       | A setting:  - 0 (no—free-text) - 1 (yes—ICD-9-CM, or ICD-10-CM after ICD-10 activation date)  A setting of  *1*  indicates that users must enter diagnoses using ICD-9-CM or ICD-10-CM (after ICD-10 activation date) codes before removing patients from the board; otherwise, users may enter free-text diagnoses.                             |
|           1.3  | DISPOSITION REQUIRED |                                            |                                       | A setting:  - 0 (no) - 1 (yes)  A setting of  *1*  indicates that users must enter patients’ dispositions before removing them from the display board                                                                                                                                                                                            |
|           1.4  | DELAY REQUIRED       |                                            |                                       | A setting:  - 0 (no) - 1 (yes)  For patients whose emergency-department stays have exceeded the number of minutes identified in the DELAY MINUTES field  (#1.5), unless patients are admitted to an observation ward, a setting of  *1*  indicates that users must select a reason for delay before removing the patients from the display board |
|           1.5  | DELAY MINUTES        |                                            |                                       | Number field:  Contains the number of minutes after which EDIS requires a reason for delay as a precondition for removing patients from the display board; accepts whole numbers between 1 and 1440                                                                                                                                              |
|           1.6  | FIRST SHIFT START    |                                            |                                       | Number field:  Contains the number of minutes from midnight to the first shift’s starting time; accepts whole numbers between 0 and 1440; EDIS currently assumes that all shifts are of equal length                                                                                                                                             |
|           1.7  | SHIFT DURATION       |                                            |                                       | Number field:  Contains the number of minutes that comprise the duration of a shift; accepts whole numbers between 0 and 1440; for eight-hour shifts, the value recorded in this field will be 480 (8*60)                                                                                                                                        |
|           1.8  | PROMPT RESIDENTS     |                                            |                                       | A setting:  - 0 (no) - 1 (yes)  A setting of  *1*  indicates that the application must prompt users to enter resident assignments (in addition to provider assignments)                                                                                                                                                                          |
|           1.9  | PROMPT CLINICS       |                                            |                                       | A setting:  - 0 (no) - 1 (yes)  A setting of  *1*  (yes) indicates that the application must prompt users to select a clinic; this allows EDIS to create visits based on explicitly selected clinics                                                                                                                                             |
|           3    | COLOR SPEC           |                                            |                                       | Word-processing field (#231.93) (no wrap): Contains an XML document that maps colors to display-board values                                                                                                                                                                                                                                     |
|           4    | DISPLAY BOARD CONFIG | Multiple  #231.94                          |                                       | Contains an XML description of each display board’s definition                                                                                                                                                                                                                                                                                   |
|         230.1  | TRACKING UPDATED     |                                            |                                       | Free-text field:  This timestamp is set whenever the data that is shown on any display board for an area has been updated.                                                                                                                                                                                                                       |
|         231.1  | CHOICES UPDATED      |                                            |                                       | Free-text field:  This is a timestamp that is set whenever the definition of any display board for a given area has been modified.                                                                                                                                                                                                               |

#### Display Board Configuration Subfile (231.94)

Table : XE Files Display Board Configuration Subfile

|   Field Number | Field Name   | Pointers   | Cross Reference   | Description                                                                                          |
|----------------|--------------|------------|-------------------|------------------------------------------------------------------------------------------------------|
|           0.01 | NAME         |            | 231.94^B          | Free-text field:  Contains the name of a specific display board                                      |
|           1    | SPEC         |            |                   | Word-processing field #231.941 (no wrap):  Contains the XML description for a specific display board |

#### Tracking Code (233.1)

The Tracking Code file contains entries that EDIS tracking functionality uses in selection lists. The software may eventually roll up selection-list entries to the emergency-department director for reporting.

The following files point to the Tracking Code file:

Table : Files and Fields that Point to Tracking Code File

| File Name                       | Field                                            |
|---------------------------------|--------------------------------------------------|
| ED Log file (#230)              | ARRIVAL MODE field (#.1)                         |
| ED Log file                     | DELAY REASON field (#1.2)                        |
| ED Log file                     | STATUS field (#3.2)                              |
| ED Log file                     | ACUITY field (#3.3)                              |
| ED Log History file (#230.1)    | ARRIVAL MODE field (#.1)                         |
| ED Log History file             | DISPOSITION field (#.11)                         |
| ED Log History file             | DELAY field (#.12)                               |
| ED Log History file             | STATUS field (#3.2)                              |
| ED Log History file             | ACUITY field (#3.3)                              |
| Tracking Room-Bed file (#233.1) | DEFAULT STATUS field (#.08)                      |
| Tracking Code file (#233.1)     | NATIONAL CODE field (#.04)                       |
| Tracking Code Set (#233.2)      | CODE field (#.02) of the CODES subfield (233.21) |

Table : Tracking Code (#233.1)

|   Field Number | Field Name    | Pointers                               | Cross References     | Description                                                                                                                                                                                                                                                                                |
|----------------|---------------|----------------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | NAME          |                                        | 233.1^B              | Free-text field: Contains unique names for values in the selection lists that EDIS is using.  To distinguish local list selections from national list selections, EDIS prefixes locally defined entries with sites’ station numbers and nationally defined entries with the letters  *edp* |
|           0.02 | DISPLAY NAME  |                                        | AB (#804)  AC (#805) | Free text field: Contains the selection’s display-board name                                                                                                                                                                                                                               |
|           0.03 | ABBREVIATION  |                                        | AB (#804)            | Free-text field: Contains display-name abbreviations that EDIS uses in some reports                                                                                                                                                                                                        |
|           0.04 | NATIONAL CODE | Pointer to Tracking Code file (#233.1) |                      | Free-text field: Will contain mappings from site-defined codes to national codes when national codes exist.                                                                                                                                                                                |
|           0.05 | FLAGS         |                                        |                      | EDIS uses flags to further classify specific codes; possible flags are:  - M (Missed opportunity) - A (Admission) - VA (VA admission) - O (Observation)  EDIS allows multiple flags with no delimiters.                                                                                    |
|           2    | DESCRIPTION   |                                        |                      | Word processing field (#233.12):  Contains a further explanation: allows sites to further explain codes (233.12)                                                                                                                                                                           |

#### Tracking Code File Indices (#233.1)

Table : Tracking Code File Indices (#233.1)

| Record Index   | Indexed Fields                      | Description                                                                                                                                                                                           |
|----------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AB (#875)      | NAME (without prefix), ABBREVIATION | This allows finding all the abbreviations for a name without regard to the site prefix. (The prefix is "edp." when nationally exported, "nnn." for locally defined, where nnn is the station number.) |
| AC (#876)      | NAME (without prefix), DISPLAY NAME | This allows finding all the display names for a name without regard to the site prefix. (The prefix is "edp." when nationally exported, "nnn." for locally defined, where nnn is the station number.) |

#### Tracking Code Set (#233.2)

The Tracking Code Set file contains collections of codes that represent specific selection lists (acuities, patient statuses, dispositions, delay reasons, and so forth) used within EDIS.

Table : Tracking Code Set (#233.2)

|   Field Number | Field Name   | Pointers           | Cross References   | Description                                                                                                                                                    |
|----------------|--------------|--------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | NAME         |                    | 233.2^B            | Free-text field (required): Contains the names of tracking code sets that  EDIS uses in selection  lists; sites may modify selection lists to meet their needs |
|           1    | CODES        | Multiple (#233.21) |                    | Contains lists of codes that are available in selection lists                                                                                                  |

#### Codes (233.21)

Table : Subfile – Tracking Code Set File – Codes (#233.21)

|   Field Number | Field Name           | Pointers                                   | Cross References   | Description                                                                                                                                                                                        |
|----------------|----------------------|--------------------------------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | SEQUENCE             |                                            | 233.21^B           | Number field (multiply asked):  Contains a number that indicates the order in which the associated code should appear in the selection list; accepts whole numbers between 1 and 9999              |
|           0.02 | CODE                 | Pointer to the Tracking Code file (#233.1) | 233.2^AS^MUMPS     | Pointer field:  Points to codes that are to be included in selection lists                                                                                                                         |
|           0.03 | INACTIVE             |                                            |                    | A setting: 1 (inactive)  0 (active)  A setting of  *1*  indicates codes that are temporarily inactivated                                                                                           |
|           0.04 | NAME AT SITE         |                                            | 233.2^AS^MUMPS     | Free-text field: Contains site-specific names; allows sites to  use different names for  display purposes without changing underlying national codes                                               |
|           0.05 | ABBREVIATION AT SITE |                                            | 233.2^AS^MUMPS     | Free-text field: Contains site-specific abbreviations: allows  sites to use different  abbreviations for national-code abbreviations without changing the underlying meaning of the national codes |

#### CPE Role (#232.5)

The CPE Role file contains the definitions for roles to be used with EDIS.

Table : CPE Role (#232.5)

|   Field Number | Field Name        | Pointers                                              | Cross References   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------|-------------------|-------------------------------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | ROLE              | USR CLASS (#8930)                                     | 232.5^B            | Pointer to the USR CLASS file This field contains the role used for the clinical practice environment.  Clerk, Nurse, Provider &amp; Resident                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|           0.02 | ABBREVIATION      |                                                       | 232.5^C            | Free text (Required)  This index holds the abbreviation as well as the IEN for each role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|           0.03 | XML ABBREVIATION  |                                                       |                    | Free text (Required) This is the xml abbreviation for the role.  Previously, logic had been hardcoded to check the role type.  'P' = "@md" 'N' =  "@rn" 'R' = "@res"  These values will remain the same.  However, they are now part of the file and can be more easily enhanced to add roles in the future.  The roles will now be able to be built without having to release a KIDS build to do so.  All role settings are now table-driven.  This is accessed and used to build information out of the CLRSTAFF tag in EDPQDBS.  Any time a new role is added, the UI will need to change to be able to consume the new role type. In addition to this field, the XML ROLE NAME will need to be entered in order to pass the needed information back to the client application.  There is flexibility in the use of these two fields.  However, they MUST be defined when creating a new role.  For example:  Currently, for the role of 'Provider', the XML ABBREVIATION field is "@md", and the XML ROLE NAME is 'providers'.  As long as these fields are unique to this role, the API's will build meaningful information for the client to consume. |
|           0.04 | DEFAULT WORKSHEET | Pointer to EDP WORKSHEET SPECIFICATION  file (#232.6) |                    | Point to the EDP WORKSHEET SPECIFICATIO  N file  This is the default worksheet for this role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|           0.05 | DEFAULT BOARD     |                                                       |                    | Free Text:  This contains the name of the default board for this role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|           0.06 | ALLOW ACUITY EDIT |                                                       |                    | Set of codes: ‘0’ – No  ‘1’ – Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|           0.07 | XML STAFF NAME    |                                                       |                    | Free Text:  This holds the staff name that is related to building the XML needed for the client portion of the application. This is built from the LOAD tag in EDPBST.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

#### EDP Worksheet Specification (#232.6)

The EDP Worksheet Specification file holds worksheet definitions for each institution/area. The EDP Worksheet Specification file also allows worksheets to be associated with user roles.

Table : EDP Worksheet Specification (#232.6)

|   Field Number | Field Name   | Pointers               | Cross References   | Description                                                                                                                                                                          |
|----------------|--------------|------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | NAME         |                        | 233.6^B            | Free-text field (required):  Contains the names of worksheets to be used with EDIS.                                                                                                  |
|           0.02 | INSTITUTION  | INSTITUTION (#4)       | 232.6^C            | Pointer to the INSTITUTION file:  Contains the institution associated with this worksheet.                                                                                           |
|           0.03 | AREA         | TRACKING AREA (#231.9) |                    | Pointer to the TRACKING AREA  file:  The tracking area associated with this worksheet.                                                                                               |
|           0.04 | TYPE         |                        |                    | Set of codes:  - ‘V’ for Visit - ‘A’ for Assess - ‘P’ for Plan - ‘E’ for Edit Closed  This is the type of this worksheet.                                                            |
|           0.05 | ROLE         | USR CLASS (#8930)      |                    | Pointer to the USR CLASS file Identifies the role  associated with this  worksheet.                                                                                                  |
|           0.06 | DISABLED     |                        |                    | Set of codes:  - 0 – False - 1 – True  This indicates whether this worksheet is disabled or not.                                                                                     |
|           0.07 | EDITABLE     |                        |                    | Set of codes:  - ‘1’ – True - ‘0’ – False                                                                                                                                            |
|           1    | SPEC         |                        |                    | Word Processing (NOWRAP)                                                                                                                                                             |
|           2    | SECTIONS     | Multiple  #232.62      |                    | This multiple holds ‘instances’ of the sections from the EDP WORKSHEET SECTION file. Each instance is tied to the worksheet so that its behavior can change on a case by case basis. |

#### Subfile: Sections (#232.62)

Table : Subfile – Sections (#232.62)

|   Field Number | Field Number     | Field Name       | Pointers                                        | Cross References   | Description                                                                                                                                                                                                 |
|----------------|------------------|------------------|-------------------------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | SECTION SEQUENCE | SECTION SEQUENCE |                                                 |                    | Number                                                                                                                                                                                                      |
|           0.02 | SECTION          | SECTION          | Pointer to EDP Worksheet Section file (#232.71) |                    |                                                                                                                                                                                                             |
|           0.03 | INITIALLY OPEN   | INITIALLY OPEN   |                                                 |                    | Set of codes:  - ‘0’ – False - ‘1’ - True                                                                                                                                                                   |
|           1    | CONFIGURATION    | CONFIGURATION    |                                                 |                    | Word Processing (NOWRAP)                                                                                                                                                                                    |
|           2    | COMPONENTS       | COMPONENTS       | Multiple to  #232.622                           |                    | The component multiple points to the EDP WORKSHEET  COMPONENTS file as an 'instance' of the component. This holds specific behavioral flags for this component, as it exists within this worksheet/section. |

#### Subfile: Components (#232.622)

Table : Subfile – Components (#232.622)

|   Field Number | Field Name         | Pointers                                          | Cross References   | Description                               |
|----------------|--------------------|---------------------------------------------------|--------------------|-------------------------------------------|
|           0.01 | COMPONENT SEQUENCE |                                                   | 232.66^B           | Number                                    |
|           0.02 | COMPONENT          | Pointer to EDP Worksheet Component file (#232.72) |                    |                                           |
|           0.03 | EDITABLE           |                                                   |                    | Set of codes:  - ‘1’ – True - ‘0’ - False |
|           0.04 | VISIBLE            |                                                   |                    | Set of codes:  - ‘1’ – True - ‘0’ - False |
|           0.05 | INCLUDE IN SUMMARY |                                                   |                    | Set of codes:  - ‘1’ – True - ‘0’ - False |
|           3    | ROLES              | Pointer to Multiple  #232.63                      |                    |                                           |

#### Subfile: Roles (#232.63)

Table : Subfile – Roles (#232.63)

|   Field Number | Field Name   | Pointers                          | Cross References   | Description   |
|----------------|--------------|-----------------------------------|--------------------|---------------|
|           0.01 | Roles        | Pointer to CPE Role File (#232.5) |                    |               |

#### EDP Worksheet Section (#232.71)

The Worksheet Section file holds the definitions for each section of a worksheet.

Table : EDP Worksheet Section (#232.71)

|   Field Number | Field Name           | Pointers                                                               | Cross References   | Description                                                                                                                      |
|----------------|----------------------|------------------------------------------------------------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | NAME                 |                                                                        | 233.71^B           | Free-text field (required):  This field holds the name of the worksheet section.                                                 |
|           0.02 | PACKAGE              |                                                                        | C (#891)           | Free-text field:  Holds the package information                                                                                  |
|           0.03 | SUMMARY PLUGIN       |                                                                        |                    | Free-text field                                                                                                                  |
|           0.04 | DEFAULT DISPLAY NAME |                                                                        |                    | Free-text field                                                                                                                  |
|           0.05 | TASK TYPE            |                                                                        |                    | Set of codes:  - ‘0’ – None - ‘1’ – Checkbox - ‘2’ – Timed  This field contains the ‘type’ associated with this worksheet.       |
|           0.06 | INITIALLY OPEN       |                                                                        |                    | Set of codes:  - 0 – False - 1 – True  This indicates whether or not the worksheet section should be open or closed initially.   |
|           1    | COMPONENTS           | Multiple (232.711)  Pointer to EDP WORKSHEET COMPONENT  file (#232.72) |                    | Pointer to EDP WORKSHEET COMPONENT (#232.72) file:  This field holds the components that will be used in this worksheet section. |
|           2    | ROLES                | Pointer to multiple (#232.712)                                         |                    |                                                                                                                                  |

#### Subfile: Components (#232.711)

Table : Subfile – Components (#232.711)

|   Field Number | Field Name   | Pointers                                          | Cross References   | Description   |
|----------------|--------------|---------------------------------------------------|--------------------|---------------|
|           0.01 | COMPONENT    | Pointer to EDP Worksheet Component file (#232.72) |                    |               |
|           0.02 | ROLES        | Pointer to multiple (#232.712)                    |                    |               |

#### Subfile: Roles (#232.712)

Table : Subfile – Roles (#232.712)

|   Field Number | Field Name   | Pointers                          | Cross References   | Description   |
|----------------|--------------|-----------------------------------|--------------------|---------------|
|           0.01 | ROLES        | Pointer to CPE ROLE FILE (#232.5) |                    |               |

#### EDP Worksheet Component (#232.72)

The Worksheet Component file holds the definition for each worksheet component.

Table : EDP Worksheet Component (#232.72)

|   Field Number | Field Name           | Pointers                                              | Cross References   | Description                                                                    |
|----------------|----------------------|-------------------------------------------------------|--------------------|--------------------------------------------------------------------------------|
|           0.01 | NAME                 |                                                       | 232.72^B           | Free-text field (required):  Indicates the name of the worksheet component.    |
|           0.02 | LABEL                |                                                       | C (#892)           | Free-text field (required):  This holds the label for the worksheet component. |
|           0.03 | DATA PROVIDER        |                                                       |                    | Free-text Computed field: PACKAGE::CLASS                                       |
|           0.04 | TYPE                 |                                                       |                    | Set of codes:  - ‘R’ – Reference - ‘V’ - Visit                                 |
|           0.05 | MONIKER              |                                                       |                    | Free-text field:  Unknown purpose                                              |
|           0.06 | WIDGET NAME          | Pointer to EDP Worksheet Component Type file  #232.73 |                    | Pointer                                                                        |
|           0.07 | PACKAGE LINK         | Pointer to Package file  #9.4                         |                    | Pointer                                                                        |
|           0.08 | VALUE                |                                                       |                    | Free-text field                                                                |
|           0.09 | SUMMARY LABEL        |                                                       |                    | Free-text field                                                                |
|           0.1  | SUMMARY ORDER        |                                                       |                    | NUMBER                                                                         |
|           0.11 | AVAILABLE            |                                                       |                    | Set of codes:  - ‘1’ – True - ‘0’ – False                                      |
|           0.12 | VISIBILITY TRIGGER   |                                                       |                    | Free-text field                                                                |
|           1.1  | ASSOCIATED FILE      |                                                       |                    | Free-text field                                                                |
|           1.2  | ASSOCIATED FIELD     |                                                       |                    | Free-text field                                                                |
|           1.3  | LOAD EVENT           |                                                       |                    | Free-text field                                                                |
|           2.1  | LOAD API             |                                                       |                    | Free-text field                                                                |
|           2.2  | SAVE API             |                                                       |                    | Free-text field                                                                |
|           3    | ALTERNATE LOAD LOGIC |                                                       |                    | Free-text field                                                                |
|           3.1  | PREVIEW TAG          |                                                       |                    | Free-text field                                                                |
|           3.2  | PREVIEW ROUTINE      |                                                       |                    | Free-text field                                                                |
|           4    | ALTERNATE SAVE LOGIC |                                                       |                    | Free-text field                                                                |
|           5    | PARAMETERS           | Multiple (#232.725)                                   |                    | Free-text field                                                                |
|           6    | DEFAULT VALUE        |                                                       |                    | Free-text field                                                                |
|           7    | REQUIRED COMPONENTS  | Multiple to  #232.727                                 |                    |                                                                                |
|           8    | ROLES                | Pointer to  #232.728                                  |                    |                                                                                |
|           9    | VALIDATOR            | Pointer to  #232.729                                  |                    |                                                                                |

#### Subfile: Parameters (#232.725)

Table : Subfile – Parameters (#232.725)

|   Field Number | Field Name     | Pointers   | Cross References   | Description                                                                               |
|----------------|----------------|------------|--------------------|-------------------------------------------------------------------------------------------|
|           0.01 | PARAMETER NAME |            | 232.725^B          | Free-text field:                                                                          |
|           1    | DATA TYPE      |            |                    | Set of codes:  - ‘S’ – String - ‘N’ - Numeric                                             |
|           2    | SAVE/LOAD TYPE |            |                    | Set of codes:  - ‘S’ – For save only - ‘L’ - For load only - ‘B’ – For both load and save |

#### Subfile: Components (#232.727)

Table : Subfile – Components (#232.727)

|   Field Number | Field Name          | Pointers   | Cross References   | Description     |
|----------------|---------------------|------------|--------------------|-----------------|
|           0.01 | REQUIRED COMPONENTS |            | 232.727^B          | Free-text field |

#### Subfile: Roles (#232.728)

Table : Subfile – Roles (#232.728)

|   Field Number | Field Name   | Pointers                          | Cross References   | Description     |
|----------------|--------------|-----------------------------------|--------------------|-----------------|
|           0.01 | ROLES        | Pointer to CPE ROLE FILE (#232.5) | 232.727^B          | Free-text field |

#### Subfile: Validator (#232.729)

Table : Subfile – Validator (#232.729)

|   Field Number | Field Name           | Pointers                                      | Cross References   | Description                                                         |
|----------------|----------------------|-----------------------------------------------|--------------------|---------------------------------------------------------------------|
|           0.01 | VALIDATOR NAME       | Pointer to EDP COMPONENT VALIDATORS (#232.74) | 232.727^B          | Free-text field:                                                    |
|           0.02 | PROPERTY             |                                               |                    | Set of codes: ‘1’ - text  ‘2’ - selectedIndex  ‘3’ - \_SelectedDate |
|           0.03 | MAX LENGTH           |                                               |                    | Number                                                              |
|           0.04 | REUQIRED             |                                               |                    | Set of codes: ‘1’ – true  ‘0’ – false                               |
|           0.05 | MIN VALUE            |                                               |                    | Free-text                                                           |
|           0.06 | LOWER THAN MIN ERROR |                                               |                    | Free-text                                                           |

#### EDP Worksheet Component Type (#232.73)

Table : EDP Worksheet Component Type (#232.73)

|   Field Number | Field Name   | Pointers   | Cross References   | Description                 |
|----------------|--------------|------------|--------------------|-----------------------------|
|           0.01 | NAME         |            | 232.73^B           | Free-text field (Required): |

#### NHAMCS Reason for Visit (#233.8)

The NHAMCS Reason for visit file holds reasons for visits.

Table : NHAMCS Reason for Visit (#233.8)

|   Field Number | Field Name   | Pointers                        | Cross Reference   | Description                                                                                      |
|----------------|--------------|---------------------------------|-------------------|--------------------------------------------------------------------------------------------------|
|           0.01 | NAME         |                                 | 233.8^B           | Free-text field (required):  Contains the name of the reason for visit                           |
|           2    | CODE         |                                 | 233.8^C           | Free-text field (required):  The code value associated with this reason for visit.               |
|           3    | PARENT CODE  | NHAMCS REASON FOR VISIT (233.8) |                   | Pointer to NHAMCS REASON FOR VISIT FILE:  Holds the parent visit code (if this is a child code). |

#### NHAMCS Reason for Visit Display (#233.81)

The NHAMCS Reason for Visit display file contains the display for an entry in the NHAMCS Reason for Visit file.

Table : NHAMCS Reason for Visit Display (#233.81)

|   Field Number | Field Name   | Pointers                        | Cross Reference    | Description                                                                     |
|----------------|--------------|---------------------------------|--------------------|---------------------------------------------------------------------------------|
|           0.01 | NAME         |                                 | 233.81^B  233.81^D | Free-text field (required):  Contains the name of the reason for visit display. |
|           2    | NHAMCS CODE  | NHAMCS REASON FOR VISIT (233.8) | 233.81^C           | Pointer to NHAMCS REASON FOR VISIT file.                                        |

#### ED Complaint (#233.82)

The ED Complaint file holds the ED complaints as well as the associated NHAMCS codes, attributes, and possible values.

Table : ED Complaint (#233.82)

|   Field Number | Field Name         | Pointers                                               | Cross Reference   | Description                                                                         |
|----------------|--------------------|--------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------|
|           0.01 | NAME               |                                                        | 233.82^B          | Free-text field (required):  Contains the name of the reason for this ED complaint. |
|           2    | NHAMCS CODE        | Pointer to NHAMCS REASON FOR  VISIT  DISPLAY (#233.81) | 233.81^C          | Pointer to NHAMCS REASON FOR VISIT  DISPLAY file.                                   |
|          10    | ATTRIBUTE          | Multiple (#233.821)                                    |                   |                                                                                     |
|          20    | ASSOCIATED SYMPTOM | Multiple (233.822)                                     |                   |                                                                                     |

#### Attribute (233.821)

Table : Attribute (#233.821)

|   Field Number | Field Name     | Pointers                                  | Cross Reference   | Description                                                                                                                                |
|----------------|----------------|-------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | NAME           |                                           | 233.821^B         | Free-text field (required):  This is the attribute that will be prompted to the user in the note template when this complaint is selected. |
|           1    | POSSIBLE VALUE | Multiple (#233.8211)                      |                   | Contains a list of possible values for this attribute.                                                                                     |
|           2    | DISPLAY TEXT   |                                           |                   | Free-text field: Contains the display value:                                                                                               |
|           3    | NHAMCS  Code   | NHAMCS REASON FOR VISIT DISPLAY (#233.81) |                   | Pointer to NHAMCS RESASON FOR VISIT DISPLAY:  Contains the NHAMCS reason for visit.                                                        |

#### Possible Value (#233.8211)

Table : Possible Value (#233.8211)

|   Field Number | Field Name   | Pointers                                  | Cross Reference   | Description                                                                                    |
|----------------|--------------|-------------------------------------------|-------------------|------------------------------------------------------------------------------------------------|
|           0.01 | SEQUENCE     |                                           | 233.8211^B        | Number:  Sequence for this value                                                               |
|           2    | DISPLAY TEXT |                                           |                   | Free-text field:  This is the display text for this possible value.                            |
|           3    | NHAMCS CODE  | NHAMCS REASON FOR VISIT DISPLAY (#233.81) |                   | Pointer to NHAMCS REASON FOR VISIT DISPLAY:  This contains the reason for visit display value. |

#### Associated Symptom (#233.822)

Table : Associated Symptom (#233.822)

|   Field Number | Field Name   | Pointers   | Cross Reference   | Description                                                   |
|----------------|--------------|------------|-------------------|---------------------------------------------------------------|
|           0.01 | SEQUENCE     |            | 233.822^B         | Number:  Sequence for this value                              |
|           2    | NAME         |            |                   | Free-text field:  This is the name of the associated symptom. |

#### Clinical Events (#234)

The Clinical events file tracks the date/time of clinical events along with vitals, medication, orderable items, and labs associated with the events.

Table : Clinical Events (#234)

|   Field Number | Field Name   | Pointers                                   | Cross Reference       | Description                                                                                                                                        |
|----------------|--------------|--------------------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
|           0.01 | DATE/TIME    |                                            | 234^B  234^AL  234^AV | Date/time (required):  This is the date/time of the clinical event.                                                                                |
|           1    | TITLE        |                                            |                       | Free-text field:  This is the title of the event, which will be displayed on data graphs                                                           |
|           2    | PATIENT      | PATIENT file (#2)                          | 234^C                 | Pointer to PATIENT file:  This is the patient for this event.                                                                                      |
|           3    | USER         | NEW PERSON  file (#200)                    |                       | Pointer to the NEW PERSON file:  This is the user responsible for creating this event.                                                             |
|           4    | TREATMENT    | ORDERABLE  ITEMS file (#101.43)            |                       | Pointer to the ORDERABLE ITEMS  file:  This is the medication or treatment the patient was receiving at the time of this event.                    |
|           5    | LAB TEST     | Pointer to the LABORATORY  TEST file (#60) |                       | Pointer to the LABORATORY TEST  file:  This is the lab test used to monitor the efficacy of this treatment, and whose result triggered this event. |
|           6    | VITAL SIGN   |                                            |                       | Set of codes:  ‘BP’ – Blood Pressure  *Note* - this DD field appears to be incomplete.. Only BP is listed in the set of codes***                   |
|          10    | DESCRIPTION  |                                            |                       | Free-text field:  The description of this event.                                                                                                   |

#### EDP Report Template (#232.1)

Table : EDP Report Template (#232.1)

|   Field Number | Field Name       | Pointers              | Cross Reference   | Description                               |
|----------------|------------------|-----------------------|-------------------|-------------------------------------------|
|           0.01 | NAME             |                       | 233.822^B         | Free-text (Required)                      |
|           0.02 | INACTIVE         |                       |                   | Set of codes:  - ‘1’ – True - ‘0’ – False |
|           0.03 | EDITABLE         |                       |                   | Set of codes:  - ‘1’ – True - ‘0’ – False |
|           1    | DISPLAY ELEMENTS | Multiple to  #232.12  |                   |                                           |
|           2    | ROLES            | Multiple to (#232.13) |                   |                                           |

#### Subfile: Sequence (#232.12)

Table : Subfile – Sequence (#232.12)

|   Field Number | Field Name   | Pointers                                      | Cross Reference   | Description   |
|----------------|--------------|-----------------------------------------------|-------------------|---------------|
|           0.01 | SEQUENCE     |                                               |                   | Number        |
|           0.02 | ELEMENT      | Pointer to EDP Report Elements file (#232.11) |                   |               |

#### Subfile: Roles (#232.13)

Table : Subfile – Roles (#232.13)

|   Field Number | Field Name   | Pointers                       | Cross Reference   | Description   |
|----------------|--------------|--------------------------------|-------------------|---------------|
|           0.01 | ROLES        | Pointer CPE ROLE FILE (#232.5) |                   |               |

#### EDP Report Elements (#232.11)

Table : EDP Report Elements (#232.11)

|   Field Number | Field Name        | Pointers   | Cross Reference   | Description          |
|----------------|-------------------|------------|-------------------|----------------------|
|           0.01 | NAME              |            | 232.11^B          | Free-text (Required) |
|           0.02 | FILE #            |            |                   | Free-text            |
|           0.03 | FIELD #           |            |                   | Free-text            |
|           0.04 | HISTORY FIELD #   |            |                   | Free-text            |
|           0.05 | HEADER            |            |                   | Free-text            |
|           1    | FORMAT LOGIC      |            |                   | Free-text            |
|           2    | EXECUTABLE LOOKUP |            |                   | Free-text            |
|           3    | DESCRIPTION       |            |                   | Free-text            |

## Exported Remote Procedure Calls

### EDIS Remote Procedure Calls

#### EDPCBRD RPC

This RPC acts as the front controller for the EDIS display board. It accepts requests that the Java middle tier initially passes to the EDIS Web server. The RPC uses these parameters to determine which command to execute. EDPCBRD allows proxy-user access.

Input parameter SESS identifies requesting users and sites, which the application passes in via its Java middle tier.

Input parameter PARAMS is a list of the parameters that the application passes to the Java middle tier via Hypertext Transfer Protocol ( HTTP) post messages.

EDPCBRD RPC formats and returns data as Extensible Markup Language (XML) documents. The XML structure varies based on the nature of the data request.

#### EDPCTRL RPC

This RPC acts as the front controller for the EDIS tracking application. It accepts requests that the Java middle tier initially passes into the EDIS Web server. The RPC uses the PARAMS parameter to determine which command to execute. The PARAMS parameter is a list of the parameters that users pass to the system’s Java middle tier via HTTP post messages. The RPC’s returned data are formatted as XML documents, the structure of which varies based upon the types of data requests.

#### EDPGLOB RPC

This RPC utilized global arrays to store and return data rather than the previous RPC’s which used only local arrays. During testing, errors were encountered due to stack sized getting too large in the local arrays. Creating and using this RPC for the calls that are more data intensive creates a way to avoid these stack &lt;STORE&gt; errors for larger amounts of data. In the future, if the amount of data is in question, this RPC should be used to avoid any potential issues. Currently this RPC is being used for Lab data retrieval, Worksheet.

## Exported Options

### EDIS Options

Table : EDIS Options

| Name                           | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EDP CONVERSION                 | Run Routine             | Allows sites to trigger the conversion of local data in their ^DIZ(1720xx) files to the new EDIS files; the option uses routine EDPFMOVE, which transfers local configuration data first, followed by all currently open visits; EDPFMOVE also queues a task to copy closed visits, thus permitting reporting functionality to run normally.  Uppercase menu text: CONVERT LOCAL ER DATA TO EDIS |
| EDPF BIGBOARD KIOSKS           | Action                  | NOTE: This option is no longer used as of EDIS v.2.1.1/EDP*2.0*6.  Allows facilities to edit the EDPB BIGBOARD KIOSKS parameter; editing parameter values via XPAR utilities is prohibited  Entry Action: D EN^EDPBKS  Uppercase menu text: DISPLAY BOARD KIOSKS                                                                                                                                 |
| EDPF TRACKING MENU ALL         | Menu                    | Provides access to all EDPF TRACKING VIEW options Timestamp: 61055,41714  Uppercase menu text: ALL TRACKING VIEWS                                                                                                                                                                                                                                                                                |
| EDPF TRACKING MENU CLINICIAN   | Menu                    | Provides access to EDPF TRACKING VIEW options typically associated with clinicians (the Update, Disposition, and Display Board views)  Timestamp: 61055,41714  Uppercase menu text: CLINICIAN TRACKING VIEWS                                                                                                                                                                                     |
| EDPF TRACKING MENU SIGNIN      | Menu                    | Provides access to the EDPF TRACKING VIEW options associated with signing in patients to the emergency department (the Sign In and Display Board views)  Timestamp: 61055,41714  Uppercase menu text: SIGN-IN TRACKING VIEWS                                                                                                                                                                     |
| EDPF TRACKING MENU TRIAGE      | Menu                    | Provides access to the EDPF TRACKING VIEW options associated with triaging patients (the Triage and Display Board views)  Timestamp: 61055,41714  Uppercase menu text: TRIAGE TRACKING VIEWS                                                                                                                                                                                                     |
| EDPF TRACKING SYSTEM           | Broker (client- server) | A context option for EDIS remote procedure calls (RPCs) at local facilities; the option uses EDPCTRL RPC and EDPCBRD RPC; assigning any EDPF TRACKING MENU or EDPF TRACKING VIEW  option implicitly provides users with access to this option  Uppercase menu text: EDIS VERSION 1.0-T28                                                                                                         |
| EDPF TRACKING VIEW BOARD       | Menu                    | Provides access specifically to the EDIS Display Board view.  Timestamp: 61514,54336  Uppercase menu text: DISPLAY BOARD                                                                                                                                                                                                                                                                         |
| EDPF TRACKING VIEW CONFIGURE   | Menu                    | Provides access specifically to the EDIS Configure view.  Timestamp: 61514,54336  Uppercase menu text: CONFIGURE TRACKING BOARD                                                                                                                                                                                                                                                                  |
| EDPF TRACKING VIEW DISPOSITION | Menu                    | Provides access specifically to the EDIS Disposition view.  Timestamp: 61514,54336  Uppercase menu text: DISPOSITION PATIENT                                                                                                                                                                                                                                                                     |
| EDPF TRACKING VIEW EDIT CLOSED | Menu                    | Provides access specifically to the EDIS Edit Closed view, which allows users to change any emergency department visit; assign this view to users who are authorized to correct data discrepancies; access should be limited; EDIS logs all changes.  Timestamp: 61514,54336  Uppercase menu text: EDIT CLOSED PATIENT                                                                           |
| EDPF TRACKING VIEW REPORTS     | Menu                    | Provides access specifically to the EDIS Reports view; security keys further restrict access to some reports. Timestamp: 61514,54336  Uppercase menu text: TRACKING REPORTS                                                                                                                                                                                                                      |
| EDPF TRACKING VIEW SIGNIN      | Menu                    | Provides access specifically to the EDIS Sign In view. Timestamp: 61514,54336  Uppercase menu text: SIGN IN PATIENT                                                                                                                                                                                                                                                                              |
| EDPF TRACKING VIEW STAFF       | Menu                    | Provides access specifically to the EDIS Assign Staff view for configuring staff assignments.  Timestamp: 61514,54336  Uppercase menu text: ASSIGN STAFF                                                                                                                                                                                                                                         |
| EDPF TRACKING VIEW TRIAGE      | Menu                    | Provides access specifically to the EDIS Triage view. Timestamp: 61514,54336  Uppercase menu text: TRIAGE PATIENT                                                                                                                                                                                                                                                                                |
| EDPF TRACKING VIEW UPDATE      | Menu                    | Provides access specifically to the EDIS Update view. Timestamp: 61514,54336  Uppercase menu text: UPDATE TRACKING BOARD                                                                                                                                                                                                                                                                         |
| EDPS BOARD CONTEXT             | Broker (client- server) | Uses EDPCBRD RPC to set the tracking board’s context.  Uppercase menu text: ED TRACKING BOARD CONTEXT                                                                                                                                                                                                                                                                                            |
| EDPSERVER                      | Server                  | Uses the EDPMAIL routine to process incoming scheduling events from VA MailMan.  Uppercase menu text: PROCESS INCOMING SCHEDULING EV                                                                                                                                                                                                                                                             |

### Include EDIS Options in Users’ Menu Trees

Include one or more of the following options in each user’s menu tree:

- EDPF TRACKING MENU ALL
- EDPF TRACKING MENU CLINICIAN
- EDPF TRACKING MENU SIGNIN
- EDPF TRACKING MENU TRIAGE
- EDPF TRACKING VIEW BOARD
- EDPF TRACKING VIEW CONFIGURE
- EDPF TRACKING VIEW DISPOSITION
- EDPF TRACKING VIEW EDIT CLOSED
- EDPF TRACKING VIEW REPORTS
- EDPF TRACKING VIEW SIGNIN
- EDPF TRACKING VIEW STAFF
- EDPF TRACKING VIEW TRIAGE
- EDPF TRACKING VIEW UPDATE

**NOTE:** The KIDS installation process does not rebuild VistA menu trees before you assign new EDIS menus. You must therefore perform a menu rebuild after you assign these menus for the first time. If you do not, graphical user interface (GUI) applications like EDIS won’t know who has access to the new options. Again, performing a menu rebuild is necessary only once, and only for menus that have never before been assigned. **You only need to perform a menu rebuild if installing EDIS for the first time; this step is not necessary after installing EDIS v2.1.2/EDP*2.0*2 if you are only updating EDIS.**

#### Assign EDIS Views to Users

Work with your site’s clinical application coordinators (CACs) and emergency- department managers to gather a list of EDIS users and determine which views each user needs. Assign to each user only views that he or she needs.

- 7.1.1.1. Log in to VistA.
- 7.1.1.2. At the Select **OPTION NAME** prompt type *eve* and then press the &lt; **Enter** &gt; key.
- 7.1.1.3. At the **Choose 1-5** prompt, type *1* (for **EVE Systems Manager Menu** ) and press the &lt; **Enter** &gt; key.
- 7.1.1.4. At the Select **Systems Manager Menu Option** prompt, type *User Management* and press the &lt; **Enter** &gt; key.
- 7.1.1.5. At the Select **User Management Option** prompt, type ***Edit*** (for **Edit an Existing User** ) and press the &lt; **Enter** &gt; key.
- 7.1.1.6. At the Select **NEW PERSON NAME** prompt **,** type the user’s name using the following format: lastname,firstname. Press the &lt; **Enter** &gt; key. VistA displays the **Edit an Existing User** dialog.
- 7.1.1.7. In the **Edit Existing User** dialog, press the &lt; **Down Arrow** &gt; key to highlight the Select **SECONDARY MENU OPTIONS** field. (Type a question mark [ *?* ] to see a list of the secondary options that are currently assigned to the user.)
- 7.1.1.8. Type in the secondary menu options field one of the options listed above and then press the &lt; **Enter** &gt; key.
- 7.1.1.9. At the “Are you adding …as a new SECONDARY MENU OPTIONS (the…for this NEW PERSON)? No//” prompt, type ***Yes*** and press the &lt; **Enter** &gt; key.
- 7.1.1.10. Press the &lt; **Enter** &gt; key again to accept this new option.
- 7.1.1.11. In the **SYNONYM** field, type a synonym for the option (optional). Press the &lt; **Enter** &gt; key.
- 7.1.1.12. Press the &lt; **Enter** &gt; key to close the **COMMAND** field and return to the Select

**SECONDARY MENU OPTIONS** field.

- 7.1.1.1. Repeat steps 8 through 11 to assign other options as necessary.
- 7.1.1.2. Press the &lt; **Down Arrow** &gt; key to move through the **Edit Existing User** dialog. At the end of each page, type the letter *n* in the **COMMAND** field to enter the following page.
- 7.1.1.3. Stop on page 3.
- 7.1.1.4. Check the user’s person class, which appears on page 3, to make sure the user’s person class is active.
- 7.1.1.5. If the user’s person class is not active, select an active person class for the user.
- 7.1.1.6. When you have entered all applicable secondary menu options and verified that the user has an active person class, type the word **Exit** in the **COMMAND** field.
- 7.1.1.7. At the **Save changes before leaving form (Y/N)?** prompt, type the letter *Y* and press the &lt; **Enter** &gt; key.

## Security

### KAAJEE

EDIS uses Kernel Authentication and Authorization for J2EE (KAAJEE) to authenticate users. KAAJEE enables Java applications to use VistA security features. Specifically, it authenticates users against your local VistA (M) system and uses VistA options and security keys to authorize access to role -based functionality. KAAJEE also transforms VistA login credentials into J2EE -compatible login credentials. For more information about KAAJEE, visit [http://vista.med.va.gov/kernel/kaajee](http://vista.med.va.gov/kernel/kaajee) .

### Secure Sockets Layer

EDIS uses Secure Sockets Layer (SSL) to secure communications between the EDIS Web server and sites’ display boards. To set up these two-way secure communications for each machine that will power a display board, you must first set up the display board to run in kiosk mode. Kiosk mode locks down the machine’s user interface to protect the application from accidental or de liberate misuse. You must then contact the VA National Helpdesk at 855-673-4357 or create a Remedy ticket. If you call the helpdesk, inform the helpdesk analyst that you are making a display-board setup request. If you create a Remedy ticket, select the **Display Board Setup Request** option.

The helpdesk analyst will add the computer to a group that enables it to automatically receive its SSL certificate for two-way authentication. This group also forces a lockdown on the machine to run in kiosk mode. See the EDIS Server Installation Guide for detailed instructions on setting up large display boards.

#### PKI Encryption Basics

To encrypt communications between the EDIS Web -application server and browsers that sites are using to run their display boards, the server and browsers exchange certificates containing their public keys.

After this exchange takes place, the browser sends a random number that it has encrypted using the server’s public key. The server decrypts this number using its private key. The browser and server then use this random number to generate session keys, which they use in conjunction with their private keys to encrypt and decrypt data exchanges during the communications session.

### Security Keys

#### EDPF KIOSKS

**NOTE: This security key is no longer used as of EDIS v.2.1.1/EDP*2.0*6.**

*This security key grants access to the EDPF BIGBOARD parameter. This parameter maps fully qualified computer names to display board names. Sites must add or change values for this parameter via the EDPF BIGBOARD KIOSKS option.*

#### EDPR EXPORT

This security key enables holders to export EDIS reports to Microsoft Excel.

#### EDPF WORKSHEETS

This security key controls access to the ability to modify worksheet configurations (this MAY be removed before release).

#### EDPR ADHOC

This security key has been added to control access to ad hoc reports.

#### EDPR XREF

This security key enables holders to view and run the EDIS Cross Reference (XRef) report, which matches emergency department visit numbers with associated patient-identity information.

#### Assign Keys for Emergency Department Users

Assign keys to users who need access to additional reporting capabilities.

- 8.1.1.1. Log in to VistA
- 8.1.1.2. At the Select **OPTION NAME** prompt, type *eve* and then press the &lt; **Enter** &gt; key.
- 8.1.1.3. At the **Choose 1-5** prompt, type the number *1* (for **EVE Systems Manager Menu** ) and then press the &lt; **Enter** &gt; key.
- 8.1.1.4. At the Select **Systems Manager Menu Option** prompt, type *menu* (for **Menu Management** ) and then press the &lt; **Enter** &gt; key.
- 8.1.1.5. At the Select **Menu Management Option** prompt, type the word *key* (for **Key Management** ) and then press the &lt; **Enter** &gt; key.
- 8.1.1.6. At the Select Key Management Option prompt, type the word *allocation* (for **Allocation of Security Keys** ).
- 8.1.1.7. At the **Allocate key** prompt, type the name of the security key you want to assign— *EDPF EXPORT* , for example.
- 8.1.1.8. At the **Holder of key** prompt, type the name of the first user to whom you are assigning the key and then press the &lt; **Enter** &gt; key.
- 8.1.1.9. At the **Another holder** prompt, type the name of a second user to whom you are assigning the key and then press the &lt; **Enter** &gt; key. Repeat this step for all users to whom you are assigning the key.
- 8.1.1.10. At the **You are allocating keys. Do you wish to proceed? YES//** prompt, press the &lt; **Enter** &gt; key to accept the default response.

## Protocols

### EDIS Protocols

EDP CHECK-IN monitors local VistA systems for Scheduling -package events that indicate VA personnel are checking patients into the emergency department. This protocol is placed on the SDAM APPOINTMENT EVENTS protocol, which is an appointment-event driver.

EDP MONITOR monitors order events for the EDIS display board. This protocol is placed on the * EVSEND OR protocols to check for updates that ancillary packages send to the Order Entry/Results Reporting package. (The asterisk in the expression ** EVSEND OR* stands as a placeholder for other package namespaces, such as PS or RA.) It monitors when ancillary packages transmit orders and when they complete the orders.

EDP NEW PATIENT defines variables to support some of the devices that previously monitored SDAM APPOINTMENT EVENTS. The application processes this protocol when users or applications add new patients to the board. Items may look for EDPDATA (EDPDATA = ED Log IEN^DFN^Time In^Hospital Location IEN). This protocol also defines the following variables:

- DFN = Patient file (#2) IEN
- SDT = Time In
- SDCL = Hospital Location file (#44) IEN
- SDATA = ^DFN ^ SDT ^ SDCL
- SDAMEVT = 1 (unscheduled new visit)

EDP OR MONITOR monitors ordering events for the EDIS display board. It is placed on the * EVSEND OR protocols to look for order numbers that are assigned to new orders from ancillary packages.

EDPF ADD BOARD provides support for an entry action (D ADD^EDPBKS) that adds a display board.

**NOTE: The EDPF BIGBOARD MENU protocol and the EDPF BIGBOARD KIOSKS list template and parameter are no longer used as of EDIS v.2.1.1/EDP*2.0*6.**

*EDPF BIGBOARD MENU defines the menu of actions for the EDPF BIGBOARD KIOSKS list template. This protocol allows facilities to edit the EDPF B IGBOARD KIOSKS parameter. Menu items include:*

- *EDPF ADD BOARD (sequence 11)*
- *EDPF REMOVE BOARD (sequence 12)*
- *EDPF CHANGE BOARD (sequence 21)*
- *EDPF SELECT DIVISION (sequence 31)*
- *EDPF QUIT (sequence 32)*
- *EDPF BLANK 1 (sequence 22)*
- *EDPF BLANK 2 (sequence 13)*
- *EDPF BLANK 3 (sequence 23)*

EDPF BLANK 1 displays a blank line; EDIS uses this protocol to provide white space on menus. (Item text is three spaces.)

EDPF BLANK 2 displays a blank line; EDIS uses this protocol to provide white space on menus. (Item text is three spaces.)

EDPF BLANK 3 displays a blank line; EDIS uses this protocol to provide white space on menus. (Item text is three spaces.)

EDPF CHANGE BOARD supports entry action D CHG^EDPBKS, which changes a computer name or display board.

EDPF QUIT supports entry action Q, which exits the EDPF BIGBOARD KIOSKS list template. **NOTE: The EDPF BIGBOARD KIOSKS list template is no longer used as of EDIS v.2.1.1/EDP*2.0*6.**

EDPF REMOVE BOARD supports entry action D REM^EDPBKS, which removes a display board.

EDPF SELECT DIVISION supports entry action D NEWDIV^EDPBKS, which allows the EDIS editor to switch to values for another division.

### Other Protocols

FH EVSEND OR sends Health Level 7 (HL7) messages from the Dietetics package to the Order Entry/Results Reporting package.

GMRC EVSEND OR sends consult requests and tracking data to the Order Entry/Results Reporting package.

LR70 CH EVSEND OR sends orders from the Laboratory package to the Order Entry/Results Reporting package.

OR EVSEND FH sends diet-message events.

OR EVSEND GMRC sends consult-message events.

OR EVSEND LRCH sends laboratory-message events.

OR EVSEND ORG sends generic event messages.

OR EVSEND PS sends pharmacy-message events.

OR EVSEND RA sends radiology and imaging events.

PS EVSEND OR sends inpatient and outpatient medication orders from the Pharmacy package to the Order Entry/Results Reporting package.

RA EVSEND OR sends radiology and imaging message events to the Order Entry/Results Reporting package.

SDAM APPOINTMENT EVENTS performs all necessary actions associated with Scheduling-package events (such as patient check in).

## List Templates

### EDIS List Templates

**NOTE: The EDPF BIGBOARD KIOSKS list template is no longer used as of EDIS v.2.1.1/EDP*2.0*6.**

*EDPF BIGBOARD KIOSKS maps fully qualified machine names to the names of EDIS big-board displays.*

## Troubleshooting

### Check-in via Scheduling

If EDIS does not automatically add patients when users create an appointment for them or check them in via the Scheduling package, make sure your site's emergency- department location is set in the EDPF LOCATION parameter. Check this parameter to ensure that its value coincides with the value of your emergency department location in file #44 (Hospital Location). EDIS uses values in the EDPF LOCATION parameter to add patients to its log when you create appointments for, or check in, emergency-department visits.

### Blank View

If users don’t see view selections when they log in to EDIS, you may not have assigned EDIS options for them. Users need at least one assigned option to access EDIS views. If users already have one or more assigned options, you may need to rebuild your site's menu trees in VistA. Rebuilding menus is necessary only after you assign new menu options for the first time.

### PCE Visits

EDIS creates a Patient Care Encounter (PCE) encounter in CPRS when users select a provider or diagnosis in EDIS. If this functionality isn’t working at your site, check:

- The location entry in the EDPF LOCATION parameter
- Physicians’ and nurses’ person-class status
#### Check the EDPF LOCATION Parameter

EDIS uses the entry in this parameter to create PCE encounters in CPRS.

#### Check for Active Person Class

Before EDIS creates PCE encounters based on physician, nurse, or resident assignments, it checks to make sure the physician, nurse, or resident has an active person class. If a user selects a provider whose person class is expired, EDIS does not create an encounter based on the user’s selection. To remedy this problem, check each person's class for each provider on your site’s staff pick lists.

### Nurse Assignments

By default, EDIS bases its nursing-staff list on all entries in the New Person file (#200). Sites can elect to have EDIS filter its nurse -selection list to allow only people who hold the ORELSE security key, only people who hold the PSJ RNURSE security key, or only people who are present and active in the Nurse Staff file (#210).

If you do not see emergency-department nurses when you are using the **Assign Staff** view to create the EDIS **Nurse** pick list, check the status of your site’s emergency- department nursing staff in the Nurse Staff file. Or, if your site has configured EDIS to base its selection list on the ORELSE or PSJ RNURSE security key, check to make sure your site’s emergency-department nurses hold the appropriate keys.

### Intermittent Login Difficulties

If your site is experiencing intermittent login difficulties and it uses a load balancer that passes control to different instances of VistA, be sure that each VistA instance is running a VistALink listener. Every system that handles VistALink connections must be running a VistALink listener.

## Index

230

Files 	20

230.04

Files 	30

Architecture 	3

Blank View                                 Troubleshooting 	78

Check-in via Scheduling

Troubleshooting 	78

Codes

233.21 ..........................................................50

CPRS Synchronization 	9

Discharge Diagnosis

Files 	30

Disk Space

Requirements 	5

Display Board 	3

URLs 	3

Display Board Configuration Subfile

231.94 ..........................................................47

ED Log

Files	20

ED Log History

230.1 ............................................................34

Files	34

EDIS Protocols

APPOINTMENT EVENTS	75

EDP CHECK-IN	75

EDP MONITOR	75

EDP NEW PATIENT	75

EDP OR MONITOR	75

EDPAF ADD BOARD	75

EDPF BIG BOARD MENU	75

EDPF BLANK 1	75

EDPF BLANK 2	75

EDPF BLANK 3	75

EDPF CHANGE BOARD	76

EDPF QUIT	76

EDPF REMOVE BOARD	76

EDPF SELECT DIVISION	76

Protocols	75

EDIS Templates

Templates	77

EDP

Globals	19

EDP CONVERSION

Exported Options	69

EDPB

Globals	19

EDPBDL

Routines 	11

EDPBLK                                                 Routines 	11

EDPBPM                                                 Routines 	11

EDPBRM                                                Routines 	11

EDPBRS

Routines 	11

EDPBSL                                                  Routines 	11

EDPBST                                                  Routines 	11

EDPCBRD

Remote Procedure Calls 	68

Routines 	12

EDPCDBG                                              Routines 	12

EDPCONV                                              Routines 	12

EDPCONV1                                            Routines 	12

EDPCSV                                                 Routines 	12

EDPCTRL

Remote Procedure Calls 	68

Routines 	12

EDPDD

Routines 	12

EDPF

Parameters	8

EDPF BIGBOARD KIOSKS

Exported Options 	69

Parameters	8

EDPF DEBUG START TIME

Parameters	8

EDPF LOCATION

Parameters	8

EDPF NURSE STAFF SCREEN

Parameters	8

EDPF SCHEDULING TRIGGER

Parameters	9

EDPF SCREEN SIZES

Parameters	9

EDPF TRACKING MENU ALL

Exported Options 	69

EDPF TRACKING MENU CLINICIAN Exported Options 	69

EDPF TRACKING MENU SIGNIN

Exported Options	69

EDPF TRACKING MENU TRIAGE

Exported Options	69

EDPF TRACKING SYSTEM

Exported Options	69

EDPF TRACKING VIEW BOARD

Exported Options	70

EDPF TRACKING VIEW CONFIGURE Exported Options	70

EDPF TRACKING VIEW DISPOSITION

Exported Options	70

EDPF TRACKING VIEW EDIT CLOSED Exported Options	70

EDPF TRACKING VIEW REPORTS

Exported Options	70

EDPF TRACKING VIEW SIGNIN

Exported Options	70

EDPF TRACKING VIEW STAFF

Exported Options	70

EDPF TRACKING VIEW TRIAGE

Exported Options	70

EDPF TRACKING VIEW UPDATE

Exported Options	70

EDPFAA

Routines	12

EDPFLEX

Routines	12

EDPFMON

Routines	12

EDPFMOVE

Routines	12

EDPFPER

Routines	12

EDPFPTC

Routines	12

EDPFPTL

Routines	12

EDPLOG

Routines	13

EDPLOG1

Routines	13

EDPLOGA

Routines	13

EDPLOGH

Routines	13

EDPLPCE

Routines	13

EDPMAIL

Routine	13

EDPQAR

Routines 	13

EDPQDB                                                 Routines 	13

EDPQDBS

Routines 	13

EDPQLE                                                 Routines 	13

EDPQLE1                                                Routines 	13

EDPQLP                                                  Routines 	13

EDPQPCE

Routines 	13

EDPR EXPORT

Security Keys 	73

EDPR XREF

Security Keys 	74

EDPRPT                                                  Routines 	13

EDPRPT1                                                Routines 	13

EDPRPT10

Routines 	13

EDPRPT11                                              Routines 	14

EDPRPT12                                              Routines 	14

EDPRPT2 	14

EDPRPT3                                                Routines 	14

EDPRPT4

Routines 	14

EDPRPT5                                                Routines 	14

EDPRPT7

Routines 	14

EDPRPT7C                                             Routines 	14

EDPRPT8

Routines 	14

EDPRPT9                                                Routines 	14

EDPRPTBV                                            Routines 	14

EDPS BOARD CONTEXT

Exported Options 	70

EDPSERVER

Exported Options 	71

EDPX

Routines	14

EDPYCHK

Routines	14

EDPYPRE

Routines	14

EDPYPST

Routines	15

Exported Options	69

Assign Views	71

Files	19

Codes	50

Display Board Configuration Subfile	47

Record Indices

#230...............................................32

Record Indices                                          230.1	38

Record Indices

231.7..................................................39

Record Indices                                          231.8	43

Tracking Area	43

Tracking Code File	47

Tracking Code Set ...........................49, 51, 67

Tracking Room-Bed	40

Tracking Staff (#231.7)	38

Globals	19

KAAJEE                                                   Security	73

Kernel Authentication and Authorization for

Java 2 Enterprise Edition (KAAJEE)	3

Minimum Hardware Requirements

System Performance	4

Namespace and Number Space	7

Nurse Assignments                      Troubleshooting	78

Optimal Viewing Requirements

System Performance	5

Orders

230.08 ....................................................31

Files	31

Parameters	8

EDPF	8

EDPF BIGBOARD KIOSKS	8

EDPF DEBUG START TIME	8

EDPF LOCATION	8

EDPF NURSE STAFF SCREEN	8

EDPF SCHEDULING TRIGGER	9

EDPF SCREEN SIZES	9

PCE Visits

Troubleshooting 	78

Presentation tier	3

Protocols 	75

FH EVSEND OR 	76

GMRC EVSEND OR 	76

LR70 CH EVSEND OR 	76

OR EVSEND FH 	76

OR EVSEND GMRC 	76

OR EVSEND LRCH 	76

OR EVSEND ORG 	76

OR EVSEND PS 	76

OR EVSEND RA 	76

PS EVSEND OR 	76

RA EVSEND OR 	76

SDAM APPOINTMENT EVENTS 	76

Rehabilitation Act of 1973 (Section 508)	1

Remote Procedure Calls 	68

Requirements

Disk Space	5

Minimum Hardware	4

Optimal Viewing	5

Response Times

System	7

Routines 	11

EDPBCF 	11

EDPBCM 	11

EDPBDL 	11

EDPBLK 	11

EDPBPM 	11

EDPBRM 	11

EDPBRS 	11

EDPBSL 	11

EDPBST 	11

EDPCBRD 	12

EDPCDBG 	12

EDPCONV 	12

EDPCONV1 	12

EDPCSV 	12

EDPCTRL 	12

EDPDD 	12

EDPFAA 	12

EDPFLEX 	12

EDPFMON 	12

EDPFMOVE 	12

EDPFPER 	12

EDPFPTC 	12

EDPFPTL 	12

EDPLOG 	13

EDPLOG1 	13

EDPLOGA 	13

EDPLOGH 	13

EDPLPCE 	13

EDPMAIL 	13

EDPQAR 	13

EDPQDB 	13

EDPQDBS 	13

EDPQLE 	13

EDPQLE1 	13

EDPQLP 	13

EDPQPCE 	13

EDPRPT 	13

EDPRPT1 	13

EDPRPT10 	13

EDPRPT11 	14

EDPRPT12 	14

EDPRPT2 	14

EDPRPT3 	14

EDPRPT5 	14

EDPRPT7 	14

EDPRPT7C 	14

EDPRPT8 	14

EDPRPT9 	14

EDPRPTBV 	14

EDPX 	14

EDPYCHK 	14

EDPYPRE 	14

EDPYPST 	15

EPTRPT4	14

Scaling Guide Memory and CPU

System Performance	5

Security	73

KAAJEE	73

PKI Encryption 	73

Secure Sockets Layer (SSL) 	73

Security keys 	73

Security Keys

Assign Keys 	74

Security 	73

System

Response Times	7

Timeouts	9

System Performance	4

Templates 	77

EDPF BIGBOARD KISOKS 	77

Timeouts

System	9

Tracking Code File

233.1........................................................ 47

Record Indices

233.1 ................................................... 49

Tracking Code Set

233.2............................................ 49, 51, 67

Tracking Room-Bed

231.8........................................................ 40

Tracking Staff File

231.7....................................................... 38

Troubleshooting 	78

Blank View 	78

Check-in via Scheduling 	78

Nurse Assignments 	78

PCE Visits 	78

URLs

Production Account	4

Test Account	4

Web Application	4

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Emergency Dept Integration Software GUI (EDIS) Version 2.2.1 Technical Manual

### IAM Single Sign-On Internal (SSOi) and VistA Integration Adapter (VIA)

EDIS uses IAM Single Sign-On Internal (SSOi) to authenticate users and VistA Integration Adapter (VIA) and SAML connect to VistA to authorize users. Specifically, it authenticates users via VA issued PIV and uses VistA options and security keys to authorize access to role -based functionality.

### PIV Provisioning

If a user is unable to sign into EDIS with their PIV card, please reference the below Knowledge Base numbers for assistance.

[KB0013359](https://yourit.va.gov/nav_to.do?uri=%2Fkb_view.do%3Fsys_kb_id%3D6b6432591b2f6cd065a4433ee54bcbdb%26sysparm_rank%3D9%26sysparm_tsqueryId%3D569565de1b14fc10b25bea0de54bcbbb) - VistA: Link PIV Card to Vista/CPRS/CAPRI

[KB0013706](https://yourit.va.gov/nav_to.do?uri=%2Fkb_view.do%3Fsys_kb_id%3D69971d831babe810176762cae54bcbb3%26sysparm_rank%3D3%26sysparm_tsqueryId%3De724ce161b943050b25bea0de54bcb11) - SSOi: Accessing Applications Using Windows Authentication

### Big Boards

#### Big Board patient data is not updating properly

If the patient data on the Big Board is not updating properly or the data is displaying incorrectly, please reboot the Big Board. It is imperative that any configuration changes, such as adjusting column widths and sizes, are performed in the EDIS desktop application. Do not make configuration changes within the Big Board itself. See Section 8.2.2, **Columns** , of the *EDIS User Guide* for assistance.

#### The display on the Big Board does not fit to the screen

There is a **Display Size** field in the EDIS desktop application within the **Configure** view. The value in the **Display Size** field should match the Display Resolution of the Big Board monitor. Someone with access to the **Configure** view will need to set the **Display Size** value in the EDIS desktop application. If the screen size is not available, add it to the EDPF SCREEN SIZES VistA Parameter:
