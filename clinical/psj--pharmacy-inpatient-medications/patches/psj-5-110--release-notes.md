---
title: PSJ*5*110 Release Notes-IMR-Phase I
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: IMR-Phase I
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*110
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - order
  - orders
  - patient
  - renewed
  - table
  - contents
  - inpatient
  - complex
  - stat
  - renew
page_count: 0
word_count: 3477
section_count: 5
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p110_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p110_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

> ![](psj-5-110-release-notes-imr-phase-i/001.png)

Inpatient Medications Requirements for theSpecial Focus Group Initial Request AnalysisPhase IRELEASE NOTES

PSS\*1\*79

PSJ\*5\*110

OR\*3\*213

PSU\*3\*34

September 2004

V*IST*A Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Required Setup](#required-setup)
- [New Features and Functionality](#new-features-and-functionality)
  - [Complex Orders](#complex-orders)
  - [Renewed Orders](#renewed-orders)
    - [## STAT and NOW Order Notification](#stat-and-now-order-notification)
    - [Adding a User as a Subscriber](#adding-a-user-as-a-subscriber)
    - [### Adding a Remote Member as a Subscriber](#adding-a-remote-member-as-a-subscriber)
  - [Files, Fields, and Cross-References](#files-fields-and-cross-references)
    - [New Files](#new-files)
    - [Changed Files](#changed-files)
    - [New Fields](#new-fields)
    - [Changed Fields](#changed-fields)
    - [New Cross-References](#new-cross-references)
    - [Changed Cross-References](#changed-cross-references)
- [Impact on Other VISTA Software Packages](#impact-on-other-vista-software-packages)
Phase I of the Inpatient Medications Requirements for the Special Focus Group Initial Requirements Analysis (IMR for SFGIRA) includes upgrades to the Inpatient Medications, Pharmacy Benefits Management (PBM), Pharmacy Data Management (PDM), and Computerized Patient Record System (CPRS) software packages. The goal of Phase I is to optimize the functionality used by clinicians who enter, maintain, and administer medication orders. It can be accomplished by providing changes to pharmacy medication ordering and by improving the communication of order information between the Inpatient Medications and CPRS packages.
These Release Notes briefly describe the new features and functionality in phase I of this project, which are included as a host file with patches PSS\*1\*79, PSJ\*5\*110, OR\*3\*213, and PSU\*3\*34.
This host file can only be run with a standard M operating system. It also requires the following Department of Veterans Affairs (VA) software packages and versions.
|                                                                                           |                            |
|-------------------------------------------------------------------------------------------|----------------------------|
| Package                                                                               | Minimum Version Needed |
| Adverse Reaction Tracking (ART)                                                           | 4.0                        |
| Decision Support System                                                                   | 3.0                        |
| Fee Basis                                                                                 | 3.5                        |
| Integrated Funds Distribution, Control Point Activity, Accounting And Procurement (IFCAP) | 5.1                        |
| Inpatient Medications                                                                     | 5.0                        |
| Integrated Billing                                                                        | 2.0                        |
| Kernel                                                                                    | 8.0                        |
| Laboratory                                                                                | 5.2                        |
| MailMan                                                                                   | 8.0                        |
| National Drug File (NDF)                                                                  | 4.0                        |
| Order Entry/Results Reporting                                                             | 3.0                        |
| Outpatient Pharmacy                                                                       | 7.0                        |
| Patient Information Management System (PIMS)                                              | 5.3                        |
| Pharmacy Data Management                                                                  | 1.0                        |
| VA FileMan                                                                                | 22.0                       |

## Required Setup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites requiring the ability to renew expired IV orders may define a period of time up to 24 hours after expiration that orders may be renewed. The Expired IV Time Limit parameter can be edited by selecting the *Systems Parameters Edit* \[PSJ SYS EDIT\] option at the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option (see section 2.2., Renewed Orders).

New mail groups PSJ STAT NOW PENDING ORDER and PSJ STAT NOW ACTIVE ORDER are created during the installation of PSJ\*5\*110. However, notification of new STAT and NOW orders are not sent until subscribers are added to the mail groups (see section 2.3., STAT and NOW Order Notification).

# New Features and Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Phase I of the IMR for SFGIRA project, upgrades were made to enable the user to identify a Complex Order, calculate a new Stop Date/Time for an existing order during the renewal process, and receive messages when STAT or NOW orders have either been received from CPRS or have been verified and made active. These new features and functionality are described in this section.

## Complex Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the past, Complex Orders were not identified as such within Inpatient Medications and were often mistakenly identified as duplicate orders or orders that were independent of each other. A Complex Order now consists of one or more individual component orders, or ‘child’ orders, that are linked together. Inpatient Medications receives the parent order number from CPRS and links the child orders together.

If the actions FN (Finish), VF (Verify), DC (Discontinue), or RN (Renew) are taken on one child order, the action must be taken on all of the complex component orders in the set. For example,

- If one child order within a Complex Order is made active, all child orders in the Complex Order must be made active.
- If one child order within a Complex Order is discontinued, all child orders in the Complex Order must be discontinued.
- If one child order within a Complex Order is renewed, all child orders in the Complex Order must be renewed.

Once a Complex Order is made active, the following fields may not be edited:

- Administration Time
- Any field where an edit would cause a new order to be created. These fields are denoted with an asterisk in the Detailed View of a Complex Order.

If a change to one of these fields is necessary, the Complex Order must be discontinued and a new Complex Order must be created.

Sets of Complex Orders with a status of “Pending” or “Non-Verified” will be grouped together in the Profile View within Inpatient Medications. Once these orders are made active, they will appear individually in the Profile View.

  
Example: Pending Complex Order in Profile View

Inpatient Order Entry Mar 07, 2004@13:03:55 Page: 1 of 1

ALASKA,FRED Ward: ONE EAST

PID: 123-45-6789 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 03/03/04

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

\- - - - - - - - - - - - - P E N D I N G C O M P L E X - - - - - - - - - - - - - - - -

1 CAPTOPRIL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 25MG PO QD

CAPTOPRIL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 50MG PO BID

CAPTOPRIL TAB ? \*\*\*\*\* \*\*\*\*\* P

Give: 100MG PO TID

 

 

 

Enter ?? for more actions

PI Patient Information SO Select Order

PU Patient Record Update NO New Order Entry

Select Action: Next Screen//

Example: Non-Verified Complex Order in Profile View

Inpatient Order Entry Mar 07, 2004@13:03:55 Page: 1 of 1

ALASKA,FRED Ward: ONE EAST

PID: 123-45-6789 Room-Bed: B-12 Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 08/18/20 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 03/03/04

Dx: TESTING Last transferred: \*\*\*\*\*\*\*\*

\- - - - - - - - - - - - N O N - V E R I F I E D C O M P L E X - - - - - - - - - - - -

1 CAPTOPRIL TAB C 03/26 03/27 N

Give: 25MG PO QD

CAPTOPRIL TAB C 03/26 03/28 N

Give: 50MG PO BID

CAPTOPRIL TAB C 03/26 03/29 N

Give: 100MG PO TID

 

 

 

Enter ?? for more actions

PI Patient Information SO Select Order

PU Patient Record Update NO New Order Entry

Select Action: Next Screen//

  
Example: Active Complex Order in Profile View

Inpatient Order Entry Apr 13, 2004@09:08:51 Page: 2 of 2

COLORADO,ALBERT Ward: GEN MED A

PID: 123-45-6789 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 02/04/25 (79) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 04/12/04

Dx: SICK Last transferred: \*\*\*\*\*\*\*\*

\+

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - -

1 PREDNISONE TAB C 04/13 04/14 A

Give: 10 MG PO BID

2 PREDNISONE TAB C 04/15 04/16 A

Give: 5 MG PO BID

3 PREDNISONE TAB C 04/17 04/21 A

Give: 2.5 MG PO QD

Enter ?? for more actions

PI Patient Information SO Select Order

PU Patient Record Update NO New Order Entry

Select Action: Quit//

When an action of FN (Finish), VF (Verify), DC (Discontinue), or RN (Renew) is taken on a ‘child’ order, a message will display informing the user that the order is part of a Complex Order and that the action must be taken on all of the associated child orders.

Example: DC (Discontinue) Action – Complex Order

Select Item(s): Next Screen// DC Discontinue

This order is part of a complex order. If you discontinue this order the

following orders will be discontinued too (unless the stop date has already

been reached).

Press Return to continue...

AMOXAPINE TAB C 03/25 04/14 A

Give: 200MG PO QD

Do you want to discontinue this series of complex orders? Yes//

Example: RN (Renew) Action – Complex Order

Select Item(s): Next Screen// RN Renew

This order is part of a complex order. If you RENEW this order the

following orders will be RENEWED too.

Press Return to continue...

DAPSONE TAB C 04/12 04/16 A

Give: 200 MG PO TID

RENEW THIS COMPLEX ORDER SERIES? YES//

## Renewed Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RN (Renew) action in Inpatient Medications calculates a new Stop Date/Time for an existing order. Prior to Phase I of the IMR for SFGIRA project, the RN (Renew) action created a new order. This caused problems, including renewed and renewal orders appearing simultaneously on the Virtual Due List (VDL) in the Bar Code Medication Administration (BCMA) package.

Instead of creating a new order, Inpatient Medications will calculate a new Stop Date/Time for a Renewed Order during the renew process. This will help to reduce the risk of administration errors in BCMA by restricting a Renewed Order to one line item on the BCMA VDL. It will also provide more complete order information in Inpatient Medications by displaying the original Start Date/Time of the order along with the most recent renew date and time.

Functional changes to Renewed Orders include the following:

- The RN (Renew) action will be modified to remove the prompt for the Start Date/Time.
- The Renewed Date/Time will display on the Patient Profile screen.
- The Renewed Date/Time and the user renewing the order will display with the detailed order information in Inpatient Medications.
- The Start Date/Time of the Renewed Order will not change.
- Unit Dose and scheduled IV orders with a status of “Expired” can only be renewed if a scheduled dose was not missed since the last BCMA action was taken on the order.
- Continuous IV orders with a status of “Expired” may only be renewed if the number of hours that have elapsed since the order expired is less than the time limit defined in the EXPIRED IV TIME LIMIT field (#34) in the PHARMACY SYSTEM file (#59.7).
- Sites requiring the ability to renew expired IV orders must define a period of time up to 24 hours after expiration that orders may be renewed. The EXPIRED IV TIME LIMIT field (#34) in the PHARMACY SYSTEM file (#59.7) can be edited by selecting the *Systems Parameters Edit* \[PSJ SYS EDIT\] option at the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option.

Example: Renewed Order in Profile View Before RN (Renew) Action

Inpatient Order Entry Apr 13, 2004@09:08:51 Page: 1 of 1

COLORADO,ALBERT Ward: GEN MED

PID: 123-45-6789 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 02/04/25 (79) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 04/12/04

Dx: SICK Last transferred: \*\*\*\*\*\*\*\*

\+

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - -

1 DAPSONE TAB C 04/10 04/14 A

Give: 25 MG PO QD

Enter ?? for more actions

PI Patient Information SO Select Order

PU Patient Record Update NO New Order Entry

Select Action: Quit//

Example: Renewed Order in Detailed Order View – Information Screen Before RN (Renew) Action

ACTIVE UNIT DOSE Apr 13, 2004@09:42:14 Page: 1 of 2

MISSISSIPPI,RANDALL Ward: GEN MED

PID: 123-45-6789 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 03/03/23 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\*(1)Orderable Item: DAPSONE TAB

Instructions:

\*(2)Dosage Ordered: 100 MG

Duration: \*(3)Start: 04/10/04 06:00

\*(4) Med Route: ORAL

\*(5) Stop: 04/14/04 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QD

\(9\) Admin Times: 1440

\(10\) Provider: DENVER,DONNA

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

DAPSONE 100MG TAB

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen// RN Renew

RENEW THIS ORDER? YES// \<Enter\>

STOP DATE/TIME: MAY 3,2004@24:00// \<Enter\> MAY 3,2004@24:00

PROVIDER: DENVER,DONNA// \<Enter\>

NATURE OF ORDER: WRITTEN// \<Enter\>W

...updating order.....DONE!

Example: Renewed Order in Detailed Order View – First Information Screen After RN (Renew) Action

ACTIVE UNIT DOSE Apr 13, 2004@09:42:14 Page: 1 of 2

MISSISSIPPI,RANDALL Ward: GEN MED

PID: 123-45-6789 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 03/03/23 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

\+

\*(1)Orderable Item: DAPSONE TAB

Instructions:

\*(2)Dosage Ordered: 100 MG

Duration: \*(3)Start: 04/10/04 06:00

\*(4) Med Route: ORAL Renewed: 04/13/04 09:51

\*(5) Stop: 05/03/04 24:00

\(6\) Schedule Type: CONTINUOUS

\*(8) Schedule: QD

\(9\) Admin Times: 1440

\(10\) Provider: DENVER,DONNA

\(11\) Special Instructions:

\(12\) Dispense Drug U/D Inactive Date

DAPSONE 100MG TAB

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen//

  
Example: Renewed Order in Detailed Order View - Second Information Screen After RN (Renew) Action

ACTIVE UNIT DOSE Apr 13, 2004@09:42:14 Page: 2 of 2

MISSISSIPPI,RANDALL Ward: GEN MED

PID: 123-45-6789 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 03/03/23 (81) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

(7)Self Med: NO

Entry By: DENVER,DONNA Entry Date: 04/13/04 09:40

Renewed By: DENVER,DONNA

\(13\) Comments:

\+ Enter ?? for more actions

DC Discontinue ED Edit AL Activity Logs

HD Hold RN Renew

FL Flag VF (Verify)

Select Item(s): Next Screen//

Example: Renewed Order in Profile View after RN (Renew) Action

Inpatient Order Entry Apr 13, 2004@09:08:51 Page: 1 of 1

COLORADO,ALBERT Ward: GEN MED A

PID: 123-45-6789 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

DOB: 02/04/25 (79) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

Sex: MALE Admitted: 04/12/04

Dx: SICK Last transferred: \*\*\*\*\*\*\*\*

\+

\- - - - - - - - - - - - - - - - - A C T I V E - - - - - - - - - - - - - -

1 DAPSONE TAB C 04/10 05/03 A 04/13

Give: 25 MG PO QD

Enter ?? for more actions

PI Patient Information SO Select Order

PU Patient Record Update NO New Order Entry

Select Action: Quit//

### ## STAT and NOW Order Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A STAT and NOW Order Notification has been added in Inpatient Medications to send a text message to pharmacy and nursing staff when orders are received with a priority of STAT or a schedule of NOW. To receive these messages, the user must subscribe to the mail group(s) described below.

| Mail Group             | Description                                                                       |
|----------------------------|---------------------------------------------------------------------------------------|
| PSJ STAT NOW PENDING ORDER | Notifies the user when a pending STAT or NOW order has been received from CPRS.       |
| PSJ STAT NOW ACTIVE ORDER  | Notifies the user when a pending STAT or NOW order has been verified and made active. |

The following are examples of STAT and NOW Order Notification messages.

Example: Messages in a Subscriber’s Inbox

IN Basket, 218 messages (1-5), 5 new

\*=New/!=Priority.......Subject.........................From...................

\*1. GEN MED-PENDING STAT-ALASKA,FRED MEDICATIONS,INPATIENT

\*2. GEN MED-PENDING NOW- ALASKA,FRED MEDICATIONS,INPATIENT

\*3. GEN MED-ACTIVE STAT- ALASKA,FRED MEDICATIONS,INPATIENT

\*4. GEN MED-ACTIVE STAT- ALASKA,FRED MEDICATIONS,INPATIENT

\*5. GEN MED-ACTIVE NOW- ALASKA,FRED MEDICATIONS,INPATIENT

IN Basket Message: 1//

Example: Pending STAT Order Notification Message

Subj: GEN MED-PENDING STAT-ALASKA,FRED \[#88123\] 04/02/04@08:51 5 lines

From: MEDICATIONS,INPATIENT In 'IN' basket. Page 1

-----------------------------------------------------------------------------

Inpatient Medications has received the following STAT order (PENDING)

Patient: ALASKA,FRED (6789)

Order Information: DIGOXIN 100MG PO QD

Order Date: 04/02/04 08:51

Example: Active NOW Order Notification Message

Subj: GEN MED-ACTIVE NOW- ALASKA,FRED \[#88123\] 04/02/04@09:01 5 lines

From: MEDICATIONS,INPATIENT In 'IN' basket. Page 1

-----------------------------------------------------------------------------

Inpatient Medications has received the following NOW order (ACTIVE)

Patient: ALASKA,FRED (6789)

Order Information: DIGOXIN 50MG PO NOW

Order Date: 04/02/04 08:51

### Adding a User as a Subscriber

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a user to the PSJ STAT NOW PENDING ORDER and the PSJ STAT NOW ACTIVE ORDER mail groups, use VA FileMan to edit the MEMBER field (#2) or the MEMBERS – REMOTE field (#12) in the MAIL GROUP file (#3.8).

### ### Adding a Remote Member as a Subscriber

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The STAT and NOW Order Notification mail groups can be set up to send text messages to a remote device. This enables anyone who has subscribed to these mail groups to use a pager, or any device that can receive an email message, to receive notification quickly when these high priority orders are received. The following example illustrates how to define a remote device for a mail group using VA FileMan.

Example: Using VA FileMan to Define a Remote Device (for PSJ STAT NOW ACTIVE ORDER Mail Group)

Select OPTION: EN ENTER OR EDIT FILE ENTRIES (Enter)

INPUT TO WHAT FILE: MAIL GROUP// MAIL GROUP (280 entries)

EDIT WHICH FIELD: ALL// 12 MEMBERS - REMOTE (multiple)

EDIT WHICH MEMBERS - REMOTE SUB-FIELD: ALL// \<Enter\>

THEN EDIT FIELD:

Select MAIL GROUP NAME: PSJ STAT NOW ACTIVE ORDER

Select REMOTE MEMBER: ? \<Enter\>

You may enter a new MEMBERS - REMOTE, if you wish

Enter a remote address (name@domain) or local device (D.device or

H.device) or local server (S.server).

Select REMOTE MEMBER: DDENVER819@SPRINTPCS.COM

Are you adding 'DDENVER819@SPRINTPCS.COM' as

a new REMOTE MEMBER (the 1ST for this MAIL GROUP)? No// Y (Yes)

Select REMOTE MEMBER:

Select MAIL GROUP NAME:

## Files, Fields, and Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed files, fields, and cross-references.

### New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new files were added to the Inpatient Medications package.

### Changed Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55) and the IV multiple (#100) of the PHARMACY PATIENT file (#55) have been changed to store information related to the renewal of an order. The NON-VERIFIED ORDERS file (#53.1) has been changed to store information related to the renewal of an order. A new EXPIRED IV TIME LIMIT field (#34) has been added to the PHARMACY SYSTEM file (#59.7). Two new mail groups have been added to the MAIL GROUP file (#3.8).

### New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PHARMACY PATIENT file (#55)

The LAST RENEW field (#114) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55) has been added to store the date and time that the order was renewed.

The LAST RENEW field (#138) of the IV multiple (#100) of the PHARMACY PATIENT file (#55) has been added to store the date and time that the order was renewed.

The LAST RENEW field (#114) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55) and the LAST RENEW field (#138) in the IV multiple (#100) of the PHARMACY PATIENT file (#55) both contain four new fields:

- RENEWED BY field (#1) – the user renewing the order
- PREVIOUS PROVIDER field (#2) – the Provider of the order prior to renewal
- PREVIOUS STOP DATE/TIME field (#3) – the Stop Date/Time of the order prior to renewal
- PREVIOUS ORDERS FILE ENTRY field (#4) – the ORDER file (#100) entry associated with the order prior to renewal

The new fields capture renewal information associated with the RN (Renew) action each time an order is renewed. Only the most recent renewal date and time will display in the various patient profile views, including the *Inpatient Profile* \[PSJ PR\] option, and in the patient’s detailed order information.

  
NON-VERIFIED ORDERS file (#53.1)

A new LAST RENEW field (#114) was added to the NON-VERIFIED ORDERS file (#53.1). This sub-file contains three new fields:

- RENEWED BY field (#1) – the user renewing the order
- PREVIOUS PROVIDER (#2) – the Provider of the order prior to renewal
- PREVIOUS STOP DATE/TIME (#3) – the Stop Date/Time prior to renewal

The new fields capture renewal information associated with the RN (Renew) action each time an order is renewed. Only the most recent renewal date and time will display in the various patient profile views, including the *Inpatient Profile* \[PSJ PR\] option, and in the patient’s detailed order information.

PHARMACY SYSTEM file (#59.7)

A new EXPIRED IV TIME LIMIT field (#34) has been added to the PHARMACY SYSTEM file (#59.7). This field defines the number of hours after expiration that a continuous IV order can be renewed.

MAIL GROUP file (#3.8)

Two new mail groups are added to the MAIL GROUP file (#3.8): PSJ STAT NOW PENDING ORDER, and PSJ STAT NOW ACTIVE ORDER.

Subscribers to the PSJ STAT NOW PENDING ORDER mail group receive a message when an order with a STAT priority or a schedule of NOW is received from CPRS. The subject of the message is formatted WARD – PENDING STAT or NOW – PATIENT NAME or WARD – PENDING NOW – PATIENT NAME.

Subscribers to the PSJ STAT NOW ACTIVE ORDER mail group receive a message when an order with a STAT priority or a schedule of NOW is verified and made active in Inpatient Medications. The subject of the message is formatted WARD – ACTIVE STAT or NOW – PATIENT NAME or WARD – ACTIVE NOW – PATIENT NAME.

The notification messages contain patient’s name, last four digits of the patient’s Social Security Number, medication name, dosage, schedule, and order date and time.

### Changed Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No fields were changed in the Inpatient Medications package.

### New Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In support of Complex Orders changes, two new cross-references have been created to group Complex child orders by their parent order. For Unit Dose orders, the cross-reference will be indexed and triggered by the ORDERS FILE PARENT ORDER field (#125) and the ORDERS FILE ENTRY field (#66) of the UNIT DOSE multiple (#62) of the PHARMACY PATIENT file (#55). For IV orders, the cross-reference will be indexed and triggered by the ORDERS FILE PARENT ORDER field (#150) and the ORDERS FILE ENTRY field (#110) of the IV multiple (#100) of the PHARMACY PATIENT file (#55). The cross-reference definition will be created by the pre-install routine PSSCMPLX.

Example: VA FileMan Listing of ACX and ACX1 Cross-References

X-ref File/Sub-file Trigger-point field(s)

-----------------------------------------------------------------

ACX PHARMACY PATIENT (#55) ORDERS FILE PARENT ORDER (#125)

/UNIT DOSE (#62) ORDERS FILE ENTRY (#66)

ACX1 PHARMACY PATIENT (#55) ORDERS FILE PARENT ORDER (#150)

/IV (#100) ORDERS FILE ENTRY (#110)

### Changed Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No cross-references were changed in the Inpatient Medications package.

*(This page included for two-sided copying.)*

# Impact on Other V*IST*A Software Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The impact that Phase I (patch PSJ\*5\*110) of this project will have on other V*IST*A software packages is described below.

CPRS

Patch OR\*3\*213 will display the original start date of a Renewed Order in the details information of an Inpatient Medications order. This change will be included in the host file with patch PSJ\*5\*110.

PBM

Patch PSU\*3\*34 will make the PBM extraction of medication dispensing data more efficient to accommodate longer average order durations resulting from the Renewed Order changes. This change will be included in the host file with patch PSJ\*5\*110.

Pharmacy Data Management

There are no functional changes to Pharmacy Data Management for Phase I of this project as a result of patch PSS\*1\*79. The changes are technical in nature and intended to make the software more efficient. The changes consist of new fields added to the PHARMACY PATIENT file (#55) that will store Renewed Order and Complex Order information. Patch PSS\*1\*79 will be included in the host file with patch PSJ\*5\*110.

*(This page included for two-sided copying.)*