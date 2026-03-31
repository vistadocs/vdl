---
title: PXRM*2*22 Teratogenic Medications Order Checks Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Teratogenic Medications Order Checks
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*22
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - reminder
  - order
  - check
  - medications
  - table
  - group
  - teratogenic
  - checks
  - orderable
  - install
page_count: 0
word_count: 4313
section_count: 10
table_count: 3
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: July 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_22_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_22_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-22-teratogenic-medications-order-checks-installation-guide/001.png)

PXRM\*2\*22OR\*3\*357

Clinical Reminders

TERATOGENIC MEDICATIONS ORDER CHECKS

INSTALLATION GUIDE

July 2012

Product Development

Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [This patch releases two new National Reminder Order Checks for placing Teratogenic Medications. A pre-installation routine will identify any previously identified components and rename them correctly, and the patch installation will create or overwrite VA-named, national reminder components](#this-patch-releases-two-new-national-reminder-order-checks-for-placing-teratogenic-medications-a-pre-installation-routine-will-identify-any-previously-identified-components-and-rename-them-correctly-and-the-patch-installation-will-create-or-overwrite-va-named-national-reminder-components)
  - [This patch also addresses two bug fixes in the Reminder Order Check setup. To address these fixes, the Reminder Order Check System had to be divided into two files:](#this-patch-also-addresses-two-bug-fixes-in-the-reminder-order-check-setup-to-address-these-fixes-the-reminder-order-check-system-had-to-be-divided-into-two-files)
  - [## Clinical Reminders PXRM\2\22 Documentation](#clinical-reminders-pxrm222-documentation)
    - [### Web Sites](#web-sites)
  - [# Pre-Installation](#pre-installation)
  - [Required Software for PXRM\2\22](#required-software-for-pxrm222)
  - [## ## Estimated Installation Time: 10-15 minutes](#estimated-installation-time-10-15-minutes)
  - [## Pre-Installation Step:](#pre-installation-step)
  - [# Installation](#installation)
  - [Backup a Transport Global](#backup-a-transport-global)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [Appendix B: Creating a list of Orderable Item Groups and Order Checks](#appendix-b-creating-a-list-of-orderable-item-groups-and-order-checks)
- [Appendix C: Frequently Asked Questions (FAQ) about the Teratogenic Medications Order Check](#appendix-c-frequently-asked-questions-faq-about-the-teratogenic-medications-order-check)
- [Acronyms](#acronyms)
    - [### National Acronym Directory:](#national-acronym-directory)
The build for this patch is distributed as part of a multi-package build that contains PXRM\*2.0\*22 and OR\*3.0\*357. The multi-package build name is TERATOGENIC MEDICATIONS ORDER CHECKS 1.0.

## This patch releases two new National Reminder Order Checks for placing Teratogenic Medications. A pre-installation routine will identify any previously identified components and rename them correctly, and the patch installation will create or overwrite VA-named, national reminder components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## This patch also addresses two bug fixes in the Reminder Order Check setup. To address these fixes, the Reminder Order Check System had to be divided into two files:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- File 801 Reminder Order Check Items Group

> File 801 contains the grouping of Orderable Items. This file has also been modified to allow groups to include entries from the Drugs file, file \#50, VA Generic file, file \#50.6 and VA Drug Class file, file \# 50.605.

- File 801.1 Reminder Order Check Rules.

> File 801.1 contains the Reminder Order Check Rules.

These changes will allow sites to modify the Active and Testing Fields for National Rules.

This patch also fixes a Mumps error when the select order checks prompt times out.

To support the two-file structures, the existing menu options have been renamed and two new options will be released with this patch: Reminder Order Check Rule Inquiry and Reminder Order Check Test. The method for creating and editing Reminder Order Checks has been modified to use ScreenMan forms. See the Reminders Manager’s Manual for further instructions.

## ## Clinical Reminders PXRM\*2\*22 Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Documentation</strong></td>
<td><strong>Documentation File name</strong></td>
</tr>
<tr class="even">
<td>Clinical Reminders Installation Guide</td>
<td><p>PXRM_2_22_IG.PDF</p>
<p>PXRM_2_22_IG.DOC</p></td>
</tr>
<tr class="odd">
<td>Clinical Reminders Manager’s Manual</td>
<td><p>PXRM_2_22_MM.PDF</p>
<p>PXRM_2_22_MM.DOC</p></td>
</tr>
<tr class="even">
<td><span id="_Toc480020407" class="anchor"></span>Clinical Reminders Release Notes</td>
<td><p>PXRM_2_22_RN.PDF</p>
<p>PXRM_2_22_RN.DOC</p></td>
</tr>
</tbody>
</table>

### ### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                       |                                                           |                                                                                            |
|---------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Site                              | URL                                                   | Description                                                                            |
| National Clinical Reminders site      | <http://vista.med.va.gov/reminders>                       | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | <http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx> | This committee directs the development of new and revised national reminders               |
| VistA Document Library                | <http://www.va.gov/vdl/>                                  | Contains manuals for Clinical Reminders and                                                |

## # Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual describes how to install the bundled patches, PXRM\*2\*22 and OR\*3\*357.

## Required Software for PXRM\*2\*22

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package/Patch</strong></td>
<td><strong>Namespace</strong></td>
<td><strong>Version</strong></td>
<td><strong>Comments</strong></td>
</tr>
<tr class="even">
<td>Clinical Reminders</td>
<td>PXRM</td>
<td>2.0</td>
<td><p>Fully patched</p>
<p>PXRM*2.0*18 required</p></td>
</tr>
<tr class="odd">
<td><p>GEN. MED. REC. – VITALS</p>
<p>GMRV*5*25</p></td>
<td>GMRV</td>
<td>5.0</td>
<td></td>
</tr>
<tr class="even">
<td>Health Summary</td>
<td>GMTS</td>
<td>2.7</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>HL</td>
<td>1.6</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>Kernel</td>
<td>XU</td>
<td>8.0</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td>XM</td>
<td>7.1</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td><p>NATIONAL DRUG FILE</p>
<p>PSN*4.0*176</p></td>
<td>PSN</td>
<td>4.0</td>
<td></td>
</tr>
<tr class="odd">
<td><p>Pharmacy Data Management</p>
<p>PSS*1.0*133</p></td>
<td>PSS</td>
<td>1.0</td>
<td></td>
</tr>
<tr class="even">
<td><p>Outpatient Pharmacy</p>
<p>PSO*7.0*299</p></td>
<td>PSO</td>
<td>7.0</td>
<td></td>
</tr>
<tr class="odd">
<td><p>RADIOLOGY/NUCLEAR MEDICINE</p>
<p>RA*5*56</p></td>
<td>RA</td>
<td>5.0</td>
<td></td>
</tr>
<tr class="even">
<td><p>TOOLKIT</p>
<p>XT*7.3*111</p></td>
<td>XT</td>
<td>7.3</td>
<td></td>
</tr>
<tr class="odd">
<td>VA FileMan</td>
<td>DI</td>
<td>22</td>
<td>Fully patched</td>
</tr>
</tbody>
</table>

## ## ## Estimated Installation Time: 10-15 minutes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Pre-Installation Step:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please Note!

- All existing reminder order checks will need to be rebuilt after installation of PXRM\*2\*22. We recommend that you print a copy of any existing Reminder Orderable Item Groups (File \#801) on your system, using FileMan or Reminder Order Checks Inquiry. This will be used to help you re-create order checks after the install. See [Appendix B](#appendix-b-creating-a-list-of-orderable-item-groups-and-order-checks) for an example of using the Reminder Order Checks Inquiry to do this.

## # Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This build can be installed with users on the system, but it should be done during non-peak hours.

*The installation needs to be done by a person with DUZ(0) set to "@."NOTE: DO NOT QUEUE THE INSTALLATION, because this installation asks questions requiring responses and queuing will stop the installation. A Reminders Manager or CAC should be present to respond to these.*

1.  Print a copy of any existing Reminder Orderable Item Groups on your system. This will be used to help you re-create order checks after the install, since all existing reminder order checks will need to be rebuilt after installation of PXRM\*2\*22. See [Appendix B](#appendix-b-creating-a-list-of-orderable-item-groups-and-order-checks) for an example.
2.  Retrieve host file containing the multi-package build

> Use ftp to access the build (the name of the host file is TERATOGENIC \_MEDICATIONS \_ORDER_CHECKS.KID.) from one of the following locations:

> Albany REDACTED

> Hines REDACTED

> Salt Lake City REDACTED REDACTED

> NOTE: Download it as an ASCII type file.

3.  Install the build first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

4.  Load the distribution.

In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and TERATOGENIC \_MEDICATIONS_ORDER\_ CHECKS.KID.at the Host File prompt.

Example

> Select Installation Option: LOAD a Distribution

> Enter a Host File: TERATOGENIC \_MEDICATIONS \_ORDER_CHECKS.KID

> KIDS Distribution saved on NOV 17, 2011@11:53:53: OR\*3\*357 and PXRM\*2.0\*22

From the Installation menu, you may elect to use the following options:

## Backup a Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

2.  Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

3.  Verify Checksums in Transport Global

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

4.  Print Transport Global (optional)

> This option will allow you to view the components of the KIDS build.

5.  Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build TERATOGENIC MEDICATIONS ORDER CHECKS 1.0 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: TERATOGENIC MEDICATIONS ORDER CHECKS 1.0

Answer "YES" to the following prompt:

> \*BUT YOU ALREADY HAVE 'REMINDER ORDERABLE ITEM GROUP' AS FILE \#801!

> Shall I write over your REMINDER ORDERABLE ITEM GROUP File? YES// yes

Answer "NO" to the following prompts:

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// NO

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> NOTE:DO NOT QUEUE THE INSTALLATION, because this installation may ask questions requiring responses and queuing will stop the installation. The most common are replacements for finding items or quick orders during the installation of Reminder Exchange file entries.

> Installation Example

> See [Appendix A](\l).

6.  Install File Print (OPTIONAL)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

> Select Utilities Option: Install File Print

> Select INSTALL NAME: TERATOGENIC MEDICATIONS ORDER

7.  Build File Print (OPTIONAL)

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print

> Select BUILD NAME: TERATOGENIC MEDICATIONS ORDER CHECKS 1.0

> DEVICE: HOME//

8.  Post-installation routine

> The installation will add/update the following items on your system.

> Data Dictionary:

> ================

> FILE \# NAME

> 801 REMINDER ORDER CHECK ITEMS GROUP

> 801.1 REMINDER ORDER CHECK RULES

> Input Templates:

> ================

> PXRM EDIT ORDER CHECK FILE \#801 DELETE AT SITE

> Options:

> ========

> PXRM MANAGERS MENU

> PXRM ORDER CHECK MENU

> PXRM ORDER CHECK RULE EDIT

> PXRM ORDER CHECK RULE INQ

> PXRM ORDER CHECK TESTER

> PXRM ORDER CHK ITEMS GROUP EDT

> PXRM ORDER CHK ITEMS GROUP INQ

> Print Templates:

> ================

> PXRM ORDER CHECK ITEMS GROUP FILE \#801 SEND TO SITE

> PXRM ORDER CHECK RULE INQUIRY FILE \#801.1 SEND TO SITE

> Form:

> =====

> PXRM OCG EDIT FILE \#801 SEND TO SITE

> PXRM OCG EDIT HISTORY FILE \#801 SEND TO SITE

> PXRM OCG EDIT RESTRICTED FILE \#801 SEND TO SITE

> PXRM OCR EDIT FILE \#801.1 SEND TO SITE

> PXRM OCR EDIT HISTORY FILE \#801.1 SEND TO SITE

> PXRM OCR EDIT RESTRICTED FILE \#801.1 SEND TO SITE

> The installation will add the following item to the Reminder Exchange File:

> 811.8 VA-TERATOGENIC MEDICATIONS ORDER CHECKS

> The post-install routine will install all the components of this Exchange file entry on your system. After the installation has finished, if you discover that any of these components weren’t installed correctly, you can use the Reminder Exchange option on the Reminders Manager Menu to install them.

> After the exchange install, the following items should be in the corresponding files:

> File 801

> VA-TERATOGENIC MEDICATIONS (CAT D OR C) GROUP

> VA-TERATOGENIC MEDICATIONS (CAT X) GROUP

> File 801.1

> VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT D) RULE

> VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT X) RULE

9.  Use the printout of existing Reminder Orderable Item Groups on your system to re-create order checks. See the Clinical Reminders Manager’s Manual for guidance on using the new Reminders order checking system.
10. Add ADAPALENE/BENZOYL PEROXIDE to VA-TERATOGENIC MEDICATIONS (CAT D OR C) GROUP Pharmacy items. This is necessary because there is a duplicate in NDF file 50.6 for that name, and the patch install’s use of reminder exchange to create the entries cannot overcome that discrepancy. The decision was made to take it out of the patch and have folks add it manually. The product has extremely minimal use across the country anyway, so the risk if it’s missed is low.

Example

Select Reminder Managers Menu Option: ROC  Reminder Order Check Menu

Select Reminder Order Check Menu Option: GE  Add/Edit Reminder Order Check Items Group

Select Reminder Order Check Items Group by one of the following:

     N:  ORDER CHECK ITEMS GROUP NAME

     C:  VA DRUG CLASS

     D:  DRUG

     G:  VA GENERIC

     O:  ORDERABLE ITEM

     R:  ORDER CHECK RULE

     Q:  QUIT

Select Reminder Order Check Items Group by:  (N/C/D/G/O/R/Q): N// \<ENTER\>   ORDER CHECK ITEM GROUP NAME

Reminder Order Check Item Group: VA-

     1   VA-TERATOGENIC MEDICATIONS (CAT D OR C) GROUP 

     2   VA-TERATOGENIC MEDICATIONS (CAT X) GROUP 

CHOOSE 1-2: 1  VA-TERATOGENIC MEDICATIONS (CAT D OR C) GROUP

Press \<ENTER\> at the PHARMACY ITEM selection cursor

PHARMACY ITEM

+DG.VANADIUM                                                             

 DG.VANDETANIB                                                           

 DG.VARICELLA                                                            

 DG.VEMURAFENIB                                                          

 DG.VIGABATRIN                                                           

 DG.VINBLASTINE                                                          

 DG.VINCRISTINE                                                          

 DG.VINORELBINE                                                          

 DG.VORICONAZOLE                                                         

 DG.VORINOSTAT                                                           

 DG.YELLOW FEVER VACCINE                                                 

 DG.ZOLEDRONIC                                                           

 DG.ZOSTER VACCINE                                                       

 DG.ADAPALENE/BENZOYL PEROXIDE    *Note: You need to type at least        *

 *through the slash (‘/’) or the system will find the existing           * 

 *entry for DG.ADAPALENE instead.*                                         



When typing in DG.ADAPALENE/BENZOYL PEROXIDE, there will be two identical choices from which to select.  Pick the FIRST entry.

Another way to do this would be to type DG.\`4537 instead, to select the item by its internal entry number.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press \<PF1-C\> to close the PHARMACY ITEM pop-up window.

COMMAND:                                       Press \<PF1\>H for help    Insert

<u>GROUP NAME</u>: VA-TERATOGENIC MEDICATIONS (CAT D OR C) GROUP                  

PHARMACY ITEM LIST (377 entries)

ORDERABLE ITEM LIST (0 entries)

REMINDER ORDER CHECKS RULES LIST (1 entry)

<u>CLASS</u>: NATIONAL

SPONSOR:

REVIEW DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press Enter to edit the Orderable Item list.

Press \<PF1-E\> to exit and save the changes.

                               Edit History

Edit by: WHUSER,TWO on 02/03/2012@13:33:21

EDIT COMMENTS: 

Press \<ENTER\> at the EDIT COMMENTS selection cursor

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press Enter to add a description of the changes made.

==\[ WRAP \]==\[ INSERT \]========\< EDIT COMMENTS \>==========\[ \<PF1\>H=Help \]====

Added ADAPALENE/BENZOYL PEROXIDE per post-install instructions.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>===

                               Edit History

Edit by: WHUSER,TWO on 02/03/2012@13:33:21

EDIT COMMENTS: Added ADAPALENE/BENZOYL PEROXIDE per post-install instruction

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit     Save     Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

Press \<PF1-E\> again to exit and save the changes.

Select Reminder Order Check Items Group by one of the following:

     N:  ORDER CHECK ITEMS GROUP NAME

     C:  VA DRUG CLASS

     D:  DRUG

     G:  VA GENERIC

     O:  ORDERABLE ITEM

     R:  ORDER CHECK RULE

     Q:  QUIT

Select Reminder Order Check Items Group by:  (N/C/D/G/O/R/Q): N// q  QUIT

11. Evaluate and consider changing Teratogenic order checks from Testing to Production after evaluating the FAQs.

# Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter a Host File: (local path):\[HDS\]TERATOGENIC_MEDICATIONS_ORDER_CHECKS.KID

KIDS Distribution saved on Nov 22, 2011@18:11:58

Comment: NATIONAL TERATOGENIC MEDICATIONS ORDER CHECKS

This Distribution contains Transport Globals for the following Package(s):

TERATOGENIC MEDICATIONS ORDER CHECKS 1.0

PXRM\*2.0\*22

OR\*3.0\*357

Distribution OK!

Want to Continue with Load? YES// YES

Loading Distribution...

TERATOGENIC MEDICATIONS ORDER CHECKS 1.0

PXRM\*2.0\*22

OR\*3.0\*357

Use INSTALL NAME: TERATOGENIC MEDICATIONS ORDER CHECKS 1.0 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: teraTOGENIC MEDICATIONS ORDER CHECKS 1.0 11/29/11@12:5 1:16

=\> NATIONAL TERATOGENIC MEDICATIONS ORDER CHECKS ;Created on Nov 22, 201

This Distribution was loaded on Nov 29, 2011@12:51:16 with header of

NATIONAL TERATOGENIC MEDICATIONS ORDER CHECKS ;Created on Nov 22, 2011@18:11:58

It consisted of the following Install(s):

TERATOGENIC MEDICATIONS ORDER CHECKS 1.0 PXRM\*2.0\*22 OR\*3.0\*357

Checking Install for Package TERATOGENIC MEDICATIONS ORDER CHECKS 1.0

Install Questions for TERATOGENIC MEDICATIONS ORDER CHECKS 1.0

Checking Install for Package PXRM\*2.0\*22

Install Questions for PXRM\*2.0\*22

Incoming Files:

801 REMINDER ORDER CHECK ITEMS GROUP

\*BUT YOU ALREADY HAVE 'REMINDER ORDERABLE ITEM GROUP' AS FILE \#801!

Shall I write over your REMINDER ORDERABLE ITEM GROUP File? YES// yes

801.1 REMINDER ORDER CHECK RULES

811.8 REMINDER EXCHANGE (including data)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// NO

Checking Install for Package OR\*3.0\*357

Install Questions for OR\*3.0\*357

Want KIDS to INHIBIT LOGONs during the install? NO// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TCP

-----------------------------------------------------------------------------

Install Started for TERATOGENIC MEDICATIONS ORDER CHECKS 1.0 :

Nov 29, 2011@12:51:44

Build Distribution Date: Nov 22, 2011

Installing Routines:

Nov 29, 2011@12:51:44

Install Started for PXRM\*2.0\*22 :

Nov 29, 2011@12:51:44

Build Distribution Date: Nov 22, 2011

Installing Routines:

Nov 29, 2011@12:51:45

Running Pre-Install Routine: PRE^PXRMP22I

Removing old data dictionaries.

Deleting data dictionary for file \# 801

Installing Data Dictionaries:

Nov 29, 2011@12:51:45

Installing Data:

Nov 29, 2011@12:51:46

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

Installing INPUT TEMPLATE

Installing FORM

Installing OPTION

Nov 29, 2011@12:51:46

Running Post-Install Routine: POST^PXRMP22I

There are 1 Reminder Exchange entries to be installed.

1\. Installing Reminder Exchange entry VA-TERATOGENIC MEDICATIONS ORDER CHECKS

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*22 Installed.

Nov 29, 2011@12:51:48

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*357 :

Nov 29, 2011@12:51:48

Build Distribution Date: Nov 22, 2011

Installing Routines:

Nov 29, 2011@12:51:48

Updating Routine file...

Updating KIDS files...

OR\*3.0\*357 Installed.

Nov 29, 2011@12:51:48

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

TERATOGENIC MEDICATIONS ORDER CHECKS 1.0 Installed.

Nov 29, 2011@12:51:48

No link to PACKAGE file

Install Completed

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

# Appendix B: Creating a list of Orderable Item Groups and Order Checks 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you install PXRM\*2\*22, you can create a list of Reminder Orderable Item Groups and Order Checks that you may have on your local system. You can use either FileMan or the Reminder Orderable Item Inquiry on the Reminder Managers Menu.

FileMan Print File Entries Example

PRINT FILE ENTRIES 

OUTPUT FROM WHAT FILE: 801  REMINDER ORDERABLE ITEM GROUP

                                          (7 entries)

SORT BY: GROUP NAME// \<RETURN\>

START WITH GROUP NAME: FIRST// \<RETURN\>

FIRST PRINT FIELD: \[CAPTIONED       

  

Include COMPUTED fields:  (N/Y/R/B): NO// \<RETURN\> - No record number (IEN), no Computed Fields

Heading (S/C): REMINDER ORDERABLE ITEM GROUP LIST  Replace \<RETURN\>

DEVICE:  

Reminder Orderable Item Inquiry option on the Reminder Orderable Item Group Menu

   CF     Reminder Computed Finding Management ...

   RM     Reminder Definition Management ...

   SM     Reminder Sponsor Management ...

   TXM    Reminder Taxonomy Management ...

   TRM    Reminder Term Management ...

   LM     Reminder Location List Management ...

   RX     Reminder Exchange

   RT     Reminder Test

   OS     Other Supporting Menus ...

   INFO   Reminder Information Only Menu ...

   DM     Reminder Dialog Management ...

   CP     CPRS Reminder Configuration ...

   RP     Reminder Reports ...

   MST    Reminders MST Synchronization Management ...

   PL     Reminder Patient List Menu ...

   PAR    Reminder Parameters ...

   ROI    Reminder Orderable Item Group Menu ...

   XM     Reminder Extract Menu ...

   GEC    GEC Referral Report

Select Reminder Managers Menu Option: ROI  Reminder Orderable Item Group Menu

   OE     Add/Edit Reminder Orderable Item Group

   OI     Reminder Orderable Item Inquiry

   OT     Reminder Orderable Item Group Test

Select Reminder Orderable Item Group Menu Option: OI  Reminder Orderable Item Inquiry

Select Reminder Orderable Item Group by one of the following:

     N:  ORDERABLE ITEM GROUP NAME

     D:  DRUG CLASS

     O:  ORDERABLE ITEM

     R:  REMINDER DEFINITION

     T:  REMINDER TERM

     Q:  QUIT

Select Reminder Orderable Item Group by:  (N/D/O/R/T/Q): N//   ORDERABLE ITEM GROUP NAME

Select Reminder Order Check Rule: OTC ANTIHISTAMINES 

DEVICE: ;;99999999  TELNET PORT    Right Margin: 80//

REMINDER ORDERABLE ITEM GROUP INQUIRY        Feb 23, 2012 12:43:43 pm  Page 1

-----------------------------------------------------------------------------

OTC ANTIHISTAMINES                                               No. 1

-----------------------------------------------------------------------------

Class:                  LOCAL

Sponsor:               

Review Date:           

Group Description:

Drug Class List:

Orderable Item List:

    DIPHENHYDRAMINE ELIXIR

    DIPHENHYDRAMINE INJ,SOLN

    QUINIDINE TAB

    DIPHENHYDRAMINE CAP,ORAL

    DESIPRAMINE TAB

    DOXEPIN SOLN,ORAL

    AMITRIPTYLINE TAB

    DOXEPIN CAP,ORAL

    IMIPRAMINE TAB

    CLOMIPRAMINE CAP,ORAL

    IMIPRAMINE PAMOATE CAP,ORAL

    AMITRIPTYLINE INJ

    PROTRIPTYLINE TAB

    NORTRIPTYLINE CAP,ORAL

    NORTRIPTYLINE HCL 10MG/5ML SOLN,ORAL

    AMOXAPINE TAB

Reminder Rule List:            

           Rule Name: GLAUCOMA CHECK

        Display Name: Diagnosis of Glaucoma

         Active Flag: Yes

        Testing Flag: No

            Severity: Medium

  

       Reminder Term: GLAUCOMA Reminder Term Status: TRUE

    Order Check Text:

                      Use of first generation antihistamines is

                      contraindicated in the presence of narrow angle

                      glaucoma

  

    Rule Description:

                      This rule is true if the patient is found to have an

                      ICD9 diagnosis of Glaucoma

  

  

Select Reminder Orderable Item Group by one of the following:

     N:  ORDERABLE ITEM GROUP NAME

     D:  DRUG CLASS

     O:  ORDERABLE ITEM

     R:  REMINDER DEFINITION

     T:  REMINDER TERM

     Q:  QUIT

Select Reminder Orderable Item Group by:  (N/D/O/R/T/Q): N//

# Appendix C: Frequently Asked Questions (FAQ) about the Teratogenic Medications Order Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Q: What is a “teratogenic” medication?

A: A teratogenic medication is one that can increase the risk of birth defects if taken at a particular time during pregnancy. A known teratogen is a medication that causes birth defects in humans. Examples include thalidomide (limb defects), isotretinoin (syndrome of defects including oral clefts), valproic acid (neural tube defects), and mycophenolate (facial clefts, anotia). A potential teratogen is a medication that causes malformations or other abnormal pregnancy outcomes in animal studies – these outcomes are more concerning if they occur at doses similar to human doses. Some medications increase the risk for pregnancy loss (miscarriage), growth abnormalities (e.g., growth restriction), or functional deficits (e.g., decreased fetal kidney function). These are also important adverse reproductive effects.

Q: What is the new Teratogenic Medication Order Check?

A: In response to several requests, a CPRS Order Check was developed to remind providers when they prescribe a known or potential teratogen for a female patient of child-bearing potential. This reminder system is based on the FDA pregnancy categories (A, B, C, D, and X) and a set of additional criteria from First Data Bank that uses published literature and other available information. For lactating patients, the system also uses criteria to notify providers when a medication can cause serious side effects in a breastfeeding infant

Q: What are the FDA pregnancy categories?

A: The FDA categories are a helpful system for distinguishing the relative teratogenic risk of a medicine based on studies in animals and experience in human pregnancy. As a health care provider, your awareness of these issues can help you better prescribe for and counsel your female patients of child-bearing potential.

Q: How will the Teratogenic Medication Order Check work?

A: When a provider prescribes a medication with a pregnancy category D or X for a female patient between the ages of 18 and 50, the system will automatically provide an order check to ensure that you are aware of the reproductive risk associated with the medication. Certain additional medications with evidence of concern (e.g., some category C medications or FDA-unclassified medications) will also trigger an alert.

  
Q: What do you do if you get an Order Check?

A: (1) Consider whether this medication is most appropriate for the patient’s condition or whether there are other appropriate options with less reproductive risk.

> \(2\) Counsel the patient about the risks and benefits of treatment should pregnancy occur.

> \(3\) Ask the patient about pregnancy planning and use of contraception. This risk/benefit discussion is an important one.

> \(4\) For breastfeeding patients, consider whether there is an alternative medication with lower concentrations in breast milk or fewer risks for the infant and encourage the patient to discuss her medications with the infant’s pediatrician. LactMed (<http://toxnet.nlm.nih.gov/cgi-bin/sis/htmlgen?LACT>) is an online resource from the NIH that provides available information about use of medications during lactation.

Q: Where can I get information about the pros/cons of continuing use of a teratogenic medication during pregnancy?

A: Deciding whether to continue a potential or known teratogen during pregnancy is complicated. Not treating or under-treating a pregnant woman’s medical condition can be riskier to the fetus than the medication itself. It is helpful to read the pregnancy subsection of drug labeling, which provides information about the reproductive risks of medications. Current labeling can be found at Drugs@FDA or at [www.DailyMed.nlm.nih.gov](http://www.DailyMed.nlm.nih.gov). Reprotox is an online resource that summarizes available information about the reproductive risks of medications. Reprotox may be available online through your facility’s library and will be available through the VACO library in the near future. The Organization of Teratology Information Services has fact sheets available online about medications and their risks during pregnancy (<http://www.otispregnancy.org/otis-fact-sheets-s13037#1>).Your local pharmacist and women’s health providers can provide more information.

Q: How can I help my patients avoid unintended pregnancy?

A: About 50% of pregnancies in the United States are unplanned. During patient encounters, ask women of child-bearing potential (age 15 to 50) about their plans for pregnancy and need for contraception.

The most effective reversible contraceptives are the IUDs (Mirena or Paragard) and subdermal implants (Nexplanon, previously Implanon). These contraceptives are available through the VA prosthetics department and can be inserted by a local trained women’s health provider. Oral contraceptive pills and emergency contraception are on the VA formulary, and condoms are available through the VA. Female Veterans using contraceptives other than IUDs and implants should be advised to keep a supply of emergency contraception on hand in case of unprotected intercourse or contraceptive failure.

Q: When will the Order Check be available?

A: The Order Check will come as a VistA Clinical Reminders patch, PXRM\*2\*22.  At the time of this message, release is anticipated during the fourth quarter of calendar year 2012.

Q: How often will this Order Check appear?

A: Clinicians will be notified every time any category D or X medications or certain other medications with evidence for concern (e.g., some category C medications or FDA-unclassified medications) are ordered for a female patient of child-bearing potential who is without documentation of medical inability to become pregnant.

Q: Will the Order Check display even if the patient has no chance of becoming pregnant, such as post-hysterectomy?

A: No. The Order Check is designed to recognize several exclusion criteria that can be generally described as “medical inability to conceive.”  For example, patients for whom the appropriate ICD-9<sup>a</sup> code for hysterectomy is recorded will not trigger an alert.  Other ICD-9<sup>a</sup> exclusion criteria include menopausal state and IUD use.

Q: Can clinicians add information to the electronic health record that should exclude a patient from this Order Check?

A: Yes, each site can define additional situations or “Health Factors” when the Order Check does not apply. The local application support team can add these Health Factors to the Reminder Term called “VA-TERATOGENIC MEDICATIONS ORDER CHECK EXCLUSIONS (TERM).” The support team can also suggest to the Women’s Health Program Office that a Health Factor be added as part of a subsequent national update.

Points of Contact for further information about the Teratogenic Medications Order Check:

- Your facility’s pharmacy informaticist (ADPAC)
- Your facility’s clinical reminders manager (often one of the Clinical Application Coordinators)
- REDACTED at Pharmacy Benefits Management REDACTED
- REDACTED, Director Reproductive Health, Women Veterans Health Strategic Healthcare Group, REDACTED

<sup>a</sup> At the time of this message, the transition from ICD-9 to ICD-10 has not yet taken place

FDA Pregnancy categories

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong>Table 1. FDA Pregnancy categories</strong></p>
<p><strong>(language summarized from 21CFR201.57)</strong></p></td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td><strong>Definition</strong></td>
</tr>
<tr class="odd">
<td><strong>A</strong></td>
<td>Adequate and well-controlled (AWC) studies in pregnant women have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of a risk in later trimesters).</td>
</tr>
<tr class="even">
<td><strong>B</strong></td>
<td>Animal reproduction studies have failed to demonstrate a risk to the fetus and there are no AWC studies in pregnant women, OR animal studies demonstrate a risk and AWC studies in pregnant women have not during the first trimester (and there is no evidence of risk in later trimesters).</td>
</tr>
<tr class="odd">
<td><strong>C</strong></td>
<td>Animal reproduction studies have shown an adverse effect on the fetus, there are no AWC studies in humans, AND the benefits from the use of the drug in pregnant women may be acceptable despite its potential risks. OR animal studies have not been conducted and there are no AWC studies in humans.</td>
</tr>
<tr class="even">
<td><strong>D</strong></td>
<td>There is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, BUT the potential benefits from the use of the drug in pregnant women may be acceptable despite its potential risks (for example, if the drug is needed in a life-threatening situation or serious disease for which safer drugs cannot be used or are ineffective).</td>
</tr>
<tr class="odd">
<td><strong>X</strong></td>
<td>Studies in animals or humans have demonstrated fetal abnormalities OR there is positive evidence of fetal risk based on adverse reaction reports from investigational or marketing experience, or both, AND the risk of the use of the drug in a pregnant woman clearly outweighs any possible benefit (for example, safer drugs or other forms of therapy are available).</td>
</tr>
</tbody>
</table>

The FDA published a proposed rule in the May 29, 2008, Federal Register that proposes new labeling regulations for prescription drugs. These regulations, once implemented, will eliminate the pregnancy categories from drug labeling. When a final rule publishes, VHA will determine how to best update this order check process so that it will remain both current and useful to VA providers.

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OIT Master Glossary is available at: <http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm>

### ### National Acronym Directory:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<http://vaww1.va.gov/Acronyms/>
| Term    | Definition                                                     |
|---------|----------------------------------------------------------------|
| ASU     | Authorization/Subscription Utility                             |
| CPRS    | Computerized Patient Record System                             |
| ESM     | Enterprise Systems Management (ESM)                            |
| FIM     | Functional Independence Measure                                |
| GUI     | Graphical User Interface                                       |
| IAB     | Initial Assessment & Briefing                                  |
| MH      | Mental Health                                                  |
| MHA3    | Mental Health Assistant Version 3                              |
| MHV     | My Healthy Vet                                                 |
| MST     | Military Sexual Trauma                                         |
| OIT     | Office of Information and Technology                           |
| OIF/OEF | Operation Iraqi Freedom/Operation Enduring Freedom             |
| OR      | Order Entry namespace                                          |
| PCS     | Patient Care Services                                          |
| PD      | Product Development                                            |
| PTSD    | Post Traumatic Stress Syndrome                                 |
| PXRM    | Clinical Reminder Package namespace                            |
| RSD     | Requirements Specification Document                            |
| TIU     | Text Integration Utility                                       |
| VA      | Department of Veteran Affairs                                  |
| VHA     | Veterans Health Administration                                 |
| VistA   | Veterans Health Information System and Technology Architecture |
| WV      | Women’s Health package namespace                               |
| YS      | Mental Health package namespace                                |
