---
title: RA*5*47 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: RA
patch_ver: 5
patch_id: RA*5*47
group_key: RA:RA:5
file_numbers:
- '31'
- '70.02'
- '70.03'
- '81'
security_keys: []
menu_options: 0
description: Patch RA\5\47 adds a Study Instance User Identification (SIUID) to specific v2.4 HL7 event messages when an order is registered, an exam cancelled, an exam reaches the Examined status, or when a report is sent.
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 3106
section_count: 7
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: August 2011
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p47.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p47.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=384
audit_applied: '2026-05-31'
master_source: RA*5*47 Release Notes
master_pub_date: August 2011
consolidated_from: 12 versions
prior_versions:
- RA*5*185 Release Notes
- RA*5*226 Release Notes
- RA*5*56 Release Notes
- RA*5*70 Release Notes
- RA*5*75 Release Notes
- RA*5*77 Release Notes
- RA*5*80 Release Notes
- RA*5*81 Release Notes
- RA*5*82 Release Notes
- RA*5*84 Release Notes
- RA*5*99 Release Notes
consolidated_title: release notes
---

![](ra-5-47-release-notes/001.png)

Radiology/Nuclear Medicine  
Release Notes

Patch RA\*5.0\*47  
August 2011

Health Systems Design & Development

Provider Systems

# Release Notes for Patch RA\*5\*47


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes for Patch RA\5\47](#release-notes-for-patch-ra547)
  - [Overview](#overview)
  - [General Installation Notes](#general-installation-notes)
  - [Specific Installation Notes](#specific-installation-notes)
- [Patch RA\5\47 New Features](#patch-ra547-new-features)
  - [Options affected by the new SSAN](#options-affected-by-the-new-ssan)
- [Patch RA\5\47 Modified Features](#patch-ra547-modified-features)
- [After Installation of Patch RA\5\47](#after-installation-of-patch-ra547)
    - [Setting Up the Voice Recognition Event Driver Protocols](#setting-up-the-voice-recognition-event-driver-protocols)
- [Software and Documentation Retrieval](#software-and-documentation-retrieval)
  - [Software](#software)
  - [Documentation](#documentation)
Patch RA\*5\*47 is an enhancement patch to standardize the VistA RIS messaging interface to the current IHE specifications by updating the messages broadcast by Vista Radiology in accordance with HL7 version 2.4 standards.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch RA\*5\*47 adds a Study Instance User Identification (SIUID) to specific v2.4 HL7 event messages when an order is registered, an exam cancelled, an exam reaches the Examined status, or when a report is sent.

- The SIUID is a unique key that associates images to a particular study, which is required in messages sent to the Picture Archiving and Communications System (PACS). HL7 is the accepted protocol for transferring this information.
- The SIUID allows VistA Radiology to send event transactions to a commercial PACS directly, bypassing the VistA Digital Imaging and Communications in Medicine (DICOM) Text Gateway.
- The VA wants to accommodate commercial PACS and supply them with HL7 order messages and discontinue the use of the DICOM for the Radiology/Nuclear Medicine application.

Configuration instructions to set up the PACS for this are included with the VistA Imaging patch MAG\*3.0\*49, which must be installed *after* this patch.

## General Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Associated patches RA\*5\*90, RA\*5\*99, and RA\*5\*104 must be installed before you install patch RA\*5\*47.
- MailMan and Kernel patches must be current on the target system to avoid problems loading and installing patch RA\*5\*47.
- The install time for patch RA\*5\*47 is less than ten minutes.
- Because patch RA\*5\*47 impacts VistA HL7 messaging, it is best installed when system activity is minimal.
- The VistA Radiology and Voice Recognition interfaces must be shutdown.
1.  On the VistA-side, the shutdown of VistA Radiology means that all radiology logical links must be shutdown.
2.  Notify the Radiology department that the VistA Radiology application will be shutdown.
3.  This shutdown will impact the HL7 messaging between VistA Radiology, Voice Recognition, PACS, and VistA Imaging.

## Specific Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Patch RA\*5.0\*47 and Patch MAG\*3.0\*49 are closely related. Patch RA\*5.0\*47 must be installed first and Patch MAG\*3.0\*49 must be installed right after Patch RA\*5.0\*47. Each patch creates APIs used by the other and therefore must be installed in that order. 
- After both RA\*5.0\*47 and MAG\*3.0\*49 are installed and properly set up, you do not need the VistA DICOM Text Gateway to create the unique key for the commercial PACS.

# Patch RA\*5\*47 New Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch RA\*5\*47 creates the new Site Specific Accession Number (SSAN) by pre-pending the Facility ID to the day-case number. A new division parameter and a set-up option are created to control the use of the SSAN.

Only when the division parameter, *Use Site Accession Number?*, is set to YES, does the Radiology package generate and store the SSAN during Registration, and add the

display of the SSAN to options, reports and look-ups, which previously displayed the case number or day-case number.

- The parameter is set by division and is distributed with a NULL value; all divisions must be set when the switch is flipped (either ALL ON or ALL OFF).
- After the parameter is set to YES, the SSAN is displayed in RA options, reports, and lookups, where the case number or day-case number was previously displayed.
- For historical cases created before the parameter is set, there is no associated SSAN; therefore, the case number or day-case number continues to display for the life of those cases.

A new option, Site Accession Number Set-up, was added to the IRM Menu.

- This option functions as a *switch* to turn on the use of the SSAN.
- This option provides the sites with the ability to NOT begin using the SSAN until all devices are able to handle the longer accession number; sites must not begin using the SSAN until all devices are able to handle the longer accession number.

  
Examples

Example of an existing display with the division parameter set to NO or NULL.

Select Exam Entry/Edit Menu Option: Case No. Exam Edit

Enter Case Number: 3039

Choice Case No. Procedure Name Pt ID

------ --------------- --------- ----------------- ------

1 032009-3039 ANGIO CAROTID CEREBRAL UN RADPATIENT,ONE 0000

(RAD Detailed) CPT:75665

Example of the new display with the division parameter set to YES.

Select Exam Entry/Edit Menu Option: Case No. Exam Edit

Enter Case Number: 141-032009-3039 User may still select by case \# (3039)

Choice Case No. Procedure Name Pt ID

------ --------------- --------- ----------------- ------

1 141-032009-3039 ANGIO CAROTID CEREBRAL UN RADPATIENT,ONE 0000

(RAD Detailed) CPT:75665

## Options affected by the new SSAN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Abnormal Exam Report                                | \[RA ABNORMAL\]             |
|-----------------------------------------------------|-----------------------------|
| Access Uncorrected Reports                          | \[RA UNCORRECTED REPORTS\]  |
| Add Exams to Last Visit                             | \[RA ADDEXAM\]              |
| Add/Remove Report From Batch                        | \[RA BTCHREMOVE\]           |
| Cancel an Exam                                      | \[RA CANCEL\]               |
| Case No. Exam Edit                                  | \[RA EDITCN\]               |
| Clinic Distribution List                            | \[RA RPTDISTLISTCLINIC\]    |
| Daily Log Report                                    | \[RA LOG\]                  |
| Delete a Report                                     | \[RA DELETERPT\]            |
| Delinquent Status Report                            | \[RA DELINQUENT\]           |
| Diagnostic Code and Interpreter Edit by Case No.    | \[RA DIAGCN\]               |
| Display Patient Demographics                        | \[RA PROFDEMOS\]            |
| Display a Rad/Nuc Med Report                        | \[RA RPTDISP\]              |
| Draft Report (Reprint)                              | \[RA REPRINT\]              |
| Duplicate Dosage Ticket                             | \[RA DOSAGE TICKET\]        |
| Duplicate Flash Card                                | \[RA FLASH\]                |
| Edit Exam by Patient                                | \[RA EDITPT\]               |
| Exam Deletion                                       | \[RA DELETEXAM\]            |
| Exam Profile (selected sort)                        | \[RA PROFSORT\]             |
| Exam Status Display                                 | \[RA STATLOOK\]             |
| Incomplete Exam Report                              | \[RA INCOMPLETE\]           |
| Indicate No Purging of an Exam/report               | \[RA NOPURGE\]              |
| Jacket Labels                                       | \[RA LABELS\]               |
| List Reports in a Batch                             | \[RA BTCHLIST\]             |
| On-line Verifying of Reports                        | \[RA RPTONLINEVERIFY\]      |
| Outside Report Entry/Edit                           | \[RA OUTSIDE RPTENTRY\]     |
| Override a Single Exam's Status to 'complete'       | \[RA OVERRIDE\]             |
| Print Division Parameter List                       | \[RA SYSDIVLIST\]           |
| Print Rad/Nuc Med Requests by Date                  | \[RA ORDERPRINTS\]          |
| Print Selected Requests by Patient                  | \[RA ORDERPRINTPAT\]        |
| Print a Batch of Reports                            | \[RA BTCHPRINT\]            |
| Profile of Rad/Nuc Med Exams                        | \[RA PROFQUICK\]            |
| Radiopharmaceutical Administration Report           | \[RA NM RADIOPHARM ADMIN\]  |
| Radiopharmaceutical Usage Report                    | \[RA NM RADIOPHARM USAGE\]  |
| Register Patient for Exams                          | \[RA REG\]                  |
| Report Entry/Edit                                   | \[RA RPTENTRY\]             |
| Report's Print Status                               | \[RA RPTDISTPRINTSTATUS\]   |
| Request an Exam                                     | \[RA ORDEREXAM\]            |
| Restore a Deleted Report                            | \[RA RESTORE REPORT\]       |
| Select Report to Print by Patient                   | \[RA RPTPAT\]               |
| Status Tracking of Exams                            | \[RA STATRACK\]             |
| Summary/Detail report (for Outpt Proc Wait Times)   | \[RA TIMELINESS REPORT\]    |
| Summary/Detail report (for Verification Timeliness) | \[RA PERFORMIN RPTS\]       |
| Unprinted Reports List                              | \[RA RPTDISTLISTUNPRINTED\] |
| Unverified Reports                                  | \[RA DAIUVR\]               |
| Unverify a Report for Amendment                     | \[RA UNVERIFY\]             |
| Update Exam Status                                  | \[RA UPDATEXAM\]            |
| Verify Batch                                        | \[RA BTCHVERIFY\]           |
| Verify Report Only                                  | \[RA RPTVERIFY\]            |
| View Exam by Case No.                               | \[RA VIEWCN\]               |
| Ward Distribution List                              | \[RA RPTDISTLISTWARD\]      |

# Patch RA\*5\*47 Modified Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Routines are modified to call Imaging APIs to get:
1.  Patient ID information for the PID segment
4.  Patient Visit information for the PV1 segment
5.  Ordering Provider Call Back Phone Number(s) for the ORC segment
6.  A unique Study Instance User Identification (SIUID) key that creates a new ZDS segment used in the ORM and ORU HL7 v2.4 message types

> The calls to the Imaging APIs are covered by ICRs 5021, 5022, and 5023.

1.  New version 2.4 event driver protocols are exported with this patch.
2.  An input template is modified to file the site accession number data in the new Site Accession Number (#31) field and the SIUID in the Study Instance UID (#81) field, both in the EXAMINATIONS (#70.03) multiple.
3.  A routine is added to update the new Site Accession Number and Study Instance UID fields and to provide VistA Imaging with new APIs through a private integration agreement.
4.  The Exam Date (#.01) field of the REGISTERED EXAMS (#70.02) sub-file is modified to make the data in the field uneditable.
5.  Because of the addition of the Site Accession Number field to the EXAMINATIONS multiple, the input template must be re-compiled. A routine re-compiles the input template.

# After Installation of Patch RA\*5\*47

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Note:</strong></th>
<th><p><strong>Do not proceed with these steps until ready to begin using the new</strong></p>
<p><strong>HL7 v2.4 messaging.</strong></p>
<p><strong>Once you are ready to switch over to the new HL7 v2.4 messaging, you must perform the following steps.</strong></p>
<ul>
<li><p><strong>These steps must be done in coordination with the voice recognition software in use at the site.</strong></p></li>
<li><p><strong>These steps should be done when the Radiology options or voice recognition software is not in use.</strong></p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Setting Up the Voice Recognition Event Driver Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to use the new Integrating the Healthcare Enterprise (IHE) compliant HL7 v2.4 messaging provided by this patch, you must add the corresponding voice recognition subscriber protocols as SUBSCRIBERS to the new v2.4 event driver protocols exported in this patch.

> **NOTE:** For setting up the VistA Imaging MAGD SEND ORM and MAGD SEND ORU subscriber protocols, refer to MAG\*3.0\*49 patch documentation.

- The voice recognition subscriber protocols are likely the subscriber protocols that the site currently uses for the existing v2.3 (or previous) protocols.
- Prior to adding the voice recognition subscriber protocols to the new v2.4 event driver protocols, the corresponding voice recognition subscriber protocols must be removed from the existing v2.3 event driver protocols, to prevent sending duplicate messages.

> **NOTE:** If the listed protocols were renamed locally at your site, use the appropriately named protocols.

In the examples, RA TALKLINK ORM/ORU is used to illustrate the

process, but the steps are the same for RA PSCRIBE ORM/ORU, RA RADWHERE

ORM/ORU, and/or RA SEND ORM/ORU; so, substitute the correct name.

#### Step 1 - Remove voice recognition and PACS subscribers from existing ORM event driver protocols

For the RA CANCEL 2.3, RA EXAMINED 2.3 and RA REG 2.3 protocols (or the appropriate protocols if the site is using a version previous to v2.3), remove the voice recognition ORM subscriber protocol.

> **NOTE:** The PACS subscriber may need to be removed from the RA REG, RA EXAMINED and RA CANCEL protocols.

- For TalkStation, the subscriber protocol is RA TALKLINK ORM Note ORM
- For PowerScribe, the subscriber protocol is RA PSCRIBE ORM Note ORM
- For RadWhere, the subscriber protocol is RA RADWHERE ORM Note ORM
- For PACS, the subscriber protocol is RA SEND ORM Note ORMExample for Step 1Note: You must perform step 1 for the RA REG 2.3, RA CANCEL 2.3, and RA EXAM 2.3 protocols, but only RA REG 2.3 is shown in this example.

Select OPTION NAME: HL7 MAIN MENU  HL MAIN MENU     HL7 Main Menu

 

                 Event monitoring menu ...

                 Systems Link Monitor

                 Filer and Link Management Options ...

                 Message Management Options ...

                 Interface Developer Options ...

                 Site Parameter Edit

          HLO    HL7 (Optimized) MAIN MENU ...

 

Select HL7 Main Menu Option:  Interface Developer Options

 

          EA     Application Edit

          EP     Protocol Edit

          EL     Link Edit

          VI     Validate Interfaces

                 Reports ...

 

Select Interface Developer Options Option:  Protocol Edit

 

Select PROTOCOL NAME: RA REG 2.3   Select v2.3 event driver protocol

   

              HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

 

              NAME: RA REG 2.3                                            

 

DESCRIPTION (wp):   \[This protocol is triggered whenever a Radiology\]

  

ENTRY ACTION:

 

EXIT ACTION:

  

TYPE: event driver  Press \<return\> at this field to go to next screen

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   

COMMAND:                                  Press \<PF1\>H for help

             HL7 EVENT DRIVER                         PAGE 2 OF 2

             RA REG 2.3                   

------------------------------------------------------------------------

     

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORM                        EVENT TYPE: O01

       MESSAGE STRUCTURE:

           PROCESSING ID:                            VERSION ID: 2.3

         ACCEPT ACK CODE:                  APPLICATION ACK TYPE:

 

 RESPONSE PROCESSING RTN: \*\*\*\*\*\*\*\*\*\*\*\*\*\*                           

                       SUBSCRIBERS

RA TALKLINK ORM   Remove VR ORM subscriber

RA SEND ORM   Remove PACS ORM subscriber, if applicable

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  

#### Step 2 - Remove voice recognition and PACS subscribers from existing ORU event driver protocol

> **NOTE:** The PACS subscriber may need to be removed from the RA RPT protocol.

For the RA RPT 2.3 protocol (or the appropriate protocol if the site is using a version previous to v2.3), remove the voice recognition ORU subscriber protocol.

- For TalkStation, the subscriber protocol is RA TALKLINK ORU Note ORU
- For PowerScribe, the subscriber protocol is RA PSCRIBE ORU Note ORU
- For RadWhere, the subscriber protocol is RA RADWHERE ORU Note ORU
- For PACS, the subscriber protocol is RA SEND ORU Note ORUExample for Step 2

Select OPTION NAME: HL7 MAIN MENU  HL MAIN MENU     HL7 Main Menu

 

                 Event monitoring menu ...

                 Systems Link Monitor

                 Filer and Link Management Options ...

                 Message Management Options ...

                 Interface Developer Options ...

                 Site Parameter Edit

          HLO    HL7 (Optimized) MAIN MENU ...

 

Select HL7 Main Menu Option:  Interface Developer Options

 

          EA     Application Edit

          EP     Protocol Edit

          EL     Link Edit

          VI     Validate Interfaces

                 Reports ...

 

Select Interface Developer Options Option:  Protocol Edit

 

Select PROTOCOL NAME: RA RPT 2.3   Select v2.3 event driver protocol

   

       HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

 

       NAME: RA RPT 2.3                                            

 

DESCRIPTION (wp):   \[This protocol is triggered whenever a Radiology\]

 

ENTRY ACTION:

 

EXIT ACTION: 

 

TYPE: event driver  Press \<return\> at this field to go to next screen

 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   

COMMAND:                                  Press \<PF1\>H for help

         HL7 EVENT DRIVER                         PAGE 2 OF 2

         RA RPT 2.3                   

-----------------------------------------------------------------------

     

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORU                        EVENT TYPE: R01

       MESSAGE STRUCTURE:

           PROCESSING ID:                            VERSION ID: 2.3  

         ACCEPT ACK CODE:                  APPLICATION ACK TYPE:

 

 RESPONSE PROCESSING RTN: \*\*\*\*\*\*\*\*\*\*\*\*\*\*                         

                    SUBSCRIBERS

RA TALKLINK ORU   Remove appropriate VR ORU subscriber

RA SEND ORU   Remove PACS ORU subscriber, if applicable

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 

#### Step 3 - Add voice recognition and PACS subscribers to new ORM event driver protocols

For the RA CANCEL 2.4, RA EXAMINED 2.4, and RA REG 2.4 protocols, add the voice recognition and PACS ORM subscriber protocol.

- For TalkStation, it is usually RA TALKLINK ORM Note ORM
- For PowerScribe, it is usually RA PSCRIBE ORM Note ORM
- For RadWhere, it is usually RA RADWHERE ORM Note ORM
- For PACS, it is usually RA SEND ORM Note ORMExample for Step 3Note: You must perform step 3 for the RA REG 2.4, RA CANCEL 2.4 and RA EXAMINED 2.4 protocols, but only RA REG 2.4 is shown in this example.

Select OPTION NAME: HL7 MAIN MENU  HL MAIN MENU     HL7 Main Menu

 

                 Event monitoring menu ...

                 Systems Link Monitor

                 Filer and Link Management Options ...

                 Message Management Options ...

                 Interface Developer Options ...

                 Site Parameter Edit

          HLO    HL7 (Optimized) MAIN MENU ...

 

Select HL7 Main Menu Option:  Interface Developer Options

 

          EA     Application Edit

          EP     Protocol Edit

          EL     Link Edit

          VI     Validate Interfaces  
Reports ...

 

Select Interface Developer Options Option:  Protocol Edit

 

Select PROTOCOL NAME: RA REG 2.4   Select v2.4 event driver protocol

   

         HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

 

         NAME: RA REG 2.4                                             

DESCRIPTION (wp):   \[This protocol is triggered whenever a Radiology\]

  

ENTRY ACTION: 

EXIT ACTION:

  

  TYPE: event driver  Press \<return\> at this field to go to next screen

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   

COMMAND:                                  Press \<PF1\>H for help

          HL7 EVENT DRIVER                         PAGE 2 OF 2

          RA REG 2.4                   

-----------------------------------------------------------------------

      

SENDING APPLICATION: RA-VOICE-SERVER

 TRANSACTION MESSAGE TYPE: ORM                      EVENT TYPE: O01

        MESSAGE STRUCTURE:

            PROCESSING ID:                      VERSION ID: 2.4   

          ACCEPT ACK CODE:                APPLICATION ACK TYPE:

 

  RESPONSE PROCESSING RTN: \*\*\*\*\*\*\*\*\*\*\*\*\*\*                              

                   SUBSCRIBERS

RA TALKLINK ORM   Add appropriate VR ORM subscriber

RA SEND ORM   Add PACS ORM subscriber, if applicable

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 

#### Step 4 - Add voice recognition subscribers to new ORU event driver protocol

For the RA RPT 2.4 protocol, add the voice recognition and PACS ORU subscriber protocol.

- For TalkStation, the subscriber protocol is RA TALKLINK ORU Note ORU
- For PowerScribe, the subscriber protocol RA PSCRIBE ORU Note ORU
- For RadWhere, the subscriber protocol RA RADWHERE ORU Note ORU
- For PACS, the subscriber protocol RA SEND ORU Note ORUExample for Step 4

Select OPTION NAME: HL7 MAIN MENU  HL MAIN MENU     HL7 Main Menu

 

                 Event monitoring menu ...

                 Systems Link Monitor

                 Filer and Link Management Options ...

                 Message Management Options ...

                 Interface Developer Options ...

                 Site Parameter Edit

          HLO    HL7 (Optimized) MAIN MENU ...

 

Select HL7 Main Menu Option:  Interface Developer Options

 

          EA     Application Edit

          EP     Protocol Edit

          EL     Link Edit

          VI     Validate Interfaces

                 Reports ...

 

Select Interface Developer Options Option:  Protocol Edit

 

Select PROTOCOL NAME: RA RPT 2.4   Select v2.4 event driver protocol

   

         HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

 

NAME: RA RPT 2.4                                            

 

DESCRIPTION (wp):   \[This protocol is triggered whenever a Radiology\]

 

ENTRY ACTION:

 

EXIT ACTION:

  

        TYPE: event driver  Press \<return\> at this field to go to next screen

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   

COMMAND:                                  Press \<PF1\>H for help

         HL7 EVENT DRIVER                         PAGE 2 OF 2

         RA RPT 2.4                   

-----------------------------------------------------------------------

     

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORU                        EVENT TYPE: R01

       MESSAGE STRUCTURE:

           PROCESSING ID:                            VERSION ID: 2.4  

         ACCEPT ACK CODE:                  APPLICATION ACK TYPE:

 RESPONSE PROCESSING RTN: \*\*\*\*\*\*\*\*\*\*\*\*\*\*                       

                     SUBSCRIBERS

RA TALKLINK ORU   Add appropriate VR ORU subscriber

RA SEND ORU   Add PACS ORU subscriber, if applicable

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   

#### Step 5 - Change the Version ID field of existing message receipt protocol to 2.4

For the existing message receipt protocol, change the Version ID field to 2.4.

- For TalkStation, it is usually RA TALKLINK TCP SERVER REPORT
- For PowerScribe, it is usually RA PSCRIBE TCP SERVER REPORT
- For RadWhere, it is usually RA RADWHERE TCP SERVER REPORT  

Example for Step 5

Select OPTION NAME: HL7 MAIN MENU  HL MAIN MENU     HL7 Main Menu

 

               Event monitoring menu ...

               Systems Link Monitor

               Filer and Link Management Options ...

               Message Management Options ...

               Interface Developer Options ...

               Site Parameter Edit

        HLO    HL7 (Optimized) MAIN MENU ...

 

Select HL7 Main Menu Option:  Interface Developer Options

 

        EA     Application Edit

        EP     Protocol Edit

        EL     Link Edit

        VI     Validate Interfaces

               Reports ...

 

Select Interface Developer Options Option: EP  Protocol Edit

 

Select PROTOCOL NAME:  RA TALKLINK TCP SERVER RPT  Select existing message receipt event

> driver protocol (TALKLINK is used in this example)

 

        HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

 

NAME: RA TALKLINK TCP SERVER RPT                            

 

DESCRIPTION (wp):   \[Driver protocol for sending report to VISTA Rad\]

 

ENTRY ACTION:

 

EXIT ACTION: 

 

        TYPE: event driver  Press \<return\> at this field to go to next screen

 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

 

          HL7 EVENT DRIVER                         PAGE 2 OF 2

          RA TALKLINK TCP SERVER RPT 

  

-----------------------------------------------------------------------

SENDING APPLICATION: RA-TALKLINK-TCP

 TRANSACTION MESSAGE TYPE: ORU              EVENT TYPE: R01

        MESSAGE STRUCTURE:          

            PROCESSING ID:                  VERSION ID: 2.3 Change this field to 2.4

 

          ACCEPT ACK CODE:                  APPLICATION ACK TYPE:

 

 RESPONSE PROCESSING RTN:

                           SUBSCRIBERS

  RA TALKLINK TCP REPORT

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### Step 6 - Turn on the use of the long site accession number

The option, Site Accession Number Set-up, functions as the *switch* to turn on the use of the Site Specific Accession Number (SSAN).

- Until this field is set to YES, the system will not generate and store the SSAN during the registration of a new case.
- Only when all devices are able to handle the SSAN, should this field be set to YES, at which point, the system will generate and store the SSAN during Registration.

Example for Step 6

    

Select OPTION NAME: RA SITEMANAGER       IRM Menu

  

          Device Specifications for Imaging Locations

          Distribution Queue Purge

          Failsoft Parameters

          Imaging Type Activity Log

          Purge Data Function

          Rebuild Distribution Queues

          Report File x-ref Clean-up Utility

          Site Accession Number Set-up

          Credit completed exams for an Imaging Location

          Resource Device Specifications for Division

          Schedule Perf. Indic. Summary for 15th of month

          Template Compilation

  Select IRM Menu Option: Site Accession Number Set-up

 

   Warning: Turning on the Site Specific Accession Number should only

   be done in conjunction with using the RA v2.4 messaging protocols.

 

   NOTE: Changing the Site Specific Accession Number parameter at a

   multidivisional site will change the parameter for ALL divisions.

 

Current value of Site Specific Accession Number parameter: NO

Use Site Specific Accession Number? YES

# Software and Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch RA\*5\*47 software and documentation are available on the Office of Information Field Offices (OIFOs) \[ANONYMOUS. SOFTWARE\] directories at the following Internet addresses:

| Preferred or Specific Server       | Internet Address                                    |
|------------------------------------|-----------------------------------------------------|
| First available ftp server         | <span class="mark">REDACTED</span> \< Preferred |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>                  |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>                  |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>                  |

This patch is available via FTP (File Transfer Protocol) in a KIDS (Kernel Installation and Distribution System) distribution file.

| File Name    | Description | Download Format |
|--------------|-------------|-----------------|
| RA_5_P47.KID | KIDS Build  | ASCII           |

## Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Manuals are also available in MS Word (.docx) format and the Portable Document Format (.pdf) on the VA Software Documentation Library

<http://www4.va.gov/vdl/>

<table>
<colgroup>
<col style="width: 62%" />
<col style="width: 23%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Document File Description</th>
<th>File Names</th>
<th>FTP Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Radiology/Nuclear Medicine User Manual</td>
<td><p>RA5_0UM.doc</p>
<p>RA5_0UM.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>Radiology/Nuclear Medicine Technical Manual</td>
<td><p>RA5_0TM.doc</p>
<p>RA5_0TM.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>Radiology/Nuclear Medicine 5.0 HL7 Interface Specification Version 3.0</td>
<td><p>RA5_0HL7spec.doc</p>
<p>RA5_0HL7spec.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>Radiology/Nuclear Medicine 5.0 HL7 Setup/Implementation Manual Version 3.0</td>
<td><p>RA5_0HL7setup.doc</p>
<p>RA5_0HL7setup.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>Radiology/Nuclear Medicine Release Notes</td>
<td><p>RA5_0RN_P47.doc</p>
<p>RA5_0RN_P47.pdf</p></td>
<td>Binary</td>
</tr>
</tbody>
</table>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: RA*5*56 Release Notes

### 'Outside Report Entry/Edit' \[RA OUTSIDE RPTENTRY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Films Reporting Menu, the 'Outside Report Entry/Edit' option allows you to enter a canned report to record the receipt of a report that was interpreted outside your facility without the need to verify the report in order for the exam status of the case to reach 'COMPLETE.' This option prompts for 'Standard' Report to Copy, Reported Date, Report Text, Impression Text, and Diagnostic Codes. It automatically assigns an Electronically Filed (EF) report status to the report, if a canned report was selected, and/or report text and/or impression text was entered via this option. Except for the Diagnostic Code, this option ignores all other site-required items for the exam status of 'COMPLETE,' including verifying physician and verified date.

If diagnostic codes are not required for the exam status of 'COMPLETE,' this option automatically sets the exam status to 'COMPLETE'; otherwise, it automatically sets the exam status to 'COMPLETE' when a diagnostic code is entered later via this option. The requirement for diagnostic code is set via the 'Examination Status Entry/Edit' \[RA EXAMSTATUS\] option.

This option also allows you to enter diagnostic codes even after the case has reached the 'COMPLETE' exam status. Each time this option is used to change or add new diagnostic codes, the added or changed codes are rechecked to see if alerts should be generated. Alerts are not generated again for existing, unchanged diagnostic codes that previously triggered the generation of alerts. The generation of alerts is based upon the value of "GENERATE ABNORMAL ALERT?" in the DIAGNOSTIC CODES file (#78.3), which is updated via the 'Diagnostic Code Enter/Edit' \[RA DIAGEDIT\] option. If an alert is generated, its notification appears as follows on the VistA roll-n-scroll screen:

RADPATIENT,ONE (R4558): Abnormal Imaging Results: CHEST 2 VIEWS PA&LAT

Enter "VA to jump to VIEW ALERTS option

A study performed and interpreted outside must be registered under a "No Credit" imaging location. If it is not, when you use this option, a warning message displays, but you can continue to enter data, provided it is an acceptable business rule in your department. (The following example shows the warning message.)

Example 1

Enter a new outside report for a case that is registered from a credit location. A warning message displays regarding the credit method.

Select Films Reporting Menu Option: OUTSIDE Report Entry/Edit

+--------------------------------------------------------+

\| \|

\| This option is for entering canned text for \|

\| outside work: interpreted report done outside, \|

\| and images made outside this facility. \|

\| \|

+--------------------------------------------------------+

Select Rad/Nuc Med Division: All//

Another one (Select/De-Select):

Select Imaging Type: All//

Another one (Select/De-Select):

Enter Case Number: RADPATIENT,ONE

RADPATIENT,ONE 6-1-27 000000000

\*\*\*\* Case Lookup by Patient \*\*\*\*

Patient's Name: RADPATIENT,ONE 000-00-0000 Run Date: MAR 5,2008

Case No. Procedure Exam Date Status of Report Imaging Loc

-------- ------------- --------- ---------------- -----------

1 2794 CHEST 2 VIEWS PA&LAT 03/05/08 RADIOLOGY L

2 2612 SPINE ENTIRE AP&LAT 02/13/08 ELECTRONICALLY F RADIOLOGY L

3 2610 ELBOW 2 VIEWS 02/13/08 DRAFT X-RAY CLINI

4 2608 HAND 1 OR 2 VIEWS 02/13/08 ELECTRONICALLY F X-RAY CLINI

5 +2552 ABDOMEN 1 VIEW 01/31/08 DRAFT X-RAY CLINI

6 .2553 ABDOMEN 2 VIEWS 01/31/08 DRAFT X-RAY CLINI

7 .2554 ABDOMEN 3 OR MORE VIEWS 01/31/08 DRAFT X-RAY CLINI

8 2551 MANDIBLE LESS THAN 4 VIEWS 01/31/08 DRAFT X-RAY CLINI

9 2498 CLAVICLE 12/19/07 (Exam Dc'd) RADIOLOGY L

10 2152 FOOT 2 VIEWS 09/08/06 VERIFIED X-RAY CLINI

11 2153 CLAVICLE 09/08/06 ELECTRONICALLY F X-RAY CLINI

12 2122 HIP 1 VIEW 07/07/06 RADIOLOGY L

Type a '^' to STOP, or

CHOOSE FROM 1-12: 1

-------------------------------------------------------------------------------

Name : RADPATIENT,ONE Pt ID : 000-00-0000

Case No. : 2794 Exm. St: WAITING FOR Procedure : CHEST 2 VIEWS PA&LAT

Tech.Comment: This is the tech comment entered during registration.

Exam Date: MAR 5,2008 10:29 Technologist:

Req Phys : RADPROVIDER,ONE

-------------------------------------------------------------------------------

This option is for Outside work (imaged and read), so the case should Warning

be 'No Credit', but this case has a credit method of 'Regular Credit' Message

Do you want to continue? NO// YES

...report not entered for this exam...

...will now initialize report entry...

-------------------------------------------------------------------------------

Select 'Standard' Report to Copy:

REPORTED DATE: T (MAR 05, 2008)

CLINICAL HISTORY:

This is the clinical history entered during Request an Exam.

+++++++++++++++++++++++++++++++++++++++++++++++++++

Required: REPORT TEXT and/or IMPRESSION TEXT

+++++++++++++++++++++++++++++++++++++++++++++++++++

REPORT TEXT:

No existing text

Edit? NO//

IMPRESSION TEXT:

No existing text

Edit? NO//

+++++++++++++++++++++++++++++++++++++++++++++++++++

Required: REPORT TEXT and/or IMPRESSION TEXT

+++++++++++++++++++++++++++++++++++++++++++++++++++

REPORT TEXT: If nothing is entered for REPORT TEXT and IMPRESSION

No existing text TEXT, the option loops back to ask for both, until data is

Edit? NO// YES is entered for at least one of them.

==\[ WRAP \]==\[ INSERT \]=============\< REPORT TEXT \>===========\[ \<PF1\>H=Help \]====

This is the report text.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

IMPRESSION TEXT:

No existing text

Edit? NO//

PRIMARY DIAGNOSTIC CODE: NORMAL

Select SECONDARY DIAGNOSTIC CODE: 9 NO DISCRETE MASS

Select SECONDARY DIAGNOSTIC CODE:

Report status is stored as "Electronically Filed".

...will now designate exam status as 'COMPLETE'... for case no. 2794

...exam status successfully updated.

...will now designate request status as 'COMPLETE'...

Visit credited.

...request status successfully updated.

> Results

- Both exam status and request status are updated to 'COMPLETE.'
- Normally, if an outside report is entered for an exam that was registered from a "No Credit" imaging location, the "Visit credited" would not appear.
- There is no alert for "Imaging Results," as would be automatically generated for Verified Reports.
- There is no Abnormal alert because the diagnostic codes here do not require alerts.
- The 'Outside Report Entry/Edit' option does not recognize the case number once the case reaches 'COMPLETE,' because the case is no longer active. You must enter the patient name or Last initial and Last 4 SSN at the Enter Case Number prompt to display a list of patient cases from which to select. This general feature is also seen from the 'View Exam by Case No.' option.

Example 1 continued

Select Films Reporting Menu Option: Outside Report Entry/Edit

+--------------------------------------------------------+

\| \|

\| This option is for entering canned text for \|

\| outside work: interpreted report done outside, \|

\| and images made outside this facility. \|

\| \|

+--------------------------------------------------------+

Select Rad/Nuc Med Division: All//

Another one (Select/De-Select):

Select Imaging Type: All//

Another one (Select/De-Select):

Enter Case Number: 2794 The completed case is no longer active.

No matches found! So, the case cannot be found by case number.

Example 2

Use the same option on an existing outside report, but do not change any data.

Select Films Reporting Menu Option: OUTSIDE Report Entry/Edit

> …

CHOOSE FROM 1-12: 1

-------------------------------------------------------------------------------

Name : RADPATIENT,ONE Pt ID : 000-00-0000

Case No. : 2794 Exm. St: COMPLETE Procedure : CHEST 2 VIEWS PA&LAT

Tech.Comment: This is the tech comment entered during registration.

Exam Date: MAR 5,2008 10:29 Technologist:

Req Phys : RADPROVIDER,ONE

-------------------------------------------------------------------------------

Select 'Standard' Report to Copy:

REPORTED DATE: MAR 5,2008//

CLINICAL HISTORY:

This is the clinical history entered during Request an Exam.

+++++++++++++++++++++++++++++++++++++++++++++++++++

Required: REPORT TEXT and/or IMPRESSION TEXT

+++++++++++++++++++++++++++++++++++++++++++++++++++

REPORT TEXT:

This is the report text.

Edit? NO//

IMPRESSION TEXT:

No existing text

Edit? NO//

PRIMARY DIAGNOSTIC CODE: NORMAL//

Select SECONDARY DIAGNOSTIC CODE: NO DISCRETE MASS

//

SECONDARY DIAGNOSTIC CODE: NO DISCRETE MASS//

Select SECONDARY DIAGNOSTIC CODE:

Report status is stored as "Electronically Filed".

Do you wish to print this report? No//

> Results

- There is no update of exam and request statuses, because this exam already reached the exam status of 'COMPLETE.'
- There is no alert because none of the diagnostic codes were changed.

Example 3

Change some diagnostic codes for a previously entered outside report.

Select Films Reporting Menu Option: Outside Report Entry/Edit

> …

CHOOSE FROM 1-12: 1

-------------------------------------------------------------------------------

Name : RADPATIENT,ONE Pt ID : 000-00-0000

Case No. : 2794 Exm. St: COMPLETE Procedure : CHEST 2 VIEWS PA&LAT

Tech.Comment: This is the tech comment entered during registration.

Exam Date: MAR 5,2008 10:29 Technologist:

Req Phys : RADPROVIDER,ONE

-------------------------------------------------------------------------------

Select 'Standard' Report to Copy:

REPORTED DATE: MAR 5,2008//

CLINICAL HISTORY:

This is the clinical history entered during Request an Exam.

+++++++++++++++++++++++++++++++++++++++++++++++++++

Required: REPORT TEXT and/or IMPRESSION TEXT

+++++++++++++++++++++++++++++++++++++++++++++++++++

REPORT TEXT:

This is the report text.

Edit? NO//

IMPRESSION TEXT:

No existing text

Edit? NO//

PRIMARY DIAGNOSTIC CODE: NORMAL// 4 ABNORMALITY, ATTN. NEEDED

Select SECONDARY DIAGNOSTIC CODE: NO DISCRETE MASS

// @

SURE YOU WANT TO DELETE THE ENTIRE SECONDARY DIAGNOSTIC CODE? Y (Yes)

Select SECONDARY DIAGNOSTIC CODE:

Report status is stored as "Electronically Filed".

Do you wish to print this report? No//

Enter Case Number:

Batch Reports Menu ...

Display a Rad/Nuc Med Report

Distribution Queue Menu ...

Draft Report (Reprint)

On-line Verifying of Reports

Outside Report Entry/Edit

Report Entry/Edit

Resident On-Line Pre-Verification

Select Report to Print by Patient

Switch Locations

Verify Report Only

RADPATIENT,ONE (R4558): Abnormal Imaging Results: CHEST 2 VIEWS PA&LAT

Enter "VA to jump to VIEW ALERTS option

> Result

> An Abnormal alert is generated because the primary diagnostic code was changed to one that requires the generation of an alert notification.

'Restore a Deleted Report' \[RA RESTORE REPORT\]

In the Supervisor Menu, the 'Restore a Deleted Report' option allows you to relink a previously deleted report to its associated case, only if another report was not linked to the case in the interim (time between deletion and restoration). The restored report is re-assigned the report status it had prior to being deleted; however, the status of the exam is not updated.

If a case had a report entered and deleted, then had a second report entered and deleted for it, the case would have two deleted reports in the database. This option allows you to choose any previously deleted report for a case, not just the most recently deleted report for that case. The other deleted report that was not selected for restoration remains as a deleted report in the database.

To view a list of deleted reports to select from this option, enter "??" at the "Select Deleted Report to restore:" prompt. After you select a deleted report, the first prompt displayed is:

Do you want to restore this deleted report? NO//

Before allowing you to restore a report, this option checks whether the case associated with this report has another report linked to it and whether the case has data for diagnostic codes, staff, and resident. If any such data are found, the option does not continue, but displays a warning message. For example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Case #123 is already associated with a report!</p>
<p>Restoration was not done.</p>
<p>This message indicates that either another previously deleted report was restored to its associated case or a new report was entered for the case during the time between report deletion and attempted restoration.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Case #461 already has SECONDARY DIAGNOSTIC CODE</p>
<p>Restoration was not done.</p>
<p>This message indicates that the case associated with this report already has secondary diagnostic code data, which may or may not be associated with this report. The supervisor must determine if the correct deleted report was selected for restoration; and if so, must remove the secondary diagnostic code from the case before the deleted report can be restored. The 'Diagnostic Code and Interpreter Edit by Case No.' [RA DIAGCN] option can be used to remove the diagnostic code data.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If no problems are found, then the patient name and some case data are displayed. If the patient name and case data match the case for the deleted report you want to restore, then enter "YES" to the second prompt:

Are you sure you want to link this report back to the case? NO//

After a report is restored to its associated case, you can view statuses for previously deleted and restored activities from the Report Activity Log section of the 'View Exam by Case No.' option.

Example of restoring a report to one case

Restore a deleted report back to its case. This option relinks the report back to its associated case and repopulates the diagnostic code(s), staff, and resident data to the case.

Select Supervisor Menu Option: RESTORE a Deleted Report

+--------------------------------------------------------+

\| \|

\| This option is for restoring a deleted report. \|

\| \|

+--------------------------------------------------------+

Select Deleted Report to restore: ??

Choose from:

013108-2551 RADPATIENT,ONE MANDIBLE LESS THAN 4 VIEWS

021308-2608 RADPATIENT,ONE HAND 1 OR 2 VIEWS

070706-2122 RADPATIENT,ONE HIP 1 VIEW

072304-1608 RADPATIENT,TWO MANDIBLE LESS THAN 4 VIEWS

072304-1609 RADPATIENT,TWO FOOT 3 OR MORE VIEWS

090806-2153 RADPATIENT,ONE CLAVICLE

Select Deleted Report to restore: 013108-2551 RADPATIENT,ONE MANDIBLE LESS THAN 4 VIEWS

Do you want to restore this deleted report? NO// YES

-------------------------------------------------------------------------------

Name : RADPATIENT,ONE Pt ID : 000-00-0000

Case No. : 2551 Exm. St: WAITING FOR Procedure : MANDIBLE LESS THAN 4 VIEW

Tech.Comment: This is the tech comment during registration

Exam Date: JAN 31,2008 10:23 Technologist:

Req Phys : RADPROVIDER,ONE

-------------------------------------------------------------------------------

Are you sure you want to link this report back to the case? NO// YES

... Restored 013108-2551's report status to: DRAFT.

... Linked restored report to case no. 2551

... Restored case 2551's PRIMARY DIAGNOSTIC CODE to: NORMAL

... Restored case 2551's SECONDARY DIAGNOSTIC CODE to: UNDICTATED FILMS NOT RETURNED, 3 DAYS

... Restored case 2551's SECONDARY DIAGNOSTIC CODE to: NO DISCRETE MASS

... Restored case 2551's PRIMARY INTERPRETING STAFF to: RADPRIMARYSTAFF,ONE

... Restored case 2551's SECONDARY INTERPRETING STAFF to: RADSECONDARYSTAFF,ONE

... Restored case 2551's PRIMARY INTERPRETING RESIDENT to: RADPRIMARYRESIDENT,ONE

\*\* You need to edit the case to update the exam status. \*\*

Press RETURN to exit.

Example of restoring a report to several cases that previously shared this report

Restore the deleted report back to its cases (printset). The option relinks the report back to its associated cases and repopulates the diagnostic code(s), staff, and resident data to each of the cases.

Select Supervisor Menu Option: RESTORE a Deleted Report

+--------------------------------------------------------+

\| \|

\| This option is for restoring a deleted report. \|

\| \|

+--------------------------------------------------------+

Select Deleted Report to restore: ??

Choose from:

013108-2553 RADPATIENT,ONE -2552,-2554 +ABDOMEN 2 VIEWS

021308-2608 RADPATIENT,ONE HAND 1 OR 2 VIEWS

070706-2122 RADPATIENT,ONE HIP 1 VIEW

072304-1608 RADPATIENT,TWO MANDIBLE LESS THAN 4 VIEWS

072304-1609 RADPATIENT,TWO FOOT 3 OR MORE VIEWS

090806-2153 RADPATIENT,ONE CLAVICLE

Select Deleted Report to restore: 013108-2553 RADPATIENT,ONE -2552,-2554

+ABDOMEN 2 VIEWS

Do you want to restore this deleted report? NO// YES

-------------------------------------------------------------------------------

Name : RADPATIENT,ONE Pt ID : 000-00-0000

Case No. : 2553 Exm. St: WAITING FOR Procedure : ABDOMEN 2 VIEWS

Tech.Comment: unable enter def CPT mod GC, 50 (case 2552, Cmod KB)

Case No. : 2552 Exm. St: WAITING FOR Procedure : ABDOMEN 1 VIEW

Tech.Comment: tech comment during registration

Case No. : 2554 Exm. St: WAITING FOR Procedure : ABDOMEN 3 OR MORE VIEWS

Exam Date: JAN 31,2008 10:24 Technologist:

Req Phys : RADPROVIDER,ONE

-------------------------------------------------------------------------------

Are you sure you want to link this report back to the cases? NO// YES

... Restored 013108-2553's report status to: DRAFT.

... Linked restored report to case no. 2552

... Linked restored report to case no. 2553

... Linked restored report to case no. 2554

... Restored case 2552's PRIMARY DIAGNOSTIC CODE to: MINOR ABNORMALITY

... Restored case 2552's SECONDARY DIAGNOSTIC CODE to: NO DISCRETE MASS

... Restored case 2552's SECONDARY DIAGNOSTIC CODE to: UNDICTATED FILMS NOT RETURNED, 3 DAYS

... Restored case 2553's PRIMARY DIAGNOSTIC CODE to: MINOR ABNORMALITY

... Restored case 2553's SECONDARY DIAGNOSTIC CODE to: NO DISCRETE MASS

... Restored case 2553's SECONDARY DIAGNOSTIC CODE to: UNDICTATED FILMS NOT RETURNED, 3 DAYS

... Restored case 2554's PRIMARY DIAGNOSTIC CODE to: MINOR ABNORMALITY

... Restored case 2554's SECONDARY DIAGNOSTIC CODE to: NO DISCRETE MASS

... Restored case 2554's SECONDARY DIAGNOSTIC CODE to: UNDICTATED FILMS NOT RETURNED, 3 DAYS

... Restored case 2552's PRIMARY INTERPRETING STAFF to: RADPRIMARYSTAFF,ONE

... Restored case 2552's SECONDARY INTERPRETING STAFF to: RADSECONDARYSTAFF,ONE

... Restored case 2552's SECONDARY INTERPRETING STAFF to: RADSECONDARYSTAFF,TWO

... Restored case 2553's PRIMARY INTERPRETING STAFF to: RADPRIMARYSTAFF,ONE

... Restored case 2553's SECONDARY INTERPRETING STAFF to: RADSECONDARYSTAFF,ONE

... Restored case 2553's SECONDARY INTERPRETING STAFF to: RADSECONDARYSTAFF,TWO

... Restored case 2554's PRIMARY INTERPRETING STAFF to: RADPRIMARYSTAFF,ONE

... Restored case 2554's SECONDARY INTERPRETING STAFF to: RADSECONDARYSTAFF,ONE

... Restored case 2554's SECONDARY INTERPRETING STAFF to: RADSECONDARYSTAFF,TWO

... Restored case 2552's PRIMARY INTERPRETING RESIDENT to: RADPRIMARYRESIDENT,ONE

... Restored case 2553's PRIMARY INTERPRETING RESIDENT to: RADPRIMARYRESIDENT,ONE

... Restored case 2554's PRIMARY INTERPRETING RESIDENT to: RADPRIMARYRESIDENT,ONE

\*\* You need to edit the cases to update the exam status. \*\*

Press RETURN to exit.

### Modified 'Delete a Report' \[RA DELETERPT\] option 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to Patch RA\*5\*56, a deleted report is erased from the database. Patch RA\*5\*56 keeps the deleted report in the RAD/NUC MED REPORTS file (#74), but removes its association to an exam, so that it is no longer accessible via the Radiology application. The only way to view a deleted report is via VA Fileman.

Example

Delete a report shared by three cases (printset). The deletion session outwardly appears the same as before patch RA\*5\*56:

Select Supervisor Menu Option: DELETE A REPORT

Select Report Day-Case#: RADPATIENT,ONE RADPATIENT,ONE 6-1-27 000000000

1 RADPATIENT,ONE 090806-2152 RADPATIENT,ONE FOOT 2 VIEWS

2 RADPATIENT,ONE 090806-2153 RADPATIENT,ONE CLAVICLE

3 RADPATIENT,ONE 013108-2551 RADPATIENT,ONE MANDIBLE LESS THAN 4 VIEWS

4 RADPATIENT,ONE 013108-2553 RADPATIENT,ONE +ABDOMEN 2 VIEWS

5 RADPATIENT,ONE 021308-2610 RADPATIENT,ONE ELBOW 2 VIEWS

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 4 013108-2553 RADPATIENT,ONE +ABDOMEN 2 VIEWS

Do you wish to delete this report? NO// Y

...report deletion complete.

...exam status remains 'WAITING FOR EXAM'.

...exam status remains 'WAITING FOR EXAM'.

...exam status remains 'WAITING FOR EXAM'.

### From: RA*5*84 Release Notes

## Anomaly with Patch RA\*5\*84

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Remedy Ticket \#251440/Resolve in Patch RA\*5.0\*78

Description: There may be extra carriage returns in the display of Radiology 5.0 reports

We made active sites aware of this anomaly and suggested to the sites that the reports be fully examined.

## Patch RA\*5\*84 Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch RA\*5\*84 provides nine new features to Radiology/Nuclear Medicine 5.0.

### Proxy User Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch creates an application proxy user account called RADIOLOGY,OUTSIDE SERVICE in the NEW PERSON (#200) file. This account represents the nationally-credentialed radiologists at the NTP, so that they do not need to be credentialed and privileged at each participating VAMC. You cannot use the proxy account to log into local VistA applications and it does not require the use of Access/Verify codes.

> **NOTE:** Do not modify the RADIOLOGY,OUTSIDE SERVICE proxy user account.  
A security policy is in place that strictly defines the attributes of this record. For more information, refer to VA Directive 6504.

The pre-install process updates the RADIOLOGY,OUTSIDE SERVICE record by assigning the NEW PERSON record a STAFF Radiology/Nuclear Medicine classification. Without the STAFF classification, exams verified by teleradiologists will not advance to an examination status of COMPLETE.

The post-install process associates RADIOLOGY,OUTSIDE SERVICE with all the active imaging locations in the IMAGING LOCATIONS (#79.1) file. Each imaging location has its own set of parameters defining location-specific criteria, such as, label/header/footer formats, printer devices for flash cards, jacket labels requests and reports, as well as how many labels to print.

### IENs in Diagnostic Codes File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch creates five new entries with correct internal entry numbers in the *local* DIAGNOSTIC CODES file, if a facility does not have the following entries with the exact internal entry numbers (IENs) in the DIAGNOSTIC CODES (#78.3) file.

- 999 TELERADIOLOGY, NOT YET DICTATED
- 1000 NO ALERT REQUIRED
- 1001 SIGNIFICANT ABNORMALITY, ATTN NEEDED
- 1002 CRITICAL ABNORMALITY
- 1003 POSSIBLE MALIGNANCY

When a facility has a diagnostic code record in the DIAGNOSTIC CODES file within the reserved IEN range, none of the aforementioned records are added to the local DIAGNOSTIC CODES file and an email message is sent to the VHA Radiology Informatics Committee mail group in Outlook, identifying the facility with this issue.

> **NOTE:** Do not modify or delete these DIAGNOSTIC CODES. These codes were established as standard diagnostic codes for communication between the teleradiology reading centers and the local VAMC sites. Codes 1001, 1002, and 1003 trigger an Abnormal Imaging Results notification to the requesting physician, and add the report to the Abnormal Exam Results management report.

### New Fields in RAD/NUC MED REPORTS File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch creates three new fields in the RAD/NUC MED REPORTS (#74) file.

- TELERADIOLOGY PHYSICIAN NAME (#9.1)
- TELERADIOLOGY PHYSICIAN NPI (#9.2)
- REPORT VERIFIED BY COTS APP (#9.3)

### New Fields in RAD/NUC MED HL7 APPLICATION EXCEPTION File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch creates two new fields in the RAD/NUC MED HL7 APPLICATION EXCEPTION (#79.7) file.

- DEFAULT DX FOR 'R' REPORT (#2.1)
- DEFAULT DX FOR 'F' REPORT (#2.2)

### New Parameter in RAD/NUC MED HL7 APPLICATION EXCEPTION File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds RA-SCIMAGE-TCP (a record in the HL7 APPLICATION PARAMETER (#771) file) to the RAD/NUC MED HL7 APPLICATION EXCEPTION (#79.7) file and defines data attributes for this record.

### HL7 ORU Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch makes it possible for VistA to accept HL7 report messages (ORU) from the teleradiology center and to automatically store the messages in VistA as verified reports, without requiring further intervention from the local medical center staff.

### Primary Dx Code Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch RA\*5.0\*84 revealed an issue with the data generated by the Abnormal Report option. Because of the way the cross-reference was created on the PRIMARY DIAGNOSTIC CODE (Node: 'P'; data dictionary: 70.03; fld: 13) field, some exams expected to display on the Abnormal Report did not. The old, traditional cross-reference is replaced with a new style cross-reference. The pre-install routine exported with this patch utilizes the correct VA FileMan utility to insure that this business rule-change is carried through to completion.

> **NOTE:** The primary Diagnostic Code data is found in the DIAGNOSTIC CODES (#78.3) file.

### RAHLO1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch updates and centralizes the report and exam lock logic. The locking and unlocking of both reports and exams happen in RAHLO1.

- LOCKX^RAHLTCPU handles exams.
- LOCKR^RAHLTCPU handles reports.

### OBR-7 Field for ORM HL7 V2.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data in the OBR-7 (Observation Date/Time) field for ORM (Order) HL7 V2.3 messages has changed. Prior to this patch, the date/time value placed in this field was the current date/time of execution or in VA FileMan NOW. This logic was correct because the message was generated immediately after the date/time the exam was registered.

With the advent of the \[RA HL7 RESEND BY DATE RANGE\]Resend Radiology HL7 Messages By Date Range option, HL7 messages are generated and broadcast long after the exam is registered. The NOW value raises an issue because the timestamp in OBR-7 is the time at which the \[RA HL7 RESEND BY DATE RANGE\] option is executed, as opposed to the date/time the exam is registered.

After this patch is installed, the date/time value placed in OBR-7 is the date/time the exam is registered. The date/time of registration is a far more accurate timestamp than the time of the actual patient encounter.

### Support for NTP Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The support plan for the release of patch RA\*5\*84 includes the addition of two new items in the Remedy software. The new NTP items are supported by Enterprise Product Support (EPS), Clinical Product Support (CPS), and Clinical 3 Team.

We are implementing the following Remedy Category-Type-Item for NTP:

Category Applications - VistA (existing)

Type Radiology

Item NTP (new)

Category Applications - VistA (existing)

Type Imaging 3.0

Item NTP (new)

## After Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch RA\*5.0\*84 exports the HL7 Application Parameter: RA-SCIMAGE-TCP.

The data in the Mail Group field is mandatory and must have a definition of: RAD HL7 MESSAGES.

> Example of how to set the entry

Name: RA-SCIMAGE-TCP Active/Inactive: ACTIVE

Facility Name: \<your facility id here\> Mail Group: RAD HL7 MESSAGES

Country Code: USA HL7 Encoding Characters: ^~\\

HL7 Field Separator: \|

> **NOTE:** Populate the Facility Name field. The Facility Name field is a free text field. Traditionally sites enter the facility name or station number when editing this field.

Patch RA\*5.0\*84 exports the following protocols:

- RA SCIMAGE ORM Type: Subscriber
- RA SCIMAGE ORU Type: Subscriber
- RA SCIMAGE TCP REPORT Type: Subscriber
- RA SCIMAGE TCP SERVER RPT Type: Event Driver

> **NOTE:** Do not associate the RA SCIMAGE subscriber protocols to the Radiology/Nuclear Medicine event driver protocols, if your facility is not participating in the National Teleradiology Project initiative.

Unnecessary HL7 messaging adds data to a facility's database, as well as to network traffic. Therefore, leave the task of linking the subscriber protocols to respective event drivers as your last step.

- Subscriber Protocol: RA SCIMAGE TCP REPORT is associated with the Receiving Application: RA-VOICE-SERVER
- Event Driver Protocol: RA SCIMAGE TCP SERVER RPT is associated with the Sending Application: RA-SCIMAGE-TCP

> **NOTE:** HL7 messaging commences when the designated subscriber protocols are associated with respective event driver protocols.

Patch RA\*5.0\*84 exports the HL LOGICAL LINK component: RA-SCIMAGE.

RA\*5.0\*84 exports RA-SCIMAGE with predetermined data attributes defined: LLP Type, TCP/IP Service Type, and so on. Do not edit these fields.

The TCP/IP Address and TCP/IP Port fields for RA-SCIMAGE differ from site to site. Because of this condition, these two fields are to be configured by the appropriate parties in the facility at which the patch is installed.

  
Step 1Example of how to edit theTCP/IP Address and TCP/IP Port fields

Identify the correct menu to use, in order to edit the TCP/IP Address and TCP/IP Port fields:

Select OPTION NAME: HL7 MAIN MENU HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

HLO HL7 (Optimized) MAIN MENU ...

Select HL7 Main Menu Option: Interface Developer Options

EA Application Edit

EP Protocol Edit

EL Link Edit this is the option to use

VI Validate Interfaces

Reports ...

Select Interface Developer Options Option: EL Link Edit

HL7 LOGICAL LINK

-----------------------------------------------------------------------------------

NODE: RA-SCIMAGE DESCRIPTION:

INSTITUTION:

MAILMAN DOMAIN:

AUTOSTART: Enabled

QUEUE SIZE: 10

LLP TYPE: TCP select 'TCP'; this action will bring you to a new screen

DNS DOMAIN:

-----------------------------------------------------------------------------------

HL7 LOGICAL LINK

-----------------------------------------------------------------------------------

-------------------------------TCP LOWER LEVEL PARAMETERS-------------------------

RA-SCIMAGE

TCP/IP SERVICE TYPE: CLIENT (SENDER)

TCP/IP ADDRESS: edit this field

TCP/IP PORT: edit this field

TCP/IP PORT (OPTIMIZED):

ACK TIMEOUT: 300 RE-TRANSMISION ATTEMPTS: 5

READ TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: shutdown

BLOCK SIZE: SAY HELO:

DIRECT CONNECT OPEN TIMEOUT:

STARTUP NODE: PERSISTENT: NO

RETENTION: UNI-DIRECTIONAL WAIT:

-----------------------------------------------------------------------------------

Step 2

RA-SCIMAGE must be associated with following subscriber protocols:

\* RA SCIMAGE ORM

\* RA SCIMAGE ORU

VAxxx must be associated with the \* RA SCIMAGE TCP REPORT subscriber protocol.

To accomplish this action, use the Protocol Edit option under the Select Interface Developer Options menu.

The RA-SCIMAGE logical link is exported as a non-persistent client.

Processes for non-persistent links hibernate when there are no more messages to exchange over the link. When there are additional messages to broadcast over this link the TCP Link Manager process *wakes up* the logical link.

To start the TCP Link Manager, use the TCP Link Manager Start/Stop option under the HL Main Menu and HL Menu Filer Link Mgt menus.

Name: RA SCIMAGE TCP REPORT Type: subscriber

Creator: Receiving Application: RA-VOICE-SERVER

Event Type: R01 Logical Link: VAxxx

Version ID: 2.3 Response Message Type: ACK

Processing Routine: D ^RAHLTCPB Sending Facility Required?: NO

Receiving Facility Required?: NO Security Required?: NO

VAxxx is the name of the multi-threaded listener running at each VAMC in the system. Each multi-threaded listener has a unique IP address, and all multi-threaded listeners have a port definition of 5000.

![](ra-5-84-release-notes/002.png)

How do you identify the proper name of the multi-threaded listener at your facility?

The best way is through the use of the VA FileMan SEARCH function.

Select OPTION: ?

Answer with OPTION NUMBER, or NAME

Choose from:

1 ENTER OR EDIT FILE ENTRIES

2 PRINT FILE ENTRIES

3 SEARCH FILE ENTRIES \<-- this is the option to use

4 MODIFY FILE ATTRIBUTES

5 INQUIRE TO FILE ENTRIES

6 UTILITY FUNCTIONS

7 OTHER OPTIONS

8 DATA DICTIONARY UTILITIES

9 TRANSFER ENTRIES

Select OPTION: SEARCH FILE ENTRIES

OUTPUT FROM WHAT FILE: HL LOGICAL LINK//

-A- SEARCH FOR HL LOGICAL LINK FIELD: INSTITUTION

-A- CONDITION: EQUALS

-A- EQUALS INSTITUTION: \<enter the name of your institution\>

-B- SEARCH FOR HL LOGICAL LINK FIELD: TCP

1 TCP/IP ADDRESS

2 TCP/IP OPENFAIL TIMEOUT

3 TCP/IP PORT n

4 TCP/IP PORT (OPTIMIZED)

5 TCP/IP SERVICE TYPE

CHOOSE 1-5: 3 TCP/IP PORT

-B- CONDITION: EQUALS

-B- EQUALS: 5000

-C- SEARCH FOR HL LOGICAL LINK FIELD:

IF: A&B INSTITUTION EQUALS \<your institution\>

and TCP/IP PORT EQUALS "5000"

OR:

STORE RESULTS OF SEARCH IN TEMPLATE:

SORT BY: NODE//

START WITH NODE: FIRST//

FIRST PRINT FIELD: .01 NODE

THEN PRINT FIELD:

Heading (S/C): HL LOGICAL LINK SEARCH Replace

DEVICE: HOME Right Margin: 80//

HL LOGICAL LINK SEARCH MAR 11,2008 11:26 PAGE 1

NODE

--------------------------------------------------------------------------

VAxxx

1 MATCH FOUND.

  
Example of RA SCIMAGE ORM

The procedure does not change based on the subscriber being edited. You edit the Logical Link field.

Select HL7 Main Menu Option: INterface Developer Options

EA Application Edit

EP Protocol Edit \<-- this is the option to use

EL Link Edit

VI Validate Interfaces

Reports ...

> Example of the first screen

HL7 INTERFACE SETUP PAGE 1 OF 2

--------------------------------------------------------------------------

NAME: RA SCIMAGE ORM

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber \<--hit the RETURN/ENTER key when this field ishighlighted.

--------------------------------------------------------------------------

HL7 SUBSCRIBER PAGE 2 OF 2

RA SCIMAGE ORM

--------------------------------------------------------------------------

RECEIVING APPLICATION: RA-SCIMAGE-TCP

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: O01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

LOGICAL LINK: \<-- enter RA-SCIMAGE here.

PROCESSING RTN:

ROUTING LOGIC:

--------------------------------------------------------------------------

Step 3

Associate the subscriber protocols with the event driver protocols.

> **NOTE:** HL7 messaging commences when the designated subscriber protocols are associated with respective event driver protocols.

Use the Protocol Edit option under the Interface Developer Options and HL7 Main Menu menus to associate the subscriber protocols with the event driver protocols.

- Subscriber Protocol: Associate RA SCIMAGE ORM with the event driver protocols: RA REG 2.3, RA EXAMINED 2.3, and RA CANCEL 2.3.
- Subscriber Protocol: Associate RA SCIMAGE ORU with the event driver protocol: RA RPT 2.3

> **NOTE:** Edit only the Subscribers field; editing any other field may compromise the integrity of the event driver protocol.

Example of associating a subscriber protocol with an event driver protocol

With RA REG 2.3 as the example, RA SCIMAGE ORM is a subscriber to RA REG 2.3, RA EXAMINED 2.3, and RA CANCEL 2.3; RA SCIMAGE ORU is a subscriber to RA RPT 2.3.

> **NOTE:** The process of adding a subscriber is the same, regardless of the message type.

Select HL7 Main Menu Option: INterface Developer Options

EA Application Edit

EP Protocol Edit \<-- this is the option to use

EL Link Edit

VI Validate Interfaces

Reports ...

Example of the first screen

HL7 INTERFACE SETUP PAGE 1 OF 2

--------------------------------------------------------------------------

NAME: RA REG 2.3

DESCRIPTION (wp): This protocol is triggered whenever a Radiology…

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver \<--hit the RETURN/ENTER key when this field ishighlighted.

--------------------------------------------------------------------------

0HL7 EVENT DRIVER PAGE 2 OF 2

RA REG 2.3

--------------------------------------------------------------------------

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

MESSAGE STRUCTURE:

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS \<-- this is the field that youwant to edit. Enter RA SCIMAGEORM here.

### From: RA*5*99 Release Notes

### Editing the 'Pregnancy Screen Comment' Prompt 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The 'Pregnancy Screen Comment' field is a required field, so the "@"command will not work. The workaround for this is to replace the entire comment with a new comment.
- If there are multiple occurrences of the word that you are replacing, only the first occurrence is replaced.
- The text is case-sensitive, so you must use the exact same case when entering the new text, in order for the replacement to take place.

> Note: For additional editing information, refer to the *Fileman Getting Started Manual*, sections: Default Responses and Longer Default Responses and the 'Replace…With' Editor  
> <http://www.va.gov/vdl/application.asp?appid=5>

#### How to replace a comment that is 20 characters or less

> Enter the replacement text after the double slashes (//). For example, at the 'Pregnancy Screen Comment' prompt:

> PREGNANCY SCREEN COMMENT: The patient had//  Enter the replacement text here

#### How to replace single and multiple words/line  

1.  At the 'Replace' prompt, enter the one word or multiple words//line you want to replace and press Enter.

> At the 'With' prompt, enter a new word or multiple words /line and press Enter.  
> The 'Replace' prompt displays again.

> To keep the word or multiple words /line just entered, press Enter.  
> To replace this word or these multiple words /line just entered, repeat steps 1 and 2 until all of the words/line are replaced.

> At the 'Replace' prompt, press Enter.  
> The updated comment displays and the system advances to the next prompt.

#### How to replace an entire comment

1.  At the 'Replace' prompt, enter 3 periods (…) and press Enter.  
    > The 'With' prompt displays.
2.  At the 'With' prompt, enter a new comment and press Enter.  
    > The 'Replace' prompt displays again.  
    > To keep the comment just entered, press Enter.

> To replace this comment just entered, enter another comment, and press Enter.

3.  At the 'Replace' prompt, press Enter.  
    > The updated comment displays and the system advances to the next prompt.
3.  The existing Pregnant field label is replaced with Pregnant At Time Of Order Entry in several options and reports.
- No functionality is changed.
- This field reflects the pregnancy status for a female patient between 12 and 55 years old at the time the order was placed.

On the Complication Report (on the 'Daily Management Reports' option), the Interpreting Stf. field label is changed to Staff Imaging Phys for both instances.

The defect reported on the 'Request an Exam' option, Remedy ticket# HD0000000309290, is fixed.

- The issue: in order to populate the pregnancy status, you must edit the pregnancy status in the same session in which you entered the request.
- This is a defect because the PREGNANT prompt should display when initially entering the request (rather than going back and editing the request at the 'Do you want to change any of the above? NO//' prompt).

On the 'Display a Rad/Nuc Med Report' and 'Resident On-Line Pre-Verification'options (off of the 'Films Reporting' menu), the Staff Phys field label is changed to Staff Imaging Phys.

The following automated emails are updated with the Pregnancy Screen and Pregnancy Screen Comment fields:

1.  The VistA email report when a user verifies a report.
2.  The VistA/CPRS alert when an image contains abnormal results.

In CPRS, Detailed Report on the Reports tab is updated with the Pregnancy Screen and Pregnancy Screen Comment fields.

### From: RA*5*75 Release Notes

## Issue One – Reason for Study

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch will require the user entering an exam request to input the reason for the request into a new field, REASON FOR STUDY, which is stored in the RAD/NUC MED ORDERS (#75.1) file. The CLINICAL HISTORY FOR EXAM prompt will become optional.

VistA Radiology/Nuclear Medicine reports, orders, and patient profile options have been enhanced to display both the REASON FOR STUDY and CLINICAL HISTORY data.

This issue arose from the inability of the Nuance PowerScribe voice recognition system to receive CLINICAL HISTORY data of indefinite length. It can only receive the REASON FOR STUDY data of a limited length, 64 characters maximum, which meets DICOM standards.

Because the physician using PowerScribe cannot view the REASON FOR STUDY that is embedded in the CLINICAL HISTORY, s/he had to switch over to the VistA Radiology system to get the data. This patch will eliminate the need for PowerScribe users to access REASON FOR STUDY from the VistA Radiology system.

> Special Notice for sites using Nuance PowerScribe

> PowerScribe cannot handle certain characters that may be entered into the new REASON FOR STUDY field. Inclusion of any of these characters will cause the entire order to disappear from the PowerScribe display screen.

> These characters are reserve characters in XML:

> Ampersand (&), Apostrophe ('), Quote ("), Greater Than (\>), and Less Than (\<).

> PowerScribe has a software fix planned, but has not announced a release date for this fix. Therefore, the person responsible for your site's PowerScribe interface should contact the PowerScribe National Support Center at 800.833.7776 and request a Dictaphone work order to correct this issue before patch RA\*5.0\*75 is installed at your site.

### Operation when ordering through the front door – CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS GUI v26 now displays one box for both HISTORY and REASON FOR EXAM. Because the CPRS GUI cannot be modified at this time, this patch will auto-populate the REASON FOR STUDY field with "See Clinical History:" in the background. This statement will be displayed in various reports, orders, and patient profiles where CLINICAL HISTORY is displayed.

CPRS GUI v27 (OR\*3.0\*243) will have separate boxes for REASON FOR STUDY and for CLINICAL HISTORY. As mentioned above, CLINICAL HISTORY will then be optional.

### Operation when ordering through the backdoor – Radiology/Nuclear Medicine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Radiology/Nuclear Medicine now collects the REASON FOR STUDY (required) and CLINICAL HISTORY (optional). When this patch is installed, CPRS GUI v26 will display both the REASON FOR STUDY and the CLINICAL HISTORY inside the existing HISTORY & REASON FOR EXAM box in a three-line format as follows:

REASON FOR STUDY will be displayed first and flagged by "REASON FOR STUDY:" then a line of hyphens, then the CLINICAL HISTORY. For example:

> REASON FOR STUDY: This is an example only

> ------------------------------------------

> The Clinical History starts here..........

CPRS GUI v27 (OR\*3.0\*243) will display REASON FOR STUDY and CLINICAL HISTORY in separate boxes. As mentioned above, CLINICAL HISTORY will then be optional.

## Issue Two - Patient Age display and algorithm

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch changes the way a patient's age is displayed at the top of a report requisition. The incorrect patient age was displayed through these two options:

- Print Rad/Nuc Med Requests by Date \[RA ORDERPRINTS\]
- Print Selected Requests by Patient \[RA ORDERPRINTPAT\]

The patient's age had been calculated against the date the request was displayed, instead of calculating the patient's age against the date the request was entered. Since users expect to see the patient's age at the time the exam was requested, a modification has been made in routine RAORD5 to calculate the patient's age based on:

- The patient's Date of Birth
- The date the request was entered.

In addition, routine RAORD6 was modified to change the request report header:

- The label "Age" has been changed to "Age at req"
- The first line now contains the word "Printed:" to indicate that the date is the date of printing, not the date of the request.

## Issue Three – Date Desired default

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies the exam request process by removing the default value from the "Date Desired" field. Whether an order is entered through CPRS or through the Radiology/Nuclear Medicine application, an erroneously entered "Date Desired" value impacts a radiology department's ability to comply with the thirty day outpatient appointment wait times mandate. Physicians sometimes use the default date of "Today" as a matter of convenience, rather than entering the actual date they want the examination to take place.

The automatic default date of "Today" has been removed, and physicians are now required to enter a date they actually desire to have the examination. This patch only addresses the backdoor (VistA Radiology/Nuclear Medicine application) order entry. CPRS GUI v27 will address the front door removal of "Today" as the default to "Date Desired."

### From: RA*5*81 Release Notes

## Enhancement \#1:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Radiology 5.0 application has established business rules for sharing an exam report between multiple cases, and for registering multiple cases at the same exam date/time:

- Cases from different orders should have their own separate reports (single orders)
- Cases from a parent procedure order should share the same report (printset)
- Cases from a parent procedure cannot be registered at the same time with cases from other orders
- Cases from more than one parent procedure cannot be registered at the same time

These business rules are not always followed by radiology departments when using voice recognition (VR) dictation systems.

Some VR systems may allow the user to group two or more cases from separate orders and dictate one report for these cases (sometimes referred to as "printset on the fly"), even though these cases were not defined to share the same report. The VR system sends this single dictated report as separate OBR segments within one HL7 message (one OBR segment for each case) to the VistA Radiology application. In the past, Radiology only accepted the first of this group of OBR segments and ignored the remaining OBR segments without sending back reject HL7 messages to notify the sending VR system that some of their OBR segments were not accepted.

This patch will modify the Radiology application's processing of an incoming HL7 message with multiple OBR segments from VR, to account for this deviation from business rules.

### Parent Procedures and Printsets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- If VR sends an HL7 message with multiple OBR segments for one dictated report based upon cases from separate orders, the Radiology application will make a separate record in the RAD/NUC MED REPORTS file (#74) for each case. The report text and impression will be identical in these separate records in file \#74.
- If VR sends an HL7 message with multiple OBR segments for one dictated report based upon cases from separate orders AND a parent procedure (printset), the Radiology application will make a separate record in the RAD/NUC MED REPORTS file (#74) for each of the cases from separate orders, but only one report record in file \#74 for all the cases within the parent procedure (printset). The report text and impression will be identical in these separate records in file \#74.
- If VR sends an HL7 message with multiple OBR segments for one dictated report based upon cases from two or more parent procedures, the Radiology application will make a separate record in the RAD/NUC MED REPORTS file (#74) for each printset under the parent procedure, but not for each case within those printsets. The report text and impression will be identical in these separate records in file \#74.

### Amended Reports and Addendums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- If VR sends an HL7 message with multiple OBR segments for the same addendum based upon cases from separate orders, the Radiology application will put the addendum into each of the existing report records for each case that is expected to have a separate report.
- If VR sends an HL7 message with multiple OBR segments for the same addendum based upon cases from separate orders and a parent procedure, the Radiology application will put the addendum into each of the existing report records for the cases that are expected to have separate reports, and the same addendum into the shared report record for the cases that are expected to share a report (those in a printset under a parent procedure).
- If VR sends an addendum that is identical to the existing verified report in the VistA database, the Radiology application will reject this message.

## Enhancement \#2:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a HL7 ORU report message is received by the Radiology application, the Radiology application files the report and broadcasts out the HL7 report message to all known subscribers. This allows all subscribers (including the original VR sender) to be updated with the same report. This patch allows the original sender to decide whether or not to prevent the Radiology application from broadcasting the HL7 report message back to them.

## Enhancement \#3:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new file has been created to hold parameters related to the application exceptions generated while processing Radiology HL7 messages: \#79.7 – Rad/Nuc Med Application Exception File. See the Radiology/Nuclear Medicine 5.0 Technical Manual for the detailed file description and security settings.

### From: RA*5*226 Release Notes

## Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Activate a selection of individual procedures

Activate or Inactivate the new standard procedures?: 1 Activate

Select one of the following:

1 Choose Individual Procedures

2 By Modality

3 All

How do you want to activate the new Oracle/Cerner standard procedures?: 1 Choose Individual Procedures

Select Procedures(s): MRI ABDOMEN\*

Another one (Select/De-Select): MRI ANKLE W/O CONTRAST LEFT (MRI Inactive) CPT:73721

Another one (Select/De-Select): US UPPER EXT\*

Another one (Select/De-Select):

MRI ABDOMEN W/ + W/O CONTRAST Activated!

MRI ABDOMEN W/ CONTRAST Activated!

MRI ABDOMEN W/O CONTRAST Activated!

MRI ANKLE W/O CONTRAST LEFT Activated!

US UPPER EXT ARTERIAL DUPLEX BILATERAL Activated!

US UPPER EXT ARTERIAL DUPLEX LEFT Activated!

US UPPER EXT ARTERIAL DUPLEX RIGHT Activated!

US UPPER EXT VEIN MAPPING BILATERAL Activated!

US UPPER EXT VEIN MAPPING LEFT Activated!

US UPPER EXT VEIN MAPPING RIGHT Activated!

US UPPER EXT VENOUS DUPLEX BILATERAL Activated!

US UPPER EXT VENOUS DUPLEX LEFT Activated!

US UPPER EXT VENOUS DUPLEX RIGHT Activated!

US UPPER EXT VENOUS PHYS STUDY BILAT Activated!

2.  Activate a selection by Modality

Select Procedure Edit Menu \<TEST ACCOUNT\> Option: activate/Inactivate Standard Procedures

Select one of the following:

1 Activate

2 Inactivate

Activate or Inactivate the new standard procedures?: 1 Activate

Select one of the following:

1 Choose Individual Procedures

2 By Modality

3 All

How do you want to activate the new Oracle/Cerner standard procedures?: 2 By Modality

Select an Imaging Type to activate: ??

Choose from:

ANGIO/NEURO/INTERVENTIONAL

CARDIOLOGY STUDIES (NUC MED)

CT SCAN

GENERAL RADIOLOGY

MAGNETIC RESONANCE IMAGING

MAMMOGRAPHY

NUCLEAR MEDICINE

ULTRASOUND

VASCULAR LAB

Select an Imaging Type to activate: NM NUCLEAR MEDICINE

NM KIDNEY FUNCTION STUDY NON-IMAGING Activated!

NM KIDNEY IMAGING MULTIPLE W/+W/O PHARM Activated!

NM KIDNEY IMAGING SINGLE W/ PHARM Activated!

NM KIDNEY IMAGING SINGLE W/O PHARM Activated!

NM KIDNEY MORPH IMAGING Activated!

NM KIDNEY MORPH IMAGING W/ VASCULAR FLOW Activated!

NM KIDNEY SPECT Activated!

NM LABELED RED CELL SEQUESTRATION Activated!

NM LIVER IMAGING SPECT Activated!

NM LIVER IMAGING SPECT W/ VASCULAR FLOW Activated!

NM LIVER IMAGING STATIC Activated!

NM LIVER IMAGING W/ VASCULAR FLOW Activated!

3.  Inactivate ALL procedures

> Select Procedure Edit Menu \<TEST ACCOUNT\> Option: activate/Inactivate Standard Procedures

> Select one of the following:

> 1 Activate

> 2 Inactivate

> Activate or Inactivate the new standard procedures?: 2 Inactivate

> Select one of the following:

> 1 Choose Individual Procedures

> 2 By Modality

> 3 All

> How do you want to inactivate the new Oracle/Cerner standard procedures?: 3 All

> Are you sure you want to inactivate ALL of the Oracle/Cerner procedures? y YES

> MRI ABDOMEN W/ + W/O CONTRAST Inactivated!

> MRI ABDOMEN W/ CONTRAST Inactivated!

> MRI ABDOMEN W/O CONTRAST Inactivated!

> MRI ANKLE W/O CONTRAST LEFT Inactivated!

> NM KIDNEY FUNCTION STUDY NON-IMAGING Inactivated!

> NM KIDNEY IMAGING MULTIPLE W/+W/O PHARM Inactivated!

> NM KIDNEY IMAGING SINGLE W/ PHARM Inactivated!

> NM KIDNEY IMAGING SINGLE W/O PHARM Inactivated!

> NM KIDNEY MORPH IMAGING Inactivated!

> NM KIDNEY MORPH IMAGING W/ VASCULAR FLOW Inactivated!

> NM KIDNEY SPECT Inactivated!

> NM LABELED RED CELL SEQUESTRATION Inactivated!

> NM LIVER IMAGING SPECT Inactivated!

> NM LIVER IMAGING SPECT W/ VASCULAR FLOW Inactivated!

> NM LIVER IMAGING STATIC Inactivated!

> NM LIVER IMAGING W/ VASCULAR FLOW Inactivated!

> US UPPER EXT ARTERIAL DUPLEX BILATERAL Inactivated!

> US UPPER EXT ARTERIAL DUPLEX LEFT Inactivated!

> US UPPER EXT ARTERIAL DUPLEX RIGHT Inactivated!

> US UPPER EXT VEIN MAPPING BILATERAL Inactivated!

> US UPPER EXT VEIN MAPPING LEFT Inactivated!

> US UPPER EXT VEIN MAPPING RIGHT Inactivated!

> US UPPER EXT VENOUS DUPLEX BILATERAL Inactivated!

> US UPPER EXT VENOUS DUPLEX LEFT Inactivated!

> US UPPER EXT VENOUS DUPLEX RIGHT Inactivated!

> US UPPER EXT VENOUS PHYS STUDY BILAT Inactivated!

### From: RA*5*77 Release Notes

## \#1 – Subscript error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user attempts to display a Radiology alert notification in the CPRS Patient Selection screen, a subscript error is filed in the error trap. This happens when an alert is opened/read elsewhere and the data has not yet been updated in CPRS. In other words, CPRS does not know that the alert has been read and the accompanying TMP global nodes have been deleted.

Resolution: Routine RAO7PC4 has been modified to to sense the absence of the data variable causing the subscript error, allowing normal logic flow to continue.

## \#2 – Missing RVU values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When using the new RVU (Relative Value Unit) reporting software, no RVU is being returned/utilized on some CPT codes.

Resolution: It has been determined that "G" codes recently converted to CPT codes do not contain an RVU value for entries without CPT code modifiers.The RVU reporting software has been modified to default a -26 CPT modifier when calling the API RVU^FBRVU . This will ensure that the appropriate RVU is returned. It is only called if the RVU value is 0 and the modifier is null.

## \#3 – Scrolling issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When using View Exam by Case No. \[RA VIEWCN\] option, the Exam Activity section scrolls out of view when displaying to the screen if there are more than two lines of Exam Activity to be displayed.

Resolution: Routine RAPROD1 has been modified to cause the display to pause and ask 'Press Return to continue or "^" to exit:" to prevent exam data from scrolling out of view.

## \#4 – RVU Reporting issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Normally, a Fee Basis patch is released each year that contains the new RVU data for the current calendar year. In some instances the needed data will not be available for an unspecified amount of time into the new calendar year.

Resolution: The RVU reporting routines have been modified to sense whether the new RVU data is available from FEE BASIS and if not, will calculate the reports with the previous year's RVU data. A note will also be placed in the report headers to denote the use of a previous calendar year's data.

## \#5 – Scaling Factor issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When listing the Work RVU Scaling factors, the following Scaled RVU reports do not print scaling factors for imaging types that do not contain an entry in the IMAGING TYPE file (#79.2), SCALING FACTOR CY field (#200):

- Physician scaled wRVU Report by Imaging Type \[RA WKLIPHY SWRVU ITYPE\]
- Physician scaled wRVU Report by CPT \[RA WKLIPHY SWRVU CPT\]
- Procedure Scaled wRVU/CPT Report \[RA PROC CPTSWRVU\]

Resolution: Modifications will be made to the Work RVU reporting routines to print a default listing of each imaging type that does not have an entry in the SCALING FACTORY CY field (#200) of the IMAGING TYPE file (#79.2) by showing that it has a default scaling factor of 1.

Example:

> ULTRASOUND US 1.00 (default)

### From: RA*5*82 Release Notes

### Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the Imaging Type of "General Radiology," only the exam status of TRANSCRIBED has the GENERATE EXAMINED HL7 MESSAGE field set to "Y". Thus, an Examined ORM message will be broadcast when a General Radiology case has reached or exceeded the exam status of TRANSCRIBED.

### Exception:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If one or more of the following five essential fields were changed during exam editing, then an Examined ORM message will be broadcast regardless of the two conditions above:

PROCEDURE

PROCEDURE MODIFIER

REQUESTING PHYSICIAN

CPT MODIFIER

TECHNOLOGIST COMMENT

In some sites, depending on the type of PACS (Picture Archiving and Communication System) being used, this exception may cause exams to be dropped from a PACS modality worklist when essential fields are updated on the PACS from Vista Radiology. To restore the exam to the PACS modality worklist, use the "Resend Radiology HL7 Message" \[RA HL7 MESSAGE RESEND\] option to re-broadcast the HL7 ORM message for that exam.

> *Note:* The "Resend Radiology HL7 Message" option requires the RA MGR security key. Since the RA MGR key also allows access to other supervisor-level options, sites may wish to create a local menu for the clerks and technologists who are given the RA MGR key. Your IRM can create a local menu for the "Resend Radiology HL7 Message" option so that other supervisor-level options are not accessible.

It is still possible to use the "Cancel an Exam" \[RA CANCEL\] option to cancel a case (not the exam request) and then re-register the case to put it back on the modality worklist, if necessary.

## Issues resolved with RA\*5\*82

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the previous patch RA\*5\*71 allowed the broadcasting of HL7 messages after each exam edit session, the following problems were noticed at sites that had COTS (Commercial off-the-shelf software ) PACS and Stentor systems.

1)  On certain PACS, a subsequent broadcast of an HL7 ORM message caused the exam to be removed from the modality work list.
2)  On the Stentor system, a subsequent broadcast of an HL7 ORM message caused the report on the Stentor system to become invalidated. This occurred when the report was manually verified via the Vista "Report Entry/Edit" \[RA RPTENTRY\] option instead of electronically verified via a voice recognition dictation system.
3)  The "Examination Status Entry/Edit" \[RA EXAMSTATUS\] option wasn't prompting for "Generate Examined HL7 Message:" anymore, which prevented Radiology ADPACs from editing this field.

This patch resolves these reported problems. The GENERATE EXAMINED HL7 MESSAGE field will be restored to the RA STATUS ENTRY input template for the EXAMINATION STATUS file (#72).
