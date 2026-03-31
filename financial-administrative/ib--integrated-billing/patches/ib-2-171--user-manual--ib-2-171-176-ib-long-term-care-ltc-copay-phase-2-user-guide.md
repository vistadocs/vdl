---
title: IB*2*171/176 IB Long Term Care (LTC) Copay Phase 2 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: IB Long Term Care (LTC) Copay Phase 2
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: archive
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*171
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - billing
  - charge
  - copay
  - patient
  - date
  - clock
  - days
  - inpt
  - table
  - contents
page_count: 0
word_count: 3265
section_count: 10
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)_Archive/ib_ltc_2_ug2.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)_Archive/ib_ltc_2_ug2.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=266"
---

![](ib-2-171-176-ib-long-term-care-ltc-copay-phase-2-user-guide/001.png)

Integrated Billing V. 2.0User GuideFor Patches IB\*2\*171 and IB\*2\*176Long Term Care Copay Phase II

September 2002

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Patch IB\2\171](#patch-ib2171)
  - [Patch IB\2\176](#patch-ib2176)
  - [The LTC Billing Menu](#the-ltc-billing-menu)
- [New Options](#new-options)
  - [LTC Billing Clock Maintenance](#ltc-billing-clock-maintenance)
    - [Adding a Free Day](#adding-a-free-day)
    - [Editing a Free Day](#editing-a-free-day)
    - [Deleting a Free Day](#deleting-a-free-day)
  - [LTC Billing Clock Inquiry](#ltc-billing-clock-inquiry)
  - [LTC Single Patient Billing Profile](#ltc-single-patient-billing-profile)
- [Modified Options](#modified-options)
  - [Billing Activity List](#billing-activity-list)
  - [Cancel/Edit/Add Patient Charges](#canceleditadd-patient-charges)
    - [Editing a LTC Charge](#editing-a-ltc-charge)
    - [Adding a LTC Charge](#adding-a-ltc-charge)
    - [Canceling a LTC Charge](#canceling-a-ltc-charge)
  - [Outpatient/Registration Events Report](#outpatientregistration-events-report)
The purpose of the Long Term Care Copay Phase II project is to meet the provisions in the Veterans Millennium Health Care and Benefits Act, Public Law 106-117 Medical Care Collections, which authorized the Department of Veterans Affairs to promulgate regulations to collect copayments for extended care services provided to veterans by the VA. Long Term Care Copay Phase I provided functionality to identify patients who financially qualify for LTC Copayment and flag episodes of care and encounters that are LTC-related. Functionality for LTC Copay Phase II includes the following:
- Implement new LTC copayment rates as defined by Public Law 106-117, Section 101.
- Identify episodes/encounters of care related to LTC (via Treating Specialties and DSS Stop Codes) to stop Means Test billing logic and start LTC billing logic.
- Determine if the patient has LTC Copayment Test (10-10EC) information on file; if not, generate a mail message bulletin to alert a designated group of users that the information is needed.
- Determine if the patient is exempt from LTC copayment; if not, obtain the patient’s monthly-calculated LTC copayment obligation from the Enrollment Package.
- Create a new LTC Billing Clock to track the patient’s first 21 days of LTC services in each 12 month period from the date LTC services began since they are not subject to LTC Copayment (21 free days).
- Create a new LTC Billing Clock Maintenance option to edit the patient’s LTC Billing Clock (21 free days).
- Create a new LTC Billing Clock Inquiry option to display data contained in the patient’s LTC Billing Clock (21 free days).
- Create a LTC monthly job that will run in the background to evaluate the patient’s LTC episodes/encounters, apply special LTC billing rules, create charges not to exceed Enrollment’s monthly calculated LTC copayment obligation, and pass the LTC charges to AR.
- Modify the existing Cancel/Add/Edit Patient Charges option to edit LTC charges that fall outside of the LTC Billing Clock (21 free days).
- Modify existing Outpatient/Registration Events Report to include all LTC outpatient activities within a user-specified date range.
- Modify existing Patient Billing Inquiry option to display all LTC data for a specified patient.
- Create a new LTC Single Patient Billing Profile option to display all LTC activity for a specified patient.
- Print LTC Copayment charges the patient’s AR patient billing statement.

## Patch IB\*2\*171

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary purpose of Patch IB\*2\*171 is to stop Means Test (MT) billing for Long Term Care (LTC) services, and to track those patients receiving LTC services so that they can be billed in the future.

Treating Specialties are used to identify LTC services for inpatients, and Clinic Stop Codes are used to identify LTC services for outpatients. Please refer to the charts that follow for a list of these codes.

|                                    |                                     |
|------------------------------------|-------------------------------------|
| Treating Specialty (Inpatient) | Type of Care                    |
| 31                                 | Institutional Inpatient GEM         |
| 32                                 | Institutional Inpatient GEM         |
| 33                                 | Institutional Inpatient GEM         |
| 34                                 | Institutional Inpatient GEM         |
| 35                                 | Institutional Inpatient GEM         |
| 37                                 | Institutional Inpatient Domiciliary |
| 80                                 | Institutional Inpatient NHCU        |
| 81                                 | Institutional Inpatient NHCU        |
| 83                                 | Institutional Inpatient Respite     |
| 85                                 | Institutional Inpatient Domiciliary |
| 86                                 | Institutional Inpatient Domiciliary |
| 87                                 | Institutional Inpatient Domiciliary |
| 88                                 | Institutional Inpatient Domiciliary |
| 96                                 | Institutional Inpatient Hospice     |

|                              |                                   |
|------------------------------|-----------------------------------|
| Clinic Stop (Outpatient) | Type of Care                  |
| 190                          | Non-institutional Outpatient ADHC |
| 319                          | Non-institutional Outpatient GEM  |

## Patch IB\*2\*176

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of patch 176 is to implement the Long Term Care (LTC) Copayment requirement as mandated by the Veterans Millennium Health Care and Benefits Act, Public Law 106-117, Section 101. It is designed to perform LTC copayment calculations. It introduces the capability to start and maintain a LTC Billing Clock for patients, and to display LTC related information.

This patch also introduces a background job that runs on the first day of each month; however, the first time this background job will run is on the first night after the patch is installed. Therefore, expect to see the first LTC related messages and charges the day after installation. The monthly job runs automatically as part of the IB MT NIGHT COMP job, and is invisible to the end user. This monthly job performs calculations to determine LTC copayments for the previous month. The first time the monthly job is run, any prior months that have not been billed since the LTC Billing effective date (JULY 5, 2002) will also be calculated. The monthly job checks patients' LTC status, applies LTC exemptions and special LTC business rules, and uses the patients' Monthly Calculated LTC Copayment Cap (obtained from Enrollment Package) to compute the proper LTC copayment amount (if any) for the patient.

## The LTC Billing Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BILS Billing Activity List

CHRG Cancel/Edit/Add Patient Charges

CLOL LTC Billing Clock Maintenance

INQL LTC Billing Clock Inquiry

PROL LTC Single Patient Billing Profile

This patch adds a new menu, the LTC Billing Menu. This menu is included on the Billing Clerk's Menu and the Billing Supervisor Menu. It includes three new options: LTC Billing Clock Maintenance, LTC Billing Clock Inquiry, and LTC Single Patient Billing Profile; and two modified options: Billing Activity List (formerly the Category C Billing Activity List option) and Cancel/Edit/Add Patient Charges.

# New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## LTC Billing Clock Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to open or edit a LTC Billing Clock for a patient. You can edit the Start Date or Days Not Subject To LTC Copay (Free Days).

If you enter a patient who does not already have a LTC Billing Clock open, you will be asked if you want to add one. If you answer yes, you will be asked for the start date.

Select PATIENT NAME: IBPATIENT, ONE IBPATIENT, ONE 6-1-43 000450000

07-18-00 NSC VETERAN

Enrollment Priority: Category: NOT ENROLLED End Date: 07/18/2000

The patient IBPATIENT, ONE has no LTC clock on file.

Do you want to add one? No// y (Yes)

You need to specify the clock start date

Enter a date: 1/1/02

Once you enter the Start Date for a new patient or the name of a patient who already has a LTC billing clock open, the billing clock information for that patient is displayed.

IBPATIENT, ONE 000-45-0000 06/01/1943 NSC VETERAN

=============================================================================

LTC Copay Clock Start Date: Jan 01, 2002 Clock Status: OPEN

LTC Copay Clock End Date : Dec 31, 2002

Free Days Remaining: 21

Days Not Subject To LTC Copay: none

User Added Entry : REDACTED May 13, 2002 3:24 pm

User Last Updated:

-----------------------------------------------------------------------------

You can edit Start Date OR Days Not Subject To LTC Copay (Free Days)

Select one of the following:

S Start Date

F Free Days

Enter response: S Start Date

Enter a date: Jan 01, 2002// 2/1

If you edit the Start Date, the End Date is automatically re-calculated (for one year).

IBPATIENT, ONE 000-45-0000 06/01/1943 NSC VETERAN

=============================================================================

LTC Copay Clock Start Date: <span class="mark">Feb 01, 2002</span> Clock Status: OPEN

LTC Copay Clock End Date : <span class="mark">Jan 31, 2003</span>

Free Days Remaining: 21

Days Not Subject To LTC Copay: none

User Added Entry : REDACTED May 13, 2002 3:24 pm

User Last Updated: REDACTED May 17, 2002 3:33 pm

When you choose to edit the Free Days, you can add, edit, or delete the days not subject to LTC copay. Dates prior to the start of the patient’s billing clock or after the current date may not be entered. Up to 21 Free Days may be entered.

### Adding a Free Day

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter response: Free Days

Days Not Subject To LTC Copay: none

Select one of the following:

A Add

E Edit

D Delete

Enter response: a Add

Enter a date: 2/4 ... Feb 04, 2002 was added.

Enter a date: 2/7 ... Feb 07, 2002 was added.

Enter a date:

Days Not Subject To LTC Copay:

1 Feb 04, 2002 2 Feb 07, 2002

### Editing a Free Day

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Days Not Subject To LTC Copay:

1 Feb 04, 2002 2 Feb 07, 2002

Select one of the following:

A Add

E Edit

D Delete

Enter response: e Edit

Enter a number (1-2): 1

Enter a date: 2/5

Days Not Subject To LTC Copay:

1 Feb 05, 2002 2 Feb 07, 2002

### Deleting a Free Day

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Days Not Subject To LTC Copay:

1 Feb 05, 2002 2 Feb 07, 2002

Select one of the following:

A Add

E Edit

D Delete

Enter response: d Delete

Enter a number (1-2): 2

Are you sure you want to delete this date? No// y (Yes)

Days Not Subject To LTC Copay:

1 Feb 05, 2002

As Free Days are added and deleted, the “Free Days Remaining” and “Days Not Subject To LTC Copay” fields are re-calculated. In the following example, four free days have been entered, which leaves 17 days remaining.

IBPATIENT, ONE 000-45-0000 06/01/1943 NSC VETERAN

=============================================================================

LTC Copay Clock Start Date: Feb 01, 2002 Clock Status: OPEN

LTC Copay Clock End Date : Jan 31, 2003

<span class="mark">Free Days Remaining: 17</span>

<span class="mark">Days Not Subject To LTC Copay:</span>

<span class="mark">1 Feb 05, 2002 3 Mar 07, 2002</span>

<span class="mark">2 Mar 01, 2002 4 Mar 08, 2002</span>

## LTC Billing Clock Inquiry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LTC Billing Clock Inquiry option allows users to view the details of the LTC Billing clock for a specific patient. No changes can be made through this option.

Select LTC Billing Menu Option: INQL LTC Billing Clock Inquiry

Select PATIENT NAME: IBPATIENT, TWO 5-1-25 000450000 NSC VETERAN 12D(NHCU)

Enrollment Priority: Category: IN PROCESS End Date:

Enter \<RETURN\> to continue. \<RET\>

Choose LTC BILLING CLOCK (1-2): Feb 02, 2002// ??

IBPATIENT, TWO has the following LTC Copay Clocks

1 Oct 01, 2001 - Sep 30, 2002 CANCELLED

2 Feb 02, 2002 - Feb 01, 2003 OPEN

Choose LTC BILLING CLOCK (1-2): Feb 02, 2002// \<RET\> (Feb 02, 2002)

DEVICE: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

IBPATIENT, TWO 000-45-0000 05/01/1925 NSC VETERAN

=============================================================================

LTC Copay Clock Start Date: Feb 02, 2002 Clock Status: OPEN

LTC Copay Clock End Date : Feb 01, 2003

Free Days Remaining: 0

Days Not Subject To LTC Copay:

1 Mar 26, 2002 8 Apr 02, 2002 15 Apr 09, 2002

2 Mar 27, 2002 9 Apr 03, 2002 16 Apr 10, 2002

3 Mar 28, 2002 10 Apr 04, 2002 17 Apr 11, 2002

4 Mar 29, 2002 11 Apr 05, 2002 18 Apr 12, 2002

5 Mar 30, 2002 12 Apr 06, 2002 19 Apr 13, 2002

6 Mar 31, 2002 13 Apr 07, 2002 20 Apr 14, 2002

7 Apr 01, 2002 14 Apr 08, 2002 21 Feb 02, 2002

User Added Entry : REDACTED Mar 26, 2002 4:54 pm

User Last Updated: REDACTED May 15, 2002 11:33 am

Enter RETURN to continue or '^' to exit:

## LTC Single Patient Billing Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a LTC billing profile for a specific patient. You can include the days not subject to LTC copay and/or LTC events. The default for the start with date is the start date for the LTC Billing Clock, and the default for the go to date is the current date.

Select PATIENT NAME: IBPATIENT, ONE IBPATIENT, ONE 12-6-59 000450000

-- NSC VETERAN 11E REHAB

Financial query queued to be sent to HEC...

Enter \<RETURN\> to continue.

IBPATIENT, ONE has the following LTC Copay Clock

1 Jan 05, 2002 - Jan 04, 2003 OPEN

Start with DATE: Jan 05, 2002// (Jan 05, 2002)

Go to DATE: Aug 20, 2002// (Aug 20, 2002)

Include DAYS NOT SUBJECT TO LTC COPAY on this report? YES//

Include LTC EVENTS on this report? YES//

DEVICE: HOME// UCX/TELNET Right Margin: 80//

LTC Billing Profile for IBPATIENT, ONE 000-45-0000

From 01/05/02 through 08/20/02 Aug 20, 2002@14:08 Page: 1

=============================================================================

LTC Copay Clock Start Date: 01/05/02 Clock Status: OPEN

LTC Copay Clock End Date: 01/04/03

Days Not Subject To LTC Copay:

1 Apr 01, 2002 8 Apr 08, 2002 15 Apr 15, 2002

2 Apr 02, 2002 9 Apr 09, 2002 16 Apr 16, 2002

3 Apr 03, 2002 10 Apr 10, 2002 17 Apr 17, 2002

4 Apr 04, 2002 11 Apr 11, 2002 18 Apr 18, 2002

5 Apr 05, 2002 12 Apr 12, 2002 19 Jan 05, 2002

6 Apr 06, 2002 13 Apr 13, 2002 20 Jan 06, 2002

7 Apr 07, 2002 14 Apr 14, 2002 21 Jan 07, 2002

BILL DATE BILL TO BILL TYPE BILL \# TOT CHARGE

-----------------------------------------------------------------------------

LTC CHARGES FOR JANUARY 2002

01/23/02 01/31/02 LTC INPATIENT GEM K90037Z \$500.00

---------

Monthly LTC Copay Cap: \$0.00 (181+ days) \$500.00

Monthly LTC Events:

Enter RETURN to continue or '^' to exit:

# Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following IB options have been modified to include LTC events. For more complete documentation on how these options work, please refer to [the Integrated Billing V. 2.0 User Manual](http://www.va.gov/vdl/Financial_Admin.asp?appID=45) in the VistA Documentation Library (VDL).

## Billing Activity List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The name of this option has been changed from "Means Test Billing Activity List" to “Billing Activity List”. All references to Means Test and Category C have been removed. The report has been modified to include both MT and LTC events.

Select OPTION NAME: Billing Activity List

Billing Activity List

Select one of the following:

0 NO

1 YES

Run this report for Purple Heart Vets only?: NO// \<RET\>

Start with DATE: T-60 (MAR 21, 2002)

Go to DATE: t (MAY 20, 2002)

DEVICE: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

Billing Activity List MAY 20, 2002@17:31 Page: 1

Charges from 03/21/02 through 05/20/02

PATIENT/ID DESCRIPTION STATUS FROM TO UNITS CHARGE

-----------------------------------------------------------------------------

IBPT,ONE 0000 INPT PER DIEM BILLED 08/29/01 04/18/02 233 \$2,330.00

INPT PER DIEM BILLED 08/29/01 04/18/02 233 \$2,330.00

INPT PER DIEM BILLED 03/07/02 04/10/02 35 \$350.00

INPT PER DIEM BILLED 04/11/02 04/18/02 8 \$80.00

INPT PER DIEM INCOMPLETE 04/19/02 05/13/02 25 \$250.00

IBPT,TWO 0000 INPT PER DIEM ON HOLD (IN 02/26/02 03/24/02 27 \$270.00

INPT PER DIEM ON HOLD (IN 02/27/02 03/24/02 26 \$260.00

IBPT,THRE 0000 OPT COPAY CANCELLED 04/19/02 04/19/02 1 \$15.00

INPT PER DIEM ON HOLD (IN 04/19/02 04/19/02 1 \$10.00

IBPT,FOUR 0000 LTC OPT ADHC ON HOLD (IN 04/26/02 04/26/02 1 \$15.00

OPT COPAY ON HOLD (IN 04/29/02 04/29/02 1 \$15.00

LTC OPT ADHC ON HOLD (IN 04/29/02 04/29/02 1 \$15.00

OPT COPAY CANCELLED 04/30/02 04/30/02 1 \$50.00

\* Purple Heart Recipient

Enter RETURN to continue or '^' to exit:

## Cancel/Edit/Add Patient Charges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Cancel/Edit/Add Patient Charges option has been modified to allow users to Cancel or Add LTC charges that fall outside of a patient’s 21 free days in their LTC Billing Clock.

Select OPTION NAME: CANCEL/EDIT/ADD Patient ChargE IB CANCEL/EDIT/ADD CHARGES

Cancel/Edit/Add Patient Charges

Select PATIENT NAME: IBPATIENT, ONE IBPATIENT, ONE 5-1-25 000450000

NSC VETERAN 12D(NHCU)

Enrollment Priority: Category: IN PROCESS End Date:

Enter \<RETURN\> to continue. \<RET\>

Search for CHARGES from: MAY 20, 2001// FEB 14, 2002 (FEB 14, 2002)

to: MAY 20, 2002// \<RET\> (MAY 20, 2002)

Include RX COPAY charges? NO// \<RET\>

Charges May 20, 2002@16:50:56 Page: 1 of 1

Cancel/Edit/Add Charges 02/14/02 THRU 05/20/02

Patient: IBPATIENT, ONE A0000

Bill From Bill To Charge Type Stop Bill \# Status Charge

1 02/14/02 02/21/02 LTC INPT RESPITE NEW K90033W BILLED \$218

2 02/24/02 02/27/02 OBSERVATION COPAY NEW ON HOLD \$50

3 02/25/02 02/25/02 OPT COPAY NEW 301 CANCELLED \$15

4 02/25/02 02/25/02 OPT COPAY NEW 301 CANCELLED \$15

5 02/26/02 03/24/02 INPT PER DIEM NEW ON HOLD \$270

6 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

7 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

8 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

9 02/27/02 03/24/02 INPT PER DIEM NEW ON HOLD \$260

Enter ?? for more actions

AC Add a Charge CP Change Patient UE Update Events

EC Edit a Charge CD Change Date Range

CC Cancel a Charge PC Pass a Charge

Select Action: Quit// EC Edit a Charge

Select Charge(s): (1-9): 1

### Editing a LTC Charge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LTC Charges may not be edited in this option. You must cancel the existing charge and add a new one.

E D I T A C H A R G E

Processing Charge \#1

-------------------------------------------------------------------------------

Name: IBPATIENT, ONE Type: LTC INPT RESPITE NEW

ID: 000-45-0000 Amt: \$218 (BILLED)

-------------------------------------------------------------------------------

Sorry! You cannot edit LTC copayment charges.

Please cancel this charge and add a new charge.

Press RETURN to process the next charge or to return to the list: \<RET\>

Charges May 20, 2002@16:51:16 Page: 1 of 1

Cancel/Edit/Add Charges 02/14/02 THRU 05/20/02

Patient: IBPATIENT, ONE A0000

Bill From Bill To Charge Type Stop Bill \# Status Charge

1 02/14/02 02/21/02 LTC INPT RESPITE NEW K90033W BILLED \$218

2 02/24/02 02/27/02 OBSERVATION COPAY NEW ON HOLD \$50

3 02/25/02 02/25/02 OPT COPAY NEW 301 CANCELLED \$15

4 02/25/02 02/25/02 OPT COPAY NEW 301 CANCELLED \$15

5 02/26/02 03/24/02 INPT PER DIEM NEW ON HOLD \$270

6 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

7 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

8 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

9 02/27/02 03/24/02 INPT PER DIEM NEW ON HOLD \$260

Enter ?? for more actions

AC Add a Charge CP Change Patient UE Update Events

EC Edit a Charge CD Change Date Range

CC Cancel a Charge PC Pass a Charge

Select Action: Quit// AC Add a Charge

### Adding a LTC Charge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A D D A C H A R G E

-------------------------------------------------------------------------------

Name: IBPATIENT, ONE \*\* ACTIVE BILLING CLOCK \*\*

ID: 000-45-0000 Clock Begin Date: 12/02/01

-------------------------------------------------------------------------------

Select CHARGE TYPE: LTC

1 LTC INPATIENT DOMICILARY DG LTC INPT DOM NEW

2 LTC INPATIENT GEM DG LTC INPT GEM NEW

3 LTC INPATIENT NURSING HOME DG LTC INPT NHCU NEW

4 LTC INPATIENT RESPITE DG LTC INPT RESPITE NEW

5 LTC OUTPATIENT ADHC DG LTC OPT ADHC NEW

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 3 DG LTC INPT NHCU NEW

\*\*Last LTC Billing Clock Start Date: Feb 02, 2002 Free Days Remaining: 0

Charge for services from: FEB 22, 2002 (FEB 22, 2002)

Charge for services to: FEB 28, 2002 (FEB 28, 2002)

Calculated Monthly Copay Cap Type to be used: INPATIENT \< 181 days.

Calculated Monthly Copay Cap is: \$ 30,000.00

Total previously billed: \$ 800.00

Charge to be billed --\> \$679.00 (for 7 days)

Linked charge to admission on 02/02/02 (Discharged on 02/22/02) ...

Okay to add this charge? YES done.

Passing the charge directly to Accounts Receivable... done

Press RETURN to process the next charge or to return to the list: \<RET\>

Charges May 20, 2002@17:09:26 Page: 1 of 1

Cancel/Edit/Add Charges 02/14/02 THRU 05/20/02

Patient: IBPATIENT, ONE A0000

Bill From Bill To Charge Type Stop Bill \# Status Charge

1 02/14/02 02/21/02 LTC INPT RESPITE NEW K90033W BILLED \$218

2 02/22/02 02/28/02 LTC INPT NHCU NEW ON HOLD \$679

3 02/24/02 02/27/02 OBSERVATION COPAY NEW ON HOLD \$50

4 02/25/02 02/25/02 OPT COPAY NEW 301 CANCELLED \$15

5 02/25/02 02/25/02 OPT COPAY NEW 301 CANCELLED \$15

6 02/26/02 03/24/02 INPT PER DIEM NEW ON HOLD \$270

7 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

8 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

9 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

10 02/27/02 03/24/02 INPT PER DIEM NEW ON HOLD \$260

Enter ?? for more actions

AC Add a Charge CP Change Patient UE Update Events

EC Edit a Charge CD Change Date Range

CC Cancel a Charge PC Pass a Charge

Select Action: Quit// CC Cancel a Charge

Select Charge(s): (1-10): 2

### Canceling a LTC Charge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

C A N C E L A C H A R G E

Processing Charge \#2

-------------------------------------------------------------------------------

Name: IBPATIENT, ONE Type: LTC INPT NHCU NEW

ID: 000-45-0000 Amt: \$679 (INCOMPLETE)

-------------------------------------------------------------------------------

Select CANCELLATION REASON: ENTERED IN ERROR

Okay to cancel this charge? YES

Updating the status of the charge to 'cancelled'... done.

Press RETURN to process the next charge or to return to the list: \<RET\>

Rebuilding list of charges...

Charges May 20, 2002@17:10:21 Page: 1 of 1

Cancel/Edit/Add Charges 02/14/02 THRU 05/20/02

Patient: IBPATIENT, ONE A0000

Bill From Bill To Charge Type Stop Bill \# Status Charge

1 02/14/02 02/21/02 LTC INPT RESPITE NEW K90033W BILLED \$218

2 02/22/02 02/28/02 LTC INPT NHCU NEW CANCELLED \$679

3 02/24/02 02/27/02 OBSERVATION COPAY NEW ON HOLD \$50

4 02/25/02 02/25/02 OPT COPAY NEW 301 CANCELLED \$15

5 02/25/02 02/25/02 OPT COPAY NEW 301 CANCELLED \$15

6 02/26/02 03/24/02 INPT PER DIEM NEW ON HOLD \$270

7 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

8 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

9 02/27/02 03/06/02 INPT PER DIEM NEW ON HOLD \$80

10 02/27/02 03/24/02 INPT PER DIEM NEW ON HOLD \$260

Enter ?? for more actions

AC Add a Charge CP Change Patient UE Update Events

EC Edit a Charge CD Change Date Range

CC Cancel a Charge PC Pass a Charge

Select Action: Quit//

## Outpatient/Registration Events Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient/Registration Events Report has been modified to include all LTC outpatient activities within a user-specified date range.

Select OPTION NAME: Outpatient/Registration Events Report

Outpatient/Registration Events Report

Start with DATE: APR 29 (APR 29, 2002)

Go to DATE: APR 30 (APR 30, 2002)

DEVICE: HOME// \<RET\> UCX/TELNET Right Margin: 80// \<RET\>

Means Test/LTC Outpatient and Registration Activity for 04/29/02

Printed: 05/20/02 Page: 1

Patient/Event Time Clinic/Stop Appt.Type (Status)

IBPATIENT, ONE 0000 \*\*Insured\*\*

CLINIC APPT 10:00 TEST CLINIC REGULAR CHECKED OUT

Stop Code: ADULT DAY HEALTH \#190 Primary Care

\* \$15.00 OUTPATIENT COPAY ON HOLD (INS)

\* \$15.00 LTC OUTPATIENT ADHC ON HOLD (INS)

Enter RETURN to continue or '^' to exit: \<RET\>

Means Test/LTC Outpatient and Registration Activity for 04/30/02

Printed: 05/20/02 Page: 2

Patient/Event Time Clinic/Stop Appt.Type (Status)

IBPATIENT, ONE 0000 \*\*Insured\*\*

CLINIC APPT 08:00 TEST TWO CLINIC REGULAR CHECKED OUT

10:00 TEST CLINIC REGULAR CHECKED OUT

Stop Code: ALZH/DEMEN/CLIN \#320 Specialty Care

\* \$50.00 OUTPATIENT COPAY CANCELLED

\* \$15.00 LTC OUTPATIENT ADHC ON HOLD (INS)

Enter RETURN to continue or '^' to exit: