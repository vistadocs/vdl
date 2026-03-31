---
consolidated_title: "laboratory nds lim user manual"
app_code: LR
doc_type: UM
master_source: "LR*5.2*500 Laboratory NDS LIM User Manual"
master_pub_date: March 2018
consolidated_from: 2 versions
prior_versions:
  - "LR*5.2*468 Laboratory NDS LIM User Manual"
---

---
title: |
  VA Laboratory Results

  Collaborative Terminology Tooling  
  & Data Management (CTT & DM)

  Native Domain Standardization  
  (NDS)

  LIM NDS User Manual
---

![](lr-5-2-500-laboratory-nds-lim-user-manual/001.png)

March 2018

Department of Veterans Affairs (VA)<span id="_Toc41989686" class="anchor"></span>

Revision History

<table>
<caption><p><span id="_Ref386465892" class="anchor"></span>Table . Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3/2018</td>
<td>1.3</td>
<td><p>Updates for patch LR*5.2*500</p>
<ul>
<li><p><a href="#notes-on-entering-or-editing-a-testspecimen-mltf-entry">Section 1.3</a> changed ‘the first 30 characters’ to ‘the first 60 characters’.</p></li>
<li><p><a href="#ntrt-process">Section 1.4</a> Figure 1 Changed email to message.</p></li>
<li><p>Added <a href="#lr5.2500">Section 1.1.7</a></p></li>
<li><p>Updated <a href="#_Using_the_Walk">Section 2.1.2</a></p></li>
<li><p>Added Walk Associate Test to MLTF Reset Functionality <a href="#Example_WAT_to_MLTF">Figure 9</a></p></li>
<li><p><a href="#using-the-managed-items-edit-option-mie">Section 2.1.3</a> item 9. Changed reference from ISAAC to CTT TOOLING.</p></li>
<li><p><a href="#_Ref505601068">Figure 10</a> and <a href="#_Ref452574668">Figure 12</a>. Changed reference from ISAAC to CTT TOOLING.</p></li>
</ul></td>
<td>Mantech Mission Solutions and Services, NDS <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/2018</td>
<td>1.2</td>
<td><p>Updates for patch LR*5.2*495:</p>
<ul>
<li><p>Added Section <u>1.1.6</u></p></li>
<li><p>Updated Table 2 in Section <u>1.7.2</u></p></li>
<li><p>Update Figure 3 in Section <u>1.7.1</u></p></li>
<li><p>Update Figure 6 in Section <u>2.1.1</u></p></li>
<li><p>Update Figure 10 in <a href="#using-the-managed-items-edit-option-mie">Section 2.1.3</a></p></li>
<li><p>Update Figure 12 in <a href="#using-the-managed-items-edit-option-mie">Section 2.1.3</a></p></li>
<li><p>Update Figure 16 in Section <u>2.1.7</u></p></li>
<li><p>Added Section <u>2.1.10</u></p></li>
<li><p>Added Section <u>2.1.11</u></p></li>
</ul></td>
<td>Collaborative Terminology Tooling &amp; Data Management (CTT &amp; DM) Mantech Mission, Solutions and Services <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2/2/2017</td>
<td>1.1</td>
<td><p>Changed 1 title from System Summary to LIM NDS SUMMARY.</p>
<p>Added caution text box to Section LIM NDS Summary <a href="#lim-nds-summary">Section 1.</a></p>
<p>Added <a href="#related-patches">Section 1.1</a> describing the patches associated to the LAB NDS effort.</p>
<p>Added <a href="#Associating_to_MLTF">Section 1.2</a> Associating Site/Specimen to MLTF.</p>
<p>Added <a href="#notes-on-entering-or-editing-a-testspecimen-mltf-entry">Section 1.3</a> Note on entering or editing a Test/Specimens MLTF entry.</p>
<p>Added <a href="#ntrt-process">Section 1.4</a> NTRT Process.</p>
<p>Changed Section 1.1 to Section 1.5</p>
<p><a href="#Master_Lab_Test_File_Create_Udate_Proces">Section 1.6.1</a> Updated items 1-9.</p>
<p>Updated <a href="#using-the-associate-test-to-nds-mltf-option-atm">Section 2.1.1</a> updated item 3 note. Updated <u>Figure 5</u>.</p>
<p>Updated <a href="#_Using_the_Walk">Section 2.1.2</a><u>,</u> Updated Figure 9</p></td>
<td>Mantech Mission, Solutions and Services <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/2016</td>
<td>1.0</td>
<td>Delivery to Customer</td>
<td>Mantech Mission, Solutions and Services Management</td>
</tr>
</tbody>
</table>

<span id="_Ref386465892" class="anchor"></span>Table . Documentation Symbol Descriptions

Contents

Figures and Tables

Table of Figures

Table of Tables

[Table 1. Documentation Symbol Descriptions [2](#_Ref386465892)](#_Ref386465892)

[Table 2. LIM NDS MENU Options and Descriptions [13](#_Ref505600969)](#_Ref505600969)

<span id="_Hlt446130591" class="anchor"></span>

Orientation

How to Use this Manual

In this manual the following major features of the Laboratory LIM NDS functions are introduced along with a description on how to use them:

- [MASTER LABORATORY TEST file Creation and Update Process Flow](#master-laboratory-test-file-creation-and-update-process-flow)
- [Navigating to the LIM NDS Menu](\l)
- [LIM NDS MENU Options and the Descriptions](\l)
- [Using the Associate Test to NDS MLTF Option](\l)
- [Using the Managed Items Edit Option](\l)
- [Using the Purge NDS File 60 Audits Option](\l)
- [Running the LIM NDS Reports Audit Option](\l)
- [<u>Using the Edit Inactive Date Multiple Option</u>](\l)
- [Using the “Inactive Date Single Edit” Option](\l)

![](lr-5-2-500-laboratory-nds-lim-user-manual/002.png) NOTE: This document is available in Microsoft Word (.docx), and Adobe Acrobat Portable Document Format (PDF)

Intended Audience

The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Automated Data Processing Application Coordinators (ADPACs)
- Information Resource Management (IRM)—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management.
- Laboratory Information Managers (LIM)

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

![](lr-5-2-500-laboratory-nds-lim-user-manual/003.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).

Documentation Disclaimer

This manual provides an overall explanation of VA Laboratory LIM NDS system and the functionality; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet Websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OI&T) VistA Development Intranet website.

![](lr-5-2-500-laboratory-nds-lim-user-manual/004.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> describes each of these symbols.

| Symbol                                                                                                            | Description                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](lr-5-2-500-laboratory-nds-lim-user-manual/005.png)      | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](lr-5-2-500-laboratory-nds-lim-user-manual/006.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |
| ![](lr-5-2-500-laboratory-nds-lim-user-manual/007.png)                                                                 | TIP: Used to inform the reader of helpful tips or tricks they can use.                                            |

<span id="_Ref505600969" class="anchor"></span>Table . LIM NDS MENU Options and Descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
- Patient and user names are formatted as follows:  
  \<*Application Name/Abbreviation/Namespace*\>PATIENT,\[*N*\] and \<*Application Name/Abbreviation/Namespace*\>USER,\[*N*\] respectively, where “\<*Application Name/Abbreviation/Namespace*\>” is defined in the Approved Application Abbreviations document and “*N*” represents the first name as a number spelled out and incremented with each new entry. For example, in VA FileMan (FM) test patient and user names would be documented as follows: FMPATIENT, ONE; FMPATIENT, TWO; FMPATIENT, THREE; etc.
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
- User’s responses to online prompts are bold typeface, underlined and highlighted in yellow (e.g., <span class="mark">\<<u>Enter</u>\></span>).
- Emphasis within a dialogue box is bold typeface, underlined and highlighted in blue (e.g. <span class="mark"><u>STANDARD LISTENER: RUNNING</u></span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](lr-5-2-500-laboratory-nds-lim-user-manual/008.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., DIEXTRACT).

![](lr-5-2-500-laboratory-nds-lim-user-manual/009.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g. CamelCase).

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to your customized toolbar.
9.  Select OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

![](lr-5-2-500-laboratory-nds-lim-user-manual/010.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

Help at Prompts

VistA software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of the software.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- Laboratory Information Manager functions

Reference Materials

Readers who wish to learn more about the VA Laboratory NTRT system should consult the following documents:

- [<u>NTRT User Guide</u>](http://vaww.oed.portal.va.gov/projects/sts/VETS%20Consolidated/VETS/STS_VETS_NTRT%20User%20Guide.docx) (STS SharePoint \> VETS Consolidated \> VETS \> STS_VETS_NTRT User Guide.docx)

VA Laboratory documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>

VistA software documentation can be downloaded from the VA Software Document Library (VDL) at: <http://www.va.gov/vdl/>

![](lr-5-2-500-laboratory-nds-lim-user-manual/011.png) REF: Laboratory manuals are located on the VDL.

# LIM NDS Summary


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [LIM NDS Summary](#lim-nds-summary)
  - [Related Patches](#related-patches)
    - [XU\8\665](#xu8665)
    - [HDI\1.0\15](#hdi1015)
    - [LR\5.2\468](#lr52468)
    - [LA\5.2\92](#la5292)
    - [LR\5.2\481](#lr52481)
    - [LR\5.2\495](#lr52495)
    - [LR\5.2\500](#lr52500)
  - [Associating a Site/Specimen to the MLTF](#associating-a-sitespecimen-to-the-mltf)
  - [Notes on Entering or Editing a Test/Specimen MLTF Entry](#notes-on-entering-or-editing-a-testspecimen-mltf-entry)
  - [NTRT Process](#ntrt-process)
  - [System Configuration](#system-configuration)
  - [MASTER LABORATORY TEST file Creation and Update Process Flow](#master-laboratory-test-file-creation-and-update-process-flow)
    - [MASTER LABORATORY TEST File Creation and Update Process](#master-laboratory-test-file-creation-and-update-process)
  - [Getting Started](#getting-started)
    - [Navigating to the LIM NDS MENU](#navigating-to-the-lim-nds-menu)
    - [LIM NDS MENU Options and the Descriptions](#lim-nds-menu-options-and-the-descriptions)
- [Using the Software](#using-the-software)
  - [Laboratory Information Manager (LIM) Native Domain Standardization (NDS) Procedures](#laboratory-information-manager-lim-native-domain-standardization-nds-procedures)
    - [Using the Associate Test to NDS MLTF Option (ATM)](#using-the-associate-test-to-nds-mltf-option-atm)
    - [Using the Walk Associate Test to MLTF Option (WAT)](#using-the-walk-associate-test-to-mltf-option-wat)
    - [Using the Managed Items Edit Option (MIE)](#using-the-managed-items-edit-option-mie)
    - [Running the LIM NDS Reports](#running-the-lim-nds-reports)
    - [Running the Lab to MLTF Extract Report](#running-the-lab-to-mltf-extract-report)
    - [Running the Print NDS Audits in File 60 Report](#running-the-print-nds-audits-in-file-60-report)
    - [Running the Print Specimens Without VUIDS Report](#running-the-print-specimens-without-vuids-report)
    - [Using the Purge NDS File 60 Audits Option](#using-the-purge-nds-file-60-audits-option)
    - [Running the Print Specimens with Inactive VUIDS Report](#running-the-print-specimens-with-inactive-vuids-report)
    - [Using the Edit Inactive Date Multiple Option](#using-the-edit-inactive-date-multiple-option)
    - [Using the “Inactive Date Single Edit” Option](#using-the-inactive-date-single-edit-option)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
  - [Changing User ID and Password](#changing-user-id-and-password)
  - [Exit System](#exit-system)
  - [Caveats and Exceptions](#caveats-and-exceptions)
  - [Troubleshooting](#troubleshooting)
    - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
- [A](#a)
- [C](#c)
- [D](#d)
- [G](#g)
- [H](#h)
- [I](#i)
- [M](#m)
- [R](#r)
- [U](#u)
- [V](#v)
- [W](#w)
Creation of one National Master Laboratory Tests file (MLTF) with Logical Observation Identifier Names and Codes (LOINC) would enable all VHA services and other non-VHA services including private sectors to perform searches, data extractions and report generations, and there would be dependency on only one master file instead of dependency on a number of Lab tables.

## Related Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The related patches for this effort are:

### XU\*8\*665

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XU\*8\*665 patch is a required Kernel system patch. This patch is used by the STS group when deploying content for the MASTER LABORATORY TEST file (#66.3)

### HDI\*1.0\*15

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HEALTH DATA & INFORMATICS (HDI) patch HDI\*1.0\*15 is a required HDI patch. This patch registers the MASTER LABORATORY TEST file (#66.3) into the HDI system. The HDI system manages the VA Unique Identifier (VUID) numbering, and is invoked during the STS content deployment.

### LR\*5.2\*468

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LR\*5.2\*46 patch is a Lab application patch. This patch contains Data Definition and routine updates needed for managing the association of LABORATORY TEST file (#60) entries with the MASTER LABORATORY TEST file (#66.3).

### LA\*5.2\*92

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LA\*5.2\*92 patch is a Lab Automated Instrument patch. This patch updates Automated Instrument routines that get the LOINC Code for a Test/Specimen.

### LR\*5.2\*481

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LR\*5.2\*481 is a Lab informational patch. This informational patch details how changing the SEND NTRT MESSAGES field (# .1) in the LAB MLTF MANAGED ITEMS file (#66.4) is set to ‘Y’ for yes. This patch should only be exercised once content for the MASTER LABORATORY TEST file (#66.3) has been deployed to your facility.

### LR\*5.2\*495

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LR\*5.2\*495 is a Lab application patch. This patch contains the Data Definition, routine updates, and functionality involving managing the modification of the new INACTIVE DATE field (#64.91) within the LABORATORY ETIOLOGY file (#61.2)

### LR\*5.2\*500

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LR\*5.2\*500 is a Lab application patch. This patch added new fields to the LABORATORY TEST File (#60) that will be utilized in the future under guidance of the VHA LABORATORY Domain personnel.

The NTRT message was enhanced to include the following additional fields: SITE NOTES (#505), INTERPRETATION (#60.01,5.5), TEST INACTIVE DATE (#133), SPECIMEN CREATE DATE (#60.01,35), IN HOUSE TEST (#134), POC TEST (#135), SCANNED IMAGE TEST (#137), PERFORMING LAB (#141), ORDER CODE (#60.16,1)

The LAB MLTF MANAGED ITEMS File (#66.4) fields whose names started with ISAAC (this was the testing name for the CTT Tooling team) have been changed to CTT TOOLING.

The MASTER LABORATORY TEST File (#66.3) has been modified to accommodate the changing field lengths for the LOINC Code information. A cross reference has been added to allow the LIM to look-up an MLTF item by the LOINC Code.

The Walk Associate Test to MLTF Option (WAT) has been updated to allow the LIM to reset the starting point back to the beginning. In the event that new test/specimens have been added since the last time the WAT option was run the LIM can reset and start with the newly add test/specimens.

## Associating a Site/Specimen to the MLTF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three ways to associate a Site/Specimen to the MLTF.

1.  Using the MLTF NUMBER prompt (field (#30) in the site/specimen sub-multiple (#60.01) when creating a new or editing an existing Site/Specimen within FileMan.

This is the current method that LIM<span id="Associating_to_MLTF" class="anchor"></span>s use to create or modify a LABORATORY TEST file (#60) entry.

2.  Using the ATM Associate Test to NDS MLTF option on the LIM NDS MENU.
3.  Using the WAT Walk Associate Test to MLTF option on the LIM NDS MENU.

Prior to the population of the MLTF field, creation of a new test in LABORATORY TEST file (# 60) will generate a mailman message to the LIM entering the new site/specimen and members of the facilities G.LMI mail group. Because the functionality to forward that message on to the NTRT team has not yet been turned on, sites should ignore these messages.

When the MLTF has been deployed a message will be listed on the NTRT_NOTIFICATION-L listserv which the LIMs will have subscribed to, (*see* the Prerequisites in Section <u>1.4:</u> NTRT Process). Informational patch LR\*5.2\*481 provides instructions for activating the NTRT message process.

## Notes on Entering or Editing a Test/Specimen MLTF Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When entering or editing a Test/Specimens MLTF entry the system will display one of the following two prompts:

- If the Test/Specimen has not been associated to an MLTF item, or if the MLTF Item name is less than nineteen characters in length, the system will display a double-slash prompt (‘//’).
- If the Test Specimen has been previously associated to an MLTF Item and the MLTF Item name is greater than 19 characters in length, the system will display the prompt ‘Replace:’.

If the Test/Specimen has not been associated to a MLTF Item the LIM may do one of the following functions:

- Enter a ‘?’ to view all active entries in the MASTER LABORATORY TEST file (#66.3).
- Enter a partial match of the MLTF Item name that they wish to associate.

If the Test/Specimen has previously been associated to a MLTF Item, the LIM may do one of the following functions:

- Enter a ‘?’ to view all active entries in the MASTER LABORATORY TEST file (#66.3)
- Enter a partial match of the MLTF Item name that they wish to associate.
- Enter the ampersand sign ‘@’ to remove the current Test/Specimen MLTF Item association.

When viewing the MASTER LABORATORY TEST file (#66.3) Items the system will display the following fields from the MASTER LABORATORY TEST file (#66.3). These additional fields are displayed to provide the LIM assistance when determining which MLTF item to use.

- The first 60 characters of the MLTF Items Name (field .01).
- The MLTF Items LOINC CODE (field .04).
- The MLTF Items SPECIMEN (field .08).
- The MLTF Items METHOD (field 1).

![](lr-5-2-500-laboratory-nds-lim-user-manual/012.png) NOTE: If the LIM has any questions regarding the association of the Site/Specimen to the MLTF please enter a help desk ticket for the clin 2 team.

## NTRT Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The items in the list below describe the NTRT process for newly added local facility Site/Specimens that were not associated with the MLTF when a Site/Specimen is created.

![](lr-5-2-500-laboratory-nds-lim-user-manual/013.png) MANDATORY PREREQUISITE: The LIM must subscribe to the NTRT_NOTIFICATION-L listserv in order to be notified when the MLTF content updates have been deployed.  
The LIM for the facility shall subscribe to this list using the following web site: <http://vaww.listserv.va.gov/scripts/wa.exe>. STS does not own this application; this is a VA service. The LIM will need to create an account using a username and password that does NOT synchronize with the user's VA network account.

- This process will be activated after the MASTER LABORATORY TEST file (#66.3) content has been deployed, and the sending of NTRT messages is activated.
- NTRT messages will not be sent for Site/Specimens that were created prior to the MLTF content deployment and the sending of NTRT messages being activated.
- An NTRT message will be sent if a site/specimen is not associated to the MLTF during the Enter / Edit of a LABORATORY TEST file (#60) site/specimen.
- The NTRT message transmission has been configured for an 8 hour delay in order to ensure that the LIM has adequate time to complete the test/specimen entry
- A mailman message is sent to the Laboratory NTRT mail group containing the following information:

  The ‘FROM:’ on the NTRT message is the facility mailman address of the LIM who added the Test/Specimen.

<span id="_Toc514840048" class="anchor"></span>Figure . NTRT Process Message Example

Site Number - From INSTITUTION file (#4) IEN

Facility Name – From INSTITUTION file (#4) field .01

Facility Number - From INSTITUTION file (#4) IEN

Facility Lab Group Mailman address – From LAB MLTF MANAGED ITEMS file (#66.4) field

2

Test Name – From LABORATORY TEST file (#60) field .01

Test IEN – From LABORATORY TEST file (#60) Test IEN

Site/Specimen IEN – From LABORATORY TEST file (#60) Sub-File SITE/SPECIMEN

(#60.01) IEN

Site/Specimen Name - From LABORATORY TEST file (#60) Sub-File SITE/SPECIMEN

(#60.01) field .01

Spec - from TOPOGRAPHY FIELD (#61) field .01

Time Aspect - From TOPOGRAPHY FIELD (#61) field .0961

Units – From LABORATORY TEST file (#60) Sub-File SITE/SPECIMEN (#60.01) field 6.

NLT – From WKLD CODE (#64) field 1

Lab Section – From WKLD CODE LAB SECT (#64.21) field 1

Subscript - From LABORATORY TEST file (#60) field 4

Data Name - From LABORATORY TEST file (#60) field 5

Data Comment - From LABORATORY TEST file (#60) field 13, Data Definition for comment

Data Type - From LABORATORY TEST file (#60) field 13, Data Definition for data Type

Reference Low - From LABORATORY TEST file (#60) Sub-File SITE/SPECIMEN (#60.01)

field 1.

Reference High - From LABORATORY TEST file (#60) Sub-File SITE/SPECIMEN (#60.01)

field 2.

Therapeutic Low - From LABORATORY TEST file (#60) Sub-File SITE/SPECIMEN (#60.01)

field 9.2.

Therapeutic High - From LABORATORY TEST file (#60) Sub-File SITE/SPECIMEN (#60.01)

field 9.3.

Test Synonyms - From LABORATORY TEST file (#60) Sub-File SYNONYM (#60.1) FIELD

.01.

Specimen Interpretation - From LABORATORY TEST file (#60) Sub-File SITE/SPECIMEN

(#60.01) field 5.5 Sub-File INTERPRETATION (#60.07) field .01.

Test Creation Date – From LABORATORY TEST File (#60) field 133

Specimen Create Date - From LABORATORY TEST file (#60) Sub-File SITE/SPECIMEN

(#60.01) field 35.

In House Test - From LABORATORY TEST File (#60) field 134.

POC Test - From LABORATORY TEST File (#60) field 135.

Scanned Image Test - From LABORATORY TEST File (#60) field 137.

Performing Lab - From LABORATORY TEST File (#60) Sub-File PERFORMING LAB (#60.16)

Field .01.

Order Code - From LABORATORY TEST File (#60) Sub-File PERFORMING LAB (#60.16)

Field 1.

Site Notes – header line for site notes

Site Notes Date - From LABORATORY TEST File (#60) Sub-File SITE NOTES DATE

(#60.0505) Field .01.

Site Note Text - From LABORATORY TEST file (#60) Sub-File SITE

NOTES DATE (#60.0505) Sub-File TEXT (#60.5051) field 1.

- An STS analyst passes this information to the Lab SME group who will decide whether to:
1.  Add a new LAB TEST NAME entry to the MLTF to the national laboratory test standard; or
2.  Suggest a mapping to an existing LAB TEST NAME entry in the MLTF.
- Once the SMEs have made a decision, an STS analyst will reply to the email address that was included in the auto email. The email address is the facilities G.LMI mailman address. The email will describe the Lab SME decision.
- If the SME decision was to suggest a mapping to an existing test, already part of the national standard, this is the end of the process. Otherwise...
- If the SMEs authorize a new lab test, that work goes to an STS analyst to create the new lab test in the STS database. The new lab test goes through several layers of testing, gets SQA approval, and is deployed to all national production sites. This process takes between 1-2 weeks.
- When a deployment is complete, STS sends a message to the NTRT_NOTIFICATION-L listserv.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The System Configuration of the Lab package is not affected by the inclusion of the CTT & DM NDS patch updates.

## MASTER LABORATORY TEST file Creation and Update Process Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MASTER LABORATORY TEST file Creation and Update Process is the process for adding a new test to the MASTER LABORATORY TEST file. This is described in the Laboratory New Test Process flow diagram reflecting the day-to-day operations. <u>*See* Figure 2. Laboratory New Test Process Flow</u>.

<span id="_Ref505601970" class="anchor"></span>Figure . Laboratory New Test Process Flow

![](lr-5-2-500-laboratory-nds-lim-user-manual/014.png)

<span id="Master_Lab_Test_File_Create_Udate_Proces" class="anchor"></span>

### MASTER LABORATORY TEST File Creation and Update Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Initial association of tests in the Laboratory Test file (#60) to MLTF is performed by the Lab Information Manager (LIM) at each facility. Once the MLTF content has been deployed to the LIMs facility the LIM would use the option Walk Associate Test to MLTF to associate Test/Specimens in their LABORATORY TEST file (#60) to the MASTER LABORATORY TEST file (#66.3).
4.  Guidance on when to change the SEND NTRT MESSAGE flag is detailed in informational patch LR\*5.2\*481.

    Once the SEND NTRT MESSAGE is set to <u>YES</u>, the NTRT request will be sent automatically to the NTRT group, if the test/specimen is not associated to the MLTF.

    The sending of the NTRT message only occurs when Entering/Modifying the Site/Specimen within FileMan. *See* item 1 under <u>Associating a Site/Specimen to the MLTF</u>) or when adding a new atomic test to the LABORATORY TEST file (#60).

> ![](lr-5-2-500-laboratory-nds-lim-user-manual/015.png) NOTE: Prior to setting the SEND NTRT MESSAGE flag to yes the addition of a SITE/SPECIMEN to an existing test will trigger a message to the G.LMI mail group. These messages should be ignored at this point. They will only be important after the SEND NTRT MESSAGE flag has been set to yes, and the MLTF content deployed.

5.  Upon entry of a new site/specimen in the LABORATORY TEST file (#60) an NTRT request will be automatically launched if that site/specimen is not associated to the MLTF. The LIM will be able to use the site/specimen in the interim while the NTRT team evaluates whether it is a new site/specimen, or if the item can be associated with an existing MLTF entry.
6.  An NTRT Exception flag will be set when a new test/specimen has been submitted to NTRT for processing.
7.  The Creation Date of the new test shall be captured and added to the LABORATORY TEST file (#60) when a new test is added.
8.  The specimen create date shall be captured and added to the LABORATORY TEST file (#60) subfile 60.01 field 35 when a new specimen is added.
9.  As a result of the NTRT request, the new test/specimen will be evaluated by the NTRT group. If it is determined the test/specimen is new, this entry will be added to the MLTF and be deployed to all facilities based on NTRT deployment methodology.
10. If the search result identifies an equivalent test/specimen already exists within the MLTF, the creation request will be rejected, and notification is sent back to the requestor including the specific entry within the MLTF that it is to be associated to.
11. On-demand reports will be made available to VHA Lab Program Office. The VHA Lab Program Office will not require the assistance of the facility to obtain the report.
12. The local site’s Lab mail group (LMI) will be utilized for email notifications.

## Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the step-by-step procedures to navigate to the LIM NDS MENU and describes the menu options.

### Navigating to the LIM NDS MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This procedure describes how to access the LIM NDS MENU.

This document is based on the assumption that the person using this document has access to the LRLIAISON options menu.

1.  At the Select Lab Liaison Menu prompt, type: NDS LIM NDS MENU, then press <span class="mark">\<Enter\></span>. The <u>LIM NDS MENU</u> displays, *see* <u>Figure 3. LIM NDS MENU</u>.

<span id="_Ref505601014" class="anchor"></span>Figure . LIM NDS MENU

LIM NDS MENU

ATM Associate Test to NDS MLTF

WAT Walk Associate Test to MLTF

MIE Managed Items Edit

PNA Print NDS Audits in File 60

PSV Print Specimens Without VUIDS

PTI Print Specimens with Inactive VUIDS

LME Lab to MLTF Extract

PRG Purge NDS File 60 Audits

LIME EDIT Inactive DT Multiple – ETIOLOGY File

LISE EDIT Inactive DT Single – ETIOLOGY File

### LIM NDS MENU Options and the Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 2. LIM NDS MENU Options and Descriptions</u> list the LIM NDS MENU option name, synonym, and a brief description of the option functions.

![](lr-5-2-500-laboratory-nds-lim-user-manual/016.png) *TIP:* You can enter the LIM NDS MENU synonym as listed in <u>Table 2. LIM NDS MENU Options and Descriptions</u> to navigate to the menu option.

| Menu Option Name                          | Synonym | Description                                                                                                                                                                                                                   |
|-------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Associate Test to NDS MLTF                | ATM     | Enter a Specimen name that is associated to the test that you wish to associate to the MLTF.                                                                                                                                  |
| Walk Associate Test to MLTF               | WAT     | This option allows you to associate lab test/specimens to the MASTER LABORATORY TEST file.                                                                                                                                    |
| Managed Items Edit                        | MIE     | This option is used for updating the 66.4 managed items file. It contains the NTRT control items. For example, mail groups and test types. This file is initially populated at the patch load with certain defaults assigned. |
| Print NDS Audits in File 60               | PNA     | Report. The Print NDS Audits in File 60 report option prints edits to file 60 items that relate to the NDS process.                                                                                                           |
| Print Specimens Without VUIDS             | PSV     | Report that displays an extract of tests/specimens to identify those items that do not have a MLTF VUID associated.                                                                                                           |
| Print Specimens with Inactive VUIDS       | PTI     | Report that displays an extract of tests/specimens that’s associated VUID is inactive.                                                                                                                                        |
| Lab to MLTF Extract                       | LME     | Report. This option is a download extract that enables you to capture what prints on the screen. You can capture the same data as the lab server side MISSING MLTF export request.                                            |
| Purge NDS File 60 Audits                  | PRG     | NTRT PURGE FILE 60 AUDITS. The purge is the trimming mechanism to control the growth of 60 file. The minimum is 220 days (retain 220 days of tracked edits).                                                                  |
| EDIT Inactive DT Multiple – ETIOLOGY File | LIME    | This option allows you to modify the INACTIVE DATE field within file 61.2 for multiple entries in one session.                                                                                                                |
| EDIT Inactive DT Single – ETIOLOGY File   | LISE    | This option allows you to modify the INACTIVE DATE field within file 61.2 for a single entry in one session.                                                                                                                  |

LIM NTRT Menu OptionsLIM NTRT Menu Options

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the procedures for using the LIM NDS MENU options.

## Laboratory Information Manager (LIM) Native Domain Standardization (NDS) Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- ATM - Associating a Lab Test to the NDS MASTER LABORATORY TEST file (MLTF)
- WAT - Using the Walk Associate Test to MLTF
- MIE - Using the Managed Items Edit
- PNA - Using the Edit Purge FILE 60 Audits Option
- Running Reports from the LIM NDS MENU
- LIME - EDIT Inactive DT Multiple – ETIOLOGY File
- LISE - EDIT Inactive DT Single – ETIOLOGY File

### Using the Associate Test to NDS MLTF Option (ATM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Type ATM for the Associate Test to NDS MLTF (ATM)Menu Option, then press <span class="mark">\<Enter\></span>, as shown in <u>Figure 4. Associate Test to NDS MLTF Menu Option</u>.

![](lr-5-2-500-laboratory-nds-lim-user-manual/017.png) NOTE: The LIM would use this option when associating or editing an existing Test/Specimen with a MLTF item. Initial association of existing tests in the LABORATORY TEST file (#60) to the MLTF is done by the LIM using the option Walk Associate Test to the MLTF.

<span id="_Ref505601786" class="anchor"></span>Figure . Associate Test to NDS MLTF Menu Option

LIM NDS MENU

<span class="mark">ATM Associate Test to NDS MLTF</span> <span class="mark"><u>\<Enter\></u></span>

WAT Walk Associate Test to MLTF

MIE Managed Items Edit

PNA Print NDS Audits in File 60

PSV Print Specimens Without VUIDS

LME Lab to MLTF Extract

PTI Print Specimens with Inactive VUIDS

PRG Purge NDS File 60 Audits

LIME EDIT Inactive DT Multiple – ETIOLOGY File

LISE EDIT Inactive DT Single – ETIOLOGY File

13. At the Select LABORATORY TEST NAME prompt: type the Laboratory Test Name, then press <span class="mark">\<Enter\></span>, as shown in <u>Figure 5. ATM Associate Test to NDS MLTF</u>.

<span id="_Ref505601676" class="anchor"></span>Figure . ATM Associate Test to NDS MLTF

Select LIM NDS MENU \<TEST ACCOUNT\> Option: ATM Associate Test to NDS MLTF

<span class="mark">Select LABORATORY TEST NAME</span>: <span class="mark">GLU</span> <span class="mark"><u>\<Enter\></u></span>

1 GLU,BUN,CREAT,LYTES

2 GLU,CHOL,TRIG

3 GLUCAGON (q,F)

4 GLUCOSE

5 GLUCOSE DTG TEST

Press \<RETURN\> to see more, '^' to exit this list, OR

<span class="mark">CHOOSE 1-5</span>:<span class="mark">1</span> <span class="mark"><u>\<Enter\></u></span>

14. Choose <span class="mark"><u>1-5</u></span> to select the Laboratory Test Name, and then press <span class="mark">\<Enter\></span>.
- If the Test Type is ‘N’ then a message displays and you are returned to the ‘LABORATORY TEST’ prompt.
- If the Test Subscript is ‘WK’, ‘BB’, ‘AU’, or ‘EM’ then a message displays and you are returned to the ‘LABORATORY TEST’ prompt.
- If the Tests LOCATION, (Data Name) is not populated a message displays and return to the ‘LABORATORY TEST’ prompt.
15. At the Select SITE/SPECIMEN prompt: Enter a specimen name to associate to the MLTF.
16. At the MLTF NUMBER prompt: Enter the MLTF test name you wish to associate the test/specimen.

![](lr-5-2-500-laboratory-nds-lim-user-manual/018.png) NOTE: If the Test/Specimen has been previously associated to a MLTF entry the ‘Select MASTER LABORATORY TEST:’ the entry may have “Replace” instead of “//”. See Section 1.3 Note on entering or editing a Test/Specimens MLTF entry for guidance.

17. If the prompt has ‘Replace’: To select a different MLTF item: Enter the first letter of the displayed MLTF name followed by 3 dots (…) at the “With” prompt enter a partial match to the new MLTF name to see the list of names OR enter a ‘?’ to be prompted for the entire MLTF list. To leave as is: press <span class="mark">\<Enter\></span>.
18. To delete the linkage, enter the <span class="mark">@</span> ("at" sign).
19. If a ‘?’ is entered to view the MLTFs on file, the listing displays: MLTF Test Name, MLTF Specimen value, MLTF Method. This is to assist you with selecting the MLTF that bests suits the local Test/Specimen.

When a MLTF has been selected, the MLTFs LOINC Code Specimen will be compared to the local Test/Specimen’s value. If they are not the same, a message displays to that effect: “The MLTF LOINC code that you have selected does not have the same specimen that you chose to test/specimen.” You are prompted: “Are you sure you want to do this?”

If you answer YES, the association is made. If you answer NO, the association is not be made, and you are returned to the MLTF NUMBER prompt.

<span id="_Ref505601047" class="anchor"></span>Figure . Example Associate Test to NDS MLTF Option (ATM)

Select LIM NDS MENU \<TEST ACCOUNT\> Option: ATM Associate Test to NDS MLTF

LABORATORY TEST: GLUCOSE

1 GLUCOSE

2 GLUCOSE TOLERANCE (BLOOD)

3 GLUCOSE, CSF

4 GLUCOSE,BUN,CREAT,LYTES GLU,BUN,CREAT,LYTES

CHOOSE 1-4: 1 GLUCOSE

SPECIMEN for GLUCOSE: SERUM

Select MASTER LABORATORY TEST: GLUCOSE STRIP MASS CONC URINE

Replace ... With GLUCOSE Replace

GLUCOSE

1 GLUCOSE 2345-7 Ser/Plas

2 GLUCOSE STRIP MASS CONC URINE 5792-7 Urine Test strip

3 GLUCOSE STRIP QL UR  GLUCOSE STRIP QL URINE 25428-4 Urine T

est strip

4 GLUCOSE, BODY FLUID 14747-0 Plr fld

CHOOSE 1-4: 1 GLUCOSE 2345-7 Ser/Plas

Test/Specimen: GLUCOSE / SERUM

Saved With MLTF: GLUCOSE

SPECIMEN for GLUCOSE:

LABORATORY TEST:

<span id="_Using_the_Walk" class="anchor"></span>

### Using the Walk Associate Test to MLTF Option (WAT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Type <span class="mark">WAT</span> for the Walk Associate Test to MLTF (WAT)Menu Option, then press <span class="mark">\<Enter\></span>, as shown in Figure 7. WAT – Walk Associate Test to MLTF Menu Option.

![](lr-5-2-500-laboratory-nds-lim-user-manual/019.png) NOTE: The LIM would use this option once the MASTER LABORATORY TEST file (66.3) content has been deployed to their facility.

This option is used for the initial association of existing Site/Specimens in the LABORATORY TEST file (#60) to the MLTF.

<span id="_Ref459138014" class="anchor"></span>Figure . WAT – Walk Associate Test to MLTF Menu Option

ATM Associate Test to NDS MLTF

<span class="mark">WAT Walk Associate Test to MLTF</span> <span class="mark"><u>\<Enter\></u></span>

MIE Managed Items Edit

PNA Print NDS Audits in File 60

PSV Print Specimens Without VUIDS

PTI Print Specimens with Inactive VUIDS

LME Lab to MLTF Extract

PRG Purge NDS File 60 Audits

LIME EDIT Inactive DT Multiple – ETIOLOGY File

LISE EDIT Inactive DT Single – ETIOLOGY File

The WAT option allows the LIM to associate lab test/specimens to the MLTF, as shown in <u>Error! Reference source not found.</u> This option goes through the LABORATORY TEST file (#60) one time, starting with the newest LABORATORY TEST file (#60) entry. Once it reaches the oldest test it will be flagged as done.

This option is re-startable. The process will pick up where the LIM left off or the starting test may be reset again to the newest LABORATORY TEST file (#60) entry. The LIM has the ability to skip a test.

The routine picks up the next oldest test or if Reset then the newest test, displays the test name, and then displays the specimens for that test.

- If the test subscript is *WK*, then it skips it.
- If the test subscript is *BB*, then it skips it.
- If the test subscript is *AU*, then it skips it.
- If the test subscript is *EM*, then it skips it.
- If the test type is *N*, then it skips it.
- If the test does not have a *Data Name*, then it skips it.
- If the test does not have any specimens a message with the test name is displayed. The option then goes to the next test.
20. At the MASTER LABORATORY TEST FILE prompt: Enter the MLTF test name you wish to associate the test/specimen.

If a ‘?’ is entered to view the MLTFs on file the listing display will be:

MLTF Test Name, MLTF Specimen value, MLTF Method

This is to assist the LIM in selecting the MLTF that bests suits the local Test/Specimen.

When a MLTF has been selected the MLTFs LOINC Code Specimen will be compared to the local Test/Specimen’s Specimen value. If they are not the same, a message will display to that effect. The MLTF LOINC code that you have selected does not have the same specimen that you chose to test/specimen. You will be prompted “Are you sure you want to do this?” If the LIM answers YES, the association will be made. If the LIM answers NO, the association will not be made and the system returns to the MASTER LABORATORY TEST FILE prompt. *See*<u>Error! Reference source not found.</u>

<span id="_Toc504489627" class="anchor"></span>Figure . Example Walk Associate Test to MLTF Continue or Reset

Select LIM NTRT MENU \<TEST ACCOUNT\> Option: wa LIM NTRT WALK ASSOCIATE TEST TO MLTF

CONTINUE WITH CLT AUG 8A \[5320\] (C)

START OVER (S)

When the “WAT Walk Associate Test to MLTF” menu option is selected the user is presented with a second option. The user may continue with the previous walk starting from where it was last ended (“C”) or the user may select to reset the walk back to the newest test (“S”).

In the example shown above the user may continue with the last test named “CLT AUG 8A” with IEN of 5320 or the user may select to start over.

The Walk Associate then proceeds from there:

<span id="_Toc504489628" class="anchor"></span>Figure . <span id="Example_WAT_to_MLTF" class="anchor"></span>Example Walk Associate Test to MLTF Test

Select LIM NDS MENU \<TEST ACCOUNT\> Option: WALK Associate Test to MLTF

TEST: PHOSPHORUS

SPECIMEN(s)

Select one of the following:

1 PLASMA \[73\]

Enter The Number For The Specimen to Associate With The MLTF: 1 PLASMA \[73\]

Select MASTER LABORATORY TEST: PH

1 PH STRIP UR PH STRIP URINE 5803-2 Urine Test strip

2 PHOSPHATE MASS CONC SERUM/PLASMA 2777-1 Ser/Plas

CHOOSE 1-2: 2 PHOSPHATE MASS CONC SERUM/PLASMA 2777-1 Ser/Plas

PLASMA: Saved With MLTF

TEST: DRVVT SCREEN (q)

SPECIMEN(s)

Select one of the following:

1 PLASMA \[73\]

Enter The Number For The Specimen to Associate With The MLTF: \<\< press Enter \>\>

Do You Wish to go to The Next Test?? YES//

TEST: HEXAGONAL PHASE NEUTRAL (q)

SPECIMEN(s)

Select one of the following:

1 PLASMA \[73\]

Enter The Number For The Specimen to Associate With The MLTF:

### Using the Managed Items Edit Option (MIE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Managed Items Edit Option(MIE) is used for updating the 66.4 Managed Items file. It contains the NTRT Control items; for example, mail groups and test types. This file is initially populated at the patch load with certain default values assigned, as shown in <u>Figure 10. MIE - Managed Items Edit Default Values</u>.

<span id="_Ref505601068" class="anchor"></span>Figure . MIE - Managed Items Edit Default Values

The LAB MANAGED ITEMS file (#66.4) is seeded at the end of the patch load LR\*5.2\*468. Patch LR\*5.2\*500 changed the name of the ISAAC fields to CTT TOOLING and updated their contents.

The default values are:

INSTITUTION POINTER: <span class="mark"><u>(local Facility Institution name of the facility loading the patch)</u></span>

NTRT SEND METHOD: <span class="mark">MAILMAN</span>

AUTO REMINDERS PARAMETER: <span class="mark">30</span>

AUDIT PURGE DAYS: <span class="mark">220</span>

CTT TOOLING ACTIVE: <span class="mark">NO</span>

LAB IEN: <span class="mark"><u>This is populated at load time with the highest file 60 IEN</u></span>

SUBSCRIPT FOR NTRT: CH

LAST AUTO TEST ID: <span class="mark"><u>will be populated when client runs Walk Associate Test to MLTF</u></span>

SEND NTRT MESSAGES: <span class="mark">NO</span> This would be changed in guidance of patch LR\*5.2\*481.

DEFAULT NTRT MAIL GROUP: G.LABORATORY [<span class="mark">NTRT@FORUM.VA.GOV</span>](mailto:NTRT@FORUM.VA.GOV)

DEFAULT SITE LAB MAIL GROUP: G.LMI@ <span class="mark"><u>DOMAIN EXAMPLE: G.LMI@BEDFORD.MED.VA.GOV</u></span>

CTT TOOLING WEB ADDRESS: <span class="mark">vaausctt203.aac.va.gov</span>

CTT TOOLING PORT NUMBER: <span class="mark">8088</span>

CTT TOOLING NTRT PATH: <span class="mark">ntrt~projects~NTRT~queues~custom~1</span>

CTT TOOLING SCHEMA NAME: <span class="mark">JIRAORAUSER</span>

CTT TOOLING SCHEMA PATH: <span class="mark"><u>no entry</u></span>

1.  Select the Managed Items Edit (MIE) Menu option, and then press <span class="mark">\<Enter\></span>, as shown in Figure 11. MIE - Managed Items Edit Menu Option.

<span id="_Ref452574287" class="anchor"></span>Figure . MIE - Managed Items Edit Menu Option

LIM NDS MENU

ATM Associate Test to NDS MLTF

WAT Walk Associate Test to MLTF

<span class="mark">MIE Managed Items Edit <u>\<Enter\></u></span>

PNA Print NDS Audits in File 60

PSV Print Specimens Without VUIDS

PTI Print Specimens with Inactive VUIDS

LME Lab to MLTF Extract

PRG Purge NDS File 60 Audits

LIME EDIT Inactive DT Multiple – ETIOLOGY File

LISE EDIT Inactive DT Single – ETIOLOGY File

21. At the Select LAB MLTF MANAGED ITEMS INSTITUTION POINTER prompt, enter the site and then press <span class="mark">\<Enter\></span>, as shown in
22. Figure 12. Example of Managed Items Edit Process.
23. At the NTRT SEND METHOD prompt press <span class="mark">\<Enter\></span> to select the default option: MAILMAN.
24. At the AUTO REMINDERS PARAMETER prompt press <span class="mark">\<Enter\></span> to select the default number 30.
25. At the AUDIT PURGE DAYS prompt, press <span class="mark">\<Enter\></span> to select the default number: 225.
26. At the CTT TOOLING Active prompt, press <span class="mark">\<Enter\></span> to select the default option: No
27. At the SUBSCRIPT FOR NTRT: CH prompt, select the number 1-8, then press <span class="mark">\<Enter\>.</span>

![](lr-5-2-500-laboratory-nds-lim-user-manual/020.png) NOTE/CAUTION: The Subscript for NTRT should only be changed with written guidance from the VHA Laboratory Program Office.

28. Select <span class="mark">\<Enter\></span> to select the defaults for the CTT TOOLING WEB ADDRESS, CTT TOOLING Port Number, CTT TOOLING NTRT PATH, CTT TOOLING SCHEMA NAME, and CTT TOOLING SCHEMA PATH. <span id="_Ref452574668" class="anchor"></span>

Figure . Example of Managed Items Edit Process

<span class="mark">Select LAB MLTF MANAGED ITEMS INSTITUTION POINTER</span>: <span class="mark"><u>?</u></span>

Answer with LAB MLTF MANAGED ITEMS INSTITUTION POINTER:

<span class="mark"><u>BEDFORD VAMC</u></span>

<span class="mark">Select LAB MLTF MANAGED ITEMS INSTITUTION POINTER</span>: <span class="mark"><u>Bedford VAMC MA VAMC 518</u></span>

INSTITUTION POINTER: BEDFORD VAMC// This is the Institution for the clients Facility.

<span class="mark">NTRT SEND METHOD</span>: <span class="mark"><u>MAILMAN// This is the method that messages are sent for NTRT validation.</u></span>

<span class="mark">Enter Method That New Tests are Sent to NTRT for Validation. Currently only MAILMAN is supported.</span>

<span class="mark">Choose from:</span>

<span class="mark">M MAILMAN</span><span class="mark">X XML</span><span class="mark">N NONE DO NOT SEND</span>

<span class="mark">NTRT SEND METHOD: MAILMAN//</span>

<span class="mark">AUTO REMINDERS PARAMETER: 30//</span>

<span class="mark">AUDIT PURGE DAYS: 220//</span> ?

<span class="mark">CTT TOOLING ACTIVE: NO//</span> ?

<span class="mark">SUBSCRIPT FOR NTRT: CH //</span> ? You can choose which test subscripts to allow for sending to NTRT.

> **NOTE:** The Subscript For NTRT should only be changed with written guidance from the VHA LAB PROGRAM OFFICE.

<span class="mark">Enter the number that corresponds to the subscript to be sent to NTRT</span>

Choose from:

<span class="mark">1 CH</span><span class="mark">2 MI</span><span class="mark">4 SP</span><span class="mark">5 CY</span><span class="mark">7 CH AND MI</span><span class="mark">8 ALL SUBSCRIPTS</span>

SUBSCRIPT FOR NTRT: CH//

<span class="mark">LAST AUTO TEST ID: 5624//</span> ? This is the last LABORATORY TEST file (#60) IEN that the client has checked for MLTF

<span class="mark">LAST AUTO TEST ID: 5624//</span>

<span class="mark">SEND NTRT MESSAGES: NO//</span> Allows the Facility to control if new laboratory tests requests are sent to NTRT

<span class="mark">DEFAULT NTRT MAIL GROUP:</span> G.LABORATORY <NTRT@FORUM.VA.GOV> The NTRT forum group that NTRT requests are sent to

<span class="mark">DEFAULT SITE LAB MAIL GROUP:</span> <G.LMI@BEDFORD.MED.VA.GOV> The facility lab mail group that NTRT will respond to.

<span class="mark">CTT TOOLING WEB ADDRESS:</span> vaausctt203.aac.va.gov Enter the CTT TOOLING Web Address in form 'WWW.CTT-TOOLING.COM'. The Address may be up to 100 characters in length.

<span class="mark">CTT TOOLING PORT NUMBER:</span> 8088 Enter the port number for the CTT TOOLING system NTRT process.

<span class="mark">CTT TOOLING NTRT PATH:</span> ntrt~projects~NTRT~queues~custom~1 Enter the CTT TOOLING system path for the NTRT process.

<span class="mark">CTT TOOLING SCHEMA NAME:</span> JIRAORAUSER Enter the CTT TOOLING schema name for processing the CTT TOOLING XML's.

<span class="mark">CTT TOOLING SCHEMA PATH</span>:

Enter the path for the CTT TOOLING SCHEMA NAME

### Running the LIM NDS Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the following procedures in this section to access and run the LIM NDS Reports<u>, *see* Figure 13. LIM NDS Reports</u>.

The following reports are available on the LIM NDS MENU:

- PNA Print NDS Audits in File 60
- PSV Print Specimens Without VUIDS
- PTI Print Specimens with Inactive VUIDS
- LME Lab to MLTF Extract

<span id="_Ref496092031" class="anchor"></span>Figure . LIM NDS Reports

LIM NDS MENU

ATM Associate Test to NDS MLTF

WAT Walk Associate Test to MLTF

MIE Managed Items Edit

<span class="mark"><u>PNA Print NDS Audits in File 60</u></span><span class="mark"><u>PSV Print Specimens Without VUIDS</u></span><span class="mark">PTI Print Specimens with Inactive VUIDS</span><span class="mark"><u>LME Lab to MLTF Extract</u></span>

PRG LIM NTRT PURGE FILE 60 Audits

LIME EDIT Inactive DT Multiple – ETIOLOGY File

LISE EDIT Inactive DT Single – ETIOLOGY File

Perform the following procedure to access the LIM NTRT Reports.

1.  Navigate to the <span class="mark"><u>LIM NDS MENU</u></span>.
29. Type <u><span class="mark">PNA</span></u> Print NDS Audits in File 60, then press \<<span class="mark">Enter</span>\> to view edits to File 60 items that relate to the NTRT process.
30. Type <span class="mark"><u>PSV</u></span> Print Specimens Without VUIDS, then press \<<span class="mark">Enter</span>\> to view Specimens without VUIDs.
31. Type <span class="mark"><u>PTI</u></span> Print Specimens with Inactive VUIDS, then press \<<span class="mark">Enter</span>\> to view Specimens that have VUIDS that are inactive.
32. Type <u><span class="mark">LME</span></u> Lab to MLTF Extract, then press \<<span class="mark">Enter</span>\> to capture what is on the screen.

### Running the Lab to MLTF Extract Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab to MLTF Extract Report is a download extract, which means that you can capture what is on the screen. This report allows you to capture the same data as the Lab server side *MISSING MLTF Export Request*, as shown in <u>Figure 14. Example Lab to MLTF Extract Report.</u>

Perform the following procedure to run the Lab to MLTF Extract Report.

1.  Navigate to the <u>LIM NDS MENU.</u>
33. Type <u><span class="mark">LME</span></u> to select the Lab to MLTF Extract Report, and then press \<<span class="mark">Enter</span>\>.
34. Type <span class="mark"><u>Yes</u></span> to capture the screen, and then press \<<span class="mark">Enter</span>\>.

<span id="_Ref505601834" class="anchor"></span>Figure . Example Lab to MLTF Extract Report

<span class="mark">Ready to Capture?</span> <u><span class="mark">Yes//</span> <span class="mark">\<Enter\></span></u>

A partial capture of the header section

...EXCUSE ME, HOLD ON...

Report Generated.......: Apr 11, 2016@12:03:38 at BEDFORD VAMC

Report requested.......: MISSING MLTF

LOINC version..........: 2.14

VistA File version.....:

Extract version........: 1.1

Total number of records: 1596

Total number of tests..: 1534

Tests with MLTF'S.......: 0

Tests with NLT code....: 1321

Antimicrobials.........: 62

Legend:

Station \#-60 ien-Spec ien-Index\|Test Name\|Spec\|Time Aspect\|Units\|MLTF\|NLT \#\|Batt

ery Code\|Battery Description\|Lab Section\|Subscript\|Comment\|Data Type\|Reference l

ow\|Reference high\|Therapeutic low\|Therapeutic high\|

Use Ref Lab\|Site Comment\|Test Synonyms\|Test Type\|MLTF Name\|MLTF Alt Name\|Submitt

ed to NTRT\|Specimen Create Date\| MISSING SPECIMENS\|Extract Ver\|

### Running the Print NDS Audits in File 60 Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print NDS Audits in File 60 Report option prints edits to File 60 items that relate to the NTRT process, as shown in <u>Figure 15. Example Print NDS Audits in File 60 Report.</u>

The following items are being tracked in the <u>Print NDS Audits in File 60 Report</u>:

- 'M' FOR MLTF VUID
- 'C' FOR TEST CREATION DATE
- 'T' FOR TEST INACTIVE DATE
- 'R' FOR SPECIMEN INACTIVE DATE
- 'E' FOR NTRT EXCEPTION FLAG
- 'Y' FOR TEST TYPE
- 'S' FOR SPECIMEN CREATION DATE
1.  Navigate to the <u>LIM NDS MENU</u>.
35. Type <span class="mark">PNA</span> to select the Print NDS Audits in File 60 Report.
36. At the Enter From Date prompt: Type the <span class="mark">From Date</span>, then press \<<span class="mark">Enter</span>\>, as shown in Figure 15. Example Print NDS Audits in File 60 Report.
37. At the <u>Enter To Date</u> prompt: Type the <span class="mark"><u>To Date</u></span>, then press \<<span class="mark">Enter</span>\>.
38. At the <u>Output device</u> prompt: Type the <span class="mark"><u>Output Device</u></span>, then press \<<span class="mark">Enter</span>\>.

<span id="_Ref449307580" class="anchor"></span>Figure . Example Print NDS Audits in File 60 Report

Print NDS Audits in File 60 items Report

<span class="mark"><u>Enter From Date</u>:</span> <u><span class="mark">(1/1/2016 - 4/11/2016): 3/1/2016 (MAR 01, 2016)</span> <span class="mark">\<Enter\></span></u>

<span class="mark"><u>Enter To Date</u>:</span> <u><span class="mark">(3/1/2016 - 4/11/2016): T (APR 11, 2016)</span> <span class="mark">\<Enter\></span></u>

<span class="mark"><u>Output device</u>:</span> <u><span class="mark">HOME// 0 TELNET</span> <span class="mark">\<Enter\></span></u>

Lab NTRT File 60 Audited items Report Page 1

Date Printed: Apr 11, 2016

Date Edit Field User Old Value New Value

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TEST: GLUCOSE DTG TEST

2016/4/9@14:11 CREATION DATE JOHNSON,DON 09 Apr 2016

2016/4/9@14:16 TEST TYPE JOHNSON,DON B

TEST: IGG

Specimen: SERUM

2016/3/2@17:25 SPEC INACT DT JOHNSON,DON 26 Feb 2016 27 Feb 2016

Specimen: SERUM

2016/3/4@05:42 SPEC INACT DT POSTMASTER 27 Feb 2016

TEST: MEM

2016/3/15@15:51 TEST TYPE JOHNSON,DON B B

TEST: TEST DON

2016/4/9@10:46 TEST TYPE JOHNSON,DON N B

2016/4/9@10:46 CREATION DATE JOHNSON,DON

TEST: TEST DTG IGG

2016/4/9@13:46 CREATION DATE JOHNSON,DON 09 Apr 2016

2016/4/9@13:55 TEST TYPE JOHNSON,DON B

Enter <span class="mark"><u>RETURN</u></span> to continue or '<span class="mark"><u>^</u></span>' to exit:

### Running the Print Specimens Without VUIDS Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM NTRT Specimen without VUID Report option allows you to view NTRT Specimens without VUIDs, as shown in <u>Figure 16. Example Print Specimens Without VUIDS.</u>

1.  Navigate to the <u>LIM NDS MENU</u>.
39. Type <span class="mark"><u>PSV</u></span> to select the <u>Print Specimens Without VUIDS Report</u>, then press \<<span class="mark">Enter</span>\>.
40. Enter the <span class="mark"><u>Outputdevice</u></span>, and then press \<<span class="mark">Enter</span>\>, as shown in Figure 16. Example Print Specimens Without VUIDS.

<span id="_Ref505601127" class="anchor"></span>Figure . Example Print Specimens Without VUIDS

Print Specimens Without VUIDS Report

<span class="mark"><u>Output device: HOME</u>//</span> 0 <u><span class="mark">TELNET</span> <span class="mark">\<Enter\></span></u>

Lab NDS File 60 Tests/Specimens Without MLTF Vuids Report

Date Printed: Mar 04, 2016 Page 82

Specimen Create DT Inactive Exception  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Hb Create Date: Inactive: N  
ARTERIAL BLOOD N N  
Heptacarboxyporphyrins Create Date: Inactive: N  
PLASMA N N  
Hexacarboxyporphyrins Create Date: Inactive: N  
PLASMA N N  
IBUPROFEN (q) Create Date: Inactive: N  
SERUM N N  
IEP-THRU 10/99 Create Date: Inactive: N  
SERUM N N  
IGA Create Date: Inactive: N  
SERUM N N  
IGA(thru 7/12/02) Create Date: Inactive: N  
SERUM N N  
IGG Create Date: 01 Feb 2016 Inactive: N  
SERUM 2016/2/2 Y Y  
Enter RETURN to continue or '^' to exit:

### Using the Purge NDS File 60 Audits Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purge NDS File 60 Auditsoption is the trimming mechanism to control the growth of that file section. The minimum is 220 days, (retain 220 days of tracked edits). This process when invoked starts a background Taskman process. *See* <u>Figure 17. LIM NDS Purge File 60 Audits Option.</u>

1.  Navigate to the LIM NDS MENU.
41. Type <span class="mark">PRG</span> to initiate the purge option, and then press \<<span class="mark">Enter</span>\>.

<span id="_Ref505601911" class="anchor"></span>Figure . LIM NDS Purge File 60 Audits Option

LIM NDS MENU

ATM Associate Test to NDS MLTF

WAT Walk Associate Test to MLTF

MIE Managed Items Edit

PNA Print NDS Audits in File 60

PSV Print Specimens Without VUIDS

PTI Print Specimens with Inactive VUIDS

LME Lab to MLTF Extract

<span class="mark">PRG LIM NTRT PURGE FILE 60 Audits</span> \<<span class="mark">Enter</span>\>

LIME EDIT Inactive DT Multiple – ETIOLOGY File

LISE EDIT Inactive DT Single – ETIOLOGY File

42. The option is initiated, and the following message: Request Queued, \# displays, as shown in <u>Figure 18. Example Purge NDS File 60 Audits Option</u>.

<span id="_Ref505673374" class="anchor"></span>Figure . Example Purge NDS File 60 Audits Option

Purge NDS File 60 Audits

<span class="mark">Request Queued</span>, \#258477

### Running the Print Specimens with Inactive VUIDS Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Specimens with Inactive VUIDS report option prints Test/Specimens that have been associated to the MLTF but whose MLTF VUID is now inactive.

1.  Navigate to the <u>LIM NDS MENU</u>.
43. Type PTI to select the Print Specimens with Inactive VUIDS Report, and then press \<<span class="mark">Enter</span>\>, as shown in <u>Figure 19. PTI - Print Specimens with Inactive VUIDS Option</u>.

<span id="_Ref459026112" class="anchor"></span>Figure . PTI - Print Specimens with Inactive VUIDS Option

LIM NDS MENU

ATM Associate Test to NDS MLTF

WAT Walk Associate Test to MLTF

MIE Managed Items Edit

PNA Print NDS Audits in File 60

PSV Print Specimens Without VUIDS

<span class="mark">PTI Print Specimens with Inactive VUIDS</span>\<<span class="mark">Enter</span>\>

LME Lab to MLTF Extract

PRG LIM NTRT PURGE FILE 60 Audits

LIME EDIT Inactive DT Multiple – ETIOLOGY File

LISE EDIT Inactive DT Single – ETIOLOGY File

44. Enter the Output device, and then press \<<span class="mark">Enter</span>\>, as shown in Figure 20. Example Print Specimens with Inactive VUIDS.

<span id="_Ref459138559" class="anchor"></span>Figure . Example Print Specimens with Inactive VUIDS

Print Specimens Without VUIDS Report

<span class="mark"><u>Output device: HOME</u>//</span> 0 <u><span class="mark">TELNET</span> <span class="mark">\<Enter\></span></u>

Lab NDS File 60 Tests/Specimens With Inactive MLTF Vuids Report

Date Printed: Jun 09, 2016 Page 1

Specimen MLTF  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

IGG \[5581\]  
BLOOD \[70\] SODIUM \[3\]

--- Report Finished ---

### Using the Edit Inactive Date Multiple Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <u>EDIT Inactive DT Multiple</u> – <u>ETIOLOGY File</u> allows the LIM to enter Inactive Dates for entries in the ETIOLOGY FIELD File (#61.2) without having to select each entry individually. The LIM can use the Identifier Name to narrow the selection entries. This option starts with the oldest entry for the Identifier Name selected and displays those entries that do not have an Inactive Date. The LIM may enter a date, and then press \<Enter\> to go the next entry, or type ‘^’ to exit. The option will retain the last entry reviewed. If the Identifier Name selected had previously been worked with the LIM will have the option to start with the next entry that follows where the last effort left off or to start over from the beginning for that Identifier Name.

This option only allows the entry of an Inactive Date. This option does not allow for the editing of previously entered Inactive Dates.

1.  Type <span class="mark"><u>LIME</u></span> for the <u>EDIT Inactive DT Single – ETIOLOGY File</u> Menu Option, then press \<<span class="mark">Enter</span>\>, as shown in Figure 21. LIME Edit Inactive DT Multiple – Etiology File Menu Option.
45. Select the Identifier Name to limit the types of entries presented. The LIM may select an Identifier Name to narrow the population of entries to review or ‘ALL’ to review all entries in the ETIOLOGY FIELD File (#61.2).

![](lr-5-2-500-laboratory-nds-lim-user-manual/021.png) NOTE: If there has been prior review for the Identifier Name selected the LIM may choose to continue with the next entry for that Identifier Name, or start over from the beginning for entries associated to the Identifier Name selected. If the LIM chooses to start over, the option will start from the beginning looking for entries associated to that Identifier Name that do not have an Inactive Date.

<span id="_Ref496014442" class="anchor"></span>Figure . LIME Edit Inactive DT Multiple – Etiology File Menu Option

LIM NDS MENU

ATM Associate Test to NDS MLTF

WAT Walk Associate Test to MLTF

MIE Managed Items Edit

PNA Print NDS Audits in File 60

PSV Print Specimens Without VUIDS

PTI Print Specimens with Inactive VUIDS

LME Lab to MLTF Extract

PRG LIM NTRT PURGE FILE 60 Audits

<span class="mark">LIME EDIT Inactive DT Multiple – ETIOLOGY File</span>

LISE EDIT Inactive DT Single – ETIOLOGY File

<span id="_Toc514840069" class="anchor"></span>Figure . LIME Edit Inactive DT Multiple – ETIOLOGY File

Select LIM NDS MENU \<TEST ACCOUNT\> Option: <span class="mark"><u>LIME Edit Inactive DT Multiple</u></span> - ETIOLOGY File

BACTERIUM           (B)

FUNGUS              (F)

PARASITE            (P)

MYCOBACTERIUM       (M)

VIRUS               (V)

CHEMICAL            (C)

DRUG                (D)

RICKETTSIAE         (R)

PHYSICAL AGENT      (A)

NULL                (N)

ALL                 (X)

Enter the Identifier Name or Code : <span class="mark"><u>BACTERIUM</u></span>

CONTINUE WITH KLEBSIELLA OXYTOCA, CARBAPENEM RESISTANT (CRE (C)

START OVER (S)

Enter response: <span class="mark"><u>CONTINUE</u></span> WITH KLEBSIELLA OXYTOCA, CARBAPENEM RESISTANT (CRE

Organism: KLEBSIELLA OXYTOCA, CARBAPENEM RESISTANT (CRE (7159231)

INACTIVE DATE: <span class="mark"><u>T</u></span>  (SEP 26, 2017)

Organism: KLEBSIELLA PNEUMONIAE, CARBAPENEM RESISTANT ( (7159230)

INACTIVE DATE:

Organism: HAEMOPHILUS APHROPHILUS/PARAPHROPHILUS (7159229)

INACTIVE DATE: <span class="mark"><u>^</u></span>

An '^' was detected. Quiting

### Using the “Inactive Date Single Edit” Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <u>Edit Inactive DT Single - ETIOLOGY File (LISE)</u> Option allows the LIM to Add, Edit, or remove the INACTIVE DATE for entries in the ETIOLOGY FIELD File (#61.2).

1.  Navigate to the LIM NDS MENU.
46. Type <span class="mark">LISE</span> to initiate the Edit Inactive DT Single – Etiology File, and then press \<<span class="mark">Enter</span>\>, as shown in Figure 23. LISE Edit Inactive DT Single – Etiology File Menu Option.

<span id="_Ref496014517" class="anchor"></span>Figure . LISE Edit Inactive DT Single – Etiology File Menu Option

LIM NDS MENU

ATM Associate Test to NDS MLTF

WAT Walk Associate Test to MLTF

MIE Managed Items Edit

PNA Print NDS Audits in File 60

PSV Print Specimens Without VUIDS

PTI Print Specimens with Inactive VUIDS

LME Lab to MLTF Extract

PRG LIM NTRT PURGE FILE 60 Audits

LIME EDIT Inactive DT Multiple – ETIOLOGY File

<span class="mark">LISE EDIT Inactive DT Single – ETIOLOGY File</span>

47. At the ‘<u>Select ETIOLOGY FIELD NAME</u>:’ Type the name of Etiology Field Entry for Inactive date you want to modify.
48. You may enter a new date, edit the date or enter ‘@’ to delete the date.
49. Enter “<u>Y</u>” to confirm the deletion of the date.

<span id="_Toc514840071" class="anchor"></span>Figure . LISE Edit Inactive DT Single – ETIOLOGY File

<span class="mark">Select ETIOLOGY FIELD NAME</span>: <span class="mark"><u>SABADILLA</u></span>

Organism: SABADILLA

Snomed Code: 6905 Gram Stain:

Identifier: CHEMICAL <span class="mark">Inactive Date</span>: <span class="mark"><u>INACTIVE DATE: T (OCT 10, 2017)</u></span>

Select ETIOLOGY FIELD NAME: SABADILLA

Organism: SABADILLA

Snomed Code: 6905 Gram Stain:

Identifier: CHEMICAL Inactive Date: OCT 10, 2017

INACTIVE DATE: OCT 10,2017// T-10 (SEP 30, 2017)

Select ETIOLOGY FIELD NAME: SABADILLA

Organism: SABADILLA

Snomed Code: 6905 Gram Stain:

Identifier: CHEMICAL Inactive Date: SEP 30, 2017

<span class="mark">INACTIVE DATE: SEP 30,2017//</span> <span class="mark"><u>@</u></span>

SURE YOU WANT TO DELETE? Y (Yes)

Select ETIOLOGY FIELD NAME:

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

### Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

<span id="_Toc446123570" class="anchor"></span>Glossary

<table>
<caption>Glossary</caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.001 FIELD</td>
<td>A field containing the internal entry number of the record.</td>
</tr>
<tr class="even">
<td>.01 FIELD</td>
<td>The one field that <em>must</em> be present for every file and file entry. It is also called the NAME field. At a file’s creation the .01 field is given the label NAME. This label can be changed.</td>
</tr>
<tr class="odd">
<td>ABBREVIATED RESPONSE</td>
<td>This feature allows you to enter data by typing only the first few characters for the desired response. This feature will <em>not</em> work unless the information is already stored in the computer.</td>
</tr>
<tr class="even">
<td>ACCESS CODES</td>
<td>In VA FileMan, a string of codes that determines your security access to files, fields, and templates. In Kernel, you enter an Access Code to identify yourself during sign on.</td>
</tr>
<tr class="odd">
<td>ALERTS</td>
<td>Brief online notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide interactive notification of pending computing activities, such as the need to reorder supplies or review a patient’s clinical test results. Along with the alert message is an indication that the View Alerts common option should be chosen to take further action.</td>
</tr>
<tr class="even">
<td>ALTERNATE EDITOR</td>
<td>One of the text editors available for use from VA FileMan. Editors available vary from site to site. They are entries in the ALTERNATE EDITOR file (#1.2).</td>
</tr>
<tr class="odd">
<td>ANSI</td>
<td>American National Standards Institute.</td>
</tr>
<tr class="even">
<td>ANSI M</td>
<td>The M (formerly known as MUMPS) programming language is a standard recognized by the American National Standard Institute (ANSI). M stands for Massachusetts Utility Multi-programming System.</td>
</tr>
<tr class="odd">
<td>AUDIT TRAIL</td>
<td>The record or log of an ongoing audit.</td>
</tr>
<tr class="even">
<td>AUDITING</td>
<td>The monitoring and recording of computer use.</td>
</tr>
<tr class="odd">
<td>BACKWARD POINTER</td>
<td>A pointer to your current file from another file; used in the extended pointer syntax.</td>
</tr>
<tr class="even">
<td>BOOLEAN EXPRESSION</td>
<td>A logical comparison between values yielding a true or false result. In M, zero means false and non-zero (often one) means true.</td>
</tr>
<tr class="odd">
<td>CALLABLE ENTRY POINT</td>
<td>An authorized developer call that can be used in any VistA application package. The DBA maintains the list of DBIC-approved entry points.</td>
</tr>
<tr class="even">
<td>CANONIC NUMBER</td>
<td>A number with no leading zeroes and no trailing zeroes after a decimal point.</td>
</tr>
<tr class="odd">
<td>CAPTION</td>
<td>In ScreenMan, a label displayed on the screen. Captions often identify fields that are to be edited.</td>
</tr>
<tr class="even">
<td>CHECKSUM</td>
<td>The result of a mathematical computation involving the individual characters of a routine or file.</td>
</tr>
<tr class="odd">
<td>COMMAND AREA</td>
<td>In ScreenMan, the bottom portion of the screen used to display help information and to accept user commands.</td>
</tr>
<tr class="even">
<td>COMMON MENU</td>
<td>The Common menu consists of options that are available to all users. Entering two question marks at the menus select prompt displays any secondary menu options available to the signed-on user, along with the common options available to all users.</td>
</tr>
<tr class="odd">
<td>CONTROLLED SUBSCRIPTION INTEGRATION AGREEMENT</td>
<td>This applies where the IA describes attributes/functions that <em>must</em> be controlled in their use. The decision to restrict the IA is based on the maturity of the custodian package. Typically, these IAs are created by the requesting package based on their independent examination of the custodian package’s features. For the IA to be approved the custodian grants permission to other VistA packages to use the attributes/functions of the IA; permission is granted on a one-by-one basis where each is based on a solicitation by the requesting package. An example is the extension of permission to allow a package (e.g., Spinal Cord Dysfunction) to define and update a component that is supported within the Health Summary package file structures.</td>
</tr>
<tr class="even">
<td>CURSOR</td>
<td>On your display terminal, the line or rectangle identifying where your next input is placed on the screen.</td>
</tr>
<tr class="odd">
<td>DATA</td>
<td>A representation of facts, concepts, or instructions in a formalized manner for communication, interpretation, or processing by humans or by automatic means. The information you enter for the computer to store and retrieve. Characters that are stored in the computer system as the values of local or global variables. VA FileMan fields hold data values for file entries.</td>
</tr>
<tr class="even">
<td>DATA ATTRIBUTE</td>
<td>A characteristic unit of data such as length, value, or method of representation. VA FileMan field definitions specify data attributes.</td>
</tr>
<tr class="odd">
<td>DATA DICTIONARY</td>
<td>A record of a file’s structure, its elements (fields and their attributes), and relationships to other files. Often abbreviated as DD.</td>
</tr>
<tr class="even">
<td>DATA DICTIONARY ACCESS</td>
<td>A user’s authorization to write/update/edit the data definition for a computer file. Also known as DD Access.</td>
</tr>
<tr class="odd">
<td>DATA INTEGRITY</td>
<td>This term refers to the condition of patient records in terms of completeness and correctness. It also refers to the process in which a particular patient’s data is synchronized at all the sites in which that patient receives care.</td>
</tr>
<tr class="even">
<td>DATA TYPE</td>
<td><p>The kind of data stored in a field. For example, the following are VA FileMan DATA TYPE field values:</p>
<p>NUMERIC</p>
<p>COMPUTED</p>
<p>WORD-PROCESSING</p></td>
</tr>
<tr class="odd">
<td>DATABASE</td>
<td>An organized collection of data spanning many files. Often, all the files on a system constitute that system’s database.</td>
</tr>
<tr class="even">
<td>DATABASE MANAGEMENT SYSTEM (DBMS)</td>
<td>A collection of software that handles the storage, retrieval, and updating of records in a database. A Database Management System (DBMS) controls redundancy of records and provides the security, integrity, and data independence of a database.</td>
</tr>
<tr class="odd">
<td>DATABASE, NATIONAL</td>
<td>A database that contains data collected or entered for all VHA sites.</td>
</tr>
<tr class="even">
<td>DBA</td>
<td>Database Administrator, oversees software development with respect to VistA Standards and Conventions (SAC) such as namespacing. Also, this term refers to the Database Administration function and staff.</td>
</tr>
<tr class="odd">
<td>DBIA</td>
<td>Database Integration Agreement (see Integration Agreements [IA]).</td>
</tr>
<tr class="even">
<td>DECENTRALIZED HOSPITAL COMPUTER PROGRAM (DHCP)</td>
<td>See VISTA.</td>
</tr>
<tr class="odd">
<td>DEFAULT</td>
<td>A computer-provided response to a question or prompt. The default might be a value pre-existing in a file. Often, you can change a default.</td>
</tr>
<tr class="even">
<td>DEPARTMENT OF VETERANS AFFAIRS</td>
<td>The Department of Veterans Affairs (formerly known as the Veterans Administration.)</td>
</tr>
<tr class="odd">
<td>DEVICE</td>
<td>Peripheral connected to the host computer, such as a printer, terminal, disk drive, modem, and other types of hardware and equipment associated with a computer. The host files of underlying operating systems may be treated like devices in that they may be written to (e.g., for spooling).</td>
</tr>
<tr class="even">
<td>DEVICE PROMPT</td>
<td>A Kernel prompt at which you identify where to send your output.</td>
</tr>
<tr class="odd">
<td>DHCP</td>
<td>Decentralized Hospital Computer Program (now known as Veterans Health Information Systems and Technology Architecture [VistA]). VistA software, developed by VA, is used to support clinical and administrative functions at VA Medical Centers nationwide. It is written in M and, via the Kernel, runs on all major M implementations regardless of vendor. VistA is composed of packages that undergo a verification process to ensure conformity with namespacing and other VistA standards and conventions.</td>
</tr>
<tr class="even">
<td>DICTIONARY</td>
<td>Database of specifications of data and information processing resources. The VA FileMan database of data dictionaries is stored in the FILE of files (#1).</td>
</tr>
<tr class="odd">
<td>DIRECT MODE UTILITY</td>
<td>A developer call that is made when working in direct programmer mode. A direct mode utility is entered at the MUMPS prompt (e.g.,&gt;D ^XUP). Calls that are documented as direct mode utilities <em>cannot</em> be used in application software code.</td>
</tr>
<tr class="even">
<td>DOMAIN</td>
<td>A site for sending and receiving mail.</td>
</tr>
<tr class="odd">
<td>DOUBLE QUOTES (““)</td>
<td>Symbol used in front of a Common option’s menu text or synonym to select it from the Common menu. For example, the five-character string “TBOX” selects the User’s Toolbox Common option.</td>
</tr>
<tr class="even">
<td>EDIT WINDOW</td>
<td>In ScreenMan, the area in which you enter or edit data. It is highlighted with either reverse video or an underline. In Screen Editor, the area in which you enter and edit text; the area between the status bar and the ruler.</td>
</tr>
<tr class="odd">
<td>ENTRY</td>
<td>A record in a file. “Entry” and “record” are used interchangeably.</td>
</tr>
<tr class="even">
<td>ERROR TRAP</td>
<td>A mechanism to capture system errors and record facts about the computing context such as the local symbol table, last global reference, and routine in use. Operating systems provide tools such as the %ER utility. The Kernel provides a generic error trapping mechanism with use of the ^%ZTER global and ^XTER* routines. Errors can be trapped and, when possible, the user is returned to the menu system.</td>
</tr>
<tr class="odd">
<td>EXTENDED POINTERS</td>
<td>A means to reference fields in files other than your current file.</td>
</tr>
<tr class="even">
<td>FACILITY</td>
<td>Geographic location at which VA business is performed.</td>
</tr>
<tr class="odd">
<td>FIELD</td>
<td>In an entry, a specified area used to hold values. The specifications of each VA FileMan field are documented in the file’s data dictionary.</td>
</tr>
<tr class="even">
<td>FIELD NUMBER</td>
<td>The unique number used to identify a field in a file. A field can be referenced by “<strong>#</strong>” followed by the field number.</td>
</tr>
<tr class="odd">
<td>FILE</td>
<td>A set of related records (or entries) treated as a unit.</td>
</tr>
<tr class="even">
<td>FILE MANAGER (VA FILEMAN)</td>
<td>VistA Database Management System (DBMS). The central component of Kernel that defines the way standard VistA files are structured and manipulated.</td>
</tr>
<tr class="odd">
<td>FORM</td>
<td>In ScreenMan, a group of one or more pages that comprise a complete transaction. Comparable to an INPUT template.</td>
</tr>
<tr class="even">
<td>FORUM</td>
<td>The central E-mail system within VistA. Developers use FORUM to communicate at a national level about programming and other issues. FORUM is located at the OI Field Office—Washington, DC (162-2).</td>
</tr>
<tr class="odd">
<td>FREE TEXT</td>
<td>A DATA TYPE field value that can contain any printable characters.</td>
</tr>
<tr class="even">
<td>FULL-SCREEN EDITING</td>
<td>The ability to enter data in various locations on the two-dimensional computer display. Compare to scrolling mode.</td>
</tr>
<tr class="odd">
<td>GLOBAL VARIABLE</td>
<td>Variable that is stored on disk (M usage).</td>
</tr>
<tr class="even">
<td>HELP PROMPT</td>
<td>The brief help that is available at the field level when entering one or more question marks.</td>
</tr>
<tr class="odd">
<td>HISTOGRAM</td>
<td>A type of bar graph that indicates frequency of occurrence of particular values.</td>
</tr>
<tr class="even">
<td>IDENTIFIER</td>
<td>In VA FileMan, a field that is defined to aid in identifying an entry in conjunction with the NAME field.</td>
</tr>
<tr class="odd">
<td>INDEX</td>
<td>An ordered list used to speed retrieval of entries from a file based on a value in some field or fields. The term “simple index” refers to an index that stores the data for a single field; the term “compound index” refers to an index that stores the data for more than one field. Indexes are created and maintained via cross-references.</td>
</tr>
<tr class="even">
<td>INPUT TEMPLATE</td>
<td>A pre-defined list of fields that together comprise an editing session.</td>
</tr>
<tr class="odd">
<td>INTEGRATION AGREEMENTS (IA)</td>
<td>Integration Agreements define agreements between two or more VistA software applications to allow access to one development domain by another. VistA software developers are allowed to use internal entry points (APIs) or other software-specific features that are <em>not</em> available to the general programming public. Any software developed for use in the VistA environment is required to adhere to this standard; as such, it applies to vendor products developed within the boundaries of DBA assigned development domains (e.g., MUMPS AudioFax). An IA defines the attributes and functions that specify access. The DBA maintains and records all IAs in the Integration Agreement database on FORUM. Content can be viewed using the DBA menu or the Health Systems Design &amp; Development’s Web page.</td>
</tr>
<tr class="even">
<td>INTERNAL ENTRY NUMBER</td>
<td>The number used to identify an entry within a file. Every record has a unique internal entry number. Often abbreviated as IEN.</td>
</tr>
<tr class="odd">
<td>INTERNAL ENTRY NUMBER (IEN)</td>
<td>The number used to identify an entry within a file. Every record has a unique internal entry number.</td>
</tr>
<tr class="even">
<td>IRM</td>
<td>Information Resource Management. A service at VA medical centers responsible for computer management and system security.</td>
</tr>
<tr class="odd">
<td>ISO</td>
<td>Information Security Officer.</td>
</tr>
<tr class="even">
<td>KERNEL</td>
<td>A VISTA software package that functions as an intermediary between the host operating system and VISTA application packages. Kernel includes installation, menu, security, and device services.</td>
</tr>
<tr class="odd">
<td>KEY</td>
<td>A group of fields that, taken collectively, uniquely identifies a record in a file or subfile. All fields in a key <em>must</em> have values. The term “simple key” refers to keys that are composed of only one field; the term “compound key” refers to keys that are composed of more than one field. Keys are stored in the KEY file (#.31)</td>
</tr>
<tr class="even">
<td>LAN</td>
<td>Local Area Network.</td>
</tr>
<tr class="odd">
<td>LAYGO</td>
<td>A user’s authorization to create a new entry when editing a computer file. An acronym for <strong>L</strong>earn <strong>A</strong>s <strong>Y</strong>ou <strong>Go</strong>.</td>
</tr>
<tr class="even">
<td>LIM</td>
<td>Laboratory Information Manager</td>
</tr>
<tr class="odd">
<td>LINE EDITOR</td>
<td>The VA FileMan editor that lets you input and change text on a line-by-line basis. The Line Editor works in scrolling mode. See Screen Editor.</td>
</tr>
<tr class="even">
<td>LOINC</td>
<td>Logical Observation Identifier Names and Codes.</td>
</tr>
<tr class="odd">
<td>LOOKUP</td>
<td>To find an entry in a file using a value for one of its fields.</td>
</tr>
<tr class="even">
<td>M (ANSI STANDARD)</td>
<td>Massachusetts General Hospital Utility Multi-Programming System (M, formerly named MUMPS) is a software package, which consists of a high level programming language and a built-in database.</td>
</tr>
<tr class="odd">
<td>MAILMAN</td>
<td>An electronic mail system (e-mail) that allows you to send messages to and receive them from other users via the computer. It is part of VISTA.</td>
</tr>
<tr class="even">
<td>MENU</td>
<td>A list that includes the names of options from which you can select an activity.</td>
</tr>
<tr class="odd">
<td>MENU SYSTEM</td>
<td>The overall Menu Manager logic as it functions within the Kernel framework.</td>
</tr>
<tr class="even">
<td>MENU TEXT</td>
<td>The descriptive words that appear when a list of option choices is displayed. Specifically, the Menu Text field of the OPTION file (#19). For example, User’s Toolbox is the menu text of the XUSERTOOLS option. The option’s synonym is TBOX.</td>
</tr>
<tr class="odd">
<td>MLTF</td>
<td>MASTER LABORATORY TEST file (#66.3).</td>
</tr>
<tr class="even">
<td>MUMPS</td>
<td>Abbreviated as M. The American National Standards Institute (ANSI) computer language used by VA FileMan and throughout VISTA. The acronym MUMPS stands for <strong>M</strong>assachusetts General Hospital <strong>U</strong>tility <strong>M</strong>ulti <strong>P</strong>rogramming <strong>S</strong>ystem.</td>
</tr>
<tr class="odd">
<td>NAME FIELD</td>
<td>The one field that <em>must</em> be present for every file and file entry. It is also called the .01 field. At a file’s creation the .01 field is given the label NAME. This label can be changed.</td>
</tr>
<tr class="even">
<td>NAMESPACE</td>
<td>A convention for naming VistA package elements. The Database Administrator (DBA) assigns unique character strings for package developers to use in naming routines, options, and other package elements so that packages may coexist. The DBA also assigns a separate range of file numbers to each package.</td>
</tr>
<tr class="odd">
<td>NAVIGATION</td>
<td><p>Navigation meanings:</p>
<p>Switching your reference point from one file to another.</p>
<p>Moving your cursor around a terminal display or a document using cursor keys and other commands.</p></td>
</tr>
<tr class="even">
<td>NODE</td>
<td>In a tree structure, a point at which subordinate items of data originate. An M array element is characterized by a name and a unique subscript. Thus the terms: node, array element, and subscripted variable are synonymous. In a global array, each node might have specific fields or “pieces” reserved for data attributes such as name.</td>
</tr>
<tr class="odd">
<td>NON-CANONIC NUMBER</td>
<td>A number with either leading zeroes or trailing zeroes after a decimal point. M treats non-canonic numbers as text instead of as numbers.</td>
</tr>
<tr class="even">
<td>NON-NULL</td>
<td>A value other than null. A space and zero are non-null values.</td>
</tr>
<tr class="odd">
<td>NTRT</td>
<td>New Term Rapid Turnaround (NTRT). The process to distribute standard reference files to VistA environments.</td>
</tr>
<tr class="even">
<td>NULL</td>
<td>Empty. A field or variable that has no value associated with it is null.</td>
</tr>
<tr class="odd">
<td>NULL RESPONSE</td>
<td>When replying to a prompt, pressing only the <strong>Enter</strong> key, abbreviated as <strong>&lt;Enter&gt;</strong>, to enter nothing.</td>
</tr>
<tr class="even">
<td>NUMERIC EXPRESSION</td>
<td>An expression whose value is a number. Compare to string expression.</td>
</tr>
<tr class="odd">
<td>NUMERIC FIELD</td>
<td>Response that is limited to a restricted number of digits. It can be dollar valued or a decimal figure of specified precision.</td>
</tr>
<tr class="even">
<td>OED</td>
<td>Office of Enterprise Development</td>
</tr>
<tr class="odd">
<td>OI&amp;T</td>
<td>Office of Information Technology</td>
</tr>
<tr class="even">
<td>OIFO</td>
<td>Office of Information Field Office.</td>
</tr>
<tr class="odd">
<td>OPERATOR</td>
<td>One of the processes done to the elements in an expression to create a value.</td>
</tr>
<tr class="even">
<td>OPTION</td>
<td>A computing activity that you can select, usually a choice from a menu.</td>
</tr>
<tr class="odd">
<td>OPTION NAME</td>
<td>Name field in the OPTION file (e.g., XUMAINT for the option that has the menu text “Menu Management”). Options are namespaced according to VistA conventions monitored by the DBA.</td>
</tr>
<tr class="even">
<td>PACKAGE (SOFTWARE)</td>
<td>The set of programs, files, documentation, help prompts, and installation procedures required for a given application (e.g., Laboratory, Pharmacy, and PIMS). A VistA software environment is composed of elements specified via the PACKAGE file (#9.4). Elements include files, associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, VistA software can be requested through the Freedom of Information Act (FOIA).</td>
</tr>
<tr class="odd">
<td>PATTERN MATCH</td>
<td>In M, an operator that compares the contents of a variable or literal to a specified pattern of characters or kinds of characters.</td>
</tr>
<tr class="even">
<td>POINTER TO A FILE</td>
<td>A DATA TYPE field value that contains an explicit reference to an entry in a file. POINTER TO A FILE-type fields are used to relate files to each other.</td>
</tr>
<tr class="odd">
<td>POPUP PAGE</td>
<td>In ScreenMan, a page that overlays the regular ScreenMan screen in order to present the contents of a selected Multiple.</td>
</tr>
<tr class="even">
<td>PREFERRED EDITOR</td>
<td>The editor always entered when you access a WORD-PROCESSING-type field; your default editor. Kernel <em>must</em> be present to establish a Preferred Editor.</td>
</tr>
<tr class="odd">
<td>PRIMARY KEY</td>
<td>A Data Base Management System construct, where one or more fields uniquely define a record (entry) in a file (table). The fields are required to be populated for every record on the file, and are unique, in combination, for every record on the file.</td>
</tr>
<tr class="even">
<td>PRIMARY MENU</td>
<td>The list of options presented at sign-on. Each user <em>must</em> have a primary menu in order to sign-on and reach Menu Manager. Users are given primary menus by Information Resource Management (IRM). This menu should include most of the computing activities the user needs.</td>
</tr>
<tr class="odd">
<td>PRINT TEMPLATE</td>
<td>The stored specifications of a printed report, including fields to be printed and formatting instructions.</td>
</tr>
<tr class="even">
<td>PRIVATE INTEGRATION AGREEMENT</td>
<td>Where only a single application is granted permission to use an attribute/function of another VistA package. These IAs are granted for special cases, transitional problems between versions, and release coordination. A Private IA is also created by the requesting package based on their examination of the custodian package’s features. Example: one package distributes a patch from another package to ensure smooth installation.</td>
</tr>
<tr class="odd">
<td>PROMPT</td>
<td>A question or message from the computer requiring your response.</td>
</tr>
<tr class="even">
<td>RECORD</td>
<td>A set of data pertaining to a single entity in a file; an entry in a file.</td>
</tr>
<tr class="odd">
<td>RECORD NUMBER</td>
<td>See Internal Entry Number.</td>
</tr>
<tr class="even">
<td>RELATIONAL NAVIGATION</td>
<td>Changing your current (or primary) file reference to another file. Relational navigation is accomplished by using the extended pointer syntax without specifying a field in the referenced file.</td>
</tr>
<tr class="odd">
<td>REQUIRED FIELD</td>
<td>A field that <em>cannot</em> be left null for an entry.</td>
</tr>
<tr class="even">
<td>REVERSE VIDEO</td>
<td>The reversal of light and dark in the display of selected characters on a video screen. For example, if text is normally displayed as black letters on a white background, reverse video presents the text as white letters on a black background or vice versa.</td>
</tr>
<tr class="odd">
<td>ROUTINE</td>
<td>Program or a sequence of instructions called by a program that may have some general or frequent use. M routines are groups of program lines, which are saved, loaded, and called as a single unit via a specific name.</td>
</tr>
<tr class="even">
<td>SAC</td>
<td>Standards and Conventions. Through a process of quality assurance, all VistA software is reviewed with respect to SAC guidelines as set forth by the Standards and Conventions Committee (SACC).</td>
</tr>
<tr class="odd">
<td>SACC</td>
<td>VistA Standards and Conventions Committee. This Committee is responsible for maintaining the SAC.</td>
</tr>
<tr class="even">
<td>SCATTERGRAM</td>
<td>A graph in which occurrences of two fields are displayed on an X-Y coordinate grid to aid in data analysis.</td>
</tr>
<tr class="odd">
<td>SCREEN EDITOR</td>
<td>VA FileMan Screen-oriented text editor. It can be used to enter data into any WORD-PROCESSING field using full-screen editing instead of line-by-line editing. See Line Editor.</td>
</tr>
<tr class="even">
<td>SCREENMAN</td>
<td>The set of routines that supports Screen-oriented data editing and data display.</td>
</tr>
<tr class="odd">
<td>SCREENMAN FORMS</td>
<td>Screen-oriented display of fields, for editing or simply for reading. VA FileMan Screen Manager is used to create forms that are stored in the FORM file (#.403) and exported with a software application. Forms are composed of blocks (stored in the BLOCK file [#.404]) and can be regular, full screen pages or smaller, “popup” pages.</td>
</tr>
<tr class="even">
<td>SCREEN-ORIENTED</td>
<td>A computer interface in which you see many lines of data at a time and in which you can move your cursor around the display screen using screen navigation commands. Compare to Scrolling Mode.</td>
</tr>
<tr class="odd">
<td>SCROLLING MODE</td>
<td>The presentation of the interactive dialogue one line at a time. Compare to Screen-oriented.</td>
</tr>
<tr class="even">
<td>SEARCH TEMPLATE</td>
<td>The saved results of a search operation. Usually, the actual entries found are stored in addition to the criteria used to select those entries.</td>
</tr>
<tr class="odd">
<td>SECURITY KEY</td>
<td>The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="even">
<td>SENSITIVE PATIENT</td>
<td>Patient whose record contains certain information, which may be deemed sensitive by a facility, such as political figures, employees, patients with a particular eligibility or medical condition. If a shared patient is flagged as sensitive at one of the treating sites, a bulletin is sent to the DG SENSITIVITY mail group at each subscribing site telling where, when, and by whom the flag was set. Each site can then review whether the circumstances meet the local criteria for sensitivity flagging.</td>
</tr>
<tr class="odd">
<td>SEPG</td>
<td>Software Engineering Process Group (SEPG) (renamed the Engineering Process Group [EPG])</td>
</tr>
<tr class="even">
<td>SERVER</td>
<td>The computer where the data and the Business Rules reside. It makes resources available to client workstations on the network. In VistA, it is an entry in the OPTION file (#19). An automated mail protocol that is activated by sending a message to a server at another location with the “S.server” syntax. A server’s activity is specified in the OPTION file (#19) and can be the running of a routine or the placement of data into a file.</td>
</tr>
<tr class="odd">
<td>SET OF CODES</td>
<td>A DATA TYPE field value where a short character string is defined to represent a longer value.</td>
</tr>
<tr class="even">
<td>SIMPLE EXTENDED POINTERS</td>
<td>An extended pointer that uses a pre-existing pointer relationship to access entries in another file.</td>
</tr>
<tr class="odd">
<td>SITE MANGER/IRM CHIEF</td>
<td>At each site, the individual who is responsible for managing computer systems, installing and maintaining new modules, and serving as a liaison to the CIO Field Offices.</td>
</tr>
<tr class="even">
<td>SOFTWARE (PACKAGE)</td>
<td>The set of programs, files, documentation, help prompts, and installation procedures required for a given application (e.g., Laboratory, Pharmacy, and PIMS). A VistA software environment is composed of elements specified via the PACKAGE file (#9.4). Elements include files, associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, VistA software can be requested through the Freedom of Information Act (FOIA).</td>
</tr>
<tr class="odd">
<td>SORT</td>
<td>To place items in order, often in alphabetical or numeric sequence.</td>
</tr>
<tr class="even">
<td>SORT TEMPLATE</td>
<td>The stored record of sort specifications. It contains sorting order as well as restrictions on the selection of entries. Used to prepare entries for printing.</td>
</tr>
<tr class="odd">
<td>SPACEBAR RETURN</td>
<td>You can answer a VA FileMan prompt by pressing the spacebar and then the Return key. This indicates to VA FileMan that you would like the last response you were working on at that prompt recalled.</td>
</tr>
<tr class="even">
<td>SPECIAL QUEUING</td>
<td>Option attribute indicating that Task Manager should automatically run the option whenever the system reboots.</td>
</tr>
<tr class="odd">
<td>STUFF</td>
<td>To place values directly into a field, usually with no user interaction.</td>
</tr>
<tr class="even">
<td>SUBENTRY</td>
<td>An entry in a Multiple; also called a Subrecord.</td>
</tr>
<tr class="odd">
<td>SUBFIELD</td>
<td>A field in a Multiple.</td>
</tr>
<tr class="even">
<td>SUBFILE</td>
<td>The data structure of a Multiple. In many respects, a Subfile has the same characteristics as a File.</td>
</tr>
<tr class="odd">
<td>SUBSCRIPT</td>
<td>A symbol that is associated with the name of a set to identify a particular subset or element. In M, a numeric or string value that: is enclosed in parentheses, is appended to the name of a local or global variable, and identifies a specific node within an array.</td>
</tr>
<tr class="even">
<td>SUPPORTED REFERENCE INTEGRATION AGREEMENT</td>
<td>This applies where any VistA application may use the attributes/functions defined by the IA (these are also called “Public “). An example is an IA that describes a standard API such as DIE or VADPT. The package that creates/maintains the Supported Reference <em>must</em> ensure it is recorded as a Supported Reference in the IA database. There is no need for other VistA packages to request an IA to use these references; they are open to all by default.</td>
</tr>
<tr class="odd">
<td>TASK MANAGER</td>
<td>Kernel module that schedules and processes background tasks (also called TaskMan)</td>
</tr>
<tr class="even">
<td>TEMPLATE</td>
<td>Means of storing report formats, data entry formats, and sorted entry sequences. A template is a permanent place to store selected fields for use at a later time. Edit sequences are stored in the INPUT TEMPLATE file (#.402), print specifications are stored in the PRINT TEMPLATE file (#.4), and search or sort specifications are stored in the SORT TEMPLATE file (#.401).</td>
</tr>
<tr class="odd">
<td>TERMINAL EMULATION</td>
<td>Using one kind of terminal or computer display to mimic another kind. Often used with PC remote communication applications.</td>
</tr>
<tr class="even">
<td>TERMINAL TYPE</td>
<td>The designation of the kind of computer peripheral being used (e.g., the kind of video display or printer). Full terminal type functionality is supplied by Kernel.</td>
</tr>
<tr class="odd">
<td>TRIGGER</td>
<td>A type of VA FileMan cross-reference. Often used to update values in the database given certain conditions (as specified in the trigger logic). For example, whenever an entry is made in a file, a trigger could automatically enter the current date into another field holding the creation date.</td>
</tr>
<tr class="even">
<td>TRUTH TEST</td>
<td>An evaluation of an expression yielding a true or false result. In M, usually a 1 (true) or a 0 (false) is returned from a truth test.</td>
</tr>
<tr class="odd">
<td>UCI</td>
<td>User Class Identification, a computing area. The MGR UCI is typically the Manager’s account, while VAH or ROU may be Production accounts.</td>
</tr>
<tr class="even">
<td>UP-ARROW</td>
<td>The <strong>^</strong> character (caret); used in VA FileMan for exiting an option or canceling a response. Also used in combination with a field name or prompt to jump to the specified field or prompt.</td>
</tr>
<tr class="odd">
<td>UPLOAD</td>
<td>Send a file from one computer system to another (usually using communications software).</td>
</tr>
<tr class="even">
<td>USER ACCESS</td>
<td>This term is used to refer to a limited level of access, to a computer system, which is sufficient for using/operating a package, but does <em>not</em> allow programming, modification to data dictionaries, or other operations that require programmer access. Any option, for example, can be locked with the key XUPROGMODE, which means that invoking that option requires programmer access. The user’s access level determines the degree of computer use and the types of computer programs available. The System Manager assigns the user an access level.</td>
</tr>
<tr class="odd">
<td>VA</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>VA FILEMAN</td>
<td>VistA Database Management System (DBMS). The central component that defines the way standard VistA files are structured and manipulated.</td>
</tr>
<tr class="odd">
<td>VAMC</td>
<td>Veterans Affairs Medical Center.</td>
</tr>
<tr class="even">
<td>VARIABLE</td>
<td>Character (or group of characters) that refers to a value. M (previously referred to as MUMPS) recognizes 3 types of variables: local variables, global variables, and special variables. Local variables exist in a partition of main memory and disappear at sign-off. A global variable is stored on disk, potentially available to any user. Global variables usually exist as parts of global arrays. The term “global” may refer either to a global variable or a global array. A special variable is defined by systems operations (e.g., $TEST).</td>
</tr>
<tr class="odd">
<td>VERIFY CODE</td>
<td><p>The Kernel’s Sign-on/Security system uses the Verify code to validate the user’s identity. This is an additional security precaution used in conjunction with the Access code. Verify codes shall be at least eight characters in length and contain three of the following four kinds of characters:</p>
<p>Letters (lowercase)</p>
<p>Letters (uppercase)</p>
<p>Numbers</p>
<p>Characters that are neither letters nor numbers (e.g., “<strong>#</strong>”, “<strong>@</strong>” or “<strong>$</strong>”).</p>
<p>If entered incorrectly, the system does <em>not</em> allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen.</p></td>
</tr>
<tr class="even">
<td>VHA</td>
<td>Veterans Health Administration.</td>
</tr>
<tr class="odd">
<td>VISN</td>
<td>Veterans Integrated Service Network</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>The Veterans Health Information Systems and Technology Architecture (VistA), within the Department of Veterans Affairs, is the component of the Veterans Health Administration that develops software and installs, maintains, and updates compatible computer systems in VA medical facilities. (Previously known as the Decentralized Hospital Computer Program [DHCP].)</td>
</tr>
<tr class="odd">
<td>VPID</td>
<td>Veterans Administration Personal Identifier.</td>
</tr>
<tr class="even">
<td>VUID</td>
<td>The VA unique identifier.</td>
</tr>
<tr class="odd">
<td>WAN</td>
<td>Wide Area Network.</td>
</tr>
</tbody>
</table>

Glossary

<span id="_Hlt446131684" class="anchor"></span>Index

# A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assumptions, 4

# C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Callout boxes, 3

Conventions, 2

# D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Disclaimer

Software, 1

Disclaimers, 1

Documentation, 2

Conventions, 2

Disclaimer, 2

Navigation, 3

Symbols, 2

# G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Glossary, 35

# H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Help, 4

at Prompts, 4

Online, 4

Question Marks, 4

Home Pages

Adobe Website, 4

VA Software Document Library (VDL) Website, 4

How to Use this Manual, 1

# I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Intended Audience, 1

# M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Manuals

Reference, 4

# R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Materials, 4

# U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

URLs

Adobe Website, 4

VA Software Document Library (VDL) Website, 4

# V

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA Software Document Library (VDL)

Website, 4

# W

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Websites

Adobe Website, 4

VA Software Document Library (VDL), 4

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: LR*5.2*468 Laboratory NDS LIM User Manual

## Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Figure 1. Laboratory New Test Process Flow 10](#_bookmark17)

> [Figure 2. LIM NDS MENU 12](#_bookmark21)

> [Figure 3. Associate Test to NDS MLTF Menu Option 14](#_bookmark27)

> [Figure 4. ATM Associate Test to NDS MLTF 15](#_bookmark28)

> [Figure 5. Example Associate Test to NDS MLTF Option (ATM) 16](#_bookmark29)

> [Figure 6. WAT – Walk Associate Test to MLTF Menu Option 17](#_bookmark31)

> [Figure 7. Example Walk Associate Test to MLTF 18](#_bookmark32)

> [Figure 8. MIE - Managed Items Edit Default Values 19](#_bookmark34)

> [Figure 9. MIE - Managed Items Edit Menu Option 19](#_bookmark35)

> [Figure 10. Example of Managed Items Edit Process 20](#_bookmark36)

> [Figure 11. LIM NDS Reports 22](#_bookmark38)

> [Figure 12. Example Lab to MLTF Extract Report 23](#_bookmark40)

> [Figure 13. Example Print NDS Audits in File 60 Report 24](#_bookmark42)

> [Figure 14. Example Print Specimens Without VUIDS 25](#_bookmark44)

> [Figure 15. LIM NDS Purge File 60 Audits Option 26](#_bookmark46)

> [Figure 16. Example Purge NDS File 60 Audits Option 26](#_bookmark47)

> [Figure 17. PTI - Print Specimens with Inactive VUIDS Option 27](#User_Access_Levels)

> [Figure 18. Example Print Specimens with Inactive VUIDS 27](#_bookmark50)

## Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Table 1. Documentation Symbol Descriptions 3](#_bookmark3)

> [Table 2. LIM NDS MENU Options and Descriptions 12](#_bookmark23)

> How to Use this Manual

### HTML Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Why produce an HTML (Hypertext Markup Language) edition of this User Manual?

- The HTML versions of the manuals are useful as online documentation support as you use the Laboratory LIM NTRT functions. HTML manuals allow you to instantly jump (link) to specific topics or references online.
- The HTML manuals are “living” documents that are continuously updated with the most current information (unlike paper or printed documentation). They are updated based on new versions, patches, or enhancements to the documentation.
- Presenting manuals in an HTML format on a Web server also gives new opportunities, such as accessing embedded multimedia training material (e.g., movies) directly in the manuals themselves.
- Manuals are accessible over the VA Intranet network.

> Intended Audience

> The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Automated Data Processing Application Coordinators (ADPACs)
- Information Resource Management (IRM)—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management.
- Laboratory Information Managers (LIM)

## Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

> ![](lr-5-2-468-laboratory-nds-lim-user-manual/003.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).

### Documentation Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual provides an overall explanation of VA Laboratory LIM NDS system and the functionality; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet Websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OI&T) VistA Development Intranet website.

> ![](lr-5-2-468-laboratory-nds-lim-user-manual/004.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

## Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> describes each of these symbols.

> <span id="_bookmark3" class="anchor"></span>Table 1. Documentation Symbol Descriptions

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Symbol</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](lr-5-2-468-laboratory-nds-lim-user-manual/005.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>NOTE / REF:</strong> Used to inform the reader of general information including references to additional reading material.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](lr-5-2-468-laboratory-nds-lim-user-manual/006.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>CAUTION / RECOMMENDATION / DISCLAIMER:</strong> Used to caution the reader to take special notice of critical information.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](lr-5-2-468-laboratory-nds-lim-user-manual/007.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>TIP:</strong> Used to inform the reader of helpful tips or tricks they can use.</p>
</blockquote></td>
</tr>
</tbody>
</table>

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
  - Patient and user names are formatted as follows:

> \<*Application Name/Abbreviation/Namespace*\>PATIENT,\[*N*\] and \<*Application Name/Abbreviation/Namespace*\>USER,\[*N*\] respectively, where “\<*Application Name/Abbreviation/Namespace*\>” is defined in the Approved Application Abbreviations document and “*N*” represents the first name as a number spelled out and incremented with each new entry. For example, in VA FileMan (FM) test patient and user names would be documented as follows: FMPATIENT, ONE; FMPATIENT, TWO; FMPATIENT, THREE;

> etc.

- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
  - User’s responses to online prompts are bold typeface, underlined and highlighted in yellow (e.g., \<Enter\>).
  - Emphasis within a dialogue box is bold typeface, underlined and highlighted in blue (e.g.

> STANDARD LISTENER: RUNNING).

- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

> ![](lr-5-2-468-laboratory-nds-lim-user-manual/008.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., DIEXTRACT).

> ![](lr-5-2-468-laboratory-nds-lim-user-manual/009.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g. CamelCase).

## Documentation Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back

> and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to your customized toolbar.
9.  Select OK.

> You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

> ![](lr-5-2-468-laboratory-nds-lim-user-manual/010.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

### Help at Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of the software.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- Laboratory Information Manager functions

## Reference Materials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Readers who wish to learn more about the VA Laboratory NTRT system should consult the following documents:

- [<u>NTRT User Guide</u>](http://vaww.oed.portal.va.gov/projects/sts/VETS%20Consolidated/VETS/STS_VETS_NTRT%20User%20Guide.docx) (STS SharePoint \> VETS Consolidated \> VETS \> STS_VETS_NTRT User Guide.docx)

> VA Laboratory documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: [<u>http://www.adobe.com/</u>](http://www.adobe.com/)

> VistA software documentation can be downloaded from the VA Software Document Library (VDL) at: [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/)

> ![](lr-5-2-468-laboratory-nds-lim-user-manual/011.png) REF: Laboratory manuals are located on the VDL.

## Associating Site/Specimen to MLTF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are three ways to associate a Site/Specimen to the MLTF.

1.  Using the MLTF NUMBER prompt (field (#30) in the site/specimen sub-multiple (#60.01) when creating a new or editing an existing Site/Specimen within FileMan.

> This is the current method that LIMs use to create or modify a LABORATORY TEST file (#60) entry.

2.  Using the ATM Associate Test to NDS MLTF option on the LIM NDS MENU.
3.  Using the WAT Walk Associate Test to MLTF option on the LIM NDS MENU.

> ![](lr-5-2-468-laboratory-nds-lim-user-manual/013.png) CAUTION: The MASTER LABORATORY TEST file (#66.3), distributed with the patch is not populated. Therefore, the options in the LIM NDS MENU should not be used at this time. In the future, the NTRT team will populate and deploy the MLTF file for all sites.

> Prior to the population of the MLTF file, creation of a new test in LABORATORY TEST file (# 60) will generate a mailman message to the LIM entering the new site/specimen and members of the facilities G.LMI mail group. Because the functionality to forward that message on to the NTRT team has not yet been turned on, sites should ignore these messages.

> When the MLTF has been deployed a message will be listed on the NTRT_NOTIFICATION-L listserv which the LIMs will have subscribed to, (see the last bullet point under section 1.4 NTRT process).

> Informational patch LR\*5.2\*481 provides instructions for activating the NTRT message process.

### A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assumptions, 5

### C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Callout Boxes, 3 Contents, iv Conventions
> Documentation, 3

### D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Disclaimers, 2
> Software, 2 Documentation
> Conventions, 3
> Navigation, 4
> Symbols, 3

### F

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figures, vi

### G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Glossary, 29

### H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Help
> At Prompts, 4
> Online, 4
> Question Marks, 4 Home Pages
> Adobe Website, 5
> VA Software Document Library (VDL) Website, 5
> How to
> Use this Manual, 1 HTML Manuals, 1

### I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Intended Audience, 1

### M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Manuals
> In HTML, 1
> Reference, 5

### O

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Online
> Documentation, 4
> Orientation, 1

### Q

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Question Mark Help, 4

### R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reference Materials, 5

### S

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Software Disclaimer, 2 Symbols
> Found in the Documentation, 3

### T

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Table of Contents, iv Tables, vi

### U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> URLs
> Adobe Website, 5
> VA Software Document Library (VDL) Website, 5

### V

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA Software Document Library (VDL) Website, 5

### W

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Websites
> Adobe Website, 5
> VA Software Document Library (VDL), 5
