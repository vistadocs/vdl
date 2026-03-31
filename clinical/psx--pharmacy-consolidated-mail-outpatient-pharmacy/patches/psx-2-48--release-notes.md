---
title: PSX*2*48 Release Notes - HIPAA NCPDP Connection for EDI Pharmacy
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: HIPAA NCPDP Connection for EDI Pharmacy
app_code: PSX
app_name: "Pharmacy: Consolidated Mail Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2*48
group_key: "PSX:PSX:2"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Project Overview](#project-overview) - [General Information](#general-information) - [HIPAA – Global Patches and Build](#hipaa-global-patches-and-build) - [Activating the ECME V. 1.0 Package](#activating-the-ecme-v-10-package) - [PSS\1\90, PSX\2\48, and PRCA\4.5\230 Patches](#pss190-psx248-and-pr
audience: 
keywords: 
  - pharmacy
  - ncpdp
  - cmop
  - ecme
  - drug
  - hipaa
  - outpatient
  - table
  - electronic
  - contents
page_count: 0
word_count: 4099
section_count: 8
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/ecme_hipaa_ncpdp_1_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/ecme_hipaa_ncpdp_1_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=85"
---

> ![](psx-2-48-release-notes-hipaa-ncpdp-connection-for-edi-pharmacy/001.png)

HIPAA NCPDP Connection for EDI Pharmacy  
(Active Release)

####### RELEASE NOTES

BPS\*1\*1  
IB\*2\*276

PRCA\*4.5\*230

PSO\*7\*148

PSS\*1\*90  
PSX\*2\*48

April 2006

VistA Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Project Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Project Overview](#project-overview)
  - [General Information](#general-information)
  - [HIPAA – Global Patches and Build](#hipaa-global-patches-and-build)
- [Activating the ECME V. 1.0 Package](#activating-the-ecme-v-10-package)
- [PSS\1\90, PSX\2\48, and PRCA\4.5\230 Patches](#pss190-psx248-and-prca45230-patches)
  - [PSS\1\90](#pss190)
  - [PSX\2\48](#psx248)
  - [PRCA\4.5\230](#prca45230)
- [BPS\1\1, PSO\7\148, and IB\2\276 Patches](#bps11-pso7148-and-ib2276-patches)
  - [HIPAA NCPDP – Global Build (BPS\1\1, PSO\7\148, and IB\2\276)](#hipaa-ncpdp-global-build-bps11-pso7148-and-ib2276)
  - [PSO\7\148](#pso7148)
- [Pre-Installation Issues](#pre-installation-issues)
- [Appendix A](#appendix-a)

## General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Healthcare Insurance Portability and Accountability Act (HIPAA) National Council for Prescription Drug Programs (NCPDP) Connection for Electronic Data Interchange (EDI) Pharmacy project, commonly referred to as HIPAA NCPDP or ePharmacy, is a collection of upgrades to the Outpatient Pharmacy V. 7.0, Pharmacy Data Management (PDM) V. 1.0, Consolidated Mail Outpatient Pharmacy (CMOP) V. 2.0, Integrated Billing (IB) V. 2.0, and Accounts Receivable (AR) V. 4.5 Veterans Health Information Systems and Technology Architecture (VistA) software packages, as well as an update to the previous dormant release of the Electronic Claims Management Engine (ECME) V. 1.0 package.

The goal of the HIPAA NCPDP project is to allow the VistA software applications to electronically transmit Outpatient Pharmacy prescription claims to payers. It will also receive claim responses (which include Drug Utilization Review (DUR) responses and warnings) on a real-time basis and in accordance with HIPAA NCPDP mandated format standards, specifically NCPDP Telecommunication Standard V. 5.1.

This project consists of two phases, a dormant phase and an active phase. The BPS V. 1.0 Master Build was the dormant phase that initiated the ECME V. 1.0 package (which occupies the BPS namespace) in a dormant state. Although the ECME V. 1.0 package’s functionality was dormant in this first release, IB V. 2.0 was enhanced in the build so that the user would be able to link pharmacy groups with insurance group plans. Also, following the installation of the BPS V. 1.0 Master Build, each site registered their pharmacy with the Financial Services Center (FSC). Additionally, functionality was added to designate over-the-counter (OTC) medications as electronically billable.

## HIPAA – Global Patches and Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The overall HIPAA NCPDP Global project consists of six patches. The first three patches, PSS\*1\*90, PSX\*2\*48, and PRCA\*4.5\*230, are independent patches that are being released at the same time as the master build. These three patches should be installed prior to the installation of the active master build.

Once PSS\*1\*90, PSX\*2\*48, and PRCA\*4.5\*230 have been installed, the ECME HIPAA NCPDP P3 1.0 Master Build, comprised of BPS\*1\*1, PSO\*7\*148, and IB\*2\*276 should be installed.

After all six patches have been correctly installed, they will provide the functionality to:

- Utilize the Outpatient Pharmacy functions to capture all data elements required to submit a billable third party claim.
- Utilize CMOP transmissions to gather and submit information to third parties through Emdeon (formerly WebMD).
- Provide reports and screens to the Outpatient Pharmacy Electronic Claims Coordinators (OPECCs) to show ECME claim statuses, etc.

![](psx-2-48-release-notes-hipaa-ncpdp-connection-for-edi-pharmacy/002.png)Important: If you have not installed the (dormant phase) BPS V. 1.0 Master Build and performed the steps outlined in the *HIPAA NCPDP Connection for EDI Pharmacy (Dormant Release) Installation Guide* before installing this (active phase) ECME HIPAA NCPDP P3 1.0 Master Build, the functionality enabling electronic claim submission to payers will not become active.

Vital instructions are provided in the *HIPAA NCPDP Connection for EDI Pharmacy (Active Release) Installation Guide* concerning:

- Required patches for PSS\*1\*90, PSX\*2\*48, and PRCA\*4.5\*230 and the ECME HIPAA NCPDP P3 1.0 Master Build.
- The ECME security key assignments.
- How to turn on switches to activate third party electronic prescription billing.

# Activating the ECME V. 1.0 Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new ECME V. 1.0 real-time system sends claim data in a HIPAA compliant NCPDP V. 5.1 format to a payer on a real-time basis and receives and processes the claim responses in the appropriate manner.

Following the installation and activation of the ECME HIPAA NCPDP P3 1.0 Master Build, ECME V. 1.0 will generate electronic claims in NCPDP V. 5.1 format based on the Outpatient Pharmacy V. 7.0 workflow, and will perform the following tasks. The software will now:

- Allow OPECCs to submit, resubmit, and reverse electronic claims.
- Provide reports for end users and management on claims status, transaction history, and system configuration standings.
- Allow Automated Data Processing Application Coordinator (ADPAC) and Information Resources Management Service (IRMS) staff to configure ECME V. 1.0 to Pharmacy site specifications.

ECME V. 1.0 processing begins when events within Outpatient Pharmacy V. 7.0 or Integrated Billing V 2.0 back-billing meet specific criteria that indicate the system should generate an electronic claim. To build a claim through ECME V. 1.0, the patient must be registered, have pharmacy insurance coverage, and have a prescription for a non-service connected condition in process.

Logic embedded within ECME V. 1.0 manages the creation of the electronic claim, which requires integration with IB V. 2.0 and PDM V. 1.0. ECME V. 1.0 also generates claims during CMOP V. 2.0 processing for prescriptions that meet billing requirements and are suspended for CMOP fills.

*(This page included for two-sided copying.)*

# PSS\*1\*90, PSX\*2\*48, and PRCA\*4.5\*230 Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General changes resulting from PSS\*1\*90, PSX\*2\*48, and PRCA\*4.5\*230 are as follows.

## PSS\*1\*90

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies PDM V. 1.0 to support the other applications in the electronic claims generation process. It does not interface with the ECME application at all. The changes to this application are the following:

1)  A new multiple field has been added to the DRUG file (#50) to store the latest National Drug Code (NDC) numbers that have been dispensed at window as well as by CMOP for a specific division. This way, when the next prescription is entered by the division for the same drug, the last used NDC is automatically retrieved from this new multiple, saved in the PRESCRIPTION file (#52), and sent to the third party payer through ECME. This field is populated automatically and does not require user input. Below is the multiple field and the fields under it:

32 NDC BY OUTPATIENT SITE

> .01 -OUTPATIENT SITE

> 1 -LAST LOCAL NDC

> 2 -LAST CMOP NDC

2)  A new field has been added to the DRUG file (#50) to store the DAW CODE (#81). DAW stands for “Dispense as Written” and refers to a set of ten NCPDP codes (0-9) that tells third party payers why a brand or generic product was selected to fill a prescription. When a new prescription is entered for a specific drug, the DAW code from the drug is stored in the PRESCRIPTION file (#52) for each fill. This field is solely being used for electronic billing purposes. It communicates to the third party payer that a drug has a special characteristic, which may prevent the payer from rejecting the claim.  
    See table below.

> DAW

> <u>Code</u> <u>Description</u>

> 0 NO PRODUCT SELECTION INDICATED

1 SUBSTITUTION NOT ALLOWED BY PRESCRIBER

2 SUBSTITUTION ALLOWED-PATIENT REQUESTED PRODUCT DISPENSED

> 3 SUBSTITUTION ALLOWED-PHARMACIST SELECTED PRODUCT DISPENSED

> 4 SUBSTITUTION ALLOWED-GENERIC DRUG NOT IN STOCK

> 5 SUBSTITUTION ALLOWED-BRAND DRUG DISPENSED AS A GENERIC

> 6 OVERRIDE

7 SUBSTITUTION NOT ALLOWED-BRAND DRUG MANDATED BY LAW

8 SUBSTITUTION ALLOWED-GENERIC DRUG NOT AVAILABLE IN MARKETPLACE

9 OTHER

> Since the VA primarily uses generic products, this has not been a major issue to date. The DAW CODE field (#81) default is 0, which means the physician did not specify whether to dispense a generic or brand name product. We anticipate getting some rejections from third parties for cases where we still dispense branded products, even though a generic is available in the marketplace. Our use of Coumadin<sup>®</sup> instead of generic Warfarin is one example.

> DAW codes are typically set for individual prescriptions, but can be set at the DRUG file (#50) level as well. An example scenario of each is given below.

> Example: Setting the DAW Code at the Prescription Level

> If you are informed that a prescription for Coumadin<sup>®</sup> was rejected for DAW reasons, you might try changing the DAW CODE of the prescription and resubmitting. The change can be made through the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option or the *Edit Prescriptions* \[PSO RXEDIT\] option in Outpatient Pharmacy V. 7.0. The DAW CODE will display for ePharmacy prescriptions. For original fills, this information can be edited by selecting screen field 21. For refills, the user must select screen field 20 (Refill Data), select the refill number to be edited; the “DAW CODE:” prompt displays after the “DIVISION:” prompt. In the case of the Coumadin<sup>®</sup> reject, you may try changing the DAW CODE to a 5 or a 1, then resubmitting to see if the claim gets processed. Both 5 and 1 are appropriate choices for the VA setting. Whether or not a claim will get rejected for these reasons and which code to use will vary from third party to third party. We are using brand name products, but are not charging for brand name products.

> The most common DAW codes are explained as follows:

> \#1: Physician stipulates that a particular brand be used.

> \#5: A brand name product is dispensed even though a generic product exists. Patient will be charged at the generic price.

> Example: Setting the DAW Code at the Drug File Level

> If you are told that almost every prescription for Coumadin<sup>®</sup> is being rejected, you may choose to make the change at the DRUG file (#50) level. Editing the DAW CODE field (#81) in the DRUG file (#50) for the Coumadin<sup>®</sup> entry will make a global change, such that each ePharmacy prescription filled for that product will use the DAW code you specify.

> Note: You may have to ask your Pharmacy ADPAC to make the change at the DRUG file (#50) level.

3)  The *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option has been modified to allow the user to associate a DAW CODE field (#81) entry to a drug in the DRUG file (#50). Every entry in the DRUG file (#50) will initially be assigned the DAW code of “0 - NO PRODUCT SELECTION INDICATED,” and can be later changed through this option.
4)  The *Lookup into Dispense Drug File* \[PSS LOOK\] option has been modified to display the DAW CODE field (#81) content for the drug being displayed. Below is the exact point where the DAW CODE field (#81) is displayed:

...

DEA, SPECIAL HDLG: 6 NDC: 00172-4390-18

DAW CODE: 5 - SUBSTITUTION ALLOWED-BRAND DRUG DISPENSED AS A GENERIC

CS FEDERAL SCHEDULE:

...

5)  The *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option has been modified to allow the user to enter a new code “E” to the DEA, SPECIAL HDLG field (#3) in the DRUG file (#50) to indicate that the drug is electronically billable. This will allow OTC drugs, supply items, and other drugs that are usually not billable to be marked for electronic billing.

> DEA, SPECIAL HDLG field effects on ePharmacy Billing:

- If the DEA, SPECIAL HDLG field (#3) contains an “I” (Investigational), “S”(Supply), or “9” (OTC), the drug is NOT billable. However, if the same drug also contains the “E” (electronically billable), the drug becomes BILLABLE.
- If the DEA, SPECIAL HDLG field (#3) contains an “M” or “0” (both designating a Compound Drug), the drug is NOT billable. If the same drug contains the “E” (electronically billable), the drug is STILL NOT billable.
- If the DEA, SPECIAL HDLG field (#3) is NULL (empty), the drug is NOT billable .

> Note that ALL other drugs are billable.

> Follow these guidelines to ensure proper electronic billing:

- If an item is to be billed, then there must be an entry in the DEA, SPECIAL HDLG field (#3). It is not necessary to include a numeric value; any value (other than the non-billable codes listed above) will allow ePharmacy to submit a bill.
- Add an “E” to all items that contain “9”,“I”or “S”, but are actually billable. This will most often occur with Insulin and Glucose test strips, which are usually marked with a 9 but are, in fact, billable for most insurance companies.
- Add a non-billable code (“0” (zero), “9”, or “M”) to all items that should NOT be billed. Specifically, the VA may not disclose any information on the following diseases: HIV, drug abuse, alcohol abuse, or sickle cell anemia without patient consent. In order to avoid disclosing these diagnoses inappropriately, it has been decided that the VA will not bill for any drug that is used exclusively or almost exclusively for these conditions. Drugs to mark as non-billable include Antiretrovirals, Disulfiram, Naltrexone, and Methadone for maintenance or detox.

> ![](psx-2-48-release-notes-hipaa-ncpdp-connection-for-edi-pharmacy/003.png)Note: The NDF option, *Rematch/Match Single Drugs* \[PSNDRUG\], screens out those items with a DEA, SPECIAL HDLG field (#3)code of “0”, “I”, or “M”. When sites receive NDF data updates that cause one of these items to be unmatched from NDF, they cannot use the *Rematch/Match Single Drugs* \[PSNDRUG\] option to rematch if they have added “0”, “I”, or “M” to drugs like Antiretrovirals, Disulfiram, Naltrexone, or Methadone for maintenance or detox.

> Sites can either:

> 1\. Rematch to NDF using another option, or

> 2\. Remove the DEA, SPECIAL HDLG field (#3) code, use the *Rematch/Match Single Drugs* option, and then add the DEA, SPECIAL HDLG field (#3) code back in.

## PSX\*2\*48

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies the CMOP application to submit electronic claims for prescriptions that are transmitted to CMOP centers to be filled and dispensed remotely. All the prescriptions that are ready to be included on the batch to be transmitted to CMOP are first transmitted to the third party insurance. Once this first step is completed, the system waits 60 seconds before starting the actual transmission to CMOP. This process will affect the existing CMOP functionality in two ways:

1)  If a response from the third party payer is not received by the time the prescription is about to be transmitted to CMOP, it is skipped and remains in the queue for the next CMOP transmission. A MailMan message containing all the prescriptions that were skipped and that remain in the queue is generated at the end of the process and is transmitted to all the holders of the PSXMAIL security key. If no users on the system have this key, the message is sent to all the users holding the PSXCMOPMGR security key.
2)  If the third party payer rejects the claim due to a DUR or a Refill Too Soon finding, the prescription is not sent to CMOP and remains in the queue to be transmitted in the next transmission. The prescription will not be transmitted to CMOP until the reject is resolved by the user through the Outpatient Pharmacy V. 7.0 application. Two new options have been created for the pharmacy users to resolve these rejects:

> *Third Party Payer Rejects – Worklist* \[PSO REJECTS WORKLIST\]

> *Third Party Payer Rejects - View/Process* \[PSO REJECTS VIEW/PROCESS\]

> The above options reside in the new *ePharmacy Menu* \[PSO EPHARMACY MENU\] option, which can be found under the *Rx (Prescriptions)* \[PSO RX\] option.

## PRCA\*4.5\*230

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch PRCA\*4.5\*230 represents the Accounts Receivable portion of the Phase III of the NCPDP-Pharmacy Connection project. It modifies the EDI LockBox functionality by adding the ability to manually process an Explanation of Benefits (EOB) related to NCPDP claims. There are no changes to the existing user interface introduced by this patch. All changes are related to internal EDI LockBox processing of Electronic Remittance Advice (ERA) related to the NCPDP ePharmacy claims. There are two functional changes introduced with this patch:

1)  Enhancements to the ECME matching procedure. Previously, as implemented in the patch PRCA\*4.5\*202, AR was using the Statement Date (Segment 05 Piece 9) to find a matching IB/AR bill. With this patch, AR will be using the “Service Date” data element for matching purposes.
2)  The EDI LockBox AR functionality was modified to screen out Electronic Explanation of Benefits (EEOB) related to ePharmacy rejects. When VistA submits an NCPDP ePharmacy claim and the claim is rejected, it does not create a bill in IB/AR. Therefore, VistA does not need to receive EEOBs in response to those claims. Additionally, VistA is unable to process those reject-related EEOBs. Previously, those EEOBs were displayed on the AR EDI LockBox Exceptions User’s Screen and required manual resolution. With this patch, AR will be able to recognize such EEOBs and disregard them; they will not display on the EDO Exceptions Screen and will not be stored in the ELECTRONIC REMITTANCE ADVICE file (#344.4).

*(This page included for two-sided copying.)*

# BPS\*1\*1, PSO\*7\*148, and IB\*2\*276 Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches BPS\*1\*1, PSO\*7\*148, and IB\*2\*276 make up the active master build. The existing ECME, Outpatient Pharmacy, and IB packages are modified or enhanced as necessary by this build to create electronic claims using billing and applicable clinical information.

The information to be collected will consist of data currently available within the Outpatient Pharmacy V. 7.0, Patient Information Management System (PIMS) V. 5.3, and IB V. 2.0 applications.

Infrastructure components at the Austin Automation Center (AAC) process incoming claim data using Vitria BusinessWare V. 3.1.7 (Vitria), the National Health Care Insurance Database (NHCID) for transaction logging, and the HIPAA EDI website to register VA pharmacies. These components also communicate with Emdeon (formerly WebMD) and third party payers for claims adjudication and return this information to VistA.

The following sections contain a brief description of changes to the ECME, IB, and Outpatient Pharmacy packages. For complete information, please refer to the following documents:

- *Electronic Claims Management Engine (ECME) User Manual*
- *Electronic Claims Management Engine (ECME) Technical Manual/Security Guide*
- *HIPAA NCPDP Integrated Billing (IB) Accounts Receivable (AR) Release Notes*
- *Outpatient Pharmacy V. 7.0 User Manual*
- *Outpatient Pharmacy V. 7.0 Technical Manual/Security Guide*

## HIPAA NCPDP – Global Build (BPS\*1\*1, PSO\*7\*148, and IB\*2\*276)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HIPAA NCPDP – Global project is fairly large and complex and involves six different applications that have been significantly changed to enable VA Medical centers to perform third party payer electronic prescription billing. Below is a list of all the applications involved along with this project.

APPLICATION/VERSIONPATCH

Accounts Receivable V. 4.5 PRCA\*4.5\*230

Consolidated Mail Outpatient Pharmacy V. 2.0 PSX\*2\*48

Electronic Claims Management Engine V. 1.0 BPS\*1\*1

Integrated Billing V. 2.0 IB\*2\*276

Outpatient Pharmacy V. 7.0 PSO\*7\*148

Pharmacy Data Management V. 1.0 PSS\*1\*90

VistA software applications and infrastructure are enhanced to allow the electronic transmission of Outpatient Pharmacy prescription claims (WINDOW, MAIL, and CMOP fills) to third party payers via the network connections available through the AAC. VistA will be enhanced to receive electronic adjudicated responses from the third party payer, which include real-time processing for DUR and Refill Too Soon warnings.

Warning information will be displayed to the pharmacist as the prescription is being processed. The pharmacist will have the capability to take the appropriate action to ensure patient safety or override the warning and resubmit the claim to the payer for payment.

When a status of “payable” is returned by the payer for a released prescription, VistA will automatically create the bill in IB V. 2.0, authorize it, and immediately create the receivable in AR V. 4.5. Since the exact amount being paid by the payer is known, a decrease adjustment will be automatically generated and applied so that the receivable is equal to the net amount due from the payer. The system also provides electronic payment matching capability (for electronically billed Outpatient Pharmacy prescriptions) using the existing EDI LockBox functionality, which processes other electronic payments from third party payers. This real-time electronic claims processing capability will be provided in accordance with the HIPAA EDI transactions and NCPDP mandated format standards, specifically NCPDP Telecommunication Standard V. 5.1.

Additional functionality delivered with this project includes:

- Pharmacy DAW prescription processing
- Auto-Release/Outpatient Pharmacy Automation Interface (OPAI) Integration
- Back-billing capability to allow electronic billing of claims from within IB V. 2.0
- Capability to MOVE a group of subscribers from one insurance plan to another while automatically “expiring” the old plan, thus saving time

Overview of the Process

When a prescription is about to be filled and dispensed by the pharmacy, the Outpatient Pharmacy V. 7.0 application submits the prescription to ECME. This application then contacts the IB V. 2.0 application to verify whether the prescription is electronically billable or not. If it is, ECME gathers the information necessary to generate an NCPDP claim. The claim information is passed to the VistA HL7 package. The HL7 package then sends the billing information to the AAC, where it is routed to the corresponding third party payer via Emdeon (formerly WebMD).

Once the payer processes the information, the response coming back from the payer is passed back to the site which made the request, and the information is stored in ECME V. 1.0. If the third party payer accepted the claim, the adjudicated information is passed along to IB V. 2.0. If the claim was rejected, the problem can be worked on and a new claim can be submitted to the payer.

For CMOP processing, the third party claim is sent just before the information is transmitted to the CMOP center. When the CMOP center sends the dispensing information back to the pharmacy, the NDC number is checked, and if it is different from what was sent to the CMOP center, a new claim is generated in the background to the third party payer. If the CMOP center indicates that a prescription cannot be dispensed, a reversal is generated and sent to the third party payer. A reversal is also sent to the payer if the NDC received from the CMOP center is not a valid NDC (see Appendix A for NDC validation).

## PSO\*7\*148

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes resulting from this Outpatient Pharmacy V. 7.0 patch are as follows:

1)  *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option

> At the point that the prescription is verified, the New Order, Edit, Renew, Refill, and Pull Early from Suspense functions will begin the third party billing evaluations. If IB V. 2.0 determines that the prescription is third party billable, messaging will be displayed on the user’s screen stating that the claim is being submitted to ECME V. 1.0 and will show the progress of the claim. If the payer rejects the claim for drug interactions, the payer's drug interaction information will be displayed, and the user will be given the opportunity to ignore the payer’s response and move on with the filling process, override the reject by resubmitting the claim or postpone the processing of the prescription by taking no action when the reject is received. For prescriptions that have been electronically submitted to the third party payer an indicator is displayed on the Patient Prescription Processing screen. This indicator will take the form of an “e” next to the prescription number  
> (e.g., “1090303\$e”).

> A new section called REFILL TOO SOON/DUR REJECTS (Third Party) has been created in the Medication Profile screen to single out prescriptions that have been rejected by third party payers for DUR or REFILL TOO SOON reasons. Prescriptions under this section have certain restrictions. Basically, they cannot be renewed, refilled, reprinted, copied, or released through the Outpatient Pharmacy Package until the REJECT is resolved. Actions may still be taken on these prescriptions through CPRS.

> When an individual prescription is selected, the user will have a new hidden option called REJ - View Reject, which will allow them to resolve the REJECT and remove it from the REFILL TOO SOON / Third Party DUR REJECTS section.

2)  *Return Medication to Stock* \[PSO RETURNED STOCK\] option

> The *Return Medication to Stock* option was modified to notify the third party payer that a previously billed prescription was not actually filled. If the prescription was previously billed to a third party payer and a payable response was received, the claim will be reversed, and the pharmacy user will see messaging stating that the third party claim was submitted for reversal. If a claim for the prescription was previously rejected by the third party payer, the user will see a message indicating that no reversal was required. If the prescription was not previously billed to a third party payer, messaging was not changed from the existing functionality.

3)  *Delete a Prescription* \[PSO RXDL\] option

> The messaging for *Delete a Prescription* was modified to perform in the same manner as the *Return Medication to Stoc*k function described above.

4)  *Pull Early from Suspense* \[PSO PNDRX\] option

> The *Pull Early from Suspense* option was modified to submit a third party claim for the prescription. Messaging will occur to notify the user of the status of the claim as it is going through the submission process.

5)  *Print from Suspense File* \[PSO PNDLBL\] option

> This option was modified to submit third party claims in the same manner as stated above, except the *Print from Suspense File* claim submission function will be performed in the background. No user interaction will occur.

6)  *ePharmacy Menu* \[PSO EPHARMACY MENU\] option

> This new menu option was created for ePharmacy related menu options. Two new options are being added with this patch:

1.  *Third Party Payer Rejects - Worklist* \[PSO REJECTS WORKLIST\] option

> This option is used to process third party payer rejects that have clinical significance. For now, only DUR and REFILL TOO SOON rejects are being considered as having significance.

> It is recommended that one designated pharmacist monitor the worklist throughout the day. The highest volume of entries is expected to be logged following a CMOP transmission or after the *Print from Suspense File* process.

2.  *Third Party Payer Rejects - View/Process* \[PSO REJECTS VIEW/PROCESS\] option

> This option performs the same functionality as the option above. However, the user has more filtering capabilities through this option. In addition, closed/resolved rejects can only be viewed by using this option.

> The View/Process function should be used on an as-needed basis, such as for viewing resolved rejects, processing rejects for a specific insurance company, and re-opening a resolved reject, among other reasons.

7)  *Release Medication* \[PSO RELEASE\] option

> The prescription release process was modified to perform NDC validation for ePharmacy prescriptions. When the user selects a new NDC a new claim is submitted to the payer before the prescription is released. Prescriptions can also be released from the Medication Profile screen and from the Outpatient Rx's \[PSD OUTPATIENT\] option for Controlled Substances.

8)  *View Prescriptions* \[PSO VIEW\] option

> This option was changed to include two new sections: ECME Log and ECME REJECT Log. Information about third party payer submission and rejects will be displayed under these sections.

Data Dictionary Changes in Outpatient Pharmacy V. 7.0:

1)  The field NDC (#4) under the CMOP EVENT multiple (#52.01) has been renamed to NDC RECEIVED. This fields holds the NDC that was received from the CMOP facility with the dispensing message. The renaming was necessary due to a new field called NDC SENT (#12) under the same multiple that is being created by this project (see below).
2)  A new field NDC SENT (#12) is being created under the CMOP EVENT multiple (#52.01) to store the NDC sent to CMOP during the CMOP transmission. This field is being used by ePharmacy to analyze differences between the NDC sent to CMOP and the actual dispensed NDC by CMOP.
3)  A new multiple field called REJECT INFO (#52.25) has been created in the PRESCRIPTION file (#52) to store information about DUR and REFILL TOO SOON rejects returned by third party payers. The following fields are part of this multiple:

.01 NCPDP REJECT CODE

> 1 DATE/TIME DETECTED

> 2 PAYER MESSAGE

> 3 REASON

> 4 PHARMACIST

> 5 FILL NUMBER

> 6 GROUP NAME

> 7 PLAN CONTACT

> 8 PLAN PREVIOUS FILL DATE

> 9 STATUS

> 10 CLOSED DATE/TIME

> 11 CLOSED BY

> 12 CLOSE REASON

> 13 CLOSE COMMENTS

> 14 REASON FOR SERVICE CODE

> 15 PROFESSIONAL SERVICE CODE

> 16 RESPONSE ID

> 17 OTHER REJECTS

> 18 DUR TEXT

> 19 RESULT OF SERVICE CODE

> 20 INSURANCE NAME

> 21 GROUP NUMBER

> 22 CARDHOLDER ID

> 23 RE-OPENED

*(This page included for two-sided copying.)*

# Pre-Installation Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** Failure to carefully follow the instructions provided in the *HIPAA NCPDP Connection for EDI Pharmacy (Active Release) Installation Guide* can result in the failure of the ECME HIPAA NCPDP P3 1.0 Master Build to install correctly.

Correct pre-installation set up is necessary for the successful installation of this build. Prior to the installation of ECME HIPAA NCPDP P3 1.0 Master Build, it is imperative that the dormant ECME V. 1.0 Master Build be installed in your account and that your site complete the required insurance matching and registration steps. Consult the *HIPAA NCPDP Connection for EDI Pharmacy (Dormant Release) Installation Guide* on the VistA Documentation Library (VDL) at <http://www.va.gov/vdl/> for specific instructions on the installation and set up requirements associated with BPS V. 1.0.

Once the dormant version of the HIPAA NCPDP Connection for EDI Pharmacy project has been installed and your site has completed registration, you may begin the installation of the HIPAA – Global project patches and build.

The first step in activating the ECME functionality is to install patches PSS\*1\*90, PSX\*2\*48, and PRCA\*4.5\*230 into your account. Once PSS\*1\*90, PSX\*2\*48, and PRCA\*4.5\*230 have been installed, the master build may be installed.

> **IMPORTANT:** During installation of the build, the user will be prompted to enter the name of the coordinator for the BPS OPECC mail group. Prior to beginning installation, this name will need to be decided upon and ready for input.

The software will still not be considered active until both the Pharmacy and the Integrated Billing departments agree to activate the software. Setup from both packages will need to be coordinated to activate the software.

Special Note:  The Chief Business Office (CBO) is controlling the "activation" of the ePharmacy product for VAMCs. CBO will communicate a list of sites to "activate" during the monthly IRM calls. In addition, CBO will be providing several IRM training calls where further instruction will be provided. Sites are NOT to "activate" unless instructed specifically by CBO. 

Pharmacy will need to assign their Outpatient Pharmacy divisions under the appropriate BPS pharmacy. This will be accomplished under the *Edit Pharmacy ECME Pharmacy Data* \[BPS SETUP PHARMACY\] option.

Select BPS PHARMACIES NAME: ALASKA

Select OUTPATIENT SITE: ALASKA VA HSRO

Are you adding ' ALASKA VA HSRO 463 ’ as a new OUTPATIENT SITE

(the 1ST for this BPS PHARMACIES)? No// Y  (Yes)

Select OUTPATIENT SITE: \<Enter\>

NCPDP \#: 1098981// \<Enter\>

CMOP SWITCH: CMOP OFF// \<Enter\>

AUTO-REVERSE PARAMETER: 0// \<Enter\>

DEFAULT DEA \#: AG12345// \<Enter\>Note: There must be at least one Outpatient Site entered for a BPS Pharmacy for electronic billing to occur. You may assign multiple Outpatient Sites to a BPS Pharmacy, as in the case of a non-dispensing CBOC.

Integrated Billing will also need to activate the ePharmacy interface using the *EDIT HIPAA NCPDP Flag* \[IBCNR EDIT HIPAA NCPDP FLAG\] option. At the following prompt, enter “Active” to activate the NCPDP FLAG:

Edit HIPAA NCPDP ACTIVE FLAG

(master switch to control e-Pharmacy NCPDP transactions)

HIPAA NCPDP ACTIVE FLAG: Active

Once these two steps are completed, prescriptions processed locally (WINDOW/MAIL FILL or REFILL) that have third party prescription coverage, with the plan linked to the appropriate VA Pharmacy plan and activated will have claims automatically generated. (Please refer to *e‑Pharmacy Claims Insurance Process User Guide* for instructions for linking prescription plans to VA Pharmacy Plans.)

After your site has determined that claim generation is working smoothly, you will want to turn on the switch for CMOP processing. This will enable any prescriptions that are processed through the CMOP software that meet the criteria of electronic claim submission to be transmitted.

The CMOP switch is controlled by the Pharmacy Service and can be edited through the *Edit Pharmacy ECME Pharmacy Data* \[BPS SETUP PHARMACY\] option.

Select BPS PHARMACIES NAME: ALASKA

Select OUTPATIENT SITE: ALASKA VA HSRO// \<Enter\>

OUTPATIENT SITE: ALASKA VA HSRO// \<Enter\>

Select OUTPATIENT SITE: \<Enter\>

NCPDP \#: 1098981// \<Enter\>

CMOP SWITCH: CMOP OFF// CMOP ON Change to CMOP ON or 1 when ready for  AUTO-REVERSE PARAMETER: 0// \<Enter\> electronic claim submission to occur  

DEFAULT DEA \#: AG12345// \<Enter\> during CMOP transmissions.            

# Appendix A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NDC format adopted by this project is 11 digits, segmented in the following way:  
NNNNN-NNNN-NN (5-4-2). Existing NDCs in the DRUG file (#50) that are not in this format will be interpreted by this project in the following way:

NDC Conversion Table

<u>Original NDC</u> <u>Conversion Logic</u> <u>Converted NDC</u>

5-4-2 No Conversion NA

4-4-2 Lead fill 1st segment with 0 5-4-2

5-3-2 Lead fill 2nd segment with 0 5-4-2

5-4-1 Lead fill 3rd segment with 0 5-4-2

6-4-2 Parse leading character from 1st seg 5-4-2

6-3-2 Lead fill 2nd segment with 0 5-4-2

Parse leading char from 1st segment

6-3-1 Lead fill both 2nd & 3rd segs with 0 5-4-2

Parse leading char from 1st segment

11 digit, no segmentation Process as 5-4-2 NDC 5-4-2

Non 11-digit, no seg. No Conversion None

For any other combination, if the first segment is greater than 5, the system will parse off all characters starting left to right until 5 digits remain. If the 2nd and/or 3rd segments are less than 4 or 2 characters respectively, the system ‘0 fills’ the entries until these segments are 4 and 2 characters, respectively. If the 2nd and/or 3rd segments are greater than 4 or 2 characters respectively, the system does nothing and treats it as if the system cannot determine the appropriate segmentation (invalid NDC). If there is no segmentation, the number must be 11 digits. If it is, the NDC is treated as a 5-4-2 NDC. If it is anything other than 11 digits, there is no interpretation of the NDC. If the first segment is greater than 6, it will be considered invalid.

*(This page included for two-sided copying.)*