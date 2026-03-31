---
title: SD 5.3 536 Recall Reminder Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 536 Recall Reminder
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*536
group_key: "SD:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 1
description: Recall Reminder Installation GuidePIMS V. 5.3 Scheduling ModulePatch SD\5.3\536Patch OR\3.0\302September 2009
audience: 
keywords: 
  - recall
  - clinic
  - print
  - table
  - contents
  - reminder
  - installation
  - sdrr
  - install
  - task
page_count: 0
word_count: 2157
section_count: 8
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/sd_53_536_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/sd_53_536_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

![](sd-5-3-536-recall-reminder-installation-guide/001.png)

Recall Reminder Installation GuidePIMS V. 5.3 Scheduling ModulePatch SD\*5.3\*536Patch OR\*3.0\*302September 2009

Office of Information and Technology (OI&T)

Office of Enterprise Development (OED)

Revision History

Initiated on 9/1/09

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 38%" />
<col style="width: 23%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Description (Patch # if applic.)</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>9/1/09</td>
<td><p>Patch SD*5.3*536 and</p>
<p>Patch OR*3.0*302 - Recall Reminder</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Installation](#installation)
  - [Software Retrieval](#software-retrieval)
  - [Patch Installation](#patch-installation)
  - [Installation Example](#installation-example)
  - [Routine Checksums](#routine-checksums)
  - [OR\3.0\302](#or30302)
  - [ORWCV 79773226](#orwcv-79773226)
  - [Post Installation](#post-installation)
This manual covers one-time information for the installation of Recall Reminder Version 1.0. Other information required to maintain this application is included in the Recall Reminder Technical and Security Guide and the Recall Reminder User Guide.
The Recall Reminder software is designed to allow facilities to implement recall scheduling. The software creates a ‘holding’ area for patients who are to return to clinic areas in more than 90 to 120 days.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the required patches are contained in the HFS file: SD_5_3_P536.KID.

Contents of SD_5_3_P536.KID are as follows.

> Patch Subject

> SD\*5.3\*536 Recall Reminder application

> OR\*3.0\*302 Recall Reminder

## Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SD_5_3_P536.KID file contains all the software and documentation necessary to install Recall Reminder. These files are available in the Office of Information Field Office (OIFO) ANONYMOUS.SOFTWARE directories listed below.

> OIFO FTP Address Directory

<span class="mark">REDACTED</span>

The files listed above may be obtained via FTP. The preferred method is to FTP the files from:

[download.vista.med.va.gov](ftp://ftp.fo-albany.med.va.gov)

## Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation should take less than 5 minutes; however, we recommend that you perform this installation at non-peak requirement hours.

Follow these steps:

1.  Download the KIDS file SD_5_3_P536.KID from the ANONYMOUS.SOFTWARE directory to the appropriate directory on your system.
2.  From the Kernel Installation & Distribution System menu, select the Installation menu.
3.  From the Installation menu, select the LOAD A DISTRIBUTION option and load SD_5_3_P536.KID.
4.  From this menu, you may elect to use the following options (when prompted for INSTALL NAME, enter SD\*5.3\*536).
    1.  Backup a Transport Global – this patch contains routines in a new namespace, therefore there are no routines to back up.
    2.  Compare Transport Global to Current System – this patch only contains new components not previously released, therefore there is nothing to compare.
    3.  Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
    4.  Print Transport Global – this option allows you to view the contents of the transport global.
5.  Use the Install Package(s) option and select the package SD\*5.3\*536.
6.  When prompted:

> Enter the Coordinator for Mail Group ‘SDRR BAD ADDRESS’: \<enter appropriate name\>

7.  When prompted:

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

8.  When prompted:

> Want KIDS to INHIBIT LOGONs during the install? YES// NO  

9.  When prompted:

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

## Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select INSTALL NAME: SD\*5.3\*536 Loaded from Distribution 7/8/09@11:13:41

=\> RECALL BUNDLE V1.0 ;Created on Jul 08, 2009@10:50:18

This Distribution was loaded on Jul 08, 2009@11:13:41 with header of

RECALL BUNDLE V1.0 ;Created on Jul 08, 2009@10:50:18

It consisted of the following Install(s):

SD\*5.3\*536 OR\*3.0\*302

Checking Install for Package SD\*5.3\*536

Install Questions for SD\*5.3\*536

Checking Install for Package SD\*5.3\*536

Install Questions for SD\*5.3\*536

Incoming Files:

403.5 RECALL REMINDERS

403.51 RECALL REMINDERS APPT TYPE

403.52 RECALL REMINDERS LETTERS

403.53 RECALL REMINDERS PARAMETERS

403.54 RECALL REMINDERS PROVIDERS

403.55 RECALL REMINDERS TEAM

403.56 RECALL REMINDERS REMOVED

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'SDRR BAD ADDRESS': POC,FORRECALL

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package OR\*3.0\*302

Install Questions for OR\*3.0\*302

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//

## Routine Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SD_5_3_P536.KID Routine CHECK1^XTSUMBLD values.

*SD\*5.3\*536*

SDRR1 13934931

SDRR5 9146765

SDRRC15 35948677

SDRRC16 36122202

SDRRC17 35448060

SDRRC18 38268527

SDRRC20 61232869

SDRRCLR 6432300

SDRRCLR2 10431466

SDRRCRR 75514794

SDRRCRR1 30605766

SDRRCRRP 40214532

SDRRDEL 3357699

SDRRINQ 72514446

SDRRINQ1 55827759

SDRRISB 778508

SDRRISRA 33542930

SDRRISRD 26348770

SDRRISRL 31811224

SDRRISRU 13362967

SDRRISRX 30760645

SDRRLRP 1446323

SDRROR 3486735

SDRRPXC 35140878

SDRRRECL 83067983

SDRRRECP 67349870

SDRRSEG3 2988411

SDRRSLC1 40514848

SDRRSLCT 60537302

SDRRTSK 13148697

SDRRTSK1 7882942

SDRRUTL 34000828

SDRRUTL1 26580492

## *OR\*3.0\*302*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ORWCV 79773226

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. If your facility has a version of Walla Walla Clinic Recall, you must remove protocol AXVCLR EVENT from the SDAM Menu Protocol using the following example.

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: PROTOCOL//

EDIT WHICH FIELD: ALL//

Select PROTOCOL NAME: SDAM MENU Appointment Management

NAME: SDAM MENU//

ITEM TEXT: Appointment Management Replace

Select SYNONYM:

PRINT NAME:

DISABLE:

LOCK:

DESCRIPTION:

This menu contains all the activities for the appointment management option.

Edit? NO//

PROHIBITED TIMES:

TYPE: menu//

FILE LINK:

COST:

Select ITEM: AXVCLR EVENT// @

SURE YOU WANT TO DELETE THE ENTIRE ITEM? Y (Yes)

2\. All sites must add SDRR EVENT to the SDAM MENU protocol. This will need to be done after normal business hours.

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: PROTOCOL//

EDIT WHICH FIELD: ALL//

Select PROTOCOL NAME: SDAM MENU Appointment Management

NAME: SDAM MENU//

ITEM TEXT: Appointment Management Replace

Select SYNONYM:

PRINT NAME:

DISABLE:

LOCK:

DESCRIPTION:

This menu contains all the activities for the appointment management

option.

Edit? NO//

PROHIBITED TIMES:

TYPE: menu//

FILE LINK:

COST:

Select ITEM: SD WAIT LIST ENTRY// SDRR EVENT Recall Reminder Action

MNEMONIC: RR (PLEASE TYPE RR AS THE MNEMONIC)

SEQUENCE:

MODIFYING ACTION:

FORMAT CODE:

DISPLAY NAME: ^

3\. Assign the SDRR MANAGER security key to your site's Recall Reminder Coordinators.

4\. Printer Terminal setting if your site chooses to print Recall cards.

TERMINAL TYPE FILE ENTRY:

NAME: P-REMOTECARD1 (TELNET) SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 35 FORM FEED: \#

PAGE LENGTH: 21 BACK SPACE: \$C(8)

OPEN EXECUTE: W \$C(27),"E",\$C(27),"&l1ol74A"

CLOSE EXECUTE: D CLOSE^NVSPRTU

The postcards are 4X6, govt. FL22 preprinted with the return address. One side of the postcard has the return address of the VA. The patient address information will be printed on this side by using Recall Reminder print options. The other side has information the patient will need about calling in to schedule the appointment.

\*\*\*There should not be any sensitive patient information included on this card.\*\*\*

The wording on the back of the cards may be preprinted by an outside vendor or a site print shop. Below are examples of possible wording which may be changed at each facility if desired. When using the cards, the only items that will print on the front of the card is the patient's address information, FL (if there is a fasting lab), NFL (if there are non-fasting labs) and \*\*## if the appointment is greater than 30 minutes.

The print options will only print the front part of the cards.

FRONT OF CARD

John Doe

1111 Street

Everywhere, OR 98321

\*\*NFL

\*\*60

Below are two examples taking into consideration patient privacy requirements. If a site chooses to print Recall Reminder Cards, they must have a source for printing the back of the cards.

\*\*\*Clinic names that reference medical specialties such as GU, Mental Health, Dermatology, etc. or diagnoses must not be included on a postcard.\*\*\*

BACK OF CARD

Example 1

Please call one of the following

numbers to arrange an appointment that will be

convenient for you during the next month.

Portland Dialing Area: 503-xxx-xxxx

Vancouver Dialing Area: 360-xxx-xxxx

All Other Toll Free 1-800-xxx-xxxx

Example 2

It's that time again!

Please call (xxx) xxx-xxxx

Or toll free 1-800-xxx-xxxx ext. xxxx

Any weekday (9:00am-3:00pm) to schedule an appointment.

Date/time\_\_\_\_\_\_\_\_\_\_\_\_\_Fasting: Yes No

VA-Putting Veterans First

5\. If your site has installed any version of Walla Walla’s Recall application, please run the following options in order. If you are unsure if your site has any version of Walla Walla’s Recall application, check to see if you have the OUTPATIENT CLINIC RECALL file (#687065) and KIDS install AXVCLR\*1.0\*01. A site must have both of these items to be able to run the conversion options. Please read the instructions below the Conversion Menu before proceeding with the conversion.

SDRR IRM MENU Conversion Menu

1 Convert OUTPATIENT CLINIC RECALL PARAM

2 Convert OUTPATIENT CLINIC RECALL APPT TYPES

3 Convert OUTPATIENT CLINIC RECALL TEAM

4 Convert OUTPATIENT CLINIC RECALL PROVIDERS

5 Convert OUTPATIENT CLINIC RECALL

Run item 1 (Convert OUTPATIENT CLINIC RECALL PARAM) – Only after receiving a VistA email relating to Step 1 should you continue with Step 2. Each step will generate a VistA e-mail. Do not continue to the next step until you have received the e-mail that shows the previous conversion has finished for each file. Please see the Recall Reminder Technical and Security Guide for additional information and e-mail samples.

> **NOTE:** When the Convert OUTPATIENT CLINIC RECALL \[SDRR CONV OUTPATIENT RECALL\] option is run, if a site added local fields to file \#687065 (OUTPATIENT CLINIC RECALL), they will not be converted to file \#403.5 (RECALL REMINDERS). Also, entries in file \#687065 which do not have an entry in Recall Date (field \#5) will not be moved over to file \#403.5.

6\. Auto Print for Recall Reminder \[SDRR TASK JOB\] needs to be setup up as a scheduled task using Kernel option Schedule/Unschedule Options \[XUTM SCHEDULE\] if your facility has selected at least one Recall Reminder Parameter to send notification type of LETTERS. When scheduling this job there is NO need to enter DEVICE FOR QUEUED JOB OUTPUT. This is determined by the printer name entered when setting up Recall Teams. ONLY printers that print 12 pitch should be selected for printing letters.

Example

Select OPTION to schedule or reschedule: SDRR TASK JOB Auto Print for Recall Reminder

Are you adding 'SDRR TASK JOB' as a new OPTION SCHEDULING (the 232ND)? No//Yes

Edit Option Schedule

Option Name: SDRR TASK JOB

Menu Text: Auto Print for Recall Reminder TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: OCT 23,2008@20:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

7\. Auto Print for Recall Reminder Cards \[SDRR TASK JOB CARD\] needs to be setup up as a scheduled task using Kernel option Schedule/Unschedule Options \[XUTM SCHEDULE\] if your facility has selected at least one Recall Reminder Parameter to send notification type of CARDS.

Example

Select OPTION to schedule or reschedule: SDRR TASK JOB Auto Print for Recall Reminder

Are you adding 'SDRR TASK JOB' as a new OPTION SCHEDULING (the 232ND)? No//Yes

Edit Option Schedule

Option Name: SDRR TASK JOB CARD

Menu Text: Auto Print for Recall Reminder Cards TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: OCT 23,2008@23:30

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

8\. Clean Up Clinic Recall Entries \[SDRR CLEAN-UP\] needs to be setup up as a scheduled task using Kernel option Schedule/Unschedule Options \[XUTM SCHEDULE\]. It is suggested this job be queued to run after 10:00pm.

Example

Select OPTION to schedule or reschedule: SDRR CLEAN-UP Clean Up Clinic Recall Entries

Are you adding 'SDRR CLEAN-UP' as a new OPTION SCHEDULING (the 231ST)? No//Yes

Option Name: SDRR CLEAN-UP

Menu Text: Clean Up Clinic Recall Entries TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: OCT 7,2008@23:30

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

9\. The following options (if your site has them) should be placed Out Of Order with a statement of “Replaced with Class I”. This should only be done once all conversions of the older Clinic Recall files have been successfully completed and your facility Recall Coordinator has given approval.

AXVC Options

Clinic Recall Menu Option \[AXVCLR CLINIC RECALL MENU\]

Print Clinic Recall Cards by Div \[AXVCLR RECALL PR CARD BY DIV\]

Print Clinic Recall Cards by Clinic \[AXVCLR RECALL PR CARD BY CLINIC\]

Print Clinic Recall Cards by Prov \[AXVCLR RECALL PRINT CARD\]

Print Clinic Recall Cards by Team \[AXVCLR RECALL PR CARD BY TM\]

Add/Edit Clinic Recall Patient \[AXVCLR RECALL CARD ADD\]

Edit/Add Clinic Recall Provider \[AXVCLR ADD RECALL PROVIDER\]

Edit/Add Recall Teams \[AXVCLR ADD RECALL TEAM\]

Inquire to Patient Recall \[AXVCLR RECALL CARD INQ\]

Recall List Print \[AXVCLR RECALL PRINT REPORT\]A687 Options

Print Clinic Recall Cards by Prov \[A687 RECALL PRINT CARD\]

Add/Edit Clinic Recall Patient \[A687 RECALL CARD ADD\]

Edit/Add Clinic Recall Provider \[A687 ADD RECALL PROVIDER\]

Inquire to Patient Recall \[A687 RECALL CARD INQ\]

Recall List Print \[A687 RECALL PRINT REPORT\]

You may have these two additional options which will need to be placed out of order.

Clinic Recall Menu \[A687 CLINIC RECALL MENU\]

Print 2 Sided Clinic Recall Cards \[A687 RECALL PRINT CARD2\]

Example

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: OPTION//

EDIT WHICH FIELD: ALL// OUT OF ORDER MESSAGE

THEN EDIT FIELD:

Select OPTION NAME: AXVCLR CLINIC RECALL MENU Recall Clinic Menu

OUT OF ORDER MESSAGE: Replaced with Class I