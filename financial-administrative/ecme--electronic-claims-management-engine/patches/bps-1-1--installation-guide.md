---
title: BPS*1*1 ECME HIPAA NCPDP Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: ECME HIPAA NCPDP
app_code: ECME
app_name: Electronic Claims Management Engine
section: FIN
app_status: active
pkg_ns: BPS
patch_ver: 1
patch_id: BPS*1*1
group_key: "ECME:BPS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - pharmacy
  - ecme
  - ncpdp
  - installation
  - link
  - table
  - contents
  - hipaa
  - site
  - claims
page_count: 0
word_count: 5751
section_count: 12
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/ecme_hipaa_ncpdp_1_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/ecme_hipaa_ncpdp_1_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=141"
---

> ![](bps-1-1-ecme-hipaa-ncpdp-installation-guide/001.png)

hipaa ncpdp connection for EDI Pharmacy  
(Active Release)INSTALLATION GUIDE

April 2006

BPS\*1\*1,PSO\*7\*148  
IB\*2\*276,PSS\*1\*90

PSX\*2\*48,PRCA\*4.5\*230

VistA Health  
Systems Design & Development

######### Table of Contents

*(This page included for two-sided copying.)*

# Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Minimum Required Packages](#minimum-required-packages)
- [Pre-Installation](#pre-installation)
  - [Required Patches](#required-patches)
  - [Exported Keys](#exported-keys)
  - [Global Growth](#global-growth)
  - [New Fields](#new-fields)
- [Installation](#installation)
- [Installation StepsIT IS VERY IMPORTANT THAT THESE INSTRUCTIONS ARE FOLLOWED STEP BY STEP IN THE EXACT ORDER INDICATED BELOW. ONCE STARTED, THE INSTALLATION NEEDS TO BE COMPLETED. FAILURE TO FULLY COMPLETE THE INSTALLATION (ONCE STARTED) WILLLIKELY CAUSE PROBLEMS FOR USERS OF THE 6 APPLICATIONS INVOLVED IN THIS PROJECT.](#installation-stepsit-is-very-important-that-these-instructions-are-followed-step-by-step-in-the-exact-order-indicated-below-once-started-the-installation-needs-to-be-completed-failure-to-fully-complete-the-installation-once-started-willlikely-cause-problems-for-users-of-the-6-applications-involved-in-this-project)
- [Post-Installation](#post-installation)
  - [Re-register the Site and Pharmacies](#re-register-the-site-and-pharmacies)
- [Activation Steps](#activation-steps)
  - [Task 1 – Configure the VistA HL7 Module](#task-1-configure-the-vista-hl7-module)
  - [Task 2 – Matching the Outpatient Site to the BPS PHARMACIES file](#task-2-matching-the-outpatient-site-to-the-bps-pharmacies-file)
  - [Task 3 – Turning On the Insurance Switch](#task-3-turning-on-the-insurance-switch)
  - [Task 4 – Activating VA Plans for Electronic Submission](#task-4-activating-va-plans-for-electronic-submission)
  - [Task 5 – Schedule the BPS Nightly Background Job](#task-5-schedule-the-bps-nightly-background-job)
  - [Task 6 – Activating the CMOP Functionality](#task-6-activating-the-cmop-functionality)
The purpose of this Installation Guide is to provide the necessary steps for the successful install of the HIPAA NCPDP Connection for EDI Pharmacy.
The HIPAA NCPDP project consists of two phases, a dormant phase and an active phase. The BPS\*1.0 Master Build, released to the field in October 2004, was the dormant phase. This build included the installation of the new ECME 1.0 package and patches PSS\*1\*81, IB\*2\*223, IB\*2\*251, and PRCA\*4.5\*202. The BPS\*1.0 Master Build released the ECME V. 1.0 package in a dormant state but provided enhancements to Integrated Billing (IB) V. 2.0 so that the user was able to link pharmacy groups with insurance group plans. Additionally, the BPS\*1.0 Master Build enhanced Pharmacy Data Management V. 1.0 to allow over the counter (OTC) medications to be marked as third party billable and to allow each site to proceed with registering their pharmacy with the Financial Services Center (FSC). These modifications involved changes to software functionality within the Pharmacy Data Management V. 1.0 pharmacy application and to the Veterans Health Information Systems and Technology Architecture (VistA) IB V. 2.0, Accounts Receivable (AR) V. 4.5 and Vitria BusinessWare software.
This second release of the HIPAA NCPDP project provides functionality that will enable the HIPAA NCPDP functionality to go active. Specifically, this release will enable the capability of the VistA software applications to electronically transmit outpatient pharmacy prescription claims to payers. The functionality also includes receiving claim responses, which include Drug Utilization Reviews (DURs) and warnings, on a real-time basis and in accordance with Healthcare Insurance Portability and Accountability Act (HIPAA) Electronic Data Interchange (EDI) transactions and National Council for Prescription Drug Programs (NCPDP) mandated format standards, specifically NCPDP Telecommunication Standard V. 5.1. The patches included in this second release of the project are: BPS\*1\*1, PSO\*7\*148, IB\*2\*276, PSS\*1\*90, PSX\*2\*48, and PRCA\*4.5\*230. The first 3 patches in this list are contained in the ECME HIPAA NCPDP P3 1.0 Master Build (Multi-Build); and the subsequent patches are to be installed separately as stand-alone patches.
The intended audience for this document is the Information Resources Management Service (IRMS) staff, the Pharmacy staff responsible for installing and maintaining the Pharmacy files, and the Outpatient Pharmacy Electronic Claims Coordinator (OPECC) or Revenue staff responsible for maintaining Insurance files and IB parameters.
*(This page included for two-sided copying.)*

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of the HIPAA NCPDP Connection for EDI Pharmacy project is to introduce the ability to collect billing and clinical information within the prescription fill workflow process. This will be accomplished in two phases. The first phase (dormant) installed a dormant ECME V. 1.0 package, while allowing the users to link the pharmacy group with the insurance group plans within the IB V. 2.0 package. The sites were also able to proceed with registering their pharmacy with the FSC and to mark over the counter medications (OTC’s) as third party billable.

During the first phase (dormant), although the system was in a dormant state, these three significant configuration activities were performed:

1.  Registration – The process of registering VAMC Outpatient Pharmacies with the remote Vitria server located at the FSC in Austin, TX was completed.
2.  Insurance Matching – The process of linking Pharmacy groups with Insurance Plans was completed. This process was described in a separate document titled *e-Pharmacy Claims Insurance Process* with the filename IB_2_251_UM.PDF User Manual and was released in conjunction with the BPS\*1.0 Master Build. The *e-Pharmacy Claims Insurance Process* document is located on the VistA Documentation Library (VDL) at <http://www.va.gov/vdl>.
3.  The sites were given the ability to mark OTC items as third party billable.

This second (active) phase will now install an active ECME V. 1.0 real-time system, which will send claim data in a HIPAA compliant (NCPDP V. 5.1) format to a payer on a real-time basis and receive and process the claim responses in the appropriate manner. The claim transactions will be sent to Integrated Billing package; the DURs and warnings will be sent to the Outpatient Pharmacy V. 7.0 package and rejections will be sent to Outpatient Pharmacy Electronic Claims Coordinator (OPECC), who will then route rejections to the appropriate personnel for review. Infrastructure components at the FSC will process incoming ePharmacy claim data using Vitria, the National Health Care Insurance Database (NHCID) for transaction logging and the HIPAA EDI website to register Veterans Health Administration (VHA) pharmacies. These components also communicate with EMDEON (formerly WebMD) and third party payers for claims adjudication and return this information to VistA.

The following VistA applications have been modified and enhanced to create and process electronic claims using billing and applicable clinical data: ECME, Outpatient Pharmacy, Integrated Billing, CMOP, Pharmacy Data Management, and Accounts Receivable.

*(This page included for two-sided copying.)*

# Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME_HIPAA_NCPDP_P3.KID Master Build can only run with a standard MUMPS operating system. It requires the following Department of Veterans Affairs (VA) software packages.

|                                              |                            |
|----------------------------------------------|----------------------------|
| Package                                  | Minimum Version Needed |
|                                              |                            |
| VA FileMan                                   | 22.0                       |
| Kernel                                       | 8.0                        |
| Patient Information Management System (PIMS) | 5.3                        |
| National Drug File (NDF)                     | 4.0                        |
| Integrated Billing (IB)                      | 2.0                        |
| Accounts Receivable (AR)                     | 4.5                        |
| Pharmacy Data Management (PDM)               | 1.0                        |
| Order Entry/Results Reporting (OE/RR)        | 3.0                        |
| Outpatient Pharmacy                          | 7.0                        |
| Consolidated Mail Outpatient Pharmacy (CMOP) | 2.0                        |
| Health Level Seven (HL7)                     | 1.6                        |
| MailMan                                      | 8.0                        |
| Visit Tracking                               | 2.0                        |

*(This page included for two-sided copying.)*

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to the installation of the ECME HIPAA NCPDP P3 1.0 Master Build, it is imperative that the BPS\*1.0 Master Build, BPS_1_0.KID, be installed in your account and that your site complete the required insurance matching and registration steps. Consult the *HIPAA NCPDP Connection for EDI Pharmacy (Dormant Release) Installation Guide* on the VistA Documentation Library (VDL) for specific instructions on the installation and set up requirements associated with BPS_1_0.KID.

PSS, PSX, and PRCA patches are being released concurrently with the HIPAA NCPDP global project. These patches will have to be installed before the ECME HIPAA NCPDP P3 1.0 Master Build.

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before load and installation of ECME HIPAA NCPDP P3 1.0 active Master Build is performed.

Required patches for PSS\*1\*90:

PSS\*1\*82

PSS\*1\*87

Required patches for PSX\*2\*48:

PSX\*2\*57

Required patches for PRCA\*4.5\*230:

PRCA\*4.5\*202

PRCA\*4.5\*208

Required package release for BPS\*1\*1 (in the master build):

BPS 1.0 (host file BPS_1_0.KID)

Required patches for PSO\*7\*148 (in the master build):

PSX\*2\*48

PSO\*7\*159

PSO\*7\*161

PSO\*7\*174

PSS\*1\*90

PSO\*7\*196

PSO\*7\*207

PSO\*7\*209

PSO\*7\*210

PSO\*7\*213

PSO\*7\*219

PSO\*7\*235

Required patches for IB\*2\*276 (in the master build):

IB\*2\*51

IB\*2\*103

IB\*2\*137

IB\*2\*155

IB\*2\*183

IB\*2\*184

IB\*2\*199

IB\*2\*210

IB\*2\*211

IB\*2\*223

IB\*2\*225

IB\*2\*247

IB\*2\*249

IB\*2\*251

PRCA\*4.5\*230

IB\*2\*309

IB\*2\*317

## Exported Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several security keys are sent along with the software. The user may need one or multiple security keys assigned, depending on the level of access they are to be granted. A table with recommended Menu and Security Key assignments may be found on page 7 of the ECME User Manual (available at [www.va.gov/vdl](http://www.va.gov/vdl)).

| SECURITY KEY            | MENU OPTION                                                                                                       |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------|
| BPSMENU                     | ECME \[BPSMENU\]                                                                                                      |
| BPS USER                    | ECME User Screen \[BPS USER SCREEN\]                                                                                  |
| BPS MANAGER                 | Pharmacy ECME Manager Menu \[BPS MANAGER MENU\]                                                                       |
|                             | Statistics Screen \[BPS STATISTICS SCREEN\]                                                                           |
|                             | ECME transaction maintenance options \[BPS MENU MAINTENANCE\]                                                         |
|                             | View/Unstrand Claims Not completed \[BPS UNSTRAND SCREEN\]                                                            |
| BPS MASTER                  | Edit Basic ECME Parameters \[BPS SETUP BASIC PARAMS\]                                                                 |
|                             | Edit ECME Pharmacy Data \[BPS SETUP PHARMACY\]                                                                        |
|                             | Pharmacy ECME Setup Menu \[BPS SETUP MENU\]                                                                           |
|                             | Register Pharmacy with Austin Automation Center \[BPS SETUP REGISTER PHARMACY\]                                       |
| BPS REPORTS                 | Pharmacy Electronic Claims Reports \[BPS MENU RPT MAIN\]                                                              |
|                             | Claim Results and Status \[BPS MENU RPT CLAIM STATUS\] and all reports under this menu                                |
|                             | Other Reports \[BPS MENU RPT OTHER\] and all reports under this menu                                                  |
| IBCNR E-PHARMACY SUPERVISOR | Allows access to the multiple options used to match insurance plans and payer sheets (released with dormant version). |

## Global Growth

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the installation of the first Master Build, BPS_1_0.KID, several new BPS globals and one Integrated Billing global were added to the installer’s systems; however, no global growth occurred following the dormant release. The following estimates are provided as general examples of the extent to which these new globals may grow following the installation of the ECME HIPAA NCPDP P3 1.0 Master Build.

![](bps-1-1-ecme-hipaa-ncpdp-installation-guide/002.png)Keep in mind that the estimates will be affected by the number of claims that your site submits to the ECME package.

Electronic Claims Management Engine V. 1.0

^BPS - MOSTLY STATIC

^BPSC - VERY DYNAMIC – CONTINUAL GROWTH

^BPSCOMB - STATIC

^BPSECP - DYNAMIC – MINIMAL GROWTH

^BPSECX - DYAMIC – MINIMAL GROWTH

^BPSEI - STATIC

^BPSF - STATIC – MINIMAL GROWTH

^BPSR - VERY DYNAMIC - CONTINUAL GROWTH

^BPST – VERY DYNAMIC – CONTINUAL GROWTH

^BPSTL – VERY DYNAMIC – CONTINUAL GROWTH

Integrated Billing V. 2.0

^IBCNR - MOSTLY STATIC

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Pharmacy Data Management

The new multiple field, NDC BY OUTPATIENT SITE (#32), has been added to the DRUG file (#50) to store the latest NDC numbers that have been dispensed locally as well as by CMOP for a specific division:

32 NDC BY OUTPATIENT SITE

.01 -OUTPATIENT SITE

1 -LAST LOCAL NDC

2 -LAST CMOP NDC

The new field, DAW CODE (#81), has been added to the DRUG file (#50). Below are the possible values for this field. Upon installation, DAW Code values for each file 50 entry will be set to “0” – NO PRODUCT SELECTION INDICATED.

0 - NO PRODUCT SELECTION INDICATED

1 - SUBSTITUTION NOT ALLOWED BY PRESCRIBER

2 - SUBSTITUTION ALLOWED-PATIENT REQUESTED PRODUCT DISPENSED

3 - SUBSTITUTION ALLOWED-PHARMACIST SELECTED PRODUCT DISPENSED

4 - SUBSTITUTION ALLOWED-GENERIC DRUG NOT IN STOCK

5 - SUBSTITUTION ALLOWED-BRAND DRUG DISPENSED AS A GENERIC

6 - OVERRIDE

7 - SUBSTITUTION NOT ALLOWED-BRAND DRUG MANDATED BY LAW

8 - SUBSTITUTION ALLOWED-GENERIC DRUG NOT AVAILABLE IN MARKETPLACE

9 - OTHER

#### Outpatient Pharmacy 

The new multiple field REJECT INFO (#52.25) has been created in the PRESCRIPTION file (#52) to store information about Drug Utilization Review (DUR) and REFILL TOO SOON Rejects returned by 3rd party payers:

.01 NCPDP REJECT CODE

1 DATE/TIME DETECTED

2 PAYER MESSAGE

3 REASON

4 PHARMACIST

5 FILL NUMBER

6 GROUP NAME

7 PLAN CONTACT

8 PLAN PREVIOUS FILL DATE

9 STATUS

10 CLOSED DATE/TIME

11 CLOSED BY

12 CLOSE REASON

13 CLOSE COMMENTS

14 REASON FOR SERVICE CODE

15 PROFESSIONAL SERVICE CODE

16 RESPONSE ID

17 OTHER REJECTS

18 DUR TEXT

19 RESULT OF SERVICE CODE

20 INSURANCE NAME

21 GROUP NUMBER

22 CARDHOLDER ID

The field NDC (#4) under the CMOP EVENT multiple (#52.01) has been renamed to NDC RECEIVED.

A new field NDC SENT (#12) is being created under the CMOP EVENT multiple

(#52.01) in order to store the NDC sent to CMOP during the CMOP transmission.

*(This page included for two-sided copying.)*

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An overview of the functionality changes resulting from the installation of the ECME HIPAA NCPDP P3 1.0 Master Build is provided in the *HIPAA NCPDP Connection for EDI Pharmacy (Active Release) Release Notes* in the VistA Documentation Library at [http://vista.med.va.gov/vdl.](http://vista.med.va.gov/vdl)

*(This page included for two-sided copying.)*

# Installation StepsIT IS VERY IMPORTANT THAT THESE INSTRUCTIONS ARE FOLLOWED STEP BY STEP IN THE EXACT ORDER INDICATED BELOW. ONCE STARTED, THE INSTALLATION NEEDS TO BE COMPLETED. FAILURE TO FULLY COMPLETE THE INSTALLATION (ONCE STARTED) WILLLIKELY CAUSE PROBLEMS FOR USERS OF THE 6 APPLICATIONS INVOLVED IN THIS PROJECT.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BEFORE PROCEEDING, please read item number 12.2 and make sure you have the

information needed in order to complete this installation.

Users should not be on the system during installation of these patches. These

patches should be installed during non-peak hours to avoid disruptions.

Installation should take approximately 15 minutes.

Notes: 1. You cannot queue this installation for a later time, because you

will be prompted to enter information during the installation.

2\. DO NOT install patch PSX\*2\*48 when prescriptions are being

transmitted to CMOP. Wait for the CMOP transmission to finish or

complete the installation before the transmission starts.

3\. For existing test sites, stop the BPS NCPDP logical link. Turn off

the logical link using the Start/Stop Links \[HL START\] option, which

is on the Filer and Link Management Options option \[HL MENU FILER

LINK MGT\] submenu of the HL7 Main Menu \[HL MAIN MENU\] option. When

prompted for the HL LOGICAL LINK NODE, enter BPS NCPDP and when

asked whether it is "Okay to shut down this job?", enter YES.

1\. These patches will be sent to your system upon release from the National

Patch Module:

\- Patch PSS\*1\*90

\- Patch PSX\*2\*48

\- Patch PRCA\*4.5\*230

Obtain the host file ECME_HIPAA_NCPDP_P3.KID, which contains the following

three KIDS build distributions:

PSO\*7.0\*148

BPS\*1.0\*1

IB\*2.0\*276

Sites may retrieve the host file in one of the following ways:

1.1 The preferred method is to FTP the file from REDACTED,

which will transmit the file from the first available FTP server.

1.2 Sites may also elect to retrieve the file directly from a specific

server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

2\. From the Kernel Installation and Distribution System (KIDS) Menu, select

the Installation menu.

3\. From this menu, for each of the three patches (PSS\*1\*90, PSX\*2\*48 and

PRCA\*4.5\*230), you may select to use the following options:

3.1. Backup a Transport Global - this option will create a backup message

of any routines exported with the patch. It will NOT backup any other

changes such as Data Dictionaries (DDs) or templates.

3.2. Compare Transport Global to Current System - this option will allow

you to view all changes that will be made when the patch is

installed. It compares all components of the patch (routines, DDs,

templates, etc.).

3.3. Verify Checksums in Transport Global - this option will ensure the

integrity of the routines that are in the transport global.

> **NOTE:** When prompted for INSTALL NAME, you should enter the corresponding

names for each patch as shown below:

PATCH INSTALL NAME

-----------------------------------

PSS\*1\*90 PSS\*1.0\*90

PSX\*2\*48 PSX\*2.0\*48

PRCA\*4.5\*230 PRCA\*4.5\*230

4\. From the Installation menu, select the Install Package(s) option and for

each one of the three patches (PSS\*1\*90, PSX\*2\*48 and PRCA\*4.5\*230) follow

the instructions below:

4.1. When prompted for the "Select INSTALL NAME:", enter the corresponding

name for the patch you are installing (see table above).

4.2. When prompted "Want KIDS to INHIBIT LOGONs during the install?

YES//", respond "NO."

4.3. When prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? YES//", respond "NO."

4.4. When prompted, "Device: Home//" respond with the correct device and

DO NOT queue to P-Message.

5\. After the installation of the 3 patches is complete (PSS\*1\*90, PSX\*2\*48,

PRCA\*4.5\*230), return to the Kernel Installation and Distribution System

(KIDS) Menu, select the Installation menu.

6\. From the Installation menu, select the Load a Distribution option.

7\. When prompted for "Enter a Host File:", enter the full directory path

where you saved the host file ECME_HIPAA_NCPDP_P3.KID (e.g.,

SYS\$SYSDEVICE:\[ANONYMOUS\]ECME_HIPAA_NCPDP_P3.KID).

8\. When prompted for "OK to continue with Load? NO//", enter "YES."

The following will display:

Loading Distribution...

ECME HIPAA NCPDP P3 1.0

BPS\*1.0\*1

PSO\*7.0\*148

IB\*2.0\*276

Use INSTALL name ECME HIPAA NCPDP P3 1.0 to install this Distribution.

9\. From the Installation menu, you may select to use the following options:

(when prompted for "Select INSTALL NAME:", enter "ECME HIPAA NCPDP P3

1.0")

9.1. Backup a Transport Global - this option will create a backup message

of any routines exported with the patch. It will NOT backup any other

changes such as Data Dictionaries (DDs) or templates.

9.2. Compare Transport Global to Current System - this option will allow

you to view all changes that will be made when the patch is

installed. It compares all components of the patch (routines, DDs,

templates, etc.).

9.3. Verify Checksums in Transport Global - this option will ensure the

integrity of the routines that are in the transport global.

10\. Back in the Installation menu, select the Install Package(s) option.

11\. When prompted for the "Select INSTALL NAME:", enter "ECME HIPAA NCPDP P3

1.0."

12\. For each one of the builds contained in the master build, the following

set of prompts will be asked:

> **NOTE:** Information such as the example below about files contained in the

build will be displayed for each KIDS build that contains Data

Dictionary changes:

Incoming Files:

52 PRESCRIPTION (Partial Definition)

> **NOTE:** You already have the 'PRESCRIPTION' File.

12.1. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of

Install? Yes//". For the builds PSO\*7.0\*148 and IB\*2.0\*276, respond

"NO." For the BPS\*1.0\*1 build, respond "YES."

12.2. For the BPS\*1.0\*1 installation, when prompted for Incoming Mail

Groups:

"Enter the Coordinator for Mail Group 'BPS OPECC':"

Please, contact your Medical Care Cost Recovery (MCCR) business

department prior to installation to determine who will be the

coordinator for this new mail group. This mail group will be used

by the BPS Nightly Background Job. Its members will receive

bulletins about electronic claims.

13\. When prompted "Want KIDS to INHIBIT LOGONs during the install? YES//",

respond "NO."

14\. When prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? YES//", respond "NO."

15\. When prompted, "Device: Home//" respond with the correct device and DO NOT

queue this to P-Message.

16\. TEST SITES ONLY: A post-installation step for test sites is to restart the BPS NCPDP

Logical link. To turn on the logical link use the Start/Stop Links

\[HL START\] option, which is on the Filer and Link Management Options

option \[HL MENU FILER LINK MGT\] submenu of the HL7 Main Menu

\[HL MAIN MENU\] option. When prompted for the HL LOGICAL LINK NODE

Enter “BPS NCPDP” and that will enable the logical link.

17\. The functionality will be implemented at sites in a phased schedule. Before performing the steps to activate ePharmacy functionality (described in the Activation Steps section), all non-test sites should wait to be contacted by the Chief Business Office (CBO).

*(This page included for two-sided copying.)*

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Re-register the Site and Pharmacies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the installation has completed, the IRMS installer should contact the Pharmacy Automated Data Processing Application Coordinator (ADPAC) and the Outpatient Pharmacy Electronic Claims Coordinator (OPECC) to re-register the site. This step must occur for the automation registration process to continue working.

The site’s Pharmacy ADPAC performs this step. All sites have already registered via this option as part of the HIPAA GLOBAL dormant release (BPS\*1\*0). However, this process needs to be repeated for this release in order to synchronize the version number between your site and the Austin Automation Center (AAC). The site and pharmacy registration data that was entered via the initial or subsequent registrations does not need to be updated unless some of the information is found to be inaccurate or outdated. At the end of the option, the Pharmacy ADPAC must send the registration messages by entering 'YES' at the 'SEND APPLICATION REGISTRATION: Y/N ?' prompt.

To register, the ADPAC will use the *Register Pharmacy with Austin Automation Center* \[BPS SETUP REGISTER PHARMACY\] option. This option can be found under the *Pharmacy ECME Setup Menu* \[BPS SETUP MENU\] under the *Pharmacy ECME Manager Menu* \[BPS MANAGER MENU\]. For more detailed information on executing this option, please refer to post installation steps 4 and 5 in the Installation Guide for the HIPAA GLOBAL dormant release (BPS_1_0_IG).

Note that the registration process uses the EPHARM OUT logical link so please be sure that this link is running via the HL7 options. If the communication is not successful or you have questions concerning the success of the communication, please seek assistance from your Systems Manager responsible for the HL7 package.

Below is an example of registering the site and current pharmacy using the data that was entered during the initial registration. As previously indicated, only data that is inaccurate needs to be updated. Be sure to enter YES at the SEND APPLICATION REGISTRATION: Y/N ? prompt.

  
Example: Registering pharmacy with AAC

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.1\*

\* VA HEARTLAND - WEST, VISN 15 \*

\* Main Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

U ECME User Screen

MGR Pharmacy ECME Manager Menu ...

RPT Pharmacy Electronic Claims Reports ...

Select \<V15 West\> ECME Option: MGR Pharmacy ECME Manager Menu

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.1\*

\* VA HEARTLAND - WEST, VISN 15 \*

\* Pharmacy ECME Manager Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

MNT ECME transaction maintenance options ...

SET Pharmacy ECME Setup Menu ...

STAT Statistics Screen

Select \<V15 West\> Pharmacy ECME Manager Menu Option: SET Pharmacy ECME Setup Menu

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.1\*

\* VA HEARTLAND - WEST, VISN 15 \*

\* Pharmacy ECME Setup Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

BAS Edit Basic ECME Parameters

PHAR Edit ECME Pharmacy Data

REG Register Pharmacy with Austin Automation Center

Select \<V15 West\> Pharmacy ECME Setup Menu Option: REG Register Pharmacy with Austin Automation Center

ENTER/VERIFY SITE REGISTRATION DATA.

PRIMARY SITE CONTACT DATA.

VA SITE CONTACT: USER, ONE//

OFFICE PHONE: 111-111-1111//

EMAIL ADDRESS: ONE.USER@MED.VA.GOV

Replace

ALTERNATE SITE CONTACT DATA.

VA Alternate Site Contract: USER, TWO//

OFFICE PHONE: 111-111-1112//

EMAIL ADDRESS:TWO.USER@MED.VA.GOV

Replace

-- APPLICATION REGISTRATION VALIDATION RESULTS. --

DOMAIN NAME - Required - VALID: EPHARMACY.VITRIA-EDI.AAC.VA.GOV

TCP/IP ADDRESS FOR "EPHARM OUT" - Required - VALID: REDACTED

"EPHARM OUT" PORT NUMBER - Required - VALID: 5105

SITE NUMBER - Required - VALID: 605

INTERFACE VERSION - Required - VALID: 2

CONTACT NAME - VALID: USER^ONE^^^^

CONTACT MEANS - VALID: ^NET^INTERNET^ONE.USER@MED.VA.GOV^^^^^^111-111-1111

ALTERNATE CONTACT NAME - VALID: USER2^TWO^^^^

ALTERNATE CONTACT MEANS - VALID: ^NET^INTERNET^TWO.USER@MED.VA.GOV^^ ^^^^111-111-1112

-- APPLICATION REGISTRATION DATA VALID. --

Enter RETURN to continue or '^' to exit:

ENTER/VERIFY PHARMACY REGISTRATION DATA.

PHARMACY SPECIFIC DATA.

Select BPS PHARMACIES NAME:

APPLICATION REGISTRATION DATA IS VALID.

PHARMACY REGISTRATION DATA IS:

VALID for PHARMACY1 and will be transmitted.

VALID for PHARMACY2 and will be transmitted.

SEND APPLICATION REGISTRATION: Y/N ? YES

APPLICATION REGISTRATION SUBMITTED.

Press RETURN to continue...

*(This page included for two-sided copying.)*

# Activation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The activation steps should be coordinated between Pharmacy Service, Billing, the OPECC, and the IRMS staff. Pharmacy and Billing each have access to a site parameter and the OPECC needs to know when the activation steps are completed. IRMS staff has access to the HL7 module. Follow these instructions carefully to correctly turn on the appropriate switches activating electronic third party prescription billing.

To activate the ECME functionality, the following tasks must be performed.

1)  The first task is to configure the HL7 module. This is to be completed by IRMS staff.
2)  The second task is to match the outpatient site(s) in the OUTPATIENT SITE file (#59) with the appropriate pharmacy in the BPS PHARMACIES file (#9002313.56). If an Outpatient Site is not assigned to a BPS Pharmacy, that BPS pharmacy will not actively generate claims. This will be completed by the Pharmacy Service.
3)  The third task is to turn on the insurance switch in the Integrated Billing package. This will be completed by Billing.
4)  The fourth task is to activate the VA Plans to which you wish to start sending electronic claims (you may want to turn these VA Plans on 1 or 2 at a time). This will be completed by Billing.
5)  The fifth task is to schedule the BPS Nightly Background Job.

Once all five of these tasks are completed, the window fill process will trigger third party insurance claims for patients who have prescription insurance coverage for the plans you have activated for electronic submission.

The final task in the process is to activate the CMOP functionality; however, this task should not be performed until your site is satisfied that the ECME window fill functionality is performing to expectations. Once the decision is made to activate the CMOP functionality, task 5 should be completed.

## Task 1 – Configure the VistA HL7 Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Setting Up the ECME HL7 Application Parameters

The ECME VISTA and VITRIA NC application parameters should automatically be installed and set up during the installation process. Please follow the directions below to update the application parameter settings. If the application parameters are not configured correctly, ECME claims will be rejected.

  
To verify the ECME VISTA application parameter:

1.  From the HL7 Main Menu, select Interface Developer Options.
2.  Select the Application Edit option (EA).
3.  At the HL7 Application Parameter Name: prompt, enter ECME VISTA.
4.  If there is any data in the Facility Name field, remove the data
5.  File the changes (Save and Exit)

To verify the VITRIA NC application parameter:

1.  From the HL7 Main Menu, select Interface Developer Options.
2.  Select the Application Edit option (EA).
3.  At the HL7 Application Parameter Name: prompt, enter VITRIA NC.
4.  If there is any data in the Facility Name field, remove the data.
5.  File the changes (Save and Exit)

Example: ECME VISTA HL7 Application Parameter Edit Screen

HL7 APPLICATION EDIT

--------------------------------------------------------------------------------

NAME: ECME VISTA ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: COUNTRY CODE: US

HL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ~^\\

MAIL GROUP:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

Setting Up the BPS NCPDP Logical Link

The BPS NCPDP link will automatically be installed and set up during the installation of the BPS_1_1.KID Master Build. Please follow the directions below to check the HL7 system monitor and confirm that the BPS NCPDP link is installed correctly.

  
To set up the BPS NCPDP Logical Link:

1.  From the HL7 Main Menu select, Interface Developer Options.
2.  Select the option, EL Link Edit.
3.  Select the BPS NCPDP Logical Link Node.
4.  Set the AUTOSTART field to Enabled.
5.  Accept the default LLP TYPE, which is TCP, by pressing the \<Enter\> key. This will take you to the TCP Lower Level Parameters.
6.  Enter REDACTED for the TCP/IP Address.
7.  Enter REDACTED for the TCP/IP port number.
8.  Set the Persistent field to NO

Example: Setting the BPS NCPDP Logical Link

HL7 LOGICAL LINK

--------------------------------------------------------------------------------

NODE: BPS NCPDP

INSTITUTION:

DOMAIN:

AUTOSTART: Enabled

QUEUE SIZE: 10

LLP TYPE: TCP \<ENTER\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND:

HL7 LOGICAL LINK

--------------------------------------------------------------------------------

┌──────────────────────TCP LOWER LEVEL PARAMETERS─────────────────────────┐

│ BPS NCPDP │

│ │

│ TCP/IP SERVICE TYPE: CLIENT (SENDER) │

│ TCP/IP ADDRESS: REDACTED │

│ TCP/IP PORT: REDACTED│

│ │

│ ACK TIMEOUT: 270 RE-TRANSMISSION ATTEMPTS: 3 │

│ READ TIMEOUT: 27 EXCEED RE-TRANSMIT ACTION: │

│ BLOCK SIZE: SAY HELO: NO │

│ │

│STARTUP NODE: PERSISTENT: NO │

│ RETENTION: 50 UNI-DIRECTIONAL WAIT: │

└─────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

Validate the HL7 System Monitor is Active/Working for the BPS NCPDP ePharmacy Link

The site’s IRMS personnel perform this step. The following steps will verify that the HL7 link has been successfully configured.

Start the New HL7 Logical Link

During this step, you will validate the link is operating correctly. Summarizing, during this step you will:

1.  Use the *Systems Link Monitor* option to confirm that the Link Manager is running.
2.  Use the *Systems Link Monitor* option to confirm that the BPS NCPDP logical link is enabled.
3.  Turn on this new logical link using the *Start/Stop Links* \[HL START\] option.

> When asked to identify whether the BPS NCPDP logical link should be started in the background, accept the default of background.

Steps for Validating the HL7 Logical Link:

1.  Once a third party prescription has gone through the pharmacy system, you can check the HL7 system monitor to see if there have been any messages sent out on the BPS NCPDP logical link. There should be one or more messages in the BPS NCPDP link. If no messages are being sent by the BPS NCPDP link, then confirm that the HL7 logical link settings for the BPS NCPDP have been entered as previously instructed and ensure that the link is enabled and running.
2.  The normal states for each link should be idle, reading, or active. The following screen print example show the BPS NCPDP logical link that has processed multiple ECME claims and associated responses.

  
Example: HL7 Systems Link Monitor

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

SYSTEM LINK MONITOR for ALBANY (P System)

MESSAGES MESSAGES MESSAGES MESSAGES DEVICE

NODE RECEIVED PROCESSED TO SEND SENT TYPE STATE

EPHARM O 4 4 4 4 NC Shutdown

LL2VISN 70 70 86 70 NC Open

NPTF 0 0 26 0 N Halting

PSO LLP1 2 N Halting

BPS NCPDP 176 176 176 176 PC Idle

PSOTPBAA 38 38 40 38 NC Enabled

Incoming filers running =\> Zero TaskMan running

Outgoing filers running =\> Zero Link Manager running

Monitor current \[next job 0.2 hr\]

Select a Command:

(N)EXT (B)ACKUP (A)LL LINKS (S)CREENED (V)IEWS (Q)UIT (?) HELP:

> Third party billable prescriptions that meet the criteria for electronic transmission should now be submitting to the ECME package. If the correct links are not running or there are any questions, please contact Enterprise VistA Support (EVS) for assistance by either submitting a Remedy Ticket (under the CTI of Applications-Vista/Electronic Claims Management Engine/Logical Link Issue) or by contacting the help desk (800-596-4357) to log a ticket for you.

## Task 2 – Matching the Outpatient Site to the BPS PHARMACIES file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Note that the user must have security key BPS MASTER to run this option.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.1\*

\* VA HEARTLAND - WEST, VISN 15 \*

\* Main Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

U Claims Data Entry Screen

MGR Pharmacy ECME Manager Menu ...

RPT Pharmacy Electronic Claims Reports ...

Select \<V15 West\> ECME Option: MGR Pharmacy ECME Manager Menu

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.1\*

\* VA HEARTLAND - WEST, VISN 15 \*

\* Pharmacy ECME Manager Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

MNT ECME transaction maintenance options ...

SET Pharmacy ECME Setup Menu ...

STAT Statistics Screen

Select \<V15 West\> Pharmacy ECME Manager Menu Option: SET Pharmacy ECME Setup Menu

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.1\*

\* VA HEARTLAND - WEST, VISN 15 \*

\* Pharmacy ECME Setup Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

BAS Edit Basic Pharmacy ECME Parameters

PHAR Edit Pharmacy ECME Pharmacy Data

REG Register Pharmacy with Austin Automation Center

Select \<V15 West\> Pharmacy ECME Setup Menu Option: PHAR Edit Pharmacy ECME Pharmacy Data

Select BPS PHARMACIES NAME: TOP

1 TOPEKA

2 TOPEKACBOC

CHOOSE 1-2: 1 TOPEKA

OUTPATIENT SITE: One or more of the VistA pharmacy package's

Outpatient Sites (File 59) must be associated with

this ECME pharmacy entry

Select OUTPATIENT SITE: TOPEKA

OUTPATIENT SITE: TOPEKA// \<ENTER\>

## Task 3 – Turning On the Insurance Switch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user must have security key IBCNR E-PHARMACY SUPERVISOR to run this option. The Edit HIPAA NCPDP Flag found on the e-Pharmacy Menu in the IB package is the main switch for e-Pharmacy transmissions. This switch must be active for electronic transmissions to leave your station. This works in combination with the Pharmacy service having Outpatient Pharmacy sites linked to the BPS Pharmacy and IB having VA Plans activated (explained in Task 4).

IBCNR E-PHARMACY MENU e-Pharmacy Menu

ECMP ECME CMOP Report

EHNF Edit HIPAA NCPDP FLAG

ENP Edit NCPDP PROCESSOR APPLICATION Sub-file

EPAY Edit PAYER APPLICATION Sub-file

EPBM Edit PBM APPLICATION Sub-file

EPLA Edit PLAN APPLICATION Sub-file

EVNT ECME Billing Events Report

MGP Match Group Plan to a Pharmacy Plan

MMGP Match Multiple Group Plans to a Pharmacy Plan

MTPS Match Test Payer Sheet to a Pharmacy Plan

RGPW Group Plan Worksheet Report

RPP Pharmacy Plan Report

Select \<V15 West\> e-Pharmacy Menu Option: EHNF Edit HIPAA NCPDP FLAG

Edit HIPAA NCPDP ACTIVE FLAG

(master switch to control e-Pharmacy NCPDP transactions)

350.9 IB SITE PARAMETERS File

11.01 HIPAA NCPDP ACTIVE FLAG Field

HIPAA NCPDP ACTIVE FLAG: Inactive// Active

## Task 4 – Activating VA Plans for Electronic Submission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user must have security key IBCNR E-PHARMACY SUPERVISOR to run this option. The individual VA Plans will need to be activated as you make the decision to start sending electronic e-Pharmacy claims to those payers. It is recommended that you start activating the VA Plans 1 or 2 at a time until you are sure transmissions are leaving and returning to your station accurately.

EHNF Edit HIPAA NCPDP FLAG

ENP Edit NCPDP PROCESSOR APPLICATION Sub-file

EPAY Edit PAYER APPLICATION Sub-file

EPBM Edit PBM APPLICATION Sub-file

EPLA Edit PLAN APPLICATION Sub-file

EVNT ECME Billing Events Report

MGP Match Group Plan to a Pharmacy Plan

MMGP Match Multiple Group Plans to a Pharmacy Plan

MTPS Match Test Payer Sheet to a Pharmacy Plan

PSI Group Plan Status Inquiry

PSR Group Plan Status Report

RGPW Group Plan Worksheet Report

RPP Pharmacy Plan Report

Select e-Pharmacy Menu Option: EPLA Edit PLAN APPLICATION Sub-file

Select Plan ID: VA103275 PRIME HOSPITALITY CORP. 600428 01062937

Plan ID: VA103275

Date/Time Created: FEB 14, 2004@16:42:37

Plan Name: PRIME HOSPITALITY CORP.

Plan Name - Short: 01062937

Payer Name:

Type:

Region: CT

Pharmacy Benefits Manager (PBM) Name: RX PRIME CIGNA

Banking Identification Number (BIN): 600428

Processor Control Number (PCN): 01062937

NCPDP Processor Name: ARGUS

Enabled?: Yes

Software Vendor ID:

Billing Payer Sheet Name: ARGUSV5

Reversal Payer Sheet Name: ARGB2V5

Rebill Payer Sheet Name:

Maximum NCPDP Transactions: 4

Test Billing Payer Sheet Name:

Test Reversal Payer Sheet Name:

Test Rebill Payer Sheet Name:

Press Enter / Return to continue:

Application: E-PHARM

Date/Time Created: FEB 15, 2004@14:43:30

Deactivated? Yes

Date/Time Deactivated: DEC 23, 2004@16:42:43

National Active? Not Active

Date/Time National Edited: DEC 23, 2004@16:42:43

Local Active? Inactive

Date/Time Local Edited:

User Edited Local:

VA103275 - Local Active?: Inactive// ACTIVE

## Task 5 – Schedule the BPS Nightly Background Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BPS nightly background job does various maintenance tasks for ECME. This should be scheduled during a non-peak processing time. One of the main tasks for this job is to send reversals to payer for payable claims that have not been released within the number of day specified in the *Edit Pharmacy ECME Pharmacy Data* option. Since this involves sending HL7 claims to the payer, it is recommended that this job not be scheduled when there is excessive HL7 processing being performed by other applications, especially CMOP.

1.  From the *Taskman Management* menu, select *Schedule/Unschedule Options*.
2.  Schedule the option *BPS NIGHTLY BACKGROUND JOB*.
3.  Select the time the option should run (during non-peak hours).
4.  Set the "Rescheduling Frequency" to 1D (once a day).

Example: Scheduling the ePharmacy Nightly Background Job

Edit Option Schedule

Option Name: BPS NIGHTLY BACKGROUND JOB

Menu Text: BPS NIGHTLY BACKGROUND JOB TASK ID: 1624

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: MAY 2,2006@02:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

## Task 6 – Activating the CMOP Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](bps-1-1-ecme-hipaa-ncpdp-installation-guide/003.png)Prior to activating the CMOP functionality, sites should allow the window fill functionality, described earlier in tasks 1, 2, 3, and 4 to be active for a period of time.

> Once your site is satisfied that the ECME window fill functionality is performing to expectations, then the decision can be made to turn on the CMOP functionality for ECME processing. Note: CMOP must be turned on for each BPS pharmacy in order for the CMOP prescriptions to be electronically billed.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* VA HEARTLAND - WEST, VISN 15 \*

\* Main Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

U Claims Data Entry Screen

MGR Pharmacy ECME Manager Menu ...

RPT Pharmacy Electronic Claims Reports ...

Select \<V15 West\> ECME Option: MGR Pharmacy ECME Manager Menu

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.1\*

\* VA HEARTLAND - WEST, VISN 15 \*

\* Pharmacy ECME Manager Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

MNT ECME transaction maintenance options ...

SET Pharmacy ECME Setup Menu ...

STAT Statistics Screen

Select \<V15 West\> Pharmacy ECME Manager Menu Option: SET Pharmacy ECME Setup Menu

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.1\*

\* VA HEARTLAND - WEST, VISN 15 \*

\* Pharmacy ECME Setup Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

BAS Edit Basic Pharmacy ECME Parameters

PHAR Edit Pharmacy ECME Pharmacy Data

REG Register Pharmacy with Austin Automation Center

Select \<V15 West\> Pharmacy ECME Setup Menu Option: PHAR Edit Pharmacy ECME Pharmacy Data

Select \<V15 West\> Pharmacy ECME Manager Menu Option: PHAR Edit Pharmacy ECME Pharmacy Data

Select BPS PHARMACIES NAME: TOPEKA

1 TOPEKA

2 TOPEKACBOC

CHOOSE 1-2: 1 TOPEKA

OUTPATIENT SITE: One or more of the VistA pharmacy package's

Outpatient Sites (File 59) must be associated with

this ECME pharmacy entry

Select OUTPATIENT SITE: TOPEKA

OUTPATIENT SITE: TOPEKA// \<ENTER\>

Select OUTPATIENT SITE: \<ENTER\>

NCPDP \#: 1712884// \<ENTER\>

CMOP SWITCH: CMOP OFF// 1

DEFAULT DEA \#: AG123456// ^

All CMOP third party billable prescriptions should now be submitting to the ECME package. If the correct links are not running or there are any questions, please contact Enterprise VistA Support (EVS) for assistance by either submitting a Remedy Ticket yourself (under the CTI of Applications-Vista/Electronic Claims Management Engine/CMOP Issue) or by contacting the help desk (800-596-4357) to log a ticket for you.