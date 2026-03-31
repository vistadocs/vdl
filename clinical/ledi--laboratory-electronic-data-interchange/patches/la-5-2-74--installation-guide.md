---
title: LA*5.2*74/LR*5.2*350/HDI*1*7  LDSI/LEDI IV Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: LEDI
app_name: "Laboratory: Electronic Data Interchange"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*74
group_key: "LEDI:LA:5.2"
file_numbers: 
  - 62
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - sent
  - alert
  - error
  - lexicon
  - lookup
  - ledi
  - entry
  - mark
  - install
  - table
page_count: 0
word_count: 12403
section_count: 10
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/lab_ledi_iv_install_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/lab_ledi_iv_install_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=75"
---

---
title: <span id="_Toc196028944" class="anchor"></span>Laboratory Data Sharing & Interoperability (LDSI) Laboratory Electronic Data Interchange (LEDI) IV
---

![](la-5-2-74-lr-5-2-350-hdi-1-7-ldsi-ledi-iv-install-guide/001.png)

LEDI IV Installation Guide

July 2013

> **IMPORTANT:** Please read this manual <u>prior</u> to installing LEDI IV

Office of Information and Technology (OI&T)

Product Development

Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 44%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Authors</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>4/1/11</td>
<td>.01</td>
<td><p>Initial Document:</p>
<p>Convert Laboratory Systems Re-engineering Project (LSRP) Installation Guide into this LEDI IV Installation Guide for Use for Alpha Testing</p></td>
<td><p>LSRP Documentation Review Team:</p>
<p>Team Lead<mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>5/3/11</td>
<td>.02</td>
<td>Update to make specific for LSRP’s reference</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/6/11</td>
<td>.03</td>
<td>Update per peer review</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/10/11</td>
<td>.04</td>
<td>Remove reference to appendix per <mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/10/11</td>
<td>.05</td>
<td>Update formatting sections</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/12/11</td>
<td>.06</td>
<td>Update per review post Original Test Account (OTA) install</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/12/11</td>
<td>.07</td>
<td>Incorporate changes in document</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/12/11</td>
<td>.08</td>
<td>Update Section 3 with patch installation instructions</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/12/11</td>
<td>.09</td>
<td>Review for content and formatting</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/13/11</td>
<td>.10</td>
<td>Update per <mark>REDACTED</mark>comments and <mark>REDACTED</mark>additions</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/6/11</td>
<td>.11</td>
<td>Update Sections 5.1.2 and 5.1.5</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/20/11</td>
<td>.11</td>
<td>Remove LSRP and Lexington specific information</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/01/11</td>
<td>.12</td>
<td><ul>
<li><p>Update with Development Team input for purposes of the BETA test</p></li>
<li><p>Remove DOD in Introduction to eliminate confusion</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/02/11</td>
<td>.12</td>
<td>Add more detail provided by <mark>REDACTED</mark>for File 63 Remediation Installation</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/12/11</td>
<td>.13</td>
<td><ul>
<li><p>Add pre-installation steps to Section 2.2.9 to prevent transmission errors between the collecting and the performing labs</p></li>
<li><p>Add reference to the LEDI III Installation Guide</p></li>
<li><p>Remove BETA references in Section 4</p></li>
<li><p>Remove Implementation Guide as a reference since it is being combined with the User Manual</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>1/6/12</td>
<td>.14</td>
<td>Update footers to prepare for BETA sites</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1/11/12</td>
<td>1.0</td>
<td>Prepare for Operational Readiness Review (ORR)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>1/26/12</td>
<td>1.1</td>
<td>Revisions from CLIN 4 and Development Team reviews</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2/02/12</td>
<td>1.2</td>
<td><ul>
<li><p>Update Section 2.2.3 to indicate that the AP and MICRO interface set ups will be done by the LSRP team</p></li>
<li><p>Per <mark>REDACTED</mark>– specify that it is the Laboratory Information Manager (LIM) who creates the orderable lab test for each subscript CY, EM, etc.</p></li>
<li><p>Add two more sections for the download of the SNOMED CT and the HDI pieces of LEDI IV</p></li>
<li><p>Clarify the CLIN 4 comments in Section 3.2.5 for Compare Transport Global to Current System</p></li>
<li><p>Move the creation of the AP collections sample and lab step from Post-Installation to Pre-Installation Instruction</p></li>
<li><p>Add the Post-Installation steps/ instructions (with screen capture) for editing the Create and Mail Lab Reports option</p></li>
<li><p>Clarify the locations from where the software will be available</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/23/12</td>
<td>1.3</td>
<td><ul>
<li><blockquote>
<p>Add that the National Service Desk is to be contacted if errors arise post-installation as well as when the LRNIGHTY process runs and errors are found</p>
</blockquote></li>
<li><blockquote>
<p>Add HDI*1.0*7 as an included patch within the LEDI IV Host build</p>
</blockquote></li>
<li><blockquote>
<p>Clarify that the configuration of LEDI IV is covered in the LEDI IV User Manual (parameter set ups, etc.)</p>
</blockquote></li>
<li><blockquote>
<p>Add HDI*1*6 must be installed prior to the HDI*1.0*7 patch, per Software Quality Assurance (SQA)</p>
</blockquote></li>
<li><blockquote>
<p>Add the message and process that displays after HDI*1.0*7 is installed</p>
</blockquote></li>
<li><blockquote>
<p>Update screen capture to reflect the inclusion of the HDI*1.0*7 in to the installation of LEDI IV</p>
</blockquote></li>
<li><blockquote>
<p>Add the mail group and option that get installed with the HDI*1.0*7 portion of this patch when there are exceptions</p>
</blockquote></li>
<li><blockquote>
<p>Add the secured FTP process with passwords that will be used for accessing both the LEDI IV and SNOMED CT files</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2/27/12</td>
<td>1.4</td>
<td><ul>
<li><blockquote>
<p>Add the DNS IP address for the FTP server per <mark>REDACTED</mark></p>
</blockquote></li>
<li><blockquote>
<p>Remove the Username and case sensitive password for the FTP server since LEDI IV will be a phased rollout; the Username and password will be provided for each site when they implement</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/28/12</td>
<td>1.5</td>
<td>Modify DNS IP address to LEDI.MED.VA.GOV for the FTP server per <mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2/29/12</td>
<td>1.6</td>
<td><p>Minor modifications:</p>
<ul>
<li><p>File 63 Remediation message only displays if there is an error</p></li>
<li><p>“Associated Patches” change to “LEDI IV”</p></li>
<li><p>Section 3.2.1.a. – remove the version number next to LEDI IV</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/19/12</td>
<td>1.6</td>
<td>Remove the word “BETA” from the title and footers</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>3/28/12</td>
<td>1.6</td>
<td><ul>
<li><p>Add the word “Note” to the front of the messages contained within the cloud diagrams on pages 15, 23 and 32 for 508 compliance</p></li>
<li><p>Align the cloud diagrams more closely to the text to which they related for 508 compliance</p></li>
<li><p>Bold the text messages that were highlighted in yellow for 508 compliance</p></li>
<li><p>Update footers to show March instead of February</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>4/27/12</td>
<td>1.7</td>
<td>Add Patch LR*5.2*413 as a pre-installation requirement</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 2012</td>
<td>1.8</td>
<td><ul>
<li><p>Modify the File 63 Remediation so that the tool analyzes and reports, but does NOT repair database issues</p></li>
<li><p>Change the File 63 Remediation process to run once per month, not nightly</p></li>
<li><p>Specify that the LSRP Installation Manual will be created and sent at a future date TBD</p></li>
<li><p>Move the post-installation step by which the LIM adds mycobacterium data to file #62.06 to the User Manual</p></li>
<li><p>Remove LR*5.2*350 from the list of required pre-installation patches</p></li>
<li><p>Add in a brief uninstall section</p></li>
<li><p>Add the LEDI IV installation can overwrite local customization to the LAB package; provide steps to prevent problems post File 63 Remediation</p></li>
<li><p>Modify the error message logic for entering SNOMED CT codes</p></li>
<li><p>Add patch LR LR*5.2*415 as a requirement for installing LEDI IV patch 20.6</p></li>
<li><p>Review with the LEDI IV Development Team; make updates</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>July 2012</td>
<td>1.9</td>
<td><p>Post meeting input from <mark>REDACTED</mark>:</p>
<ul>
<li><p>Remove Section 3.2.8, SNOMED CT Mail Messages and insert a note instead</p></li>
</ul>
<p>Post meeting input from <mark>REDACTED</mark>:</p>
<ul>
<li><p>Update the wording in the File 63 Remediation section</p></li>
<li><p>Form and style updates</p></li>
<li><p>Add more detail on what LEDI III Manual references</p></li>
<li><p>Reformat Sections 3.2.1 to 3.2.4</p></li>
<li><p>Remove all Note symbols to ensure consistency</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 2012</td>
<td>2.0</td>
<td><ul>
<li><p>Enter the required patch list from Development; six patches added to the list</p></li>
<li><p>Add clarification to the SNOMED CT Messages section per CLIN 4 review</p></li>
<li><p>Remove two patches from the required patch list</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>September 2012</td>
<td>2.1</td>
<td><ul>
<li><p>Remove all references to LSRP in the body of the document, including the screen captures</p></li>
<li><p>Replace “LSRP” with “Lab System”</p></li>
<li><p>Replace the LSRPUSER in the screen captures with “LEDIUSER”</p></li>
<li><p>Add Post-Install step to allow user at each site to edit the .01 field for Files 61, 61.2 and 62</p></li>
<li><p>Add a deletion step per Standards and Terminology Service (STS) input at the end of Section 3.2.4.2 Run KIDS Build</p></li>
<li><p>Add the TCP/IP communication protocol section for the pre-install portion</p></li>
</ul>
<p>Updates per <mark>REDACTED</mark>:</p>
<ul>
<li><p>Remove the last line about “334 messages” from the Figure 10 screen capture</p></li>
<li><p>Insert the word “NOTE” just above Figure 11</p></li>
</ul>
<p>Per <mark>REDACTED</mark>:</p>
<ul>
<li><p>Replace numerous references to Lab System with “future LEDI patch” since the future LEDI patch will include AP/MICRO and LOINC</p></li>
<li><p>Reiterate the SP, CY and EM tests are to be included in the lab test set ups, depending on the accession areas used by the site</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/5/12</td>
<td>2.2</td>
<td>Remove hyperlink to VA Intranet site for the LSRP glossary; LSRP no longer exists</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>9/10/12</td>
<td>2.3</td>
<td><ul>
<li><p>Add reference to the LEDI IV FAQ SharePoint</p></li>
<li><p>Modify the AP Collection Sample view, per CLIN 4 Input</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/12/12</td>
<td>2.4</td>
<td>Add the manual running of the File 63 Remediation for both CHEM and MICRO per input from CLIN 4</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>9/17/12</td>
<td>2.5</td>
<td>Add descriptive text by the screen captures that have “dialogue bubbles” to ensure 508 compliance</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/10/13</td>
<td>2.5</td>
<td>Based on input from the field, remove the following from page 39: “a.) Compare the ERROR LOG file (#3.075) to the initial snapshot of the file in Section 4.2.3.”</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/14/13</td>
<td>2.6</td>
<td>Add uninstall steps to Section 3.2.9, Step 3 for the LEDI IV Update patch; the LEDI IV Update patch numbers are: LR*5.2*427 and LA*5.2*80</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/16/13</td>
<td>2.6</td>
<td><p>Make document 508 compliant as follows:</p>
<ul>
<li><p>Add “Editor Notes” to allow the visually-impaired to see special hints and tips on the screens captures</p></li>
<li><p>Add screen tips to the web links identified as warning markers by the 508 Compliance Checker</p></li>
<li><p>Ensure bookmarks at the left top corner of each table</p></li>
<li><p>Remove minus symbols from the Table of Contents</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/14/13</td>
<td>2.6</td>
<td>Final review</td>
<td>EES</td>
</tr>
</tbody>
</table>
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose](#purpose)
  - [Definitions, Acronyms, and Abbreviations](#definitions-acronyms-and-abbreviations)
- [Pre-installation Considerations](#pre-installation-considerations)
  - [Associated Patches](#associated-patches)
  - [## AP Collection Sample and Laboratory Test Set Up](#ap-collection-sample-and-laboratory-test-set-up)
  - [TCP/IP Communication Protocol](#tcpip-communication-protocol)
  - [Requirements](#requirements)
    - [Test Account](#test-account)
    - [Staffing Requirements](#staffing-requirements)
    - [Coordination Requirements](#coordination-requirements)
    - [User Interface](#user-interface)
    - [Communications Interfaces](#communications-interfaces)
    - [Hardware Platform](#hardware-platform)
    - [Hardware Interfaces](#hardware-interfaces)
    - [LEDI IV Equipment Requirements](#ledi-iv-equipment-requirements)
    - [Shipping Configuration](#shipping-configuration)
    - [Install Can Overwrite Custom Changes to Lab Software](#install-can-overwrite-custom-changes-to-lab-software)
- [Load and Install LEDI IV Patches](#load-and-install-ledi-iv-patches)
  - [Allocate ZTMQ Security Key](#allocate-ztmq-security-key)
  - [Retrieve and Install LEDI IV Patches](#retrieve-and-install-ledi-iv-patches)
    - [Obtain Software and Documentation](#obtain-software-and-documentation)
    - [Shut Down Lab (LA) Related HL7 Interfaces](#shut-down-lab-la-related-hl7-interfaces)
    - [Load and Configure the LEDI IV Patches](#load-and-configure-the-ledi-iv-patches)
    - [Install LEDI IV Combined Build](#install-ledi-iv-combined-build)
    - [File 63 Remediation](#file-63-remediation)
    - [Restart the Lab HL7 Logical Links Shutdown Above](#restart-the-lab-hl7-logical-links-shutdown-above)
    - [Add members to the VistA LAB MAPPING Mail Group](#add-members-to-the-vista-lab-mapping-mail-group)
    - [Perform SNOMED CT Upload and Mapping](#perform-snomed-ct-upload-and-mapping)
    - [Post-Installation Steps to Perform](#post-installation-steps-to-perform)
- [File 63 Remediation Tool](#file-63-remediation-tool)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Laboratory Electronic Data Interchange (LEDI) IV introduces enhancements to the bi-directional interface that allows Department of Veterans Affairs (VA) laboratories to communicate with other VA facilities, Commercial Reference Laboratories, and Department of Defense (DoD) labs, and sets the foundation for future communication of Anatomic Pathology (AP) and Microbiology (Micro) orders and results with a future LEDI patch.

NOTE 1: The functionality to electronically transmit AP orders and AP and Micro results are not being made available with this patch. A future LEDI patch will allow for this functionality.

NOTE 2: The LEDI IV software is released as a multi-package host build that includes the following builds: HDI\*1.0\*7, LR\*5.2\*350, and LA\*5.2\*74.

The software has the capacity and features necessary for sharing secure, encrypted laboratory data between VA to VA, VA to Commercial Reference Laboratories, VA to DoD Labs, and future VA to the Lab System. The LEDI IV software is an extension of the LEDI III software.

For Laboratory System:

LEDI IV software enhances the general LED III functionality.

It will support the sending and receiving of Micro and AP orders and results between a Lab System and the associated VistA database with the future release of the Lab System.

> **NOTE:** A future LEDI patch that will be released to the field prior to the Laboratory System will also allow for MICRO and AP for the following connections:

- For VA-to-VA Interfaces:

> LEDI IV enhances the general LEDI III functionality.

- For VA to Commercial Reference LAB:

> LEDI IV enhances the general LEDI III functionality.

- For VA to DoD LAB:

> LEDI IV enhances the general LEDI III functionality.

- File \#63 (Lab Data) Cleanup:
  - The software creates an automated tool to check the LAB DATA File (#63) for Data Dictionary issues. The tool checks for the following issues:
    - Errors that may have occurred when an antibiotic was added by the local site to the Organism Sub-field (#63.3) of the LAB DATA file (#63).
    - Errors with the data names in the LABORATORY TEST file (#60), for tests in the Clinical Chemistry (Chemistry and Hematology) section. It checks the CHEM, HEM, TOX, RIA, SER, etc. Sub-file (#63.04) of the LAB DATA file (#63) looking for possible discrepancies in the Data Dictionary.
  - The File \#63 Remediation tool runs in analyze mode during the post installation of patch LR\*5.2\*350.
  - If there are errors, a report is generated in a mail message. It is strongly recommended if errors are reported, that the site log a Remedy ticket and not try to fix error. NOTE: If errors are found as part of the install, or as part of the LR NIGHTY run, the MAIL Message reads, “Contact the National Service Desk to request assistance from the Clin 4 Product Support team in resolving the following errors identified in the VistA Laboratory package.”

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this LEDI IV Installation Guide is designed to provide the Department of Veterans Affairs (VA), Veterans Health Administration (VHA), Information Resources Management Service (IRM), and the VistA Laboratory Information Manager (LIM) with the necessary technical information required to successfully install and implement LEDI IV. It provides a step-by-step guide for creating a working production environment with LEDI IV.

## Definitions, Acronyms, and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definitions applicable to LEDI IV are included in the Master Term Glossary found in the Project Notebook in the VA Office of Enterprise Development (OED) Technical Services Project Repository (TSPR).

Acronyms are listed at the following link: <http://vaww1.va.gov/acronyms>.

# Pre-installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several LAB patches that need verification of their installation prior to the installation of LEDI IV‘s combined build, which includes patches HDI\*1.0\*7, LA\*5.2\*74 and LR\*5.2\*350. The pre-installation instructions establish specific requirements that must be accomplished before installing the LEDI IV patches.

## Associated Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Associated patches that must be installed before LEDI IV:

|  LR\*5.2\*378 | XM\*8\*36    |
|---------------|--------------|
| LR\*5.2\*244  | LR\*5.2\*218 |
| LR\*5.2\*291  | HDI\*1.0\*6  |
| LR\*5.2\*313  | LR\*5.2\*300 |
| LR\*5.2\*330  | LR\*5.2\*323 |
| LR\*5.2\*339  | LR\*5.2\*337 |
| LR\*5.2\*360  | LR\*5.2\*347 |
| LR\*5.2\*362  | LR\*5.2\*361 |
| LR\*5.2\*352  | LR\*5.2\*348 |
| LR\*5.2\*364  | LR\*5.2\*358 |
| LR\*5.2\*384  | LR\*5.2\*363 |
| LR\*5.2\*372  | LR\*5.2\*375 |
| LR\*5.2\*388  | LR\*5.2\*386 |
| LR\*5.2\*315  | LR\*5.2\*365 |
| LR\*5.2\*397  | LR\*5.2\*392 |
| LR\*5.2\*308  | LR\*5.2\*395 |
| LR\*5.2\*334  | LR\*5.2\*402 |
| LR\*5.2\*368  | LR\*5.2\*295 |
| LR\*5.2\*406  | LR\*5.2\*356 |
| LEX\*2.0\*41  | LR\*5.2\*373 |
| LA\*5.2\*66   | LR\*5.2\*317 |
| LA\*5.2\*68   | LR\*5.2\*413 |
| LR\*5.2\*269  | LR\*5.2\*415 |

## ## AP Collection Sample and Laboratory Test Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Anatomic Pathology (SP, CY, and EM) login process (using the ‘Log-in, anat path \[LRAPLG\]’ option) has been modified with LEDI IV to require a selection from the COLLECTION SAMPLE file (#62), an entry from the TOPOGRAPHY FIELD file (#61), and a selection of an orderable test from the LABORATORY TEST file (#60), whether it is Surgical Pathology, Cytology and/or Electron Microscopy. Please see the next paragraph for more details.

To be able to select an appropriate Specimen Topography, Collection sample, and Laboratory test on AP Log-In, the LIM must create a Collection Sample File (#62) entry & a Laboratory Test File (#60) entry. At least one orderable Laboratory test is required for each subscript of: (SP) Surgical Pathology, (CY) Cytology, and Electron Microscopy (EM) as applicable for the active accession areas used by the site. Sites can create a choice of multiple tests as necessary for the scope of services offered by Anatomic Pathology. These entries should be created prior to the LEDI IV patch installation.

By creating these entries prior to the LEDI IV installation, the sites will not need to wait for these entries to be created before they can log in AP specimens. If these entries are not created before the LEDI IV installation, once LEDI IV is installed AP users will not be able to log-in specimens until this step is completed.

<span id="_Toc359228394" class="anchor"></span>Figure 1: Example Creating AP Collection Sample (#62) Entry

VA FileMan 22.0

Select OPTION: ENTER \<ENTER\> OR EDIT FILE ENTRIES 

INPUT TO WHAT FILE: COLLECTION SAMPLE// \<ENTER\>

EDIT WHICH FIELD: ALL// \<ENTER\>

Select COLLECTION SAMPLE NAME: AP SPECIMEN \<ENTER\>

  Are you adding 'AP SPECIMEN' as a new COLLECTION SAMPLE (the 72ND)? No// Y \<ENTER\> (Yes)

   COLLECTION SAMPLE DEFAULT SPECIMEN: \<ENTER\>

   COLLECTION SAMPLE TUBE TOP COLOR: \<ENTER\>

DEFAULT SPECIMEN: \<ENTER\>

TUBE TOP COLOR: \<ENTER\>

VOLUME LARGE: \<ENTER\>

VOLUME SMALL: \<ENTER\>

LAB SECTION: \<ENTER\>

CAN LAB COLLECT: N \<ENTER\> NO

Select SYNONYM: TISSUE SPECIMEN AP \<ENTER\>

Select SYNONYM: GYN SPECIMEN AP \<ENTER\>

Select SYNONYM: NONGYN SPECIMEN AP \<ENTER\>

Select SYNONYM: NON GYN SPECIMEN AP \<ENTER\>

Select SYNONYM: FNA SPECIMEN AP \<ENTER\>

Select SYNONYM: DERMPATH SPECIMEN AP \<ENTER\>

Select SYNONYM: NEUROPATH SPEC AP \<ENTER\>

Select SYNONYM: \<ENTER\>

Select ACCESSION AREA: \<ENTER\>

Select COLLECTION SAMPLE NAME: \<ENTER\>

<span id="_Toc359228395" class="anchor"></span>Figure 2: Example Creating AP Laboratory Tests (#60) Entry

VA FileMan 22.0

Select OPTION: ENTER \<ENTER\> OR EDIT FILE ENTRIES 

INPUT TO WHAT FILE: LABORATORY TEST// \<ENTER\>

EDIT WHICH FIELD: ALL// \<ENTER\>

Select LABORATORY TEST NAME: PATHOLOGY SURGICAL TISSUE REQUEST \<ENTER\>

  Are you adding 'PATHOLOGY SURGICAL TISSUE REQUEST' as

    a new LABORATORY TEST (the 1231ST)? No// Y \<ENTER\> (Yes)

   LABORATORY TEST SUBSCRIPT: SURG \<ENTER\> SURGICAL PATHOLOGY

   LABORATORY TEST HIGHEST URGENCY ALLOWED: ROUTINE \<ENTER\>

   LABORATORY TEST PRINT NAME: TISS EX \<ENTER\>

   LABORATORY TEST DATA NAME: \<ENTER\>

TEST COST: \<ENTER\>

Select SYNONYM: PATHOLOGY TISSUE EXAM \<ENTER\> *Editor Note: Synonyms are optional and may vary by site.*

Select SYNONYM: TISSUE REQUEST SURGICAL PATHOLOGY \<ENTER\>

Select SYNONYM: SURGICAL PATHOLOGY TISSUE EXAM \<ENTER\>

Select SYNONYM: \<ENTER\>

TYPE: OUTPUT \<ENTER\> *Editor Note: Configure AP Tests with the Type field set to “OUTPUT”.*

SUBSCRIPT: SURGICAL PATHOLOGY// \<ENTER\>

LOCATION (DATA NAME): \<ENTER\>

Select INSTITUTION: LEDIA \<ENTER\>              980 *Editor Note: Include all institutions (along with CBOCs)that can place this AP order.*

  ACCESSION AREA: SURGICAL PATHOLOGY \<ENTER\>

UNIQUE ACCESSION \#: \<ENTER\>

UNIQUE COLLECTION SAMPLE: Y \<ENTER\> YES

LAB COLLECTION SAMPLE: \<ENTER\>

REQUIRED TEST: \<ENTER\>

PROCEDURE (SNOMED): \<ENTER\>

\*QUICK INDEX: \<ENTER\>

EXTRA LABELS: \<ENTER\>

HIGHEST URGENCY ALLOWED: ROUTINE// \<ENTER\>

FORCED URGENCY: \<ENTER\>

PRINT NAME: TISS EX// \<ENTER\> *Editor Note: PRINT NAME may vary by site.*

Reserved: \<ENTER\>

PRINT CODE: \<ENTER\>

PRETTY PRINT ENTRY: \<ENTER\>

PRETTY PRINT ROUTINE: \<ENTER\>

PRINT ORDER: \<ENTER\>

NATIONAL VA LAB CODE: Surgical Pathology Tissue Exam \<ENTER\>      93940.0000

RESULT NLT CODE: \<ENTER\>

CATALOG ITEM: \<ENTER\>

EDIT CODE: \<ENTER\>

\*BATCH DATA CODE: \<ENTER\>

EXECUTE ON DATA REVIEW: \<ENTER\>

Select SITE/SPECIMEN: \<ENTER\>

GENERAL PROCESSING INST.: \<ENTER\>

  1\>

Select LAB TEST: \<ENTER\>

Select COLLECTION SAMPLE: AP SPECIMEN \<ENTER\>          

  FORM NAME/NUMBER: \<ENTER\>

  MIN VOL (in mls.): \<ENTER\>

  MAX. ORDER FREQ.: \<ENTER\>

  SINGLE DAY MAX ORDER FREQ: \<ENTER\>

  WARD REMARKS: \<ENTER\>

  1\>

  LAB PROCESSING INSTRUCTIONS : \<ENTER\>

  1\>

  REQUIRED COMMENT: \<ENTER\>

  Select SAMPLE WKLD CODE: \<ENTER\>

GENERAL WARD INSTRUCTIONS: \<ENTER\>

  1\>

REQUIRED COMMENT: \<ENTER\>

DATA NAME: \<ENTER\>

CULTURE ID PREFIX: \<ENTER\>

Select VERIFY WKLD CODE: \<ENTER\>

Select ACCESSION WKLD CODE: \<ENTER\>

\*ASK AMIS/CAP CODES: \<ENTER\>

COMBINE TEST DURING ORDER: \<ENTER\>

CIS TEST CODE: \<ENTER\>

Select SITE NOTES DATE: \<ENTER\>

DEFAULT SITE/SPECIMEN CPT: \<ENTER\>

HCPCS CODE: \<ENTER\>

AMA COMPLIANT/BILLABLE PANEL: \<ENTER\>

Select LABORATORY TEST NAME: CYTOLOGY REQUEST \<ENTER\>

  Are you adding 'CYTOLOGY REQUEST' as a new LABORATORY TEST (the 1232ND)? No// Y \<ENTER\> (Yes)

   LABORATORY TEST SUBSCRIPT: CYT \<ENTER\> CYTOLOGY

   LABORATORY TEST HIGHEST URGENCY ALLOWED: ROUTINE \<ENTER\>

   LABORATORY TEST PRINT NAME: CY EXAM \<ENTER\>

   LABORATORY TEST DATA NAME: \<ENTER\>

TEST COST: \<ENTER\>

Select SYNONYM: CYTOLOGY EXAM \<ENTER\>

Select SYNONYM: \<ENTER\>

TYPE: OUTPUT \<ENTER\>

SUBSCRIPT: CYTOLOGY// \<ENTER\>

LOCATION (DATA NAME): \<ENTER\>

Select INSTITUTION: LEDIA \<ENTER\>                   980 

  ACCESSION AREA: CYTOPATHOLOGY \<ENTER\>

UNIQUE ACCESSION \#: \<ENTER\>

UNIQUE COLLECTION SAMPLE: YE \<ENTER\> YES

LAB COLLECTION SAMPLE: \<ENTER\>

REQUIRED TEST: Y \<ENTER\> YES

PROCEDURE (SNOMED): \<ENTER\>

\*QUICK INDEX: \<ENTER\>

EXTRA LABELS: \<ENTER\>

HIGHEST URGENCY ALLOWED: ROUTINE// \<ENTER\>

FORCED URGENCY: \<ENTER\>

PRINT NAME: CY EXAM// \<ENTER\>

Reserved: \<ENTER\>

PRINT CODE: \<ENTER\>

PRETTY PRINT ENTRY: \<ENTER\>

PRETTY PRINT ROUTINE: \<ENTER\>

PRINT ORDER: \<ENTER\>

NATIONAL VA LAB CODE: Report Cytology \<ENTER\>      88593.0000

RESULT NLT CODE: \<ENTER\>

CATALOG ITEM: \<ENTER\>

EDIT CODE: \<ENTER\>

\*BATCH DATA CODE: \<ENTER\>

EXECUTE ON DATA REVIEW: \<ENTER\>

Select SITE/SPECIMEN: \<ENTER\>

GENERAL PROCESSING INST.: \<ENTER\>

  1\>

Select LAB TEST: \<ENTER\>

Select COLLECTION SAMPLE: AP SPECIMEN \<ENTER\>          

  FORM NAME/NUMBER: \<ENTER\>

  MIN VOL (in mls.): \<ENTER\>

  MAX. ORDER FREQ.: \<ENTER\>

  SINGLE DAY MAX ORDER FREQ: \<ENTER\>

  WARD REMARKS: \<ENTER\>

  1\>

  LAB PROCESSING INSTRUCTIONS : \<ENTER\>

  1\>

  REQUIRED COMMENT: \<ENTER\>

  Select SAMPLE WKLD CODE: \<ENTER\>

GENERAL WARD INSTRUCTIONS: \<ENTER\>

  1\>

REQUIRED COMMENT: \<ENTER\>

DATA NAME: \<ENTER\>

CULTURE ID PREFIX: \<ENTER\>

Select VERIFY WKLD CODE: \<ENTER\>

Select ACCESSION WKLD CODE: \<ENTER\>

\*ASK AMIS/CAP CODES: \<ENTER\>

COMBINE TEST DURING ORDER: \<ENTER\>

CIS TEST CODE: \<ENTER\>

Select SITE NOTES DATE: \<ENTER\>

DEFAULT SITE/SPECIMEN CPT: \<ENTER\>

HCPCS CODE: \<ENTER\>

AMA COMPLIANT/BILLABLE PANEL: \<ENTER\>

Select LABORATORY TEST NAME: \<ENTER\>

NOTE 1: The Select SYNONYM prompts are optional and may vary by site.

NOTE 2: Next to the TYPE prompt for AP tests, enter OUTPUT to configure the test.

NOTE 3: Next to the Select INSTITUTION prompt for AP tests, Include all institutions (along with all CBOCs) that can place this AP order.

NOTE 4: Print Name may vary by site, next to that prompt.

## TCP/IP Communication Protocol 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The functionality to use the TCP/IP protocol as a communication protocol for the transmission of LEDI HL7 messages was released in LEDI II. Sites that are still using the legacy MailMan protocol for LEDI messaging should switch to TCP/IP before the installation of the LEDI IV patch.

To convert from MailMan to the TCP/IP communication protocol on existing LEDI interfaces between VA facilities, both sites should use the LEDI Setup option to select TCP as the communication protocol. This switch should be coordinated and occur at the same time at both facilities. The HL package will encounter difficulties in transmitting and processing messages when the sender and receiver are using different communication protocols. Conversion should occur when the affected LA7V\* HL7 messaging queues for both facilities have no messages awaiting transmission.

## Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Test Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that the VistA LEDI IV software be installed into a test account before installing into a live production account.. The test and production accounts must include all required software versions and patches to ensure a successful test installation of the LEDI IV patches HDI\*1.0\*7, LA\*5.2\*74 and LR\*5.2\*350.

### Staffing Requirements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Information Resource Management (IRM) staff is required for software installation, including:

> 1\. Installing the LEDI IV bundle (HDI\*1.0\*7, LA\*5.2\*74 and LR\*5.2\*350).

> 2\. Establishing mail groups and menu assignments.

> 3\. Loading the SNOMED CT mapping file.

#### LIM staff is needed for any software configurations, including:

1.  Setting up the AP Collection Sample and Test.
2.  Adding existing mycobacterium drugs to the Antimicrobial Susceptibility File.
3.  Editing Package level Parameters if needed.

### Coordination Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to install, the IRM and LIM staff of the Collecting and Host facilities must coordinate the implementation of the LEDI IV setup. (For example, ensure that each site’s shipping configurations match.)

NOTE 1: The LEDI IV configuration process must be performed in the sequence specified in the LEDI IV User Manual.

NOTE 2: The actual usage of the Collecting and Host facilities to send and receive AP and MICRO electronic orders and results will be covered in a separate installation manual to be provided with a future LEDI patch at a time to be determined.

### User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV is a patch that runs on the VistA Legacy Lab “roll and scroll” interface.

### Communications Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA LEDI IV software application has no communications interfaces.

### Hardware Platform

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA LEDI IV software application operates on the current VA computer hardware systems.

### Hardware Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no hardware interfaces.

### LEDI IV Equipment Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To realize the maximum benefit from the VistA LEDI IV software functionality, barcode printers, barcode accession labels, and scanners are required for accessioning patient specimens. The manual accessioning method is intended as a backup procedure for accessioning patient specimens.

> **NOTE:** Using the manual accessioning method results in significant risk of transcription errors and increased accessioning time.

### Shipping Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM must ensure that the collection and performing sites have their shipping configurations correct prior to the installation of LEDI IV. LEDI IV has stricter checks than LEDI III when checking for a matching test/specimen combination on the performing lab’s shipping configuration. To prevent Application Error (AE) transmission errors after LEDI IV is installed at a performing Lab’s site, the collecting sites should refer to the performing lab’s Electronic Catalog and ensure that their LABORATORY TEST file (#60) and LAB SHIPPING CONFIGURATION file (#62.9) for the performing lab’s LEDI test is consistent with the collection requirements contained in the catalog.

If the collecting lab is sending a specimen that the performing lab isn’t configured for, they will receive an AE/ transmission error after the performing lab installs LEDI IV. Updating their LABORATORY TEST file (#60) and/or LAB SHIPPING CONFIGURATION file (#62.9) will allow future orders to transmit properly.

Also, refer to the LEDI III Implementation and User Guide in the VistA Software Document Library (VDL) for setting up the host performing and collection facilities. (See link above in the Reference Materials section.)

### Install Can Overwrite Custom Changes to Lab Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the site has made any local modifications to the nationally-released Lab software, there is a possibility that the site’s custom changes could be over written by the LEDI IV install. For instance, if the site has done any local modifications as a joint DOD/VA facility and then installs LEDI IV, the custom changed software may behave differently. This can and has caused patient safety issues in the field until they were fixed.

Before installing LEDI IV, do a Checksum comparison. Make note of and back up any routines that have local modifications and save them off for potential future use. The site can then analyze the local modifications and determine how best to proceed.

# Load and Install LEDI IV Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how to obtain, load, and install LEDI IV patches (HDI\*1.0\*7, LR\*5.2\*350, and LA\*5.2\*74).

## Allocate ZTMQ Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to install LEDI IV patches in a VistA account, the installer needs to have the ZTMQ security key; otherwise, the installation aborts.

<span id="_Toc361644541" class="anchor"></span>Figure 3: List Users with Specific Keys

List users holding a certain key \[XQSHOKEY\]

Select Key Management Option: LIST users holding a certain key

Which key? ZTMQ

Current holders of the key ZTMQ

LEDIUSER, ONE

LEDIUSER, TWO

LEDIUSER, THREE

LEDIUSER, FOUR

LEDIUSER, FIVE

LEDIUSER, SIX

LEDIUSER, SEVEN

LEDIUSER, EIGHT

To allocate the ZTMQ security key to a user, do the following steps shown below:

> **NOTE:** If user already holds ZTMQ security key, the system displays the “Person already holds key” message.

<span id="_Toc361644542" class="anchor"></span>Figure 4: Allocating the ZTMQ Security Key

Select Systems Manager Menu Option: menu \<Enter\> Management

Edit options

Key Management ...

Secure Menu Delegation ...

Restrict Availability of Options

Option Access By User

List Options by Parents and Use

Fix Option File Pointers

Help Processor ...

OPED Screen-based Option Editor

Display Menus and Options ...

Edit a Protocol

Menu Rebuild Menu ...

Out-Of-Order Set Management ...

See if a User Has Access to a Particular Option

Show Users with a Selected primary Menu

Select Menu Management Option: key \<Enter\> Management

Allocation of Security Keys

De-allocation of Security Keys

Enter/Edit of Security Keys

All the Keys a User Needs

Change user's allocated keys to delegated keys

Delegate keys

Keys For a Given Menu Tree

List users holding a certain key

Remove delegated keys

Show the keys of a particular user

Select Key Management Option: allocation \<Enter\> of Security Keys

Allocate key: ZTMQ

Another key: \<Enter\>

Holder of key: LEDIUSER,ONE \<Enter\> FL OI&T STAFF m

Another holder: \<Enter

You've selected the following keys:

ZTMQ

You've selected the following holders:

LEDIUSER,ONE

You are allocating keys. Do you wish to proceed? YES// \<Enter\>

ZTMQ being assigned to:

LEDIUSER,ONE Person already holds key - no action taken

*Editor note: If user already holds ZTMQ security key, the system displays the “Personalready holds key” message.*

## Retrieve and Install LEDI IV Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HDI\*1.0\*7 patch will be installed first as part of the Host Build followed by the LR\*5.2\*350 & LA\*5.2\*74 patches.

### Obtain Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### LEDI IV Software and Documentation

> To control the implementation of the LEDI IV patch and related SNOMED CT files, a secured ftp server with passwords will be used. By using this ftp server and password combination, the Lab users will install and use LEDI IV on a controlled basis.

> The password-protected FTP server on Forum is shown below. User names and case-sensitive passwords will be issued by the Product Development Team to the particular lab sites involved in the phased rollout.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>FTP Server</th>
<th>LEDI.MED.VA.GOV</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>“Top-Level” Directory Name</td>
<td>[LEDI_IV]</td>
</tr>
<tr class="even">
<td><p>Subdirectory Name</p>
<p>(for SNOMED files)</p></td>
<td>[LEDI_IV.SNOMED_CT]</td>
</tr>
<tr class="odd">
<td><p>Subdirectory Name</p>
<p>(for software/manuals)</p></td>
<td>[LEDI_IV.SOFTWARE]</td>
</tr>
<tr class="even">
<td>Username</td>
<td>(Will be provided when a site installs LEDI IV)</td>
</tr>
<tr class="odd">
<td><p>Password</p>
<p>(case-sensitive)</p></td>
<td>(Will be provided when a site installs LEDI IV)</td>
</tr>
</tbody>
</table>

#### SMOMED CT Mapping File

> The SNOMED CT Mapping Files will be obtained from the same Secured FTP Server as the LEDI IV Build. See Section 3.2.1 1 above for details on the location of the FTP Server.

### Shut Down Lab (LA) Related HL7 Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Point of Care Option

> If the site is using the Lab Point of Care (POC) HL7 interface, the POC Logical Links (LA7POC\*) should be shut down before LEDI IV patch installation. Use the HL7 menu option Start/Stop Links \[HL START\] to shutdown these Logical Links if they are running.

> The corresponding COTS systems these logical links communicate with should have the analogous process(s) which they use to communicate with VistA shutdown or suspended to prevent/block any transmission to VistA Lab during the install. Use the respective vendor’s documentation for these systems to perform the corresponding function in the vendor’s system.

<span id="_Toc361644543" class="anchor"></span>Figure 5: Lab POC HL7 Menu Option Stat/Stop Links to Shutdown

Select HL7 Main Menu Option: ?

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer \<ENTER\> and Link Management Options

SM Systems Link Monitor

FL Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL \<ENTER\> Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: LA7POC1\<ENTER\>

The LLP was last started on MAR 01, 2011 09:18:50.

Okay to shut down this job? YES \<ENTER\>

The job for the LA7POC1 Lower Level Protocol will be shut down.

#### Universal Interface Option

> If the site is using the Lab Universal Interface (UI) HL7 interface, the UI Logical Links (LA7UI\*) should be shut down before LEDI IV patch installation. Use the HL7 menu option Start/Stop Links \[HL START\] to shutdown these Logical Links if they are running.

> The corresponding COTS systems these logical links communicate with should have the analogous process(s) which they use to communicate with VistA shutdown or suspended to prevent/block any transmission to VistA Lab during the install. Use the respective vendor’s documentation for these systems to perform the corresponding function in the vendor’s system.

> NOTE: The KIDS install will automatically shut down the Lab Universal Interface Auto Download process and restart after successful patch installation if running at the start of the install.

<span id="_Toc361644544" class="anchor"></span>Figure 6: Lab UI HL7 Menu Option Stat/Stop Links to Shutdown

> Select HL7 Main Menu Option: ?

> Event monitoring menu ...

> Systems Link Monitor

> Filer and Link Management Options ...

> Message Management Options ...

> Interface Developer Options ...

> Site Parameter Edit

> Select HL7 Main Menu Option: FILER \<Enter\> and Link Management Options

> SM Systems Link Monitor

> FL Monitor, Start, Stop Filers

> LM TCP Link Manager Start/Stop

> SA Stop All Messaging Background Processes

> RA Restart/Start All Links and Filers

> DF Default Filers Startup

> SL Start/Stop Links

> PI Ping (TCP Only)

> ED Link Edit

> ER Link Errors ...

> Select Filer and Link Management Options Option: SL \<Enter\> Start/Stop Links

> This option is used to launch the lower level protocol for the

> appropriate device. Please select the node with which you want

> to communicate

> Select HL LOGICAL LINK NODE: LA7UI1\<ENTER\>

> The LLP was last started on MAR 21, 2011 19:02:30.

> Okay to shut down this job? YES

> The job for the LA7UI1 Lower Level Protocol will be shut down.

#### LEDI HL7 Option

> If the site is using the Lab LEDI Interfaces (LEDI) HL7 interface, the LEDI Logical Links (LA7V\*) should be shut down before LEDI IV patch installation. Use the HL7 menu option Start/Stop Links \[HL START\] to shutdown these Logical Links if they are running.

> If this LEDI interface communicates with a local COTS system then the COTS systems which these logical links communicate with should have the analogous process(s) used to communicate with VistA shutdown or suspended. This shutdown or suspension prevents/blocks any transmissions to VistA Lab during the install. Use the respective vendor’s documentation for these systems to perform the corresponding function in the vendor’s system.

> NOTE: LEDI interfaces that are VA to VA and utilize standard VA logical links (VAxxx) should not be shut down as it will impact other VistA applications.

<span id="_Toc361644545" class="anchor"></span>Figure 7: Lab LEDI HL7 Menu Option Stat/Stop Links to Shutdown

> Select HL7 Main Menu Option: ?

> Event monitoring menu ...

> Systems Link Monitor

> Filer and Link Management Options ...

> Message Management Options ...

> Interface Developer Options ...

> Site Parameter Edit

> Select HL7 Main Menu Option: FILER \<Enter\> and Link Management Options

> SM Systems Link Monitor

> FL Monitor, Start, Stop Filers

> LM TCP Link Manager Start/Stop

> SA Stop All Messaging Background Processes

> RA Restart/Start All Links and Filers

> DF Default Filers Startup

> SL Start/Stop Links

> PI Ping (TCP Only)

> ED Link Edit

> ER Link Errors ...

> Select Filer and Link Management Options Option: SL \<Enter\> Start/Stop Links

> This option is used to launch the lower level protocol for the

> appropriate device. Please select the node with which you want

> to communicate

> Select HL LOGICAL LINK NODE: LA7V123\<ENTER\>

> The LLP was last started on MAR 21, 2011 19:02:30.

> Okay to shut down this job? YES

> The job for the LA7V123 Lower Level Protocol will be shut down.

### Load and Configure the LEDI IV Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LEDI IV is a multi-package build consisting of the following patches:

- HDI\*1.0\*7
- LR\*5.2\*350
- LA\*5.2\*74

Suggested time to install: non-peak requirement hours.

|                                                   |                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------|
| ![](la-5-2-74-lr-5-2-350-hdi-1-7-ldsi-ledi-iv-install-guide/003.png) | IMPORTANT: This patch MUST BE installed when Laboratory users are NOT on the system. |

Install Time – Approximately 60 minutes.

<span id="_Toc361644546" class="anchor"></span>Figure 8: Load and Configure the LEDI IV Patches

> Select KIDS OPTION: LOAD A DISTRIBUTION

> Enter a Host File: USER\$:\[TEMP\]LAB_LEDI_IV.KID

> KIDS Distribution saved on Mon DD, YYYY@hh:mm:ss

> Comment: HDI7, LR350, AND LA74

> This Distribution contains Transport Globals for the following Package(s):

> HDI\*1.0\*7

> LR\*5.2\*350

> LA\*5.2\*74

> Distribution OK!

> Want to Continue with Load? YES// \<Enter\>

> Loading Distribution...

> HDI\*1.0\*7

> Build LR\*5.2\*350 has an Environmental Check Routine

> Want to RUN the Environment Check Routine? YES// \<Enter\>

> LR\*5.2\*350

> Will first run the Environment Check Routine, LR350

> Sending transport global loaded alert to mail group G.LMI

> --- Environment is okay ---

> LA\*5.2\*74

> Will first run the Environment Check Routine, LA74

> Sending transport global loaded alert to mail group G.LMI

> --- Environment okay ---

> Use INSTALL NAME: HDI\*1.0\*7 to install this Distribution.

### Install LEDI IV Combined Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Enter Install Step Command

> From the Installation menu, you may elect to use the following options (when prompted for the INSTALL NAME, enter HDI\*1.0\*7):

1.  Backup a Transport Global – This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System – This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.). NOTE: Routines that previously were un patched may show an inappropriate comment that the patch list does not match. Below is a sample of a comment that might be displayed if a routine has never been patched previously:

> \*\*\* WARNING, your routine has different patches than the incoming routine \*\*\*

3.  Verify Checksums in Transport Global – This option will allow you to ensure the integrity of the routines that are in the transport global.

#### Run KIDS Build

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option ‘Install Package(s)’.

1)  Use Install Name HDI\*1.0\*7.
2)  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, choose NO.
3)  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//’, choose NO.
4)  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//’, choose NO.
5)  A message displays after HDI\*1.0\*7 is installed. The message reads, “Deleting invalid VUIDs entered for Lab set of code fields” followed by a list of VUIDs (Veterans Health Administration Unique Identifier)s. The VHA Unique ID (VUIDs) will be deleted from the  XTID VUID FOR SET OF CODES file (8985.1). This post-install process ensures that Lab sets of codes that were not assigned consistently (and/or erroneously), will not be messaged to the Health Data Repository.
6)  Once the patch installation steps have been completed, delete the routines: HDI1007A and HDI1007B.

> NOTE: DO NOT QUEUE THE INSTALLATION, because this installation may ask questions requiring responses and queuing will stop the installation.

<span id="_Toc361644547" class="anchor"></span>Figure 9: Installing the LEDI IV combined build (1 of 2)

Select KIDS OPTION: INSTALL \<Enter\> PACKAGE(S)

Select INSTALL NAME: HDI\*1.0\*7 \<Enter\> Loaded from Distribution 6/3/10@15:59:19

=\> HDI7, LR350, AND LA74 ;Created on *Mon DD, YYYY*@hh:mm:ss

This Distribution was loaded on Jun 03, 2010@15:59:19 with header of

HDI7, LR350, AND LA74 ;Created on Mon DD, YYYY@hh:mm:ss

It consisted of the following Install(s):

HDI\*1.0\*7 LR\*5.2\*350 LA\*5.2\*74

Checking Install for Package HDI\*1.0\*7

Install Questions for HDI\*1.0\*7

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'HDIS LAB EXCEPTIONS': LEDIUSER,ONE// LEDIUSER,TWO LEDIUSER,TWO (Initials) (User Description)

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<Enter\>

Checking Install for Package LR\*5.2\*350

Will first run the Environment Check Routine, LR350

Sending install started alert to mail group G.LMI

> **IMPORTANT:** Shutdown your POC COTS system's VistA link.

Continue (Yes/No/Ignore): YES// \<Enter\>

Disabling Option \[LRMENU\]

Disabling Option \[LA7 ADL SEND\]

Disabling Option \[LA DOWN\]

Disabling Option \[LA7 ADL START/STOP\]

Shutting down Lab Universal Interface Auto Download Job..........

Shutting down currently running Lab HL7 processes

Acquiring locks ...

Locks acquired.

N O T E: If you abort this installation

D RESTORE^LR350 from this console.

--- Environment is okay ---

Install Questions for LR\*5.2\*350

Incoming Files:

60 LABORATORY TEST (Partial Definition)

61 TOPOGRAPHY FIELD (Partial Definition)

61.2 ETIOLOGY FIELD (Partial Definition)

62 COLLECTION SAMPLE (Partial Definition)

62.06 ANTIMICROBIAL SUSCEPTIBILITY (Partial Definition)

63 LAB DATA (Partial Definition)

64 WKLD CODE (Partial Definition)

64.061 LAB ELECTRONIC CODES (including data)

I will OVERWRITE your data with mine.

64.062 LAB ELECTRONIC SUBTYPES (including data)

I will OVERWRITE your data with mine.

64.5 LAB REPORTS (Partial Definition)

69 LAB ORDER ENTRY (Partial Definition)

69.6 LAB PENDING ORDERS ENTRY

95.4 LAB MAPPING TRANSPORT

Incoming Mail Groups:

*Editor Note: Enter the name of the mail group coordinator (substitute it for the placeholder “LEDIUSER, ONE”). See next line.*

Enter the Coordinator for Mail Group 'LAB MAPPING': LEDIUSER,ONE// LEDIUSER,TWO LEDIUSER,TWO (Initials) (User Description)

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<Enter\>

Checking Install for Package LA\*5.2\*74

Will first run the Environment Check Routine, LA74

Sending install started alert to mail group G.LMI

--- Environment okay ---

Install Questions for LA\*5.2\*74

Incoming Files:

62.4 AUTO INSTRUMENT (Partial Definition)

62.47 LAB CODE MAPPING

62.48 LA7 MESSAGE PARAMETER (Partial Definition)

62.485 LA7 MESSAGE LOG BULLETINS (including data)

I will OVERWRITE your data with mine.

62.49 LA7 MESSAGE QUEUE

62.8 LAB SHIPPING MANIFEST (Partial Definition)

62.9 LAB SHIPPING CONFIGURATION (Partial Definition)

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'LAB MESSAGING': LEDIUSER,ONE// LEDIUSER,TWO LEDIUSER,TWO (Initials) (User Description)

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<Enter\>

Want KIDS to INHIBIT LOGONs during the install? NO// \<Enter\>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// No

Delay Install (Minutes): (0-60): 0// \<Enter\>

Install Started for HDI\*1.0\*7 :

Jun 03, 2010@16:00:20

Build Distribution Date: Nov 23, 2008

Installing Routines

Jun 03, 2010@16:00:33

Installing PACKAGE COMPONENTS:

Installing MAIL GROUP

Installing OPTION

Jun 03, 2010@16:00:39

Running Post-Install Routine: POST^HDI1007A

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~~

Post-Installation (POST^HDI1007A) will now be run

Deleting invalid VUIDs entered for Lab set of code fields.

File: XXXX Field: XXXX

Post-Installation ran to completion

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~~

Updating Routine file...

Updating KIDS files...

HDI\*1.0\*7 Installed.

Jun 03, 2010@16:00:48

NO Install Message sent

Install Started for LR\*5.2\*350 :

Jun 03, 2010@16:00:50

Build Distribution Date: Nov 23, 2008

Installing Routines:

Running Pre-Install Routine: PRE^LR350A

\*\*\* Pre install started \*\*\*

Purging field \#2 DD for file \#61 and file \#61.2

Purging DDs and data for files \#64.061, \#64.062, \#95.4

Deleting DD for Micro Audit subfile \#63.539

Deleting "AB" cross reference on COLLECTION SAMPLE field (#60.03,.01)

\*\*\* Pre install completed \*\*\*

Installing Data Dictionaries:

Jun 03, 2010@16:00:55

Installing Data: ...................................................

Jun 03, 2010@16:01:06

Installing PACKAGE COMPONENTS:

Installing HELP FRAME

Installing MAIL GROUP

Installing OPTION

Installing PARAMETER DEFINITION

Installing PARAMETER TEMPLATE

Jun 03, 2010@16:01:07

Running Post-Install Routine: POST^LR350

\*\*\* Post install started \*\*\*

\*\*\* Configuring mail group 'LAB MAPPING' \*\*\*

\*\*\* Tasking post-install check of MI Antibiotic Field Definitions in LAB DATA file \*\*\*

\*\*\* Task \#XXXXXXX created \*\*\*

\*\*\* Tasking post-install check of bad test names \*\*\*

\*\*\* Post install completed \*\*\*

Sending install completion alert to mail group G.LMI

Updating Routine file...

Updating KIDS files...

LR\*5.2\*350 Installed.

Jun 03, 2010@16:01:07

Not a production UCI

NO Install Message sent

Install Started for LA\*5.2\*74 :

Jun 03, 2010@16:01:07

Build Distribution Date: Nov 23, 2008

Installing Routines

Jun 03, 2010@16:01:08

Running Pre-Install Routine: PRE^LA74

\*\*\* Pre install started \*\*\*

Checking for local codes in \#62.47

0 local codes found in \#62.47

Deleting File \#62.47 data and DD

Purging DD for file \#62.49

\*\*\* Pre install completed \*\*\*

Installing Data Dictionaries:

Jun 03, 2010@16:01:08

Installing Data:

Jun 03, 2010@16:01:08

Installing PACKAGE COMPONENTS:

Installing HELP FRAME

Installing MAIL GROUP

Installing OPTION

Installing PARAMETER DEFINITION

Installing PARAMETER TEMPLATE

Jun 03, 2010@16:01:09

Running Post-Install Routine: POST^LA74

\*\*\* Post install started \*\*\*

USER CLASS update for Lab application proxy user:

User LRLAB,HL okay.

User LRLAB,POC okay.

User LRLAB,TASKMAN okay.

Adding 1732 records to File \#62.47

Restoring 0 local codes to \#62.47

\*\*\* Post install completed \*\*\*

Sending install completion alert to mail group G.LMI

\* \* \* Releasing system \* \* \*

Released lock on ^LAHM(62.49,"HL7 PROCESS")

Released lock on ^LAHM(62.48,"Z")

Enabling Option \[LA7 ADL START/STOP\]

Enabling Option \[LA DOWN\]

Enabling Option \[LA7 ADL SEND\]

Enabling Option \[LRMENU\]

Restarting Lab Universal Interface Auto Download Job.

Restart your POC COTS' VistA link:

Updating Routine file...

Updating KIDS files...

LA\*5.2\*74 Installed.

Jun 03, 2010@16:01:26

NO Install Message sent

Install Completed

> NOTE: The HDI\*1.0\*7 patch has a Mail Group and Option that get installed with the patch. The MAIL GROUP is HDIS LAB EXCEPTIONS. The new OPTION installed with the HDI\*1.0\*7 portion of the patch is HDIS-LAB-EXCEPTION-SERVER.

### File 63 Remediation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File 63 Remediation Tools run automatically after successful completion of installation of the LR\*5.2\*350. The two File 63 Remediation Tools will analyze, identify, and report on the data dictionary configuration errors identified in the VistA Laboratory Package LAB DATA File (#63). These errors were likely introduced when users at the sites used FileMan to create fields to store test data that did not adhere to instructions or did not use the approved laboratory options. These tools will analyze fields that store:

- Tool \#1: Antibiotic susceptibilities, associated interpretations and display screens.
- Tool \#2: Chemistry/Hematology laboratory results.

Upon completion, the File \#63 remediation tool will send two emails to the LMI mail group and the person installing the patch during the KIDS post-install.

The MailMan message sent by File 63 Remediation Tool when errors are found post-KIDS Install will start with “Contact the National Service Desk to request assistance from the Clin 4 Product Support team in resolving the following errors identified in the VistA Laboratory package.”

Examples of MailMan messages sent by File 63 Remediation Tool when there are no errors:

> Subj: LAB DATA file (#63) Microbiology Antibiotic Fields Cleanup  \[#2544774\] 11/

> 02/11@15:28  12 lines

> From: LAB, USER ONE  In 'IN' basket.   Page 1

> -------------------------------------------------------------------------------

> The LAB DATA file (#63) cleanup process has completed.

> Tool run in ANALYZE/REPAIR MODE for: Dallas Office of Information Field Office -

> Lab Development (FS.FO-ALBANY.MED.VA.GOV).

> This process checked the Organism Sub-field (#63.3) of the LAB DATA file (#63)

> to locate potential Data Dictionary discrepancies related to the definition and

> setup of fields for reporting antibiotic sensitivities.

> The following report lists any discrepancies found:

> -------------------------------------------------------------------------------

> \*\*\* NO DISCREPANCIES WERE FOUND IN FILE (#63). \*\*\*

> Enter message action (in IN basket): Ignore//

> IN Basket Message: 4277//

> Subj: DATA DICTIONARY ^DD(63.04 CHECK REPORT Nov 02, 2011@15:29:01  \[#2544775\] 1

> 1/02/11@15:29  3 lines

> From: LAB, USER ONE  In 'IN' basket.   Page 1

> -------------------------------------------------------------------------------

> Dallas Office of Information Field Office - Lab Development (FS.FO-ALBANY.MED.VA

> .GOV)      Nov 02, 2011

> \*\*\* NO ERRORS FOUND \*\*\*

> Enter message action (in IN basket): Ignore//

### Restart the Lab HL7 Logical Links Shutdown Above

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If the site is using the Lab Point of Care (POC) HL7 interface, and shut down the POC Logical links (LA7POCx) before LEDI IV patch installation, they should be restarted now. Use the HL menu option Start/Stop Links \[HL START\] to restart these Logical Links.

> The corresponding COTS systems these logical links communicate with should have the analogous process(s) which they use to communicate with VistA started to resume transmission to VistA Lab. Use the respective vendor’s documentation for these systems to perform the corresponding function in the vendor’s system.

<span id="_Toc361644548" class="anchor"></span>Figure 10: Lab POC HL7 Menu Option Stat/Stop Links to Restart

Select HL7 Main Menu Option: ?

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer \<ENTER\> and Link Management Options

SM Systems Link Monitor

FL Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL \<ENTER\> Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: LA7POC1\<ENTER\>

The LLP was last shutdown on MAY 13, 2011 09:03:14.

Job was queued as 413795.

2.  If the site is using the Lab Universal Interface (UI) HL7 interface, the UI Logical Links (LA7UI\*) should be restarted now that were shut down above. Use the HL7 menu option Start/Stop Links \[HL START\] to restart these Logical Links if they are running.

> The corresponding COTS systems these logical links communicate with should have the analogous process(s) which they use to communicate with VistA started to resume transmission to VistA Lab. Use the respective vendor’s documentation for these systems to perform the corresponding function in the vendor’s system

> NOTE: The KIDS install will automatically restart the Lab Universal Interface Auto Download process if running at the start of the install.

<span id="_Toc361644549" class="anchor"></span>Figure 11: Lab UI HL7 Menu Option Stat/Stop Links to Restart

Select HL7 Main Menu Option: ?

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer \<ENTER\> and Link Management Options

SM Systems Link Monitor

FL Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL \<ENTER\> Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: LA7UI1\<ENTER\>

The LLP was last shutdown on MAY 13, 2011 09:03:14.

Job was queued as 413795.

3.  If the site is using the Lab LEDI Interfaces (LEDI) HL7 interface, the LEDI Logical Links (LA7V\*) should be restarted now that were shut down above. Use the HL7 menu option Start/Stop Links \[HL START\] to restart these Logical Links if they are running.

> If this LEDI interface communicates with a local COTS system then start any analogous process(s) which they use to communicate with VistA to resume transmission to VistA Lab. Use the respective vendor’s documentation for these systems to perform the corresponding function in the vendor’s system

<span id="_Toc361644550" class="anchor"></span>Figure 12: Lab LEDI HL7 Menu Option Stat/Stop Links to Restart

Select HL7 Main Menu Option: ?

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Filer \<ENTER\> and Link Management Options

SM Systems Link Monitor

FL Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL \<ENTER\> Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: LA7V123\<ENTER\>

The LLP was last shutdown on MAY 13, 2011 09:03:14.

Job was queued as 413795.

### Add members to the VistA LAB MAPPING Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add members to the VistA LAB MAPPING mail group. This mail group is used for sending automated system messages to the recipients when certain fields of monitored files (#61, \#61.2, and \#62) are added and/or modified.

Example: When a NAME field (#.01) of ETIOLOGY FIELD file (#61.2) is created or modified, an alert is automatically generated and sent directly to the Standards & Terminology Services (STS) mail group on forum to notify them of the change. A separate message is also sent to the local Lab Mapping mail group notifying them of the change as well and containing the tracking information for the STS alert.

> **NOTE:** Make sure there is at least one VA employee included in the Lab Mapping mail group.

<span id="_Toc361644551" class="anchor"></span>Figure 13: Sample Lab Mapping Mail Group Properties

MAIL GROUP LIST DEC 17,2010 14:38 PAGE 1

---------------------------------------------------------------------------

NAME: LAB MAPPING TYPE: public

ALLOW SELF ENROLLMENT?: NO

REFERENCE COUNT: 2 LAST REFERENCED: DEC 17, 2010

COORDINATOR: LEDIUSER,ONE

MEMBER: LRUSER,ONE

MEMBER: LRUSER,TWO

MEMBER: LRUSER,THREE

ORGANIZER: LRUSER,ONE

### Perform SNOMED CT Upload and Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  After installing the LEDI IV patches, users must perform the Systemized Nomenclature of Medicine Clinical Terminology (SNOMED CT) upload and mapping.
2.  Obtain the SNOMED CT (SCT) mappings and term disposition text file using an FTP ASCII file transfer. See the download section above. This mapping is usually provided by Standards & Terminology Services (STS) after they have extracted and mapped the site's local terms to the appropriate SCT code. If no mapping is provided then a disposition is stored with the reason. A SCT mapping can also be provided as part of the mediation process that occurs when a new term is added either by the site or via an HL7 interface from an external laboratory which uses the new term.
3.  Verify the file format is formatted correctly. For example, the headers should appear as follows:

Format 1:

Station \#-File \#-IEN\|Entry Name\|SNOMED I\|SNOMED CT\|STS_EXCEPTION\|STS_EXCEPTION_REASON\|TRANSACTION NUMBER\|

4.  Place the file in a file directory or other designated location accessible from VistA when using the option in the next step.
5.  From the Test an Option Not in Your Menu option, select the Load SNOMED SCT Mapping option \[LA7S LOAD MAPPING SCT\] to load the SNOMED CT (SCT) mappings and term disposition text file into the target file entry. This option:
    1.  Prompts the user to specify the location of the file.
    2.  Loads the contents of the file into a temporary holding LAB MAPPING TRANSPORT file (#95.4).
    3.  Allows the user to apply the mappings to the target entries.
6.  Select the “Process SNOMED CT mappings directly” function to process the SNOMED CT mappings.

> NOTE 1: If there is a problem with the import of SNOMED CT mappings, you can resume the process by choosing option 2 – process previous loaded file:

> Load SNOMED SCT Mapping

> Select one of the following:

> 1 Load file

> 2 Process previous loaded file

> Enter response: 2//

> NOTE 2: Most SNOMED CT code mapping exceptions are caused for the following reasons:

- SNOMED CT code is inactive.
- Entry did not exist.
- Entry name in account did not match what was in the mapping file received from STS.

> NOTE 3: When an exception is generated during the processing of the SNOMED CT mapping file, an alert is generated and send to the STS team for resolution. The user does not need to take any action in regards to the exception, as the STS team will be notified via the alert, and if needed, the STS team will send the site an updated SCT mapping. In a production account, the alert is sent to the HDIS LAB EXCEPTIONS mail group on FORUM (users do not need to be added to this mail group since it is only referenced on the FORUM system). In a test account, the alert is sent to the user applying the mappings.

<span id="_Toc361644552" class="anchor"></span>Figure 14: SNOMED CT Upload—Process SNOMED CT Mappings Directly Option

Select OPTION NAME: LA7S LOAD MAPPING SCT \<Enter\> Load SNOMED SCT

HOST FILE DIRECTORY: USER\$:\[TEMP\]// \<Enter\> *Editor Note: You can enter a different directory if you have saved the mapping file in another location. Initially the option displays the PRIMARY HFS DIRECTORY specified in the KERNAL SYSTEM PARAMATERS file.*

Using filespec \*.TXT

Select FILE: 1// ??

1 HUNTINGTON_SCT_12-14-10.TXT;2

2 HUNT_CORRECT_3-31-11.TXT;1

3 LEDI_LEDI COTS_IP_PORT_CONFIGURATION.TXT;1

4 RELNOTES.TXT;3

5 WORKLOAD_TO_VISTA_201012.TXT;1

Select a file by number from the list

Select FILE: 1// 1 *Editor Note: Choose the file that contains the SNOMED CT mappings.*

Directory: USER\$:\[TEMP\]

File.....: HUNTINGTON_SCT_12-14-10.TXT;2

Loading file into TMP global

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

Processing file data and storing in file \#95.4

...SORRY, JUST A MOMENT PLEASE...

Records added: 13685

Select one of the following:

0 Quit - no action

1 Process SNOMED CT mappings directly

2 Task processing SNOMED CT mappings

Processing Action: 0// 1 \<Enter\> Process SNOMED CT mappings directly

Loading files with National SNOMED CT Codes

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Loading file \#61 \[TOPOGRAPHY FIELD\]

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.......

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent....

Lexicon SCT lookup error STS alert sent.......

Lexicon SCT lookup error STS alert sent..........

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent..................

Lexicon SCT lookup error STS alert sent.........

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent....................

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.....

Lexicon SCT lookup error STS alert sent.............

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.....

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.....................

Lexicon SCT lookup error STS alert sent.....

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent....

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent....

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.........

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent......

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent....

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent......

No such entry: File \#61 IEN:8828 STS alert sent.

No such entry: File \#61 IEN:8829 STS alert sent.

No such entry: File \#61 IEN:8830 STS alert sent...

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Loading file \#61.2 \[ ETIOLOGY FIELD \]

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.....

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent....

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent....

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent...

Names do not match: \[CLOSTRIDIUM DIFFICILE TOXIN A/B POSITIVE \< - \> CLOSTRIDIUM DIFFICILE TOXIN B DNA DETECTED\] STS alert sent.

Names do not match: \[CLOSTRIDIUM DIFFICILE TOXIN A/B NEGATIVE \< - \> CLOSTRIDIUM DIFFICILE TOXIN B DNA NOT DETECTED\] STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

No such entry: File \#61.2 IEN:7159319 STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent...

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

\*\*\*\*\*\*\*\*\* Loading file \#62 \[ COLLECTION SAMPLE \] \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.

Names do not match: \[AP SPECIMEN \< - \> AXILLA\] STS alert sent.

No such entry: File \#62 IEN:118 STS alert sent.

No such entry: File \#62 IEN:119 STS alert sent.

No such entry: File \#62 IEN:120 STS alert sent.

No such entry: File \#62 IEN:121 STS alert sent.

No such entry: File \#62 IEN:122 STS alert sent.

No such entry: File \#62 IEN:123 STS alert sent.

No such entry: File \#62 IEN:124 STS alert sent.

No such entry: File \#62 IEN:125 STS alert sent.

No such entry: File \#62 IEN:126 STS alert sent.

No such entry: File \#62 IEN:127 STS alert sent.

No such entry: File \#62 IEN:128 STS alert sent.

No such entry: File \#62 IEN:129 STS alert sent.

No such entry: File \#62 IEN:130 STS alert sent.

No such entry: File \#62 IEN:131 STS alert sent.

No such entry: File \#62 IEN:132 STS alert sent.

No such entry: File \#62 IEN:133 STS alert sent.

No such entry: File \#62 IEN:134 STS alert sent.

No such entry: File \#62 IEN:135 STS alert sent.

No such entry: File \#62 IEN:136 STS alert sent.

No such entry: File \#62 IEN:137 STS alert sent.

No such entry: File \#62 IEN:138 STS alert sent.

No such entry: File \#62 IEN:139 STS alert sent.

No such entry: File \#62 IEN:140 STS alert sent.

No such entry: File \#62 IEN:141 STS alert sent.

No such entry: File \#62 IEN:142 STS alert sent.

No such entry: File \#62 IEN:143 STS alert sent.

No such entry: File \#62 IEN:144 STS alert sent.

No such entry: File \#62 IEN:145 STS alert sent.

No such entry: File \#62 IEN:146 STS alert sent.

No such entry: File \#62 IEN:147 STS alert sent.

No such entry: File \#62 IEN:148 STS alert sent.

No such entry: File \#62 IEN:149 STS alert sent.

No such entry: File \#62 IEN:150 STS alert sent.

No such entry: File \#62 IEN:151 STS alert sent.

No such entry: File \#62 IEN:152 STS alert sent.

No such entry: File \#62 IEN:153 STS alert sent.

No such entry: File \#62 IEN:154 STS alert sent.

No such entry: File \#62 IEN:155 STS alert sent.

No such entry: File \#62 IEN:156 STS alert sent.

No such entry: File \#62 IEN:157 STS alert sent.

No such entry: File \#62 IEN:174 STS alert sent.

No such entry: File \#62 IEN:175 STS alert sent.

No such entry: File \#62 IEN:176 STS alert sent.

No such entry: File \#62 IEN:177 STS alert sent.

No such entry: File \#62 IEN:178 STS alert sent.

No such entry: File \#62 IEN:179 STS alert sent.

No such entry: File \#62 IEN:180 STS alert sent.

No such entry: File \#62 IEN:181 STS alert sent.

No such entry: File \#62 IEN:182 STS alert sent.

No such entry: File \#62 IEN:183 STS alert sent.

No such entry: File \#62 IEN:184 STS alert sent.

No such entry: File \#62 IEN:185 STS alert sent.

No such entry: File \#62 IEN:186 STS alert sent.

No such entry: File \#62 IEN:187 STS alert sent.

No such entry: File \#62 IEN:188 STS alert sent.

No such entry: File \#62 IEN:189 STS alert sent.

No such entry: File \#62 IEN:190 STS alert sent.

No such entry: File \#62 IEN:191 STS alert sent.

No such entry: File \#62 IEN:192 STS alert sent.

No such entry: File \#62 IEN:193 STS alert sent.

No such entry: File \#62 IEN:194 STS alert sent.

No such entry: File \#62 IEN:195 STS alert sent.

No such entry: File \#62 IEN:196 STS alert sent.

No such entry: File \#62 IEN:197 STS alert sent.

No such entry: File \#62 IEN:198 STS alert sent.

No such entry: File \#62 IEN:199 STS alert sent.

No such entry: File \#62 IEN:200 STS alert sent.

No such entry: File \#62 IEN:201 STS alert sent.

No such entry: File \#62 IEN:202 STS alert sent.

No such entry: File \#62 IEN:203 STS alert sent.

No such entry: File \#62 IEN:204 STS alert sent.

No such entry: File \#62 IEN:205 STS alert sent..

No such entry: File \#62 IEN:206 STS alert sent.

No such entry: File \#62 IEN:207 STS alert sent.

No such entry: File \#62 IEN:208 STS alert sent.

No such entry: File \#62 IEN:209 STS alert sent.

Lexicon SCT lookup error STS alert sent..

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

Lexicon SCT lookup error STS alert sent.

After processing the SNOMED CT mapping file, verify the SNOMED CT mappings were applied.

1.  Verify the SNOMED CT mappings were applied – Use VA FileMan's Inquire to File Entries option to view sample SNOMED CT entries. Figure 15 illustrates what an entry will look like post SNOMED CT mapping.

<span id="_Toc361644553" class="anchor"></span>Figure 15: SNOMED CT Upload—Sample Post Mapping Entry

Select VA FileMan Option: INQ \<Enter\> Inquire to File Entries

OUTPUT FROM WHAT FILE: 61 \<Enter\> TOPOGRAPHY FIELD (8585 entries)

Select TOPOGRAPHY FIELD NAME: SERUM

ANOTHER ONE: \<Enter\>

STANDARD CAPTIONED OUTPUT? Yes// \<Enter\> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// \<Enter\> - No record number (IEN), no Computed Fields

NAME: SERUM SNOMED CODE: 0X500

ABBREVIATION: S COLLECTION SAMPLE: SERUM

HL7 CODE: SER LEDI HL7: Serum

TIME ASPECT: POINT

SYNONYM: SERUM

SNOMED CT ID: 67922002 SCT CODE STATUS: PREFERRED TERMSCT TOP CONCEPT: SCT SubstanceSCT STATUS DATE: DEC 17, 2010@14:18:16 SCT STATUS CHANGE TO: PREFERRED TERMSCT STATUS USER: LEDIUSER,ONESCT COMMENT TEXT:File used to apply mapping and/or disposition: HUNTINGTON_SCT_12-14-10.TXT;3

Select TOPOGRAPHY FIELD NAME:

2.  Review any alerts:

    NOTE: A View Alert is generated and sent to the G.LAB MAPPING mail group when the SCT mapping has been triggered and another alert is sent when the task has completed.

<span id="_Toc361644554" class="anchor"></span>Figure 16: SNOMED CT Upload—Sample Alerts Generated

SNOMED CT mapping has been triggered from STS on Jan 10, 2011@16:39 SNOMED CT mapping has completed on Jan 10, 2011@16:44

Enter "VA to jump to VIEW ALERTS option

3.  NOTE: In the test account any exceptions generated during the SNOMED CT mapping will be sent to the person applying the mapping. These messages can be ignored.

<span id="_Toc361644555" class="anchor"></span>Figure 17: SNOMED CT Upload—Sample Exception Message Delivered Locally as it is Not a Production System

Subj: Lab Exception(s): 581-61-1527 \[#210312\] 01/10/11@16:39 53 lines

From: Data Standardization Toolset In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------

Transaction Number: 581-1-3110110.16395-61:1527 Exception Type Code: 1

Time Stamp: 3110110.16395

ID (Fac#-File#-IEN): 581-61-1527 SNOMED CT:

SNOMED CT Term: Mapping Exception:

Term Status:

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

begin 644 581-20110110-163950.XML M/#\]X;6P@=F5R\<VEO;CTB,2XP(B!E;F-O9&EN9STB=71F+3@B(#\\#0H\3&%B M7T5X8V5P=&EO;G,^#0H\3&%B7T5X8V5P=&EO;E\]\$871A/@T\*/\$%D;6EN:7-T M\<F%T:79E7T1A=&\$^#0H\17AC97!T:6\]N7U-T871I;VY?3G5M8F5R/C4X,3PO M17AC97!T:6\]N7U-T871I;VY?3G5M8F5R/@T\*/\$5X8V5P=&EO;E\]3=&%T:6\]N M7T1O;6%I;E\])4#Y(54Y4-2Y&3RU"05E024Y%4RY-140N5D\$N1T\]6/"\]%\>&-E

Enter RETURN to continue or '^' to exit: \<Enter\>

Subj: Lab Exception(s): 581-61-1527 \[#210312\] Page 2

M\<'1I;VY?4W1A=&EO;E\]\$;VUA:6Y?25 ^#0H\17AC97!T:6\]N7U-T871I;VY? M4WES=&5M7U1Y\<&4^5\$535#PO17AC97!T:6\]N7U-T871I;VY?4WES=&5M7U1Y M\<&4^#0H\17AC97!T:6\]N7U1Y\<&5?0V\]D93XQ/"\]%\>&-E\<'1I;VY?5'EP95\]# M;V1E/@T\*/\$5X8V5P=&EO;E\]4\<F%N\<V%C=&EO;E\].=6UB97(^-3@Q+3\$M,S\$Q M,#\$Q,"XQ-C,Y-2TV,3HQ-3(W/"\]%\>&-E\<'1I;VY?5')A;G-A8W1I;VY?3G5M M8F5R/@T\*/\$5X8V5P=&EO;E\]4:6UE7U-T86UP/C(P,3\$M,#\$M,3!4,38Z,SDZ M-3 M,#4P,#PO17AC97!T:6\]N7U1I;65?4W1A;7 ^#0H\3&%B7U!A8VMA9V5? M17AC97!T:6\]N7U1E\>'0^3&5X:6-O;B!30U0@;&\]O:W5P(&5R\<F\]R/"\],86)? M4&%C:V%G95\]%\>&-E\<'1I;VY?5&5X=#X-"CPO061M:6YI\<W1R871I=F5?1&%T M83X-"CQ,86)?1FEL95\]33D\]-141?1&%T83X-"CQ&86-I;&ET\>4YU;6)E\<E\]& M:6QE3G5M8F5R7TE%3CXU.#\$M-C\$M,34R-SPO1F%C:6QI='E.=6UB97)?1FEL M94YU;6)E\<E\])14X^#0H\16YT\<GE?3F%M93Y"3TY%(\$\]&(%-(3U5,1\$52/"\]% M;G1R\>5\].86UE/@T\*/%-.3TU%1%\])/E0M,3\$S,#\$\\U-.3TU%1%\])/@T\*/%95 M240O/@T\*/%-.3TU%1%\]#5"\\#0H\4TY/345\$7T-47U1E\<FTO/@T\*/\$UA\<'!I M;F=?17AC97!T:6\]N+SX-"CQ296QA=&5D7U-P96-I;65N+SX-"CQ296QA=&5D M7U-P96-I;65N7TE\$+SX-"CQ%\>'1R86-T7U9E\<G-I;VX^,2XR/"\]%\>'1R86-T M7U9E\<G-I;VX^#0H\5&5R;5\]3=&%T=7,O/@T\*/"\],86)?1FEL95\]33D\]-141? M1&%T83X-"CQ-87!P:6YG7T1A=&%?0F5I;F=?3&\]A9&5D/@T\*/\$UA\<'!I;F=? M1&%T85\]&86-I;&ET\>4YU;6)E\<E\]&:6QE3G5M8F5R7TE%3CXU.#\$M-C\$M,34R M-SPO36%P\<&EN9U\]\$871A7T9A8VEL:71Y3G5M8F5R7T9I;&5.=6UB97)?245.

M/@T\*/\$UA\<'!I;F=?1&%T85\]%;G1R\>5\].86UE/D)/3D4@3T8@4TA/54Q\$15(\\ M+TUA\<'!I;F=?1&%T85\]%;G1R\>5\].86UE/@T\*/\$UA\<'!I;F=?1&%T85\]33D\]- M141?23Y4+3\$Q,S Q/"\]-87!P:6YG7T1A=&%?4TY/345\$7TD^#0H\36%P\<&EN M9U\]\$871A7U-44U\]&=7)T:&5R7T%C=&EO;CXV,#@X,# P-3PO36%P\<&EN9U\]\$ M871A7U-44U\]&=7)T:&5R7T%C=&EO;CX-"CQ-87!P:6YG7T1A=&%?4U137U-# M5%\])1#XQ/"\]-87!P:6YG7T1A=&%?4U137U-#5%\])1#X-"CPO36%P\<&EN9U\]\$ M871A7T)E:6YG7TQO861E9#X-"CQ2969E\<F5N8V5?3&%B7T1A=&\$^#0H\4F5F M97)E;F-E7TQA8E\]4\>7!E7T-O9&4O/@T\*/%)E9F5R96YC95\],86)?4W1A=&EO M;E\].=6UB97(O/@T\*/%)E9F5R96YC95\],86)?3F%M92\\#0H\4F5F97)E;F-E M7TQA8E\]/0E@M,R\\#0H\4F5F97)E;F-E7TQA8E\]/0E@M-2\\#0H\\U)E9F5R M96YC95\],86)?1&%T83X-"CPO3&%B7T5X8V5P=&EO;E\]\$871A/@T\*/"\],86)? -17AC97!T:6\]N\<SX-"B @ \` end

enter message action (in IN basket): Ignore//

> Checkpoint: Check VistA Error Logs — This is a checkpoint step for VistA installers to verify the installation is progressing as expected up to this point:

1.  Check the VistA Error Trap for any issues.
2.  The LIM should check their VistA mail to see if any error messages were sent to the G.LMI mail group.

### Post-Installation Steps to Perform 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Create and Mail Lab Reports

> Patch LR\*5.2\*164 released the capability to transmit reports on specimens received from other VAMC laboratories via network mail. It released an option, ‘Create and Mail Lab Reports’ \[LRRMM TASK MAIL LAB REPORTS\], and provided instructions for how a Host site can customize it to automatically send back reports via network mail back to the Collecting Facilities. It required setting the variables LRRLROC (if using the ONELOC entry point) or LRRLST (if using the MANYLOC entry point).  

> If the location was another Institution, then only the first 15 characters of the Institution name was used. However, with LEDI IV <u>the first 20 characters</u> of the Institution name are required. After LEDI IV is installed, if the site is using this option, they must work with their IRM staff to modify the tasked option to use the first 20 characters of the Institution Name in order to ensure the reports continue to be generated.

<span id="_Toc361644556" class="anchor"></span>Figure 18: Create and Mail Lab Reports Option

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: OPTION//

Select OPTION NAME: LRRMM TASK MAIL LAB REPORTS Create and Mail Lab Reports

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// - No record number (IEN), no Computed

Fields

NAME: LRRMM TASK MAIL LAB REPORTS MENU TEXT: Create and Mail Lab Reports

TYPE: action CREATOR: PROVIDER,TWOHUNDREDNINETYSEVEN

E ACTION PRESENT: YES

DESCRIPTION: This option produces the interim reports for lab work from

other hospitals and sends it to a spool file. The reports are then taken from

the spool file and loaded into a mail message. Network mail transmits the

reports to the referring hospital.

ENTRY ACTION: S LRRLROC="SOUTHERN ARIZON",LRRSITE="TUCSON.VA.GOV" D ONELOC^LRR

MM SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: CREATE AND MAIL LAB REPORTS

Select OPTION NAME:

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: OPTION//

EDIT WHICH FIELD: ALL// ENTRY ACTION

THEN EDIT FIELD:

Select OPTION NAME: LRRMM TASK MAIL LAB REPORTS Create and Mail Lab Reports

ENTRY ACTION: S LRRLROC="SOUTHERN ARIZON",LRRSITE="TUCSON.VA.GOV" D ONELOC^LRRMM

Replace SOUTHERN ARIZON With SOUTHERN ARIZONA VA

Replace

S LRRLROC="SOUTHERN ARIZONA VA ",LRRSITE="TUCSON.VA.GOV" D ONELOC^LRRMM

Select OPTION NAME:

2.  Add Antibiotics

> The LIM should refer to the User Manual for instructions on how to add their existing mycobacterium antibiotics to the antimicrobial susceptibility file \# 62.06.

3.  Uninstall  
    > 

> Please enter a Remedy ticket and the Support Team will work with the sites as required should an uninstall be needed.

4.  Allow editing of the Name field in the Topography, Etiology and Collection Sample Files

> The Name field (#.01) in the TOPOGRAPHY FIELD file (#61), COLLECTION SAMPLE file (#62), and ETIOLOGY FIELD file (#61.2) are marked as Uneditable. A user with programmer access, and access to the option Uneditable Data \[DIUNEDIT\] under the Utility Functions \[DIUTILITY\] FileMan menu should edit the NAME field (#.01) in these files to make them Editable again.

<span id="_Toc361644557" class="anchor"></span>Figure 19: Make the NAME Field Editable Using the FileMan Option Uneditable Data \[DIUNEDIT\]

VA FileMan 22.0

Select OPTION: 6 \<ENTER\> UTILITY FUNCTIONS

Select UTILITY OPTION: 9 \<ENTER\> UNEDITABLE DATA

MODIFY WHAT FILE: OPTION// 61 \<ENTER\> TOPOGRAPHY FIELD (8514 entries)

Select FIELD: .01 \<ENTER\> NAME

FIELD IS ALREADY UNEDITABLE

DO YOU WANT TO ALLOW EDITING AGAIN? No// Y \<ENTER\> (Yes) ..OK

Select UTILITY OPTION: 9 \<ENTER\> UNEDITABLE DATA

MODIFY WHAT FILE: TOPOGRAPHY FIELD// 62 \<ENTER\> COLLECTION SAMPLE

(70 entries)

Select FIELD: .01 \<ENTER\> NAME

FIELD IS ALREADY UNEDITABLE

DO YOU WANT TO ALLOW EDITING AGAIN? No// Y \<ENTER\> (Yes) ..OK

Select UTILITY OPTION: 9 \<ENTER\> UNEDITABLE DATA

MODIFY WHAT FILE: COLLECTION SAMPLE// 61.2 \<ENTER\> ETIOLOGY FIELD

(4681 entries)

Select FIELD: .01 \<ENTER\> NAME

FIELD IS ALREADY UNEDITABLE

DO YOU WANT TO ALLOW EDITING AGAIN? No// Y \<ENTER\> (Yes) ..OK

# File 63 Remediation Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new tool is released to check the LAB DATA file (#63) for Data Dictionary issues. The tool checks for the following issues:

1.  Errors that may have occurred when an antibiotic was added by the local site to the Organism Sub-field (#63.3) of the LAB DATA file (#63).
2.  Errors with the data names in the LABORATORY TEST file (#60), for tests in the Clinical Chemistry (Chemistry and Hematology) section. It checks the CHEM, HEM, TOX, RIA, SER, etc. Sub-file (#63.04) of the LAB DATA file (#63) looking for possible discrepancies in the Data Dictionary.

When issues are found by the tool, users should contact the National Service Desk to request assistance from the Product Support team in resolving the errors.

The tool can run in two modes:

1.  Analyze and Report – In this mode, the tool analyzes the Data Dictionary for any issues, and if any issues are found the tool does not attempt to repair them. A report of the issues found by the tool is generated and sent in a MailMan message.

> The tool runs automatically in Analyze and Report mode after the successful installation of LEDI IV, and on the first of each month as part of the tasked option NIGHTLY CLEANUP \[LRTASK NIGHTY\]. The tool can also be run in Analyze and Report mode from the programmer’s prompt.

2.  Analyze, Repair, and Report – In this mode, the tool analyzes the Data Dictionary for any issues, and if any issues are found the tool attempts to automatically repair them. Not all issues can be automatically repaired by the tool; there are some issues that will require analysis and review by Subject Matter Experts (SMEs), and will require a manual repair. A report of the issues found by the tool is generated and sent in a MailMan message. The MailMan message will indicate which issues were auto-repaired and which issues require more analysis and will need to be manually repaired.  
      
    The only way to run the tool in Analyze, Repair, and Report mode is from the programmer’s prompt. This should only be done after entering a ticket with the National Service Desk and consulting with the Support Team.

> When run in repair mode, data dictionary changes may be made to lab files. Therefore, no lab orders or results for either Micro (if running Micro) or Chemistry (if running Chemistry) should occur during this time.  The repair mode can take approximately 2 hours to run.

<span id="_Toc361644558" class="anchor"></span>Figure 20: Running Chemistry File \#63 Remediation Tool in Analyze/Report Mode from Programmer Prompt

DEVISC1A3:MHCVSS\>D ^LRWU9 \<ENTER\>

This process will check the CHEM, HEM, TOX, RIA, SER, etc.

Sub-file (#63.04) of the LAB DATA file (#63) looking for

possible discrepancies in the Data Dictionary. Once the

process has completed, a MailMan message will be sent to the

user that started this process and any other user selected.

The two modes in which this process can be run are ANALYZE

and REPAIR. If the ANALYZE option is chosen, the process will

only look for discrepancies and report the findings via a

MailMan message. If the ANALYZE,REPAIR option is chosen the

process will ANALYZE and REPAIR any discrepancies found that

can be fixed programmatically and list all those that could

not be fixed but need attention.

Do you want to continue with this process? NO// Y \<ENTER\> YES

Select the action you wish to take:

1\. Analyze and Report.

2\. Analyze, Repair, and Report.

3\. Quit - No Action.

Enter a number 1 thru 3: 3// 1 \<ENTER\>

Are you sure you want to proceed? NO// Y \<ENTER\> YES

Send mail to: LRPROVIDER,TWO// \<ENTER\> LRPROVIDER,TWO

Select basket to send to: IN// \<ENTER\>

And Send to: \<ENTER\>

LRDFN=

DEVISC1A3:MHCVSS\>

<span id="_Toc361644559" class="anchor"></span>Figure 21: Running Micro File \#63 Remediation Tool in Analyze/Report Mode from Programmer Prompt

DEVISC1A3:MHCVSS\>D ^LRWU8\<ENTER\>

This process will check the Organism Sub-field (#63.3) of

the LAB DATA file (#63) looking for possible discrepancies

in the Data Dictionary. Once the process has completed, a

MailMan message will be sent to the user that started this

process and any other user selected.

The two modes in which this process can be run are ANALYZE

and REPAIR. If the ANALYZE option is chosen, the process will

only look for the discrepancies and report the findings via

a MailMan message. If the ANALYZE/REPAIR option is chosen the

process will ANALYZE and REPAIR any discrepancies found that

can be fixed programmatically and list all those that could

not be fixed but need attention.

Do you want to continue with this process? NO// Y \<ENTER\> YES

Select the action you wish to take:

1\. Analyze and Report.

2\. Analyze, Repair and Report.

3\. Quit - No Action.

Enter a number 1 thru 3: 3// 1 \<ENTER\>

Are you sure you want to proceed? NO// Y\<ENTER\> YES

Send mail to: LRPROVIDER,TWO// \<ENTER\> LRPROVIDER,TWO

Select basket to send to: IN// \<ENTER\>

And Send to: \<ENTER\>

Analyzing LRDFN: 0

DEVISC1A3:MHCVSS\>