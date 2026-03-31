---
title: IB*2*457 Electronic Insurance Identification (eII) User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Electronic Insurance Identification (eII)
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*457
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: VistA Financial Annual Enhancements \#1Electronic Insurance Identification (eII)User Manual UpdatesPatch IB\2\457
audience: 
keywords: 
  - insurance
  - table
  - contents
  - extract
  - mail
  - ibcnf
  - redacted
  - group
  - notification
  - ready
page_count: 0
word_count: 2154
section_count: 14
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_p457_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_p457_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

VistA Financial Annual Enhancements \#1Electronic Insurance Identification (eII)User Manual UpdatesPatch IB\*2\*457

![](ib-2-457-electronic-insurance-identification-eii-user-manual/001.png)

June 2012

VISTA Health  
Systems Design & Development

Table of Contents

This page intentionally left blank.

# Document Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Document Purpose](#document-purpose)
- [Scope of Patch IB\2\457](#scope-of-patch-ib2457)
- [Updates to Electronic Insurance Identification (eII) User Manual](#updates-to-electronic-insurance-identification-eii-user-manual)
- [Enhancements](#enhancements)
  - [HMS Extract File Transfer to AITC](#hms-extract-file-transfer-to-aitc)
  - [HMS Results File Transfer to VAMCs](#hms-results-file-transfer-to-vamcs)
  - [File Upload to Insurance Buffer File](#file-upload-to-insurance-buffer-file)
  - [XML File to Business Office](#xml-file-to-business-office)
  - [Frequency of Extract Files](#frequency-of-extract-files)
  - [Notification Message of File Failure](#notification-message-of-file-failure)
  - [Notification Message of Acknowledgement](#notification-message-of-acknowledgement)
  - [Enable/Disable Access](#enabledisable-access)
- [Updates to Electronic Insurance Identification (eII)](#updates-to-electronic-insurance-identification-eii)
  - [Required Security Key](#required-security-key)
  - [Needed Mail Groups (all are new groups):](#needed-mail-groups-all-are-new-groups)
  - [Suggested Menus and Options:](#suggested-menus-and-options)
  - [Setup for the Electronic Insurance Identification (eII) Software:](#setup-for-the-electronic-insurance-identification-eii-software)
  - [IRM Adding Members to the IBCNF EII IRM and IBCNF EII XML READY Mailgroups:](#irm-adding-members-to-the-ibcnf-eii-irm-and-ibcnf-eii-xml-ready-mailgroups)
This document presents the new functionality provided by the Patch IB\*2\*457. As well as set up instructions for the software. The material presented in this document is provided in lieu of inserting revisions directly into the text of an existing user manual.

# Scope of Patch IB\*2\*457

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*457 provides new functionality to automate the VistA extract and insurance information exchange to provide a more efficient and secure insurance identification process.

The scope of the enhancement is limited to automating the HMS extract file transfer between VA Medical Centers (VAMCs) and the Austin Information Technology Center (AITC), with notification transactions going to VAMCs, the AITC as well as enabling and disabling access to the file transfer based on contract status.

The IRMs can validate HMS contract status with CPAC IV Manager responsible for the site.

If the site does not have a current contract with HMS (Health Management Systems) you still need to install the IB\*2\*457 patch.

If the site has a current contract with HMS, an HMS build that will also need to be installed VEHM 3.0 patch as well.

# Updates to Electronic Insurance Identification (eII) User Manual 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements discussed herein are provided to update users with information about the new functionality provided in Patch IB\*2\*457.

> **NOTE:** This patch is dependent on the IB\*2\*312 patch. Patch IB\*2\*312 must be installed prior to patch IB\*2\*457. If the site has an HMS contract, they will need to also load the VEHM patch as well.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this patch is to automate the Extract file transfer created by the HMS data extractor at the VAMCs, sending the data to the HMS Inc server via the AITC DMI Queue and an approved VPN.

The data sent will be used to identify patients’ current, active insurance.

HMS Inc., after processing the extract files, sends the result file back from through AITC DMI to the VAMC site so it can be uploaded to the Insurance Buffer file by the HMS Data Extractor. eII software alleviates the administrative burden to the IRM and HMS staff that manually transfers and collects data files from SharePoint, providing a more efficient and secure insurance identification process.

HMS/VEHM software must already be installed at the site for the extract process to work. Pre-installation instructions in the patch description describe how to check if the HMS software is on the system.

## HMS Extract File Transfer to AITC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HMS extracts from VistA will be routed automatically to a central server at AITC as MailMan messages, with no manual intervention from IRM or HMS. Each file is sent as one or more MailMan messages. When the extracts are transmitted, they will be removed from the directory.

Each VAMC may contract individually with HMS to receive up to four different insurance services: 

1.  HMS_NOINSUR – pulls patient information when there is no insurance on file
2.  HMS_ENHNOIN - pulls patient information when the records reflect Medicare but no other commercial insurance
3.  HMS_NORXINS - pulls patient information when there is no “Prescription Only” insurance on file
4.  HMS_NONVERINS – pulls patient information for re-verification purposes

<u>A site may only run the extracts identified in the current contract and must disable any extract in the event it is not included in a subsequent contract renewal. </u> The CPAC IV Manager is the COTR for each contract and is expected to communicate any changes in contract status to the IRM’s.

If the sites are currently using the HMS data extractor software, they can see which extracts are active by accessing that application.

Some facilities that are still not in CPAC.  Facilities that still have the MCCF department would need direction from the MCCF contact person, or perhaps the revenue manager of the facility.  
  
In addition, a programmer could look for your namespace routines using ^%RD and looking for VEHM\* routines:  
  
HMS3_PRE\>D ^%RD  
  
Routine(s): VEHM\*  
Routine(s):  
Long or Short form (L or S)? S =\>  
Find routines last modified since date:  
                 and on or before date:  
  
Display on  
Device:  
Right margin: 80 =\>  
  
                Short Listing of Selected Routine/Include Files  
                              Namespace: HMS3_PRE  
                         29 May 2012  1:49 PM   Page 1  
  
                                  --  .INT  --  
VEHM1P1   VEHM1P1A  VEHMAUP   VEHMBT    VEHMBWF   VEHMIN5A  VEHMINI   VEHMINI1......  
  
 or checking for your globals:  
  
HMS3_PRE\>D ^%GD  
  
Which globals? \* =\> VEHM\*  
Include system globals? No =\>  
Show global mappings? No =\>  
Device:  
Right margin: 80 =\>  
                      Global Directory Display of HMS3_PRE  
                              1:51 PM  May 29 2012  
VEHM                VEHMS  
  
2 globals listed

## HMS Results File Transfer to VAMCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AITC routes the HMS results to the VAMC that initiated the extract as MailMan messages. The eII software will extract the returning HMS results data from the MailMan messages, and place the resulting file in the designated VMS directory.

Members of the IBCNF EII IRM Mail Group will be notified when a results file has been received and saved to the designated HMS directory, and is ready to be uploaded to the Insurance Buffer.

When a notification message is in the Inbox, it will look like this when read:

Subj: HMS result file REDACTED VA442.TXT is ready \[#141308\] 03/01/12@19:06

2 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

HMS result file REDACTED VA442.TXT has been created and is ready to be uploaded to the insurance buffer file

> **NOTE:** The file names will have the number of the VAMC site. The file names shown in these messages are examples. Actual file names will vary by site.

## File Upload to Insurance Buffer File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eII software will send the IBCNF EII IRM mail group a notification when the results are in the directory. The IRM can upload the results to the VistA insurance buffer file. Once the results are uploaded to the insurance buffer file, the results file in the directory is deleted.

When a notification message is in the Inbox, it will look like this when read:

Subj: HMS result file REDACTED VA442.TXT is ready \[#141308\] 03/01/12@19:06

2 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

HMS result file REDACTED VA442.TXT has been created and is ready to be uploaded to the insurance buffer file

> **NOTE:** The file names will have the number of the VAMC site. The file names shown in these messages are examples. Actual file names will vary by site.

## XML File to Business Office

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HMS results file will be produced in XML format for the insurance verifiers in the Business Office; this file contains Medicare and Pharmacy information that cannot be uploaded to the insurance buffer file. The file will contain two additional fields: Patient Relationship to Insured ID and Patient ID. When this file is created, the IBCNF EII XML READY mail group will be notified.

Example of the XML File ready notification message:

Subj: HMS result XML file REDACTED VAXML442.XML is ready \[#141309\] 03/01/12@19:06

1 line

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

HMS result XML file REDACTED VA442.XML is ready to be retrieved

> **NOTE:** The file names will have the number of the VAMC site. The file names shown in these messages are examples. Actual file names will vary by site.

## Frequency of Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing HMS extract files shall continue to be produced on a monthly schedule. The exception to that are the reverification extract files; if your site is contracted for reverification services, the site may generate this extract as needed.

## Notification Message of File Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Automated notification messages will be sent to the IBCNF EII IRM mail group at the VAMC site if an HMS extract file is not generated by the HMS data extractor software at VAMCs, when expected, as defined in the IB SITE PARAMETERS file.

The notification message sent to this Mail Group looks like this:

Subj: Expected Extract files have not been created. \[#141551\] 03/02/12@13:52

3 lines

From: REDACTEDIn 'IN' basket. Page 1

-------------------------------------------------------------------------------

The following Extract file(s) have not been created yet:

VEHMH442.TXT

VEHMX442.TXT

Automated notification messages shall be sent to the members of the IBCNF EII IRM Mail group if a result file is not received from AITC when expected.

The notification message sent to this Mail Group looks like this:

Subj: Expected Result file has not been received. \[#143430\] 03/03/12@10:43

1 line

From: POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Expected Result file VA442.TXT has not been received yet

> **NOTE:** The file names will have the number of the VAMC site. These names are examples. Actual file names will vary by site.

## Notification Message of Acknowledgement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Automated acknowledgement messages are sent from AITC to the VAMCs acknowledging that the extract file message(s) are received by AITC. If the confirmation message(s) are not received within 24 hours, the IBCNF EII IRM mail group is notified, to start troubleshooting the issue.

## Enable/Disable Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eII Edit Configuration \[IBCNF EDIT CONFIGURATION\] option is used to enable/disable file transfer and/or or set other parameters for eII software.

# Updates to Electronic Insurance Identification (eII)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- IBCNF EDIT

## Needed Mail Groups (all are new groups):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the mail groups in this section are created during the patch installation and the person installing the patch will be asked to assign the mail group coordinator.

The following mail groups should only have a single member (REDACTED) which is automatically populated during patch installation.

- IBN
- IBK
- IBX
- IBH

The following mail groups are populated with the person installing the patch and a message is sent to that person indicating that other members may need to be added. CPAC IV Managers and other designated personnel will need to be added to the IBCNF EII XML READY mail group. IRMs should consult with the Business Office to determine appropriate members of this group.

- IBCNF EII IRM
- IBCNF EII XML READY

## Suggested Menus and Options: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Manage Mailman ... \[XMMGR\]
- Group/Distribution Management ... \[XMMGR-GROUP-MAINTENANCE\]
- Mail Group Edit \[XMEDITMG\]
- IB SITE MGR MENU \[System Manager's Integrated Billing Menu\]

## Setup for the Electronic Insurance Identification (eII) Software:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Integrated Billing Master Menu Option: IRM System Manager's Integrated Billing Menu

Enter IRM SYSTEM NANAGER’S INTEGRATED BILLING MENU:

REDACTED

Select System Manager's Integrated Billing Menu Option: eII Edit Configuration

REDACTED

INITIAL EII Edit Configuration:

The HMS directory is the directory that holds the extracts when they are created and is where the results file and the XML file reside when they are created.

> **NOTE:** Information shown in the screen is an example. Each VAMC site should validate the entries and update as needed.

REDACTD

REVIEW/CHANGE HMS DIRECTORY:

> **NOTE:** Directory name and file name are examples, the file name should contain the VAMC site number.

REDACTED

REVIEW/CHANGE settings for NONVERINS Extract file(s):

> **NOTE:** Directory name and file name are examples, the file name should contain the VAMC site number.

REDACTED

REVIEW/CHANGE settings for NOINSUR Extract file(s):

> **NOTE:** the Directory name and file name are examples, the file name should contain the VAMC site number.

REDACTED

REVIEW/CHANGE settings for ENHNOIN Extract file(s):

> **NOTE:** the Directory name and file name are examples, the file name should contain the VAMC site number.

REDACTED

REVIEW/CHANGE settings for NORXINS Extract file(s):

> **NOTE:** the Directory name and file name are examples, the file name should contain the VAMC site number.

REDACTED

Extract File Types:

NOINSUR - (HMS No Insurance Data Extract) Pulls patients with no insurance info on file.

ENHNOIN - (HMS Enhanced No Insurance Data Extract) pulls patients with only Medicare insurance on file and no commercial insurance.

NORXINS - (HMS No Prescription Insurance Extract) Pulls patients with active insurance that is not "Prescription Only" and identifies Prescription Only insurance in the monthly insurance matching process.

NONVERINS - (HMS Non-Verified Insurance Data Extract) Pulls patients treated within a user-specified date range WITH insurance information and where the insurance information has NOT been re-verified in the last six months (or other specified period). This file is also known as the reverification file.

> **NOTE:** For each of the extracts running at the site it is recommended that you set the expected day to 22 (twenty-two) and the days before late message is sent to 0 (zero)

The exception to this is the NONVERINS extract, which is run as needed.

## IRM Adding Members to the IBCNF EII IRM and IBCNF EII XML READY Mailgroups:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From Systems Managers Menu:

REDACTED

Select Manage Mailman

Select Group/Distribution Management:

REDACTED

Select Mail Group Edit for IBCNF EII IRM:

REDACTED

Select Mail Group Edit for IBCNF EII XML READY:

REDACTED