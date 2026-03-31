---
title: PADP Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: NUPA
app_name: Patient Assessment Documentation Package (PADP)
section: CLI
app_status: active
pkg_ns: NUPA
patch_ver: 1
patch_id: NUPA*1
group_key: "NUPA:NUPA:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - nupa
  - consult
  - table
  - contents
  - class
  - installation
  - care
  - admission
  - padp
  - plan
page_count: 0
word_count: 3594
section_count: 8
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Assessment_Documentation_Package/nupa1_0ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Assessment_Documentation_Package/nupa1_0ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=193"
---

---
title: Patient Assessment Documentation Package (PADP)
---

C3-C1 Conversion Project

Package Status Update, January 2014:

This package’s status has been changed to Class 3 Software, and will no longer be supported nationally.

Installation Guide for NUPA Version 1.0

![](padp-version-1-installation-guide/001.png)

April 2012

Office of Information and Technology (OIT)

Office of Enterprise Development (OED)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date         | Patch or Version | Description                                                                                             | Author                             |
|--------------|------------------|---------------------------------------------------------------------------------------------------------|------------------------------------|
| January 2014 |                  | This package’s status has been changed to Class 3 Software, and will no longer be supported nationally. | <span class="mark">REDACTED</span> |
| April 2012   | 1.0              | Original release                                                                                        | <span class="mark">REDACTED</span> |
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [Introduction](#introduction)
- [Pre-installation Instructions](#pre-installation-instructions)
  - [Requirements for M Server Installation](#requirements-for-m-server-installation)
  - [Note Titles](#note-titles)
- [Installation Procedures](#installation-procedures)
  - [Anonymous Software and Documentation](#anonymous-software-and-documentation)
  - [Server Installation/Kernel Installation and Distribution System (KIDS)](#server-installationkernel-installation-and-distribution-system-kids)
- [Post-installation VistA Setup](#post-installation-vista-setup)
  - [IRM Support Staff](#irm-support-staff)
    - [Assign Menu and FileMan Access](#assign-menu-and-fileman-access)
    - [Schedule NUPA Purge Saved Notes Option](#schedule-nupa-purge-saved-notes-option)
  - [CAC or ADPAC Staff](#cac-or-adpac-staff)
    - [Set up Executables on the Tools Menus](#set-up-executables-on-the-tools-menus)
    - [Parameters for Consults Ordered from the PADP Templates](#parameters-for-consults-ordered-from-the-padp-templates)
    - [Set up Consult Parameters](#set-up-consult-parameters)
- [Attention: Site ISOs and Privacy Officers Update your existing site PIA](#attention-site-isos-and-privacy-officers-update-your-existing-site-pia)
Package Status Update, January 2014:
This package’s status has been changed to Class 3 Software, and will no longer be supported nationally.
In the Package file (#9.4), this application is known as Patient Assessment Documentation (PADP). The package namespace is NUPA. File numbers are in the range of 1927.09 to 1927.6. Contents of this package can be found in the VistA Software Documentation Library (VDL) in the Clinical Section. <http://www4.va.gov/vdl/>
The PADP software application enables Registered Nurses (RNs) to document, in a standardized format, patient care during an inpatient stay. Although the content is standardized for use across the VA system, some parameters can be set to support the unique processes at individual medical centers.
PADP consists of a KIDS build, NUPA 1.0, and four (4) Delphi GUI templates in three executables.
1.  The executable, Admassess.exe, contains the Admission - RN Assessment template and the Admission - Nursing Data Collection template.
- Admission – RN Assessment allows RNs to document the status of the patient at admission.
- Admission – Nursing Data Collection allows Licensed Practical Nurses (LPNs) and other nursing staff, including the RN, to enter basic patient data, such as vitals and belongings at the time of admission.
2.  The executable, Admassess_Shift.exe, contains the RN Reassessment template.  
    RN Reassessment allows RNs to document the condition of the patient on a regular basis and any time during the inpatient stay.
3.  The executable, Admassess_Careplan.exe, contains the Interdisciplinary Plan of Care template.  
    Interdisciplinary Plan of Care interfaces with admission and reassessment data, and allows additional information to be entered by the RN and other health care personnel (physicians, social workers, chaplain, etc.). All clinical staff can enter information into the Plan of Care. The Plan of Care can be printed and given to the patient when appropriate.
PADP also adds to VistA new health factors, fourteen (14) files, thirty-six (36) parameters, and five (5) printouts. The 5 printouts are:
1.  The Daily Plan<sup>®</sup> is a health summary designed to be given to the patient and family
    Located in Interdisciplinary Plan of Care, view CP tab
2.  Plan of Care is a plan designed to guide the nursing staff
    Located in Interdisciplinary Plan of Care, view CP tab
3.  Discharge Plan is for discharge planners
    Located in Interdisciplinary Plan of Care, view CP tab
4.  Belongings is a list of patient belongings
    Located in Admission – RN Assessment/Admission - Nursing Data Collection
5.  Safe Patient Handling is designed to guide the transfer of a patient  
    > Located on the Function tab in Admission - RN Assessment, RN Reassessment, and Interdisciplinary Plan of Care, view CP tab

# Pre-installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Requirements for M Server Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Related Software: All referenced software and patches must be up-to-date.  
PADP requires that the following software is installed and fully-patched.

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Package</th>
<th>Namespace</th>
<th>Minimum Version</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinical Reminders</td>
<td>PXRM</td>
<td>2.0*5</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td><p>OR</p>
<p>OR</p></td>
<td><p>GUI V. 27.90</p>
<p>3.0*243 (V. 27)</p></td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td>XU</td>
<td>8.0</td>
</tr>
<tr class="even">
<td>MailMan</td>
<td>XM</td>
<td>8.0</td>
</tr>
<tr class="odd">
<td>Text Integration Utilities</td>
<td>TIU</td>
<td>1.0</td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td>DI</td>
<td>22.0</td>
</tr>
<tr class="odd">
<td>Vitals/Measurements</td>
<td>GMRV</td>
<td>5.0*22</td>
</tr>
<tr class="even">
<td>Adverse Reaction Tracking</td>
<td>GMRA</td>
<td>4.0*42</td>
</tr>
<tr class="odd">
<td>Consult Request Tracking</td>
<td>GMRC</td>
<td>3.0*1</td>
</tr>
<tr class="even">
<td>Remote Procedure Call</td>
<td>XWB</td>
<td>1.1*47</td>
</tr>
<tr class="odd">
<td><p>MHA DLL (Mental Health Assistant DLL)</p>
<p>Mental Health Assistant</p></td>
<td><p>YS*5.01*98</p>
<p>All YS* patches</p></td>
<td></td>
</tr>
<tr class="even">
<td>Patient Care Encounter</td>
<td>PX</td>
<td>1</td>
</tr>
</tbody>
</table>

## Note Titles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PADP is hard-coded to look for the EXACT TIU Progress Note Title and that title must be associated with the following VHA Enterprise Standard Title.

| PADP Delphi Template:          | Admission – RN Assessment             |
|--------------------------------|---------------------------------------|
| TIU Progress Note Title:       | RN Admission Assessment               |
| VHA Enterprise Standard Title: | Nursing Admission Evaluation Note     |
|                                |                                       |
| PADP Delphi Template:          | Admission – Nursing Data Collection   |
| TIU Progress Note Title:       | Nursing Admission Data Collection     |
| VHA Enterprise Standard Title: | Nursing Admission Evaluation Note     |
|                                |                                       |
| PADP Delphi Template:          | RN Reassessment                       |
| TIU Progress Note Title:       | RN Reassessment                       |
| VHA Enterprise Standard Title: | Nursing Inpatient E & M Note          |
|                                |                                       |
| PADP Delphi Template:          | Interdisciplinary Plan of Care        |
| TIU Progress Note Title:       | Interdisciplinary Plan of Care        |
| VHA Enterprise Standard Title: | Interdisciplinary Treatment Plan Note |

A Clinical Application Coordinator (CAC) or an Automated Data Processing Application Coordinator (ADPAC) creates the note titles in TIU: *Create Document Definitions under Progress Notes Document Class*.

> **NOTE:** Do not add boilerplate text. However, if the note titles are already in the system, any associated boilerplate or template will not interfere with PADP process.

Example

Select Document Definitions (Manager) Option: create document definitions

![](padp-version-1-installation-guide/002.png)

Create Document Definitions page

Select Action: Next Screen// title Title

Enter the Name of a new NURSING TITLES: RN ADMISSION ASSESSMENT

CLASS OWNER: CLINICAL COORDINATOR// CLINICAL COORDINATOR

EVERY Local Title must be mapped to a VHA Enterprise Standard Title.

Direct Mapping to Enterprise Standard Title...

Your LOCAL Title is: RN ADMISSION ASSESSMENT

Select VHA ENTERPRISE STANDARD TITLE: NURSING ADMISSION EVALUATION NOTE

I found a match of: NURSING ADMISSION EVALUATION NOTE ... OK? Yes// YES

Ready to map LOCAL Title: RN ADMISSION ASSESSMENT to

VHA Enterprise Standard Title: NURSING ADMISSION EVALUATION NOTE. OK? Yes// YES Done.

STATUS: (A/I/T): INACTIVE// a ACTIVE Entry Activated.

SEQUENCE:

MENU TEXT: Rn Admission Assessm Replace

<span class="mark">Entry Created</span>

# Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** If PADP is installed and not implemented, only the Server Installation needs to be completed.  
If the application is implemented, both the Server Installation and VistA Setup must be completed. This includes assigning menu and file access, as well as setting up the TIU Progress Note Titles, the Tools links, and the Parameters for all Required and Optional Consult Services the facility is using.

- The IRM installs the M component and three Graphical User Interface (GUI) components. All the required M files are contained in the KIDS distribution file NUPA_1_0.KID. The executable files and help files are bundled into a zip file, NUPA.ZIP.
- Installation should take less than 3 minutes, but installing at non-peak hours is recommended.

## Anonymous Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PADP software and documentation files are available in the following names and formats:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 30%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Document File Description</th>
<th>File Names</th>
<th>FTP Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>KIDS Build</p>
<p>Executable and Help files</p></td>
<td><p>NUPA_1_0.KID</p>
<p>NUPA.ZIP</p></td>
<td><p>ASCII</p>
<p>Binary</p></td>
</tr>
<tr class="even">
<td>PADP Installation Guide</td>
<td><p>NUPA1_0IG.DOCX</p>
<p>NUPA1_0IG.PDF</p></td>
<td></td>
</tr>
<tr class="odd">
<td>PADP Technical Manual</td>
<td><p>NUPA1_0TM. DOCX</p>
<p>NUPA1_0TM.PDF</p></td>
<td></td>
</tr>
<tr class="even">
<td>PADP Admission – RN Assessment<br />
User Manual</td>
<td><p>NUPA1_0_AUM. DOCX</p>
<p>NUPA1_0_AUM.PDF</p></td>
<td></td>
</tr>
<tr class="odd">
<td>PADP RN Reassessment<br />
User Manual</td>
<td><p>NUPA1_0_RUM. DOCX</p>
<p>NUPA1_0_RUM.PDF</p></td>
<td></td>
</tr>
<tr class="even">
<td>PADP Admission – Nursing Data Collection<br />
User Manual</td>
<td><p>NUPA1_0_DCUM. DOCX</p>
<p>NUPA1_0_DCUM.PDF</p></td>
<td></td>
</tr>
<tr class="odd">
<td>PADP Interdisciplinary Plan of Care<br />
User Manual</td>
<td><p>NUPA1_0_IUM. DOCX</p>
<p>NUPA1_0_IUM.PDF</p></td>
<td></td>
</tr>
</tbody>
</table>

Retrieve these files via FTP from download.vista.med.va.gov, which transmits the files from the first available FTP server (preferred method). You can also retrieve the files directly from one of the following FTP sites:

| OIFO                               | FTP Address                        | Directory                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

## Server Installation/Kernel Installation and Distribution System (KIDS) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download NUPA_1_0.KID (ASCII mode), and NUPA.ZIP (BINARY mode), from the FTP server listed on the previous page.
4.  Move the files to the appropriate directory on your system.
5.  Select the Load a Distribution option and enter NUPA_1_0.KID when prompted at the host file prompt. You may need to prefix a directory name.

Example

Select Installation Option: LOAD a Distribution

Enter a Host File: VA16\$\[SMAVISTA.IRMPERSON\]NUPA_1_0.KID

KIDS Distribution saved on Jan 19, 2012@10:16:50

Comment: NUPA 1.0

This Distribution contains Transport Globals for the following Package(s):

NUPA\*1.0\*0

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

NUPA\*1.0\*0

Use INSTALL NAME: NUPA\*1.0\*0 to install this Distribution.

6.  Select any or all of the following options (KIDS Installation Menu) as desired:
- Print Transport Global
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
7.  From the Kernel Installation & Distribution System menu, select the Backup a Transport Global menu.

Select Installation Option: Backup a Transport Global

Select INSTALL NAME: NUPA\*1.0\*0 Loaded from Distribution 1/19/12@10:16:05

=\> Completed/Released NUPA\*1.0\*0

It consists of the following Install(s):

NUPA\*1.0\*0

Subject: Backup of NUPA\*1.0\*0 install on Jan 19, 2012

Replace

Loading Routines for NUPA\*1.0\*0…

Send Mail to:G.PATCHES BACKUP

And Send to:

…….message sent……

8.  From the Kernel Installation & Distribution System menu, select the Installation menu.

Select Installation Option: Install Package(s)

Select INSTALL NAME: NUPA\*1.0\*0 1/13/12@12:45:21

=\> NUPA 1.0 ;Created on Jan 19, 2012@10:16:50

This Distribution was loaded on 1/13/12@12:45:21 with header of

NUPA 1.0 ;Created on Jan 19, 2012@10:16:50

It consists of the following Install(s):

NUPA\*1.0

Checking Install for Package NUPA\*1.0\*0

Install Questions for NUPA\*1.0\*0

Incoming Files:

   1927.09   NUPA SAVED NOTES

   1927.2    NUPA ASSESSMENT PROBLEMS  (including data)

   1927.23   NUPA PLAN DESCRIPTION TABS  (including data)

   1927.24   NUPA ASSESSMENT INTERVENTIONS  (including data)

   1927.3    NUPA ASSESSMENT DESCRIPTIONS  (including data)

   1927.32   NUPA PCE INFO

   1927.4    NUPA CARE PLANS

   1927.401  NUPA CARE PLAN PRESSURE ULCERS

   1927.4011 NUPA CARE PLAN SKIN ALT TYPES  (including data)

   1927.402  NUPA CARE PLAN IVS

   1927.403  NUPA CARE PLAN GI/GU DEVICES

   1927.41   NUPA COMPONENT ITEMS  (including data)

   1927.5    NUPA CARE PLAN TEXT CHANGE LOG

   1927.6    NUPA DISCHARGE PLANNING GOAL COMMENTS

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   HOME  (CRT)

                                NUPA\*1.0\*0                                  

 Installing OPTION

 Installing PARAMETER DEFINITION

               Jan 11, 2012@12:46:40

 Running Post-Install Routine: ^NUPAPI

 Updating Routine file...

 Updating KIDS files...

 NUPA\*1.0\*0 Installed.

               Jan 11, 2012@12:46:40

100%

Complete

Install Completed

9.  Verify new Checksums.

Select Programmer Options Option: Calculate and Show Checksum Values

This option determines the current Old (CHECK^XTSUMBLD) or New (CHECK1^XTSUMBLD) logic checksum of selected routine(s).

     Select one of the following:

          1         Old

          2         New

New or Old Checksums: New//

New CheckSum CHECK1^XTSUMBLD:This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

   followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

   exceptions noted above) by multiplying the ASCII value of each

   character by its position on the line and position of the line in

   the routine being checked.

     Select one of the following:

          P         Package

          B         Build

Build from: Package

 

All Routines? No =\> No

Routine: NUPABCL

Routine: NUPABCL1

Routine: NUPABCL2

Routine: NUPAOBJ

Routine: NUPAOBJ1

Routine: NUPAPI

Routine: NUPAPI1

Routine: NUPAPI2

Routine:

8 routines

NUPABCL value = 28658049

NUPABCL1 value = 34269162

NUPABCL2 value = 92151696

NUPAOBJ value = 46106373

NUPAOBJ1 value = 73459792

NUPAPI value = 36387812

NUPAPI1 value = 181278121

NUPAPI2 value = 181599162

done

10. The IRM support staff unzips the NUPA.ZIP file and places the files in a designated folder on an application server, i.e., \\vhaxxxmul##\VISTA_Software\CPRS\NursingAssessment.

> The NUPA.ZIP file contains the following files:

1.  Admassess.exe
11. Admassess_Shift.exe
12. Admassess_Careplan.exe
13. Admassess_CRC.txt
14. borlndmm.dll
15. Nupa1_0um help DC.chm
16. Nupa1_0um help R.chm
17. Nupa1_0um help IPofC.chm
18. Nupa1_0um help A.chm

> **NOTE:** If the site chooses to only INSTALL Patient Assessment Documentation Package and not implement, you have completed the install process. The VistA set up of PADP is only required if you are planning to implement the new application.

# Post-installation VistA Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## IRM Support Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Assign Menu and FileMan Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Assign menu and FileMan access.
1.  For all staff who will enter data into the four templates:Assign the NUPA ASSESSMENT GUI as a secondary menu option.
2.  For the person responsible for the NUPA parameters:  
    Assign FileMan Codes: Nn and give Read, Write, Delete and Laygo access for the NUPA ASSESSMENT HEALTH FACTORS/PCE INFO file (#1927.32).  
    The other NUPA files must not be edited locally.

> **NOTE:** Assigning the FileMan menu is optional.  
If the site is not setting up Nursing Reminders to be resolved in PADP, do not edit this file.  
If your site is setting up Nursing Reminders, discuss this with the Clinical Reminders CAC at your site and refer to Edit File NUPA PCE Info in the *PADP Technical Manual* for setup examples.

### Schedule NUPA Purge Saved Notes Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

19. Schedule the NUPA PURGE SAVED NOTES option.
1.  Information from notes *saved for later*: Nursing Admission Data Collection, RN Admission Assessment and RN Reassessment, is in the NUPA SAVED NOTES file (#1927.09).
2.  To purge the NUPA SAVED NOTES file (#1927.09) on a regular basis, the IRM staff must set up the purge option. This purges any saved (unsigned) information older than five days.
3.  Queue the NUPA PURGE SAVED NOTES option to run via Taskman’s Schedule/Unschedule Options (XUTM SCHEDULE) menu to run on a daily basis shortly after midnight.

Select OPTION to schedule or reschedule: NUPA PURGE SAVED NOTES       Purge Saved Notes Over 5 Days Old

         ...OK? Yes//   (Yes)

                        Edit Option Schedule

    Option Name: NUPA PURGE SAVED NOTES

    Menu Text: Purge Saved Notes Over 5 Days Ol          TASK ID: 2885947

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

  QUEUED TO RUN AT WHAT TIME: DEC 4,2009@00:30

 

DEVICE FOR QUEUED JOB OUTPUT:

 

 QUEUED TO RUN ON VOLUME SET:

 

      RESCHEDULING FREQUENCY: 1D

              TASK PARAMETERS:

            SPECIAL QUEUEING:

## CAC or ADPAC Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IRM support staff provides to the CAC the exact server folder name in which the NUPA.zip file was placed. The CAC uses this server address to set up the executables on the Tools menu in CPRS.

### Set up Executables on the Tools Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Set up the executables on the CPRS Tools menu.
- Admassess.exe contains the templates: Admission - RN Assessment and Admission - Nursing Data Collection
- Admassess_Shift.exe contains the template: RN Reassessment
- Admassess_Careplan.exe contains the template: Interdisciplinary Plan of Care

> Follow the steps in the example

1.  Select the CPRS Manager Menu option: PE CPRS Configuration (Clin Coord).  
    Select GP, GUI Parameters to set up the Tools link for admassess.exe.

Select GUI Parameters Option: TM GUI Tool Menu Items

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[DEVCUR.FO-SLC.MED.VA.GOV\]

Enter selection: 3 Division INSTITUTION

Select INSTITUTION NAME: SALT LAKE CITY OIFO UT ISC 5000

------- Setting CPRS GUI Tools Menu for Division: SALT LAKE CITY OIFO -------Select Sequence: 2

Are you adding 2 as a new Sequence? Yes// y YES

Sequence: 2// 2

Name=Command: Admission Assessment= ”\\vhaxxxmul##\VISTA_Software\CPRS\NursingAssessment\Admassess.exe” %SRV %PORT %DFN

> **NOTE:** The Assessment is not CCOW compliant; including %DFN in the command line, forces the chart to open at the same patient to which CPRS is currently open.

2.  For Admission - Nursing Data Collection, set up the item as in the example, but add the parameter datacoll to the end of the Name:Command line.
3.  Repeat step a for the Interdisciplinary Plan of Care (admassess_careplan.exe) and RN Reassessment (admassess_shift.exe).

Summary of display from the CPRS Manager Menu

Admission Assessment= ”\\vhaxxxmul##\VISTA_Software\CPRS\NursingAssessment\Admassess.exe” %SRV %PORT %DFN

Nursing Data Collection=

”\\vhaxxxmul##\VISTA_Software\CPRS\NursingAssessment\Admassess.exe” %SRV %PORT %DFN datacoll

RN Reassessment=

”\\vhaxxxmul##\VISTA_Software\CPRS\NursingAssessment\Admassess_shift.exe” %SRV %PORT %DFN

Interdisciplinary Plan of Care=

”\\vhaxxxmul##\VISTA_Software\CPRS\NursingAssessment\admassess_Careplan.exe" %SRV %PORT %DFN

### Parameters for Consults Ordered from the PADP Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following parameters control consults that can be ordered from the PADP templates.

#### Parameters that control required consults

The following consult parameters control required consults.

NUPA CHAPLAIN CONSULT Chaplain Consult

NUPA NUTRITION CONSULT Nutrition consult name

NUPA PRESSURE ULCER SITE Pressure ulcer site

NUPA SOCIAL WORK CONSULT Social Work consult name

NUPA SPEECH CONSULT Speech consult name

NUPA WOUND CARE CONSULT Wound care consult

#### Parameters that control optional consults

The following parameters control optional consults.

1.  If you will use the Associated Consult in your Patient Assessment Documentation system, set the SEND parameter value to YES.

NUPA SEND DIAB NURSE CONS Send Diabetes Nurse Consult

NUPA SEND DISCH PLAN CONSULT Send Discharge Planning Consult

NUPA SEND HOME CARE CONSULT Send Home Care Consult

NUPA SEND NURSE REHAB CONSULT Send Nurse Rehab consult

NUPA SEND NURSE REST CONSULT Send Nurse Rest. consult

NUPA SEND RESPIRATORY CONSULT Send respiratory consult

NUPA SEND TELEHEALTH CONSULT Send Telehealth Consult

NUPA SEND WOMENS H CONSULT Send Women's Health consult

20. For the eight SEND parameters above with a value set to YES, now enter the name of the Associated Consult specialty in the NUPA Consult parameters below.

NUPA DIAB NURSE CONSULT Diabetes Nurse Consult

NUPA DISCH PLAN CONSULT Discharge Planning consult name

NUPA HOME CARE CONSULT Home Care consult name

NUPA NURSE REHAB CONSULT Rehab consult name

NUPA NURSE REST CONSULT Nurse Restorative consult name

NUPA RESPIRATORY CONSULT      Respiratory consult name

NUPA TELEHEALTH CONSULT Telehealth Consult name

NUPA WOMENS HEALTH CONSULT Women's Health Consult name

### Set up Consult Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To set up the parameters, use the XPAR Menu Tools, Edit Parameter Values \[XPAR EDIT PARAMETER\].

1.  Review the consults in your system.
21. Identify the consult specialties that you order via the notes: RN Admission Assessment and RN Reassessment.
22. Keep the following considerations in mind:
- If you are a single division medical center, set the parameter at System or Division level. Associate the System or Division with the appropriate consult.
- If there is only one consult for a Specialty for the entire system or division, set the parameter at the System or Division level. Associate the System or Division with the appropriate consult.
- If there is one consult for a Specialty per Division, set the parameter at the Division level. Associate the Division with the appropriate consult.
- If there is more than one consult per Specialty for a Division, like one social work consult for Med/Surg units and another one for Mental Health/Psych units, set the parameter at the Location (MAS bed section, ward) level. Associate each Location with the appropriate consult.

Example: Set One Consult Service per Specialty at the System Level

Set up NUPA CHAPLAIN CONSULT as:

Select Menu Option: IR CPRS Configuration (IRM)

Select CPRS Configuration (IRM) Option: XX General Parameter Tools

Select General Parameter Tools Option: EP Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME:NUPA CHAPLAIN CONSULT

NUPA CHAPLAIN CONSULT may be set for the following:

1 Location LOC \[choose from HOSPITAL LOCATION\]

2 Division DIV \[choose from INSTITUTION\]

3 System SYS \[TEST.BRONX.MED.VA.GOV\]

Enter selection: 3 System

Select SYSTEM NAME: TEST.BRONX.MED.VA.GOV

---------- Setting NUPA CHAPLAIN CONSULT for System:

Consult name: CHAPLAIN

# Attention: Site ISOs and Privacy Officers Update your existing site PIA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must add the following information to the appropriate Minor Application tab of your existing site PIA.

- Tab 10 is for a minor application that gets security controls from VistA. 
- Tab 11 is for a standalone minor application.

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Patient Assessment Documentation Package (PADP)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td><p>The Patient Assessment Documentation Package (PADP) is a Veterans Health Information Systems and Technology Architecture (VistA) software application that enables Registered Nurses (RNs) to document, in a standardized format, patient care during an inpatient stay.</p>
<p>NUPA namespace</p></td>
</tr>
<tr class="even">
<td>Comments</td>
<td></td>
</tr>
<tr class="odd">
<td>Is PII collected by this minor application?</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Does this minor application store PII?</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>If yes, where?</td>
<td>VistA</td>
</tr>
<tr class="even">
<td>Who has access to this data?</td>
<td>Local VA clinicians</td>
</tr>
</tbody>
</table>