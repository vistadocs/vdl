---
title: PXRM*2*55 Pneumococcal Update Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Pneumococcal Update
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*55
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - class
  - table
  - bookmark
  - span
  - reminder
  - transport
  - global
  - mark
  - contents
  - install
page_count: 0
word_count: 1123
section_count: 3
table_count: 5
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: January 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_55_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_55_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-55-pneumococcal-update-installation-guide/001.png)

> Pneumococcal Reminders update

> PXRM\*2.0\*55

> INSTALLATION and SETUP GUIDE

> January 2015

> Product Development Department of Veterans Affairs

> <u>Contents</u>

1.  [Retrieve the host file from one of the following locations (with the ASCII file type) 9](#_bookmark7)
2.  [Install the patch first in a training or test account 9](#_bookmark8)
3.  [Load the distribution. 9](#_bookmark9)
4.  [Backup a Transport Global 9](#_bookmark10)

[a. Compare Transport Global to Current System 10](#_bookmark11)

5.  [Install the build. 10](#_bookmark12)
6.  [Install File Print 10](#_bookmark13)
7.  [Build File Print 11](#_bookmark14)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Required Software for PXRM\2\55](#required-software-for-pxrm255)
  - [Related Documentation](#related-documentation)
    - [The installation needs to be done by a person with DUZ(0) set to "@."](#the-installation-needs-to-be-done-by-a-person-with-duz0-set-to)
- [<u>Acronyms</u>](#uacronymsu)
> Description:
> In August 2014, the Advisory Committee on Immunization Practices (ACIP) updated recommendations for use of PCV13 to include patients age 65 and over. This patch updated the existing reminders to include that new recommendation. The spacing between a dose of PCV13 and PPSV23 is now recommended to be 6 months (8 weeks minimum but preferably 6 months). Pneumococcal vaccine-naïve persons. ACIP recommends that adults aged \>=19 years with immunocompromising conditions, functional or anatomic asplenia, CSF leaks, or cochlear implants, and who have not previously received PCV13 or PPSV23, should receive a dose of PCV13 first, followed by a dose of PPSV23 at least 8 weeks later (Table). Subsequent doses of PPSV23 should follow current PPSV23 recommendations for adults at high risk. Specifically, a second PPSV23 dose is recommended 5 years after the first PPSV23 dose for persons aged 19- 64 years with functional or anatomic asplenia and for persons with immunocompromising conditions. Additionally, those who received PPSV23 before age 65 years for any indication should receive another dose of the vaccine at age 65 years, or later if at least 5 years have elapsed since their previous PPSV23 dose. Previous vaccination with PPSV23. Adults aged
> \>=19 years with immunocompromising conditions, functional or anatomic asplenia, CSF leaks, or cochlear implants, who previously have received \>=1 doses of PPSV23 should be given a PCV13 dose \>=1 year after the last PPSV23 dose was received. For those who require additional doses of PPSV23, the first such dose should be given no sooner than 8 weeks after PCV13 and at least 5 years after the most recent dose of PPSV23.
This patch does the following during installation:
1.  Updates the existing reminder definitions:
> VA-PNEUMOCOCCAL IMMUNIZATION PPSV23 VA-PNEUMOCOCCAL IMMUNIZATION PCV13 VA-OB PNEUMOCOCCAL PPSV23 INDICATIONS VA-OB PNEUMOCOCCAL PCV13 INDICATIONS
2.  Updates the existing reminder Dialogs
> VA-PNEUMOCOCCAL IMMUNIZATION PPSV23 PNEUMOVAX VA-PNEUMOCOCCAL IMMUNIZATION PCV13 PREVNAR
3.  Updates the existing Taxonomies if not already done by PXRM\*2\*50: VA-PNEUMOC DZ RISK - HIGHEST/NOT IMMUNO COMP
> VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED VA-PNEUMOC DZ RISK - HIGH
> VA-PNEUMOC DZ RISK - CHEMOTHERAPY (includes drug classes and drugs)
> Updates made in this patch:
> PCV13 due for over 65; PPSV23 not applicable over age 65 until PCV13 is given and 6 months has passed unless the patient has a contraindication/other reason to not get PCV13. Text information for PCV13 over 65 added
> PCV13 ‘incorrect diagnosis’ option now suppressed for over 65 just like that option is for PPSV23
> Finding 10 in PPSV23 now turns off the reminder in all cases for 6 months. Wait 6 months after PCV13 to give any dose of PPSV23
> Drug statuses have been added to chemotherapy to include any administration of drug in the past 6 months in order to make MHV and PCV13/PPSV23 the same
> Removed 1 M due in advance
> Pneumococcal indications – fixed a bug where the time periods in the object were different than in the reminder - use same time period on object as is in the reminder
> PCV 13 Object from changed to IC 4y 2y
> Highest 4y 10y
> Chemo drugs 90D 6M
> PPV23 Object
> Chemo drugs 90D 6M
> Added text related to requiring documentation of prior vaccines before recording them
> How the reminders work:
1.  Only see one reminder at a time – never both
2.  Counts the number of PPSV23 doses given either by counting doses recorded or looking for a ‘SERIES’ marked as booster, 2, 3 or 4.
3.  If the PCV13 immunization is needed, then the PPSV23 is NA.
4.  If PCV13 is given, contraindicated or not indicated, then the PPSV23 reminder is applicable unless
    1.  PCV13 was given in the past 6 months or
    2.  The patient has already received PPSV23 and is not yet due again, or
    3.  Has a contraindication/allergy recorded.
5.  The PPSV23 reminder takes into account:
    1.  Diagnoses that would require a 2<sup>nd</sup> dose after 5 years
    2.  Age so that a dose is given after age 65
6.  If PPSV23 has been given in the past year and the patient should get PCV13, the PCV13 reminder will not come due until one year after the most recent PPSV23
7.  Logic for PPSV23:
> Taxonomies that are used in the logic:
- IC: immunocompromised (HIV, renal failure, nephrotic syndrome, splenic dysfx, etc.
- Highest Risk= HstR: cochlear implant, CSF leak
- High Risk=HR - Other Diagnoses: (cardiac, pulmonary, smoking, liver disease)
- Chemo=CH : taxonomy and drugs
- LTS=Long term steroids
> Included in the COHORT if:
1.  (IC or HstR or CH or LTS or Age \>64) and either already got PCV13 but not in the past 6 months or has contraindication to PCV13
2.  Other dx or age\>64 and not IC/HstR/CH/LTS or has contraindication to PCV13
> Baseline frequencies
<table>
<colgroup>
<col style="width: 66%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>1. &gt;65</p>
<p>2. IC</p></th>
<th><p>99Y</p>
<p>5Y</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3. HstR</td>
<td>99Y</td>
</tr>
<tr class="even">
<td>4. HR</td>
<td>99Y</td>
</tr>
<tr class="odd">
<td>5. LTS</td>
<td>5Y</td>
</tr>
<tr class="even">
<td>6. CH</td>
<td>5Y</td>
</tr>
</tbody>
</table>
> Function Findings 1,2,3,8 Frequency Rank
> 3 no dose \>64, IC/CH/LTS and no 2nd dose 5Y 2
> 8 \>age 64, IC/CH/LTS, has PCV13, no dose\>64 5Y 2
> \*2 doses are counted only if given more than 1460 days apart (4Y) or one is marked as a booster dose.
> For IC/CH/LTS: FF 1,2,3,8
> FF3 above can be explained this way - Patient is IC and has had a dose before age 65, needs a second dose 5 years later. FF(3) is true and the reminder is due 5Y after the recorded dose.
> If that second dose is given, then FF(1) takes over and the reminder is resolved (99Y).
> If the patient turns 65, then FF(8) is true and the reminder is due again 5Y after the last dose. Once that dose after age 65 is given, then FF(2) takes over and the reminder is resolved (99Y).
> Function Findings 2,4,6 Frequency Rank
| 2 \>age 64 and 1 dose after age 64:           | 99Y | 1   |
|-----------------------------------------------|-----|-----|
| 4 \>age 64,dosed \<65, no dose\>64, not IC/CH | 5Y  | 2   |
| 6 (HR or Other dx) not IC/CH and \<age 65:    | 99Y | 3   |
> For not IC/CH/LTS: FF 6,4
> Baseline dose due for HR and HstR, FF6 sets for patients \<age 65 who are not IC/CH/LTS. Once they turn 65, then FF4 is applicable and the reminder is due 5 years after the prior dose. Once a dose is given after age 65,
> then FF2 is applicable and any dose after age 65 will resolve.
> Resolution: PPSV23 or deferral or an order
> Function Findings 5, 7, 10, 16, 17, 18, 19, 20
> FF5 provides a message about the need for an additional dose after age 65 if the patient's most recent dose was prior to age 65 for non-IC/CH/LTS patients.
> FF7 provides a message about the need for an additional dose after age 65 for IC/CH/LTS patients who have already gotten PCV13.
> FF10 assesses the last 2 doses of pneumococcal vaccine to be sure that they were more than 4 years apart
> FF16, 17, 18 and 19 look at finding 16 and evaluate to see if it is an ICD code, an outpatient drug or a non-intravitreal administration of a chemotherapy drug.
> FF20 provides a message if PCV13 is needed. This is just in case someone looks at this reminder to see why it is NOT due.
> Long Term steroids is set up in a local reminder term and a local reminder in order to allow sites to modify this option. This was done since there is not a clear consensus on how to best identify these patients or to define long term steroid use and pharmacy practices in how the day’s supply is recorded may vary.
> Map local dosage formulations to the reminder term: STEROIDS - PNEUMOCOCCAL DZ RISK (see post install instructions).
> Once those are mapped, a reminder LONG TERM STEROID USE evaluates the recent fills of steroid to identify patients with long term use. This reminder defines long term use as:
1.  any fill that is marked with a day’s supply of \>70 days
2.  or 3 recent fills each with a day’s supply of \>21 days.
> The CDC Guidance on the amount of steroid use that causes a level of immunosuppression sufficient to warrant pneumococcal immunization is two weeks on
> every-day dosing of corticosteroids of at least 20 mg/day or 2 mg/kg/day. However, higher thresholds were chosen for these reminders because there were many false positives included in the reminder cohort logic when looking for shorter durations or fewer fills. Patients who received one or 2 recent tapers of steroids that were of short duration (7-14 days) were identified and included incorrectly in the cohort if only one fill was used because even though the patient got only a limited duration of steroid, the day’s supply was marked as 30 days.
> Local sites can modify this reminder or map some other entry to the term that is used in the pneumococcal reminder logic if needed. This reminder is used in the term: VA-PNEUMOC DZ RISK - LONG TERM STEROIDS.
> <span id="_bookmark1" class="anchor"></span><u>Pre-Installation</u>

## Required Software for PXRM\*2\*55

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Package/Patch        | Namespace | Version | Comments  |
|--------------------------|---------------|-------------|---------------|
| Clinical Reminders       | PXRM          | 2.0         | Fully patched |
| Health Summary           | GMTS          | 2.7         | Fully patched |
| Kernel                   | XU            | 8.0         | Fully patched |
| NATIONAL DRUG FILE       | PSN           | 4.0         | Fully patched |
| Pharmacy Data Management | PSS           | 1.0         | Fully patched |
| Outpatient Pharmacy      | PSO           | 7.0         | Fully patched |
| VA FileMan               | DI            | 22          | Fully patched |
| PCE                      | PX            | 1.0         | Fully patched |

## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Documentation            | Documentation File name |
|------------------------------|-----------------------------|
| Installation and Setup Guide | PXRM_2_0_55_IG.PDF          |

> <span id="_bookmark4" class="anchor"></span>Web Sites

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 36%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site</strong></th>
<th><strong>URL</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>National Clinical Reminders site</td>
<td><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></td>
<td><p>Contains manuals, PowerPoint presentations, and other information</p>
<p>about Clinical Reminders</p></td>
</tr>
<tr class="even">
<td>National Clinical Reminders Committee</td>
<td><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/ncrc</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>public/default.aspx</u></a></td>
<td><p>This committee directs the</p>
<p>development of new and revised national reminders</p></td>
</tr>
<tr class="odd">
<td><p>VistA Document</p>
<p>Library</p></td>
<td><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></td>
<td><p>Contains manuals for Clinical</p>
<p>Reminders and</p></td>
</tr>
</tbody>
</table>

1.  Do a reminder inquiry on both the reminders VA-PNEUMOCOCCAL IMMUNIZATION PPSV23 and VA-PNEUMOCOCCAL IMMUNIZATION PCV13 and save this as a reference for post installation
2.  Check the dialog elements for quick orders for the immunizations and record those entries so they can be re-entered after installation:

> OI PNEUMOC PCV13 OUTPT SHORT OI PNEUMOC PPSV23 OUTPT

> <span id="_bookmark5" class="anchor"></span><u>Installation</u>

> <span id="_bookmark6" class="anchor"></span>*This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes*

### The installation needs to be done by a person with DUZ(0) set to "@."

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  <span id="_bookmark7" class="anchor"></span>Retrieve the host file from one of the following locations (with the ASCII file type):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Albany</p>
</blockquote></th>
<th><mark>REDACTED</mark></th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

2.  <span id="_bookmark8" class="anchor"></span>Install the patch first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

3.  <span id="_bookmark9" class="anchor"></span>Load the distribution.

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name. KID at the Host File prompt.

> Example

> From the Installation menu, you may elect to use the following options:

4.  <span id="_bookmark10" class="anchor"></span>Backup a Transport Global

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

1.  <span id="_bookmark11" class="anchor"></span>Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

5.  <span id="_bookmark12" class="anchor"></span>Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*55 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompts:

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> NOTE: DO NOT QUEUE THE INSTALLATION, because this installation asks questions requiring responses and queuing will stop the installation.

> Installation Example

> See [<u>Appendix A</u>](#_bookmark16).

6.  <span id="_bookmark13" class="anchor"></span>Install File Print

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.

7.  <span id="_bookmark14" class="anchor"></span>Build File Print

> Use the KIDS Build File Print option to print out the build components.

> <span id="_bookmark15" class="anchor"></span>Post-Install Set-up Instructions

1.  Check the mapping of the reminder terms in the reminder definitions by comparing the reminder inquiry that was save prior to installation with a reminder inquiry post-install.
2.  Check the reminder terms for the 2 immunizations and include any local entries. The national entries for these 2 immunizations are included:

> PNEUMOCOCCAL CONJUGATE PCV 13 PNEUMOCOCCAL POLYSACCHARIDE PPV23

3.  Check that the order dialogs are present in the 2 reminder dialog elements for ordering the immunizations from the pre-install steps.
4.  The order option in the dialog can be suppressed for specific user classes or for everyone using the reminder terms:

> VA-PNEUMOC PCV13 ORDER SUPPRESSION VA-PNEUMOC PPSV23 ORDER SUPPRESSION

1.  To suppress for specific user classes, in the above Terms configure the VA-ASU USER CLASS computed finding and DELETE the VA-AGE finding. NOTE: If the Age finding is not deleted, the user class settings will not work.

> VA-ASU USER CLASS

> Enter the user class in the Computed Finding Parameter field that should NOT see the option to order the pneumococcal vaccines.

> If more than one user class is needed, add additional findings of the CF VA-ASU USER CLASS for each one as needed.

2.  To suppress for EVERYONE, in the above TERMS DELETE the VA-ASU USER CLASS finding and edit the VA-AGE computed finding.

> VA-AGE

> To suppress the order from being seen by ANYONE, delete the Condition within the VA-AGE computed finding.

5.  2 Template fields are used for Lot \#s and expiration dates. They are exported as EDIT BOXES, for free text entry. Sites may choose to change the TYPE to a COMBO box and then populate the template fields with local lot \#s and expiration dates. Verify that these are still set up to your sites preference

> IM PCV13 LOT# EXP DATE IM PPSV23 LOT# EXP DATE

> Changing the type is done in CPRS under Template Editor on the Notes Tab.

> ![](pxrm-2-55-pneumococcal-update-installation-guide/002.png)

> <span id="_bookmark16" class="anchor"></span><u>Appendix A: Installation Example</u>

> Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: Installation

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution Enter a Host File: *\<your directory name\>*PXRM_2_0_55.KID

> KIDS Distribution saved on Dec 22, 2014@13:11:40 Comment: PNEUMOCOCCAL REMINDERS UPDATE

> This Distribution contains Transport Globals for the following Package(s): Build PXRM\*2.0\*55 has been loaded before, here is when:

> PXRM\*2.0\*55 Install Completed

> was loaded on Nov 20, 2014@13:17:41 PXRM\*2.0\*55 Install Completed

> was loaded on Dec 22, 2014@13:54:50 PXRM\*2.0\*55 Install Completed

> was loaded on Dec 23, 2014@13:48:32 OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// Loading Distribution...

> PXRM\*2.0\*55

> Use INSTALL NAME: PXRM\*2.0\*55 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: INstall Package(s) Select INSTALL NAME: PXRM\*2.0\*55 1/29/15@07:21:06

> =\> PNEUMOCOCCAL REMINDERS UPDATE ;Created on Dec 22, 2014@13:11:40

> This Distribution was loaded on Jan 29, 2015@07:21:06 with header of PNEUMOCOCCAL REMINDERS UPDATE ;Created on Dec 22, 2014@13:11:40

> It consisted of the following Install(s):

> PXRM\*2.0\*55

> Checking Install for Package PXRM\*2.0\*55 Install Questions for PXRM\*2.0\*55 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// TELNET PORT

> PXRM\*2.0\*55

> 

> 

> Installing Data:

> Jan 29, 2015@07:21:24

> Running Post-Install Routine: POST^PXRMP55I

> There are 1 Reminder Exchange entries to be installed.

> 1\. Installing Reminder Exchange entry PATCH PXRM\*2\*55 PNEUMOCOCCAL UPDATE Updating Routine file...

> Updating KIDS files...

> PXRM\*2.0\*55 Installed.

> Jan 29, 2015@07:25:07

> 

> 

> 100%  25 50 75 

> Complete 

# <u>Acronyms</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The OIT Master Glossary is available at [<u>http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm</u>](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)

| Term   | Definition                                                  |
|------------|-----------------------------------------------------------------|
| ASU        | Authorization/Subscription Utility                              |
| Clin4      | National Customer Support team that supports Clinical Reminders |
| CPRS       | Computerized Patient Record System                              |
| DBA        | Database Administration                                         |
| DG         | Registration and Enrollment Package namespace                   |
| ESM        | Enterprise Systems Management (ESM)                             |
| FIM        | Functional Independence Measure                                 |
| GMTS       | Health Summary namespace (also HSUM)                            |
| GUI        | Graphic User Interface                                          |
| HRMH/HRMHP | High Risk Mental Health Patient                                 |
| IAB        | Initial Assessment & Briefing                                   |
| ICD-10     | International Classification of Diseases, 10th Edition          |
| ICR        | Internal Control Number                                         |
| IOC        | Initial Operating Capabilities                                  |
| LSSD       | Last Service Separation Date                                    |
| MH         | Mental Health                                                   |
| MHTC       | Mental Health Treatment Coordinator                             |
| OHI        | Office of Health Information                                    |
| OI         | Office of Information                                           |
| OIF/OEF    | Operation Iraqi Freedom/Operation Enduring Freedom              |
| OIT/OI&T   | Office of Information Technology                                |
| OMHS       | Office of Mental Health Services                                |
| ORR        | Operational Readiness Review                                    |
| PCS        | Patient Care Services                                           |
| PD         | Product Development                                             |
| PIMS       | Patient Information Management System                           |
| PMAS       | Program Management Accountability System                        |

| Term | Definition                                                 |
|----------|----------------------------------------------------------------|
| PTM      | Patch Tracker Message                                          |
| PXRM     | Clinical Reminder Package namespace                            |
| RSD      | Requirements Specification Document                            |
| SD       | Scheduling Package Namespace                                   |
| SQA      | Software Quality Assurance                                     |
| USR      | ASU package namespace                                          |
| VA       | Department of Veteran Affairs                                  |
| VHA      | Veterans Health Administration                                 |
| VISN     | Veterans Integrated Service Network                            |
| VistA    | Veterans Health Information System and Technology Architecture |