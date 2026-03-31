---
title: PXRM*2*43 Military Sexual Trauma (MST) Referral Question & Re-Deployment Activation Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Military Sexual Trauma (MST) Referral Question & Re-Deployment Activation
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*43
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](pxrm-2-43-military-sexual-trauma-mst-referral-question-re-deployment-activation-/001.png)
audience: 
keywords: 
  - contents
  - table
  - health
  - install
  - referral
  - reminder
  - pxrm
  - mental
  - screening
  - installation
page_count: 0
word_count: 3242
section_count: 18
table_count: 7
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: JUNE 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_43_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_43_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-43-military-sexual-trauma-mst-referral-question-re-deployment-activation-/001.png)

Military Sexual Trauma Clinical Reminder

Referral Question and Re-Deployment Activation Patch

PXRM\*2.0\*43

INSTALLATION and SETUP GUIDE

JUNE 2015

Product Development

Contents

# <u> </u><u>(Page intentionally left blank)</u>


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [<u> </u><u>(Page intentionally left blank)</u>](#u-uupage-intentionally-left-blanku)
- [<u> </u><u>Introduction</u>](#u-uuintroductionu)
  - [Revisions to the MST Clinical Reminder](#revisions-to-the-mst-clinical-reminder)
  - [Revised MST Clinical Reminder Language](#revised-mst-clinical-reminder-language)
  - [Referral for Mental Health Services Following a Positive MST Screen:](#referral-for-mental-health-services-following-a-positive-mst-screen)
  - [Screening Parameters](#screening-parameters)
- [<u>Pre-Installation:</u>](#upre-installationu)
  - [Pre-installation task: Processing MST-related mental health care referrals](#pre-installation-task-processing-mst-related-mental-health-care-referrals)
  - [## <u>Related Documentation</u>](#urelated-documentationu)
    - [<u>Web Sites</u>](#uweb-sitesu)
- [# <u>Installation</u>](#uinstallationu)
  - [Retrieve the host filefrom one of the following locations (with the ASCII file type):](#retrieve-the-host-filefrom-one-of-the-following-locations-with-the-ascii-file-type)
  - [Install the patch first in a training or test account.](#install-the-patch-first-in-a-training-or-test-account)
  - [Load the distribution.](#load-the-distribution)
  - [Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Install the build.](#install-the-build)
  - [## Install File Print](#install-file-print)
  - [## Build File Print](#build-file-print)
  - [Post-installation routines](#post-installation-routines)
  - [Add local quick order or menu for referrals:](#add-local-quick-order-or-menu-for-referrals)
  - [Assign the VA-MST SCREENING clinical reminder to the coversheet based on local processes. All Primary Care and Mental Health clinics are required to be able to access this reminder.](#assign-the-va-mst-screening-clinical-reminder-to-the-coversheet-based-on-local-processes-all-primary-care-and-mental-health-clinics-are-required-to-be-able-to-access-this-reminder)
- [<u>Appendix A: Installation Examples</u>](#uappendix-a-installation-examplesu)
- [Install Completed<u> Appendix B</u><u>: Acronyms</u>](#install-completedu-appendix-buu-acronymsu)

# <u> </u><u>Introduction</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PXRM\*2.0\*43 Military Sexual Trauma (MST) Clinical Reminder package releases one updated National VHA Clinical Reminder to the field, without any changes to routines, data dictionaries, or other package functions – “content” only.

## Revisions to the MST Clinical Reminder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The revised MST Clinical Reminder aims to

1)  standardize the MST screening and referral process nation wide
2)  facilitate Veteran comfort with the screening process and disclosure
3)  provide an opportunity for Veteran and provider education regarding the definition of MST and the availability of free MST-related care
4)  provide national data to assist in monitoring whether Veterans with a positive MST screen who request a mental health referral are connected with services
5)  re-screen Veterans following additional military service separation. If a previous service separation MST screening was positive, an alternate dialog will be displayed to the provider than if the previous screening was negative. This is done with branching logic functionality in the reminder dialog.

Patch PXRM\*2.0\*43 makes the following dialogue and functionality changes to the existing national MST Clinical Reminder (MST CR) (VA-MST SCREENING):

Dialogue

1.  Addition of an introduction: The introduction informs Veterans that screening is conducted in order to offer free care for all MST-related services. The introduction also indicates that Veteran may decline the MST screen or simply respond with ‘yes’ or ‘no’. Veterans who decline the initial screen are re-screened in one year. 
2.  Revisions to MST screening questions: Minor changes to the screening language of both questions to increase behavioral specificity and to provide examples of experiences such as coercion or inability to consent.  Addition of the adjectives ‘repeated’ and ‘threatening’ to the first screening question to better reflect the language in Public Law 106-117, Section 115. Revision of the abbreviation ‘i.e.’ in the first screening question to the more accurate abbreviation ‘e.g.’
3.  Addition of a mental health care referral question following a positive response to the screening questions to assess a Veteran’s desire for mental health services. 

Functionality

1.  Addition of a link to a printable MST Factsheet for Veterans.
2.  Addition of text that will auto-populate the progress note associated with the MST CR. Auto-populated text provides further information for the provider about MST and free MST-related care.
3.  Revision of the reminder definition to rescreen upon entry of a new DD214 in recognition that Veterans who are re-deployed or otherwise returned to military service are at risk for new MST experiences. This was accomplished by creating a new reminder definition to be used in branching logic term evaluation. The name of the definition is VA-BL MULTIPLE SSD AND MST YES. Reminder term VA-BL MULTIPLE SSD AND MST YES was also created. This term has a mapped item of CF.VA-REMINDER DEFINTION. The CF parameter entry is reminder definition VA-BL MULTIPLE SSD AND MST YES. The condition is set to I V=”DUE NOW”. If this term evaluates as true, the replacement dialog group will be used.
4.  Added FF(4) to check if MST YES REPORTS health factor or positive CF VA-MST status with Y value is more recent than latest service separation date.
5.  Changed Resolution Logic from FI(1)!FI(2)!FI(3) to (FI(1)&FF(4))!(FI(2)&FF(1))!(FI(3)&FF(3))
6.  Changed Cohort Logic from (SEX)&(AGE)&FI(4) to (FI(4))!(FI(4)&FF(2))
7.  Three new health factors added
    1.  VA-MST REQUESTS MH REFERRAL
    2.  VA-MST DECLINE MH REFERRAL
    3.  VA-MST CURRENTLY ENROLLED IN MH

## Revised MST Clinical Reminder Language

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*To ensure the accuracy of national monitoring efforts, NATIONAL HEALTH FACTOR NAMES MAY NOT BE EDITED.* ![](pxrm-2-43-military-sexual-trauma-mst-referral-question-re-deployment-activation-/002.png)

*Now I’m going to ask about some things that may have happened to you while you were in the military. We ask all Veterans these questions because VA offers free care related to these experiences*. *You can decline to answer these questions if you prefer or you may simply say ‘yes’ or ‘no.’ 1. When you were in the military, did you ever receive unwanted, threatening, or repeated sexual attention (for example, touching, cornering, pressure for sexual favors, or inappropriate verbal remarks, etc.)?2. When you were in the military, did you have sexual contact against your will or when you were unable to say no (for example, after being forced or threatened or to avoid other consequences)?*

Please check off the appropriate box below based on the Veteran’s responses to the above questions.

- NO - denies prior military sexual trauma (MST)
  - (answered ‘NO’ to BOTH questions)
- YES - reports military sexual trauma (MST) in the past
  - (answered ‘YES’ to AT LEAST ONE question)
- DECLINE Patient declined to answer question regarding MST

\[IF YES\] *VA refers to this type of experience as ‘military sexual trauma’ or ‘MST’ and VA offers free MST-related care for both physical and mental health concerns. Would you like to speak to a provider about this care?*

Offer MST Factsheet: <http://www.mentalhealth.va.gov/docs/mst_general_factsheet.pdf>

## Referral for Mental Health Services Following a Positive MST Screen:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If Patient reports MST, Mental Health services can or will be offered to the patient. Screen shot below outlines the possible outcomes and health factors entered.

Algorithm if patient responds positively to MST screening

1.  YES veteran requests Mental Health services. HF VA-MST REQUESTS MH REFERRAL is entered into encounter
2.  NO veteran declined a referral for Mental Health services at this time. HF VA-MST DECLINES MH REFERRAL is entered into encounter
3.  NO veteran is currently in treatment with a Mental Health provider. HF VA-MST CURRENTLY ENROLLED IN MH is entered into encounter

![](pxrm-2-43-military-sexual-trauma-mst-referral-question-re-deployment-activation-/003.png)

*Language auto-populated in note:*

> **NOTE:** The Veteran’s subjective experience is sufficient for a positive screen. Verification or additional detail is not necessary. MST can occur on or off base and while a Veteran was on or off duty. Perpetrators can be anyone: men or women, military personnel or civilians, strangers, friends, or intimate partners. Examples of MST include a wide range of unwanted sexual experiences, including offensive behavior or remarks, unwanted sexual attention, or any unwanted sexual touching or other activity that occurred while the Veteran was unable to refuse, coerced (i.e. implied special treatment or hazardous duty or other negative consequences), threatened, or forced. Physical force may or may not be used and compliance does not indicate consent. All health care services (inpatient, outpatient, and pharmaceutical care) for physical and mental health conditions related to MST are provided free of charge.

The handling of mental health referrals is discussed below in the Pre-Installation section. Re-activation of the reminder after re-deployment is described below in the Screening Parameters section.

## Screening Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Cohort: Male and female Veterans of any age
- Frequency: VA-MST SCREENING is completed at least once for all Veterans but varies based upon response and deployment history.
  - Positive Screen: If a Veteran’s initial screen is positive (HF.MST YES REPORTS), the CR is resolved and will not be due again.
  - Decline: If a Veteran declines the initial screen (HF.MST DECLINES TO ANSWER), a decline resolves the MST CR for one year and then the MST CR will be due again.
  - Redeployment activation: If a Veteran has an additional service separation, they should be rescreened. If the previous MST screening was positive, an alternate dialog will be available to the provider. The MST CR will be due again if the date of the most recent screen is earlier than the Veteran’s last Service Separation Date.
- Activation Settings: The MST CR should be assigned according to individual facility guidelines with the following requirements:
  - Active for patients in all primary care and mental health clinics.
  - Must be completed by appropriate clinical providers. 
- This reminder is resolved:
  - For one year by a health factor indicating that the MST CR was completed and the screen is decline: MST DECLINES TO ANSWER
  - Permanently by a health factor indicating that the MST CR was completed, the screen is negative, and the MST CR occurred after the Veteran’s last Service Separation Date: MST NO DOES NOT REPORT
  - Permanently[^1] by a health factor indicating that the MST CR was completed and the screen is positive: MST YES REPORTS

# <u>Pre-Installation:</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing the MST CR revision patch, facilities will determine how MST-related mental health care referrals will be processed (Pre-installation task 1 below). This information should have been communicated to the CAC and the MST Coordinator. The name and contact information for your facility’s MST Coordinator can be found here: <https://vaww.portal.va.gov/sites/mst_community/section_pages/People-Finder/Find-MST-Coordinators.aspx>

## Pre-installation task: Processing MST-related mental health care referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Facilities will differ on how the referral request is handled but all Veterans who request mental health services should be connected to care in a timely manner. It is recommended that facilities use the same mental health referral process for the MST Clinical Reminder as is used for other positive mental health clinical reminders.

*Warm Hand-Off*: The majority of screening will be completed in primary care settings and within the Patient Aligned Care Teams (PACT). When a Veteran screens positive for MST and requests a referral for MST-related mental health services, primary care team members are encouraged to provide a warm hand-off to a mental health provider, which may or may not include a consult. <u>If a mental health provider is not available for a warm hand-off, the PACT team member who completed the screener should follow the procedure supported in the referral question, such as generating a consult or contacting the party who will receive the referral.</u>

*The clinical reminder must include a method for processing a mental health care referral request when a warm hand-off is not feasible.* Two common options are reviewed below: adding an order menu that will generate a consult or providing the referral contact information.

*Option 1: Generate Consult*

If a referral request will be addressed by ordering a consultation, facility leadership will decide which individual/team/clinic will receive the consult request. Common options are listed below but this list is not exhaustive.

Option 1a: ORDER CONSULT to a general or specialty mental health clinic

Option 1b: ORDER CONSULT to MST Coordinator. If consults will be sent to the MST Coordinator, it is recommended that the MST Coordinator is provided additional full-time equivalent (FTE)/unscheduled clinical time to manage this responsibility in addition to their other MST Coordinator duties (in addition to FTE for typical MST Coordinator duties). The appropriate amount of additional FTE will vary depending on facility size and number of Veterans who screen positive for MST and request a referral.

*Option 2: Order menu text box with referral contact information*

A referral request may also be addressed by adding an order menu text box that lists the contact information of the person or clinic who will receive the referral information. See post-installation instructions below.

<u>Required Software for PXRM\*2\*43</u>

|                    |               |             |               |
|--------------------|---------------|-------------|---------------|
| Package/Patch  | Namespace | Version | Comments  |
| Clinical Reminders | PXRM          | 2.0         | Fully patched |
| Health Summary     | GMTS          | 2.7         | Fully patched |
| Kernel             | XU            | 8.0         | Fully patched |
| VA FileMan         | DI            | 22          | Fully patched |

## ## <u>Related Documentation</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                              |                             |
|------------------------------|-----------------------------|
| Documentation            | Documentation File name |
| Installation and Setup Guide | PXRM_2_0_43_IG.PDF          |

### <u>Web Sites</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                       |                                                           |                                                                                            |
|---------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Site                              | URL                                                   | Description                                                                            |
| National Clinical Reminders site      | <http://vista.med.va.gov/reminders>                       | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | <http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx> | This committee directs the development of new and revised national reminders               |
| VistA Document Library                | <http://www.va.gov/vdl/>                                  | Contains manuals for Clinical Reminders                                                    |
| MST Resource Homepage                 | [http://vaww.mst.va.gov](http://vaww.mst.va.gov/)         | Contains education materials for providers on the revised MST Clinical Reminder            |

# # <u>Installation</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 1-2 minutes

## *Retrieve the host filefrom one of the following locations (with the ASCII file type):* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Albany <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Salt Lake City <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

## *Install the patch first in a training or test account.* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

## *Load the distribution.* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name. KID at the Host File prompt.

Example

Use INSTALL NAME: PXRM\*2.0\*43 to install this Distribution. Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File:

KIDS Distribution saved on Feb 21, 2014@09:16:46

Comment: MST Screening

This Distribution contains Transport Globals for the following Package(s):

PXRM\*2.0\*43

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

PXRM\*2.0\*43

Use INSTALL NAME: PXRM\*2.0\*43 to install this Distribution.

  
From the Installation menu, you may elect to use the following options:

## *Backup a Transport Global* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

## *Compare Transport Global to Current System*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

## *Install the build.*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*43 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: PXRM\*2.0\*43

Answer "NO" to the following prompts:

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Installation Example

> See [Appendix A](\l).

## ## *Install File Print* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

> Select Utilities Option: Install File Print

> Select INSTALL NAME: PXRM\*2.0\*43

## ## *Build File Print* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print

> Select BUILD NAME: PXRM\*2.0\*43

> DEVICE: HOME//

## *Post-installation routines*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After successful installation, the following init routines may be deleted:

> PXRMP43E

> PXRMP43I

<u>Post-Install Set-up Instructions</u>*The national dialog and component elements and groups may only be appended; none of the national dialog or component elements can be deleted. NATIONAL HEALTH FACTOR NAMES MAY NOT BE EDITED. THIS DIRECTLY IMPACTS MONITORING OF MST SCREENING AND MST-RELATED CARE.*

During our testing, we found that sites may have local copies of MST dialog elements or groups embedded in local templates.  The following problems may arise after the new MST dialog is installed:

1.  New health factors may not be added to the encounter form from the local dialog; thus Veterans may not be asked if they would like a referral for MST-related services or their referral choice will not be accurately captured within national data
2.  Exclusion of new branching logic to give alternate text based on multiple service separations

Our recommendation is to identify your local templates that contain local copies of the current MST dialog components and replace them with the updated MST dialog components.  If you need assistance in identifying any local dialogs that contain MST copied components, please enter a national remedy/CA ticket.

VA-MST SCREENING Reminder: After the installation of patch PXRM\*2.0\*43, do the following steps to set up the VA-MST Screening reminder.

## Add local quick order or menu for referrals:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These edits will vary based on your facility’s determination of how MST-related mental health care referrals will be addressed. The instructions for two common options are below.

*Option 1: Generate consult*

When your facility has decided which individual/team/clinic will receive the referral for MST-related care, the local CAC must amend the MST Clinical Reminder to add this functionality. The local CAC can create a quick order in VistA for a consult. Quick order or menu can be added as a finding to the dialog group: VA-MST REQUESTS MH REFERRAL. <span class="mark">If your site has multiple locations/consults for referral, you will need to create an order menu and attach that to the dialog element</span>.

*Option 2: Order menu text box with referral contact information*

As discussed above, the referral request may also be addressed by adding an order menu text box (Generic Order) that lists the contact information of the person or clinic who will receive the referral.

\*If your site determines that the MST Coordinator should receive all referrals, it is recommended that the MST Coordinator is provided additional FTE to manage this responsibility in addition to their other MST Coordinator duties. The appropriate amount of additional FTE will vary depending on facility size and number of Veterans who screen positive for MST and request a referral for mental health services.

## Assign the VA-MST SCREENING clinical reminder to the coversheet based on local processes. All Primary Care and Mental Health clinics are required to be able to access this reminder.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>Appendix A: Installation Examples</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: Load a Distribution

Enter a Host File: VA16\$:\[SMAVISTA.KRUSEJ\]PXRM_2_0_43.KID;1

KIDS Distribution saved on Jun 03, 2015@12:03:25

Comment: MST SCREENING

This Distribution contains Transport Globals for the following Package(s):

Build PXRM\*2.0\*43 has been loaded before, here is when:

PXRM\*2.0\*43 Install Completed

was loaded on Feb 21, 2014@09:30:04

PXRM\*2.0\*43 Install Completed

was loaded on Jan 22, 2015@14:22:07

PXRM\*2.0\*43 Install Completed

was loaded on Feb 11, 2015@14:25:36

PXRM\*2.0\*43 Install Completed

was loaded on Mar 12, 2015@10:28:28

PXRM\*2.0\*43 Install Completed

was loaded on Mar 25, 2015@14:22:46

PXRM\*2.0\*43 Install Completed

was loaded on Jun 03, 2015@12:06:11

PXRM\*2.0\*43 Install Completed

was loaded on Jun 03, 2015@12:12:10

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

PXRM\*2.0\*43

Use INSTALL NAME: PXRM\*2.0\*43 to install this Distribution.

Select Installation \<TEST ACCOUNT\> Option: Install Package(s)

Select INSTALL NAME: PXRM\*2.0\*43 7/6/15@08:10:55

=\> MST SCREENING ;Created on Jun 03, 2015@12:03:25

This Distribution was loaded on Jul 06, 2015@08:10:55 with header of

MST SCREENING ;Created on Jun 03, 2015@12:03:25

It consisted of the following Install(s):

PXRM\*2.0\*43

Checking Install for Package PXRM\*2.0\*43

Install Questions for PXRM\*2.0\*43

Incoming Files:

811.8 REMINDER EXCHANGE (including data)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;99 SSH Virtual Terminal

PXRM\*2.0\*43



Installing Data:

Jul 06, 2015@08:12:54

Running Post-Install Routine: POST^PXRMP43I

There are 1 Reminder Exchange entries to be installed.

1\. Installing Reminder Exchange entry VA-MST SCREENING PXRM\*2\*43

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*43 Installed.

Jul 06, 2015@08:13:06

Not a production UCI

NO Install Message sent





100%  25 50 75 

Complete 

# Install Completed<u> Appendix B</u><u>: Acronyms</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OIT Master Glossary is available at <http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm>

| Term     | Definition                                                      |
|----------|-----------------------------------------------------------------|
| ASU      | Authorization/Subscription Utility                              |
| CAC      | Clinical Application Coordinator                                |
| Clin4    | National Customer Support team that supports Clinical Reminders |
| CPRS     | Computerized Patient Record System                              |
| FTE      | Full-time equivalent                                            |
| GUI      | Graphic User Interface                                          |
| HIS      | Health Information Specialist                                   |
| IRM      | Information Resources Management                                |
| LSSD     | Last Service Separation Date                                    |
| MH       | Mental Health                                                   |
| MHS      | Mental Health Services                                          |
| MHTC     | Mental Health Treatment Coordinator                             |
| MST      | Military Sexual Trauma                                          |
| OHI      | Office of Health Information                                    |
| OI       | Office of Information                                           |
| OIT/OI&T | Office of Information Technology                                |
| PACT     | Patient Aligned Care Team                                       |
| PCS      | Patient Care Services                                           |
| PXRM     | Clinical Reminder Package namespace                             |
| RSD      | Requirements Specification Document                             |
| SQA      | Software Quality Assurance                                      |
| VA       | Department of Veteran Affairs                                   |
| VHA      | Veterans Health Administration                                  |
| VISN     | Veterans Integrated Service Network                             |
| VistA    | Veterans Health Information System and Technology Architecture  |

[^1]: MST Clinical Reminder can be manually updated by a provider and the Reminder is resolved.