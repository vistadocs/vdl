---
title: Hospital Based Primary Care (former HBHC) Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: HBPC
app_name: Home Based Primary Care
section: CLI
app_status: active
pkg_ns: HBPC
patch_ver: 1
patch_id: HBPC*1
group_key: "HBPC:HBPC:1"
file_numbers: []
security_keys: []
menu_options: 0
description: This package was developed under Kernel 7, FileMan 19, MailMan 7, MAS 5.1, and references the NEW PERSON (200) file.
audience: 
keywords: 
  - hbhc
  - filed
  - edit
  - hbhcrp
  - package
  - clinic
  - fileman
  - visit
  - application
  - coordinator
page_count: 0
word_count: 1300
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 1993
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbhc_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbhc_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=68"
---

Decentralized Hospital Computer Program

HOSPITAL BASED HOME CAREINSTALLATION GUIDE

November 1993

Hines Information Systems Center

Chicago, Illinois

General Information

This package was developed under Kernel 7, FileMan 19, MailMan 7, MAS 5.1, and references the NEW PERSON (200) file.

Data Storage Requirements

Estimated data storage requirements using Hospital Based Home Care (HBHC) service at Little Rock Veterans Affairs Medical Center as an example:

File Name File Number Record/Bytes Records/Month

===============================================================

HBHC PATIENT 631 355 15 additions

(150 initially)

-----------------------------------------------------------------------------------------------------------------

HBHC REJECT/ 631.1 60 static

WITHDRAW REASON (10 initially)

-----------------------------------------------------------------------------------------------------------------

HBHC EXPRESSIVE 631.2 81 static

COMMUNICATION (6 initially)

-----------------------------------------------------------------------------------------------------------------

HBHC RECEPTIVE 631.3 91 static

COMMUNICATION (6 initially)

-----------------------------------------------------------------------------------------------------------------

HBHC PROVIDER 631.4 36 semi-static

(34 initially)

-----------------------------------------------------------------------------------------------------------------

HBHC TYPE OF 631.5 91 static

VISIT (7 initially)

-----------------------------------------------------------------------------------------------------------------

HBHC CLINIC 631.6 5 semi-static

(8 initially)

-----------------------------------------------------------------------------------------------------------------

HBHC PERIOD OF 631.7 32 static

SERVICE (11 initially)

-----------------------------------------------------------------------------------------------------------------

HBHC VALID 631.8 5 semi-static

STATE CODE

-----------------------------------------------------------------------------------------------------------------

HBHC SYSTEM 631.9 17 static

PARAMETERS (1 only)

-----------------------------------------------------------------------------------------------------------------

HBHC VISIT 632 147 800 additions

-----------------------------------------------------------------------------------------------------------------

File Name File Number Record/Bytes Records/Month

================================================================= HBHC TEAM 633 30 semi-static

(3 initially)

-----------------------------------------------------------------------------------------------------------------

HBHC TRANSMIT 634 125 800 per cycle

-----------------------------------------------------------------------------------------------------------------

HBHC EVALUATION/ 634.1 255 scratch

ADMISSION ERROR(S)

-----------------------------------------------------------------------------------------------------------------

HBHC VISIT ERROR(S) 634.2 255 scratch

-----------------------------------------------------------------------------------------------------------------

HBHC DISCHARGE 634.3 1235 scratch

ERROR(S)

-----------------------------------------------------------------------------------------------------------------

HBHC FORM 6 634.4 125 limited

CORRECTIONS

-----------------------------------------------------------------------------------------------------------------

Installation Instructions

Obtain a list of HBHC Clinics from the HBHC Application Coordinator using the Clinic Worksheet located at the back of this Installation Guide. Consult the Application Coordinator for the "Package Startup Date" and "Number of Visit Days to Scan" system parameter field entries desired. (Parameter explanations follow.)

<u>Package Startup Date System Parameter</u>

> **NOTE:** The Package Startup Date parameter is IMPORTANT.

Once entered, this date CANNOT be changed.

> The Package Startup Date is the "changeover" date for switching from paper visit logs being mailed, to "electronic transmission" of visit records to Austin. This is an either/or situation. Paper visit logs should not be mailed for data entry by Austin, if electronic transmission, of the same visit records, is to occur. This would duplicate the visit workload at Austin, since Austin has no duplicate record check available for visit information.

> Any visits prior to the Package Startup Date are automatically excluded from all transmissions. (e.g. Little Rock VAMC entered 6/1/92 as their Package Startup Date. All visit logs prior to 6/1/92 were mailed to Austin for data entry. All visits occurring AFTER 6/1/92 were entered in the HBHC database and electronically transmitted to Austin. No paper visit logs with dates after 6/1/92 were mailed to Austin.) Admission and Discharge records do not use this parameter.

<u>Number of Visit Days to Scan System Parameter</u>

> The Number of Visit Days to Scan parameter controls the number of days processed and automatically written to the HBHC Visit file by the Make Appointment option. This field may be edited as needed by the Application Coordinator.

> The smallest number of days that will be workable for HBHC data entry procedures should be entered. (e.g., If visit data is entered on a daily basis, enter 7. Enter 35 if visit data is only updated monthly.) 7 thru 365 are valid.

> This parameter also determines the date range of visits displayed for selection by the Visit Data Entry option.

> <u>Station Number System Parameter</u>

> The Station Number System Parameter holds your hospital site number as listed in File \#4 (Institution), and will be referenced when obtaining the

> station name for headings of the various HBHC reports.

• Ensure the Q-HBH domain and any relay domains are not closed when installing to the production account, and are closed when installing to a test account.

• Load the HBHC\* routines from the distribution tape into the account where you wish the routines to reside. Initially loading into a test account and then finally into the production account is recommended.

• Place the ^HBHC global using the appropriate system utility. The ^HBHC global should be journaled and backed up.

• D ^HBHCINIT (The INIT should take less than 5 minutes.)

This version (#1) of "HBHCINIT" was created on 06-JAN-1993

(at LITTLE ROCK VAMC, by VA FileMan V.19)

I AM GOING TO SET UP THE FOLLOWING FILES:

631 HBHC PATIENT

631.1 HBHC REJECT/WITHDRAW REASON (including data)

I will OVERWRITE your data with mine.

631.2 HBHC EXPRESSIVE COMMUNICATION (including data)

I will OVERWRITE your data with mine.

631.3 HBHC RECEPTIVE COMMUNICATION (including data)

I will OVERWRITE your data with mine.

631.4 HBHC PROVIDER

631.5 HBHC TYPE OF VISIT (including data)

I will OVERWRITE your data with mine.

631.6 HBHC CLINIC

631.7 HBHC PERIOD OF SERVICE (including data)

I will OVERWRITE your data with mine.

631.8 HBHC VALID STATE CODE

631.9 HBHC SYSTEM PARAMETERS (including data)

I will MERGE your data with mine.

632 HBHC VISIT

633 HBHC TEAM

634 HBHC TRANSMIT

634.1 HBHC EVALUATION/ADMISSION ERROR(S)

634.2 HBHC VISIT ERROR(S)

634.3 HBHC DISCHARGE ERROR(S)

634.4 HBHC FORM 6 CORRECTIONS

> **NOTE:** This package also contains INPUT TEMPLATES

> **NOTE:** This package also contains SECURITY KEYS

> **NOTE:** This package also contains OPTIONS

ARE YOU SURE EVERYTHING'S OK? Y (YES)

...HMMM, LET ME PUT YOU ON "HOLD" FOR A SECOND............

"HBHC APPOINTMENT" Option Filed

"HBHC CANCEL APPOINTMENT" Option Filed

"HBHC EDIT CLINIC (631.6)" Option Filed

"HBHC EDIT HBHC TEAM (633)" Option Filed

"HBHC EDIT PROVIDER (631.4)" Option Filed

"HBHC EDIT SYSTEM PARAMETERS" Option Filed

"HBHC INFORMATION SYSTEM MENU" Option Filed

"HBHC MANAGER MENU" Option Filed

"HBHC REPORTS MENU" Option Filed

"HBHC TRANSMISSION MENU" Option Filed

"HBHC VISIT" Option Filed

"HBHCADM" Option Filed

"HBHCDIS" Option Filed

"HBHCFILE" Option Filed

"HBHCRP1" Option Filed

"HBHCRP10" Option Filed

"HBHCRP11" Option Filed

"HBHCRP12" Option Filed

"HBHCRP13" Option Filed

"HBHCRP2" Option Filed

"HBHCRP3" Option Filed

"HBHCRP4" Option Filed

"HBHCRP5" Option Filed

"HBHCRP6" Option Filed

"HBHCRP7" Option Filed

"HBHCRP8" Option Filed

"HBHCRP9" Option Filed

"HBHCRXMT" Option Filed

"HBHCUPD" Option Filed

"HBHCXMT" Option Filed

OK, I'M DONE.

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

• Once the INIT has been run, use FileMan to enter HBHC System Parameters as follows:

> **NOTE:** Field entries should be supplied by the HBHC Application Coordinator

\>D P^DI

VA FileMan 19.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 631.9 HBHC SYSTEM PARAMETERS

(1 entry)

EDIT WHICH FIELD: ALL// 2 PACKAGE STARTUP DATE

THEN EDIT FIELD: 3 NUMBER OF VISIT DAYS TO SCAN

THEN EDIT FIELD; 4 STATION NUMBER

THEN EDIT FIELD: \<RET\>

> Select HBHC SYSTEM PARAMETERS PACKAGE NAME: HOSPITAL BASED HOME CARE

> PACKAGE STARTUP DATE: mm/dd/yy

> NUMBER OF VISIT DAYS TO SCAN: 30// enter AC supplied number

> HOSPITAL NUMBER: Enter your site \#

> Select HBHC SYSTEM PARAMETERS PACKAGE NAME: \<RET\>

• This package transmits data to Austin. Verify that patch number XM\*DBA\*9 has been installed. This patch sets up the Q-HBH domain used by the HBHC package for transmission purposes. (This domain was originally entered for use by the Generic Code Sheet package, but has been authorized for use by this HBHC package.)

> **NOTE:** The Q-HBH domain and any relay domains for FOC-AUSTIN should be CLOSED on the test account to prevent transmission to Austin from the test account. Use FileMan as follows to close a domain:

\>D P^DI

VA FileMan 19.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 4.2 DOMAIN

EDIT WHICH FIELD: ALL// 1 FLAGS

THEN EDIT FIELD: \<RET\>

> Select DOMAIN NAME: Q-HBH

> ARE YOU ADDING "Q-HBH" AS A NEW DOMAIN (THE 261ST)? Y (YES)

> FLAGS: C

Repeat for all domains necessary.

• Again, ensure the domains are NOT closed when HBHC is installed in the production account.

• If Mail Group "HBH" exists, verify it is a "public" type mail group, the application coordinator is a member, and there are "No Authorized Senders". (This group is used to receive Austin transmission confirmation messages.) If "HBH" does not exist, use FileMan to create the mail group as follows:

\>D P^DI

VA FileMan 19.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 3.8 MAIL GROUP

EDIT WHICH FIELD: ALL// .01 NAME

THEN EDIT FIELD: 2 MEMBER (multiple)

EDIT WHICH MEMBER SUB-FIELD: ALL// \<RET\>

THEN EDIT FIELD: 4 TYPE

THEN EDIT FIELD: \<RET\>

Select MAIL GROUP NAME: HBH

ARE YOU ADDING "HBH" AS A NEW MAIL GROUP (THE nnTH)? Y

(YES)

Select MEMBER: Application Coordinator's name

Select MEMBER: \<RET\>

TYPE: PU public

Select MAIL GROUP NAME: \<RET\>

• The HBHC Application Coordinator should also supply a list of states that are to be included in their HBHC program to IRM. This list will then be used to populate the HBHC Valid State Code file (631.8). This may be accomplished using FileMan as follows:

\>D P^DI

VA FileMan 19.0

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 631.8 HBHC VALID STATE CODE

Select HBHC VALID STATE CODE NUMBER: MICHIGAN

ARE YOU ADDING "MICHIGAN" AS A NEW HBHC VALID STATE CODE (THE 1ST)? Y (YES)

Select HBHC VALID STATE CODE NUMBER: \<RET\>

Repeat for as many states as are listed by the Application Coordinator

(normally one to four states would be entered here).

• The HBHC Application Coordinator should supply a list of HBHC clinic names used by HBHC since all clinics referenced by the package must exist in the HOSPITAL LOCATION (#44) file. (See Clinic Worksheet located at the back of this guide.) Consult with the MAS Application Coordinator to determine if the HBHC clinics have prohibited access due to "YES" in the "PROHIBIT ACCESS TO CLINIC" (#2500) field. If "YES", then all HBHC package user names must be added to the "Privileged User" multiple (field \#2501) in the Hospital Location file for the HBHC clinics using FileMan as follows:

\>D P^DI

VA FileMan 19.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 44 HOSPITAL LOCATION

EDIT WHICH FIELD: ALL// 2501 PRIVILEGED USER (multiple)

EDIT WHICH PRIVILEGED USER SUB-FIELD: ALL// \<RET\>

THEN EDIT FIELD: \<RET\>

Select HOSPITAL LOCATION: enter HBHC clinic name

Select PRIVILEGED USER: enter HBHC user name(s)

Select PRIVILEGED USER: \<RET\>

Repeat for all HBHC clinics listed on worksheet.

• Assign File Access

> All HBHC files are exported with FileMan security codes set to "@" for Data Dictionary, Read, Write, Delete, LAYGO, & Audit file access. (See HBHC Package Security Guide if additional information is desired.)

> If Part 3 of the Kernel has been run at your site, the following example is a suggestion of how the file access should be allocated utilizing the accessible File (#32) field in the NEW PERSON (#200) file. If Kernel Part 3 has not been implemented at your site, each of the files listed below would need the FileMan security code changed from "@" to an appropriate code for the HBHC service. Each service will need to determine the proper access level for their users.

> Data Dictionary and Audit access are reserved for the IRM staff. Delete access should NOT be allowed on any HBHC files since these files point to or are referenced by other files. Read and/or Write access is granted by virtue of the menu options that reference each file. The Read/Write access suggested as follows allows the Application Coordinator to access the HBHC files via FileMan for creating other reports as desired, provided FileMan report generation is allowed by IRM.

File

File Name Number LAYGO Read Write

========================================================

HBHC PATIENT 631 \| AC \* \| AC \| AC \|

-------------------------------------------------------

\| User \| \| \|

----------------------------------------------------------------------------------------------------

HBHC PROVIDER 631.4 \| AC \| AC \| AC \|

----------------------------------------------------------------------------------------------------

HBHC CLINIC 631.6 \| AC \| AC \| AC \|

----------------------------------------------------------------------------------------------------

HBHC VISIT 632 \| \| AC \| AC \|

----------------------------------------------------------------------------------------------------

HBHC TEAM 633 \| AC \| AC \| AC \|

----------------------------------------------------------------------------------------------------

\* application coordinator

• Assign the "HBHC Information System Menu" option to the desired user(s).

• Assign the following security keys to the desired user(s):

HBHC TRANSMIT

This key locks the HBHC Transmission Menu option and should be assigned to users responsible for data transmission to Austin and the Application Coordinator.

HBHC MANAGER

This key locks the HBHC Manager Menu option and should be assigned to the Application Coordinator.

• Delete HBHCI\* routines (Optional, but recommended).

Package Startup

> **NOTE:** This portion of the package setup may be completed by the HBHC Application Coordinator.

• Populate the following files using the options located on the HBHC Manager Menu:

> (Since this is a new package, you may also be a new application coordinator not well versed in using FileMan or DHCP functionality. The following options simply prompt you for the information needed to populate the files. Enter one or more question marks at any field prompt to access on-line help concerning the type of data allowed in each field.)

• *Team File \#633 Data Entry*

> Data should be entered into this file first, since the HBHC PROVIDER File references it. This file contains 1 field, Team Name. Use the format desired for the Team Census Report (e.g., mixed case, all uppercase).

• *Provider File \#631.4 Data Entry*

> This file contains the following fields: Provider Number (this is the HBHC provider number), Provider Name, Degree, Grade/Step, FTEE on HBHC, and HBHC Team.

> Once the Provider file is complete, run the HBHC PROVIDER File Report option to check for data entry accuracy.

• *Clinic File \#631.6 Data Entry*

> This file contains 1 field, HBHC Clinic Name. These clinics must exist in the HOSPITAL LOCATION (#44) file. All clinics listed on the clinic worksheet should be included.

• The package is now ready for use.

Clinic Worksheet

> **NOTE:** All HBHC Clinics used by the HBHC service for scheduling appointments using the MAS Make Appointment \[SDM\] scheduling option capability should be included.

Clinic Name

===============================================================

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------

-----------------------------------------------------------------