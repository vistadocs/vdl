---
title: BPS Version 1 (Dormant Release) Release Notes
doc_type: RN
doc_label: Release Notes
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
description: - [Project Overview](#project-overview) - [The New ECME V. 1.0 Package](#the-new-ecme-v-10-package) - [Pharmacy Data Management V. 1.0, IB V. 2.0, and AR V. 4.5](#pharmacy-data-management-v-10-ib-v-20-and-ar-v-45) - [Pre-Installation Issues](#pre-installation-issues) The Healthcare Insurance Portabi
audience: 
keywords: 
  - pharmacy
  - ecme
  - ncpdp
  - hipaa
  - installation
  - claims
  - table
  - contents
  - management
  - build
page_count: 0
word_count: 1176
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/bps_1_0_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/bps_1_0_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=141"
---

> ![](bps-version-1-dormant-release-release-notes/001.png)

HIPAA NCPDP Connection for EDI Pharmacy(Dormant Release)

####### RELEASE NOTES

BPS\*1.0

PSS\*1\*81

IB\*2.0\*223

IB\*2.0\*251

PRCA\*4.5\*202

October 2004

V*IST*A System Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Project Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Project Overview](#project-overview)
- [The New ECME V. 1.0 Package](#the-new-ecme-v-10-package)
- [Pharmacy Data Management V. 1.0, IB V. 2.0, and AR V. 4.5](#pharmacy-data-management-v-10-ib-v-20-and-ar-v-45)
- [Pre-Installation Issues](#pre-installation-issues)
The Healthcare Insurance Portability and Accountability Act (HIPAA) National Council for Prescription Drug Programs (NCPDP) Connection for Electronic Data Interchange (EDI) Pharmacy project, commonly referred to as HIPAA NCPDP, is a collection of upgrades to Pharmacy Data Management V. 1.0, Integrated Billing (IB) V. 2.0, and Accounts Receivable (AR) V. 4.5 Veterans Health Information Systems and Technology Architecture (V*IST*A) software packages and a release for the new Electronic Claims Management Engine (ECME) V. 1.0 V*IST*A package. The goal of the HIPAA NCPDP project is to allow the V*IST*A software applications to electronically transmit outpatient pharmacy prescription claims to payers. It will also receive claim responses (which include drug utilization responses and warnings) on a real-time basis and in accordance with HIPAA NCPDP mandated format standards, specifically NCPDP Telecommunication Standard V. 5.1.
This project consists of two phases, a dormant phase and an active phase. This BPS\*1.0 Master Build is the dormant phase, releasing the ECME V. 1.0 package (which occupies the BPS namespace) in a dormant state. Although the ECME V. 1.0 package’s functionality is dormant in this first release, Integrated Billing (IB) V. 2.0 is enhanced in this build, so that the user will be able to link pharmacy groups with insurance group plans in this phase. Also, each site must proceed with registering their pharmacy with the Financial Services Center (FSC).
The active phase, which will be released later, allows the ECME V. 1.0 package to produce electronic claims. These changes will allow the V*IST*A software applications to electronically transmit outpatient pharmacy prescription claims to payers. It will also receive claim responses (which include drug utilization responses and warnings) on a real-time basis and in accordance with HIPAA EDI transactions and NCPDP mandated format standards, specifically NCPDP Telecommunication Standard V. 5.1.
This BPS\*1.0 Master Build includes the installation of the new ECME V. 1.0 package and Patches PSS\*1\*81, IB\*2\*223, IB\*2\*251, and PRCA\*4.5\*202. Together, these patches provide the functionality to:
> • Capture all data elements required to submit a billable third party claim.
> • Use the NCPDP V. 5.1 standard to formulate the Pharmacy billing transactions.
> • Provide a new Electronic Claims Management Engine (ECME) V. 1.0 package that will generate electronic claims in NCPDP V. 5.1 format based on the Outpatient Pharmacy V. 7.0 workflow.
> • Establish Application Programming Interfaces (API’s) for communication between Integrated Billing and Pharmacy/ECME V. 1.0.
> • Establish communication protocols to submit the claims for payment in real-time mode.
> • Store the response messages into a data file for use by future iterations of this project.
- Provide reports and methods for the correction of erroneous data by the claim’s coordinator.
> **IMPORTANT:** Sites should not expect activation of the ability to submit third party claims when this first Master Build, BPS\*1.0, is loaded. Sites must install the first build and perform the steps outlined in the *HIPAA NCPDP Connection for EDI Pharmacy (Dormant Release) Installation Guide* and then install the second Master Build (once it is released at a later date) before the functionality enabling electronic claim submission to payers will become active.
Vital instructions are provided in the *HIPAA NCPDP Connection for EDI Pharmacy (Dormant Release) Installation Guide* concerning:
- What menu options and security keys should be assigned to allow registration and insurance matching.
- How to register a pharmacy with the FSC.
- How to check the Health Level 7 Standard (HL7) Systems Link Monitor.

# The New ECME V. 1.0 Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Administration (VHA) developed the ECME V. 1.0 software in order to comply with the Health Insurance Portability and Accountability Act of 1996, which requires health care providers to electronically transmit outpatient pharmacy prescription claims to payers in the NCPDP format and to receive responses on a real-time basis. ECME V. 1.0 is derived from the Pharmacy Point of Sale V. 1.0 (POS) application developed by the Indian Health Service (IHS).

The new ECME V. 1.0 real-time system sends claim data in a HIPAA compliant NCPDP V. 5.1 format to a payer on a real-time basis and receives and processes the claim responses in the appropriate manner.

ECME V. 1.0 generates electronic claims in NCPDP V. 5.1 format based on the Outpatient Pharmacy V. 7.0 workflow and performs the following tasks:

- Allows pharmacy users to submit, resubmit, and reverse electronic claims.
- Provides reports for end users and management on claims status, transaction history, and system configuration standings.
- Allows Automated Data Processing Application Coordinator (ADPAC) and Information Resources Management Service (IRMS) staff to configure ECME V. 1.0 to pharmacy site specifications.

ECME V. 1.0 processing begins when events within Outpatient Pharmacy V. 7.0 meet specific criteria that indicate the system should generate an electronic claim. To build a claim through ECME V. 1.0, the patient must be registered, have pharmacy insurance coverage, and have a prescription for a non-service connected condition in process.

Logic embedded within ECME V. 1.0 manages the creation of the electronic claim, which requires integration with Integrated Billing (IB) V. 2.0, Pharmacy Data Management V. 1.0, and the National Drug File (NDF) V. 4.0. ECME V. 1.0 also generates claims during Consolidated Mail Outpatient Pharmacy (CMOP) V. 2.0 processing for prescriptions that meet billing requirements and are suspended for CMOP fills.

*(This page included for two-sided copying.)*

# Pharmacy Data Management V. 1.0, IB V. 2.0, and AR V. 4.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Existing V*IST*A applications Pharmacy Data Management V. 1.0, IB V. 2.0, and AR V. 4.5, are modified or enhanced as necessary to create electronic claims using billing and applicable clinical information. The information to be collected will consist of data currently available within the Outpatient Pharmacy V. 7.0, Patient Information Management System (PIMS) V. 5.3, and IB V. 2.0 applications.

Infrastructure components at the Austin Automation Center (AAC) process incoming claim data using Vitria BusinessWare V. 3.1.7 (Vitria), the National Health Care Insurance Database (NHCID) for transaction logging, and the HIPAA EDI website to register VHA pharmacies. These components also communicate with WebMD and third party payers for claims adjudication and return this information to V*IST*A.

*(This page included for two-sided copying.)*

# Pre-Installation Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** Failure to carefully follow the instructions provided in the *HIPAA NCPDP Connection for EDI Pharmacy (Dormant Release) Installation Guide* can result in failure of the BPS\*1.0 Master Build to install correctly.

Correct pre-installation set up is imperative to the successful installation of this build. Prior to installation of the BPS\*1.0 Master Build, each site will need to check that the required patches listed in the *HIPAA NCPDP Connection for EDI Pharmacy (Dormant Release) Installation Guide* have been installed.

Before installing the BPS\*1.0 Master Build, the domain EPHARMACY.VITRIA-EDI.AAC.VA.GOV <u>must</u> be added to the DOMAIN file (#4.2) as per instructions provided in Patch XM\*DBA\*160. This domain is used to register pharmacies with Vitria and receive payer sheets via HL7 for the HIPAA NCPDP project. This domain is required to be in place before the installation of the IB\*2\*251, which is included in the BPS\*1.0 Master Build.

Additionally, the patch IB\*2.0\*223 has an environment check routine. It checks the RATE TYPE file (#399.3). Your site may have the Rate Types defined but the names may have been changed. The following Rate Types must be present <u>exactly</u> as follows:

CHAMPUS

CHAMPUS REIMB. INS.

CHAMPVA

CHAMPVA REIMB. INS.

If your site does not have the exact spelling as shown above, the BPS\*1.0Master Build will fail.

You may correct the Rate Type names yourself using FileMan or you can contact Enterprise V*IST*A Support (EVS) for assistance by contacting the help desk (800-596-4357) to log a National On-line Information System (NOIS) for you or you can submit a NOIS yourself.

Again, consult the *HIPAA NCPDP Connection for EDI Pharmacy (Dormant Release) Installation Guide* for specific instructions on the pre installation steps necessary to successfully install this master build.

*(This page included for two-sided copying.)*