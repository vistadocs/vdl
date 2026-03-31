---
title: PIMS Version 5.3 User Manual - Copay Exemption Test Supervisor Menu (Updated DG*5.3*891)
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Copay Exemption Test Supervisor Menu (Updated DG*5.3*891)
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: active
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3*891
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 13%\\" /> <col style=\\"width: 36%\\" /> <col style=\\"width: 25%\\" /> <col style=\\"width: 25%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th><strong>Date</strong></th> <th><strong>Description (Patch # if applic.)</strong></th> <th><strong>Project Manager</strong></th> <"
audience: 
keywords: 
  - test
  - copay
  - exemption
  - veteran
  - income
  - dependent
  - spouse
  - date
  - amount
  - mark
page_count: 0
word_count: 3322
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/dg_5_3_891_cets_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/dg_5_3_891_cets_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

PIMS V. 5.3 ADT Module User ManualCopay Exemption Test Supervisor Menu

Copay Exemption Test User Menu

> Add a Copay Exemption Test

> Copay Exempt Test Needing Update At Next Appt.

> Edit an Existing Copay Exemption Test

> List Incomplete Copay Exemption Test

> View a Past Copay Test

Delete a Copay Exemption Test

View Copay Exemption Test Editing Activity

Revision History

Initiated on 8/12/05

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 36%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description (Patch # if applic.)</strong></th>
<th><strong>Project Manager</strong></th>
<th><strong>Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8/12/05</td>
<td><p>DG*5.3*624 – 10-10EZ 3.0 Enhancements</p>
<ul>
<li><blockquote>
<p>Changed Printing Prompt Sequence in Financial Assessment Applications. Added note for Roll-Up Means Test Dollar Amounts (GAI and NW) to conform with amounts on Feb 2005 VistA-Printed 10-10EZ/EZR Forms.</p>
</blockquote></li>
<li><blockquote>
<p>Added updates based on revised business rules for evaluating child(ren)’s Income Available to veteran and how it affects the Gross Annual Income dollar amounts printed on the 10-10EZ/EZR and displayed in the Child(ren)’s column on the Previous Calendar Year Gross Income Screen 2.</p>
</blockquote></li>
</ul></td>
<td><mark>Redacted</mark></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>6/7/06</td>
<td>DG*5.3*611 – Fix Means Test Display – Updated Add a Copay Exemption Test and Edit a Copay Exemption Test options</td>
<td><mark>redacted</mark></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>8/14/08</td>
<td>Minor Formatting Changes</td>
<td><mark>redacted</mark></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>8/5/15</td>
<td>DG*5.3*890 – Contributed to Spouse and Contributed to Child – Amount Contributed is no longer asked and is replaced with Did you contribute to support Y/N</td>
<td><mark>redacted</mark></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>11/04/2015</td>
<td>TW review: DG_53_P891_KID</td>
<td><mark>redacted</mark></td>
<td><mark>redacted</mark></td>
</tr>
</tbody>
</table>

Overview

The Copay Exemption Test Supervisor menu contains the options used in all aspects of Copay Testing. This includes adding, editing, deleting, viewing past Copay Tests and editing activity, and listing incomplete tests. The following is a brief description of the options contained in this menu.

COPAY EXEMPTION TEST USER MENU

> ADD A COPAY EXEMPTION TEST

> This option allows adding a new Copay Test into the system.

> COPAY EXEMPT TEST NEEDING UPDATE AT NEXT APPT.

> This option is used to generate a listing of future appointments listing Copay Exemption Tests which will require updating.

> EDIT AN EXISTING COPAY EXEMPTION TEST

> This option is used to make changes to data in existing Copay Tests.

> LIST INCOMPLETE COPAY EXEMPTION TEST

> This option is used to generate a listing of patients who have an incomplete Copay Test on file.

> VIEW A PAST COPAY TEST

> This option is used to view past Copay Test data.

DELETE A COPAY EXEMPTION TEST

This option is used to delete individual dates of Copay Tests for a specified patient from the ANNUAL MEANS TEST file (#408.31).

VIEW COPAY EXEMPTION TEST EDITING ACTIVITY

This option provides a method of viewing changes made to Copay Test data.

Copay Exemption Test User MenuAdd a Copay Exemption Test

The Add a Copay Exemption Test option is used to enter a new Copay Test into the system. Only one date of test should exist for a patient annually. The following rules apply to adding a Copay Test.

- date of test cannot be before 10/29/92
- date of test cannot be before the last date of test
- new date of test cannot be added if one exists in the last 365 days unless it is a new calendar year

The Copay Exemption Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. After editing, each screen is refreshed with the new values. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Copay Exemption Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

- Bypasses the copay test screens
- Assigns a Copay Exemption Test status of NON-EXEMPT, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

Copay Exemption Test User MenuAdd a Copay Exemption TestScreen1-MaritalStatus/Dependents is used to enter data on the veteran's spouse and dependent children. Name, social security number, sex, and date of birth must be entered for the veteran's spouse and dependent children if it has not already been filled in through registration. Spouse’s maiden name, address and telephone number may optionally be entered. The total allowed number of dependents is one (1) spouse and nineteen (19) children. Dependent’s (Child’s) address information may be optionally entered as well. This information is extremely important as it is critical in determining the annual income thresholds for the veteran.

The system identifies whether the Spouse and/or Dependent Child(ren) have been marked as included in the Means Test with an (\*) in the column titled “MT”. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an (\*) in the column titled “Address”.

Spouse and dependent children income collection is dependent on several factors. The spouse's income need only be entered if the spouse lived with the veteran last calendar year or, if they did not live together, the veteran contributed to the spouse's support. The amount contributed to child support may be entered if the dependent did not live with the veteran last calendar year and “Yes” is entered for question, “Did you contribute to the child’s support?”. The “If you did not live with child, amount contributed to child last year?” question is no longer asked. Dependent children income is only required if the child had income which was available to the veteran last calendar year. The following is a brief explanation of some of the actions that may be taken.

- DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Copay Test.
- DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be mainly used to delete duplicate dependents. In order to delete a dependent, they must be removed from every Copay Test (using the RE protocol).
- CD - Copy Data can only be used if there is previous year income on file and no income on file for this year.
- ED - Expand Dependent will move to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

Copay Exemption Test User MenuAdd a Copay Exemption TestScreen2-PreviousCalendarYearGrossIncome is used to enter income information such as military retirement, total employment income, and social security. Some fields may be filled in from information collected in registration. Depending on the information entered on Screen 1, this screen may appear with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/ dependents). When the Spouse and/or Dependent Child(ren) have been marked (\*) as being included in the Means Test and the child(ren)’s income has been marked as available to the veteran, the system will display the Spouse and Children columns on the screen. If they have not been marked (no asterisk), they will not display.

> **NOTE:** The same rules apply to the printed 10-10EZ and 10-10EZR forms whereas the system will not print the Previous Calendar Year Gross Annual Income amounts for the Spouse and/or Dependent Child(ren) when they have not been marked with an asterisk as included in the Means Test regardless of whether or not the child(ren)’s income has been marked as available to the veteran.

The required information will be prompted for each column shown. The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three will be displayed.

Screen3-DeductibleExpenses is used to enter any medical, funeral/burial expenses, and children's educational expenses. A child's educational expenses can only be claimed if the child had total employment income.

The Gross Medical Expenses amount is editable for the Means Test originating site. It is Display-Only for all others. When the veteran’s Means Test data has been updated by the HEC Legacy application, the Gross Medical Expenses amount and all Means Test data will be Display-Only for all sites of record. The calculated Adjusted Medical Expenses amount is Display-Only for all sites of record.

For Means Tests done prior to the existence of the Gross Medical Expenses amount, the system will re-calculate and present the Gross Medical Expenses amount from the patient’s existing Medical Expenses amount. For these historical Means Tests, the existing Medical Expenses amount becomes the Adjusted Medical Expenses amount. And, if and when the Gross Medical Expenses amount is updated, the system will automatically re-calculate the Adjusted Medical Expenses amount.

You may choose to print the 10-10EZR form when the Copay Test is completed.

Copay Exemption Test User MenuAdd a Copay Exemption TestNote: To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.

Because the Gross Annual Income (GAI) and Net Worth (NW) money categories in VistA do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA printing software will:

1.  Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar amount in block “*3. LIST OTHER INCOME AMOUNTS (Social Security, compensation, pension, interest, dividends.) EXCLUDING WELFARE.*” of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
- \[1\] Social Security (Not SSI) +
- \[2\] U.S. Civil Service +
- \[3\] U.S. Railroad Retirement +
- \[4\] Military Retirement +
- \[5\] Unemployment Compensation +
- \[6\] Other Retirement +
- \[8\] Interest, Dividend, Annuity +
- \[9\] Worker’s Comp or Black Lung
2.  Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar amount in block “*1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)*” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
- \[1\] Cash, Amts in Bank Accts +
- \[2\] Stocks and Bonds
3.  Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar amount in block “*3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)*” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
- \[4\] Other Property or Assets –
- \[5\] Debts

Access to this option is limited to holders of the DG MEANSTEST security key.

Copay Exemption Test User MenuCopay Exempt Test Needing Update At Next Appt.

The Copay Exempt Test Needing Update At Next Appt. option is used to generate a listing of future appointments for a selected date range. The output will list copay exemption tests that will require updating by that appointment time.

You may select to report one/many/all divisions and one/many/all clinics. The output includes the date range, report run date, clinic name, and division. Patient name, patient ID, appointment date/time, Copay Test status, and date of last Copay Test are provided for each patient listed.

Copay Exemption Test User MenuEdit an Existing Copay Exemption Test

The Edit an Existing Copay Exemption Test option is used to make changes to data in existing Copay Tests. It may also be used to complete Copay Tests on patients. Only the latest Copay Test may be edited.

The Copay Exemption Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. After editing, each screen is refreshed with the new values. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Copay Exemption Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

- Bypasses the copay test screens
- Assigns a Copay Exemption Test status of NON-EXEMPT, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

The Edit a Copay Exemption Test option operates similarly to the Add a Copay Exemption Test option; however, it is the only option that allows changes to completed Copay Tests. After these changes are entered, the system re-determines the patient's Copay status and changes it, if necessary.

The date(s) and name(s) of individual(s) making changes is recorded by the system and may be seen through the View Copay Exemption Test Editing Activity option.

A patient may apply for a Copay Test under the following conditions.

Copay Exemption Test User MenuEdit an Existing Copay Exemption Test

1.  Applicant is a veteran
2.  Applicant's primary or other eligibility does NOT contain:
- service connected 50% to 100% or
- aid and attendance or
- housebound or
- VA pension
3.  Primary eligibility is NSC and a Means Test is not required
4.  Applicants who have answered NO to receiving A&A, HB, or pension
5.  Applicants who have previously qualified and applied for a Copay exemption, still qualify, and have NOT been Copay Tested in the past year

Should these criteria change, a Copay Test status of NO LONGER APPLICABLE will be assigned to the Copay Test. Tests with this status CANNOT be edited.

The following is a brief explanation of some of the actions that may be taken on Screen 1 - Marital Status/Dependents.

- DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Copay Test.
- DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be used to delete duplicate dependents. In order to delete a dependent, they must be removed from every Copay Test (using the RE protocol).
- CD - Copy Data can only be used if there is previous year income on file and no income on file for this year.
- ED - Expand Dependent will move to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

Depending on the information entered on Screen 1, Screen 2 may appear with one column - veteran; two columns - veteran/spouse; or three columns - veteran/spouse/dependents. The required information will be prompted for each column shown. The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three will be displayed.

Copay Exemption Test User MenuEdit an Existing Copay Exemption Test

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

You may print the 10-10EZR form when the Copay Test is complete.

> **NOTE:** To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.

Because the Gross Annual Income (GAI) and Net Worth (NW) money categories in VistA do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA printing software will:

1.  Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar amount in block “*3. LIST OTHER INCOME AMOUNTS (Social Security, compensation, pension, interest, dividends). EXCLUDING WELFARE.*” of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
    - \[1\] Social Security (Not SSI) +
    - \[2\] U.S. Civil Service +
    - \[3\] U.S. Railroad Retirement +
    - \[4\] Military Retirement +
    - \[5\] Unemployment Compensation +
    - \[6\] Other Retirement +
    - \[8\] Interest, Dividend, Annuity +
    - \[9\] Worker’s Comp or Black Lung
4.  Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar amount in block “*1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)*” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
    - \[1\] Cash, Amts in Bank Accts +
    - \[2\] Stocks and Bonds

Copay Exemption Test User MenuEdit an Existing Copay Exemption Test

Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar amount in block “*3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)*” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:

- \[4\] Other Property or Assets
- \[5\] Debts

You may not edit or delete a Copay Exemption Test that was created at another VAMC and distributed by the HEC.

Access to this option is limited to holders of the DG MEANSTEST security key.

Copay Exemption Test User MenuList Incomplete Copay Exemption Test

The List Incomplete Copay Exemption Test option is used to generate a listing of patients who have an incomplete Copay Test on file. The patient name, patient ID number, source of test, and date of test are provided. The patients are listed in alphabetical order on the output.

You will be prompted for the Copay Test status, a date range, and a device.

Copay Exemption Test User MenuView a Past Copay Test

The View a Past Copay Test option is used to view past Copay Tests data. The option does not allow editing. You will be prompted for the patient's name and the date of the Copay Test you wish to view. A question mark (?) entered at the date prompt will provide you with a list of the selected patient's Copay Test dates.

If certain circumstances exist for the selected patient, messages may be displayed. A message will be printed if no detailed income information is on file for the veteran, or if the veteran's Copay Test status is NO LONGER APPLICABLE. Since income data can be entered/edited through registration, once a Copay Test has this status, the income data being viewed may differ from that originally entered as part of the Copay Test.

You will be able to view the following three Copay Test screens through this option.

> Screen 1 - Marital Status/Dependents

> Screen 2 - Previous Calendar Year Gross Income

> Screen 3 - Deductible Expenses

Delete a Copay Exemption Test

The Delete a Copay Exemption Test option is used to delete individual dates of Copay Tests for a specified patient from the ANNUAL MEANS TEST file (#408.31). It can also be used to delete all Copay Tests for a non-veteran patient.

Utilizing this option only deletes the patient's Copay Test status. All information concerning income, assets, debts, spouse, dependent children, etc. is maintained.

You may not edit or delete a Copay Exemption Test that was created at another VAMC and distributed by the HEC.

Only users holding the DG MTDELETE security key may access this option.

View Copay Exemption Test Editing Activity

The View Copay Exemption Test Editing Activity option provides a method of viewing changes made to Copay Test data. The computer keeps track, by patient, each time any change is made to the Copay Test data either through Copay Test or Registration.

The types of changes that are captured are shown below. Both the old and new status value will be shown on the report.

- add new Copay Test
- edit existing Copay Test info
- Copay Test status change

The output generated by this option will include the following information: patient name, Copay Test date, date of change, type of change, and the user who made the change. If no changes have been made to the selected Copay Test, the output will state that fact.

If the selected patient has more than one Copay Test on file, they will be listed for selection.

You must hold the DG MEANSTEST security key to access this option.