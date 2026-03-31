---
consolidated_title: "release notes/installation guide"
app_code: IB
doc_type: IG
master_source: "IB*2*506 Release Notes/Installation Guide"
master_pub_date: revision_count: 0
consolidated_from: 6 versions
prior_versions:
  - "IB*2*447 Release Notes/Installation Guide"
  - "IB*2*497 Release Notes/Installation Guide"
  - "IB*2*517 Release Notes/Installation Guide"
  - "IB*2*547 Release Notes/Installation Guide"
  - "IB*2*549 Release Notes/Installation Guide"
---

![](ib-2-506-release-notes-installation-guide/001.png)

Electronic Data Interchange (EDI)New Standards and Operating Rules VHA Provider-side Technical Compliance RequirementsVA118-1001-1018

eIV System Modifications

####### Integrated Billing (IB)

####### 

####### RELEASE NOTES/Installation Guide

IB\*2\*506May 2014Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Documentation and Distribution](#documentation-and-distribution)
- [Patch Description and Installation Instructions](#patch-description-and-installation-instructions)
  - [Patch Description](#patch-description)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Installation Instructions](#installation-instructions)
- [Enhancements](#enhancements)
  - [Enhancements to the Insurance Buffer](#enhancements-to-the-insurance-buffer)
    - [Insurance Buffer – Create New ‘Complete Buffer’ (CB) Screen](#insurance-buffer-create-new-complete-buffer-cb-screen)
    - [Insurance Buffer – Default View to be the ‘Complete Buffer’ (CB) Screen](#insurance-buffer-default-view-to-be-the-complete-buffer-cb-screen)
    - [Insurance Buffer – ‘Complete Buffer’ Screen Contents](#insurance-buffer-complete-buffer-screen-contents)
    - [Insurance Buffer – ‘Complete Buffer’ Screen Actions](#insurance-buffer-complete-buffer-screen-actions)
    - [Insurance Buffer – Ability to Jump to the ‘Complete Buffer’ Screen](#insurance-buffer-ability-to-jump-to-the-complete-buffer-screen)
    - [Insurance Buffer – ‘Positive Buffer’ Screen Fix Filter](#insurance-buffer-positive-buffer-screen-fix-filter)
    - [Insurance Buffer – ‘Medicare Buffer’ Screen Fix Filter](#insurance-buffer-medicare-buffer-screen-fix-filter)
    - [Insurance Buffer – ‘Negative Buffer’ Screen Fix Filter](#insurance-buffer-negative-buffer-screen-fix-filter)
    - [Insurance Buffer – Remove ‘Future Appointments’ Screen](#insurance-buffer-remove-future-appointments-screen)
    - [Insurance Buffer – Create New ‘Failure Buffer’ (FB) Screen](#insurance-buffer-create-new-failure-buffer-fb-screen)
    - [Insurance Buffer – ‘Failure Buffer’ Screen Contents](#insurance-buffer-failure-buffer-screen-contents)
    - [Insurance Buffer – ‘Failure Buffer’ Screen Actions](#insurance-buffer-failure-buffer-screen-actions)
    - [Insurance Buffer – Remove ‘Verify Entry’ Action from the Buffer Views](#insurance-buffer-remove-verify-entry-action-from-the-buffer-views)
    - [Insurance Buffer – Filter Insurance Buffer Records Based on User’s Security Keys (Revised)](#insurance-buffer-filter-insurance-buffer-records-based-on-users-security-keys-revised)
    - [Insurance Buffer – Ability to Jump to the ‘Failure Buffer’ Screen](#insurance-buffer-ability-to-jump-to-the-failure-buffer-screen)
    - [Insurance Buffer – Remove Ability to Create New Insurance Company](#insurance-buffer-remove-ability-to-create-new-insurance-company)
    - [Insurance Buffer – Remove Ability to Create New Group/Plan](#insurance-buffer-remove-ability-to-create-new-groupplan)
    - [Insurance Buffer – Rename the Insurance Buffer File](#insurance-buffer-rename-the-insurance-buffer-file)
    - [Insurance Buffer – Create Insurance Buffer Entry for Appointments with Nationally Inactive Payers](#insurance-buffer-create-insurance-buffer-entry-for-appointments-with-nationally-inactive-payers)
    - [Insurance Buffer – Add “Escalate” Action to the Buffer Views](#insurance-buffer-add-escalate-action-to-the-buffer-views)
    - [Insurance Buffer – Restrict use of the “Escalate” Action](#insurance-buffer-restrict-use-of-the-escalate-action)
    - [Insurance Buffer – Implement the “Escalate” Action](#insurance-buffer-implement-the-escalate-action)
  - [System Feature: eIV – HL7 Transactions](#system-feature-eiv-hl7-transactions)
    - [eIV HL7 Transactions - Daily Registration Message to FSC](#eiv-hl7-transactions-daily-registration-message-to-fsc)
    - [eIV HL7 Transactions – Receive Retry Flag from FSC](#eiv-hl7-transactions-receive-retry-flag-from-fsc)
    - [eIV HL7 Transactions – Store Retry Flag from FSC](#eiv-hl7-transactions-store-retry-flag-from-fsc)
    - [eIV HL7 Transactions – Receive Freshness Days from FSC](#eiv-hl7-transactions-receive-freshness-days-from-fsc)
    - [eIV HL7 Transactions – Store Freshness Days from FSC](#eiv-hl7-transactions-store-freshness-days-from-fsc)
    - [eIV HL7 Transactions – Receive Timeout Days from FSC](#eiv-hl7-transactions-receive-timeout-days-from-fsc)
    - [eIV HL7 Transactions – Store Timeout Days from FSC](#eiv-hl7-transactions-store-timeout-days-from-fsc)
    - [eIV HL7 Transactions – Treat all AAA Action Codes as Though the Payer/FSC Responded](#eiv-hl7-transactions-treat-all-aaa-action-codes-as-though-the-payerfsc-responded)
    - [eIV HL7 Transactions – Honor the Retry Flag when Resending an eIV Inquiry](#eiv-hl7-transactions-honor-the-retry-flag-when-resending-an-eiv-inquiry)
    - [eIV HL7 Transactions – Honor the Timeout Days when Resending an eIV Inquiry](#eiv-hl7-transactions-honor-the-timeout-days-when-resending-an-eiv-inquiry)
    - [eIV HL7 Transactions – Honor the ‘NUMBER RETRIES’ when Resending an eIV Inquiry](#eiv-hl7-transactions-honor-the-number-retries-when-resending-an-eiv-inquiry)
    - [eIV HL7 Transactions – Honor the Payer’s Nationally Active Flag when Resending an eIV Inquiry](#eiv-hl7-transactions-honor-the-payers-nationally-active-flag-when-resending-an-eiv-inquiry)
    - [eIV HL7 Transactions – Do Not Send MailMan Message When Retries are Exhausted](#eiv-hl7-transactions-do-not-send-mailman-message-when-retries-are-exhausted)
  - [System Feature: eIV Site Parameters](#system-feature-eiv-site-parameters)
    - [eIV Site Parameters – Retry Flag Not Editable](#eiv-site-parameters-retry-flag-not-editable)
    - [eIV Site Parameters - Freshness Days Not Editable](#eiv-site-parameters-freshness-days-not-editable)
    - [eIV Site Parameters – Timeout Days Not Editable](#eiv-site-parameters-timeout-days-not-editable)
    - [eIV Site Parameters – Set the Value of ‘NUMBER RETRIES’ Field](#eiv-site-parameters-set-the-value-of-number-retries-field)
    - [eIV Site Parameters – Set the Initial Value of the Retry Flag](#eiv-site-parameters-set-the-initial-value-of-the-retry-flag)
    - [eIV Site Parameters – Set the Initial Value of the Freshness Days](#eiv-site-parameters-set-the-initial-value-of-the-freshness-days)
    - [eIV Site Parameters – Set the Initial Value of the Timeout Days](#eiv-site-parameters-set-the-initial-value-of-the-timeout-days)
    - [eIV Site Parameters - Set the Value of the ‘HL7 Response Processing’ Field](#eiv-site-parameters-set-the-value-of-the-hl7-response-processing-field)
    - [eIV Site Parameters – ‘HL7 Response Processing’ Field Not Editable](#eiv-site-parameters-hl7-response-processing-field-not-editable)
    - [eIV Site Parameters – Restrict eIV Number of Possible Retries](#eiv-site-parameters-restrict-eiv-number-of-possible-retries)
  - [System Feature: Security Keys](#system-feature-security-keys)
    - [Security Key – Create New Key to Add/Edit an Insurance Company](#security-key-create-new-key-to-addedit-an-insurance-company)
    - [Security Key – Lock the “Insurance Company Entry/Edit” Option](#security-key-lock-the-insurance-company-entryedit-option)
    - [Security Key – User Requires Key to Add/Edit Insurance Company in the Insurance Buffer](#security-key-user-requires-key-to-addedit-insurance-company-in-the-insurance-buffer)
    - [Security Key – Create New Key to Add/Edit a Group/Plan](#security-key-create-new-key-to-addedit-a-groupplan)
    - [Security Key – User Requires Key to Add/Edit Group/Plan in the Buffer](#security-key-user-requires-key-to-addedit-groupplan-in-the-buffer)
    - [Security Key – Lock the Ability to Create a Group/Plan within ‘Patient Insurance Info View/Edit’ Option](#security-key-lock-the-ability-to-create-a-groupplan-within-patient-insurance-info-viewedit-option)
  - [System Feature: Eligibility Benefits](#system-feature-eligibility-benefits)
    - [Eligibility Benefits – Update the Eligibility Benefit Information Accessed via the ‘Process Insurance Buffer’ option](#eligibility-benefits-update-the-eligibility-benefit-information-accessed-via-the-process-insurance-buffer-option)
    - [Eligibility Benefits – Update the Eligibility Benefit Information Accessed via the ‘TPJI’ Option](#eligibility-benefits-update-the-eligibility-benefit-information-accessed-via-the-tpji-option)
    - [Eligibility Benefits – Update the Eligibility Benefit Information Accessed via the ‘Patient Insurance Info View/Edit’ Option](#eligibility-benefits-update-the-eligibility-benefit-information-accessed-via-the-patient-insurance-info-viewedit-option)
    - [Eligibility Benefits – Include the Eligibility Benefit Information on the eIV Response Report](#eligibility-benefits-include-the-eligibility-benefit-information-on-the-eiv-response-report)
    - [Eligibility Benefits – Store the Service Date on the Patient’s Policy Record](#eligibility-benefits-store-the-service-date-on-the-patients-policy-record)
    - [Eligibility Benefits – Store the Service Type on the Patient’s Policy Record](#eligibility-benefits-store-the-service-type-on-the-patients-policy-record)
    - [Eligibility Benefits – Display the Service Date of the Response](#eligibility-benefits-display-the-service-date-of-the-response)
    - [Eligibility Benefits – Display the Service Type of the Response](#eligibility-benefits-display-the-service-type-of-the-response)
    - [Eligibility Benefits – Eligibility Benefit (1st Priority Sort Order): Insurance Status](#eligibility-benefits-eligibility-benefit-1st-priority-sort-order-insurance-status)
    - [Eligibility Benefits - Eligibility Benefit (2nd Priority Sort Order): Insurance Type](#eligibility-benefits-eligibility-benefit-2nd-priority-sort-order-insurance-type)
    - [Eligibility Benefits – Eligibility Benefit (3<sup>rd</sup> Priority Sort Order): Coordination of Benefits (COB) (Removed – 08/01/2013)](#eligibility-benefits-eligibility-benefit-3suprdsup-priority-sort-order-coordination-of-benefits-cob-removed-08012013)
    - [Eligibility Benefits - Eligibility Benefit (4th Priority Sort Order): Indication of Other Insurance](#eligibility-benefits-eligibility-benefit-4th-priority-sort-order-indication-of-other-insurance)
This Integrated Billing (IB) patch introduces substantial changes to
VistA's electronic Insurance Verification (eIV) Eligibility Inquiry and
Response Processing in order to meet the Committee on Operating Rules for
Information Exchange (CORE) Operating Rules.
APPLICATION/VERSION PATCH
---------------------------------------------------------------
INTEGRATED BILLING (IB) V. 2.0 IB\*2\*506
This patch (IB\*2\*506) is being released in the Kernel Installation and Distribution System (KIDS) distribution.

## Documentation and Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to File Transfer Protocol (FTP) the files from

REDACTED This transmits the files from the first

available FTP server. Sites may also elect to retrieve software directly

from a specific server as follows:

Albany REDACTED REDACTED

Hines REDACTED REDACTED

Salt Lake City REDACTED REDACTED

Documentation can also be found on the VA Software Documentation Library

at:

http://www.va.gov/vdl/

Title File Name FTP Mode

-----------------------------------------------------------------------

IB eIV System Modification Compliance

Release Notes/Installation Guide

(IB\*2.0\*506) ib_2_p506_rn.pdf Binary

Electronic Insurance Verification

User Guide ib_2_0_eIV_ug_r0514.pdf Binary

Electronic Insurance Verification

Technical Manual/Security Guide ib_2_0_eIV_tm_r0514.pdf Binary

Integrated Billing (IB) V. 2.0

Technical Manual ib_2_0_tm_r0514.pdf Binary

# Patch Description and Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

=============================================================================

Run Date: JUN 06, 2014 Designation: IB\*2\*506

Package : INTEGRATED BILLING Priority : MANDATORY

Version : 2 Status : COMPLETE/NOT RELEASED

=============================================================================

Associated patches: (v)IB\*2\*142 \<\<= must be installed BEFORE \`IB\*2\*506'

(v)IB\*2\*276 \<\<= must be installed BEFORE \`IB\*2\*506'

(v)IB\*2\*399 \<\<= must be installed BEFORE \`IB\*2\*506'

(v)IB\*2\*416 \<\<= must be installed BEFORE \`IB\*2\*506'

(v)IB\*2\*435 \<\<= must be installed BEFORE \`IB\*2\*506'

(v)IB\*2\*438 \<\<= must be installed BEFORE \`IB\*2\*506'

(v)IB\*2\*479 \<\<= must be installed BEFORE \`IB\*2\*506'

(v)IB\*2\*497 \<\<= must be installed BEFORE \`IB\*2\*506'

Subject: EIV SYSTEM MODIFICATIONS

Category: ROUTINE

DATA DICTIONARY

ENHANCEMENT

INPUT TEMPLATE

OTHER

Description:

===========

This Integrated Billing (IB) patch introduces substantial changes to

Veterans Health Information Systems & Technology Architecture (VistA)'s

electronic Insurance Verification (eIV) eligibility inquiry and

response processing in order to meet the Committee on Operating Rules for

Information Exchange (CORE) Operating Rules.

Complete list of patch items:

1\. Revised the insurance buffer views and actions.

a\) The new default view for those who select the option PROCESS

INSURANCE BUFFER \[IBCN INSURANCE BUFFER PROCESS\] is the "Complete

Buffer". The "Complete Buffer" view consists of a list of all

insurance buffer entries that have the status of 'ENTERED'.

b\) Added a new insurance buffer view "Failure Buffer", which consists

of a list of all entries that have the status of 'ENTERED' and has

the eIV symbol of "!".

c\) The insurance buffer view "Future Appointments" has been removed.

d\) The action (VE) VERIFY ENTRY has been removed.

e\) A new action (ES) ESCALATE ENTRY has been introduced with this

patch. More details regarding this action are listed below.

2\. The ability to escalate an insurance buffer entry was introduced with

this patch.

a\) Two new security keys were added to VistA as a result of this

patch. If a user selects the option PROCESS INSURANCE BUFFER

\[IBCN INSURANCE BUFFER PROCESS\] and they have neither of the new

security keys (IB INSURANCE COMPANY EDIT and IB GROUP PLAN EDIT),

then the only insurance buffer records that are displayed to them

would be entries for eIV confirmed active policies ("+" entries)

when the patient in that record has an active policy on file in

VistA. Other active policies marked with an "\$" eIV symbol will

not be displayed to these users.

b\) Only users with neither of the new security keys (IB INSURANCE

COMPANY EDIT and IB GROUP PLAN EDIT), may use the new action

(ES) ESCALATE ENTRY within the option PROCESS INSURANCE BUFFER

\[IBCN INSURANCE BUFFER PROCESS\].

c\) The "+" eIV symbol of insurance buffer entries that have been

escalated using the new action (ES) ESCALATE ENTRY, will be

replaced with an "\$" eIV symbol.

3\. Disabled the ability to create a new Insurance Company and/or a new

Group/Plan in VistA through the option PROCESS INSURANCE BUFFER \[IBCN

INSURANCE BUFFER PROCESS\].

4\. The name of the VistA file that stores the records for the Insurance

Buffer has been renamed from the "INSURANCE BUFFER" to the

"INSURANCE VERIFICATION PROCESSOR". The file number and file layout

remain the same. The patch includes the DATE ENTERED (#355.33,.01)

field although it was not changed, in order for KIDS to update the

file name of the file \#355.33 on the system where this patch is being

installed.

5\. Modified the daily eIV registration message that is automatically sent

by VistA via a Health Level 7 (HL7) message to the Financial Service

Center (FSC) in Austin, TX. The updated message now includes

additional data regarding the site's current eIV Site Parameter

settings.

6\. Modified the eIV Site Parameters that are viewed/edited using the

option MCCR SITE PARAMETER DISPLAY/EDIT \[IBJ MCCR SITE PARAMETERS\].

a\) The value of the existing FRESHNESS DAYS field (#350.9,51.01),

which controls the days between electronic re-verification checks,

is now controlled by FSC through HL7 messages. This field may no

longer be edited using the option MCCR SITE PARAMETER DISPLAY/EDIT

\[IBJ MCCR SITE PARAMETERS\].

b\) The existing TIMEOUT DAYS field (#350.9,51.05) which controls the

number of days between when an eIV inquiry is sent to FSC and when

the eIV system determines that FSC did not send an eIV response in

time. The value of this existing field is now controlled by FSC

through HL7 messages.

c\) The new RETRY FLAG field (#350.9,51.26) which controls whether

VistA will retransmit an eIV inquiry if an eIV response is not

received from FSC within the value of the TIMEOUT DAYS

(#350.9,51.05). This flag is controlled by FSC.

d\) The value of the existing field HL7 RESPONSE PROCESSING

(#350.9,51.13) is no longer displayed within the eIV Site

Parameters. The value of this field may no longer be edited using

the option MCCR SITE PARAMETER DISPLAY/EDIT \[IBJ MCCR SITE

PARAMETERS\].

7\. Modified VistA's retry methodology (resending inquiries to FSC)

so that any payer's eIV response will be considered a final

response to the eIV inquiry. Prior to this change, payer's eIV

response could result in an eIV inquiry being resent to the payer

(with no modifications to the eIV inquiry) every few days without

actually providing an answer to the eligibility inquiry itself.

8\. The option INSURANCE COMPANY ENTRY/EDIT \[IBCN INSURANCE CO EDIT\] has

been locked with the new security key IB INSURANCE COMPANY EDIT.

9\. The ability to add a new group/plan through the option PATIENT

INSURANCE INFO VIEW/EDIT \[IBCN PATIENT INSURANCE\] has been locked

with the new security key IB GROUP PLAN EDIT.

10\. The option EIV RESPONSE REPORT \[IBCNE IIV RESPONSE REPORT\] has been

modified to include the associated eligibility benefit information.

11\. For the following options, the display of eligibility benefits has

been modified with this patch to include a summary of key elements of

data when available. This summary will contain the Coverage Status

and Coverage Type for all payers that send this information in their

eIV response. When the software determines that the eIV eligibility

data from Medicare payers indicate possible other insurance for that

patient, this information will be included in the summary of key data

elements. This change to the display of eligibility information

applies to the following options:

a\) PROCESS INSURANCE BUFFER \[IBCN INSURANCE BUFFER PROCESS\]

b\) PATIENT INSURANCE INFO VIEW/EDIT \[IBCN PATIENT INSURANCE\]

c\) EIV RESPONSE REPORT \[IBCNE IIV RESPONSE REPORT\]

d\) THIRD PARTY JOINT INQUIRY \[IBJ THIRD PARTY JOINT INQUIRY\]

12\. The EIV STATISTICAL REPORT \[IBCNE IIV STATISTICAL REPORT\] was modified

to include 'Escalated' records in the insurance buffer breakout of the

eIV symbols.

13\. Increased the length of field ORIGINAL SUBSCRIBER ID (#365.1,1.05)

from 20 to 80 characters.

14\. Increased the length of field HL7 SUBSCRIBER ID FIELD (#365.1,.16)

from 20 to 80 characters.

Patch Components

================

Files & Fields Associated:

File Name (#) New/Modified/

Sub-file Name (#) Field Name (Number) Deleted

------------------- --------------------------------- -------------

PATIENT (#2) Modified

INSURANCE TYPE sub-file (#2.312) Modified

REQUESTED SERVICE DATE (#8.01) New

REQUESTED SERVICE TYPE (#8.02) New

IB SITE PARAMETERS (#350.9) Modified

RETRY FLAG (#51.26) New

INSURANCE VERIFICATION PROCESSOR (#355.33) Modified

DATE ENTERED (#.01) Modified

IIV STATUS TABLE (#365.15) Modified

CODE (#.01) Modified

IIV TRANSMISSION QUEUE (#365.1) Modified

HL7 SUBSCRIBER ID FIELD (#.16) Modified

ORIGINAL SUBSCRIBER ID (#1.05) Modified

Mail Groups Associated:

New/Modified/

Mail Group Name Deleted

--------------- -------------

N/A

Options Associated:

New/Modified/

Option Name Type Deleted

----------- ---- -------------

IBCN INSURANCE CO EDIT run routine Modified

Protocols Associated:

New/Modified/

Protocol Name Deleted

------------- -------------

IBCNB ENTRY ESCALATE New

IBCNB ENTRY SCREEN MENU Modified

IBCNB ENTRY VERIFY Delete

IBCNB LIST APPOINTMENTS VIEW Delete

IBCNB LIST COMPLETE VIEW New

IBCNB LIST FAILURE VIEW New

IBCNB LIST SCREEN MENU Modified

Security Keys Associated:

New/Modified/

Security Key Name Deleted

----------------- -------------

IB GROUP PLAN EDIT New

IB INSURANCE COMPANY EDIT New

Templates, Input Associated:

New/Modified/

Template Name Type File Name (Number) Deleted

------------- ---- ------------------ -------------

IBCNE GENERAL Input IB SITE PARAMETERS (#350.9) Modified

PARAMETER EDIT

Templates, List Associated:

New/Modified/

TEMPLATE Name Type Deleted

------------- ---- -------------

IBCNB INSURANCE BUFFER ENTRY List Modified

IBCNB INSURANCE BUFFER LIST List Modified

Additional Information:

New Service Requests (NSRs)

----------------------------

\#20110503 Electronic Data Interchange (EDI) New Standards and Operating

Rules (Veterans Health Administration) VHA Provider-Side TCRs.

Patient Safety Issues (PSIs)

-----------------------------

N/A

Remedy Ticket(s) & Overview

---------------------------

N/A

Test Sites:

----------

REDACTED

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview

------------------------------

Two new security keys were added as a result of this patch. These keys

need to be assigned to the appropriate folks as determined by the site.

a\) The security key IB INSURANCE COMPANY EDIT is to be assigned to users

who are authorized to add new insurance companies in VistA.

b\) The security key IB GROUP PLAN EDIT is to be assigned to users who are

authorized to add new group plans and individual plans in VistA.

There is a post install routine, IBY506PO that is included in this patch.

After the patch has been installed the post install routine may be deleted

by the site.

1\. Initializes several eIV site Parameters

2\. Loops through the IIV TRANSMISSION QUEUE file (#365.1) and performs

the following for all entries with a TRANSMISSION STATUS (#365.1,.04)

that has a value of HOLD.

a\) Changes the TRANSMISSION STATUS (#365.1,.04) to COMMUNICATION

FAILURE.

b\) Identifies all associated entries in the IIV RESPONSE file (#365)

and changes the TRANSMISSION STATUS (#365,.06) to COMMUNICATION

FAILURE unless it currently has the status of RESPONSE RECEIVED.

c\) Identifies any associated insurance buffer entry and changes the

eIV symbol to be "#" and indicate that a communication failure

occurred.

3\. Adds two new entries to the existing IIV STATUS TABLE (#365.15)

4\. A one-time subscriber update utility must be scheduled upon

installation of the patch. Unless the installation is queued, the

post-install will prompt the installer of the patch to schedule this

activity for off-hours. If the installation is queued, the new update

utility will be scheduled for tomorrow at 9 PM. NOTE: This part of

the process does NOT require that IB users be off the system, or

un-scheduling of the eIV Nightly Process \[IBCNE IIV BATCH PROCESS\]

option. A message will be sent to the MailMan mailbox of the installer,

upon successful completion of the subscriber update process. It is

recommended that one look for the MailMan message 24 hours after the

process is scheduled to run.

The subject of the message will be "Subscriber Update Has Completed".

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

-------------------------

This patch may be installed with users on the system although it is

\*strongly\* recommended that it be installed during non-peak hours to

minimize potential disruption to users. This patch should take less

than 5 minutes to install.

The following Menu Options at the site should be disabled during

install:

PROCESS INSURANCE BUFFER \[IBCN INSURANCE BUFFER PROCESS\]

MCCR SITE PARAMETER DISPLAY/EDIT \[IBJ MCCR SITE PARAMETERS\]

INSURANCE COMPANY ENTRY/EDIT \[IBCN INSURANCE CO EDIT\]

PATIENT INSURANCE INFO VIEW/EDIT \[IBCN PATIENT INSURANCE\]

EIV RESPONSE REPORT \[IBCNE IIV RESPONSE REPORT\]

THIRD PARTY JOINT INQUIRY \[IBJ THIRD PARTY JOINT INQUIRY\]

Pre-Installation Instructions

-----------------------------

1\. Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch

IB\*2.0\*506:

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as Data Dictionaries (DD's) or

templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch to install.

5\. 355.33 INSURANCE VERIFICATION PROCESSOR (Partial Definition)

\*BUT YOU ALREADY HAVE 'INSURANCE BUFFER' AS FILE \#355.33!

Shall I write over your INSURANCE BUFFER File? YES//

6\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

Install? YES//YES'

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*IMPORTANT\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

You must answer 'Yes' to the Want KIDS to Rebuild Menu Trees Upon

Completion of Install? YES//' prompt.

Failure to do so will cause the Insurance Buffer to not function

properly until the rebuild runs at night.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

7\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//'

8\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? YES//YES'

When prompted 'Enter options you wish to mark as 'Out Of Order':

Enter the following options one at a time:

PROCESS INSURANCE BUFFER \[IBCN INSURANCE BUFFER PROCESS\]

MCCR SITE PARAMETER DISPLAY/EDIT \[IBJ MCCR SITE PARAMETERS\]

INSURANCE COMPANY ENTRY/EDIT \[IBCN INSURANCE CO EDIT\]

PATIENT INSURANCE INFO VIEW/EDIT \[IBCN PATIENT INSURANCE\]

EIV RESPONSE REPORT \[IBCNE IIV RESPONSE REPORT\]

THIRD PARTY JOINT INQUIRY \[IBJ THIRD PARTY JOINT INQUIRY\]

When prompted 'Enter protocols you wish to mark as 'Out Of Order':

Press the Return or Enter key as there are no protocols that

needs to be marked as 'Out of Order'.

9\. If prompted "Delay Install (minutes): (0 - 60): 0// respond 0.

10\. There is no need to queue the install. At the 'DEVICE' prompt, hit

the return key which will enable the Install to run in the foreground.

a '^' to abort the install.

DEVICE: HOME//

11\. A one-time subscriber update utility must be scheduled upon

installation of the patch. During installation, the post-install

routine prompts for the installer to schedule the one time subscriber

update utility and will not complete installation until it is

scheduled.

The following shows an example of the message and then the date/time prompt

that is generated:

Creating Task to Update the Insurance Type File...

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* IMPORTANT!! \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This option will scan through the entire Patient File for patients with

insurance where the relationship to insured is self. Certain fields in

Insurance Type sub-file will be updated to match the patient data if it

does not already exist. This will take a while and must be queued to run

in the background when there are few users on the system. The default is

tomorrow at 9:00 p.m.

Enter date/time to queue the option: T+1@2100//

Post-Installation Instructions

------------------------------

Post-Installation Instructions

------------------------------

1\. Two new security keys were added as a result of this patch. These keys

need to be assigned to the appropriate folks as determined by the site.

a\. The security key IB INSURANCE COMPANY EDIT is to be assigned to users

who are authorized to add new insurance companies in VistA and/or

users who currently have the IB EDI INSURANCE EDIT security key

assigned to them.

b\. The security key IB GROUP PLAN EDIT is to be assigned to users who are

authorized to add new group plans and individual plans in VistA.

2\. A message will be sent to the MailMan mailbox of the installer,

upon successful completion of the subscriber update process. It is

recommended that one look for the MailMan message 24 hours after the

process is scheduled to run.

The subject of the message will be "Subscriber Update Has Completed".

3\. There is a post install routine, IBY506PO that is included in this

patch. After the patch has been installed the post install routine may

be deleted by the site.

Routine Information:

====================

The second line of each of these routines now looks like:

;;2.0;INTEGRATED BILLING;\*\*\[Patch List\]\*\*;21-MAR-94;Build 74

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: IBCNBAA

Before: B67963575 After: B75234738 \*\*82,184,246,416,506\*\*

Routine Name: IBCNBLA

Before: B65832730 After: B68621473 \*\*82,149,153,184,271,416,506\*\*

Routine Name: IBCNBLA1

Before: B83105620 After:B100917255 \*\*82,133,149,184,252,271,416,

438,506\*\*

Routine Name: IBCNBLL

Before:B101908545 After:B138729075 \*\*82,149,153,183,184,271,345,

416,438,435,506\*\*

Routine Name: IBCNEDE2

Before: B60928994 After: B63879348 \*\*184,271,249,345,416,438,506\*\*

Routine Name: IBCNEDE6

Before: B32414593 After: B33816621 \*\*184,271,345,416,497,506\*\*

Routine Name: IBCNEDEP

Before: B86075479 After: B83976754 \*\*184,271,300,416,438,506\*\*

Routine Name: IBCNEDST

Before: B52803166 After: B47395616 \*\*497,506\*\*

Routine Name: IBCNEHL1

Before:B206919324 After:B215626728 \*\*300,345,416,444,438,497,506\*\*

Routine Name: IBCNEHL3

Before:B168485042 After:B171692667 \*\*300,416,497,506\*\*

Routine Name: IBCNEHL4

Before:B174356077 After:B174792299 \*\*300,416,438,497\*506\*\*

Routine Name: IBCNEHLM

Before: B26579443 After: B28096778 \*\*184,251,300,416,438,497,506\*\*

Routine Name: IBCNEHLT

Before: B77895122 After: B80145618 \*\*184,251,271,300,416,438,506\*\*

Routine Name: IBCNERP8

Before: B66453982 After: B75472595 \*\*184,271,345,416,506\*\*

Routine Name: IBCNERP9

Before:B102330381 After:B103562066 \*\*184,271,416,506\*\*

Routine Name: IBCNERPE

Before: B60593817 After: B65900140 \*\*271,300,416,438,497,506\*\*

Routine Name: IBCNES

Before: B28429551 After: B63081036 \*\*416,438,497,506\*\*

Routine Name: IBCNEUT1

Before: B35326232 After: B44078437 \*\*184,497,506\*\*

Routine Name: IBCNSJ12

Before: B20812349 After: B21606758 \*\*28,62,142,506\*\*

Routine Name: IBCNSJ3

Before: B17659726 After: B19317542 \*\*28,497,506\*\*

Routine Name: IBCNSM3

Before: B14041849 After: B14271242 \*\*6,28,85,211,251,399,506\*\*

Routine Name: IBCNSUR

Before: B23131946 After: B24160231 \*\*103,276,506\*\*

Routine Name: IBCNUPD

Before: B15205533 After: B19970193 \*\*497,506\*\*

Routine Name: IBJPI

Before: B21978399 After: B19548396 \*\*184,271,316,416,438,479,506\*\*

Routine Name: IBY506PO

Before: n/a After: B23493376 \*\*506\*\*

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following features in VistA, Integrated Billing are affected by this effort:

## Enhancements to the Insurance Buffer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Insurance Buffer – Create New ‘Complete Buffer’ (CB) Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides a new view, the ‘Complete Buffer’ (CB) view, within the Insurance Buffer.

### Insurance Buffer – Default View to be the ‘Complete Buffer’ (CB) Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Process Insurance Buffer \[IBCN INSURANCE BUFFER PROCESS\] option defaults to the ‘Complete Buffer’ (CB) view.

### Insurance Buffer – ‘Complete Buffer’ Screen Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contains all of the records found on the other Insurance Buffer views.

### Insurance Buffer – ‘Complete Buffer’ Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides the user with the same actions as found on the Positive Buffer view.

### Insurance Buffer – Ability to Jump to the ‘Complete Buffer’ Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides the capability to jump to the ‘Complete Buffer’ (CB) screen.

### Insurance Buffer – ‘Positive Buffer’ Screen Fix Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contains only non-Medicare records that meet any of the following criteria:

- Non-Medicare records that have an eIV symbol of “+”
- Non-Medicare records that have an “\*” that previously had an eIV symbol of “+”
- Non-Medicare records that have an “\*” with no current or past eIV symbol
- Non-Medicare records that have a “\$” symbol

### Insurance Buffer – ‘Medicare Buffer’ Screen Fix Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contains only Medicare records regardless of the eIV symbol.

### Insurance Buffer – ‘Negative Buffer’ Screen Fix Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contains only non-Medicare records that meet any of the following criteria:

- Non-Medicare records that have an eIV symbol of “-“
- Non-Medicare records that have an “\*” that had an eIV symbol of “-“

### Insurance Buffer – Remove ‘Future Appointments’ Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ‘Future Appointment’ view has been removed from the Insurance Buffer.

### Insurance Buffer – Create New ‘Failure Buffer’ (FB) Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ‘Failure Buffer’ (FB) view is available from within the Insurance Buffer.

### Insurance Buffer – ‘Failure Buffer’ Screen Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contains non-Medicare records having an eIV symbol of “!” only.

### Insurance Buffer – ‘Failure Buffer’ Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Allows the user to perform the same actions as the ‘Positive Buffer’ view.

### Insurance Buffer – Remove ‘Verify Entry’ Action from the Buffer Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can no longer select the action ‘Verify Entry’ from within the Insurance Buffer.

### Insurance Buffer – Filter Insurance Buffer Records Based on User’s Security Keys (Revised)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All Insurance Buffer views show users (who do NOT have either the new insurance edit key or the new group/plan edit key) only those NON-MEDICARE buffer records that have an eIV symbol of “+” and the patient identified on the buffer record has at least one active policy on their insurance records. (The insurance company name has no part in this comparison.)

- In other words: the user would see the same things on the complete buffer view and the positive view, while all other views will be empty of records.

### Insurance Buffer – Ability to Jump to the ‘Failure Buffer’ Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the views within the Insurance Buffer contain the ability to jump to the ‘Failure Buffer’ (FB) screen.

### Insurance Buffer – Remove Ability to Create New Insurance Company

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user no longer has the ability to create a new insurance company from within the Insurance Buffer.

### Insurance Buffer – Remove Ability to Create New Group/Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user no longer has the ability to create a new group/plan from within the Insurance Buffer.

### Insurance Buffer – Rename the Insurance Buffer File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA ‘Insurance Buffer’ (#355.33) file is now named the ‘Insurance Verification Processor’ (#355.33).

### Insurance Buffer – Create Insurance Buffer Entry for Appointments with Nationally Inactive Payers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system creates an Insurance Buffer record with a blank eIV symbol for instances in which the eIV appointment extract would have created an eIV inquiry except for the fact that the payer is nationally inactive.

### Insurance Buffer – Add “Escalate” Action to the Buffer Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the new action, “Escalate”.

### Insurance Buffer – Restrict use of the “Escalate” Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“Escalate” can only be used by users who do NOT have either the new insurance edit key or the new group/plan edit key.

### Insurance Buffer – Implement the “Escalate” Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“Escalate” replaces the “+” symbol with a “\$” for the selected insurance buffer entry to indicate that the policy on the insurance buffer record cannot be processed by that user.

## System Feature: eIV – HL7 Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### eIV HL7 Transactions - Daily Registration Message to FSC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system transmits the following data to FSC daily via the eIV Registration message:

- The value of Freshness Days (#350.9,51.01)
- The value of Timeout Days (#350.9,51.05)
- The value of Retry Flag (#350.9,51.26)

### eIV HL7 Transactions – Receive Retry Flag from FSC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides users with the ability to receive the Retry flag when received as an eIV table update message (HL7 MFN^M01).

### eIV HL7 Transactions – Store Retry Flag from FSC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides users with the ability to store the Retry flag within the IB Site Parameters file.

### eIV HL7 Transactions – Receive Freshness Days from FSC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides users with the ability to receive the Freshness Days when received as an eIV table update message (HL7 MFN^M01).

### eIV HL7 Transactions – Store Freshness Days from FSC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides users with the ability to store the Freshness Days within the IB Site Parameters file.

### eIV HL7 Transactions – Receive Timeout Days from FSC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides users with the ability to receive the Timeout Days when received as an eIV table update message (HL7 MFN^M01).

### eIV HL7 Transactions – Store Timeout Days from FSC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides users with the ability to store the Timeout Days within the IB Site Parameters file.

### eIV HL7 Transactions – Treat all AAA Action Codes as Though the Payer/FSC Responded

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV system does NOT resend an inquiry for any X12 271 message that contains an error action code and treats the X12 271 as having received an answer to the X12 270 inquiry.

### eIV HL7 Transactions – Honor the Retry Flag when Resending an eIV Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV system only resends an X12 270 message (eIV inquiry) if the Retry flag is set to YES and all other criteria is met.

### eIV HL7 Transactions – Honor the Timeout Days when Resending an eIV Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV system only resends an X12 270 message (eIV inquiry) if it has been at least the number of Timeout Days since the last time the eIV inquiry was sent to FSC and all other criteria is met.

### eIV HL7 Transactions – Honor the ‘NUMBER RETRIES’ when Resending an eIV Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV system only resends an X12 270 message (eIV inquiry) if the number of times an eIV inquiry was resent to FSC is less than the ‘NUMBER RETRIES’ allowed and all other criteria is met.

### eIV HL7 Transactions – Honor the Payer’s Nationally Active Flag when Resending an eIV Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV system only resends an X12 270 message (eIV inquiry) if the payer defined in the eIV inquiry is currently Nationally Active and all other criteria is met.

### eIV HL7 Transactions – Do Not Send MailMan Message When Retries are Exhausted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV system does not send a MailMan message when the number of retries for a missing X12 271 message (eIV response) has been exhausted.

## System Feature: eIV Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### eIV Site Parameters – Retry Flag Not Editable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV Site Parameters do not display the Retry Flag.

### eIV Site Parameters - Freshness Days Not Editable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the Freshness Days as viewable only.

### eIV Site Parameters – Timeout Days Not Editable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV Site Parameters do not display the Timeout Days.

### eIV Site Parameters – Set the Value of ‘NUMBER RETRIES’ Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV Site Parameter, ‘NUMBER RETRIES’, is initially defined as having a value of “1.”

### eIV Site Parameters – Set the Initial Value of the Retry Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV Site Parameter, ‘Retry Flag’, is initially defined as having a value of “No.”

### eIV Site Parameters – Set the Initial Value of the Freshness Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV Site Parameter, ‘Freshness Days’, is initially defined as having a value of “180”.

### eIV Site Parameters – Set the Initial Value of the Timeout Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV Site Parameter, ‘Timeout Days’, is initially defined as having a value of “5.”

### eIV Site Parameters - Set the Value of the ‘HL7 Response Processing’ Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV Site Parameter, ‘HL7 Response Processing’ field is initially defined as having a value of ‘immediate’.

### eIV Site Parameters – ‘HL7 Response Processing’ Field Not Editable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV Site Parameters does not display the ‘HL7 Response Processing’ field.

### eIV Site Parameters – Restrict eIV Number of Possible Retries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV Site Parameter, ‘NUMBER RETRIES’ field is defined as having a value of ‘1’.

## System Feature: Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Security Key – Create New Key to Add/Edit an Insurance Company

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Includes a new IB security key to control edits/additions to records in VistA’s Insurance Company file.

### Security Key – Lock the “Insurance Company Entry/Edit” Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restricts the ability to add/edit an insurance company through the “Insurance Company Entry/Edit” \[IBCN INSURANCE CO EDIT\] option to only users with the new IB INSURANCE COMPANY EDIT security key.

### Security Key – User Requires Key to Add/Edit Insurance Company in the Insurance Buffer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restricts the ability of users to add/edit an insurance company through the Insurance Buffer to only those users with the new IB INSURANCE COMPANY EDIT security key.

### Security Key – Create New Key to Add/Edit a Group/Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Includes a new IB security key to control edits/additions to records in VistA’s Group Insurance Plan file.

### Security Key – User Requires Key to Add/Edit Group/Plan in the Buffer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restricts the ability of users to add/edit a Group/Plan through the Insurance Buffer to only those users with the new IB GROUP PLAN EDIT security key.

### Security Key – Lock the Ability to Create a Group/Plan within ‘Patient Insurance Info View/Edit’ Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restricts the ability of users to add/edit a Group/Plan through the ‘Patient Insurance Info View/Edit’ option to only those users with the new IB GROUP PLAN EDIT security key.

## System Feature: Eligibility Benefits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Eligibility Benefits – Update the Eligibility Benefit Information Accessed via the ‘Process Insurance Buffer’ option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the newly formatted eligibility benefit information when accessed by the ‘Process Insurance Buffer’ option.

### Eligibility Benefits – Update the Eligibility Benefit Information Accessed via the ‘TPJI’ Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the newly formatted eligibility benefit information when accessed by the ‘TPJI’ option.

### Eligibility Benefits – Update the Eligibility Benefit Information Accessed via the ‘Patient Insurance Info View/Edit’ Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the newly formatted eligibility benefit information when accessed by the ‘Patient Insurance Info View/Edit’ option.

### Eligibility Benefits – Include the Eligibility Benefit Information on the eIV Response Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the eligibility benefit information that is associated with the X12 271 response on the eIV Response Report.

### Eligibility Benefits – Store the Service Date on the Patient’s Policy Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Stores on the patient’s record the Service Date associated with the eligibility benefits when eligibility benefits are saved from the Insurance Buffer to the patient’s policy.

### Eligibility Benefits – Store the Service Type on the Patient’s Policy Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Stores on the patient’s record the Service Type that was inquired about when eligibility benefits are saved from the Insurance Buffer to the patient’s policy.

### Eligibility Benefits – Display the Service Date of the Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the service date the payer responded to at the top of the Eligibility Benefit section above the insurance status.

### Eligibility Benefits – Display the Service Type of the Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the service type inquired about at the top of the Eligibility Benefit section above the insurance status.

### Eligibility Benefits – Eligibility Benefit (1st Priority Sort Order): Insurance Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the insurance status of the policy found within the eligibility benefit data at the top of the Eligibility Benefit section.

### Eligibility Benefits - Eligibility Benefit (2nd Priority Sort Order): Insurance Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Displays the insurance type of the policy, when available, that is found in the eligibility benefit data as the second data element of the Eligibility Benefit section.

### Eligibility Benefits – Eligibility Benefit (3<sup>rd</sup> Priority Sort Order): Coordination of Benefits (COB) (Removed – 08/01/2013)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Eligibility Benefits - Eligibility Benefit (4th Priority Sort Order): Indication of Other Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Indicates possible other insurance as the fourth data element of the Eligibility Benefit section, only if the payer’s response contains potential additional insurance.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: IB*2*549 Release Notes/Installation Guide

## Overview of Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not able to be a “one size fits all” solution. The general strategy for a VistA rollback is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch. If not, the site should contact the product support team directly for specific solutions to their unique problems.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA installation procedure of the KIDS build, the installer can back up the modified routines using the ‘Backup a Transport Global’ action. The installer can restore the routines using the MailMan message that was saved prior to the installation of the patch. The backout procedure for global, data dictionary and other VistA components is more complex and will require issuance of a follow-up patch to ensure all components are properly removed. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with the restoration of the data. This backout process may need to include a database cleanup process.

Please contact the product support team for assistance if the installed patch that needs to be backed out contains anything at all besides routines before trying to backout the patch. If the installed patch that needs to be backed out includes a pre or post install routine, please contact the product support team before attempting the backout.

From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following option:

- Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.

> **NOTE:** When prompted for the INSTALL enter the patch \#.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure for VistA patches is complicated and may require a follow-up patch to fully roll back to the pre-patch state. This is due to the possibility of Data Dictionary updates, Data updates, cross references, and transmissions from VistA to offsite data stores.

Please contact the product development team for assistance if needed.

## Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following features of the IB software will be affected by this project.

### Electronic Insurance Verification (eIV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following modifications have been made to eIV:

- eIV data extracts and eIV Request Electronic Insurance Inquiry.
  - eIV Appointment extract will include Prescription only coverages.
  - eIV Appointment extract will include Prescription type of plans.
  - eIV Appointment extract will exclude specific types of coverages.
  - eIV Appointment extract will exclude specific types of plans.
  - eIV Request Electronic Insurance Inquiry will allow inquiries for deceased patients, but will not use Date of Death (DOD) as the service date.
- eIV processing and transmission:
  - eIV Auto Update will only update active policies.
  - "IIV EC" Health Level Sever (HL7) logical link will use a domain name.

### Integrated Billing Screen Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This project made modifications to several screens in Integrated Billing:

- Date of Death:
  - When a patient is marked as deceased in Veterans Health Information Systems and Technology Architecture (VistA), their active policies will automatically be termed.
  - Patient Policy information screen will reflect the patient's date of death.
- Security Key:
  - Existing "IB GROUP PLAN EDIT" security key is required to edit Coverage Limitations (action CV) within:
    - The Insurance Company Entry/Edit option on the Insurance Company screen.
    - The Patient Insurance Info View/Edit option on the Patient Insurance screen.
  - Existing "IB GROUP PLAN EDIT" security key is required to edit Annual Benefits (action AB) within:
    - The Insurance Company Entry/Edit option on the Insurance Company screen.
    - The Patient Insurance Info View/Edit option on the Patient Insurance screen.
  - Existing "IB GROUP PLAN EDIT" security key is required to edit Change Plan Info (action PI) within:
    - The Insurance Company Entry/Edit option on the Insurance Company screen.
    - The Patient Insurance Info View/Edit option on the Patient Insurance screen.
  - Existing "IB GROUP PLAN EDIT" security key is required to edit UR Info (action UI) within:
    - The Insurance Company Entry/Edit option on the Insurance Company screen.
    - The Patient Insurance Info View/Edit option on the Patient Insurance screen.
  - Existing "IB GROUP PLAN EDIT" security key is required to Inactivate a Plan (action IP) within:
    - The Insurance Company Entry/Edit option on the Insurance Company screen.
    - The Patient Insurance Info View/Edit option on the Patient Insurance screen.
  - Existing "IB GROUP PLAN EDIT" security key is required to Edit Comments (action PC) within the Insurance Company Entry/Edit option on the Insurance Company screen.
  - Existing "IB GROUP PLAN EDIT" security key is required to Fast Edit All (action EA) plan specific information within the Patient Insurance Info View/Edit option on the Patient Insurance screen.
- Process Insurance Buffer option and eIV Response data:
  - Insurance Buffer will no longer allow a user to directly access the eIV Response Report via RR action.
  - Insurance Buffer's expand benefit (action EB) will include additional eIV Response data.
  - Insurance Buffer's accept entry (action AE) process will allow acceptance of additional eIV Response data.
  - Insurance Buffer will display all Medicare entries to all users.
- Patient Insurance screen (Patient Insurance Info View Entry/Edit option):
  - Patient Insurance screen will display additional eIV Response data.
  - "Policy Not Billable" prompt will be modified to “Stop Policy From Billing” to make it more clear to the user.
- Insurance Company screen (Insurance Company Entry/Edit option):
  - The Expand Benefits action (EB) will display additional eIV Response data.
- Enhance VistA Insurance Capture Buffer (ICB):
  - ICB will not create a new insurance company if the user lacks the proper security key.
  - ICB will not create a new group plan if the user lacks the proper security key or it already exists.
- Enhance VistA Data Dictionary (DD):
  - Create new entry in the file TYPE OF INSURANCE COVERAGE (#355.2).
  - Create new entry in the file TYPE OF PLAN (#355.1).

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This project created or modified the following reports:

- List Plans by Insurance Company report:
  - Added additional filters.
  - Modified the report layout.
- Patients without Medicare Insurance report:
  - Modified user prompts.
  - Added a new filter based on appointment date.
  - Modified the report layout.
- Active Policies with no Effective Date report:
  - Added additional filters.
  - Modified the report layout.
- eIV Auto Update Report (currently known as the eIV Patient Insurance Update Report):
  - Renamed eIV Patient Insurance Update report to eIV Auto Update Report.
  - Updated the user prompts.
  - Modified the report to display only those patient insurance entries that were updated by eIV Auto Update.
  - Modified the report layout.
- Creation of new Insurance Plans Missing Data report:
  - Create new report that allows a user to search for missing data within active insurance companies.
  - Users may search the following fields in the GROUP INSURANCE PLAN file (#355.3) looking for missing data:
    - GROUP NUMBER (#2.02).
    - TYPE OF PLAN (#.09).
    - PLAN STANDARD FTF (#.16).
    - PLAN STANDARD FTF Value (#.17).
    - ELECTRONIC PLAN TYPE (#.15).
    - BANKING IDENTIFICATION NUMBER (#6.02).
    - PROCESSOR CONTROL NUMBER (PCN) (#6.03).
  - Users may search for missing plan coverage limitations that are found in the PLAN COVERAGE LIMITATIONS file (#355.32).
- Modifications to the worklist, Move Subscribers to a Different Plan:
  - Added functionality so that a user may move individual patients instead of an entire group if they desire.
  - Added additional user prompts.

### Patient Policy Comment Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following modifications have been made to Patient Policy Comments:

- Insurance Comments (Patient Insurance Info View Entry/Edit option):
  - Provided ability to capture additional data for patient policy comments.
  - Removed the "Insur. Contact Inf. (IC)" action from the Patient Policy Information screen.
  - Removed the Insurance Comment (last) section from the Patient Policy Information screen.
  - Added new "Group Plan Comment (GC)" action to the Patient Policy Information screen.
  - Added ability for users to view the historical list of patient policy comments.
  - Provided search functionality for historical patient policy comments.
- Insurance Comments (Claims Tracking screens/options):
  - Added new "Pt Policy Comments (PT)" action to claims tracking screens.
  - Added ability for users to view the historical list of patient policy comments.
- Insurance Comments (Third Party Joint Inquiry (TPJI) option):
  - Added new "Pt Policy Comments (PT)" action to TPJI when PATIENT NAME is selected. Selecting by BILL NUMBER in TPJI has not been modified.
  - Added ability for users to view the historical list of patient policy comments.

### IV Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following modifications have been made to IV Site Parameters:

- IV Site Parameters:
  - Redesigned user screen.
  - Allows edit functionality of the following data elements:
    - Medicare Payer.
    - HMS Directory.
    - EII Active
  - Displays in view only mode:
    - Retry Flag.
    - Timeout Days.
    - Timeout Mailman Msg.
    - Number Retries.
    - Default Service Type Code.
    - HL7 Maximum Number.
  - Removed functionality of the following data elements:
    - Contact Person.
    - Contact's phone number.
    - Contact's email address.
  - Added the following new data elements:
    - Master Switch Realtime.
    - Master Switch Nightly.
  - Removed edit abilities for the data elements:
    - Failure Mailman Msg.
    - Messages Mailgroup.

### National Insurance File Interface Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following modifications have been made to the National Insurance File Interface:

- Sending HL7 messages to the NIF:
  - VistA now checks the IB NIF TCP entry in the HL7 logical link and verifies that it is up and running. An email is generated and sent to VHAeInsuranceRapidResponse@va.gov when the IB NIF TCP entry needs to be restarted/bounced.

## Issue Resolutions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch addresses the following New Service Request (NSR):

NSR 20140413 - Medical Care Collection Fund (MCCF) eInsurance Compliance Phase 3

### Defect Tracking System Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no defect tracking system tickets associated with this patch.

### From: IB*2*547 Release Notes/Installation Guide

### Enter/Edit Billing Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Make any necessary changes to the logic for determining Current Procedural Terminology (CPT)/Healthcare Common Procedure Coding System (HCPCS) code service lines and revenue codes to ensure that identical codes either:
  - Combine and calculate the correct number of units – no Print Order
  - Do not combine – Print Order
- Remove the fatal error that prevents the authorization of a claim for a patient with only a last name in the Patient file
- Remove the fatal error that prevents the authorization of a claim for a subscriber with only a last name
- Remove the obsolete Present on Admission (POA) code option of Blank/Exempt from POA Reporting

### Printed Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add the ability to print the amount paid on a claim by the previous payer(s) in Box 29 of the CMS-1500 claim form when a secondary/tertiary claim is printed locally
- Remove the printing of the admission date and time from the UB04 claim form (FL12/13) when an outpatient, institutional claim is printed locally
- Remove the printing of the discharge time from the UB04 claim form (FL16) when an outpatient, institutional claim is printed locally

### Insurance Company Entry/Edit/View Insurance Company

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add the ability to define multiple Additional Primary Payer Identification numbers for an insurance company for the purpose of routing claims to different administrative contractors for both Medicare Will Not Reimburse (WNR) and commercial \[non-Medicare (WNR)\] insurance companies
- Add the ability to view what is defined as the insurance company addresses in Insurance Company Entry/Edit and View Insurance Company even if the address is incomplete or blank
- Add the ability to define a Utilization Management Organization (UMO) identifier to be transmitted in the X12N 5010 Health Care Services Review – Request for Review and Response (278) transaction

### Integrated Billing Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add a parameter that controls how long the VistA system will store American Standard Code (ASC) X12N Health Care Claim Request For Additional Information (277) transactions (default = infinity)
- Add a parameter that controls how long an ASC X12N Health Care Claim Request For Additional Information (277) transaction will display on the ASC X12N Health Care Claim Request For Additional Information (277) worklist
- Add the ability to maintain a list of revenue codes that will be used to make some printed claims exempt from tracking
- Add ability to define Alternate Primary Payer ID Types to be used to qualify Alternate Primary Payer IDs

### Claims Status Awaiting Resolution (CSA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add the ability to view through CSA, the Health Care Clearing House (HCCH) that sent a Claim Status (277) message for a claim when the message source is an HCCH

### Third Party Joint Inquiry (TPJI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add the ability to view through TPJI, the HCCH that sent a Claim Status (277) message for a claim when the message source is an HCCH
- Modify the Electronic Explanation of Benefits (EEOB) view within the Claim Information action to display the Claim Adjustment Reason Codes (CARCs) and Remittance Advice Remark Codes (RARCs) descriptions from the new AR EDI CARC DATA and AR EDI RARC DATA files (345 and 346)
- Add the ability to view comments added to the Request for Additional Information (RFAI) Worklist for a claim

### EDI Menu For Electronic Bills ... 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Modify the Electronic Explanation of Benefits (EEOB) to display the Claim Adjustment Reason Codes (CARCs) and Remittance Advice Remark Codes (RARCs) descriptions from the new AR EDI CARC DATA and AR EDI RARC DATA files (345 and 346) from the following locations:
- Print EOB \[IBCE PRINT EOB\]

### View/Resubmit Claims - Live or Test (RCB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add the ability to look up claims for an insurance company by Electronic Data Interchange (EDI) Payer ID in addition to the name of the insurance company
- Add the ability to search for claims that were previously printed and transmit them via the test queue

### Medicare Management Worklist (MRW)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Modify the EEOB view to display the CARCs and Remittance Advice Remark Codes (RARCs) descriptions from the new AR EDI CARC DATA and AR EDI RARC DATA files (345 and 346) from the following options:
- View MRA EOB \[IBCEM VIEW MRA EOB\]
- MRW \[IBCE MRA MANAGEMENT\]

### Billing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add the ability to track claims that are printed locally based on specific search criteria for CPAC and TRICARE/CHAMPVA claims
- Modify the Re-generate Unbilled Amounts Report \[IBT RE-GEN UNBILLED REPORT\] summary to display the summary totals before divisional totals and to provide the ability to select whether or not the report is sorted by division

### Copy and Cancel (CLON)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Modify the existing logic associated with copying a claim to ensure the Coordination of Benefits (COB) data associated with the cancelled claim is associated with the new copy

### COB Management Worklist (CBW)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add the ability to search for claims on the COB Management Worklist by payer sequence and to sort the claims by payer sequence
- Modify the EEOB to display the CARCs and RARCs descriptions from the new CARC and RARC files (344 and 345) from the following CBW actions:
- Print EOB/MRA
- View EOB

### Request For Additional Information Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add the ability to view and manage manually, requests for additional claim information (ASC X12N Health Care Claim Request For Additional Information (277) transactions) received from payers

### ASC X12N Health Care Claim (837) Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add the ability to transmit all claims with a rate type for which the insurer is responsible in an ASC X12N Health Care Claim (837) transaction
- Add the ability to transmit up to 25 procedures codes in an institutional ASC X12N Health Care Claim (837) transaction
- Add the ability to transmit up to 12 External Cause of Injury diagnosis codes in an institutional ASC X12N Health Care Claim (837) transaction
- Modify the ASC X12N Health Care Claim (837) layout to include maximum allowable data element lengths for the insurance fields whose lengths were increased by the eInsurance Patch IB\*2\*497
- Modify the ASC X12N Health Care Claim (837) layout to only transmit an admission date on inpatient claims
- Modify the ASC X12N Health Care Claim (837) layout to only transmit a discharge date/time on inpatient claims

### ASC X12N Health Care Claim Request For Additional Information (277) Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add the ability to receive a ASC X12N Health Care Claim Request For Additional Information (277) equivalent transaction from FSC

### New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch addresses the following New Service Request (NSR):

NSR 20140414 - Medical Care Collection Fund (MCCF) eBilling Compliance Phase 3.\\

### Defect Tracking System Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Remedy Ticket \#1262831 is associated with this patch.

Problem:

Re-Generate Unbilled Amounts Report \[IBT RE-GEN UNBILLED REPORT\].

After install of IB\*2\*516 the last 3 columns of the report for CPT, I. Rate, and P. Rate no longer display data.

Resolution:

Problem is corrected with the installation of this patch. The Re-generate Unbilled Amounts report summary is modified to display the summary totals before divisional totals and to provide the ability to select whether or not the report is sorted by

division.

### CA SDM Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CA SDM Ticket \# I6528186FY16 is associated with this patch.

Problem:

--------

If the user selects to sort the CBW (COB Management Worklist) by

Secondary Insurance Company, when the worklist displays the Secondary

Insurance Company name in the header is incorrect.

Resolution:

-----------

Corrected with the install of this patch. The IBCAPP2 routine was

incorrectly assuming for secondary claims where Medicare was the insurer,

that the tertiary insurance company was the current insurance company

name to use in the header.

### From: IB*2*497 Release Notes/Installation Guide

## Documentation Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new and modified functionality introduced by this patch is available.

The preferred method is to FTP the files from REDACTED This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

Albany REDACTED REDACTED

Hines REDACTED REDACTED

Salt Lake City REDACTED REDACTED

Documentation can also be found on the VA Software Documentation Library

at:http://WWW.va.gov/vdl/

Title File Name FTP Mode

-----------------------------------------------------------------------

Release Notes/Installation Guide ib_2_p497_rn.pdf Binary

eIV User Guide ib_2_p497_eIV_ug.pdf Binary

EIV Technical Manual/Security Guide ib_2_p497_eIV_tm.pdf Binary

IB User Manual ib_2_p497_um.pdf Binary

IB Technical Manual ib_2_p497_tm.pdf Binary

*(This page included for two-sided copying.)*

## Process Insurance Buffer \[IBCN INSURANCE BUFFER PROCESS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- AAA Errors – Response Report

> Provides the ability for users to view the Error Reporting Codes and corresponding textual description in the Response Report View of the Insurance Buffer when an error Reporting Code is received in response to an X12N/5010 Health Care Eligibility Benefits Inquiry (270).

- X12N/5010 271 Code Sets – Expanded Benefits

> Provides the ability to receive the all Codes and Qualifiers in Expanded Benefits when received in an X12N/5010 Health Care Eligibility Benefits Response (271) without validation.

- X12N/5010 271 Code Sets – Expanded Benefits

> Provides the ability to store the all Codes and Qualifiers in Expanded Benefits when received in an X12N/5010 Health Care Eligibility Benefits Response (271) without validation.

- X12N/5010 271 Code Sets – Expanded Benefits

> Provides the ability to display the all Codes and Qualifiers in Expanded Benefits when received in an X12N/5010 Health Care Eligibility Benefits Response (271) without validation.

## HL7 Transactions Related to 270/271 Transactions/Daily Registration Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Daily Statistics to FSC

> Transmits additional statistical information in the daily eIV registration message (HL7 MFN message) to the FSC in Austin, Texas.

- 270 - Transmit Insured Name – Patient Subscriber

> Transmits the NAME OF INSURED Field (2.312:17) in the PID segment of the 270 HL7 message when the patient is the subscriber and there is a value in the NAME OF INSURED field.

- 270 - Transmit Patient Name – Patient Subscriber

> Transmits the NAME Field (2: .01) in the PID segment of the 270 HL7 message when the patient is the subscriber and there is no value in the Name of Insured field.

- 270 - Transmit Patient Name – Patient Not Subscriber

> Continues to transmit the NAME Field (2: .01) in the PID segment and the NAME OF INSURED field in the GT1 segment (2.312:17) of the 270 HL7 message when the patient is not the subscriber.

- 270 - Extract – Default Service Type Codes

> Automatically includes the 30-Health Benefit Plan Coverage default Service Type code replacing the current list of codes in the NTE segment of the 270 HL7 messages transmitted automatically through the buffer extract.

- 270 – Receive EB\*V~MSG\*additional Error Message Text~ – AAA Error Message Text

> Provides the ability to receive the AAA additional Error Message Text when received in an X12N/5010 Health Care Eligibility Benefits Response.

- 270 – Store EB\*V~MSG\*additional Error Message Text~ – AAA Error Message Text

> Provides the ability to store the AAA additional Error Message Text when received in an X12N/5010 Health Care Eligibility Benefits Response.

- 270 – Display EB\*V~MSG\*additional Error Message Text~ – AAA Error Message Text

> Provides the ability to display the AAA additional Error Message Text on the Response Report View of the Insurance Buffer when received in an X12N/5010 Health Care Eligibility Benefits Response.

- 270 – Transmit Registration Message after initial installation of the Patch

> Transmits a registration message upon initial installation of the software into production at each VAMC informing FSC of the upgrade to the new interface version.

## Patient Insurance Info View/Edit \[IBCN PATIENT INSURANCE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Update Subscriber Information

> Includes a new option required to be scheduled to update the subscriber fields in the Insurance Type file, with the values stored in the Patient file, upon installation of the software at a site when the patient’s relationship to the insured is self (18) and the field is blank and the insurance policy is Active.

## MCCR System Definition Menu \[IB SYSTEM DEFINITION MENU\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Add New Option for Subscriber Information

> Includes a new option to provide the ability for users holding the IB SUPERVISOR KEY to update subscriber fields in the Insurance Type sub-file for all patients, with the values stored in the Patient file, when the patient’s relationship to the insured is self (18) and the field is blank and the insurance policy is Active.

- Store Default Service Type Codes

> Stores only Service Type Code 30 – Health Benefit Plan Coverage in the IB Site Parameters file accessible from \[MCCR Site Parameter Display/Edit\].

- Site-defined Service Type Codes

> No longer allow users to define Service Type codes by site, to be included automatically in 270 HL7 messages.

- Remove Existing Site-defined Service Type Codes

> Updates the IB Site Parameters file (350.9) to remove all site-defined Service Type codes after the software is installed.

- Site-defined Service Type Codes Screen Display

> No longer contains a section on the \[MCCR Site Parameter Display/Edit\] ListManager screen to display Service Type codes by site.

## Medicare Insurance Intake \[IBCN MEDICARE INSURANCE INTAKE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Remove Medicare Insurance Intake Option

> No longer provides the ability for users to enter Patient Insurance information through the Medicare Insurance Intake option, \[IBCN MEDICARE INSURANCE INTAKE\].

## Integrated Billing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]
- Claims Tracking Edit \[IBT EDIT BI TRACKING ENTRY\]
- Patient Insurance Info View/Edit \[IBCN PATIENT INSURANCE\]
- Process Insurance Buffer \[IBCN INSURANCE BUFFER PROCESS\]
- eIV Response Report \[IBCNE IIV RESPONSE REPORT\]
- eIV Ambiguous Policy Report \[IBCNE IIV AMBIGUOUS POLICY RPT\]
- eIV Inactive Policy Report \[IBCNE IIV INACTIVE POLICY RPT\]

## Request Electronic Insurance Inquiry \[IBCNE REQUEST INQUIRY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Eligibility Date Criteria
- Eligibility Date Default
- Eligibility Date Transmission
- 270 Individual Request - Default Service Type Codes
- 270 Individual Request - Default Service Type Codes

### From: IB*2*517 Release Notes/Installation Guide

## System Feature: 278X217 – Health Care Services Review – Creation and Transmission of Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create and transmit Accredited Standards Committee (ASC) X12N 5010 Health Care Services Review - Request for Review and Response (278X217) transactions to the Financial Services Center (FSC).

## System Feature: 278X217 – Health Care Services Review – Receiving, Storing and Displaying of Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Receive, store and display ASC X12N 5010 Health Care Services Review - Request for Review and Response (278X217) transactions that come back from payers.

## System Feature: 278X215 – Health Care Services Review – Creation and Transmission of Inquiry and Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create and transmit ASC X12N 5010 Health Care Services Review - Inquiry and Response (278X215) transaction to FSC for a previously submitted ASC X12N 5010 Health Care Services Review - Request for Review and Response (278X217) request once an ASC X12N 5010 Health Care Services Review - Request for Review and Response (278x217) transaction returns with a pending status.

## System Feature: 278X215 – Health Care Services Review – Receiving, Storing and Displaying of Inquiry and Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Receive, store and display ASC X12N 5010 Health Care Services Review - Inquiry and Response (278X215) transactions that return from payers.

## System Feature: Create New Claims Tracking Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create new claims tracking site parameters \[IBJ MCCR SITE PARAMETERS\] for the search of the appointments and the admissions.

## System Feature: Create New Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create new security key \[IB HCSR PARAM EDIT\] to add/edit claims tracking site parameters.

## System Feature: Create New Health Care Services Review Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a new worklist \[IBT HCSR WORKLIST\] for future appointments, future admissions, past appointments and past admissions based on site parameters.

## System Feature: Create a Health Care Services Review Worklist Trigger to Request for Review and Response 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the ability to trigger ASC X12N 5010 Health Care Services Review - Request for Review and Response (278X217) transaction from the worklist.

## System Feature: Create a Health Care Services Review Worklist Trigger to Request for Inquiry and Response 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the ability to trigger ASC X12N 5010 Health Care Services Review - Inquiry and Response (278X215) transaction from the worklist.

## System Feature: 278 Health Care Services Review – Worklist – Add Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the ability for users to add an entry to the HCSR Worklist.

## System Feature: 278 Health Care Services Review – Worklist – Deletion Reason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the ability for users to add a reason for the deletion of an entry on the HSCR Worklist.

## System Feature: 278 Health Care Services Review - Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the ability for users to choose between deleting data or saving data when they exit before completing an X12N Health Care Service Review request (278X217) transaction.

## System Feature: 278 Health Care Services Review - Worklist – View Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the ability to view the data \[IBT HCSR RESPONSE VIEW\] that was transmitted in an ASC X12N Health Care Services Review-Request (278) transactions.

## System Feature: Create Health Care Services Review Response Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a Response worklist \[IBT HCSR WORKLIST\] of 278 response messages received for all ASC X12N 5010 Health Care Services Review -Request for Review and Response (278x217) and all ASC X12N 5010 Health Care Services Review - Inquiry and Response (278x215) messages submitted.

## System Feature: Automatically add the Authorization Number(s) to Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the ability to automatically add the authorization number(s) to claims.

## System Feature: Claims Tracking - Insurance Review - Authorizations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the ability to automatically add an Authorization Number that is received in an Health Care Service Review response (278X217) transaction to the Insurance Review for a Claims Tracking event at the following times:

\* When the final 278 is received if the billable event already exists in Claims Tracking.

\* When the billable event is added to Claims Tracking if the Authorization Number was received prior to the event being added to Claims Tracking.

## System Feature: 278 Health Care Services Review – Reports (278x217)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide statistical reporting of the ASC X12N Health Care Services Review-Request for Review and Response (278x217) transactions.

## Systems Feature: 278 Health Care Services Review – Reports (278x215)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide statistical reporting of the ASC X12N Health Care Services Review-Inquiry for Review and Response (278x215) transactions.

## System Feature: 278 Health Care Services Review - Table Maintenance – Payer IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the ability to send the 278 Payer IDs to be used for ASC X12N Health Care Services Review-Request for Review and Response (278) transactions if available.

## System Feature: 278 Health Care Services Review - Table Maintenance – Code Sets 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the ability to add industry standard codes that are used for ASC X12N Health Care Services Review-Request for Review and Response (278) transactions.

### From: IB*2*447 Release Notes/Installation Guide

## Hardware Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special hardware considerations.

## System Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special system considerations.

## Installation and Configuration Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IB\*2\*447 and PRCA\*4.5\*275 (E-claims5-5010) should be installed as a Multi-Build (Host-file) installation, using the KIDS Installation 6 (Install package) option. Please refer to the patch description for instructions on where to download the multi-patch host file. Please also note for Step 4b of the KIDS Patch Description, if you select option \#1 to run a Full Comparison you will get a system error: \<UNDEFINED\>S+1^DIQ ^IBA(364.6,2209,0) due to a known issue with the KIDS Full Compare option (see Remedy Ticket \# HD0000000449218). You can run any of the other 3 compare options without issue.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Security Key Changes for Patch IB\*2\*447
