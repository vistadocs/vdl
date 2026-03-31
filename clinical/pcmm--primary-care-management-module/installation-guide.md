---
consolidated_title: "pcmm install guide/release notes"
app_code: PCMM
doc_type: IG
master_source: "SD*5.3*177 PCMM Install Guide/Release Notes"
master_pub_date: September 1999
consolidated_from: 2 versions
prior_versions:
  - "SD*5.3*148 PCMM Install Guide/Release Notes"
---

![](sd-5-3-177-pcmm-install-guide-release-notes/001.png)

Scheduling V. 5.3Primary Care Management Module(PCMM)Installation Guide/Release Notes

Patch SD\*5.3\*177

September 1999

V*IST*A Technical Services

Table of Contents

Installation Guide 1

I. Introduction 1

II Pre Installation 1

> Server 1

> HL7 Incoming and Outgoing Filers 2

> Client 2

III\. Installation Activities 3

> Server 3

> A. Installation Steps 3

> B. Sever Installation Notes 5

> C. Sample of Server Installation 5

> D. Routine Checksums 9

> Client 11

> Client Installation Notes 12

IV\. Installation of the PCMM Client Software 13

Release Notes 19

User Release Notes 19

> I. GUI Side 19

> A. PC Attending Assignments 19

> B. Preceptor Assignment 20

> C. Messages 20

> D. Patient Team Position Assignment Screen 20

> E. Team Patient Listings Report 21

> II\. Server Side 21

Technical Release Notes 23

> I. V*IST*A Client Changes 23

> A. Mail Messages 23

> B. Kernel Security 23

> II\. V*IST*A Server Changes 23

> A. Data Dictionary Changes 23

> B. Mail Groups 24

> C. New Options 24

> D. “B”-Type Options 25

> E. APIs 25

> F. HL7 25

> G. List Template 26

> H. Associated Patches 26

Installation Guide

I. Introduction

This manual provides details on the preparation for and installation of Patch SD\*5.3\*177 to the PCMM software. It includes instructions on the installation of both the Client software and the Server software.

If PCMM has not been installed at your site, you must start with Scheduling Patch SD\*5.3\*41 and load all subsequent patches prior to loading SD\*5.3\*177. Patch SD\*5.3\*177 is not a virgin install patch.

This patch provides updates to the Scheduling and Registration software. There are no changes to any other V*IST*A applications.

II. Pre Installation*Server*

The following package versions (or higher) must be installed prior to loading the PCMM software. Since this patch is to existing PIMS software, all preceding PIMS patches should be installed.

|                      |                              |                                       |
|----------------------|------------------------------|---------------------------------------|
| Application Name | Minimum Version or Patch | Checked for in Build SD\*5.3\*177 |
| PIMS                 | SD\*5.3\*148                 | YES                                   |
| PIMS                 | SD\*5.3\*157                 | YES                                   |
| PIMS                 | SD\*5.3\*169                 | YES                                   |
| PIMS                 | SD\*5.3\*41                  | YES                                   |
| PIMS                 | SD\*5.3\*144                 | YES                                   |
| PIMS                 | SD\*5.3\*149                 | YES                                   |
| PIMS                 | SD\*5.3\*171                 | YES                                   |
| PIMS                 | SD\*5.3\*195                 | YES                                   |
| MailMan              | XMB\*999\*125                | YES                                   |
| FileMan              | FM\*22.0                     | YES                                   |

  
*HL7 Incoming and Outgoing Filers*

The PCMM software uses HL7 messages to communicate with the National Patient Care Database (NPCDB). In order for the HL7 messages to be transmitted, at least one HL7 incoming filer and one HL7 outgoing filer must be running. The option Monitor incoming & outgoing filers \[HL FILER MONITOR\] should be used to verify that the HL7 incoming and outgoing filers are running. Information about this option and the HL7 incoming and outgoing filers can be obtained from the V*IST*A HL7 V. 1.6 User Manual.

*Client*

The workstation must have one of the following operating systems.

- MS Windows 95B or higher
- MS Windows NT Workstation V. 3.51

Each workstation should be networked into your V*IST*A Server through a local area network. The RPC Broker’s RPC Broker Test should have successfully run on each client workstation.

III. Installation Activities*Server*

Installation of the server build will affect the running of ALL previous client versions of PCMM. All previous client versions of PCMM should not function.

Several changes in this patch effect Scheduling and Registration routines. As a result it is highly recommended that this patch be loaded after hours when there are no Scheduling or Registration users on the system. The installation of the server software takes less than 5 minutes.

A. Installation Steps1. The KIDs build is distributed in a host file, SD_53_177.KID, which must be obtained from an appropriate CIOFO FTP site. When transporting the KIDS file from the FTP site, be sure to set the type as ASCII.
2. Place the host file into a directory that is accessible from the account into which you are installing.
3. Review your mapped set. If any of the routines listed in the Routine Summary section of this guide are mapped, they should be removed from the mapped set at this time.
4. From the Kernel Installation and Distribution System menu, select the Installation Menu.
5. Select LOAD A DISTRIBUTION. When prompted for a host file name, enter SD_53_177.KID. This will load the distribution onto your system.
6. You may now elect to use the following options (when prompted for INSTALL NAME, enter SD\*5.3\*177).

> a. Backup a Transport Global – This option will create a backup message of any routines exported with the patch. It will NOT backup any changes such as DDs or templates.

> b. Compare Transport Global to Current System – This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> c. Verify Checksums in Transport Global – This option will allow you to ensure the integrity of the routines that are in the transport global.

7. Use the Install Package(s) option and select package SD\*5.3\*177.
8. This build will bring in two new mail groups, PCMM AUSTIN REPORTS and PCMM HL7 MESSAGES. You will be asked for a coordinator. Enter the name of the person responsible for PCMM.
9. The install will ask if you wish to rebuild menu trees. It is recommended that you answer NO to this prompt. The trees will be rebuilt next time the system does this task.
10. When prompted “Want KIDS to INHIBIT LOGONs during the install? YES//”, it is recommended you answer NO. The disabling of the Scheduling and Registration options will protect the installation.
11. When prompted to select the options you would like to place out of order, enter the following.

> SDAPP Appointment Menu

> SDMGR Scheduling Manager’s Menu

> SDNEXT Find next Available Appointment

> SDOUTPUT Outputs

> SDSUP Supervisor Menu

> SDM Make Appointment

> SDAM APPT MGT Appointment Management

> SDPATIENT Patient Profile MAS

> SC PCMM GUI WORKSTATION PCMM GUI Workstation

> SC PCMM PT LIST W/TEAM ASSIGN Patient Listing for Team Assignments

> SC PCMM PRACT PATIENTS Practitioner's Patients

> SC PCMM REPORTS MENU PCMM Reports

> DG LOAD PATIENT DATA Load/Edit Patient Data

12. If routines were unmapped as part of Step 2, they should be returned to the mapped set once the installation has run to completion. Consider mapping the following routines: SCAP\* SCUTBK\* SCMCT\*.
13. Ensure the AutoStart field (#4.5) in the HL Logical Link file (#870) for entry PCMM is set to ENABLED.
14. Schedule PCMM’s HL7 transmission builder.

> a. From the TaskMan Management Menu, select the *Schedule/Unschedule Options* option.

> b. At the “Select OPTION to schedule or reschedule: ” prompt, enter *SCMC PCMM HL7 TRANSMIT*.

> c. At the “Are you adding SCMC PCMM HL7 TRANSMIT as a new OPTION SCHEDULING ? ” prompt, enter *YES*.

> d. In the ScreenMan form, enter *T+1@01:00* into the QUEUED TO RUN AT WHAT TIME field and *1D* into the RESCHEDULING FREQUENCY field.

> e. Save changes and exit the form.

15. Start PCMM’s HL7 Lower Level Protocol (LLP).

> a. From the HL7 Main Menu, select the *V1.6 OPTIONS* menu.

> b. From this menu, select the *Communications Server* menu.

> c. From this menu, select the *Start LLP* option.

> d. At the “Select HL LOGICAL LINK NODE: ” prompt, enter *PCMM*.

> e. Accept the default response at the “Method for running the receiver: B// ” prompt.

B. Server Installation Notes

Installation of the new HL7 Protocol will cause the following verbiage to appear during the install. “Not a known package or a local namespace.” This is because these are new protocols. Everything will be installed ok.

Sites that have not yet installed XU\*8.0\*124 will see the following error message in the KIDS dialog relating to the import of data into Files 403.43 and 403.44. This error message is extraneous and does not impact the build. Installation of XU\*8.0\*124 is recommended but not necessary.

“\*\*ERROR IN DATA DICTIONARY FOR FILE \# XXX.XX\*\*”

The KIDS build will import changes to the List Template SDAM APPT MGT. This will overwrite any modifications your site may have made.

C. Sample of Server Installation

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: SD\*5.3\*177 Loaded from Distribution 9/9/99@12:59:36

=\> PCMM BUILD ;Created on Sep 08, 1999@13:56:40

This Distribution was loaded on Sep 09, 1999@12:59:36 with header of

PCMM BUILD ;Created on Sep 08, 1999@13:56:40

It consisted of the following Install(s):

SD\*5.3\*177 DG\*5.3\*239

Checking Install for Package SD\*5.3\*177

Will first run the Environment Check Routine, SD53P177

Install Questions for SD\*5.3\*177

Incoming Files:

403.43 SCHEDULING EVENT (including data)

> **NOTE:** You already have the 'SCHEDULING EVENT' File.

I will OVERWRITE your data with mine.

403.44 SCHEDULING REASON (including data)

> **NOTE:** You already have the 'SCHEDULING REASON' File.

I will OVERWRITE your data with mine.

404.41 OUTPATIENT PROFILE (Partial Definition)

> **NOTE:** You already have the 'OUTPATIENT PROFILE' File.

404.43 PATIENT TEAM POSITION ASSIGNMENT

> **NOTE:** You already have the 'PATIENT TEAM POSITION ASSIGNMENT' File.

404.44 PCMM PARAMETER (including data)

> **NOTE:** You already have the 'PCMM PARAMETER' File.

I will OVERWRITE your data with mine.

404.45 PCMM SERVER PATCH (including data)

> **NOTE:** You already have the 'PCMM SERVER PATCH' File.

I will OVERWRITE your data with mine.

404.46 PCMM CLIENT PATCH (including data)

> **NOTE:** You already have the 'PCMM CLIENT PATCH' File.

I will OVERWRITE your data with mine.

404.48 PCMM HL7 EVENT

> **NOTE:** You already have the 'PCMM HL7 EVENT' File.

404.49 PCMM HL7 ID

> **NOTE:** You already have the 'PCMM HL7 ID' File.

404.52 POSITION ASSIGNMENT HISTORY (Partial Definition)

> **NOTE:** You already have the 'POSITION ASSIGNMENT HISTORY' File.

404.53 PRECEPTOR ASSIGNMENT HISTORY

> **NOTE:** You already have the 'PRECEPTOR ASSIGNMENT HISTORY' File.

404.57 TEAM POSITION

> **NOTE:** You already have the 'TEAM POSITION' File.

409.92 ACRP REPORT TEMPLATE PARAMETER (including data)

> **NOTE:** You already have the 'ACRP REPORT TEMPLATE PARAMETER' File.

I will OVERWRITE your data with mine.

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'PCMM AUSTIN REPORTS': SMITH, RICK

COMPUTER SPECIALIST

Enter the Coordinator for Mail Group 'PCMM HL7 MESSAGES': SMITH, RICK

COMPUTER SPECIALIST

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Checking Install for Package DG\*5.3\*239

Install Questions for DG\*5.3\*239

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

Enter options you wish to mark as 'Out Of Order': SDAPP

Enter options you wish to mark as 'Out Of Order': SDMGR

Enter options you wish to mark as 'Out Of Order': SDNEXT

Enter options you wish to mark as 'Out Of Order': SDOUTPUT

Enter options you wish to mark as 'Out Of Order': SDSUP

Enter options you wish to mark as 'Out Of Order': SDM

Enter options you wish to mark as 'Out Of Order': SDAM APPT MGT

Enter options you wish to mark as 'Out Of Order': SDPATIENT

Enter options you wish to mark as 'Out Of Order': SC PCMM GUI WORKSTATION

Enter options you wish to mark as 'Out Of Order': SC PCMM PST W/TEAM ASSIGN

Enter options you wish to mark as 'Out Of Order': SC PCMM PRACT PATIENTS Enter options you wish to mark as 'Out Of Order': SC PCMM REPORTS MENU Enter options you wish to mark as 'Out Of Order': DG LOAD PATIENT DATA

Enter protocols you wish to mark as 'Out Of Order':

Delay Install (Minutes): (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// UCX/TELNET

Install Started for SD\*5.3\*177 : Sep 09, 1999@13:03:32

Build Distribution Date: Sep 08, 1999

Installing Routines: Sep 09, 1999@13:03:48

Running Pre-Install Routine: PRE^SD53P177

Deleting file \#409.92 entries...

Installing Data Dictionaries:

\*\* ERROR IN DATA DICTIONARY FOR FILE \# 403.43 \*\*

Data Dictionary not installed; FIA node is set to "No DD Update"

\*\* ERROR IN DATA DICTIONARY FOR FILE \# 403.44 \*\*

Data Dictionary not installed; FIA node is set to "No DD Update"

Sep 09, 1999@13:04:03

Installing Data: Sep 09, 1999@13:04:07

Installing PACKAGE COMPONENTS:

Installing MAIL GROUP

Installing HL LOWER LEVEL PROTOCOL PARAMETER

Installing HL LOGICAL LINK

Installing HL7 APPLICATION PARAMETER

Installing PROTOCOL

Installing REMOTE PROCEDURE

Installing LIST TEMPLATE

Installing OPTION Sep 09, 1999@13:04:35

Running Post-Install Routine: POST^SD53P177

Move current preceptor assignments to Preceptor History file

Sep 09, 1999@13:04:35 (by: 0)

------------------------------------------------------------

: Queued - Task# 141716

Reindexing of file 404.43 queued.

Generating mail message with PCMM Inconsistency Report totals.

Editing menu text values for GUI report selection...

Updating Routine file...

Updating KIDS files...

SD\*5.3\*177 Installed. Sep 09, 1999@13:04:45

DG\*5.3\*239

─────────────────────────────────────────────────────────────────────────────

Install Started for DG\*5.3\*239 :

Sep 09, 1999@13:04:45

Build Distribution Date: Sep 08, 1999

Installing Routines: Sep 09, 1999@13:04:46

Updating Routine file...

Updating KIDS files...

DG\*5.3\*239 Installed. Sep 09, 1999@13:04:47

Install Completed

D. Routine Checksums

The following is a list of the routine(s) included in this patch. The second line of each of these routine(s) will look like:

\<tab\>;;5.3;Scheduling;\*\*\[patch list\]\*\*;AUG 13, 1993

CHECK^XTSUMBLD results

Routine name Before Patch After Patch Patch List

============ ============ =========== ==========

SCAPMC 6857758 7956411 41,177

SCAPMC21 5281594 5142284 41,148,177

SCAPMC24 3741743 3977217 41,148,177

SCAPMC25 4477025 5524623 41,177

SCAPMC3 2653336 2770454 41,177

SCAPMC33 N/A 3527086 177

SCAPMC34 N/A 3511312 177

SCAPMC8 4379039 5350655 41,177

SCAPMC8A N/A 2365501 177

SCAPMC8C N/A 4362775 177

SCAPMC8P N/A 4281646 177

SCAPMCA N/A 1947176 177

SCAPMCA1 N/A 6363899 177

SCAPMCU1 6781359 8220234 41,45,48,177

SCAPMCU2 7201711 8613214 41,177

SCAPMCU3 3394109 4970759 41,45,177

SCAPMCU5 N/A 3360719 177

SCMCBK 7408285 6802845 41,51,148,157,177

SCMCBK5 2325438 2432956 148,177

SCMCBK6 1555967 1832960 148,177

SCMCBK7 3399449 3338017 148,177

SCMCBK8 4278210 4560566 148,177

SCMCCV3 6497864 6492408 195,177

SCMCDD 12778341 12827432 41,51,177

SCMCGU 1204651 1372019 195,177

SCMCHL N/A 3499315 177

SCMCHLB N/A 2682646 177

SCMCHLB1 N/A 3642671 177

SCMCHLB2 N/A 2546291 177

SCMCHLE N/A 1655433 177

SCMCHLG N/A 2380461 177

SCMCHLM N/A 2193938 177

SCMCHLR N/A 4489109 177

SCMCHLS N/A 1380175 177

SCMCHLX N/A 1291785 177

SCMCHLX1 N/A 2276272 177

SCMCHLZ N/A 2120667 177

SCMCLK N/A 6643624 177

SCMCMM 1318327 1545875 41,177

SCMCMU2 13709944 13709948 148,177

SCMCQK 6083157 6148118 148,177

SCMCQK1 12166811 12130808 148,177

SCMCTMM 9675406 9780103 41,45,87,100,130

177

SCMCTPU4 6696171 6605851 148,177

SCMCU1 819873 812453 41,177

SCMCUT N/A 3869854 177

SCRPBK1 4907035 4999190 41,177

SCRPEC 4888747 4951439 41,140,174,177

SCRPEC2 6683293 7757888 41,140,174,177

SCRPEC3 4007435 5091953 41,48,52,177

SCRPITP 4144858 4771270 41,52,177

SCRPITP2 5337807 6519044 41,177

SCRPMPSP 10947655 11004913 148,157,169,177

SCRPO N/A 9013648 177

SCRPO1 N/A 15269249 177

SCRPO2 N/A 14407873 177

SCRPO3 N/A 14691019 177

SCRPO4 N/A 7296135 177

SCRPO5 N/A 7236817 177

SCRPO6 N/A 12525471 177

SCRPO7 N/A 11997428 177

SCRPPAT 6947612 10278931 41,52,177

SCRPPAT2 8172506 8798204 41,48,174,181,177

SCRPPAT3 7317322 8025045 41,52,148,174,181

177

SCRPRAC 3717903 2883175 41,52,177

SCRPRAC2 3626396 5994526 41,177

SCRPSLT 4875040 5540131 41,52,177

SCRPSLT2 4889295 7870988 41,174,177

SCRPTA 6873963 6144666 41,48,52,114,174

181,177

SCRPTA2 6451681 7729402 41,88,140,148,174

181,177

SCRPTM 6336968 7188793 41,48,52,181,177

SCRPTM2 5183085 6472376 41,140,177

SCRPTP 5920383 6478803 41,48,174,177

SCRPTP2 7016274 7531793 41,53,52,174,177

SCRPTP3 6390783 6767820 41,48,98,177

SCRPU3 5800911 5974611 41,45,52,140,181

177

SCRPU4 1228733 189028 41,177

SCRPV1 N/A 6104082 177

SCRPV1A N/A 8820855 177

SCRPV1B N/A 7490878 177

SCRPV1B1 N/A 12907171 177

SCRPW25 27373533 28714128 144,177

SCUTBK11 6362605 7036633 41,54,86,148,177

SCUTBK3 2029958 3151906 41,51,177

SD53P177 N/A 4464040 177

SDAL 7212199 7641091 37,46,106,171,177

SDAL0 14046778 14119646 28,37,106,149,171

177

SDAM 3465080 3995198 149,177

SDPPALL 6524499 5759518 6,41,177

SDPPTEM 6500287 8547137 41,177

SDUTL3 1449734 1664797 30,39,41,148,177

*Client*

The installation of the client software should take less than 5 minutes per workstation. The following steps must be taken for each PCMM workstation.

1. Download the SD_53_177.EXE file from an appropriate CIOFO FTP site.

> a. Make sure to set transfer as BINARY.

> b. Get the SD_53_177.EXE;1 file. Depending on the FTP software, this file might be placed in C:\WINDOWS, C:\\ or some other directory. If you cannot find it, use Window’s File Manager’s Search functionality.

> c. VMS requires the “;1” extension on this file. It is necessary to rename the file to SD_53_177.EXE (without the “;1”).

2. Copy the SD_53_177.EXE file into an empty (temporary or scratch) directory.
3. Run the SD_53_177.EXE file (double click on it). This starts the PCMM installation. See Section IV, Installation of the PCMM Client Software, for information on the files installed in the Client Workstation.

Client Installation Notes

A PCMM.EXE cannot be placed on a workstation and successfully executed if the full installation has never been run on the workstation. The full installation registers two DLLs that are needed for the .EXE to run. If the full client installation has been performed, then any subsequent .EXE can be placed on the PC and utilized. The installation will install the following files onto that workstation.

> PCMM.EXE 1369 KB

> PCMM.HLP 115 KB

> RESIZER.DLL 559 KB

> RESIZABLECONTROL.DLL 130 KB

IV. Installation of the PCMM Client Software

The following screens illustrate the installation of the PCMM client software. If all the default responses are accepted, the PCMM software will be installed into the appropriate V*IST*A directory on the user’s workstation.

This version of the client software can be installed as either a patch to the existing client software or as a new installation.

![](sd-5-3-177-pcmm-install-guide-release-notes/002.png)

The first screen is a welcome or introduction screen. After reading and following the instructions, click on the NEXT button to continue.

![](sd-5-3-177-pcmm-install-guide-release-notes/003.png)

The second screen displays the directory into which the software will be installed. This is the default directory used for V*IST*A software. It is recommended that you accept this directory.

![](sd-5-3-177-pcmm-install-guide-release-notes/004.png)

This next screen allows the installer to define the program icon that is created. Accepting the default is recommended.

![](sd-5-3-177-pcmm-install-guide-release-notes/005.png)

This screen displays the type of installation, where the software is going to be placed, and who is performing the installation.

Upon selecting the NEXT button on this screen, Install Shield will install the PCMM software in the target folder and set up the program icon. It will also create/update a subfolder of PCMM\docs in which it stores all the documentation files in a .PDF format.

![](sd-5-3-177-pcmm-install-guide-release-notes/006.png)

This is the last window in the installation. At this point, the software is installed. Install Shield asks the installer if they wish to run the application. There are no recommended responses at this point. If the YES box is checked, Install Shield will start PCMM. If it is not checked, Install Shield will finish and close.

Release Notes

USER RELEASE NOTES

This patch makes changes to the PCMM software, addressing some of the reported NOIS issues and adding new functionality. The changes and additions are defined below. If necessary, please refer to the PIMS User Manual - Scheduling Module regarding PCMM Reports, the PCMM User Guide, the Practice Profiling Software Requirements Specifications, or the online help for further information.

Several new enhancements have been made to the PCMM GUI software to comply with the Practice Profiling effort. This new functionality addresses the need to show a relationship between the *associate provider* (the provider that sees the patient on a day to day basis) and the *primary care provider* (the person that is ultimately responsible for the care of that patient). This relationship will be established through the preceptor functionality available in PCMM. As a result of this new linkage the following changes have been made.

I. GUI SideA. PC Attending Assignments

PC attending assignments can no longer be made. With this new preceptor linkage there is no longer a need to utilize the PC attending assignment designation when assigning patients to positions. The PCP will be established through the link. The GUI screens that allowed the PC attending assignments have been adjusted to remove that functionality. They include the following.

> Multiple Patient Assignment

> Multiple Patient Reassignment

> Position Information screen

  
B. Preceptor Assignment

A Preceptor button has been added on the Primary Care Team Position Setup screen under the current Staff button. The Preceptor button launches the user into the Preceptor Assignment screen. The Preceptor Assignment screen functions exactly like the Staff Assignment screen, except preceptor positions are selected/filed instead of staff. The Preceptor Assignment screen will include the name of the preceptor once assigned, the effective date of the assignment, status, and status reason. Preceptor history information will be retained and displayed. When the Assign button is clicked the Preceptor Lookup Screen will display. The Preceptor Lookup Screen will list all of the currently valid preceptor positions for the team.

Once a preceptor is assigned it will be displayed on the General Tab. The preceptor field will display the current preceptor assignment.

Assignment of a preceptor position locks the precepted position and the preceptor position into a “Preceptor Link”. For preceptor positions, the Staff Assignment form will not close if there is not a current staff assignment. For precepted positions, the Preceptor Assignment form will not close if there are current or future patient assignments and there is not a current preceptor assignment. When a position becomes part of a preceptor link, the “Can Act As Primary Care” and “Can Act as Preceptor” checkboxes on the Settings tab will not be allowed to change.

Positions with “Can Act as Preceptor” checked will have the Preceptor button disabled.

C. Messages

On the Messages tab, a Preceptor checkbox has been added for each message type. Checking the box will result in the current preceptor receiving the mail notification in addition to the current staff assigned to the position. The preceptor checkboxes will be disabled for positions with ‘Can Act as Preceptor’ checked.

D. Patient Team Position Assignment Screen

The information display columns have been changed to the following order: PC, Team Member, Position, Preceptor (PCP name), Standard Role. The AT column has been removed. The PC column will use an \* to identify PCP positions and an x to identify AP positions.

E. Team Patient Listings Report

As a result of the changes to the PCMM V*IST*A reports, the Patient Status radio check box will no longer be needed and has been removed from the report form.

II. Server Side

- Several changes have been made to various reports. The following options have been adjusted so that the PCP and AP information for each patient is correctly displayed.

> Non PCMM Options

> ACRP Ad Hoc Report \[SCRPW AD HOC REPORT\]

> Appointment List \[SDLIST\]

> Appointment Management \[SDAM APPT MGT\]

> Load/Edit Patient Data \[DG LOAD PATIENT DATA\]

> Patient Inquiry \[DG PATIENT INQUIRY\]

> Patient Profile MAS \[SDPATIENT\]

> PCMM Options

> DPA Detailed Patient Assignments (formerly Detailed Patient Enrollments)

> ITP Individual Team Profile

> PATA Patient Listing for Team Assignments (formerly Patient with Team Assignments)

> PD Practitioner Demographics

> PP Practitioner's Patients

> SLT Summary Listing of Teams (formerly Summary of Teams)

> TML Team Member Listing (formerly Team’s Members)

> TPL Team Patient Listing (formerly Team’s Patients)

> Primary Care Team/Posn Assign or Unassign

- The following menu and reports have been created to help manage the PCMM data. New reports have also been added to support the new functionality.

> *Menu Option*

> HAR Historical Assignment Reports

> *Report Options*

> *PAD Historical Patient Assignment Detail*

> Used for printing all provider, position and team assignments that exist for a patient during a specified date range.

> *PRAL Historical Provider Position Assignment Listing*

> Used for printing provider position assignments that exist during a specified date range.

> *PTAL Historical Patient Position Assignment Listing*

> Used for printing patient position assignments that exist during a specified date range.

> *TAS Historical Team Assignment Summary*

> Used for printing counts of team and team position assignments and unique patients within a specified date range.

> *PCMM Inconsistency Report*

> This report prompts the user for those team and position assignments that are to be validated according to the business rules that have been established for PCMM and the relationship between associate provider and preceptor. This report will be run as part of the installation process to get a summary of information. The PCMM Inconsistency Report checks for the following inconsistencies.

- Patient has no staff assigned.
- Patient has no PCPs assigned.
- Patient has multiple PCPs assigned.
- Associate Provider & PCP are the same for the same patient.
- Associate Provider is without a Preceptor.
- Associate Provider is not designated for PC.
- Preceptor is not designated for PC.

TECHNICAL RELEASE NOTESI. V*IST*A Client Changes

The client version for this release of the PCMM software is *1.2.0.0*. Version information may be viewed by clicking HELP\|ABOUT.

The total size of SD_53_177.EXE is 1683 KB. This file will load the following files on each workstation.

> PCMM.EXE 1369 KB

> PCMM.HLP 115 KB

> RESIZER.DLL 559 KB

> RESIZABLECONTROL.DLL 130 KB

A. Mail Messages

PCMM Reports users will be able to select “P-MESS” as an output device.

B. Kernel Security

PCMM client version 1.2.0.0 will look to “SCMC PCMM GUI WORKSTATION” to verify user access to remote procedures. Client versions prior to 1.2.0.0 look to “SC PCMM GUI WORKSTATION”. This option has been placed out of order and should not be enabled under any circumstances. Users with programmer access will continue to be able to use old client versions, but should do so only for trouble-shooting purposes.

II. V*IST*A Server Changes

The server version for this release of the PCMM software is *SD\*5.3\*177*.

A. Data Dictionary Changes

*<u>Existing Files</u>*

SCHEDULING EVENT (403.43) New scheduling events have been added.

SCHEDULING REASON (403.44) New Scheduling reasons have been added.

OUTPATIENT PROFILE (404.41) Two fields have been starred for deletion.

\*CURRENT PC ATTENDING (202)

\*CURRENT PC ATTENDING POSITION (205)

POSITION ASSIGNMENT HISTORY Update to .01 field.

(404.52) Two new fields:

USER ENTERING (.07)

DATE/TIME ENTERED (.08)

TEAM POSITION (404.57) One field has been starred for deletion.

\*PRECEPTOR POSITION

Eleven new fields.

PRECEPTOR DEATH MESSAGE (2.05)

PRECEPTOR INPATIENT MESSAGE (2.06)

PRECEPTOR TEAM MESSAGE (2.07)

PRECEPTOR CONSULT MESSAGE (2.08)

FUTURE \# OF PC PATIENTS (202)

FUTURE \# OF PATIENTS (203)

CURRENT PRECEPTOR POSITION (305)

CURRENT PRECEPTOR (306)

ACTIVE PRECEPTS (307)

ALLOW PRECEPTED CHANGE (400)

ALLOW PRECEPTOR CHANGE (401)

ACRP REPORT TEMPLATE PARAMETER (409.92)

*<u>New Files</u>*

PCMM PARAMETER (404.44)

PCMM SERVER PATCH (404.45)

PCMM CLIENT PATCH (404.46)

PCMM HL7 EVENT (404.48)

PCMM HL7 ID (404.49)

PRECEPTOR ASSIGNMENT HISTORY (404.53)

B. Mail Groups

New mail groups have been added to support HL7 transmission of primary care data to the Austin Automation Center.

> PCMM AUSTIN REPORTS

> PCMM HL7 MESSAGES

C. New Options

Historical Patient Assignment Detail \[SC PCMM HIST ASSIGN DETAIL\]

Historical Provider Position Assignment Listing \[SC PCMM HIST PROV ASSIGN LIST\]

Historical Patient Position Assignment Listing \[SC PCMM HIST PAT ASSIGN DETAIL\]

Historical Team Assignment Summary \[SC PCMM HIST TEAM ASSIGN SUM\]

PCMM HL7 Resubmit Rejects \[SCMC PCMM HL7 REJECTS\]\*

\*Currently out-of-order - released for future use

D. “B”-Type Options

*<u>Updated</u>*

SC PCMM GUI WORKSTATION placed out of order; should NOT be reactivated.

*<u>New</u>*

SCMC PCMM GUI WORKSTATION replaces inactivated “B” option

E.APIs

*<u>Updated</u>*

OUTPTAP^SDUTL3(DFN,SCDATE) ;given patient, return internal^external of the

pc associate provider.

*<u>New</u>*

GETALL^SCAPMCA(DFN,SCDT,SCARR) ;Get all assignment information

F. HL7

*Batch Job*

SCMC PCMM HL7 TRANSMIT

*Protocol*

PCMM SEND CLIENT FOR ADT-A08

PCMM SEND SERVER FOR ADT-A08

*HL7 Application Parameter*

PCMM

*HL Lower Level Protocol Parameter*

PCMM

*HL Logical Link*

PCMM

G. List Template

*<u>Updated</u>*

SDAM APPT MGT: The Top Margin field (.06) will be set to 6.

H. Associated Patches

The following V*IST*A packages anticipate a future release of a patch to use the preceptor information.

> CPRS OR\*3\*65

> PCE PX\*1.0\*78