---
title: PXRM*2*10 Skin Assessment Templates Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Skin Assessment Templates Install Guide
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*10
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - contents
  - table
  - install
  - skin
  - risk
  - consult
  - reminder
  - assessment
  - installation
  - global
page_count: 0
word_count: 2688
section_count: 24
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_10_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_10_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-10-skin-assessment-templates-install-guide/001.png)

Skin Risk AssessmentPXRM\*2.0\*10GMTS\*2.7\*87TIU\*1\*230

INSTALLATION & SETUP GUIDE

October 2007

Health Provider Systems

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Contents](#contents)
- [Introduction](#introduction)
  - [Skin Risk Assessment](#skin-risk-assessment)
  - [### Web Sites](#web-sites)
  - [# Pre-Installation](#pre-installation)
  - [Required Software](#required-software)
  - [## Estimated Installation Time](#estimated-installation-time)
  - [## Consult Orderable Item](#consult-orderable-item)
  - [# Installation](#installation)
  - [Retrieve the PXRM\2.0\10, TIU\1\230, and GMTS\2.7\87 build](#retrieve-the-pxrm2010-tiu1230-and-gmts2787-build)
  - [Install the build first in a training or test account.](#install-the-build-first-in-a-training-or-test-account)
  - [Load the distribution.](#load-the-distribution)
  - [## Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
  - [Print Transport Global (optional)](#print-transport-global-optional)
  - [Install the package.](#install-the-package)
  - [Install File Print](#install-file-print)
  - [Build File Print](#build-file-print)
  - [Post-installation routines](#post-installation-routines)
  - [Deletion of init routines](#deletion-of-init-routines)
  - [Ensure that reminders and dialogs are installed](#ensure-that-reminders-and-dialogs-are-installed)
- [Setup and Maintenance](#setup-and-maintenance)
- [Three patches are included with the Skin Assessment/Reassessment application:](#three-patches-are-included-with-the-skin-assessmentreassessment-application)
  - [Post-Install instructions](#post-install-instructions)
  - [## Setting up the Skin Assessment and Skin Risk Assessment Templates](#setting-up-the-skin-assessment-and-skin-risk-assessment-templates)
  - [Reminder Reports](#reminder-reports)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Skin Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pressure ulcers are a problem in all health care settings and result in significant morbidity, mortality, and costs for the health care system.

The national Handbook and Directive to the field in June 2006 establishes procedures for the assessment and prevention of pressure ulcers in VHA to provide a guideline for consistent and acceptable skin care practices. A key part of the plan is to have a system of reporting in order to monitor system-wide care.

VA Nursing Outcomes Database (VANOD) originally collected this pressure ulcer prevalence data, which was a cumbersome process involving customized Excel spreadsheets, and also failed to link nursing processes with outcomes of hospital-acquired pressure ulcers.

A more seamless method was developed, using clinical reminders dialog templates, which allow collection of standardized patient data across the system. This data will populate the progress note, and the captured health factors will provide daily concurrent reports on individual patients for care management. Ultimately, aggregate reports will be available at the facility, VISN, and national levels.

VANOD pilot-tested the skin risk admission and reassessment template at 10 sites, preparatory to this release as a national clinical reminder template

Once the template is implemented, the benefit for VA will be a consistent format for data entry that is available for a global view of VHA practice in regard to skin risk assessment, preventive strategies, and incidence of community vs hospital acquired pressure ulcers.

Advantages for staff nurses and Wound Ostomy and Continence (WOC) nurses at the facility level as well, including:

For staff nurses:

- Braden scale prompt and reassessment expectations
- Reminders for the staff nurse of prior risk assessment scores and the presence and stage of existing pressure ulcers.
- Prompts for interventions and alerts to clinicians

For WOC clinicians:

- Ability to run daily reports that would provide information on patients found to be high-risk or with pressure ulcers on the admission assessment, OR patients found to have developed a pressure ulcer.

Nationally:

- Comparative national, VISN and facility reports on VA practice in regard to documented skin risk assessment, reassessment practices, community acquired vs hospital-acquired pressure ulcers.

## ### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                  |                                               |                                                                                            |
|----------------------------------|-----------------------------------------------|--------------------------------------------------------------------------------------------|
| Site                         | URL                                       | Description                                                                            |
| National Clinical Reminders site | <http://vista.med.va.gov/reminders>           | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| VANOD                            | <http://vaww.vanod.med.va.gov/collage/vanod/> | VA Nursing Outcomes Database                                                               |

## # Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual describes how to install and set up Clinical Reminders patch PXRM\*2\*10, TIU\*1\*230, AND GMTS\*2.7\*87.

## Required Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                            |               |             |               |
|----------------------------|---------------|-------------|---------------|
| Package/Patch          | Namespace | Version | Comments  |
| Clinical Reminders         | PXRM          | 2.0         | Fully patched |
| Health Summary             | GMTS          | 2.7         |               |
| HL7                        | HL            | 1.6         | Fully patched |
| Kernel                     | XU            | 8.0         | Fully patched |
| MailMan                    | XM            | 7.1         | Fully patched |
| Text Integration Utilities | TIU           | 1.0         |               |
| VA FileMan                 | DI            | 22          | Fully patched |

## ## Estimated Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                         |                                                                                 |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Installation                                                                            | About 5 minutes                                                                 |
| Setup after installation by the Reminder Manager or CAC to address local implementation | One-four hours (depending partly on the experience level of the manager or CAC) |

## ## Consult Orderable Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following dialog elements are meant to be used for ordering a consult to the team at your facility that does further evaluation.

VA-VANOD OI SKIN RISK ORDER NUTRITION CONSULT

VA-VANOD OI WOUND CONSULT

At the time of install, the Reminder Dialog will use the GMRCOR CONSULT as the consult orderable item for both of the dialog elements. Sites should substitute a quick order or order menu for ordering consults to the Nutrition Team or a Wound Care Specialist at your facility. If no such service is available yet, then sites may wish to leave the GMRCOR CONSULT in the dialog element until a consult becomes available.

National Health Summary Types

Because of Remote Data View, the Health Summary Types cannot be installed in the 5000000 number spaces. A pre-install routine will create stub entries for each Health Summary as blank entries that are not in the 5000000 number spaces. To verify that the new Health Summary Types were installed at a blank IEN location not in the 5000000 number spaces, do the following:

1\. Back up your data in file ^GMT(142

2\. Capture a global listing of file \#142. This is done from the programmer prompt.

DEVCUR\>D ^%G

Device: Right margin: 80=\>

Global ^GMT(142,,0

^GMT(142,1,0)=DAVID'S^^1294

^GMT(142,2,0)=DISCHARGE SUMMARY^^1118

^GMT(142,3,0)=SRI^^1118

.

.

^GMT(142,257,0)=TELE MHAS^^1118^^Y

^GMT(142,260,0)=SKIN ASSESSMENT^^123456789169^^Y

^GMT(142,261,0)=JG1^^15^^Y

^GMT(142,5000001,0)=REMOTE DEMO/VISITS/PCE (3M)^GMTSMGR^.5^Y

^GMT(142,5000002,0)=REMOTE MEDS/LABS/ORDERS (3M)^GMTSMGR^.5^Y

^GMT(142,5000003,0)=REMOTE TEXT REPORTS (3M)^GMTSMGR^.5^Y

3\. Install the patch

4\. Redo the global listing of file \#142

DEVCUR\>D ^%G

Device: Right margin: 80=\>

Global ^GMT(142,,0

^GMT(142,1,0)=DAVID'S^^1294

^GMT(142,2,0)=DISCHARGE SUMMARY^^1118

^GMT(142,3,0)=SRI^^1118

.

.

^GMT(142,257,0)=TELE MHAS^^1118^^Y

^GMT(142,258,0)=VA-PRESSURE ULCER^^^^Y

^GMT(142,259,0)=VA-PU INTERVENTIONS^^^^Y

^GMT(142,260,0)=SKIN ASSESSMENT^^123456789169^^Y

^GMT(142,261,0)=JG1^^15^^Y

^GMT(142,262,0)=VA-BRADEN SCALE 30D^^^^Y

^GMT(142,5000001,0)=REMOTE DEMO/VISITS/PCE (3M)^GMTSMGR^.5^Y

^GMT(142,5000002,0)=REMOTE MEDS/LABS/ORDERS (3M)^GMTSMGR^.5^Y

5\. Verify that the New Health Summary Types were installed at a blank IEN location that is not in the 5000000 number spaces.

## # Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This build can be installed with users on the system, but it should be done non-peak hours.

*The install needs to be done by a person with DUZ(0) set to "@."*

## Retrieve the PXRM\*2.0\*10, TIU\*1\*230, and GMTS\*2.7\*87 build 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The name of the host file is PXRM_GMTS_TIU_SKIN_RISK_ASSESSMENTS.KID.

> Use ftp to access the build from one of the following locations:

> Albany <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Salt Lake City <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

## Install the build first in a training or test account. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In programmer mode, do ^XUP, select the Kernel Installation & Distribution System menu

(XPD MAIN), then the Installation option, then the option LOAD a Distribution. Enter your directory name and PXRM_GMTS_TIU_SKIN_RISK_ASSESSMENTS.KID at the Host File prompt.

Example

> Select Installation Option: LOAD a Distribution

> Enter a Host File: PXRM_GMTS_TIU_SKIN_RISK_ASSESSMENTS.KID

> KIDS Distribution saved on

> Comment: VANOD Skin Risk Assessment templates

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

## Install the package.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*10 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: PXRM\*2.0\*10

Answer "NO" to the following prompts:

> Want KIDS to INHIBIT LOGONs during install? NO // NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO // NO

> When prompted "Delay Install (Minutes): (0-60): respond '0'.

> This installation should not be queued, because it installs some packed reminder definitions and may require selection of replacements for some components. Therefore, it is recommended that the site’s Clinical Reminder Manager is present during the install.

Installation Example

Setting up programmer environment

Terminal Type set to: C-VT220

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System menu

Select Kernel Installation & Distribution System Option: Installation

Select Installation Option: Install Package(s) \[XPD INSTALL BUILD\]

Select INSTALL NAME: PXRM\*2\*10

Loaded from Distribution 7/12/07@17:10:58

=\> JFKD ;Created on Jul 12, 2007@17:08:21

This Distribution was loaded on Jul 12, 2007@17:10:58 with header of

JFKD ;Created on Jul 12, 2007@17:08:21

It consisted of the following Install(s):

PXRM\*2.0\*10 GMTS\*2.7\*87 TIU\*1.0\*230

Checking Install for Package PXRM\*2.0\*10

Install Questions for PXRM\*2.0\*10

Incoming Files:

801.41 REMINDER DIALOG (including data)

> **NOTE:** You already have the 'REMINDER DIALOG' File.

I will OVERWRITE your data with mine.

811.8 REMINDER EXCHANGE (including data)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Checking Install for Package GMTS\*2.7\*87

Install Questions for GMTS\*2.7\*87

Checking Install for Package TIU\*1.0\*230

Install Questions for TIU\*1.0\*230

Want KIDS to INHIBIT LOGONs during the install? NO// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME

Install Started for PXRM\*2.0\*10 :

Jul 12, 2007@17:11:17

Build Distribution Date: Jul 12, 2007

Installing Routines:

Running Pre-Install Routine: PRE^PXRMP10I

Installing Data Dictionaries:

Installing Data:

Jul 12, 2007@17:11:17

Running Post-Install Routine: POST^PXRMP10

Installing reminder VA-VANOD SKIN ASSESSMENT

Installing reminder VA-VANOD SKIN REASSESSMENT

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*10 Installed.

Jul 12, 2007@17:11:52

Install Message sent \#93577

Install Started for GMTS\*2.7\*87 :

Jul 12, 2007@17:11:53

Build Distribution Date: Jul 12, 2007

Installing Routines:

Running Pre-Install Routine: PRE^GMTSP87I

Running Post-Install Routine: POST^GMTSP87I

Installing reminder GMTS SKIN RISK HS TYPES

Installing reminder GMTS SKIN RISK HS OBJECTS

Updating Routine file...

Updating KIDS files...

GMTS\*2.7\*87 Installed.

Jul 12, 2007@17:11:53

Install Message sent \#93579

Install Started for TIU\*1.0\*230 :

Jul 12, 2007@17:11:53

Build Distribution Date: Jul 12, 2007

Installing Routines:

Running Pre-Install Routine: EN^TIUPR230

Creation of TIU Object BRADEN SCALE 30D successful...

Creation of TIU Object PRESSURE ULCER successful...

Creation of TIU Object PU INTERVENTIONS successful...

Object creation finished.

Updating Routine file...

Updating KIDS files...

TIU\*1.0\*230 Installed.

Jul 12, 2007@17:11:56

Install Message sent \#93581

Install Completed

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

## Install File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process.

> Select Installation & Distribution System Option: Utilities

> Select Utilities Option: Install File Print

> Select INSTALL NAME: PXRM\*2\*10

## Build File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

> Select Installation & Distribution System Option: Utilities

> Select Utilities Option: Build File Print

> Select BUILD NAME: PXRM\*2.0\*10 CLINICAL REMINDERS

> DEVICE: HOME//

## Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> POST^PXRMP10

> POST^GMTSP87I

## Deletion of init routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The init routines PXRMP10I and GMTSP87I may be deleted once the installation has completed. Sites should use the Kernel "Delete Routines" option \[XTRDEL\] to delete this routine.

## Ensure that reminders and dialogs are installed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the installation has finished, if you discover that the reminders weren’t installed correctly for some reason, you can use the Exchange options on the Reminders Manager Menu to install the “packed” reminders.

# Setup and Maintenance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Three patches are included with the Skin Assessment/Reassessment application:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Clinical Reminders patch PXRM\*2\*10

> This patch releases two new national Reminder Definitions and Dialogs used for Skin Risk Assessment. The Reminder Definitions are used only for distributing the national Dialogs – there is no evaluation logic in the Reminder Definitions.

> Reminder Definitions and Dialogs names:

> VA-VANOD SKIN INITIAL ASSESSMENT

> VA-VANOD SKIN REASSESSMENT

> These Reminder Dialogs have been developed and sponsored by The Office of Nursing Services.

> This patch also includes 10 national Additional Prompts and one Forced Value used in the dialogs.

> Additional Prompts:

> PXRM BRADEN 6-8

> PXRM BRADEN 10-12

> PXRM BRADEN 13-14

> PXRM BRADEN 15-18

> PXRM BRADEN 19-23

> PXRM VANOD PU LOCATIONS

> PXRM VANOD SKIN COLOR

> PXRM VANOD SKIN MOISTURE

> PXRM VANOD SKIN TEMP

> PXRM VANOD SKIN TURGOR

> Forced Value:

> PXRM VISIT DATE FORCED TODAY

2\. Health Summary patch GMTS\*2.7\*87

> This patch includes three Health Summary objects and Health Summary Types.

> Health Summary Types:

> VA-BRADEN SCALE 30D

> VA-PRESSURE ULCER

> VA-PU INTERVENTIONS

> Health Summary Objects

> VA-BRADEN SCALE 30D (TIU)

> VA-PRESSURE ULCER (TIU)

> VA-PU INTERVENTIONS (TIU)

> Objects are built to pull in information from a previous Skin Assessment.

3\. TIU patch TIU\*1\*230

> The TIU patch creates the TIU portion of the TIU\HS Objects:

> BRADEN SCALE 30D

> PRESSURE ULCER

> PU INTERVENTIONS

> These objects will be used by the Reminder Dialogs to display the Health Summary data

## Post-Install instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following dialog elements are meant to be used for ordering a consult to the team at your facility that does further evaluation.

VA-VANOD OI SKIN RISK ORDER NUTRITION CONSULT

VA-VANOD OI WOUND CONSULT

At the time of install, the Reminder Dialog will use the GMRCOR CONSULT as the consult orderable item for both of the dialog elements. *Substitute a quick order or order menu for ordering consults to the Nutrition Team or a Wound Care Specialist at your facility.* If no such service is available yet, you may leave the GMRCOR CONSULT in the dialog element until a consult becomes available.

Map the site-specific Quick Order (from the Reminder Managers menu) as follows:

1\. Select DM for Reminder Dialog Management

2\. Select DI for Reminder Dialogs

3\. Type CV for Change View

4\. Type E for Element

5\. Type SL for Search List

6\. Type the name of the dialog element,

VA-VANOD OI SKIN RISK ORDER NUTRITION CONSULT and press Enter

7\. At the "Find Next" prompt type No

8\. Type the item number next to the element

9\. At the finding Item Prompt, enter Q. plus the name of the site-specific

Quick Order or order menu

10\. Press Enter at the Additional Finding prompt

11\. Press Enter at the Edit prompt

11\. Repeat the above steps for the other dialog element,

VA-VANOD OI WOUND CONSULT

## ## Setting up the Skin Assessment and Skin Risk Assessment Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow these steps to set up the Skin Risk Assessment templates as a Clinical Reminders dialog.

1\. Edit the TIU TEMPLATE parameter

- Go to the option TIU Template Reminder Dialog Parameter, on the CPRS Parameter menu on the Clinical Reminders Manager menu.
- Add these two dialogs to the list at the System level as available templates

2\. Open the template editor in CPRS and create two new templates. They are reminder dialog templates and you can place them in a folder or assign them to progress note titles. Dialogs may also be inserted in to current reminder dialogs to replace existing skin assessments.

3\. Health summary objects

> Three health summary objects are embedded in these reminder dialog templates. These objects will already be set up and included with the patch release.

4\. Orders and alerts

> Two elements in the dialog templates allow you to set up orders or alerts to send to the wound care specialist or to the dietitian. You must decide how you want these to work – either as consults or as generic orders with an orderable item that sends an alert to a user or to a group of users. The second option may be useful if there is concern at your site about nurses entering consult orders and signing them for a clinician. Instructions on how to do this follow.

Setting up a consult

1.  Create the type of order that you want to use.
2.  Go to the Reminder Dialog Management menu, choose DI Reminder Dialogs, and change view to Dialog Elements.
3.  For the nutrition consult/alert, find the element: VA-VANOD OI SKIN RISK ORDER NUTRITION CONSULT.
4.  Edit this element.
    1.  In the finding item field, enter “Q.” and then the name of your order.
5.  For the wound care consult/alert, find the element VA-VANOD OI WOUND CONSULT and enter the name of the order in the finding item field with a “Q.” in front of the name of the order.

Creating a generic order that doesn’t require provider signature and that sends an alert:

> a\. Create a generic order with a new orderable item.

> When creating the order, answer the prompt for signature required to ORELSE, OREMAS, or NONE. This allows an RN to sign and release, an RN or LVN to sign and release, or allows a user to release the order without a signature.

> The orderable item needs to be unique to this order.

> b\. Go to the CPRS manager options and open the Notifications menu.

> Choose the option to flag orderable items to send notifications. Follow the sequence of steps below twice – once for inpatient as shown, and also for outpatients, since the initial skin assessment could be done prior to admission while the patient is waiting for an admission. The alerts can be sent to an individual, a team, or to a printer (device).

Flag ORDERABLE ITEMS to send Notifications

1\. Flag INPATIENT orders/results/expiring orders.

2\. Flag OUTPATIENT orders/results/expiring orders.

3\. Flag Lab tests for Threshold Exceeded alerts.

Select "1" to flag INPT orders/results, "2" to flag OUTPT orders/results, "3" to set Lab Thresholds: 1

Flag INPATIENT orderable items to send Notifications/Alerts

1\. Flag Inpatient ORDERS.

2\. Flag Inpatient ORDERS for PROVIDER RECIPIENTS.

3\. Flag Inpatient RESULTS.

4\. Flag Inpatient RESULTS for PROVIDER RECIPIENTS.

5\. Flag Inpatient EXPIRING orders.

6\. Flag Inpatient EXPIRING orders for PROVIDER RECIPIENTS.

Select "1 or 2" to flag inpt ORDERS, "3 or 4" to flag inpt RESULTS, "5 or 6" to flag inpt EXPIRING orders: 1

Flag Items to Send INPT ORDER Notifs may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Team (OE/RR) OTL \[choose from OE/RR LIST\]

3 Device DEV \[choose from DEVICE\]

Enter selection: 1 User NEW PERSON

Select NEW PERSON NAME: CRPROVIDER,THREE TC -- XXX/XX STAFF RN

--- Setting Flag Items to Send INPT ORDER Notifs for User: CRPROVIDER,THREE ---

Select Orderable Item: SKIN & WOUND Skin & Wound

Are you adding Skin & Wound as a new Orderable Item? Yes// YES

Orderable Item: SKIN RISK - DIETITIAN// SKIN RISK - DIETITIAN

Send alert for ALL inpatients?: YES

Select Orderable Item:

## Reminder Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Once the new VANOD Skin Assessment reminder dialog is installed and in use, you will be able to build and run multiple reminder reports.
- These reports can be made into user reports for various levels of the staff to use as needed. Some of them could be as follows.

Concurrent Reports: Facility Level

- List of patients with pressure ulcers and stages
- List of patients with pressure ulcers and their Ward locations
- List of patients with hospital acquired pressure ulcers
- List of patients with pressure ulcers and risk factors

List of patients identified at risk by Braden Score (18 or less) without interventions

Retrospective Reports:  
Both National and Facility Levels

Should be as close to real time as possible.

- % of patients with timely assessments
- % of patients with timely reassessments with Braden per risk, on transfer and at discharge
- % of patients assessed at low risk on admission who developed an ulcer
- % of high risk patients who did not develop a pressure ulcer

You can also make multiple reports into one:

- All patients admitted with a Braden score of 18 or less and a stage two or greater pressure ulcer
- All patients admitted with a Braden score of 18 or less and a stage three or greater pressure ulcer

These are just some of the reports that you can make with the various health factors in this reminder dialog. You will be able to develop your own, as needed for your location and your local policies.

These should be developed with input from your nurse leaders, unit managers and wound care nurses.

Exported Health Factors

- BRADEN SCALE 19 OR HIGHER
- BRADEN SCALE 15-18
- BRADEN SCALE 13-14
- BRADEN SCALE 10-12
- BRADEN SCALE 9 OR LOWER
- SKIN INTEGRITY – WOUND
- PRESSURE ULCER
- STAGE I
- STAGE II
- STAGE III
- STAGE IV
- NEW PRESSURE ULCER

  
Steps to add or edit dialog elements:

> a\. Select Dialog management (DM) from the Reminders Manager Menu, then select Dialog (DI):

> Select Reminder Managers Menu Option: DM Reminder Dialog Management

> DP Dialog Parameters ...

> DI Reminder Dialogs

> Select Reminder Dialog Management Option: DI Reminder Dialogs

> <u>Dialog List Aug 30, 2007@09:55:38 Page: 1 of 8</u>

> REMINDER VIEW (ALL REMINDERS BY NAME)

> <u>Item Reminder Name Linked Dialog Name & Dialog Status</u>

> 1 757 NUR ALCOHOL USE SCREEN 757 ALCOHOL USE SCREEN

> 2 757 NUR SEATBELT & ACCIDENT AVOID 757 SEATBELT AND ACCIDENT A

> 3 A A BLOOD EXPOSURE

> 4 A A PAIN VITAL SIGN VA-PAIN SCREEN AND HX

> 5 A NEW REMINDER A NEW REMINDER

> 6 AGETEST AGETEST Disabled

> 7 ALCOHOL USE SCREEN ALCOHOL USE SCREEN DIALOG

> 8 ANDREW TEST OBJECT ANDREW OBJECT

> + Enter ?? for more actions \>\>\>

> AR All reminders LR Linked Reminders QU Quit

> CV Change View RN Name/Print Name

> Select Item: Next Screen//

> b\. Use the Change View (CV) action to see the Dialog View.

> Select Item: Next Screen// CV

> Select one of the following:

> D Reminder Dialogs

> E Dialog Elements

> F Forced Values

> G Dialog Groups

> P Additional Prompts

> R Reminders

> RG Result Group (Mental Health)

> RE Result Element (Mental Health)

> TYPE OF VIEW: R// D

> <u>Dialog List Aug 30, 2007@09:55:38 Page: 1 of 8</u>

> DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)

> <u>Item Reminder Dialog Name Source Reminder Status</u>

> 1 571B SMOKING CESSATION EDUCATI

> 2 571a SMOKING CESSATION EDUCATI

> 3 757 ALCOHOL USE SCREEN 757 NUR ALCOHOL USE SCREE Linked

> 4 757 SEATBELT AND ACCIDENT AVOIDANCE 757 NUR SEATBELT & ACCIDE Linked

> 5 A A PAIN SCREEN AND INTERVENTION \*NONE\*

> 6 A A SG PAIN HISTORY DIA ZZPJH REMINDER

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

> AD Add Reminder Dialog PT List/Print All QU Quit

> CV Change View RN Name/Print Name

> Select Item: Next Screen//

> c\. Use the Search List (SL) action to get to the VANOD–named dialogs, then enter the number of the reminder.

> Select Item: Next Screen// SL SL

> Search for: va-VANOD

> ...searching for 'va-VANOD'.

> <u>Dialog List Aug 30, 2007@09:56:21 Page: 3 of 3</u>

> DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)

> <u>+Item Reminder Dialog Name Source Reminder Status</u>

> 37 VA-VANOD SKIN INITIAL ASSESSMENT VA-VANOD SKIN ASSESSMENT Linked

> 38 VA-VANOD SKIN REASSESSMENT VA-VANOD SKIN REASSESSMEN Linked

> 39 VA-WH MAMMOGRAM REVIEW RESULTS VA-WH MAMMOGRAM REVIEW RE Linked

> 40 VA-WH MAMMOGRAM SCREENING VA-WH MAMMOGRAM SCREENING Linked

> 41 VA-WH PAP SMEAR REVIEW RESULTS VA-WH PAP SMEAR REVIEW RE Linked

> 42 VA-WH PAP SMEAR SCREENING VA-WH PAP SMEAR SCREENING Linked

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

> Find Next 'va-VANOD'? Yes// no

> d\. Select the dialog number to see details, and to enable the dialog.

> Select Item: Quit// 38

> Dialog Edit List Sep 12, 2007@10:03:10 Page: 1 of 19

> REMINDER DIALOG NAME: VA-VANOD SKIN REASSESSMENT \[NATIONAL\] \*LIMITED EDIT\*

> <u>Item Seq. Dialog Summary</u>

> 1 20 Group: VA-VANOD GP BRADEN SKIN RISK REASSESSMENT

> 2 20.5 Element: VA-VANOD TEXT BRADEN SCALE INFO DETAILS

> 3 20.10 Element: VA-VANOD TEXT BRADEN SCORE PREVIOUS

> Suppressed if Reminder Term VANOD BL BRADEN SCALE 30D evaluates

> as FALSE

> 4 20.15 Group: VA-VANOD GP BRADEN SCORE

> 5 20.15.10 Element: VA-VANOD BRADEN 19 OR HIGHER

> 6 20.15.20 Element: VA-VANOD BRADEN 15-18

> 7 20.15.30 Element: VA-VANOD BRADEN 13-14

> + + Next Screen - Prev Screen ?? More Actions \>\>\>

> ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print

> CO Copy Dialog DO Dialog Overview QU Quit

> DD Detailed Display DT Dialog Text

> DP Progress Note Text ED Edit/Delete Dialog

> Select Item: Next Screen// 2

> Select one of the following:

> E Edit

> C Copy and Replace current element

> D Delete element from this dialog

> Select Dialog Element Action: E// dit

> Dialog Element Type: E// lement

> Current dialog element/group name: VA-VANOD TEXT BRADEN SCALE INFO DETAILS

> Used by: VA-VANOD GP BRADEN SKIN RISK ASSESSMENT (Dialog Group)

> VA-VANOD GP BRADEN SKIN RISK REASSESSMENT (Dialog Group)

> NAME: VA-VANOD TEXT BRADEN SCALE INFO DETAILS Replace

> DISABLE:

> CLASS: NATIONAL//

> SPONSOR: Office of Nursing Service//

> REVIEW DATE:

> RESOLUTION TYPE:

> ORDERABLE ITEM:

> FINDING ITEM:

> DIALOG/PROGRESS NOTE TEXT:

> 1\>{FLD:VANOD BRADEN INSTRUCTIONS}

> 2\>{FLD:VANOD BRADEN SCALE INFO}

> 3\> \\

> EDIT Option:

> ALTERNATE PROGRESS NOTE TEXT:

> 1\>

> EXCLUDE FROM PROGRESS NOTE: YES//

> SUPPRESS CHECKBOX: SUPPRESS//

> Select ADDITIONAL FINDINGS:

> RESULT GROUP/ELEMENT:

> Select SEQUENCE:

> REMINDER TERM:

> Input your edit comments.

> Edit? NO//