---
title: PXRM*2*28 Women's Health Clinical Reminder Updates Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Women's Health Clinical Reminder Updates
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*28
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: > Patch PXRM\2.0\28 is the second patch to the Clinical Reminder package that uses the recently-approved expedited patch process. The patch releases one new and five updated National VHA reminders to the field, without any changes to routines, data dictionaries, or other package functions – “content
audience: 
keywords: 
  - reminder
  - screening
  - women
  - table
  - years
  - contents
  - health
  - installation
  - cancer
  - smear
page_count: 0
word_count: 2435
section_count: 3
table_count: 4
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: June 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_28_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_28_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-28-women-s-health-clinical-reminder-updates-installation-guide/001.png)

# Women’s Health Clinical Reminder Updates


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Women’s Health Clinical Reminder Updates](#womens-health-clinical-reminder-updates)
- [INSTALLATION and SETUP GUIDE](#installation-and-setup-guide)
  - [Introduction](#introduction)
- [Pre-Installation](#pre-installation)
    - [Required Software for PXRM\2\28](#required-software-for-pxrm228)
    - [Related Documentation](#related-documentation)
- [Installation](#installation)
- [Post-Install Set-up Instructions](#post-install-set-up-instructions)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [Appendix B: Default Outside Location](#appendix-b-default-outside-location)
  - [Acronyms](#acronyms)
> PXRM\*2.0\*28

# INSTALLATION and SETUP GUIDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> June 2013

> Product Development Department of Veterans Affairs

> <u>Contents</u>

1.  [Retrieve the host file containing from one of the following locations 14](#1._Retrieve_the_host_file_from_one_of_th)
2.  [Install the build first in a training or test account. 14](#2._Install_the_patch_first_in_a_training)
3.  [Load the distribution. 14](#load-the-distribution.)
    1.  [Backup a Transport Global 14](#backup-a-transport-global)
    2.  [Compare Transport Global to Current System 14](#compare-transport-global-to-current-system)
    3.  [Verify Checksums in Transport Global 15](#verify-checksums-in-transport-global)
4.  [Install the build. 15](#install-the-build.)
5.  [Install File Print 15](#install-file-print)
6.  [Build File Print 16](#build-file-print)
7.  [Post-installation routines 16](#post-installation-routines)

[Post-Install Set-up Instructions 17](#post-install-set-up-instructions)

[Appendix A: Installation Example 19](#appendix-a-installation-example)

[Appendix B: Default Outside Location](#_bookmark19) 22

[Acronyms 25](#acronyms)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PXRM\*2.0\*28 is the second patch to the Clinical Reminder package that uses the recently-approved expedited patch process. The patch releases one new and five updated National VHA reminders to the field, without any changes to routines, data dictionaries, or other package functions – “content” only. The six reminders (6) reminders are:

1.  VA-WH DISCUSS BREAST CA SCREEN WOMAN 40-49 (new)
2.  VA-WH MAMMOGRAM SCREENING (updated)
3.  VA-MHV MAMMOGRAM SCREENING (updated)
4.  VA-WH PAP SMEAR SCREENING (updated)
5.  VA-WH PAP SMEAR REVIEW RESULTS (updated)
6.  VA-MHV CERVICAL CANCER SCREENING (updated)
7.  VA-BREAST TUMOR Taxonomy (updated)
8.  VA-WH MAMMOGRAM REVIEW RESULTS (dialog updated only) BREAST CANCER REMINDERS

> These reminders implement VHA clinical guidance related to breast cancer screening as defined in the VHA Breast Cancer Screening Clinical Preventive Services Guidance Statement ([<u>http://vaww.prevention.va.gov/Screening_for_Breast_Cancer.asp</u>](http://vaww.prevention.va.gov/Screening_for_Breast_Cancer.asp)):

- “The decision to start regular screening every 2 years with mammography for average risk women age 40 to 49 years should be an individual decision and take the patient's values into account including values about specific benefits and harms.”
- “VHA recommends screening for breast cancer with mammography every 2 years for average risk women age 50-74.”
- “The VHA neither recommends for or against screening for breast cancer for women age 75 and older. The current evidence is insufficient to assess the balance of benefits and harms of screening for breast cancer with mammography in women age 75 and older. If screening for breast cancer with mammography is offered, patients should understand the uncertainty about the balance of benefits and harms.”
- “The VHA neither recommends for or against clinician breast exam for breast cancer screening. The current evidence is insufficient to assess the additional benefits and harms of clinical breast examination beyond mammography for breast cancer screening.”

> VA-WH DISCUSS BREAST CA SCREEN WOMAN 40-49 is a new reminder that was developed to prompt a discussion between women 40-49 and their providers about when to start breast cancer screening. Health factors indicating that the woman either wants to begin screening in her 40’s or wants to wait until she is 50 to begin screening are generated as a result of documenting the discussion. Options were also included to defer the discussion and to allow providers to resolve the reminders if the patient is not expected to experience a net benefit from

> breast cancer screening because of less than 5 year life expectancy and/or patient could not tolerate the further work-up or treatment (if the screen was positive) because of co- morbidities.

- This reminder applies to women ages 40-49. Women who a documented life expectancy of 6 months or less or to women with a diagnosis of terminal cancer of the esophagus, pancreas or liver are excluded from the cohort.
- Frequency: The frequency is 99Y (once) for a one-time discussion. However, if the patient had a mammogram, the reminder is resolved after the procedure and the frequency changes to 2 years. The discussion can then occur 2 years after the most recent mammogram resolve the reminder permanently.
- This reminder is resolved:
  - permanently by either of the new health factors that indicate the discussion has occurred and the women has made a decision (VA-WH BR CA 40-49 BEGIN AGE 50 or VA-WH BR CA 40-49 WANTS SCREEN) or
  - by any of the new health factors that defer the discussion for a specific period of time (VA-WH BR CA 40-49 DEFER 6M,VA-WH BR CA 40-49 DEFER 1Y,

> VA-WH BR CA 40-49 DEFER 5Y) or

- for 5 years if the primary care provider documents that he/she:
  - believes that this patient is unlikely to experience a <u>net</u> benefit from cervical cancer screening, i.e. no benefit expected or benefits are not expected to outweigh harms for the following reason:
    - Life expectancy is \<5 years. Specific diagnosis/reason: (required)
    - Patient could not tolerate the further work-up or treatment (if the screen was positive) because of co-morbidities Specific diagnoses/reason: (required)
- Additional comments: The setting of the Custom Date Due prevents the following problem: patient has a mammogram, then 2 years later the reminder shows and the discussion is deferred for 6 months. Without the CDD, the reminder would be due 2 years later instead of 6 months later.

> VA-WH MAMMOGRAM SCREENING was updated to increase the upper age range of the cohort from 69 to 74 and to include in the cohort women in their 40s who have completed the discussion described above and have decided to begin screening in their 40’s. Additional options were also added to allow providers to resolve the reminders if the patient is not expected to experience a net benefit from breast cancer screening because of less than 5 year life expectancy and/or patient could not tolerate the further work-up or treatment (if the screen was positive) because of co-morbidities.

- Cohort:
  - Women age 50-74 and women aged 40-49 who have decided to begin screening in their 40s as indicated by either of these new health factors: VA-WH BR CA 40-49. WANTS SCREEN. Women who a documented life expectancy of 6

> months or less or women with a diagnosis of terminal cancer of the esophagus, pancreas or liver are excluded from the cohort.

- Frequency:
  - The baseline frequency is set to every 2 years.

> o The provider is able to change the frequency to every 4 or 6 months or to every 1 year for an individual patient.

- This reminder is resolved:
  - by a completed or incomplete mammogram in the radiology package or in the Women’s Health package or
  - by a health factor indicating an mammogram done elsewhere as indicated by one of the following new health factors: WH OUTSIDE NORMAL MAMMOGRAM, WH OUTSIDE ABNL MAMMOGRAM, or
  - for 5 years if the primary care provider documents that he/she:
    - believes that this patient is unlikely to experience a <u>net</u> benefit from cervical cancer screening, i.e. no benefit expected or benefits are not expected to outweigh harms for the following reason:
      - Life expectancy is \<5 years. Specific diagnosis/reason: (required)
      - Patient could not tolerate the further work-up or treatment (if the screen was positive) because of co-morbidities Specific diagnoses/reason: (required)
  - for 90 days if a mammogram is ordered
  - for 4 months by selection of a health factors for deferral of the screen by the provider or declination of the screen by the patient
- Additional comments: Although there is a new health factor for an incomplete outside mammogram WH OUTSIDE INCOMPLETE MAMMOGRAM), this health factor does not resolve the reminder. However, this health factor will be used by new, not yet released Women’s Heath software.

> VA-MHV MAMMOGRAM SCREENING was updated to expand the age range from 40-69 to 40-74 and to add specific cohort found text regarding the new recommendation for an individual decision about when to begin screening by women in their 40’s. Additional edits were done to increase readability.

> CERVICAL CANCER REMINDERS

> These reminders implement VHA clinical guidance related to cervical cancer screening as defined in the VHA Cervical Cancer Screening Clinical Preventive Services Guidance Statement ([<u>http://vaww.prevention.va.gov/Screening_for_Cervical_Cancer.asp</u>](http://vaww.prevention.va.gov/Screening_for_Cervical_Cancer.asp)) as follows:

- “VHA recommends screening for cervical cancer with cytology (Pap test) every 3 years for women ages 21-65 who have a cervix OR, for women ages 30-65 who want to lengthen the screening interval, screening with a combination of cytology and human papillomavirus (HPV) testing every 5 years.”
- “VHA recommends against screening for cervical cancer in women who are younger than 21 years.”
- “VHA recommends against using human papillomavirus (HPV) testing alone or in combination with cytology for cervical cancer screening in women younger than 30 years.”
- “VHA recommends against screening for cervical cancer in women older than 65 years of age if they have had adequate prior screening and are not otherwise at high risk for cervical cancer.”
- “VHA recommends against screening for cervical cancer in women who have had a total hysterectomy (cervix removal) for benign disease.”

> VA-WH PAP SMEAR SCREENING definition and dialog were edited to add an every 5 year frequency option for women ages 30-64 who are screened with both a Pap test and HPV test. This option is available only if the last HPV test, if done, was negative. Additional options were also added to allow providers to resolve the reminders if the patient is not expected to experience a net benefit from cervical cancer screening because of less than 5 year life expectancy and/or patient could not tolerate the further work-up or treatment (if the screen was positive) because of co-morbidities. Links to recommended guidelines for follow- up in the case of a positive screen were added to the reminder dialog.

- Cohort:
  - women ages 21-65
  - does not apply to women who have had a hysterectomy where the cervix was removed
  - does not apply to women with a documented life expectancy of 6 months or less or to women with a diagnosis of terminal cancer of the esophagus, pancreas or liver
- Frequency:
  - The baseline frequency for Pap testing is every 3 years.
  - Clinicians may manage follow-up screening to occur every 4 or 6 months or 1 year when PAP smear results are unsatisfactory or abnormal
  - The clinician can alter the screening frequency to every 1 , 2 or 3 years for individual patients based on patient and family history, and discussions with the patient.
  - For women ages 30-65 only, a q5 year frequency is available if the woman is screened with both a pap and an HPV test and the HPV test was negative. Note: even if the frequency is set to every 5 years, if the last HPV test was positive, the frequency will go back to every 3 years.
- This reminder is resolved by:
  - PAP Smears completed recorded as one of the following:
    - Laboratory result matching Cytology or Surgical Pathology SNOMED
    - Women's Health procedure result
    - Health Factor (Historical outside PAP smear result)
    - PCE CPT procedure code
    - Completed consult order for outside procedure
  - In patients ages 30-65 who have evidence of a recent negative HPV result and no prior abnormal PAP smear, the PAP smear will resolve the reminder for 5 years.
  - Screening will be resolved for 9 months or until results are recorded to indicate the PAP smear has been completed:
    - PAP smear obtained at this encounter
    - Health Factor documenting an order for PAP Smear screening
    - Patient declined PAP smear
    - Clinician deferred PAP smear
  - Screening will be resolved for 5 years if the primary care provider documents that he/she:
    - believes that this patient is unlikely to experience a <u>net</u> benefit from cervical cancer screening, i.e. no benefit expected or benefits are not expected to outweigh harms for the following reason:
      - Life expectancy is \<5 years. Specific diagnosis/reason: (required)
      - Patient could not tolerate the further work-up or treatment (if the screen was positive) because of co-morbidities Specific diagnoses/reason: (required)
- Additional comments:
  - Management of an abnormal PAP is included in this screening reminder only if the clinician indicates what frequency is required for an individual patient. As a safety measure, a code for abnormal PAP changes the frequency to 1 year. This 1 year frequency is subsequently overridden if any other frequency is chosen by the clinician since the appropriate follow-up time may be less than a year depending on the individual Pap result.
  - Not all sites report HPV tests as a chemistry test. Some sites include HPV test results in the text of a Pap test result (a cervical cytology report). If HPV rest results are not entered as a chemistry test, the reminder is unable to find these results and the clinician must enter the HPV result manually in the reminder dialog in order for the q5 year frequency to function for women aged 30-65.
  - Be sure to work with your Lab ADPAC to see how your site documents HPV results. So that when you map your local tests and add conditions to find Positive or Negative results, you are inclusive of the way your site documents.

> <span id="_bookmark1" class="anchor"></span>VA-WH PAP SMEAR REVIEW RESULTS definition was edited to add a link to the VHA Cervical Cancer Screening Guidance Statement. The dialog was edited to include the q5yr frequency option in the dialog.

- This reminder applies to women who have a Pap smear in need of review in the Women’s health Package (i.e. in an open status with a value of pending)
- This reminder does not have any findings that resolve it, once there is no longer a Pap smear in need of review in the Women’s Health Package; the reminder is no longer applicable. The reminder dialog provides a mechanism to display the PAP smear results and for the clinician to record clinical review information in the current progress note and in the Women's Health package.
- Additional comments: The dialog also offers selections the clinician can use to document patient notification of PAP smear results in the Women's Health package and to optionally generate a letter to the patient.

> VA-MHV CERVICAL CANCER SCREENING definition was edited to be a copy of the new VA-WH PAP SMEAR SCREENING definition and to add specific cohort found text regarding the new every 5 year screening option with Pap and HPV for women ages 30-64. Additional edits were done to increase readability.

# Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Required Software for PXRM\*2\*28

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

### Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Documentation            | Documentation File name |
|------------------------------|-----------------------------|
| Installation and Setup Guide | PXRM_2_0_28_IG.PDF          |

> <span id="Web_Sites" class="anchor"></span>Web Sites

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

> Select Women's Health Menu Option: MF Manager's Functions

> WOMEN'S HEALTH: \* MANAGER'S FUNCTIONS \* MARTINEZ OPC/CREC

> FM File Maintenance Menu ... PQ Print Queued Letters

> MPM Manager's Patient Management ... LDE Lab Data Entry Menu ...

> Select Manager's Functions Option: FM File Maintenance Menu

> WOMEN'S HEALTH: \* FILE MAINTENANCE MENU \* MARTINEZ OPC/CREC

> AEP Add/Edit a Notification Purpose & Letter PPL Print Notification Purpose & Letter File ESN Edit Synonyms for Notification Types OUT Add/Edit Notification Outcomes

> ESP Edit Site Parameters

> CM Add/Edit Case Managers

> TR Transfer a Case Manager's Patients AUTO Automatically Load Patients RAD Import Radiology/NM Exams PRD Print Results/Diagnosis File

> ESR Edit Synonyms for Results/Diagnoses PSR Print Synonyms for Results/Diagnoses EDX Edit Diagnostic Code Translation File PDX Print Diagnostic Code Translation File RS Add/Edit to Referral Source File

> PAP Link Pap Smear with SNOMED Codes

> Select File Maintenance Menu Option: AEP Add/Edit a Notification Purpose & Letter

> \* \* \* WOMEN'S HEALTH: EDIT NOTIFICATION PURPOSE & LETTER FILE \* \* \*

> Select WV NOTIFICATION PURPOSE: PAP result NEM, next PAP 5Y Are you adding 'PAP result NEM, next PAP 5Y' as

> a new WV NOTIFICATION PURPOSE (the 78TH)? No// Y (Yes) WV NOTIFICATION PURPOSE PRIORITY: ROUT ROUTINE

> \* \* \* EDIT NOTIFICATION PURPOSE & LETTER \* \* \*

> Purpose of Notification: PAP result NEM, next PAP 5Y Active: YES

> Synonym: PN5Y

> Priority: ROUTINE FORM LETTER (WP): +

> Result or Reminder Letter: RESULT Associate with BR or CX Tx: CERVICAL

> Breast Treatment Need: Breast Treatment Due Date:

> Cervical Treatment Need: Routine PAP Cervical Treatment Due Date: 5Y

> \_

> Exit Save Refresh COMMAND: Save

> \* \* \* EDIT NOTIFICATION PURPOSE & LETTER \* \* \*

> Purpose of Notification: PAP result NEM, next PAP 5Y Active: YES

> Synonym: PN5Y

> Priority: ROUTINE FORM LETTER (WP): +

> Result or Reminder Letter: RESULT Associate with BR or CX Tx: CERVICAL

> Breast Treatment Need: Breast Treatment Due Date:

> Cervical Treatment Need: Routine PAP Cervical Treatment Due Date: 5Y

> \_

> Exit Save Refresh COMMAND: Exit

> \* \* \* WOMEN'S HEALTH: EDIT NOTIFICATION PURPOSE & LETTER FILE \* \* \*

> Select WV NOTIFICATION PURPOSE: CPRS UPDATE PAP TX NEED 5Y

> Are you adding 'CPRS UPDATE PAP TX NEED 5Y' as

> a new WV NOTIFICATION PURPOSE (the 79TH)? No// Y (Yes) WV NOTIFICATION PURPOSE PRIORITY: ROUT ROUTINE

> \* \* \* EDIT NOTIFICATION PURPOSE & LETTER \* \* \*

> Purpose of Notification: CPRS UPDATE PAP TX NEED 5Y Active: YES

> Synonym:

> Priority: ROUTINE FORM LETTER (WP): +

> Result or Reminder Letter: REMINDER Associate with BR or CX Tx: CERVICAL

> Breast Treatment Need: Breast Treatment Due Date:

> Cervical Treatment Need: Routine PAP Cervical Treatment Due Date: 5Y

> Exit Save Refresh COMMAND: Save

> \* \* \* EDIT NOTIFICATION PURPOSE & LETTER \* \* \*

> Purpose of Notification: CPRS UPDATE PAP TX NEED 5Y Active: YES

> Synonym:

> Priority: ROUTINE FORM LETTER (WP): +

> Result or Reminder Letter: REMINDER Associate with BR or CX Tx: CERVICAL

> Breast Treatment Need: Breast Treatment Due Date:

> Cervical Treatment Need: Routine PAP Cervical Treatment Due Date: 5Y

> Exit Save Refresh COMMAND: Exit

2.  Verify that your existing reminder terms are mapped correctly.
3.  Open the Reminder Dialog Manager and review the following dialog elements and groups. These items may have quick orders and menus linked to them and these may need to be re-entered after the installation. Additionally, as a double check, it is recommended to compare these elements and groups in your test account (after installation) to the live account (before

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *This patch can be installed with users on the system, but it should be done during non-peak hours.* <span id="_bookmark6" class="anchor"></span>*Estimated Installation Time: 10-15 minutes*

> *The installation needs to be done by a person with DUZ(0) set to "@."*

#### NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.

1.  <span id="1._Retrieve_the_host_file_from_one_of_th" class="anchor"></span>Retrieve the host file from one of the following locations (with the ASCII file type):

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
<th><mark><u>REDACTED</u></mark></th>
<th><mark><u>REDACTED</u></mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><mark><u>REDACTED</u></mark></td>
<td><mark><u>REDACTED</u></mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark><u>REDACTED</u></mark></td>
<td><mark><u>REDACTED</u></mark></td>
</tr>
</tbody>
</table>

2.  <span id="2._Install_the_patch_first_in_a_training" class="anchor"></span>Install the patch first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

#### Load the distribution.

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name. KID at the Host File prompt.

#### Example

> From the Installation menu, you may elect to use the following options:

#### Backup a Transport Global

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

#### Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

#### Verify Checksums in Transport Global

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.

> Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk <span class="mark">REDACTED</span> to report the problem.

#### Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*28 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE: DO NOT QUEUE THE INSTALLATION, because this installation asks questions requiring responses and queuing will stop the installation. A Reminders Manager or CAC should be present to respond to these.

#### Installation Example

> See [<u>Appendix A</u>](#appendix-a-installation-example).

#### Install File Print

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.

#### Build File Print

> Use the KIDS Build File Print option to print out the build components.

#### Post-installation routines

> After successful installation, the following init routines may be deleted:

> PXRMP28E PXRMP28I

# Post-Install Set-up Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Map new reminder terms.
    1.  VA-WH HPV TESTING NEGATIVE
    2.  VA-WH HPV TESTING POSITIVE

> For both of these terms, you will need to include any CH (Chem/Hem) subscripted lab tests that represent Intermediate or High Risk HPV testing AND you will need to set the condition for any lab test that is added. The health factors for negative and positive HPV testing are included already in these terms. Use a condition string that includes the result the way that you laboratory reports out these negative and positive lab tests. Set the case sensitive field to ‘NO’ and for the positive term, set the findings to ‘Use Status/Cond in Search: YES’.

> If you do not have any CH subscripted lab tests for HPV, then leave only the health factor in the reminder term.

> Do not include lab tests that represent low risk HPV in either reminder term. Example

> VA-WH HPV TESTING NEGATIVE (FI(20))

> Mapped Findings:

1.  HF.OUTSIDE CERVICAL HPV TESTING NEGATIVE
2.  LT.Hpv High Risk

> Condition: I V\["NOT DET"!(V\["NEG")!(V="NON REACTIVE")!(V="NON- REACTIVE")!(V="NR")!(V\["NONE")

> Condition Case Sensitive: NO

3.  LT.Hpv Intermediate Risk

> Condition: I V\["NOT DET"!(V\["NEG")!(V="NON REACTIVE")!(V="NON- REACTIVE")!(V="NR")!(V\["NONE")

> Condition Case Sensitive: NO

> VA-WH HPV TESTING POSITIVE (FI(21))

1.  HF.OUTSIDE CERVICAL HPV TESTING POSITIVE
2.  LT.Hpv High Risk

> Condition: I V="DETECTED"!(V\["POS")!(V="REACTIVE")!(V="DET")!(+V\>0)

> Condition Case Sensitive: NO Use Status/Cond in Search: YES

3.  LT.Hpv Intermediate Risk

> Condition: I V="DETECTED"!(V\["POS")!(V="REACTIVE")!(V="DET")!(+V\>0)

> Condition Case Sensitive: NO

# Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> +-------------------------------------------------------------------------------

> --------------------------------------------------------------------------------

> +-------------------------------------------------------------------------------

> --------------------------------------------------------------------------------

> PXRM\*2.0\*28

> ----------------------------

> ---------------------------------------------------

> Install Started for PXRM\*2.0\*28 :

> Jan 15, 2013@13:39:13

> Build Distribution Date: Jan 15, 2013

> Installing Routines:

> Jan 15, 2013@13:39:14

> Running Pre-Install Routine: PRE^PXRMP28I

> DISABLE options.

> DISABLE protocols.

> Renaming health factors.

> Installing Data Dictionaries:

> Jan 15, 2013@13:39:14

> Installing Data:

> Jan 15, 2013@13:39:15

> Running Post-Install Routine: POST^PXRMP28I

> ENABLE options.

> ENABLE protocols.

> There are 12 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry VA-WH DISCUSS BREAST CA SCREEN WOMAN40-49
2.  Installing Reminder Exchange entry VA-WH DISCUSS BREAST CA WOMAN 40-49DIALOG
3.  Installing Reminder Exchange entry VA-WH MAMMOGRAM SCREENING
4.  Installing Reminder Exchange entry VA-WH MAMMOGRAM SCREENING DIALOG
5.  Installing Reminder Exchange entry VA-WH PAP SMEAR REVIEW RESULTS
6.  Installing Reminder Exchange entry VA-WH PAP SMEAR REVIEW RESULTS DIALOG
7.  Installing Reminder Exchange entry VA-WH PAP SMEAR SCREENING
8.  Installing Reminder Exchange entry VA-WH PAP SMEAR SCREENING DIALOG
9.  Installing Reminder Exchange entry VA-MHV CERVICAL CANCER SCREEN
10. Installing Reminder Exchange entry VA-MHV MAMMOGRAM SCREENING
11. Installing Reminder Exchange entry VA-WH MAMMOGRAM REVIEW RESULTS DIALOG
12. Installing Reminder Exchange entry VA-BREAST TUMOR

> Linking and enabling dialogs

> Linking and enabling reminder dialog VA-WH DISCUSS BREAST CA WOMAN 40-49to reminder definition VA-WH DISCUSS BREAST CA SCREEN WOMAN 40-49.

> Linking and enabling reminder dialog VA-WH MAMMOGRAM SCREENING to reminder definition VA-WH MAMMOGRAM SCREENING.

# Appendix B: Default Outside Location 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Within portions of a reminder dialog where historical encounter information is entered, a new parameter, ORQQPX DEFAULT LOCATIONS, can be set up to define default outside locations for the PXRM OUTSIDE LOCATION prompt. Each free-text entry in this multi-valued parameter will appear at the top of the list of locations in the drop-down list in CPRS. If a number is entered as the free-text value, CPRS will attempt to locate an entry in the Institution file (#4) with the same internal entry number.

> *Example*

> Select CPRS Reminder Configuration Option: dl Default Outside Location Default Outside Locations may be set for the following:

> 1 User USR \[choose from NEW PERSON\]

3.  Service SRV \[choose from SERVICE/SECTION\]
4.  Division DIV \[choose from INSTITUTION\]
5.  System SYS \[DEVCUR.ISC-SLC.VA.GOV\]
6.  Package PKG \[ORDER ENTRY/RESULTS REPORTING\] Enter selection: 1 User NEW PERSON

> Select NEW PERSON NAME: CRPROVIDER,TWO TC

> ---------- Setting Default Outside Locations for User: CRPROVIDER,ONE ------

> Select Display Sequence: 1

> Display Sequence: 1// 1

> Outside Location (Text or Pointer): 663 Select Display Sequence: 2

> Are you adding 2 as a new Display Sequence? Yes// \<Enter\> YES

> Display Sequence: 2// \<Enter\>

> Outside Location (Text or Pointer): Local Pharmacy

> Select Display Sequence: 3

> Are you adding 3 as a new Display Sequence? Yes// \<Enter\> YES Display Sequence: 3// \<Enter\> 3

> Outside Location (Text or Pointer): 640

> Select Display Sequence: 4

> Are you adding 4 as a new Display Sequence? Yes// \<Enter\> YES Display Sequence: 4// \<Enter\> 4

> Outside Location (Text or Pointer): Outside Physician's Office

> Select Display Sequence: ???

> Display Sequence Value

> ---------------- -----

> 1 663

> 2 Local Pharmacy

> 3 640

> 4 Outside Physician's Office

> Default Location as it appears in CPRS:

> ![](pxrm-2-28-women-s-health-clinical-reminder-updates-installation-guide/002.png)

> Note that Seattle, WA and Palo Alto are entries in the institution file with internal entry numbers of 663 and 640, respectively.

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The OIT Master Glossary is available at [<u>http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm</u>](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)
|     | Term   | Definition                                                  |
|-----|------------|-----------------------------------------------------------------|
|     | ASU        | Authorization/Subscription Utility                              |
|     | Clin4      | National Customer Support team that supports Clinical Reminders |
|     | CPRS       | Computerized Patient Record System                              |
|     | DBA        | Database Administration                                         |
|     | DG         | Registration and Enrollment Package namespace                   |
|     | ESM        | Enterprise Systems Management (ESM)                             |
|     | FIM        | Functional Independence Measure                                 |
|     | GMTS       | Health Summary namespace (also HSUM)                            |
|     | GUI        | Graphic User Interface                                          |
|     | HRMH/HRMHP | High Risk Mental Health Patient                                 |
|     | IAB        | Initial Assessment & Briefing                                   |
|     | ICD-10     | International Classification of Diseases, 10th Edition          |
|     | ICR        | Internal Control Number                                         |
|     | IOC        | Initial Operating Capabilities                                  |
|     | LSSD       | Last Service Separation Date                                    |
|     | MH         | Mental Health                                                   |
|     | MHTC       | Mental Health Treatment Coordinator                             |
|     | OHI        | Office of Health Information                                    |
|     | OI         | Office of Information                                           |
|     | OIF/OEF    | Operation Iraqi Freedom/Operation Enduring Freedom              |
|     | OIT/OI&T   | Office of Information Technology                                |
|     | OMHS       | Office of Mental Health Services                                |
|     | ORR        | Operational Readiness Review                                    |
|     | PCS        | Patient Care Services                                           |
|     | PD         | Product Development                                             |
|     | PIMS       | Patient Information Management System                           |
|     | PMAS       | Program Management Accountability System                        |
|     | PTM        | Patch Tracker Message                                           |
| Term | Definition                                                 |
|----------|----------------------------------------------------------------|
| PXRM     | Clinical Reminder Package namespace                            |
| RSD      | Requirements Specification Document                            |
| SD       | Scheduling Package Namespace                                   |
| SQA      | Software Quality Assurance                                     |
| USR      | ASU package namespace                                          |
| VA       | Department of Veteran Affairs                                  |
| VHA      | Veterans Health Administration                                 |
| VISN     | Veterans Integrated Service Network                            |
| VistA    | Veterans Health Information System and Technology Architecture |
