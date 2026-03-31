---
consolidated_title: "install guide"
app_code: FB
doc_type: IG
master_source: "FB*3.5*158 Install Guide"
master_pub_date: revision_count: 0
consolidated_from: 6 versions
prior_versions:
  - "FB*3.5*123 Install Guide"
  - "FB*3.5*132 Install Guide"
  - "FB*3.5*135 Install Guide"
  - "FB*3.5*146 Install Guide"
  - "FB*3.5*163 Install Guide"
---

FEE BASISINSTALLATION GUIDE

![](fb-3-5-158-install-guide/001.png)

Patch FB\*3.5\*158Health Administration Product Enhancements (HAPE)Electronic Data Interchange (EDI)Purchased Care (PC)– Electronic Remittance Advice (ERA) ComplianceJanuary 2018Version 2.3

Office of Information and Technology

Product Development

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [Introduction](#introduction)
  - [Software Overview](#software-overview)
  - [Document Overview](#document-overview)
    - [Additional Resources](#additional-resources)
- [Software Prerequisites](#software-prerequisites)
  - [Software Dependencies](#software-dependencies)
- [Patch Components](#patch-components)
  - [Files and Fields](#files-and-fields)
  - [Forms](#forms)
  - [Mail Groups](#mail-groups)
  - [Options](#options)
  - [Protocols](#protocols)
  - [Security Keys](#security-keys)
  - [Templates](#templates)
  - [Bulletins](#bulletins)
  - [Additional Information](#additional-information)
  - [New Service Requests (NSRs)](#new-service-requests-nsrs)
  - [Patient Safety Issues (PSIs)](#patient-safety-issues-psis)
  - [Estimated Installation Time](#estimated-installation-time)
- [Pre/Post Installation Overview](#prepost-installation-overview)
- [Installation Instructions](#installation-instructions)
- [Post-Installation Instructions](#post-installation-instructions)
- [Routine Information](#routine-information)
- [Back-out and Roll-back Procedures](#back-out-and-roll-back-procedures)
  - [Back-out Procedure](#back-out-procedure)
  - [Roll-back Procedure](#roll-back-procedure)
Table i. Revision History
<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 50%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Project Mgr/Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/13/17</td>
<td>2.3</td>
<td>Updated Post-Install instructions</td>
<td><ul>
<li><blockquote>
<p>Project Manager<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Lead Developer/Technical Writer REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>11/03/2017</td>
<td>2.2</td>
<td>Updated sections 1.2.1, 3.7, 5 per Product Supoort review and the expected release date</td>
<td><ul>
<li><blockquote>
<p>Project Manager<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Lead Developer/Technical Writer REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>06/14/2017</td>
<td>2.1</td>
<td>Updated section 4 Pre/Post Installation Overview</td>
<td><ul>
<li><blockquote>
<p>Project Manager<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Lead Developer/Technical Writer REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>10/13/2016</td>
<td>2.0</td>
<td>VA COR accepted document effective October 13, 2016. Document has been baselined for release.</td>
<td><ul>
<li><blockquote>
<p>Project Manager<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Lead Developer/Technical Writer REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>9/27/2016</td>
<td>1.4</td>
<td><p>Sentence added to Post Install instructions to schedule the task for off-hours.</p>
<p>Update software dependencies and description of CARC/RARC Relationship updates.</p></td>
<td><ul>
<li><blockquote>
<p>Project Manager<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Lead Developer/Technical Writer REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>9/13/2016</td>
<td>1.3</td>
<td>Added Tucson to Section 1.3. Modified text in Section 6.</td>
<td><ul>
<li><blockquote>
<p>Project Manager<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Lead Developer/Technical Writer REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>9/6/2016</td>
<td>1.2</td>
<td>CR related development added.</td>
<td><ul>
<li><blockquote>
<p>Project Manager<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Lead Developer/Technical Writer REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>2/2/2016</td>
<td>1.1</td>
<td>Updated dependencies list</td>
<td><ul>
<li><blockquote>
<p>Project Manager<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Lead Developer/Technical Writer REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>7/22/2015</td>
<td>1.0</td>
<td>Baselined at Version 1.0 per request from VA PM on 22 July 2015, so that document can be submitted to VA COR for final approval.</td>
<td><ul>
<li><blockquote>
<p>Project Manager<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Lead Developer/Technical Writer REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>
Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Software Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Electronic Remittance Advice (ERA) Compliance Fee Basis Patch (FB\*3.5\*158) addresses enhancements to VistA Fee Basis and its compliance to Committee on Operating Rules for Information Exchange (CORE) Level III Electronic Remittance Advice (ERA) / Electronic Funds Transfer (EFT) standards, as part of the Health Administration Product Enhancements (HAPE) Electronic Data Interchange (EDI) Purchased Care (PC) software enhancement project.

## Document Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides installation and setup steps for Fee Basis Patch FB\*3.5\*158. It is intended for VistA administrators at Veterans Affairs (VA) facilities, and it assumes familiarity with installing Kernel Installation and Distribution System (KIDS) file distributions on VistA servers.

### Additional Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software and Documentation Retrieval Instructions:

----------------------------------------------------

Software being released as a host file and/or documentation describing the new functionality introduced by this patch are available.

The preferred method is to retrieve files from REDACTED. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

Hines: REDACTED

Salt Lake City: REDACTED

Documentation can also be found on the VA Software Documentation Library at:

<http://www.va.gov/vdl/>

Title File Name

-----------------------------------------------------------------------

Fee Basis User Manual FB_3_5_UM_R1217.PDF

Fee Basis Technical Manual FB_3_5_TM_R1217.PDF

/Security Guide

Fee Basis Install Guide FB_3_5_P158_IG.PDF

Fee Basis Release Notes FB_3_5_P158_RN.PDF

#### ## Test Site Acknowledgment

The planned test sites for Fee Basis Patch FB\*3.5\*158 are the following:

- redacted

# Software Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fee Basis Patch FB\*3.5\*158 is a KIDS software release.

## Software Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches *<u>must</u>* be installed prior to FB\*3.5\*158:

| Software | Version | Required Patches |
|--------------|-------------|----------------------|
| Fee Basis    | 3.5         | FB\*3.5\*73          |
| Fee Basis    | 3.5         | FB\*3.5\*91          |
| Fee Basis    | 3.5         | FB\*3.5\*127         |
| Fee Basis    | 3.5         | FB\*3.5\*128         |
| Fee Basis    | 3.5         | FB\*3.5\*153         |
| Fee Basis    | 3.5         | FB\*3.5\*154         |
| Fee Basis    | 3.5         | FB\*3.5\*157         |

# Patch Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File Name (Number) Field Name (Number) New/Modified/Deleted

------------------ ------------------- --------------------

FEE BASIS SITE PARAMETERS NEXT BATCH NUMBER (#10) Modified

(#161.4)

FEE BASIS BATCH (#161.7) NUMBER (.01) Modified

ADJUSTMENT REASON REMITTANCE REMARK (5) New

(#161.91) CORE SCENARIO (6) New

ADJUSTMENT GROUP (7) New

REMITTANCE REMARK ADJUSTMENT GROUP (3) New

(#161.93)

FEE BASIS PAYMENT (#162) ADJUSTMENT (162.08,1) New

PAYMENT METHODOLOGY New

(162.03,82)

AUTHORIZATION NUMBER New

(162.03,83)

ATTACHMENT ID New

(162.03,84)

FEE BASIS PHARMACY INVOICE ADJUSTMENT (#162.15,1) New

(#162.1)

AUTHORIZATION NUMBER New

(162.11,40)

FEE BASIS INVOICE (#162.5) ADJUSTMENT (#162.559,1) New

AUTHORIZATION NUMBER New

(162.5,88)

ATTACHMENT ID New

(162.5,91)

PAYMENT METHODOLOGY New

(162.5,90)

FEE BASIS PAYMENT New

METHODOLOGY (#163.98)

## Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mail Group Name New/Modified/Deleted

--------------- --------------------

N/A

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Option Name Type New/Modified/Deleted

----------- ---- --------------------

FBAA BATCH 7YR PURGE run routine New

ZTMQUEUABLE OPTIONS menu Modified

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Security Keys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Templates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Template Name Type File Name (Number) New/Modified/Deleted

------------- ---- ------------------ --------------------

FBCH EDIT PAYMENT INPUT FEE BASIS INVOICE (162.5) Modified

FBCH ENTER PAYMENT INPUT FEE BASIS INVOICE (162.5) Modified

FBNH EDIT PAYMENT INPUT FEE BASIS INVOICE (162.5) Modified

## Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no bulletins associated with this patch.

## Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional information is included with this installation guide.

## New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no NSRs associated with this patch.

## Patient Safety Issues (PSIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no PSIs associated with this patch.

## Estimated Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The estimated installation time for Fee Basis Patch FB\*3.5\*158 is less than one minute.

# Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre-Installation Instructions:

------------------------------

![](fb-3-5-158-install-guide/002.png)ALL Payment Batches MUST be Transmitted to Central Fee and have a status of 'Vouchered' prior to installing FB\*3.5\*158.

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users.  This patch should take less than 5 minutes to install.

There are no options to disable for this installation.

The post-installation routine, FBXIP158, will run to compile the modified input templates and remove the option, FB FPPS TRANSMIT, from its parent menu. It will also establish CARC/RARC relationships.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation will install new and modified routines, Data Dictionaries,

and Input Templates.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, use the following options. When prompted for the INSTALL enter the patch \# (FB\*3.5\*158):

![](fb-3-5-158-install-guide/003.png) It is very highly recommended that the installing person perform step 3a here to make a backup copy of the Transport Global and save this as a MailMan message.

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as Data Dictionaries (DDs) or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  When prompted with 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//'
6.  When prompted with 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
7.  When prompted with 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO.

> When prompted with 'Enter protocols you wish to mark as 'Out Of Order':' press \<return\>.

8.  If prompted with "Delay Install (Minutes): (0 - 60): 0// respond with 0.

# Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REQUIRED: With this patch the method of batch transmissions will change, transmissions will now go through Central Feed instead Vitria. The Vitria feed must be shut down to prevent duplicate claims from being processed. To shut down the Vitria fee the option, FB FPPS TRANSMIT, needs to be removed from TaskManager three days after the FB\*3.5\*158 installation; the Vitria feed may be shut down during business hours.

1.  In the EVE Systems Manager Menu, when prompted with ‘Select Systems Manager Menu Option:’answer Taskman Management.
2.  When prompted with ‘Select Taskman Management Option:’ answer Schedule/Unschedule Options.
3.  When prompted with ‘Select OPTION to schedule or reschedule:’ answer FB FPPS TRANSMIT.
4.  When prompted with ‘Transmit Invoices to FPPS...OK? Yes//’ press \<return\>.
5.  When prompted with ‘Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to. COMMAND:’ answer N.
6.  In the ‘Option Name:’ field, enter @.
7.  When prompted with ‘Are you sure you want to delete this entire record (Y/N)?’ answer Yes.

OPTIONAL: The option, FBAA BATCH 7YR PURGE, can now be scheduled to run monthly in TaskManager. It is recommended that the task be scheduled for off-hours when users are not on the system.

# Routine Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second line of each of these routines now looks like:

;;3.5;FEE BASIS;\*\*\[Patch List\]\*\*;JAN 30, 1995;Build 94

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](fb-3-5-158-install-guide/004.png)</th>
<th><p><strong>NOTE:</strong> The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.</p>
<p>Routine Name: FBAACIE</p>
<p>Before: B16604968 After: B17356437 38,61,91,154,158</p>
<p>Routine Name: FBAACO2</p>
<p>Before: B31897549 After: B33011458 4,55,61,77,116,122,133,108,</p>
<p>135,139,123,157,158</p>
<p>Routine Name: FBAACO3</p>
<p>Before: B58658444 After: B57937070 4,38,55,61,116,122,133,108,</p>
<p>124,143,139,157,154,158</p>
<p>Routine Name: FBAADOB</p>
<p>Before: B2793564 After: B2800687 158</p>
<p>Routine Name: FBAAEPI</p>
<p>Before: B33105165 After: B32470147 38,61,124,132,123,154,158</p>
<p>Routine Name: FBAAFR</p>
<p>Before: B2615408 After: B13991294 61,158</p>
<p>Routine Name: FBAAMP</p>
<p>Before:B134317556 After:B133720533 4,21,38,55,61,67,116,108,143,</p>
<p>123,154,158</p>
<p>Routine Name: FBAAMP1</p>
<p>Before: B12344888 After: B12388857 4,55,61,77,139,158</p>
<p>Routine Name: FBAAPET</p>
<p>Before: B51663555 After: B51739856 4,38,55,61,77,116,122,133,</p>
<p>108,124,132,139,123,154,158</p>
<p>Routine Name: FBAAPP0</p>
<p>Before: B4309645 After: B4339891 61,91,158</p>
<p>Routine Name: FBAAUTL</p>
<p>Before: B26368074 After: B36872113 101,114,108,124,127,158</p>
<p>Routine Name: FBAAUTL3</p>
<p>Before: B4132421 After: B4122598 132,158</p>
<p>Routine Name: FBAAV0</p>
<p>Before: B56393278 After: B76214254 3,4,55,89,98,116,108,132,139,</p>
<p>123,158</p>
<p>Routine Name: FBAAV01</p>
<p>Before: B27989531 After: B48459341 89,98,108,123,158</p>
<p>Routine Name: FBAAV1</p>
<p>Before: B29697333 After: B29696707 10,36,39,98,158</p>
<p>Routine Name: FBAAV2</p>
<p>Before: B17032694 After: B39413585 3,89,98,116,108,123,158</p>
<p>Routine Name: FBAAV3</p>
<p>Before: B3409907 After: B4896340 3,89,116,132,158</p>
<p>Routine Name: FBAAV4</p>
<p>Before: B39089780 After: B39332795 13,34,37,70,146,127,153,158</p>
<p>Routine Name: FBAAV5</p>
<p>Before:B101588501 After:B139989645 3,55,89,98,116,108,139,123,158</p>
<p>Routine Name: FBAAV8</p>
<p>Before:B119931377 After:B120330474 123,158</p>
<p>Routine Name: FBAAVR5</p>
<p>Before: B40211184 After: B40211366 132,158</p>
<p>Routine Name: FBBPG7Y</p>
<p>Before: n/a After: B8669207 158</p>
<p>Routine Name: FBCHEAP</p>
<p>Before: B21240885 After: B21016855 38,55,61,77,154,158</p>
<p>Routine Name: FBCHFR</p>
<p>Before: B2637264 After: B8623931 61,158</p>
<p>Routine Name: FBCHPET</p>
<p>Before: B44036498 After: B43033601 4,38,61,77,116,108,124,132,</p>
<p>123,154,158</p>
<p>Routine Name: FBNHEP1</p>
<p>Before: B9319871 After: B9136492 12,61,158</p>
<p>Routine Name: FBRXFR</p>
<p>Before: B2618713 After: B9233192 61,158</p>
<p>Routine Name: FBSVBR</p>
<p>Before: B72554273 After: B79485755 131,132,158</p>
<p>Routine Name: FBSVVA</p>
<p>Before: B19365869 After: B22383786 131,132,158</p>
<p>Routine Name: FBUTL1</p>
<p>Before: B14646555 After: B19606435 61,158</p>
<p>Routine Name: FBUTL2</p>
<p>Before: B53713039 After: B70356259 61,73,158</p>
<p>Routine Name: FBUTL4</p>
<p>Before: B23579110 After: B26671787 61,158</p>
<p>Routine Name: FBUTL4A</p>
<p>Before: n/a After: B30641813 61,158</p>
<p>Routine Name: FBX2P158</p>
<p>Before: n/a After:B176094799 158</p>
<p>Routine Name: FBXIP158</p>
<p>Before: n/a After: B8013846 158</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Back-out and Roll-back Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event that a site determines, for whatever reason, that they need to uninstall the HAPE EDI PC – ERA Compliance patch (FB\*3.5\*158) and return their system to the way it was before this patch was installed, please follow these instructions. For the purpose of this discussion, the back-out procedure will include the actual software that needs to be removed. This would include both VistA routines and VistA input templates. The roll-back procedure will include a discussion of data dictionaries that are created by this patch.

It is recommended that sites log a Remedy ticket if it is a nationally released patch; otherwise, the site should contact the product development team directly for specific solutions to their unique problems.

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 2 build components that need to be uninstalled here: existing Fee Basis routines and existing Fee Basis Input Templates. The existing Fee Basis routines may be restored from the backup MailMan PackMan message that should have been created in step 3.a. in section 5, Installation Instructions (“Backup a Transport Global”). There are three input templates that need to be restored to the previous version. They are listed in section 3.7 of this document in the Templates section. They are named \[FBCH EDIT PAYMENT\], \[FBCH ENTER PAYMENT\], and \[FBNH EDIT PAYMENT\]. It is not standard practice to proactively backup input templates before patch installation. Therefore, in order to restore these input templates to the pre-patch FB\*3.5\*158 state, a new patch will be required to be sent to the target site and installed. Please contact Product Support in this case for further instructions. Product Support will work closely with the site and with the VistA Fee Basis development team.

## Roll-back Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following data dictionaries will need to be restored to the pre FB\*3.5\*158 versions:

Required: Due to the introduction of new X-References and supporting code to manage them, these DDs must be restored.

FEE BASIS PAYMENT (#162)

FEE BASIS PHARMACY INVOICE (#162.1)

FEE BASIS INVOICE (#162.5)

ADJUSTMENT REASON (#161.91)

REMITTANCE REMARK (#161.93)

Optional: *One field in each file was expanded to accommodate larger input values. There should be no significant impact to system performance if these changes remain.*

FEE BASIS SITE PARAMETERS (#161.4)

FEE BASIS BATCH (#161.7)

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: FB*3.5*132 Install Guide

## Test Site Acknowledgment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Fee and IFCAP Automation Enhancements project team would like to thank the following test sites for their assistance in testing Patch FB\*3.5\*132:

- REDACTED

## Patches Installed Together

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following four patches are related and must be installed at the same time to avoid application/processing errors. The recommended patch install order is as follows:

<table>
<colgroup>
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 62%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Order</strong></th>
<th><strong>Software</strong></th>
<th><strong>Version</strong></th>
<th><strong>Required Patches</strong></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">1.</td>
<td>IFCAP</td>
<td>5.1</td>
<td><p>PRC*5.1*162</p>
<p>If the IFCAP package is <em><u>not</u></em> installed at a site, then there is no need to install patch PRC*5.1*162.</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">2.</td>
<td>Fee Basis</td>
<td>3.5</td>
<td><p>FB*3.5*132</p>
<p>If the FEE BASIS package is not installed at a site then there is no need to install patch FB*3.5*132.</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">3.</td>
<td>Generic Code Sheet</td>
<td>2.0</td>
<td>GEC*2.0*35</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">4.</td>
<td>Fee Basis Claims System (FBCS)</td>
<td>3.2</td>
<td><p>DSIF*3.2*34</p>
<p>If the FEE BASIS CLAIMS SYSTEM (FBCS) is not installed at a site then there is no need to install patch DSIF*3.2*34.</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">![](fb-3-5-132-install-guide/003.png)</td>
<td colspan="5"><strong>ALERT:</strong> Please review the installation instructions of all the applicable patches before installing any of these patches to ensure all applicable patches can be installed at the same time.</td>
</tr>
</tbody>
</table>

## Patch Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File Name (Number) Field Name (Number) New/Modified/Deleted

------------------ ------------------- --------------------

FEE BASIS PAYMENT FILE \# (#.01) Modified

MOVES (#161.45) NEW IENS (#2) Modified

FEE BASIS BATCH (#161.7) STATUS (#11) Modified

FINALIZED WITH VISTA New

(#20)

VOUCHER MSG DATE New

(#21)

VOUCHER MSG ACK New

STATUS (#22)

STATUS SET TO New

RETRANSMIT BY (#23)

STATUS SET TO New

RETRANSMIT DATE (#24)

TRANSMITTED BATCH New

WAS REJECTED (#25)

FEE BASIS PAYMENT REJECT All New

CODE (#161.99)

FEE BASIS PAYMENT (#162)

SERVICE PROVIDED (#162.03) BATCH NUMBER (#7) Modified

INVOICE NUMBER (#14) Modified

INTERFACE REJECT New

(#21.3)

REJECT CODE (#21.6) New

REJECT CODE (#162.031) All New

TRAVEL PAYMENT DATE INTERFACE REJECT New

(#162.04) (#6.3)

REJECT CODE (#6.6) New

REJECT CODE (#162.041) All New

FEE BASIS PHARMACY INVOICE

(#162.1)

PRESCRIPTION NUMBER INTERFACE REJECT New

(#162.11) (#19.3)

REJECT CODE (#19.6) New

REJECT CODE (#162.111) All New

FEE BASIS INVOICE (#162.5) INTERFACE REJECT New

(#15.3)

REJECT CODE (#15.6) New

REJECT CODE (#162.515) All New

### Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mail Group Name New/Modified/Deleted

--------------- --------------------

FEE FINANCE New

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Option Name Type New/Modified/Deleted----------- ---- --------------------

FB PAYMENT AGING RPT run routine New

FBAA FINALIZE BATCH run routine Modified

FBAA OUTPUTS MENU menu Modified

FBAA REPROCESS BATCH run routine New

FBAA RESEND VOUCHER MSG run routine New

FBAA SUPERVISOR OPTIONS menu Modified

FBAA VOUCHER DELETE REJECT run routine Modified

FBCH OUTPUT MENU menu Modified

### Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Security Keys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- FBAAFINANCE
- FBAAREJECT

### Templates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bulletin Name comment------------- -------

FBAA SERVER new

### Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FEE BASIS PAYMENT REJECT CODE (#161.99) file will be exported with data.

### New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Fee and IFCAP automation enhancement (#20110212).

### Patient Safety Issues (PSIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Estimated Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The estimated installation time for Fee Basis Patch FB\*3.5\*132 is less than five minutes.

### From: FB*3.5*163 Install Guide

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These three patches have enhancements that extend the capabilities of the Veterans Health Information Systems and Technology Architecture (VistA), Accounts Receivable (PRCA), Fee Basis (FB), and Integrated Billing (IB). Below is a list of all the applications involved in this project along with their patch number:

<span id="_Toc475710928" class="anchor"></span>Table ‑ List of Applications

| Application/Version         | Patch          |
|-----------------------------|----------------|
| ACCOUNTS RECEIVABLE V 4.5   | PRCA\*4.5\*310 |
| FEE BASIS (FB) V 3.5        | FB\*3.5\*163   |
| INTEGRATED BILLING (IB) 2.0 | IB\*2.0\*554   |

The patches (PRCA\*4.5\*310, FB\*3.5\*163, and IB\*2.0\*554) are being released in the Kernel Installation and Distribution System (KIDS).

The Chief Business Office (CBO) is requesting system enhancements to the Veterans Health Information Systems and Technology Architecture (VistA) Integrated Billing (IB), Accounts Receivable (AR), and Fee Basis (FB) software modules that would allow segregating all billing and Collection activities for Non-Department of Veterans Affairs (Non-VA) Care Third Party Insurance carriers' reimbursement.

Current Medical Care Collections Fund (MCCF) Third Party billing and collections applications in the VistA information system do not segregate the Non-VA care claims from those claims for service rendered at Veterans Health Administration (VHA) healthcare facilities. This makes it difficult to determine whether all monies due VA for Non-VA care services are being billed and collected from Third Party insurance carriers, where applicable. The current process is a resource intensive, manual process with no assurance that all applicable Non-VA Care charges have been billed and collected.

This project will improve and automate the transfer of data from VistA Fee Basis to Integrated Billing. It will record Non-VA revenue in a different fund to allow separate tracking of these revenues. The patch makes the following changes and enhancements:

- System to automatically populate information entered in VistA Fee Basis authorizations into VistA IB software to accelerate claims for Non-VA health care services.
- Assist the VA Medical Centers in obtaining timely precertification from third party payers before care is rendered.
- Enhancements to the Potential Cost Recovery Report removed Service Connected decision and added additional display fields.
- Added CHOICE program fields to the Fee Basis Contract File.

### Document Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this patch is available from the VA SFTP server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

Albany: REDACTED

Hines: REDACTED

Salt Lake City: REDACTED

Documentation can also be found on the VA Software Documentation Library at:

<http://www.va.gov/vdl/>

File Description File Name

----------------------------------------------------------------------------------------

Installation Guide FB_3_5_163_ig.pdf

Release Notes FB_3_5_163_rn.pdf

User Manual FB_3_5_163_um.pdf

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch can install with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

- The install order must be: PRCA\*4.5\*310, IB\*2.0\*554, FB\*3.5\*163

  These patches must install before FB\*3.5\*163 can be installed:
- FB\*3.5\*154
- IB\*2\*528
- IB\*2\*530
- IB\*2\*554
- PRCA\*4.5\*310
- FB\*3.5\*166

## Pre/Post-Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Retrieval 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*163 must be retrieved from FORUM. The resulting email should then be forwarded to the local server for installation.

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vista Installation Instructions

Users should not be impacted by the application while the patch is being installed. This VistA patch should take less than 5 minutes to install.

1.  Once the email with the build is received, extract the distribution.
2.  Next from the Installation Menu, users may elect to use the following options. When prompted for the INSTALL name enter the patch FB\*3.5\*163:
1.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
2.  Print Transport Global – This option allows the user to print the Transport Global Report
3.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD’s, templates, etc.).
4.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD’s or templates.
3.  From the Installation Menu, select the Install Package(s) option and enter FB\*3.5\*163.
4.  <u>If</u> prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’ answer NO and press enter.
5.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? YES//’ answer NO and press enter.
6.  When prompted 'Want to DISABLE Scheduled Options, Menu Options and Protocols? YES//' answer YES and press enter.
1.  When prompted ‘Enter options you wish to mark as ‘Out of Order’ enter FB PCR
7.  <u>If</u> prompted ‘Delay Install (Minutes): (0 – 60): 0//’ respond 0 and press enter.
8.  There are no installation routines to delete.

## Routine Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the routine(s) included in this build. The second line of each routine will look as follows:

3.5;FEE BASIS;\*\*\[patch list\]\*\*;JAN 30, 1995;

Using New CheckSum (CHECK1^XTSUMBLD) verify Checksums:

Routine New

----------------------------------------------------------------

FBAACFE value = 2043443

FBPCR value = 129969114

FBPCR2 value = 114255841

FBPCR3 value = 37091499

FBPCR671 value = 51983526

## Post-Install Routine Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no post-install routine associated with this patch.

### From: FB*3.5*146 Install Guide

### Document Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this bundle is available.

The preferred method is to FTP the files from REDACTED/. This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

Albany REDACTED \<REDACTED\>

Hines REDACTED \<REDACTED\>

Salt Lake City REDACTED \<REDACTED\>

The documentation will be in the form of Adobe Acrobat files.

Documentation can also be found on the VA Software Documentation Library at: <http://www.va.gov/vdl/>

File Description File Name FTP Mode

-----------------------------------------------------------------------------------------------

Fee Basis User Manual fb3_5um.pdf Binary

PIMS v5.3 ADT User Manual Registration dg_5_3_reg_um.pdf Binary

The procedure guide, Care for Newborn of Women Veterans, located at [http://nonvacare.hac.med.va.gov/policy- programs/procedure-guides.asp](http://nonvacare.hac.med.va.gov/policy-%20programs/procedure-guides.asp), should be distributed to those personnel registering newborns and/or processing newborn claims.

### From: FB*3.5*135 Install Guide

## FB\*3.5\*135

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## December 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Version 1.3 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Office of Information and Technology (OIT) Product Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 11%" />
<col style="width: 43%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>July 6, 2012</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td>Initial document creation</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sept 18, 2012</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td>FB UCID UTILITY MENU update</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>November 7, 2012</p>
</blockquote></td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td>Updated Post Installation Instructions</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Dec. 11,2012</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td>Updated from patch review feedback</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ii Fee Basis FB\*3.5\*135 Installation Guide December 2012
