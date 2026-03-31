---
title: SCIDO Version 3 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: SPN
app_name: Spinal Cord Injury and Disorders Outcomes (SCIDO)
section: GUI
app_status: active
pkg_ns: SPN
patch_ver: 3
patch_id: SPN*3
group_key: "SPN:SPN:3"
file_numbers: []
security_keys: []
menu_options: 0
description: SPINAL CORD INJURY and DISORDERS OUTCOMES (SCIDO) 3.0Interim VistA INSTALLATION GUIDE
audience: 
keywords: 
  - routine
  - calculated
  - disk
  - table
  - contents
  - install
  - installation
  - spinal
  - cord
  - mark
page_count: 0
word_count: 4786
section_count: 13
table_count: 8
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: February 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Spinal_Cord_Injury_Disorders_Outcomes/scido_3_0_interim_vista_installation_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Spinal_Cord_Injury_Disorders_Outcomes/scido_3_0_interim_vista_installation_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=196"
---

![](scido-version-3-installation-guide/001.png)

SPINAL CORD INJURY and DISORDERS OUTCOMES (SCIDO) 3.0Interim VistA INSTALLATION GUIDE

![](scido-version-3-installation-guide/002.png)

February 2011

VistA Health System Design & Development

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 52%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description</th>
<th>Author/Project Manager</th>
</tr>
<tr class="odd">
<th>2/17/2011</th>
<th>Minor formatting, preparation for VDL</th>
<th><mark>REDACTED</mark></th>
</tr>
<tr class="header">
<th>9/14/2010</th>
<th><p>Added routine ^HLCSRP4 to the routine list.</p>
<p>Updated file names for file retrieval.</p></th>
<th><mark>REDACTED</mark></th>
</tr>
<tr class="odd">
<th>9/13/2010</th>
<th>Updates – Product Support review</th>
<th><mark>REDACTED</mark></th>
</tr>
<tr class="header">
<th>9/8/2010</th>
<th><p>-Corrected checksums</p>
<p>-Screen capture for new distribution without ‘TEST’ in the header</p></th>
<th><mark>REDACTED</mark></th>
</tr>
<tr class="odd">
<th>7/6/2010</th>
<th><p>- Removed ‘draft’ watermark.</p>
<p>- Updated installation instructions for final version.</p>
<p>- Added sections for back out procedure, known anomalies, and troubleshooting, per operational readiness review.</p>
<p>- Updated table of contents.</p></th>
<th><mark>REDACTED</mark></th>
</tr>
<tr class="header">
<th>5/14/2010</th>
<th>Removed step 5 from page 11 which advised installer to restart the filers.</th>
<th><mark>REDACTED</mark></th>
</tr>
<tr class="odd">
<th>5/13/2010</th>
<th><p>Update version number and routine checksums</p>
<p>Captured output of installing vT14 and pasted to the document.</p></th>
<th><mark>REDACTED</mark></th>
</tr>
<tr class="header">
<th>5/7/2010</th>
<th>Add DISUSER information</th>
<th><mark>REDACTED</mark></th>
</tr>
<tr class="odd">
<th>7/30/2009</th>
<th>Updates for KIDS build test version 13</th>
<th><mark>REDACTED</mark></th>
</tr>
<tr class="header">
<th>12/24/2008</th>
<th>Updates for KIDS build test version 12</th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>09/24/2008</td>
<td>Add additional Proxy Setup information. Update checksums and build numbers for new test version of build.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/05/2008</td>
<td>Format document</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/22/2008</td>
<td>Updates from latest build and to add note of critical security key</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/11/2007</td>
<td>To include 4<sup>th</sup> step for setup of New Person user account</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/04/2007</td>
<td>To include Progress Note titles</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/21/2006</td>
<td>Initial documentation</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>03/29/2007</td>
<td>Updates from latest build</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [VistA Software Requirements](#vista-software-requirements)
  - [Routine List – Pre Installation](#routine-list-pre-installation)
  - [Routine List – Post Installation](#routine-list-post-installation)
  - [Options](#options)
  - [## Security Keys](#security-keys)
  - [Remote Procedures](#remote-procedures)
- [VistA Installation](#vista-installation)
  - [PART I – Install the Spinal Cord Injury and Disorders Outcomes V. 3.0 Package:](#part-i-install-the-spinal-cord-injury-and-disorders-outcomes-v-30-package)
    - [VistA Software Retrieval](#vista-software-retrieval)
  - [Installation Instructions for the SPN 3.0 package](#installation-instructions-for-the-spn-30-package)
    - [Step 1 Download Host KIDS File:](#step-1-download-host-kids-file)
    - [Step 2 Select Installation Option:](#step-2-select-installation-option)
    - [Step 3 Select Installation Option: Install Package(s):](#step-3-select-installation-option-install-packages)
    - [Step 3a - Load the distribution](#step-3a-load-the-distribution)
    - [Step 3b - Verify Checksums](#step-3b-verify-checksums)
    - [Step 3c - Backup a Transport Global](#step-3c-backup-a-transport-global)
    - [Step 4 Install the KIDS build:](#step-4-install-the-kids-build)
- [PART II – Verify/Set-up VistALink Connector Proxy account:](#part-ii-verifyset-up-vistalink-connector-proxy-account)
- [PART III – Setup New Person user accounts to be compatible with SCIDO V. 3.0:](#part-iii-setup-new-person-user-accounts-to-be-compatible-with-scido-v-30)
- [PART IV – Setup ADT Mail Groups in Mail Group file and Assign any Applicable Users to them:](#part-iv-setup-adt-mail-groups-in-mail-group-file-and-assign-any-applicable-users-to-them)
- [PART V – Verify that Spinal Cord Progress Note Titles are Present and Active:](#part-v-verify-that-spinal-cord-progress-note-titles-are-present-and-active)
  - [Spinal Cord Injury and Disorders Outcomes V. 3.0](#spinal-cord-injury-and-disorders-outcomes-v-30)
  - [Post Installation Activities](#post-installation-activities)
- [Appendices](#appendices)
  - [Back out Procedure](#back-out-procedure)
  - [Trouble Shooting Guide](#trouble-shooting-guide)
  - [Known Issues with VistA Remote Procedure Calls](#known-issues-with-vista-remote-procedure-calls)
The Spinal Cord Injury and Disorders Outcomes (SCIDO) application is a system for compiling spinal cord injury and disorders information. The SCIDO application accesses several other Veterans Health Information Systems and Technology Architecture (VistA) programs that contain information regarding diagnoses, prescriptions, surgical procedures, laboratory tests, radiological exams, patient demographics, hospital admissions, and clinical visits. This access allows clinical staff to take advantage of the data supported by VistA. Information can be summarized at three levels: local medical center, SCI region, or national research access.

# VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the installation of Spinal Cord Injury and Disorders Outcomes V. 3.0, the following packages must be installed and fully patched. The Installation Checklist provided in Addendum A of this document is organized in a step-wise manner to assist in loading any missing or new package/patch in the correct order.

| Software                | Version | Required Patches |
|-------------------------|---------|------------------|
| Kernel                  | V. 8    | Fully patched    |
| Kernel Toolkit          | V. 7.3  | Fully patched    |
| VA FileMan              | V. 22   | Fully patched    |
| VistALink               | V. 1.5  | Fully patched    |
| TIU                     | V. 1.0  | Fully patched    |
| Registration            | V. 5.3  | Fully patched    |
| Spinal Cord Dysfunction | V. 2.0  | Fully patched    |
| Surgery                 | V. 3.0  | Fully patched    |
| Prosthetics             | V. 3.0  | Fully patched    |

## Routine List – Pre Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list contains the routines that will be modified with Spinal Cord Injury and Disorders Outcomes V. 3.0. The checksums prior to this install are as follows:

| Routine | CHECK1^XTSUMBLD Value | CHECK^XTSUMBLD Value |
|---------|-----------------------|----------------------|
| SPNLRL1 | 11922728              | 5898379              |
| SPNLRL2 | 13807792              | 5836094              |
| SPNLRL3 | 10458300              | 4917596              |

## Routine List – Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list contains the routines included in Spinal Cord Injury and Disorders Outcomes V. 3.0

| Routine  | CHECK1^XTSUMBLD Value | CHECK^XTSUMBLD Value |
|----------|-----------------------|----------------------|
| SPNJRP4A | 1258600               | 589325               |
| SPNJRPC0 | 4797467               | 1650252              |
| SPNJRPC1 | 25695639              | 4803120              |
| SPNJRPC2 | 8549659               | 2897184              |
| SPNJRPC3 | 53506814              | 12712659             |
| SPNJRPC4 | 38673987              | 9287080              |
| SPNJRPC5 | 14449910              | 4594768              |
| SPNJRPC6 | 4635814               | 2462077              |
| SPNJRPC7 | 352636                | 166368               |
| SPNJRPC8 | 1723581               | 794489               |
| SPNJRPC9 | 17400459              | 5130695              |
| SPNJRPCC | 705728                | 355388               |
| SPNJRPCD | 26963457              | 10474519             |
| SPNJRPCE | 947821                | 426992               |
| SPNJRPCM | 3844721               | 1835099              |
| SPNJRPCP | 454442                | 121840               |
| SPNJRPCS | 842386                | 460523               |
| SPNJRPCX | 81896576              | 14117786             |
| SPNJRPDC | 7788443               | 2529003              |
| SPNJRPE2 | 1830378               | 730585               |
| SPNJRPET | 981420                | 528004               |
| SPNJRPFB | 2618869               | 910547               |
| SPNJRPIC | 7764384               | 2598285              |
| SPNJRPIL | 1214679               | 562685               |
| SPNJRPIP | 4321660               | 1738611              |
| SPNJRPIW | 77468632              | 15147655             |
| SPNJRPML | 5642555               | 2547143              |
| SPNJRPOP | 5917365               | 1887600              |
| SPNJRPP1 | 23248535              | 6509516              |
| SPNJRPP2 | 18150887              | 5238518              |
| SPNJRPPL | 1212848               | 526633               |
| SPNJRPPM | 12765608              | 3610707              |
| SPNJRPPN | 1907848               | 876549               |
| SPNJRPPR | 3055124               | 929249               |
| SPNJRPRC | 3460486               | 1399883              |
| SPNJRPRE | 5915306               | 2162773              |
| SPNJRPSC | 1441105               | 497305               |
| SPNJRPSD | 22832226              | 6538636              |
| SPNJRPSR | 2758801               | 1093225              |
| SPNJRPX2 | 33025054              | 7576956              |
| SPNLRK7  | 1438782               | 730996               |
| SPNLRK8  | 15230861              | 8533195              |
| SPNLRL1  | 19098772              | 8384499              |
| SPNLRL2  | 24652075              | 9481675              |
| SPNLRL3  | 16249663              | 7188957              |
| SPNLRL7  | 3954554               | 1423555              |
| SPNLRM7  | 3003178               | 1234153              |
| SPNLRM8  | 23501774              | 10537733             |
| SPNLRM9  | 9152833               | 4844155              |
| SPNLRR7  | 9512592               | 3606424              |
| SPNLRS7  | 19321322              | 6179931              |
| SPNRPC03 | 10552423              | 3737264              |
| SPNRPC1  | 17718596              | 6511719              |
| SPNRPC10 | 2838928               | 1310531              |
| SPNRPC13 | 19205247              | 7185321              |
| SPNRPC4  | 51645622              | 11014607             |
| SPNRPC4B | 46067512              | 10621527             |
| SPNRPC5  | 609564                | 297572               |
| SPNRPC6  | 851415                | 476487               |
| SPNRPC7  | 3491672               | 2043744              |
| SPNRPC8  | 1815443               | 664444               |
| SPNRPC9  | 2808690               | 1336821              |
| SPNRPCA1 | 4948876               | 1949821              |
| SPNRPCB  | 889413                | 401184               |
| SPNRPCC  | 15974748              | 4716332              |
| SPNRPCD  | 17417590              | 4665233              |
| SPNRPCE  | 23315717              | 7085434              |
| SPNRPCF  | 23018946              | 7392052              |
| SPNRPCG  | 9080936               | 3279358              |
| SPNRPCH  | 12245424              | 3398338              |
| SPNRPCI  | 18057216              | 3813644              |
| SPNRPCIC | 97795                 | 53557                |
| SPNRPCJ  | 16481640              | 4441860              |
| SPNRPCL  | 16794514              | 5125791              |
| SPNRPCM  | 21192373              | 6784024              |
| SPNRPCN  | 14508746              | 4922473              |
| SPNRPCO  | 12699717              | 4068267              |
| SPNRPCQ  | 6960635               | 2746399              |
| SPNRPCW  | 13994447              | 5013374              |
| SPNRPCW2 | 20809166              | 6522502              |

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is being sent to the site so that Spinal Cord Injury and Disorders Outcomes users will be able to view non-SCIDO data and reports via RPCs.

| Name                 | Status       |
|----------------------|--------------|
| SPN GENERAL USER RPC | SEND TO SITE |

## ## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following security keys are being sent to the site and are used by the KAAJEE software to add enhanced ‘Strong’ security to the Spinal Cord Injury and Disorders Outcomes system for users.

| Name                                                                                      | Status       |
|-------------------------------------------------------------------------------------------|--------------|
| SPN_ADMIN (this should only be given to users requiring Administration rights)            | SEND TO SITE |
| SPN_CATCHMENT (this should only be given to users requiring access to regional reporting) | SEND TO SITE |
| SPN_CLINICIAN (this should only be given to users requiring Clinician rights)             | SEND TO SITE |
| SPN_IRM (this should only be given to IRMs)                                               | SEND TO SITE |
| SPN_RESEARCHER (this should only be given to users requiring researcher rights)           | SEND TO SITE |

## Remote Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Remote Procedures:

| Name                                     | Function                                                        | Status       |
|------------------------------------------|-----------------------------------------------------------------|--------------|
| SPN ADMISSIONS REPORT                    | RPC ADMISSIONS REPORT BY DATE RANGE                             | SEND TO SITE |
| SPN BUILD PICK LIST ENTRIES              | Returns LAB TEST/DRUG NAMES/PROS REPORTS&FILTERS                | SEND TO SITE |
| SPN COMM DISCHARGES                      | Returns Discharge to Community info                             | SEND TO SITE |
| SPN CURRENT INPATS                       | Returns Current Inpatients data                                 | SEND TO SITE |
| SPN FEE BASIS ICNS                       | Returns list of ICNs who match Fee Basis Criteria               | SEND TO SITE |
| SPN GET ADT DATA                         | Returns ADT Patient movement entries for requested date         | SEND TO SITE |
| SPN GET CLINIC STOPS                     | Returns Clinic Stops                                            | SEND TO SITE |
| SPN GET ENROLLMENT                       | Returns most recent Eligibility Enrollment Application          | SEND TO SITE |
| SPN GET ETHNICITY                        | Returns VA Ethnicity Info                                       | SEND TO SITE |
| SPN GET FUTURE APPTS                     | Returns list of patients with future appointments.              | SEND TO SITE |
| SPN GET LAST SEEN                        | Returns list of patients with their date last seen              | SEND TO SITE |
| SPN GET MAILING ADDRESS                  | Returns Patient addresses for mailing labels                    | SEND TO SITE |
| SPN GET PAIN RATING                      | Returns most recent Vitals Pain Rating                          | SEND TO SITE |
| SPN GET PROS ITEMS                       | Returns list of Prosthetic Items                                | SEND TO SITE |
| SPN GET RACE                             | Returns VA Race info                                            | SEND TO SITE |
| SPN GET RAD REPORTS                      | Returns Radiology Report / Impression / Clinical history text.  | SEND TO SITE |
| SPN GET SCI COORDINATORS                 | Returns SCI Coordinator Providers from New Person file          | SEND TO SITE |
| SPN GET SPEC CODES                       | Returns Specialty PTF codes                                     | SEND TO SITE |
| SPN GET VA STATUS                        | Returns VA SCI Status                                           | SEND TO SITE |
| SPN ICD9 CODE SEARCH                     | Returns ICD9 Codes based on search criteria                     | SEND TO SITE |
| SPN ICDS/CPTS & DESCRIPTIONS             | CPTS/ICDS CODES & DESCRIPTS                                     | SEND TO SITE |
| SPN ICDS/CPTS W RAD COMMENTS             | List Recent Diagnoses with Rad. comments                        | SEND TO SITE |
| SPN ICN LOADER                           | Returns ICNs for list of DFNs                                   | SEND TO SITE |
| SPN IDT DISCHARGE LOCATIONS              | Returns Discharge date and location                             | SEND TO SITE |
| SPN INFLUENZA RPT                        | Returns INFLUENZA Lab test results                              | SEND TO SITE |
| SPN INPAT CARE                           | Returns Applications for Inpatient Care data                    | SEND TO SITE |
| SPN INPAT OUTPAT ACTIVITY                | Returns Inpatient/Outpatient Activity for list of pats          | SEND TO SITE |
| SPN INPAT OUTPAT SPECIFIC                | Returns Inpatient/Outpatient Specific for list of pats          | SEND TO SITE |
| SPN INPATIENT ICNS                       | Returns list of ICNs for Inpatients                             | SEND TO SITE |
| SPN LAB COMPLETE BLOOD COUNT             | Returns Lab test results for the complete blood count           | SEND TO SITE |
| SPN LAB MICRO BLOOD                      | Returns MICROBIOLOGY BLOOD Lab test results                     | SEND TO SITE |
| SPN LAB MICRO URINE                      | Returns MICROBIOLOGY URINE Lab test results                     | SEND TO SITE |
| SPN LAB SPUTUM                           | Returns SPUTUM LAB results box                                  | SEND TO SITE |
| SPN LAB URINALYSIS                       | Returns URINALYSIS Lab test results                             | SEND TO SITE |
| SPN LAB UTL REPORT                       | LAB TEST UTILIZATION REPORT                                     | SEND TO SITE |
| SPN LAB UTL SPECIFIC                     | Laboratory Utilization rpt specific RPC                         | SEND TO SITE |
| SPN LIST ICDS/CPTS                       | Returns list of ICD/CPT LONG DESCRIPTIONS                       | SEND TO SITE |
| SPN LIST PROGRESS NOTE TITLES            | Returns TIU doc titles from 8925.1                              | SEND TO SITE |
| SPN MAILMAN NOTIFICATION                 | Send Mailman notifications                                      | SEND TO SITE |
| SPN MEANS & ELIGIBILITY                  | Returns most recent Means and Eligibility info for all patients | SEND TO SITE |
| SPN MEDICATIONS ICNS                     | Returns list of ICNs who match VA Drug Class criteria           | SEND TO SITE |
| SPN MEDS 1<sup>ST</sup> 2-CHARS VA CLASS | PHARMACY RX'S WHEN AN RX MATCHES THE FIRST TWO CHAR             | SEND TO SITE |
| SPN MEDS BY FULL VA CLASS                | Returns PHARMACY RX'S WITH A SPECIFIC NDC                       | SEND TO SITE |
| SPN NUTRITION PRECAUTIONS                | Nutrition Dietary Precautions RPC                               | SEND TO SITE |
| SPN OUTPATIENT ICNS                      | Returns list of ICNs for Outpatients                            | SEND TO SITE |
| SPN PAIN VITALS                          | Routine to list Vitals / Cover Sheet data                       | SEND TO SITE |
| SPN PAT BREAKDOWN                        | Returns Breakdown of Patient data                               | SEND TO SITE |
| SPN PHARMACY UTL REPORT                  | Pharmacy Utilization rpt RPC                                    | SEND TO SITE |
| SPN PROGRESS NOTES WRAPPER               | RPC to record SCI Progress Notes                                | SEND TO SITE |
| SPN PROS UTL REPORT                      | Returns Prosthetic Utilization info                             | SEND TO SITE |
| SPN PROS UTL SPECIFIC                    | Returns Prosthetic Utilization Specific info                    | SEND TO SITE |
| SPN PROSTHETICS ICNS                     | Returns list of ICNs who match Prosthetics criteria             | SEND TO SITE |
| SPN PUT LAB COMPLETE BLOOD               | Returns Lab test results for the complete blood count           | SEND TO SITE |
| SPN PUT LAB CYTOPATH                     | Returns Lab test results for CYTOPATHOLOGY                      | SEND TO SITE |
| SPN PUT LAB MICRO                        | Returns Lab test results for MICROBIOLOGY                       | SEND TO SITE |
| SPN PUT LAB SURG PATH                    | Returns Lab test results for SURGICAL PATHOLOGY                 | SEND TO SITE |
| SPN PUT PROSTHETIC DEVICES               | Returns PROSTHETIC DEVICES                                      | SEND TO SITE |
| SPN RAD UTL REPORT                       | RAD Utilization rpt RPC                                         | SEND TO SITE |
| SPN READMISSIONS REPORT                  | RPC READMISSIONS REPORT BY DATE RANGE                           | SEND TO SITE |
| SPN RECENT MED CENTERS                   | Returns sites where Patient has been treated                    | SEND TO SITE |
| SPN RX UTILIZATION SPECIFIC              | Pharmacy Utilization rpt specific RPC                           | SEND TO SITE |
| SPN SCI SCD DISCHARGES                   | Returns SCI/SCI Discharges data                                 | SEND TO SITE |
| SPN SCI USER ROLES                       | Returns SCI Roles for all SCI NEW PERSON entries                | SEND TO SITE |
| SPN SECONDARY ICDS                       | Returns ICD'S excluding SCI. No cut date                        | SEND TO SITE |
| SPN SERVICE CONNECTED ICNS               | Returns list of ICNs who match Service Connection criteria      | SEND TO SITE |
| SPN VADPT VALUES                         | Returns patient demographics from VADPT APIs                    | SEND TO SITE |

# VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following action is needed to configure the VistA side of the SCIDO application once all of the dependencies have been installed (see Appendix A):

## PART I – Install the Spinal Cord Injury and Disorders Outcomes V. 3.0 Package:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDs file Package

SPN_3_0.KID SPN 3.0

### VistA Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Spinal Cord Injury and Disorders Outcomes V. 3.0 M package (Host File name SPN_3_0.KID) and documentation can be downloaded from the Enterprise VistA Support (EVS) anonymous directories:

<span class="mark">REDACTED</span>

(This Preferred Method transmits the files from the first available FTP server.)

## Installation Instructions for the SPN 3.0 package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access the KIDS menu in VistA (Kernel Installation & Distribution, and select the Installation option.

### Step 1 Download Host KIDS File:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download the KIDS file SPN_3_0.KID from the ANONYMOUS.SOFTWARE directory of Albany, Hines, or the Salt Lake CIOFO to the appropriate directory on your system.

1.  START UP KIDS

Start up the Kernel Installation and Distribution System Menu \[XPD MAIN\]:

Edits and Distribution

Utilities

Installation

Select Kernel Installation & Distribution System Option: Installation

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

### Step 2 Select Installation Option:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Load a Distribution and select Host File: SPN_3_0.KID

> **NOTE:** The following are OPTIONAL - (When prompted for the INSTALL NAME, enter SPN 3):

Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.

Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).

### Step 3 Select Installation Option: Install Package(s):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*This is the step to start the installation of this KIDS build:

Choose the Install Package(s) option to start the patch install.

When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//’ Is recommended, but is up to the installers discretion.

When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//' answer NO (unless otherwise indicated)

When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//' answer NO (unless otherwise indicated)

### Step 3a - Load the distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Kernel Installation & Distribution System Option: Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 1 Load a Distribution

Enter a Host File: SYS\$SYSDEVICE:\[ANONYMOUS\]SPN_3_0.KID

KIDS Distribution saved on Sep 14, 2010@10:35:35

Comment: SPINAL CORD VERSION 3.0

This Distribution contains Transport Globals for the following Package(s):

SPN 3.0

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

SPN 3.0

Use INSTALL NAME: SPN 3.0 to install this Distribution.

### Step 3b - Verify Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 2 Verify Checksums in Transport Global

Select INSTALL NAME: SPN 3.0 Loaded from Distribution 9/14/10@11:00:37

=\> SPINAL CORD VERSION 3.0 ;Created on Sep 09, 2010@11:22:43

This Distribution was loaded on Sep 14, 2010@11:00:37 with header of

SPINAL CORD VERSION 3.0 ;Created on Sep 09, 2010@11:22:43

It consisted of the following Install(s):

SPN 3.0

Want each Routine Listed with Checksums: Yes// YES

DEVICE: HOME// HOME;;999 UCX/TELNET

PACKAGE: SPN 3.0 Sep 14, 2010 11:03 am PAGE 1

------------------------------------------------------------------------------

SPNJRP4A Calculated 1258600

SPNJRPC0 Calculated 4797467

SPNJRPC1 Calculated 25695639

SPNJRPC2 Calculated 8549659

SPNJRPC3 Calculated 53506814

SPNJRPC4 Calculated 38673987

SPNJRPC5 Calculated 14449910

SPNJRPC6 Calculated 4635814

SPNJRPC7 Calculated 352636

SPNJRPC8 Calculated 1723581

SPNJRPC9 Calculated 17400459

SPNJRPCC Calculated 705728

SPNJRPCD Calculated 26963457

SPNJRPCE Calculated 947821

SPNJRPCM Calculated 3844721

SPNJRPCP Calculated 454442

SPNJRPCS Calculated 842386

SPNJRPCX Calculated 81896576

SPNJRPDC Calculated 7788443

SPNJRPE2 Calculated 1830378

SPNJRPET Calculated 981420

SPNJRPFB Calculated 2618869

SPNJRPIC Calculated 7764384

SPNJRPIL Calculated 1214679

SPNJRPIP Calculated 4321660

SPNJRPIW Calculated 77468632

SPNJRPML Calculated 5642555

SPNJRPOP Calculated 5917365

SPNJRPP1 Calculated 23248535

SPNJRPP2 Calculated 18150887

SPNJRPPL Calculated 1212848

SPNJRPPM Calculated 12765608

SPNJRPPN Calculated 1907848

SPNJRPPR Calculated 3055124

SPNJRPRC Calculated 3460486

SPNJRPRE Calculated 5915306

SPNJRPSC Calculated 1441105

SPNJRPSD Calculated 22832226

SPNJRPSR Calculated 2758801

SPNJRPX2 Calculated 33025054

SPNLRK7 Calculated 1438782

SPNLRK8 Calculated 15230861

SPNLRL1 Calculated 19098772

SPNLRL2 Calculated 24652075

SPNLRL3 Calculated 16249663

SPNLRL7 Calculated 3954554

SPNLRM7 Calculated 3003178

SPNLRM8 Calculated 23501774

SPNLRM9 Calculated 9152833

SPNLRR7 Calculated 9512592

SPNLRS7 Calculated 19321322

SPNRPC03 Calculated 10552423

SPNRPC1 Calculated 17718596

SPNRPC10 Calculated 2838928

SPNRPC13 Calculated 19205247

SPNRPC4 Calculated 51645622

SPNRPC4B Calculated 46067512

SPNRPC5 Calculated 609564

SPNRPC6 Calculated 851415

SPNRPC7 Calculated 3491672

SPNRPC8 Calculated 1815443

SPNRPC9 Calculated 2808690

SPNRPCA1 Calculated 4948876

SPNRPCB Calculated 889413

SPNRPCC Calculated 15974748

SPNRPCD Calculated 17417590

SPNRPCE Calculated 23315717

SPNRPCF Calculated 23018946

SPNRPCG Calculated 9080936

SPNRPCH Calculated 12245424

SPNRPCI Calculated 18057216

SPNRPCIC Calculated 97795

SPNRPCJ Calculated 16481640

SPNRPCL Calculated 16794514

SPNRPCM Calculated 21192373

SPNRPCN Calculated 14508746

SPNRPCO Calculated 12699717

SPNRPCQ Calculated 6960635

SPNRPCW Calculated 13994447

SPNRPCW2 Calculated 20809166

79 Routines checked, 0 failed.

### Step 3c - Backup a Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: Backup a Transport Global

Select INSTALL NAME: SPN 3.0 Loaded from Distribution 5/14/10@11:00:37

=\> SPINAL CORD VERSION 3.0 ;Created on Sep 09, 2010@11:22:43

This Distribution was loaded on Sep 14, 2010@11:00:37 with header of

SPINAL CORD VERSION 3.0 ;Created on Sep 09, 2010@11:22:43

It consisted of the following Install(s):

SPN 3.0

Subject: Backup of SPN 3.0 install on Sep 14, 2010 Replace

Loading Routines for SPN 3.0

Routine SPNJRP4A is not on the disk..

Routine SPNJRPC0 is not on the disk..

Routine SPNJRPC1 is not on the disk..

Routine SPNJRPC2 is not on the disk..

Routine SPNJRPC3 is not on the disk..

Routine SPNJRPC4 is not on the disk..

Routine SPNJRPC5 is not on the disk..

Routine SPNJRPC6 is not on the disk..

Routine SPNJRPC7 is not on the disk..

Routine SPNJRPC8 is not on the disk..

Routine SPNJRPC9 is not on the disk..

Routine SPNJRPCC is not on the disk..

Routine SPNJRPCD is not on the disk..

Routine SPNJRPCE is not on the disk..

Routine SPNJRPCM is not on the disk..

Routine SPNJRPCP is not on the disk..

Routine SPNJRPCS is not on the disk..

Routine SPNJRPCX is not on the disk..

Routine SPNJRPDC is not on the disk..

Routine SPNJRPE2 is not on the disk..

Routine SPNJRPET is not on the disk..

Routine SPNJRPFB is not on the disk..

Routine SPNJRPIC is not on the disk..

Routine SPNJRPIL is not on the disk..

Routine SPNJRPIP is not on the disk..

Routine SPNJRPIW is not on the disk..

Routine SPNJRPML is not on the disk..

Routine SPNJRPOP is not on the disk..

Routine SPNJRPP1 is not on the disk..

Routine SPNJRPP2 is not on the disk..

Routine SPNJRPPL is not on the disk..

Routine SPNJRPPM is not on the disk..

Routine SPNJRPPN is not on the disk..

Routine SPNJRPPR is not on the disk..

Routine SPNJRPRC is not on the disk..

Routine SPNJRPRE is not on the disk..

Routine SPNJRPSC is not on the disk..

Routine SPNJRPSD is not on the disk..

Routine SPNJRPSR is not on the disk..

Routine SPNJRPX2 is not on the disk..

Routine SPNLRK7 is not on the disk..

Routine SPNLRK8 is not on the disk..

Routine SPNLRL1 is not on the disk..

Routine SPNLRL2 is not on the disk..

Routine SPNLRL3 is not on the disk..

Routine SPNLRL7 is not on the disk..

Routine SPNLRM7 is not on the disk..

Routine SPNLRM8 is not on the disk..

Routine SPNLRM9 is not on the disk..

Routine SPNLRR7 is not on the disk..

Routine SPNLRS7 is not on the disk..

Routine SPNRPC03 is not on the disk..

Routine SPNRPC1 is not on the disk..

Routine SPNRPC10 is not on the disk..

Routine SPNRPC13 is not on the disk..

Routine SPNRPC4 is not on the disk..

Routine SPNRPC4B is not on the disk..

Routine SPNRPC5 is not on the disk..

Routine SPNRPC6 is not on the disk..

Routine SPNRPC7 is not on the disk..

Routine SPNRPC8 is not on the disk..

Routine SPNRPC9 is not on the disk..

Routine SPNRPCA1 is not on the disk..

Routine SPNRPCB is not on the disk..

Routine SPNRPCC is not on the disk..

Routine SPNRPCD is not on the disk..

Routine SPNRPCE is not on the disk..

Routine SPNRPCF is not on the disk..

Routine SPNRPCG is not on the disk..

Routine SPNRPCH is not on the disk..

Routine SPNRPCI is not on the disk..

Routine SPNRPCIC is not on the disk..

Routine SPNRPCJ is not on the disk..

Routine SPNRPCL is not on the disk..

Routine SPNRPCM is not on the disk..

Routine SPNRPCN is not on the disk..

Routine SPNRPCO is not on the disk..

Routine SPNRPCQ is not on the disk..

Routine SPNRPCW is not on the disk..

Routine SPNRPCW2 is not on the disk..

Send mail to:

### Step 4 Install the KIDS build:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: Install Package(s)

Sep 14, 2010@11:07:05

Build Distribution Date: Sep 14, 2010

SPINAL CORD VERSION 3.0 ;Created on Sep 09, 2010@11:22:43

It consisted of the following Install(s):

SPN 3.0

This Distribution was loaded on Sep 14, 2010@11:00:37 with header of

SPINAL CORD VERSION 3.0 ;Created on Sep 09, 2010@11:22:43

It consisted of the following Install(s):

SPN 3.0

Checking Install for Package SPN 3.0

Install Questions for SPN 3.0

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TCP

Install Started for SPN 3.0 :

Sep 14, 2010@11:07:05

Build Distribution Date: Sep 14, 2010

Installing Routines:

Sep 14, 2010@11:07:06

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing REMOTE PROCEDURE

Installing OPTION

Sep 14, 2010@11:07:07

Updating Routine file...

Updating KIDS files...

SPN 3.0 Installed.

Sep 14, 2010@11:07:08

Install Message sent \#2729

Call MENU rebuild

Starting Menu Rebuild: Dec 24, 2008@12:12:26

Collecting primary menus in the New Person file...

Primary menus found in the New Person file

------------------------------------------

OPTION NAME MENU TEXT \# OF LAST LAST

USERS USED BUILT

XMUSER MailMan Menu 354 04/19/05 12/24/08

EVE Systems Manager Menu 16 03/29/07 12/24/08

PSZMGR Pharmacy 2 04/18/05 12/24/08

PSO OUTPUTS Output Reports 1 02/04/05 12/24/08

…

Building secondary menu trees....

Merging.... done.

Menu Rebuild Complete: Sep 14, 2010@11:07:21

─────────────────────────────────────────────────────

┌─────────────────────────────────────────────────

│ 25 50 75 100% │

Complete └────────────────────────────────────────────────────┘

Install Completed

# PART II – Verify/Set-up VistALink Connector Proxy account:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A VistALink Connector Proxy account may already be established at each site, but it is recommended that a new Connector Proxy account be created using the naming convention as follows:

Name: VISTALINK,SCIDO

(<u>NOTE:</u> After you’ve established the Access/Verify Codes for this account, sign into your system using these codes, reset the verify code and clear any other first sign-on steps i.e. on-line information security agreements).

From the Operations Management menu on the EVE menu, select the Foundations Management menu. Select CP (Enter/Edit Connector Proxy User)

<u>Set the following parameters in File 200 – New Person File:</u>

The Connector Proxy account for SCIDO must have the “Verify Code never expires” field in the New Person file set to “Yes.”

The Connector Proxy account for SCIDO must have the “Multiple Logins” field in the New Person file set to “Allowed”.

The Connector Proxy account for SCIDO must have the DISUER field in the New Person file set to “No”.

The Connector Proxy account needs to have the following Secondary Menu Options set the in the New Person file (#200):

SPN GENERAL USER RPC

XUS KAAJEE WEB LOGON

DGRR GUI PATIENT LOOKUP

The Connector Proxy account needs to have the following Security Key to allow for users to view patient specific data for the Utilization reports:

SPNL SCD PTS

Refer to the VistALink documentation for more information. Refer to the ‘Guidance of Connector Proxy User Accounts’ attachment of the MOU for ‘VistA and New Generation VistA System Connections’ for information on transmitting the Connector Proxy account information securely to the IRM staff and/or Regional Data Center staff who will be responsible for installing the web-based part of Spinal Cord Injury and Disorders Outcomes Version 3.0.

Specifically, the following information must be provided to the Development Team so that the Connector proxy account information is set properly inside the SCIDO application log-in script:

The name of the Connector proxy account (VISTALINK,SCIDO)

The DUZ numbers for the Connector Proxy accounts

The access and verify code of the Connector proxy account

The names of the Production accounts

The port number for VistALink (generally 8000, 8001 or 8100) – Make a FileMan Inquiry into the VistALink Listener Configuration file for the VistALink port number at your Facility.

# PART III – Setup New Person user accounts to be compatible with SCIDO V. 3.0:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for VistA users to access and use the Spinal Cord Injury Disorders & Outcomes web application, they must be set up with the following values in the New Person (#200) file:

They will need one or more of the following Security Keys, depending on their role in SCI:

SPN_CLINICIAN (this should only be given to users requiring Clinician rights)

SPN_RESEARCHER (this should only be given to users requiring researcher rights)

SPN_ADMIN (this should only be given to users requiring Administration rights)

SPN_IRM (this should only be given to IRMs)

SPN_CATCHMENT (this should only be given to users requiring access to regional reporting. Users requiring this key must also have the SPN_CLINICIAN or SPN_ADMIN security key)

SPNL SCD PTS (If user needs to view patient specific data for the Utilization reports)

Their Menu Options should include:

SPN GENERAL USER RPC

XUS KAAJEE WEB LOGON

DGRR GUI PATIENT LOOKUP

An electronic signature code is needed in order to store Progress Notes.

<u>Provider</u> User Class is needed to sign Progress Notes.

# PART IV – Setup ADT Mail Groups in Mail Group file and Assign any Applicable Users to them:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One of the features in the Spinal Cord Injury Disorders & Outcomes web application is to search the VistA Patient Movement file on a nightly basis and report on any Admissions, Discharges, or Transfers that occurred on that day for any given patient in the Spinal Cord Registry. An ADT summary notification is submitted to VistA and entered into the VistA Mailman system. These notifications will be sent to one of two mail group types, one for Multiple Sclerosis (MS) patients and another for general Spinal Cord Injury patients. The names of these mail groups need to be coordinated and must be identical to the names of those used on the Spinal Cord Injury Disorders & Outcomes web application.

Coordinate with IRM staff and/or Regional Data Center staff who will be responsible for installing the web-based part of Spinal Cord Injury and Disorders Outcomes Version 3.0 to derive the names of the MS Mail Group(s) and SCI Mail Group(s) needed for the ADT Notification process.

Enter the new Mail Groups into the VistA Mail Group file (#3.8) and set the Type field to PUBLIC.

Enter the names of the employees (from the New Person file (#200)) to the appropriate Mail Group(s) if they are to receive these notifications.

For general Spinal Cord Injury patients, use the existing SPNL SCD COORDINATOR mail group.

For MS patients, create a new mail group:

MAIL GROUP NAME: SCIDO ADT MS// \[All caps with a space between each word\]Select MEMBER:TYPE:DESCRIPTION: == \[WRAP\] == \[INSERT\] ========\< DESCRIPTION \>======= \[\<PF1\>H=Help\] ====MailMan alerts about Admission/Discharge/Transfer (ADT) activities at the site as related to Spinal Cord Injury patients with MS.T=======T=======T=======T=======T=======T=======T=======T\>======

TYPE: pu  public

ALLOW SELF ENROLLMENT?: No

ORGANIZER:

IRM COORDINATOR:

Select AUTHORIZED SENDER:

# PART V – Verify that Spinal Cord Progress Note Titles are Present and Active:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for the Spinal Cord Injury Disorders & Outcomes Progress Notes functionality to work properly, the following Progress Note Titles must be present and active in the TIU Document Definition File (# 8925.1):

SCI FUNCTIONAL INDEPENDENCE MEASURE

SCI GENERAL NOTE

SCI CRAIG HANDICAP ASSESSMENT&REPORTING TECHNIQUE-SHORT FORM

SCI DIENER SATISFACTION WITH LIFE SCALE

## Spinal Cord Injury and Disorders Outcomes V. 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System Requirements:

Below is the summary of the package implementation for Spinal Cord Injury and Disorders Outcomes V. 3.0 distributed as SPN_3_0.KID. See the previous sections for dependant/required patch and packages.

| Installed Y/N | Package                                          | Distribution | Patch/Package                                                                              |
|---------------|--------------------------------------------------|--------------|--------------------------------------------------------------------------------------------|
|               | Spinal Cord Injury and Disorders Outcomes V. 3.0 | SPN_3_0.KID  | SPN 3.0 This is the build required to run Spinal Cord Injury and Disorders Outcomes V. 3.0 |

## Post Installation Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Setup:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>Complete Y/N</th>
<th>Step</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><p>NOTE: Provide Connector Proxy information from VistALink installation above to the Spinal Cord deployment team. Connector Proxy account should have the following secondary menu options:</p>
<p>SPN GENERAL USER RPC</p>
<p>XUS KAAJEE WEB LOGON</p>
<p>DGRR GUI PATIENT LOOKUP</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>Add secondary menu to Spinal Cord Injury and Disorders Outcomes V. 3.0 VistA User Accounts:</p>
<p>SPN GENERAL USER RPC</p>
<p>XUS KAAJEE WEB LOGON</p>
<p>DGRR GUI PATIENT LOOKUP</p></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Add selected Security Keys to Spinal Cord Injury and Disorders Outcomes V. 3.0 VistA User Accounts:</p>
<p>SPN_CLINICIAN (for Clinician role)</p>
<p>SPN_ADMIN (for Administrator role)</p>
<p>SPN_RESEARCHER (for Researcher role) – issue this key only on direction of National Spinal Cord Injury and Disorders Services Office</p>
<p>SPN_IRM (for IRMs)</p>
<p>SPN_CATCHMENT (for regional perspective only)</p>
<p>SPNL SCD PTS</p></td>
</tr>
<tr class="even">
<td></td>
<td>Enter Electronic Signature code if user will be storing progress notes</td>
</tr>
<tr class="odd">
<td></td>
<td>Assign User to appropriate Mail Group if receiving ADT Mailman Notifications (Mail Groups must be set up in the VistA FileMan Mail Group file (#3.8)</td>
</tr>
</tbody>
</table>

# Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Version 2 of Spinal Cord Dysfunction can run with version 3 installed, so it in the event that severe problems are encountered with Version 3 it is unlikely that it will need to be backed out. Simply continuing use with Version 2 until the problems are resolved will most likely be adequate.

However, these steps may be followed to back out version 3:

Step 1: Insure that a backup of the version 2 routines was made as specified in the installation guide. Back out should not proceed until it is verified that a backup of the routines is available.

Step 2: Delete all the routines that were included in the installation.

Step 3: Install the routines from the backup.

Step 4: Delete all the SPN\* remote procedures.

Step 5: Delete the SPN GENERAL USER RPC option.

Step 6: Rebuild the menu trees.

## Trouble Shooting Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1)  If local troubleshooting fails to identify the problem, Product Support should be notified via Remedy. 
2)  Most problems that occur while using SCIDO result in a log entry made on the regional server.    Product Support can check these logs.
3)  The Kernel error trap may be checked to determine whether or not a hard error was encountered by the SCIDO application.
4)  Listed here are some of the issues that might arise after installing SCIDO:
    1.  Was the connector proxy created with DISUSER set to NO and VERIFY CODE NEVER EXPIRES set to YES?
    2.  Was the connector proxy assigned the following secondary options?
- SPN GENERAL USER RPC
- XUS KAAJEE WEB LOGON
- DGRR GUI PATIENT LOOKUP
  1.  If patient data doesn’t appear in the utilization reports, was the connector proxy assigned the SPNL SCD PTS security key?
  2.  Failure to connect to the regional SCIDO server after installation may indicate an issue with the site’s login script on the regional server.  Product Support may be requested to check that via Remedy.
  3.  Failure of SCIDO later on could be due to a connectivity problem, or might be due to the regional server being down.   Product Support may be requested to check that via Remedy.
  4.  Was the user given the right security keys for his/her role(s)?
  5.  Was the user given these menu options?
- SPN GENERAL USER RPC
- XUS KAAJEE WEB LOGON
- DGRR GUI PATIENT LOOKUP
  1.  Was the user assigned the appropriate Provider User Class for creating Progress Notes?
  2.  Does the user have an electronic signature established for signing progress notes?
  3.  If a user isn’t receiving Mailman notifications of ADT events, check that they are entered to the appropriate mail group that was created for these notifications.
  4.  If users aren’t receiving Mailman notifications of ADT events, then notify local IT support to verify the mail group(s) on the regional server.
  5.  If the progress notes functionality isn’t working properly, verify that the following titles are in TIU and active:
- SCI FUNCTIONAL INDEPENDENCE MEASURE
- SCI GENERAL NOTE
- SCI CRAIG HANDICAP ASSESSMENT&REPORTING TECHNIQUE-SHORT FORM
- SCI DIENER SATISFACTION WITH LIFE SCALE

If the titles are there, does your facility have a business rule created through the Authorization/Subscription application that controls access to Progress Note Titles? If so, you must assign an appropriate Person Class to the Connector Proxy account via the User Edit option to facilitate automated notes through SCIDO.

## Known Issues with VistA Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following issues are excerpted from the document ‘Request for Concurrence to Release Software with Known Anomalies’ for SCIDO 3.0. They represent outstanding problems that are not severe and will be addressed in later version of SCIDO. Most of SCIDO’s outstanding issues do not lie on the M VistA side of SCIDO and so are not shown here.

| SCI00000801 | Outpatient Visit RPC Issue (SPN OUTPATIENT ICNS RPC): When same start/end date is used, the Outpatient Visit filter doesn’t work | Avg. | User can specify a larger time frame. | Will be addressed in Version 3.1 scope and prioritized by VHA stakeholders |
|-------------|----------------------------------------------------------------------------------------------------------------------------------|------|---------------------------------------|----------------------------------------------------------------------------|