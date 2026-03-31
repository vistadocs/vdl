---
title: PXRM*2*52 Hepatitis C Risk Assessment & Testing , National Taxonomy & Veterans Choice Updates Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Hepatitis C Risk Assessment & Testing , National Taxonomy & Veterans Choice Updates
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*52
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: > HCV is the most common chronic blood-borne pathogen in the U. S. An estimated 3.2 million Americans are living with chronic HCV infection. In the U.S., there are approximately 17,000 new cases of HCV annually. HCV is acquired primarily by percutaneous exposures to blood. Approximately 15,000 death
audience: 
keywords: 
  - blockquote
  - risk
  - hepatitis
  - class
  - table
  - testing
  - assessment
  - contents
  - reminder
  - strong
page_count: 0
word_count: 2038
section_count: 4
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: May 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_52_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_52_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/001.png)

# Hepatitis C Risk Assessment & Hepatitis C Testing Reminders, National Taxonomy updates, and Updates to Veterans Choice Template


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Hepatitis C Risk Assessment & Hepatitis C Testing Reminders, National Taxonomy updates, and Updates to Veterans Choice Template](#hepatitis-c-risk-assessment-hepatitis-c-testing-reminders-national-taxonomy-updates-and-updates-to-veterans-choice-template)
- [INSTALLATION and SETUP GUIDE](#installation-and-setup-guide)
  - [Introduction](#introduction)
  - [Pre-Installation](#pre-installation)
    - [Required Software for PXRM\2\52](#required-software-for-pxrm252)
    - [Related Documentation](#related-documentation)
    - [Web Sites](#web-sites)
- [<u>Post-Install Set-up Instructions</u>](#upost-install-set-up-instructionsu)
- [<u>Appendix A: Installation Example</u>](#uappendix-a-installation-exampleu)
  - [Acronyms](#acronyms)
> PXRM\*2.0\*52

# INSTALLATION and SETUP GUIDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> May 2015

> Product Development Department of Veterans Affairs

> <u>Contents</u>

1.  [Retrieve the host file from one of the following locations (with the ASCII file type) 13](#retrieve-the-host-file-from-one-of-the-following-locations-with-the-ascii-file-type)
2.  [Install the patch first in a training or test account 13](#install-the-patch-first-in-a-training-or-test-account.)
3.  [Load the distribution. 13](#load-the-distribution.)
4.  [Backup a Transport Global 13](#backup-a-transport-global)
5.  [Compare Transport Global to Current System 13](#compare-transport-global-to-current-system)
6.  [Install the build. 13](#install-the-build.)
7.  [Install File Print 14](#install-file-print)
8.  [Build File Print 14](#build-file-print)
9.  [Post-installation routines 14](#post-installation-routines)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Description:

> HCV is the most common chronic blood-borne pathogen in the U. S. An estimated 3.2 million Americans are living with chronic HCV infection. In the U.S., there are approximately 17,000 new cases of HCV annually. HCV is acquired primarily by percutaneous exposures to blood. Approximately 15,000 deaths from chronic liver disease per year are associated with HCV.[<sup><u>4</u></sup>](http://vaww.prevention.va.gov/Screening_for_Hepatitis_C.asp#4) HCV diagnosis and treatment may mitigate some of the negative health outcomes of HCV infection. In the VHA, the prevalence of HCV infection has been found to be 6.2% overall and 10.1% in Veterans born during 1945-1965.

> The United States Preventive Services Task Force (USPSTF) recommends screening for HCV infection in persons at high risk for infection. The USPSTF also recommends offering one-time screening for HCV infection to adults born between 1945 and 1965.

> This patch installs the following for the Hepatitis C reminders/dialogs during installation:

1.  Reminders Definitions:

> VA-HEPATITIS C RISK ASSESSMENT VA-HEPATITIS C TESTING

> VA-HEP C RISK FACTOR OBJECT

2.  Dialogs

> VA-HEPATITIS C RISK ASSESSMENT VA-HEPATITIS C TESTING

3.  Taxonomies

> VA-ALCOHOL ABUSE

> VA-DRUG ABUSE FOR HCV TESTING VA-HEPATITIS C INFECTION

> VA-HEPATITIS C SEROPOSITIVE VA-HIV INFECTION

> VA-TERMINAL CANCER PATIENTS

4.  Terms

> VA-DECLINED HEP C RISK ASSESSMENT VA-DECLINED HEP C TESTING

> VA-HEP C LAB TESTS ORDERED VA-HEP C OUTSIDE RESULTS VA-HEP C RNA

> VA-HEP C VIRUS ANTIBODY NEGATIVE VA-HEP C VIRUS ANTIBODY POSITIVE VA-HEPATITIS C INFECTION

> VA-HEPATITIS C SEROPOSITIVE

> VA-LIFE EXPECTANCY \< 6 MONTHS VA-NO RISK FACTORS FOR HEP C VA-RISK FACTOR FOR HEPATITIS C VA-TERMINAL CANCER PATIENT

5.  Health Factors

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DECLINED HEP C RISK ASSESSMENT</p>
<p>DECLINED HEP C TESTING</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HCV RISK: 20/&gt; LIFETIME SEXUAL PARTNERS HCV RISK: BLOOD/ORGAN TX PRIOR TO 1992</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HCV RISK: BORN TO HCV+ MOTHER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HCV RISK: HEMODIALYSIS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HCV RISK: HEMOPHILIA/CLOTTING FACTOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HCV RISK: HIV INFECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HCV RISK: HX OF ALCOHOL HEP/ABUSE/DEPEND</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HCV RISK: INCARCERATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HCV RISK: INTRANASAL DRUG USER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HCV RISK: INTRAVENOUS DRUG USE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HCV RISK: NEEDLE\MUCOSAL EXPOSURE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HCV RISK: SEXUAL HCV EXPOSURE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HCV RISK: TATTOO/PIERCING</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HCV RISK: UNEXPL LIVER DZ/ABN LIVER FX</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HCV RISK: VIETNAM-ERA VETERAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HEP C RISK</p>
<p>HEP C TESTING DEFERRED</p>
<p>HEP C TESTING NOT INDICATED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HEP C SCREEN NOT INDICATED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NO RISK FACTORS FOR HEP C</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREVIOUS NEGATIVE ANTI-HCV PREVIOUS POSITIVE ANTI-HCV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREVIOUS NEGATIVE HCV RNA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREVIOUS POSITIVE HCV RNA</p>
<p>RISK FACTOR FOR HEPATITIS C</p>
</blockquote></td>
</tr>
</tbody>
</table>

6.  TIU Template Field

> VA-HEP C NCP GUIDANCE STATEMENT

7.  Health Summary Type

> VA-HEP C RISK FACTORS

8.  TIU Object

> VA-HEP C RISK FACTORS

> This patch also installs the following edits to the Veterans Choice reminder dialog:

> The groups and elements modified were minimal as they are used in both the Pre and Post Visit sections. The Groups and Elements are:

> Group: VA-DG VETERANS CHOICE CLINICAL INFO

> Element: VA-DE VETERANS CHOICE CLINICAL INFO TEXT Group: VA-DG VETERANS CHOICE ADDITIONAL COMMENTS

> Element: VA-DE VETERANS CHOICE ADDITIONAL COMMENTS

> The modifications are:

- Remove the suppression of the check boxes on the Groups
- Remove Show on the Groups (hide the elements in the groups)
- Moved the display only Clinical Information instructions from the Group to the Element.
- Added “\\” to the Clinical Info element to modify indent.

#### Pre-Visit Section Before:

> ![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/002.png)

> After:

> ![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/003.png)

> Post-Visit Section Before:

> ![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/004.png)

> After:

> ![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/005.png)

> How the Hepatitis C reminders work:

1.  Only see one reminder at a time – never both
2.  The Hepatitis C Risk Assessment reminder definition will be applicable to all patients who have not had a risk assessment documented. It will not be applicable for patients already at risk; including those born during 1945-1965 or patients already tested for hepatitis C. Patients with terminal cancer or documented with a limited life expectancy are also excluded.
    1.  The computed finding VA-DATE OF BIRTH uses the CONDITION

> “I V\>2441231&(V\<2660101)” to identify patients with a date of birth during 1945- 1965.

3.  The Hepatitis C Risk Assessment is resolved with a documented risk assessment, documentation of a patient declining the risk assessment, a hepatitis C serology lab test (anti- HCV) order, or documentation of an outside or previous hepatitis C serology or RNA lab test.
4.  The Hepatitis C Testing reminder definition will be applicable to
    1.  Patients with a documented risk of hepatitis C and not already tested for hepatitis C AND
    2.  Patients with a positive HCV serology lab test (anti-HCV), but without a HCV RNA lab result.

> Patients with terminal cancer or documented with a limited life expectancy are excluded.

5.  The Hepatitis C Testing reminder is resolved with an HCV lab test order, documentation of a patient declining the screen, deferring the hepatitis C screen, documentation of an outside or previous hepatitis C negative serology (anti-HCV), a negative hepatitis C serology, documentation of an outside or previous hepatitis C RNA, or a HCV RNA result.
6.  The reminder dialogs attached to each definition contain groups with embedded branching logic.
    1.  The VA-HEPATITIS C RISK ASSESSMENT reminder dialog contains branching logic in the VA-HEP C RISK ASSMNT TESTING HEADER group to determine whether the options for the VA-HEPATITIS C TESTING reminder should populate the dialog. The instructions for this branching logic are below in the post-installation instructions.

> 25 5.15.5.10.10 Group: VA-HEP C RISK ASSMNT TESTING HEADER

> Suppressed if Reminder Term VA-BL HEP C RISK ASSMNT ORDERS OPTION evaluates as FALSE

2.  The VA-HEPATITIS C RISK ASSESSMENT also contains branching logic in the embedded VA-HEP C TESTING OPTIONS (ANTI-HCV POS) HEADER group. This branching logic term will not evaluate in the Risk Assessment dialog because it is below another branching logic level. However, the correct options will display in the dialog and the branching logic should not be removed.
3.  The VA-HEPATITIS C TESTING reminder dialog contains branching logic in the VA-HEP C TESTING TEXT/OPTIONS group. The branching is triggered by a true evaluation of the VA-HEP C VIRUS ANTIBODY POSITIVE reminder term. The logic determines what options are displayed to the user to resolve the reminder.

> If the patient does not have a documented positive HCV serology test, then the user will be given options to order and document a previous HCV serology test AND options to document a previous HCV RNA test. The options are below:

![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/006.png)

> If the patient does have a documented positive HCV serology test, then the user will be given options to order and document a previous HCV RNA test. The options are below:

![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/007.png)

> Terms that are used in the logic: <u>VA-RISK FACTOR FOR HEPATITIS C</u>

> This term is released with the health factor RISK FACTOR FOR HEPATITIS C. This term includes national taxonomies for alcohol abuse, drug abuse, and HIV infection. Map any local findings that meet the intent of this term in the REMINDER TERM file (811.5).

> <u>VA-NO RISK FACTORS FOR HEP C</u>

> This term is released with the health factor NO RISK FACTORS FOR HEP C. Map any local findings that meet the intent of this term in the REMINDER TERM file (811.5).

> <u>VA-DECLINED HEP C RISK ASSESSMENT</u>

> This term is released with the health factor DECLINED HEP C RISK ASSESSMENT. Map any local findings that meet the intent of this term in The REMINDER TERM file (811.5).

> <u>VA-DECLINED HEP C TESTING</u>

> This term is released with the health factor DECLINED HEP C TESTING. Map any local findings that meet the intent of this term in The REMINDER TERM file (811.5).

> <u>VA-HEP C OUTSIDE RESULTS</u>

> This term is released with the health factors PREV POSITIVE TEST FOR HEP C and PREV NEGATIVE TEST FOR HEP C. Map any local findings that identify the patient as previously assessed for Hepatitis C risk factors in the REMINDER TERM file(811.5).

> This term was originally distributed as PREV POSITIVE TESTFOR HEP C, but was changed to provide sites with a way to identify a patient as previously assessed for Hepatitis C risk factors. This term will also be used to document historical positive tests completed outside the facility.

> <u>VA-HEP C VIRUS ANTIBODY POSITIVE</u>

> This term is released with the health factor PREVIOUS POSITIVE ANTI-HCV. Map any local findings that meet the intent of this term in The REMINDER TERM file (811.5).

#### Also:

> Map local HCVAb lab tests with a condition in the REMINDER TERM file. An example of the condition field might be: I V="positive" or I (V\["P")!(V\["p"). The text used in the condition definition (I V="text") should be based on the local LABORATORY TEST file (60) print codes when defined, rather than the result in the LAB DATA file (63).

> <u>VA-HEP C VIRUS ANTIBODY NEGATIVE</u>

> This term is released with the health factor PREVIOUS NEGATIVE ANTI-HCV. Map any local findings that meet the intent of this term in The REMINDER TERM file (811.5).

#### Also:

> Map local HCVAb lab tests with a condition in the REMINDER TERM file. An example of the condition field might be: I V="negative" or I (V\["N")!(V\["n"). The text used in the condition definition (I V="text") should be based on the local LABORATORY TEST file (60) print codes when defined, rather than the result in the LAB DATA file (63).

> <u>VA-HEP C LAB TESTS ORDERED</u>

> Map local HCVAb and HCV RNA lab test orderable items in the REMINDER TERM file. The orderable items should have the following status; ACTIVE, PENDING, RENEWED, SCHEDULED.

> <u>VA-LIFE EXPECTANCY \<6 MONTHS</u>

> This term is released with the health factor VA-TERMINAL CANCER PATIENTS. Map any local findings that identify patients with a terminal illness.

> <u>VA-HEP C RNA</u>

> This term is released with the health factors PREVIOUS POSITIVE HCV RNA and PREVIOUS NEGATIVE HCV RNA. Map any local findings that meet the intent of this term in The REMINDER TERM file (811.5).

#### Also:

> Map local HCV RNA lab tests. If the local site cancels lab tests and enters a "cancel" comment as the result, then a condition will need to be added in the REMINDER TERM preventing the cancelled test from resolving the reminder.

> <u>VA-HEPATITIS C SEROPOSITIVE</u>

> This term includes the national taxonomy VA-HEPATITIS C SEROPOSITIVE. Codes for HCV infection and HCV seropositive

> <u>VA-TERMINAL CANCER PATIENTS</u>

> This term included the national taxonomy VA-TERMINAL CANCER PATIENTS. No local mapping is necessary.

#### Hepatitis C testing reminder option to view patient risk(s)

> The Hepatitis C testing reminder dialog has an option for the user to view patient-specific risks, which have triggered the reminder to be due (highlighted below). This group contains three branching logic elements to help clearly communicate the risks. The branching logic uses the same reminder terms as each reminder definition, so no additional local modification is required.

![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/008.png)

> 5.2.5 Element: VA-HEP C TESTING RISK BIRTH

> Suppressed if Reminder Term VA-HEP C BIRTH COHORT evaluates as FALSE

> This element will display the following statement if the patient falls within the birth cohort, which is determined by the VA_HEP C BIRTH COHORT reminder term.

![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/009.png)

> 5.2.10 Element: VA-HEP C TESTING RISK POS SEROLOGY

> Suppressed if Reminder Term VA-HEP C VIRUS ANTIBODY POSITIVE evaluates as FALSE

> This element will display the following statement if the patient has a documented positive hepatitis c antibody lab test, which is determined by the VA_HEP C VIRUS ANTIBODY POSITIVE reminder term.

![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/010.png)

15. Element: VA-HEP C TESTING RISK OTHER

> Suppressed if Reminder Term VA-RISK FACTOR FOR HEPATITIS C evaluates as FALSE

> This element will display a similar statement as below if the patient has any one of the other hepatitis c risk factors, including the risk factor health factors, codes in the risk factor taxonomies, and any local findings added to the VA-RISK FACTOR FOR HEPATITIS C, which is also the trigger for the branching logic. The TIU object is populated with the clinical maintenance of the VA-HEP C RISK FACTOR OBJECT reminder definition.

![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/011.png)

## Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Required Software for PXRM\*2\*52

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Package/Patch</strong></th>
<th><strong>Namespace</strong></th>
<th><strong>Version</strong></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinical Reminders</td>
<td>PXRM</td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Documentation</strong></p>
</blockquote></th>
<th><strong>Documentation File name</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| Hepatitis C install guide | PXRM_2_0_52_IG.PDF |
|---------------------------|--------------------|

### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 36%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site</strong></th>
<th><blockquote>
<p><strong>URL</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>National Clinical Reminders site</td>
<td><blockquote>
<p><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Contains manuals, PowerPoint presentations, and other information</p>
<p>about Clinical Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td>National Clinical Reminders Committee</td>
<td><blockquote>
<p><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/ncrc</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>public/default.aspx</u></a></p>
</blockquote></td>
<td><blockquote>
<p>This committee directs the</p>
<p>development of new and revised national reminders</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>VistA Document</p>
<p>Library</p></td>
<td><blockquote>
<p><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Contains manuals for Clinical</p>
<p>Reminders and</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark5" class="anchor"></span><u>Installation</u>

> *This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes*

> *The installation needs to be done by a person with DUZ(0) set to "@."*

#### NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.

#### Retrieve the host file from one of the following locations (with the ASCII file type):

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 31%" />
<col style="width: 51%" />
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

#### Install the patch first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

#### Load the distribution.

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name. KID at the Host File prompt.

#### Example

> From the Installation menu, you may elect to use the following options:

#### Backup a Transport Global

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

#### Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

#### Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM and proceed with the install. If you have

> problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompts:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//NO

#### Installation Example

> See <u>Appendix A</u>.

#### Install File Print

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

#### Build File Print

> Use the KIDS Build File Print option to print out the build components.

#### Post-installation routines

> After successful installation, the following init routines may be deleted:

# <u>Post-Install Set-up Instructions</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Map local lab tests
    1.  Map HCV RNA lab tests and health factors

> Map to this term: VA-HEP C RNA

> Description:

> Map any local health factors that represent previous or outside HCV RNA results. Also, map local HCV RNA lab tests. If the local site cancels lab tests and enters a "cancel" comment as the result, then a condition will need to be added in the REMINDER TERM preventing the cancelled test from resolving the reminder.

> Condition example: I V’\[“CANC”

2.  Map HCV lab tests with a positive result

> Map to this term: VA-HEP C VIRUS ANTIBODY POSITIVE

> Description:

> Map any local health factors that represent previous or outside positive HCV serology results. Also,

> map local HCVAb lab tests with a condition. The text used in the condition definition (I V="text") should be based on the local LABORATORY TEST file (60) print codes when defined, rather than the result in the LAB DATA file (63).

> Condition example(s): I V="positive" or I (V\["P")!(V\["p").

3.  Map HCV lab tests with a negative result

> Map to this term: VA-HEP C VIRUS ANTIBODY NEGATIVE

> Description:

> Map any local health factors that represent previous or outside negative HCV serology results.

> Also, map local HCVAb lab tests with a condition. The text used in the condition definition (I V="text") should be based on the local LABORATORY TEST file (60) print codes when defined, rather than the result in the LAB DATA file (63).

> Condition example(s): I V="negative" or I (V\["N")!(V\["n").

2.  Map any existing local health factors
    1.  Map your local health factors for Hepatitis C risk factors to the reminder term: VA-RISK FACTOR FOR HEPATITIS C
    2.  Map your local health factors that represent no Hepatitis C risk factors present to the reminder term: VA-NO RISK FACTORS FOR HEP C
    3.  Map your local health factors that represent a patient declined the Hepatitis C risk assessment to the reminder term:

> VA-DECLINED HEP C RISK ASSESSMENT

4.  Map your local health factors that represent a patient declined the Hepatitis C test to the reminder term: VA-DECLINED HEP C TESTING
5.  Map your local health factors that identify the patient as previously assessed for Hepatitis C risk factors to the reminder term:

> VA-HEP C OUTSIDE RESULTS

3.  Map your local orderable items for HCV lab tests

> Map your local orderable items for HCV serology and HCV RNA lab tests to the reminder term: VA-HEP C LAB TESTS ORDERED

> Map local HCV Ab and HCV RNA orderable items in the REMINDER TERM file. The orderable items should have the following status; ACTIVE, PENDING, RENEWED, SCHEDULED.

> The orders will resolve the reminders for 6 months or until they are resulted.

4.  Map any limited life expectancy health factors

> Map any limited life expectancy health factors to the reminder term:

> VA-LIFE EXPECTANCY \<6 MONTHS

5.  Embed appropriate HCV serology lab quick order

> The VA-HEPATITIS C TESTING dialog has an option for a provider to order a HCV serology lab. The element VA-HEP C TESTING ORDER ANTI-HCV needs to be mapped to the appropriate local HCV serology lab test order for the option to work correctly.

1.  Find the VA-HEP C TESTING ORDER ANTI-HCV element and select EDIT
2.  Place the quick order name in the FINDING ITEM field (example below).

> Dialog Name: VA-HEP C TESTING ORDER ANTI-HCV

> Current dialog element/group name: VA-HEP C SCREEN ORDER ANTI-HCV Used by: VA-HEP C TESTING TEXT/OPTIONS (Dialog Group)

> FINDING ITEM:Q.LRZ ANTI-HCV LAB ORDER

6.  Embed appropriate HCV RNA lab quick order

> The VA-HEP C TESTING OPTIONS (ANTI-HCV POS) group has an option for a provider to order a HCV RNA lab. This group is a replacement group for branching logic, so it can be accessed by searching for the dialog group in the DIALOG GROUPS view of dialog. The element VA-HEP C TESTING ORDER HCV RNA needs to be mapped to the appropriate local HCV RNA lab test order for the option to work correctly.

1.  Find the VA-HEP C TESTING ORDER HCV RNA element and select EDIT
2.  Place the quick order name in the FINDING ITEM field (example below).

> Dialog Name: VA-HEP C TESTING ORDER HCV RNA

> Current dialog element/group name: VA-HEP C SCREEN ORDER HCV RNA FINDING ITEM:Q.LRZ HCV RNA LAB ORDER

7.  Activate or inactivate the optional hepatitis C risk factor list in the VA-HEPATITIS C RISK ASSESSMENT reminder dialog.

> The dialog linked to the VA-HEPATITIS C RISK ASSESSMENT definition has a group that displays a list of hepatitis C risk factors for the user to choose to apply to a patient’s record (below). Each option has a distinct health factor. The list is included for sites that want providers to document specific risk factors.

> The group name is HEP C RISK ASSMNT RISK FACTOR OPTIONS. It has a “local” class, so it can be disabled/enabled depending on the site’s preference to include the list in the dialog or not.

> The health factors in the elements in this group have no function in the reminder logic, so the reminders will work correctly whether the group is enabled or disabled.

![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/012.png)

8.  Decide whether or not to include the Hepatitis C Testing dialog in the Hepatitis C Risk Assessment.

> The Hepatitis C Risk Assessment dialog includes the options for documenting a Hepatitis C Testing in the positive risk assessment option (below). This is included for sites that want the ability to resolve both reminders in the same encounter as their reminder processing allows. This function is optional.

> The screening section in the risk assessment is controlled with branching logic within the VA-HEPATITIS C RISK ASSESSMENT dialog. The group named VA HEP C RISK ASSMNT TESTING HEADER has a reminder term VA-BL HEP C RISK ASSMNT ORDER OPTION, which decides whether to display the options or not.

> <u>To display the screen options in the risk assessment:</u>

> Do nothing. The term is installed with the computed finding VA-AGE, which is evaluated as TRUE for all patients and displays the screen options.

> <u>To remove the screen options from the risk assessment:</u>

> Remove the VA-AGE computed finding from the term and leave the term blank. The term will evaluate as FALSE and the screen options will not display to the user in the VA-HEPATITIS C RISK ASSESSMENT.

![](pxrm-2-52-hepatitis-c-risk-assessment-testing-national-taxonomy-veterans-choice-/013.png)

# <u>Appendix A: Installation Example</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution Enter a Host File: \<your directory\>PXRM_2_0_52.KID

> KIDS Distribution saved on Apr 15, 2015@12:37:27 Comment: HEPATITIS C REMINDERS

> This Distribution contains Transport Globals for the following Package(s): OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// Loading Distribution...

> PXRM\*2.0\*52

> Use INSTALL NAME: PXRM\*2.0\*52 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: Install Package(s) Select INSTALL NAME: PXRM\*2.0\*52 5/19/15@09:33:35

> =\> HEPATITIS C REMINDERS ;Created on Apr 15, 2015@12:37:27

> This Distribution was loaded on May 19, 2015@09:33:35 with header of HEPATITIS C REMINDERS ;Created on Apr 15, 2015@12:37:27

> It consisted of the following Install(s): PXRM\*2.0\*52

> Checking Install for Package PXRM\*2.0\*52

> Install Questions for PXRM\*2.0\*52 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data)

> Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// TELNET PORT

> --------------------------------------------------------------------------------

> Install Started for PXRM\*2.0\*52 : May 19, 2015@09:33:44

> Build Distribution Date: Apr 15, 2015 Installing Routines:

> May 19, 2015@09:33:44

> Running Pre-Install Routine: PRE^PXRMP52I Installing Data Dictionaries:

> May 19, 2015@09:33:44

> Installing Data:

> May 19, 2015@09:33:46

> Running Post-Install Routine: POST^PXRMP52I There are 2 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry PATCH PXRM\*2\*52 HEPATITIS C REMINDERS
2.  Installing Reminder Exchange entry VA-VETERANS CHOICE COMPONENT UPDATE

> Linking and enabling dialogs

> Linking and enabling reminder dialog VA-HEPATITIS C RISK ASSESSMENT to reminder definition VA-HEPATITIS C RISK ASSESSMENT.

> Linking and enabling reminder dialog VA-HEPATITIS C TESTING to reminder definition VA-HEPATITIS C TESTING.

> Updating Routine file...

> Updating KIDS files... PXRM\*2.0\*52 Installed.

> May 19, 2015@09:34:41

> Not a production UCI

> PXRM\*2.0\*52

> Install Completed

## Acronyms 

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
| Term | Definition                                                 |
|----------|----------------------------------------------------------------|
| ORR      | Operational Readiness Review                                   |
| PCS      | Patient Care Services                                          |
| PD       | Product Development                                            |
| PIMS     | Patient Information Management System                          |
| PMAS     | Program Management Accountability System                       |
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
