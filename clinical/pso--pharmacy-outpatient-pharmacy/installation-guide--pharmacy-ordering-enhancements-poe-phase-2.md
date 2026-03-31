---
title: Pharmacy Ordering Enhancements (POE) Phase 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject: Pharmacy Ordering Enhancements (POE) Phase 2
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this Installation Guide is to provide an explanation of the installation process for the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build. The intended audience for this document is the Information Resources Management Service (IRMS) staff and Pharmacy staff responsible for instal
audience: 
keywords: 
  - orwdq
  - pharmacy
  - psoz
  - cprs
  - installation
  - install
  - ordering
  - enhancements
  - build
  - outpatient
page_count: 0
word_count: 4843
section_count: 1
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/cprs_poe_1_0_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/cprs_poe_1_0_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

> ![](pharmacy-ordering-enhancements-poe-phase-2-installation-guide/001.png)

pharmacy ordering enhancements  
(poe)phase 2

######### 

######### INSTALLATION GUIDE

PSO\*7\*46

OR\*3\*94

PSS\*1\*38

PSJ\*5\*50

September 2001

V*IST*A System Design & Development

# # \< This page left blank for two-sided printing. \>


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# \< This page left blank for two-sided printing. \>](#this-page-left-blank-for-two-sided-printing)
- [Purpose](#purpose)
- [Scope](#scope)
- [Pre-Installation](#pre-installation)
- [Minimum Required Packages](#minimum-required-packages)
- [Required Patches](#required-patches)
- [Installation](#installation)
- [Installation Steps](#installation-steps)
- [Post-Installation](#post-installation)

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide an explanation of the installation process for the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build. The intended audience for this document is the Information Resources Management Service (IRMS) staff and Pharmacy staff responsible for installing and maintaining the Pharmacy files required for drug selection through Pharmacy and Computerized Patient Record System (CPRS).

The Pharmacy Ordering Enhancements (POE) Phase 2 project completes the work that the POE Pharmacy Data Management (PDM) Pre-Release began. The earlier POE PDM Pre-Release project created new fields and provided reports and options to assist in the population and maintenance of data that would be necessary for the installation of this CPRS/Pharmacy Ordering Enhancements 1.0 Master Build.

The POE Phase 2 project includes the installation of the PSO\*7\*46, OR\*3\*94, PSS\*1\*38, and PSJ\*5\*50 patches, which will provide or relocate needed functionality and delete obsolete options. These changes will allow for streamlining of the medication order entry process, expanded order checking, and improved medication order transfer between the Inpatient Medications and Outpatient Pharmacy applications.

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS Clinical Workgroup (the Workgroup) requested changes in the Pharmacy medication ordering dialogs in order to eliminate the need for redundant entry of drug information during medication order entry and to improve the process for transferring orders between the Inpatient Medications and Outpatient Pharmacy applications. Additional enhancement requests from the Workgroup were to provide order checks for all medication orders entered through CPRS and to provide drug specific information during medication order entry.

\< This page left blank for two-sided printing. \>

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pharmacy-ordering-enhancements-poe-phase-2-installation-guide/002.png)

Significant changes to routines, options, files and fields will occur with the installation of the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build. Prior to installation of the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build the installer should carefully read the Pharmacy Ordering Enhancements (POE) Phase 2 Release Notes found on the V*ist*A Documentation Library (VDL) web page at <http://vista.med.va.gov/vdl>.

Additionally, before installing the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build, it is imperative that the POE PDM Pre-Release patch PSS\*1\*34 be installed and that the setup steps in the POE PDM Pre-Release Implementation Guide be completed. Instructions on the installation of PSS\*1\*34 and the necessary modifications to Pharmacy files can be found in the POE PDM Pre-Release Implementation Guide in the VDL at <http://vista.med.va.gov/>vdl.

Note that the earlier POE PDM Pre-Release changes were made directly into the production account. Therefore, the production account must be mirrored to the test account prior to the installation of the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build into the test account, to insure that the test account will be current.

Once the production account has successfully been mirrored to the test account, the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build can then be installed into the test account.

Prior to installation of the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build, as many pending Outpatient Pharmacy and Inpatient Medication orders should be finished as possible.

![](pharmacy-ordering-enhancements-poe-phase-2-installation-guide/003.png) OR\*3\*109 and the associated GUI executable file must be installed prior to the installation of the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build for all Pharmacy Ordering Enhancements Phase 2 functionality to be available to the CPRS user. See the OR\*3\*109 patch description for installation instructions and requirements.

![](pharmacy-ordering-enhancements-poe-phase-2-installation-guide/004.png)Before beginning the installation of the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build, the IRMS representative, or party responsible for installing the patch, should mirror the current production account to the test account so that it will be updated to reflect all changes made as a result of the POE PDM Pre-Release project. Once the production account has been mirrored to the test account, the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build may be installed into the test account.

# Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This CPRS/Pharmacy Ordering Enhancements 1.0 Master Build can only be run with a standard MUMPS operating system and requires the following Department of Veterans Affairs (VA) software packages.

|                                              |                            |
|----------------------------------------------|----------------------------|
| Package                                  | Minimum Version Needed |
|                                              |                            |
| Pharmacy Data Management (PDM)               | 1.0                        |
| VA FileMan                                   | 22.0                       |
| Kernel                                       | 8.0                        |
| Patient Information Management System (PIMS) | 5.3                        |
| National Drug File (NDF)                     | 4.0                        |
| Integrated Billing                           | 2.0                        |
| Fee Basis                                    | 3.5                        |
| Adverse Reaction Tracking (ART)              | 4.0                        |
| Inpatient Medications (IM)                   | 5.0                        |
| IFCAP                                        | 5.0                        |
| Laboratory                                   | 5.2                        |
| Order Entry/Results Reporting (OERR)         | 3.0                        |
| Outpatient Pharmacy (OP)                     | 7.0                        |
| Decision Support System                      | 3.0                        |
|                                              |                            |

The above software is not included in this Master Build and must be installed for this build to be completely functional.

\< This page left blank for two-sided printing. \>

# Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to installation of this CPRS/Pharmacy Ordering Enhancements 1.0 Master Build, the following patches must be installed into each of the applications listed below.

#### Outpatient Pharmacy V. 7.0

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>PSO*7*41</p>
<p>PSO*7*49</p>
<p>PSO*7*51</p>
<p>PSO*7*54</p></td>
<td><p>PSO*7*55</p>
<p>PSO*7*62</p>
<p>PSO*7*64</p></td>
</tr>
</tbody>
</table>

#### Computerized Patient Record System V. 1.0

OR\*3\*11

OR\*3\*87

OR\*3\*97

OR\*3\*99  
OR\*3\*106

OR\*3\*108

OR\*3\*109

Pharmacy Data Management V. 1.0

#### PSS\*1\*20 PSS\*1\*27

#### PSS\*1\*33

#### PSS\*1\*34 PSS\*1\*40

PSS\*1\*45

#### Inpatient Medications V. 5.0

#### PSJ\*5\*47 PSJ\*5\*49 PSJ\*5\*51

#### PSJ\*5\*60  

\< This page left blank for two-sided printing. \>

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The POE Phase 2 project is comprised of four patches. All four patches will install when the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build is loaded into the test account. Patch PSO\*7\*46 will load first, followed by OR\*3\*94, PSS\*1\*38, and PSJ\*5\*50. Please read the following installation instructions carefully before beginning the installation. Information on routines, options, protocols, files, and fields that have been deleted or changed can be found in the POE Release Notes in the V*ist*A Documentation Library at <http://vista.med.va.gov/vdl>.

Before installing this patch, use the TaskMan *List Tasks* option to list currently running tasks. It is recommended that no Outpatient Pharmacy, Inpatient Medications, PDM or CPRS tasks be running at the time of this installation. The suggested time to install is during non-peak requirement hours for Outpatient Pharmacy, Inpatient Medications, PDM, BCMA, and CPRS users. For best results, it is recommended that this patch not be installed while Outpatient Pharmacy, Inpatient Medications, PDM, BCMA, or CPRS users are using the software. Additionally, Consolidated Mail Outpatient Pharmacy (CMOP) transmissions should not be taking place during the installation of the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build.

The user who installs the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build should receive several mail messages when the installation is complete. These messages are sent only to the person who performs the installation. Installers may want to consider forwarding these messages to additional staff as deemed appropriate. Examples of these messages are contained in the Post-Installation section of this manual.

PSO\*7\*46 queues a background job within the post-install routine. This routine sets the field POE RX in the Prescription file (#52) equal to 1. The setting of this field is not dependant on any other data entered into the file. Because this background is not dependant on any other data there is not a restart entry point. The background job will display as “Flagging All Prescriptions as POE Orders.”

This patch will be available only as a host file. The name of the file is CPRS_POE_10.KID. This file needs to be retrieved in ASCII format.

Sites will retrieve VistA software from the following FTP addresses. The preferred method is to FTP the files from <span class="mark">REDACTED</span>. This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows.

<u>OI Field Office</u> <u>FTP Address</u> <u>Directory</u>

<span class="mark">REDACTED</span>

Installation should take no longer than 30 minutes.

\< This page left blank for two-sided printing. \>

# Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Download the KIDS file CPRS_POE_10.KID via FTP. This file needs to be retrieved in ASCII format.

2\. Review mapped sets for the PSO\*, OR\*, PSS\*, PSJ\*, PSG\*, -PSGW\* and PSIV\* namespaces. If the routines are mapped, they should be removed from the mapped set at this time.

3\. From the *Kernel Installation & Distribution System* menu, select the *Installation* menu.

4\. From this menu, select the *Load a Distribution* option*.* When prompted for a file name, enter CPRS_POE_10.KID

5\. From this menu, the installer may select to use the following options:

(When prompted for INSTALL NAME, enter CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0)

a\. *Backup a Transport Global* - This option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.

b\. *Compare Transport Global to Current System -* This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

c\. *Verify Checksums in Transport Global* - This option will ensure the integrity of the routines that are in the transport global.

6\. Use the *Install Package(s)* option and select the package CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0.

7\. When prompted, "Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//" respond NO.

8\. When prompted, "Want KIDS to INHIBIT LOGONs during the install? YES//" respond NO.

9\. When prompted, "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//" respond NO.

10\. If routines were unmapped as part of step 2, they should be returned to the mapped set once the installation has run to completion.

\< This page left blank for two-sided printing. \>

#### Example of Installation

Select Kernel Installation & Distribution System Option: INstallation

Select Installation Option: LOad a Distribution

Enter a Host File: CPRS_POE_10.KID

KIDS Distribution saved on Aug 01, 2001@11:38:38

Comment: CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0

This Distribution contains Transport Globals for the following Package(s):

CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0

PSO\*7.0\*46

OR\*3.0\*94

PSS\*1.0\*38

PSJ\*5.0\*50

Distribution OK!

Want to Continue with Load? YES// \<Enter\>

Loading Distribution...

Build CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0 has an Enviromental Check Routine

Want to RUN the Environment Check Routine? YES//\<Enter\>

CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0

Will first run the Environment Check Routine, PSSPRE38

PSO\*7.0\*46

OR\*3.0\*94

PSS\*1.0\*38

PSJ\*5.0\*50

Use INSTALL NAME: CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0 to install this Distribution.

Select Installation Option: INstall Package(s)

Select INSTALL NAME: CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0 Loaded from Distribution 8/1/01@11:43:39

=\> CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0 ;Created on Aug 01, 2001@11:3

This Distribution was loaded on Aug 01, 2001@11:43:39 with header of

CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0 ;Created on Aug 01, 2001@11:38:38

It consisted of the following Install(s):

CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0 PSO\*7.0\*46 OR\*3.0\*94

PSS\*1.0\*38 PSJ\*5.0\*50

Checking Install for Package CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0

Will first run the Environment Check Routine, PSSPRE38

Install Questions for CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0

Checking Install for Package PSO\*7.0\*46

Install Questions for PSO\*7.0\*46

Incoming Files:

52 PRESCRIPTION (Partial Definition)

> **NOTE:** You already have the 'PRESCRIPTION' File.

52.41 PENDING OUTPATIENT ORDERS (Partial Definition)

> **NOTE:** You already have the 'PENDING OUTPATIENT ORDERS' File.

Checking Install for Package OR\*3.0\*94

Install Questions for OR\*3.0\*94

Incoming Files:

101.41 ORDER DIALOG (including data)

> **NOTE:** You already have the 'ORDER DIALOG' File.

I will REPLACE your data with mine.

101.43 ORDERABLE ITEMS (Partial Definition)

> **NOTE:** You already have the 'ORDERABLE ITEMS' File.

Checking Install for Package PSS\*1.0\*38

Install Questions for PSS\*1.0\*38

Incoming Files:

50 DRUG (Partial Definition)

> **NOTE:** You already have the 'DRUG' File.

50.606 DOSAGE FORM (Partial Definition)

> **NOTE:** You already have the 'DOSAGE FORM' File.

50.7 PHARMACY ORDERABLE ITEM (Partial Definition)

> **NOTE:** You already have the 'PHARMACY ORDERABLE ITEM' File.

51 MEDICATION INSTRUCTION (Partial Definition)

> **NOTE:** You already have the 'MEDICATION INSTRUCTION' File.

51.1 ADMINISTRATION SCHEDULE (Partial Definition)

> **NOTE:** You already have the 'ADMINISTRATION SCHEDULE' File.

52.6 IV ADDITIVES (Partial Definition)

> **NOTE:** You already have the 'IV ADDITIVES' File.

52.7 IV SOLUTIONS (Partial Definition)

> **NOTE:** You already have the 'IV SOLUTIONS' File.

55 PHARMACY PATIENT (Partial Definition)

> **NOTE:** You already have the 'PHARMACY PATIENT' File.

59.7 PHARMACY SYSTEM (Partial Definition)

> **NOTE:** You already have the 'PHARMACY SYSTEM' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Checking Install for Package PSJ\*5.0\*50

Install Questions for PSJ\*5.0\*50

Incoming Files:

53.1 NON-VERIFIED ORDERS (Partial Definition)

> **NOTE:** You already have the 'NON-VERIFIED ORDERS' File.

53.2 UNIT DOSE ORDER SET (Partial Definition)

> **NOTE:** You already have the 'UNIT DOSE ORDER SET' File.

53.3 ACTIVITY LOG REASON (including data)

> **NOTE:** You already have the 'ACTIVITY LOG REASON' File.

I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by entering a ‘Q’ at the device prompt.

DEVICE: HOME// \<Enter device here.\>

Install Started for CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0 :

Aug 01, 2001@15:48:59

Build Distribution Date: Aug 01, 2001

Installing Routines:

Aug 01, 2001@15:48:59

Install Started for PSO\*7.0\*46 :

Aug 01, 2001@15:48:59

Build Distribution Date: Aug 01, 2001

Installing Routines:

Aug 01, 2001@15:49:03

Installing Data Dictionaries:

Aug 01, 2001@15:49:06

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Located in the PSO (OUTPATIENT PHARMACY) namespace.

Located in the PSO (OUTPATIENT PHARMACY) namespace.

Installing LIST TEMPLATE

Aug 01, 2001@15:49:09

Running Post-Install Routine: EN^PSOPOST2

Queuing Background Job to Flag Prescriptions as POE Orders...

Attempting to Convert Outpatient Pharmacy Pre-POE Pending Orders...

Updating Routine file...

The following Routines were created during this install:

PSOXZA

PSOXZA1

PSOXZA10

PSOXZA2

PSOXZA3

PSOXZA4

PSOXZA5

PSOXZA6

PSOXZA7

PSOXZA8

PSOXZA9

Updating KIDS files...

PSO\*7.0\*46 Installed.

Aug 01, 2001@15:49:11

Install Message sent \# 32156890

Install Started for OR\*3.0\*94 :

Aug 01, 2001@15:49:11

Build Distribution Date: Jul 31, 2001

Installing Routines:

Aug 01, 2001@15:49:14

Running Pre-Install Routine: PRE^ORY94

Installing Data Dictionaries:

Aug 01, 2001@15:49:15

Installing Data: ..........

Aug 01, 2001@15:49:28

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Aug 01, 2001@15:49:28

Running Post-Install Routine: EN^ORY94

Updating Routine file...

Updating KIDS files...

OR\*3.0\*94 Installed.

Aug 01, 2001@15:49:30

Install Message sent \# 32156892

Install Started for PSS\*1.0\*38 :

Aug 01, 2001@15:49:30

Build Distribution Date: Aug 01, 2001

Installing Routines:

Aug 01, 2001@15:49:33

Installing Data Dictionaries:

Aug 01, 2001@15:49:40

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing OPTION

Aug 01, 2001@15:49:44

Running Post-Install Routine: ^PSSPOST2

Deleting obsolete fields...

Deleting obsolete data...

Updating IV Additive Orderable Items...

Updating IV Solution Orderable Items...

Setting new Orderable Item cross reference......................................

Updating Pharmacy Orderable Items ...............................................

................................................................................

Updating Routine file...

The following Routines were created during this install:

PSSVX6

PSSVX61

PSSVX62

PSSVX63

PSSVX64

PSSVX65

PSSVX66

PSSJXR

PSSJXR1

PSSJXR10

PSSJXR11

PSSJXR12

PSSJXR13

PSSJXR14

PSSJXR15

PSSJXR16

PSSJXR17

PSSJXR18

PSSJXR19

PSSJXR2

PSSJXR20

PSSJXR21

PSSJXR22

PSSJXR23

PSSJXR24

PSSJXR25

PSSJXR26

PSSJXR3

PSSJXR4

PSSJXR5

PSSJXR6

PSSJXR7

PSSJXR8

PSSJXR9

Updating KIDS files...

PSS\*1.0\*38 Installed.

Aug 01, 2001@15:51:54

Install Message sent \# 32156895

Install Started for PSJ\*5.0\*50 :

Aug 01, 2001@15:51:54

Build Distribution Date: Aug 01, 2001

Installing Routines:

Aug 01, 2001@15:51:58

Installing Data Dictionaries:

Aug 01, 2001@15:52

Installing Data:

Aug 01, 2001@15:52

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Located in the PSJ (INPATIENT MEDICATIONS) namespace.

Aug 01, 2001@15:52:02

Running Post-Install Routine: POE^PSJPST50

Updating Routine file...

The following Routines were created during this install:

PSGXR3

PSGXR31

PSGXR310

PSGXR311

PSGXR312

PSGXR32

PSGXR33

PSGXR34

PSGXR35

PSGXR36

PSGXR37

PSGXR38

PSGXR39

Updating KIDS files...

PSJ\*5.0\*50 Installed.

Aug 01, 2001@15:52:04

Install Message sent \# 32156897

Updating Routine file...

Updating KIDS files...

CPRS/PHARMACY ORDERING ENHANCEMENTS 1.0 Installed.

Aug 01, 2001@15:52:04

No link to PACKAGE file

NO Install Message sent

Install Completed

\< This page left blank for two-sided printing. \>

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy V. 7.0

#### There are no Outpatient Pharmacy mail messages delivered to the installer or any other users as a result of the installation of the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build.

#### Computerized Patient Record System V. 1.0

The user who installs the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build should receive a mail message similar to the following when the CPRS conversion is complete. The IRMS representative may find it helpful to forward this information to the Pharmacy Automated Data Processing Application Coordinator (ADPAC). The number of Pharmacy quick orders listed in this example is typical of an active site.

Subj: PATCH OR\*3\*94 CONVERSION COMPLETED \[#44950376\] 322 lines

From: PATCH OR\*3\*94 CONVERSION In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The quick order conversion of patch OR\*3\*94 has completed.

The following quick orders have inactive orderable items that

were unable to be automatically replaced with active ones:

PSJQ59 IPRATROPIU (IPRATROPIUM INHALER)

PSJQ67 NEOMYCIN/P (NEOMYCIN/POLYMYCIN/BACITRACIN)

PSJQ65 MISOPROSTO (MISOPROSTOL PO BID)

PSJQ112 COMPAZINE (COMPAZINE IV)

PSJQOS CISPLATIN 2 (METOCLOPRAMIDE/DIPHENHYDRAMINE INJ )

PSJQOS CHOP 9 (PROCHLORPERAZINE INJ )

PSJQOS VAD 8 (PROCHLORPERAZINE INJ )

PSJQOS ABVD 11 (PROCHLORPERAZINE INJ )

PSJQOS FENTANYL/BUPIVACAINE EPIDURAL 3 (PROCHLORPERAZINE INJ )

PSJQOS MORPHINE/BUPIVACAINE EPIDURAL 3 (PROCHLORPERAZINE INJ )

PSJQOS MORPHINE EPIDURAL 3 (PROCHLORPERAZINE INJ )

PSJIZ BOLUS KCL 10MEQ/50ML PREMIX (BOLUS KCL 10MEQ/50ML)

PSJIZ BOLUS KCL 20MEQ/100ML PREMIX (BOLUS KCL 20MEQ/100ML PREMIX)

PSJIZ HEPARIN DRIP PROTOCOL (HEPARIN PROTOCOL)

ORWDQ 2173593D (KCL IV REPLACEMENT)

PSOZ NIASPAN STARTER KIT (NIASPAN STARTER KIT)

ORWDQ 26A1D3E3 (deb-entex)

ORWDQ CE9532B1 (streptokinase)

ORWDQ C5E36192 (DIMETAPP)

ORWDQ D67DF0D6 (ENTEX)

PSJUZ METRONIDAZOLE IVPB (METRONIDAZOLE IVPB)

ORWDQ 3E7A04E6 (DEXTROSE 5% IN 0.45% NS INJ,SOLN IV 1000 ml )

ORWDQ 78F48C65 (DEXTROSE 5% IN 0.45% NS INJ,SOLN IV 1000 ml, DEXTROSE 5% IN

0.9% NS INJ,SOLN IV 1000 ml )

ORWDQ 30638E98 (HEPARIN GTT)

ORWDQ 89B4D0E4 (KCL 20 BOLUS)

ORWDQ 6FF3D36D (KCL 10 BOLUS)

ORWDQ 0C6FFA4E (KCL40 BOLUS)

ORWDQ 414A9799 (kcl)

ORWDQ 24D00935 (CLYSIS)

ORWDQ E17E4400 (Dimetapp-SR)

ORWDQ 60522D57 (BACITRACIN/NEOMYCIN/POLYMYXIN OINT)

ORWDQ 0A068832 (HEPARIN DRIP)

PSJUZ PROCHLORPERAZINE 5MG IV Q4H PRN AA (PROCHLORPERAZINE 5MG IV Q4H PRN)

PSJUZ PROCHLORPERAZINE 5MG IM Q4H PRN AA (PROCHLORPERAZINE 5MG IM Q4H PRN)

The following Outpatient Pharmacy quick orders have

instructions that were unable to be re-formatted:

ORWDQ BBC7C057 (Furosemide 40mg po hs)

PSOZ LOVASTATIN 10MG (LOVASTATIN 10MG)

PSOZ LOVASTATIN 20MG (LOVASTATIN 20MG)

PSOZ SIMVASTATIN 5MG (SIMVASTATIN 5MG)

PSOZ SIMVASTATIN 10MG (SIMVASTATIN 10MG)

PSOZ SIMVASTATIN 20MG (SIMVASTATIN 20MG)

PSOZ SIMVASTATIN 40MG (SIMVASTATIN 40MG)

PSOZ ATORVASTATIN 10MG (ATORVASTATIN 10MG)

PSOZ ATORVASTATIN 20MG (ATORVASTATIN 20MG)

PSOZ ATORVASTATIN 40MG (ATORVASTATIN 40MG)

PSOZ NIACIN UD (NIACIN 100MG UD)

PSOZ NIACIN 500MG (1) (NIACIN 500MG (1))

PSOZ NIACIN 500MG (2) (NIACIN 500MG (2))

PSOZ GEMFIBROZIL (GEMFIBROZIL)

PSOZ COLESTIPOL (COLESTIPOL)

PSOZ APAP PRN (ACETAMINOPHEN PRN)

PSOZ APAP 500MG (ACETAMINOPHEN 500MG)

PSOZ BISMUTH SUBSALICYLATE (BISMUTH SUBSALICYLATE)

PSOZ METRONIDAZOLE 250MG (METRONIDAZOLE 250MG)

PSOZ TETRACYCLINE 500MG (TETRACYCLINE 500MG)

PSOZ AMOXICILLIN 500MG (AMOXICILLIN 500MG)

PSOZ METRONIDAZOLE 500MG (METRONIDAZOLE 500MG)

PSOZ AMOXICILLIN 500MG BID (AMOXICILLIN 500MG BID)

PSOZ CLARITHROMYCIN BID (CLARITHROMYCIN BID)

PSOZ LANSOPRAZOLE 30MG (LANSORPRAZOLE 30MG)

PSOZ CLARITHROMYCIN TID (CLARITHROMYCIN TID)

PSOZ CIMETIDINE (CIMETIDINE)

PSOZ FAMOTIDINE (FAMOTIDINE)

PSOZ LANSOPRAZOLE 15MG (LANSOPRAZOLE 15MG)

PSOZ LANSOPRAZOLE 30MG GERD (LANSOPRAZOLE 30MG GERD)

PSOZ PROMETHAZINE SUPP (PROMETHAZINE SUPP)

PSOZ SIMVASTATIN 80MG (SIMVASTATIN 80MG)

PSOZ NIASPAN STARTER KIT (NIASPAN STARTER KIT)

PSOZ NIACIN ER 750MG (NIACIN ER 750MG)

PSOZ NIACIN ER 1000MG (NIACIN ER 1000MG)

ORWDQ 69C6DA84 (lidocaine/benadrly/maalox)

ORWDQ D391E262 (cortisporin otic suspension)

ORWDQ 6D422C36 (auralgan otic soln)

ORWDQ 465DF2B8 (Debrox for ear wash)

ORWDQ BC916C7A (anusol hc supp)

ORWDQ F00E6742 (deb-cough)

ORWDQ 46E7733D (deb-bactrium)

ORWDQ 26A1D3E3 (deb-entex)

ORWDQ 3BD6C0C0 (PHENOL)

ORWDQ 66611B79 (fleet prep for be)

ORWDQ E5E29A25 (ALBUTEROL)

ORWDQ A420FDCB (SALINE)

ORWDQ 011FDFCC (CORTISPORIN)

ORWDQ D6D43783 (CHLORPHEN)

ORWDQ 8C6282FA (AFRIN)

ORWDQ CA2BAA66 (ANALG)

ORWDQ 529DFCC8 (COMPAZ SUPP)

ORWDQ AD7F024B (GUAIFENESIN)

ORWDQ C5E36192 (DIMETAPP)

ORWDQ D67DF0D6 (ENTEX)

ORWDQ 9ACA46CF (ANUSOL HC HEMMORHOIDAL SUPPOSITORIES)

ORWDQ E257E16D (GG)

ORWDQ E6C4C4F1 (ACETAMINOPHEN 300MG/CODEINE 30MG TAB 1OR 2 PO Q4-6 HRS Qua

ntity: 40 1 refills )

ORWDQ 5B3D370B (KCL 10 MEQ QD X 1 MONTH)

ORWDQ 86455117 (ALBUTEROL HHN Q4-6 PRN)

ORWDQ B951FD70 (ATROVENT HHN Q6 PRN)

ORWDQ 29D88A28 (PREDNISONE TAPERING DOSE)

ORWDQ D344985B (ATROVENT MDI)

ORWDQ 5381E3B0 (mom 30cc poqhs prn)

OUTPATIENT SLIDING SCALE (Outpatient Insulin/Sliding Scale)

ORWDQ 8E31270E (robitus)

ORWDQ 9D627983 (Insulin S.S.)

ORWDQ E1714A51 (PREDNISONE)

PSOZ TABLET SPLITTER (TABLET SPLITTER)

PSOZ LOVASTATIN 40MG (LOVASTATIN 40MG)

ORWDQ CF20484A (golightley)

ORWDQ D420E3DF (beclamethasone)

ORWDQ 93D1E005 (beclamethasone)

ORWDQ 820A3941 (Atrovent)

ORWDQ 3C43AE58 (beclomethasone oral inhalor)

ORWDQ C4378697 (Medrol Dose Pack)

ORWDQ 550F3CEA (Atarax)

ORWDQ 72798026 (Accu check lancets NIDDM)

ORWDQ 476AB6FA (Accu Check Strips NIDDM)

ORWDQ 510907D1 (Robitussin alc-f/Sf)

ORWDQ 6A44B4A9 (Ventolin Inhalor)

ORWDQ 2C08EB6C (Benadryl)

ORWDQ 12BD8386 (Nitroglycerine .4mg)

ORWDQ 2AA38D11 (Chlor-Trimeton)

ORWDQ 09934A78 (Vasocon)

ORWDQ 94DCB74F (Gentamicin eye drops)

ORWDQ 88D312D0 (Diltiazem)

ORWDQ 484B8B9C (Atrovent)

ORWDQ 8AF76BBD (triamincilone)

ORWDQ 61D4322D (hydrocortisone 1% lotion)

ORWDQ 866F998C (Atrovent)

ORWDQ 36298849 (MORPHINE 10MG/5ML ORAL SOLN, (PER ML) 20MG PO Q2-4H Quanti

ty: 500 ML 0 refills )

ORWDQ 6051FCBA (clotrimazole)

PSOZ NIACIN ER 500MG (NIACIN ER 500MG)

ORWDQ 7793F577 (Robitussim DM)

ORWDQ 9EAD5153 (fleet)

ORWDQ 418091C9 (Antivert)

ORWDQ 92C55D53 (rocephin)

ORWDQ 785F85F5 (guaifenisen DM)

ORWDQ 0B1E51C1 (Oceania)

PSOZ LOVASTATIN 10MG - DC TO PC (LOVASTATIN 10MG-DC TO PC)

PSOZ LOVASTATIN 20MG - DC TO PC (LOVASTATIN 20MG-DC TO PC)

PSOZ LOVASTATIN 40MG - DC TO PC (LOVASTATIN 40MG-DC TO PC)

PSOZ SIMVASTATIN 5MG - DC TO PC (SIMVASTATIN 5MG-DC TO PC)

PSOZ SIMVASTATIN 10MG - DC T0 PC (SIMVASTATIN 10MG-DC TO PC)

PSOZ SIMVASTATIN 20MG - DC TO PC (SIMVASTATIN 20MG-DC TO PC)

PSOZ SIMVASTATIN 40MG - DC TO PC (SIMVASTATIN 40MG-DC TO PC)

PSOZ SIMVASTATIN 80MG - DC TO PC (SIMVASTATIN 80MG-DC TO PC)

PSOZ ATORVASTATIN 10MG - DC TO PC (PSOZ ATORVASTATIN 10MG-DC TO PC)

PSOZ ATORVASTATIN 20MG - DC TO PC (ATORVASTATIN 20MG-DC TO PC)

PSOZ ATORVASTATIN 40MG - DC TO PC (ATORVASTATIN 40MG-DC TO PC)

PSOZ NIACIN 500MG (1) - DC TO PC (NIACIN 500MG (1)-DC TO PC)

PSOZ NIACIN 500MG (2) - DC TO PC (NIACIN 500MG (2)-DC TO PC)

PSOZ NIACIN ER 500MG - DC TO PC (NIACIN ER 500MG-DC TO PC)

PSOZ NIACIN ER 750MG - DC TO PC (NIACIN ER 750MG-DC TO PC)

PSOZ NIACIN ER 1000MG - DC TO PC (NIACIN ER 1000MG-DC TO PC)

PSOZ GEMFIBROZIL - DC TO PC (GEMFIBROZIL-DC TO PC)

ORWDQ FE4CC0ED (Pyridoxine)

ORWDQ AE905647 (Fleet)

ORWDQ 13B85A8C (Ocean)

ORWDQ 72C28530 (Capsaicin 0.025%)

PSOZ GOLYTELY (GOLYTELY FOR FLEX-SIG)

PSOZ FLEET PREP KIT (FLEET PREP KIT FOR BARIUM ENEMA)

PSOZ SIMETHICONE 80MG (SIMETHICONE 80MG FOR SONOGRAM)

ORWDQ 6EA379D6 (Multivitamins)

ORWDQ BA484545 (vitamin e)

ORWDQ CFE5A57A (ocean mist)

ORWDQ 9BD667D1 (kenalog 0.25% lotion)

ORWDQ 873E6438 (Ketoconazole)

ORWDQ E830205C (nasalcrom)

ORWDQ B0A90520 (LO DOSE SYRINGE)

ORWDQ D6C4BC69 (GOLYTELY)

ORWDQ 28BCCAD6 (AUGMENTIN)

ORWDQ 1470CEDE (GUAIFENESIN 100MG/5ML ALC-F/SF SY (ML))

ORWDQ 8F2EFB98 (TYLENOL ES)

ORWDQ 9D17C439 (LODINE XL )

ORWDQ D6AE4C8F (TMCL crm)

ORWDQ 4358E69F (METFORMIN)

ORWDQ DB77E69B (ATENOLOL - LOW DOSE)

ORWDQ 3B532F18 (TMCL)

ORWDQ 6BD8A5A5 (FLEX PREP KIT)

ORWDQ A9FBA090 (LEVOTHYROXINE 0.025MG TAB)

ORWDQ 1BC8BC3A (MYCELEX 1% crm)

ORWDQ EACAABC6 (guaifenesin)

ORWDQ AD876D33 (Z PACK)

ORWDQ 1DE4338B (nasalcrom)

ORWDQ EA52B702 (ANALGESIC BALM (PER GM) )

ORWDQ 4ED04CCC (Fleetprep)

ORWDQ 0A5C1C6E (TMCL/VANICREAM)

ORWDQ 83924D86 (VIT B)

ORWDQ E17E4400 (Dimetapp-SR)

ORWDQ 4ED25B7B (TMCL1%)

ORWDQ 4BDD9AD1 (NYSTATIN susp)

ORWDQ 413B4F51 (PEG ELECTROLYTE SOLN, 4000ML)

ORWDQ 5F217B2F (CLOTRIMAZOLE 1% CR)

ORWDQ C16C8073 (PEG ELECTROLYTE SOLN, 4000ML)

ORWDQ 32949FC4 (ZINC OXIDE BANDAGE, 4 INCH)

ORWDQ DD8ACE6E (GOLYTELY prep.)

ORWDQ 938FD6BB (GOLYTELY)

ORWDQ EB5D3CB5 (PSYLLIUM POWDER SUGARFREE)

ORWDQ CC70D17C (TUSK)

ORWDQ 165F7C01 (ZINC OXIDE 20% OINT (PER GM) )

ORWDQ 60522D57 (BACITRACIN/NEOMYCIN/POLYMYXIN OINT)

ORWDQ 4B346503 (GUAIFENESIN 100MG/5ML ALC-)

ORWDQ FADAF6F2 (salsalate)

ORWDQ DFA998B6 (AEROCHAMBER)

ORWDQ F33B968F (UNSCENTED MOISTURIZING CR)

ORWDQ 2EB325D9 (PENCICLOVIR 1% CREAM, )

ORWDQ 38A85384 (SSKI)

ORWDQ F58DE01D (PREDNISONE 20MG TAB 1 TABLET(S) PO QD for 4 days, 1/2 TABL

ET(S) PO QD for 4 days, 1/4 TABLET(S) PO QD for 4 days Quantity: 0 refills )

ORWDQ 9AE6E041 (chlorpheneramine)

ORWDQ F9DFB96D (SS INSULIN OP)

ORWDQ D6A76414 (combivent)

ORWDQ 916A3DED (Synthroid)

ORWDQ 776A7AF8 (RANITIDINE 150MG TAB )

ORWDQ B8A4DB32 (VANCENASE)

ORWDQ F48158CD (GOLYTELY 1 gallon)

ORWDQ 742D3532 (ACCUCHEK LANCETS)

ORWDQ 016F18EB (KAOPECTATE)

PSOZ CURE DISCHARGE (Cure Discharge-Restricted to Cardiology)

PSOZ CURE OUTPATIENT \#2 (Cure Outpatient \#2-Restrected to Cardiology)

PSOZ CURE OUTPATIENT \#3 (Cure Outpatient \#3-Restricted to Cardiology)

PSOZ CURE OUTPATIENT \#4 (Cure Outpatient \#4-Restricted to Cardiology)

PSOZ CURE OUTPATIENT \#5 (Cure Outpatient \#5-Restricted to Cardiology)

ORWDQ 9E0749AC (maxzide)

ORWDQ 7157D40E (PREDNISONE TITRATION)

ORWDQ E5D6EB4F (PREDNISONE TAPER)

ORWDQ 0EF6D792 (TMCL 0.1% crm)

ORWDQ E3219065 (RANITIDINE 150MG TAB )

ORWDQ 3549EE28 (urinary leg bag)

ORWDQ 13BDF900 (condom cath)

ORWDQ D2E0FBDE (accuchecks)

ORWDQ 5E68CC17 (ACCUCHEK COMFORT CURVE GLUCOSE STRIP)

ORWDQ D72A1300 (tapering dose prednisone)

ORWDQ A8C3E2D6 (tylenol \#3)

ORWDQ 0F824EF4 (golytely)

ORWDQ 76AED14E (MILK OF MAGNESIA,)

ORWDQ 40781DFB (Lodine 600)

ORWDQ 67918E2B (CROMOLYN SODIUM NASAL SOLN,)

ORWDQ E2AD7635 (GUAIFENESIN 100MG/5ML)

ORWDQ 8FBBD82F (Lodine XL (etodolac))

ORWDQ DE9CAEDF (lodine)

GOLYTELY ORDER (GOLYTELY ORDER)

ORWDQ 61C05CE5 (PEG)

ORWDQ 4A1C30C6 (NYSTATIN 100,000U/ML ORAL SUSP,)

ORWDQ 46C661A8 (quinine)

ORWDQ 5CC5F1AD (ACYCLOVIR 200MG CAP )

ORWDQ EB0C2788 (ACYCLOVIR 5% OINT, (PER GM) )

ORWDQ 01EDA60C (POLYMYXIN/TRIMETHOPRIM OS (PER ML) 4 DROP(S) OU QID Quanti

ty: 1 0 refills )

ORWDQ 55610324 (PEG ELECTROLYTE SOLN, 4000ML )

ORWDQ FA8CEF42 (REBETRON 1200)

ORWDQ C32AB6E3 (REBETRON 1000MG)

ORWDQ E7BA9427 (REBETRON 1200MG)

ORWDQ 3DE70642 (anusol hc)

ORWDQ 09EBE052 (lancets)

ORWDQ 5D90485D (BISACODYL/PHOSPHO SODA PREP KIT)

ORWDQ ADC399E9 (PEG ELECTROLYTE SOLN, 4000ML)

ORWDQ 4B0C04D7 (immodium)

ORWDQ E1A21E19 (BISACODYL/PHOSPHO SODA PREP KIT )

ORWDQ 29D82A10 (MILK OF MAGNESIA,)

ORWDQ 5D009A2D (cromolyn nasal)

ORWDQ 6807B3D8 (CROMOLYN SODIUM NASAL SOLN,)

ORWDQ 3DE18B89 (PREDNISONE COMPLEX DOSE)

PSOZ GOLYTELY 1 GAL (GOLYTELY FOR FLEX-SIG)

ORWDQ CA2AC6CF (GUAIFENESIN 100MG/5ML ALC-F/SF SY (ML))

ORWDQ F7762572 (LASIX1V)

ORWDQ B780DC6B (ibuprofen)

ORWDQ 850258A4 (nasalcrom)

ORWDQ 4C2568BC (diltiazem 300mg)

ORWDQ 8128348E (nasel chrom)

PSOZ ATORVASTATIN 80MG (ATORVASTATIN 80MG)

PSOZ ATORVASTATIN 80MG - DC TO PC (ATORVASTATIN 80MG-DC TO PC)

ORWDQ 6B3C6F15 (ACETIC ACID 2/HC 1% OTIC SOLN)

ORWDQ 980D8EA9 (hydrocortisone)

ORWDQ 99BBB564 (docusate)

ORWDQ EFA1D5E5 (nasel chrom)

ORWDQ 1B8B6FE7 (loition)

ORWDQ 622EA25D (ASA)

ORWDQ 3670BFD7 (metamucil)

ORWDQ DBD64369 (zyprexa/ olanzapine)

ORWDQ 106FC487 (prednisone tapering dose)

ORWDQ C05F7CDC (ACETIC ACID 2/HC 1% OTIC SOLN )

ORWDQ FC1EDF81 (ACETIC ACID 2/HC 1% OTIC SOLN )

ORWDQ 877BF6F4 (aerobid)

ORWDQ 430F1DF6 (tylenol)

ORWDQ CA178F38 (Cortisporin otic)

ORWDQ 01B784EF (Cortisporin otic)

ORWDQ 1D5D12FB (Sliding scale)

ORWDQ 9638BF20 (RANITIDINE 150MG TAB 1 PO QHS)

BACITRACIN/POLYMIXIN OINT,TOP (BACITRACIN/POLYMIXIN OINT,TOP)

UREA 10% LOTION (UREA 10% LOTION)

FLUOCINOLONE 0.01% SOLN, TOP (FLUOCINOLONE 0.01% SOLN,TOP)

UREA 20% CREAM, TOP (UREA 20% CREAM, TOP)

TRIAMCINOLONE 0.1% CREAM, TOP (TRIAMCINOLONE 0.1% CREAM, TOP)

ORWDQ 1C231DB0 (etodolac)

ORWDQ F5A44C18 (anusol )

ORWDQ 90468FF9 (Lodine XL BID)

ORWDQ 616BE3FD (sodium chloride aerosol)

ORWDQ 13AB6210 (albuterol aerosol)

ORWDQ 2486FA44 (ipratropium aerosol)

ORWDQ AC06E1D4 (LANCETS ACCUCHEK SOFTCLIX )

ORWDQ 3FCCAA3B (Regular Insulin/Sliding Scale)

ORWDQ B27FC003 (MEDROL DOSE PACK)

ORWDQ A7B99429 (ROBITUSSIN)

ORWDQ F7856811 (clotrimazole)

ORWDQ 3371B1EC (CROMOLYN SODIUM NASAL SOLN)

ORWDQ 5950316E (PEG ELECTROLYTE SOLN,)

ORWDQ 576DCDF4 (zovirax)

ORWDQ 6E2257B6 (CROMOLYN NASAL)

ORWDQ 768CA7AE (tocopherol)

ORWDQ 61660CF3 (LODINE)

ORWDQ DDCBF9C9 (ETODOLAC)

ORWDQ 77C6FEB6 (xylocaine oral combination)

ORWDQ 0401D660 (psyllium powder bid)

ORWDQ 8EF09F5D (permethrin shampoo)

ORWDQ A848D615 (lindaine 1%)

ORWDQ 71D57CEA (fleet prep kit (for BE))

ORWDQ 4319F7DB (MICONAZOLE 2% TOP CR, (PER GM))

ORWDQ 0258A7E9 (REBETRON 1000)

ORWDQ 62646437 (REBETRON 1200)

#### ORWDQ 0E7FDC87 (ROMOLYN SODIUM NASAL SOLN,)

#### #### #### In addition to the mail message, after the installation of the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build, CPRS has a post-init routine that loops though all of the Pharmacy quick orders stored in CPRS to fix the following two problems.

1.  CPRS looks for any Pharmacy quick orders that use Orderable Items that PDM has inactivated and makes a call to see if PDM has a new Orderable Item to replace the old Orderable Item. If a new Orderable Item is returned, CPRS updates the Pharmacy quick order automatically. If a new Orderable Item is not returned, a bulletin is generated at the end of the post-init that contains a list of all Pharmacy quick orders that still have inactive Orderable Items, and the bulletin is sent to the user who ran the install.
2.  Because this patch changes the way that dose instructions are prompted for in the Outpatient Pharmacy ordering dialog, the same routine will also attempt to convert the dose saved with Outpatient Pharmacy quick orders into the new format. Any Outpatient Pharmacy quick order that cannot be automatically converted will be listed in the bulletin generated at the end of the post-init.

#### #### Pharmacy Data Management V. 1.0

#### The person who installs the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build should receive the following message when the PDM post-installation is complete.The message captures the start time and end time of the installation.

Subj: Pharmacy Ordering Enhancements Install \[#83473\] 01 Jun 01 12:20

3 lines

From: PHARMACY DATA MANAGEMENT PACKAGE In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

The Pharmacy Ordering Enhancements installation is complete.

It started on JUN 01, 2000@12:14:07.

It ended on JUN 01, 2001@12:20:45.

#### Enter message action (in IN basket): Ignore//

#### The Pharmacy Data Management post-install routine, PSSPOST2, has a line tag that can be called from programmer mode in the event that this routine generates an error. The line tag is RESTART^PSSPOST2. By calling that line tag, the entire post-install routine will run again. The code has been written so it can run multiple times, but the routine will only run on the first installation of the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build.

#### #### #### Inpatient Medications V. 5.0

#### The person who installs the CPRS/Pharmacy Ordering Enhancements 1.0 Master Build should receive the following message when the conversion for Inpatient Medications is complete. The IRMS representative may find it helpful to forward this information to the Pharmacy ADPAC.

Subj: Inpatient Meds IV conversion \[#44950402\] 29 Apr 01 22:37 2 lines

From: INPATIENT MEDS POE In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

The conversion was first started: Apr 29, 2001@21:52:31

It ran to completion: Apr 29, 2001@22:37:23

Enter message action (in IN basket): Delete//

#### #### ####