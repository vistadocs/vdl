---
title: IB*2*432 eClaims Iteration 4 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: eClaims Iteration 4
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*432
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - span
  - billing
  - table
  - provider
  - secondary
  - contents
  - claims
  - class
  - edit
  - insurance
page_count: 0
word_count: 5957
section_count: 14
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_p432_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_p432_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

eClaims Iteration 4

Release Notes

![](ib-2-432-eclaims-iteration-4-release-notes/001.png)

Patch IB\*2\*432

September 2011

Veterans Affairs

Product Development (PD)

Revision History

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 39%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>9/20/11</td>
<td>1.0</td>
<td>Initial</td>
<td><p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Hardware Compatibility](#hardware-compatibility)
  - [System Specifications](#system-specifications)
  - [Installation and Configuration Notes](#installation-and-configuration-notes)
  - [Supported Functionality](#supported-functionality)
- [Release Changes and Enhancements](#release-changes-and-enhancements)
  - [Modified Option - Enter/Edit Billing Information \[IB Edit Billing Info\]](#modified-option-enteredit-billing-information-ib-edit-billing-info)
    - [Addition of New Screen 8](#addition-of-new-screen-8)
    - [Changes to Existing Screens](#changes-to-existing-screens)
    - [Screen 6 and 7 – Section 5](#screen-6-and-7-section-5)
    - [Changes to Error/Warning Messages](#changes-to-errorwarning-messages)
  - [Modified Option – Provider ID Maintenance \[IBCE Provider Maint\]](#modified-option-provider-id-maintenance-ibce-provider-maint)
    - [Changes to Non-VA Facility Information](#changes-to-non-va-facility-information)
  - [Modified – Output Formatter](#modified-output-formatter)
  - [Modified – Billing Provider Name](#modified-billing-provider-name)
  - [Modified – Auto-Biller processes](#modified-auto-biller-processes)
  - [Modified Option – Insurance Company Entry/Edit \[IBCN Insurance Co Edit\]](#modified-option-insurance-company-entryedit-ibcn-insurance-co-edit)
    - [Additions to EDI Parameters](#additions-to-edi-parameters)
    - [New Electronic Plan Types](#new-electronic-plan-types)
  - [Modified Option – MCCR Site Parameters Display/Edit \[IBJ MCCR Site Parameters\]](#modified-option-mccr-site-parameters-displayedit-ibj-mccr-site-parameters)
    - [IB Site Parameters](#ib-site-parameters)
  - [Automatic Processing of non-MRA Secondary/Tertiary Claims](#automatic-processing-of-non-mra-secondarytertiary-claims)
  - [New Option – COB Management Worklist \[IBCE COB Management\]](#new-option-cob-management-worklist-ibce-cob-management)
    - [COB Management Worklist](#cob-management-worklist)
- [Support Information](#support-information)
Release Date: September 2011
Patch Release: IB\*2\*432
The intent of this patch is to:
- Add new fields to the Enter/Edit Billing Information option to allow users to enter new X12 5010 data elements to claims for health care services provided to patients;
- Remove fields that are no longer needed in an X12 5010 claims transmission from the Enter/Edit Billing Information option;
- Modify the HIPAA 837 Health Care Claim message formats to reflect the changes made to Enter/Edit Billing Information
- Modify the Enter/Edit Billing Information option to retrieve the calculated Billing Provider’s name from the new 200 field of the Institution file;
- Modify the Enter/Edit Billing Information option to allow the creation of electronic claims to a payer which are subsequent to Medicare WNR (Will Not Reimburse), without first sending the claims to Medicare for receipt of Medicare-equivalent Advice (MRA);
- Modify the Enter/Edit Billing Information option to allow users to enter larger dollar amounts for each line item (9999999.99);
- Modify the Enter/Edit Billing Information option and the HIPAA 837 Health Care Claim transmissions to no longer require or transmit SSNs as primary IDs for human providers;
- Modify the Auto-biller process so that claims for health care services provided to patients are only created for dates of service that fall within both the Filing Time Frame (FTF) of the payer and the effective dates of the patients’ insurance;
- Modify the Auto-biller process so that institutional claims for health care services provided to patients are created with a calculated Billing Provider of the Veterans Affairs Medical Center (VAMC) if the patient was treated at the VAMC or the first Community Based Outpatient Clinic (CBOC) if the patient was not treated at the VAMC but was treated at more than one CBOC on the date of service;
- Modify the Provider ID Maintenance option to allow users to define Contact Information for non-VA Facilities;
- Modify the Insurance Company Entry/Edit option to allow users to set a flag that will determine when automatically create secondary/tertiary claims must be forced to print locally (set to allow transmission at the time of installation);
- Modify the Insurance Company Entry/Edit option to allow users to set a flag that will determine when claims secondary to Medicare WNR claims which were not first sent to Medicare (no MRAs) must be forced to print locally (set to allow transmission at the time of installation);
- Modify the Insurance Company Entry/Edit option to allow users to select additional Electronic Plan Type Qualifiers;
- Add the ability for the system to automatically create and transmit secondary/tertiary claims (non-Medicare) to payers when the Explanation of Benefits (EOB) data from the primary/secondary claims meets specified criteria;
- Add the ability for users to access a new option, COB Management Worklist, to manage those secondary/tertiary claims whose EOB data fails to meet specified criteria;
- Add a new, non-human user called AUTHORIZER,IB REG to the New Person (#200) file to which the automatic processing of secondary/tertiary claims will be attributed.
- Add new and remove old warning/error messages to support the changes to the Enter/Edit Billing Information option;
- Remove the default Billing Provider Secondary ID (the Tax ID Number of the VAMC) that used to be added to claims if no Billing Provider Secondary ID was defined in Insurance Company Entry/Edit;
- Modify the Enter/Edit Billing Information option to prevent the addition of the hard-coded Medicare Billing Provider Secondary IDs (674499 and 670899) from being erroneously added to Medicare WNR Part A claims when they are not defined in the Insurance Company Entry/Edit option;
- Modify the MCCR Site Parameters Display/Edit option to allow users to define printers to which automatically created secondary/tertiary claims and their associated EOBs can be sent when the payer is unable to accept electronic claims and to disable the automatic processing of secondary/tertiary claims.

## Hardware Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special hardware considerations.

## System Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special system considerations.

## Installation and Configuration Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IB\*2\*432 should be installed using the KIDS Installation 6 (Install package) option. Please note for Step 3b of the KIDS Patch Description, if you select option \#1 to run a Full Comparison you will get a system error: \<UNDEFINED\>S+1^DIQ ^IBA(364.6,1937,0) due to a known issue with the KIDS Full Compare option (see Remedy Ticket \# HD0000000449128). You can run any of the other 3 compare options without issue.

Important Note:

There is one MANDATORY pre-installation activity associated with this install. The IB Staff MUST empty the 837 extract/transmission queue PRIOR to the installation of this patch.

Recommended Procedure:

The site IRM would coordinate with the Billing Department to insure that the 837 extract/transmission queue is empty. The Billing Department should be aware of the set of instructions to be executed. If not billing supervisor can be contacted. Once the Billing Department has completed the instruction, the Billing department is to inform IRM that the patch installation could proceed.

There are no other mandatory pre-installation activities associated with this package.

There are several new fields being added to the Insurance Company file (file \#36), the IB Site Parameters file (file \#350.9 ), and the IB Non/Other VA Billing Provider file (file \#355.93 ) with this install that the facility may want to complete sometime after the installation is done. Most are Yes/No fields or default printers and are discussed in more detail in Section 2, Release Changes and Enhancements.

This patch also included modifications to the Group Insurance Plan file (file \#355.3), the IB Bill/Claims Prescription Refill file (file \#362.4), and deletions, modifications and additions to entries in the IB Error file (file \#350.8), the IB Data Element Definition file (file \#364.5), the IB Form Skeleton Definition file (file \#364.6), and the IB Form Field Content file (file \#364.7). If your facility has any local print fields, these changes may affect them. If your facility has placed local code within the definitions of any entry in files 364.5 and/or 364.7 that is being modified or deleted with this install, then you will need to save the custom code and review it after the installation.

Below is a list of Boxes/Form Locators that have changed:

The following new 364.5, IB DATA ELEMENT DEFINITIONS are created with this install:

1.  N-REFERRING PROVIDER NAME BR
2.  N-OPERATING PHYSICIAN NAME BR
3.  N-SPRVSING PROV FULL NAME BR
4.  N-OPERATING PHYSICIAN DATA BR
5.  N-RENDERING PHYSICIAN NAME BR
6.  N-ATTENDING PHYSICIAN NAME BR
7.  N-ATT/REND PHYSICIAN NAME BR
8.  N-CMS-1500 BOX 24I ID QUAL BR
9.  N-CMS-1500 24J REND PROV ID BR

Some of these new definitions have been used in the CMS-1500 report in the following fields:

1.  Box 17. NAME OF REFERRING PROVIDER OR OTHER SOURCE

> N-REFERRING PROVIDER NAME BR

2.  Block 31. SIGNATURE OF PHYSICIAN OR SUPPLIER INCLUDING DEGREES OR CREDENTIALS

> N-ATT/REND PHYSICIAN NAME BR

3.  Box 24I. ID. QUAL

> N-CMS-1500 BOX 24I ID QUAL BR

4.  Box 24J. RENDERING PROVIDER ID# and NPI

> N-CMS-1500 24J REND PROV ID BR

Code was changed in dictionary 364.7 in the CMS-1500 report in the following fields:

1.  Box 17A/1. REFERRING PROVIDER OTHER ID QUALIFIER
2.  Box 17A/2. REFERRING PROVIDER OTHER ID#
3.  Box 17B. REFERRING PROVIDER NPI.
4.  Block 31. SIGNATURE OF PHYSICIAN OR SUPPLIER INCLUDING DEGREES OR CREDENTIALS.

Code was changed in dictionary 364.7 in the UB-04 report in the following fields:

1.  FL-76 ATTENDING Last Name
2.  FL-76 ATTENDING First Name
3.  FL-77 OPERATING Last Name
4.  FL-77 OPERATING First Name
5.  FL-78 OTHER Last Name
6.  FL-78 OTHER First Name

The following entries in file 364.7 (listed by internal entry number) are being deleted with this installation:

150, 204, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 470, 576, 577, 578, 579, 580, 581, 582, 588, 1022, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1614, 1688, and 1689

In addition to the file changes already mentioned, there are more than 60 new or modified fields being added to the Bill/Claims file (file \#399). Also new or modified in this patch are: more than 90 IB routines, 9 IB Screens, 3 IB Options, 18 Protocols and 2 List Templates. Because of the extensive number of changes to IB files, routines, protocols and screens in this patch, it is necessary that this patch be installed after hours, when no IB users are on the system.

The patch includes a pre-install (IBY432PR) and post-install routine (IBY432PO), which will run automatically with the KIDS install. The pre-install routine deletes output formatter entries in files 364.5, 364.6 and 364.7 that are no longer being used and also modifies and adds new entries to those files, recompiles all the billing screens and deletes some fields from the Data Dictionary of the Bill/Claims file (file \#399) that were marked for deletion in May of 2007. The obsolete fields to be deleted from this file are field \#’s: 450, 451, 452 and 456. The post-install routine recompiles the billing screens again, after the KIDS install makes all of the previously mentioned file changes. In addition, the post-install also adds the following generic user to file 200: AUTHORIZER,IB REG, to be used with the new automatic processing of non-MRA Secondary/Tertiary claims (see section 2.8 for more details). Lastly, the following post-install activity will be preformed: It loops through the claim file (#399) to find any ENTERED/NOT REVIEWED claims that do NOT have a Taxonomy Code assigned at the claim level for a Provider. It will add the Provider’s Taxonomy Code at the time of the claim event date to the claim. It will display the following information to your screen for each claim that it modifies:

Taxonomy code Internal Entry Number (IEN) *\[number\]*for provider *\[name\]*added to bill# *\[bill\]*

At the end of the process it will give you the total number of bills that were updated.

<span id="_Toc303235587" class="anchor"></span>Because the IB\*2\*432 Patch includes modified menu options, you MUST answer YES at the following prompt:

 

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

## Supported Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release will provide the ability for the VA to transmit 837 Health Care Claim transmissions to the VA’s Financial Services Center (FSC) with sufficient data to allow FSC to create either X12 4010 claim messages or X12 5010 claim messages depending upon the readiness of the destination payer to accept X12 5010 claim transmissions.

This release will also provide the functionality that will support the automatic processing of secondary/tertiary (non-Medicare) claims based upon specified criteria as well as the functionality to support the manual management by users of those claims which fail the automatic processing criteria.

# Release Changes and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Modified Option - Enter/Edit Billing Information \[IB Edit Billing Info\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Addition of New Screen 8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There will be a new billing screen 8. The existing billing screen 8 will become screen 10. The new billing screen 8 will provide the ability for users to add new claim level data elements to an institutional or professional claim.

The new field, COB Non-Covered Charge Amt, in Section 1 will provide the ability for users to enter an amount that can be transmitted to payers who are subsequent to MRA and who accept electronic claims without MRA Coordination of Benefits data.

Screen 8 – CMS 1500

IB,PATIENT TWO XX-XX-XXXX BILL#: KXXXXXX - Outpat/<span class="mark">1500</span> SCREEN \<8\>

================================================================================

BILLING - CLAIM INFORMATION\[1\] COB Non-Covered Charge Amt:

\[2\] Property Casualty Information

Claim Number: Contact Name:

Date of 1st Contact: Contact Phone:

\[3\] Ambulance Information

D/O Location:

P/U Address1: D/O Address1:

P/U Address 2: D/O Address2:

P/U City: D/O City:

P/U State/Zip: D/O State/Zip:

\[4\] Surgical Codes for Anesthesia Claims

Primary Code: Secondary Code:

\[5\] Paperwork Attachment Information

Report Type: Transmission Method:

Attachment Control \#:

\[6\] Disability Start Date: Disability End Date:

\[7\] Assumed Care Date: Relinquished Care Date:

\<RET\> to CONTINUE, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT:

Not all data elements on Screen 8 are allowed on institutional claims. Those fields that are inappropriate for institutional claims are disabled when the form type is UB04.

Screen 8 – UB04

IB,PATIENT ONE XX-XX-XXXX BILL#: KXXXXXX - Outpat/<span class="mark">UB04</span> SCREEN \<8\>

================================================================================

BILLING - CLAIM INFORMATION\[1\] COB Non-Covered Charge Amt:

\[2\] Property Casualty Information

Claim Number: Contact Name:

Date of 1st Contact: Contact Phone:

<span class="mark">\<3\> Ambulance Information</span>

D/O Location:

P/U Address1: D/O Address1:

P/U Address 2: D/O Address2:

P/U City: D/O City:

P/U State/Zip: D/O State/Zip:

<span class="mark">\<4\> Surgical Codes for Anesthesia Claims</span>

<span class="mark">Primary Code: Secondary Code:</span>

\[5\] Paperwork Attachment Information

Report Type: Transmission Method:

Attachment Control \#:

<span class="mark">\<6\> Disability Start Date: Disability End Date:</span>

<span class="mark">\<7\> Assumed Care Date: Relinquished Care Date:</span>

\<RET\> to CONTINUE, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT:

### Changes to Existing Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There will be changes to Section 2 of billing screen 3 to no longer populate the Billing Provider Secondary ID with the VAMC’s Tax Identification Number when no ID has been defined in the Insurance Company Editor for a payer.

Screen 3

IB,PATIENT ONE XX-XX-XXXX BILL#: K701XXX - Inpat/UB04 SCREEN \<3\>

================================================================================

PAYER INFORMATION\[1\] Rate Type : REIMBURSABLE INS. Form Type: UB-04

Responsible: INSURER Payer Sequence: Primary

Bill Payer : MRA NEEDED FROM MEDICARE Transmit: Yes

Ins 1: MEDICARE (WNR) WILL NOT REIMBURSE Policy \#: XXXXXXXXXA

Grp \#: PART B Whose: VETERAN Rel to Insd: PATIENT

Grp Nm: PART B Insd Sex: FEMALE Insured: IB,PATIENT O

Ins 2: BLUE CROSS CA (W Policy \#: 111XXXB

Grp \#: GRP NUM 11207 Whose: VETERAN Rel to Insd: PATIENT

Grp Nm: SPRACKLEN Insd Sex: FEMALE Insured: IB,INPAT ONE

\[2\] Billing Provider Secondary IDs:

<span class="mark">Primary Payer:</span>

Secondary Payer: XXXXX Tertiary Payer:

\[3\] Mailing Address : Electronic ID: 12M61

NO MAILING ADDRESS HAS BEEN SPECIFIED! (Patient has Medicare)

Send Bill to PAYER listed above.

\<RET\> to CONTINUE, 1-3 to EDIT, '^N' for screen N, or '^' to QUIT:

There will be changes to Section 4 of billing screens 4/ 5 that will provide the ability for users to add new line level data elements to an institutional or professional claim.

Section 4 - Institutional

Select PROCEDURE: 71010

Searching for a CPT, (pointed-to by PROCEDURES)

Searching for a CPT

71010 CHEST X-RAY

...OK? Yes// (Yes)

PROCEDURES: 71010//

Select CPT MODIFIER SEQUENCE:

CPT MODIFIER:

<span class="mark">Rendering Provider</span>: IB,DOCTOR CARD DCI CARDIOLOGIST

TAXONOMY: Allopathic and Osteopathic Physicians

//

Classification: Thoracic Surgery (Cardiothoracic Vascular Surgery)

Specialty Code: 33

Taxonomy X12 Code: 208G00000X

Prov Specialty On File: 33

CREDENTIALS: MD//

\*\*\*\* SECONDARY PERFORMING PROVIDER IDs \*\*\*\*

PRIMARY INSURANCE CO: BLUE CROSS CA (WY)

PROVIDER: IB,DOCTOR CARD (RENDERING)

INS. COMPANY'S DEFAULT SECONDARY ID TYPE IS: BLUE CROSS

AND IS REQUIRED TO BE ENTERED FOR THIS CLAIM

SELECT A SECONDARY ID OR ACTION FROM THE LIST BELOW:

1 - NO SECONDARY ID NEEDED

2 - ADD AN ID FOR THIS CLAIM ONLY

3 - \<DEFAULT\> VAD000 BLUE CROSS

Selection: 3//

ID SELECTED:

3 - \<DEFAULT\> VAD000 BLUE CROSS

IS THIS CORRECT?: YES//

<span class="mark">Referring Provider</span>: IB,do

Searching for a VistA identified provider

1 IB,DOCTOR CARD DCI CARDIOLOGIST

2 IB,DOCTOR GP DGI PHYSICIAN

3 IB,DOCTOR RAD DRI RADIOLOGIST

CHOOSE 1-3: 2 IB,DOCTOR GP DGI PHYSICIAN

TAXONOMY: Allopathic and Osteopathic Physicians

//

Classification: Internal Medicine

Area of Specialization: Adolescent Medicine

Specialty Code: 11

Taxonomy X12 Code: 207RA0000X

Prov Specialty On File: 11

CREDENTIALS: MD//

\*\*\*\* SECONDARY PERFORMING PROVIDER IDs \*\*\*\*

PRIMARY INSURANCE CO: BLUE CROSS CA (WY)

PROVIDER: IB,DOCTOR GP (REFERRING)

INS. COMPANY'S DEFAULT SECONDARY ID TYPE IS: BLUE CROSS

SELECT A SECONDARY ID OR ACTION FROM THE LIST BELOW:

1 - NO SECONDARY ID NEEDED

2 - ADD AN ID FOR THIS CLAIM ONLY

3 - \<DEFAULT\> VAD000 BLUE CROSS

Selection: 3//

ID SELECTED:

3 - \<DEFAULT\> VAD000 BLUE CROSS

IS THIS CORRECT?: YES//

<span class="mark">Operating Physician</span>:

<span class="mark">Other Operating Physician</span>:

ASSOCIATED CLINIC: RADIOLOGY DIV 442 OOS ID 105

DIVISION: ANYSITE VAMROC//

PRINT ORDER: 1

<span class="mark">Enter Attachment Control Number? NO// YES</span>

<span class="mark">Report Type</span>: 10 Continued Treatment

<span class="mark">Report Transmission Method</span>: E-Mail

<span class="mark">Attachment Control Number</span>: 123456ACN

Adding OP Visit Date of OCT 06, 2010

Section 4 – Professional

PROCEDURES: 71010//

Select CPT MODIFIER SEQUENCE: 1

CPT MODIFIER: 26 PROFESSIONAL COMPONENT

Select CPT MODIFIER SEQUENCE:

<span class="mark">Rendering Provider</span>: IB,DOCTOR RAD

Searching for a VistA identified provider

IB,DOCTOR RAD DRI RADIOLOGIST

...OK? Yes// (Yes)

TAXONOMY: Allopathic and Osteopathic Physicians

//

Classification: Radiology

Area of Specialization: Body Imaging

Specialty Code: 30

Taxonomy X12 Code: 2085B0100X

Prov Specialty On File: 30

CREDENTIALS: MD//

\*\*\*\* SECONDARY PERFORMING PROVIDER IDs \*\*\*\*

PRIMARY INSURANCE CO: BLUE CROSS CA (WY)

PROVIDER: IB,DOCTOR RAD (RENDERING)

INS. COMPANY'S DEFAULT SECONDARY ID TYPE IS: BLUE SHIELD

AND IS REQUIRED TO BE ENTERED FOR THIS CLAIM

NO SECONDARY IDS ARE DEFINED FOR THIS PROV THAT ARE VALID FOR THIS CLAIM

SELECT A SECONDARY ID OR ACTION FROM THE LIST BELOW:

1 - NO SECONDARY ID NEEDED

2 - ADD AN ID FOR THIS CLAIM ONLY

Selection: 1// 2

PRIM INS PERF PROV SECONDARY ID TYPE: 1B BLUE SHIELD 1B

PRIM INS PERF PROV SECONDARY ID: 12345BS

<span class="mark">Referring Provider</span>: IB,DOCTOR GP

Searching for a VistA identified provider

IB,DOCTOR GP DGI PHYSICIAN

...OK? Yes// (Yes)

TAXONOMY: Allopathic and Osteopathic Physicians

//

Classification: Internal Medicine

Area of Specialization: Adolescent Medicine

Specialty Code: 11

Taxonomy X12 Code: 207RA0000X

Prov Specialty On File: 11

CREDENTIALS: MD//

\*\*\*\* SECONDARY PERFORMING PROVIDER IDs \*\*\*\*

PRIMARY INSURANCE CO: BLUE CROSS CA (WY)

PROVIDER: IB,DOCTOR GP (REFERRING)

INS. COMPANY'S DEFAULT SECONDARY ID TYPE IS: BLUE SHIELD

AND IS REQUIRED TO BE ENTERED FOR THIS CLAIM

NO SECONDARY IDS ARE DEFINED FOR THIS PROV THAT ARE VALID FOR THIS CLAIM

SELECT A SECONDARY ID OR ACTION FROM THE LIST BELOW:

1 - NO SECONDARY ID NEEDED

2 - ADD AN ID FOR THIS CLAIM ONLY

Selection: 1// 2

PRIM INS PERF PROV SECONDARY ID TYPE: 1B BLUE SHIELD 1B

PRIM INS PERF PROV SECONDARY ID: 1234BS

<span class="mark">Supervising Provider</span>:

ASSOCIATED CLINIC: RADIOLOGY DIV 442 OOS ID 105

DIVISION: ANYSITE VAMROC//

PLACE OF SERVICE: 22 OUTPATIENT HOSPITAL

TYPE OF SERVICE: 4 DIAGNOSTIC X-RAY

EMERGENCY PROCEDURE?: NO// NO

PRINT ORDER: 1

----------------- Existing Diagnoses for Bill -----------------

1\. 466.0 ACUTE BRONCHITIS (3)

\*\*\* Please select procedure diagnoses by number to left of diagnosis code \*\*\*

Associated Diagnosis (1): 1 466.0

Associated Diagnosis (2):

PURCHASED COST:

SERVICE LINE COMMENT QUALIFIER:

SERVICE LINE COMMENT:

<span class="mark">Enter Attachment Control Number? NO//</span>

EDIT CMS-1500 SPECIAL PROGRAM FIELDS and BOX 19?: NO//

There will also be a line level change for Anesthesia claims to allow users to add additional minutes to anesthesia claims for obstetric procedures when more than the normal amount of minutes were required.

Section 4 - Professional

PRINT ORDER: 2

MINUTES: 60

<span class="mark">Additional OB Minutes</span>:

There will be changes to Section 3 of billing screen 10 to provide the ability for users to add additional provider types to an institutional or professional claim.

The name for the calculated Billing Provider displayed in Section 5 of billing screen 10 will be retrieved from the new 200 field in the Institution file (#4). If there is no value in that field, the name will be retrieved from the .01 field.

There will be changes to Section 1 of billing screen 10 to provide the ability for users to add a Referral number(s) to an institutional or professional claim.

Screen 10 – Outpatient

IB,PATIENT T XX-XX-XXXX BILL#: KXXXXXXX - Outpat/UB04 SCREEN \<10\>

================================================================================

BILLING - SPECIFIC INFORMATION

\[1\] Bill Remarks

\- FL-80 : UNSPECIFIED \[NOT REQUIRED\]

ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

<span class="mark">Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]</span>

Admission Source : UNSPECIFIED

\[2\] Pt Reason f/Visit : UNSPECIFIED

\[3\] Providers :

\- ATTENDING (MD) : IB,DOCTOR ONE Taxonomy: 208G00000X (33)

\[P\]VAD000

\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]

\[5\] Billing Provider : ANYSITE VAMC

Taxonomy Code : 282N00000X

\[6\] Force To Print? : NO FORCED PRINT

\[7\] Provider ID Maint : (Edit Provider ID information)

\<RET\> to QUIT, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT: 1

BILL REMARKS:

PRIMARY INSURANCE ICN/DCN:

SECONDARY INSURANCE ICN/DCN:

TERTARY INSURANCE ICN/DCN

PRIMARY AUTHORIZATION CODE:

<span class="mark">PRIMARY REFERRAL NUMBER:</span>

SECONDARY AUTHORIZATION CODE:

<span class="mark">SECONDARY REFERRAL NUMBER:</span>

TERTIARY AUTHORIZATION CODE:

<span class="mark">TERTIARY REFERRAL NUMBER</span>:

There will be changes to billing Screen 6 and 7 to remove the Covered Days, Non-Covered Days and Coinsurance Days fields. The data previously handled by these fields will be managed through Condition Codes.

Screen 6 – Section 1

IB,PATIENT TWO XX-XX-XXXX BILL#: K701XXX - Inpat/UB04 SCREEN \<6\>

===============================================================================

BILLING - GENERAL INFORMATION

\[1\] Bill Type : 111 Loc. of Care: HOSPITAL - INPT OR OPT (INCLU

Charge Type : INSTITUTIONAL Timeframe: ADMIT THRU DISCHARGE

Form Type : UB-04 Division: ANYSITE VAMROC

Bill Classif: INPATIENT (MEDICARE-A)

Screen 7 – Section 1

IB,PATIENT ONE XX-XX-XXXX BILL#: KXXXXXX - Outpat/1500 SCREEN \<7\>

================================================================================

BILLING - GENERAL INFORMATION\[1\] Bill Type : 131 Loc. of Care: HOSPITAL - INPT OR OPT (INCLU

Charge Type : PROFESSIONAL Disch Stat: DISCHARGED TO HOME UNDER CARE

Form Type : CMS-1500 Timeframe: ADMIT THRU DISCHARGE

Bill Classif: OUTPATIENT Division: ANYSITE VAMROC

### Screen 6 and 7 – Section 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The dollar amount that can be associated with a line item can now be larger, 9999999.99, before the charges must be split.

### Changes to Error/Warning Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes were made to existing error and/or warning messages to support the changes made in Enter/Edit Billing information.

Example:

Human providers will no longer be required to have a Social Security Number (SSN) defined in VistA and no SSNs will be transmitted in 837 Health Care Claim transmissions therefore the error message for missing provider SSNs was removed.

## Modified Option – Provider ID Maintenance \[IBCE Provider Maint\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Changes to Non-VA Facility Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There will be changes to Provider ID Maintenance non-VA FacilityFacility Information that will provide the ability for users to define Contact Information for a non-VA facility.

Facility Information

NAME: IB OUTSIDE FACILITY//

STREET ADDRESS: 1234 TEST BLVD//

STREET ADDRESS LINE 2: SUITE 2001//

CITY: ANYSITE//

STATE: WYOMING//

ZIP CODE: 82003//

<span class="mark">CONTACT NAME: IB,CONTACT O//</span>

<span class="mark">CONTACT PHONE NUMBER: XXX-XXX-XXXX//</span>

<span class="mark">CONTACT PHONE EXTENSION: XXXXX//</span>

ID Qualifier: 24 - EMPLOYER'S IDENTIFICATION \#

Lab or Facility Primary ID: 1234567890//

X12 TYPE OF FACILITY: SERVICE LOCATION//

MAMMOGRAPHY CERTIFICATION \#:

NPI: 0000000006//

Select TAXONOMY CODE: Ambulatory Health Care Facilities

//

TAXONOMY CODE: Ambulatory Health Care Facilities

//

PRIMARY CODE: YES//

STATUS: ACTIVE//

Non-VA Lab or Facility Info Sep 16, 2010@13:36:47 Page: 1 of 1

Name: IB OUTSIDE FACILITY

Address: 1234 TEST BLVD

ANYCITY, WYOMING 82003

<span class="mark">Contact Name: IB,CONTACT O</span>

<span class="mark">Contact Phone: 703-333-3333 67587</span>

Type of Facility: SERVICE LOCATION

Primary ID: 1234567890

ID Qualifier: 24 - EMPLOYER'S IDENTIFICATION \#

Mammography Certification \#:

NPI: 0000000006

Taxonomy Code: 261QR0200X (Primary)

Enter ?? for more actions

FI Lab/Facility Info LI Lab/Facility Ins ID

LO Lab/Facility Own ID EX Exit

Select Action: Quit//

## Modified – Output Formatter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There were many changes and additions made to the 837 Health Care Claim map.

## Modified – Billing Provider Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The calculated Billing Provider name used to be retrieved from the .01 field of the Institution file (#4). It will now be retrieved from the 200 field, Billing Facility Name, of the Institution file. If for any reason, the new field is not populated, the software will then retrieve the name from the .01 field.

## Modified – Auto-Biller processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Auto-Biller will not create claims for patient services unless the timeframe falls within both the Insurance Company’s Filing Time Frame (FTF) and the Effective Date of the patient’s insurance.

Fields .18 and .19 of the Insurance Company file (#36) must be populated in order for this software to function correctly. Filling in the free text field is not sufficient to cause the Auto-Biller to verify the FTF.

When the Auto-Biller process creates an institutional claim for services provided to a patient at multiple locations on the same day, the calculated Billing Provider will be:

- the VAMC if any of the locations are the VAMC
- the first CBOC (acceptable facility type) if the patient was seen at multiple CBOCs and no VAMC

Insurance Company Editor – BP Billing/EDI ParametersInsurance Company Editor Oct 04, 2010@14:42:39 Page: 1 of 9

Insurance Company Information for: IB INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

Billing Parameters

Signature Required?: NO Type Of Coverage: HEALTH INSURAN

Reimburse?: WILL REIMBURSE Billing Phone: XXX-XXX-XXXX

Mult. Bedsections: Verification Phone: XXX-XXX-XXXX

One Opt. Visit: NO Precert Comp. Name:

Diff. Rev. Codes: Precert Phone:

Amb. Sur. Rev. Code:

Rx Refill Rev. Code:

Filing Time Frame: (12 MONTH(S))

EDI Parameters

Transmit?: YES-LIVE Insurance Type:

\+ Enter ?? for more actions \>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen// bp Billing/EDI Param

SIGNATURE REQUIRED ON BILL?: NO//

REIMBURSE?: WILL REIMBURSE//

ALLOW MULTIPLE BEDSECTIONS:

DIFFERENT REVENUE CODES TO USE:

ONE OPT. VISIT ON BILL ONLY:

AMBULATORY SURG. REV. CODE:

PRESCRIPTION REFILL REV. CODE:

<span class="mark">STANDARD FILING TIME FRAME: MONTH(S)//</span><span class="mark">STANDARD FILING TIME FRAME VALUE: 12//</span>

FILING TIME FRAME:

TYPE OF COVERAGE: HEALTH INSURANCE//

## Modified Option – Insurance Company Entry/Edit \[IBCN Insurance Co Edit\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Additions to EDI Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There will be changes to the Insurance Company Editor Billing/EDI Param. There will be additional fields that will provide the ability for users to determine whether or not:

- automatically created non-Medicare secondary/tertiary claims must be printed locally
- secondary/tertiary Medicare claims which did not go to Medicare and for which there are no MRAs must be printed locally

These fields will be Blank when the patch is installed and will therefore be set to transmit the claims if the payer is an electronic payer.

Insurance Company Editor - Billing/EDI Param

SIGNATURE REQUIRED ON BILL?: NO//

REIMBURSE?: WILL REIMBURSE//

ALLOW MULTIPLE BEDSECTIONS:

DIFFERENT REVENUE CODES TO USE:

ONE OPT. VISIT ON BILL ONLY:

AMBULATORY SURG. REV. CODE:

PRESCRIPTION REFILL REV. CODE:

STANDARD FILING TIME FRAME: MONTH(S)//

STANDARD FILING TIME FRAME VALUE: 18//

FILING TIME FRAME:

TYPE OF COVERAGE: HEALTH INSURANCE//

BILLING PHONE NUMBER: XXX-XXX-XXXX//

VERIFICATION PHONE NUMBER: XXX-XXX-XXXX//

Are Precerts Processed by Another Insurance Co.?:

PRECERTIFICATION PHONE NUMBER: XXX-XXX-XXXX//

EDI - Transmit?: YES-LIVE//

EDI - Inst Payer Primary ID: 12B30//

EDI - 1ST Inst Payer Sec. ID Qualifier:

EDI - Prof Payer Primary ID: SB960//

EDI - 1ST Prof Payer Sec. ID Qualifier:

EDI - Insurance Type: GROUP POLICY//

EDI - Bin Number:

<span class="mark">EDI - Print Sec/Tert Auto Claims?:</span>

<span class="mark">EDI - Print Medicare Sec Claims w/o MRA?:</span>

### New Electronic Plan Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There will be changes to the Insurance Company editorView PlansView/Edit PlanChange Plan Info to provide the ability for users to add two new types of Electronic Plan Types.

Insurance Company Editor – View Plans - Change Plan Info

GROUP PLAN NUMBER: XXXXXX//

BANKING IDENTIFICATION NUMBER:

PROCESSOR CONTROL NUMBER (PCN):

TYPE OF PLAN: PREFERRED PROVIDER ORGANIZATION (PPO)//

ELECTRONIC PLAN TYPE:??

This field contains the X12 data needed to identify the source of pay type

Choose from:

16 HMO MEDICARE

MX MEDICARE A or B

TV TITLE V

MC MEDICAID

BL BC/BS

CH TRICARE

15 INDEMNITY

CI COMMERCIAL

HM HMO

DS DISABILITY

12 PPO

13 POS

ZZ OTHER

<span class="mark">FI FEP</span>

<span class="mark">17 DENTAL</span>

ELECTRONIC PLAN TYPE:

## Modified Option – MCCR Site Parameters Display/Edit \[IBJ MCCR Site Parameters\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IB Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes will be made to the Section 7 of the IB Site Parameters that will provide the ability for users to define 3 printers to be used to print automatically created non-Medicare secondary/tertiary claims and their associated EOBs to payers who are unable to accept secondary/tertiary claims electronically.

IB Site Parameters - Section 7

IB Site Parameters Feb 02, 2011@15:28:21 Page: 2 of 5

Only authorized persons may edit this data.

\+

\[5\] Medical Center : ANYSITE VAMC Default Division : ANYSITE VAMR

MAS Service : BUSINESS OFFICE Billing Supervisor : REDACTED

\[6\] Initiator Authorize: YES Xfer Proc to Sched : YES

Ask HINQ in MCCR : YES Use Non-PTF Codes : YES

Multiple Form Types: YES Use OP CPT screen : YES

\[7\] UB-04 Print IDs : YES UB-04 Address Col :

CMS-1500 Print IDs : YES CMS-1500 Addr Col : 40

ENTERED/NOT REVIEWED <span class="mark">CMS-1500 Auto Prter: RM340 UB-04 Auto Prter : RM340</span>

<span class="mark">EOB Auto Prter : RM340 MRA Auto Prter : RM340</span>

\[8\] Default RX DX Cd : V68.1 Default ASC Rev Cd : 490

Default RX CPT Cd : J8499 Default RX Rev Cd : 250

\[9\] Bill Signer Name : \<No longer used\> Federal Tax \# : XX-XXXXXXX

Bill Signer Title : \<No longer used\>

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen// EP=7 Edit Set

UB-04 PRINT LEGACY ID: YES//

CMS-1500 PRINT LEGACY ID: YES//

UB-04 ADDRESS COLUMN:

CMS-1500 ADDRESS COLUMN: 40//

CMS-1500 Auto Printer: RM340//

UB-04 Auto Printer: RM340//

EOB Auto Printer: RM340//

MRA Auto Printer: RM340//

Changes will be made to the Section 14 of the IB Site Parameters that will provide the ability for users to stop the automatic processing of secondary/tertiary non-MRA claims. The claims will then appear on the COB Management Worklist.

IB Site Parameters - Section 14IB Site Parameters Feb 02, 2011@15:31:24 Page: 4 of 5

Only authorized persons may edit this data.

\+

EDI Contact Phone : XXX-XXX-XXXX

EDI 837 Live Transmit Queue : MCT

EDI 837 Test Transmit Queue : MCT

Auto-Txmt Bill Frequency : Every Day

Hours To Auto-Transmit : 1130;1500;1700

Max \# Bills Per Batch : 10

Only Allow 1 Ins Co/Claim Batch?: YES

Last Auto-Txmt Run Date : 02/02/11

Days To Wait To Purge Msgs : 15

Allow MRA Processing? : YES

Enable Automatic MRA Processing?: YES

<span class="mark">Enable Auto Reg EOB Processing? : YES</span>

\[15\]Are we using ClaimsManager? : NO

Is ClaimsManager working OK? : NO

ClaimsManager TCP/IP Address : XX.XXX.XX.XXX

ClaimsManager TCP/IP Ports : XXXXX

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen//

## Automatic Processing of non-MRA Secondary/Tertiary Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There will be a new, non-human user added to the system when the patch is installed to which the automatic processing of non-MRA secondary/tertiary claims will be attributed – IB,AUTHORIZE REG.

When all Explanation of Benefits (EOB) for a claim are received in VistA and Accounts Receivable (AR) personnel have posted the payment and closed the bill and the patient has additional insurance coverage, the system will no longer trigger an email to Integrated Billing informing them that there is a potential secondary/tertiary bill that needs to be created. If the information in the EOB meets the following criteria for all service lines, then the bill to the next payer will be created automatically:

- Adjustment Group Code = CO and is associated with one of the following Reason Codes: A2; B6; 42; 45; 102; 104; 118; 131; 23; 232; 44; 59; 94; 97; or 10; and
- Patient Responsibility Group Code = PR is associated with one of the following Reason Codes: 1; 2; or 66; and
- The sum of the deductible, coinsurance and co-payment amounts is greater than \$0.00; and
- The claim status is Approved; and
- The Claim Status Code (CLP02) = 1; 2; or 3.

  Bills that fail to criteria to create the secondary/tertiary claim automatically will be placed on the COB Management Worklist.

## New Option – COB Management Worklist \[IBCE COB Management\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### COB Management Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new option will be added to the existing EDI Menu for Electronic Bills that will provide the ability for users to manage those claims that fail to automatically create subsequent bills because they fail to meet the criteria for automatic processing. This new option will be very similar to the existing MRA Management Worklist.

EDI Menu For Electronic Bills

Select Billing Supervisor Menu Option: EDI Menu For Electronic Bills

MM EDI Return Message Management ...

TR EDI Transmission Status Reports ...

MRA MRA Management Menu ...

RCB View/Resubmit Claims - Live or Test

<span class="mark">CBW COB Management Worklist</span>

EXT Extract Status Management

SEND Transmit EDI Bills – Manual

Select EDI Menu For Electronic Bills Option:

COB Management Worklist

COB Management WorkList May 25, 2010@14:04:18 Page: 1 of 10

Bill \# Svc Date Patient Name SSN Pt Resp Bill Amt Care/Form

BILLER: IB,CLERK 1

1 442-K700XXX\* 09/07/06 IB,PATIENT 1 XXXX 0.00 60.07 OP/1500

Insurers: MEDICARE (WNR), UNITED COMMERCIAL TRAVELERS

EOB Status: DENIED, Oct 25, 2006

2 442-K700XXX 10/20/05 IB,PATIENT 2 XXXX 0.00 341.46 OP/UB-04

Insurers: MEDICARE (WNR), MUTUAL OF OMAHA

EOB Status: DENIED, Dec 05, 2006

3 442-K700XXX 10/21/05 IB,PATIENT 19 XXXX 0.00 76.36 OP/UB-04

Insurers: MEDICARE (WNR), BLUE CROSS/BS NE (65+WY)

EOB Status: DENIED, Dec 05, 2006

4 442-K700XXX 09/15/06 IB,PATIENT 66 XXXX 0.00 81.71 OP/UB-04

Insurers: MEDICARE (WNR), MAIL HANDLERS BENEFIT PLAN

EOB Status: DENIED, Jan 03, 2007

5 442-K700XXX 09/07/06 IB,PATIENT TWO XXXX 29.25 29.25 OP/1500

Insurers: MEDICARE (WNR), MUTUAL OF OMAHA

\+ Enter ?? for more actions

PC Process COB CB Cancel Bill RM Remove from Worklist

VE View an EOB CR Correct Bill PE EOB/MRA Printing

EC Enter/View Comments CC Cancel/Clone A Bill TP Third Party Joint Inq.

RS Review Status VB View Bill EX Exit

Select Action: Next Screen//

# Support Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing, these patches will be supported by the Office of Enterprise Development, the development team. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any issues that arrive related to these patches. At the end of this 30 day period, assistance with issues related to these patches will be addressed through the Help Desk and the submittal of Remedy tickets if needed.