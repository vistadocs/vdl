---
title: IVMB*2*463 Error Processing Phase 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Error Processing Phase 1
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*463
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - prompt
  - error
  - process
  - seeding
  - installation
  - table
  - contents
  - press
  - install
  - message
page_count: 0
word_count: 2995
section_count: 9
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p463_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p463_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

![](ivmb-2-463-error-processing-phase-1-installation-guide/001.png)

Error Processing phase 1

Health eligibility center (HEC)

installation guide

Patch IVMB\*2\*463

May 2001

V*IST*A System Design & Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose](#purpose)
  - [Related Manuals](#related-manuals)
- [Preinstallation Considerations](#preinstallation-considerations)
  - [User Access to the Software](#user-access-to-the-software)
  - [Other Software Versions Required](#other-software-versions-required)
  - [Using the Software](#using-the-software)
- [Installation Instructions](#installation-instructions)
- [Sample Installation](#sample-installation)
- [Post-installation Considerations](#post-installation-considerations)
  - [Seeding Process](#seeding-process)
  - [Purge Process](#purge-process)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Eligibility Center (HEC) system sends eligibility data, enrollment data, income data, and Means Test data to the local VA Medical Centers (VAMCs) using HL7 messaging. Eligibility, enrollment, and income data are sent via a Z11 HL7 transmission; Means Test data via a Z10 HL7 transmission. In the event that a local VAMC is unable to process the information received, it will notify the HEC of a problem. This notification is transmitted via an Application Error (AE) message.

The HEC performs its own error checking to prevent bad data from being sent to the VAMC where it will be rejected and sent back to the HEC as an AE message. This error checking process notifies the HEC of the problem via a Consistency Check (CC) message. Previously, both the AE and CC messages were transmitted via a bulletin to various users at the HEC. Some of these error messages can be corrected through a manual correction at the HEC; the patient record must then be re-queued to be transmitted to the VAMC.

The Error Processing Tool was created to easily correct the inaccurate data, send the updated data to the VAMC, and keep track of the progress of the error correction process. It allows users to review the errors, exchange messages with VAMC personnel regarding the resolution of the data discrepancy, queue a transmission to be sent to the VAMC, and make corrections at the HEC, if necessary.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of Patch IVMB\*2\*463 is to provide an error processing tool that allows users at the HEC to:

- Easily correct inaccurate data at the HEC
- Send updated data to the VAMC
- Track the progress of the error correction process
- Review errors
- Exchange messages with VAMC personnel regarding the resolution of the data discrepancy
- Queue a transmission to be sent to the VAMC

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following manuals will also be released with Patch IVMB\*2\*463.

- Error Processing Phase 1 Technical Manual
- Error Processing Phase 1 User Manual

You can download the Error Processing Phase 1 documentation as follows:

From the Anonymous Directory

1.  Go to the anonymous.software directory.
2.  Ftp the files listed in the following table. Remember to use binary format.

|                    |                             |
|--------------------|-----------------------------|
| File Name      | Documentation Component |
| IVMB_2_p463_um.pdf | User Manual                 |
| IVMB_2_p463_tm.pdf | Technical Manual            |
| IVMB_2_p463_ig.pdf | Installation Guide          |

From the Project Notebook Web Page

REDACTED

# Preinstallation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## User Access to the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All users must be defined in the Error Processing User Group option in order to have access to the Error Processing Tool software. This option allows supervisors to assign individual users to a user-defined group and to define the sort criteria for displaying the list of error messages displayed in the Error Processing Tool.

## Other Software Versions Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following V*IST*A package versions or higher must be installed prior to installing Patch IVMB\*2\*463:

|                     |                              |
|---------------------|------------------------------|
| Package Name    | Minimum Version Required |
| IVM                 | 2.0                          |
| Kernel              | 8.0                          |
| VA FileMan          | 22.0                         |
| V*IST*A HL7 | 1.6                          |

## Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is not necessary for the users to be off the system during installation; however, the new software should not be used until the seeding process is complete. Using the software prior to completion of seeding could cause problems with the data stored in the tool. Refer to the Error Processing Phase 1 User Manual for instructions for using the Error Processing Tool software.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IVMB\*2\*463 can be loaded with users on the system. Installation will take several days because the post-installation routine will be seeding the ERROR LOG File (#3.075). It is very important to begin this installation on a Friday afternoon. Due to the complexity of the seeding process, it will take two to three days for the process to complete. The goal is to complete the process by Monday morning. In the following instructions, user responses are shown in bold type.

1.  Enter the MailMan menu to get the message from the build. After you locate, read, and exit the message, the following prompt will appear: “Enter message action (in IN basket): Ignore//”. At this prompt, type X and press \<Enter\>.
2.  At the “Select PackMan function:” prompt, select Option 6, which is the INSTALL/CHECK MESSAGE option.
3.  Review your mapped set. If any of the routines listed in the ROUTINE SUMMARY section are mapped, they should be removed from the mapped set at this time.
4.  At the “Want to continue with Load? YES//” prompt, type YES.
5.  At the “Select PackMan function:” prompt, press \<Enter\>. Continue pressing \<Enter\> until you are at the programmer’s prompt.
6.  At the programmer’s prompt, type D ^XUP and press \<Enter\>. This will take you to the Kernel Installation and Distribution Menu.
7.  From the Kernel Installation and Distribution System Menu, type Installation Menu.
8.  At the “Select Installation Option:” prompt, follow the steps below. (Note: These steps are optional for Options 1-5. They are mandatory for Option 6.)
    1.  Select Option 5, “Backup a Transport Global” - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates. When completed, the prompt: “Select Installation Option” will appear again.
    2.  Select Option 4, “Compare Transport Global to Current System” - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.). When completed, the prompt: “Select Installation Option” will appear again.
    3.  Select Option 2, “Verify Checksums in Transport Global” - this option will allow you to ensure the integrity of the routines that are in the transport global. When completed, the prompt: “Select Installation Option” will appear again.
    4.  Select Option 3, “Print Transport Global” - this option will allow you to view the components of the KIDS build. When completed, the prompt: “Select Installation Option” will appear again.
9.  At the “Select Installation Option:” prompt, select Option 6, “Install Package(s)”.
    10. At the “Select INSTALL NAME:” prompt, type IVMB\*2.0\*463.
    11. At the “Want KIDS to INHIBIT LOGONs during the install? YES//” prompt, respond NO.
    12. At the “Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//” prompt, respond YES.
    13. At the “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” prompt, respond YES.
    14. If routines were unmapped as part of step 2, they should be returned to the mapped set once the installation has run to completion.
    15. At the “Enter options you wish to mark ‘Out Of Order’:” prompt, press \<Enter\>.
    16. At the “Enter protocols you wish to mark as ‘Out Of Order’:” prompt, press \<Enter\>.
    17. At the “Delay Install (Minutes): (0-60): 0//” prompt, press \<Enter\>.
    18. You will be prompted to enter the device you want to print the Install messages. Use your choice for this prompt.
    19. At the “OKAY TO START SEEDING ROUTINE? NO//” prompt, respond YES.
    20. The message “Beginning Seeding Process (Present Date and Time)” will print to the screen. After this message, if you receive the following message: \*\*ERROR: FAILED TO QUEUE THE SEEDING ROUTINE!\*\*, you must get back to the programmer’s prompt, type

> D ^IVMB463P and press \<Enter\>. If you receive the same error message, contact a supervisor at the HEC.

21. The seeding process will take a couple of days. Upon completion of this process, you will receive a MailMan message notifying you of the number of errors filed in the tool, the number of duplicate errors that were not filed in the tool, and a list of records that should and should not be in the tool. These records can be used to validate that the seeding process has functioned correctly by checking the list against the entries in the tool. When the purge is complete, you will receive a MailMan message notifying you of the name of the VMS file that contains the purged data. If at any time the seeding process should error, enter the following at the programmer’s prompt: D ^IVMB463P. The seeding process will pick up where it left off.
22. The following steps will schedule and activate the Error Purge process. This is a background process needed to thin out the ERROR LOG File (#3.075).

From the programmer’s prompt, enter the FileMan option (\>D P^DI).

> a\) At the “Select OPTION:” prompt, type Enter/Edit and press \<Enter\>.

1.  At the “INPUT TO WHAT FILE:” prompt, type OPTION and press \<Enter\>. (Select \#1 if more than one option appears.)
2.  At the “EDIT WHICH FIELD: ALL//” prompt, type 209 and press \<Enter\>.
3.  At the next prompt, press \<Enter\> until the prompt “Select OPTION NAME:” appears.
4.  At the “Select OPTION NAME:” prompt, type AYCB ERROR PURGE and press \<Enter\>.
5.  At the prompt, “SCHEDULING RECOMMENDED:”, type Y and press \<Enter\>. Continue pressing \<Enter\> until you exit the option and are returned to the programmer’s prompt.
23. Enter the Kernel system by typing (\>D ^XUP) at the programmer’s prompt and press

\<Enter\>.

1.  At the “OPTION NAME:” prompt, type TASKMAN MANAGEMENT and press \<Enter\>.
2.  At the “Select TaskMan Management Option:” prompt, type Schedule/Unschedule Options and press \<Enter\>.
3.  At the “Select OPTION to schedule or reschedule:” prompt, type AYCB ERROR PURGE and press \<Enter\>.
4.  At the “Are you adding 'PURGE ERROR FILE' as a new OPTION SCHEDULING (the \###th)?” prompt, type Y and press \<Enter\>.
5.  Continue pressing \<Enter\> until you are at the “QUEUED TO RUN AT WHAT TIME:” prompt.
6.  At the “QUEUED TO RUN AT WHAT TIME:” prompt, type T+1@0100 and press \<Enter\>. This will schedule the deletion routine to run at 1 a.m. Any time may be specified between 12:30 a.m. and 5:00 a.m. (0030-0500).
7.  At the next few prompts, continue pressing \<Enter\> until the “RESCHEDULING FREQUENCY:” prompt appears.
8.  At the “RESCHEDULING FREQUENCY:” prompt, type 24H and press \<Enter\>.
9.  At the next few prompts, continue pressing \<Enter\> until the command box appears at the bottom of the screen.
10. In the command box at the flashing cursor, type S (Save) and press \<Enter\>.
11. Another command box will appear in the same place with a flashing cursor again. Type E in this command box and press \<Enter\>.
12. Starting at the “Select OPTION to schedule or reschedule:” prompt, press \<Enter\> and continue pressing \<Enter\> until you return to the programmer’s prompt.
24. The final step of this installation is to set up security keys to limit access to several of the menu options. The following menu options need to have security keys assigned to only allow supervisors access:

> 2 Error Processing Reports

> 3 Error Processing Purge Parameters

> 4 Error Processing User Group

The installation of Patch \#IVMB463P is now complete.

# Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a copy of the screen dialog displayed when Patch IVMB\*2\*463 was installed in a test account. User responses are shown in bold type.

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: 6 INSTALL/CHECK MESSAGE

Line 6 Message \#14872886 Unloading KIDS Distribution IVMB\*2.0\*463

Want to Continue with Load? YES// YES

Loading Distribution...

IVMB\*2.0\*463

Select PackMan function: ^

Enter message action (in IN basket): Ignore// ^

End reached. Begin again? No// NO

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

The only option shown here will be Option \# 6. The other options are explained in the Installation Instructions. Remember, when using other options, always type IVMB\*2.0\*463 at the “Select INSTALL NAME:” prompt.

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: IVMB\*2.0\*463

IVMB\*2.0\*463

Checking Install for Package IVMB\*2.0\*463

Install Questions for IVMB\*2.0\*463

Incoming Files:

742070 HEC PARAMETER (including data)

742080 HEC ERROR PROCESSING LOG

742081 HEC ERROR PROCESSING GROUP

742082 HEC ERROR PROCESSING USER

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// YES

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// YES

Enter options you wish to mark as 'Out Of Order': \<Enter\>

Enter protocols you wish to mark as 'Out Of Order': \<Enter\>

Delay Install (Minutes): (0-60): 0// \<Enter\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\> GENERIC INCOMING TELNET

Install Started for IVMB\*2.0\*463 :

Apr 24, 2001@10:44:25

Build Distribution Date: Apr 20, 2001

Installing Routines:

Apr 24, 2001@10:44:26

IVMB\*2.0\*463

--------------------------------------------------------------------------------

Installing Data Dictionaries:

Apr 24, 2001@10:44:26

Installing Data:

Apr 24, 2001@10:44:27

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Installing LIST TEMPLATE

Installing OPTION

Apr 24, 2001@10:44:29

Running Post-Install Routine: ^IVMB463P

OKAY TO START SEEDING ROUTINE? ? NO// YES

--------------------------------------------------------------------------------

\[------------------------------------------------------------\]

0% \| 25 50 75 \|

Complete \[------------------------------------------------------------\]

During the seeding process, all of the AEs and CCs

encountered in the ^XMB global will be purged from this

global and stored in a separate file.

Please select a location for this file:

Select one of the following:

1 Local Directory (Development)

2 Production Directory

VMS File Location: 2// 2 Production Directory

Error Log File Seeding Process

Once the post-install is complete, a mail message

will be sent that will report the count of error

messages that were filed into the error log file.

Additionally, the report will contain notes about

any errors encountered during the seeding process.

Beginning Seeding Process Apr 24, 2001@11:03:25

Queued. Keep note of the task number \_\_\_\_\_\_.

If you wish to stop the seeding process for whatever

reason, use your User's Toolbox option to stop/start it.

If the seeding process does not start, the following screen will appear instead of the one above:

OKAY TO START SEEDING ROUTINE? ? NO// YES

--------------------------------------------------------------------------------

\[------------------------------------------------------------\]

0% \| 25 50 75 \|

Complete \[------------------------------------------------------------\]

During the seeding process all of the AE's and CC's

encountered in the ^XMB global will be purged from this

global and stored in a separate file.

Please select a location for this file:

Select one of the following:

1 Local Directory (Development)

2 Production Directory

VMS File Location: 2// 2 Production Directory

Error Log File Seeding Process

Once the post-install is complete, a mail message

will be sent that will report the count of error

messages that were filed into the error log file.

Additionally, the report will contain notes about

any errors encountered during the seeding process.

Beginning Seeding Process Apr 24, 2001@11:03:25

\*\*ERROR: FAILED TO QUEUE THE SEEDING ROUTINE!\*\*

If this occurs, get back to the programmer’s prompt and type D ^IVMB463P . If the process starts, you will get the following screen:

IVMB463P

OKAY TO START SEEDING ROUTINE? ? NO// YES

--------------------------------------------------------------------------------

\[------------------------------------------------------------\]

0% \| 25 50 75 \|

Complete \[------------------------------------------------------------\]

During the seeding process all of the AE's and CC's

encountered in the ^XMB global will be purged from this

global and stored in a separate file.

Please select a location for this file:

Select one of the following:

1 Local Directory (Development)

2 Production Directory

VMS File Location: 2// 2 Production Directory

Error Log File Seeding Process

Once the post-install is complete, a mail message

will be sent that will report the count of error

messages that were filed into the error log file.

Additionally, the report will contain notes about

any errors encountered during the seeding process.

Beginning Seeding Process Apr 24, 2001@11:03:25

Queued. Keep note of the task number \_\_\_\_\_\_.

If you wish to stop the seeding process for whatever

reason, use your User's Toolbox option to stop/start it.

# Post-installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Over the next several days, two separate processes will be activated: a seeding process and a purge process.

## Seeding Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the seeding process has completed, the user who installed the patch will receive the following mail message.

HEC Error Project Seeding process

(numeric number) errors have been logged into the Error Log File

(numeric number) duplicate errors were not logged into the file

(numeric number) ^XMB Records are set to be purged

Post HEC ERROR PROJECT Message

Seeding Process and patch is Complete

\*\*\*\*\*\*\*\*\*\* END OF REPORT \*\*\*\*\*\*\*\*\*\*

## Purge Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the purge process has completed, the Error Processing Active/Exempt mail group will receive the following mail message:

Error Project XMB purge data

The Error Project has purged all Z11 ""AE"" and ""CC"" type

messages from the ^XMB global.

The file: (name of file)

contains the purge data that could be used to re-populate the

Error Processing Tool if needed.

\*\*\*\*\*\*\*\*\*\* END OF REPORT \*\*\*\*\*\*\*\*\*\*

If the purge process fails, the Error Processing Active/Exempt mail group will receive the following mail message:

Error Project XMB purge data

The XMB Purge failed because it was unable to open

the file: (name of file)

\*\*\*\*\*\*\*\*\*\* END OF REPORT \*\*\*\*\*\*\*\*\*\*

If this message appears, please contact your NVS support person.

Once the seeding process has been queued, take the following steps if it needs to be halted at any time:

1)  At the programmer’s prompt, type D ^XUP and press \<Enter\>.
2)  At the “Select OPTION NAME:” prompt, type Taskman User and press \<Enter\>.
3)  Make sure you have the task number obtained when the seeding routine was originally started. Enter that number at the “Select TASK:” prompt.
4)  If you do not have the task number, type ?? at the “Select TASK:” prompt.
5)  Look through the tasks and find the task that has the following information:

(Task \[task number\]) START^AYCBEPS3, IVMB\*2\*463 SEEDING. No device. PDQ,ROU.

6)  Get the task number from this entry. At the “End of listing. Press \<Enter\>to continue:” prompt, type ^.
7)  At the “Select TASK:” prompt, type the task number and press \<Enter\>.
8)  At the “Select Action (Task (\[task number):” prompt, type Stop and press \<Enter\>. This will stop the process. Then get in contact with the supervisor at the HEC.