---
title: DVB*4*49 Training Guide
doc_type: TRG
doc_label: Training Guide
doc_layer: patch
doc_subject: 
app_code: HINQ
app_name: Hospital Inquiry
section: FIN
app_status: active
pkg_ns: DVB
patch_ver: 4
patch_id: DVB*4*49
group_key: "HINQ:DVB:4"
file_numbers: []
security_keys: []
menu_options: 1
description: "> HINQ Replacement Interim Solution introduces the following functionality for VHA and VBA Data Sharing Strategy –Interim Solution:"
audience: 
keywords: 
  - hinq
  - table
  - contents
  - training
  - guide
  - strong
  - blockquote
  - request
  - objective
  - replacement
page_count: 0
word_count: 2208
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Hosp_Inquiry_(HINQ)/dvb_4_p49_tg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Hosp_Inquiry_(HINQ)/dvb_4_p49_tg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=41"
---

## HINQ REPLACEMENT INTERIM SOLUTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 4.1

![](dvb-4-49-training-guide/001.png)

### Welcome to HINQ Replacement Interim Solution Training Session

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This information is based upon the following Patches:

>  IVMB\*2\*792, IVMB\*2\*835, DVB\*4\*49, DG\*5.3\*631 and DGBT \*1\*11

> The HINQ Replacement Interim Solution Enhancements provides data to the following Information Centers:

#### Health Eligibility Center’s Information System

- VistA

### Introduction:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Why change HINQ
- New VBA Corporate database
- Eventual retirement of C&P and BIRLS
- Timelines for implementation

> The HEC Legacy/ V*ist*A Enhancements supports several critical business processes associated with congressionally mandated initiatives.

> VHA and VBA representatives in 2002 decided to replace the existing HINQ, which accesses older VBA (BIRLS and C&P) databases, with a new HINQ that also accesses the new VBA Corporate Database.

> The HINQ Replacement Interim Solution software package provides the current HEC Legacy/V*ist*A systems, with the ability to continue to operate seamlessly while VBA transfers its C&P processing to the new VBA corporate database.

> VBA is in the initial stages of deploying its modernized claims applications known as VETSNET. As part of this application deployment, VBA is processing new C&P awards in its corporate database, and will be moving records in from its legacy mainframe environment, the C&P Benefits Delivery Network (BDN), to this database in 2006.

> VHA uses the Hospital Inquiry (HINQ) system to query VBA’s C&P BDN to secure information about C&P entitlement and eligibility. Replacement HINQ will give VHA access to data in VBA’s corporate database environment.

> HINQ Interim Solution with Simultaneous HEC update

> ![](dvb-4-49-training-guide/002.png)

Suspense File

> TCP/IP

> VBA BDN

> C&P

> e\*Gate HINQ Server

> Corporate Database

> VBA’s New HINQ

> program

> VBA BDN BIRLS

> Benefits Delivery Network

> During VBA’s transition, all databases will be searched; upon completion of conversion, all legacy database searches will be dropped.

> DVB_4_P49_TG

> Legend

> Blue = VHA Black = AAC

> Green = VBA 6

### Training Objectives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Objective \#1

- Changes to the HINQ Response and HINQUP Features

#### Objective \#2

- Miscellaneous Changes in HINQ Response
- Objective \#3
  - Processing Changes
    - New Business Process
    - ![](dvb-4-49-training-guide/003.png)![](dvb-4-49-training-guide/004.png)![](dvb-4-49-training-guide/005.png)Responses to VistA’s HINQ simultaneously sent to HEC

#### Objective \#4

- Common Security Services (CSS)

#### Objective \#5

- How to request a HINQ

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HINQ Replacement Interim Solution introduces the following functionality for VHA and VBA Data Sharing Strategy –Interim Solution:

- A new single IP address is added to capture all HINQ requests that are directed to the AAC. The HINQ messages are translated and transmitted between V*ist*A and the VBA environments through the AAC interface.
- VBA has added up to 150 Service Connected (SC) Disabilities conditions to the HINQ response that is captured through the VBA Data set.
- Modifications made to the Z11 (MVR through HEC) upload process.
- Data Dictionary changes were made by adding new fields to the Veterans ID and Verification Access.
- Changes were made to the Template to include subfields from the Veterans ID and Verifications Access.

![](dvb-4-49-training-guide/006.png)

# Objective \# 1


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [HINQ REPLACEMENT INTERIM SOLUTION](#hinq-replacement-interim-solution)
    - [Welcome to HINQ Replacement Interim Solution Training Session](#welcome-to-hinq-replacement-interim-solution-training-session)
    - [Introduction:](#introduction)
    - [Training Objectives](#training-objectives)
    - [Overview](#overview)
- [Objective \# 1](#objective-1)
  - [Changes to the HINQ Response & HINQUP Features](#changes-to-the-hinq-response-hinqup-features)
    - [What’s New ?](#whats-new)
    - [As-Is HINQ](#as-is-hinq)
    - [What’s New?](#whats-new-1)
- [HINQUP Features](#hinqup-features)
  - [HINQ Replacement Interim Solution](#hinq-replacement-interim-solution-1)
- [Error Conditions](#error-conditions)
  - [HINQ Replacement Interim Solution](#hinq-replacement-interim-solution-2)
    - [Disability Condition as a HINQ message](#disability-condition-as-a-hinq-message)
- [Objective \# 2](#objective-2)
    - [Miscellaneous Changes in HINQ Responses](#miscellaneous-changes-in-hinq-responses)
- [Objective \# 3](#objective-3)
- [Objective \# 4](#objective-4)
    - [New Security Requirements](#new-security-requirements)
- [Objective \# 5](#objective-5)
    - [How to request a HINQ](#how-to-request-a-hinq)
    - [How to generate an HINQ Request:](#how-to-generate-an-hinq-request)
    - [Using the Individual HINQ Request option:](#using-the-individual-hinq-request-option)
    - [Generate HINQ Requests](#generate-hinq-requests)
    - [Example A –](#example-a)
    - [Individual HINQ Request](#individual-hinq-request)
    - [Patient Method](#patient-method)
    - [Example B](#example-b)
    - [Direct Method](#direct-method)
    - [Example C](#example-c)
    - [HINQ Replacement Interim Solution](#hinq-replacement-interim-solution-3)

## Changes to the HINQ Response & HINQUP Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dvb-4-49-training-guide/007.png)![](dvb-4-49-training-guide/008.png)

### What’s New ?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Veterans Name :

> Social Security: 0004567890 Claim Number :

> Service Number : OK ? Yes// (Yes)

> Enter HINQ PASSWORD:

#### As-Is HINQ

> Web HINQ

> Veteran’s name is no

> longer used to request HINQs

> Enter one of the following numbers - Social Security Number, Claim Number or Service Number.

> Social Security:

> Claim Number: 0004567890 OK ? Yes// (Yes)

> Enter HINQ PASSWORD:

![](dvb-4-49-training-guide/009.png)![](dvb-4-49-training-guide/010.png)

#### AS-IS HINQ

> VBA name = TAPATIENT Vietnam Service Name = TESTA, PATIENT Verified Svc-Data

> Address = 10 MAIN STREET Original Award = MAR 01, 2003 Address = ATLANTA GA Networth = Zero Networth

> ZIP = 00000 Combat Disability = NONE

> Sex = MALE SSI Income = Receipt Benefits Date of Birth = JAN 1, 1934

> C&P SSN = 000456789 Verified SSA

#### WEB HINQ

> VBA name = TAPATIENT Vietnam Service

> Prior names = Verified Svc-Data TEST A PATIENT

> TEST ABC PATIENT Name = TEST A PATIENT

> Address = 10 MAIN STREET Address = ATLANTA GA

> ZIP = 00000 Sex = MALE

> Date of Birth = JAN 1, 1934

> VBA SSN = 000456789 Unverified

![](dvb-4-49-training-guide/011.png)![](dvb-4-49-training-guide/012.png)

#### AS-IS HINQ

> POW = Not applicable

> Total Active Svc = 20 yr 27 days

> INDICATORS (Active Duty Training NO Disability NO Homeless Veteran NO) Service data C&P BIRLS

> Branch of Service = Army ARMY ARMY ARMY EOD = JUL 19,1970 OCT 27,1952 FEB 23,1961 JUL 19,1970

> RAD = JUN 30,1973 DEC 12,1960 FEB 21,1967 JUN 30,1973

> Char of Service = HONORABLE HON HON HON Additional service = Not an issue

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 29%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Svc Branch: Army</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Army</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Army</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>EOD: JUL 19,1970</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FEB 23,1961</strong></p>
</blockquote></td>
<td><strong>OCT 27,1952</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>RAD: JUN 30,1973</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FEB 21,1967</strong></p>
</blockquote></td>
<td><strong>DEC 12,1960</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Char of Svc: Honorable</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Honorable</strong></p>
</blockquote></td>
<td><strong>Honorable</strong></td>
</tr>
</tbody>
</table>

> AS-IS HINQ

> Entitlement = Vietnam Era(Compensation) - 71 Master Record Type = Veterans Master Record - A

> Diary data: FEB, 2012 RO-issue Dependency Verification form. - 24 DISABILITIES( Combined % = 90 SC/Total = 9/6 Additional = 7 )

> 9411 - POST-TRAUMATIC STRESS DISORDER - 30% - Service Connected

> 5010 - TRAUMATIC ARTHRITIS - 30% - Service Connected 7122 - COLD INJURY RESIDUALS - 30% - Service Connected 7122 - COLD INJURY RESIDUALS - 30% - Service Connected 8520 - PARALYSIS OF SCIATIC NERVE - 20% - Service Connected

> 8520 - PARALYSIS OF SCIATIC NERVE - 20% - Service Connected

> Type Benefit: Compensation

> WEB HINQ

> “Entitlement” Field is now “Type Benefit”

> DISABILITIES( Combined % = 90 Number of Disabilities in Record = 9) Effective Date of Combined Evaluation = Jun 5, 2005

> NEW!

Disability EXTR Orig Eff CurrentDate Eff Date

> 9411 - POST-TRAUMATIC STRESS DISORDER - 30 %

> 5201 - LIMITED MOTION OF ARM - 30 % LU

> 7122 - COLD INJURY RESIDUALS - 30 % RL

> 7122 - COLD INJURY RESIDUALS - 30 %

> 8520 - PARALYSIS OF SCIATIC NERVE - 20 %

> 8520 - PARALYSIS OF SCIATIC NERVE - 20 %

> 6260 - TINNITUS - 10 %

> 6100 - IMPAIRED HEARING - 0 %

> 7805 - SCARS - 0 %

> Displays unlimited \# of SC conditions; more descriptive codes, extremity and award Dates; NSC conditions are not Retrieved; New fields are not available for HINQ up

### As-Is HINQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Perm.,total Disability = Cannot be determined AID & ATTEND = PAY A&A

> Chief Attorney, fiduciary = Employable indicator = Unemployable

> Competency indicator = Competent, or not an issue Competency Pay Status = Competent, or not an issue, Pay direct

> Web HINQ

#### Perm.,total Disability = Cannot be determined AID & ATTEND = A&A Paid

> Employable indicator = Unemployable

#### Competency indicator = Competent, or not an issue

![](dvb-4-49-training-guide/013.png)![](dvb-4-49-training-guide/014.png)

> As-Is HINQ

> INDICATORS( NO Severence Recoupment NO PFOP/FDIB NO Consolidated Payment)

> Anatomical loss = No Amputation - 00

> Other loss = Loss or loss of use of creative organ. - 1 Vet married Vet = No spouse or not eligible -

> Spec. Month comp. = One disability under (k) - 01 Special Provision = Analogous Ratings - 5 Spouse name = Spouse1 DOB = JUL 30, 1942

> CHAMPVA = Eligible Number of CHILDREN

> ------------------------------------------------------------------------------------------------

> School = Helpless School = Depend. total = V-S This Award = V-S Check Amount= '\$2513.00' Hardship Exp.= '\$0' Net Award= '\$2513.00

#### Web HINQ

> Anatomical loss = No Amputation - 00 Loss of use = No Amputation - 00

> Other loss = Loss or loss of use of creative organ. - 1 Vet married Vet = No spouse or not eligible

> Spouse name = Spouse1 DOB = JUL 10, 1943 Check Amount= '\$2513.00' Net Award= '\$2513.00'

![](dvb-4-49-training-guide/015.png)![](dvb-4-49-training-guide/016.png)

### What’s New?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Redirecting HINQ Transaction

#### Formerly all requests were processed through one of five regional concentrators

> Redirecting HINQ

> One Single IP Address

> However, with the new single IP address, all HINQ Requests are addressed to one interface connection at the AAC.

![](dvb-4-49-training-guide/017.png)

# HINQUP Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HINQ Replacement Interim Solution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dvb-4-49-training-guide/018.png)![](dvb-4-49-training-guide/019.png)![](dvb-4-49-training-guide/020.png)

> Screen 0

> This screen is a verification screen only. Allows the user the ability to review the following fields:

- HINQ Responses
- Patient File data

> -----------------------------------------------------------------------------

> Name: TESTA,PATIENT TESTA,PATIENT Sex: MALE MALE

> SSN: 000456789 000456789 Verified VBA

> Claim \#: 0005499

> Address: 123 Anywhere Street

> Pat. Type: SC VETERAN Elig. Stat.:

> Vet. Y/N: YES Stat. Date:Ser. Con.: YES Verif. Meth.:Ser. Con. %: 50 Disab. Ind.:

> Elig. code: SERVICE CONNECTED 50% to 100%

> Is this the patient to be updated (YES, NO, IGNORE)? YES// \<RET\> (YES)

> *Viewing Purpose only*

> What’s New?

> HINQUP Screen Option Change

> Screen 1

> Allows the user the ability to upload a veteran’s address information:

> \*Street Address \*City

> \*State \*Zip Code

> \*County

> TESTA,PATIENT Patient File ((1)) HINQ Response SSN: 6789

> ------------------------------------------------------------------------------

> \[1\] Address: 123 Anywhere Street TESTA,PATIENT

> 123 Anywhere ST Mytown MS

> Veteran’s address data

> ![](dvb-4-49-training-guide/021.png)![](dvb-4-49-training-guide/022.png)![](dvb-4-49-training-guide/023.png)City: Mytown State: Mystate Zip: 99999

> County: Mycounty

> \<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL

> to update: \<RET\>

> DVB_4_P49_TG 20

> What’s New?

> HINQUP Screen Option Change

> Screen 2

> Contains the following data items:

> \*Claim Number \*Date of Birth

> \*Gender \*Date of Death

> \*Incompetency Rating \*POW Status

> \*Claim Folder Location \*Unemployable Status

> \[1\] Claim Num. : 0005499

> \[2\] Date of Birth: 08/01/1906 AUG 31,1906

3.  Sex: MALE MALE
4.  Date of Death:
5.  Rated Incomp.: Competent, or not an issue
6.  POW: Not applicable
7.  Folder Loc. : 306
8.  Unemployable: Employable

> \<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update: A

> TESTA,PATIENT Patient File ((2)) HINQ Response SSN: 6789

> Veteran’s Key Information

![](dvb-4-49-training-guide/024.png)![](dvb-4-49-training-guide/025.png)![](dvb-4-49-training-guide/026.png)

> DVB_4_P49_TG 21

#### What’s New?

> HINQUP Screen Option Change

> Screen 3

> Allows the user access to the following fields:

- Rated Disabilities
- Combined Disability percent
- Active Duty Training
- Total Active Service
- P&T

![](dvb-4-49-training-guide/027.png)![](dvb-4-49-training-guide/028.png)![](dvb-4-49-training-guide/029.png)

> TESTPATIENT, ONE SLYGOOPLEPatient File((3)) HINQ Response SSN: 000002004

> -------------------------------------------------------------------------------

> Act. Duty Training: Tot. Act. Ser.: Perm. & Tot.:

1.  Ver. SVC data: YES
2.  Vietnam Ser.:
3.  Rated Disab.(Pat. File)-Comb. SC%: 40 Eff. Date Comb. Eval.: OCT 01, 1970

> Original Current

> Disability % Extr.Eff. Date Eff. Date UPPER ARM CONDITION 40 LU

> Rated Disab. (HINQ)- Comb. SC%: 40 Eff. Date Comb. Eval.: OCT 01,1970

> Original Current

> Disability % Extr.Eff. Date Eff. Date UPPER ARM CONDITION 40 LU

> \<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update:

> Field Service Information

![](dvb-4-49-training-guide/030.png)![](dvb-4-49-training-guide/031.png)

> Screen 4

> This screen contains data elements that are related to military service:

> \*Entry Date \*Branch of Service \*Incompetency Rating

> \*POW Status \*Serial Number \*Discharge Date

> \*Character of Discharge

> TESTA,PATIENT Patient File ((4)) HINQ Response SSN: 6789

> ------------------------------------------------------------------------------

> HINQ Data

> EOD RAD Bran. Ser. Char. Ser. Ser. Num.

> ------------------------------------------------------------------------------

> SEP 18,1943 NOV 21,1945 NAVY Honorable 8007926

> Patient File

> ------------------------------------------------------------------------------

1.  Last episode
2.  NTL episode
3.  NNTL episode
4.  Per. of Ser.: WORLD WAR II

> \<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update: 1

> Service Information

3

![](dvb-4-49-training-guide/032.png)![](dvb-4-49-training-guide/033.png)![](dvb-4-49-training-guide/034.png)

> TESTA,PATIENT Patient File ((5)) HINQ Response SSN: 6789

> ------------------------------------------------------------------------------

> Check Amt.: \$600.00 Combined %: Net Award Amt:

> Benefit Type: Income for VA Purposes: Aid & Attendance:

> --- Patient Data ---

1)  Elig. Stat.: VERIFIED Elig. Stat. ent. by: USER, TEST Stat. date: OCT 27,1989 Monetary Ben. Verif:

> Verif. Meth.: BIRLS Patient Elig.:

2)  Pat. Type: SC VETERAN Vet. (Y/N)?: YES Ser. Con.: YES
3)  A&A: Amt.: \$ VA Pension: Amt.: \$ House Bound: Amt.: \$ VA Disability: Amt.: \$

> IVAP

> Screen 6 was removed and all data is illustrated on Screen 5

24

![](dvb-4-49-training-guide/035.png)

# Error Conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HINQ Replacement Interim Solution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dvb-4-49-training-guide/036.png)![](dvb-4-49-training-guide/037.png)

### Disability Condition as a HINQ message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Guidelines to follow

- Occasionally it is possible that a Service-Connected Condition code from a HINQ response will not be found in the local database.
- This will occur only when the local site is not up to date with their HINQ patches.
- In the event this occurs the user will see a message, to contact the PAS.
- The PAS will need to contact his/her IRM support person for the HINQ package.
- The IRM support person will install any DVB (HINQ package) patches that are missing.

> *Note:* A Disability Condition that is missing from the local database will not update the Patient’s VistA record.

![](dvb-4-49-training-guide/038.png)

# Objective \# 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Miscellaneous Changes in HINQ Responses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HINQUP Fields Removed

#### VBA is no longer supporting the following data fields:

- Combat Disability Indicator
- Additional Service
- Rated Disabilities Verified – calculated based on the veteran’s net award, check amount non-pay status and service separation date
- Type of Benefit
- Amount Social Security
- Other Annual Retirement- Payee
- Amount Other Annual Retirement - Payee
- Amount Other Annual Income - Payee
- Amount Social Security - Spouse
- Other Annual Retirement - Spouse
- Amount Other Annual Retirement - Spouse
- Amount Other Annual Income - Spouse
- Amount Other Annual Retirement - Spouse
- Master Record Type
- Number SC Disabilities - calculated
- Additional Disabilities
- Hardship Expenses
- Severance Recoupment
- PFOP/FDIB
- Consolidated Payment
- Special Provision
- Special Monthly Compensation
- Diary Date
- Diary Reason
- Nursing Home Indicator
- Competency Payment Factor
- CHAMPVA Indicator
- SSI

> Retrieval of the more descriptive code for SC conditions

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Current HINQ</p>
</blockquote></th>
<th><blockquote>
<p>HINQ Redesign</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>5299 Condition of The Skeletal System</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>5293 Invertebral disc syndrome</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>5010 Traumatic Arthritis</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>5206 Limited Flexion of Forearm</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>5010 Traumatic Arthritis</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>5260 Limited Flexion of Knee</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

![](dvb-4-49-training-guide/039.png)

# Objective \# 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Business Process Changes
- Responses to VistA HINQ Simultaneous HL7 sent to HEC

> HINQ Response Routing

#### Every successful HINQ response will also send an update to the HEC immediately.

- This will help insure that HEC enrollment records have the most current VBA information.

> Detecting terminated VBA records

- VBA’s Corporate Database keeps the eligibility factors on file even after a benefit is terminated.
- Responses should be carefully reviewed to see if the Net Award Amount is \$0, particularly in Pension cases.
- It is possible for the Check Amount to be \$0, while the New Award Amount is greater than zero.
- If the Net Award Amount is zero and the benefit is Pension, then VBA has terminated the award.
- It is critical that the site call the HEC in this case so the veteran can be properly re-categorized.

> What to do when you don’t get a HINQ response

#### Check the following:

- Verified Eligibility is completed at site.
- Check the eligibility to ensure the enrollment status is verified.
- Verify the veteran’s Means Test Status to ensure it is not in a ‘pending or not completed’ status.
- If either the eligibility or means tests status is not verified,
  - Query the HEC for an update from the Registration Menu, enrollment option, sub menu Send Query.
- If the Query to HEC does not resolve the eligibility, Allow 24 hours before contacting HEC via facsimile to REDACTED or email to VHA CIO HECAlert mail group.
- If updated eligibility that agrees with your determination is not received within 24-48 hours, query the HEC using Registration Menu, Enrollment Option, sub menu Send Query.
- Check response from message to see why an update is not being provided.
- For NSC and 0% Non-compensable Veterans, HEC’s Legacy System will use information on file at site with verified eligibility. If no verified eligibility located at site(s) veteran has visited, record will remain unverified. Sites receive a bulletin indicating HEC has no verified Eligibility.
- If HEC has no verified eligibility on a NSC and 0% Non-compensable Veteran, sites should verify the record on Registration screen 11 and wait 24 hours for information to transmit to HEC and retransmit back to site.
- Records that fail to update as a result of your HINQ inquiry will go into a Review File for Daily Manual Review by HEC Staff.

![](dvb-4-49-training-guide/040.png)

# Objective \# 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Security Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> New Security Requirements

- VBA’s new system provides an opportunity to enhance access security
- VHA users must be identified in VBA’s Common Security Services (CSS); old HINQ passwords will continue to be used
- New Access Rules:

#### All accounts are active for 90 days once the HINQ user is established in CSS.

- ![](dvb-4-49-training-guide/041.png)All users must interact with their accounts within 90 days to keep their accounts from becoming deactivated.

> DVB_4_P49_TG

![](dvb-4-49-training-guide/042.png)

> New Security Requirements

- VBA encourages deactivated users to contact the VBA ISO directly.

>  Remember that the application name is WEB HINQ!

- On all reset accounts the user has until the end of the day to use their password, otherwise the account will automatically revert back to an inactive status.
- All accounts that are inactive for 180 days will be automatically deleted.

![](dvb-4-49-training-guide/043.png)

# Objective \# 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### How to request a HINQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HINQ Request

### How to generate an HINQ Request:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Suspense file
- Individual HINQ request

### Using the Individual HINQ Request option:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Direct Method
- Patient Method

> *Note:*

- HINQ Request functionality was not changed by HINQ software package.

### Generate HINQ Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Suspense File requests

#### Placing the request into a Suspense file queues the request until someone with a DVBHINQ security key processes the Suspense file.

- Any user can add a HINQ request to the Suspense file (i.e. DVBHINQ security key is not required).

### Example A –

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Adding a request to the suspense file

### Individual HINQ Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Individual HINQ request provides an immediate (or real-time) response for the user.
- The user must have the DVBHINQ security key to use the Individual HINQ request option.
- There are two types of Individual requests:
  - *Patient Method*
  - *Direct Method*

### Patient Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Patient method requires that the patient be in the VistA PATIENT file.

![](dvb-4-49-training-guide/044.png)![](dvb-4-49-training-guide/045.png)![](dvb-4-49-training-guide/046.png)

### Example B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Individual HINQ Request using the Patient Method

> Select patients, enter your Password and HINQ requests will be sent Select Medical Center Division: BRONX OPC// \<RET\>

> Select PATIENT NAME: TESTI,PATIENT 02-16-27 000451832 SC VETERAN Select PATIENT NAME: TESTJ,PATIENT 07-01-40 000083997 SC VETERAN Select PATIENT NAME: TESTK,PATIENT 09-30-26 000662389 NSC VETERAN Select PATIENT NAME: \<RET\>

> Enter HINQ PASSWORD: Direct Requests Queued \#111111111

### Direct Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The Direct method prompts the user for the patient’s SSN, Claim Number, or Service Number.

- The user is then prompted for his/her HINQ password.
- Then the HINQ request is transmitted immediately to the AAC.

![](dvb-4-49-training-guide/047.png)![](dvb-4-49-training-guide/048.png)

### Example C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Individual HINQ Request using the Direct Method

> This option will take 30 seconds to activate – using IP Addressing Do you wish to continue? YES// \<RET\> (YES)

> Connecting to VBA database. . .

> Select Input: Patient File, or Direct P// D

> Enter one of the following numbers: Claim Number Social Security Number, or Service Number.

1.  Claim Number
2.  Social Security Number
3.  Service Number CHOICE: 1// 2

> Social Security: 000456789 OK ? Yes// (Yes)

> Enter HINQ PASSWORD:

> Response received and mailed

> DVB_4_P49_TG 47

![](dvb-4-49-training-guide/049.png)

> Questions & Comments

### HINQ Replacement Interim Solution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dvb-4-49-training-guide/050.png)![](dvb-4-49-training-guide/051.png)

> VistA Documentation Library

#### Review all HINQ Documentation on the VistA Documentation Library.

- User Manual
- Technical Manual
- Release Notes
- Installation Guide
- <http://www.va.gov/vdl/Financial_Admin.asp?appID=41>