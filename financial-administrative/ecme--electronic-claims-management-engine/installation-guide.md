---
title: BPS Version 1 (Dormant Release) Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: (Dormant Release)
app_code: ECME
app_name: Electronic Claims Management Engine
section: FIN
app_status: active
pkg_ns: ECME
patch_ver: 1
patch_id: ECME*1
group_key: "ECME:ECME:1"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this Installation Guide is to provide an explanation of the installation process for the BPS\*1.0 Master Build. This Master Build is the release mechanism of the HIPAA NCPDP Connection for EDI Pharmacy project, which includes the new Electronic Claims Management Engine (ECME) V. 1.0 p
audience: 
keywords: 
  - pharmacy
  - table
  - contents
  - installation
  - install
  - ncpdp
  - build
  - registration
  - located
  - namespace
page_count: 0
word_count: 5817
section_count: 7
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/bps_1_0_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/bps_1_0_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=141"
---

> ![](bps-version-1-dormant-release-installation-guide/001.png)

hipaa ncpdp connection for EDI Pharmacy (Dormant Release)

######### 

######### INSTALLATION GUIDE

October 2004

BPS\*1.0

PSS\*1\*81

IB\*2\*223

IB\*2\*251

PRCA\*4.5\*202

V*IST*A Health Systems Design & Development

# ######### Table of Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [######### Table of Contents](#table-of-contents)
- [Purpose](#purpose)
- [Scope](#scope)
- [Pre-Installation](#pre-installation)
- [Minimum Required Packages](#minimum-required-packages)
- [Required Patches](#required-patches)
- [New Globals](#new-globals)
- [Installation](#installation)
- [Installation Steps](#installation-steps)
- [Example of Installation](#example-of-installation)
- [Post-Installation](#post-installation)
  - [Setup the BPS and IB Security Keys and Assign New Menu Options](#setup-the-bps-and-ib-security-keys-and-assign-new-menu-options)
  - [Configure the VISTA HL7 Module](#configure-the-vista-hl7-module)
    - [<u>Configure HL7 Logical Links</u>](#uconfigure-hl7-logical-linksu)
    - [### <u>Configuring the EPHARM OUT Logical Link</u>](#uconfiguring-the-epharm-out-logical-linku)
    - [<u>Configuring the EPHARM IN Link</u>](#uconfiguring-the-epharm-in-linku)
  - [Validate the HL7 System Monitor is Active and Working for the Two ePharmacy Links](#validate-the-hl7-system-monitor-is-active-and-working-for-the-two-epharmacy-links)
    - [The site’s IRMS personnel perform this step. The following activities will verify that the HL7 links have been successfully configured.](#the-sites-irms-personnel-perform-this-step-the-following-activities-will-verify-that-the-hl7-links-have-been-successfully-configured)
    - [<u>Start the New HL7 Logical Links</u>](#ustart-the-new-hl7-logical-linksu)
    - [<u>Validating the HL7 Logical Links:</u>](#uvalidating-the-hl7-logical-linksu)
    - [### > Example: Starting HL7 Logical Link EPHARM OUT](#example-starting-hl7-logical-link-epharm-out)
    - [<u>Re-starting the HL7 Logical Links if Re-Installing the Master Build :</u>](#ure-starting-the-hl7-logical-links-if-re-installing-the-master-build-u)
  - [Enter Site and Pharmacy Registration Information](#enter-site-and-pharmacy-registration-information)
    - [### <u>Required and Optional Fields</u>](#urequired-and-optional-fieldsu)
    - [<u>Detailed Registration Steps</u>](#udetailed-registration-stepsu)
  - [Ensure the Registration Request was sent to Austin](#ensure-the-registration-request-was-sent-to-austin)
  - [Schedule the ePharmacy Nightly Process](#schedule-the-epharmacy-nightly-process)
*(This page included for two-sided copying.)*

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide an explanation of the installation process for the BPS\*1.0 Master Build. This Master Build is the release mechanism of the HIPAA NCPDP Connection for EDI Pharmacy project, which includes the new Electronic Claims Management Engine (ECME) V. 1.0 package and a patch from the Pharmacy Data Management V. 1.0 application. The intended audience for this document is the Information Resources Management Service (IRMS) staff and Pharmacy staff responsible for installing and maintaining the Pharmacy files.

This project consists of two phases, a dormant phase and an active phase. This BPS\*1.0 Master Build is the dormant phase, which releases the ECME V. 1.0 package as dormant. Even though this package is dormant, Integrated Billing (IB) V. 2.0 is enhanced in this build, so that the user will be able to link pharmacy groups with insurance group plans in this phase. Also, each site must proceed with registering their pharmacy with the Financial Services Center (FSC). This Master Build includes the installation of the new ECME V. 1.0 package and Patches PSS\*1\*81, IB\*2\*223, IB\*2\*251, and PRCA\*4.5\*202.

These modifications involve changes to software functionality within the Pharmacy Data Management V. 1.0 pharmacy application. In addition, modifications to the Veterans Health Information Systems and Technology Architecture (V*IST*A) IB V. 2.0, Accounts Receivable (AR) V. 4.5 and Vitria BusinessWare software are required.

Resource requirements of this project include the assignment of an Outpatient Pharmacy Electronic Claims Coordinator (OPECC), whose primary responsibility is the coordination and adjudication of Department of Veterans Affairs (VA) Outpatient Pharmacy electronic claims. These responsibilities encompass processing rejected claims by reviewing and triaging claims based on the reject code, resubmitting the claim when resolved, facilitating external local and regional trading partner relationships as appropriate, coordinating with the national ePayments enrollment team, and producing management reports for trending and analysis. More information on the OPECC position may be obtained in a Directive memorandum to be distributed to the sites by the Central Business Office (CBO).

The active phase, which will be released later, allows the ECME V. 1.0 package to produce electronic claims. These changes will allow the V*IST*A software applications to electronically transmit outpatient pharmacy prescription claims to payers. It will also receive claim responses (which include drug utilization responses and warnings) on a real-time basis and in accordance with Healthcare Insurance Portability and Accountability Act (HIPAA) Electronic Data Interchange (EDI) transactions and National Council for Prescription Drug Programs (NCPDP) mandated format standards, specifically NCPDP Telecommunication Standard v. 5.1.

![](bps-version-1-dormant-release-installation-guide/002.png)Note: The electronic transmission of outpatient pharmacy prescription claims will not be available until the active phase of this project is released.

*(This page included for two-sided copying.)*

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of the HIPAA NCPDP Connection for EDI Pharmacy project is to introduce the ability to collect billing and clinical information within the prescription fill workflow process. This will be accomplished in two phases. The first phase (dormant) will install a dormant ECME V. 1.0 package, while allowing the users to link the pharmacy group with the insurance group plans within the IB V. 2.0 package. The user will also be able to proceed with registering their pharmacy with the FSC.

During this phase, although the system will be in a dormant state, these two significant configuration activities are required:

1.  Registration – The process of registering the Outpatient Pharmacy at the Medical Center with the remote Vitria server located at the FSC in Austin, TX.
2.  Insurance Matching – The process of linking Pharmacy groups with Insurance Plans. This process is described in a separate document titled *e-Pharmacy Claims Insurance Process*. (See the BPS\*1.0 Master Build Description for the document location.)

The second phase (active) will install an active ECME V. 1.0 real-time system, which will send claim data in a HIPAA compliant (NCPDP V. 5.1) format to a payer on a real-time basis and receive and process the claim responses in the appropriate manner. The claim transactions are sent to IB V. 2.0, the Drug Utilization responses and warnings are sent to the Outpatient Pharmacy V. 7.0 package and rejections are sent to the appropriate personnel for review.

The existing V*IST*A applications, that include Pharmacy Data Management V. 1.0, IB V. 2.0, and AR V. 4.5, are modified or enhanced as necessary to create electronic claims using billing and applicable clinical information. The information to be collected will consist of data currently available within the Outpatient Pharmacy V. 7.0, Patient Information Management System (PIMS) V. 5.3, and IB V. 2.0 applications, and data passed to the Outpatient Pharmacy V. 7.0 application from external applications.

Infrastructure components at the FSC, process incoming ePharmacy claim data using Vitria, the National Health Care Insurance Database (NHCID) for transaction logging and the HIPAA EDI website to register Veterans Health Administration (VHA) pharmacies. These components also communicate with WebMD and third party payers for claims adjudication and return this information to V*IST*A.

*(This page included for two-sided copying.)*

# Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integrated Billing V. 2.0

The patch IB\*2.0\*223 has an environment check routine. It checks the RATE TYPE file (#399.3). Your site may have the Rate Types defined but the names may have been changed. The following Rate Types must be present <u>exactly</u> as follows:

TRICARE

TRICARE REIMB. INS.

CHAMPVA

CHAMPVA REIMB. INS.

If your site does not have the exact spelling as shown above, the BPS\*1.0 Master Build will fail.

You may correct the Rate Type names yourself using FileMan or you can contact Enterprise V*IST*A Support (EVS) for assistance by contacting the help desk (888-596-4357) to log a National On-line Information System (NOIS) for you or submitting a NOIS yourself under the package synonym BPS or ECME.

*(This page included for two-sided copying.)*

# Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BPS\*1.0 Master Build can only run with a standard MUMPS operating system. It requires the following VA software packages:

|                                              |                            |
|----------------------------------------------|----------------------------|
| Package                                  | Minimum Version Needed |
|                                              |                            |
| Pharmacy Data Management                     | 1.0                        |
| VA FileMan                                   | 22.0                       |
| Kernel                                       | 8.0                        |
| Patient Information Management System (PIMS) | 5.3                        |
| National Drug File (NDF)                     | 4.0                        |
| Integrated Billing (IB)                      | 2.0                        |
| Accounts Receivable (AR)                     | 4.5                        |
| Pharmacy Data Management                     | 1.0                        |
| Order Entry/Results Reporting (OE/RR)        | 3.0                        |
| Outpatient Pharmacy                          | 7.0                        |
| Consolidated Mail Outpatient Pharmacy (CMOP) | 2.0                        |
| Health Level Seven (HL7)                     | 1.6                        |
| MailMan                                      | 8.0                        |
| Visit Tracking                               | 2.0                        |

The above software is not included in this Master Build and must be installed for this build to be completely functional.

*(This page included for two-sided copying.)*

# Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing the BPS\*1.0 Master Build, the domain EPHARMACY.VITRIA-EDI.AAC.VA.GOV <u>must</u> be added to the DOMAIN file (#4.2) as per instructions provided in Patch XM\*DBA\*160. All other listed patches must have been previously installed into each of the applications listed below prior to installing this build.

#### Electronic Claims Management Engine V. 1.0

This is a new software package release, included in the build, and therefore does not have any required patches.

Pharmacy Data Management V. 1.0  
 PSS\*1\*61

#### Integrated Billing V. 2.0

(The patches in each column are pre-requisites for the specific patch listed at the column heading. Patches IB\*2.0\*251 and IB\*2.0\*223 are included in this build.)

<u>Patch IB\*2.0\*251</u> <u>Patch IB\*2.0\*223</u>

XM\*DBA\*160 (Domain must be added before the IB\*2\*13

Installation of IB\*2\*251, which is included in the IB\*2\*115

BPS\*1.0 Master Build.) IB\*2\*137

HL\*1.6\*108 IB\*2\*183

IB\*2\*211 IB\*2\*202

IB\*2\*229 IB\*2\*245

IB\*2\*246 IB\*2\*247

IB\*2\*252

#### Accounts Receivable V. 4.5

<u>Patch PRCA\*4.5\*202</u>

IB\*2.0\*223 (Included in this BPS\*1.0 Master Build)

PRCA\*4.5\*158

PRCA\*4.5\*196

PRCA\*4.5\*208

*(This page included for two-sided copying.)*

# New Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assist in planning for system growth and placement of new globals in your appropriate volume(s), the following information is provided. No global growth is expected with the dormant release and installation. Estimates for the global growth will be available in the active release documentation. This version will require approximately 28 MB of disc space, initially.

Electronic Claims Management Engine V. 1.0

^BPS - MOSTLY STATIC

^BPSC - VERY DYNAMIC - WILL CONTINUALLY GROW

^BPSCOMB - STATIC – CURRENTLY NOT USED BY THE VA

^BPSECP - DYNAMIC – DOES NOT GROW

^BPSECX - DYAMIC – DOES NOT GROW A LOT

^BPSEI - STATIC – CURRENTLY NOT USED BY THE VA

^BPSF - STATIC – DOES NOT GROW

^BPSR - DYNAMIC - GROWS CONTINUALLY

^BPST - DYNAMIC - GROWS

^BPSTL - DYNAMIC - GROWS

#### Integrated Billing V. 2.0

^IBCNR - MOSTLY STATIC

*(This page included for two-sided copying.)*

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HIPAA NCPDP Connection for EDI Pharmacy project is comprised of the new ECME V. 1.0 package and four patches. The new package and all four patches will install when the BPS\*1.0 Master Build is loaded. BPS\*1.0 will load first, followed by PSS\*1\*81, IB\*2\*223, IB\*2\*251, and PRCA\*4.5\*202. Please read the following installation instructions carefully before beginning the installation. An overview of any functionality changes resulting from the installation of the BPS\*1.0 Master Build is provided in the HIPAA NCPDP Connection for EDI Pharmacy (Dormant Release) Release Notes in the V*ist*A Documentation Library at <http://www.va.gov/vdl/default.asp>

> ![](bps-version-1-dormant-release-installation-guide/003.png)Before installing the BPS\*1.0 Master Build, the domain EPHARMACY.VITRIA-EDI.AAC.VA.GOV <u>must</u> be added to the DOMAIN file (#4.2) as per instructions provided in Patch XM\*DBA\*160. This domain is used to register pharmacies with Vitria and receive payer sheets via HL7 for the HIPAA project. The domain will be used for Kernel DNS lookups on the HL7.EPHARMACY.VITRIA-EDI.AAC.VA.GOV domain name. (Since MailMan will not use the domain, no transmission scripts are necessary and the domain is marked ‘closed’.) This domain is required to be in place before the installation of IB\*2\*251, which is included in the BPS\*1.0 Master Build.

Before installing the BPS\*1.0 Master Build, use the TaskMan *List Tasks* \[XUTM INQ\] option on the TaskMan *Management* \[XUTM MGR\] menu to list currently running tasks. It is recommended that no Pharmacy Data Management, IB, or AR tasks be running at the time of this installation. The suggested time to install is during non-peak hours.

This build will be available only as a host file. The name of the file is BPS_1_0.KID. This file needs to be retrieved in ASCII format.

Sites will retrieve V*IST*A software from the following File Transfer Program (FTP) addresses. The preferred method is to FTP the files from REDACTED. This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows.

<u>OI Field Office</u> <u>FTP Address</u> <u>Directory</u>

Albany REDACTED \[anonymous.software\]

Hines REDACTED \[anonymous.software\]

Salt Lake City REDACTED \[anonymous.software\]

Installation should take no longer than 5 minutes.

*(This page included for two-sided copying.)*

# Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Add the new domain, EPHARMACY.VITRIA-EDI.AAC.VA.GOV, to the DOMAIN file (#4.2) following the installation instructions included in the patch description for the XM\*DBA\*160 patch. This domain must be in place before the installation of the IB\*2\*251 patch that is included in the BPS\*1.0 Master Build.

![](bps-version-1-dormant-release-installation-guide/004.png)Note: After you have added the new domain, if you encounter the following message, “Couldn't resolve Domain EPHARMACY.VITRIA-EDI.AAC.VA.GOV for Logical Link EPHARM OUT”, it should not impact the registration process or your sites ability to match pharmacy group plans with insurance companies. However, if you are unable to successfully register your pharmacy due to a domain issue, please provide this information, along with any other relevant error messages within your NOIS entry for follow up.

2\. Download the KIDS file BPS_1_0.KID via FTP. This file needs to be retrieved in ASCII format.

3\. Review mapped sets for the PSS\*, IB\*, and PRCA\*namespaces. If the routines are mapped, they should be removed from the mapped set at this time.

4\. For DSM sites, please be aware that this package introduces 10 new globals in the BPS\* namespace. You should ensure that your Translation Table has an entry for B\* or BPS\* globals, and that the target Volume Set configuration has adequate space to accommodate the new globals, which should remain static until the active release later this year. We also recommend you check the MAXIMUM GLOBALS setting under VOLMAN (for this volume) to insure you do not reach the upper limit of this parameter, with this installation. Cache sites should be OK.

5\. From the *Kernel Installation & Distribution System* menu, select the *Installation* menu.

6\. From this menu, select the *Load a Distribution* option*.* When prompted for a host file, enter the disk and directory name designated during the FTP process, followed by BPS_1_0.KID. (Determine the location where you stored the build in Step \#2 above, to decide the correct disk and directory names.) In the install example, which follows these steps, the complete file name is USER\$:\[ANONYMOUS\]BPS_1_0.KID.

7\. When prompted, “Want to Continue with Load: YES//” respond YES.

8\. At the “Want to RUN the Environment Check Routine? YES//”, respond YES.

9\. When the *Load a Distribution* option has completed, you are prompted to “Select Installation Option:” again. This time respond 6 for the Install Package(s) option or the installer may elect to use the following options:

(When prompted for INSTALL NAME, enter BPS 1.0)

a\. *Backup a Transport Global* - This option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.

b\. *Compare Transport Global to Current System -* This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

c\. *Verify Checksums in Transport Global* - This option will ensure the integrity of the routines that are in the transport global.

10\. After you have responded 6 for the Install package(s) option, at the “Select INSTALL NAME:” prompt, respond with BPS 1.0.

11\. Any time you are prompted, "Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//" respond NO.

12\. Any time you are prompted, "Want KIDS to INHIBIT LOGONs during the install? YES//" respond NO.

13\. Any time you are prompted, "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//" respond NO.

14\. When prompted, "Device:" respond with the correct device and <u>DO NOT</u> queue this to P-Message.

15\. If routines were unmapped as part of step 3, they should be returned to the mapped set once the installation has run to completion.

# Example of Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Kernel Installation & Distribution System Option: INSTallation

Select Installation Option: 1 LOAD a Distribution

Enter a Host File: USER\$:\[ANONYMOUS\]BPS_1_0.KID

KIDS Distribution saved on Sep 08, 2004@12:58:23

Comment: BPS DORMANT RELEASE

This Distribution contains Transport Globals for the following Package(s):

BPS 1.0

PSS\*1.0\*81

IB\*2.0\*223

IB\*2.0\*251

PRCA\*4.5\*202

Distribution OK!

Want to Continue with Load? YES// \<Enter\> or YES

Loading Distribution...

BPS 1.0

PSS\*1.0\*81

Build IB\*2.0\*223 has an Enviromental Check Routine

Want to RUN the Environment Check Routine? YES// \<Enter\> or YES

IB\*2.0\*223

Will first run the Environment Check Routine, IB20P223

IB\*2.0\*251

PRCA\*4.5\*202

Use INSTALL NAME: BPS 1.0 to install this Distribution.

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: BPS 1.0 Loaded from Distribution 9/10/04@15:12:09

=\> BPS DORMANT RELEASE ;Created on Sep 08, 2004@12:58:23

This Distribution was loaded on Sep 10, 2004@15:12:09 with header of

BPS DORMANT RELEASE ;Created on Sep 08, 2004@12:58:23

It consisted of the following Install(s):

BPS 1.0 PSS\*1.0\*81 IB\*2.0\*223 IB\*2.0\*251 PRCA\*4.5\*202

Checking Install for Package BPS 1.0

Install Questions for BPS 1.0

Incoming Files:

9002313.02BPS CLAIMS

9002313.03BPS RESPONSES

9002313.1 BPS COMBINED INSURANCE

9002313.31BPS CERTIFICATION

9002313.4 BPS INSURER

9002313.51BPS DATA INPUT

9002313.511BPS NCPDP OVERRIDE

9002313.515BPS INPUT USER PREF

9002313.516BPS ORIGIN OF INPUT

9002313.53BPS PRICING TABLES

9002313.56BPS PHARMACIES

9002313.57BPS LOG OF TRANSACTIONS

9002313.58BPS STATISTICS

9002313.59BPS TRANSACTION

9002313.61BPS REPORT MASTER

9002313.81BPS TRANSLATE 9999999.36

9002313.82103BPS NCPDP FIELD 103 (including data)

9002313.82305BPS NCPDP FIELD 305 (including data)

9002313.82306BPS NCPDP FIELD 306 (including data)

9002313.82307BPS NCPDP FIELD 307 (including data)

9002313.82308BPS NCPDP FIELD 308 (including data)

9002313.82309BPS NCPDP FIELD 309 (including data)

9002313.82406BPS NCPDP FIELD 406 (including data)

9002313.82408BPS NCPDP FIELD 408 (including data)

9002313.82416BPS NCPDP FIELD 416 (including data)

9002313.82419BPS NCPDP FIELD 419 (including data)

9002313.8242BPS NCPDP FIELD 420 (including data)

9002313.82423BPS NCPDP FIELD 423 (including data)

9002313.82425BPS NCPDP FIELD 425 (including data)

9002313.82429BPS NCPDP FIELD 429 (including data)

9002313.82432BPS NCPDP FIELD 432 (including data)

9002313.82436BPS NCPDP FIELD 436 (including data)

9002313.82439BPS NCPDP FIELD 439 (including data)

9002313.8244BPS NCPDP FIELD 440 (including data)

9002313.82441BPS NCPDP FIELD 441 (including data)

9002313.82501BPS NCPDP FIELD 501 (including data)

9002313.82522BPS NCPDP FIELD 522 (including data)

9002313.82528BPS NCPDP FIELD 528 (including data)

9002313.82529BPS NCPDP FIELD 529 (including data)

9002313.82532BPS NCPDP FIELD 532 (including data)

9002313.82533BPS NCPDP FIELD 533 (including data)

9002313.82535BPS NCPDP FIELD 535 (including data)

9002313.83BPS RESULT CATEGORY

9002313.89BPS ERROR CODES

9002313.91BPS NCPDP FIELD DEFS (including data)

9002313.92BPS NCPDP FORMATS (including data)

9002313.93BPS NCPDP REJECT CODES

9002313.94BPS INSURANCE RULES

9002313.99BPS SETUP (including data)

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Checking Install for Package PSS\*1.0\*81

Install Questions for PSS\*1.0\*81

Checking Install for Package IB\*2.0\*223

Will first run the Environment Check Routine, IB20P223

Install Questions for IB\*2.0\*223

Incoming Files:

361.1 EXPLANATION OF BENEFITS (Partial Definition)

> **NOTE:** You already have the 'EXPLANATION OF BENEFITS' File.

363 RATE SCHEDULE (Partial Definition)

> **NOTE:** You already have the 'RATE SCHEDULE' File.

399 BILL/CLAIMS (Partial Definition)

> **NOTE:** You already have the 'BILL/CLAIMS' File.

Checking Install for Package IB\*2.0\*251

Install Questions for IB\*2.0\*251

Incoming Files:

350.9 IB SITE PARAMETERS (Partial Definition)

> **NOTE:** You already have the 'IB SITE PARAMETERS' File.

355.3 GROUP INSURANCE PLAN (Partial Definition)

> **NOTE:** You already have the 'GROUP INSURANCE PLAN' File.

355.33 INSURANCE BUFFER (Partial Definition)

> **NOTE:** You already have the 'INSURANCE BUFFER' File.

366.01 NCPDP PROCESSOR (including data)

366.02 PHARMACY BENEFITS MANAGER (PBM) (including data)

366.03 PLAN (including data)

366.11 NCPDP PROCESSOR APPLICATION (including data)

366.12 PHARMACY BENEFITS MANAGER (PBM) APPLICATION (including data)

366.13 PLAN APPLICATION (including data)

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Checking Install for Package PRCA\*4.5\*202

Install Questions for PRCA\*4.5\*202

Incoming Files:

344 AR BATCH PAYMENT (Partial Definition)

> **NOTE:** You already have the 'AR BATCH PAYMENT' File.

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter Device Here\>

Install Started for BPS 1.0 :

Sep 10, 2004@15:17:54

Build Distribution Date: Sep 08, 2004

Installing Routines:

Sep 10, 2004@15:18:02

Installing Data Dictionaries:

Sep 10, 2004@15:18:13

Installing Data:

Sep 10, 2004@15:19:38

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing PRINT TEMPLATE

Installing SORT TEMPLATE

Installing INPUT TEMPLATE

Installing FORM

Installing HL LOGICAL LINK

Couldn't resolve Domain EPHARMACY.VITRIA-EDI.AAC.VA.GOV for Logical Link EPHARM OUT

Installing HL7 APPLICATION PARAMETER

Installing PROTOCOL

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Located in the BPS (IHS PHARMACY POINT OF SALE) namespace.

Installing LIST TEMPLATE

Installing OPTION

Sep 10, 2004@15:19:56

Running Post-Install Routine: ^BPSJXI1

Updating Routine file...

Updating KIDS files...

BPS 1.0 Installed.

Sep 10, 2004@15:20:01

Not a production UCI

NO Install Message sent

Install Started for PSS\*1.0\*81 :

Sep 10, 2004@15:20:01

Build Distribution Date: Sep 08, 2004

Installing Routines:

Updating Routine file...

Updating KIDS files...

PSS\*1.0\*81 Installed.

Sep 10, 2004@15:20:01

Not a production UCI

Install Message sent \#31959

Install Started for IB\*2.0\*223 :

Sep 10, 2004@15:20:01

Build Distribution Date: Sep 08, 2004

Installing Routines:

Sep 10, 2004@15:20:02

Installing Data Dictionaries:

Sep 10, 2004@15:20:06

Running Post-Install Routine: POST^IB20P223

Updating Routine file...

The following Routines were created during this install:

IBXX

IBXX1

IBXX10

IBXX11

IBXX12

IBXX13

IBXX14

IBXX15

IBXX16

IBXX17

IBXX18

IBXX19

IBXX2

IBXX20

IBXX21

IBXX22

IBXX23

IBXX24

IBXX25

IBXX26

IBXX27

IBXX3

IBXX4

IBXX5

IBXX6

IBXX7

IBXX8

IBXX9

Updating KIDS files...

IB\*2.0\*223 Installed.

Sep 10, 2004@15:20:07

Not a production UCI

Install Message sent \#31960

Install Started for IB\*2.0\*251 :

Sep 10, 2004@15:20:07

Build Distribution Date: Sep 08, 2004

Installing Routines:

Sep 10, 2004@15:20:10

Installing Data Dictionaries:

Sep 10, 2004@15:20:12

Installing Data:

Sep 10, 2004@15:23:31

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing PROTOCOL

Located in the IB (INTEGRATED BILLING) namespace.

Located in the IB (INTEGRATED BILLING) namespace.

Located in the IB (INTEGRATED BILLING) namespace.

Located in the IB (INTEGRATED BILLING) namespace.

Located in the IB (INTEGRATED BILLING) namespace.

Located in the IB (INTEGRATED BILLING) namespace.

Located in the IB (INTEGRATED BILLING) namespace.

Located in the IB (INTEGRATED BILLING) namespace.

Located in the IB (INTEGRATED BILLING) namespace.

Installing LIST TEMPLATE

Installing OPTION

Sep 10, 2004@15:23:33

Updating Routine file...

Updating KIDS files...

IB\*2.0\*251 Installed.

Sep 10, 2004@15:23:34

Not a production UCI

Install Message sent \#31961

Install Started for PRCA\*4.5\*202 :

Sep 10, 2004@15:23:34

Build Distribution Date: Sep 08, 2004

Installing Routines:

Sep 10, 2004@15:23:34

Installing Data Dictionaries:

Sep 10, 2004@15:23:35

Updating Routine file...

Updating KIDS files...

PRCA\*4.5\*202 Installed.

Sep 10, 2004@15:23:35

Not a production UCI

Install Message sent \#31962

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the installation has completed, the IRMS installer should contact the Pharmacy Automated Data Processing Application Coordinator (ADPAC) and the OPECC for ECME V. 1.0 setup. This setup must occur before this package/project is available for use. The steps are as follows:

1.  Setup the BPS and IB security keys and assign new menu options.
2.  Configure the V*IST*A HL7 Module
3.  Validate the HL7 system monitor is active and working for the two ePharmacy links
4.  Enter Site and Pharmacy Registration information
5.  Ensure the Registration request was sent to Austin
6.  Schedule the ePharmacy nightly process through Taskman

At any point after the BPS\*1.0 Master Build has been installed, the Insurance Matching process may occur. This is described in a separate document titled *e-Pharmacy Claims Insurance Process*. (See the BPS\*1.0 Master Build Description for the document location.) The site does not have to be registered to perform this matching process. However, sites do need to be registered to stay current with Pharmacy Group Plan information, specifically the most current Payer Sheet information. The Payer Sheets, linked to the Pharmacy Group Plans, define the format of the claims for specific Insurance Companies.

As mentioned, the first post installation step is to setup the BPS and IB security keys and assign several menu options, which is described as follows.

## Setup the BPS and IB Security Keys and Assign New Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The Pharmacy ADPAC must answer some questions concerning primary contact information and register the pharmacy with WebMD. These activities are described in detail in post installation Step 4, Enter Site and Pharmacy Registration Information. As these questions are being answered, a background job is kicked off to update the HL7 Payer sheets.

> To register the pharmacy, update the contact information, and ensure access to all ECME V. 1.0 menu screens, IRMS must assign the Pharmacy ADPAC and any other Medical Center personnel who need this access, the following keys:

BPSMENU BPS REPORTSBPS USER BPS BILLER

> BPS MANAGER.

The IRMS staff must assign several ECME V. 1.0 menu options for pharmacy registration, which will be performed in post installation Step 4, Enter Site and Pharmacy Registration Information. The site’s Pharmacy ADPAC and other appropriate staff should receive the menu option assignments. These menu options are as follows:

> *ECME Main Menu* \[BPSMENU\] option

> *Pharmacy ECME Manager Menu* \[BPS MANAGER MENU\] option

> *Pharmacy ECME Setup Menu* \[BPS SETUP MENU\] option

> *Register Pharmacy with WebMD* \[BPS SETUP REGISTER PHARMACY\] option

2.  A new IB security key has been developed to restrict access to the Pharmacy Group Matching functionality. This key, IBCNR E-PHARMACY SUPERVISOR should be restricted to only Medical Center personnel who will perform this function. (The Insurance Supervisor will need this security key.) The document for this function is separate from this Guide and is titled *e-Pharmacy Claims Insurance Process*. (See the BPS\*1.0 Master Build Description for the document location.)

> ![](bps-version-1-dormant-release-installation-guide/005.png)Note: Assignment of the IBCNR E-PHARMACY SUPERVISOR security key will automatically result in an expansion of the Patient Insurance Menu (IBCN Insurance Management Menu) to include additional e-Pharmacy menu options, which are necessary for the insurance matching process.

The personnel that are assigned this security key will see more menu options on the *ePharmacy Menu* option than the report options (*Group Plan Worksheet Report* option and *Pharmacy Plan Report* option) that other personnel assigned the IBCN Insurance Management Menu will see. These seven new menu options are listed below with an asterisk (\*) in front of them.

> Example: New Menu Options on the ePharmacy Menu

> EHNF Edit HIPAA NCPDP FLAG

> \*\*\> Out of order: OPTION NOT YET AVAILABLE

> \* ENP Edit NCPDP PROCESSOR APPLICATION Sub-file

> \* EPAY Edit PAYER APPLICATION Sub-file

> \* EPBM Edit PBM APPLICATION Sub-file

> \* EPLA Edit PLAN APPLICATION Sub-file

> \* MGP Match Group Plan to a Pharmacy Plan

> \* MMGP Match Multiple Group Plans to a Pharmacy Plan

> \* MTPS Match Test Payer Sheet to a Pharmacy Plan

> RGPW Group Plan Worksheet Report

> RPP Pharmacy Plan Report

> The *Edit HIPAA NCPDP FLAG* option is denoted with an out-of-order statement. This option is not available with this dormant release but will be available in the next release (active).

## Configure the VISTA HL7 Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### <u>Configure HL7 Logical Links</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The site’s IRMS personnel perform this function. All required HL7 applications, links, and protocols were installed when the BPS\*1.0 Master Build completed.

> There are two HL7 Logical Links to configure; the link to send registration information is EPHARM OUT and the link to receive payer sheet information is EPHARM IN.

> You should have received patch XM\*DBA\*160 SEQ \#157 to manually create a new domain in your Domain File (#4.2) - EPHARMACY.VITRIA-EDI.AAC.VA.GOV. This domain will be used for Logical Link EPHARM OUT.

### ### <u>Configuring the EPHARM OUT Logical Link</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the HL7 Main Menu select, Interface Developer Options.
2.  Select the option, EL Link Edit.
3.  Select the EPHARM OUT Logical Link Node.
4.  For Institution: \<Enter\> to leave blank.
5.  Enter EPHARMACY.VITRIA-EDI.AAC.VA.GOV for the Domain.
6.  Set the AUTOSTART field to Enabled.
7.  Set the QUEUE SIZE field to 10.
8.  Accept the default LLP TYPE, which is TCP, by pressing the \<Enter\> key. This will take you to the TCP Lower Level Parameters.
9.  Enter 10.224.187.133 for the TCP/IP Address.
10. Enter 5105 for the TCP/IP port number.

  
Example: Configuring the EPHARM OUT Logical Link

> CHOOSE 1-15: 11 HL MAIN MENU HL7 Main Menu

> Systems Link Monitor

> Filer and Link Management Options ...

> Message Management Options ...

> Interface Developer Options ...

> Site Parameter Edit

> Select HL7 Main Menu Option: Interface Developer Options

> EA Application Edit

> EP Protocol Edit

> EL Link Edit

> VI Validate Interfaces

> Reports ...

> Select Interface Developer Options Option: EL Link Edit

> Select HL LOGICAL LINK NODE: EPHARM

> 1 EPHARM IN

> 2 EPHARM OUT

> CHOOSE 1-2: 2 EPHARM OUT

> HL7 LOGICAL LINK

> --------------------------------------------------------------------------

> NODE: EPHARM OUT

> INSTITUTION:

> DOMAIN: EPHARMACY.VITRIA-EDI.AAC.VA.GOV

> AUTOSTART: Enabled

> QUEUE SIZE: 10

> LLP TYPE: TCP

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

--------------------------------------example continues--------------------------------------

Example: Configuring the EPHARM OUT Logical Link (continued)

> HL7 LOGICAL LINK

> --------------------------------------------------------------------------

> \[----------------------TCP LOWER LEVEL PARAMETERS-------------------------\]

> \| EPHARM OUT \|

> \| \|

> \| TCP/IP SERVICE TYPE: CLIENT (SENDER) \|

> \| TCP/IP ADDRESS: 10.224.187.133 \|

> \| TCP/IP PORT: 5105 \|

> \| \|

> \| \|

> \| ACK TIMEOUT: 60 RE-TRANSMISION ATTEMPTS: \|

> \| READ TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: restart \|

> \| BLOCK SIZE: SAY HELO: \|

> \| \|

> \|STARTUP NODE: PERSISTENT: NO \|

> \| RETENTION: 60 UNI-DIRECTIONAL WAIT: \|

> \[-------------------------------------------------------------------------\]

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> COMMAND: Press \<PF1\>H for help Insert

### <u>Configuring the EPHARM IN Link</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. From the HL7 Main Menu select, Interface Developer Options.

> 2\. Select the option, EL - Link Edit.

> 3\. Select the EPHARM IN Logical Link Node.

> 4\. Leave the Institution prompt blank.

> 5\. Leave the Domain prompt blank.

> 6\. Change the AUTOSTART field to Enabled.

> 7\. Enter 10 for the Queue Size.

> 8\. Accept the default LLP TYPE, which is TCP, by pressing the Enter key. This will take you to the TCP Lower Level Parameters.

9.  Validate the IP address for the node that this HL7 listener will be running on. This address is automatically updated during the initial BPS\*1.0 Master Build installation.

> **NOTE:** This IP address should match the IP address in the “IIV SERVER” Logical Link.

> 10\. Confirm that the TCP/IP Port is set to 5105. This is the port number that has been assigned for the e-Pharmacy project by the VA HL7 group. All incoming communications for e-Pharmacy will be using port 5105.

> 11\. The STARTUP NODE field is available to the DSM/VMS sites. (This is a Kernel TaskMan issue.) Cache/VMS and Cache/NT sites do not have this functionality. Hit ‘?” to see the available choices for your DSM/VMS system and select the appropriate startup node option.

Example: Configuring the EPHARM IN Logical Link

> CHOOSE 1-15: 11 HL MAIN MENU HL7 Main Menu

> Systems Link Monitor

> Filer and Link Management Options ...

> Message Management Options ...

> Interface Developer Options ...

> Site Parameter Edit

> Select HL7 Main Menu Option: Interface Developer Options

> Select Interface Developer Options Option: EL Link Edit

> Select HL LOGICAL LINK NODE: EPHARM

> 1 EPHARM IN

> 2 EPHARM OUT

> CHOOSE 1-2: 1 EPHARM IN

> HL7 LOGICAL LINK

> --------------------------------------------------------------------------

> NODE: EPHARM IN

> INSTITUTION:

> DOMAIN:

> AUTOSTART: Enabled

> QUEUE SIZE: 10

> LLP TYPE: TCP

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> COMMAND: Press \<PF1\>H for help Insert

--------------------------------------example continues--------------------------------------

Example: Configuring the EPHARM IN Logical Link (continued)

> HL7 LOGICAL LINK

> --------------------------------------------------------------------------

> \[---------------------TCP LOWER LEVEL PARAMETERS-----------------------\]

> \| IIV SERVER \|

> \| \|

> \| TCP/IP SERVICE TYPE: SINGLE LISTENER \|

> \| TCP/IP ADDRESS: {This is the IP address for the node on which \|

> \| this link will be run} \|

> \| TCP/IP PORT: 5105 \|

> \| \|

> \| \|

> \| ACK TIMEOUT: 40 RE-TRANSMISION ATTEMPTS: \|

> \| READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: restart\|

> \| BLOCK SIZE: SAY HELO: \|

> \| \|

> \|STARTUP NODE: ROU:500A01 PERSISTENT: \|

> \| RETENTION: UNI-DIRECTIONAL WAIT: \|

> \[----------------------------------------------------------------------\]

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Close Refresh

> Enter a command or '^' followed by a caption to jump to a specific field.

> COMMAND: Close Press \<PF1\>H for help Insert

## Validate the HL7 System Monitor is Active and Working for the Two ePharmacy Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The site’s IRMS personnel perform this step. The following activities will verify that the HL7 links have been successfully configured.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### <u>Start the New HL7 Logical Links</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, you will validate the links are operating correctly. Summarizing, during this step you will:

1.  Use the *Systems Link Monitor* option within the *HL7 MAIN MENU* option to confirm that the Link Manager is running.
2.  Use the *Systems Link Monitor* option within the *HL7 MAIN MENU* option to confirm that at least 1 incoming and 1 outgoing filer are running.
3.  Turn on these two new logical links using the *Start/Stop Links* \[HL START\] option.

> When asked to identify whether the EPHARM IN logical link should be started in the background, accept the default of background.

### <u>Validating the HL7 Logical Links:</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The normal states for each link should be idle, reading, or inactive. The following screen print example illustrates what to look for.

Example: Validating Link Manager and Filers are Running

> Select OPTION NAME: HL7

> 1 HL7 MAIL MESSAGE SERVER HL SERVER HL7 Mail Message Server

> 2 HL7 MAIN MENU HL MAIN MENU HL7 Main Menu

> 3 HL7 MESSAGING MONITOR RGMT MONITOR MESSAGING HL7 Messaging Monitor

> 4 HL7 V1.5 OPTIONS HL MENU 1.5 HL7 V1.5 OPTIONS

> 5 HL7 V1.6 MAIL MESSAGE SERVER HL V16 SERVER HL7 v1.6 Mail Message Server

> CHOOSE 1-5: 2 HL MAIN MENU HL7 Main Menu

> Systems Link Monitor

> Filer and Link Management Options ...

> Message Management Options ...

> Interface Developer Options ...

> Site Parameter Edit

> Find running tasks

> Select \<V15 West\> HL7 Main Menu Option: Systems Link Monitor

> SYSTEM LINK MONITOR for VA HEARTLAND - WEST, VISN 15 (T System)

> MESSAGES MESSAGES MESSAGES MESSAGES DEVICE

> NODE RECEIVED PROCESSED TO SEND SENT TYPE STATE

> DGRU-LE 1062 1062 1062 1062 NC Inactive

> DGRU-TO 157 157 157 157 NC Inactive

> DGRU-WI 1039 1039 1039 1039 NC Inactive

> EPHARM I 337 337 337 337 SS Reading

> EPHARM O 340 340 340 340 NC Inactive

> EPI-LAB 1369 1369 1369 1369 MM IDLE

> IIV EC 38097 38097 38097 38097 NC Inactive

> IIV SERV 39298 39298 39298 39298 SS Reading

> LA7V 657 11330 11330 11476 11476 MM IDLE

> LL15VISN 438763 438763 439138 438763 NC Inactive

> Incoming filers running =\> 2 TaskMan running

> Outgoing filers running =\> 2 Link Manager running

> Select a Command:

> (N)EXT (B)ACKUP (A)LL LINKS (S)CREENED (V)IEWS (Q)UIT (?) HELP:N

If the correct links are not running or there are any questions regarding this, please contact EVS support for assistance by contacting the help desk (888-596-4357) to log a NOIS for you or submitting a NOIS yourself under the package synonym BPS or ECME.

> Example: Starting HL7 Logical Link EPHARM IN

> Select HL7 Main Menu Option: Filer and Link Management Options

> Select Filer and Link Management Options Option: SLStart/Stop Links

> This option is used to launch the lower level protocol for the

> appropriate device. Please select the node with which you want

> to communicate

> Select HL LOGICAL LINK NODE: EPHARM IN

> Select one of the following:

> F FOREGROUND

> B BACKGROUND

> Q QUIT

> Method for running the receiver: B// B BACKGROUND

> Job was queued as 221129.

### ### > Example: Starting HL7 Logical Link EPHARM OUT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select HL7 Main Menu Option: Filer and Link Management Options

> Select Filer and Link Management Options Option: SLStart/Stop Links

> This option is used to launch the lower level protocol for the

> appropriate device. Please select the node with which you want

> to communicate

> Select HL LOGICAL LINK NODE: EPHARM OUT

> This LLP has been enabled!

### <u>Re-starting the HL7 Logical Links if Re-Installing the Master Build :</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before re-installing the Master Build, you must first stop the logical links, EPHARM IN and EPHARM OUT. Afterwards, you should be ready to re-install the Master Build. Following the build re-installation, and prior to performing Step 4, Enter Site and Pharmacy Registration Information, the logical links EPHARM IN and EPHARM OUT must be started up.

1.  Stopping the HL7 Logical Link EPHARM IN
    1.  From the HL7 Main Menu, select Filer and Link Management Options.
    2.  Select the option SL – Start/Stop Links.
    3.  Enter Logical Link Node: EPHARM IN.
    4.  Shut down this job? YES.

> Example: Stopping HL7 Logical Link EPHARM IN

> Select HL7 Main Menu Option: Filer and Link Management Options

> Select Filer and Link Management Options Option: SLStart/Stop Links

> Select HL LOGICAL LINK NODE: EPHARM IN

> The LLP was last started on AUG 12, 2004 15:35:41.

> Okay to shut down this job? YES

> The job for the EPHARM IN Lower Level Protocol will be shut down.

2.  Repeat Step A for Stopping the HL7 Logical Link EPHARM OUT
3.  Re-install the Master Build.
4.  Starting the HL7 Logical Link EPHARM IN
1.  From the HL7 Main Menu, select Filer and Link Management Options.
2.  Select the option SL – Start/Stop Links.
3.  Enter Logical Link Node: EPHARM IN.
4.  Select Method for running the receiver: B – BACKGROUND.
5.  Starting the HL7 Logical Link EPHARM OUT
1.  From the HL7 Main Menu, select Filer and Link Management Options.
2.  Select the option SL – Start/Stop Links.
3.  Enter Logical Link Node: EPHARM OUT.
6.  Proceed to Step 4 Enter Site and Pharmacy Registration Information

## Enter Site and Pharmacy Registration Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The site’s Pharmacy ADPAC performs this step. For the initial registration of a pharmacy to use ECME V. 1.0, the ADPAC will use the *Register Pharmacy with WebMD* \[BPS SETUP REGISTER PHARMACY\] option.

> During the initial e-Pharmacy registration, HL7 communication is attempted with the communication servers located at the FSC in Austin, TX. If communication is successful, the server receives the application registration request and acknowledges registration. Once the Application Registration has been accepted, all Outpatient Pharmacies will be registered. This response is sent back via the HL7 interface immediately. Additionally, when the Application Registration has been successful, Payer Sheets will be transmitted from the Vitria server.

> If the communication is not successful, or you have questions concerning the success of the communication, please seek assistance from your Systems Manager responsible for the HL7 package or contact EVS support for assistance by contacting the help desk (888-596-4357) to log a NOIS for you or submitting a NOIS yourself under the package synonym BPS or ECME.

> This step should be repeated for any future registration information changes.

### ### <u>Required and Optional Fields</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The following items are optional fields. In the event of a communications problem, the site and alternate site information will be used by the FSC for contacting your site. (Normally, the site’s IRMS staff will be entered in these fields.) All names must have previously been set up in the NEW PERSON file (#200). Associated predefined data, such as telephone data and email addresses, are pulled from this file when the contact name is entered. The following information is asked, but is not mandatory:

VA SITE CONTACT

OFFICE PHONE

> EMAIL ADDRESS  
> VA ALTERNATE SITE CONTACT

OFFICE PHONE

> EMAIL ADDRESS

2.  Fields are either required or optional for input to complete the registration process. If any of the required fields are left blank, the Pharmacy’s Registration will not be transmitted. The following list includes all of the fields displayed during the registration process and the required fields are designated with an asterisk (\*).

> \*BPS PHARMACIES NAME

> \*NCPDP \#

> \*DEFAULT DEA \#

> \*SITE ADDRESS NAME

> \*SITE ADDRESS 1

> SITE ADDRESS 2

> \*SITE CITY

> \*SITE STATE

> \*SITE ZIP CODE

> \*REMITTANCE ADDRESS NAME

> \*REMIT ADDRESS 1

> REMIT ADDRESS 2

> \*REMIT CITY

> \*REMIT STATE

> \*REMIT ZIP

> DAILY HOURS OF OPERATION (SUN-SAT, OPEN & CLOSE)

> \*VA CONTACT

> TITLE

> OFFICE PHONE

> EMAIL ADDRESS

> \*VA ALTERNATE CONTACT

> TITLE

> OFFICE PHONE

> EMAIL ADDRESS

> \*VA LEAD PHARMACIST

> TITLE

> VA LEAD PHARMACIST LICENSE \#

![](bps-version-1-dormant-release-installation-guide/006.png)Note: Unless any of the pharmacy information changes, this *Register Pharmacy with WebMD* \[BPS SETUP REGISTER PHARMACY\] option will probably not be used after the initial setup.

### <u>Detailed Registration Steps</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To register the pharmacy and update the contact information, use the following menu path:

*ECME Main Menu* \[BPSMENU\] (Locked: BPSMENU)

*Pharmacy ECME Manager Menu* \[BPS MANAGER MENU\] (Locked: BPS MANAGER)

*Pharmacy ECME Setup Menu* \[BPS SETUP MENU\]

> *Register Pharmacy with WebMD* \[BPS SETUP REGISTER PHARMACY\]

2.  The first prompts will be the name and information of the Primary point of contact for the site. Please enter the Primary contact name. The office phone number and e-mail address will be automatically updated from the NEW PERSON file (#200) if available.

> PRIMARY SITE CONTACT DATA.

> VA SITE CONTACT: ECMEIRMS27,FIVE

> OFFICE PHONE: 555-555-7890

> EMAIL ADDRESS: FIVE.ECMEIRMS27@med.va.gov

3.  The next prompts will request the same information for an Alternate point of contact. Please enter the Alternate contact name. The office phone number and e-mail address will be automatically updated from the NEW PERSON file (#200) if available.

> ALTERNATE SITE CONTACT DATA.

> VA ALTERNATE SITE CONTACT: ECMEIRMS1,FIVE

> OFFICE PHONE: 555-555-7123

> EMAIL ADDRESS: FIVE.ECMEIRMS1@med.va.gov

4.  Once the site’s information has been entered, the validation of the entire Application Registration HL7 Message will occur. This validation includes both the site information and the HL7 parameters. The validation display will be similar to the example below.

Example: Validation of Site Information and HL7 Parameters

> -- APPLICATION REGISTRATION VALIDATION RESULTS. --

> DOMAIN NAME - Required - VALID: EPHARMACY.VITRIA-EDI.AAC.VA.GOV

> TCP/IP ADDRESS FOR EPHARM IN - Required - VALID: 63.80.242.54

> TCP/IP ADDRESS FOR EPHARM OUT - Required - VALID: 10.224.187.133

> "EPHARM OUT" PORT NUMBER - Required - VALID: 5105

> SITE NUMBER - Required - VALID: 509

> INTERFACE VERSION - Required - VALID: 1

> "EPHARM IN" PORT NUMBER - Required - VALID: 5105

> CONTACT NAME - VALID: ECMEIRMS27^FIVE^^^

> CONTACT MEANS - VALID: ^NET^INTERNET^FIVE.ECMEIRMS27@med.va.gov~^WPN^PH^^^555555^7890

> ALTERNATE CONTACT NAME - VALID: ECMEIRMS1^FIVE^^^

> ALTERNATE CONTACT MEANS - VALID: ^NET^INTERNET^FIVE.ECMEIRMS1@med.va.gov~^WPN^PH^^^555555^7123

> -- APPLICATION REGISTRATION DATA VALID. –

> If an INVALID field is identified, it will be displayed with leading stars “\*\*”, and the last line will flag the registration as INVALID. Additionally, although pharmacy registration data entry will be allowed, registration processing will abort before HL7 messages are actually sent. The following is a sample of an Invalid registration.

Example: Invalid Site Information and HL7 Parameters

> -- APPLICATION REGISTRATION VALIDATION RESULTS. --

> DOMAIN NAME - Required - VALID: EPHARMACY.VITRIA-EDI-TEST.AAC.VA.GOV

> \* WARNING: "EPHARM IN" TCP/IP ADDRESS IS DIFFERENT THAN "IIV EC" TCP/IP ADDRESS.

> EPHARM IN: 12.162.5.29 IIV EC: 12.162.10.300

> TCP/IP ADDRESS FOR EPHARM OUT - Required - VALID: 10.224.187.133

> "EPHARM OUT" PORT NUMBER - Required - VALID: 5105

> SITE NUMBER - Required - VALID: 509

> INTERFACE VERSION - Required - VALID: 1

> \*\* "EPHARM IN" PORT NUMBER - Required - INVALID

> CONTACT NAME - VALID: ECMEIRMS27^FIVE^^^

> CONTACT MEANS - VALID: ^NET^INTERNET^FIVE.ECMEIRMS27@med.va.gov~^WPN^PH^^^555555^7890

> ALTERNATE CONTACT NAME - VALID: ECMEIRMS1^FIVE^^^

> ALTERNATE CONTACT MEANS - VALID: ^NET^INTERNET^FIVE.ECMEIRMS1@med.va.gov~^WPN^PH^^^555555^7123

> \*\* APPLICATION REGISTRATION DATA INVALID!!! \*\*

> \*\* APPLICATION REGISTRATION AND PHARMACY \*\*

> \*\* REGISTRATIONS WILL NOT BE SENT! \*\*

5.  Outpatient Pharmacy Registration Data screen will be displayed at this point.

> PHARMACY SPECIFIC DATA.

> Select BPS PHARMACIES NAME: PHARMACY-1

> Enter a BPS PHARMACIES NAME, or OUTPATIENT SITE. By entering a question mark (?), the system will return the available BPS Pharmacies. A new BPS Pharmacy can be entered and the name must be 3 – 30 alphabetical characters (<u>not</u> numeric and can <u>not</u> start with a punctuation mark). No Community Based Outpatient Clinics (CBOCs), satellite, or remote pharmacies should be registered at this time.

6.  The Pharmacy Name is displayed again for verification and then additional prompts for all of the fields will display. Enter the pharmacy’s data:

Example: Pharmacy Fields

> NAME: PHARMACY-1

> NCPDP \#: 1516206

> DEFAULT DEA \#: AV4309628

> SITE ADDRESS NAME: PHARMACY ONE

> SITE ADDRESS 1: 104 OAK STREET

> SITE ADDRESS 2: \<Enter\>

> SITE CITY: BIRMINGHAM

> SITE STATE: AL

> SITE ZIP CODE: 35203

> REMITTANCE ADDRESS NAME: PHARMACY ONE BUSNESS OFFICE

> REMIT ADDRESS 1: 104 OAK STREET

> REMIT ADDRESS 2: \<Enter\>

> REMIT CITY: BIRMINGHAM

------------------------------------example continues------------------------------------

  
Example: Pharmacy Fields (continued)

> REMIT STATE: AL

> REMIT ZIP: 35203

> DAILY HOURS OF OPERATION

> DAY 1-SUN 2-MON 3-TUE 4-WED 5-THU 6-FRI 7-SAT

> OPEN TIME 0800 0800 0800 0800 0800 0800

> CLOSE TIME 1600 1600 1600 1600 1600 1600

> Enter Day to Edit: (1-7): 7

> Enter Open Time (4 digit military time, C=Closed,24 for open 24 hours): C

> DAILY HOURS OF OPERATION

> DAY 1-SUN 2-MON 3-TUE 4-WED 5-THU 6-FRI 7-SAT

> OPEN TIME 0800 0800 0800 0800 0800

> CLOSE TIME 1600 1600 1600 1600 1600

> Enter Day to Edit: (1-7): 6

> Enter Open Time (4 digit military time, C=Closed,24 for open 24 hours): 0800

> Enter Close Time (4 digit military time): 2000

> DAILY HOURS OF OPERATION

> DAY 1-SUN 2-MON 3-TUE 4-WED 5-THU 6-FRI 7-SAT

> OPEN TIME 0800 0800 0800 0800 0800

> CLOSE TIME 1600 1600 1600 1600 2000

> Enter Day to Edit: (1-7): \<Enter\>

> VA CONTACT: ECMEPHARMACIST2,THREE

> TITLE: \<Enter\>

> OFFICE PHONE: 555 555 7789

> EMAIL ADDRESS: THREE.ECMEPHARMACIST2@med.va.gov

> ALTERNATE CONTACT DATA.

> VA ALTERNATE CONTACT: EMCEPHARMACIST30,THREE

> TITLE: PHARMACIST

> OFFICE PHONE: 555 555 7644

> EMAIL ADDRESS: THREE.EMCEPHARMACIST30@med.va.gov

> PHARMACIST DATA.

> VA LEAD PHARMACIST: EMCEPHARMACIST30,THREE

> TITLE: PHARMACIST

> VA LEAD PHARMACIST LICENSE \#: 987654ZYX

7.  Once all the fields have been entered, validation will automatically be performed, and results similar to the following will be displayed:

Example: Validation of Pharmacy Information

> -- PHARMACY REGISTRATION VALIDATION RESULTS. --

> NABP NUMBER - Required - VALID: NCPDP-1234

> PHARMACY NAME - Required - VALID: PHARMACY-1

> DEA NUMBER - Required - VALID: DEA-5678

> HOURS OF OPERATION - VALID: MON^MON^0800^1600~TUE^TUE^0800^1600~WED^WED^0800^

> 1600~THU^THU^0800^1600~FRI^FRI^0800^2000

> MAILING ADDRESS - Required - VALID: PHARMACY ONE 104 OAK STREET^^BIRMINGHAM^AL^35203

> REMITTANCE ADDRESS - Required - VALID: PHARMACY ONE BUSNESS OFFICE 104 OAK STREET^^BIRMINGHAM^AL^35203

> CONTACT NAME - Required - VALID: ECMEPHARMACIST2^THREE^^^^

> CONTACT TITLE - VALID:

> CONTACT MEANS - VALID:

> ^NET^INTERNET^THREE.ECMEPHARMACIST2@med.va.gov~^WPN^PH^^^555555^7789

> ALTERNATE CONTACT NAME - Required - VALID: EMCNPHARMACIST30^THREE^^^^

> ALTERNATE CONTACT TITLE - VALID: PHARMACIST

> ALTERNATE CONTACT MEANS - VALID:

> ^NET^INTERNET^THREE.ECMPHARMACIST30@med.va.gov~^WPN^PH^^^555555^7644

> LEAD PHARMACIST NAME - Required - VALID: ECMEPHARMACIST30^THREE^^^^

> LEAD PHARMACIST TITLE - VALID: PHARMACIST

> LEAD PHARMACIST LICENSE NUMBER - Required - VALID: 987654ZYX

> --PHARMACY REGISTRATION DATA VALID. –

> If an INVALID field is identified, it will be displayed with leading stars “\*\*”, and the last line will flag the registration as INVALID. When invalid fields are identified, the pharmacy’s registration data will not be transmitted. The following is a sample of Invalid pharmacy information.

Example: Invalid Pharmacy Information

> -- PHARMACY REGISTRATION VALIDATION RESULTS. --

> \*\* NABP NUMBER - Required - INVALID

> PHARMACY NAME - Required - VALID: PHARMACY-2

> \*\* DEA NUMBER - Required - INVALID

> HOURS OF OPERATION - VALID: MON^MON^0800^1600~TUE^TUE^0800^1600~WED^WED^0800^

> 1600~THU^THU^0800^1600~FRI^FRI^0800^2000

> MAILING ADDRESS - Required - VALID: 104 OAK STREET^^BIRMINGHAM^AL^35203

> REMITTANCE ADDRESS - Required - VALID: 104 OAK STREET^^BIRMINGHAM^AL^35203

> CONTACT NAME - Required - VALID: ECMEPHARMACIST2^THREE^^^^

> CONTACT TITLE - VALID:

> CONTACT MEANS - VALID:

> ^NET^INTERNET^THREE.ECMEPHARMACIST2@med.va.gov~^WPN^PH^^^555555^7789

> ALTERNATE CONTACT NAME - Required - VALID: EMCNPHARMACIST30^THREE^^^^

> ALTERNATE CONTACT TITLE - VALID: PHARMACIST

> ALTERNATE CONTACT MEANS - VALID:

> ^NET^INTERNET^THREE.ECMPHARMACIST30@med.va.gov~^WPN^PH^^^555555^7644

> LEAD PHARMACIST NAME - Required - VALID: ECMEPHARMACIST30^THREE^^^^

> LEAD PHARMACIST TITLE - VALID: PHARMACIST

> LEAD PHARMACIST LICENSE NUMBER - Required - VALID: 987654ZYX

> \*\* PHARMACY REGISTRATION DATA INVALID!!! \*\*

> \*\* THIS PHARMACY'S REGISTRATION WILL NOT BE SENT! \*\*

> Although this pharmacy’s registration data is flagged as invalid, it will not prevent the sending of a valid site registration, along with other valid pharmacy’s registrations.

8.  After the validation information has been displayed, you will be returned to the “Select BPS PHARMACIES NAME:” prompt. Entering another name will repeat the pharmacy data entry process for that pharmacy. Pressing the Enter key (\<Enter\>) will exit from the Pharmacy Registration Data Entry process. No CBOCs, satellite, or remote pharmacies should be registered at this time.
9.  When exiting the Pharmacy Registration Data Entry process, you will be returned to the Application Registration process. If the application registration data is valid, then you will be prompted to send all valid registration data:

> APPLICATION REGISTRATION DATA IS VALID FOR TRANSMISSION.

> PHARMACY REGISTRATION DATA IS:

> \*INVALID for EPHARMACY-1 and will NOT be transmitted.

> VALID for EPHARMACY-2 and will be transmitted.

> SEND APPLICATION REGISTRATION: Y/N YES

> APPLICATION REGISTRATION SUBMITTED.

> If the application registration data is invalid, the registration process will abort, displaying the following message:

> REGISTRATION ABORTED DUE TO INVALID SITE REGISTRATION DATA.

![](bps-version-1-dormant-release-installation-guide/007.png)Note: During this step, please monitor the HL7 message traffic using the HL7 system monitor tools to watch for messages being sent and received on the EPHARM IN and EPHARM OUT logical links as described below. This may require assistance from a Systems Manager that is responsible for the HL7 package.

> Check the HL7 system monitor to see if there have been any messages sent out on the EPHARM OUT logical link. There should be 1 or more messages in the EPHARM OUT link. The initial transmission is the Application Registration. If no messages are being sent by the EPHARM OUT link, then confirm that the HL7 logical link settings for the EPHARM OUT have been entered as previously instructed and ensure that the link is enabled and running.

> Check the HL7 system monitor to see if there have been any messages received on the EPHARM IN logical link. There should be 1 or more messages in the EPHARM IN link. The initial transmission received is the Application Registration Acknowledgement. If no messages are being received by the EPHARM IN link at all, then confirm that the HL7 logical link settings for the EPHARM IN link has been entered as previously instructed and ensure that the link is enabled and running. If you find that configuration changes need to be made, attempt to register again by starting over with step \#1 in the Detail Registration Steps section. If everything seems to be correct with the configuration and no messages were received, please contact EVS support for assistance by contacting the help desk (888-596-4357) to log a NOIS for you or submitting a NOIS yourself under the package synonym BPS or ECME.

## Ensure the Registration Request was sent to Austin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The site’s Pharmacy ADPAC performs this validation step. If you see the following message, the registration was successfully sent to Austin:

> APPLICATION REGISTRATION SUBMITTED.

Once you see this message, send an Outlook message to the ePharmacy Registration mail group with the following text: “The \<VAMC Name\>, Site Number \<NNN\> has completed the registration process for e-Pharmacy. Please confirm that the application registration was received and processed properly.”

After confirmation of application registration is received, continue with the next step. For registrations that occur during the weekday from 8:00 AM to 4:00 PM Central time, you may expect confirmation or further communication within one (1) hour.

## Schedule the ePharmacy Nightly Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The site’s IRMS personnel perform this step. The registration process must complete successfully before continuing.

There is one new option that should be scheduled to run once per day, the *BPS APP REG TASKMAN* \[EPHARMACY APPLICATION REGISTRATION - TASKMAN\] option. You can schedule the e-Pharmacy Nightly process through Taskman. This nightly background job performs two major tasks. First it resends the e-Pharmacy application registration then it resends all the Outpatient Pharmacy registration data including any new Outpatient Pharmacies that were added since the last registration cycle.

![](bps-version-1-dormant-release-installation-guide/008.png)Note: It is recommended that this option be scheduled to run during non-peak times in the evening. Assistance from a system manager may be required to schedule this option.

1.  From the *Taskman Management* menu select, *Schedule/Unschedule Options*.
2.  Schedule the option, BPS APP REG TASKMAN.
3.  Select the time the option should run (during non-peak hours).
4.  Set the "Rescheduling Frequency" to 1D (once a day).

  
Example: Scheduling the ePharmacy Nightly Process

> Taskman Management

> Schedule/Unschedule Options

> One-time Option Queue

> Taskman Management Utilities ...

> List Tasks

> Dequeue Tasks

> Requeue Tasks

> Delete Tasks

> Print Options that are Scheduled to run

> Cleanup Task List

> Print Options Recommended for Queueing

> Select Taskman Management Option: SCHEdule/Unschedule Options

> Select OPTION to schedule or reschedule: BPS APP REG TASKMAN

> EPHARMACY APPLICATION REGISTRATION - TASKMAN

> Are you adding 'BPS APP REG TASKMAN as

> a new OPTION SCHEDULING (the 82ND)? No// YES (Yes)

> Edit Option Schedule

> Option Name: BPS APP REG TASKMAN

> Menu Text: EPHARMACY APPLICATION REGISTRATION – TASKMAN

> TASK ID:

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> QUEUED TO RUN AT WHAT TIME: FEB 14,2004@01:00

> DEVICE FOR QUEUED JOB OUTPUT:

> QUEUED TO RUN ON VOLUME SET:

> RESCHEDULING FREQUENCY: 1D

> TASK PARAMETERS:

> SPECIAL QUEUEING:

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> Enter a command or '^' followed by a caption to jump to a specific field.

*  
(This page included for two-sided copying.)*