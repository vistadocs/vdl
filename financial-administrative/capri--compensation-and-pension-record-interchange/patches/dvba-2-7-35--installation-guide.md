---
title: DVBA*2.7*35 Server Side Modifications AMIE II/CAPRI Install Guide/Rel Notes
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Server Side Modifications AMIE II/CAPRI Install Guide/Rel Notes
app_code: CAPRI
app_name: Compensation and Pension Record Interchange
section: FIN
app_status: active
pkg_ns: DVBA
patch_ver: 2.7
patch_id: DVBA*2.7*35
group_key: "CAPRI:DVBA:2.7"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Connection with the RPC Broker](#connection-with-the-rpc-broker) ![](dvba-2-7-35-server-side-modifications-amie-ii-capri-install-guide-rel-notes/001.png)
audience: 
keywords: 
  - dvbab
  - summary
  - capri
  - report
  - health
  - install
  - dvba
  - installation
  - patch
  - limit
page_count: 0
word_count: 2550
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/dvba_27_35_igrn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/dvba_27_35_igrn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=133"
---

## Table of Contents

    - [Connection with the RPC Broker](#connection-with-the-rpc-broker)
![](dvba-2-7-35-server-side-modifications-amie-ii-capri-install-guide-rel-notes/001.png)

####### Automated Medical Information Exchange

(AMIE) V. 2.7

####### Server Side Modifications for

####### AMIE II/CAPRI

#### Installation Guide/Release Notes

######## Patch DVBA\*2.7\*35

######## June 2001

######### 

V*IST*A System Design & Development
Table of Contents

#### Installation Guide 1

I. Introduction 1
II\. Pre-Installation 1
> Server 1
> Client 1
III\. Installation Activities 2
> Server 2
> Sample Server Install 3
> Routine Checksums 5
> Connection with the RPC Broker 5
> Client 6
IV\. Post-Installation Activities 6
> User Access to CAPRI 6

#### Release Notes 7

I. User Release Notes 7
> CAPRI Overview 7
> CAPRI Health Summary 7
> Creating CAPRI Health Summary 8
> Adding CAPRI Health Summary to CPRS GUI for Display 10
> Purging C&P Exam Results 11
II\. Technical Release Notes 12
> Server Software Components 12
> Post Installs 12
> Menu Options 12
> Remote Procedures 12
Installation Guide

#### I. INTRODUCTION

This manual provides details on the preparation for, and installation of, Patch DVBA\*2.7\*35 (SERVER SIDE MODIFICATIONS FOR AMIE II/CAPRI GUI) software. The Compensation & Pension Record Interchange (CAPRI) Project is a One VA cooperative effort with objectives of creating, testing, and nationally implementing a graphical user interface to enhance the retrieval and dissemination of data from V*IST*A AMIE II menu options.
This installation is a virgin install. It will bring in the necessary (M)umps Remote Procedure Calls to support the CAPRI GUI /Client software.
This patch provides updates to the AMIE software only. There are no changes to any other V*IST*A applications.

#### II. PRE-INSTALLATION

#### Server

The following package versions (or higher) must be installed prior to loading the CAPRI server software.
<u>Application Name</u> <u>Minimum Version or Patch</u> <u>Checked for in build DVBA\*2.7\*35</u>
AMIE V2.7 Yes
CPRS V1.0 No
RPC Broker V1.1 No

#### Client

The CAPRI GUI/Client software will be distributed by VBA Hines to the appropriate VARO sites. The CAPRI GUI/Client software will not be distributed to local VHA field sites and does not require installation on the local V*IST*A workstation.
III. Installation Activities

#### Server

The V*IST*A server portion of the CAPRI application is distributed in a PackMan message through the National Patch Module. The KIDS build is DVBA\*2.7\*35.
- AMIE Users can be on the system and working during this installation.
- The installation of the server software takes less than 5 minutes.
1\) Send the PackMan patch message to the account in which you wish to install the build. Use the 'INSTALL/CHECK MESSAGE' option from the PackMan menu. This will load the PackMan KIDS build.
2\) From the Kernel Installation and Distribution System menu, select the installation menu.
3\) You may now elect to use the following options (when prompted for INSTALL NAME, enter DVBA\*2.7\*35).
a\) Backup a Transport Global – This option will create a backup message of any routines exported with the patch. It will NOT backup any changes such as DDs or templates.
> b\) Compare Transport Global to Current System – This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
> c\) Verify Checksums in Transport Global – This option will allow you to ensure the integrity of the routines that are in the transport global.
4\) Use the Install Package(s) option and select package DVBA\*2.7\*35.
5\) The install will ask if you wish to rebuild menu trees. It is recommended that you answer NO to this prompt. The trees will be rebuilt next time the system performs this task.
6\) When prompted 'Want KIDS to INHIBIT LOGONs' during the install? YES//', it is recommended that you answer NO.
7\) When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//', answer NO.
8\) At the 'Enter the Device you want to print the Install Messages’ prompt, you can direct output to your desired device.

#### *Sample Server Install*

KIDS Kernel Installation & Distribution System
Edits and Distribution ...
Utilities ...
Installation ...
Select Kernel Installation & Distribution System Option: INstallation
1 Load a Distribution
2 Verify Checksums in Transport Global
3 Print Transport Global
4 Compare Transport Global to Current System
5 Backup a Transport Global
6 Install Package(s)
Restart Install of Package(s)
Unload a Distribution
Select Installation Option: 6 Install Package(s)
Select INSTALL NAME: DVBA\*2.7\*35 Loaded from Distribution 4/9/01@16:21
=\> DVBA\*2.7\*35
This Distribution was loaded on Apr 09, 2001@16:21 with header of
DVBA\*2.7\*35
It consisted of the following Install(s):
DVBA\*2.7\*35
Checking Install for Package DVBA\*2.7\*35
Will first run the Environment Check Routine, DVBA35P
Install Questions for DVBA\*2.7\*35
Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO
Want KIDS to INHIBIT LOGONs during the install? YES// NO
Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO
Enter the Device you want to print the Install messages.
You can queue the install by enter a 'Q' at the device prompt.
Enter a '^' to abort the install.
DEVICE: HOME// \<RET\>
Install Started for DVBA\*2.7\*35 :
Apr 09, 2001@16:21
Build Distribution Date: Apr 09, 2001
Installing Routines:
Apr 09, 2001@16:21
Installing PACKAGE COMPONENTS:
Installing REMOTE PROCEDURE
Installing OPTION
DVBA\*2.7\*35
─────────────────────────────────────────────────────────────────────────────
Apr 09, 2001@16:21
Running Post-Install Routine: POST^DVBA35P
\>\> starting Post-installation for DVBA\*2.7\*35
2507 REQUEST FILE (#396.3) History retention updated to 365 days
\>\> Post-installation completed
Updating Routine file...
Updating KIDS files...
DVBA\*2.7\*35 Installed.
Apr 09, 2001@16:21
Install Message sent \#3468525
─────────────────────────────────────────────────────────────────────────────
┌────────────────────────────────────────────────────────────┐
100% │ 25 50 75 │
Complete └────────────────────────────────────────────────────────────┘
Install Completed

#### *Routine Checksums*

The following is a list of the routine(s) included in this patch. The second line of each of these routine(s) will look like:
\<tab\>;;2.7;AMIE;\*\*\[patch list\]\*\*;Apr 10, 1995
CHECK^XTSUMBLD results
Routine name Before Patch After Patch Patch List
============ ============ =========== ==========
DVBA35P N/A 7674345 35
DVBAB1 N/A 6540543 35
DVBAB2 N/A 11422836 35
DVBAB3 N/A 2390164 35
DVBAB4 N/A 9073986 35
DVBAB5 N/A 1762227 35
DVBAB51 N/A 14170056 35
DVBAB52 N/A 8119229 35
DVBAB53 N/A 11588177 35
DVBAB54 N/A 8601558 35
DVBAB56 N/A 11788450 35
DVBAB57 N/A 7035974 35
DVBAB58 N/A 4410506 35
DVBAB6 N/A 23090459 35
DVBAB67 N/A 12253136 35
DVBAB68 N/A 8303178 35
DVBAB70 N/A 21756045 35
DVBAB71 N/A 12765699 35
DVBAB9 N/A 10403184 35
DVBAB96 N/A 17420589 35
DVBAB97 N/A 5230871 35
DVBAB98 N/A 9679435 35
DVBAB99 N/A 8542026 35

### Connection with the RPC Broker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for the VBA to connect, each site will need to inform the CAPRI Project of the site's method of accessing the RPC Broker.
<span class="mark">REDACTED</span>
- Preferred method of accessing the RPC Broker at site (e.g., DNS entry or IP address)
- DNS entry
- IP address
- Port \# (normally 9200)
Client
The CAPRI GUI/Client software will be distributed by VBA Hines to the appropriate VARO sites. The CAPRI GUI/Client software will not be distributed to local VHA field sites and does not require installation on the local V*IST*A workstation.
IV.POST-Installation ActivitiesUser Access to CAPRI
CAPRI users without the @ sign and programmer access will have to be assigned an option context to use an option. The security aspect of CAPRI is that it looks for option context DVBA CAPRI GUI in the user's menu structure (part of a primary menu or on a secondary menu). So if the option is not assigned in some fashion, the user will get a message that they do not have access to CAPRI.
There are two ways to grant a user access to CAPRI.
- You can add CAPRI GUI Broker \[DVBA CAPRI GUI\] as an ITEM in the OPTION file on a user's assigned primary menu.
- You can place CAPRI GUI Broker \[DVBA CAPRI GUI\] on a user's individual secondary menu.
Release Notes

#### I. USER RELEASE NOTES

#### CAPRI Overview

Compensation & Pension Record Interchange (CAPRI) is a Graphic User Interface (GUI) for V*IST*A Automated Medical Information Exchange (AMIE II) menu options. The CAPRI Project is a One VA cooperative effort with objectives of creating, testing, and nationally implementing a graphical user interface to enhance the retrieval and dissemination of data from V*IST*A AMIE II menu options.

#### CAPRI Health Summary

Health Summaries are customized reports comprised of V*IST*A components specified by end users.
The St. Petersburg VARO, in cooperation with VISN 8, has developed a Health Summary type named VARO Rating. This name was specified by Rating Specialists to facilitate their work process. VBA prefers the name VARO Rating Health. However, the name is optional.
This Health Summary uses a number of nationally named components. The *Summary Order* is used to determine the order of display for each component. *Occurrence Limit* and *Time Limit* are used to set parameters for the amount of data displayed – i.e., either a maximum of the last 10 occurrences displayed or, if less than 10 occurrences, all occurrences over the last 5 years.
The response to the *Suppress Print of Components Without Data* prompt determines if the name of the component will be displayed when no data is found.
While the Health Summary is compiling (when run to the screen in both GUI and Roll & Scroll), the screen display will freeze until compiling is complete. Depending on the volume of data being retrieved, the screen display may freeze anywhere from 5 to 75 seconds.
Use of this Health Summary is determined by local policies.
*Creating CAPRI Health Summary*
From the Health Summary Enhanced Menu, select the Create/Modify Health Summary Type option \[GMTS TYPE ENTER/EDIT\].
Select Health Summary Type: VARO RATING
Are you adding 'VARO RATING' as a new HEALTH SUMMARY TYPE? No// YES
NAME: VARO RATING// \<RET\>
TITLE: VARO RATING
SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: NO
LOCK: \<RET\>
OWNER: {UserName}// \<RET\>*- This will be the name of the user building the report. Some users may not be able to edit this field.*
Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO
Select COMPONENT: DEM
SUMMARY ORDER: 5// \<RET\>
HEADER NAME: Demographics// \<RET\>
Select COMPONENT: RI (RADIOLOGY IMPRESSION)
SUMMARY ORDER: 10// \<RET\>
OCCURRENCE LIMIT: 10
TIME LIMIT: 5Y
HEADER NAME: Imaging Impression// \<RET\>
Select COMPONENT: CVF (MAS CLINIC VISITS FUTURE)
SUMMARY ORDER: 15// \<RET\>
HEADER NAME: Clinic Visits, Fut// \<RET\>
Select COMPONENT: CVP (MAS CLINIC VISITS PAST)
SUMMARY ORDER: 20// \<RET\>
OCCURRENCE LIMIT: 100
TIME LIMIT: 5Y
HEADER NAME: Clinic Visits, Past// \<RET\>
Select COMPONENT: ADC (ADMISSION/DISCHARGE)
SUMMARY ORDER: 25// \<RET\>
OCCURRENCE LIMIT: 100
TIME LIMIT: 5Y
HEADER NAME: Admission/Discharge// \<RET\>
Select COMPONENT: DCS (DISCHARGE SUMMARY)
SUMMARY ORDER: 30// \<RET\>
OCCURRENCE LIMIT: 20
TIME LIMIT: 5Y
HEADER NAME: Discharge Summary// \<RET\>
Select COMPONENT: PN (PROGRESS NOTES)
SUMMARY ORDER: 35// \<RET\>
OCCURRENCE LIMIT: 500
TIME LIMIT: 5Y
HEADER NAME: Progress Notes// \<RET\>
Select COMPONENT: SR (SURGERY REPORTS)
SUMMARY ORDER: 40// \<RET\>
OCCURRENCE LIMIT: 10
TIME LIMIT: 5Y
HEADER NAME: Surgery Rpt (OR/NON) Replace \<RET\>
Select COMPONENT: MEDF (MEDICINE FULL REPORT)
SUMMARY ORDER: 45// \<RET\>
OCCURRENCE LIMIT: 10
TIME LIMIT: 5Y
CPT MODIFIERS DISPLAYED: YES
HEADER NAME: Med Full Report// \<RET\>
Select COMPONENT: \<RET\>
Do you wish to review the Summary Type structure before continuing? NO// YES
Health Summary Type Inquiry
Type Name: VARO RATING
Title: VARO RATING
Owner: {User Name}
SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: NO
Max Hosp ICD Prov
Abb. Order Component Name Occ Time Loc Text Narr Selection
----------------------------------------------------------------------------------
DEM 5 Demographics
RI 10 Imaging Impression 10 5Y
CVF 15 Clinic Visits, Fut
CVP 20 Clinic Visits, Past 100 5Y
ADC 25 Admission/Discharge 100 5Y
DCS 30 Discharge Summary 20 5Y
PN 35 Progress Notes 500 5Y
SR 40 Surgery Rpt (OR/NON) 10 5Y
MEDF 45 Med Full Report 10 5Y
\* = Disabled Components
Select Component:
*Adding CAPRI Health Summary to CPRS GUI for Display*
The health summaries visible within CAPRI are now the same as in the CPRS GUI. At most hospitals, this listing is controlled by the Clinical Application Coordinator (CAC). The CAC, IRM, or person responsible for the GUI Health Summary setup will need to add the new VARO RATING summary to the CPRS Health Summary parameters in order for it to be used in CAPRI.
From the GUI Parameters Menu \[ORW PARAM GUI\], select the GUI Health Summary Types option \[ORW HEALTH SUMMARY TYPES\].
Allowable Health Summary Types may be set for the following:
2 User USR \[choose from NEW PERSON\]
4 System SYS \[VASITE.VA.GOV\]
Enter selection: 4 System VASITE.VA.GOV
*Whether the site will add the new health summary to the user or system level parameter is a local decision. By adding it at the system level, all users will be able to access the new health summary without needing to add it to each Regional Office user. This will require less set-up. If you choose to add it to each user, you will have to repeat this process for every user who needs to use the health summary.*
---- Setting Allowable Health Summary Types for System: VASITE.VA.GOV ---
Select Sequence: 200
*The sequence selected will determine where in the list the health summary appears. Most sites alphabetize their listing.*
Are you adding 200 as a new Sequence? Yes// YES
Sequence: 200// \<RET\>
Health Summary: VARO RATING
Select Sequence: \<RET\>Purging C&P Exam Results
Currently, Rating Specialists are not able to review C&P exam results that are older than 60-90 days, since the exam results are usually purged from the V*IST*A system within that time frame. Therefore, it is not possible for a Rating Specialist to use CAPRI to “mark” a C&P exam as “insufficient” that is older than 60-90 days.
The loading of patch DVBA\*2.7\*35 will set the number of days to keep C&P exam results to 365 days if this figure is currently less than 365 days. Should the number of days already be set to a higher number, no action will be taken. It will use the post-install routine of the patch to set the DAYS TO KEEP 2507 HISTORY field (#11) of the AMIE SITE PARAMETER file (#396.1) to a value of 365. The local V*IST*A site may modify the purge criteria based on local records processing and maintenance practice in accordance with VHA Patient Record Retention Regulations.  
II. TECHNICAL RELEASE NOTES

#### Server Software Components

This patch introduces the (M)umps server software to support V*IST*A patient data access by the CAPRI GUI/Client software and provides no new or enhanced functionality to the V*IST*A system. The technical components included in this patch are as follows.
- Post Installs
Routine: DVBA35P
The post-install will also update the value of the AMIE SITE PARAMETER (#396.1) file, DAYS TO KEEP 2507 HISTORY (#.11) field to ‘365’ days.
- Menu Options
The following menu option will be added.
Name: DVBA CAPRI GUI
Menu Text: CAPRI GUI (Broker)
Type: Broker (Client/Server)
Description: This is the ‘B’ type option used by the CAPRI GUI client application. It contains all the RPCs used by the CAPRI GUI application.
- Remote Procedures
The following Remote Procedure calls are exported with this patch.
DVBAB 2507 PENDING REPORT
Generates report based on status of 2507 requests.
DVBAB AMIS REPORT
Returns AMIS report for specified search criteria.
DVBAB APPOINTMENT LIST
Returns list of past, future, or all appointments.
DVBAB CHECK CREDENTIALS
Verifies user has been granted access to AMIE II/CAPRI.
DVBAB DATETIME
Returns the current date/time from V*IST*A.
DVBAB DIVISION
Returns division name.
DVBAB FIND EXAMS
Lists all of the patient's AMIE II C&P exam requests whether complete, new, or pending.
DVBAB HEALTH SUMMARY TEXT
Retrieves the report text for a report selected on the Report tab.
DVBAB INCREASE EXAM COUNT
Used to record the number of exams pending for a specified patient.
DVBAB INST LIST
Returns list of institutions.
DVBAB LABLIST
Returns a list of the site's laboratory test names.
DVBAB PENDING C&P REPORT
Generates a report containing the pending C&P exam requests.
DVBAB PTINQ
Returns a patient inquiry text report.
DVBAB REPORT 7131INQ
Returns a 7131 inquiry report.
DVBAB REPORT ADMINQ
Returns an admission inquiry report for the specified date range.
DVBAB REPORT ADMISSIONS
Generates an admission report for the specified date range.
DVBAB REPORT CHECKLIST
Generates an exam worksheet.
DVBAB REPORT CPDETAILS
Returns a detailed summary of a specific C&P request.
DVBAB REPORT DISCHARGE
Generates a discharge report.
DVBAB REPORT EXAM CHKLIST
Generates an exam worksheet.
DVBAB REPORT INCOMPVET
Generates an incompetent veteran report.
DVBAB REPORT LISTS
Returns a list of reports, Health Summary types, and date ranges that can be displayed at the workstation.
DVBAB REPORT PENDING7131
Generates a list of pending 7131 requests.
DVBAB REPORT READMIT
Generates a readmission report.
DVBAB SC VETERAN REPORT
Generates a service-connected veterans report.
DVBAB SEND MSG
Used to generate e-mail messages for specific CAPRI actions, such as changing a C&P exam request.
DVBAB VERSION
Used to ensure GUI and V*IST*A are on the same version of CAPRI.
