---
title: ARCH Version 1 Installation Guide (Pilot Program)
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: (Pilot Program)
app_code: FB
app_name: Fee Basis
section: FIN
app_status: active
pkg_ns: FB
patch_ver: 1
patch_id: FB*1
group_key: "FB:FB:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - arch
  - reminder
  - dialog
  - table
  - contents
  - installation
  - install
  - pilot
  - prompt
  - project
page_count: 0
word_count: 3566
section_count: 17
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: June 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/arch_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/arch_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=40"
---

![](arch-version-1-installation-guide-pilot-program/001.png)

Project ARCH

Enhance the Veteran Experience and Access to Healthcare (EVEAH) InitiativeAccess Received Closer to Home Automated Eligibility Determination

INSTALLATION and SETUP GUIDE

June 2011

Product Development

Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Automated notification of ARCH eligibility is accomplished using a nationally developed clinical reminder that uses a computed finding to determine patient eligibility. The patient eligibility information originally comes from an ADUSH/PP database, which is imported into the VistA FEE BASIS PATIENT file (#161) during the post installation process of the ARCH BUNDLE 1.0 multi-build distribution. The clinical reminder computed finding uses a Fee Basis API to determine Project ARCH eligibility. If the Veteran is determined to be Project ARCH eligible, a reminder dialog is available so that the provider can offer the Veteran various clinical services that are covered under the pilot program and are closer to the Veterans home.](#automated-notification-of-arch-eligibility-is-accomplished-using-a-nationally-developed-clinical-reminder-that-uses-a-computed-finding-to-determine-patient-eligibility-the-patient-eligibility-information-originally-comes-from-an-adushpp-database-which-is-imported-into-the-vista-fee-basis-patient-file-161-during-the-post-installation-process-of-the-arch-bundle-10-multi-build-distribution-the-clinical-reminder-computed-finding-uses-a-fee-basis-api-to-determine-project-arch-eligibility-if-the-veteran-is-determined-to-be-project-arch-eligible-a-reminder-dialog-is-available-so-that-the-provider-can-offer-the-veteran-various-clinical-services-that-are-covered-under-the-pilot-program-and-are-closer-to-the-veterans-home)
- [Pre-Installation](#pre-installation)
  - [Required Software for PXRM\2\20](#required-software-for-pxrm220)
  - [Required Software for FB\3.5\119](#required-software-for-fb35119)
  - [# Installation](#installation)
  - [Retrieve the host file containing the multi-package build](#retrieve-the-host-file-containing-the-multi-package-build)
  - [Install the build first in a training or test account.](#install-the-build-first-in-a-training-or-test-account)
  - [Load the distribution.](#load-the-distribution)
  - [## Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
  - [Print Transport Global (optional)](#print-transport-global-optional)
  - [Install the build.](#install-the-build)
  - [Install File Print](#install-file-print)
  - [Build File Print](#build-file-print)
  - [Post-installation routines](#post-installation-routines)
  - [Back-out Procedures](#back-out-procedures)
- [Set-up Instructions](#set-up-instructions)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [# # Release Notes](#release-notes)
- [Acronyms](#acronyms)
The Access Received Closer to Home (ARCH) Automated Eligibility Determination project is an interface between Veterans Health Information Systems and Technology Architecture (VistA)/Computerized Patient Record System (CPRS), and a data set containing geo-spatial information on eligible Veterans. The VistA software patches that support this initiative (PXRM\*2.0\*20 and FB\*3.5\*119) are being released in a Kernel Installation and Distribution System (KIDS) multi-package build, ARCH PILOT PROJECT 1.0.
The Veterans' Mental Health And Other Care Improvements Act Of 2008, Section 403, Public Law 110-387 mandates that the Department of Veterans Affairs (VA) conduct a pilot program over three years for contract care of eligible Veterans in selected Veterans Integrated Service Networks (VISNs).The Office of Policy Analysis within the Office of the Assistant Deputy Under Secretary for Health for Policy and Planning (ADUSH/PP) requested the capability to automatically identify all Veterans who are eligible for a high visibility Congressionally mandated contract care pilot program (named Project ARCH, Access to Care Received Closer to Home) in five VISNs (1, 6, 15, 18, and 19).

## Automated notification of ARCH eligibility is accomplished using a nationally developed clinical reminder that uses a computed finding to determine patient eligibility. The patient eligibility information originally comes from an ADUSH/PP database, which is imported into the VistA FEE BASIS PATIENT file (#161) during the post installation process of the ARCH BUNDLE 1.0 multi-build distribution. The clinical reminder computed finding uses a Fee Basis API to determine Project ARCH eligibility. If the Veteran is determined to be Project ARCH eligible, a reminder dialog is available so that the provider can offer the Veteran various clinical services that are covered under the pilot program and are closer to the Veterans home.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Project ARCH preferences presented to the provider in the reminder dialog are:

- ARCH: No service needed this visit
- ARCH: Does NOT consent at this time
- ARCH: Needs service & consents to program

Links are available in the reminder dialog to a consent form, a FAQ document, and the Care Coordinator’s phone number and email.

If the Veteran doesn’t need the service at this visit, clicking the first box will resolve the reminder until the next day.

If the Veteran does not consent to participate in the program, clicking the second box will resolve the reminder until the next day.

If the Veteran needs the service and consents to participate, clicking the third box will bring up a specific Project ARCH consult request that will be sent to the designated Care Coordinator.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Software for PXRM\*2\*20

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package/Patch</strong></td>
<td><strong>Namespace</strong></td>
<td><strong>Version</strong></td>
<td><strong>Comments</strong></td>
</tr>
<tr class="even">
<td>Clinical Reminders</td>
<td>PXRM</td>
<td>2.0</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td><p>GEN. MED. REC. – VITALS</p>
<p>GMRV*5*25</p></td>
<td>GMRV</td>
<td>5.0</td>
<td></td>
</tr>
<tr class="even">
<td>Health Summary</td>
<td>GMTS</td>
<td>2.7</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>HL</td>
<td>1.6</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>Kernel</td>
<td>XU</td>
<td>8.0</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td>XM</td>
<td>7.1</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td><p>NATIONAL DRUG FILE</p>
<p>PSN*4.0*176</p></td>
<td>PSN</td>
<td>4.0</td>
<td></td>
</tr>
<tr class="odd">
<td><p>Pharmacy Data Management</p>
<p>PSS*1.0*133</p></td>
<td>PSS</td>
<td>1.0</td>
<td></td>
</tr>
<tr class="even">
<td><p>Outpatient Pharmacy</p>
<p>PSO*7.0*299</p></td>
<td>PSO</td>
<td>7.0</td>
<td></td>
</tr>
<tr class="odd">
<td><p>RADIOLOGY/NUCLEAR MEDICINE</p>
<p>RA*5*56</p></td>
<td>RA</td>
<td>5.0</td>
<td></td>
</tr>
<tr class="even">
<td><p>TOOLKIT</p>
<p>XT*7.3*111</p></td>
<td>XT</td>
<td>7.3</td>
<td></td>
</tr>
<tr class="odd">
<td>VA FileMan</td>
<td>DI</td>
<td>22</td>
<td>Fully patched</td>
</tr>
</tbody>
</table>

## Required Software for FB\*3.5\*119

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                   |               |             |               |
|-------------------|---------------|-------------|---------------|
| Package/Patch | Namespace | Version | Comments  |
| Fee Basis         | FB            | 3.5         | Fully patched |

## # Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how to install the bundled patches, FB\*3.5\*119 and PXRM\*2\*20.

This build can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: Less than 5 minutes.

*The installation needs to be done by a person with DUZ(0) set to "@."*NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them immediately.

## Retrieve the host file containing the multi-package build 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use ftp to access the build (the name of the host file (ARCH_PILOT_PROJECT_1_0.KID) from one of the following locations:

> Albany REDACTED REDACTED

> Hines REDACTED REDACTED

> Salt Lake City REDACTED REDACTED

## Install the build first in a training or test account. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and ARCH_PILOT_PROJECT_1_0.KID at the Host File prompt.

From the Installation menu, you may elect to use the following options:

## ## Backup a Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

## Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

## Verify Checksums in Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

## Print Transport Global (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view the components of the KIDS build.

## Install the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build ARCH PILOT PROJECT 1.0 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: ARCH PILOT PROJECT 1.0    3/28/11@10:08:12

>      =\> ARCH PROJECT  ;Created on Mar 28, 2011@07:34:52

Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE:DO NOT QUEUE THE INSTALLATION. This installation may ask questions requiring responses and queuing will stop the installation. The most common are replacements for finding items or quick orders during the installation of Reminder Exchange file entries.

> Installation Example

> See [Appendix A](\l).

## Install File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If desired, you can use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

> Select Utilities Option: Install File Print

> Select INSTALL NAME:

## Build File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If desired, you can use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print

> Select BUILD NAME: FB\*3.5\*119   

> 1.0

> DEVICE: HOME//

## Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Do not complete this step until Project ARCH services have been implemented at your site. The Office of Policy Analysis will inform each site when Project ARCH Services will begin.

> The post-install routine, POST^FBARCH0, populates ARCH ELIGIBILITY entries in the FEE BASIS PATIENT file (#161).

> The post-install routines, PXRMP20E and PXRMP20I, install the following:

> ROUTINE

> PXRMARCH

> TIU TEMPLATE FIELD

> ARCH SERVICE LIST

> ARCH CONSENT FORM URL

> ARCH OVERVIEW TEXT

> ARCH FAQ URL

> ARCH CARE COORDINATOR

> HEALTH FACTORS

> ARCH

> ARCH-NO SERVICE NEEDED THIS VISIT

> ARCH-SERVICE NEEDED THIS VISIT DECLINES

> ARCH-SERVICE NEEDED THIS VISIT CONSENTS

> REMINDER SPONSOR

> VHA Office of the Assistant Deputy Under Secretary for Health for Policy

> and Planning

> REMINDER COMPUTED FINDINGS

> VA-PROJECT ARCH ELIGIBILITY

> REMINDER DEFINITION

> VA-PROJECT ARCH VISN CONTRACT CARE PILOT

> REMINDER DIALOG

> VA-PROJECT ARCH VISN CONTRACT CARE PILOT ELIGIBILITY

> These post-install routines can be deleted after the installation is complete.

## Back-out Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In reference to back-out procedures or a back-out plan, Project ARCH has neither, as CPRS changes can be rolled back, but database changes cannot. If any issues occur involving this patch, Support staff will need to resolve them.

# Set-up Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local sites can customize various portions of the Reminder Dialog in which they indicate whether a veteran will receive ARCH services.

- Each VISN has the ability to customize the services available at its location and/or to see services available at other locations.
- Each VISN can tailor its own links for consent forms.
- Each VISN can configure the type of order, or quick order, that is associated with the reminder when the Veteran consents to services offered.
- Under the “ARCH: Does NOT consent at this time” section of the Project ARCH Preferences, a user can record a health factor comment that contains the service the patient declined. This provides the ability to track the services in your VISN that are being declined.
- Under the “ARCH: Needs service and consents” section of the Project ARCH Preferences, a user can record a health factor comment that contains the service the patient accepted. This provides the ability to track the services in your VISN that are being accepted.

Set-up Steps

Edit the following Template Fields in the Template Field Editor (on the Options menu in CPRS, when you have the Consults or Notes tab open):

- ARCH CARE COORDINATOR
- ARCH CONSULT FORM URL
- ARCH FAQ URL
- ARCH SERVICE LIST
- ARCH OVERVIEW TEXT (This field can be edited, but it is not recommended.)

> **NOTE:** In order to use the Edit Template Fields option to edit template fields used in Reminder Dialogs, the following need to be enabled or assigned:

- TIU Template Reminder Dialog Parameter (on the CPRS Parameter menu on the Reminder Manager Menu)
- TIU parameter TIU FIELD EDITOR CLASSES
- User Class of Clinical Coordinator
1.  Open the Notes tab in CPRS and create a new progress note.

![](arch-version-1-installation-guide-pilot-program/002.png)

2.  Select Options on the Menu bar:

![](arch-version-1-installation-guide-pilot-program/003.png)

3.  Customize Care Coordinator contact information, using the Template Field Editor, to add ARCH coordinator information for your site.

![](arch-version-1-installation-guide-pilot-program/004.png)

4.  Configure linked consent (ARCH CONSENT FORM URL): Change the default address (<http://www.va.gov>) to point to the location where your ARCH consent form is stored,

![](arch-version-1-installation-guide-pilot-program/005.png)

5.  Add a link for the FAQ document (ARCH FAQ URL), if needed. Change the default address (<http://www.va.gov>) to point to the location where your ARCH FAQ document is stored

i![](arch-version-1-installation-guide-pilot-program/006.png)

6.  Edit text of available services for your VISN. You can also remove all the VISNs other than your own.

> ![](arch-version-1-installation-guide-pilot-program/007.png)

> *A word of caution:*  The template field editor doesn’t handle text wrapping very well, so it’s a good practice to stretch that window out the full length of your screen.  That will show the text of a given template field as it was intended to be seen.  Also, when exiting this window, use the “X” or Cancel button.  If you click OK to exit, you could adversely affect the formatting for a given template field. 

7.  Edit the ARCH COMMENT Additional Prompt. The list of services that add that comment to the health factor is shown. Go into the Reminders Manager’s menu in VistA, select Reminder Dialog Management (DM), then Reminder Dialogs (DI). When the Dialog screen opens, select the action Change View (CV), and then select Additional Prompts.

<u>Dialog List Mar 16, 2011@16:25:53 Page: 1 of 36</u>

REMINDER VIEW (ALL REMINDERS BY NAME)

<u>Item Reminder Name Linked Dialog Name & Dialog Status</u>

1 01-DIAB PTS (5Y) W/O DIAB EXAM (1Y

2 10-DIAB PTS (5Y) W/O DIAB EXAM (1Y

3 21-DIAB PTS (5Y) W/O DIAB EXAM (1Y

4 37-PC-PTSD SCREENING

5 691 PNT EYE CLINIC PNT EYE DIABETES-DLG

6 A NEW REMINDER A NEW REMINDER Disabled

7 AAA SCREENING AAA RISK SCREENING

8 AGETEST VA-HEPC AUTOGENERATE TEST

9 AGP ABNORMAL WH STUFF

10 AGP APPOINTMENT

11 AGP AUDC

12 AGP AUTO GENERATE AGP AUTO GENERATE Disabled

13 AGP BPRS

14 AGP BPRS TEST AGP BPRS DIALOG

15 AGP BRANCHING LOGIC DIALOG AGP BRANCHING LOGIC DIALOG

16 AGP BRANCHING LOGIC REMINDER

\+ Enter ?? for more actions \>\>\>

AR All reminders LR Linked Reminders QU Quit

CV Change View RN Name/Print Name

Select Item: Next Screen// CV Change View

Select one of the following:

D Reminder Dialogs

E Dialog Elements

F Forced Values

G Dialog Groups

P Additional Prompts

R Reminders

RG Result Group (Mental Health)

RE Result Element (Mental Health)

TYPE OF VIEW: R// P Additional Prompts

<u>Dialog List Mar 16, 2011@16:26:01 Page: 1 of 17</u>

DIALOG VIEW (ADDITIONAL PROMPTS)

<u>Item Dialog Name Dialog type Status</u>

1 A A PAIN BLANK TEXT PROMPT Additional Prompt

2 A A PAIN ENTER ALL APPLY Additional Prompt

3 A A PAIN FREQ HX Additional Prompt

4 A A PAIN ONSET PROMPT Additional Prompt

5 A A PAIN TXT 3CHR Additional Prompt

6 A A SG PAIN HISTORY LOCATION PROMPT Additional Prompt

7 A A TEST BTN1-10 Additional Prompt

8 AAAA Additional Prompt

9 ABILITY FAIR PROMPT Additional Prompt

10 ABILITY GOOD PROMPT Additional Prompt

11 ABILITY POOR PROMPT Additional Prompt

12 ADD TO PROB Additional Prompt

13 AGP LEVEL OF UNDERSTANDING Additional Prompt

14 AGP TEST PROMPT Additional Prompt

15 ANTI-COAGULANTS CONTRAINDICATED Additional Prompt

16 ARCH COMMENT Additional Prompt

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

AD Add CV Change View INQ Inquiry/Print

CO Copy Dialog PT List/Print All QU Quit

Select Item: Next Screen// 16

Current dialog element/group name: ARCH COMMENT

Used by: ARCH LOCAL CONSULT (Dialog Element)

ARCH SVC NEEDED DECLINES (Dialog Element)

NAME: ARCH COMMENT//

DISABLE:

CLASS: LOCAL//

SPONSOR: VHA Office of the Assistant Deputy Under Secretary for Health for Polic

y and Planning (10A5)//

REVIEW DATE:

PROMPT CAPTION:

EXCLUDE FROM PROGRESS NOTE:

DEFAULT VALUE:

Select CHECKBOX SEQUENCE: 3// ?

Answer with CHECKBOX SEQUENCE

Choose from:

1 VISN SERVICE 1

2 VISN SERVICE 2

3 VISN SERVICE 3

You may enter a new CHECKBOX SEQUENCE, if you wish

Type a Number between 1 and 500, 0 Decimal Digits

Select CHECKBOX SEQUENCE: 3// This is where new services can be added

Select CHECKBOX SEQUENCE: 3//

CHECKBOX SEQUENCE: 3//

TEXT: VISN SERVICE 3//

Select CHECKBOX SEQUENCE:

Input your edit comments.

Edit? NO//

8.  Add a consult orderable item, if needed.
    1.  Add content for the orderable item.

Example

CF Reminder Computed Finding Management ...

RM Reminder Definition Management ...

SM Reminder Sponsor Management ...

TXM Reminder Taxonomy Management ...

TRM Reminder Term Management ...

LM Reminder Location List Management ...

RX Reminder Exchange

RT Reminder Test

OS Other Supporting Menus ...

INFO Reminder Information Only Menu ...

DM Reminder Dialog Management ...

CP CPRS Reminder Configuration ...

RP Reminder Reports ...

MST Reminders MST Synchronization Management ...

PL Reminder Patient List Menu ...

PAR Reminder Parameters ...

ROI Reminder Orderable Item Group Menu ...

XM Reminder Extract Menu ...

GEC GEC Referral Report

Select Reminder Managers Menu Option: dm Reminder Dialog Management

DP Dialog Parameters ...

DI Reminder Dialogs

DR Dialog Reports ...

IA Inactive Codes Mail Message

Select Reminder Dialog Management Option: di Reminder Dialogs

<u>Dialog List Mar 14, 2011@09:58:20 Page: 1 of 36</u>

REMINDER VIEW (ALL REMINDERS BY NAME)

<u>Item Reminder Name Linked Dialog Name & Dialog Status</u>

1 01-DIAB PTS (5Y) W/O DIAB EXAM (1Y

2 10-DIAB PTS (5Y) W/O DIAB EXAM (1Y

3 21-DIAB PTS (5Y) W/O DIAB EXAM (1Y

4 37-PC-PTSD SCREENING

5 691 PNT EYE CLINIC PNT EYE DIABETES-DLG

6 A NEW REMINDER A NEW REMINDER Disabled

7 AAA SCREENING AAA RISK SCREENING

8 AGETEST VA-HEPC AUTOGENERATE TEST

9 AGP ABNORMAL WH STUFF

10 AGP APPOINTMENT

11 AGP AUDC

15 AGP BRANCHING LOGIC DIALOG AGP BRANCHING LOGIC DIALOG

16 AGP BRANCHING LOGIC REMINDER

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

AR All reminders LR Linked Reminders QU Quit

CV Change View RN Name/Print Name

Select Item: Next Screen// cv Change View

Select one of the following:

D Reminder Dialogs

E Dialog Elements

F Forced Values

G Dialog Groups

P Additional Prompts

R Reminders

RG Result Group (Mental Health)

RE Result Element (Mental Health)

TYPE OF VIEW: R// e Dialog Elements

<u>Dialog List Mar 14, 2011@10:02:42 Page: 12 of 178</u>

DIALOG VIEW (DIALOG ELEMENTS)

<u>+Item Dialog Name Dialog type Status</u>

177 APAT ROSI RX METFORMIN Dialog Element

178 APAT ROSI RX SULFON Dialog Element

179 APAT ROSI RX SULFON OR METFORMIN Dialog Element

180 APAT ROSI SULFON CANT OTHER Dialog Element

181 APAT ROSI SULFON MAY TRY ALPHA Dialog Element

182 APAT ROSI SULFON TIMPACT TXT Dialog Element

183 ARCH CARE COORDINATOR Dialog Element

184 ARCH CONSENT URL Dialog Element

185 ARCH FAQ URL Dialog Element

186 ARCH LOCAL CONSULT Dialog Element

187 ARCH NO SVC NEEDED DECLINES Dialog Element

188 ARCH OVERVIEW Dialog Element

189 ARCH SERVICE LIST Dialog Element

190 ASPIRIN THERAPY CONTRAINDICATED Dialog Element

191 ASPIRIN THERAPY TAKING FROM OTHER SOURC Dialog Element

192 Antry's - Blood test from finger. Dialog Element

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

AD Add CV Change View INQ Inquiry/Print

CO Copy Dialog PT List/Print All QU Quit

Select Item: Next Screen// 186

Dialog Name: ARCH LOCAL CONSULT

Current dialog element/group name: ARCH LOCAL CONSULT

Used by: ARCH SVC NEEDED CONSENTS (Dialog Group)

NAME: ARCH LOCAL CONSULT//

Dialog Name: ARCH LOCAL CONSULT

DISABLE:

CLASS: LOCAL//

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE: ORDERED//

ORDERABLE ITEM:

Finding item: Q GMRCOR CONSULT

FINDING ITEM: GMRCOR CONSULT// This is where you can enter the local name your site uses, if it’s different

Additional findings: none

Select ADDITIONAL FINDING:

DIALOG/PROGRESS NOTE TEXT:

Place order to ARCH program service

Edit? NO//

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE:

REMINDER TERM:

  
Examples of entering a patient’s responses in CPRS/Clinical Reminder

Reminder Showing as DUE NOW on the CPRS GUI Coversheet:

![](arch-version-1-installation-guide-pilot-program/008.png)

The Reminder is also viewable by clicking the reminder clock icon in the CPRS GUI header bar.

![](arch-version-1-installation-guide-pilot-program/009.png) ![](arch-version-1-installation-guide-pilot-program/010.png)

Reminder Inquiry

![](arch-version-1-installation-guide-pilot-program/011.png)

![](arch-version-1-installation-guide-pilot-program/012.png)

Resolving Reminders

1\. Log on to CPRS, select a patient, and select the *Notes* tab.

2\. Click on the New Note button.

3\. Select any title or type a new title in the title box.

4\. Choose a visit with which to associate the note. You can use the TELEPHONE CLINIC selection for telephone notes.

5\. When the note opens, "drawers" open in the lower left section of the screen. Click on the Reminders drawer to open it.

6\. When the Reminders drawer opens, you can see the reminders on which you can act.  

![](arch-version-1-installation-guide-pilot-program/013.png)

![](arch-version-1-installation-guide-pilot-program/014.png)![](arch-version-1-installation-guide-pilot-program/015.png)

Expanded sections of Reminder Dialog (window resized to show only relevant info)

No service needed this visit:

![](arch-version-1-installation-guide-pilot-program/016.png)

Not consenting at this time; capturing health factor comment for services declined:

![](arch-version-1-installation-guide-pilot-program/017.png)

Consenting, ordering a consult, and capturing health factor comment for services accepted

![](arch-version-1-installation-guide-pilot-program/018.png)

# Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Document Enhancement type patches

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System Option: INStallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: ARCH PILOT PROJECT 1.0 3/25/11@06:31:32

=\> PROJECT ARCH ;Created on Mar 24, 2011@11:19:03

This Distribution was loaded on Mar 25, 2011@06:31:32 with header of

PROJECT ARCH ;Created on Mar 24, 2011@11:19:03

It consisted of the following Install(s):

ARCH PILOT PROJECT 1.0 FB\*3.5\*119 PXRM\*2.0\*20

Checking Install for Package ARCH PILOT PROJECT 1.0

Install Questions for ARCH PILOT PROJECT 1.0

Checking Install for Package FB\*3.5\*119

Install Questions for FB\*3.5\*119

Incoming Files:

161 FEE BASIS PATIENT

> **NOTE:** You already have the 'FEE BASIS PATIENT' File.

Checking Install for Package PXRM\*2.0\*20

Install Questions for PXRM\*2.0\*20

Incoming Files:

811.4 REMINDER COMPUTED FINDINGS (including data)

> **NOTE:** You already have the 'REMINDER COMPUTED FINDINGS' File.

I will OVERWRITE your data with mine.

811.8 REMINDER EXCHANGE (including data)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//

FB\*3.5\*119

-------------------------------------------------------------------------

Installing Routines:

Mar 25, 2011@06:33:36

Install Started for FB\*3.5\*119 :

Mar 25, 2011@06:33:36

Build Distribution Date: Mar 24, 2011

Installing Routines:

Mar 25, 2011@06:33:36

Installing Data Dictionaries:

Mar 25, 2011@06:33:36

Running Post-Install Routine: POST^FBARCH0

Populating ARCH ELIGIBILITY in file (#161).....

--------------------------------------------------------------

100% - 25 50 75 -

Complete --------------------------------------------------------------

-------------------------------------------------------------------------

PXRM\*2.0\*20

--------------------------------------------------------------------------

DISABLE protocols.

Installing Data Dictionaries:

Mar 25, 2011@06:34:29

Installing Data:

Mar 25, 2011@06:34:29

Running Post-Install Routine: POST^PXRMP20I

ENABLE options.

ENABLE protocols.

There are 1 Reminder Exchange entries to be installed.

1\. Installing Reminder Exchange entry VA-PROJECT ARCH VISN CONTRACT

CARE PILOT ELIGIBILITY

------------------------------------------------------------------------

--------------------------------------------------------------

100% - 25 50 75 -

Complete --------------------------------------------------------------

Install Completed

# # # Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Reminders changes included in PXRM\*2\*20:

- A new clinical reminder and a new reminder dialog have been created to support identifying patients eligible to participate in Project ARCH, Access to Care Received Closer to Home. This project is only running in VISNs 1, 6, 15, 18 and 19.
- The reminder and dialog share the same name:

> VA-PROJECT ARCH VISN CONTRACT CARE PILOT ELIGIBILITY

- The reminder uses a new computed finding (VA-PROJECT ARCH ELIGIBILITY), which calls a Fee Basis API to determine if a given patient is eligible to participate in the Project ARCH.

Fee Basis changes included in FB\*3.5\*119:

- The Fee Basis patch only imports the eligibility data; there are no additional or modified Fee Basis options
- File (DD) changes:

> 161 FEE BASIS PATIENT

> <u>Field Type Changes</u>

> 161 161.011,.01 ARCH ELIGIBILITY DATE 0;1 DATE

> 161 161.011,2 ARCH ELIGIBILITY 0;2 SET

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term     | Definition                                                     |
|----------|----------------------------------------------------------------|
| ADUSH/PP | Under Secretary for Health for Policy and Planning             |
| ARCH     | Access to Care Received Closer to Home                         |
| ASU      | Authorization/Subscription Utility                             |
| CPRS     | Computerized Patient Record System                             |
| DG       | Registration and Enrollment Package namespace                  |
| ESM      | Enterprise Systems Management (ESM)                            |
| EVEAH    | Enhance The Veteran Experience and Access to Health Care       |
| FIM      | Functional Independence Measure                                |
| GUI      | Graphic User Interface                                         |
| IAB      | Initial Assessment & Briefing                                  |
| OI       | Office of Information                                          |
| OIF/OEF  | Operation Iraqi Freedom/Operation Enduring Freedom             |
| PCS      | Patient Care Services                                          |
| PXRM     | Clinical Reminder Package namespace                            |
| RSD      | Requirements Specification Document                            |
| SD       | Scheduling Package Namespace                                   |
| VA       | Department of Veteran Affairs                                  |
| USR      | ASU package namespace                                          |
| VistA    | Veterans Health Information System and Technology Architecture |
OIT Master Glossary: REDACTED
