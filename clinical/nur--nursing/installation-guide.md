---
title: Nursing Version 4 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: NUR
app_name: Nursing
section: CLI
app_status: active
pkg_ns: NUR
patch_ver: 4
patch_id: NUR*4
group_key: "NUR:NUR:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - nurs
  - colspan
  - class
  - nursing
  - installation
  - nursf
  - even
  - width
  - amis
page_count: 0
word_count: 3424
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nursing/nurs4_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nursing/nurs4_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=80"
---

> ![](nursing-version-4-installation-guide/001.png)

NURSING INSTALLATION GUIDE

> Version 4.0

> April 1997

> (Revised January 2000)

> Department of Veterans Affairs Technical Service

> Clinical Applications Product Line

> Installation Guide

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [Nursing V. 4.0 Installation](#nursing-v-40-installation)
- [Example - Nursing Installation (Non-virgin install)](#example-nursing-installation-non-virgin-install)
- [Post Initialization Tasks](#post-initialization-tasks)
- [File Security](#file-security)
- In this Installation Guide, the following applications are known as:
<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 39%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u>Package File Name</u></p>
<p>Nursing Service</p></th>
<th><blockquote>
<p><u>Application</u></p>
<p>Nursing</p>
</blockquote></th>
<th><blockquote>
<p><u>Namespace</u></p>
<p>NUR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Gen. Med. Rec. - I/O</td>
<td><blockquote>
<p>Intake and Output</p>
</blockquote></td>
<td><blockquote>
<p>GMRY</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Gen. Med. Rec. – Vitals</td>
<td><blockquote>
<p>Vitals/Measurements</p>
</blockquote></td>
<td><blockquote>
<p>GMRV</p>
</blockquote></td>
</tr>
</tbody>
</table>
- Nursing V. 4.0, Intake and Output V. 4.0, and Vitals/Measurements V. 4.0 are distributed together and their functionality is linked together. You should install these three packages one immediately after the other in the following order:
  1.  Intake and Output V. 4.0
  2.  Vitals/Measurements V. 4.0
  3.  Nursing V. 4.0
- If the Nursing package is installed on your system, Nursing Version 3.0, along with patches 1 and 3 (i.e., NUR\*3\*1 and NUR\*3\*3) must be resident before Version 4.0 can be installed.
- The following describes the installation environment for Nursing Version 4.0:
1.  Nursing V. 4.0 requires that the following V*IST*A (Veterans Health Information Systems and Technology Architecture) packages must be loaded in order to use the software:
    1.  VA FileMan V. 21 or greater,
    2.  Kernel V. 8.0 or greater,
    3.  Kernel Toolkit V. 7.3 or greater,
    4.  PIMS V. 5.3 or greater,
    5.  PAID V. 4.0 or greater (optional),
    6.  Dietetics V. 4.6 or greater (optional),
    7.  Health Summary V. 2.7 or greater (optional),
    8.  Intake and Output V. 4.0,
    9.  Vitals/Measurements V. 4.0,
    10. Text Generator V. 3.0.
> Installation Guide
- Sites having made any local modifications to verified Nursing routines and/or data dictionaries may have such modifications overwritten. The convention for locally modified or developed routines is to have them stored as namespace_Z (i.e., NURAZ\*, NURCZ\*, NURQZ\*, and NURSZ\*) routines. The convention for adding fields to the database is that such field numbers are prefixed with the station number followed by three or more other numbers (e.g. 578xxx). Local changes that comply with these conventions are not overwritten during this installation.
- The Nursing package uses the Text Generator V. 3.0 package to create nursing care plans. If you wish to use the nursing care plan functionality you must have the Text Generator package installed. If you need to install the Text Generator package, please ensure that 30 megabytes of free space is available for installation of the Aggregate Term (#124.2) file. This free space requirement is only for installation of the package. The amount of free space can be determined by running one of the following operating system utilities:
1)  DSM ^FASTDBT or ^DBT
2)  OPENM ^%FREECNT
3)  MSM ^%SP
- Resource Requirements
1.  Data Entry and Printer Devices:
> The minimal hardware requirements for input and output devices are dependent upon the location in which patient care is provided and the quality of reports generated.
> Input devices: In an inpatient setting, there should be a sufficient number of data input devices at the point of care, in the nurse's station, physician offices, and conference rooms. Ambulatory Care settings should provide input devices in each clinic room, physician offices, conference rooms and reception areas.
> Output devices: The graphic reports (Vitals Graphic Record, blood pressure and weight reports) display data in a linear format when a programmable laser printer is used to print patient information. Printers included in this category:
1.  Have been previously purchased through a central procurement (Kyocera F-800A laser printers).
2.  Are Hewlett-Packard compatible printers (e.g. HP LaserJet III, HP LaserJet 4, HP LaserJet 5, and Epson EPL-8000 printers) that have been purchased by the medical center.
> There should be minimally one to two laser printers on an inpatient unit to support this application. Ambulatory care areas should have a printer in both the reception area and a centralized location in each clinic.
Installation Guide
2.  Printer Setup Issues: When using a programmable graphic laser printer, the setups need to be checked, to insure the correct format on the printed page.
> The following special printer setup is for Kyocera type printers:
1.  Ensure the existence of a Kyocera entry in the Terminal Type file. This device compresses print and has a margin width of 132 characters. This entry may be exported by Kernel, or you may have to set up your own entry.
    1.  The Name (#.01) field should begin with the characters P-KYOCERA, e.g., P- KYOCERA-P16. This is important as the software will not recognize the device as a Kyocera printer if this Terminal Type entry is not set up properly.
    2.  The Right Margin (#1) field must be 132.
2.  Create a Device file entry for the Kyocera printer.
    1.  The Name (#.01) field should contain the word KYOCERA. This isn't required, but will make selection of this device by users easier.
    2.  Sub-Type (#3) field should point to a Terminal Type entry that fits the characteristics defined above in (a-1).
    3.  Margin Width (#9) field should be 132.
3.  In the Kyocera printer, PRESCRIBE Macro Buffer Size (H0)=99. To reprogram your printer,
    1.  Type: !R! RES; FRPO H0, 99; EXIT; on your terminal/input device.
    2.  Print this code on your Kyocera printer (using appropriate print commands). This may be done through a mail message.
    3.  Turn off the printer for a few seconds, then place the printer back on line (by turning it on). The printer will then be ready to print the linear graphic reports (e.g., SF511).
> The following special printer setup is for HP LASERJET III, HP LASERJET 4 and HP LASERJET 5 printers:
1.  Ensure the existence of a HP LASERJET entry in the Terminal Type file. This device compresses print and has a margin width of 132 characters. This entry may be exported by Kernel, or you may have to set up your own entry.
> Installation Guide
1.  The Name (#.01) field should begin with the characters P-HPLASER, e.g., P-HPLASER- L180. This is important as the Vitals/Measurements software will not recognize the device as an HP LASERJET printer if this Terminal Type entry is not set up properly.
2.  The Right Margin (#1) field must be 132.
2.  Create a Device file entry for the HP LASERJET printer.
    1.  The Name (#.01) field should contain the word HPLASER. This isn't required, but will make selection of this device by users easier.
    2.  Sub-Type (#3) field should point to a Terminal Type entry that fits the characteristics defined above in (b-1).
    3.  Margin Width (#9) field should be 132.
    4.  Suppress Form Feed at Close (#11.2) field should be set to YES.
> Note: If the printer is not set up correctly, it will affect the printed output. KYOCERA and HPLASER are key words in the routine to identify which printer is being used, and IRMS (Information Resource Management Service) must edit the Device file so the word KYOCERA or HPLASER appears in the name of the device (e.g., KYOCERA-PORT).
3.  Disk Storage:
> The following statistics regarding disk storage requirements of this Nursing software were compiled by the Alpha/Beta test sites.
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 37%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><u>Globals</u></th>
<th><blockquote>
<p><u>Type of Data</u></p>
</blockquote></th>
<th><blockquote>
<p>Installation Guide</p>
<p><u>Size</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DDs</td>
<td></td>
<td><blockquote>
<p>340 blocks</p>
</blockquote></td>
</tr>
<tr class="even">
<td>NURSA</td>
<td><blockquote>
<p>AMIS data classification</p>
</blockquote></td>
<td><blockquote>
<p>3-4 blocks/nursing location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>NURC</td>
<td><blockquote>
<p>Care plan data</p>
</blockquote></td>
<td><blockquote>
<p>2-12 blocks/patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td>NURQ</td>
<td><blockquote>
<p>QI Summary</p>
</blockquote></td>
<td><blockquote>
<p>1-18 blocks/patient</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>NURSF</td>
<td><blockquote>
<p>Staff data</p>
</blockquote></td>
<td><blockquote>
<p>.86 blocks/staff</p>
</blockquote></td>
</tr>
<tr class="even">
<td>NURSF(213.1</td>
<td><blockquote>
<p>Nursing pointer files</p>
</blockquote></td>
<td><blockquote>
<p>block size is dependent upon class of hospital: Class I - 296 Class II - 256 Class III - 111 Class V - 98</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>GMR</td>
<td><blockquote>
<p>Patient data for the Vitals/Measurements, and Intake and Output Modules</p>
</blockquote></td>
<td><blockquote>
<p>50-75 blocks/ patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td>GMRD</td>
<td><blockquote>
<p>Static data for the Vitals/Measurements, and Intake and Output Modules</p>
</blockquote></td>
<td><blockquote>
<p>1200-1400 blocks depending on the global efficiency</p>
</blockquote></td>
</tr>
</tbody>
</table>
- The following steps are a sample of an installation of Version 4.0 of the Nursing software:

# Nursing V. 4.0 Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Pre-installation instructions:
    1.  Make sure Nursing V. 3.0 is installed. You can check this by entering the following command:
        - W \$\$VERSION^XPDUTL("NURS")

> \> 3.0

2.  Make sure patch NUR\*3\*1 is installed. You can check this by entering the following command:

> \> W \$D(^NURQ(217,0))

> \> 1

> Installation Guide

3.  Make sure patch NUR\*3\*3 is installed. You can check this by entering the following command:

> \> W \$D(^NURSF(212.7,0))

> \> 1

4.  Make sure Text Generator V. 3.0 is installed. You can check this by entering the following command:
    - W \$\$VERSION^XPDUTL("GMRG")
    - 3.0
5.  Make sure Intake and Output is installed. You can check this by entering the following command:
    - W \$\$VERSION^XPDUTL("GMRY")
    - 4.0
6.  Make sure Vitals/Measurements is installed. You can check this by entering the following command:
    - W \$\$VERSION^XPDUTL("GMRV")
    - 4.0
7.  Use FileManager to find and re-point any Package (#9.4) file entries which have NUR as the Prefix (#1) field value to the NURSING SERVICE entry.

> Select OPTION: 3 SEARCH FILE ENTRIES

> OUTPUT FROM WHAT FILE: PACKAGE// 9.4 PACKAGE (150 entries)

> -A- SEARCH FOR PACKAGE FIELD: 1 PREFIX

> -A- CONDITION: EQUALS

> -A- EQUALS: NUR

> -B- SEARCH FOR PACKAGE FIELD: \<RET\>

> IF: A// \<RET\> PREFIX EQUALS "NUR"

> STORE RESULTS OF SEARCH IN TEMPLATE: \<RET\>

> SORT BY: NAME// \<RET\>

> START WITH NAME: FIRST// \<RET\> FIRST PRINT FIELD: .01 NAME THEN PRINT FIELD: 1 PREFIX THEN PRINT FIELD: \<RET\>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Heading (S/C): PACKAGE SEARCH// \<RET\>

> DEVICE: Enter appropriate device

> PACKAGE SEARCH JAN 29,1997 10:53 PAGE 1 NAME PREFIX

> NURSING PACKAGE NUR

Installation Guide

> 1 MATCH FOUND.

> Note: If you have any entries in the Package (#9.4) file which have NUR as the Prefix (#1) field value (i.e., the Namespace) and the Name (.01) field value is not NURSING SERVICE you must delete those entries and update pointers to the NURSING SERVICE entry.

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES INPUT TO WHAT FILE: PACKAGE// \<RET\>

> EDIT WHICH FIELD: ALL// \<RET\>

> Select PACKAGE NAME: NURSING PACKAGE NUR NAME: NURSING PACKAGE// @

> SURE YOU WANT TO DELETE THE ENTIRE 'NURSING PACKAGE' PACKAGE? Y (Yes) SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

> BY ENTRIES IN THE 'DIALOG' FILE, ETC.,

> DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// Y

> (Yes)

> WHICH DO YOU WANT TO DO? --

1)  DELETE ALL SUCH POINTERS
2)  CHANGE ALL SUCH POINTERS TO POINT TO A DIFFERENT 'PACKAGE' ENTRY

> CHOOSE 1) OR 2): 2

> THEN PLEASE INDICATE WHICH ENTRY SHOULD BE POINTED TO Select PACKAGE NAME: NURSING SERVICE

1.  NURSING SERVICE NURS
2.  NURSING SERVICE STAFF PROFILE NW CHOOSE 1-2: 1

> (RE-POINTING WILL OCCUR WHEN YOU LEAVE 'ENTER/EDIT' OPTION)

> Select PACKAGE NAME: \<RET\>

> ...EXCUSE ME, HOLD ON...

> DEVICE: HOME// Enter appropriate device

> DIALOG entries whose 'PACKAGE' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> INSTITUTION entries whose '\*PAXKAGE X-REF' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> KERNEL SITE PARAMETERS entries whose 'ALPHA/BETA TEST PACKAGE' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> Installation Guide

> BUILD entries whose 'PACKAGE FILE LINK' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> INSTALL entries whose 'PACKAGE FILE LINK' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> OPTION entries whose 'PACKAGE' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> ORDER entries whose 'PACKAGE' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> ORDER STATISTICS entries whose 'PACKAGE' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> ORDER PARAMETERS entries whose 'PACKAGE SITE PARAMETERS' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> ORDER PARAMETERS entries whose 'PACKAGE PARAMETERS' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> PROTOCOL entries whose 'PACKAGE' pointers have been changed

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> KERNEL SYSTEM PARAMETERS entries whose 'ALPHA/BETA TEST PACKAGE' pointers have been changed

Installation Guide

> JAN 29,1997 10:54 PAGE 1

> ...

> ...

> ...

> MASTER CONTROL entries whose 'PACKAGE' pointers have been changed

> JAN 29,1997 10:55 PAGE 1

> ...

> ...

> ...

1.  Use FileManager to change the Prefix (#1) field value from NURS to NUR for the NURSING SERVICE entry in the Package (#9.4) file.

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES INPUT TO WHAT FILE: PACKAGE// \<RET\>

> EDIT WHICH FIELD: ALL// 1 PREFIX

> THEN EDIT FIELD: \<RET\>

> Select PACKAGE NAME: NURSING SERVICE

1.  NURSING SERVICE NURS
2.  NURSING SERVICE STAFF PROFILE NW CHOOSE 1-2: 1

> PREFIX: NURS// NUR

> Select PACKAGE NAME: \<RET\>

2.  Before installation of the nursing software:
    1.  Coordinate the installation with the package ADPAC.
    2.  Schedule downtime with the users of the package. Since the installation will put the NUR namespace options out-of-service for the duration of the install, the system does not have to be down during the installation.
    3.  Backup the system.
    4.  Disable routine mapping and journaling if appropriate. MSM sites should not turn journaling off, but should monitor journal space being used during the installation. The following routines have been recommended for mapping:

> NURSCPL, NURSAMSG, NURACE\*, NURSAPCH, NURSCUTL and NURSAWCK.

5.  Set variables DUZ and DUZ(0)="@" by executing the following command D ^XUP.
3.  (Optional) Test sites may delete any old nursing routines (NURA\*, NURC\*, NURQ\*, NURS\* and NURE\*), not including local routines NURAZ\*, NURCZ\*, NURSZ\* and NUREZ\*, from the system.

> Installation Guide

4.  Use the Schedule/Unschedule option to unschedule the Nursing Acuity/ Separation- Activation Run \[NURAAM-ACU\] option before installation.
5.  Load the KIDS Distribution containing Nursing V. 4.0 build.

Installation Guide

# Example - Nursing Installation (Non-virgin install)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- D ^XUP

> Setting up programmer environment Terminal Type set to: C-VT100

> Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: INStallation

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation Option: LOAD a Distribution Enter a Host File: NURS4.KID

> KIDS Distribution saved on Feb 10, 1997@11:21:56 Comment: Nursing v4.0 KIDS Build

> This Distribution contains Transport Globals for the following Package(s): NURSING SERVICE 4.0

> Want to Continue with Load? YES// \<RET\>

> Loading Distribution...

> Want to RUN the Environment Check Routine? YES// \<RET\>

> NURSING SERVICE 4.0

> Will first run the Environment Check Routine, NURXENV

> Use INSTALL NAME: NURSING SERVICE 4.0 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: NURSING SERVICE 4.0 Loaded from Distribution 2/ 10/97@11:25:51

> =\> Nursing v4.0 KIDS Build ;Created on Feb 10, 1997@11:21:56

> April 1997 Nursing V. 4.0 Installation Guide 11

> Installation Guide

> This Distribution was loaded on Feb 10, 1997@11:25:51 with header of Nursing v4.0 KIDS Build ;Created on Feb 10, 1997@11:21:56

> It consisted of the following Install(s):

> NURSING SERVICE 4.0

> NURSING SERVICE 4.0

> Will first run the Environment Check Routine, NURXENV Install Questions for NURSING SERVICE 4.0

> 210 NURS STAFF

> Note: You already have the 'NURS STAFF' File.

1.  NURS PAY SCALE (including data) Note: You already have the 'NURS PAY SCALE' File. Data will NOT be added.
2.  \*NURS GRADE/STEP

> Note: You already have the '\*NURS GRADE/STEP' File.

3.  NURS SERVICE POSITION (including data) Note: You already have the 'NURS SERVICE POSITION' File. Data will NOT be added.
4.  NURS LOCATION

> Note: You already have the 'NURS LOCATION' File.

5.  NURS CLINICAL BACKGROUND (including data) Note: You already have the 'NURS CLINICAL BACKGROUND' File. Data will NOT be added.
6.  NURS TOUR OF DUTY (including data) Note: You already have the 'NURS TOUR OF DUTY' File. Data will NOT be added.
7.  NURS AMIS POSITION (including data) Note: You already have the 'NURS AMIS POSITION' File. Data will NOT be added.
8.  NURS POSITION CONTROL

> Note: You already have the 'NURS POSITION CONTROL' File.

9.  NURS VACANCY/TRANSFERRED REASONS (including data) Note: You already have the 'NURS VACANCY/TRANSFERRED REASONS' File. Data will NOT be added.
1.  NURS EDUCATION (including data)

Installation Guide

> Note: You already have the 'NURS EDUCATION' File. Data will NOT be added.

2.  NURS CERTIFICATION (including data) Note: You already have the 'NURS CERTIFICATION' File. Data will NOT be added.
3.  NURS COLLEGE MAJOR (including data) Note: You already have the 'NURS COLLEGE MAJOR' File. Data will NOT be added.
4.  \*NURS MANDATORY INSERVICE

> Note: You already have the '\*NURS MANDATORY INSERVICE' File.

> 212.42 \*NURS MI CLASS GROUP

> Note: You already have the '\*NURS MI CLASS GROUP' File.

6.  NURS PRIVILEGE (including data) Note: You already have the 'NURS PRIVILEGE' File. Data will NOT be added.
7.  NURS PRODUCT LINE (including data) Note: You already have the 'NURS PRODUCT LINE' File. Data will NOT be added.
1.  \*NURS AMIS 1106 CLASS

> Note: You already have the '\*NURS AMIS 1106 CLASS' File.

2.  NURS AMIS 1106B FTEE

> Note: You already have the 'NURS AMIS 1106B FTEE' File.

3.  NURS AMIS WARD (including data) Note: You already have the 'NURS AMIS WARD' File. Data will NOT be added.
4.  NURS AMIS 1106 MANHOURS

> Note: You already have the 'NURS AMIS 1106 MANHOURS' File.

5.  NURS AMIS DAILY EXCEPTION REPORT

> Note: You already have the 'NURS AMIS DAILY EXCEPTION REPORT' File.

> 213.9 NURS PARAMETERS

> Note: You already have the 'NURS PARAMETERS' File.

> 214 NURS PATIENT

> Note: You already have the 'NURS PATIENT' File.

> Installation Guide

6.  NURS CLASSIFICATION

> Note: You already have the 'NURS CLASSIFICATION' File.

7.  NURS REVIEW CLASSIFICATION

> Note: You already have the 'NURS REVIEW CLASSIFICATION' File.

> 216.8 NURS CARE PLAN

> Note: You already have the 'NURS CARE PLAN' File.

217. NURQ QI SUMMARY

> Note: You already have the 'NURQ QI SUMMARY' File.

1.  NURQ STANDARDS OF CARE/PRACTICE

> Note: You already have the 'NURQ STANDARDS OF CARE/PRACTICE' File.

2.  NURQ RATIONALE (including data) Note: You already have the 'NURQ RATIONALE' File. Data will NOT be added.
3.  NURQ FREQUENCY (including data) Note: You already have the 'NURQ FREQUENCY' File. Data will NOT be added.

> 219.7 \*NURS CONVERSION NAME CHANGE

> Note: You already have the '\*NURS CONVERSION NAME CHANGE' File.

> If there is no Coordinator entered for the NURS-ADP mail group, the following will appear:

> Incoming Mail Groups:

> Enter the Coordinator for Mail Group 'NURS-ADP': LAST,FIRST

> Want to overwrite the package's file security codes? ?

> Answer NO if you do not want to change the file security codes. Answer YES to overwrite the package's file security codes with mine.

> Want to overwrite the package's file security codes? YES

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// \<RET\>

> Enter options you wish to mark as 'Out Of Order': \<RET\> Enter protocols you wish to mark as 'Out Of Order': \<RET\> Delay Install (Minutes): (0-60): 0// \<RET\>

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// Enter appropriate device

Installation Guide

> Install Started for NURSING SERVICE 4.0 :

> Feb 10, 1997@11:28:30

> Installing Routines:

> Feb 10, 1997@11:29:39

> Running Pre-Install Routine: ^NURXPRE Setting Nursing software switch to OFF-LINE

> Killing old data dictionary nodes that are no longer needed.

> Installing Data Dictionaries:

> Feb 10, 1997@11:30:47

> Installing Data: ..

> Feb 10, 1997@11:31

> Installing PACKAGE COMPONENTS:

> Installing HELP FRAME Installing PRINT TEMPLATE Installing SORT TEMPLATE Installing INPUT TEMPLATE Installing FORM Installing MAIL GROUP Installing OPTION

> Feb 10, 1997@11:32:40

> Running Post-Install Routine: ^NURXPST

> Reminder: Make certain the NURS-ADP mail group has at least one member. Setting Nursing file security...

> Before setting Nursing software back on-line, I need to update the NURS Patient file (#214) with any MAS patient movements that took place while this software was installed. At the programmers prompt please do the following:

> D MAS^NURXPST

> Updating Routine file...

> The following Routines were created during this install: NURAPA

> NURAPA1 NURAPA2 NURSPA NURSPA1 NURSPA2 NURSPA3 NURAPB

> Updating KIDS files...

> Installation Guide

> NURSING SERVICE 4.0 Installed.

> Feb 10, 1997@11:33:03..

> Install Message sent \#7923 Install Completed

Installation Guide

# Post Initialization Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  (Mandatory) Update the NURS Patient file (#214) with any PIMS patient movements which took place during the installation. To do this go into programmer mode and run the following code:

> D MAS^NURXPST

> This will also set the Nursing software back on-line. For example:

> \>D MAS^NURXPST

> Ward Deactivation and Patient entry for the following Nursing units(s): 15E

> 7W

> 4E

> ...

> ...

> Done ...

> Ward Activation and Patient entry for the following Nursing units(s): 15E

> 7W

> 4E

> ...

> ...

> Done ...

> Setting Nursing software switch back to ON-LINE.

2.  There are no security keys exported with the Nursing software.
3.  Review the scheduling of the following options:
    1.  (Mandatory) NURAAM-ACU (Nursing Acuity/Separation-Activation Run) should be tasked to run daily after midnight with no device selected.
    2.  (Mandatory) NURAMN-MANCK (Nursing Batch Job Status Check) should be scheduled to run at 0600 hrs., daily with no device selection.
    3.  (Optional) The NURAAM-UNCBAT (Batch Run of Unclassified AMIS 1106 Patients) option is an optional job which prints the unclassified AMIS 1106 patient list. To run this option manually, use the Unclassified AMIS 1106 Patients option under the Special Functions menu.

> Installation Guide

4.  (Optional) The NURAAM-MD-UNCBAT (Batch Run of Unclassified Midnight Patients) option is an optional job which prints the unclassified midnight patient list. To run this option manually, use the Unclassified Midnight Patients option under the Special Functions menu.
5.  (Optional) The NURAED-BATSEP-QUEUE (TaskManager Activation/ Separation Report) option is an optional job which prints daily position control changes on employees. The data for the reports (unclassified AMIS 1106 patients, unclassified midnight patient and position control changes) are generated by the Nursing Acuity/Separation-Activation Run (NURAAM-ACU) option. The NURAED-BATSEP- QUEUE option should be queued to run approximately two (2) hours after the NURAAM-ACU option is scheduled to ensure availability of the required data. To run this option manually, use the Employee Activation/Separation Report option under the Special Functions menu.
6.  (Optional) The NURAPR-RES-CURWKL-QUEUE (TaskManager Workload Statistic Report (Current)) option is an optional job which prints current workload statistics information. To run this option manually, use the Workload Statistics Report (Current) option under the Resource Management Reports menu.
4.  The following routines should be mapped on all CPUs using the PIMS system: NURSCPL, NURSAMSG, NURACE\*, NURSAPCH, NURSCUTL and NURSAWCK.
5.  The following globals should be journaled and appear in the UCI translation table for each CPU: NUR\*
6.  Move the NUR\* routines onto all appropriate systems, if applicable.
7.  For information on assigning menus, refer to page 1.14 in Chapter 1 Implementation and Maintenance of the Nursing User Manual.

Installation Guide

# File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 28%" />
<col style="width: 19%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>NUMBER</th>
<th>NAME</th>
<th></th>
<th>GLOBAL NAME</th>
<th>DD ACC</th>
<th>RD ACC</th>
<th>WR ACC</th>
<th>DEL ACC</th>
<th><blockquote>
<p>LAY ACC</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>210</td>
<td>NURS</td>
<td>STAFF</td>
<td>^NURSF(210,</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>211.1</td>
<td>NURS</td>
<td>PAY SCALE</td>
<td>^NURSF(211.1,</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>211.2</td>
<td colspan="2">*NURS GRADE/STEP</td>
<td>^NURSF(211.2,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>211.3</td>
<td colspan="2">NURS SERVICE POSITION</td>
<td>^NURSF(211.3,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>211.4</td>
<td colspan="2">NURS LOCATION</td>
<td>^NURSF(211.4,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>211.5</td>
<td colspan="2">NURS CLINICAL BACKGROUND</td>
<td>^NURSF(211.5,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>211.6</td>
<td colspan="2">NURS TOUR OF DUTY</td>
<td>^NURSF(211.6,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>211.7</td>
<td colspan="2">NURS AMIS POSITION</td>
<td>^NURSF(211.7,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>211.8</td>
<td colspan="2">NURS POSITION CONTROL</td>
<td>^NURSF(211.8,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>211.9</td>
<td colspan="2">NURS VACANCY/TRANSFERRED</td>
<td>^NURSF(211.9,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>212.1</td>
<td colspan="2">NURS EDUCATION</td>
<td>^NURSF(212.1,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>212.2</td>
<td colspan="2">NURS CERTIFICATION</td>
<td>^NURSF(212.2,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>212.3</td>
<td colspan="2">NURS COLLEGE MAJOR</td>
<td>^NURSF(212.3,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>212.4</td>
<td colspan="2">*NURS MANDATORY INSERVICE</td>
<td>^NURSF(212.4,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>212.42</td>
<td colspan="2">*NURS MI CLASS GROUP</td>
<td>^NURSF(212.42,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>212.6</td>
<td colspan="2">NURS PRIVILEGE</td>
<td>^NURSF(212.6,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>212.7</td>
<td colspan="2">NURS PRODUCT LINE</td>
<td>^NURSF(212.7,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>213.1</td>
<td colspan="2">*NURS AMIS 1106 CLASS</td>
<td>^NURSA(213.1,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>213.2</td>
<td colspan="2">NURS AMIS 1106B FTEE</td>
<td>^NURSA(213.2,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>213.3</td>
<td colspan="2">NURS AMIS WARD</td>
<td>^NURSF(213.3,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>213.4</td>
<td colspan="2">NURS AMIS 1106 MANHOURS</td>
<td>^NURSA(213.4,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>213.5</td>
<td colspan="2">NURS AMIS DAILY EXCEPTION</td>
<td>^NURSA(213.5,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>213.9</td>
<td colspan="2">NURS PARAMETERS</td>
<td>^DIC(213.9,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>214</td>
<td colspan="2"><blockquote>
<p>NURS PATIENT</p>
</blockquote></td>
<td>^NURSF(214,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>214.6</td>
<td colspan="2">NURS CLASSIFICATION</td>
<td>^NURSA(214.6,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>214.7</td>
<td colspan="2">NURS REVIEW CLASSIFICATIO</td>
<td>^NURSA(214.7,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>216.8</td>
<td colspan="2">NURS CARE PLAN</td>
<td>^NURSC(216.8,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>217</td>
<td colspan="2"><blockquote>
<p>NURQ QI SUMMARY</p>
</blockquote></td>
<td>^NURQ(217,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>217.1</td>
<td colspan="2">NURQ STANDARDS OF CARE/PRA</td>
<td>^NURQ(217.1,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>217.2</td>
<td colspan="2">NURQ RATIONALE</td>
<td>^NURQ(217.2,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>217.3</td>
<td colspan="2">NURQ FREQUENCY</td>
<td>^NURQ(217.3,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>219.7</td>
<td colspan="2">*NURS CONVERSION NAME CHA</td>
<td>^NURSF(219.7,</td>
<td>@</td>
<td colspan="2"><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Installation Guide