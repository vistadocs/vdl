---
title: BPS*1*8 ECME Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: ECME
app_name: Electronic Claims Management Engine
section: FIN
app_status: active
pkg_ns: BPS
patch_ver: 1
patch_id: BPS*1*8
group_key: ECME:BPS:1
file_numbers:
- '900231'
security_keys: []
menu_options: 0
description: '- Introduction - Patch Description and Installation Instructions - Enhancements - Technical Modifications - ECME Engine - [ECME User Screen...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 5599
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: August 2010
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/bps_1_p8_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/bps_1_p8_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=141
audit_applied: '2026-05-31'
master_source: BPS*1*8 ECME Release Notes
master_pub_date: August 2010
consolidated_from: 7 versions
prior_versions:
- BPS*1*11 ECME Release Notes
- BPS*1*15 ECME Release Notes
- BPS*1*17 ECME Release Notes
- BPS*1*18 ECME Release Notes
- BPS*1*19 ECME Release Notes
- BPS*1*20 ECME Release Notes
consolidated_title: ecme release notes
---

> ![](bps-1-8-ecme-release-notes/001.png)

Outpatient Pharmacy

ePharmacy Phase 4 COB

####### E-Claims Management Engine (ECME)

####### RELEASE NOTES

BPS\*1\*8

August 2010

V*IST*A Health  
Systems Design & Development

Table of Contents

This page intentionally left blank.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Patch Description and Installation Instructions](#patch-description-and-installation-instructions)
- [Enhancements](#enhancements)
  - [Technical Modifications](#technical-modifications)
    - [ECME Engine](#ecme-engine)
    - [ECME User Screen Modifications](#ecme-user-screen-modifications)
    - [Reversing Claims](#reversing-claims)
    - [Resubmit Claims and Resubmit Claims w/EDITS (RED) Functionality](#resubmit-claims-and-resubmit-claims-wedits-red-functionality)
    - [Send to Worklist Functionality](#send-to-worklist-functionality)
    - [ECME Claims Results Report](#ecme-claims-results-report)
    - [ECME Claims-Response Inquiry \[BPS RPT CLAIMS RESPONSE\] Report](#ecme-claims-response-inquiry-bps-rpt-claims-response-report)
    - [ECME Potential Secondary Rx Claims Report \[BPS COB RPT SECONDARY CLAIMS\]](#ecme-potential-secondary-rx-claims-report-bps-cob-rpt-secondary-claims)
    - [Potential TRICARE Rx Claims Report \[BPS COB RPT TRICARE CLAIMS\]](#potential-tricare-rx-claims-report-bps-cob-rpt-tricare-claims)
    - [Process Secondary/TRICARE Rx to ECME \[BPS COB PROCESS SECOND TRICARE\]](#process-secondarytricare-rx-to-ecme-bps-cob-process-second-tricare)
    - [COB Indicators for Pharmacy Activity Log Entries](#cob-indicators-for-pharmacy-activity-log-entries)
  - [Issue Resolutions](#issue-resolutions)
    - [HD374000 Inability to Reverse TRICARE Claims](#hd374000-inability-to-reverse-tricare-claims)
    - [HD374001 Incorrect Rx Cost Calculation for TRICARE Claims](#hd374001-incorrect-rx-cost-calculation-for-tricare-claims)
This patch has enhancements that extend the capabilities of the V*IST*A ePharmacy billing system, primarily to allow for the electronic submission of secondary pharmacy claims. Below is a list of all the applications involved in this project along with their patch number:
<u>APPLICATION/VERSION PATCH</u>
Integrated Billing (IB) V. 2.0 IB\*2\*411
Electronic Claims Management Engine (ECME) V. 1.0 BPS\*1\*8
Outpatient Pharmacy (OP) V. 7.0 PSO\*7\*290
The three patches (PSO\*7\*290, IB\*2\*411, and BPS\*1\*8) are being released in the Kernel Installation and Distribution System (KIDS) multi-build distribution BPS PSO IB BUNDLE 4.0 For more specific instruction please refer to the installation steps provided in each of the patches.
This page intentionally left blank.

# Patch Description and Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DHCP Patch Display Page: 1

=============================================================================

Run Date: SEP 01, 2010 Designation: BPS\*1\*8

Package : E CLAIMS MGMT ENGINE Priority : MANDATORY

Version : 1 Status : RELEASED

=============================================================================

Associated patches: (v)BPS\*1\*7 \<\<= must be installed BEFORE \`BPS\*1\*8'

Subject: ePHARMACY COB SUPPORT

Category: ROUTINE

DATA DICTIONARY

Description:

===========

This patch has enhancements which extend the capabilities of the Veterans

Health Information Systems and Technology Architecture (VistA) electronic

pharmacy (ePharmacy) billing system. Below is a list of all the

applications involved in this project along with their patch number:

APPLICATION/VERSION PATCH

--------------------------------------------------------------

OUTPATIENT PHARMACY (OP) V. 7.0 PSO\*7\*290

INTEGRATED BILLING (IB) V. 2.0 IB\*2\*411

ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*8

The three patches (PSO\*7\*290, IB\*2\*411 and BPS\*1\*8) are being released in

a Kernel Installation and Distribution System (KIDS) multi-build

distribution bundle BPS PSO IB BUNDLE 4.0. For more specific instructions

please refer to the installation steps provided in each of the patches.

The main purpose of this patch is to implement functionality that

supports e-billing of the patient's secondary insurance plans. These

modifications allow the VA to send additional claims electronically to the

patient's secondary insurances in order to reimburse money from those

payers that are responsible for the payments but were not billed

previously. Thus this enhancement will help VA sites to increase their

revenue.

While claims to the Primary insurance companies are sent automatically,

the claims to the Secondary insurance companies can now be sent manually

by using the new menu option Process Secondary/TRICARE Rx to ECME \[BPS COB

PROCESS SECOND TRICARE. The same menu option can also be used to manually

generate primary claims if the patient has a dual eligibility (for

example, a TRICARE patient has both reimbursable insurance and TRICARE

plans with Pharmacy coverage), these cases were not previously handled by

the software. With this enhancement patch, duel eligible patients can now

be manually billed using the ePharmacy software.

Two new reports are introduced with this patch to support both secondary

billing and primary billing for TRICARE patients. The first report,

Potential Secondary Rx Claims Report \[BPS COB RPT SECONDARY CLAIMS\], will

identify prescriptions/refills that potentially can be billed to the

secondary insurance plans. The second report, Potential TRICARE Claims

Report \[BPS COB RPT TRICARE CLAIMS\], will identify prescriptions/refills

for TRICARE patients that potentially can be billed to the TRICARE

insurance plans.

All three new menu options are combined together under the new ECME

Pharmacy COB \[BPS COB MENU\] menu:

COB ECME Pharmacy COB ...

SEC Potential Secondary Rx Claims Report

TRI Potential TRICARE Claims Report

PRO Process Secondary/TRICARE Rx to ECME

This patch modifies the Electronic Claims Management Engine v1.0

application as described below:

1\. ECME engine:

The modifications made in this patch allow:

\- the engine to recognize secondary claims and process additional COB

(Coordination Of Benefits) fields specific for secondary claims

\- the engine to use specific plans and rate types selected by the user

\- specific data collected for secondary claims to be stored in the BPS

TRANSACTION, BPS LOG OF TRANSACTIONS, BPS CLAIMS and BPS REQUESTS files

\- specific data collected for secondary claims to be processed, formatted

and included in HL7 messages sent to the payer

\- specific entries in the BPS NCPDP FIELD DEFS file (#9002313.91) to be

updated in order to process the additional COB fields and transmit them

to the secondary payer in the correct format

\- COB Indicator information to be returned in the EN^BPSNCPDP API

\- the ECME to send reject codes to Outpatient Pharmacy along with the COB

indicator so the Pharmacy software can distinguish reject codes returned

by secondary and primary payers

The new routine BPSFLD01 was created to store GET, SET and FORMAT code to

support processing of the COB fields transmitted to the secondary payers.

The claim status code was adjusted to provide correct status information

for secondary and primary claims.

The API DUR1^BPSNCPD3 (ICR \#4560) was modified to allow the calling

application to specify the COB (payer sequence) indicator of the claim

for which it is called and to implement a new format of the array for

returned values.

The testing tool was modified to process secondary claims.

2\. ECME User Screen modifications to display COB (payer sequence)

indicators:

2.1. Main Display Screen and Further Research Screen modifications.

To distinguish primary and secondary claims displayed on the screen, each

status line is supplied with COB indicators: "p" for primary and "s" for

secondary claims. Status of another claim associated with the same

prescription/refill (if any) is displayed in parenthesis.

9.1 ACETAMINOPHEN 650 12345-4321-22 03/02 102287 1/0113558 W RT DIS/NR

p-Reversal accepted

9.2 MEDROXYPROGESTRON 00009-0050-02 02/11 102289 0/0113560 W RT ACT/RL

s-Payable (p-Payable)

2.2. The Print Claim Log screen displays a new label to indicate the COB

insurance level:

Rx Coordination of Benefits: PRIMARY

2.3. The initial page of the developer log was updated to display the

information for the specific claim line selected.

Insurance: COB INSURANCE

RX Coord of Benefits: Secondary

The subsequent pages are based upon the prescription and fill and are not

able to differentiate between insurances. However, a log entry

indicating the COB level will be added each time the prescription and fill

is processed.

BPSOSRB-Secondary Insurance

BPSOSQA-Secondary Insurance

3\. Reversing claims:

The primary claim cannot be reversed if there is a payable secondary

claim. In such a case the user will be advised to reverse the secondary

claim first.

1.12 FLURAZEPAM 15MG C 00140-0065-14 03/04 102322\$ 2/0113596 W RT ACT/RL

cannot be Reversed if the secondary claim is payable.

Please reverse the secondary claim first.

4\. Resubmit Claims and Resubmit claims w/EDITS (RED) functionality:

The primary claim cannot be resubmitted if there is a payable secondary

claim. In such a case the user shall be advised to reverse the secondary

claim first.

1.12 FLURAZEPAM 15MG C 00140-0065-14 03/04 102322\$ 2/0113596 W RT ACT/RL

Are you sure?(Y/N)? y YES

The claim:

1.12 FLURAZEPAM 15MG C 00140-0065-14 03/04 102322\$ 2/0113596 W RT ACT/RL

cannot be Resubmitted if the secondary claim is payable.

Please reverse the secondary claim first.

5\. Send to Worklist functionality:

The ECME software was modified to

\- allow secondary claims to be sent to the Pharmacy Worklist manually

from the User Screen,

\- send Refill Too Soon and DUR rejects for secondary claims to the

Pharmacy Worklist automatically.

6\. ECME Claim Results and Status reports:

The ECME Claim Results and Status reports (Payable Claims Report \[BPS RPT

PAYABLE\], Rejected Claims Report \[BPS RPT REJECTION\], Reversal Claims

Report \[BPS RPT REVERSAL\], Claims Submitted, Not Yet Released \[BPS RPT NOT

RELEASED\], Recent Transactions \[BPS RPT RECENT TRANSACTIONS\], and Closed

Claims Report \[BPS RPT CLOSED CLAIMS\]) were modified to display the COB

indicators. The Excel format of the reports include the COB indicator of

the submitted claim as a new piece of data in the data string.

7\. ECME Claims-Response Inquiry \[BPS RPT CLAIMS RESPONSE\] report:

The report reflects new COB data sent in secondary claims.

8\. ECME Potential Secondary Rx Claims Report \[BPS COB RPT SECONDARY

CLAIMS\]:

This new report returns all primary prescription claims, whether

processed electronically or paper, that has possible secondary insurance

identified in the patient insurance file.

9\. Potential TRICARE Claims Report \[BPS COB RPT TRICARE CLAIMS\]:

This new report returns prescriptions that have not yet been billed for

any patient who has an active insurance plan with a type of plan = TRICARE

and who has a dual eligibility (veteran and TRICARE) and whose

prescription Rx Patient Status is not exempt for TRICARE Billing. This

report also includes prescriptions for patients who have TRICARE only in

case of the system not being available and the prescription not being

processed automatically by ECME.

10\. Process Secondary/TRICARE Rx to ECME \[BPS COB PROCESS SECOND TRICARE\]:

The new option was introduced to process the claims identified on the new

reports. This option will submit the claim to ECME and also can be

used to resubmit the claim when the user needs to change data specific

for secondary claims. Any other processing on this claim can be done

through the existing actions available on the ECME User Screen.

When processing a claim using a specific prescription number, the users

will need to select the fill number from the list provided by the software

to generate a claim. The user will be required to enter the billing rate

type since there are 2 types of claims that will primarily be using this

option. Reimbursable Insurance and TRICARE (including TRICARE Reimbursable

Insurance) are the only types of Billing Rates that will be allowed to be

used for ECME billing at this time.

When processing the secondary claim, the users will be presented with the

secondary claim data and will be prompted to edit this data if

necessary. Secondary claim data elements include:

Other Coverage Code

Other Payer Coverage Type

Other Payer ID Qualifier

Other Payer ID

Other Payer Date

If the primary payer paid the primary claim:

Other Payer Amount Paid Qualifier (mult)

Other Payer Amount Paid (mult)

If the primary payer rejected the primary claim:

Other Payer Reject Codes (mult)

This option can also be used to resubmit secondary claims when the user

needs to edit the specific secondary claims information submitted

previously. The user will be prompted for the same information and this

time the default values for the prompts will be set to data submitted in

the latest transaction. In addition during resubmission the user can

change the secondary payer and the rate type if needed. The resubmission

is allowed only for rejected or reversed secondary claims. The payable

claims need to be reversed in the User Screen before they can be

resubmitted through this menu option.

This option also allows the user to submit and resubmit primary claims

for prescriptions/refills for TRICARE patients and patients with dual

eligibility. When processing primary claims the users will be prompted to

select a primary payer for the e-claim and the rate type. The software

allows the user to resubmit the existing primary claims and change the

payer and/or the rate type if needed. The resubmission is allowed only

for rejected or reversed claims. The payable claims need to be reversed

in the User Screen before they can be resubmitted through this menu

option.

11\. COB indicators for Pharmacy Activity log entries:

ECME code was modified to add COB indicators to Pharmacy Activity log

when the claim is resubmitted via User Screen actions "Resubmit Claim"

and "Resubmit Claim w/EDITS" and also when it is reversed manually via

"Reverse Payable Claim" action or automatically by ECME nightly processing

job (auto reversals).

This patch addresses the following New Service Request (NSR):

-------------------------------------------------------------

There is no NSR associated with this patch.

This patch addresses the following Remedy Tickets:

--------------------------------------------------

1\. HD374000 Inability to reverse TRICARE claims

2\. HD374001 Incorrect Rx cost calculation for TRICARE claims

Overview of Remedy Tickets:

---------------------------

1\. HD374000 Inability to reverse TRICARE claims

Problem:

--------

VA Eastern Kansas HCS reported they are unable to reverse electronic

TRICARE claims through the ECME user screen. They are getting a message

stating: "The claim: ... is Tricare claim and cannot be Reversed."

Resolution:

-----------

Remove the lines of code in routine BPSSCRRV that prevented this

functionality.

2\. HD374001 Incorrect Rx cost calculation for TRICARE claims

Problem:

--------

VA Eastern Kansas HCS reported that the billing software is incorrectly

calculating the prescription cost for ECME claims in cases where the drug

is using the NCPDP QUANTITY MULTIPLIER field. The billing software is

calculating the cost based on the NCPDP quantity rather than the

dispensed quantity.

Resolution:

-----------

Correct the ECME utilities STARRAY^BPSNCPD1 and EN^BPSNCPD2 to NOT send

the NCPDP quantity to billing, but instead send the dispensed quantity to

billing as found in the prescription fill and refill data. Continue to

send the NCPDP quantity in the ECME ePharmacy transaction. Also, correct

the ECME utility IBSEND^BPSECMP2 to send the dispensed quantity to

billing as found in the prescription fill and refill data.

Components Sent With Patch

--------------------------

The following is a list of files and fields included in this patch:

UP SEND DATA USER

DATE SEC. COMES OVER

FILE \# FILE NAME DD CODE W/FILE RIDE

-------------------------------------------------------------------

9002313.02 BPS CLAIMS YES NO NO NO

Partial DD: subDD: 9002313.02 fld: .08

subDD: 9002313.0401fld: 443

9002313.57 BPS LOG OF TRANSACTIONS YES NO NO NO

Partial DD: subDD: 9002313.57 fld: 1204

fld: 1205

subDD: 9002313.5714

subDD: 9002313.57902fld: 902.28

fld: 902.29

fld: 902.3

fld: 902.31

fld: 902.32

fld: 902.33

9002313.59 BPS TRANSACTION YES NO NO NO

Partial DD: subDD: 9002313.59 fld: 1204

fld: 1205

subDD: 9002313.5914

subDD: 9002313.59902fld: 902.28

fld: 902.29

fld: 902.3

fld: 902.31

fld: 902.32

fld: 902.33

9002313.77 BPS REQUESTS YES NO NO NO

Partial DD: subDD: 9002313.77 fld: 1.08

fld: 1.09

fld: 1.1

fld: 1.11

fld: 1.12

subDD: 9002313.778

9002313.78 BPS INSURER DATA YES NO NO NO

Partial DD: subDD: 9002313.78 fld: 3.06

The following is a list of options included in this patch:

Option Name Distribution

----------- ------------

BPS COB MENU SEND TO SITE

BPS COB PROCESS SECOND TRICARE SEND TO SITE

BPS COB RPT SECONDARY CLAIMS SEND TO SITE

BPS COB RPT TRICARE CLAIMS SEND TO SITE

BPSMENU USE AS LINK FOR MENU ITEMS

Documentation Retrieval:

========================

Sites may retrieve documentation in one of the following ways:

1\. The preferred method is to FTP the files from

REDACTED, which will transmit the files from the

first available FTP server.

2\. Sites may also elect to retrieve documentation directly from a

specific server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

3\. Documentation can also be retrieved from the VistA Documentation

Library (VDL) on the Internet at the following address,

http://www.va.gov/vdl.

The documentation distribution includes:

FILE NAME DESCRIPTION

---------------------------------------------------------------------

bps_1_p8_rn.pdf ECME Release Notes

bps_1_p8_um.pdf ECME User Manual

bps_1_p8_tm.pdf ECME Technical Manual

Test Sites:

===========

REDACTED

================INSTALLATION INSTRUCTIONS =================

To avoid disruptions, these patches should be installed when users are

not on the system and during non-peak hours. Of particular concern would

be the items below.

1\. Do not install the patch when ECME claims are being generated

by the BPS Nightly Background Job option \[BPS NIGHTLY

BACKGROUND JOB\]. Wait for this job to finish or complete the

installation before this job starts.

2\. Do not install the patch when prescriptions are being

transmitted to CMOP. Wait for the CMOP transmission to finish

or complete the installation before the transmission starts.

Check with Pharmacy Service or your pharmacy Automated Data

Processing Application Coordinator (ADPAC) to find out when

CMOP transmissions occur.

Install Note: Because of the updating entries for the file (#9002313.91)

BPS NCPDP FIELD DEFS, during the install you will see the following

messages

Starting post-install of BPS\*1\*8

updating data for the NCPDP field# 337...

updating data for the NCPDP field# 338...

updating data for the NCPDP field# 339...

updating data for the NCPDP field# 340...

updating data for the NCPDP field# 341...

updating data for the NCPDP field# 342...

updating data for the NCPDP field# 431...

updating data for the NCPDP field# 443...

updating data for the NCPDP field# 471...

updating data for the NCPDP field# 472...

updating data for the NCPDP field# 412...

updating data for the NCPDP field# 477...

updating data for the NCPDP field# 481...

updating data for the NCPDP field# 483...

14 entries have been updated successfully

Install Time - Approximately less than 5 minutes

1\. OBTAIN PATCHES

--------------

Obtain the host file BPS_1_8_PSO_IB.KID, which contains the following

three patch installs:

BPS\*1.0\*8

PSO\*7\*290

IB\*2.0\*411

Sites can retrieve VistA software from the following FTP addresses.

The preferred method is to FTP the files from:

REDACTED

This will transmit the files from the first available FTP server.

Sites may also elect to retrieve software directly from a specific

server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

The BPS_1_8_PSO_IB.KID host file is located in the anonymous.software

directory. Use ASCII Mode when downloading the file.

2\. START UP KIDS

-------------

Start up the Kernel Installation and Distribution System Menu option

\[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INStallation

---

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option:

3\. LOAD TRANSPORT GLOBAL FOR MULTI-BUILD

-------------------------------------

From the Installation menu, select the Load a Distribution option.

When prompted for "Enter a Host File:", enter the full directory path

where you saved the host file BPS_1_8_PSO_IB.KID (e.g.,

SYS\$SYSDEVICE:\[ANONYMOUS\]BPS_1_8_PSO_IB.KID).

When prompted for "OK to continue with Load? NO//", enter "YES."

The following will display:

Loading Distribution...

BPS PSO IB BUNDLE 4.0

BPS\*1.0\*8

PSO\*7.0\*290

IB\*2.0\*411

Use INSTALL NAME: BPS PSO IB BUNDLE 4.0 to install this

Distribution.

7\. RUN OPTIONAL INSTALLATION OPTIONS FOR MULTI-BUILD

-------------------------------------------------

From the Installation menu, you may select to use the following

options (when prompted for the INSTALL NAME, enter

BPS PSO IB BUNDLE 4.0):

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

8\. INSTALL MULTI-BUILD

-------------------

This is the step to start the installation of this KIDS patch. This

will need to be run for the BPS PSO IB BUNDLE 4.0.

a\. Choose the Install Package(s) option to start the patch

install.

b\. When prompted for the "Select INSTALL NAME:", enter BPS PSO IB

BUNDLE 4.0.

c\. For the BPS\*1\*8 patch, when prompted "Want KIDS to Rebuild Menu

Trees Upon Completion of Install? YES//" enter YES unless your

system does this in a nightly TaskMan process.

d\. For the PSO\*7\*290 patch, when prompted "Want KIDS to Rebuild Menu

Trees Upon Completion of Install? YES//" enter YES unless your

system does this in a nightly TaskMan process.

e\. For the IB\*2\*411 patch, when prompted "Want KIDS to Rebuild Menu

Trees Upon Completion of Install? YES//" enter YES unless your

system does this in a nightly TaskMan process.

f\. When prompted "Want KIDS to INHIBIT LOGONs during the

install? YES//" enter NO.

g\. When prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? YES//" enter YES.

h\. When prompted "Enter options you wish to mark as 'Out Of

Order':" enter the following options:

Billing Clerk's Menu \[IB BILLING CLERK MENU\]

Billing Supervisor Menu ... \[IB BILLING SUPERVISOR MENU\]

Patient Insurance Menu ... \[IBCN INSURANCE MGMT MENU\]

e-Pharmacy Menu ... \[IBCNR E-PHARMACY MENU\]

ECME Billing Events Report option \[IB ECME BILLING EVENTS\]

ECME \[BPSMENU\]

ECME User Screen \[BPS USER SCREEN\]

Rx (Prescriptions) \[PSO RX\]

ePharmacy Menu \[PSO EPHARMACY MENU\]

Suspense Functions \[PSO PND\]

i\. When prompted "Enter protocols you wish to mark as 'Out Of

Order':" enter \<return\>.

j\. When prompted "Delay Install (Minutes): (0-60): 0//" enter an

appropriate number of minutes to delay the installation in

order to give users enough time to exit the disabled options

before the installation starts.

k\. When prompted "Device: Home//" respond with the correct device.

The second line of each of the following routines now looks like:

;;1.0;E CLAIMS MGMT ENGINE;\*\*\[Patch List\]\*\*;JUN 2004;Build 29

Routine Information:

====================

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: BPS10P8

Before: n/a After: B14241991 \*\*8\*\*

Routine Name: BPSBCKJ

Before: B46863482 After: B49753700 \*\*1,2,5,7,8\*\*

Routine Name: BPSBUTL

Before: B52438241 After: B54102124 \*\*1,3,2,5,7,8\*\*

Routine Name: BPSECA1

Before: B9994271 After: B12154283 \*\*1,5,8\*\*

Routine Name: BPSECMP2

Before: B65381768 After: B81277814 \*\*1,5,6,7,8\*\*

Routine Name: BPSECX0

Before: B4171802 After: B23106196 \*\*1,5,8\*\*

Routine Name: BPSFLD01

Before: n/a After: B9727334 \*\*8\*\*

Routine Name: BPSNCPD1

Before: B46831868 After: B44878746 \*\*1,3,5,6,7,8\*\*

Routine Name: BPSNCPD2

Before: B37810791 After: B42415694 \*\*1,5,6,7,8\*\*

Routine Name: BPSNCPD3

Before: B28795294 After: B28796956 \*\*1,5,6,7,8\*\*

Routine Name: BPSNCPD4

Before: B40771134 After: B43623914 \*\*6,7,8\*\*

Routine Name: BPSNCPD5

Before: B64980990 After: B78805427 \*\*7,8\*\*

Routine Name: BPSNCPD6

Before: B36903046 After: B39101412 \*\*7,8\*\*

Routine Name: BPSNCPDP

Before: B54845917 After: B76105402 \*\*1,3,4,2,5,6,7,8\*\*

Routine Name: BPSOS6M

Before: B10068430 After: B11551065 \*\*1,5,8\*\*

Routine Name: BPSOSC2

Before: B29561871 After: B34066005 \*\*1,5,8\*\*

Routine Name: BPSOSCC

Before: B24314564 After: B26147652 \*\*1,2,5,8\*\*

Routine Name: BPSOSCD

Before: B38794587 After: B50726570 \*\*1,3,2,5,7,8\*\*

Routine Name: BPSOSCE

Before: B13508896 After: B14075186 \*\*1,5,7,8\*\*

Routine Name: BPSOSCF

Before: B26940349 After: B28717442 \*\*1,5,8\*\*

Routine Name: BPSOSH2

Before: B26441893 After: B63139845 \*\*1,5,8\*\*

Routine Name: BPSOSHF

Before: B11141582 After: B32080446 \*\*1,5,8\*\*

Routine Name: BPSOSIY

Before: B55797518 After: B67267504 \*\*1,3,5,6,7,8\*\*

Routine Name: BPSOSIZ

Before: B14362353 After: B16026755 \*\*1,5,7,8\*\*

Routine Name: BPSOSQA

Before: B8495270 After: B9957067 \*\*1,5,7,8\*\*

Routine Name: BPSOSRB

Before: B38286741 After: B41392879 \*\*1,5,7,8\*\*

Routine Name: BPSOSRX

Before: B40176170 After: B41387461 \*\*1,5,7,8\*\*

Routine Name: BPSOSRX2

Before: B19493151 After: B20068937 \*\*7,8\*\*

Routine Name: BPSOSRX3

Before: B60624911 After:B105355282 \*\*7,8\*\*

Routine Name: BPSOSRX4

Before: B38901734 After: B55754369 \*\*7,8\*\*

Routine Name: BPSOSRX5

Before: B30558901 After: B36392851 \*\*7,8\*\*

Routine Name: BPSOSRX6

Before: B25462490 After: B25512407 \*\*7,8\*\*

Routine Name: BPSPRRX

Before: n/a After: B99076770 \*\*8\*\*

Routine Name: BPSPRRX1

Before: n/a After: B12437232 \*\*8\*\*

Routine Name: BPSPRRX2

Before: n/a After: B8324629 \*\*8\*\*

Routine Name: BPSPRRX3

Before: n/a After: B99615569 \*\*8\*\*

Routine Name: BPSPRRX4

Before: n/a After: B15420214 \*\*8\*\*

Routine Name: BPSPRRX5

Before: n/a After: B48156542 \*\*8\*\*

Routine Name: BPSPRRX6

Before: n/a After: B57663596 \*\*8\*\*

Routine Name: BPSRES

Before: B66886236 After: B93916400 \*\*3,5,7,8\*\*

Routine Name: BPSRPT1

Before: B52062138 After: B52995272 \*\*1,5,7,8\*\*

Routine Name: BPSRPT4

Before: B67405446 After: B69467414 \*\*1,5,7,8\*\*

Routine Name: BPSRPT5

Before: B72711123 After: B79661218 \*\*1,3,5,7,8\*\*

Routine Name: BPSRPT6

Before: B59574231 After: B66218478 \*\*1,3,5,7,8\*\*

Routine Name: BPSRPT7

Before: B77006502 After: B77430067 \*\*1,3,5,7,8\*\*

Routine Name: BPSRPT8

Before: B78632943 After: B84250810 \*\*1,3,5,7,8\*\*

Routine Name: BPSRPT9

Before: n/a After: B81558879 \*\*8\*\*

Routine Name: BPSRPT9A

Before: n/a After: B71706588 \*\*8\*\*

Routine Name: BPSSCR03

Before: B48894943 After: B42145046 \*\*1,5,7,8\*\*

Routine Name: BPSSCRCL

Before: B65041094 After: B76318080 \*\*1,3,5,7,8\*\*

Routine Name: BPSSCRLG

Before: B95335082 After: B97729982 \*\*1,5,7,8\*\*

Routine Name: BPSSCRRS

Before: B34449344 After: B44067784 \*\*1,3,5,7,8\*\*

Routine Name: BPSSCRRV

Before: B37049932 After: B40545723 \*\*1,5,6,7,8\*\*

Routine Name: BPSSCRU3

Before: B30240821 After: B30637579 \*\*1,5,7,8\*\*

Routine Name: BPSSCRU5

Before: B61189921 After: B62214356 \*\*1,5,7,8\*\*

Routine Name: BPSSCRU6

Before: B5405845 After: B18199575 \*\*3,8\*\*

Routine Name: BPSTEST

Before: B58349994 After: B68950406 \*\*6,7,8\*\*

Routine Name: BPSUTIL2

Before: B11085686 After: B26258660 \*\*7,8\*\*

Routine Name: BPSWRKLS

Before: B27286584 After: B31684663 \*\*7,8\*\*

Routine list of preceding patches: 7

=============================================================================

User Information:

Entered By : REDACTED Date Entered : OCT 25,2007

Completed By: REDACTED Date Completed: SEP 1,2010

Released By : Date Released :

This page intentionally left blank.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ECME Engine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The modifications made in this patch allow:

- The engine to recognize secondary claims and process additional Coordination of Benefits (COB) fields specific for secondary claims
- The engine to use specific plans and rate types selected by the user
- The collection of specific data for secondary claims that is stored in the BPS TRANSACTION, BPS CLAIMS OF TRANSACTION, and BPS REQUESTS files
- The collection of specific data for secondary claims so they can be processed, formatted, and included in HL7 messages sent to the payer
- The entries in the file (#9002313.91) BPS NCPDP FIELD DEFS to be updated by the post-install routine to allow the software to process the additional COB fields and transmit them to the secondary payer in the correct format
- The COB Indicator information to be returned in the EN^BPSNCPDP API
- The ECME to send reject codes to Outpatient Pharmacy along with the COB indicator so the Pharmacy software can distinguish reject codes returned by secondary and primary payers
- The new routine BPSFLD01, created to store GET, SET, and FORMAT code, to support processing of the COB fields transmitted to the secondary payers
- The claim status code, which has been adjusted, to provide correct status information for secondary and primary claims
- The modified API DURI^BPSNCPD3 (ICR#4560 to allow the calling application to specify the COB (payer sequence) indicator of the claim for which it is called and to implement a new format of the array for returned values
- The modified testing tool to process secondary claims

### ECME User Screen Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME User Screen modifications allow the display of COB (payer sequence) indicators:

- The Main Display Screen and Further Research Screen modifications distinguish between primary and secondary claims displayed on the screen. Each status line is supplied with the COB indicators "p" for primary claims and "s" for secondary claims. Status of another claim associated with the same prescription/refill (if any) is displayed in parentheses:
  - 9.1 ACETAMINOPHEN 650 12345-4321-22 03/02 102287 1/0113558 W RT DIS/NR p-Reversal accepted
  - 9.2 MEDROXYPROGESTRON 00009-0050-02 02/11 102289 0/0113560 W RT ACT/RL s-Payable (p-Payable)
- The Print Claim Log screen displays a new label to indicate the COB insurance level:
  - Rx Coordination of Benefits: PRIMARY
- The initial page of the developer log was updated to display the information for the specific claim line selected:
  - Insurance: COB INSURANCE
  - RX Coord of Benefits: PRIMARY

The subsequent pages are based upon the prescription and fill and are not able to differentiate between insurances. However, a log entry indicating the COB level will be added each time the prescription and fill is processed:

- BPSOSRB-Secondary Insurance
- BPSOSQA-Secondary Insurance

### Reversing Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary claim cannot be reversed if there is a payable secondary claim. In such a case the user will be advised to reverse the secondary claim first.

- 1.12 FLURAZEPAM 15MG C 00140-0065-14 03/04 102322\$ 2/0113596 W RT ACT/RL cannot be Reversed if the secondary claim is payable. Please reverse the secondary claim first

### Resubmit Claims and Resubmit Claims w/EDITS (RED) Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary claim cannot be resubmitted if there is a payable secondary claim. In such a case the user shall be advised to reverse the secondary claim first.

- 1.12 FLURAZEPAM 15MG C 00140-0065-14 03/04 102322\$ 2/0113596 W RT ACT/RL Are you sure? (Y/N)? y YES

> The claim:

- 1.12 FLURAZEPAM 15MG C 00140-0065-14 03/04 102322\$ 2/0113596 W RT ACT/RL cannot be Resubmitted if the secondary claim is payable.

> Please reverse the secondary claim first

### Send to Worklist Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME software was modified to:

- Allow secondary claims to be sent to the Pharmacy Worklist manually from the User Screen
- Send Refill Too Soon and DUR rejects for secondary claims to the Pharmacy Worklist automatically

### ECME Claims Results Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME Claims Result reports (Payable Claims Report \[BPS RPT PAYABLE\], Rejected Claims Report \[BPS RPT REJECTION\], Reversal Claims Report \[BPS RPT REVERSAL\], Claims Submitted, Not Yet Released \[BPS RPT NOT RELEASED\], Recent Transactions \[BPS RPT RECENT TRANSACTIONS\], and Closed Claims Report \[BPS RPT CLOSED CLAIMS\]) were modified to display the COB indicators. The Excel format of the reports include the COB indicator of the submitted claims as a new piece of data in the data string.

### ECME Claims-Response Inquiry \[BPS RPT CLAIMS RESPONSE\] Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The report reflects new COB data sent in secondary claims.

### ECME Potential Secondary Rx Claims Report \[BPS COB RPT SECONDARY CLAIMS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new report returns all primary prescription claims, whether processed electronically or on paper, that have possible secondary insurance identified in the patient insurance file.

### Potential TRICARE Rx Claims Report \[BPS COB RPT TRICARE CLAIMS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new report returns prescriptions that have not yet been billed for any patient who has an active insurance plan with a type of plan = TRICARE and who has a dual eligibility (veteran and TRICARE) and whose prescription Rx Patient Status is not exempt for Champus Billing. This report also includes prescriptions for patients who have TRICARE only in case the system is not available and the prescription cannot be processed automatically by ECME.

### Process Secondary/TRICARE Rx to ECME \[BPS COB PROCESS SECOND TRICARE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new option was introduced to process the claims identified on the new reports. This option will submit the claim to ECME and also can be used to resubmit the claim when the user needs to change data specific for secondary claims. Any other processing on this claim can be done through the existing actions available on the ECME User Screen.

When processing a claim using a specific prescription number, the users will need to select the fill number from the list provided by software to generate a claim. The user will be required to enter the billing rate type since there are 2 types of claims that will primarily be using this option. Reimbursable Insurance and TRICARE (including TRICARE Reimbursable Insurance) are the only types of Billing Rates that will be allowed at this time.

When processing the secondary claim, the users will be presented with the secondary claim data and will be prompted to edit this data if necessary. Secondary claim data elements include:

- Other Coverage Code
- Other Payer Coverage Type
- Other Payer ID Qualifier
- Other Payer ID
- Other Payer Date

If the primary payer paid the primary claim:

- Other Payer Amount Paid Qualifier (mult)
- Other Payer Amount Paid (mult)

If the primary payer rejected the primary claim:

- Other Payer Reject Codes (mult)

This option can also be used to resubmit secondary claims when the user needs to edit the specific secondary claims information submitted previously. The user will be prompted for the same information and this time the default values for the prompts will be set to data submitted in the latest transaction. In addition during resubmission the user can change the secondary payer and the rate type if needed. The resubmission is allowed only for rejected or reversed secondary claims. The payable claims need to be reversed in the User Screen before they can be resubmitted through this menu option.

This option also allows the user to submit and resubmit primary claims for prescriptions/refills for TRICARE patients and patients with dual eligibility. When processing primary claims the users will be prompted to select a primary payer for the e-claim and the rate type. The software allows the user to resubmit the existing primary claims and change the payer and/or the rate type if needed. The resubmission is allowed only for rejected or reversed claims. The payable claims need to be reversed in the User Screen before they can be resubmitted through this menu option.

### COB Indicators for Pharmacy Activity Log Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ECME code has been modified to add COB indicators to Pharmacy Activity log when the claim is submitted via User Screen actions "Resubmit Claim" and "Resubmit Claim w/EDITS" and also when it is reversed manually via "Reverse Payable Claim" action or automatically by ECME nightly processing job (auto reversals).

## Issue Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There were no New Service Requests (NSRs) for this patch. This patch does address the following Remedy Tickets associated with this patch:

1.  HD374000 Inability to reverse TRICARE claims.
2.  HD374001 Incorrect Rx cost calculation for TRICARE claims.

### HD374000 Inability to Reverse TRICARE Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem: VA Eastern Kansas HCS reported they are unable to reverse electronic TRICARE claims through the ECME user screen. They are getting a message stating: "The claim: ... is TRICARE claim and cannot be Reversed."

Resolution: Remove the lines of code in routine BPSSCRRV that prevented this functionality.

### HD374001 Incorrect Rx Cost Calculation for TRICARE Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem: VA Eastern Kansas HCS reported that the billing software is incorrectly calculating the prescription cost for ECME claims in cases where the drug is using the NCPDP QUANTITY MULTIPLIER field. The billing software is calculating the cost based on the NCPDP quantity rather than the dispensed quantity.

Resolution: Correct the ECME utilities STARRAY^BPSNCPD1 and EN^BPSNCPD2 to NOT send the NCPDP quantity to billing, but instead send the dispensed quantity to billing as found in the prescription fill and refill data. Continue to send the NCPDP quantity in the ECME ePharmacy transaction. Also, correct the ECME utility IBSEND^BPSECMP2 to send the dispensed quantity to billing as found in the prescription fill and refill data.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: BPS*1*11 ECME Release Notes

## Documentation Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation distribution includes:

 

    FILE NAME                         DESCRIPTION

    ---------------------------------------------------------------------

BPS_1_P11_RN.PDF ECME Release Notes

BPS_1_P11_UM.PDF ECME User Manual

BPS_1_P11_TM.PDF ECME Technical Manual/Security Guide

*(This page included for two-sided copying.)*

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch Display Page: 1

=============================================================================

Run Date: JAN 19, 2012 Designation: BPS\*1\*11

Package : E CLAIMS MGMT ENGINE Priority : MANDATORY

Version : 1 Status : RELEASED

=============================================================================

Associated patches: (v)BPS\*1\*12 \<\<= must be installed BEFORE \`BPS\*1\*11'

Subject: EPHARMACY PHASE 6

Category: ENHANCEMENT

ROUTINE

OTHER

DATA DICTIONARY

Description:

===========

This patch has enhancements that extend the capabilities of the Veterans

Health Information Systems and Technology Architecture (VistA) electronic

pharmacy (ePharmacy) billing system. Below is a list of all the

applications involved in this project along with their patch number:

APPLICATION/VERSION PATCH

---------------------------------------------------------------

OUTPATIENT PHARMACY (OP) V. 7.0 PSO\*7\*385

INTEGRATED BILLING (IB) V. 2.0 IB\*2\*452

ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*11

CONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP) V. 2.0 PSX\*2\*73

The patches (PSO\*7\*385, IB\*2\*452, BPS\*1\*11, and PSX\*2\*73) are being released

in the Kernel Installation and Distribution System (KIDS) multi-build

distribution BPS PSO IB PSX BUNDLE 7.0.

The purpose of this software package is to maintain compliance with

legislative and federal mandates and to address and correct gaps and

inefficiencies in the current electronic pharmacy billing processes. This

will ultimately increase revenues collected by VA Medical Centers and

outpatient pharmacies by reducing the volume of short pays and payment

denials.

All pharmacy claims for payers that are processed electronically are

compliant with the current industry standards. This software adds support

for the electronic billing of the Health Administration Center (HAC) CHAMPVA

payer in order to provide an automated process and to prevent manual

workarounds for CHAMPVA.

This specific patch contains the following functionality:

---------------------------------------------------------

1\. A new reject code "eC" has been added to the BPS NCPDP REJECT CODES

file (#9002313.93). The associated description for this new code

is CHAMPVA-DRUG NON BILLABLE.

2\. A new mailgroup for CHAMPVA claims has been created with this patch.

When ECME has problems in processing a CHAMPVA claim, a message will

be sent to this mailgroup. Members can be added to the mail group by

using the Mail Group Edit \[XMEDITMG\] option.

3\. The Payable Claims Report \[BPS RPT PAYABLE\], Reversal Claims Report

\[BPS RPT REVERSAL\], and Closed Claims Report \[BPS RPT CLOSED CLAIMS\]

have been modified to include the patient eligibility (VETERAN,

TRICARE, or CHAMPVA). The report display and the Excel output version

now contain a column header and data for eligibility. A new filter

has been added to these reports that allows the user to select a

specific patient eligibility or ALL. In addition, the location of the

eligibility column on both the screen display and Excel output of the

Rejected Claims Report \[BPS RPT REJECTION\] was moved to match the

other reports.

4\. For CHAMPVA eligible patient, the ECME User Screen displays CVA

eligibility as part of the patient/insurance line.

5\. The Change View action of the ECME User Screen \[BPS USER SCREEN\]

allows the user to select NCPDP submissions with a CHAMPVA patient

eligibility.

6\. The Change View action of the ECME User Screen \[BPS USER SCREEN\]

allows the user to select NCPDP submissions with an UNSTRANDED

status.

7\. When a claim rejection has been ignored by using the IGN action on the

Third Party Payer Rejects - Worklist \[PSO REJECTS WORKLIST\] or via the

Reject Notification Screen, the comment entered during the ignore

process will be displayed in the ECME User Screen \[BPS USER SCREEN\]

prefaced by the word "IGNORED".

8\. When using the Resubmit with Edits (RED) action on the ECME User

Screen \[BPS USER SCREEN\], the user will now be allowed to edit the

Date of Service field on an ECME claim if the prescription is

released. Additionally, the Relationship Code prompt was changed to

Pharmacy Relationship Code that the Person Code prompt was changed

to Pharmacy Person Code. Also, the list of submission clarification

codes that can be selected has been updated to reflect new values in

the NCPDP standard.

9\. A new report called View ePharmacy Rx is now available from multiple

locations in ECME and Outpatient Pharmacy. This new report combines

data from multiple screens and reports in Outpatient Pharmacy, ECME,

and Integrated Billing. The combined data is presented in a single

List Manager screen. In ECME, this report is available via the View

ePharmacy Rx \[BPS RPT VIEW ECME RX\] option on the Other Reports \[BPS

MENU RPT OTHER\] menu.

10\. The LOG action - Print Claim Log - of the ECME User Screen \[BPS USER

SCREEN\] has been enhanced as follows:

a\. NCPDP quantity and units are displayed if they exist and Billed

quantity and units are displayed.

b\. All of the fees, costs and amounts sent on an ECME claim are now

displayed with the proper field labels.

c\. Extraneous whitespace has been removed.

11\. The ePharmacy Date of Service calculation algorithm has been modified

with this patch. The fill date is no longer considered an acceptable

value for the date of service. The algorithm uses the release date if

it exists. If the release date doesn't exist, then the system uses

the current date.

12\. References in the ECME system to Fill Date have been changed to be

Date of Service to more accurately indicate the data being displayed.

13\. The ECME system now has the ability to remove outbound messages from

the HL7 queue if the user unstrands a claim using the option

View/Unstrand Submissions Not Completed \[BPS UNSTRAND SCREEN\].

14\. When an NCPDP response with a DUPLICATE status is received, the ECME

system will now process that response as a normal payable response in

order to create bills in IB and AR if a bill does not yet exist. The

IB system will make that determination.

15\. The ECME system will now use the indicator "P2" to indicate that the

ECME claim was initiated by the PRO option - Process Secondary/TRICARE

Rx to ECME \[BPS COB PROCESS SECOND TRICARE\]. The user will also be

able to filter results on the ECME User Screen \[BPS USER SCREEN\] and

on the ECME Claims Reports by RT - Real Time Fills, BB - Backbilling,

or P2 - PRO option.

16\. The ECME system receives all appropriate fees and costs from the

Integrated Billing system and uses them in the correct NCPDP fields

on the claim. These include:

a\. Dispensing Fee (412-DC)

b\. Basis of Cost Determination (423-DN)

c\. Gross Amount Due (430-DU)

d\. Administrative Fee (480-H9)

e\. Ingredient Cost (409-D9)

f\. Usual and Customary Charge (426-DQ)

17\. Several ECME reports have been updated to display the above fees and

costs when using the Excel output versions of the report data.

18\. The Process Secondary/TRICARE Rx to ECME \[BPS COB PROCESS SECOND

TRICARE\] option was modified to correctly handle the previous

payment when the primary claim was paper.

19\. A bulletin is created whenever a primary claim is closed in ECME

and there is an open secondary claim. This scenario can occur when

and inpatient claim is auto-reversed by the ECME Nightly Background

Job or if the prescription is returned to stock or the prescription

is deleted.

20\. When the ECME Nightly Background Job does an inpatient auto-reversal,

the reason not billable is set to 'INPATIENT RX AUTO-REVERSAL', which

is a new non-billable reason created in Integrated Billing.

Previously, the non-billable reason of 'OTHER' was used.

21\. The Payable Claims Report \[BPS RPT PAYABLE\], Rejected Claims Report

\[BPS RPT REJECTION\], Claims Submitted, Not Yet Released Report \[BPS

RPT NOT RELEASED\], and Spending Account Report \[BPS RPT SPENDING

ACCOUNT\] have been corrected to display the correct amount in the

\$BILLED column.

Patch Components

================

Files & Fields Associated:

File Name (#) New/Modified/

Sub-File Name (#) Field Name (#) Deleted

------------------- ------------------- -------------

BPS CLAIMS (#9002313.02)

TRANSACTIONS sub-file (#9002313.0201)

DISPENSING FEE SUBMITTED (#412) Modified

BPS LOG OF TRANSACTIONS (#9002313.57)

HL7 MESSAGE ID (#2) New

QUANTITY (#501) Modified

BILLING QUANTITY (#509) New

BILLING UNIT (#510) New

PATIENT INSURANCE MULTIPLE sub-file (#9002313.57902)

PATIENT RELATIONSHIP CODE (#902.07) Modified

PERSON CODE (#902.1) New

INGREDIENT COST (#902.2) New

ELIGIBILITY (#902.28) Modified

BPS TRANSACTION (#9002313.59)

HL7 MESSAGE ID (#2) New

QUANTITY (#501) Modified

BILLING QUANTITY (#509) New

BILLING UNIT (#510) New

PATIENT INSURANCE MULTIPLE sub-file (#9002313.59902)

PATIENT RELATIONSHIP CODE (#902.07) Modified

PERSON CODE (#902.1) New

INGREDIENT COST (#902.2) New

ELIGIBILITY (#902.28) Modified

BPS REQUESTS (#9002313.77)

BILLING QUANTITY (#4.08) New

BILLING UNIT (#4.09) New

BPS INSURER DATA (#9002313.78)

PATIENT RELATIONSHIP CODE (#1.05) Modified

PERSON CODE (#1.09) New

INGREDIENT COST (#2.08) New

ELIGIBILITY (#3.04) Modified

Forms Associated:

Form Name File \# New/Modified/Deleted

--------- ------ --------------------

N/A

List Templates Associated:

List Template Name New/Modified/Deleted

------------------ --------------------

BPS LSTMN ECME UNSTRAND Modified

BPS LSTMN ECME USRSCR Modified

BPS LSTMN RSCH MENU Modified

BPS VIEW ECME RX New

Mail Groups Associated:

Mail Group Name New/Modified/Deleted

--------------- --------------------

BPS CHAMPVA New

Options Associated:

Option Name Type New/Modified/Deleted

----------- ---- --------------------

BPS COB PROCESS SECOND TRICARE run routine Modified

BPS MENU RPT OTHER menu Modified

BPS RPT VIEW ECME RX run routine New

Protocols Associated:

Protocol Name New/Modified/Deleted

------------- --------------------

BPS PRTCL USRSCR HIDDEN ACTIONS Modified

BPS PRTCL USRSCR VIEW ECME RX New

BPS VIEW ECME RX MENU New

BPS VRX NAV BILL LIST New

BPS VRX NAV BILLING EVENTS RPT New

BPS VRX NAV CRI New

BPS VRX NAV DG ELIG STATUS New

BPS VRX NAV DG ELIG VERIFICATION New

BPS VRX NAV ECME CLAIM LOG New

BPS VRX NAV INS POL New

BPS VRX NAV TPJI AR ACCT PROFILE New

BPS VRX NAV TPJI AR COMMENT HISTORY New

BPS VRX NAV TPJI CLAIM INFORMATION New

BPS VRX NAV TPJI ECME RX INFO New

BPS VRX NAV VIEWRX New

Security Keys Associated:

Security Key Name

-----------------

N/A

Templates Associated:

Template Name Type File Name (Number) New/Modified/Deleted

------------- ---- ------------------ --------------------

N/A

Additional Information:

New Service Requests (NSRs)

----------------------------

Request Name: ePharmacy Claims Phase 6 (FY10)

Request ID: 20090215

Patient Safety Issues (PSIs)

-----------------------------

N/A

Remedy Ticket(s) & Overview

---------------------------

N/A

Test Sites:

----------

REDACTED

Documentation Retrieval Instructions

------------------------------------

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to FTP the files from

ftp://REDACTED. This transmits the files from the first

available FTP server. Sites may also elect to retrieve software directly from

a specific server as follows:

Albany REDACTED \<ftp://REDACTED\>

Hines REDACTED \<ftp://REDACTED\>

Salt Lake City REDACTED \<ftp://REDACTED\>

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl/

Title File Name FTP Mode

-----------------------------------------------------------------------

ECME Release Notes BPS_1_P11_RN.PDF Binary

ECME User Manual BPS_1_P11_UM.PDF Binary

ECME Technical Manual/Security Guide BPS_1_P11_TM.PDF Binary

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a post-install routine associated with this patch named

POST^BPS10P11. The purpose of the post install routine is to:

a\. Create a new entry called 'CHAMPVA DRUG NON BILLABLE' in the BPS

NCPDP REJECT CODES (#9002313.93) dictionary.

b\. Update several pricing fields in the BPS NCPDP FIELD DEFS

(#9002313.92) file so that the NCPDP claims will have the new data

returned by IB Billing Determination.

c\. Remove the DATE OF SERVICE (#401) field from the TRANSACTION

multiple (#400) of the BPS CLAIMS (#9002313.02) file.

d\. Remove the obsolete SUBMISSION CLARIFICATION CODE (#420) field from

the TRANSACTION multiple (#400) of the BPS CLAIMS (#9002313.02) file.

e\. Validate that the PATIENT RELATIONSHIP CODE (#1.05) field of the

BPS INSURER DATA (#9002313.78) file has the correct range of data

(0-4) and correct it if it does not.

f\. Remove cached hidden menu pointers allowing modified protocols to

display correctly.

g\. When appropriate, swap the data in the DUR REASON CODE (#.01) and

DUR PROFESSIONAL SERVICE CODE (#.02) fields of the DUR (#9002313.771)

multiple of the BPS REQUESTS (#9002313.77) file.

h\. Change the Read Security of the BPS NCPDP FIELD CODES (#9002313.94)

file to "Pp", which matches the rest of the ECME files.

i\. Add two new NCPDP reject codes to the BPS NCPDP REJECT CODES

(#9002313.93) dictionary.

The post-install routine is automatically deleted by the system if

allowed by your Kernel site parameters configuration. You may delete

routine BPS10P11 if the installation was successful and it is not

automatically deleted by KIDS.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should take up to 20 minutes to install.

DO NOT QUEUE the installation of this patch.

To avoid disruptions, these patches should be installed during non-peak

hours when there is minimal activity on the system. Avoid times when ECME

claims are being transmitted. Of particular concern would be the options

below.

1\. BPS NIGHTLY BACKGROUND JOB \[BPS NIGHTLY BACKGROUND JOB\]

Do not install the patch when ECME claims are being generated

by the BPS Nightly Background Job option. Wait for this job to

finish or complete the installation before this job starts.

2\. Scheduled CS Transmission \[PSXR SCHEDULED CS TRANS\] and

Scheduled Non-CS Transmission \[PSXR SCHEDULED NON-CS TRANS\]

Do not install the patch when prescriptions are being

transmitted to CMOP. Wait for the CMOP transmissions to finish

or complete the installation before the transmissions start. Both

the CS (Controlled Substances) and the non-CS CMOP transmission

options should be checked. Check with Pharmacy Service or your

Pharmacy ADPAC to find out when CMOP transmissions occur.

\*\*\*\*\* IMPORTANT INSTALLATION NOTES \*\*\*\*\*

This patch bundle is changing the name of File \#52.87. The current name of

this file is 'PSO TRICARE AUDIT LOG'. The new name of this file is 'PSO AUDIT

LOG'. During the patch installation you will see the following information

presented to the screen:

52.87 PSO AUDIT LOG

\*BUT YOU ALREADY HAVE 'PSO TRICARE AUDIT LOG' AS FILE \#52.87!

Shall I write over your PSO TRICARE AUDIT LOG File? YES//

Please accept the default answer of YES to this question.

You will also be prompted to enter the coordinator for the new BPS CHAMPVA

mail group. Prior to installation, please contact your Medical Care Cost

Recovery (MCCR) business department (Facility Revenue Manager) to

determine who will be the coordinator for this new mail group. The users

in this mail group will receive bulletins related to the processing of

CHAMPVA electronic claims. After the patch is installed, members can be

added to the mail group by using the Mail Group Edit \[XMEDITMG\] option.

Pre-Installation Instructions

-----------------------------

1\. OBTAIN PATCHES

--------------

Obtain the host file BPS_1_11_PSO_IB_PSX.KID, which contains the

following patches:

BPS\*1.0\*11

PSO\*7.0\*385

IB\*2.0\*452

PSX\*2.0\*73

Sites can retrieve VistA software from the following FTP addresses.

The preferred method is to FTP the files from:

REDACTED

This will transmit the files from the first available FTP server.

Sites may also elect to retrieve software directly from a specific

server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

The BPS_1_11_PSO_IB_PSX.KID host file is located in the

anonymous.software directory. Use ASCII Mode when downloading the

file.

2\. START UP KIDS

-------------

Start up the Kernel Installation and Distribution System Menu option

\[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INStallation

---

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option:

3\. LOAD TRANSPORT GLOBAL FOR MULTI-BUILD

-------------------------------------

From the Installation menu, select the Load a Distribution option.

When prompted for "Enter a Host File:", enter the full directory path

where you saved the host file BPS_1_11_PSO_IB_PSX.KID (e.g.,

SYS\$SYSDEVICE:\[ANONYMOUS\]BPS_1_11_PSO_IB_PSX.KID).

When prompted for "OK to continue with Load? NO//", enter "YES."

The following will display:

Loading Distribution...

BPS PSO IB PSX BUNDLE 7.0

BPS\*1.0\*11

PSO\*7.0\*385

IB\*2.0\*452

PSX\*2.0\*73

Use INSTALL NAME: BPS PSO IB PSX BUNDLE 7.0 to install this

Distribution.

4\. RUN OPTIONAL INSTALLATION OPTIONS FOR MULTI-BUILD

-------------------------------------------------

From the Installation menu, you may select to use the following

options (when prompted for the INSTALL NAME, enter

BPS PSO IB PSX BUNDLE 7.0):

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

5\. INSTALL MULTI-BUILD

-------------------

This is the step to start the installation of this KIDS patch. This

will need to be run for the BPS PSO IB PSX BUNDLE 7.0.

a\. Choose the Install Package(s) option to start the patch

install.

b\. When prompted for the "Select INSTALL NAME:", enter BPS PSO IB

PSX BUNDLE 7.0.

c\. When prompted to "Enter the Coordinator for Mail Group 'BPS

CHAMPVA':", please respond with the appropriate person.

d\. When prompted "Shall I write over your PSO TRICARE AUDIT LOG File?

YES//", please accept the default of YES in order to change the name

of this file as instructed above.

e\. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of

Install? YES//", enter YES unless your system does this in a nightly

TaskMan process.

f\. When prompted "Want KIDS to INHIBIT LOGONs during the install?

YES//", enter NO.

g\. When prompted " Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//", enter NO.

h\. When prompted "Device: HOME//", respond with the correct device

but do not queue this install.

Post-Installation Instructions

------------------------------

N/A

Routine Information:

====================

The second line of each of these routines now looks like:

;;1.0;E CLAIMS MGMT ENGINE;\*\*\[Patch List\]\*\*;JUN 2004;Build 27

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: BPS10P11

Before: n/a After: B81376656 \*\*11\*\*

Routine Name: BPSBUTL

Before: B55262641 After: B69452320 \*\*1,3,2,5,7,8,9,10,11\*\*

Routine Name: BPSECA8

Before: B28856161 After: B28789947 \*\*1,5,10,12,11\*\*

Routine Name: BPSECFM

Before: B9768202 After: B10365847 \*\*1,7,10,11\*\*

Routine Name: BPSECMC2

Before: B15229460 After: B15123037 \*\*1,2,5,11\*\*

Routine Name: BPSECMP2

Before: B98781684 After:B189210451 \*\*1,5,6,7,8,10,11\*\*

Routine Name: BPSECMPS

Before: B98920700 After: B96560458 \*\*1,2,5,6,7,10,11\*\*

Routine Name: BPSELG

Before: B36086244 After: B29703667 \*\*10,11\*\*

Routine Name: BPSNCPD1

Before: B45414191 After: B52273565 \*\*1,3,5,6,7,8,9,10,11\*\*

Routine Name: BPSNCPD2

Before: B62016998 After: B60489856 \*\*1,5,6,7,8,10,11\*\*

Routine Name: BPSNCPD3

Before: B48711811 After: B60635405 \*\*1,5,6,7,8,10,11\*\*

Routine Name: BPSNCPD4

Before: B45568614 After: B43924039 \*\*6,7,8,10,11\*\*

Routine Name: BPSNCPD5

Before: B79985749 After: B76118605 \*\*7,8,10,11\*\*

Routine Name: BPSNCPD6

Before: B28619607 After: B28397403 \*\*7,8,10,11\*\*

Routine Name: BPSNCPD9

Before: B36538508 After: B36455524 \*\*10,11\*\*

Routine Name: BPSNCPDP

Before: B79480311 After: B93011711 \*\*1,3,4,2,5,6,7,8,10,11\*\*

Routine Name: BPSOS57

Before: B15079066 After: B14911792 \*\*1,5,10,11\*\*

Routine Name: BPSOSC2

Before: B59488348 After: B59304642 \*\*1,5,8,10,11\*\*

Routine Name: BPSOSCC

Before: B25822348 After: B26536547 \*\*1,2,5,8,10,11\*\*

Routine Name: BPSOSCD

Before: B76120342 After: B71384866 \*\*1,3,2,5,7,8,10,11\*\*

Routine Name: BPSOSCE

Before: B12883469 After: B12221266 \*\*1,5,7,8,10,11\*\*

Routine Name: BPSOSHF

Before: B48018870 After: B41365864 \*\*1,5,8,10,11\*\*

Routine Name: BPSOSIY

Before: B68639944 After: B71169390 \*\*1,3,5,6,7,8,10,11\*\*

Routine Name: BPSOSO2

Before: B33642927 After: B33643009 \*\*1,3,5,10,11\*\*

Routine Name: BPSOSRB

Before: B37930857 After: B38172979 \*\*1,5,7,8,10,11\*\*

Routine Name: BPSOSRX2

Before: B31124186 After: B33272416 \*\*7,8,10,11\*\*

Routine Name: BPSOSRX3

Before:B117328424 After:B119940068 \*\*7,8,10,11\*\*

Routine Name: BPSOSRX4

Before: B57083414 After: B62988205 \*\*7,8,10,11\*\*

Routine Name: BPSOSRX5

Before: B45774231 After: B43074906 \*\*7,8,10,11\*\*

Routine Name: BPSOSRX8

Before: B22878740 After: B21154002 \*\*7,10,11\*\*

Routine Name: BPSOSSG

Before: B29948946 After: B31935652 \*\*1,5,10,11\*\*

Routine Name: BPSOSUC

Before: B9012826 After: B8834830 \*\*1,5,7,10,11\*\*

Routine Name: BPSPRRX

Before:B106329171 After:B105159701 \*\*8,9,11\*\*

Routine Name: BPSPRRX2

Before: B8324629 After: B4776068 \*\*8,11\*\*

Routine Name: BPSPRRX3

Before:B196212053 After:B136159744 \*\*8,10,11\*\*

Routine Name: BPSPRRX4

Before: B20637795 After: B9705676 \*\*8,9,11\*\*

Routine Name: BPSPRRX5

Before: B48238265 After: B46870876 \*\*8,10,11\*\*

Routine Name: BPSPRRX6

Before: B57670037 After:B112918559 \*\*8,10,11\*\*

Routine Name: BPSREOP1

Before: B59523437 After: B60493248 \*\*3,7,10,11\*\*

Routine Name: BPSRES

Before:B125666033 After:B155712159 \*\*3,5,7,8,10,11\*\*

Routine Name: BPSRPT0

Before: B22539987 After: B22597769 \*\*1,5,7,10,11\*\*

Routine Name: BPSRPT1

Before: B53891828 After: B54969091 \*\*1,5,7,8,10,11\*\*

Routine Name: BPSRPT3

Before: B37506169 After: B38545074 \*\*1,3,5,7,11\*\*

Routine Name: BPSRPT4

Before: B76530531 After: B93729370 \*\*1,5,7,8,10,11\*\*

Routine Name: BPSRPT5

Before:B136990119 After:B146517138 \*\*1,3,5,7,8,10,11\*\*

Routine Name: BPSRPT7

Before:B105055369 After:B107914214 \*\*1,3,5,7,8,10,11\*\*

Routine Name: BPSRPT8

Before:B125609567 After:B178450227 \*\*1,3,5,7,8,10,11\*\*

Routine Name: BPSSCR01

Before: B17522420 After: B17522420 \*\*1,5,11\*\*

Routine Name: BPSSCR02

Before: B42496170 After: B45202471 \*\*1,3,7,10,11\*\*

Routine Name: BPSSCR03

Before: B40126137 After: B42385571 \*\*1,5,7,8,10,11\*\*

Routine Name: BPSSCR04

Before: B53618434 After: B53618434 \*\*1,5,11\*\*

Routine Name: BPSSCRCL

Before: B76318080 After: B76318080 \*\*1,3,5,7,8,11\*\*

Routine Name: BPSSCRCV

Before: B45399490 After: B46628770 \*\*1,5,7,11\*\*

Routine Name: BPSSCRLG

Before:B171520017 After:B232085722 \*\*1,5,7,8,10,11\*\*

Routine Name: BPSSCRRS

Before: B34060825 After: B38581404 \*\*1,3,5,7,8,10,11\*\*

Routine Name: BPSSCRSL

Before: B14489161 After: B14563351 \*\*1,7,11\*\*

Routine Name: BPSSCRU1

Before: B2399860 After: B1962116 \*\*1,11\*\*

Routine Name: BPSSCRU2

Before: B46275468 After: B47071661 \*\*1,3,5,10,11\*\*

Routine Name: BPSTEST

Before: B93493261 After: B93493717 \*\*6,7,8,10,11\*\*

Routine Name: BPSUSCR1

Before: B52105056 After: B78355256 \*\*1,5,7,10,11\*\*

Routine Name: BPSUSCR2

Before: B14190168 After: B13930186 \*\*7,10,11\*\*

Routine Name: BPSUSCR4

Before: B15393480 After: B14730277 \*\*1,3,7,10,11\*\*

Routine Name: BPSUTIL2

Before: B28691065 After: B32920062 \*\*7,8,10,11\*\*

Routine Name: BPSVRX

Before: n/a After:B234422538 \*\*11\*\*

Routine Name: BPSVRX1

Before: n/a After:B188435062 \*\*11\*\*

Routine Name: BPSVRX2

Before: n/a After:B141561911 \*\*11\*\*

Routine Name: BPSWRKLS

Before: B31684663 After: B31684664 \*\*7,8,11\*\*

Routine list of preceding patches: 12

### New NCPDP Reject Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new reject code "eC" has been added to the BPS NCPDP REJECT CODES file (#9002313.93). The associated description for this new code is CHAMPVA- DRUG NON BILLABLE.

### New CHAMPVA Mailgroup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new mailgroup for CHAMPVA claims has been created with this patch. When ECME has problems in processing a CHAMPVA claim, a message will be sent to this mailgroup. Members can be added to the mailgroup by using the Mail Group Edit \[XMEDITMG\] option.

### Changes to ECME Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Payable Claims Report \[BPS RPT PAYABLE\], Reversal Claims Report \[BPS RPT REVERSAL\], and Closed Claims Report \[BPS RPT CLOSED CLAIMS\] have been modified to include the patient eligibility (VETERAN, TRICARE, or CHAMPVA). The report display and the Excel output version now contain a column header and data for eligibility. A new filter has been added to these reports that allows the user to select a specific patient eligibility or ALL. In addition, the location of the eligibility column on both the screen display and Excel output of the Rejected Claims Report \[BPS RPT REJECTION\] was moved to match the other reports.

### CHAMPVA Eligibility Displayed on ECME User Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For CHAMPVA eligible patients, the ECME User Screen displays CVA eligibility as part of the patient/insurance line.

### Changes to Change View Action of the ECME User Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Change View action of the ECME User Screen \[BPS USER SCREEN\] allows the user to select NCPDP submissions with a CHAMPVA patient eligibility.
- The Change View action of the ECME User Screen \[BPS USER SCREEN\] allows the user to select NCPDP submissions with an UNSTRANDED status.

### Comment Display for Ignored Claim Rejections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a claim rejection has been ignored by using the IGN action on the Third Party Payer Rejects – Worklist \[PSO REJECTS WORKLIST\] or via the Reject Notification Screen, the comment entered during the ignore process will be displayed in the ECME User Screen \[BPS USER SCREEN\] prefaced by the word "IGNORED".

### Changes to Resubmit with Edits Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When using the Resubmit with Edits (RED) action on the ECME User Screen \[BPS USER SCREEN\], the user will now be allowed to edit the Date of Service field on an ECME claim if the prescription is released. Additionally, the Relationship Code prompt was changed to Pharmacy Relationship Code and the Person Code prompt was changed to Pharmacy Person Code. Also, the list of submission clarification codes that can be selected has been updated to reflect new values in the NCPDP standard.

### View ePharmacy Rx \[BPS RPT (Option Name TBD)\] Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new report called View ePharmacy Rx is now available from multiple locations in ECME and Outpatient Pharmacy. This new report combines data from multiple screens and reports in Outpatient Pharmacy, ECME, and Integrated Billing. The combined data is presented in a single List Manager screen. In ECME, this report is available via the View ePharmacy Rx \[BPS RPT VIEW ECME RX\] option on the Other Reports \[BPS MENU RPT OTHER\] menu.

### Changes to Print Claim Log Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LOG action – Print Claim Log – of the ECME User Screen \[BPS USER SCREEN\] has been enhanced as follows:

- NCPDP quantity and units are displayed if they exist and Billed quantity and units are displayed.
- All of the fees, costs and amounts sent on an ECME claim are now displayed with the proper field labels.
- Extraneous whitespace has been removed.

### Changes to Date of Service Calculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePharmacy Date of Service calculation algorithm has been modified with this patch. The fill date is no longer considered an acceptable value for the date of service. The algorithm uses the release date if it exists. If the release date doesn't exist, then the system uses the current date.

### Display of Fill Date changed to Date of Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

References in the ECME system to Fill Date have been changed to be Date of Service to indicate more accurately the data being displayed.

### Removal of Outbound HL7 Messages from Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME system now has the ability to remove outbound messages from the HL7 queue if the user unstrands a claim using the option View/Unstrand Submissions Not Completed \[BPS UNSTRAND SCREEN\].

### Processing of "Duplicate" Response 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an NCPDP response with a DUPLICATE status is received, the ECME system will now process that response as a normal payable response in order to create bills in IB and AR if a bill does not yet exist. The IB system will make that determination.

### "P2" Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME system will now use the indicator "P2" to indicate that the ECME claim was initiated by the PRO option – Process Secondary/TRICARE Rx to ECME \[BPS COB PROCESS SECOND TRICARE\]. The user will also be able to filter results on the ECME User Screen \[BPS USER SCREEN\] and on the ECME Claims Reports by RT – Real Time Fills, BB – Backbilling, or P2 – PRO option.

### Use of IB Fees and Costs on Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME system receives all appropriate fees and costs from the Integrated Billing system and uses them in the correct NCPDP fields on the claim. These include:

- Dispensing Fee (412-DC)
- Basis of Cost Determination (423-DN)
- Gross Amount Due (430-DU)
- Administrative Fee (480-H9)
- Ingredient Cost (409-D9)
- Usual and Customary Charge (426-DQ)

### Display of IB Fees and Costs in Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several ECME reports have been updated to display the above fees and costs when using the Excel output versions of the report data.

### Change to Process Secondary/TRICARE Rx to ECME Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Process Secondary/TRICARE Rx to ECME \[BPS COB PROCESS SECOND TRICARE\] option was modified to correctly handle the previous payment when the primary claim was paper.

### New Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A bulletin is created whenever a primary claim is closed in ECME and there is an open secondary claim. This scenario can occur when and inpatient claim is auto-reversed by the ECME Nightly Background Job or if the prescription is returned to stock or the prescription is deleted.

### New Reason Not Billable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the ECME Nightly Background Job does an inpatient auto-reversal, the reason not billable is set to 'INPATIENT RX AUTO-REVERSAL', which is a new non-billable reason created in Integrated Billing. Previously, the non-billable reason of 'OTHER' was used.

### Correction to \$BILLED Report Column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Payable Claims Report \[BPS RPT PAYABLE\], Rejected Claims Report \[BPS RPT REJECTION\], Claims Submitted, Not Yet Released Report \[BPS RPT NOT RELEASED\], and Spending Account Report \[BPS RPT SPENDING ACCOUNT\] have been corrected to display the correct amount in the \$BILLED column.

### New Service Requests (NSR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch addresses the following New Service Request (NSR):

> -------------------------------------------------

> Request Name: ePharmacy Claims Phase 6 (FY10)

> Request ID: 20090215

### Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no Remedy Tickets associated with this patch.

###

### From: BPS*1*20 ECME Release Notes

## Documentation and Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to retrieve files from REDACTED.

This transmits the files from the first available server. Sites may also elect

to retrieve files directly from a specific server.

Sites may retrieve the documentation directly using Secure File Transfer

Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI

Field Offices:

Albany: REDACTED

Hines: REDACTED

Salt Lake City: REDACTED

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl

Title File Name Transfer Mode

---------------------------------------------------------------------------

Release Notes/Installation Guide BPS_1_P20_RN.PDF Binary

User Manual BPS_1_UM.PDF Binary

Technical Manual/Security Guide BPS_1_TM.PDF Binary

*(This page included for two-sided copying.)*

## Overview of Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not able to be a "one size fits all." The general strategy for VistA rollback is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch; otherwise, the site should contact the Enterprise Program Management Office (EPMO) directly for specific solutions to their unique problems.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA Installation Procedure of the KIDS build, the installer can back up the modified routines using the 'Backup a Transport Global' action. The installer can restore the routines using the MailMan message that were saved prior to installing the patch. The backout procedure for global, data dictionary and other VistA components is more complex and will require issuance of a follow-up patch to ensure all components are properly removed. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with restoration of the data. This backout may need to include a database cleanup process.

Please contact the EPMO for assistance if the installed patch that needs to be backed out contains anything at all besides routines before trying to backout the patch. If the installed patch that needs to be backed out includes a pre or post install routine please contact the EPMO before attempting the backout.

From the Kernel Installation and Distribution System Menu, select

the Installation Menu.  From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch \#.

    a. Backup a Transport Global - This option will create a backup

       message of any routines exported with this patch. It will not

       backup any other changes such as DD's or templates.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure for VistA patches is complicated and may require a follow-up patch to fully roll back to the pre-patch state. This is due to the possibility of Data Dictionary updates, Data updates, cross references, and transmissions from VistA to offsite data stores.

Please contact the product development team for assistance if needed.

*(This page included for two-sided copying.)*

## System Feature: ECME User Screen Comment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the ECME User screen \[BPS USERS SCREEN\], the user is able to enter a comment that will display on the pharmacist's worklist.

## System Feature: ECME Resubmit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a resubmit is initiated from ECME, the system captures information.

## System Feature: ECME User Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME User screen \[BPS USERS SCREEN\] shows a resubmission indicator, a new OPECC Reject Information action, and a new action to resubmit a claim without a reversal. Also, several actions have been hidden, unhidden or removed.

## System Feature: ECME User Screen Non-Billable Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME User screen \[BPS USERS SCREEN\] displays non-billable entries, displayed with an open/close indicator. Several actions are unavailable for non-billable entries.

## System Feature: Closed Claims Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Closed Claims Report \[BPS RPT CLOSED CLAIMS\] displays the billed amount in the Excel download format.

## System Feature: Potential Claims Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Potential TRICARE Claims Report \[BPS COB RPT TRICARE CLAIMS\] is renamed to Potential Claims Report for Dual Eligible \[BPS POTENTIAL CLAIMS RPT DUAL\]. The Potential Claims Report for Dual Eligible \[BPS POTENTIAL CLAIMS RPT DUAL\] displays eligibility and can sort by eligibility.

## System Feature: Report Resubmission Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA ECME system uses indicator "RS" to indicate that a claim has been resubmitted via the ECME User Screen \[BPS USER SCREEN and reports filters allow the users to select resubmission as a filter option.

## System Features: Date of Service Algorithm 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option to Process Secondary/TRICARE Rx to ECME \[BPS COB PROCESS SECOND TRICARE\] uses the same date of service algorithm used in outpatient pharmacy.

## System Features: OPECC Productivity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system contains a report for OPECC productivity which requires new security key BPS SUPERVISOR.

## System Features: NCPDP Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system supports NCPDP Telecommunications version E7 according to the October 2015 NCPDP release. Support for new and modified reject codes through this release is also included.

### From: BPS*1*15 ECME Release Notes

## Functional Specifications for Electronic Claims Management Engine (ECME)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Miscellaneous Decommissioned Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Remove Drugs non-Covered Report

The BPS MENU MAINTENANCE Menu no longer contained the following option:

> NON Drugs Non-Covered Report

This requirement pertains to decommissioned functionality.

#### Remove reference to IB NDC NON-COVERED BY PLAN

The VistA system no longer referenced file IB NDC NON-COVERED BY PLAN (366.16).

The ECME code no longer added data to the file. ECME routine BPSOSQL was modified by removing the call to UPDLST^IBNCDNC, which added data to file IB NDC NON-COVERED BY PLAN (366.16).

This requirement pertains to decommissioned functionality.

### ECL Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Change the ID for field 501, Header Response Status

The VistA ePharmacy system contained an ID of "F1" for field 501, Header Response Status.

In file 902313.91 BPS NCPDP FIELD DEFS, the ID field was "F1" for entry 501, Header Response Status.

#### Increase Length for Field 450, Compound Dosage Form Description Code

The VistA ePharmacy system accommodated 15 characters for Field 450, Compound Dosage Form Description Code.

The field length was increased from 4 characters to 15 characters.

#### Apply Annual Update

The VistA ePharmacy system contained the annual updates to the ECL values as of NCPDP compliance date 10/15/2012.

#### No Duplicate Reject Codes

The updates to the ECL values were applied such that there were no duplicate reject codes in the affected VistA ePharmacy database.

#### No Leading Spaces in Code

The updates to the ECL values were applied such that the reject codes did not have leading spaces in the affected VistA ePharmacy database.

#### No Trailing Spaces in Code

The updates to the ECL values were applied such that the reject codes did not have trailing spaces in the affected VistA ePharmacy database.

#### No Leading Spaces in Description

The updates to the ECL values were applied such that the reject code descriptions did not have leading spaces in the affected VistA ePharmacy database.

#### No Trailing Spaces in Description

The updates to the ECL values were applied such that the reject code descriptions did not have trailing spaces in the affected VistA ePharmacy database.

#### No Descriptions that Exceed 70 Characters

The updates to the ECL values were applied such that the reject code descriptions do not exceed a length of 70 characters in the affected VistA ePharmacy database.

### Telecommunications Standards for NCPDP versions D.1 – D.9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Modify Database for Alpha Characters

The VistA database was modified so that the NCPDP code can contain an alphabetic character within the first three characters of the code.

The NCPDP codes allowed an alphabetic character, preceding the hyphen. For example, "B04-BT" is now a valid NCPDP code.

#### Accommodate the Alpha Character Database Change

The VistA ePharmacy system was modified so that the info structure accommodated the database modification for the NCPDP code.

#### Support new Data Elements

The VistA ePharmacy system supported new data elements for NCPDP versions D.1 through D.9. The new data elements are listed below.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>NCPDP ID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>579-582</td>
<td>Associated prescription/service information.</td>
</tr>
<tr class="even">
<td>583-587</td>
<td>Service provider information: name, address, city, state, zip</td>
</tr>
<tr class="odd">
<td>590</td>
<td>Seller initials</td>
</tr>
<tr class="even">
<td>591-677</td>
<td>Purchaser Information: ID qualifier, Purchaser ID, gender code, DOB, sex, city, state, zip</td>
</tr>
<tr class="odd">
<td>678</td>
<td>Time of Service</td>
</tr>
<tr class="even">
<td>679-680</td>
<td>Seller ID and Qualifier</td>
</tr>
<tr class="odd">
<td>681</td>
<td>Sales Transaction ID</td>
</tr>
<tr class="even">
<td>A22</td>
<td>Patient ID state or province code</td>
</tr>
<tr class="odd">
<td>A23</td>
<td>Purchaser relationship code</td>
</tr>
<tr class="even">
<td>A24-A27</td>
<td>Prescriber ID, alternate ID</td>
</tr>
<tr class="odd">
<td>A28</td>
<td>Adjudicated payment type</td>
</tr>
<tr class="even">
<td>A29</td>
<td>Reported payment type<br />
May be outbound</td>
</tr>
<tr class="odd">
<td>A30-A31</td>
<td>Released date, released time</td>
</tr>
<tr class="even">
<td>A32</td>
<td>Compound preparation time</td>
</tr>
<tr class="odd">
<td>A43</td>
<td>Patient Country Code codes</td>
</tr>
<tr class="even">
<td>A45</td>
<td>Veterinary use indicator</td>
</tr>
<tr class="odd">
<td>B04</td>
<td>Next available fill date</td>
</tr>
</tbody>
</table>

#### Use Pharmacist's Initials

The data transmitted for an NCPDP claim showed the pharmacist's initials for NCPDP field 590-YT, seller's initials.

#### Use Time of Service

The data transmitted for an NCPDP claim showed the time of service for NCPDP field 678-Y6, time of service.

The current time was used for the first transmission. All subsequent transmissions used this same time.

#### Use Pharmacist's Identifier

The data transmitted for an NCPDP claim showed the pharmacist's identifier for NCPDP field 679-Y9, seller's identification.

The internal number used for the pharmacist with the station number was appended to that value.

#### Store the Next Available Fill Date

The VistA database stored the next available fill date returned in NCPDP field B04-BT.

### Messages for "not processed for site"

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### TRICARE Messages

The ePharmacy system no longer generated or sent "not processed for site" messages to the BPS TRICARE mail group for released TRICARE prescriptions.

#### CHAMPVA Messages

The ePharmacy system no longer generated or sent "not processed for site" messages to the BPS CHAMPVA mail group for released CHAMPVA prescriptions.

#### Veteran Messages

The ePharmacy system no longer generated or sent "not processed for site" messages to the BPS OPECC mail group for released Veteran prescriptions.

### ECME User Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Display a Comment for Transfer Rejects

The ECME User Screen displayed a comment to indicate an automatic transfer to the Third Party Payer Rejects – Worklist occurred for a transfer reject code.

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 OPPATIENT, ONE (282P) EPHARM I/444-444-4444 VET Pb:0 Rj:1 AcRv:0 RjRv:0

1.1 AMPICILLIN 250MG 55370088008 11/20 2719998\$ 0/000004316840 W RT AC/N

11/20/12 – Auto Send to Pharmacy Worklist due to Transfer Reject Code

(OPUSER, NAME)

p-Rejected

#### Display a Comment for Reject Resolution Required

The ECME User Screen displayed a comment to indicate an automatic transfer to the Third Party Payer Rejects – Worklist occurred for a Reject Resolution Required code.

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 OPPATIENT, ONE (282P) EPHARM I/444-444-4444 VET Pb:0 Rj:1 AcRv:0 RjRv:0

1.1 AMPICILLIN 250MG 55370088008 11/20 2719998\$ 0/000004316840 W RT AC/N

11/20/12 – Auto Send to Pharmacy Worklist due to Reject Resolution Required

(OPUSER, NAME)

p-Rejected

#### Move Copay Question

The ECME User Screen action to close a claim asked the release copay question after the additional insurance question.

This patient has ADDITIONAL insurance with Rx Coverage that may be

used to bill this claim. The system will change the CT entry to a

NON-BILLABLE Episode. If appropriate, please go to the ECME Pharmacy

COB Menu and use the PRO – Process Secondary/TRICARE Rx to ECME

option to create an ePharmacy secondary claim.

Patient: OPPATIENT, ONE

Date of service: APR 09, 2012

Insurance: EPHARM INSURANCE

Group number: 12345

AMOXICILLIN 250MG 00029600632 11/27 2720010\$ 0/000004316852 W RT AC/R

Do you want to print the information (above) concerning additional

insurance?

(Y/N)? n NO

ALL Selected Rxs were CLOSED using the same information gathered in the

following prompts.

Are you sure?(Y/N)? Y

Select CLAIMS TRACKING NON-BILLABLE REASONS NAME: 39 NON-COVERED DRUG PER PLAN

Comment : ECME rej/med not cov

Release Patient CoPay(Y/N)? y YES

Are you sure?(Y/N)? y YES

#### Display Next Available Fill Date

The ECME Claim Log displayed the next available fill date received in NCPDP field B04-BT.

If there was no data to display for the next available fill, the new label should not have been displayed.

Response Information (CLAIM REQUEST)(#1932)-----------------------------------

Response Received: NOV 20,2012@17:46:51

Date of Service: 11/20/2012

Next Available Fill Date: 12/20/2012

Transaction Response Status: Rejected

Total Amount Paid: \$

Ingredient Cost Paid: \$15.33 Dispensing Fee Paid: \$0.00

Patient Resp (INS): (\$10.00)

Reject code(s):

229:Patient Phone Number is not used for this Transaction Code

Payer Message: EMD 1000: CLAIM PAID

Payer Additional Message: EMD 1000: CLAIM PAID RX:000004316840FILL:2012-11-2

0 BIN:610144 PCN:TEST

Reason for Service Code:

DUR Text:

DUR Additional Text:

### ECME Claims Response Inquiry (CRI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Display Next Available Fill Date

The ECME Claims-Response Inquiry Report displayed the next available fill date received in NCPDP field B04-BT.

If there was no data to display for the next available fill, the new label should not have been displayed.

### From: BPS*1*18 ECME Release Notes

## System Feature: ePharmacy Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ePharmacy Transactions - Maintain the Pharmacy Bank Identification Number/Processor Control Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HPID/OEID does not replace the pharmacy Bank Identification Number/Processor Control Number (BIN/PCN) identifier in electronic pharmacy transactions.

<u>Note:</u> The BIN/PCN are tied to the entity that will be processing the transaction or where the transaction is to be sent (routing) and are used for effective and efficient pharmacy claim adjudication. Use of BIN/PCN is mandatory in electronic pharmacy transactions.

### ePharmacy Transactions - ePharmacy HPID/OEID Data Contained in the NCPDP (National Council for Prescription Drug Program) Response Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software provides the ability for ePharmacy HPID/OEID data to be received and stored in ECME when contained in the NCPDP response segment from the Processor/Payer/PBM (Pharmacy Benefit Management)/ Intermediary/TPA (Third Party Administrator).

### ePharmacy Transactions - ePharmacy Software to Recognize the HPID/OEID Data Returned in the NCPDP Response Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePharmacy software recognizes the HPID/OEID data being returned in the NCPDP Response segments.

## System Feature: Reports/Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Reports/Screens - Modify the following ePharmacy Screens/Reports to Include the HPID/OEID 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following ePharmacy screens/reports include the HPID/OEID ID:

- Print Claim Log \[BPS PRTCL USRCR CLAIM LOG\] (when included in the incoming response)
- ECME Billing Events Report \[IB ECME BILLING EVENTS\]
- ECME Claims-Response Inquiry Report \[BPS RPT CLAIMS RESPONSE\] (when included in the incoming response)
- Third Party Joint Inquiry (TPJI), Claim Information \[IBJ THIRD PARTY JOINT INQUIRY\] (below the ECME Ap No and NPI) (when included in the incoming response)
- TPJI, ECME Rx information \[IBJ THIRD PARTY JOINT INQUIRY\] (below the ECME Ap No) (when included in the incoming response)
- Coordination of Benefit screens/reports (ECME option ECME Pharmacy COB) include:
  - SEC Potential Secondary Rx Claims Report
  - TRI Potential TRICARE Claims Report

### From: BPS*1*19 ECME Release Notes

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Updated documentation describing the new functionality introduced by this patch is available.

> The preferred method is to FTP the files from : REDACTED This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

> Albany REDACTED

> Hines REDACTED

> Salt Lake City REDACTED

> Documentation can also be found on the VA Software Documentation Library at: [http://www.va.gov/vdl/](%20http://www.va.gov/vdl/)

> Title File Name FTP Mode

> Release Notes/Installation Guide BPS_1_P19_RN.PDF Binary User Manual BPS_1_UM_R0116.PDF Binary Technical Manual/Security Guide BPS_1_TM_R0116.PDF Binary

#### (This page included for two-sided copying.)

## Routine Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The second line of each of these routines now looks like:

> ;;1.0;E CLAIMS MGMT ENGINE;\*\*\[Patch List\]\*\*;JUN 2004;Build 18

> The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

> Routine Name: BPS19PRE

> Before: n/a After: B6858890 \*\*19\*\* Routine Name: BPS19PST

> Before: n/a After: B32874086 \*\*19\*\* Routine Name: BPSECA1

> Before: B14865597 After: B14554293 \*\*1,5,8,10,15,19\*\*

> Routine Name: BPSECMP2

> Before:B189210451 After:B193647932 \*\*1,5,6,7,8,10,11,19\*\*

> Routine Name: BPSECMPS

> Before:B102705765 After:B117919679 \*\*1,2,5,6,7,10,11,15,19\*\*

> Routine Name: BPSECX0

> Before: B36997821 After: B39590401 \*\*1,5,8,10,15,19\*\*

> Routine Name: BPSJHLT

> Before: B56892934 After: B56866826 \*\*1,10,15,19\*\*

> Routine Name: BPSJZPR

> Before: B67732564 After: B69333659 \*\*1,10,15,19\*\*

> Routine Name: BPSNCPD1

> Before: B55346306 After: B55779572 \*\*1,3,5,6,7,8,9,10,11,15,19\*\*

> Routine Name: BPSNCPD3

> Before: B63091448 After: B64625279 \*\*1,5,6,7,8,10,11,15,19\*\*

> Routine Name: BPSNCPDP

> Before: B93011711 After: B93601523 \*\*1,3,4,2,5,6,7,8,10,11,19\*\*

> Routine Name: BPSOSCC

> Before: B26536547 After: B27473638 \*\*1,2,5,8,10,11,19\*\*

> Routine Name: BPSOSCD

> Before: B85972758 After:B104589879 \*\*1,3,2,5,7,8,10,11,15,19\*\*

> Routine Name: BPSOSCE

> Before: B12911947 After: B13028933 \*\*1,5,7,8,10,11,15,19\*\*

> Routine Name: BPSOSCF

> Before: B30647894 After: B30984367 \*\*1,5,8,10,15,19\*\*

> Routine Name: BPSOSH2

> Before:B138588771 After:B141967265 \*\*1,5,8,10,15,19\*\*

> Routine Name: BPSPRRX3

> Before:B136159744 After:B123904591 \*\*8,10,11,19\*\*

> Routine Name: BPSPRRX6

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 31%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Before:B112918559</th>
<th>After:B114820084</th>
<th><blockquote>
<p>8,10,11,19</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Routine Name: BPSRPAY</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Before: B34787453</td>
<td>After: B35888506</td>
<td><blockquote>
<p>1,7,10,15,19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Routine Name: BPSRPT0</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 28%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Before: B22597769</p>
</blockquote></th>
<th>After: B27167649</th>
<th><blockquote>
<p>1,5,7,10,11,19</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Routine Name: BPSRPT1</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Before: B54969091</p>
</blockquote></td>
<td>After: B58952344</td>
<td><blockquote>
<p>1,5,7,8,10,11,19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Routine Name: BPSRPT3</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Before: B39556380</p>
</blockquote></td>
<td>After:B122921088</td>
<td><blockquote>
<p>1,3,5,7,11,14,19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Routine Name: BPSRPT4</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Before: B93729370</p>
</blockquote></td>
<td>After: B99407580</td>
<td><blockquote>
<p>1,5,7,8,10,11,19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Routine Name: BPSRPT5</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Before:B146517138</p>
</blockquote></td>
<td>After:B167824717</td>
<td><blockquote>
<p>1,3,5,7,8,10,11,19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Routine Name: BPSRPT7</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Before:B107914214</p>
</blockquote></td>
<td>After:B164190587</td>
<td><blockquote>
<p>1,3,5,7,8,10,11,19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Routine Name: BPSRPT8</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Before:B178450227</p>
</blockquote></td>
<td>After:B147944651</td>
<td><blockquote>
<p>1,3,5,7,8,10,11,19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Routine Name: BPSSCRCL</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Before: B75888961</p>
</blockquote></td>
<td>After: B82378286</td>
<td><blockquote>
<p>1,3,5,7,8,11,15,19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Routine Name: BPSTEST</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Before:B102852240</p>
</blockquote></td>
<td>After:B147504088</td>
<td><blockquote>
<p>6,7,8,10,11,15,19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Routine Name: BPSUTIL2</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Before: B52546743 After: B53070606 \*\*7,8,10,11,17,19\*\*

> Routine list of preceding patches: 14, 15, 17

### NCPDP Version E.0 through E.6.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The VistA ePharmacy system is modified to support new data elements for NCPDP versions E.0 through .6.

#### The BPS NCPDP FIELD DEFS ((#9002313.91) file was updated with new and modified NCPDP field information.

#### The BPS NCPDP REJECT CODES (#9002313.93) file was updated with new and modified NCPDP reject codes.

#### The claims submission process was updated to send data for new NCPDP fields for which VistA has data to send. In addition, some existing fields were updated to include additional NCPDP values. The list of NCPDP fields that had modifications and also have a major impact on NCPDP processing is below.

#### <u>Patient Segment</u>

#### B08-7A - Patient Street Address Line B09-7B - Patient Street Address Line 2

#### B38-1Y - Patient ID Associated Country Code

#### <u>Prescriber Segment</u>

#### B26-7T - Prescriber Telephone Number Extension B27-7U - Prescriber Street Address Line 1

#### B28-7V - Prescriber Street Address Line 2

#### B40-3A - Prescriber Alternate ID Associated Country Code B41-3B - Prescriber ID Associated Country Code

#### B42-3C - Prescriber Country Code <u>Pricing Segment</u>

#### 479-H8 - Other Amount Claimed Submitted Qualifier <u>Coordination of Benefits/Other Payers Segment</u>

#### 342-HC - Other Payer Amount Paid Qualifier) 393-MV - Benefit Stage Qualifier)

#### 339-6C - Other Payer ID Qualifier)

#### The claims response process was updated to include new NCPDP fields and to process existing NCPDP fields that had changes to the data that can be returned by the third party payer. The list of NCPDP fields that had modifications and also have a major impact on NCPDP processing is below.

#### <u>Response Insurance Segment</u>

#### 568-J7 - Payer ID Qualifier <u>Response Pricing Segment</u>

#### 561-AZ - Percentage Sales Tax Basis Paid 564-J3 - Other Amount Paid Qualifier

#### <u>Response Coordination of Benefits/Other Payers Segment</u>

#### B23-7Q - Other Payer Help Desk Telephone Number Extension <u>Response Intermediary Segment</u>

#### B52-8R - Response Intermediary Authorization Count 53-8S - Response Intermediary Authorization Type ID B54-8TB - Response Intermediary Authorization ID B51-8Q - Intermediary Message

### Close Claim Action Medication on ECME User Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The Close Claim \[CLO\] action on the ECME User Screen \[BPS USER SCREEN\] option was modified to prevent a claim from being closed if the claim has open rejects on the Pharmacist worklist.

### RXs Not Processed for Site bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The Rx Not Processed for Site bulletin was modified to direct the user to the correct ECME option in order to get more information on the reject.

### Rx Not Processed for Site bulletin to Include ECME Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The Rx Not Processed for Site bulletin was modified to include the associated ECME number, if it exists

### Claim Results and Status Menu Modification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The Claim Results and Status \[BPS MENU RPT CLAIM STATUS\] menu was modified to include a new Non-Billable Status Report \[BPS RPT NON-BILLABLE REPORT\] option. This new report will provide users with a tool to identify prescriptions that are not being billed and the reason the prescription was not billed.

### TRICARE OR CHAMPVA Inpatient Claim Reversals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### All inpatient claims, whether for Veteran, CHAMPVA or TRICARE, are now filled and billed to a third party payer. The BPS Nightly Background Job will reverse the claims that should not be billable (TRICARE and CHAMPVA).

#### If a TRICARE or CHAMPVA inpatient claim is reversed by the inpatient auto reversal process of the BPS NIGHTLY BACKGROUND JOB, the transaction will be filed in the PSO AUDIT LOG (#52.87) file as a bypass prescription so that it will be displayed on the TRICARE- CHAMPVA Bypass/Override Report, which is part of the Outpatient Pharmacy application.
