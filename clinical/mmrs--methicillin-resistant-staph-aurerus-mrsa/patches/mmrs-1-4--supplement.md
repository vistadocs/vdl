---
title: MMRS*1*4 Remediation Guide
doc_type: SUP
doc_label: Supplement
doc_layer: patch
doc_subject: Remediation Guide
app_code: MMRS
app_name: Methicillin Resistant Staph Aurerus (MRSA)
section: CLI
app_status: active
pkg_ns: MMRS
patch_ver: 1
patch_id: MMRS*1*4
group_key: "MMRS:MMRS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - strong
  - mdro
  - table
  - tools
  - site
  - contents
  - setup
  - press
  - division
  - parameters
page_count: 0
word_count: 5666
section_count: 16
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 2017
revision_count: 2
revision_newest: 03/09/2017
revision_oldest: 03/08/2017
docx_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/vle_micro_mmrs_1_0_4_remediation_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/vle_micro_mmrs_1_0_4_remediation_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=189"
---

VistA Lab Enhancements (VLE) – MicrobiologyRelease: MMRS\*1.0\*4Post-Installation Remediation Guide

![](mmrs-1-4-remediation-guide/001.png)

March 2017

Document Version 1.1

Office of Information and Technology (OI&T)

*.*

Revision History

| Date       | Revision | Description                                                                          | Author                             |
|------------|----------|--------------------------------------------------------------------------------------|------------------------------------|
| 03/09/2017 | 1.1      | Removed backing up globals; not required per Product Support. Updated section 6.3.1. | <span class="mark">REDACTED</span> |
| 03/08/2017 | 1.0      | Document baselined.                                                                  | <span class="mark">REDACTED</span> |

<span id="_Toc454522212" class="anchor"></span>Table 1: Documentation Descriptions

Table of Contents

List of Figures

List of Tables

[Table 1: Documentation Descriptions [2](#_Toc454522212)](#_Toc454522212)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the Guide](#organization-of-the-guide)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
- [System Summary](#system-summary)
  - [User Access Levels](#user-access-levels)
  - [Keyboard Conventions](#keyboard-conventions)
- [Preparation](#preparation)
  - [Print out the Checklist](#print-out-the-checklist)
- [Overview of Instructions](#overview-of-instructions)
- [Obtaining Parameter Information](#obtaining-parameter-information)
  - [Inquiry for MDRO Ward Mappings](#inquiry-for-mdro-ward-mappings)
  - [Inquiry for MDRO Tools LAB SEARCH/EXTRACT](#inquiry-for-mdro-tools-lab-searchextract)
- [Review and Remediation](#review-and-remediation)
  - [Deleting the Lab Configurations for a Division(s)](#deleting-the-lab-configurations-for-a-divisions)
  - [Review MDRO Types](#review-mdro-types)
    - [Deleting MDRO Types](#deleting-mdro-types)
  - [Review the MDRO Site Parameters](#review-the-mdro-site-parameters)
    - [Deleting MDRO Site Parameters](#deleting-mdro-site-parameters)
- [Parameter Review and Re-Configuration](#parameter-review-and-re-configuration)
  - [Overview of Program Tools Setup Menu Options](#overview-of-program-tools-setup-menu-options)
  - [Review the MRSA Tools Site Parameter Setup](#review-the-mrsa-tools-site-parameter-setup)
  - [Review the MDRO Historical Days Edit](#review-the-mdro-historical-days-edit)
  - [Review the CRE Tools Site Parameter Setup](#review-the-cre-tools-site-parameter-setup)
  - [Review Isolation Orders](#review-isolation-orders)
    - [Delete Isolation Orders](#delete-isolation-orders)
- [Appendix A: Checklist](#appendix-a-checklist)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a site has installed the MMRS\*1.0\*4 patch, the site’s local configurations will need to be verified for accuracy and possibly re-configured in certain areas as the patch will have overwritten some of the site’s original configurations. Do not run any MDRO reports until the configurations have been verified and remedied. Consultation between Laboratory Information Managers (LIMs), Methicillin-resistant staphylococcus aureus Prevention Coordinators (MPCs), and Information Technologists (IT) will be required to verify and re-configure the site’s MDRO parameters.

Historical configurations and reports prior to the installation of the MMRS\*1.0\*4 patch will provide helpful information in the review process to assess a site’s MDRO parameters. Some examples of historical reports are the IPEC Admission and Discharge/Transmission Reports which contain useful configuration information.

This guide contains sequential instructions for the examination, verification, and possible re-configuration of MDRO parameters. Read the entire guide prior to performing the steps outlined. Appendix A contains a checklist which will aid the user in the steps required. Print out the checklist prior to performing the instructions provided in this guide.

Patch MMRS\*1.0\*5 will not overwrite a site’s local configurations. When the patch is nationally available, proceed with the instructions to install the MMRS\*1.0\*5 patch as outlined in the Patch Description. However, if the site has installed the MMRS\*1.0\*4 patch, the site must perform the tasks specified in this guide.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Organization of the Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is arranged in a manner in which LIMs, MPCs, Information Resource Managers (IRMs) and Automated Data Processing Application Coordinators (ADPACs) staff members who are well versed in VistA’s roll-and-scroll functionality will utilize the software.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, menus, and required security keys.
- User is familiar with the VistA MDRO Program Tools software package.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Oversight for the review and required updates of parameter configurations should be a collaborative process between the LIM, MPC, and IT personnel.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes descriptions of any formatting or symbols and their meaning.

Various symbols are used throughout the documentation to alert the reader to special information. Table 1 gives a description of each of these symbols.

| Font              | Use                              | Example                                                                                                               |
|-----------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined | Hyperlink to another document or URL | For further instructions, refer to the link: <http://www.va.gov/vdl>                                                      |
| Courier New           | Menu options                         | MDRO Tools Parameter Setup                                                                                                |
|                       | Screen prompts                       | Want KIDS to INHIBIT LOGONs during the install? YES//                                                                     |
|                       | VistA filenames                      | XYZ file \#798.1                                                                                                          |
|                       | VistA field names                    | “In the Indicator field, enter the logic that is to be used to determine if the test was positive for the selected MDRO.” |
| Courier New, bold     | User responses to screen prompts     | NO                                                                                                                    |
| Courier New, bold     | Keyboard keys                        | \< F1 \>, \< Alt \>, \< L \>, \<Tab\>, \<Enter\>                                                                          |
| Courier New           | Report names                         | Procedures report                                                                                                         |
| Times New Roman       | Body text (Normal text)              | “There are no changes in the performance of the system once the installation process is complete.”                        |
| Times New Roman Bold  | Emphasis                             | Note: You can also type the access code, followed by a semicolon, followed by the verify code.                        |
| Times New Roman Bold  | Very Important                       | ![](mmrs-1-4-remediation-guide/002.png) symbol                |

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Supporting documentation, such as User Guides, are available on the Department of Veterans Affairs Software Document Library (VDL). The online versions will be updated as needed. Please look for the latest version on the VDL: <http://www.va.gov/vdl>

The following documents were used in preparation of this guide:

- MMRS\*1.0\*4 Patch Description. January 2017.
- MMRS\*1.0\*4 User Guide, Version 1.0, January 2017.

# System Summary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides information regarding access levels, keyboard conventions, and instructions for reviewing and configuring parameters.

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM or IT personnel are responsible for assigning the MDRO Tools Setup Menu, the MDRO Tools Reports Menu, and the MMRS SETUP security key to the appropriate users.

It should be noted that a user who <u>does</u> <u>not</u> have the MMRS Setup security key will only have access to the MDRO Tools Reports Menu.

IRM personnel, LIMs, and MPCs will be jointly responsible for setting up the parameter options in the MDRO Tools Setup Menu.

## Keyboard Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Text centered between arrows represents a keyboard key that should be pressed in order for the system to capture a user response or to move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be selected. \<Tab\> indicates that the Tab key must be selected. For information on the use of the keys is provided below.

- Use the \<Tab\> key to move the cursor to the next field.
- Use the \<Enter\> to select the default.

One, two, or three question marks can be entered at any of the prompts for online help.

| ?   | One question mark displays a brief statement of what information is appropriate for the prompt.             |
|-----|-------------------------------------------------------------------------------------------------------------|
| ??  | Two question marks provide more help, plus any hidden actions.                                              |
| ??? | Three question marks will provide more detailed help, including a list of possible answers, if appropriate. |

The caret (^) plus the \<Enter\> key can be used to exit the current option.

# Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IT personnel will be responsible for performing the majority of the tasks outlined in this guide; therefore, ensure that IT personnel are available.

## Print out the Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](mmrs-1-4-remediation-guide/003.png) Print out the checklist in Appendix A prior to following the instructions in the subsequent sections.

# Overview of Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IT personnel will be responsible for performing the tasks outlined in sections 5 and 6 utilizing FileMan; therefore, ensure that IT personnel are available. The MPC or LIM at the site may perform the parameter review and potential re-configuration(s) as outlined in section 7.

In summary, site personnel will be performing the following tasks:

1.  Removal of the parameters for divisions that were erroneously added by the installation of the MMRS\*1.0\*4 patch.

> In order to determine which parameters will be required to be removed, ask the MPC(s) at your site to provide information on which divisions the reports were previously generated for in order to obtain division information. It is important to note that reports are generated by the configurations of the MDRO Ward Mappings File; if these configurations have not been previously established, then the information will not be available.

> To obtain information on the parameters for the divisions that were erroneously added, follow one of the two steps below depending on whether or not the MDRO Ward Mappings have been configured:

1.  If the MDRO Ward Mappings have been configured, follow the instructions in the section entitled “Inquiry for MDRO Ward Mappings”.
2.  If the MDRO Ward Mappings have <u>not</u> been configured, then perform a FileMan Inquiry for the MDRO Tools Lab Search/Extract File (#104.1) to assess which parameters for divisions were erroneously added. Follow the instructions in the section entitled “Inquiry for MDRO Tools Lab Search/Extract”.
2.  Restoration of the parameter settings for a division that existed before the installation of

> the MMRS\*1.0\*4 patch that were erroneously overwritten. This information is captured in the section entitled “Review and Remediation”.

3.  Finally, review parameters and perform modifications to configurations if required for the following:
- MRSA Tools Site Parameter Setup
- MDRO Historical Days Edit 
- CRE Tools Site Parameter Setup
- Isolation Orders Add/Edit

> Information on how to perform the review and possible re-configuration(s) is included in the section entitled “Parameter Review and Re-Configuration”.

# Obtaining Parameter Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to obtain parameter information, follow the instructions in either the “Review the MDRO Ward Mappings” section if Ward Mappings have been previously configured, or the “Inquiry for MDRO Tools Lab Search/Extract” section if Ward Mappings have not been configured.

![](mmrs-1-4-remediation-guide/004.png) It is required that IT personnel with FileMan access perform the tasks outlined in this entire section.

The following screen capture illustrates the MDRO related files for inquiry.

<span id="_Toc476829521" class="anchor"></span>Figure 1: FileMan MDRO Inquiries

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select VA FileMan Option: Inquire to File Entries</p>
<p>Output from what File: MDRO</p>
<p> </p>
<p>   1      MDRO SITE PARAMETERS <br />
   2      MDRO Tools LAB SEARCH/EXTRACT <br />
   3      MDRO TYPES <br />
   4      MDRO WARD MAPPINGS <br />
 </p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Inquiry for MDRO Ward Mappings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In FileMan, review the MDRO Ward Mappings to investigate which divisions had mappings configured and to aid in the determination of which divisions <u>should</u> <u>not</u> be deleted.

![](mmrs-1-4-remediation-guide/005.png) Existing mappings shown will not require any editing or deleting within the MDRO Ward Mappings.

Follow the instructions below to obtain parameter information:

1.  In FileMan, enter the option Inquire to File Entries and press the \<ENTER\> key.
2.  When prompted, Output From What File:, enter MDRO WARD MAPPINGS and press the \<ENTER\> key.
3.  When prompted, Select MDRO WARD MAPPINGS NAME, enter ? and press the \<ENTER\> key.
4.  When prompted, Do you want the entire XX-Entry MDRO WARD MAPPINGS List? enter Yes and press the \<ENTER\> key.
5.  Enter the MDRO Ward Mappings Name from the list provided for details on the configurations.
6.  Review the list and take note of any configurations for a division(s) that need to be deleted.

An example is provided below.

<span id="_Toc476829522" class="anchor"></span>Figure 2: Review MDRO Ward Mappings

![](mmrs-1-4-remediation-guide/006.png)

## Inquiry for MDRO Tools LAB SEARCH/EXTRACT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An additional way to obtain information is through a FileMan Inquiry of the MDRO Tools Lab Search/Extract File (#104.1).

1.  In FileMan, enter the option Enter or Edit File Entries and press the \<ENTER\> key.
2.  When prompted, INPUT FROM WHAT FILE:, enter MDRO TOOLS LAB SEARCH/EXTRACT and press the \<ENTER\> key.
3.  When prompted, EDIT WHICH FIELD, enter ALL and press the \<ENTER\> key.
4.  When prompted, MDRO TOOLS LAB SEARCH/EXTRACT enter ? press the \<ENTER\> key.
5.  When prompted, Do you want the entire XX-Entry MDRO TOOLS LAB SEARCH/EXTRACT List? enter Yes and press the \<ENTER\> key.
6.  Review the list and take note of any configurations for a division(s) that need to be deleted.

> **NOTE:** The next section entitled “Deleting the Lab Configurations for a Division” provide instructions on how to perform deletions if required.

An example is provided below.

<span id="_Toc476829523" class="anchor"></span>Figure 3: MDRO Tools Lab Search/Extract Review

![](mmrs-1-4-remediation-guide/007.png)

# Review and Remediation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In FileMan, perform reviews and any required remediation by following the instructions in this section.

![](mmrs-1-4-remediation-guide/008.png) It is required that IT personnel with FileMan access perform the tasks outlined in this entire section.

## Deleting the Lab Configurations for a Division(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](mmrs-1-4-remediation-guide/009.png) Delete only those entries that have not been configured that may have been erroneously added after the installation of the MMRS\*1.0\*4 patch. These entries will show information populated in the \#.01 MDRO and the \#1 Division fields, however, lab parameter settings will not have been configured.

To delete the lab configurations for a division(s), follow the instructions below.

1.  In FileMan, enter the option Enter or Edit File Entries and press the \<ENTER\> key.
2.  When prompted, INPUT FROM WHAT FILE:, enter MDRO TOOLS LAB SEARCH/EXTRACT and press the \<ENTER\> key.
3.  When prompted, EDIT WHICH FIELD, enter ALL and press the \<ENTER\> key.
4.  When prompted, MDRO TOOLS LAB SEARCH/EXTRACT enter ? press the \<ENTER\> key.
5.  When prompted, Do you want the entire XX-Entry MDRO TOOLS LAB SEARCH/EXTRACT List? enter Yes and press the \<ENTER\> key.
6.  When prompted, Select MDRO TOOLS LAB SEARCH/EXTRACT: enter the name of each MDRO (i.e. CRB-R).
7.  When prompted, …OK? Yes// press the \<ENTER\> key.
8.  Choose the MDRO(s) and division to delete.
9.  When prompted, enter @ to delete.
10. When prompted, SURE YOU WANT TO DELETE THE ENTIRE MDRO TOOLS LAB SEARCH/EXTRACT? enter Yes and press the \<ENTER\> key.

An example is provided below.

<span id="_Toc476829524" class="anchor"></span>Figure 4: Delete Division(s)

![](mmrs-1-4-remediation-guide/010.png)

## Review MDRO Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In FileMan, review the MDRO Types (#104.2). An example is provided below.

1.  In FileMan, enter the option Inquire to File Entries and press the \<ENTER\> key.
2.  When prompted, OUTPUT FROM WHAT FILE:, enter MDRO Types and press the \<ENTER\> key.
3.  When prompted, MDRO TYPES ABBREVIATION enter ? press the \<ENTER\> key.

<span id="_Toc476829525" class="anchor"></span>Figure 5: Review MDRO Types

![](mmrs-1-4-remediation-guide/011.png)

### Deleting MDRO Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](mmrs-1-4-remediation-guide/012.png) Delete only the types that may have been erroneously added after the installation of the MMRS\*1.0\*4 patch.

1.  In FileMan, enter the option Enter or Edit File Entries and press the \<ENTER\> key.
2.  When prompted, INPUT FROM WHAT FILE:, enter MDRO Types and press the \<ENTER\> key.
4.  When prompted, EDIT WHICH FIELD, enter ALL and press the \<ENTER\> key.
5.  When prompted, MDRO TYPES ABBREVIATION enter the MDRO (i.e. C. Diff) press the \<ENTER\> key.
6.  When prompted, Are you adding ‘x’ as a new MDR Types (the Xth)? enter No and press the \<ENTER\> key.
7.  When prompted, MDRO TYPES ABBREVIATION enter the MDRO (e.g. C. Diff) press the \<ENTER\> key.
8.  When prompted, Select Division: press the \<ENTER\> key to accept.
9.  When prompted, enter @ to delete.
10. When prompted, SURE YOU WANT TO DELETE THE ENTIRE DIVISION? enter Yes and press the \<ENTER\> key.

## Review the MDRO Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In FileMan, review the MDRO Site Parameters.

1.  In FileMan, enter the option Enter or Edit File Entries and press the \<ENTER\> key.
2.  When prompted, OUTPUT FROM WHAT FILE:, enter MDRO SITE PARAMETERS and press the \<ENTER\> key.
3.  When prompted, MDRO SITE PARAMETERS DIVISION, enter ? and press the \<ENTER\> key.
4.  When prompted, EDIT WHICH FIELD, enter ALL and ? and press the \<ENTER\> key.

### Deleting MDRO Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](mmrs-1-4-remediation-guide/013.png) Delete only the parameters that may have been erroneously added after the installation of the MMRS\*1.0\*4 patch.

1.  In FileMan, enter the option Enter or Edit File Entries and press the \<ENTER\> key.
2.  When prompted, INPUT FROM WHAT FILE:, enter MDRO SITE PARAMETERS and press the \<ENTER\> key.
3.  When prompted, MDRO SITE PARAMETERS DIVISION, enter ? and press the \<ENTER\> key.
4.  When prompted, EDIT WHICH FIELD, enter ALL and ? and press the \<ENTER\> key.
5.  When prompted, Do you want the entire X-Entry MEDICAL CENTER DIVISION LIST? enter No and press the \<ENTER\> key.
6.  When prompted, Select MDRO SITE PARAMETER DIVISION enter the name of the division and press the \<ENTER\> key.
7.  When prompted, OK? Yes// press the \<ENTER\> key to accept.
8.  When prompted DIVISION:, enter @ to delete.
9.  When prompted, SURE YOU WANT TO DELETE THE ENTIRE MDRO SITE PARAMETERS? enter Yes and press the \<ENTER\> key.
10. If prompted, DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE A WHILE) enter Yes and press the \<ENTER\> key. Follow the next two instructions.
11. When prompted, WHICH DO YOU WANT TO DO? Enter 1 to DELETE ALL SUCH POINTERS.
12. When prompted, DELETE ALL POINTERS? enter Yes and press the \<ENTER\> key.

<span id="_Toc476829526" class="anchor"></span>Figure 6: Deleting MDRO Site Parameters Division

![](mmrs-1-4-remediation-guide/014.png)

# Parameter Review and Re-Configuration 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPC or LIM at the site may perform the parameter review and potential re-configuration(s) outlined in this entire section.

Follow the instructions in this section to review parameters and perform modifications to configurations if required for the following:

- MRSA Tools Site Parameter Setup
- MDRO Historical Days Edit 
- CRE Tools Site Parameter Setup
- Isolation Orders Add/Edit

## Overview of Program Tools Setup Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the parameters for the six options listed under the MDRO Tools Setup Menu. Out of the six options shown, only the four highlighted options, as stated previously, need to be reviewed and possibly re-configured.

Included in this section are screen captures which contain examples with pre-populated fields.

![](mmrs-1-4-remediation-guide/015.png)In order to obtain access to the menu, the IRM or IT personnel will need to assign access rights to the MDRO Tools Setup Menu and provide the MMRS SETUP key.

The MDRO Tools Setup Menu Options are illustrated in the screen capture below.

<span id="_Toc476210779" class="anchor"></span>Figure 7: MDRO Tools Setup Menu Options

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MMRS MDRO TOOLS SETUP MENU     MDRO Tools Setup Menu </p>
<p>   <mark>1</mark>      <mark>MRSA Tools Site Parameter Setup</mark> <br />
   2      MDRO Tools Lab Parameter Setup <br />
   3      MRSA Tools Ward Mapping Setup <br />
   <mark>4</mark>      <mark>MDRO Historical Days Edit <br />
</mark>   <mark>5</mark>      <mark>CRE Tools Site Parameter Setup</mark></p>
<p><mark>6</mark> <mark>Isolation Orders Add/Edit</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Review the MRSA Tools Site Parameter Setup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the parameters in this section. An overview is provided below.

The MRSA Tools Site Parameter Setup option allows the user(s) to setup the following:

- Divisions for their facility.
- Business rules for nares screening for each division.

When adding divisions, include the following facility areas:

- Acute care hospital(s) (AC)
- Community Living Centers (CLC)

> **NOTE:** When adding divisions, do not include Community Based Outreach Clinics (CBOC), behavioral/mental health facilities, domiciliary facilities, etc.

During parameter setup, the user will have to answer prompts regarding business rules for nares screening on transfer and discharge. Based on the business rules at the facility enter either YES or NO in the prompts. Historical information may be obtained from IPEC Reports generated prior to the installation of patch MMRS\*1.0\*4. For example, historical IPEC Admission and Discharge /Transmission reports may be utilized to gain information on answering required prompts in the MRSA Tools Site Parameter Setup.

Information regarding MDRO Tools Lab Parameter Setup option screen prompts and help prompts definitions are provided in Appendix A.

> **NOTE:** The MDRO-PT national package materials (i.e., IPEC Reports) should be reviewed periodically by the sites for data validation.

<span id="_Toc476829528" class="anchor"></span>Figure 8: MRSA Tools Site Parameter Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu &lt;TEST ACCOUNT&gt; Option: 1 MRSA Tools Site Parameter</p>
<p>Setup</p>
<p>Select MRSA Site Parameters Division: CHE</p>
<p>1 XXXXX MOC 442HK</p>
<p>2 XXXXX VAMROC 442</p>
<p>CHOOSE 1-2: 2 XXXXX VAMROC 442</p>
<p>1. Receiving unit screen on unit-to-unit transfers: NO// <strong>NO</strong></p>
<p>2. Discharging unit screen on unit-to-unit transfers: YES// <strong>YES</strong></p>
<p>3. Screen patients with MRSA history on transfer-in: YES// <strong>YES</strong></p>
<p>4. Screen patients with MRSA history on discharge/death/transfer-out: YES// <strong>YES</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** There should never be a NO listed for both the Receiving unit screen on unit-to-unit transfers and Discharging unit screen on unit-to-unit transfers prompts. This would indicate to the program that neither the receiving nor discharging unit is screening the patients on unit-to-unit transfers.

> **NOTE:** It is required that business rules are added for each division.

## Review the MDRO Historical Days Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the information in this section for accuracy of historical reporting days. Perform re-configurations if deemed necessary. An overview is provided below.

This option allows the user to define the time frame selected for each MDRO defined in the MDRO Tools Lab Parameter Setup. The information entered in this menu provides information for the Print Isolation Report option (the report displays patient’s historical lab data for certain MDROs). The user will be asked to enter the number of historical days the program should search for a positive result for each MDRO. This information can only be entered in days (e.g., 30 for 1 month; 90 for 1 quarter; 365 for 1 year). If no response is entered, the program will not display that MDRO on the Isolation Report.

![](mmrs-1-4-remediation-guide/016.png)Note:All sites must enter the following in historical days: 365; this will ensure that the history within the past year is identified for prevalence and transmission purposes. However, the MPC at the site may provide different guidelines.

For other MDROs selected, it is at the discretion of the facility to determine the time frame to search for the last positive MDRO result.

1.  Select the division by entering it. Press the \<ENTER\> key. For a list of divisions, enter a ?
2.  When prompted, enter the number of historical days the program should search for a positive result for each MDRO.

<span id="_Toc475968379" class="anchor"></span>Figure 9: MDRO Historical Days Edit

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu Option: <strong>MDRO Historical Days Edit</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Enter the number of days to search for MRSA: <strong>365</strong></p>
<p>Enter the number of days to search for IMP: <strong>365</strong></p>
<p>Enter the number of days to search for VRE: <strong>365</strong></p>
<p>Enter the number of days to search for C. diff: <strong>365</strong></p>
<p>Enter the number of days to search for ESBL: <strong>365</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Review the CRE Tools Site Parameter Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides instructions for reviewing the CRE parameters. Specifically, a site may:

- Add division(s) by following the instructions in this section.
- Add or delete specimen(s) by following the instructions in this section.

To add a division, follow the instructions below.

1.  When prompted, Select CRE Site Parameters Division: enter a ? and press the \<ENTER\> key.
2.  When prompted, Select CRE Site Parameters Division: enter the division for the parameters and press the \<ENTER\> key.
1.  When prompted, Are you adding 'Division Name' as a new MDRO SITE PARAMETERS (the XTH)? enter Yes and press the \<ENTER\> key.

An example is provided below.

<span id="_Toc476829530" class="anchor"></span>Figure 10: Add Division(s) for CRE

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu &lt;TEST ACCOUNT&gt; Option: 5 CRE Tools Site Parameter</p>
<p>Setup</p>
<p>Select CRE Site Parameters Division: ?</p>
<p>Answer with MDRO SITE PARAMETERS DIVISION</p>
<p>Choose from:</p>
<p>CASPER</p>
<p>XXXXX MOC</p>
<p>XXXXX VAMROC</p>
<p>FORT COLLINS</p>
<p>GREELEY</p>
<p>SIDNEY</p>
<p>You may enter a new MDRO SITE PARAMETERS, if you wish</p>
<p>Enter the division the parameters are for.</p>
<p>Answer with MEDICAL CENTER DIVISION NUM, or NAME</p>
<p>Choose from:</p>
<p>1 XXXXX VAMROC 442</p>
<p>2 CASPER 442GA</p>
<p>3 FORT COLLINS 442GC</p>
<p>4 GREELEY 442GD</p>
<p>5 SIDNEY 442GB</p>
<p>6 XXXXX MOC 442HK</p>
<p>7 SQADIVTESTFEB2017 442SQA</p>
<p>Select CRE Site Parameters Division: SQADIVTESTFEB2017 442SQA</p>
<p>Are you adding 'SQADIVTESTFEB2017' as</p>
<p>a new MDRO SITE PARAMETERS (the 7TH)? No// <strong>YES</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

To review CRE parameters and either add or edit/delete specimen(s), follow the instructions below. The CRE Tools Parameter Setup menu allows the user(s) to configure the CRE parameters for division(s) by either adding or editing specimens.

1.  When prompted, enter the name of the division and press the \<ENTER\> key or press the ? for a list of divisions and select the division from the list.
2.  When prompted, select either Add to add a specimen for CRE Surveillance Screens or Edit to edit an existing specimen.
    1.  If editing or deleting a specimen, type Edit and press the \<ENTER\> key. Enter the name of the specimen and press the \<ENTER\> key. To obtain a list of specimens, type ? and the \<ENTER\> key. Note: If the list of specimens does not appear correctly for the site, edit the specimens. Use this option to delete specimens that may have been erroneously entered during the installation of patch MMRS\*1.0\*4.
    2.  If adding a specimen, type Add and press the \<ENTER\> key. Enter the name of the specimen and press the \<ENTER\> key.

<span id="_Toc476829531" class="anchor"></span>Figure 11: CRE Tools Site Parameter Setup: Edit/Delete a Specimen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu &lt;FACILITY ACCOUNT&gt; Option: 5 CRE Tools Site Parameter</p>
<p>Setup</p>
<p>Select CRE Site Parameters Division: ?</p>
<p>Answer with MDRO SITE PARAMETERS DIVISION</p>
<p>Choose from:</p>
<p>CASPER</p>
<p>XXXXX MOC</p>
<p>XXXXX VAMROC</p>
<p>FORT COLLINS</p>
<p>GREELEY</p>
<p>SIDNEY</p>
<p>You may enter a new MDRO SITE PARAMETERS, if you wish Enter the division the parameters are for.</p>
<p>Answer with MEDICAL CENTER DIVISION NUM, or NAME</p>
<p>Choose from:</p>
<p>1 XXXXX VAMROC 442</p>
<p>2 CASPER 442GA</p>
<p>3 FORT COLLINS 442GC</p>
<p>4 GREELEY 442GD</p>
<p>5 SIDNEY 442GB</p>
<p>6 XXXXX MOC 442HK</p>
<p>Select CRE Site Parameters Division: 1 XXXXX VAMROC 442</p>
<p>...OK? Yes// (Yes)</p>
<p>Select one of the following:</p>
<p>A ADD</p>
<p>E EDIT</p>
<p>Do you want to Add or Edit specimen(s) for CRE Surveillance Screens: E// EDIT</p>
<p>Select Specimen to delete: ?</p>
<p>Answer with SPECIMEN</p>
<p>Choose from:</p>
<p>FECES</p>
<p>SKIN</p>
<p>Enter the specimen you want to edit.</p>
<p>Select Specimen to delete: FECES</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc476829532" class="anchor"></span>Figure 12: CRE Tools Site Parameter Setup: Add a Specimen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu &lt;FACILITY ACCOUNT&gt; Option: 5 CRE Tools Site Parameter</p>
<p>Setup</p>
<p>Select CRE Site Parameters Division: ?</p>
<p>Answer with MDRO SITE PARAMETERS DIVISION</p>
<p>Choose from:</p>
<p>CASPER</p>
<p>XXXXX MOC</p>
<p>XXXXX VAMROC</p>
<p>FORT COLLINS</p>
<p>GREELEY</p>
<p>SIDNEY</p>
<p>You may enter a new MDRO SITE PARAMETERS, if you wish Enter the division the parameters are for.</p>
<p>Answer with MEDICAL CENTER DIVISION NUM, or NAME</p>
<p>Choose from:</p>
<p>1 XXXXX VAMROC 442</p>
<p>2 CASPER 442GA</p>
<p>3 FORT COLLINS 442GC</p>
<p>4 GREELEY 442GD</p>
<p>5 SIDNEY 442GB</p>
<p>6 XXXXX MOC 442HK</p>
<p>Select CRE Site Parameters Division: 1 XXXXX VAMROC 442</p>
<p>...OK? Yes// (Yes)</p>
<p>Select one of the following:</p>
<p>A ADD</p>
<p>E EDIT</p>
<p>Do you want to Add or Edit specimen(s) for CRE Surveillance Screens: E// ADD</p>
<p>Select Specimen: FECES</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Review Isolation Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the orderable item(s). Note any Isolation Orders that need to be deleted.

The Isolation Orders Add/Edit option allows the user to enter the orderable item(s) at their site that are used for isolation purposes. Each Isolation Order added must be mapped to one of the following Expanded Precaution Types: Contact Precautions, Contact Precautions Special, Airborne Infection, Droplet, Protective Environment, and Isolation Order. The information entered will be used to populate the Print Isolation Report option.

> **NOTE:** This option should only be used if the site uses orderable items when a patient is required to be in isolation.

1.  Select the division.
2.  At the Isolation Orders, enter an order and press \<TAB\>
3.  At the Expanded Precaution Type, enter a precaution type and press \<TAB\> to return to the Isolation Orders field.
4.  When finished, enter the \<TAB\> key at the Isolation Orders field.
5.  At the Command prompt, enter S to save the form and press the \<ENTER\> key.
6.  At the Command prompt, enter E to exit the form and press the \<ENTER\> key.

<span id="_Toc249158689" class="anchor"></span>Figure 13: MDRO Tools Isolation Orders Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS ISOLATION ORDERS SETUP</p>
<p>DIVISION: XXXXX VAMC</p>
<p>___________________________________________________________________________</p>
<p>Isolation Orders Expanded Precaution Type</p>
<p><strong>CONTACT PRECAUTIONS CONTACT PRECAUTIONS</strong></p>
<p><strong>CONTACT PRECAUTIONS SPECIAL CONTACT PRECAUTIONS SPECIAL</strong></p>
<p><strong>AIRBORNE INFECTION ISOLATIOTI AIRBORNE INFECTION</strong></p>
<p><strong>DROPLET PRECAUTIONS DROPLET</strong></p>
<p><strong>PROTECTIVE ENVIRONMENT PROTECTIVE ENVIRONMENT</strong></p>
<p><strong>ISOLATION ORDER ISOLATION ORDER</strong></p>
<p>__________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Delete Isolation Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](mmrs-1-4-remediation-guide/017.png)Delete only the Isolation Orders that may have been erroneously added after the installation of the MMRS\*1.0\*4 patch.

1.  In the Isolation Orders Add/Edit option, select a Division.
2.  Under the Isolation Orders field, enter a @ to delete.
3.  When prompted, Are you sure you want to delete this entire Subrecord (Y/N)? enter Yes and press the \<ENTER\> key.

<span id="_Toc476829534" class="anchor"></span>Figure 14: Delete Isolation Orders

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>                      MDRO TOOLS ISOLATION ORDERS SETUP</p>
<p><strong>DIVISION</strong>: <strong>XXXXX VAMROC                   </strong></p>
<p>________________________________________________________________________________</p>
<p>Isolation Orders                       Expanded Precaution Type</p>
<p><strong>1 1/2 HOUR GLUCOSE PP              </strong>    <strong>                                   </strong></p>
<p> <strong>                                    </strong>   <strong>                                   </strong></p>
<p>_______________________________________________________________________________</p>
<p>COMMAND:    </p>
<p>       MDRO TOOLS ISOLATION ORDERS SETUP</p>
<p><strong>DIVISION</strong>: <strong>XXXXX VAMROC                   </strong></p>
<p>________________________________________________________________________________</p>
<p>Isolation Orders                       Expanded Precaution Type</p>
<p><strong>@                                  </strong>    <strong>                                   </strong></p>
<p>_______________________________________________________________________________</p>
<p>COMMAND:                             </p>
<p>MDRO TOOLS ISOLATION ORDERS SETUP</p>
<p><strong>DIVISION</strong>: <strong>XXXXX VAMROC                   </strong></p>
<p>________________________________________________________________________________</p>
<p>Isolation Orders                       Expanded Precaution Type</p>
<p>_______________________________________________________________________________</p>
<p>  WARNING: DELETIONS ARE DONE IMMEDIATELY!</p>
<p>           (EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)</p>
<p>Are you sure you want to delete this entire Subrecord (Y/N)? <strong> Y </strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Appendix A: Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Print out the checklist below to ensure that all of the instructions have been completed.

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 57%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>#</strong></th>
<th><strong>Actions/Steps</strong></th>
<th><strong>Section Reference</strong></th>
<th><strong>Owner</strong></th>
<th><strong></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1.</strong></td>
<td><strong>Print out the Checklist.</strong></td>
<td><strong>3.1</strong></td>
<td><strong>IT</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>2.</strong></td>
<td><strong>Read Overview of Instructions.</strong></td>
<td><strong>4.</strong></td>
<td><strong>IT, MPC, LIM</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>3.</strong></td>
<td><p><strong>Obtain Parameter Information:</strong></p>
<p><strong>Either:</strong></p>
<ol type="a">
<li><p><strong>Inquiry for MDRO Ward Mappings</strong></p></li>
</ol>
<p><strong><u>OR</u></strong></p>
<ol start="2" type="a">
<li><p><strong>Inquiry for MDRO Tools Lab Search/Extract</strong></p></li>
</ol></td>
<td><strong>5.</strong></td>
<td><strong>IT</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>4.</strong></td>
<td><strong>Perform remediation if required for deleting the lab configurations for a division.</strong></td>
<td><strong>6.1</strong></td>
<td><strong>IT</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>5.</strong></td>
<td><strong>Review MDRO Types.</strong></td>
<td><strong>6.2</strong></td>
<td><strong>IT</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>6.</strong></td>
<td><strong>Perform remediation if required for deleting MDRO Types.</strong></td>
<td><strong>6.2.1</strong></td>
<td><strong>IT</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>7.</strong></td>
<td><strong>Review MDRO Site Parameters.</strong></td>
<td><strong>6.3</strong></td>
<td><strong>IT</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>8.</strong></td>
<td><strong>Perform remediation if required for deleting MDRO Site Parameters.</strong></td>
<td><strong>6.3.1</strong></td>
<td><strong>IT</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>9.</strong></td>
<td><strong>Read the Parameter Review and Reconfiguration &amp; the Overview of Program Tools Setup Menu Options.</strong></td>
<td><strong>7. &amp; 7.1</strong></td>
<td><strong>MPC or LIM</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>10.</strong></td>
<td><strong>Review the MRSA Tools Site Parameter Setup.</strong></td>
<td><strong>7.2</strong></td>
<td><strong>MPC or LIM</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>11.</strong></td>
<td><strong>Perform remediation if required for re-configuration of the MRSA Tools Site Parameters.</strong></td>
<td><strong>7.2</strong></td>
<td><strong>MPC or LIM</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>12.</strong></td>
<td><strong>Review the MDRO Historical Days Edit.</strong></td>
<td><strong>7.3</strong></td>
<td><strong>MPC or LIM</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>13.</strong></td>
<td><strong>Perform remediation if required for re-configuration of MDRO Historical Days Edit.</strong></td>
<td><strong>7.3</strong></td>
<td><strong>MPC or LIM</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>14.</strong></td>
<td><strong>Review the CRE Tools Site Parameter Setup.</strong></td>
<td><strong>7.4</strong></td>
<td><strong>MPC or LIM</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>15.</strong></td>
<td><strong>Perform remediation if required for re-configuration of CRE Tools Site Parameter Setup (i.e. deleting specimen(s)).</strong></td>
<td><strong>7.4</strong></td>
<td><strong>MPC or LIM</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>16.</strong></td>
<td><strong>Review the Isolation Orders setup.</strong></td>
<td><strong>7.5</strong></td>
<td><strong>MPC or LIM</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>17.</strong></td>
<td><strong>Perform remediation if required for the possible deletion of Isolation Orders.</strong></td>
<td><strong>7.5.1</strong></td>
<td><strong>MPC or LIM</strong></td>
<td></td>
</tr>
</tbody>
</table>