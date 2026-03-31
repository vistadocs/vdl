---
title: IB*2 Integrated Billing Version 2 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: archive
pkg_ns: IB
patch_ver: 2
patch_id: IB*2
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 7
description: 
audience: 
keywords: 
  - physician
  - date
  - bill
  - insurance
  - patient
  - billing
  - table
  - charges
  - report
  - contents
page_count: 0
word_count: 91402
section_count: 65
table_count: 45
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: September 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)_Archive/ib_2_0_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)_Archive/ib_2_0_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=266"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Integrated Billing

  Version 2.0

  User Guide
---

![](ib-2-integrated-billing-version-2-user-manual/001.png)

September 2023

Office of Information and Technology

Revision History

Initiated on 12/29/2004.

<table>
<caption><p><span id="_Toc143780832" class="anchor"></span>Table : Common Actions</p></caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 44%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>September 2023</td>
<td>3.31</td>
<td><p>Patch IB*2*752:</p>
<ul>
<li><blockquote>
<p>Removed some reports from the Insurance Reports menu: List Group Plans with No Annual Benefits, Veterans w/Insurance and Inpatient Admissions, and Veterans w/Insurance and Opt. Visits (section 6)</p>
</blockquote></li>
<li><blockquote>
<p>Enhanced prompts and output related to the Insurance Company Link Report (section 6)</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="even">
<td>July 2023</td>
<td>3.30</td>
<td><p>Patch IB*2*747:</p>
<ul>
<li><blockquote>
<p>Removes the Social Security Number from the List Current / Past Held Charges by Pt [IB OUTPUT HELD CHARGES/PT] option.</p>
</blockquote></li>
<li><blockquote>
<p>Removes the Social Security Number from the Patient Billing Clock Inquiry [IB MT CLOCK INQUIRY] option.</p>
</blockquote></li>
<li><blockquote>
<p>Removes the Social Security Number from the Single Patient Means Test Billing Profile [IB MT PROFILE] option.</p>
</blockquote></li>
<li><blockquote>
<p>Removes the Social Security Number from the Estimate Means Test Charges for an Admission [IB MT ESTIMATOR] option.</p>
</blockquote></li>
</ul></td>
<td>CC DSO Development Team</td>
</tr>
<tr class="odd">
<td>March 2023</td>
<td>3.29</td>
<td><p>Patch IB*2*745:</p>
<ul>
<li><blockquote>
<p>Removes SSN display for two options: Third-Party Joint Inquiry and Urgent Care Visit Tracking Inquiry.</p>
</blockquote></li>
<li><blockquote>
<p>Updates the URGENT CARE VISIT MAINTENANCE Option so that Veterans with an Indian Attestation will act like Veterans who are in Priority Groups 1-5, allowing them 3 Free Visits.</p>
</blockquote></li>
</ul></td>
<td>CC DSO Development Team</td>
</tr>
<tr class="even">
<td>February 2023</td>
<td>3.28</td>
<td>Patch IB*2*716: Added the Indian Attestation Copay Exemption Report to the Patient Billing Reports Menu.</td>
<td>CC DSO Development Team</td>
</tr>
<tr class="odd">
<td>October 2022</td>
<td>3.27</td>
<td>Patch IB*2*732 and DG*3.5*1080: Added Vision to list of Coverage Limitations.</td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="even">
<td>September 2022</td>
<td>3.26</td>
<td>Patch IB*2*720: Enhanced the COMPACT Act Copay Review Report – adding Sort by Division feature and Procedure column to output.</td>
<td>CC DSO Development Team</td>
</tr>
<tr class="odd">
<td>August 2022</td>
<td>3.25</td>
<td><p>Patch IB*2*713:</p>
<ul>
<li><blockquote>
<p>Updated Patient Policy Information screen shots to include Expand Benefits.</p>
</blockquote></li>
<li><blockquote>
<p>Added date of death to Patient Insurance Management screens.</p>
</blockquote></li>
<li><blockquote>
<p>Removed List Inactive Ins. Co. Covering Patients.</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="even">
<td>May 2022</td>
<td>3.24</td>
<td><p>Patch IB*2*702:</p>
<ul>
<li><blockquote>
<p>Edited Insurance Reports menu, Insurance Buffer Activity, and Insurance Buffer Employee.</p>
</blockquote></li>
<li><blockquote>
<p>Added Coverage Limitations Report.</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>January 2022</td>
<td>3.23</td>
<td>Patch IB*2*709: Added the COMPACT Act Copay Review Report to the Patient Billing Reports Menu.</td>
<td>CC DSO Development Team</td>
</tr>
<tr class="even">
<td>December 2021</td>
<td>3.22</td>
<td><p>Patch IB*2*687:</p>
<ul>
<li><blockquote>
<p>Edited MCCR Site Parameters screen, Insurance Company Editor screen, Insurance Reports list.</p>
</blockquote></li>
<li><blockquote>
<p>Added Interfacility Ins. Update Report and Insurance Company Link Report, and Payer Link Report.</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>August 2021</td>
<td>3.21</td>
<td>Patch IB*2*701 updates: Enhanced the <u>Former OTH Patient Eligibility Change Report</u> – added MST column to assist billing team with reconciliation processes.</td>
<td>Liberty IT Solutions SHRPE Team</td>
</tr>
<tr class="even">
<td>August 2021</td>
<td>3.20</td>
<td>Patch IB*2.0*676: Added new connectivity in IB RxCopay to Cerner. When Cerner is in Treating Facility List HL7 messages are used for Query, Query Response, sending, receiving new transactions, and the Nightly Jobs.</td>
<td>Cerner Pharmacy CoPay Team</td>
</tr>
<tr class="odd">
<td>April 2021</td>
<td>3.19</td>
<td><p>Patch IB*2.0*688:</p>
<ul>
<li><p>Updated <u>Former OTH Patient Eligibility Change Report</u> and <u>Former OTH Patient Detail Report</u> under Patient Billing Reports Menu to allow the CPAC/Billing user to review Former Service Member's past episodes of care (Outpatient, Inpatient, and Prescriptions) that occurred during pending VBA adjudication period.</p></li>
</ul>
<ul>
<li><blockquote>
<p>Added Presumptive Psychosis Reconciliation Report under [KPA FACILITY REVENUE BILLING] (sub-menu under the CPAC Facility Integrated Billing Menu Option).</p>
</blockquote></li>
</ul></td>
<td>Liberty IT Solutions SHRPE Team</td>
</tr>
<tr class="even">
<td>April 2021</td>
<td>3.18</td>
<td><p>Patch IB*2*668:</p>
<ul>
<li><blockquote>
<p>Edited Insurance Company Editor screens – changes are directly related to the ‘Payer’ section.</p>
</blockquote></li>
<li><blockquote>
<p>Redacted some additional data on a few of the sample screen shots.</p>
</blockquote></li>
</ul></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>December 2020</td>
<td>3.17</td>
<td>Patch IB*2.0*685: Added Former OTH Patient Eligibility Change Report and Former OTH Patient Detail Report to Patient Billing Reports Menu [IB OUTPUT PATIENT REPORT MENU] to allow the CPAC / Billing user to review Former Service Member's past treatments that occurred during pending VBA adjudication (Page 83).</td>
<td>Liberty IT Solutions SHRPE Team</td>
</tr>
<tr class="even">
<td>November 2020</td>
<td>3.16</td>
<td>Patch IB*2*664: Added information regarding the Date of Death report (PDOD) and Source of Information Report (SOUR).</td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>October 2020</td>
<td>3.15</td>
<td>Patch IB*2.0*682: Modifies the Cancel a Charge (CC) action within the IB CANCEL/EDIT/ADD CHARGES option to allow a user to re-bill a previously canceled bill.</td>
<td>CC IBAR Enhancements</td>
</tr>
<tr class="even">
<td>September 2020</td>
<td>3.14</td>
<td><p>Patch IB*2.0*678:</p>
<ul>
<li><blockquote>
<p>Limits the list of Cancellation reasons to display when performing a ?? when canceling an Urgent Care (UC) copay.</p>
</blockquote></li>
<li><blockquote>
<p>Allow users the option to cancel a duplicate medical copayment.</p>
</blockquote></li>
</ul></td>
<td>CC IBAR Enhancements</td>
</tr>
<tr class="odd">
<td>August 2020</td>
<td>3.13</td>
<td><p>Patch IB*2.0*677:</p>
<ul>
<li><blockquote>
<p>Allows the IB CANCEL/EDIT/ADD CHARGES option to properly identify the retroactive award period when determining the Enrollment Priority Group when processing Urgent Care (UC) Copayment Charges.</p>
</blockquote></li>
<li><blockquote>
<p>Changes the IBUC VISIT MAINT options Security Access Key from IB AUTHORIZE to IB EDIT to properly limit the access to the UC Visit Maintenance Utility.</p>
</blockquote></li>
<li><blockquote>
<p>Removes any Urgent Care visits with a REMOVED status from counting towards the total number of UC visits when displaying the total number of UC visits in the IB CANCEL/EDIT/ADD CHARGES Option.</p>
</blockquote></li>
<li><blockquote>
<p>Prevents erroneous <strong>Patient not found at site</strong> error messages from displaying in the IBUC COPAY exceptions report.</p>
</blockquote></li>
<li><blockquote>
<p>Added a new Cancellation Reason, <strong>PANDEMIC RESPONSE</strong> to the IB CHARGE REMOVE REASON FILE (#350.3).</p>
</blockquote></li>
<li><blockquote>
<p>Allows the RELEASE CHARGES <strong>ON HOLD</strong> report to update a UC Visit Charge that was ON HOLD with its Bill Number when releasing multiple charges that are ON HOLD for a single patient.</p>
</blockquote></li>
<li><blockquote>
<p>Allows the IB CANCEL/EDIT/ADD CHARGES Option to link Community Care (CC) Long Term Care (LTC) with a previously filed Patient Treatment File (PTF) so that the CC LTC copay may be charged to the patient correctly.</p>
</blockquote></li>
<li><blockquote>
<p>Modified the text displaying to the user when linking CC LTC Copays to a PTF.</p>
</blockquote></li>
<li><blockquote>
<p>Adds a warning message when a user attempts to access the AC (Add A Charge) Action in the IB CANCEL/EDIT/ADD CHARGES Option and the user does not have the IB EDIT Security Key assigned to them.</p>
</blockquote></li>
</ul></td>
<td>Urgent Care / COVID IBAR Enhancements</td>
</tr>
<tr class="even">
<td>June 2020</td>
<td>3.12</td>
<td><p>Patch IB*2.0*675:</p>
<ul>
<li><blockquote>
<p>Updates to prevent the error currently occurring at UPDUCDB+2^IBRREL when running the RELEASE CHARGES 'ON HOLD' report [IB MT RELEASE CHARGES].</p>
</blockquote></li>
<li><blockquote>
<p>Updated IBUC VISIT MAINT option to allow Facility Revenue Managers to enter Free Urgent Care Visits for a Veteran if the Veterans Urgent Care visit occurred between the day an Enrollment Group change was awarded, and the Date the Enrollment Change is considered effective.</p>
</blockquote></li>
</ul></td>
<td>Urgent Care IBAR Enhancements</td>
</tr>
<tr class="odd">
<td>May 2020</td>
<td>3.11</td>
<td><p>Patch IB*2.0*674:</p>
<ul>
<li><blockquote>
<p>Updates the IBUC URGENT CARE EXCEPTIONS Mail Group from Private to public so that the mail group members will receive the emails sent to this group.</p>
</blockquote></li>
<li><blockquote>
<p>Updates the IBUC ELIG GROUP Function so that it correctly identifies a patient's Enrollment Group so that the patient Urgent Care Visit data at other facilities the patient is enrolled at will update correctly.</p>
</blockquote></li>
<li><blockquote>
<p>Modifies the IBUC MULTI FAC COPAY SYNCH nightly process option to assign a user to the Option so that the task will correctly file patient Urgent Care Visit updates at remote facilities.</p>
</blockquote></li>
</ul></td>
<td>Urgent Care IBAR Enhancements</td>
</tr>
<tr class="even">
<td>May 2020</td>
<td>3.10</td>
<td><p>Patch IB*2.0*669:</p>
<ul>
<li><blockquote>
<p>Updated LIST ALL BILLS FOR A PATIENT to allow the user to filter out either Third-Party insurance bills or First Party Copays if they wish to.</p>
</blockquote></li>
<li><blockquote>
<p>Updated LIST ALL BILLS FOR A PATIENT to allow the user to limit the amount of data on the report to a user-defined range of dates.</p>
</blockquote></li>
<li><blockquote>
<p>Updated LIST ALL BILLS FOR A PATIENT to allow the output of the report to be in a delimited format for import into a spreadsheet.</p>
</blockquote></li>
<li><blockquote>
<p>Updated IB CANCEL/EDIT/ADD CHARGES to allow certain existing Cancellations Reasons to cancel CC URGENT CARE Copay charges.</p>
</blockquote></li>
<li><blockquote>
<p>Inactivated the UC - ENTERED IN ERROR and UC - CHANGE IN ELIGIBILITY Cancellation Reasons and adds the UC - PG6 REVIEWED in the IB CHARGE REMOVE REASON file (#350.3).</p>
</blockquote></li>
<li><blockquote>
<p>Updated the IB CANCEL/EDIT/ADD CHARGES to allow only holders of the IB EDIT Security Key access to the AC (Add Charges) function.</p>
</blockquote></li>
</ul></td>
<td>Urgent Care IBAR Enhancements</td>
</tr>
<tr class="odd">
<td>March 2020</td>
<td>3.9</td>
<td><p>Patch IB*2.0*671:</p>
<ul>
<li><blockquote>
<p>Updated Cancel / Edit / Add to use the Veteran PG status in effect on the Date of Service.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Cancel / Edit / Add to check for duplicates for outpatient copayments and ask if the copayment should be added.</p>
</blockquote></li>
<li><blockquote>
<p>Allows users to manually request an update for UC visits.</p>
</blockquote></li>
<li><blockquote>
<p>Added <strong>Visit Only</strong> as an option for UC visit tracking.</p>
</blockquote></li>
<li><blockquote>
<p>Updated the landing page for the UC Visit Maintenance screen.</p>
</blockquote></li>
<li><blockquote>
<p>Updated the UC Visit Tracking Detail Report to display in alphabetical order.</p>
</blockquote></li>
</ul></td>
<td>Urgent Care IBAR Enhancements</td>
</tr>
<tr class="even">
<td>March 2020</td>
<td>3.8</td>
<td><p>Patch IB*2.0*663:</p>
<ul>
<li><blockquote>
<p>Created Urgent Care visit tracking functionality and reporting.</p>
</blockquote></li>
<li><blockquote>
<p>Allows users to add / edit / review UC visits for individual patients.</p>
</blockquote></li>
<li><blockquote>
<p>Provides facility-level reports for UC.</p>
</blockquote></li>
<li><blockquote>
<p>Added instructions and screen shots for Urgent Care.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Cancel / Edit / Add Charges to prevent duplicate copayments for inpatient Per Diem and inpatient, and outpatient Long Term Care (LTC) copayments.</p>
</blockquote></li>
<li><blockquote>
<p>Updated the Third-Party Follow-Up report to correctly report Community Care.</p>
</blockquote></li>
</ul></td>
<td>Urgent Care IBAR Enhancements</td>
</tr>
<tr class="odd">
<td>January 2020</td>
<td>3.7</td>
<td>Patch IB*2.0*656: Updated Single Patient Means Test Billing Profile screen shots.</td>
<td>Urgent Care IBAR Enhancements</td>
</tr>
<tr class="even">
<td>December 2019</td>
<td>3.6</td>
<td>Patch IB*2.0*652 updates: Additional NP action for Add Group Plan.</td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>December 2019</td>
<td>3.5</td>
<td>Patch IB*2.0*627: Updated the following pages to reflect the Medal of Honor change and displays: Page 2, 32-33, 55, 58, 163, 165, 170, and 174</td>
<td>EPMO TW</td>
</tr>
<tr class="even">
<td>October 2019</td>
<td>3.4</td>
<td>Patch IB*2.0*631: Added Delete option to CV Coverage Limitations</td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>September 2019</td>
<td>3.3</td>
<td><p>Patch IB*2.0*618:</p>
<ul>
<li><blockquote>
<p>VistA – Integrated Billing to allow new action types, rate types, and AR categories to be mapped to Revenue Source Codes (RSC) and be externally reported within FMS systems using the RSC.</p>
</blockquote></li>
<li><blockquote>
<p>Added VA Mission Act 2018 information to the Release of Information Report section.</p>
</blockquote></li>
</ul></td>
<td>Community Care Integrated Billing and Accounts Receivables Enhancements</td>
</tr>
<tr class="even">
<td>July 2019</td>
<td>3.2</td>
<td>Patch IB*2.0*624: Updated Release of Information Report criteria.</td>
<td>ePharmacy Development Team</td>
</tr>
<tr class="odd">
<td>March 2019</td>
<td>3.15</td>
<td>Patch IB*2.0*602: Added menu option Expire Group Plan in Patient Insurance Menu section, including description and screen and prompt samples.</td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="even">
<td>October 2018</td>
<td>3.1</td>
<td><p>Patch IB*2.0*614:</p>
<ul>
<li><blockquote>
<p>Added information regarding adding / deleting charges for patients with a Category 1 High Risk for Suicide Patient Record Flag using the Cancel / Edit / Add Patient Charges option, p. 33 – 34.</p>
</blockquote></li>
<li><blockquote>
<p>Added IB MEANS TEST mail group, p. 282.</p>
</blockquote></li>
</ul></td>
<td>Suicide High-Risk Patient Enhancements Team</td>
</tr>
<tr class="odd">
<td>May 2018</td>
<td>3.0</td>
<td>Patch IB*2.0*568: Updated Third-Party Joint Inquiry sample screen shots – Type column for active and inactive bills.</td>
<td>FY 16 Revenue Enhancements</td>
</tr>
<tr class="even">
<td>August 2016</td>
<td>2.9</td>
<td><p>Patch IB*2.0*549:</p>
<ul>
<li><blockquote>
<p>Updated Patient Policy Information screen shots.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Patient Insurance Menu section.</p>
</blockquote></li>
<li><blockquote>
<p>Updated the List Plans by Insurance Company Report screen.</p>
</blockquote></li>
<li><blockquote>
<p>Added Insurance Plans Missing Data Report.</p>
</blockquote></li>
<li><blockquote>
<p>Updated MCCR Site Parameter Display/Edit section.</p>
</blockquote></li>
<li><blockquote>
<p>Updated MCCR Site Parameter Screen section.</p>
</blockquote></li>
</ul></td>
<td>FY15 eInsurance Development Team</td>
</tr>
<tr class="odd">
<td>August 2016</td>
<td>2.8</td>
<td><ul>
<li><blockquote>
<p>Updated Introduction to reference new Claims Tracking User Guide.</p>
</blockquote></li>
<li><blockquote>
<p>Removed reference to Claim Tracking on p. 4.</p>
</blockquote></li>
</ul>
<p>Moved Sections below to a separate Claims Tracking User Guide:</p>
<ul>
<li><blockquote>
<p>Claims Tracking Master Menu.</p>
</blockquote></li>
<li><blockquote>
<p>Supervisors Menu (Claims Tracking).</p>
</blockquote></li>
<li><blockquote>
<p>Reports Menu (Claims Tracking).</p>
</blockquote></li>
</ul></td>
<td>Harris Team</td>
</tr>
<tr class="even">
<td>August 2016</td>
<td>2.7</td>
<td><p>Patch IB*2*0*550:</p>
<ul>
<li><blockquote>
<p>Updated Title Page to current OI&amp;T Standards.</p>
</blockquote></li>
<li><blockquote>
<p>Added description for Release of Information Report</p>
</blockquote></li>
</ul></td>
<td>Harris Team</td>
</tr>
<tr class="odd">
<td>August 2016</td>
<td>2.6</td>
<td>Updated for patch IB*2.0*562: Added new option IB MT FIX/DISCH SPECIAL CASE p. 47.</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>June 2016</td>
<td>2.5</td>
<td><p>Comprehensive Updates for IB *2.0*529 and IB*2.0*530:</p>
<ul>
<li><blockquote>
<p>Updated title page and footers.</p>
</blockquote></li>
<li><blockquote>
<p>Updated screen options p.24 – 27.</p>
</blockquote></li>
<li><blockquote>
<p>Added Reject Indicator p. 60.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Insurance Payment Trend Report p. 146-147.</p>
</blockquote></li>
</ul></td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>February 2016</td>
<td>2.4</td>
<td><p>Patch IB*2.0*525 and IB*2.0*528 updates:</p>
<ul>
<li><blockquote>
<p>Updated Patient to Subscriber.</p>
</blockquote></li>
<li><blockquote>
<p>Added section on Manually Added HPIDs to Billing Claim Report to Patient Billing Reports Menu.</p>
</blockquote></li>
<li><blockquote>
<p>Added material on viewing Patient Policy comments from Claims Tracking edit option.</p>
</blockquote></li>
</ul></td>
<td>FY14 eInsurance Development Team</td>
</tr>
<tr class="even">
<td>September 2015</td>
<td>2.3</td>
<td><p>Updates for IB*2.0*522, ICD-10 Patient Treatment File (PTF) Modifications:</p>
<ul>
<li><blockquote>
<p>Updated title page and footers.</p>
</blockquote></li>
<li><blockquote>
<p>Reformatted Revision History.</p>
</blockquote></li>
<li><blockquote>
<p>Added text describing patch changes to Enter / Edit Billing Information on p.45.</p>
</blockquote></li>
</ul></td>
<td>VA OIT Product Development, ICD-10 PTF Modifications Team</td>
</tr>
<tr class="odd">
<td>January 2015</td>
<td>2.2</td>
<td><p>Patch IB*2.0*521:</p>
<ul>
<li><blockquote>
<p>Updated cover page.</p>
</blockquote></li>
<li><blockquote>
<p>Updated footer dates.</p>
</blockquote></li>
<li><blockquote>
<p>Updated screenshots on pages 34 and 296 for addition of HPID / OEID in TPJI.</p>
</blockquote></li>
</ul></td>
<td><p>Redacted</p>
<p>FirstView Team</p></td>
</tr>
<tr class="even">
<td>November 2014</td>
<td>2.1</td>
<td><p>Patch IB*2.0*519:</p>
<ul>
<li><blockquote>
<p>Modified footer.</p>
</blockquote></li>
<li><blockquote>
<p>Updated screens for ‘Insurance Company Editor’ screens.</p>
</blockquote></li>
</ul></td>
<td><p>Redacted</p>
<p>FirstView Team</p></td>
</tr>
<tr class="odd">
<td>September 2014</td>
<td>2.0</td>
<td><p>Patch IB*2.0*461.</p>
<ul>
<li><blockquote>
<p>Changed all references to ICD-9 to generic ICD: p. 15, 116, 117, 122, 155.</p>
</blockquote></li>
<li><blockquote>
<p>Added ICD-10 text to Glossary: p. 334.</p>
</blockquote></li>
</ul></td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>3/5/2014</td>
<td>1.9</td>
<td><p>Patch IB*2.0*385: Updated and highlighted the following options under the Medication Copayment Income Exemption Menu to include changes implemented by the Veterans’ Financial Assessment Project implemented with IB*2.0*385.</p>
<ul>
<li><blockquote>
<p>Letters to Exempt Patients</p>
</blockquote></li>
<li><blockquote>
<p>Reprint Single Income Test Reminder Letter</p>
</blockquote></li>
</ul></td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>1/27/2014</td>
<td>1.8</td>
<td><p>Patch IB*2.0*497:</p>
<ul>
<li><blockquote>
<p>Updated cover page.</p>
</blockquote></li>
<li><blockquote>
<p>Updated footer dates.</p>
</blockquote></li>
<li><blockquote>
<p>Replaced screenshots where screens went from double column to single column to accommodate longer fields.</p>
</blockquote></li>
</ul></td>
<td><p>Redacted</p>
<p>FirstView Team</p></td>
</tr>
<tr class="even">
<td>3/26/2013</td>
<td>1.7</td>
<td><p>Document formatting revisions:</p>
<ul>
<li><blockquote>
<p>Updated cover page.</p>
</blockquote></li>
<li><blockquote>
<p>Added blank pages and noted pages left intentionally blank: p. iv, 6, 8, 10, 12, 52, 78, 132, 138, 218, 292, and 308.</p>
</blockquote></li>
<li><blockquote>
<p>Removed extra blank pages.</p>
</blockquote></li>
<li><blockquote>
<p>Corrected heading styles and updated Table of Contents.</p>
</blockquote></li>
<li><blockquote>
<p>Added <strong>Sample Screens</strong> label to p. 187 and <strong>Sample Output</strong> label to p. 200.</p>
</blockquote></li>
<li><blockquote>
<p>Rearranged options in the IRM System Manager’s Integrated Billing Menu section to better reflect actual menu layout in Table of Contents. Options were moved up to p. 298-307.</p>
</blockquote></li>
</ul></td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>3/26/2013</td>
<td>1.6</td>
<td><p>Updated for patch IB*2.0*458:</p>
<ul>
<li><blockquote>
<p>Added new ROI Consent option to Claims Tracking Editor screen on p. 17, 21, and 22.</p>
</blockquote></li>
<li><blockquote>
<p>Added new ROI Special Consent screen to p. 20 and 22.</p>
</blockquote></li>
<li><blockquote>
<p>Reformatted bulleted lists and added note about additional review types on p.18, 115, and 120.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Days Denied Report description and sample output on p. 142-143.</p>
</blockquote></li>
<li><blockquote>
<p>Added new ROI Expired Consent Report to p. 217.</p>
</blockquote></li>
<li><blockquote>
<p>Added new RC Change Facility Type option to Charge Master IRM Menu on p. 317.</p>
</blockquote></li>
</ul></td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>3/26/2013</td>
<td>1.5</td>
<td>Updated for patch IB*2.0*474. Changed last sentence under <strong>Rate Schedule Adjustment Enter/Edit</strong> option on p.317.</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>8/17/2011</td>
<td>1.4</td>
<td>Updated for patch IB*2.0*449. Technical writer review—format and convert to Section 508 compliant PDF.</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>10/16/2007</td>
<td>1.3</td>
<td>Updated for patch IB*2*303.</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>5/27/2005</td>
<td>1.2</td>
<td>Re-paged for clarity.</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>12/29/2004</td>
<td>1.1</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>12/29/2004</td>
<td>1.0</td>
<td>PDF file checked for accessibility to readers with disabilities.</td>
<td>Redacted</td>
</tr>
</tbody>
</table>

<span id="_Toc143780832" class="anchor"></span>Table : Common Actions

Preface

This is the user manual for the Integrated Billing (IB) software package.

This manual is designed to provide guidance to a broad range of users within Department of Veterans Affairs (VA) medical facilities in daily usage of the Integrated Billing software.

Related Manuals

| Reference                                                                                         | Location                                               |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| IB\*2 Electronic Insurance Verification (eIV) and Interfacility Insurance Update (IIU) User Guide | [VDL](https://www.va.gov/vdl/application.asp?appid=45) |
| IB\*2 EDI User Guide                                                                              | [VDL](https://www.va.gov/vdl/application.asp?appid=45) |

<span id="_Toc143780833" class="anchor"></span>Table : Common Actions

Table of Contents

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Patient Billing](#patient-billing)
  - [Third-Party Billing](#third-party-billing)
  - [Insurance Data Capture](#insurance-data-capture)
  - [Additional Functionality](#additional-functionality)
- [Orientation](#orientation)
- [Package Management](#package-management)
- [Package Operation](#package-operation)
- [Billing Clerk’s Menu](#billing-clerks-menu)
  - [Third-Party Joint Inquiry (TPJI)](#third-party-joint-inquiry-tpji)
  - [Third-Party Active Bills Screen](#third-party-active-bills-screen)
  - [Inactive Bills Screen](#inactive-bills-screen)
  - [Patient Insurance Screen](#patient-insurance-screen)
  - [Claim Information Screen](#claim-information-screen)
  - [Bill Charges Screen](#bill-charges-screen)
  - [Bill Diagnosis Screen](#bill-diagnosis-screen)
  - [Bill Procedures Screen](#bill-procedures-screen)
  - [AR Account Profile Screen](#ar-account-profile-screen)
  - [AR Transaction Profile Screen](#ar-transaction-profile-screen)
  - [AR Comment History Screen](#ar-comment-history-screen)
  - [Insurance Reviews / Contacts Screen](#insurance-reviews-contacts-screen)
  - [Expanded Appeals / Denials Screen](#expanded-appeals-denials-screen)
  - [Expanded Insurance Reviews Screen](#expanded-insurance-reviews-screen)
  - [Insurance Company Screen](#insurance-company-screen)
  - [Patient Policy Information Screen](#patient-policy-information-screen)
  - [Annual Benefits Screen](#annual-benefits-screen)
  - [Patient Eligibility Screen](#patient-eligibility-screen)
  - [Enter / Edit Billing Information](#enter-edit-billing-information)
  - [Automated Means Test Billing Menu](#automated-means-test-billing-menu)
    - [Cancel / Edit / Add Patient Charges](#cancel-edit-add-patient-charges)
    - [Adding Prescription Copay Charges for Patients with a National Category 1 Patient Record Flag](#adding-prescription-copay-charges-for-patients-with-a-national-category-1-patient-record-flag)
    - [Canceling Copay Charges for Patients with an Urgent Care Visit](#canceling-copay-charges-for-patients-with-an-urgent-care-visit)
    - [Patient Billing Clock Maintenance](#patient-billing-clock-maintenance)
    - [Estimate Means Test Charges for an Admission](#estimate-means-test-charges-for-an-admission)
  - [Urgent Care Visit Tracking Menu](#urgent-care-visit-tracking-menu)
    - [Urgent Care Visit Tracking Maintenance](#urgent-care-visit-tracking-maintenance)
    - [Urgent Care Visit Tracking Inquiry](#urgent-care-visit-tracking-inquiry)
    - [Urgent Care Visit Summary / Detail Report](#urgent-care-visit-summary-detail-report)
    - [Urgent Care Pull Request by Patient](#urgent-care-pull-request-by-patient)
  - [On Hold Menu](#on-hold-menu)
    - [On Hold Charges Released to AR](#on-hold-charges-released-to-ar)
    - [Count / Dollar Amount of Charges on Hold](#count-dollar-amount-of-charges-on-hold)
    - [Days on Hold Report](#days-on-hold-report)
  - [Held Charges Report](#held-charges-report)
    - [History of Held Charges](#history-of-held-charges)
    - [Release Charges 'On Hold'](#release-charges-on-hold)
    - [List Charges Awaiting New Copay Rate](#list-charges-awaiting-new-copay-rate)
    - [Send Converted Charges to A/R](#send-converted-charges-to-ar)
    - [Release Charges 'Pending Review'](#release-charges-pending-review)
    - [List Current / Past Held Charges by Pt](#list-current-past-held-charges-by-pt)
    - [Release Charges Awaiting New Copay Rate](#release-charges-awaiting-new-copay-rate)
    - [Patient Billing Clock Inquiry](#patient-billing-clock-inquiry)
    - [Category C Billing Activity List](#category-c-billing-activity-list)
    - [Single Patient Means Test Billing Profile](#single-patient-means-test-billing-profile)
    - [Disposition Special Inpatient Billing Cases](#disposition-special-inpatient-billing-cases)
    - [List Special Inpatient Billing Cases](#list-special-inpatient-billing-cases)
  - [CHAMPUS Billing Menu](#champus-billing-menu)
    - [Delete Reject Entry](#delete-reject-entry)
    - [Reject Report](#reject-report)
    - [Resubmit a Claim](#resubmit-a-claim)
    - [Reverse a Claim](#reverse-a-claim)
    - [Transmission Report](#transmission-report)
    - [IB MT FIX / DISCH Special Case](#ib-mt-fix-disch-special-case)
  - [Patient Billing Reports Menu](#patient-billing-reports-menu)
    - [Catastrophically Disabled Copay Report](#catastrophically-disabled-copay-report)
    - [COMPACT Act Copay Review Report](#compact-act-copay-review-report)
    - [Patient Currently Cont. Hospitalized since 1986](#patient-currently-cont-hospitalized-since-1986)
    - [Print IB Actions by Date](#print-ib-actions-by-date)
    - [Employer Report](#employer-report)
    - [Episode of Care Bill List](#episode-of-care-bill-list)
    - [Estimate Means Test Charges for an Admission](#estimate-means-test-charges-for-an-admission-1)
    - [Outpatient / Registration Events Report](#outpatient-registration-events-report)
    - [Held Charges Report](#held-charges-report-1)
    - [Manually Added HPIDs to Billing Claim Report](#manually-added-hpids-to-billing-claim-report)
    - [Indian Attestation Copay Exemption Report](#indian-attestation-copay-exemption-report)
    - [### Patient Billing Inquiry](#patient-billing-inquiry)
    - [List all Bills for a Patient](#list-all-bills-for-a-patient)
    - [Category C Billing Activity List](#category-c-billing-activity-list-1)
    - [Former OTH Patient Eligibility Change Report](#former-oth-patient-eligibility-change-report)
    - [Former OTH Patient Detail Report](#former-oth-patient-detail-report)
  - [Third-Party Output Menu](#third-party-output-menu)
    - [Veterans w/Insurance and Discharges](#veterans-winsurance-and-discharges)
    - [Veteran Patient Insurance Information](#veteran-patient-insurance-information)
    - [Veterans w/ Insurance and Inpatient Admissions](#veterans-w-insurance-and-inpatient-admissions)
    - [Veterans w/Insurance and Opt. Visits](#veterans-winsurance-and-opt-visits)
    - [Patient Review Document](#patient-review-document)
    - [Inpatients w/ Unknown or Expired Insurance](#inpatients-w-unknown-or-expired-insurance)
    - [Outpatients w/Unknown or Expired Insurance](#outpatients-wunknown-or-expired-insurance)
    - [Single Patient Means Test Billing Profile](#single-patient-means-test-billing-profile-1)
  - [Third-Party Billing Menu](#third-party-billing-menu)
    - [Print Bill Addendum Sheet](#print-bill-addendum-sheet)
    - [Authorize Bill Generation](#authorize-bill-generation)
    - [Enter / Edit Billing Information](#enter-edit-billing-information-1)
    - [Cancel Bill](#cancel-bill)
    - [Copy and Cancel](#copy-and-cancel)
    - [Delete Auto Biller Results](#delete-auto-biller-results)
    - [Print Bill](#print-bill)
    - [Patient Billing Inquiry](#patient-billing-inquiry-1)
    - [Print Auto Biller Results](#print-auto-biller-results)
    - [Print Authorized Bills](#print-authorized-bills)
  - [Return Bill Menu](#return-bill-menu)
    - [Edit Returned Bill](#edit-returned-bill)
    - [Returned Bill List](#returned-bill-list)
    - [Return Bill to A/R](#return-bill-to-ar)
    - [UB-82 Test Pattern Print](#ub-82-test-pattern-print)
    - [UB-92 Test Pattern Print](#ub-92-test-pattern-print)
    - [HCFA-1500 Test Pattern Print](#hcfa-1500-test-pattern-print)
    - [Outpatient Visit Date Inquiry](#outpatient-visit-date-inquiry)
- [Patient Insurance Menu](#patient-insurance-menu)
  - [Patient Insurance Info View / Edit](#patient-insurance-info-view-edit)
  - [Patient Insurance Management Screen](#patient-insurance-management-screen)
  - [Patient Policy Information Screen](#patient-policy-information-screen-1)
  - [Annual Benefits Editor Screen](#annual-benefits-editor-screen)
    - [Benefits Used by Date Editor Screen](#benefits-used-by-date-editor-screen)
  - [View Patient Insurance](#view-patient-insurance)
  - [Patient Insurance Management Screen](#patient-insurance-management-screen-1)
  - [Patient Policy Information Screen](#patient-policy-information-screen-2)
  - [Annual Benefits Editor Screen](#annual-benefits-editor-screen-1)
  - [Benefits Used By Date Editor Screen](#benefits-used-by-date-editor-screen-1)
  - [Insurance Company Entry / Edit](#insurance-company-entry-edit)
  - [Insurance Company Editor Screen](#insurance-company-editor-screen)
  - [Insurance Plan List Screen](#insurance-plan-list-screen)
  - [Annual Benefits Editor Screen](#annual-benefits-editor-screen-2)
  - [View / Edit Plan Screen](#view-edit-plan-screen)
  - [View Insurance Company](#view-insurance-company)
  - [Insurance Company Editor Screen](#insurance-company-editor-screen-1)
  - [Process Insurance Buffer](#process-insurance-buffer)
  - [Insurance Buffer List Screen](#insurance-buffer-list-screen)
  - [Insurance Buffer Process Screen](#insurance-buffer-process-screen)
  - [Insurance Buffer Entry Screen](#insurance-buffer-entry-screen)
  - [Manually Added HPIDs to Billing Claim Report](#manually-added-hpids-to-billing-claim-report-1)
  - [Expire Group Plan (XPIR)](#expire-group-plan-xpir)
  - [Release of Information Report](#release-of-information-report)
  - [Insurance Reports Menu](#insurance-reports-menu)
    - [List Plans by Insurance Company](#list-plans-by-insurance-company)
    - [List New not Verified Policies](#list-new-not-verified-policies)
    - [Insurance Plans Missing Data Report](#insurance-plans-missing-data-report)
    - [eIV Payer Date of Death Report](#eiv-payer-date-of-death-report)
    - [Source of Information Report](#source-of-information-report)
    - [Interfacility Ins. Update Report](#interfacility-ins-update-report)
    - [Ins Company Link Report (aka “Insurance Company Link Report”)](#ins-company-link-report-aka-insurance-company-link-report)
    - [Payer Link Report](#payer-link-report)
    - [Coverage Limitations Report](#coverage-limitations-report)
- [Billing Supervisor Menu](#billing-supervisor-menu)
  - [Insurance Buffer Activity](#insurance-buffer-activity)
  - [Management Reports (Billing) Menu](#management-reports-billing-menu)
    - [Statistical Report (IB)](#statistical-report-ib)
    - [Most used Outpatient CPT Codes](#most-used-outpatient-cpt-codes)
    - [Insurance Buffer Employee](#insurance-buffer-employee)
    - [New Companies (0%), 0 New Group/Plans (0%), 1 New Patient Policy (20%) Clerk Productivity](#new-companies-0-0-new-groupplans-0-1-new-patient-policy-20-clerk-productivity)
    - [Rank Insurance Carriers By Amount Billed](#rank-insurance-carriers-by-amount-billed)
    - [Billing Rates List](#billing-rates-list)
    - [Revenue Code Totals by Rate Type](#revenue-code-totals-by-rate-type)
    - [Bill Status Report](#bill-status-report)
    - [Rate Type Billing Totals Report](#rate-type-billing-totals-report)
    - [Insurance Payment Trend Report](#insurance-payment-trend-report)
    - [Unbilled BASC for Insured Patient Appointments](#unbilled-basc-for-insured-patient-appointments)
    - [ROI Expired Consent](#roi-expired-consent)
  - [Medication Copayment Income Exemption Menu](#medication-copayment-income-exemption-menu)
    - [Print Charges Canceled Due to Income Exemption](#print-charges-canceled-due-to-income-exemption)
    - [Edit Copay Exemption Letter](#edit-copay-exemption-letter)
    - [Inquire to Medication Copay Income Exemptions](#inquire-to-medication-copay-income-exemptions)
    - [Manually Change Copay Exemption (Hardships)](#manually-change-copay-exemption-hardships)
    - [Letters to Exempt Patients](#letters-to-exempt-patients)
    - [List Income Thresholds](#list-income-thresholds)
    - [Print Patient Exemptions or Summary](#print-patient-exemptions-or-summary)
    - [Reprint Single Income Test Reminder Letter](#reprint-single-income-test-reminder-letter)
    - [Add Income Thresholds](#add-income-thresholds)
    - [Print / Verify Patient Exemption Status](#print-verify-patient-exemption-status)
  - [MCCR System Definition Menu](#mccr-system-definition-menu)
    - [Enter / Edit Automated Billing Parameters](#enter-edit-automated-billing-parameters)
  - [Charge Master Menu](#charge-master-menu)
    - [Enter / Edit Charge Master](#enter-edit-charge-master)
    - [Print Charge Master](#print-charge-master)
    - [Activate Revenue Codes](#activate-revenue-codes)
    - [Enter / Edit Billing Rates](#enter-edit-billing-rates)
    - [Flag Stop Codes / Dispositions / Clinics](#flag-stop-codes-dispositions-clinics)
    - [Flag Stop Codes / Clinics for Third-Party](#flag-stop-codes-clinics-for-third-party)
    - [Insurance Company Entry / Edit](#insurance-company-entry-edit-1)
    - [List Flagged Stop Codes / Dispositions / Clinics](#list-flagged-stop-codes-dispositions-clinics)
    - [Billing Rates List](#billing-rates-list-1)
    - [MCCR Site Parameter Enter / Edit](#mccr-site-parameter-enter-edit)
    - [Purge Insurance Buffer](#purge-insurance-buffer)
    - [MCCR Site Parameter Display / Edit](#mccr-site-parameter-display-edit)
    - [Re-Generate Unbilled Amounts Report](#re-generate-unbilled-amounts-report)
    - [Send Test Unbilled Amounts Bulletin](#send-test-unbilled-amounts-bulletin)
    - [View Unbilled Amounts](#view-unbilled-amounts)
    - [Third-Party Joint Inquiry](#third-party-joint-inquiry)
    - [Fast Enter of New Billing Rates](#fast-enter-of-new-billing-rates)
    - [Delete Charges from the Charge Master](#delete-charges-from-the-charge-master)
    - [Inactivate / List Inactive Codes in Charge Master](#inactivate-list-inactive-codes-in-charge-master)
- [IRM System Manager's Integrated Billing Menu](#irm-system-managers-integrated-billing-menu)
  - [Purge Functionality](#purge-functionality)
    - [Select Default Device for Forms](#select-default-device-for-forms)
    - [Display Integrated Billing Status](#display-integrated-billing-status)
    - [Enter / Edit IB Site Parameters](#enter-edit-ib-site-parameters)
    - [Inquire an IB Action](#inquire-an-ib-action)
    - [Patient IB Action Inquiry](#patient-ib-action-inquiry)
    - [Repost IB Action to Filer](#repost-ib-action-to-filer)
    - [Start the Integrated Billing Background Filer](#start-the-integrated-billing-background-filer)
    - [Stop the Integrated Billing Background Filer](#stop-the-integrated-billing-background-filer)
    - [Verify RX Co-Pay Links](#verify-rx-co-pay-links)
    - [Forms Output Utility](#forms-output-utility)
  - [Purge Menu](#purge-menu)
    - [Purge Update File](#purge-update-file)
    - [Archive Billing Data](#archive-billing-data)
    - [Archive / Purge Log Inquiry](#archive-purge-log-inquiry)
    - [Delete Entry from Search Template](#delete-entry-from-search-template)
    - [Find Billing Data to Archive](#find-billing-data-to-archive)
    - [List Archive / Purge Log Entries](#list-archive-purge-log-entries)
    - [List Search Template Entries](#list-search-template-entries)
    - [Purge Billing Data](#purge-billing-data)
  - [Charge Master IRM Menu](#charge-master-irm-menu)
    - [Load Host File into Charge Master](#load-host-file-into-charge-master)
    - [Rate Schedule Adjustment Enter / Edit](#rate-schedule-adjustment-enter-edit)
    - [RC Change Facility Type](#rc-change-facility-type)
    - [Start the CHAMPUS Rx Billing Engine](#start-the-champus-rx-billing-engine)
    - [Stop the CHAMPUS Rx Billing Engine](#stop-the-champus-rx-billing-engine)
    - [Edit the CIDC Insurance Switch](#edit-the-cidc-insurance-switch)
- [APPENDIX A – Acronyms and Abbreviations](#appendix-a-acronyms-and-abbreviations)
- [APPENDIX B – Military Time Conversion Table](#appendix-b-military-time-conversion-table)
- [APPENDIX C – List Manager Appendix](#appendix-c-list-manager-appendix)
The release of Integrated Billing (IB) version 2.0 introduces fundamental changes to the way Medical Care Cost Recovery (MCCR) related tasks are done. This software introduces three new modules:
1.  Claims Tracking
2.  Encounter Form Utilities
3.  Insurance Data Capture
There are also significant enhancements to the previous modules, Patient Billing and Third-Party Billing. IB has moved from a package with the singular purpose of identifying billable episodes of care and creating bills to a package responsible for the whole billing process through to the passing of charges to Accounts Receivable (AR). Functionality has been added to assist in capturing patient data, tracking potentially billable episodes of care, completing Utilization Review (UR) tasks, and capturing more complete insurance information.
This version of IB targets a much wider audience than previous versions.
- The Encounter Form Utilities module is used by Medical Administration Service (MAS) Automated Data Processing Applications Coordinators (ADPAC)s or clinic supervisors to create and print clinic-specific forms. Physicians use the forms and consequently provide input into form creation.
- A separate Claims Tracking User Manual has been created and Claim Tracking module information can be located in that document. UR nurses can utilize this new User Guide within MCCR and Quality Management (QM) to track episodes of care, do pre-certifications, do continued stay reviews, and complete other UR tasks.
- Insurance verifiers use the Insurance Data Capture module to collect and store patient and insurance carrier-specific data.
- Billing Clerks will see substantial changes with the enhancements provided in the Patient Billing and Third-Party Billing modules.
The following is an overview of the major functions of the Integrated Billing software, excluding the Encounter Form functionality. That information can be found in the IB User Manual, Encounter Form Utilities Module.

## Patient Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Updates the Cancel/Edit/Add option to identify retroactive award periods when determining the Enrollment Priority Group for Urgent Care (UC) charges, links Community Care (CC) Long Term Care (LTC) charges to filed Patient Treatment File (PTF) entries, updates the language to reflect PTF entries vice inpatient periods and adds a warning message when users do not have the correct security key assigned. Changed the IBUC VISIT MAINT option to utilize the IB EDIT security key for access. Added a new Cancellation Reason of PANDEMIC RESPONSE. Allows the RELEASE CHARGES ON HOLD report to update bill numbers for a single patient when multiple charges are released at the same time. Updated the UC visit count parameter to display the number of visits that are not in a REMOVED status. Prevents erroneous Patient Not Found at Site messages from displaying in the IBUC URGENT CARE EXCEPTIONS report.
- Updates the Release Charges on Hold report so that users are not ‘kicked out’ when releasing multiple charges at the same time and updates the Urgent Care Visit Tracking Maintenance option to allow Facility Revenue (FR) supervisors to enter Free visits for Veterans that have a date discrepancy related to retro-active Priority Group changes via an override option.
- Updates the Urgent Care Visit Tracking functionality to automatically update all sites a patient where a patient receives care, ensures the nightly job runs appropriately, and changed the Veterans Health Information System and Technology Architecture (VistA) Urgent Care Exceptions mail group to public.
- Updates the List All Bills for a Patient report to allow users to filter by 1<sup>st</sup> or 3<sup>rd</sup> Party, define a date range for data, export the data to an Excel spreadsheet, and ensures only one patient’s data appears. Updates the 1st party Cancellation Reasons in the IB Charge Remove Reason file to inactivate UC-Entered in Error and UC-Change in Eligibility and activate UC-PG6 Reviewed. Updates the IB Cancel/Edit/Add Charges module to only allow changes with the IB EDIT security key.
- Incorporates the ability to add Urgent Care (UC) copayments in the Cancel/Edit/Add screens, provides functionality to track, modify and report UC visits, and automatically update all stations where a Veteran is enrolled with UC data in accordance with the MISSION Act of 2018.
- Automates billing of pharmacy, inpatient, Nursing Home Care Unit (NHCU), and outpatient copayments; inpatient and NHCU per diem charges; and passing charges to Accounts Receivable (AR).
- Automatically exempts patients who are eligible for VA Pension, Aid and Attendance, or House Bound benefits from the Medication Copayment requirement.
- Provides for manual assignment of hardship exemptions from the copayment requirement and the ability to track those exemptions.
- Integrates with the checkout functionality released in the PIMS V. 5.3 package. Patients who claim exposure to Agent Orange and environmental contaminants, and who are treated for conditions not related to this exposure, are billed automatically.
- Allows patient charges to be added, edited, or deleted if there is no automated charge or the automated charge is incorrect.
- Creates subsistence charges for Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) patients and passes to Accounts Receivable. This functionality will not be activated until the AR package releases a patch that allows AR to process CHAMPVA receivables.
- Allows Means Test billing data to be transmitted between facilities in conjunction with PDX V. 1.5.
- Automatically creates Means Test charges when a verified Means Test is electronically received from the Income Verification Match (IVM) Center.
- Exempt Medal of Honor (MOH) recipients from medication copayments.
- Allows cancellation of medication copayment charge using the reason, Medal of Honor.

## Third-Party Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Updated the Third-Party Follow-Up report to correctly report Community Care.
- Automates the creation of third-party billing forms (UB-82, UB-92, Health Care Finance Administration \[HCFA-1500\]), allowing for the entry, editing, authorizing, printing, and canceling of bills.
- Provides the ability to add prescription refills and prosthetic items to bills.
- Expands the UB-92 functionality to include the ability to add/edit all unlabeled form locators (except 49), and additional diagnosis.
- Provides a check-off sheet (can be replaced by the Encounter Form depending on local needs) that can be printed in a variety of site-configurable formats to be used in clinics to identify Current Procedural Terminology (CPT) codes.
- Allows the transfer of CPT codes between the billing screens and the SCHEDULING VISITS file.
- Provides reports to identify billable episodes of care, patient and insurance inquiries, and statistical data.
- Provides the ability to create CHAMPVA bills. The user will not be able to transfer bills to Accounts Receivable until the AR package releases a patch that allows AR to process CHAMPVA receivables.
- Provides an employer report, which lists uninsured patients who are employed.
- Allows printing of all authorized bills in user-specified order.
- Provides an Automated Biller that will automatically generate reimbursable insurance bills for inpatient stays, outpatient visits, and prescription refills. With site parameters, sites can specify which types of events are billed using the Automated Biller.
- Provides an expanded HCFA-1500 claim form to include inpatient bills, user-specified charges, and multiple pages.
- Provides an addendum sheet to HCFA-1500 claim form to list the bill's prescription refills and prosthetic items.

## Insurance Data Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Stores multiple addresses (main mailing, outpatient claims, inpatient claims, prescription claims, appeals, inquiries) for each insurance carrier.
- Provides insurance company-specific billing parameters so bills can reflect local insurance company requirements.
- Provides the ability to establish group plans that will be pointed to by each patient with a policy attached to the plan. This saves re-entry of the same policy data for each patient.
- Stores annual benefits associated with group plans.
- Provides tools to maintain and/or clean up the INSURANCE COMPANY file.
- Allows patient insurance information to be updated and verified.
- Stores benefits used by a patient, such as deductibles and lifetime maximums.
- Provides an insurance worksheet for use by the insurance verifier.

## Additional Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Purges data from selected IB files.
- Provides medical centers flexibility in implementing the package functionality through site parameters.
- Provides the ability to enter new billing rates and VA pension income thresholds.
- Produces management reports to provide workload, productivity, statistical, and historical data.

Related materials include the IB User Manual, Encounter Form Utilities Module, IB Technical Manual, Package Security Guide, Installation Guide, and Release Notes. The Technical Manual assists the site manager in maintenance of the software. The Package Security Guide provides information concerning security requirements for the package. The Installation Guide helps in installation of the package while the Release Notes describe modifications and enhancements to the software that are new to this version.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use This Manual

This manual is presented in an online format, but it may also be printed; however, because its intent is for online viewing, and it is not anticipated that it will be printed in its entirety, it has not been formatted for double-sided printing.

The best way to navigate through this manual is by using the Table of Contents (for Word format) and Bookmarks (for pdf format). In later versions of Word, the user may also use the Navigation pane.

The Table of Contents and Bookmarks are presented in a format like the exported menu structure.

# Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data in the Integrated Billing Action file should not be added to, edited, or deleted. This data is designed to provide an audit trail of transactions. If the charges for a copayment are removed, a separate transaction that is a cancellation type will be created and cause the decrease adjustment to be made. If charges are to be changed, the original (or last) charges are canceled and the new charges are set-up as an update type transaction. Data in this file is maintained through documented routine calls from the Outpatient Pharmacy and MAS packages to Integrated Billing. Data in other Integrated Billing files should be maintained through package options.

Instructions to enter new billing rates and VA pension income thresholds will be provided by VA Central Office (VACO) and/or the Albany Information Systems Center (ISC).

The automated billing of Category C Veterans for outpatient copayments, inpatient copayments, and per diems happens automatically through links to the scheduling event driver, the MAS movement event driver, and the nightly background job.

Numerous parameters in the IB SITE PARAMETERS file affect the functional and technical operations of the billing software.

Several options have parameters that affect the operation of the IB package. The MCCR Site Parameter Enter/Edit option parameters affect the operation of the Patient and Third-Party Billing modules. The Select Default Device for Forms option affects where forms will print. The Claims Tracking Parameter Edit option affects the operation of the Claims Tracking module. The Enter/Edit Automated Billing Parameters option allows the site to determine when and which bills the Automated Biller generates. The Enter/Edit IB Site Parameters option on the System Manager's IB Menu affects many of the technical aspects of the IB package.

Per Veterans Health Administration (VHA) Directive 10-93-142, many of the IB routines, data dictionaries, and data files are not to be modified. Only the routines for Encounter Form utilities and selected outputs may be modified.

An electronic signature code is required for users of the Manually Change Copay Exemption (Hardships) option under the Medication Copayment Income Exemption Menu and the Purge Update File and Archive Billing Data options under the Purge Menu.

# Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On-line Help

When the format of a response is specific, a Help message is usually provided for that prompt. Help messages provide lists of acceptable responses or format requirements that provide instruction on how to respond.

A Help message can be requested by typing one or two question marks. The Help message will appear under the prompt, then the prompt will be repeated.

For example:

BILLING LOCATION OF CARE: 1//

and the user needs assistance answering. Enter ?? and the Help message will appear.

BILLING LOCATION OF CARE: 1// ??

This identifies the type of facility at which care was administered.

> Choose from:

> 1 HOSPITAL (INCLUDES CLINIC) - INPT. OR OPT.

> 2 SKILLED NURSING (NHCU)

> 3 CLINIC (WHEN INDEPENDENT OR SATELLITE)

BILLING LOCATION OF CARE: 1//

For some prompts, the system will list the possible answers the user can select. Any time choices appear with numbers, the system will usually accept the number or the name.

A Help message may not be available for every prompt. If the user enters question marks at a prompt that does not have a Help message, the system will repeat the prompt.

1.  Users with QUME Terminals:

    It is very important that the user set up the Qume terminal properly. After entering access and verifying codes, the following prompt will appear:

    Select TERMINAL TYPE NAME: {type}//

Please make sure that C-QUME is entered here. This entry will become the default and then enter \<RET\> for all subsequent log-ins. If any other terminal type of configuration is set, options using the List Manager utilities will not display nor function properly on the terminal.

# Billing Clerk’s Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Third-Party Joint Inquiry (TPJI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides information needed to answer questions from insurance carriers regarding specific bills or episodes of care. This information is presented in List Manager Screens. Because the same actions are available on most screens, and most screens can be accessed from any other screen; these Common Actions are listed first and are not repeated under each screen description. Only actions specific to a screen are included with that screen description.

2.  When viewing the TPJI main screen, the user must have already selected a specific Claim \# for which to see additional information.

The user may QUIT from any screen; it will bring the user back one level or screen. EXIT is also available on most screens. EXIT returns the user to the menu. For more information on the use of the List Manager utility, please refer to [Appendix C](#appendix-c-list-manager-appendix) at the end of this manual.

Third-Party Joint Inquiry Sample Screen

Claim Information Mar 07, 2023@14:23:14 Page: 1 of 3.

K234ABC GGGGGGG,NNN SSSSS DOB: 08/17/54 Subsc ID: XXXXXXXXX

.

Insurance Demographics

Bill Payer: AAAAA BB HEALTHCARE

Claim Address: PO BOX 987654

EL PASO, TX 79998

Claim Phone: 800 666-5678

Subscriber Demographics

Group Number: GRP NUM 22222

Group Name: PPPPPPP

Subscriber ID: XXXXXXXXX

Employer: US GOVERNMENT

Insured's Name: GGGGGGG,NNN SSSSS

Relationship: PATIENT .

\+ \|% EEOB \| Enter ?? for more actions\| .

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CB Change Bill HS Health Summary EL Patient Eligibility

ED EDI Status AL Go to Active List EB Expand Benefits

RX ECME Information EP ERA/835 EX Exit

Select Action: Next Screen//

| Acronym | Description         | Action                                                                                                                                                                        |
|---------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BC      | Bill Charges        | Accesses the Bill Charges screen.                                                                                                                                             |
| DX      | Bill Diagnoses      | Accesses the Bill Diagnoses screen.                                                                                                                                           |
| PR      | Bill Procedures     | Accesses the Bill Procedures screen.                                                                                                                                          |
| CB      | Change Bill         | Accesses the Change Bill screen.                                                                                                                                              |
| ED      | EDI Status          | Accesses the EDI Status screen.                                                                                                                                               |
| RX      | ECME Information    | Accesses the EDI Information screen.                                                                                                                                          |
| AR      | Account Profile     | Accesses the Account Profile screen.                                                                                                                                          |
| CM      | Comment History     | Accesses the Comment History screen.                                                                                                                                          |
| IR      | Insurance Reviews   | Accesses the Insurance Reviews screen.                                                                                                                                        |
| HS      | Health Summary      | Displays a Health Summary report. The information displayed on the Health Summary is site specified through the MCCR Site Parameter Display / Edit option.                    |
| AL      | Go to Active List   | Returns the user to the Third-Party Active Bills screen if that screen was accessed upon entering this option; otherwise, this action returns the user to the menu.           |
| EP      | ERA/835             | Accesses the ERA / 835 screen.                                                                                                                                                |
| VI      | Insurance Company   | Accesses Insurance Company Screen.                                                                                                                                            |
| VP      | Policy              | Displays the same information and action options as when selecting the same action option from TPJI Main Screen and returns the user to the ERA / 835 screen.                 |
| AB      | Annual Benefits     | Accesses the Annual Benefits screen.                                                                                                                                          |
| EL      | Patient Eligibility | Displays the same information and action options as when the same action option is selected from the TPJI Main Screen and returns the user to the ERA/835 screen.             |
| EB      | Expand Benefits     | Displays detailed information on patient benefits.                                                                                                                            |
| EX      | Exit                | Exit the TPJI Claim Information screen.                                                                                                                                       |
| CI      | Go to Claim Screen  | Returns the user to the Claim Information screen from any of the common actions screens and is available on all screens that may be opened from the Claim Information screen. |

<span id="_Toc143780834" class="anchor"></span>Table : Common Actions

## Third-Party Active Bills Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the first screen displayed if the user enters a patient name at the first prompt of this option. It lists all active third-party bills for the specified patient in order of date created. All bills created in the Integrated Billing Third-Party Billing module can be found on this screen or the Inactive Bills screen.

Third-Party Active Bills Screen Sample

Third-Party Active Bills Feb 28, 2018@15:19:44 Page: 1 of 1

IBPATIENT,ONE I9999 NSC

Bill \# From To MT? Type Stat Rate Insurer Orig Amt Curr Amt

1 %XXXXXXX 01/03/17 01/03/17 NO O/I/O A REIM IN NALC HI 8451.27 7519.05

2 %XXXXXXX 02/13/17 02/13/17 NO O/I/O A REIM IN NALC HI 230.73 230.73

3 XXXXXXXX 04/04/17 04/04/17 NO O/ /R A REIM IN CAREMAR 158.68 78.52

4 XXXXXXXX 05/02/17 05/02/17 NO O/ /R A REIM IN CAREMAR 132.31 93.12

5 XXXXXXXX 05/05/17 05/05/17 NO O/ /R A REIM IN CAREMAR 158.68 78.52

\|r Referred\|\* MT on Hold \|+ Multi Carriers\|% EEOB\|

CI Claim Information IL Inactive Bills PI Patient Insurance

CP Change Patient HS Health Summary EL Patient Eligibility

Select Action: Quit//

| Acronym | Description       | Action                                                                                                          |
|---------|-------------------|-----------------------------------------------------------------------------------------------------------------|
| IL      | Inactive Bills    | Accesses the Inactive Bills screen.                                                                             |
| PI      | Patient Insurance | Accesses the Patient Insurance screen.                                                                          |
| CP      | Change Patient    | Allows the user to select another patient and re-displays the Third-Party Active Bills screen for that patient. |

<span id="_Toc143780835" class="anchor"></span>Table : Common Actions

## Inactive Bills Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen lists inactive bills for a specified patient. All bills created in the Integrated Billing Third-Party Billing module are found on this screen or the Third-Party Active Bills screen. Bills are displayed beginning with the most recent statement from date.

Inactive Bills Screen SampleInactive Bills Feb 28, 2018@15:40:48 Page: 1 of 4

IBPATIENT,ONE I9999 \*\* All Inactive Bills \*\* (51)

Bill \# From To Type Stat Rate Insurer Orig Amt Curr Amt

1 XXXXXXX 05/05/13 05/05/13 O/I/O CB REIM IN 0.00 0.00

2 %XXXXXXX 04/02/13 04/02/13 O/I/O CC REIM IN +CLAIMS 3932.93 0.00

3 XXXXXXX 04/01/13 04/16/13 I/P/I CB REIM IN +MEDICAR 0.00 0.00

4 %XXXXXXX 04/01/13 05/05/13 I/P/I CC REIM IN +CLAIMS 104.29 0.00

5 XXXXXXX 04/01/13 05/05/13 I/P/I CB REIM IN +MEDICAR 0.00 0.00

6 %XXXXXXX 03/28/13 04/01/13 I/I/I CC REIM IN +CLAIMS 1184.00 0.00

7 %XXXXXXX 03/28/13 04/01/13 I/P/I CC REIM IN +CLAIMS 2.05 0.00

8 %XXXXXXX 03/28/13 04/01/13 I/P/I CC REIM IN +CLAIMS 12.06 0.00

9 %XXXXXXX 03/28/13 04/01/13 I/P/I CC REIM IN +CLAIMS 25.93 0.00

10 %XXXXXXX 03/28/13 04/01/13 I/P/I CC REIM IN +CLAIMS 1.71 0.00

11 %XXXXXXX 03/28/13 04/01/13 I/P/I CC REIM IN +CLAIMS 5.48 0.00

12 %XXXXXXX 03/28/13 04/01/13 I/P/I CC REIM IN +CLAIMS 19.54 0.00

13 %XXXXXXX 03/28/13 04/01/13 I/P/I CC REIM IN +CLAIMS 16.29 0.00

14 %XXXXXXX 03/28/13 04/01/13 I/P/I CC REIM IN +CLAIMS 19.54 0.00

15 %XXXXXXX 03/28/13 04/01/13 I/P/I CC REIM IN +CLAIMS 20.20 0.00

16 %XXXXXXX 03/28/13 04/01/13 I/P/I CC REIM IN +CLAIMS 1.71 0.00

\+ \|r Referred\|\* MT on Hold \|+ Multi Carriers\|% EEOB\|

CI Claim Information AL Go to Active List CD Change Dates

EX Exit

Select Action: Next Screen//

| Acronym | Description  | Action                                                                                                          |
|---------|--------------|-----------------------------------------------------------------------------------------------------------------|
| CD      | Change Dates | Allows the user to change the bills listed by changing the most recent statement from date to be displayed. |

<span id="_Toc143780836" class="anchor"></span>Table : Common Actions

## Patient Insurance Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays the list of insurance policies for a patient. It is based on the Patient Insurance Management screen of the Patient Insurance Info View/Edit option. It is only available from the Third-Party Active Bills screen.

Patient Insurance Sample ScreenPatient Insurance May 31, 1995 @10:07:11 Page 1 of 1

Insurance Management for Patient: IBpatient,one XXXX

Insurance Co. Type of Policy Group Holder Effect. Expires

1 HEALTH INS LTD GN 48923222 SELF 01/01/87

2 ABC MAJOR MEDICAL AE 76899354 SPOUSE 10/1/90 11/30/95

3 XYZ INS INDEMNITY T109 OTHER 10/1/94 01/01/95

4 BC/BS MAJOR MEDICAL GN 392043 SELF 01/01/90 12/31/92

VI Insurance Company VP Policy AB Annual Benefits

AL Go to Active List EX Exit Action

Select Action: Quit//

## Claim Information Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen contains bill data and status information to provide an overall status of the bill. This is the primary claim screen for the inquiry and many actions are provided to expand on claim details.

If a policy has been updated but the bill has not, those changes are not reflected on this screen. Updated or current insurance information may be viewed using the three insurance screens.

Claim Information Screen

Claim Information Dec 12, 2013@08:10:10 Page: 1 of 3

XXXXXXXX PXXXX DOB: XX/XX/XX Subsc ID: XXXXXXXXX

-------------------------------------------------------------------------------

Insurance Demographics

Bill Payer: CAREMARK 6XXXXX

Claim Address: PO BOX XXXXX

ANYTOWN, AZ XXXXX

Claim Phone: XXX-XXX-XXXX

Subscriber Demographics

Group Number: GRP PLN 1605501

Group Name: GICRX

Subscriber ID: XXXXXXXXX

Employer: BIG COMPANY

Insured's Name: IB,SPOUSE

Relationship: SPOUSE

+---------\|% EEOB \| Enter ?? for more actions\|--------------------------------

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CB Change Bill HS Health Summary EL Patient Eligibility

ED EDI Status AL Go to Active List EB Expand Benefits

RX ECME Information EX Exit

Select Action: Next Screen// NEXT SCREEN

Claim Information Dec 12, 2013@08:10:21 Page: 2 of 3

XXXXXXXX PATIENT,IB PXXXX DOB: XX/XX/XX Subsc ID: XXXXXXXXX

+-----------------------------------------------------------------------------

Claim Information

Bill Type: OUTPATIENT Charge Type:

Time Frame: ADMIT THRU DISCHARGE Service Dates: 01/31/12 - 01/31/12

Rate Type: REIMBURSABLE INS. Orig Claim: 12.85

AR Status: COLLECTED/CLOSED Balance Due: 0.00

Sequence: PRIMARY

Purch Svc: NO

ECME No: XXXXXXXXXXXX

ECME Ap No: XXXXXXXXXXXXXXXXXXXX

NPI: XXXXXXXXXX

HPID: XXXXXXXXXX

+---------Enter ?? for more actions---------------------------------------------

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CB Change Bill HS Health Summary EL Patient Eligibility

ED EDI Status AL Go to Active List EB Expand Benefits

RX ECME Information EX Exit

Select Action: Next Screen// NEXT SCREEN

Claim Information Dec 12, 2013@08:10:24 Page: 3 of 3

XXXXXXXX PATIENT,IB PXXXX DOB: XX/XX/XX Subsc ID: XXXXXXXXX

+------------------------------------------------------------------------------

Entered: 01/31/12 by IB,TESTER

Authorized: 01/31/12 by IB,TESTER

First Printed: 01/31/12 by IB,TESTER

Related Prescription Copay Information

Rx: 2326479 Chg: \$8.00 Status: On Hold Bill:

----------Enter ?? for more actions---------------------------------------------

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CB Change Bill HS Health Summary EL Patient Eligibility

ED EDI Status AL Go to Active List EB Expand Benefits

RX ECME Information EX Exit

Select Action: Quit//

| Acronym | Description | Action                                                                                                                                                                                                                                                   |
|---------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CB      | Change Bill | Allows the user to change the bill being displayed. If the user entered a patient name at the first prompt of this option, only bills for that patient may be selected. If the user entered a bill number at the first prompt, any bill may be selected. |

<span id="_Toc143780837" class="anchor"></span>Table : Common Actions

## Bill Charges Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays a bill's charge information as it would print on the bill. For UB-92 bills, this closely corresponds to Form Locators 42 - 49; therefore, any prosthetic items, Rx refills, or additional diagnoses and procedures are included. For HCFA 1500 bills, this closely corresponds to Block 24.

Bill Charges Sample ScreenBill Charges May 31, 1995 @10:07:11 Page 1 of 1

XXXXXX IBpatient,one XXXX DOB: X/XX/XX Subsc ID: XXXXXXXX

11/16/93 - 11/17/93 ADMIT THRU DISCHARGE Orig Amt: 199.00

OUTPATIENT VISIT

500 OUTPATIENT SVS 178.00 1 178.00

PRESCRIPTION

257 DRGS/NONSCRPT 21.00 1 21.00

001 TOTAL CHARGE 199.00

OP VISIT DATE(S) BILLED: NOV 16, 1993

PRESCRIPTION REFILLS:

XXXXX NOV 17, 1993 ABBOCATH-T 18G 1.25 IN

QTY: 20 for 10 days supply

Bill Remark: This is a demonstration bill created for Joint Billing Inquiry

Enter ?? for more actions

DX Bill Diagnosis AR Account Profile VI Insurance Company

PR Bill Procedures CM Comment History VP Policy

CI Go to Claim Screen IR Insurance Reviews AB Annual Benefits

HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

Bill Charges Sample Screen continued...Bill Charges May 31, 1995 @10:07:11 Page 1 of 1

XXXXXX IBpatient,one XXXX DOB: X/XX/XX Subsc ID: XXXXXXXX

03/02/94 - 03/31/94 INTERIM - FIRST CLAIM Orig Amt: 11221.00

30 DAYS INPATIENT CARE

INTERMEDIATE CARE

101 ALL INCL R&B 246.00 30 7380.00

240 ALL INCL ANCIL 48.00 30 1440.00

960 PRO FEE 49.00 30 1470.00

274 PROSTH/ORTH DEV 931.00 1 931.00

001 TOTAL CHARGE 11221.00

PROSTHETIC ITEMS:

Sep 18, 1994 WHEELCHAIR

Sep 21, 1994 CANE-ALL OTHER

Enter ?? for more actions

DX Bill Diagnosis AR Account Profile VI Insurance Company

PR Bill Procedures CM Comment History VP Policy

CI Go to Claim Screen IR Insurance Reviews AB Annual Benefits

HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

## Bill Diagnosis Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays all diagnoses assigned to the bill in the order printed.

Bill Diagnosis Sample Screen

Bill Diagnosis May 17, 1996 14:07:56 Page: 1 of 1

XXXXXX IBpatient,one 1111 DOB: XX/XX/XX Subsc ID: XXXXXXXX

11/16/93 - 11/17/93 ADMIT THRU DISCHARGE CLAIM Orig Amt: 199.00

1\) 490. BRONCHITIS NOS

2\) 030.1 TUBERCULOID LEPROSY

3\) 101. VINCENT'S ANGINA

4\) 330.1 CEREBRAL LIPIDOSES

5\) 461.0 AC MAXILLARY SINUSITIS

6\) 310.0 FRONTAL LOBE SYNDROME

7\) 200.01 RETICULOSARCOMA HEAD

Enter ?? for more actions

BC Bill Charges AR Account Profile VI Insurance Company

PR Bill Procedures CM Comment History VP Policy

CI Go to Claim Screen IR Insurance Reviews AB Annual Benefits

HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

## Bill Procedures Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen lists all procedures assigned to a bill in the order printed.

Bill Procedures Sample ScreenBill Procedures May 17, 1996 14:12:58 Page: 1 of 1

XXXXXX IBpatient,one XXXX DOB: X/XX/XX Subsc ID: XXXXXXXX

11/16/93 - 11/17/93 ADMIT THRU DISCHARGE CLAIM Orig Amt: 199.00

XXXXX SURGICAL CLEANSING OF SKIN 11/16/93

XXXXX ADDITIONAL CLEANSING OF SKIN 11/16/93

XXXXX REPAIR SUPERFICIAL WOUND(S) 11/16/93

Enter ?? for more actions

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

CI Go to Claim Screen IR Insurance Reviews AB Annual Benefits

HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

## AR Account Profile Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen provides the financial history of a claim's account. This includes the current status of the bill in both IB and AR, as well as the payment or transaction history of the bill from Accounts Receivable. This screen is loosely based on the Profile of Accounts Receivable option.

AR Account Profile Sample ScreenAR Account Profile May 31, 1995 @10:07:11 Page: 1 of 1

XXXXXX IBpatient,one XXXX DOB: XX/XX/XX Subsc ID: XXXXXXXX

AR Status: ACTIVE Orig Amt: 11221.00 Balance Due: 856.45

04/01/94 IB Status: Printed (Last) 11221.00 11221.00

1 1578 05/07/94 PAYMENT (IN PART) 7856.21 3364.79

2 1598 07/07/94 PAYMENT (IN PART) 2508.34 856.45

3 1601 07/08/94 COMMENT 0.00 856.45

Total Collected: 10364.55

Percent Collected: 92.37%

Enter ?? for more actions

BC Bill Charges VT Transaction Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

| Acronym | Description         | Action                                                                 |
|---------|---------------------|------------------------------------------------------------------------|
| VT      | Transaction Profile | Accesses the AR Transaction Profile screen for a selected transaction. |

<span id="_Toc143780838" class="anchor"></span>Table : Common Actions

## AR Transaction Profile Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays detailed account transaction information for individual claim transactions. It is loosely based on the Accounts Receivable Transaction Profile option.

AR Transaction Profile Sample ScreenAR Transaction Profile May 31, 1995 @10:07:11 Page 1 of 1

XXXXXX IBpatient,one XXXX DOB: XX/XX/XX Subsc ID: XXXXXXX

AR Status: ACTIVE Orig Amt: 11221.00 Balance Due: 856.45

TRANS. NO: 1578 TRANS. TYPE: PAYMENT (IN PART)

TRANS. DATE: 05/07/94 DATE POSTED: 05/10/94 (ARH)

TRANS. AMOUNT: 7856.21 RECEIPT \#: XXXXXXXX

BALANCE COLLECTED

------------- ---------------

PRINCIPLE: 3364.79 7856.21

INTEREST: 0.00 0.00

ADMINISTRATIVE: 0.00 0.00

MARSHALL FEE: 0.00 0.00

COURT COST: 0.00 0.00

-------- ---------

TOTAL: 3364.79 7856.21

FY: 94 PR AMT: 3364.79 FY TR AMT: 7856.21

COMMENTS: Date of Deposit: MAY 10, 1994

Enter ?? for more actions

CI Go to Claim Screen AL Go to Active List EX Exit Action

Select Action: Quit//

## AR Comment History Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays AR comments for the claim's account.

AR Comment History Sample ScreenAR Comment History May 17, 1996 14:21:37 Page: 1 of 1

XXXXXX IBpatient,one XXXX DOB: XX/XX/XX Subsc ID: XXXXXXXX

AR Status: CANCELLED Orig Amt: 1026.02 Balance Due: 1026.02

1582 04/21/92 Copy of bill sent. FOLLOW-UP DT: 05/12/92

Carrier did not receive initial bill.

1594 05/20/92 Bill canceled, wrong form type. FOLLOW-UP DT: 06/01/92

Carrier refuses to process this type of bill on a UB-92.

They are requiring the HCFA 1500 form.

Enter ?? for more actions

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis AD Add AR Comment VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

| Acronym | Description    | Action                                                                                                                                                            |
|---------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AD      | Add AR Comment | Allows the user to add an AR Transaction Comment to the bill being displayed. Comment transactions may not be added to a bill that has not been authorized in IB. |

<span id="_Toc143780839" class="anchor"></span>Table : Field Descriptions

## Insurance Reviews / Contacts Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays all insurance reviews and contacts for the episodes of care on a bill. It is based on the Insurance Reviews/Contacts screen of the Claims Tracking Insurance Review Edit option. The primary difference between the two screens is that this screen consolidates all contacts for each episode being billed on a claim, while the Claims Tracking screen displays the contacts for a single episode of care.

Insurance Reviews/Contacts Sample ScreenInsurance Reviews/Contacts May 31, 1995 @10:07:11 Page: 1 of 1

Insurance Review Entries for: N10072 IBpatient,one XXXX

Date Ins. Co. Type Contact Action Auth. No. Days

OUTPATIENT VISIT of AMBULATORY SURGERY OFFICE on 11/16/93

1 11/30/93 HEALTH INS LIMITED 1st Appeal-Clin APPROVED AU XXXXX

2 11/17/93 HEALTH INS LIMITED OPT DENIAL 0

PRESCRIPTION REFILL of XXXXX on 11/17/93

3 11/17/93 HEALTH INS LIMITED OPT APPROVED RN XXXXXXX

Service Connected: NO Previous Spec. Bills: TORT \>\>\>

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures VR Reviews/Appeals AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

| Acronym | Description     | Action                                                                                                                                                                                                                                                                                             |
|---------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VR      | Reviews/Appeals | Displays expanded information on a selected insurance contact. The screen accessed by this action will depend on the type of contact selected. If the contact is an appeal or denial, the Expanded Appeals / Denials screen is opened; otherwise, the Expanded Insurance Reviews screen is opened. |

<span id="_Toc143780840" class="anchor"></span>Table : Status Descriptions

## Expanded Appeals / Denials Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays expanded information on insurance appeals and denials listed on the Insurance Review/Contacts screen. This screen is based on the Expanded Appeals/Denials screen of the Claims Tracking Appeal/Denial Edit option.

Expanded Appeals/Denials Sample ScreenExpanded Appeals/Denials May 31, 1995 @10:07:11 Page 1 of 2

Insurance Appeal/Denial for: IBpatient,one 1111 ROI: NOT REQUIRED

Visit Information Action Information

Visit Type: OUTPATIENT VISIT Type Contact: INITIAL APPEAL

Visit Date: 03/09/94 9:00 am Appeal Type: CLINICAL

Clinic: AMBULATORY SURGERY Case Status: OPEN

Appt. Status: CHECKED OUT No Days Pending:

Appt. Type: REGULAR Final Outcome:

Special Cond:

Clinical Information Appeal Address Information

Provider: Ins. Co. Name: HEALTH INS LIMITED

Provider: Alternate Name:

Diagnosis: Street line 1: HIL - APPEALS OFFICE

Diagnosis: Street line 2: 1099 THIRD AVE, SUITE

Special Cond: Street line 3:

City/State/Zip: ANYTOWN, NY 12345

Insurance Policy Information

Ins. Co. Name: HEALTH INS LIMITED Subscriber Name: IBpatient,one

Group Number: GN 48923222 Subscriber ID: XXXXXXXXX

Whose Insurance: VETERAN Effective Date: 01/01/87

Pre-Cert Phone: XXX-XXX-XXXX E Expiration Date:

User Information Contact Information

Entered By: EMPLOYEE Contact Date: 04/01/94

Entered On: 11/16/93 3:30 pm Person Contacted: SPOUSE

Last Edited By: Contact Method: PHONE

Last Edited On: Call Ref. Number: RN XXXXXX

Review Date: 06/02/95

Comments

Policy should cover treatment.

Service Connected Conditions:

Service Connected: NO

NO SC DISABILITIES LISTED

Enter ?? for more actions \>\>\>

CI Go to Claim Screen AL Go to Active List EX Exit Action

Select Action: Quit//

## Expanded Insurance Reviews Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays expanded information on insurance reviews listed on the Insurance Reviews/Contacts screen. This screen is based on the Expanded Insurance Reviews screen of the Claims Tracking Insurance Review Edit option.

Expanded Insurance Reviews Sample ScreenExpanded Insurance Reviews May 31, 1995 @10:07:11 Page 1 of 2

Insurance Review Entries for: IBpatient,one XXXX ROI: NOT REQUIRED

Contact Information Action Information

Contact Date: 11/17/93 Type Contact: OUTPATIENT TREATMEN

Person Contacted: Steve Opt Treatment: RX REFILL

Contact Method: PHONE Action: APPROVED

Call Ref. Number: RN XXXXXXX Auth. Number: RN XXXXXXX

Review Date: 06/02/95

Insurance Policy Information

Ins. Co. Name: HEALTH INS LIMITED Subscriber Name: IBpatient,one

Group Number: GN 48923222 Subscriber ID: XXXXXXXX

Whose Insurance: VETERAN Effective Date: 01/01/87

Pre-Cert Phone: XXX-XXXX Expiration Date:

Appeal Address Information User Information

Ins. Co. Name: HEALTH INS LIMITED Entered By: EMPLOYEE

Alternate Name: Entered On: 11/17/93 12:54 pm

Street line 1: HIL - APPEALS OFFICE Last Edited By: EMPLOYEE

Street line 2: 1099 THIRD AVE, SUITE 301 Last Edited On: 11/20/93 12:55 pm

Street line 3:

City/State/Zip: ANYTOWN, NY 12345

Comments

One refill of prescription approved.

Service Connected Conditions:

Service Connected: NO

NO SC DISABILITIES LISTED

Enter ?? for more actions \>\>\>

CI Go to Claim Screen AL Go to Active List EX Exit Action

Select Action: Quit//

## Insurance Company Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays extended information on an Insurance Company. It is based on the Insurance Company Editor screen of the Insurance Company Entry/Edit option. This screen may be entered from the Patient Insurance screen or any of the bill-specific screens. Once a bill is selected, this screen displays only information related to the insurance carriers assigned to that bill.

Insurance Company Sample ScreenInsurance Company May 17, 1996 15:25:42 Page: 1 of 5

Insurance Company Information for: HEALTH INS LIMITED Primary

Type of Company: HEALTH INSURANCE Currently Active

Billing Parameters

Signature Required?: YES Attending Phys. ID: AT PH ID VAXXXXXXX

Reimburse?: WILL REIMBURSE Hosp. Provider No.:

Mult. Bedsections: YES Primary Form Type:

Diff. Rev. Codes: Billing Phone:

One Opt. Visit: NO Verification Phone:

Amb. Sur. Rev. Code: Precert Comp. Name: ABC INSURANCE

Rx Refill Rev. Code: Precert Phone: XXX-XXX-XXXX

Filing Time Frame:

Main Mailing Address

Street: 2345 CENTRAL AVENUE City/State: ANYTOWN, NY 12345

Street 2: FREAR BUILDING Phone: XXX-XXXX

Street 3: Fax: XXX-XXXX

Inpatient Claims Office Information

Street: 2345 CENTRAL AVENUE City/State: ANYTOWN, NY 12345

Street 2: FREAR BUILDING Phone: XXX-XXXX

Street 3: Fax: XXX-XXXX

Outpatient Claims Office Information

Street: 789 3RD STREET City/State: ANYTOWN, NY 12345

Street 2: Phone: XXX-XXX-XXXX

Street 3: Fax: XXX-XXX-XXXX

Insurance Company Sample Screen, continued

Prescription Claims Office Information

Company Name: GHI PROCESSING Street 3:

Street: 1933 CORPORATE DRIVE City/State: ANYTOWN, NY 39332

Street 2: TANGLEWOOD PARK Phone: XXX-XXXX

Fax:

Appeals Office Information

Street: HIL - APPEALS OFFICE City/State: ANYTOWN, NY 12345

Street 2: 1099 THIRD AVE, SUITE 301 Phone: XXX-XXXX

Street 3: Fax: XXX-XXXX

Inquiry Office Information

Street: 2345 CENTRAL AVENUE City/State: ANYTOWN, NY 12345

Street 2: FREAR BUILDING Phone: XXX-XXXX

Street 3: Fax: XXX-XXXX

Remarks

Synonyms

<u>Enter ?? for more actions \>\>\></u>

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

## Patient Policy Information Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays extended information on insurance policies. It is based on the Patient Policy Information screen of the Patient Insurance Info View/Edit option. This screen may be entered from either the Patient Insurance screen or any of the bill-specific screens. Once a bill is selected, this screen will only display information related to the insurance policies assigned to the bill.

The PT action is used to view Patient Policy Comments history. This action does not allow one to add, edit, or delete comments.

3.  The user will NOT be able to view the Patient Policy Comments history if TPJI was entered using a bill number at the first prompt of the option.

Patient Policy Information Sample Screen

Patient Policy Information Dec 12, 2013@08:13:21 Page: 1 of 5

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

--------------------------------------------------------------------------------

Insurance Company

Company: IB INSURANCE

Street: SOME ST

Street 2:

City/State: ANYTOWN, MD XXXXX

Billing Ph: (XXX)XXX-XXXX

Precert Ph: (XXX)XXX-XXXX

Plan Information

Is Group Plan: YES

Group Name: GROUP NAME

Group Number: XXXXXXXXXX

BIN:

PCN:

Type of Plan:

Plan Filing TF:

ePharmacy Plan ID:

+---------Enter ?? for more actions---------------------------------------------

AL Active List PT Pt Policy Comments EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:30 Page: 2 of 5

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

ePharmacy Plan Name:

ePharmacy Natl Status:

ePharmacy Local Status:

Utilization Review Info Effective Dates & Source

Require UR: NO Effective Date: 01/01/13

Require Amb Cert: NO Expiration Date:

Require Pre-Cert: NO Source of Info: INTERVIEW

Exclude Pre-Cond: NO Stop Policy From Billing: NO

Benefits Assignable: YES

Subscriber Information

Whose Insurance: VETERAN

Subscriber Name: IB,PATIENT

Relationship: SELF

Primary ID: XXXXXX

+---------Enter ?? for more actions---------------------------------------------

AL Go To Active List PT Pt Policy Comments EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:31 Page: 3 of 5

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

Coord. Benefits: PRIMARY

Subscriber's Employer Information

Employment Status: Emp Sponsored Plan: No

Employer: Claims to Employer: No, Send to Insurance

Street: Retirement Date:

City/State:

Phone:

Primary Provider:

Prim Prov Phone:

Subscriber's Information (use Subscriber Update Action)

Insured's DOB: XX/XX/XXXX

Str 1: SOME ST

Str 2:

+---------Enter ?? for more actions---------------------------------------------

AL Active List PT Pt Policy Comments EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:32 Page: 4 of 5

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

City: SOME CITY

St/Zip: MA XXXXX

SubDiv:

Country:

Phone: XXX-XXX-XXXX

Insured's Sex: MALE

Insured's Branch: ARMY

Insured's Rank:

Insurance Company ID Numbers (use Subscriber Update Action)

Subscriber ID: XXXXXX

Plan Coverage Limitations

Coverage Effective Date Covered? Limit Comments

+---------Enter ?? for more actions---------------------------------------------

AL Active List PT Pt Policy Comments EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:39 Page: 5 of 5

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Comment –- Group Plan

None

Comment – Patient Policy

<u>Dt Entered Entered By Method Person Contacted</u>

+03/17/16 IB,CLERK

Patient Policy Comment

03/14/16 POSTMASTER

TEST COMENT

Personal Riders

Rider \#1: DENTAL COVERAGE

----------Enter ?? for more actions---------------------------------------------

AL Active List PT Pt Policy Comments EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

## Annual Benefits Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays extended information on the annual benefits of insurance policies. It is based on the Annual Benefits Editor screen of the Patient Insurance Info View/Edit option. This screen may be entered from the Patient Insurance screen or any of the bill-specific screens. Once a bill has been chosen, this screen displays information related to the insurance policies assigned to that bill.

Annual Benefits Sample ScreenAnnual Benefits May 17, 1996 15:39:23 Page: 1 of 3

Annual Benefits for: GHI Ins. Co Primary

Policy: GN 48923222 Ben Yr: MAR 01, 1993

Policy Information

Max. Out of Pocket: \$ 500

Ambulance Coverage (%): 85 %

Inpatient

Annual Deductible: \$ 500 Drug/Alcohol Lifet. Max: \$

Per Admis. Deductible: \$ 100 Drug/Alcohol Annual Max: \$

Inpt. Lifetime Max: \$ Nursing Home (%):

Inpt. Annual Max: \$ Other Inpt. Charges (%):

Room & Board (%):

Outpatient

Annual Deductible: \$ 50 Surgery (%):

Per Visit Deductible: \$ 50 Emergency (%): 85%

Lifetime Max: \$ Prescription (%): 80%

Annual Max: \$ Adult Day Health Care?: UNK

Visit (%): Dental Cov. Type: PERCENTAGE AMOU

Max Visits Per Year: Dental Cov. (%): 48%

Mental Health Inpatient Mental Health Outpatient

MH Inpt. Max Days/Year: MH Opt. Max Days/Year:

MH Lifetime Inpt. Max: \$ MH Lifetime Opt. Max: \$

MH Annual Inpt. Max: \$ MH Annual Opt. Max: \$

Mental Health Inpt. (%): Mental Health Opt. (%):

Home Health Care Hospice

Care Level: Annual Deductible: \$

Visits Per Year: Inpatient Annual Max.: \$

Max. Days Per Year: Lifetime Max.: \$

Med. Equipment (%): Room and Board (%):

Visit Definition: Other Inpt. Charges (%):

Rehabilitation IV Management

OT Visits/Yr: IV Infusion Opt?: UNK

PT Visits/Yr: IV Infusion Inpt?: UNK

ST Visits/Yr: IV Antibiotics Opt?: UNK

Med Cnslg. Visits/Yr: IV Antibiotics Inpt?: UNK

User Information

Entered By: EMPLOYEE

Entered On: 02/02/94

Last Updated By: EMPLOYEE

Last Updated On: 02/18/94

Enter ?? for more actions \>\>\>

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

## Patient Eligibility Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays the current information on the patient's eligibility for care and service connection status. It is loosely based on the Eligibility Inquiry for Patient Billing option. This screen is available from the Third-Party Active Bills screen and the bill-specific screens.

If this screen is accessed from one of the bill-specific screens, such as the Claim Information screen, the standard list of bill screen actions will be available from this screen.

If this screen is accessed from the Patient Insurance screen, no other screens are available as actions from this screen; and the user must return to a previous screen to access other screens.

Patient Eligibility Sample ScreenPatient Eligibility May 20, 1996 07:45:44 Page: 1 of 1

XXXXXX IBpatient,one 1111 DOB: XX/XX/XX Subsc ID: XXXXXXX

Means Test: CATEGORY A Insured: Yes

Date of Test: 08/24/94 A/O Exposure:

Co-pay Exemption Test: Rad. Exposure:

Date of Test:

Primary Elig. Code: NSC

Other Elig. Code(s): EMPLOYEE

AID & ATTENDANCE

Service Connected: No

Rated Disabilities: BONE DISEASE (0%-NSC)

DEGENERATIVE ARTHRITIS (40%-NSC)

Enter ?? for more actions

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EX Exit Action

AL Go to Active List

Select Action: Quit//

## Enter / Edit Billing Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB EDIT security key is required to access this option.

The Enter/Edit Billing Information option is used to enter the information required to generate a third-party bill and to edit existing billing information. A new bill can be entered (or an existing bill can be edited) if the existing bill has not been authorized or canceled. Once a bill has been filed (billing record number established), it cannot be deleted. The bill can be canceled through the Cancel Bill option.

If the selected patient's eligibility has not been verified and the ASK HINQ IN MCCR parameter is set to YES, the user will have the opportunity to enter a HINQ (Hospital Inquiry) request into the HINQ Suspense File. This request will be transmitted to the Veterans Benefits Administration to obtain the patient's eligibility information. If Means Test data such as category, Means Test last applied, and date Means Test completed is available, it will be displayed after the patient’s name or bill number has been entered.

When entering a new bill, the system will prompt for EVENT DATE. When billing for multiple outpatient visits, the date of the initial visit is used. For an inpatient bill, the date of the admission is used. If an interim bill is being issued, the EVENT DATE should be the date of admission for that episode of care.

The Medical Care Cost Recovery data is arranged so that it can be viewed and edited through various screens. The data is grouped into sections for editing. Each section is labeled with a number to the left of the data items. Data group numbers enclosed by brackets (\[ \]) can be edited while those enclosed by arrows (\< \>) cannot. The patient's name, social security number, bill number, bill classification (Inpatient or Outpatient), and screen number appear at the top of every screen. A \<?\> entered at the prompt that appears at the bottom of every screen will provide the user with a HELP SCREEN for that screen. The HELP SCREEN lists the data groups found on that screen and provides the name and number of each available screen in the option. Please see the Supplement at the end of this section for descriptions and samples of the billing screens.

The bill mailing address appears on this screen. Please see the Supplement at the end of this section for important information on how this is determined.

4.  In September 2015, the Inpatient Bill/Claim was updated to accommodate the expanded number of ICD-10 diagnosis and procedure codes available in the Patient Treatment File (PTF). Enter/Edit Billing Information displays and allows selection of all diagnoses and procedures in the PTF record within the date range of the bill, and the screen displays the Present On Admission (POA) indicator associated with the diagnosis if present in PTF. The screen also displays an asterisk (\*) before each PTF ICD procedure that matches a procedure and date already assigned to the bill. It is possible that the same procedure may be completed multiple times on the same date. These duplicate ICD procedures are displayed in the list of PTF ICD procedures as separate line items, and duplicates can be added to the bill.

When insurance companies are entered into the INSURANCE COMPANY file, the system prompts for whether this company will reimburse VA for the cost of the patient's care. Entry of an insurance company that has been designated as will not reimburse is not allowed at this screen. For bills where the payer is the insurance company and the patient has <u>one</u> insurance company that will reimburse the government, that company will be stored as the primary insurance company. Inactivating the insurance company has no effect on the insurance carriers associated with the bill.

Selection of insurance companies is limited to the primary, secondary, and tertiary insurance companies that are billable for the event date. A provider number can be entered for each of the three possible insurance carriers. This field will be loaded from the Hospital Provider Number if one has been entered for the insurance carrier.

Insurance company addresses can only be edited through the Insurance Company Entry/Edit option.

Any bill with a CHAMPVA rate type requires the primary insurance carrier to have a type of coverage defined as CHAMPVA; otherwise, the bill cannot be authorized.

If the MULTIPLE FORM TYPES site parameter is set to YES, a form type prompt will appear. The UB-82 and UB-92 are considered a single form, so for a site to have multiple forms it would have to use one of the UB forms and the HCFA-1500.

Changing the form type to HCFA-1500 will cause the CODING METHOD field to default to CPT-4 if it has not already been defined. Changing the primary insurance carrier or responsible institution will cause the revenue codes to be rebuilt and charges to be recalculated.

If the MCCR site parameter USE OP CPT SCREEN is set to YES, the Current Procedural Terminology Code Screen will appear when editing procedure codes. The screen will list CPT codes for the dates associated with the bill.

An associated diagnosis (diagnosis responsible for the procedure being performed) must be entered for each procedure for HCFA-1500s. the user can enter from one to four associated diagnoses. The associated diagnosis must match one of the first four diagnoses entered.

Adding a BASC procedure or an OP VISIT DATE will cause the revenue codes to be rebuilt and charges recalculated for both UB-82/92 and HCFA-1500 form types. Only one visit date is allowed on a UB-82/92 that also has BASC procedures. This restriction does not apply to HCFA-1500s.

A print order can be specified for each procedure/diagnosis entered. If no print order is specified, the procedures/diagnoses will print in the order entered. The six procedures and nine diagnoses with the lowest print order will be printed in the boxes on the form and the remainder will print as additional procedures/diagnoses.

If the TRANSFER PROCEDURES TO SCHED? parameter is set to YES, any ambulatory surgery entered on the bill can be transferred to the Scheduling Visits file and stored under a 900 stop code. An associated clinic must be entered for all procedures that are to be transferred to the Scheduling Visits file.

Several site parameters and two security keys affect the prompts that will appear at the end of this option. Please see the Supplement at the end of this section for an explanation of how these site parameters and security keys affect the option.

A mail group can be specified (through the site parameters) so that every time a bill is disapproved during the authorization phase of the billing process, all members of this group are notified via electronic mail. If this group is not specified, only the billing supervisor, the initiator of the billing record, and the user who disapproved the bill will be a recipient of the message. An example of this message can be found in the Supplement.

The UB-82, UB-92, and HCFA-1500 billing forms are the output that can be produced from this option. The data elements, and design of these forms, have been determined by the National Uniform Billing Committee and have been adapted to meet the specific needs of the Department of Veterans Affairs. The billing forms must be generated (printed) at 80 characters per line at 10 pitch. Copies of the billing forms are included in the Print Bill option documentation.

The UB-82, UB-92, and HCFA-1500 billing forms are the output that may be produced from this option. The data elements, and design of these forms, have been determined by the National Uniform Billing Committee and have been adapted to meet the specific needs of the Department of Veterans Affairs. The billing forms must be generated (printed) at 80 characters per line at 10 pitch. Copies of the billing forms are included in the Print Bill option documentation.

## Automated Means Test Billing Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Cancel / Edit / Add Patient Charges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB AUTHORIZE security key is required to access this option. Only holders of the IB EDIT Security Key have access to the AC (Add Charges) function and the IBUC VISIT MAINT option so that Separation of Duties can be maintained.

The Cancel/Edit/Add Patient Charges option allows the user to manually cancel, edit, or add per diem and copayment patient charges or Community Care services for a specified patient and date range. When a charge is edited, the original charge is canceled, and a new charge is added. Once added or edited, the charges are passed to Accounts Receivable. The user may receive Accounts Receivable mail messages when editing/canceling through this option.

The user cannot add medication copayment charges for patients determined to be exempt from the medication copayment requirement.

The user can choose whether to include pharmacy copay charges. Only pharmacy charges that have been added through this option can be edited or deleted through this option.

The user can also choose to bill CHAMPVA inpatient subsistence charges for past admissions. (Current and future admissions will be billed automatically at discharge). The CHAMPVA inpatient subsistence charge may be canceled through this option, but it will be canceled only in IB. The user must go into the AR module to decrease the receivable to zero (\$0).

Charges are displayed for the specified patient and date range and several actions can be taken against these charges. The user can add/edit/cancel a charge, pass a charge to Accounts Receivable, change to another patient or date range, update an event by changing the event status, or change the date used to record the last date for which Means Test charges were billed for the admission.

List Manager actions are also available (e.g., First Screen, Last Screen, Up a Line, Down a Line, etc.). If the user needs help utilizing the List Manager functionality, please refer to the Appendix of this user manual.

Once an action has been taken on a charge, the screen is redisplayed showing the new data. If the user has edited a charge, the status of the original entry is changed to CANCELLED, and two new entries are added. The first entry offsets the original charge (the amount appears in parentheses indicating a credit) and the new charge is shown.

Charges added or edited through this option are added/edited to the INTEGRATED BILLING ACTION file (#350). When adjustments are made through this option that affect the number of inpatient days or inpatient amount, the user is prompted to choose whether the user wishes to adjust the Means Test Billing Clock.

If the option Add/Edit/Cancel is used for Pharmacy CoPay changes, no back billing will take place.

Public Law 114-315 dated December 16, 2016, the Jeff Miller and Richard Blumenthal Veterans Health Care and Benefits Improvement Act of 2016, makes Medal of Honor recipients eligible for Veterans Affairs: (1) hospital, nursing home, and domiciliary care; (2) extended care services for non-service-connected disabilities, with no copayment; and (3) medications, with no copayment. Outpatient Pharmacy Copayment charges can be canceled using the reason, Medal of Honor.

Public Law 115-182 dated June 6, 2018, the Maintaining Internal Systems and Strengthening Integrated Outside Networks (MISSION) Act of 2018 ends the Veterans Choice Program and established a new Veterans Community Care benefit allowing Veterans to receive Urgent Care services through VA’s network of community providers.

#### Canceling Duplicate Copay Charges from Within Add A Charge

Occasionally, the user may encounter a scenario where a patient already has a Medical (either an Inpatient, Outpatient, or LTC) copay for the day, the user is entering the copayment for. The Add A Charge action will allow the user to cancel the duplicate copayment if an existing copayment is smaller than the copayment attempting to be entered.

A D D A C H A R G E

-----------------------------------------------------------------------------

Name: IBPatient, One \*\* NO ACTIVE BILLING CLOCK \*\*

ID: XXX-XX-XXXX

-----------------------------------------------------------------------------

Select CHARGE TYPE: OUTPATIENT COPAY DG OPT COPAY NEW

Visit Date: 8/23 (AUG 23, 2020)

This charge will be billed under the following closed clock:

Begin Date: 08/01/19 \# Inpt Days:

Closed Date: 07/30/20 1st 90 Days: \$0

Select one of the following:

C Clinic

S Stop Code

Enter response: Stop Code

Select OUTPATIENT VISIT STOP CODE: 307 GASTROENTEROLOGY EffDate:12/06/01 Spe

cialty

Charge to be billed under the Specialty Care Rate --\> \$50.00

This patient has already been billed a medical copayment for this date.

Please review the associated dates and charges for this patient.

BILL BILL STOP BILL

FROM TO CHARGE TYPE CODE NUMBER STATUS CHARGE

-----------------------------------------------------------------------------

08/23/20 08/23/20 CC (OPT) NEW ON HOLD 15

Do you wish to cancel this existing copayment and continue billing the current

copayment? : YES

Select CANCELLATION REASON: BILLE

1 BILLED AT HIGHER TIER RATE

2 BILLED LTC CHARGE

CHOOSE 1-2: 1 BILLED AT HIGHER TIER RATE

Okay to cancel this charge? YES

Updating the status of the charge to 'canceled'... done.

Press RETURN to process the next charge or to return to the list:

The copayment was canceled. Please continue adding the new copay.

Press any key to continue.

Okay to add this charge? YES done.

Passing the charge directly to Accounts Receivable... done.

Press RETURN to process the next charge or to return to the list:

In addition, the Cancel a Charge (CC) action within the IB CANCEL/EDIT/ADD CHARGES option allows the user to re-bill a previously canceled bill. In the example below, a \$15 copay was canceled because a \$50 specialty visit was billed at the higher tier rate for the same day. If the user cancels the \$50 specialty visit, the system will allow the user to re-bill the original \$15 copay (for the same day) that was canceled.

Charges Sep 21, 2020@14:13:58 Page: 1 of 1

Cancel/Edit/Add Charges 09/22/19 THRU 09/21/20

Patient: IBPATIENT,FIVE IXXXX

Bill From Bill To Charge Type Stop Bill \# Status Charge

1 09/15/20 09/15/20 OPT COPAY NEW 323 CANCELLED \$15

2 09/15/20 09/15/20 OPT COPAY NEW 307 ON HOLD \$50

Enter ?? for more actions

AC Add a Charge CP Change Patient UE Update Events

EC Edit a Charge CD Change Date Range

CC Cancel a Charge PC Pass a Charge

Select Action: Quit// CC Cancel a Charge

Select Charge(s): (1-2): 2

C A N C E L A C H A R G E

Processing Charge \#2

-----------------------------------------------------------------------------

Name: IBPATIENT,FIVE XXXXXXX Type: OPT COPAY NEW 307

ID: XXX-XX-XXXX Amt: \$50 (ON HOLD)

-----------------------------------------------------------------------------

Select CANCELLATION REASON: ENTERED IN ERROR

Okay to cancel this charge? YES

Updating the status of the charge to 'canceled'... done.

The following copay charges from the same date may be re-billed:

Bill From Bill To Charge Type Bill \# Cancel Reason Stop Charge

-----------------------------------------------------------------------------

1 09/15/20 09/15/20 DG OPT COPAY NEW ENTERED IN ERROR 323 \$15

Please review the above list of potentially (re)billable items.

Select charge to re-bill (1 - 1) or type '^' to skip this step: 1

A D D A C H A R G E

-----------------------------------------------------------------------------

Name: IBPATIENT,FIVE XXXXXXX \*\* NO ACTIVE BILLING CLOCK \*\*

ID: XXX-XX-XXXX

-----------------------------------------------------------------------------

Select CHARGE TYPE: OUTPATIENT COPAY// DG OPT COPAY NEW

Visit Date: SEP 15, 2020// (SEP 15, 2020)

This charge will be billed under the following closed clock:

Begin Date: 07/04/19 \# Inpt Days:

Closed Date: 07/02/20 1st 90 Days: \$0

Select one of the following:

C Clinic

S Stop Code

Enter response: Stop Code

Select OUTPATIENT VISIT STOP CODE: 323 PRIMARY CARE/MEDICINE EffDate:10/01/02

Basic

Charge to be billed under the Basic Care Rate --\> \$15.00

Okay to add this charge? YES done.

Passing the charge directly to Accounts Receivable... done.

Press RETURN to process the next charge or to return to the list:

Rebuilding list of charges...

Charges Sep 21, 2020@14:15:31 Page: 1 1

Cancel/Edit/Add Charges 09/22/19 THRU 09/21/20

Patient: IBPATIENT,FIVE IXXXX

Bill From Bill To Charge Type Stop Bill \# Status Charge

1 09/15/20 09/15/20 OPT COPAY NEW 323 CANCELLED \$15

2 09/15/20 09/15/20 OPT COPAY NEW 307 CANCELLED \$50

3 09/15/20 09/15/20 OPT COPAY NEW 323 ON HOLD \$15

Enter ?? for more actions

AC Add a Charge CP Change Patient UE Update Events

EC Edit a Charge CD Change Date Range

CC Cancel a Charge PC Pass a Charge

Select Action: Quit//

#### Canceling copay charges for patients with a Category 1 Patient Record Flag

The user can use the Cancel/Edit/Add Patient Charges option to manually cancel the outpatient visit copay charges for a patient with an active National Category 1 High Risk for Suicide flag. Select HRFS FLAGGED from the list of cancellation choices at the Select CANCELLATION REASON prompt.

C A N C E L A C H A R G E

Processing Charge \#1

---------------------------------------------------------------------------

Name: IBPatient,one Type: CC URGENT CARE (OPT) NEW

ID: 999-99-9XXX Amt: \$30 (BILLED)

---------------------------------------------------------------------------

Select CANCELLATION REASON: ??

Choose from:

4 ENTERED IN ERROR

9 EMPLOYEE

11 PATIENT DECEASED

14 ELIGIBILITY INCORRECT

15 CHANGE IN ELIGIBILITY

17 MT OP APPT NO-SHOW

18 MT OP APPT CANCELLED

19 MT CHARGE EDITED

20 INSURANCE CO PAID IN FULL

22 MT STATUS CHANGED FROM YES

23 COMP & PENSION VISIT RECORDED

24 CHAMPVA ADMISSION DELETED

25 RECD INPATIENT CARE

26 CHECK OUT DELETED

27 CLASSIFICATION CHANGED

28 RESEARCH VISIT/ADMISSION

29 SERVICE CONNECTED VISIT/ADM

30 HARDSHIP GRANTED

31 ADJUDICATED AS CATEGORY A

32 TREATED AT OTHER FACILITY

33 AGENT ORANGE RELATED

34 IONIZING RAD RELATED

35 SOUTHWEST ASIA RELATED

36 CLASS II DENTAL VISIT

37 MILITARY SEXUAL TRAUMA

39 CANCER OF HEAD/NECK

41 PURPLE HEART CONFIRMED

42 BILLED AT HIGHER TIER RATE

43 BILLED LTC CHARGE

44 COMBAT VETERAN

47 KATRINA AFFECTED VETERAN

48 PROJECT 112/SHAD

50 HRFS FLAGGED

53 UC - DUPLICATE VISIT

54 UC - SEQUENCE UPDATE

55 MEDAL OF HONOR

56 UC - PG6 REVIEWED

57 PANDEMIC RESPONSE

Select CANCELLATION REASON:

5.  The user cannot add an outpatient visit copay charge for a patient with an active National Category 1 High Risk for Suicide flag.

A D D A C H A R G E

--------------------------------------------------------------------------------

Name: IBPATIENT,ONE \*\* ACTIVE BILLING CLOCK \*\*

ID: XXX-XX-XXXX Clock Begin Date: 05/30/18

--------------------------------------------------------------------------------

Select CHARGE TYPE: OUTPATIENT COPAY DG OPT COPAY NEW

Visit Date: T (JUL 02, 2018)

This patient is 'Exempt' from Outpatient Visit charges on that date of service.

Press RETURN to process the next charge or to return to the list:

### Adding Prescription Copay Charges for Patients with a National Category 1 Patient Record Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When adding an outpatient prescription copay charge for a patient with an active National Category1 High Risk for Suicide flag, enter the prescribed days’ supply of medication at the DAYS SUPPLY prompt. The prescription copay charge will be prorated for a Days Supply of less than 30 days, including refills for a 30-day period.

A D D A C H A R G E

--------------------------------------------------------------------------------

Name: IBPATIENT,AFIVE \*\* NO ACTIVE BILLING CLOCK

ID: XXX-XX-XXXX

--------------------------------------------------------------------------------

Select CHARGE TYPE: NSC PHARMACY COPAY PSO NSC RX COPAY NEW

Rx Date: T (JUL 02, 2018)

ENTER THE COPAY TIER: (1-3): 2//

DAYS SUPPLY: (1-90): 30// 15

Units: 1

Charge to be billed --\> \$4.00

Okay to add this charge?

### Canceling Copay Charges for Patients with an Urgent Care Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can use the Cancel/Edit/Add Patient Charges option to manually cancel the outpatient visit copay charges for a patient with an Urgent Care visit. There are six regular cancellation reasons and three UC cancellation reasons available, select the appropriate reason code of; PATIENT DECEASED, RECD INPATIENT CARE, BILLED AT HIGHER TIER RATE, ENTERED IN ERROR, CHANGE IN ELIGIBILITY, PANDEMIC RESPONSE, UC-Duplicate Visit, UC-Sequence Update and UC-PG6 REVIEWED from the list of cancellation choices at the Select CANCELLATION REASON prompt.

A UC copay can ONLY be canceled using the cancellation codes listed. The UC visit tracker will be updated when a UC cancellation reason is selected.

- PATIENT DECEASED – Removes the copayment and visit from tracking. The letter (R) signifying the visit was Removed is appended to the Date of Service (DOS) listed in the UC Visit Tracking Maintenance report.
- RECD INPATIENT CARE – Removes the copayment and lists the encounter as Visit Only in the UC Visit Tracking Maintenance report. The letter (V) signifying the visit as Visit Only is appended to the Date of Service (DOS) listed in the UC Visit Tracking Maintenance report.
- BILLED AT HIGHER TIER RATE – Removes the copayment and lists the encounter as Visit Only in the UC Visit Tracking Maintenance report. The letter (V) signifying the visit as Visit Only is appended to the visit in the UC Visit Tracking Maintenance report.
- Entered in Error – Removes the copayment and visit from tracking and being counted. The letter (R) is appended to the Date of Service (DOS) listed in the UC Visit Tracking Maintenance report. This will impact patients with Free visits.
- Change in Eligibility – Does not remove the visit from tracking. May provide a patient with Free visits if the eligibility is moved to a higher Priority Group. The letter (F) signifying the visit as a Free visit is appended to the Date of Service (DOS) listed in the UC Visit Tracking Maintenance report.
- UC - PG6 REVIEWED – Removes the copayment and lists the encounter as Visit Only in the UC Visit Tracking Maintenance report. The letter (V) signifying the visit as Visit Only is appended to the Date of Service (DOS) listed in the UC Visit Tracking Maintenance report.
- UC-Duplicate Visit – Removes the copayment and visit from tracking and being counted. The letter (R) signifying the visit was Removed is appended to the Date of Service (DOS) listed in the UC Visit Tracking Maintenance report. This will impact patients with Free visits.
- UC-Sequence Update – Does not remove the visit from tracking. May provide a patient with Free visits if a visit from a different station precedes a visit at the home station. May be used to ensure collection credit is provided to the correct facility. The letter (F) signifying the visit as a Free visit is appended to the Date of Service (DOS) listed in the UC Visit Tracking Maintenance report.
- PANDEMIC RESPONSE – Removes the copayment and visit from tracking and being counted. The letter (R) signifying the visit was Removed is appended to the Date of Service (DOS) listed in the UC Visit Tracking Maintenance report. This will impact patients with Free visits.

C A N C E L A C H A R G E

Processing Charge \#1

--------------------------------------------------------------------------

Name: IBPatient,one Type: CC URGENT CARE (OPT) NEW

ID: XXX-XX-XXXX Amt: \$30 (BILLED)

--------------------------------------------------------------------------

Select CANCELLATION REASON: ??

Choose from:

4 ENTERED IN ERROR

11 PATIENT DECEASED

15 CHANGE IN ELIGIBILITY

25 RECD INPATIENT CARE

42 BILLED AT HIGHER TIER RATE

43 BILLED LTC CHARGE

53 UC - DUPLICATE VISIT

54 UC - SEQUENCE UPDATE

56 UC - PG6 REVIEWED

57 PANDEMIC RESPONSE

Select CANCELLATION REASON:

### Patient Billing Clock Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB AUTHORIZE security key is required to access this option.

This option allows adding or editing of patient billing clocks. Most often this option will be used to add or edit clocks of patients transferred from other facilities. The following fields are editable: clock begin date, status, 90-day inpatient amounts, and the number of inpatient days. A free text field is also provided to include a reason for the update.

The fields contained in this option are used to determine and directly affect the copayment charges billed to the patient for care received. These fields can also be affected by other options such as the Cancel/Edit/Add Patient Charges option. For further details, please see that option documentation.

The clock will automatically be closed after 365 days or on the date the patient is no longer Category C, whichever is earlier. Billing clocks that may have been left open due to a lack of billable activity will be closed during the nightly compilation job that is run automatically. Billing clocks that must be deleted for any reason will have a status of CANCELLED.

### Estimate Means Test Charges for an Admission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to estimate the Means Test charges for an episode of hospital or nursing home care for a proposed length of stay. It can also be used to estimate charges to be billed to a current inpatient for the remainder of his/her stay.

The report will indicate whether the patient has an active billing clock, the start date, and the number of inpatient days of care within that clock.

If a patient has an active clock and has already been charged a copayment for the current 90 days of inpatient care, the amount that was billed is shown. Also provided is the amount of copay and per diem that would be billed for this proposed episode of care.

Sample Output

Select Automated Means Test Billing Menu \<TEST ACCOUNT\> Option: ESTM Estimate Means

Test Charges for an Admission

Select PATIENT NAME: AAAAAAAA,EEEEEE DDDDD 9-8-34 XXXXXXXXX NO

NSC VETERAN CD

Enrollment Priority: GROUP 8c Category: IN PROCESS End Date:

Please note that this patient was admitted on 05/07/22 and Means Test charges

have been calculated through 05/13/22.

Proposed DISCHARGE Date: 080822 (AUG 08, 2022)

DEVICE: HOME// HOME (CRT) Right Margin: 80//

Estimated Means Test Inpatient Charges for AAAAAAAA,EEEEEE DDDDD

Please note that this patient is a current inpatient.

Charges will be estimated from 05/14/22 through 08/08/22.

\*\* THIS PATIENT HAS AN ACTIVE BILLING CLOCK \*\*

Clock date: 02/01/22 Days of inpatient care within clock: 1

Copayments made for current 90 days of inpatient care: \$0.00

COPAYMENT CHARGES for GENERAL MEDICAL CARE

--------------------------------------------------------------------------------

Billing Dates Inpt. Days Clock Days

From To 1st Last 1st Last Charge

--------------------------------------------------------------------------------

05/14/22 05/14/22 2 2 103 103 \$1,556.00

----------

\$1,556.00

PER DIEM CHARGES for HOSPITAL CARE

--------------------------------------------------------------------------------

05/14/22 08/07/22 86 days @ \$10.00/day \$860.00

----------

Total Estimated Charges: \$2,416.00

Type \<Enter\> to continue or '^' to exit:

Select PATIENT NAME:

The following table describes the fields.

| Field                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Clock Date                                            | Date the current billing clock began for this patient.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Days of Inpatient Care within Clock                   | Number of days of inpatient care within the current billing clock.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Copayments made for Current 90 days of Inpatient Care | Total amount of copayment made for the current 90 days of inpatient care for the current billing clock.                                                                                                                                                                                                                                                                                                                                                                                                   |
| Copayment Charges for (type of care)                  | Amount of the copayment charge for this proposed inpatient stay. The copayment charge differs depending on the type of inpatient care; however, it will not exceed the current Medicaid deductible. Once the deductible is met, the patient is covered for a 90-day period. For the second, third, and fourth 90 days of hospital care, the copayment charge is half of the current Medicaid deductible. For other than hospital care (i.e., NHCU), the full deductible applies for each 90 days of care. |
| Billing Dates (from/to)                               | Date(s) the copayment occurred. If the proposed episode of care was for a total of five days (2/1/92 – 2/5/92) but the deductible was met the first day, the billing dates (from and to) would reflect the first day only (2/1/92).                                                                                                                                                                                                                                                                       |
| Inpatient Days (1st/Last)                             | On which days of the current 90 days of inpatient care this copayment occurred. If the patient previously had two days of inpatient care in the current 90 days and the deductible was met the first day of this proposed episode of care, the inpatient days would reflect day three as the days (1<sup>st</sup> and last) this copayment was incurred.                                                                                                                                              |
| Clock Days (1st/Last)                                 | On which days of the current billing clock this copayment was incurred. If the current billing clock began on 2/1/92 and the copayment for this proposed episode of care was incurred on 2/15 and 2/16/92, the clock days would reflect day 15 for the 1<sup>st</sup> and day 16 for the last.                                                                                                                                                                                                        |
| Charge                                                | Amount of the copayment or per diem charge for this proposed episode of care.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Per Diem Charges for (type of care)                   | A daily charge for the inpatient stay. No charge is incurred for the day of discharge (i.e., if the proposed inpatient stay is 2/1/92 through 2/5/92 and the per diem rate is \$10.00, the total per diem charge would be \$40.00).                                                                                                                                                                                                                                                                       |
| Total Estimated Charges                               | Total of the copayment and the per diem charges for the proposed inpatient stay.                                                                                                                                                                                                                                                                                                                                                                                                                          |

<span id="_Toc143780841" class="anchor"></span>Table : Field Descriptions

## Urgent Care Visit Tracking Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Urgent Care Visit Tracking Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report lists all Urgent Care visits for a patient during a calendar year that have a status of Free, Billed, Removed, or Visit Only. The report provides the ability to Add/Edit visits to accurately record the patient’s UC visits and assigned copayments.

6.  Patch IB\*2\*745 provides changes so that Veterans with an Indian Attestation will have the same UC eligibility as Veterans who are in Priority Groups 1-5 (allowing them 3 Free Visits).

| Status     | Definition                                                                                                                                        |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Free       | Per the MISSION Act of 2018, a PG 1-5 and certain PG 6 Veterans receive three (3) Free visits for UC services before being charged the copayment. |
| Billed     | A UC visit that is billed the required copayment.                                                                                                 |
| Removed    | A UC visit that is not counted in the Veteran’s visit total.                                                                                      |
| Visit Only | A UC visit counted for the total number of visits, but a copayment was not assigned.                                                              |

<span id="_Toc143780842" class="anchor"></span>Table : Data Element Descriptions

Sample Output<u>Add an Urgent Care Visit</u>

Select Urgent Care Visit Tracking Menu \<TEST ACCOUNT\> Option: UCVM Urgent Care Visit Tracking Maintenance

Select PATIENT NAME: Veteran, Air F X-X-XX 99999999 NO NSC VETERAN CD

Enrollment Priority: GROUP 8c Category: ENROLLED End Date:

Enter Year: 2019// 2019

Urgent Care Visits in 2019 for VETERAN, Air Force 999-99-9XXX

=============================================================================

1 Jun 06, 2019 F 7 Aug 15, 2019 13 Sep 03, 2019

2 Jun 28, 2019 8 Aug 16, 2019 14 Sep 04, 2019 V

3 Jul 03, 2019 F 9 Aug 17, 2019 15 Nov 13, 2019 R

4 Jul 05, 2019 F 10 Aug 19, 2019 16 Nov 21, 2019

5 Aug 01, 2019 R 11 Aug 21, 2019 17 Dec 01, 2019

6 Aug 14, 2019 12 Sep 02, 2019 18 Dec 25, 2019

(A)dd an Urgent Care Visit, (E)dit an existing Visit, or (Q)uit: A// DD

Visit Date: 122519

(F)REE,(B)ILLED, or (V)isit Only: BILLED

Bill Number: ON HOLD

Is the above information correct? : YES

Enter RETURN to continue or '^' to exit.:

<u>Edit an Urgent Care Visit</u>

Select Urgent Care Visit Tracking Menu \<TEST ACCOUNT\> Option: UCVM Urgent Care Visit Tracking Maintenance

Select PATIENT NAME: Veteran, Air F X-X-XX 99999999 NO NSC VETERAN CD

Enrollment Priority: GROUP 8c Category: ENROLLED End Date:

Enter Year: 2019// 2019

Urgent Care Visits in 2019 for VETERAN, Air Force 999-99-9XXX

=============================================================================

1 Jun 06, 2019 F 7 Aug 15, 2019 13 Sep 03, 2019

2 Jun 28, 2019 8 Aug 16, 2019 14 Sep 04, 2019 V

3 Jul 03, 2019 F 9 Aug 17, 2019 15 Nov 13, 2019 R

4 Jul 05, 2019 F 10 Aug 19, 2019 16 Nov 21, 2019

5 Aug 01, 2019 R 11 Aug 21, 2019 17 Dec 01, 2019

6 Aug 14, 2019 12 Sep 02, 2019 18 Dec 20, 2019

(A)dd an Urgent Care Visit, (E)dit an existing Visit, or (Q)uit: ED Edit

Enter Visit Number: 10

Date of Visit Station Status Bill No. Reason

------------- ------- ------ -------- ------

Aug 19, 2019 XXX-CHEYENNE VAMC BILLED

(F)REE,(B)ILLED,(R)emoved, or (V)isit Only: VISIT ONLY

Is the above information correct? : YES

Enter RETURN to continue or '^' to exit.

<u>Override for an Urgent Care Visit</u>

Select Urgent Care Visit Tracking Menu \<TEST ACCOUNT\> Option: UCVM Urgent Care Visit Tracking Maintenance

Select PATIENT NAME: Veteran, Air F X-X-XX 99999999 NO NSC VETERAN CD

Enrollment Priority: GROUP 8c Category: ENROLLED End Date:

Enter Year: 2019// 2019

Urgent Care Visits in 2019 for VETERAN, Air Force 999-99-9XXX

=============================================================================

1 Jun 06, 2019 7 Aug 15, 2019 13 Sep 03, 2019

2 Jun 28, 2019 8 Aug 16, 2019 14 Sep 04, 2019 V

3 Jul 03, 2019 9 Aug 17, 2019 15 Nov 13, 2019 R

4 Jul 05, 2019 10 Aug 19, 2019 16 Nov 21, 2019

5 Aug 01, 2019 R 11 Aug 21, 2019 17 Dec 01, 2019

6 Aug 14, 2019 12 Sep 02, 2019 18 Dec 20, 2019 F

(A)dd an Urgent Care Visit, (E)dit an existing Visit, or (Q)uit: ADD

Visit Date: 122019

(F)REE,(B)ILLED, or (V)isit Only: FREE

This Veteran is not eligible for a Free Visit. Do you wish to Override?: YES

Are you sure? YES

Is the above information correct?: YES

Enter RETURN to continue or '^' to exit.:

### Urgent Care Visit Tracking Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report lists all Urgent Care visits for a patient during selected calendar year(s) with a visit date within the specified year.

Sample Output

Select Urgent Care Visit Tracking Menu \<TEST ACCOUNT\> Option: ucql Urgent Care

Visit Tracking Inquiry

Select PATIENT NAME: PPPPPP,VVVVV JJJJJ PPPPPP,VVVVV JJJJJ

11-30-57 XXXXXXXXX NO NSC VETERAN C

Enrollment Priority: GROUP 6 Category: ENROLLED End Date:

Start YEAR: : 2019// 2019

Go to YEAR: : 2019// 2022 2022

DEVICE: HOME// HOME (CRT)

Urgent Care Visit Profile for PPPPPP,VVVVV JJJJJ

From 2019 through 2022 Mar 07, 2023@15:04 Page: 1

VISIT DATE SITE STATUS BILL NO. REASON

-------------------------------------------------------------------------------

2022

----

Jan 05, 2022 WHITE RIVER JCT VA REMOVED Entered in Error

Feb 01, 2022 WHITE RIVER JCT VA REMOVED Entered in Error

Feb 02, 2022 WHITE RIVER JCT VA REMOVED Entered in Error

Feb 05, 2022 WHITE RIVER JCT VA FREE MISSION Act

Feb 10, 2022 WHITE RIVER JCT VA BILLED 405-K234BAZ

Mar 01, 2022 WHITE RIVER JCT VA BILLED 405-K234BAV

End of the report. Enter RETURN to continue or '^' to exit:

### Urgent Care Visit Summary / Detail Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report lists all Urgent Care visits for a Veterans Administration Medical Center (VAMC) by month and patient during a specific selected period in either summary (Monthly) or detailed (Monthly by patient) format. Both reports will display data for the current VAMC or include visits for patients made at another VAMC that are enrolled at the current VAMC.

Sample Output

Type '^' to stop, or choose a number from 1 to 4 :1 Urgent Care Visit Summary/Detail Report

You have 2 bill(s) pending approval.

Start with DATE: Jan 01, 2020// 010120 (Jan 01, 2020)

Go to DATE: Feb 29, 2020// T (Feb 05, 2020)

(S)ummary or (D)etailed Report: S// DETAILED

(C)urrent or (A)ll Sites: A// ALL SITES

Export the report to Microsoft Excel (Y/N)? NO//

DEVICE: HOME// HOME (CRT) Right Margin: 80//

URGENT CARE VISIT TRACKING DETAIL REPORT

FOR ALL SITES

From 01/01/20 through 02/29/20 Feb 05, 2020@13:02 Page: 1

TOTAL REMOVED VISITS UNIQUE

MONTH YEAR VISITS FREE BILLED VISITS ONLY PATIENTS

-----------------------------------------------------------------------------

JANUARY 2020 22 7 12 3 0 11

AVETERAN,Marine 2 0 2 0 0

BVETERAN,Army 2 2 0 0 0

CVETERAN,Navy 1 1 0 0 0

DVETERAN,Air Force 2 2 0 0 0

EVETERAN,Coast G 1 0 1 0 0

FVETERAN,Vietnam 1 0 1 0 0

GVETERAN,Korea 2 2 0 0 0

HVETERAN,German 1 0 0 1 0

IVETERAN,Japanese 8 0 7 1 0

JVETERAN,Tuskegee 1 0 1 0 0

KVETERAN,Women 1 0 0 1 0

FEBRUARY 2020 5 3 1 0 1 2

AVETERAN,Marine 3 3 0 0 0

BVETERAN,Army 2 0 1 0 1

-----------------------------------------------------------------------------

REPORT TOTALS 27 10 13 3 1 12

\*The total unique patient number only counts a patient once for the period

of the report.

End of the report. Enter RETURN to continue or '^' to exit:

Type '^' to stop, or choose a number from 1 to 5 :2 Urgent Care Visit Summary/Detail Report

You have 2 bill(s) pending approval.

Start with DATE: Feb 01, 2020// 100119 (Oct 01, 2019)

Go to DATE: Feb 29, 2020// (Feb 29, 2020)

(S)ummary or (D)etailed Report: S// SUMMARY

(C)urrent or (A)ll Sites: A// LL SITES

Export the report to Microsoft Excel (Y/N)? NO//

Report requires 132 columns.

DEVICE: HOME// HOME (CRT) Right Margin: 80// 132

URGENT CARE VISIT TRACKING SUMMARY REPORT

FOR ALL SITES

From 10/01/19 through 02/29/20 Feb 05, 2020@13:17 Page: 1

TOTAL REMOVED VISITS UNIQUE

MONTH YEAR VISITS FREE BILLED VISITS ONLY PATIENTS

-----------------------------------------------------------------------------

OCTOBER 2019 21 0 19 2 0 12

NOVEMBER 2019 16 0 12 4 0 7

DECEMBER 2019 57 12 25 18 2 16

JANUARY 2020 22 7 12 3 0 11

FEBRUARY 2020 5 3 1 0 1 2

-----------------------------------------------------------------------------

REPORT TOTALS 121 22 69 27 3 34

\*The total unique patient number only counts a patient once for the period

of the report.

End of the report. Enter RETURN to continue or '^' to exit:

### Urgent Care Pull Request by Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Urgent Care Pull Request by Patient allows Facility Revenue to request an account update for a single patient that has not received care through the facility previously. The option is only to be used if the normal nightly update is not completed or data is required immediately. This is a real-time request and will engage the VistA session until completed.

Sample Output

Select Core Applications \<TEST ACCOUNT\> Option: ^URGENT

1 Urgent Care Pull Request by Patient \[IBUC MULTI FAC COPAY PULL REQ\]

2 Urgent Care Visit Summary/Detail Report \[IBUC VISIT REPORT\]

3 Urgent Care Visit Tracking Menu \[IBUC MAIN MENU\]

4 Urgent Care Visit Tracking Inquiry \[IBUC VISIT INQUIRE\]

5 Urgent Care Visit Tracking Maintenance \[IBUC VISIT MAINT\]

Type '^' to stop, or choose a number from 1 to 5 :1 Urgent Care Pull Request by

Patient

You have 2 bill(s) pending approval.

Select PATIENT NAME: VETERAN,MARINE CORPS 9-9-99 99999999 NO NSC VETERAN CD

Enrollment Priority: GROUP 8c Category: ENROLLED End Date:

Now sending query to CHEYENNE VAMC ...

Now sending query to PHILADELPHIA, PA VAMC ...

## On Hold Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### On Hold Charges Released to AR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report lists all charges identified as once being ON HOLD (after the installation of patch IB\*2\*70) that currently have a status of BILLED, and the DATE LAST UPDATED is within the specified date range.

Sample Output

List of ON HOLD Charges released to AR between JAN 09, 1998 and MAR 10, 1998

Date Printed: MAR 10,1998 Page 1

-----------------------------------------------------------------------------

Name Pt.ID Act.ID Bill \# Type From To Charge

-----------------------------------------------------------------------------

IBpatient,one XXXX XXXXXX XXXXXXX OPT 08/30/94 08/30/94 36.00

IBpatient,two XXXX XXXXXXX XXXXXXX OPT 02/07/96 02/07/96 41.00

IBpatient,three XXXX XXXXXX XXXXXXX OPT 01/25/95 01/25/95 39.00

IBpatient,four XXXX XXXXXX XXXXXXX OPT 05/02/94 05/02/94 36.00

IBpatient,five XXXX XXXXXXX XXXXXXX OPT 05/14/96 05/14/96 41.00

XXXXXXX XXXXXXX INPT 01/21/97 01/21/97 736.00

IBpatient,six XXXX 500680 XXXXXXX INPT 07/15/94 07/15/94 696.00

XXXXXX XXXXXXX INPT 10/13/94 10/13/94 348.00

XXXXXX XXXXXXX NHCU 11/09/94 11/10/94 348.00

### Count / Dollar Amount of Charges on Hold

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces the Count and Dollar Amount of Charges on Hold Report. The report provides a subtotal and sub count, by action type, of each patient charge with an ON HOLD status. These charges have not been passed to Accounts Receivable. Accounting is responsible for supplying these figures to FMS monthly.

### Days on Hold Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces the Days on Hold Report. The report lists all Integrated Billing charges that have had a status of ON HOLD for an extended period.

Sample Output

CHARGES ON HOLD LONGER THAN 60 DAYS Mar 10, 1998@11:42:06 PAGE 1

HELD CHARGES CORRESPONDING THIRD PARTY BILLS

===============================================================================================\|\|================================

On Hold \# Days \|\| AR

Name Pt.ID Act.ID Type From To Date On Hold Charge\|\| Bill# Status Charge Paid

===============================================================================================\|\|================================

IBpatient,one XXXXX XXXXXXX INPT 04/10/97 04/10/97 08/11/97 88 368.00\|\|

XXXXXXX INPT 07/14/97 07/15/97 08/11/97 88 736.00\|\|

## Held Charges Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Held Charges Report provides the user with a list of all charges with a status of ON HOLD. Charges for Category C patients with insurance are placed on hold until the patient's insurance company bill is resolved. When payment is received from the insurance carrier, the status of the charge is updated through the Release Charges 'On Hold' option.

This report can be used to ensure that there is an insurance bill established for each charge on hold, and to identify charges that should be released when payments are received from insurance carriers.

Sample Output

CATEGORY C CHARGES ON HOLD MAR 10,1998 PAGE 1

HELD CHARGES CORRESPONDING THIRD PARTY BILLS

=====================================================================================\|\|=====================================

Name Pt.ID Act.ID Type Bill# From To Charge \|\| Bill# AR-Status Charge Paid

=====================================================================================\|\|=====================================

=====================================================================================\|\|=====================================

IBpatient,one 1111 XXXXXX OPT XXXXXX 03/01/92 03/11/92 30.00 \|\| XXXXXX NEW BILL 148.00 0.00

XXXXXX INPT XXXXXX 03/11/92 03/14/92 652.00 \|\|

XXXXXX OPT XXXXXX 03/11/92 03/11/92 30.00 \|\|

IBpatient,two 2222 XXXXXXX OPT XXXXXX 05/08/92 05/08/92 30.00 \|\|

IBpatient,three 3333 XXXXXXX OPT XXXXXX 04/07/92 04/07/92 30.00 \|\|

XXXXXXX OPT XXXXXX 04/03/92 04/03/92 30.00 \|\| XXXXXX NEW BILL 296.00 0.0

IBpatient,four 4444 XXXXXXX INPT XXXXXX 05/19/92 05/19/92 238.00 \|\|

IBpatient,five 5555 XXXXXXX INPT XXXXXX 03/01/92 03/01/92 652.00 \|\| XXXXXX NEW BILL 5736.00 0.00

IBpatient,six 6666 XXXXXXX INPT XXXXXX 04/13/92 04/16/92 652.00 \|\|

IBpatient,seven 7777 XXXXXXX OPT XXXXXX 03/23/92 03/23/92 30.00 \|\| XXXXXX NEW BILL 740.00 0.00

XXXXXXX OPT XXXXXX 03/23/92 03/23/92 30.00 \|\|

XXXXXXX OPT XXXXXX 03/23/92 03/23/92 30.00 \|\|

XXXXXXX OPT XXXXXX 03/23/92 03/23/92 30.00 \|\|

XXXXXXX OPT L10121 03/23/92 03/23/92 30.00 \|\|

CATEGORY C CHARGES ON HOLD MAR 10,1998 PAGE 1

HELD CHARGES CORRESPONDING THIRD PARTY BILLS

=====================================================================================\|\|========================================

Name Pt.ID Act.ID Type Bill# From To Charge \|\| Bill# AR-Status Charge Paid

=====================================================================================\|\|========================================

=====================================================================================\|\|========================================

IBpatient,one XXXX Insurance Co. Subscriber ID Group Eff Dt Exp Dt

=====================================================================================\|\|========================================

BLUE CROSS/BLUE XXXXXX MAN32 01/00/93

Plan Coverage Effective Date Covered? Limit Comments

------------- -------------- -------- --------------

INPATIENT BY DEFAULT

OUTPATIENT BY DEFAULT

PHARMACY BY DEFAULT

DENTAL BY DEFAULT

MENTAL HEALTH BY DEFAULT

LONG TERM CARE BY DEFAULT

PROSTHETICS BY DEFAULT

VISION BY DEFAULT

----------------------------------------------------------------------------

XXXXXXX OPT 03/02/98 03/02/98 45.80 \|\|

### History of Held Charges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a count and dollar amount of charges that have been on hold for a specified date range. This report sorts charges by current status. The user will be able to keep track of how many charges are canceled, released (billed), or remain on hold. This report only counts charges with an ON HOLD DATE defined.

### Release Charges 'On Hold'

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB AUTHORIZE security key is required to access this option.

The Release Charges 'On Hold' option is used to release Means Test Category C charges, with a status of ON HOLD, to Accounts Receivable. This option is also available on the Agent Cashier's Menu in Accounts Receivable.

If the HOLD MT BILL W/INS parameter is set to YES, inpatient and outpatient copayments for Category C patients with insurance will automatically be placed on hold. These charges will not be passed to Accounts Receivable until released through this option.

7.  The \$5/\$10 hospital/NHCU per diem charges are not placed on hold.

If the original bill number is no longer open when the charge is passed to Accounts Receivable, a new bill number is assigned.

### List Charges Awaiting New Copay Rate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Charges Awaiting New Copay Rate option is used to generate a list of all Means Test outpatient copayment charges that have been placed on hold because the copay rate is over one year old.

New billing rates are scheduled to be released from VA Central Office at the beginning of each fiscal year (10/1). However, there may be a delay in the release of these new rates. If the rate on file for the Means Test outpatient copayment charge is over one year old at the time the bill is created, these charges will be held until the new copay rate is entered. When the rate is entered, the user is given the opportunity to release the charges to Accounts Receivable at that time or released through the Release Charges Awaiting New Copay Rate option.

Sample Output

LIST OF ALL OUTPATIENT COPAYMENT CHARGES 'ON HOLD'

AWAITING ENTRY OF THE NEW COPAYMENT RATE

Page: 1

Run Date: 10/18/93

-----------------------------------------------------------------------------

Patient Name (ID) Visit Date Charge

-----------------------------------------------------------------------------

IBpatient,one (1111) 10/08/93 \$33

IBpatient,two (2222) 10/12/93 \$33

IBpatient,three (3333) 10/05/93 \$33

10/04/93 \$33

IBpatient,four (4444) 10/01/93 \$33

IBpatient,five (5555) 10/05/93 \$33

### Send Converted Charges to A/R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB AUTHORIZE security key is required to access this option.

This option is designed for use after the Integrated Billing conversion is completed. After the conversion, certain inpatient and outpatient charges will have a status of CONVERTED. This option allows the user to choose which converted charges are passed to Accounts Receivable.

During the conversion, the BILLS/CLAIMS file (#399) is checked to ensure that each outpatient visit has been billed. For each visit without an established bill, one is established and given a status of CONVERTED. The conversion cannot determine whether an episode of care has been billed for inpatients; therefore, all billable inpatient episodes are provided a status of CONVERTED and the user must determine which ones should be passed.

The user can choose to pass the charges by patient or date. If patient is selected, all billing actions with a status of CONVERTED are displayed. The user can then select which actions will be passed to accounts receivable. If date is selected, all outpatient copay and fee service billing actions that were created on or before the selected date are passed to accounts receivable.

If the HOLD MT BILL W/INS parameter at the site is set to YES, inpatient and outpatient copayments for Category C patients with insurance will automatically be placed on hold. These charges will not be passed to Accounts Receivable until released through the Release Charges 'On Hold' or Cancel/Edit/Add Patient Charges options. The user may wish to set this parameter to NO until all charges that should be passed to A/R are passed.

This option is being distributed as out of order, as it is no longer needed, and will be deleted in the next release of Integrated Billing.

### Release Charges 'Pending Review'

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release Charges 'Pending Review' option is used to review charges that have been created when an Income Verification Match (IVM) verified Means Test has been received and filed at the medical facility. If such a Means Test results in changing the patient's Means Test status from Category A to Category C, copayment and per diem charges for previous episodes of care will automatically be created. The charges will not be automatically passed to Accounts Receivable but will be held in Billing until a review of the charges is complete. A mail message is sent to the Category C Billing mail group notifying users that the charges have been created and are pending review.

After review, the user may pass on the charges to Accounts Receivable for billing or cancel the charges. If passed to AR, the billing information will also be passed to the IVM software that will in turn transmit it to the IVM Center in Atlanta.

Since the billing clock was updated when the charge was originally built, the user may need to update the billing clock if the charge is canceled. This can be accomplished through the Patient Billing Clock Maintenance option.

### List Current / Past Held Charges by Pt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists all IB Actions for a patient that are currently on hold or were on hold for a specified date range. The report lists IB Action ID, Rate Type, Bill \#, AR status, IB Status, and information related to corresponding Third-Party Claims. Only charges placed on hold since the installation of patch IB\*2\*70 will appear on this report.

Sample Output

Select On Hold Menu \<TEST ACCOUNT\> Option: PT List Current/Past Held Charges by

Pt

Select PATIENT NAME: FFFF,PPPP LLL FFFF,PPPP LLL 12-17-50 XXXXXXXXX

NO NSC VETERAN C

Enrollment Priority: GROUP 5 Category: ENROLLED End Date:

Start with DATE: 010123 (JAN 01, 2023)

Go to DATE: T (JUN 26, 2023)

Include Pharmacy Co-pay charges on this report? NO// Y YES

\*\*\* Margin width of this output is 132 \*\*\*

\*\*\* This output should be queued \*\*\*

DEVICE: HOME// 0;132 HOME (CRT)

List of all HELD bills for FFFF,PPPP LLL JUN 26,2023 PAGE 1

PATIENT CHARGES CORRESPONDING THIRD PARTY BILLS

=====================================================================================\|\|==========================================

From/ Date AR IB \|\| AR

Action ID Type Bill# Fill Dt to AR Charge Status Status\|\| Bill# Classf(\$Typ) ST Charge % Paid

=====================================================================================\|\|==========================================

'\*' = outpt visit on same day as Rx fill date \|\|

=====================================================================================\|\|==========================================

4053571534 LTC IN 05/31/23 576.00 ON HOL\|\|

4053571332 LTC IN 04/30/23 596.00 ON HOL\|\|

4053571261 LTC IN 03/31/23 576.00 ON HOL\|\|

4053571164 LTC IN K305B3E 02/28/23 05/31/23 636.00 ACTIVE BILLED\|\|

4053571159 LTC IN K304W31 01/31/23 05/03/23 576.00 ACTIVE BILLED\|\|

4053571063 LTC IN K304RGR 12/31/22 04/02/23 576.00 ACTIVE BILLED\|\|

### Release Charges Awaiting New Copay Rate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release Charges Awaiting New Copay Rate option is used to release charges that have been placed on hold because the outpatient copay rate is over one year old.

New billing rates are scheduled to be released from VA Central Office at the beginning of each fiscal year (10/1). However, there may be a delay in the release of these new rates. If the rate on file for the Means Test outpatient copayment charge is over one year old at the time the bill is created, these charges will be held until the new copay rate is entered. When the rate is entered, the user is given the opportunity to release the charges to Accounts Receivable at that time or released through this option. The user will be prompted to task off a job that will automatically update the dollar amount and bill all such charges. The user will receive a message when the tasked job has been completed.

If the copay rate currently in the Billing Table is too old to use, the following message will appear:

> The current copay rate (effective \[date\]) is still too old to use. Please be sure that you have entered the most current rate in your Billing Rates table.

### Patient Billing Clock Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to display data contained in the patient billing clock. It can be used to view the number of inpatient days and the amount billed for inpatient copayments for Category C patients.

When the patient is selected, all billing clocks for that patient are displayed. The reference number, patient name, and the cycle begin date are provided. Once a clock is selected, information such as the clock status, primary eligibility code, cycle begin and end dates, number of inpatient days, and 90-day inpatient amounts are displayed.

Sample Output

Select Automated Means Test Billing Menu \<TEST ACCOUNT\> Option: INQC Patient Billing

Clock Inquiry

Select MT Billing Clock by PATIENT NAME: AAAAAAAA,EEE 44275194 AAAAAAAA,EEEEEE DDDDD

02-01-22 CURRENT

DEVICE: HOME// HOME (CRT) Right Margin: 80//

AAAAAAAA,EEEEEE DDDD 09/08/1934 NSC VETERAN

================================================================================

Reference Number: 44275194

Status: CURRENT

Primary Elig. Code: NSC

Clock Begin Date: FEB 1,2022

Clock End Date:

Number Inpatient Days: 1

90 Day Inpatient Amounts

1st 90 Day Amount:

2nd 90 Day Amount:

3rd 90 Day Amount:

4th 90 Day Amount:

Date Entry Added: MAR 31,2022

Date Last Updated: OCT 31,2022

Update Reason:

Type \<Enter\> to continue or '^' to exit:

Select MT Billing Clock by PATIENT NAME:

### Category C Billing Activity List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Category C Billing Activity List option is used to list all Means Test/Category C charges within a specified date range. The list is alphabetical by patient name.

This output provides the patient’s name and ID, a brief description, the status and the billing period for the bill, the units (the number of days a charge occurred), and the amount of the charge. For inpatient copay charges, the description includes the treating specialty for the episode of care.

As stated above, the units reflect the number of days a charge occurred. For inpatient copay charges the unit will always be one, even if the patient accrued the charges over several days before the Medicaid deductible was met.

Sample Output

Category C Billing Activity List FEB 26, 1992@09:14:28 Page: 1

Charges from 01/01/92 through 02/26/92

PATIENT/ID DESCRIPTION STATUS FROM TO UNITS CHARGE

--------------------------------------------------------------------------------------

IBpatient,one XXXX INPT PER DIEM BILLED 01/02/92 01/03/92 2 \$20.00

INPT COPAY (ALC) BILLED 01/02/92 01/03/92 1 \$476.00

IBpatient,two XXXX OPT COPAY PENDING A/R 02/11/92 02/11/92 1 \$0.00

IBpatient,three XXXX INPT PER DIEM BILLED 01/13/92 01/14/92 2 \$20.00

INPT COPAY (MED) BILLED 01/13/92 01/14/92 1 \$652.00

IBpatient,four XXXX OPT COPAY PENDING A/R 02/12/92 02/12/92 1 \$0.00

IBpatient,five XXXX OPT COPAY BILLED 02/17/92 02/17/92 1 \$30.00

IBpatient,six XXXX OPT COPAY BILLED 02/13/92 02/13/92 1 \$30.00

IBpatient,seven XXXX INPT PER DIEM BILLED 01/13/91 01/18/92 6 \$60.00

INPT COPAY (MED) BILLED 01/13/92 01/18/92 1 \$24.00

IBpatient,eight XXXX OPT COPAY BILLED 02/12/92 02/12/92 1 \$30.00

### Single Patient Means Test Billing Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Single Patient Means Test Billing Profile option provides a list of all Means Test/Category C charges within a specified date range for a selected patient.

The user will be prompted for the patient name, date range, and device. The default at the Start with DATE prompt is October 1, 1990. This is the earliest date for which charges can be displayed.

This output displays the date the Means Test billing clock began, the bill date, the bill type (including the treating specialty for inpatient copay charges), the bill number, the bill to date (for inpatient charges), the amount of each charge, and the total charges for the selected date range.

Sample Output

Means Test Billing Profile for Test,Name

From 01/01/14 through 10/29/19 OCT 29, 2019@08:54 Page: 1

BILL DATE BILL TYPE BILL \# BILL TO TOT CHARGE

-----------------------------------------------------------------------------------------------

05/22/12 Begin Means Test Billing Clock

12/30/14 Begin Means Test Billing Clock

12/30/14 OUTPATIENT COPAY XXXXXXX \$15.00

12/31/14 OUTPATIENT COPAY XXXXXXX \$15.00

01/06/15 OUTPATIENT COPAY XXXXXXX \$15.00

01/13/15 OUTPATIENT COPAY XXXXXXX \$15.00

01/14/15 OUTPATIENT COPAY XXXXXXX \$15.00

01/14/15 FEE SERVICE/INPATIENT XXXXXXX 01/17/15 \$243.20 \*

01/14/15 FEE SERV INPT PER DIEM XXXXXXX 01/17/15 \$6.00 \*

01/14/15 FEE SERVICE/INPATIENT XXXXXXX 01/17/15 (\$243.20) \*

Charge Removal Reason: ENTERED IN ERROR

01/14/15 FEE SERV INPT PER DIEM XXXXXXX 01/17/15 (\$6.00) \*

Charge Removal Reason: ENTERED IN ERROR

01/14/15 CC INPATIENT XXXXXXX 01/15/15 \$25.00 \*

01/14/15 CC PER DIEM XXXXXXX 12/29/15 \$698.00 \*

01/14/15 CC PER DIEM XXXXXXX 01/15/15 \$2.00 \*

\*\*\*\*\*\*\*\*\*\*Bills display continue on several pages\*\*\*\*\*\*\*\*\*\*

07/01/15 CCN PER DIEM XXXXXXX 07/31/15 (\$60.00) \*

Charge Removal Reason: ELIGIBILITY INCORRECT

08/01/15 CC MTF PER DIEM XXXXXXX 08/31/15 \$60.00 \*

08/01/15 CC MTF PER DIEM XXXXXXX 08/31/15 (\$60.00) \*

Charge Removal Reason: CHANGE IN ELIGIBILITY

09/01/15 CHOICE PER DIEM XXXXXXX 09/30/15 \$58.00 \*

09/01/15 CHOICE PER DIEM XXXXXXX 09/30/15 (\$58.00) \*

Charge Removal Reason: ENTERED IN ERROR

12/15/18 CC RX COPAY XXXXXXX \$8.00

12/15/18 CC RX COPAY XXXXXXX (\$8.00)

Charge Removal Reason: ENTERED IN ERROR

06/06/19 CC URGENT CARE XXXXXXX \$30.00

06/06/19 CC URGENT CARE T002X25 (\$30.00)

Charge Removal Reason: UC - CHANGE IN ELIGIBILITY

09/02/19 CC OUTPATIENT XXXXXXX \$15.00

09/02/19 CC OUTPATIENT XXXXXXX (\$15.00)

Charge Removal Reason: ELIGIBILITY INCORRECT

'\*' - Geographic Means Test rates

----------\$303.00

### Disposition Special Inpatient Billing Cases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Disposition Special Inpatient Billing Cases option is used to enter the reason for not billing inpatient billing cases for Veterans whose care is related to exposure to Agent Orange, ionizing radiation, or environmental contaminants. This option can also be used to edit the reason on cases that have already been dispositioned.

Inpatient bills created for Veterans who claim exposure to Agent Orange, ionizing radiation, or environmental contaminants are automatically placed on hold. Once the Veteran's treatment has been completed and s/he is discharged, a determination needs to be made if in fact the care rendered was related to the claimed exposure. If the case was not related, charges will have to be entered through the Cancel/Edit/Add Patient Charges option and passed to Accounts Receivable for billing. If the care was related, the patient will not be billed, and the case will be dispositioned after the reason for not billing is entered through this option.

The user will be prompted for the patient’s name. The following information will be displayed for the case record: patient name, type, admission date, discharge date, care related to exposure (yes/no), case dispositioned (yes/no), date record last edited, and edited by. The user will then be prompted for the reason the case was not billed. This is a free text field allowing up to 80 characters.

### List Special Inpatient Billing Cases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Special Inpatient Billing Cases option is used to provide a listing of all special inpatient billing cases, both dispositioned and un-dispositioned. Special inpatient billing cases are those where the Veteran has claimed his need for treatment is related to exposure to Agent Orange, ionizing radiation, or environmental contaminants.

Inpatient care for NSC Category C Veterans who claim exposure to Agent Orange, ionizing radiation, or environmental contaminants is not automatically billed. Once the Veteran's treatment has been completed and s/he is discharged, a determination needs to be made if in fact the care rendered was related to the claimed exposure. If the care was related, the patient should not be billed, and the case should be dispositioned through the Disposition Special Inpatient Billing Cases option. If the case was not related to exposure, charges will have to be entered manually through the Cancel/Edit/Add Patient Charges option and passed to Accounts Receivable for billing. If the case is billed, the system automatically dispositions the special case.

The following information may be displayed for each case record on the output: patient name, type, admission date, discharge date, care related to exposure (yes/no), case dispositioned (yes/no), date record last edited, and edited by.

Sample Output

LIST ALL SPECIAL INPATIENT BILLING CASES

Page: 1

Run Date: 10/20/93

-----------------------------------------------------------------------------

Pt. Name: IBpatient,one (1111) Care related to EC: NO

Type: ENV CONTAMINANT Case Dispositioned: YES

Adm Date: 11/17/93 2:23 pm Date Last Edited: 11/22/93 10:04 am

Disc Date: 11/22/93 9:52 am Last Edited By: JOHN

-----------------------------------------------------------------------------

Charges Billed:

INPT COPAY (MED) NEW 11/17/93 11/17/93 \$676 BILLED

INPT PER DIEM NEW 11/17/93 11/21/93 \$40 BILLED

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

Pt. Name: IBpatient,one (1111) Care related to AO: YES

Type: AGENT ORANGE Case Dispositioned: YES

Adm Date: 10/03/93 10:10 pm Date Last Edited: 10/20/93 7:46 am

Disc Date: 10/06/93 2:25 pm Last Edited By: JANE

-----------------------------------------------------------------------------

Reason for Non-Billing:

TREATMENT FOR AGENT ORANGE

-----------------------------------------------------------------------------

## CHAMPUS Billing Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Delete Reject Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to delete individual entries from the Civilian Health and Medical Program of the Uniformed Services (CHAMPUS) PHARMACY REJECTS (#351.52) file. Entries are automatically deleted from this file when a rejected transmission is re-submitted and subsequently approved. However, there will be instances when rejected transmissions will not be re-submitted. Therefore, this option may be used to purge unwanted rejected transactions from the file.

### Reject Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reject Report allows the user to view all the entries in the CHAMPUS PHARMACY REJECTS (#351.52) file and determine the reason(s) for the rejected entries. Rejected entries for transactions that will not be re-submitted and continue to be displayed on this report may be deleted using the Delete Reject Entry option.

Sample Output

=============================================================================

Date: 05/30/97 IPS Unresolved Reject Report Page: 1

=============================================================================

RX# XXXXXX, filled on 09/10/96 (IBpatient,one XXXXXXXX) rejected because:

Invalid NDC Number

Missing/Invalid Insurance data

NDC not in local AWP file

Call Failed

RX# XXXXXX, filled on 02/03/94 (IBpatient,one XXXXXXXX) rejected because:

Modem is not Responding

Bad/Invalid baud Rate Setting

Call Interrupted by User

Bad/Invalid Data bits Setting

### Resubmit a Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to re-submit a transaction that was originally rejected by the FI (Fiscal Intermediary – the company with which a Tricare patient holds Tricare insurance coverage). The user can select a prescription that has not been submitted for billing or was submitted and then rejected. The prescription is then placed in the queue to be processed by the IB background filer, and it is processed in the same manner as prescriptions that are queued by the foreground processor. If the prescription was previously submitted and rejected, the reject entry in file \#351.52 will automatically be deleted if the prescription is authorized for billing.

### Reverse a Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may be used to reverse or cancel a claim for a prescription that was submitted in error. The user can select a prescription that was previously billed. The prescription is then placed in the queue to be processed by the IB background filer. The filer creates a cancellation-type transaction message that is transmitted to the RNA package. When the receipt confirmation has been received by Veterans Health Information System and Technology Architecture (VistA) from the Fiscal Intermediary (FI), through RNA, another job is queued that cancels the patient copayment charge and the claim for the FI.

### Transmission Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transmission report allows the user to view a list of pharmacy transmissions for prescriptions that were filled during a specified date range.

Sample Output

Date: 05/30/97 IPS Prescription Status Report Page: 1

JAN 1,1996 through MAY 30,1997

RX# Fill Date Patient Name Patient SSN

NDC AWP Copay Ing Cost Fee Paid Total PD

Auth. \# Message

Reject Failure Codes

=============================================================================

XXXXXX 09/10/96 IBpatient,one XXXXXXXX

Drug Name: PRESAMINE 50MG TABS

Status: Rejected

Invalid NDC Number

Missing/Invalid Insurance data

NDC not in local AWP file

Call Failed

### IB MT FIX / DISCH Special Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will update records in the Special Inpatient Billing Cases File (#351.2) with discharge dates if any exist in the Patient Movement File (#405).

## Patient Billing Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Catastrophically Disabled Copay Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Catastrophically Disabled Copay Report option provides a list of charges for a specified date range that may need to be canceled due to a patient’s Catastrophically Disabled status. The Catastrophically Disabled legislation effective date is May 5, 2010. The user should not enter a date prior to that date; any date entered before that will be automatically changed to May 5, 2010. It should be queued to a printer off hours as it can take some time to run with at least a margin of 132 columns. The report is based on the Date of Decision date stored in the Patient (#2) file. Even though charges may be canceled, the report may continue to show \$0 charges. If the charge in IB is canceled but there are still charges on the AR side on the same bill number, it will continue to appear on the report. This is because there is no way of determining which charges on an AR bill are canceled vs. not canceled. Sites should not expect to see a clean report; the report is for informational purposes for review. After the review of a specified timeframe is completed, it is recommended sites use subsequent timeframes for review.

Sample Output:

Catastrophically Disabled Copayment Charge Report PAGE: 1

PATIENT SSN CD DATE DOS RX TYPE BILL NO STATUS BALANCE PD PRIN INT ADM TOP FUND RSC

-----------------------------------------------------------------------------------------------------------------------------------

IBPATIENT,ONE XXXX 03/01/11 03/25/11 DG OPT CO XXXXXXX BILLED 15.00 0.00 0.00 0.00 528703

IBPATIENT,TWO A XXXX 03/31/11 03/31/11 XXXXXX PSO NSC R XXXXXXX BILLED 64.00 0.00 0.00 0.00 528701

IBPATIENT,THREE XXXX 02/05/11 05/31/11 XXXXXX PSO NSC R XXXXXXX BILLED 64.00 0.00 0.00 0.00 528701

IBPATIENT,FOUR XXXX 03/21/11 03/31/11 DG OPT CO XXXXXXX BILLED 185.00 0.00 0.00 0.00 528703

### COMPACT Act Copay Review Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option identifies all copays that may be eligible for cancellation under the COMPACT Act of 2020. The COMPACT Act states that the VA may not charge the Veteran for medical visits which may have been the result of an Acute Suicide event. The report creates a list of bills that need review by Mental Health Revenue Utilization Review experts to determine if the Copayment qualifies for cancellation.

The User chooses the option, and then selects the starting and ending Copay Billed dates. Next, the User may sort the report by Division. If the User responds Yes, they may then choose One, Many (up to 20), or All Divisions. The User may also export the report output to Microsoft Excel. The report requires 132 columns for output. An example follows:

Select Patient Billing Reports Menu \<TEST ACCOUNT\> Option: CMPR COMPACT Act Copay Review Report

Start with Date Copay Billed : May 24, 2022// 112821 (NOV 28, 2021)

End with Date Copay Billed : May 31, 2022// (MAY 31, 2022)

\*\*\* Selected date range from Nov 28, 2021 to May 31, 2022 \*\*\*

Do you wish to sort this report by division? NO// YES

Select division: ALL// ??

ENTER:

\- Return for all divisions, or

\- A division and return when all divisions have been selected--limit 20

Imprecise selections will yield an additional prompt.

(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)

Choose from:

1 Main VAMC 999

2 CBOC 1 999GA

3 CBOC 2 999GZ

Select division: ALL// \<RET\>

\*\* This report can take a while to run and may be queued to run after hours. \*\*

> **NOTE:** Copay displays only if at least one COMPACT diagnosis is hit.

Export the report to Microsoft Excel (Y/N)? NO// \<RET\>

Report requires 132 columns.

DEVICE: 0;132 HOME (CRT)

COMPACT ACT Copay Review Report from Nov 28, 2021 to May 31, 2022 Date of Report: May 31, 2022 Page: 1

For Division(s) -

Patient Name ID Bill Number Stat Descr. Fill/Adm/DOS RX Number RX Name DX Proc. Amount (\$)

-----------------------------------------------------------------------------------------------------------------------------------

ACCCCCC,QQQQQQQ JJ A7557 405-K2006HT BILL DG OPT COPAY 20 Nov 2021 R45.851 99283 50.00

ACCCCCC,QQQQQQQ JJ A7557 405-K2006HV BILL DG OPT COPAY 30 Nov 2021 T14.91XA 99284 50.00

ADDDD,RRRRRRR A A1199 405-K200U3A BILL DG OPT COPAY 02 Oct 2021 T14.91XD 99283 50.00

ADDDD,RRRRRRR A A1199 405-K200U3B BILL DG OPT COPAY 03 Oct 2021 T14.91XS 99284 50.00

MMMMMM,BBBBBB AAA M5959 405-K200U38 BILL DG INPT PER 26 Nov 2021 R45.851 20.00

MMMMMM,BBBBBB AAA M5959 405-K201CZT BILL DG TRICARE I 26 Nov 2021 R45.851 450.00

MSSSSSS,CCCCCCC M4455 405-K2006I2 BILL DG OPT COPAY 01 Dec 2021 T14.91XA 99283 50.00

MSSSSSS,CCCCCCC M4455 405-K2006I3 BILL DG OPT COPAY 03 Dec 2021 R45.851 99283 50.00

Type \<Enter\> to continue or '^' to exit:

### Patient Currently Cont. Hospitalized since 1986

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to print a list (from the IB CONTINUOUS PATIENT file) of current inpatients continuously hospitalized at the same level of care since 1986. This report can be used to verify that all continuous patients are correctly identified. The margin width for this report is 132 columns.

Patients continuously hospitalized since 7/1/86 are exempt from the Medicare deductible copayments but may still be subject to per diem charges. Facilities are authorized to charge inpatients a per diem charge of \$10.00 a day for each day of inpatient care or \$5.00 for each day of NHCU care.

Sample Output

APR 28,1992 \*\*\*Patients Continuously Hospitalized Since July 1, 1986\*\*\* PAGE 1

Patient NAME Pt-Id Ward Location Last Means Means Test Eligibility

Test Date Status

=============================================================================================

IBpatient,one XXX-XX-XXXX 4D(NHCU) NSC

IBpatient,two XXX-XX-XXXX 4A(NHCU) 04/02/90 CATEGORY C NSC

IBpatient,three XXX-XX-XXXX 4B(NHCU) 02/18/92 CATEGORY C NSC

IBpatient,four 4B(NHCU) 02/18/92 CATEGORY C NSC

### Print IB Actions by Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print IB Actions by Date option provides a list of the Integrated Billing actions for a specified date range. Although totals are included, this output should not be used for statistical reporting. The Statistical Report option is provided for that purpose.

This output can be sorted by a specified field. \<??\> can be entered for a list of appropriate fields for selection and additional commands that may be used to customize the report. If the user opts to sort by a certain field, the user will be prompted to enter a range for that field. If the user accepts the default of FIRST, the system will:

Sample Output

INTEGRATED BILLING ACTION LIST APR 19,1991 10:34 PAGE 1

PATIENT REF. NO TYPE STATUS DATE ADDED UNITS CHARGE BRIEF DESCRIPTION CHARGE ID

------------------------------------------------------------------------------------------------------------------

IBpatient,one XXXXXX SC RX COPAY NEW BILLED APR 5,1991 1 2.00 322B-RANITIDINE 15-1 XXX-XXXXXX

IBpatient,two XXXXXX SC RX COPAY NEW BILLED APR 5,1991 1 2.00 230A-AMPICILLIN 50-1 XXX-XXXXXX

IBpatient,three XXXXXX NSC RX COPAY NEW BILLED APR 5,1991 1 2.00 193B-BELLADONNA TI-1 XXX-XXXXXX

IBpatient,four XXXXXX SC RX COPAY NEW BILLED APR 5,1991 3 6.00 357-BENZTROPINE 1M-3 XXX-XXXXXX

--------- ----- --------

SUBTOTAL 6 12.00

SUBCOUNT 4

IBpatient,one XXXXXX SC RX COPAY NEW CANCELLED APR 4,1991 1 2.00 352-AMPICILLIN 25, 1 XXX-XXXXXX

IBpatient,two XXXXXX SC RX COPAY NEW CANCELLED APR 4,1991 1 2.00 286A-CIMETIDINE 3, 1 XXX-XXXXXX

IBpatient,three XXXXXX SC RX COPAY NEW CANCELLED APR 4,1991 3 6.00 167A-ACETAMINOPHE, 3 XXX-XXXXXX

--------- ----- --------

SUBTOTAL 5 10.00

SUBCOUNT 3

--------- ----- --------

TOTAL 11 22.00

COUNT 7

### Employer Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Employer Report option is used to provide a listing of patients' and spouses' employers for patients without active insurance that can be used by billing clerks to confirm insurance coverage with those employers.

The report is sorted by employer name and is run for a selected date range. The user can run the report for inpatient admissions or outpatient visits. One, many, or all divisions can be chosen. For outpatients, patients are included on the report if the patient has an event within the specified date range, does not have active insurance on the event date, and the patient or spouse's employment status is one of the following:

- EMPLOYED FULL TIME
- EMPLOYED PART-TIME
- SELF EMPLOYED
- RETIRED

Events include admissions for inpatients and scheduled/unscheduled visits and dispositions that are not Application without Exam for outpatients.

Deceased Veterans do not appear on the report.

The following information may appear on the output: employer name, address, phone number, patient name, Social Security Number (SSN), occupation, employment status, home and work phone numbers, primary eligibility, admission date, transaction type, appointment date, and appointment type. This report requires a 132-column margin width.

Sample Output

EMPLOYER REPORT FOR INPATIENT ADMISSIONS JUN 1,1993 - OCT 21,1993 OCT 21, 1993 11:15 PAGE 1

---------------------------------------------------------------------------------------------------------------

ACME 4444 E KINDER RD, ANYTOWN, NEW YORK 12443

Patient: IBpatient,one XXX-XX-XXXX NSC JUN 10, 1993 ADMISSION Home:

Employed: Spouse: SPOUSE DAY CARE RETIRED

---------------------------------------------------------------------------------------------------------------

XYZ, INC. 518-5551234 5678 South St, ANYTOWN, New York 12345

Patient: IBpatient,three XXX-XX-XXX NSC JUN 10, 1993 ADMISSION Home: XXX-XXXXXXX

Employed: Patient: IBpatient,one XXX-XX-XXX Hertygertyman FULL TIME Work: XXX-XXXXXXX

---------------------------------------------------------------------------------------------------------------

XXX CORPORATION XXX-XX-XXXX 1 XXX LANE, ANYTOWN, NEW YORK 10045

Patient: IBpatient, two XXX-XX-XXXX SC 1 JUN 02, 1993 ADMISSION Home: XXX-XXXXXXX

Employed: Patient: IBpatient, two XXX-XX-XXXX Computer Operator FULL TIME Work: XXX-XXXXXXX

### Episode of Care Bill List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Episode of Care Bill List option is used to list all bills related to an episode of care. The bills are listed by event date in reverse date order. The bill number, rate type, bill classification, event date, statement from and to dates, bill status, and time frame of the bill will be displayed for each bill on the list.

The user may enter the bill number, event date, or patient name at the bill selection prompt. If the event date or patient name is entered, all bills with that event date or for that patient will be listed for selection. Only patients with bills on file may be entered.

8.  The output produced by this option must be generated at a 132-column margin width.

Sample Output

LIST OF ALL BILLS FOR AN EPISODE OF CARE JUL 5,1990@08:16 PAGE 1

FOR PATIENT: IBpatient,one EVENT DATE: FEB 13,1987

STATEMENT STATEMENT

BILL NO. RATE TYPE CLASSIFICATION EVENT DATE FROM DATE TO DATE STATUS TIMEFRAME OF BILL

---------------------------------------------------------------------------------------------------------------

XXXXXX MEANS TEST/CAT. C INPATIENT 02/13/87 02/13/87 03/12/87 PRINTED INTERIM - CONTINUING

PAYOR: Patient - IBpatient,one

XXXXXX REIMBURSABLE INS. INPATIENT 02/13/87 03/13/87 04/12/87 PRINTED INTERIM - CONTINUING

PAYOR: Insurance Co. - ABC INSURANCE

XXXXXX REIMBURSABLE INS. INPATIENT 02/13/87 04/13/87 04/30/87 AUTHORIZED INTERIM - LAST

PAYOR: Insurance Co. - ABC INSURANCE

### Estimate Means Test Charges for an Admission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to estimate the Means Test charges for an episode of hospital or nursing home care for a proposed length of stay. It may be used to answer patient inquiries pertaining to estimated charges to be billed for an inpatient stay.

The report will indicate whether the patient has an active billing clock, the start date, and the number of inpatient days of care within that clock.

If a patient has an active clock and has already been charged a copayment for the current 90 days of inpatient care, the amount that was billed is shown. Also provided is the amount of copay and per diem that would be billed for this proposed episode of care.

Sample Output

Select Automated Means Test Billing Menu \<TEST ACCOUNT\> Option: ESTM Estimate Means

Test Charges for an Admission

Select PATIENT NAME: AAAAAAAA,EEEEEE DDDDD 9-8-34 XXXXXXXXX NO

NSC VETERAN CD

Enrollment Priority: GROUP 8c Category: IN PROCESS End Date:

Please note that this patient was admitted on 05/07/22 and Means Test charges

have been calculated through 05/13/22.

Proposed DISCHARGE Date: 080822 (AUG 08, 2022)

DEVICE: HOME// HOME (CRT) Right Margin: 80//

Estimated Means Test Inpatient Charges for AAAAAAAA,EEEEEE DDDDD

Please note that this patient is a current inpatient.

Charges will be estimated from 05/14/22 through 08/08/22.

\*\* THIS PATIENT HAS AN ACTIVE BILLING CLOCK \*\*

Clock date: 02/01/22 Days of inpatient care within clock: 1

Copayments made for current 90 days of inpatient care: \$0.00

COPAYMENT CHARGES for GENERAL MEDICAL CARE

--------------------------------------------------------------------------------

Billing Dates Inpt. Days Clock Days

From To 1st Last 1st Last Charge

--------------------------------------------------------------------------------

05/14/22 05/14/22 2 2 103 103 \$1,556.00

----------

\$1,556.00

PER DIEM CHARGES for HOSPITAL CARE

--------------------------------------------------------------------------------

05/14/22 08/07/22 86 days @ \$10.00/day \$860.00

----------

Total Estimated Charges: \$2,416.00

Type \<Enter\> to continue or '^' to exit:

Select PATIENT NAME:

The table below describes the fields:

| Fields                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Clock Date                                            | Date the current billing clock began for this patient.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Days of Inpatient Care within Clock                   | Number of days of inpatient or nursing home care within the current billing clock.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Copayments made for Current 90 Days of Inpatient Care | Total amount of copayments made for the current 90 days of inpatient care for the current billing clock.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Copayment Charges for (type of care)                  | Amount of the copayment charge for this proposed inpatient stay. The copayment charge differs depending on the type of inpatient care; however, it will not exceed the current Medicare deductible. Once the deductible is met, the patient is covered for 90 days of hospital care. For the second, third, and fourth 90 days of hospital care, the copayment charge is half of the current Medicaid deductible. For other than hospital care (i.e., NHCU), the full deductible applies for each 90 days of care. |
| Billing Dates (from/to)                               | Date(s) the copayment occurred. If the proposed episode of care was for a total of five days (2/1/92 – 2/5/92), but the deductible was met the first day; the billing dates (from and to) would reflect the first day only (2/1/92).                                                                                                                                                                                                                                                                               |
| Inpatient Days (1st/Last)                             | On which days of the current 90 days of inpatient care this copayment occurred. If the patient previously had two days of inpatient care in the current 90 days and the deductible was met the first day of this proposed episode of care, the inpatient days would reflect day three as the days (1<sup>st</sup> and last) this copayment was incurred.                                                                                                                                                       |
| Clock Days (1st/Last)                                 | On which days of the current billing clock this copayment was incurred. If the current billing clock began on 2/1/92 and the copayment for this proposed episode of care was incurred on 2/15/92 and 2/16/92, the clock days would reflect day 15 for the 1<sup>st</sup> and day 16 for the last.                                                                                                                                                                                                              |
| Charge                                                | Amount of the copayment or per diem charge for this proposed episode of care.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Per Diem Charges for (type of care)                   | A daily charge for the inpatient stay. No charge is incurred for the day of discharge (i.e., if the proposed inpatient stay is 2/1/92 through 2/5/92 and the per diem rate is \$10.00, the total per diem charge would be \$40.00).                                                                                                                                                                                                                                                                                |
| Total Estimated Charges                               | Total of the copayment and the per diem charges for the proposed inpatient stay.                                                                                                                                                                                                                                                                                                                                                                                                                                   |

<span id="_Toc143780843" class="anchor"></span>Table : Common Actions

### Outpatient / Registration Events Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Integrated Billing V. 1.5, the Outpatient/Registration Events Report was used primarily to list potentially billable outpatient activity (for Category C Veterans) for the purpose of billing charges that were not automatically billable by the system. As IB V. 2.0 completes the automation of Means Test billing for all outpatient activity, this report becomes a validation tool.

This option lists all episodes of outpatient care for Category C Veterans within a user-specified date range; appointments, stop codes, and registrations. For each visit, the clinic, appointment time, type, and status are provided. Clinics with a default type of research are flagged on the report to assist sites in determining if regular appointments are being scheduled in clinics where the primary intent is research. For each patient listed, the report indicates whether the patient has claimed exposure to Agent Orange, ionizing radiation, or environmental contaminants and whether the patient has active insurance. If exposure is claimed, the responses to the Classification questions answered during the checkout process are displayed. Any charges associated with the episode of care are included.

A separate page will print for each date within the date range; therefore, the user can limit the date range selected; run this report during off hours, as it may be quite time-consuming.

Sample Output

Category C Outpatient and Registration Activity for 09/01/93

Printed: 09/13/93 Page: 1

Patient/Event Time Clinic/Stop Appt.Type (Status)

IBpatient,one XXXX \[AO\] \*\*Insured\*\*

CLINIC APPT 12:00 PODIATRY REGULAR NO ACTION TAKEN

IBpatient,two 2222 \[AO\] \*\*Insured\*\*

CLINIC APPT 09:00 GEN. MEDICAL REGULAR CHECKED OUT

Care related to AO? YES

STOP CODE 09:00 EKG REGULAR

09:00 LABORATORY REGULAR

Category C Outpatient and Registration Activity for 09/02/93

Printed: 09/13/93 Page: 2

Patient/Event Time Clinic/Stop Appt.Type (Status)

No Outpatient activity recorded for Category C patients on 09/02/93.

### Held Charges Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Held Charges Report provides the user with a list of all charges with a status of ON HOLD. Charges for Category C patients with insurance are placed on hold until the patient's insurance company bill is resolved. When payment is received from the insurance carrier, the status of the charge is updated through the Release Charges 'On Hold' option.

This report may be used to ensure that there is an insurance bill established for each charge on hold, and to identify charges that should be released when payments are received from insurance carriers.

Sample Output

CATEGORY C CHARGES ON HOLD MAY 26,1992 PAGE 1

HELD CHARGES CORRESPONDING THIRD PARTY BILLS

==========================================================================\|\|======================================

Name Pt.ID ActionID Type Bill# From To Charge \|\| Bill# AR-Status Charge Paid

==========================================================================\|\|======================================

IBpatient,one 1111 XXXXXX OPT XXXXXX 03/01/92 03/11/92 30.00 \|\| XXXXXX NEW BILL 148.00 0.00

XXXXXX INPT XXXXXX 03/11/92 03/14/92 652.00 \|\|

XXXXXX OPT XXXXXX 03/11/92 03/11/92 30.00 \|\|

IBpatient,two 2222 XXXXXX OPT XXXXXX 05/08/92 05/08/92 30.00 \|\|

IBpatient,three 3333 XXXXXX OPT XXXXXX 04/07/92 04/07/92 30.00 \|\|

XXXXXX OPT XXXXXX 04/03/92 04/03/92 30.00 \|\| XXXXXX NEW BILL 296.00 0.00

IBpatient,four 4444 XXXXXX INPT XXXXXX 05/19/92 05/19/92 238.00 \|\|

IBpatient,five 5555 XXXXXX INPT XXXXXX 03/01/92 03/01/92 652.00 \|\| XXXXXX NEW BILL 5736.00 0.00

IBpatient,six 6666 XXXXXX INPT XXXXXX 04/13/92 04/16/92 652.00 \|\|

IBpatient,seven 7777 XXXXXX OPT XXXXXX 03/23/92 03/23/92 30.00 \|\| XXXXXX NEW BILL 740.00 0.00

XXXXXX OPT XXXXXX 03/23/92 03/23/92 30.00 \|\|

XXXXXX OPT XXXXXX 03/23/92 03/23/92 30.00 \|\|

XXXXXX OPT XXXXXX 03/23/92 03/23/92 30.00 \|\|

XXXXXX OPT XXXXXX 03/23/92 03/23/92 30.00 \|\|

### Manually Added HPIDs to Billing Claim Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report generates a list of Health Plan Identifier (HPID) numbers that have been added directly to claims. It allows billing staff to track the instances when an HPID number is added to a third-party claim and to generate an ad-hoc report of authorized claims with this entry information. Only HPIDs that have been manually added will appear on this report.

The user will be prompted for the date range, report format, and device. The date range pertains to when the HPID was manually added to the claim.

This output displays the patient name, last 4 of SSN, payer, HPID, claim number, username, date HPID added, Professional ID, and Institutional ID.

Sample Output

MANUALLY ADDED HPIDS TO BILLING CLAIM REPORT AUG 02, 2015@19:59 Page: 1

PT NAME SSN PAYER HPID CLAIM \# USER NAME DATE HPID ADDED PROF ID INST ID

------------------------------------------------------------------------------------------------------------------------------------

IBPATIENT,ONE 1111 BLUE CROSS XXXXXXXXXX XXX-XXXXXXX IBUSER,ONE 12/02/2014 1234567XXX 0987654XXX

IBPATIENT,ONE 1111 BLUE CROSS XXXXXXXXXX XXX-XXXXXXX IBUSER,ONE 01/15/2015 1234567XXX 0987654XXX

IBPATIENT,ONE 1111 BLUE CROSS XXXXXXXXXX XXX-XXXXXXX IBUSER,ONE 01/22/2015 1234567XXX 0987654XXX

IBPATIENT,ONE 1111 BLUE CROSS XXXXXXXXXX XXX-XXXXXXX IBUSER,ONE 01/22/2015 1234567XXX 0987654XXX

IBPATIENT,ONE 1111 BLUE CROSS XXXXXXXXXX XXX-XXXXXXX IBUSER,ONE 01/23/2015 1234567XXX 0987654XXX

IBPATIENT,ONE 1111 BLUE CROSS XXXXXXXXXX XXX-XXXXXXX IBUSER,ONE 02/05/2015 1234567XXX 0987654XXX

IBPATIENT,TWO 9341 BLUE CROSS XXXXXXXXXX XXX-XXXXXXX IBUSER,ONE 02/09/2015 1234567XXX 0987654XXX

IBPATIENT,TWO 9341 BLUE CROSS XXXXXXXXXX XXX-XXXXXXX IBUSER,ONE 02/09/2015 1234567XXX 0987654XXX

IBPATIENT,TWO 9341 BLUE CROSS XXXXXXXXXX XXX-XXXXXXX IBUSER,ONE 02/09/2015 1234567XXX 0987654XXX

### Indian Attestation Copay Exemption Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA has been updated to support the changes needed to comply with the Johnny Isakson and David P. Roe, M.D. Veterans Health Care and Benefits Improvement Act of 2020 (Public Law 116-315). This bill includes a provision (section 3002) to prevent billing or collection of payment for health care services obtained through the Department of Veterans Affairs (VA) from Veterans that identify as Indian or urban Indian.

The Indian Attestation Copay Exemption Report provides a list of patients who have identified themselves as Native American/Indian in VistA and their associated bills. The user will review the report to determine whether the patient should have the copays canceled (in the case of Bills with Indian Attestation Status = Y) or re-billed (in the case of Bills with Indian Attestation Status = N). Re-billing cases would be appropriate for a Veteran who claimed the exemption but had the designation removed later. The user will enter the beginning and ending dates for the Indian Attestation Change date, and whether to export the report to Microsoft Excel (Y/N).

Sample Output

Indian Attestation Copay Exemption Report Nov 02, 2022 Page: 1

Indian Attestation Change dates: Jan 01, 2022 - Nov 02, 2022

Bills with Indian Attestation Status = Y : Eligible for possible cancellation.

Bills with Indian Attestation Status = N : Eligible for possible re-billing.

Indian Change Indian Bill From Bill To Bill

Name ID Date/Time Status Bill \# Charge Type Bill Status Date Date Amount

------------------------------------------------------------------------------------------------------------------------------------

AAA,DDDDD E A7373 02/07/22@13:53:28 Y 405-K201ZR1 DG OPT COPAY BILLED 06/01/22 06/01/22 \$50.00

AAA,DDDDD E A7373 02/07/22@13:53:28 Y 405-K201ZR2 CC URGENT CA BILLED 05/01/22 05/01/22 \$30.00

AAA,DDDDD E A7373 02/07/22@13:53:28 Y 405-K201ZR3 CC URGENT CA BILLED 06/05/22 06/05/22 \$30.00

AAA,DDDDD E A7373 02/07/22@13:53:28 Y 405-K203BAT DG OPT COPAY BILLED 06/22/22 06/22/22 \$50.00

AAA,DDDDD E A7373 02/07/22@13:53:28 Y 405-K2021S6 PSO NSC RX C BILLED 06/27/22 06/27/22 \$5.00

AAA,DDDDD E A7373 02/07/22@13:53:28 Y 405-K203BAU DG OPT COPAY BILLED 06/27/22 06/27/22 \$50.00

AAA,DDDDD E A7373 02/07/22@13:53:28 Y 405-K203B9T DG OPT COPAY BILLED 08/11/22 08/11/22 \$50.00

AAA,DDDDD E A7373 02/07/22@13:53:28 Y 405-K203B9I PSO NSC RX C BILLED 08/11/22 08/11/22 \$15.00

GGGGGGG,DDDDD JJJJJ G8686 10/18/22@12:35 N 405-K203BAG DG LTC OPT A CANCELLED 07/22/22 07/22/22 \$15.00

GGGGGGG,DDDDD JJJJJ G8686 10/18/22@12:35 N DG LTC OPT R CANCELLED 08/06/22 08/06/22 \$15.00

LLLLL,DDDDDDD J L8888 10/17/22@13:10:48 N 405-K303588 CC URGENT CA CANCELLED 05/01/22 05/01/22 \$30.00

LLLLL,DDDDDDD J L8888 10/17/22@13:10:48 N 405-K303589 CC (RX) NEW CANCELLED 05/02/22 05/02/22 \$33.00

LLLLL,DDDDDDD J L8888 10/17/22@13:10:48 N 405-K30358A PSO NSC RX C CANCELLED 10/14/22 10/14/22 \$15.00

NNNNNNN,MMMMM LLL N8765 02/07/22@12:22:55 Y CC URGENT CA ON HOLD 06/01/22 06/01/22 \$30.00

Type \<Enter\> to continue or '^' to exit:

### ### Patient Billing Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Billing Inquiry option allows the user to display/print information on any reimbursable insurance bill, Pharmacy Copay, or Means Test bill. The information provided differs depending on the bill type.

For reimbursable insurance bills, the information provided includes bill status, rate type, reason canceled (if applicable), admission date (for inpatients), all outpatient visits (for outpatients), charges, the amount paid, statement to and from dates, each action that was taken on that bill, and the user who performed it. If the user opts to view the full inquiry, address information from the PATIENT file (#2) and the bill is also provided.

The information provided in a brief inquiry for Pharmacy Copay charges includes the date of the charge, type of charge (syntax: patient eligibility - action type - status), brief description (syntax: prescription \# - drug name - \# of units), amount of charge or credit, and an explanation of any charge removed, if applicable. A full inquiry, in addition to the information provided in the brief inquiry, provides information from the PRESCRIPTION file (#52), as well as the address information on the patient.

The display/output for Means Test bills is very similar to the brief inquiry for Pharmacy Copay. It includes the date of the charge, charge type, brief description, units, and amount of charge. A full inquiry also includes address information on the patient.

The medication copayment exemption status and reason are displayed for medication copayment and Means Test bills.

Medication Copayment charge cancellation can be displayed in the Brief and Full output (Public Law 114-315).

Sample Output of Brief Inquiry

FFFF,PPPP LLL 442-K5038N3 JUN 26, 2023@14:31 PAGE: 1

Medication Copayment Exemption Status: NON-EXEMPT

Patient's income is greater than Copay Income Threshold

DATE CHARGE TYPE BRIEF DESCRIPTION UNITS CHARGE

===============================================================================

NOV 01, 2022 LTC INPT NHCU NEW LTC INPATIENT NURSIN 31 \$1,512.00

------------

\$1,512.00

Sample Output of Full Inquiry

FFFF,PPPP LLL 442-K5038N3 JUN 26, 2023@14:34 PAGE: 1

Medication Copayment Exemption Status: NON-EXEMPT

Patient's income is greater than Copay Income Threshold

===============================================================================

NOV 01, 2022 LTC INPT NHCU NEW LTC INPATIENT NURSIN 31 \$1,512.00

------------

\$1,512.00

Type \<Enter\> to continue or '^' to exit:

FFFF,PPPP LLL 442-K5038N3 JUN 26, 2023@14:34 PAGE: 2

Medication Copayment Exemption Status: NON-EXEMPT

Patient's income is greater than Copay Income Threshold

===============================================================================

\*\*\* ADDRESS INFORMATION \*\*\*

Patient Address: 3320 TOMAHAWK DR UNIT 10

LK HAVASU CTY, ARIZONA 86406

\(888\) 888-8888

Type \<Enter\> to continue or '^' to exit:

### List all Bills for a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List all Bills for a Patient option is used to print a list of all bills on file for a selected patient. The patient may be selected by name or social security number.

The List all Bills for a Patient includes three options:

- First-Party Bills Only
- Third-Party Bills Only
- Both Bill Types

This allows the user to view bills for a certain bill type, filter the bills for a specified time period, and add a starting date of care and an ending date of care.

The bills are listed by date of care in reverse date order. The bill number, date printed, action/rate type, classification, date of care, the statement from and to dates, the amount collected, status, and timeframe of the bill will be displayed for each bill on the list.

The table below provides a brief explanation of some of these data elements:

| Data Element       | Description                                                                                                                                                                                |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bill Number        | If IB action is incomplete, pending is displayed. If IB action is converted, this field will be blank.                                                                                 |
| Date Printed       | Date bill generated.                                                                                                                                                                       |
| Action/Rate Type   | Action for IB actions; rate type for insurance bills.                                                                                                                                      |
| Date of Care       | Admission date for inpatients; opt visit date for outpatients; date medication dispensed for Pharmacy Copay.                                                                               |
| Amount Collected   | Not applicable to patient bills; amount from Accounts Receivable for insurance bills.                                                                                                      |
| Time frame of Bill | Null if IB action.                                                                                                                                                                         |
| Reject Indicator   | The c indicates a rejected bill. A reject is defined to be a billing reject that is on the Claim Status Awaiting Resolution (CSA) or Medicare Remittance Advice Worklist (MRW) report. |

<span id="_Toc143780844" class="anchor"></span>Table : Common Actions

- The user will be prompted for a patient name and prompted to include or not include Pharmacy Copay charges on the report.
- The user will also be prompted for an option to export the report to Microsoft Excel.
- The output produced by this option must be generated at a 132-column margin width.

Sample Output

Select Billing \<TEST ACCOUNT\> Option: ^List All

1 List all Menu Templates \[XQTSHO\]

2 List all Bills for a Patient \[IB LIST ALL BILLS FOR PAT.\]

3 List All Local Print Fields \[IBCE LIST LOCAL\]

4 List All Bills \[PRCA LIST ALL BILLS\]

Type '^' to stop, or choose a number from 1 to 4 :2 List all Bills for a Patien

t

Select PATIENT NAME: IBPatient,one IBPatient,one X-X-XX XXXXXXXX NO NSC VETERAN CD

Enrollment Priority: GROUP 8c Category: ENROLLED End Date:

Include Pharmacy Co-Pay charges on this report? NO//

Select one of the following:

F FIRST PARTY

T THIRD PARTY

B BOTH

(F)irst Party Bills,(T)hird Party Bills, or (B)oth on this report: B// OTH

Enter Starting Date of Care: 2/1/19 (FEB 01, 2019)

Enter Ending Date of Care: Apr 13, 2020// 8/1/19 (AUG 01, 2019)

Export the report to Microsoft Excel (Y/N)? NO// YES

Before continuing, please set up your terminal to capture the

detail report data and save the detail report data in a text file

to a local drive. This report may take a while to run.

> **NOTE:** To avoid undesired wrapping of the data saved to the file,

please enter '0;256;99999' at the 'DEVICE:' prompt.

DEVICE: HOME// HOME (CRT) Right Margin: 80// 132

List of all Bills for IBPatient,one SSN: XXX-XX-XXX APR 13,2020@11:08:27 PAGE 1

BILL DATE DATE OF STATEMENT STATEMENT AMOUNT

NO. PRINTED ACTION/RATE TYPE CLASSIFICATION CARE FROM DATE TO DATE COLLECTED STATUS TIMEFRAME OF BILL

-------------------------------------------------------------------------------------------------------------------------------

XXXXXXX 04/01/20 CC (RX) NEW RX COPAYMENT 03/15/20 03/15/20 03/15/20 N/A BILLED

XXXXXXX 03/20/20 CC URGENT CARE (O CC URGENT OPT 03/13/20 03/13/20 03/13/20 N/A CANCELLED

XXXXXXX 03/20/20 CC URGENT CARE (O CC URGENT OPT 03/12/20 03/12/20 03/12/20 N/A CANCELLED

XXXXXXX 03/20/20 OPT COPAY NEW OPT COPAYMENT 03/11/20 03/11/20 03/11/20 N/A CANCELLED

XXXXXXX 03/20/20 CC (OPT) NEW CC OPT COPAY 03/10/20 03/10/20 03/10/20 N/A CANCELLED

XXXXXXX 03/20/20 CC (OPT) NEW CC OPT COPAY 03/10/20 03/10/20 03/10/20 N/A CANCELLED

### Category C Billing Activity List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Category C Billing Activity List option is used to list all Means Test/Category C charges within a specified date range. The list is alphabetical by patient name.

This output provides the patient’s name and ID, a brief description, the status and the billing period for the bill, the units (the number of days a charge occurred), and the amount of the charge. For inpatient copay charges, the description includes the treating specialty for the episode of care.

As stated above, the units reflect the number of days a charge occurred. For inpatient copay charges the unit will always be one, even if the patient accrued the charges over several days before the Medicare deductible was met.

Sample Output

Category C Billing Activity List FEB 26, 1992@09:14:28 Page: 1

Charges from 01/01/92 through 02/26/92

PATIENT/ID DESCRIPTION STATUS FROM TO UNITS CHARGE

----------------------------------------------------------------------------------

IBpatient,one XXXX INPT PER DIEM BILLED 01/02/92 01/03/92 2 \$20.00

INPT COPAY (ALC) BILLED 01/02/92 01/03/92 1 \$476.00

IBpatient,two XXXX OPT COPAY PENDING A/R 02/11/92 02/11/92 1 \$0.00

IBpatient,three XXXX INPT PER DIEM BILLED 01/13/92 01/14/92 2 \$20.00

INPT COPAY (MED) BILLED 01/13/92 01/14/92 1 \$652.00

IBpatient,four XXXX OPT COPAY PENDING A/R 02/12/92 02/12/92 1 \$0.00

### Former OTH Patient Eligibility Change Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report identifies Former Service Members whose Primary Eligibility changed from EXPANDED MH CARE NON-ENROLLEE to a new Primary Eligibility with a VERIFIED eligibility status. These patients are no longer treated under the Other Than Honorable (OTH) authority (VHA Directive 1601A.02).

The date range entered is used to select the last episode of care and/or released prescriptions. The patient will not display on the report if there is no episode of care or released prescription within the date range.

\*\*\* THIS REPORT REQUIRES 132 COLUMN margin width \*\*\*

9.  The figure below is an example of the Former OTH Patient Eligibility Change Report.

FORMER OTH PATIENT ELIGIBILITY CHANGE REPORT Page: 1

====================================================================================================================================

OTH Eligibility Change Date Range: 02/13/2021 TO 05/24/2021 Date Printed : Jun 16, 2021 11:31 am

List of Patients whose primary eligibility changed from EXPANDED MH CARE NON-ENROLLEE to a new primary eligibility code with

eligibility status of VERIFIED and episode(s)of care.

The Current MST Screening indicates the latest MST screening result for the patient.

The Station column provides data on which site(s) the patient was treated.

====================================================================================================================================

PATIENT NAME DATE OF PID OTH REG NEW ELIGIBILITY CODE CURRENT MST SC% ELIGIBILITY STATION

BIRTH DATE SCREEN STATUS CHANGE DATE

--------------------------- ---------- ----- ---------- ----------------------------- -------------- --- ----------- -------

IBPATIENT,TESTONE (XXXXX) XX/XX/XXXX XXXXX 02/13/2021 SC LESS THAN 50% UNKNOWN 20 05/24/2021 442

IBPATIENT,TESTTWO (XXXXX) XX/XX/XXXX XXXXX 03/16/2021 SC LESS THAN 50% YES 0 04/23/2021 442

IBPATIENT,TESTTWA (XXXXX) XX/XX/XXXX XXXXX 04/14/2021 SC LESS THAN 50% DECLINE 0 04/27/2021 442

IBPATIENT,TESTTWB (XXXXX) XX/XX/XXXX XXXXX 04/29/2021 NSC NO DATA FOUND 04/29/2021 442

IBPATIENT,TESTTWC (XXXXX) XX/XX/XXXX XXXXX 05/24/2021 SC LESS THAN 50% YES 0 06/11/2021 442

IBPATIENT,TESTTWD (XXXXX) XX/XX/XXXX XXXXX 05/24/2021 SC LESS THAN 50% NO 0 06/14/2021 442

====================================================================================================================================

Number of Unique Patients: 6

\<\< end of report \>\>

### Former OTH Patient Detail Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report assists billing user in reviewing Former Service Member's past episodes of care and released prescription details to determine if potential back-billing is necessary.

\*\*\*THIS REPORT REQUIRES 132 COLUMN OUTPUT TO PRINT CORRECTLY \*\*\*Sample Output: Eligibility Section

FORMER OTH PATIENT DETAIL REPORT

Patient Name: IBPATIENT,TESTONE (XXXXX) DOB: XXX XX,XXXX

==========================================================================================================

Current Eligibility Code : SC LESS THAN 50% -- VERIFIED 05/26/2021

Other Eligibility Code(s): NO ADDITIONAL ELIGIBILITIES IDENTIFIED

Enrollment Priority : GROUP 1

----------------------------------------------------------------------------------------------------------

Means Test Signed?:

Patient's status is MT COPAY REQUIRED based on primary means test

Has agreed to pay the deductible

Primary Means Test Last Applied 'MAY 26,2021' (COMPLETED: MAY 26,2021@13:44)

Service Connected : YES SC Percent : 0%

Rated Disabilities: 9410 - NEUROSIS (0% SC)

Health Insurance : NO

Insurance COB Subscriber ID Group Holder Effective Expires

==========================================================================================================

No Insurance Information

\*\*\* Patient has Insurance Buffer entries \*\*\*

#### Former OTH Patient Detail Report

Sample Output: Eligibility Section

Patient Name: IBPATIENT,TESTONE (I6863) DOB: XXX XX,XXXX

====================================================================================================================================

PRIMARY ELIGIBILITY/EXPANDED CARE TYPE HISTORY

------------------------------------------------------------------------------------------------------------------------------------

Primary Eligibility Date of Change

------------------------------------------------------------------------------------------------------------------------------------

SC LESS THAN 50% 05/26/2021

EXPANDED MH CARE NON-ENROLLEE (OTH-90) 07/28/2020

Sample Output: Patient’s Episode of Care

Patient Name: IBPATIENT,TESTONE (XXXXX) DOB: XXX XX,XXXX

====================================================================================================================================

PATIENT'S EPISODE OF CARE

Date Range: 07/28/2020 - 05/26/2021

------------------------------------------------------------------------------------------------------------------------------------

Location of Clinic Stop/ Primary Div. Date of Last Updated Bill \# Action Type/ IB Status

Care Treating Specialty DX Service By Rate Type

------------------------------------------------------------------------------------------------------------------------------------

RDCLINIC4 POLYTRAUMA/TBI IND E11.00 442GB 02/25/2021 USER,USERONE

------------------------------------------------------------------------------------------------------------------------------------

Total Number of Episode(s) of Care: 1

#### Former OTH Patient Detail Report

Sample Output: Patient’s Released Prescription

Patient Name: IBPATIENT,TESTONE (XXXXX) DOB: XXX XX,XXXX

====================================================================================================================================

PATIENT'S RELEASED PRESCRIPTION

Date Range: 07/28/2020 - 05/26/2021

Sorted By: Rx Release Date

------------------------------------------------------------------------------------------------------------------------------------

Rx \# Copay \# of Days Division Fill Date Rx Release Bill \# Action Type/ IB Status

Tier Refills Supply Date Rate Type

------------------------------------------------------------------------------------------------------------------------------------

XXXXXXX 2 11 10 442GC 05/24/2021 05/24/2021

XXXXXXX 1 11 10 442GC 05/24/2021 05/24/2021

XXXXXXX 1 11 10 442GC 05/24/2021 05/24/2021

XXXXXXX(X) 2 11 10 442QD 05/25/2021 05/26/2021 XXXXXXX PSO NSC RX COPAY NEW BILLED

XXXXXXX(X) 1 11 10 442QD 05/25/2021 05/26/2021 XXXXXXX PSO NSC RX COPAY NEW BILLED

XXXXXXX(X) 1 11 10 442QD 05/25/2021 05/26/2021 XXXXXXX PSO NSC RX COPAY NEW BILLED

XXXXXXXX 2 11 10 442QD 05/26/2021 05/26/2021 XXXXXXX PSO NSC RX COPAY NEW BILLED

XXXXXXXX 2 5 10 442QD 05/26/2021 05/26/2021 XXXXXXX PSO NSC RX COPAY NEW BILLED

------------------------------------------------------------------------------------------------------------------------------------

Total Number of Rx: 5

\<\< end of report \>\>

## Third-Party Output Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Veterans w/Insurance and Discharges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans w/Insurance and Discharges option is used to produce a list of all patients who have reimbursable insurance and who were discharged from the medical center during a selected date range. For dates of care prior to 10/1/90, service-connected Veterans with insurance who were treated for a non-service-connected condition (from the PTF record) will be included on the list. This list may be used to help ensure that a bill exists for all billable inpatient episodes of care for that date range.

The user may include unbilled patients, previously billed patients, or both on the report. If the user opts to print ALL (both unbilled and previously billed), the report is sorted by these two categories. The unbilled patients portion displays the patient ID#, patient name, SSN, eligibility status, date of care (event date), and the patient's insurance companies. The previously billed list displays the same data plus every bill within the selected date range for each patient showing the bill number, bill rate type, the statement from and to dates, and the debtor.

The lists are printed in alphabetical order by patient name or numerically by the terminal digit (8<sup>th</sup> and 9<sup>th</sup> digit of the SSN, then 6th and 7th, etc.). For multidivisional sites, the user may print a list for each division.

It is recommended the report be queued to print during non-peak user hours.

Sample Output

\*Veterans with Reimbursable Insurance and INPATIENT Discharges for the period covering FEB 01,1992 through FEB 29,1992

UNBILLED PATIENTS for Division ANYTOWN Printed: MAR 01,1992@06:00 Page: 1

PT ID PATIENT SSN ELIGIBILITY DATE OF DISCHARGE INSURANCE COMPANIES

======================================================================================================================

XXXX IBpatient,one XXX-XX-XXXX NON-SERVICE CONN FEB 20,1992@15:51:15 ABC

XXXX IBpatient,two XXX-XX-XXXX NON-SERVICE CONN FEB 19,1992@12:52:51 ALLSTATE

XXXX IBpatient,three XXX-XX-XXXX NON-SERVICE CONN FEB 19,1992@14:40:18 NORTHWEST

\*Veterans with Reimbursable Insurance and INPATIENT Discharges for the period covering FEB 01,1992 through FEB 29,1992

PREVIOUSLY BILLED PATIENTS for Division ANYTOWN Printed: MAR 01,1992@06:00 Page: 1

PT ID PATIENT SSN ELIGIBILITY DATE OF DISCHARGE INSURANCE COMPANIES

======================================================================================================================

XXXX IBpatient,one XXX-XX-XXXX NON-SERVICE CONN FEB 7,1992@13:48:23 ABC

XXXXXX REIM INS-INPT From: 02/07/92 To: 02/07/92 Debtor: ABC

XXXX IBpatient,two NON-SERVICE CONN FEB 14,1992@13:00 ABC

XXXXXX REIM INS-INPT From: 02/14/92 To: 02/19/92 Debtor: ABC

XXXX IBpatient,three XXX-XX-XXXX NON-SERVICE CONN FEB 7,1992@13:48:23 ABC

XXXXXX REIM INS-INPT From: 02/07/92 To: 02/10/92 Debtor: ABC

### Veteran Patient Insurance Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veteran Patient Insurance Information option provides insurance information on Veteran inpatients. This includes such information as the insurance company, insurance number, group number, and insurance expiration date. Medical information is also shown. Dates of admission and discharge and the status of the PTF records are provided. The report is broken down by patient, with information on the length of stay for each bed section, diagnoses, and diagnostic codes. The total length of stay is shown with the primary diagnosis.

The form indicates whether the policy shown will reimburse VA for the cost of medical care. If the REIMBURSE field of the INSURANCE COMPANY file is set to NO for any of the companies that cover the applicant, an asterisk (\*) will be shown next to the insurance company name and the following message will appear.

\* - Insurer may not reimburse!!

All this information is used in billing the insurance companies for the cost of the Veteran's care.

The report may be sorted sequentially by discharge or admission date. The user will be prompted for a date range and device. Depending on the number of applicable admissions and the size of the date range specified, the generation of this report could be time-consuming. The user may opt to queue the report to print during non-peak user hours.

Sample Output

THIRD PARTY REIMBURSEMENT PRINTED: JAN 11,1991@0915

IBpatient,one EMPLOYMENT STATUS: EMPLOYED

(PT ID: XXXXXXXX) EMPLOYER: ABC LUMBER

307 TEST BLVD OCCUPATION: CARPENTER

ANYTOWN, OHIO 55555

INSURANCE TYPE INSURANCE \# GROUP \# EXPIRES HOLDER

--------- ---- --------- - ----- - ------- ------

ABC INS xxx 887 01/01/93 VETERAN

\*XYZ INS xxxxx 21 12/31/91 VETERAN

\* - Insurer may not reimburse!!

Admitted: APR 9,1990@14:00 Discharged: APR 19,1990@13:39

PTF Record not closed

DATE LOS BEDSECTION LOS DIAGNOSES

---- --------------- ---- ---------

APR 10,1990@11:29 OPHTHALMOLOGY 1 334.4 (CORNEAL ABRASION)

APR 11,1990@10:10 UROLOGY 1 778.0 (URINARY TRACT INFECTION,

UNSPEC.)

APR 19,1990@13:39 CARDIOLOGY 8 654.00 (MYOCARDIAL INFARCTION)

---- -----------

TOTAL LOS: 10 DXLS: 654.00 (MYOCARDIAL INFARCTION)

### Veterans w/ Insurance and Inpatient Admissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans with Insurance and Inpatient Admissions option is used to produce a list of all patients who have reimbursable insurance and who had admissions to the medical center during a selected date range. For dates of care prior to 10/1/90, service-connected Veterans with insurance who were treated for a non-service-connected condition (from the PTF record) will be included on the list. This list may be used to help ensure that a bill exists for all inpatient billable episodes of care for the selected date range.

The user may include unbilled patients, previously billed patients, or both on the report. If the user opts to print ALL (both unbilled and previously billed), the report is sorted by these two categories. The unbilled patients portion displays the patient ID#, patient name, SSN, eligibility status, date of care (event date), and the patient's insurance companies. The previously billed list displays the same data plus every bill within the selected date range for each patient showing the bill number, bill rate type, the statement from and to dates, and the debtor.

The lists are printed in alphabetical order by patient name or numerically by the terminal digit (8<sup>th</sup> and 9<sup>th</sup> digit of the SSN, then 6<sup>th</sup> and 7<sup>th</sup>, etc.). For multidivisional sites, the user may print a list for each division.

Depending on the size of the database and the date range selected, this report could be quite lengthy. It is recommended the report be queued to print during non-peak user hours.

Sample Output

Veterans with Reimbursable Insurance and INPATIENT Admissions for period covering FEB 1,1992 through FEB 29, 1992

UNBILLED PATIENTS for Division ANYTOWN Printed: MAR 01,1992@06:00 Page: 1

PT ID PATIENT SSN ELIGIBILITY DATE OF CARE INSURANCE COMPANIES

======================================================================================================

XXXX IBpatient,one XXX-XX-XXXX NON-SERVICE CONN FEB 05,1992@15:51:15 ABC

XXXX IBpatient,two XXX-XX-XXXX NON-SERVICE CONN FEB 13,1992@13:40 NATIONWIDE

Veterans with Reimbursable Insurance and INPATIENT Admissions for period covering FEB 1,1992 through FEB 29, 1992

PREVIOUSLY BILLED PATIENTS for Division ANYTOWN Printed: MAR 01,1992@06:00 Page: 1

PT ID PATIENT SSN ELIGIBILITY DATE OF CARE INSURANCE COMPANIES

======================================================================================================

XXXX IBpatient,one XXX-XX-XXXX NON-SERVICE CONN FEB 1,1992@11:10 XYZ INS

XXXXXX REIM INS-INPT From: 02/01/92 To: 02/10/92 Debtor: XYZ INS

XXXX IBpatient,two XXX-XX-XXXX NON-SERVICE CONN FEB 24,1992@08:09 UNITED WORKERS

XXXXXX REIM INS-INPT From: 02/24/92 To: 02/28/92 Debtor: UNITED WORKERS

XXXXXX REIM INS-INPT From: 02/28/92 To: 02/29/92 Debtor: UNITED WORKERS

XXXX IBpatient,three XXX-XX-XXXX NON-SERVICE CONN FEB 10,1992@13:34 INTERNATIONAL

XXXXXX REIM INS-INPT From: 02/10/92 To: 02/14/92 Debtor: INTERNATIONAL

### Veterans w/Insurance and Opt. Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans w/Insurance and Opt. Visits option is used to produce a list of all patients who have reimbursable insurance and who had outpatient visits to the medical center during a selected date range. For dates of care prior to 10/1/90, service-connected Veterans with insurance will be included on the list.

Non-count clinics and unbillable appointment types are excluded from the list. This list may be used to help ensure that a bill exists for all outpatient billable episodes of care for that time frame.

This report includes patients who have either add/edit stop codes, 10-10 registrations, or scheduled appointments during the selected date range. The stop code, registration type, or clinic is included in the output for each entry. This information may be used to aid in determining how a charge should be billed.

The user may include unbilled patients, previously billed patients, or both on the report. If the user opts to print ALL (both unbilled and previously billed), the report is sorted by these two categories. The unbilled patients portion displays the patient ID#, patient name, SSN, eligibility status, date of care (event date), and the patient's insurance companies. The previously billed list displays the same data plus every bill within the selected date range for each patient showing the bill number, bill rate type, the statement from and to dates, and the debtor.

The lists are printed in alphabetical order by patient name or numerically by the terminal digit (8th and 9th digit of the SSN, then 6th and 7th, etc.). For multidivisional sites, the user may print a list for each division.

It is recommended the report be queued to print during non-peak user hours.

Sample Output

Veterans with Reimbursable Insurance and OUTPATIENT Appointments for period covering FEB 1,1992 through FEB 29, 1992

UNBILLED PATIENTS for Division ANYTOWN Printed: MAR 01,1992@06:00 Page: 1

PT ID PATIENT SSN ELIGIBILITY DATE OF CARE INSURANCE COMPANIES

======================================================================================================

XXXX IBpatient,one XXX-XX-XXXX NON-SERVICE CONN FEB 12,1992@09:45 XYZ INS

Add/Edit Stop Code with 900,

XXXX IBpatient,two XXX-XX-XXXX NON-SERVICE CONN FEB 23,1992@13:40 ABC

Clinic: Dermatology

XXXX IBpatient,three XXX-XX-XXXX NON-SERVICE CONN FEB 29,1992@09:44 ABC

Clinic: Dermatology

XXXX IBpatient,four XXX-XX-XXXX NON-SERVICE CONN FEB 18,1992@23:45 BLUE SHIELD

Registration: HOSPITAL ADMISSION

Veterans with Reimbursable Insurance and OUTPATIENT Appointments for period covering FEB 1,1992 through FEB 29, 1992

PREVIOUSLY BILLED PATIENTS for Division ANYTOWN Printed: MAR 01,1992@06:00 Page: 1

PT ID PATIENT SSN ELIGIBILITY DATE OF CARE INSURANCE COMPANIES

======================================================================================================

XXXX IBpatient,one XXX-XX-XXXX NON-SERVICE CONN FEB 11,1992@14:34 BLUE CROSS

Add/Edit Stop Code with 102, 301, 706

XXXXXX REIM INS-OUTP From: 02/11/92 To: 02/11/92 Debtor: BLUE CROSS

XXXX IBpatient,two XXX-XX-XXXX NON-SERVICE CONN FEB 12,1992@07:09 ABC INSURANCE

Clinic: MEDICAL

00089A REIM INS-OUTP From: 02/12/92 To: 02/12/92 Debtor: ABC INSURANCE

XXXX IBpatient,three XXX-XX-XXXX NON-SERVICE CONN FEB 26,1992@09:45 ABC INSURANCE

Clinic: MEDICAL

00096A REIM INS-OUTP From: 02/26/92 To: 02/29/92 Debtor: ABC INSURANCE

### Patient Review Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Review Document option is used to print the Third-Party Review Form by patient name and admission date specifications. This form is used in connection with Veteran patients admitted to the hospital who have private medical insurance. The form provides the patient's name, patient ID#, admission date, diagnoses, and ward location. Insurance information provided includes the insurance company name, address and phone number, policy number, and group number. The insurance data is not displayed if the insurance has expired.

The form is then divided into four sections. Section one concerns pre-admission certification. It shows whether pre-admission certification is required. If required, it provides information concerning the decision made by the insurance company regarding the admission. Information includes the number of days certified, whether medical information is insufficient, and whether outpatient care is more appropriate. Section two concerns the need for a second surgical opinion (if required) and the results of the second opinion.

Section three provides information concerning the length of stay review; if further stay was approved or if disapproved, the reasons for denial. Section four shows bill status – denied in full, denied in part, or paid in full. If denied, the reasons for the denial are given. The bill number is also shown.

Sample Output

NAME: IBpatient,one DATE PRINTED: DEC 12, 1990

PT ID: XXXXXXXX

INSURANCE CARRIER: ABC Insurance Company

ADDRESS: 234 Test St., ANYTOWN, California 15436

PHONE: XXX-XXXX POLICY \#: XXXXXXXXX GROUP \#: 10

PRE-CERT PHONE: BILLING PHONE:

INSURANCE CARRIER:

ADDRESS:

PHONE: POLICY \#: GROUP \#:

PRE-CERT PHONE: BILLING PHONE:

INSURANCE CARRIER:

ADDRESS:

PHONE: POLICY \#: GROUP \#:

PRE-CERT PHONE: BILLING PHONE:

ADMITTING DX: Pneumonia WARD: 8A

SCHEDULED ADMISSION DATE: ADMISSION DATE: JUN 26, 1986

------------------------------------------------------------------------------------------------------

PRE-ADMISSION CERTIFICATION:

\_\_\_NUMBER DAYS CERTIFIED \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_AUTHORIZATION NUMBER

\_\_\_NOT REQUIRED

\_\_\_FAILURE TO MEET ESTABLISHED ADMISSION CRITERIA

\_\_\_MEDICAL INFORMATION IS INSUFFICIENT

\_\_\_OPT CARE IS MORE APPROPRIATE

\_\_\_OTHER LEVELS OF SERVICE ARE MORE APPROPRIATE (NURSING HOME VS HOSPITAL)

\_\_\_POLICY DOES NOT COVER MEDICAL CARE REQUIRED

\_\_\_COVERAGE EXHAUSTED

\_\_\_OTHER PREPARED BY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

------------------------------------------------------------------------------------------------------

SECOND SURGICAL OPINION NEEDED: \_\_\_\_\_\_YES \_\_\_\_\_\_NO

SECOND SURGICAL OPINION OBTAINED: \_\_\_\_\_\_YES \_\_\_\_\_\_\_OUTSIDE MD RECOMMENDED AGAINST SURGERY

\_\_\_\_\_\_NOT APPLICABLE \_\_\_\_\_\_\_OTHER

\_\_\_\_\_\_NOT RECEIVED PREPARED BY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

------------------------------------------------------------------------------------------------------

LOS REVIEW DATE: \_\_\_\_\_\_\_\_\_\_ DATE APPROVED: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NUMBER OF DAYS EXTENDED: \_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_AUTHORIZATION NUMBER

\_\_\_PRE-OP DAYS DENIED \_\_\_APPROPRIATE ALTERNATIVE TREATMENT OPTIONS EXIST

\_\_\_MORE MEDICAL INFORMATION NEEDED \_\_\_ALTERNATIVE TREATMENT NOT COVERED BY POLICY

\_\_\_FAILURE TO MEET CONTINUED STAY CRITERIA \_\_\_AVAILABILITY OF ALTERNATIVE TREATMENT

\_\_\_APPROPRIATE ALTERNATIVE TREATMENT OPTIONS EXIST \_\_\_COVERAGE EXHAUSTED

\_\_\_OTHER PREPARED BY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

------------------------------------------------------------------------------------------------------

BILLS DENIED IN FULL: BILL DENIED IN PART:

\_\_\_\_\_\_\_\_\_EXCLUSIONARY CLAUSE STILL IN EFFECT \_\_\_\_\_\_\_\_\_DEDUCTIBLE/COPAYMENT APPLIES

\_\_\_\_\_\_\_\_\_DEDUCTIBLE/COPAYMENT APPLIES \_\_\_\_\_\_\_\_\_PORTION OF CARE NOT COVERED BY POLICY

\_\_\_\_\_\_\_\_\_TYPE OF CARE NOT COVERED BY POLICY \_\_\_\_\_\_\_\_\_EXCEEDS USUAL AND CUSTOMARY CHARGES

\_\_\_\_\_\_\_\_\_PATIENT DOES NOT HAVE CURRENT COVERAGE \_\_\_\_\_\_\_\_\_PAYMENT LIMITED TO PREAUTHORIZED DAYS

\_\_\_\_\_\_\_\_\_INSURER WILL NOT PAY PER DIEM RATES \_\_\_\_\_\_\_\_\_OTHER

\_\_\_\_\_\_\_\_\_TREATMENT/ADMISSION NOT AUTHORIZED BY INSURANCE CARRIER

\_\_\_\_\_\_\_\_\_OTHER \_\_\_\_\_\_\_\_\_BILL PAID IN FULL

PREPARED BY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

------------------------------------------------------------------------------------------------------

REMARKS:

BILL \# \_\_\_\_\_\_\_\_\_\_\_\_\_

### Inpatients w/ Unknown or Expired Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to print a list of Veteran inpatients with no insurance, expiring insurance (expired or will expire within 30 days), or unknown insurance. The user may include any or all of these categories. The output may then be used to obtain insurance information from the Veterans while current inpatients.

If the site is multidivisional, one, many, or all divisions may be included. A subtotal is provided for each division.

The report may be printed for the current date or a specified date range. When the user selects a date range, all patients who were admitted during that date range are included. If the user opts to display the current date, all patients who are currently inpatients are included. The report may be further sorted by ward.

Producing this output may be very time-consuming. It is recommended to queue this option and run it during off hours. The required margin width is 132 columns.

Sample Output

JUN 1,1993 PAGE 1

VETERANS WITH NO INSURANCE THAT WERE ADMITTED BETWEEN MAY 22,1993 AND JUN 1,1993

PATIENT/WARD PT ID ADMISSION DATE AGE %SC MARITAL STATUS EMPLOYMENT STATUS

--------------------------------------------------------------------------------------------------------------------------------

Division: NORTHSIDE

=================================================================================================================================

Ward: 11B

IBpatient,one XXX-XX-XXXX MAY 22,1993@16:37 55 40 WIDOW/WIDOWER EMPLOYED FULL TIME

11B Address: 555 KILBOURN Tele: XXX-XXX-XXXX

ANYTOWN,NY XXXXX

Employer: ACME CONSTRUCTION Tele: XXX-XXX-XXXX

MAPLE AVE

ANYTOWN,NY 12208

IBpatient,two XXX-XX-XXXX MAY 30,1993@07:00 62 0 MARRIED EMPLOYED FULL TIME

11B Address: 000 1ST ST. Tele: XXX-XXX-XXXX

ANYTOWN,NY 12208

Employer: ALBANY PLUMBING Tele: XXX-XXX-XXXX

23 RAILROAD AVE.

ANYTOWN,NY 12208

---------------------------------------------------------------------------------------------------------------------------------

Ward: 11C

IBpatient,three XXX-XXX-XXXX JUN 1,1993@11:32 42 0 MARRIED EMPLOYED FULL TIME

11C Address: 121 TEST AVE Tele: XXX-XXX-XXXX

ANYTOWN,NY 12184

Employer: VAMC ALBANY Tele: XXX-XXX-XXXX

113 HOLLAND AVE.

ANYTOWN,NY 12208

---------------------------------------------------------------------------------------------------------------------------------

Subtotal: 3

----------------

Total: 3

JUN 1,1993 PAGE 2

VETERANS WHOSE INSURANCE IS EXPIRED OR WILL EXPIRE WITHIN 30 DAYS THAT WERE ADMITTED BETWEEN MAY 22,1993 AND JUN 1,1993

PATIENT/WARD PT ID ADMISSION DATE AGE %SC MARITAL STATUS EMPLOYMENT STATUS

---------------------------------------------------------------------------------------------------------------------------------

Division: NORTHSIDE

=================================================================================================================================

Ward: 11B

IBpatient,one XXX-XXX-XXXX MAY 25,1993@16:37 35 0 WIDOW/WIDOWER NOT EMPLOYED

11B Address: 49 TEST AVE Tele: XXX-XXX-XXXX

ANYTOWN,NY 12180

Insurance: XYZ INS Expiration: JUN 15,1993

---------------------------------------------------------------------------------------------------------------------------------

----------------

Subtotal: 1

----------------

Total: 1

JUN 1,1993 PAGE 3

VETERANS WHOSE INSURANCE IS UNKNOWN THAT WERE ADMITTED BETWEEN MAY 22,1993 AND JUN 1,1993

PATIENT/WARD PT ID ADMISSION DATE AGE %SC MARITAL STATUS EMPLOYMENT STATUS

---------------------------------------------------------------------------------------------------------------------------------

Division: NORTHSIDE

=================================================================================================================================

Ward: 11C

IBpatient,one XXX-XXX-XXXX MAY 22,1993@16:37 82 10 WIDOW/WIDOWER RETIRED

11C Address: 55 TEST AVE Tele: XXX-XXX-XXXX

ANYTOWN,NY 12180

IBpatient,two XXX-XXX-XXXX MAY 25,1993@07:00 60 0 MARRIED EMPLOYED FULL TIME

11C Address: 256 HOLLAND AVE. Tele: XXX-XXX-XXXX

ANYTOWN,NY 12208

Employer: ABC SECURITY Tele: XXX-XXX-XXXX

519 4TH ST

ANYTOWN,NY 12208

---------------------------------------------------------------------------------------------------------------------------------

Subtotal: 2

----------------

Total: 2

### Outpatients w/Unknown or Expired Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to print a list of Veteran outpatients with no insurance, expiring insurance (expired or will expire within 30 days), or unknown insurance for a specified date range. The user may include any or all of these categories.

One, many, or all divisions (if the site is multidivisional) and clinics may be included. A subtotal is provided for each division/clinic.

This option may be used to identify those patients who should be interviewed for insurance information while visiting a specified clinic. This report may be printed for a specified date or range of dates and sent to the appropriate clinic for follow-up.

This output may be very time-consuming and should be queued. The margin width is 132 columns.

Sample Output

OUTPATIENT VISITS FOR VETERANS WITH NO INSURANCE JUN 1,1992 PAGE 1

FOR APPOINTMENTS FROM MAY 22,1992 TO JUN 1,1992

PATIENT NAME PT ID APPT DATE/TIME AGE %SC MARITAL STATUS EMPLOYMENT STATUS

------------------------------------------------------------------------------------------------------------------

Division: ALBANY

Clinic: DERMATOLOGY

IBpatient,one XXX-XXX-XXXX MAY 22,1992@16:37 55 40 WIDOW/WIDOWER EMPLOYED FULL TIME

Address: 555 TEST Tele: XXX-XXX-XXXX

ANYTOWN,NY XXXXX

Employer: ACME CONSTRUCTION Tele: XXX-XXX-XXXX

MAPLE AVE

ANYTOWN,NY 12208

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Clinic Subtotal : 1

Clinic: ORTHOPEDIC

IBpatient,two XXX-XXX-XXXX JUN 1,1992@11:32 42 0 MARRIED EMPLOYED FULL TIME

Address: 121 TEST AVE Tele: XXX-XXX-XXXX

ANYTOWN,NY 12184

Employer: VAMC ALBANY Tele: XXX-XXX-XXXX

113 HOLLAND AVE.

ANYTOWN,NY 12208

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Clinic Subtotal : 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Division Subtotal: 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Total : 2

OUTPATIENT VISITS FOR VETERANS WHOSE INSURANCE IS EXPIRED OR WILL EXPIRE WITHIN 30 DAYS JUN 1,1992 PAGE 1

FOR APPOINTMENTS FROM MAY 22,1992 TO JUN 1,1992

PATIENT NAME PT ID APPT DATE/TIME AGE %SC MARITAL STATUS EMPLOYMENT STATUS

------------------------------------------------------------------------------------------------------------------

Division: ALBANY

Clinic: OPHTHALMOLOGY

IBpatient,one XXX-XXX-XXXX MAY 25,1992@16:37 35 0 WIDOW/WIDOWER NOT EMPLOYED

Address: 49 TEST AVE Tele: XXX-XXX-XXXX

ANYTOWN,NY 12180

Insurance: XYZ INS Expiration: JUN 15,1992

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Clinic Subtotal : 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Division Subtotal: 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Total : 1

OUTPATIENT VISITS FOR VETERANS WHOSE INSURANCE IS UNKNOWN JUN 1,1992 PAGE 1

FOR APPOINTMENTS FROM MAY 22,1992 TO JUN 1,1992

PATIENT NAME PT ID APPT DATE/TIME AGE %SC MARITAL STATUS EMPLOYMENT STATUS

------------------------------------------------------------------------------------------------------------------

Division: ALBANY

Clinic: MEDICAL

IBpatient,two XXX-XXX-XXXX MAY 22,1992@16:37 82 10 WIDOW/WIDOWER RETIRED

Address: 55 TEST AVE Tele: XXX-XXX-XXXX

ANYTOWN,NY 12180

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Clinic Subtotal : 1

Clinic: SURGICAL

IBpatient,three XXX-XXX-XXXX MAY 25,1990@07:00 60 0 MARRIED EMPLOYED FULL TIME

Address: 256 TESTING AVE. Tele: XXX-XXX-XXXX

ANYTOWN,NY 12208

Employer: GAVIN'S SECURITY Tele: XXX-XXX-XXXX

519 4TH ST

ANYTOWN,NY 12208

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Clinic Subtotal : 1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Division Subtotal: 2

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Total : 2

### Single Patient Means Test Billing Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Single Patient Means Test Billing Profile option provides a list of all Means Test/Category C charges within a specified date range for a selected patient.

The user will be prompted for the patient's name, date range, and device. The default at the Start with DATE prompt is October 1, 1990. This is the earliest date for which charges may be displayed.

This output displays the date the Means Test billing clock began, the bill date, bill type (including the treating specialty for inpatient copay charges), the bill number, the bill to date (for inpatient charges), the amount of each charge, and the total charges for the selected date range.

Sample Output

Means Test Billing Profile for Test,Name

From 01/01/14 through 10/29/19 OCT 29, 2019@08:54 Page: 1

BILL DATE BILL TYPE BILL \# BILL TO TOT CHARGE

----------------------------------------------------------------------------------------------

05/22/12 Begin Means Test Billing Clock

12/30/14 Begin Means Test Billing Clock

12/30/14 OUTPATIENT COPAY XXXXXXX \$15.00

12/31/14 OUTPATIENT COPAY XXXXXXX \$15.00

01/06/15 OUTPATIENT COPAY XXXXXXX \$15.00

01/13/15 OUTPATIENT COPAY XXXXXXX \$15.00

01/14/15 OUTPATIENT COPAY XXXXXXX \$15.00

01/14/15 FEE SERVICE/INPATIENT XXXXXXX 01/17/15 \$243.20 \*

01/14/15 FEE SERV INPT PER DIEM XXXXXXX 01/17/15 \$6.00 \*

01/14/15 FEE SERVICE/INPATIENT XXXXXXX 01/17/15 (\$243.20) \*

Charge Removal Reason: ENTERED IN ERROR

01/14/15 FEE SERV INPT PER DIEM XXXXXXX 01/17/15 (\$6.00) \*

Charge Removal Reason: ENTERED IN ERROR

01/14/15 CC INPATIENT XXXXXXX 01/15/15 \$25.00 \*

01/14/15 CC PER DIEM XXXXXXX 12/29/15 \$698.00 \*

01/14/15 CC PER DIEM XXXXXXX 01/15/15 \$2.00 \*

\*\*\*\*\*\*\*\*\*\*Bills display continue on several pages\*\*\*\*\*\*\*\*\*\*

07/01/15 CCN PER DIEM XXXXXXX 07/31/15 (\$60.00) \*

Charge Removal Reason: ELIGIBILITY INCORRECT

08/01/15 CC MTF PER DIEM XXXXXXX 08/31/15 \$60.00 \*

08/01/15 CC MTF PER DIEM XXXXXXX 08/31/15 (\$60.00) \*

Charge Removal Reason: CHANGE IN ELIGIBILITY

09/01/15 CHOICE PER DIEM XXXXXXX 09/30/15 \$58.00 \*

09/01/15 CHOICE PER DIEM XXXXXXX 09/30/15 (\$58.00) \*

Charge Removal Reason: ENTERED IN ERROR

12/15/18 CC RX COPAY XXXXXXX \$8.00

12/15/18 CC RX COPAY XXXXXXX (\$8.00)

Charge Removal Reason: ENTERED IN ERROR

06/06/19 CC URGENT CARE XXXXXXX \$30.00

06/06/19 CC URGENT CARE XXXXXXX (\$30.00 )

Charge Removal Reason: UC - CHANGE IN ELIGIBILITY

09/02/19 CC OUTPATIENT XXXXXXX \$15.00

09/02/19 CC OUTPATIENT XXXXXXX (\$15.00)

Charge Removal Reason: ELIGIBILITY INCORRECT

'\*' - Geographic Means Test rates

----------\$303.00

## Third-Party Billing Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Print Bill Addendum Sheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print the addendum sheets that may accompany HCFA-1500 prescription refills or prosthetic bills. The addendum contains information that could not fit on the bill form.

Prescription refill data provided on the addendum sheet may include prescription number, refill date, drug, quantity, \# of days’ supply, and the National Drug Code (NDC) \#. Prosthetic data will include the date delivered to the patient and the item.

For the bill addendums to automatically print for every HCFA-1500 bill with prescription refills or prosthetic items, the billing default printer for the BILL ADDENDUM form type must be set through the Select Default Device for Forms option found on the System Manager's Integrated Billing Menu.

Sample Output

BILL ADDENDUM FOR IBpatient,one - XXXXXX JAN 28, 1994 11:00 PAGE 1

------------------------------------------------------------------------------

PRESCRIPTION REFILLS:

XXX Jan 03, 1994 DIGOXIN 0.25MG QTY: 60 DAYS SUPPLY: 30 NDC \#: XX-XXX-XXX

XXX Jan 10, 1994 NAPROXEX 250MG S.T. QTY: 10 DAYS SUPPLY: 10 NDC \#: XX-XXX-XXX

PROSTHETIC ITEMS:

JAN 02, 1994 WALKER-FOLDING-WHEELED

JAN 02, 1994 CANE-ALL OTHER

### Authorize Bill Generation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Authorize Bill Generation option is used to authorize the printing of third-party bills and the release of the information to Fiscal Service.

When a billing record is selected, the system performs a check to determine if another user is currently processing the same record. If not, the system will lock the record. If the lock is unsuccessful, it means another user already has that record locked and the following message will be displayed:

> No further processing of this record permitted at this time.  
> Record locked by another user. Try again later.

A final review/edit of the information in the billing record may be performed through this option. The data is arranged so that it may be viewed and edited through various screens. The data is grouped into sections for editing. Each section is labeled with a number to the left of the data items. Data group numbers enclosed by brackets (\[ \]) may be edited while those enclosed by arrows (\< \>) may not. The patient's name, social security number, bill number, bill classification (Inpatient or Outpatient), and screen number appear at the top of every screen. A \<?\> entered at the prompt that appears at the bottom of every screen will provide the user with a HELP SCREEN for that screen. The HELP SCREEN lists the data groups found on that screen and provides the name and number of each available screen in the option. For more detailed documentation on editing a bill, please see the Enter/Edit Billing Information option documentation.

For a detailed explanation of all screens, please see the Supplement at the end of this section.

The CAN INITIATOR AUTHORIZE? site parameter and the IB AUTHORIZE security key affect the prompts that appear at the end of this option.

CAN INITIATOR AUTHORIZE?

If set to YES, the user who initiated the bill can authorize the generation of the billing form (if required security key is held). If this parameter is set to NO, the initiator of the bill will not be allowed to authorize its generation.

IB AUTHORIZE

Allows the holder to authorize the generation of bills. The user must hold this key to access this option.

The UB-82, UB-92, and HCFA-1500 billing forms are the output that may be produced from this option. The data elements, and design of these forms, have been determined by the National Uniform Billing Committee and have been adapted to meet the specific needs of the Department of Veterans Affairs. The billing forms must be generated (printed) at 80 characters per line at 10 pitch. Copies of the billing forms are included in the Print Bill option documentation.

### Enter / Edit Billing Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB EDIT security key is required to access this option.

The Enter/Edit Billing Information option is used to enter the information required to generate a third-party bill and to edit existing billing information. A new bill may be entered, or an existing bill can be edited. Only existing bills that have not been authorized or canceled may be edited. Once a bill has been filed (billing record number established), it cannot be deleted. The bill may be canceled through the Cancel Bill option.

If the selected patient's eligibility has not been verified and the ASK HINQ IN MCCR parameter is set to YES, the user will have the opportunity to enter a HINQ (Hospital Inquiry) request into the HINQ Suspense File. This request will be transmitted to the Veterans Benefits Administration to obtain the patient's eligibility information. If Means Test data such as category, Means Test last applied, and date Means Test completed is available, it will be displayed after the patient’s name or bill number has been entered.

When entering a new bill, the system will prompt for EVENT DATE. When billing for multiple outpatient visits, the date of the initial visit is used. For an inpatient bill, the date of the admission is used. If an interim bill is being issued, the EVENT DATE should be the date of admission for that episode of care.

The Medical Care Cost Recovery data is arranged so that it may be viewed and edited through various screens. The data is grouped into sections for editing. Each section is labeled with a number to the left of the data items. Data group numbers enclosed by brackets (\[ \]) may be edited while those enclosed by arrows (\< \>) may not. The patient's name, social security number, bill number, bill classification (Inpatient or Outpatient) and screen number appear at the top of every screen. A \<?\> entered at the prompt that appears at the bottom of every screen will provide the user with a HELP SCREEN for that screen. The HELP SCREEN lists the data groups found on that screen and provides the name and number of each available screen in the option.

### Cancel Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB AUTHORIZE security key is required to access this option.

The Cancel Bill option allows the user to cancel a bill at any point in the billing process. Once the bill is canceled, there is no way to view the data contained in that bill.

If the user selects a bill that has been previously canceled, certain prompts will appear with defaults.

A mail group may be specified (through the site parameters) so that every time a bill is canceled, all members of this group are notified through electronic mail. If this group is not specified, only the billing supervisor and the user who canceled the bill will be recipients of the message. An example of this message may be found in the Example Section of this option.

When a bill is canceled, it is removed as a Prior Bill Number from previous bills in the Primary/Secondary/Tertiary Series.

Sample Mail Message

Subj: MAS UB-92 BILL CANCELLATION BULLETIN \[#120774\] 22 Mar 95 13:22 11 Lines

From: EMPLOYEE (ALBANY ISC) in 'IN' basket. Page 1

------------------------------------------------------------------------------

The following UB-92 bill has been canceled:

Bill Number: XXXXXX

Patient Name: IBpatient,one PT ID: XXX-XXX-XXXX

Event Date: MAR 12,1995@08:00

Reason for cancellation: Patient is service connected.

Status when canceled: CANCELLED - Not passed to AR

Select MESSAGE Action: IGNORE (in IN basket)//

### Copy and Cancel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB AUTHORIZE security key is required to access this option.

The CAN INITIATOR AUTHORIZE? site parameter affects this option.

This option is used to cancel a bill, copy all the information into a new bill, and edit the new bill where necessary. The status of the new bill is ENTERED/NOT REVIEWED. This process prevents having to use the Enter/Edit Billing Information option to create a new bill that would require the re-entry of ALL data. Bills returned from Accounts Receivable with minor inconsistencies can quickly and easily be corrected through this option.

The Medical Care Cost Recovery data is arranged so that it may be viewed and edited through various screens. The data is grouped into sections for editing. Each section is labeled with a number to the left of the data items. Data group numbers enclosed by brackets (\[ \]) may be edited while those enclosed by arrows (\< \>) may not. The patient's name, social security number, bill number, bill classification (Inpatient or Outpatient), and screen number appear at the top of every screen. A \<?\> entered at the prompt that appears at the bottom of every screen will provide the user with a HELP SCREEN for that screen. The HELP SCREEN lists the data groups found on that screen and provides the name and number of each available screen in the option.

A mail group may be specified (through the site parameters) so that every time a bill is disapproved during the authorization phase of the billing process, or suspended during the generation phase, all members of this group are notified via electronic mail. If this group is not specified, only the billing supervisor, the initiator of the billing record, and the user who disapproved or generated the bill will be recipients of the message. Examples of messages may be found in the Enter/Edit Billing Information documentation. An explanation of how the bill mailing address field is determined is provided in the Supplement at the end of this option documentation.

The UB-82, UB-92, and HCFA-1500 billing forms are the output that may be produced from this option. The data elements, and design of both forms, have been determined by the National Uniform Billing Committee and have been adapted to meet the specific needs of the Department of Veterans Affairs. Both must be generated (printed) at 80 characters per line at 10 pitch. Copies of the billing forms are included in the Print Bill option documentation.

Please see the Supplement found at the end of this section for descriptions of the parameter and security key as well as a description of most fields included on the billing screens.

### Delete Auto Biller Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to delete entries from the Automated Biller Errors/Comments report prior to a user-selected date for any entry not associated with a bill.

The auto biller checks a variety of data elements concerning an event before a bill is created. The auto biller will only create reimbursable insurance bills, so the patient must be a Veteran with active insurance. The disposition prior to the event date is checked and if the need for care was related to an accident or the Veteran's occupation, the auto biller will not create a bill. Since dental is usually billed separately, any event with a dental clinic stop will also be excluded. The auto biller also checks to ensure that the event has not already been billed.

Entries are removed from the Automated Biller Errors/Comments report in two ways. If a bill was created for the event, the bill's entry is removed from the report when the bill is either printed or canceled. If a bill was not created, this option must be used to delete the entry.

The user will be prompted for a date. The default value provided is three days before the current date.

### Print Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Bill option is used to print third-party bills on the appropriate form (UB-82/92 or HCFA-1500) after all required information has been input and the billing record has been authorized. The user may also reprint a previously printed bill.

A final review of the information in the billing record may be performed through this option. The data is arranged so that it may be viewed through various screens. The patient's name, social security number, bill number, bill classification (Inpatient or Outpatient), and screen number appear at the top of every screen. A \<?\> entered at the prompt that appears at the bottom of each screen will provide the user with a HELP SCREEN for that screen. The HELP SCREEN lists the name and number of each available screen for the working bill and the data groups for that screen.

No editing of the data is allowed in this option. Data can be edited through the Enter/Edit Billing Information option, if necessary.

The UB-82, UB-92, and HCFA-1500 billing forms are the output that may be produced from this option. The data elements, and design of these forms, have been determined by the National Uniform Billing Committee and have been adapted to meet the specific needs of the Department of Veterans Affairs. The billing forms must be generated (printed) at 80 characters per line at 10 pitch.

### Patient Billing Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Billing Inquiry option allows the user to display/print information on any reimbursable insurance bill, pharmacy copay, or Means Test bill. The information provided differs depending on the bill type.

For reimbursable insurance bills, the information provided includes bill status, rate type, reason canceled (if applicable), admission date (for inpatients), all outpatient visits (for outpatients), charges, the amount paid, statement to and from dates, each action that was taken on that bill, and the user who performed it. If the user opts to view the full inquiry, address information from the PATIENT file and the bill is also provided.

The information provided in a brief inquiry for Pharmacy Copay charges includes the date of the charge, type of charge (syntax: patient eligibility - action type - status), brief description (syntax: prescription \# - drug name - \# of units), amount of charge or credit, and an explanation of any charge removed, if applicable. A full inquiry, in addition to the information provided in the brief inquiry, provides information from the PRESCRIPTION file, as well as the address information on the patient.

The display/output for Means Test bills is very similar to the brief inquiry for Pharmacy Copay. It includes the date of the charge, charge type, brief description, units, and amount of charge. A full inquiry also includes address information on the patient.

Sample Outputs

Full inquiry for a reimbursable insurance bill.

IBpatient,one XXX-XXX-XXXX XXX-XXXXXX FEB 19, 1992@14:17 PAGE:1

=============================================================================

Bill Status : PRINTED - RECORD IS UNEDITABLE

Rate Type : REIMBURSABLE INSURANCE

Op Visit dates : APR 14,1992

Charges : \$148.00

LESS Offset : \$30.00

Bill Total : \$118.00

Statement From : APR 14,1992

Statement To : APR 14,1992

Entered : APR 15, 1992 by ED

First Reviewed : APR 16, 1992 by SUE

Last Reviewed : APR 16, 1992 by SUE

Authorized : APR 16, 1992 by SUE

Last Printed : APR 16, 1992 by GARY

IBpatient,one XXX-XXX-XXXX XXX-XXXXXX FEB 19, 1992@14:17 PAGE: 2

=============================================================================

\*\*\* ADDRESS INFORMATION \*\*\*

Patient Address: 117 TEST DRIVE

ANYTOWN, NEW YORK

XXX-XXX-XXXX

Mailing Address: ABC

1262 TEST AVENUE

ANYTOWN, CALIFORNIA 12345

Ins Co. Address: ABC

1262 TEST AVENUE

ANYTOWN, CALIFORNIA 12345

XXX-XXX-XXXX

Full inquiry for a Means Test bill.

IBpatient,one XXX-XXX-XXXX XXX-XXXXXX FEB 24, 1992@09:09 PAGE: 1

==============================================================================

FEB 14, 1992 INPT COPAY (MED) NEW INPT CO-PAY (MED) 1 \$200.00

FEB 20, 1992 INPT COPAY (MED) CAN INPT CO-PAY (MED) 1 (\$200.00)

Charge Removal Reason: MT CHARGE EDITED

------------

\$0.00

IBpatient,one XXX-XXX-XXXX XXX-XXXXXX FEB 24, 1992@09:09 PAGE: 2

==============================================================================

\*\*\* ADDRESS INFORMATION \*\*\*

Patient Address: 28 TEST RD

ANYTOWN, MASSACHUSETTS

XXX-XXX-XXXX

Brief inquiry for a Pharmacy Copay bill.

IBpatient,one XXX-XXX-XXXX XXX-XXXXXX FEB 24, 1992@09:18 PAGE:1

DATE CHARGE TYPE BRIEF DESCRIPTION UNITS CHARGE

=============================================================================

MAR 15, 1991 SC RX COPAY NEW RX#XXXXXX-REF 5-ENDU 3 \$6.00

MAR 15, 1991 SC RX COPAY NEW RX#XXXXXX 9999-CLONI 4 \$8.00

-----------

\$14.00

### Print Auto Biller Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print the Automated Biller Errors/Comments report. The results of the execution of the auto biller are listed in this report. For Claims Tracking events for which the auto biller attempted to create a bill, this report will list either the reason a bill was not created or the bill number and any comments on the bill.

The auto biller checks a variety of data elements concerning an event before a bill is created. The auto biller will only create reimbursable insurance bills, so the patient must be a Veteran with active insurance. The disposition prior to the event date is checked and if the need for care was related to an accident or the Veteran's occupation, the auto biller will not create a bill. Since dental is usually billed separately, any event with a dental clinic stop will also be excluded. The auto biller also checks to ensure that the event has not already been billed.

Entries are removed from the Automated Biller Errors/Comments report in two ways. If a bill was created for the event, the bill's entry is removed from the report when the bill is either printed or canceled. If a bill was not created, the Delete Auto Biller Results option must be used to delete the entry.

The bills will be grouped on the output by the date entered. The following information may appear on the report: patient name, event type, episode date, bill number, bill status, the timeframe of the bill, and statement covers from and to dates. Comments relating to individual bills may also be provided.

The user will be prompted for a date range, a patient range, and a device.

Sample Output

AUTOMATED BILLER ERRORS/COMMENTS FOR Nov 1, 1993 - Nov 10, 1993 DEC 10,1993 13:19 PAGE 1

EVENT BILL TIMEFRAME OF STATEMENT STATEMENT

PATIENT TYPE EPISODE DATE NUMBER STATUS BILL COVERS FROM COVERS TO

---------------------------------------------------------------------------------------------------------------------------------

DATE ENTERED: NOV 1,1993

IBpatient, one XXXXX INPA SEP 1,1993 17:07 XXXXXX ENTERED INTERIM - FIRST SEP 1,1993 SEP 30,1993

IBpatient, two XXXXX INPA SEP 1,1993 01:00 XXXXXX ENTERED INTERIM - FIRST SEP 1,1993 SEP 30,1993

IBpatient, three XXXXX INPA SEP 14,1993 11:42 XXXXXX ENTERED ADMIT THRU DISC SEP 14,1993 SEP 14,1993

No billable Days.

DATE ENTERED: NOV 3,1993

IBpatient,one XXXXX INPA SEP 1,1993 17:07 XXXXXX ENTERED INTERIM - CONTI OCT 1,1993 OCT 31,1993

IBpatient,one XXXXX INPA SEP 1,1993 01:00 XXXXXX ENTERED INTERIM - CONTI OCT 1,1993 OCT 31,1993

DATE ENTERED: NOV 8,1993

IBpatient,one XXXXX INPA SEP 15,1993 12:30 XXXXXX ENTERED INTERIM - CONTI OCT 1,1993 OCT 31,1993

### Print Authorized Bills

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Authorized Bills option will print all bills with a status of AUTHORIZED in a user-specified order. The bills may be sorted by zip code, insurance company name, and patient name.

The user may enter \<??\> at the Begin printing bills? prompt to see a list of all the bills that will print when this option is utilized. The list will show the bill number, patient name, event date, inpatient or outpatient bill, bill type, bill status (AUTHORIZED), and bill form type. If this list is quite lengthy, queue the output to print during off hours.

The user is not prompted for a device in this option. Each bill form type will print on the billing default printer specified through the Select Default Device for Forms option on the System Manager's Integrated Billing Menu. Any form type not set up there, will not print when utilizing this option.

## Return Bill Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit Returned Bill

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB EDIT security key is required to access this option.

The Edit Returned Bill option is used to correct bills with a status of RETURNED FROM AR (NEW) that have been returned to MAS from Accounts Receivable. Generate the returned bill report through the Returned Bill List option before utilizing this option. That report contains a listing of all bills that have been returned to MAS providing the reason returned for each. This information is required to make the appropriate corrections to each bill. The bill number appears on that report preceded by the station number. The station number should not be entered when selecting the bill for editing.

After editing, return the bill to Accounts Receivable and print the bill if the required security key is held. It should be noted that returned bills with a status of RETURNED FOR AMENDMENT cannot be edited through this option and must be corrected through the Copy and Cancel option.

Supplemental information such as sample billing screens is provided in the Supplement at the end of this section.

10. It is possible to edit a returned bill if it is not an electronically transmittable bill. For returned electronically transmittable bills/claims, the IB COPY AND CANCEL option will need to be used.

### Returned Bill List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Returned Bill List option prints a listing of all bills that have been returned to MAS from Accounts Receivable. When the user logs onto the Billing System, the following message appears:

> You have {#} bill(s) returned from Fiscal (New Bill).

When this occurs, the user needs to generate the output produced by this option to obtain a listing of the returned bills.

The following data items may be provided for each bill on the list: bill number, payer, the previous and current status of the bill, original bill amount, service which approved the bill and when, returned by, reason returned, and date returned. The bill number appears on this report preceded by the station number. The station number should not be entered when selecting the bill for editing.

The user will need this report when using the Edit Returned Bill option to determine why the bill was returned and what needs to be corrected. Once bills have been corrected and sent back to Accounts Receivable, these no longer appear on the Returned Bill List.

Sample Output

\<\< BILL RETURNED FROM AR \>\>

============================================================================

BILL NO.: XXX-XXXXXX PAYER: ABC

PREV. STATUS: NEW BILL CURR. STATUS: RETURNED FROM AR (NEW)

ORIGINAL AMOUNT: \$70 SERVICE: MEDICAL ADMINISTRATION

\<\< SERVICE \>\>

APPROV. BY: JAMES DATE: JUL 2,1990

\<\< FISCAL \>\>

RETN'D BY: ALAN DATE: JUL 5,1990

RETN'D REASON:

RETURNED FOR CORRECT RATES

============================================================================

\<\< BILL RETURNED FROM AR \>\>

============================================================================

BILL NO.: XXX-XXXXXX PAYER: ABC

PREV. STATUS: NEW BILL CURR. STATUS: RETURNED FROM AR (NEW)

ORIGINAL AMOUNT: \$673 SERVICE: MEDICAL ADMINISTRATION

\<\< SERVICE \>\>

APPROV. BY: JAMES DATE: JUL 2,1990

\<\< FISCAL \>\>

RETN'D BY: ALAN DATE: JUL 5,1990

RETN'D REASON:

RETURNED FOR CORRECT INS ADDRESS

### Return Bill to A/R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB AUTHORIZE security key is required to access this option.

The Return Bill to A/R option is used to send bills that have been returned to MAS back to Accounts Receivable after correction. Editing is not allowed in this option. All editing is done through the Edit Returned Bill option; however, all billing screens associated with the bill may be displayed for viewing.

### UB-82 Test Pattern Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The UB-82 Test Pattern Print option is used to print a test pattern on the UB-82 billing form so that the form alignment in the printer may be checked. This will ensure that each data item prints in the correct block on the form.

The test pattern displays which data element should appear in the different blocks of the billing form. For example, in Block 3 - Patient Control Number, BILL NUMBER will be printed in that block when this option is utilized.

Sample Output

\*\*\* UB-82 TEST PATTERN \*\*\*

AGENT CASHIER

AGENT CASHIER STREET F. L. 2 BILL NUMBER XXX

CITY STATE ZIP

PHONE \# BC/BS \# FED TAX \# F. L.9

PATIENT NAME PATIENT ADDRESS

PT DOB X X ADM DT HR X X AH DH XX FROM TO F. L.27

OC DATE OC DATE OC DATE OC DATE OC DATE

MAILING ADDRESS NAME

STREET ADDRESS 1 CC CC CC CC CC F. L. 45

STREET ADDRESS 2

STREET ADDRESS 3

CITY STATE ZIP

000 DAYS MEDICAL CARE

REV CODE 1 000.00 000 00 0000.00

REV CODE 2 000.00 000 00 0000.00

REV CODE 3 000.00 000 00 0000.00

SUBTOTAL 00000.00

TOTAL 00000.00

PAYER 1 X X

PAYER 2 X X

PAYER 3 X X

INSURED NAME 1 X XX POLICY \# 1 GROUP NAME 1 GROUP \# 1

INSURED NAME 2 X XX POLICY \# 2 GROUP NAME 2 GROUP \# 2

INSURED NAME 3 X XX POLICY \# 3 GROUP NAME 3 GROUP \# 3

X X EMPLOYER NAME CITY STATE ZIP

PRINCIPAL DIAGNOSIS CODE CODE CODE CODE CODE

X PRINCIPAL PROCEDURE CODE DATE CODE DATE CODE DATE

TX. AUTH. Dept. Veterans Affairs F. L. 93

Patient ID: XXXXXXXXX

Bill Type: XXXX XXXXXXX

UB-82 TEST PATTERN

\*\*TEST PATTERN\*\* UB-82 SIGNER NAME

UB-82 SIGNER TITLE DATE

### UB-92 Test Pattern Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The UB-92 Test Pattern Print option is used to print a test pattern on the UB-92 billing form so that the form alignment in the printer may be checked. This will ensure that each data item prints in the correct block on the form.

Sample Output

XXXXSR \*\*\* UB-92 TEST PATTERN \*\*\*

AGENT CASHIER

AGENT CASHIER STREET BN XXX XXX

CITY STATE ZIP

PHONE \# TAX# XXXX 5/1/93 5/4/93

PATIENT NAME PT SHORT ADDRESS

DOB X X DATE HR X X DR ST 000-00-0XXX CC CC CC CC CC CC CC

OC DATE OC DATE OC DATE OC DATE OC DATE

RESPONSIBLE PARTY'S NAME

STREET ADDRESS 1

STREET ADDRESS 2

STREET ADDRESS 3

CITY STATE ZIP

CD1 REV CODE description xx xxxx.xx

CD2 REV CODE description xx xxxx.xx

CD3 REV CODE description xx xxxx.xx

Subtotal xxxx.xx

Total xxxx.xx

For your information, even though the patient may be otherwise eligible

for Medicare, no payment may be made under Medicare to any Federal provider

of medical care or services and may not be used as a reason for non-payment.

Please make your check payable to the Department of Veterans Affairs and

send to the address listed above.

The undersigned certifies that treatment rendered is not for a

service connected disability.

Name of Payer 1 Provider \# x x

Name of Payer 2 Provider \# x x

Name of Payer 3 Provider \# x x

Insured's Name 1 x Insurance \# Group Name Group \#

Insured's Name 2 x Insurance \# Group Name Group \#

Insured's Name 3 x Insurance \# Group Name Group \#

Treatment Auth. Cd x Employer Name Employer Location

x Employer Name Employer Location

x Employer Name Employer Location

PDX Dx Cd Dx Cd Dx Cd Dx Cd Dx Cd Dx Cd Dx Cd Dx Cd ADMT DX

P-code mmddyy P-code mmddyy P-code mmddyy Attending Phys. ID#

P-code mmddyy P-code mmddyy P-code mmddyy Other Phys. ID#

Patient ID#: xxx-xx-xxxx

Bill Type: xxx xxxxxx

UB 92 TEST PATTERN Provider Representative DATE

\*\*\* comment \*\*\*

### HCFA-1500 Test Pattern Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to print a test pattern on the HCFA-1500 form for the form alignment in the printer to be checked. The test pattern displays which data element should appear in the different blocks of the billing form. This ensures that each data item prints in the correct block on the form.

Sample Output

INSURANCE CARRIER NAME

CARRIER ADDRESS LINE 1

CARRIER ADDRESS LINE 2

CARRIER ADDRESS LINE 3

CARRIER CITY, STATE ZIP

SUBSCRIBER ID#

PATIENT NAME MM DD YY INSURED'S NAME

PATIENT ADDRESS STREET INSURED'S ADDRESS STREET

PATIENT ADDRESS CITY ST INSURED'S ADDRESS CITY ST

PT ZIP CODE 999 999-9999 INS ZIP CODE 999 999-9999

OTHER INSURED'S NAME INSURED'S POLICY GROUP

OTHER POLICY NUMBER MM DD YY

MM DD YY ST INSURED'S EMPLOYER

OTHER'S EMPLOYER INSURANCE PLAN NAME

OTHER'S INSURANCE PLAN

MM DD YY MM DD YY MM DD YY MM DD YY

REFERRING PHYSICIAN PHYSICIAN ID MM DD YY MM DD YY

9999.99 9999.99

X99.99 X99.99

X99.99 X99.99

MM DD YY MM DD YY CPT MODIF DIAG 9999.99 BC/BS#

MM DD YY MM DD YY CPT MODIF DIAG 9999.99 BC/BS#

FEDERAL TAX ID PAT ACCT# 9999.99 9999.99 9999.99

VAMC AGENT CASHIER (999) 999-9999

STREET ADDRESS STREET ADDRESS

CITY, STATE ZIP CITY, STATE ZIP

### Outpatient Visit Date Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Visit Date Inquiry option allows the user to display information on any outpatient insurance bill for a selected patient. The user will be prompted for a patient name and an outpatient visit date. Select any patient with billed outpatient visits. \<??\> may be entered at the second prompt for a list of billed visits for the selected patient.

The information provided includes bill status, rate type, reason canceled (if applicable), outpatient visit date, charges, the amount paid, the statement from and to dates, each action that was taken on that bill, the date, and the user who performed it.

Sample Output

IBpatient,one XXX-XX-XXXX XXX-XXXXXX MAR 19, 1992@14:17 PAGE: 1

=============================================================================

Bill Status : CANCELLED - RECORD IS UNEDITABLE

Rate Type : REIMBURSABLE INS.

Reason Canceled: Write off

Op Visit dates : JAN 25,1992

Charges : \$148.00

LESS Offset : \$30.00

Bill Total : \$118.00

Statement From : JAN 25,1991

Statement To : JAN 25,1991

Entered : FEB 15, 1991 by EDWARD

First Reviewed : FEB 16, 1991 by SUE

Last Reviewed : FEB 16, 1991 by SUE

Authorized : FEB 16, 1991 by SUE

Last Printed : FEB 16, 1991 by GARY

Cancelled : MAR 6, 1992 by EMPLOYEE

# Patient Insurance Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patient Insurance Info View / Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Insurance Info View/Edit option is used to look at a patient's insurance information and edit that data, if necessary. The system groups information that is specific to the insurance company, specific to the patient, specific to the group plan, specific to the annual benefits available, and the annual benefits already used. This option also displays eIV Response data. Inactive policies will be listed if the patient has not been repointed from that inactive policy to an active policy.

About the Screens

In the top left corner of each screen is the screen title. On some screens, the following line is a description of the information displayed. A plus sign (+) at the bottom of the screen indicates there are additional screens. Left or right arrows (\<\<\< \>\>\>) may be displayed to indicate there is additional information to the left or right of the screen. Available actions are displayed below the screen. \<??\> entered at any Select Action prompt displays all available actions for that screen.

The user can QUIT from any screen; this will bring the user back one level or screen. EXIT is also available on most screens. When EXIT is entered, the user is prompted Exit option entirely? A yes response returns the user to the menu. A NO response has the same result as the QUIT action. For more information on the use of the List Manager utility, please refer to [Appendix C](#appendix-c-list-manager-appendix) at the end of this manual.

The following sections display screens under this option, with a brief action description. Once an action has been selected, \<??\> may be entered at most of the prompts that appear for lists of acceptable responses or instructions on how to respond.

## Patient Insurance Management Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a patient is selected, this screen is displayed listing all the patient's insurance policies. Information provided for each policy may include the type of policy, group name, holder, effective date, date of death, and expiration date.

| Acronym | Description                                                      | Action                                                                                                                                                                                                                          |
|---------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AP      | Add Policy                                                       | Allows the user to add an insurance policy for the selected patient.                                                                                                                                                            |
| VP      | Policy Edit / View (accesses Patient Policy Information screen)  | Allows the user to view and edit extensive insurance policy data.                                                                                                                                                               |
| DP      | Delete Policy                                                    | Allows the user to delete an insurance policy for the selected patient. IB INSURANCE SUPERVISOR security key is required.                                                                                                       |
| AB      | Annual Benefits -(accesses Annual Benefits Editor screen)        | Used to enter annual benefits data for the selected policy. IB GROUP PLAN EDIT security key is required for editing.                                                                                                            |
| EA      | Fast Edit All                                                    | A quick way to enter portions of the patient insurance information. IB GROUP PLAN EDIT security key is required for editing.                                                                                                    |
| BU      | Benefits Used (accesses the Benefits Used by Date Editor screen) | Used to enter policy benefits already used.                                                                                                                                                                                     |
| VC      | Verify Coverage                                                  | Allows the user to enter the system verification that the insurance coverage exists, and the information is correct.                                                                                                            |
| RI      | Personal Riders                                                  | Displays current riders and allows the addition of new riders.                                                                                                                                                                  |
| CP      | Change Patient                                                   | Allows the user to change to another patient without returning to the beginning of the option.                                                                                                                                  |
| WP      | Worksheet Print                                                  | Used to print the standard worksheet showing the data for the benefit year within the past 12 months. If no benefit year is on file, will print the standard form without the data. Must be printed at 132 column margin width. |
| PC      | Print Insurance Cov.                                             | Similar to a worksheet. Used when the bulk of the information is already in the computer. Will show the two most recent benefit years. If no benefit years are on file, will offer WP action (see above).                       |

<span id="_Toc143780845" class="anchor"></span>Table : Common Actions

## Patient Policy Information Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen is displayed listing expanded policy information for the selected company. Categories include utilization review data, subscriber data, subscriber's employer information, effective dates, plan coverage limitations, last contact, and comments on the patient policy or insurance group plan. The sections on user information and insurance company information are not editable.

| Acronym | Description                                                      | Action                                                                                                                                                                                                                    |
|---------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PI      | Change Plan Info                                                 | Allows entry / edit of group plan information. IB GROUP PLAN EDIT security is required to change plan information.                                                                                                        |
| UI      | UR Info                                                          | Allows entry / edit of utilization review information. IB GROUP PLAN EDIT security key is required for editing.                                                                                                           |
| ED      | Effective Dates                                                  | Allows the user to edit the effective date and expiration date of the insurance policy.                                                                                                                                   |
| SU      | Subscriber Update                                                | Allows the user to edit the subscriber (person who holds the insurance coverage) information.                                                                                                                             |
| IP      | Inactive Plan                                                    | Allows the user to inactivate an insurance plan or move subscribers from multiple insurance plans into one master plan. IB GROUP PLAN EDIT security key is required.                                                      |
| GC      | Group Plan Comments                                              | Allows the user to view, add, edit, or delete comments regarding the group plan. IB GROUP PLAN EDIT security key is required to edit comments.                                                                            |
| EM      | Employer Info                                                    | Allows the user to edit the subscriber's employer information.                                                                                                                                                            |
| PT      | Pt Policy Comments                                               | Allows the user to view, add, edit, or delete comments regarding the patient's policy.[^1] For more detailed information on Patient Policy Comments, refer to the *Electronic Insurance Verification* (*eIV) User Guide.* |
| EA      | Fast Edit All                                                    | A quick way to enter portions of the patient insurance information. IB GROUP PLAN EDIT security key is required for editing.                                                                                              |
| CP      | Change Policy Plan                                               | Allows the user to change the plan a Veteran is subscribing.                                                                                                                                                              |
| VC      | Verify Coverage                                                  | Allows the user to enter the system verification that the insurance coverage exists, and the information is correct.                                                                                                      |
| AB      | Annual Benefits (accesses Annual Benefits Editor screen)         | Used to enter annual benefits data for the selected policy.                                                                                                                                                               |
| CV      | Add/Edit Coverage                                                | Allows the user to add, edit, or delete (unwanted) coverage limitations for a specific plan. IB GROUP PLAN EDIT security key is required for editing.                                                                     |
| BU      | Benefits Used (accesses the Benefits Used by Date Editor screen) | Used to enter policy benefits already used.                                                                                                                                                                               |
| EB      | Expand Benefits                                                  | Displays detailed information on patient benefits.                                                                                                                                                                        |

<span id="_Toc143780846" class="anchor"></span>Table : Common Actions

## Annual Benefits Editor Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the benefit year is selected, this screen is displayed listing all the benefits for the selected insurance policy and benefit year. Benefit categories may include inpatient benefits, outpatient benefits, mental health, home health care, hospice, rehabilitation, and IV management.

| Acronym | Description        | Action                                                                       |
|---------|--------------------|------------------------------------------------------------------------------|
| PI      | Policy Information | Allows entry / edit of maximum out-of-pocket and ambulance coverage.         |
| IP      | Inpatient          | Allows entry / edit of inpatient benefits data.                              |
| OP      | Outpatient         | Allows entry / edit of outpatient benefits data.                             |
| MH      | Mental Health      | Allows entry / edit of mental health inpatient and outpatient benefits data. |
| HH      | Home Health        | Allows entry / edit of home health care benefits data.                       |
| HS      | Hospice            | Allows entry / edit of hospice benefits data.                                |
| RH      | Rehab              | Allows entry / edit of rehabilitation benefits data.                         |
| IV      | IV Mgmt.           | Allows entry / edit of intravenous management benefits data.                 |
| EA      | Edit All           | Lists editable fields line by line for quick data entry.                     |
| CY      | Change Year        | Allows the user to change to another benefit year.                           |

<span id="_Toc143780847" class="anchor"></span>Table : Common Actions

### Benefits Used by Date Editor Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the benefit year is selected, this screen is displayed listing all the benefits used for the selected insurance policy and benefit year. Benefit categories may include inpatient and outpatient deductibles.

| Acronym | Description | Action                                                                                        |
|---------|-------------|-----------------------------------------------------------------------------------------------|
| PI      | Policy Info | Allows entry / edit of policy information such as deductible met and pre-existing conditions. |
| OD      | Opt Deduct  | Allows entry / edit of the outpatient deductible insurance information.                       |
| ID      | Inpt Deduct | Allows entry / edit of the inpatient deductible insurance information.                        |
| AC      | Add Comment | Allows the user to add a comment regarding claims filed.                                      |
| EA      | Edit All    | A quick way to enter portions of the patient insurance information.                           |
| CY      | Change Year | Allows the user to change to another benefit year.                                            |

<span id="_Toc143780848" class="anchor"></span>Table : Common Actions

Sample Screens

Select Patient Insurance Menu \<TEST ACCOUNT\> Option: PI Patient Insurance Info View/Edit

Select PATIENT NAME: IBSUB,AC,ACTIVE A IBSUB,ACTIVE A 2-2-22 XXXXXXXXX NO NSC VETERAN

Enrollment Priority: GROUP 8c Category: ENROLLED End Date:

<u>Patient Insurance Management Jul 22, 2013@11:51:39 Page: 1 of 1</u>

Insurance Management for Patient: IBSUB,ACTIVE A I8542 XX/XX/XXXX

\*\*\* Patient has Insurance Buffer Records

<u>Insurance Co. Type of Policy Group Holder Effect. Expires</u>

1 AETNA COMPREHENSIVE M GRP NUM 13 SPOUSE 01/01/13

----------Enter ?? for more actions---------------------------------------\>\>\>

AP Add Policy EA Fast Edit All CP Change Patient

VP Policy Edit/View BU Benefits Used WP Worksheet Print

DP Delete Policy VC Verify Coverage PC Print Insurance Cov.

AB Annual Benefits RI Personal Riders EB Expand Benefits

RX RX COB Determination EX Exit

Select Item(s): Quit// VP Policy Edit/View .......................

Sample Screens

Patient Policy Information Dec 12, 2013@08:13:21 Page: 1 of 9

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

--------------------------------------------------------------------------------

Insurance Company

Company: IB INSURANCE

Street: SOME ST

Street 2:

City/State: ANYTOWN, MD XXXXX

Billing Ph: (XXX)XXX-XXXX

Precert Ph: (XXX)XXX-XXXX

Plan Information

Is Group Plan: YES

Group Name: GROUP NAME

Group Number: XXXXXX

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info IC Insur. Contact Inf. CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update AC Add Comment BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:30 Page: 2 of 9

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

BIN:

PCN:

Type of Plan: MEDICARE (M)

Plan Category: MEDICARE PART A

Electronic Type: MEDICARE A or B

Plan Filing TF: 1 YEAR (1 YEAR(S))

ePharmacy Plan ID:

ePharmacy Plan Name:

ePharmacy Natl Status:

ePharmacy Local Status:

Utilization Review Info Effective Dates & Source

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:31 Page: 3 of 9

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Require UR: NO Effective Date: 01/01/13

Require Amb Cert: NO Expiration Date:

Require Pre-Cert: NO Source of Info: INTERVIEW

Exclude Pre-Cond: NO Policy Not Billable: NO

Benefits Assignable: YES

Subscriber Information

Whose Insurance: VETERAN

Subscriber Name: IB,PATIENT

Relationship: SELF

Primary ID: XXXXXX

Coord. Benefits: PRIMARY

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comment BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:31 Page: 4 of 9

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Subscriber's Employer Information

Employment Status: Emp Sponsored Plan: No

Employer: Claims to Employer: No, Send to Insurance

Street: Retirement Date:

City/State:

Phone:

Primary Provider:

Prim Prov Phone:

Subscriber's Information (use Subscriber Update Action)

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comment BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:32 Page: 5 of 9

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Subscriber's DOB: XX/XX/XXXX

Str 1: SOME ST

Str 2:

City: SOME CITY

St/Zip: MA XXXXX

SubDiv:

Country:

Phone: XXXXXX

Subscriber's Sex: MALE

Subscriber's Branch: ARMY

Subscriber's Rank:

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:36 Page: 6 of 9

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Insurance Company ID Numbers (use Subscriber Update Action)

Subscriber ID: XXXXXX

Plan Coverage Limitations

Coverage Effective Date Covered? Limit Comments

-------- -------------- -------- --------------

INPATIENT 07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

OUTPATIENT 07/01/1998 NO

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:37 Page: 7 of 9

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

01/01/1998 NO

11/01/1996 NO

PHARMACY 08/29/2008 NO

07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

DENTAL 07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

MENTAL HEALTH 07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:38 Page: 8 of 9

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

LONG TERM CARE 07/01/1998 NO

01/01/1998 NO

PROSTHETICS 07/01/1998 NO

01/01/1998 NO

VISION 07/01/1998 NO

User Information

Entered By:

Entered On: 06/05/13

Last Verified By:

Last Verified On:

Last Updated By: IB,TESTER

Last Updated On: 09/24/13

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info IC Insur. Contact Inf. CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update AC Add Comment BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:39 Page: 9 of 9

For: IB,PATIENT XXX-XX-XXXX XX/XX/XXXX DoD: XX/XX/XXXX

IB INSURANCE \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Comment -- Group Plan

This is a long group comment. This area can hold much more than 80

Characters in the field.

Comment -- Patient Policy

<u>Dt Entered Entered By Method Person Contacted</u>

09/25/15 IBCLERK,TWO PHONE USER-A

JUST A COMMENT AND NOTHING ELSE

+09/25/15 IBCLERK,TWO PHONE USER-A

THIS IS A COMMENT THAT IS LONGER THAN 77 CHARACTERS TO TEST THE WRAP INDICATO

Personal Riders

Rider \#1: DENTAL COVERAGE

----------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Quit//

## View Patient Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Patient Insurance option is used to look at a patient's insurance information. The system groups information that is specific to the insurance company, specific to the patient, specific to the group plan, specific to the annual benefits available, and the annual benefits already used. Editing of the data is not allowed through this option.

About the Screens

In the top left corner of each screen is the screen title. On some screens, the following line is a description of the information displayed. A plus sign (+) at the bottom of the screen indicates there are additional screens. Left or right arrows (\<\<\< \>\>\>) may be displayed to indicate there is additional information to the left or right of the screen. Available actions are displayed below the screen. \<??\> entered at any Select Action prompt displays all available actions for that screen.

The user can QUIT from any screen; this will bring the user back one level or screen. EXIT is also available on most screens. When EXIT is entered, the user is prompted to Exit option entirely? A yes response returns the user to the menu. A NO response has the same result as the QUIT action. For more information on the use of the List Manager utility, please refer to [Appendix C](#appendix-c-list-manager-appendix) at the end of this manual.

The following sections display screens found under this option, with a brief action description allow.

## Patient Insurance Management Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a patient is selected, this screen is displayed listing all the patient's insurance policies. Information provided for each policy may include the type of policy, group name or individual, holder, effective date, date of death, and expiration date.

| Acronym | Description                                                    | Action                                                                                         |
|---------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| VP      | View Policy Info (accesses Patient Policy Information screen)  | Allows the user to view extensive insurance policy data.                                       |
| AB      | Annual Benefits - (accesses Annual Benefits Editor screen)     | Used to view annual benefits data for the selected policy.                                     |
| BU      | Benefits Used - (accesses Benefits Used By Date Editor screen) | Used to view policy benefits already used.                                                     |
| CP      | Change Patient                                                 | Allows the user to change to another patient without returning to the beginning of the option. |

<span id="_Toc143780849" class="anchor"></span>Table : Common Actions

## Patient Policy Information Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen is displayed listing expanded policy information for the selected company. Categories include utilization review data, subscriber data, subscriber's employer information, policy information, effective dates, plan coverage limitations, last contact, comments on the patient policy or insurance group plan, and personal riders. The only action allowed from this screen is EXIT.

## Annual Benefits Editor Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the benefit year is selected, this screen is displayed listing all the benefits for the selected insurance policy and benefit year. Benefit categories may include inpatient benefits, outpatient benefits, mental health, home health care, hospice, rehabilitation, and IV management. The only actions allowed from this screen are CY to change the benefit year and EXIT.

## Benefits Used By Date Editor Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the benefit year is selected, this screen is displayed listing all the benefits used for the selected insurance policy and benefit year. Benefit categories may include inpatient and outpatient deductibles. The only actions allowed from this screen are CY to change the benefit year and EXIT.

Sample Screens

Select PATIENT NAME: IBpatient,one XX-XX-XX XXXXXXXX YES C VETERAN

<u>Patient Insurance Management Nov 22, 1993 13:51:09 Page: 1 of 1</u>

Insurance Management for Patient: IBpatient,one XXXX XX/XX/XXXX

<u>Insurance Co. Type of Policy Group Holder Effect. Expires</u>

1 RIGHA 1546 UNKNOWN

2 XYZ INS MAJOR MEDICAL 123 SELF 04/01/93

<u>Enter ?? for more actions \>\>\></u>

VP Policy Edit/View BU Benefits Used EX Exit

AB Annual Benefits CP Change Patient

Select Item(s): Quit// VP=2 View Policy Info

Sample Output

Patient Insurance Management Jul 22, 2013@11:51:39 Page: 1 of 1

Insurance Management for Patient: IBSUB,ACTIVE A I8542 XX/XX/XXXX

\*\*\* Patient has Insurance Buffer Records

Insurance Co. Type of Policy Group Holder Effect. Expires

1 AETNA COMPREHENSIVE M GRP NUM 13 SPOUSE 01/01/13

----------Enter ?? for more actions---------------------------------------\>\>\>

AP Add Policy EA Fast Edit All CP Change Patient

VP Policy Edit/View BU Benefits Used WP Worksheet Print

DP Delete Policy VC Verify Coverage PC Print Insurance Cov.

AB Annual Benefits RI Personal Riders EB Expand Benefits

RX RX COB Determination EX Exit

Select Item(s): Quit// VP Policy Edit/View

Sample Output

Patient Policy Information Dec 12, 2013@08:13:21 Page: 1 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DOD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

--------------------------------------------------------------------------------

Insurance Company

Company: MEDICARE (WNR)

Street: PO BOX 10066

Street 2: HEALTH CARE FINANCING

City/State: ANYTOWN, MD 21207

Billing Ph: (XXX)XXX-XXXX

Precert Ph: (XXX)XXX-XXXXX

Plan Information

Is Group Plan: YES

Group Name: MEDICARE PART A

Group Number: XXXXXX00010

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:30 Page: 2 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DOD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

BIN:

PCN:

Type of Plan: MEDICARE (M)

Plan Category: MEDICARE PART A

Electronic Type: MEDICARE A or B

Plan Filing TF: 1 YEAR (1 YEAR(S))

ePharmacy Plan ID:

ePharmacy Plan Name:

ePharmacy Natl Status:

ePharmacy Local Status:

Utilization Review Info Effective Dates & Source

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:31 Page: 3 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DOD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Require UR: NO Effective Date: 01/01/13

Require Amb Cert: NO Expiration Date:

Require Pre-Cert: NO Source of Info: INTERVIEW

Exclude Pre-Cond: NO Policy Not Billable: NO

Benefits Assignable: YES

Subscriber Information

Whose Insurance: VETERAN

Subscriber Name: IBSUB,TWOTRLRS

Relationship: SELF

Primary ID: XXXXXXXXXX

Coord. Benefits: PRIMARY

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:31 Page: 4 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Subscriber's Employer Information

Employment Status: Emp Sponsored Plan: No

Employer: Claims to Employer: No, Send to Insurance

Street: Retirement Date:

City/State:

Phone:

Primary Provider:

Prim Prov Phone:

Insured Subscriber's Information (use Subscriber Update Action)

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:32 Page: 5 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DOD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Subscriber's DOB: XX/XX/XX

Str 1: PALMER HOUSE HEALTH CARE

Str 2: SHEARER ST

City: ANYTOWN

St/Zip: MA 01069

SubDiv:

Country:

Phone: XXXXXXXXXX

Subscriber's Sex: MALE

Subscriber's Branch: ARMY

Subscriber's Rank:

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:36 Page: 6 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DOD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Insurance Company ID Numbers (use Subscriber Update Action)

Subscriber ID: XXXXXXXXXX

Plan Coverage Limitations

Coverage Effective Date Covered? Limit Comments

-------- -------------- -------- --------------

INPATIENT 07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

OUTPATIENT 07/01/1998 NO

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:37 Page: 7 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DOD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

01/01/1998 NO

11/01/1996 NO

PHARMACY 08/29/2008 NO

07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

DENTAL 07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

MENTAL HEALTH 07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:38 Page: 8 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

LONG TERM CARE 07/01/1998 NO

01/01/1998 NO

PROSTHETICS 07/01/1998 NO

01/01/1998 NO

VISION 07/01/1998 NO

User Information

Entered By: IB,TESTER

Entered On: 06/05/13

Last Verified By:

Last Verified On:

Last Updated By: IB,TESTER

Last Updated On: 09/24/13

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:39 Page: 9 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DOD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Comment -- Group Plan

This is a long group comment. This area can hold much more than 80

Characters in the field.

Comment -- Patient Policy

<u>Dt Entered Entered By Method Person Contacted</u>

09/25/15 IBCLERK,TWO PHONE USER-A

JUST A COMMENT AND NOTHING ELSE

+09/25/15 IBCLERK,TWO PHONE USER-A

THIS IS A COMMENT THAT IS LONGER THAN 77 CHARACTERS TO TEST THE WRAP INDICATO

Personal Riders

Rider \#1: DENTAL COVERAGE

----------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Quit//

## Insurance Company Entry / Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Insurance Company Entry/Edit option is used to enter new insurance companies into the INSURANCE COMPANY file and edit data on existing companies. An insurance company must be in the INSURANCE COMPANY file before it can be entered into a patient's record.

When entering new insurance companies, the user will be prompted for the company street address, city, and whether the company will reimburse for treatment.

Following is a listing of the actions found on the screen in this option and a brief description of each. Once an action has been selected, \<??\> may be entered at most of the prompts that appear for lists of acceptable responses or instructions on how to respond.

## Insurance Company Editor Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the insurance company is selected, this screen is displayed listing the following groups of information for that company: billing parameters, main mailing address, inpatient claims office data, outpatient claims office data, prescription claims office data, appeals office data, inquiry office data, remarks, and synonyms.

<table>
<caption><p><span id="_Toc143780850" class="anchor"></span>Table : Common Actions</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 24%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym</th>
<th>Description</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BP</td>
<td>Billing Parameters</td>
<td>Allows the user to add / edit the billing parameters for the selected MM Main Mailing Address - Allows the user to add/edit the company's main mailing address. The address entered here will automatically be entered for the other office addresses.</td>
</tr>
<tr class="even">
<td>IC</td>
<td>Inpt Claims Office</td>
<td>Allows the user to add / edit the company's inpatient claims office name, address, phone, and fax numbers.</td>
</tr>
<tr class="odd">
<td>OC</td>
<td>Opt Claims Office</td>
<td>Allows the user to add / edit the company's outpatient claims office name, address, phone, and fax numbers.</td>
</tr>
<tr class="even">
<td>PC</td>
<td>Prescr Claims Of -</td>
<td>Allows the user to add / edit the company's prescription claims office name, address, phone, and fax numbers.</td>
</tr>
<tr class="odd">
<td>AO</td>
<td>Appeals Office</td>
<td>Allows the user to add / edit the company's appeals office name, address, phone, and fax numbers.</td>
</tr>
<tr class="even">
<td>IO</td>
<td>Inquiry Office -</td>
<td>Allows the user to add / edit the company's inquiry office name, address, phone, and fax numbers.</td>
</tr>
<tr class="odd">
<td>RE</td>
<td>Remarks -</td>
<td>Allows the user to enter comments concerning the selected insurance company.</td>
</tr>
<tr class="even">
<td>SY</td>
<td>Synonyms -</td>
<td>Allows the user to add / edit any synonyms for the selected company.</td>
</tr>
<tr class="odd">
<td>EA</td>
<td>Edit All</td>
<td>Lists editable fields line by line for quick data entry.</td>
</tr>
<tr class="even">
<td>AI</td>
<td>(In)Activate Company</td>
<td><p>Allows the user to activate / inactivate the selected insurance company. This may be used to inactivate duplicate companies in the system. When an insurance company is no longer valid, it is important to inactivate the company rather than delete it from the system. The IB INSURANCE SUPERVISOR security key is required. Once a company has been inactivated, it may not be selected when entering billing information.</p>
<p>The user may also obtain a report of patients insured by a given company through this action.</p></td>
</tr>
<tr class="odd">
<td>CC</td>
<td>Change Insurance Co.</td>
<td>Allows the user to change to another company without returning to the beginning of the option.</td>
</tr>
<tr class="even">
<td>DC</td>
<td>Delete Company</td>
<td>Allows the user to delete an entry from the Insurance Company (#36) file. If claims have been submitted to the company, another company must be selected in which to point all claims and receivables information.</td>
</tr>
<tr class="odd">
<td>PL</td>
<td>Plans (accesses Insurance Plan List screen)</td>
<td>Allows the user to display and change plan attributes associated with the insurance company.</td>
</tr>
</tbody>
</table>

<span id="_Toc143780850" class="anchor"></span>Table : Common Actions

## Insurance Plan List Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen lists all plans (active and inactive, group and individual) for the selected insurance company.

| Acronym | Description                                              | Action                                                                                                                                                               |
|---------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VP      | View/Edit Plan (accesses View/Edit Plan screen)          | Allows the user to display /change plan detailed information.                                                                                                        |
| IP      | Inactive Plan                                            | Allows the user to inactivate an insurance plan or move subscribers from multiple insurance plans into one master plan. IB GROUP PLAN EDIT security key is required. |
| AB      | Annual Benefits (accesses Annual Benefits Editor screen) | Used to enter annual benefits data for the selected policy. IB GROUP PLAN EDIT security key is required for editing.                                                 |
| NP      | New Plan                                                 | Used to add a new group plan without assigning a subscriber. IB GROUP PLAN EDIT security key is required.                                                            |

<span id="_Toc143780851" class="anchor"></span>Table : Common Actions

## Annual Benefits Editor Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the benefit year is selected, this screen is displayed listing all the benefits for the selected insurance policy and benefit year. Benefit categories may include inpatient benefits, outpatient benefits, mental health, home health care, hospice, rehabilitation, and IV management.

| Acronym | Description        | Action                                                                       |
|---------|--------------------|------------------------------------------------------------------------------|
| PI      | Policy Information | Allows entry / edit of maximum out-of-pocket and ambulance coverage.         |
| IP      | Inpatient          | Allows entry / edit of inpatient benefits data.                              |
| OP      | Outpatient         | Allows entry / edit of outpatient benefits data.                             |
| MH      | Mental Health      | Allows entry / edit of mental health inpatient and outpatient benefits data. |
| HH      | Home Health        | Allows entry / edit of home health care benefits data.                       |
| HS      | Hospice            | Allows entry / edit of hospice benefits data.                                |
| RH      | Rehab              | Allows entry / edit of rehabilitation benefits data.                         |
| IV      | IV Mgmt.           | Allows entry / edit of intravenous management benefits data.                 |
| EA      | Edit All           | Lists editable fields line by line for quick data entry.                     |
| CY      | Change Year        | Allows the user to change to another benefit year.                           |

<span id="_Toc143780852" class="anchor"></span>Table : Common Actions

## View / Edit Plan Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays plan information for viewing/editing including utilization review info, plan coverage limitations, annual benefit dates, user information, and plan comments.

| Acronym | Description                                                | Action                                                                                                                                                                                                                                   |
|---------|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PI      | Policy Information                                         | Allows entry / edit of maximum out-of-pocket and ambulance coverage. IB GROUP PLAN EDIT security key for editing.                                                                                                                        |
| UI      | UR Info                                                    | Allows entry / edit of utilization review information. IB GROUP PLAN EDIT security key is required for editing.                                                                                                                          |
| CV      | Add/Edit Coverage                                          | Allows the user to add, edit, or delete (unwanted) coverage limitations for a specific plan. IB GROUP PLAN EDIT security key is required for editing.                                                                                    |
| PC      | Plan Comments                                              | Allows editing of comments for the plan. IB GROUP PLAN EDIT security key is required for editing.                                                                                                                                        |
| IP      | (In)Activate Plan                                          | Allows the user to inactivate an insurance plan or move subscribers from multiple insurance plans into one master plan. IB GROUP PLAN EDIT security key is required.                                                                     |
| AB      | Annual Benefits - (accesses Annual Benefits Editor screen) | Used to enter annual benefits data for the selected policy. IB GROUP PLAN EDIT security key is required for editing.                                                                                                                     |
| CP      | Change Plan                                                | Allows the user to select another plan for this insurance company without having to exit back to the previous screen. Although this option is not locked, the MCCR System Definition Menu is locked with the IB SUPERVISOR security key. |

<span id="_Toc143780853" class="anchor"></span>Table : Common Actions

Sample Screens

Insurance Company Editor Nov 26, 2014@12:19:25 Page: 1 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

------------------------------------------------------------------------------

Billing Parameters

Signature Required?: YES Type Of Coverage: HEALTH INSURAN

Reimburse?: WILL NOT REIMBURSE Billing Phone:

Mult. Bedsections: YES Verification Phone:

One Opt. Visit: NO Precert Comp. Name:

Diff. Rev. Codes: Precert Phone:

Amb. Sur. Rev. Code:

Rx Refill Rev. Code:

Filing Time Frame: (1 YEAR(S))

EDI Parameters

Transmit?: YES-LIVE Insurance Type: GROUP POLICY

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:24:58 Page: 2 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+----------------------------------------------------------------------------

Inst Payer Primary ID: Prof Payer Primary ID:

Inst Payer Sec ID Qual: Prof Payer Sec ID Qual:

Inst Payer Sec ID: Prof Payer Sec ID:

Inst Payer Sec ID Qual: Prof Payer Sec ID Qual:

Inst Payer Sec ID: Prof Payer Sec ID:

Bin Number: Prnt Sec/Tert Auto Claims:

HPID/OEID: Prnt Med Sec Claims w/o MRA: YES

Main Mailing Address

Street: PO BOX City/State:

Street 2: Phone:

Street 3: Fax:

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:26:11 Page: 3 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Inpatient Claims Office Information

Company Name: INSURANCE COMPANY Street 3:

Street: City/State:

Street 2: Phone:

Fax:

Outpatient Claims Office Information

Company Name: INSURANCE COMPANY Street 3:

Street: City/State:

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:26:53 Page: 4 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Street 2: Phone:

Fax:

Prescription Claims Office Information

Company Name: INSURANCE COMPANY Street 3:

Street: City/State:

Street 2: Phone:

Fax:

Appeals Office Information

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:27:16 Page: 5 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Company Name: INSURANCE COMPANY Street 3:

Street: City/State:

Street 2: Phone:

Fax:

Inquiry Office Information

Company Name: INSURANCE COMPANY Street 3:

Street: City/State:

Street 2: Phone:

Fax:

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:27:39 Page: 6 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Associated Insurance Companies

This insurance company is not defined as either a Parent or a Child.

Provider IDs

Billing Provider Secondary ID

Additional Billing Provider Secondary IDs

VA-Laboratory or Facility Secondary IDs

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:27:51 Page: 7 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

ID Parameters

Attending/Rendering Provider Secondary ID Qualifier (1500):

Attending/Rendering Provider Secondary ID Qualifier (UB-04):

Attending/Rendering Secondary ID Requirement: NONE REQUIRED

Referring Provider Secondary ID Qualifier (1500): UPIN

Referring Provider Secondary ID Requirement: NONE

Use Att/Rend ID as Billing Provider Sec. ID (1500): NO

Use Att/Rend ID as Billing Provider Sec. ID (UB-04): NO

Always use main VAMC as Billing Provider (1500)?: NO

Always use main VAMC as Billing Provider (UB-04)?: NO

Transmit no Billing Provider Sec. ID for the Electronic Plan Types:

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:28:12 Page: 8 of 9

Insurance Company Information for: INSURNACE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Payer: PAYER A

VA National ID: VA1 CMS National ID:

Deactivated: YES Date Deactivated: 11/04/2014

Payer Application: eIV

Nationally Enabled: YES FSC Auto-Update: YES

Locally Enabled: YES

Payer Application: IIU

Nationally Enabled: YES Receive IIU Data: YES

Locally Enabled: YES

Remarks

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:28:30 Page: 9 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+----------------------------------------------------------------------------

6/05 Will not pay for Omeprazole/Prilosec..jc

1/1/04 All XXXXX are combined to this one this year and an all inclusive

\# is xxx-xxx-xxxx..ID# are changing over to W + 9 digits now too..jc

This insurance carrier entry and phone number is inclusive for the

'Bxxxxx Company'. mdm

Synonyms

XXX

----------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Quit//

## View Insurance Company

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Insurance Company option is used to look at data related to a selected insurance company. Editing of the data is not allowed through this option.

About the Screen

In the top left corner of each screen is the screen title. The following line is a description of the information displayed. A plus sign (+) at the bottom of the screen indicates there are additional screens. Left or right arrows (\<\<\< \>\>\>) may be displayed to indicate there is additional information to the left or right of the screen. Available actions are displayed below the screen. \<??\> entered at any Select Action prompt displays all available actions for that screen.

The user can QUIT from any screen; this will bring the user back one level or screen. EXIT is also available on most screens. When EXIT is entered, the user is prompted to Exit option entirely? A yes response returns the user to the menu. A NO response has the same result as the QUIT action. For more information on the use of the List Manager utility, please refer to [Appendix C](#appendix-c-list-manager-appendix) at the end of this manual.

## Insurance Company Editor Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the insurance company is selected, this screen is displayed listing the following groups of information for that company: billing parameters, main mailing address, inpatient claims office data, outpatient claims office data, prescription claims office data, appeals office data, inquiry office data, remarks, and synonyms.

The two actions available through this option are CC Change Insurance Co. which allows the user to change to another company without returning to the beginning of the option and EXIT.

Sample Screens

Insurance Company Editor May 29, 2014@13:46:36 Page: 1 of 8

Insurance Company Information for: BIG LOSS INSURANCE

Type of Company: HEALTH INSURANCE Currently Active

----------------------------------------------------------------------------

Billing Parameters

Signature Required?: NO Type Of Coverage: HEALTH INSURAN

Reimburse?: WILL REIMBURSE Billing Phone:

Mult. Bedsections: YES Verification Phone:

One Opt. Visit: NO Precert Comp. Name:

Diff. Rev. Codes: Precert Phone:

Amb. Sur. Rev. Code:

Rx Refill Rev. Code:

Filing Time Frame: (NO FILING TIME FRAME LIMIT)

EDI Parameters

Transmit?: YES-LIVE Insurance Type: GROUP POLICY

Inst Payer Primary ID: Prof Payer Primary ID:

+---------Enter ?? for more actions------------------------------------------\>\>\>

CC Change Insurance Co. EX Exit

Select Action: Next Screen// NEXT SCREEN

Insurance Company Editor May 29, 2014@13:46:50 Page: 2 of 8

Insurance Company Information for: BIG LOSS INSURANCE

Type of Company: HEALTH INSURANCE Currently Active

+--------------------------------------------------------------------------

Inst Payer Sec ID Qual: Prof Payer Sec ID Qual:

Inst Payer Sec ID: Prof Payer Sec ID:

Inst Payer Sec ID Qual: Prof Payer Sec ID Qual:

Inst Payer Sec ID: Prof Payer Sec ID:

Bin Number: Prnt Sec/Tert Auto Claims:

HPID/OEID: Prnt Med Sec Claims w/o MRA:

Main Mailing Address

Street: 123 STREET City/State: ANYTOWN, WY 5180

Street 2: Phone:

Street 3: Fax:

+---------Enter ?? for more actions----------------------------------------\>\>\>

CC Change Insurance Co. EX Exit

Select Action: Next Screen// NEXT SCREEN

Insurance Company Editor May 29, 2014@13:47:39 Page: 3 of 8

Insurance Company Information for: BIG LOSS INSURANCE

Type of Company: HEALTH INSURANCE Currently Active

+---------------------------------------------------------------------------

Inpatient Claims Office Information

Company Name: BIG LOSS INSURANCE Street 3:

Street: 123 STREET City/State: ANYTOWN, WY 5180

Street 2: Phone:

Fax:

Outpatient Claims Office Information

Company Name: BIG LOSS INSURANCE Street 3:

Street: 123 STREET City/State: ANYTOWN, WY 5180

Street 2: Phone:

Fax:

+---------Enter ?? for more actions------------------------------------------\>\>\>

CC Change Insurance Co. EX Exit

Select Action: Next Screen// NEXT SCREEN

Insurance Company Editor May 29, 2014@13:47:42 Page: 4 of 8

Insurance Company Information for: BIG LOSS INSURANCE

Type of Company: HEALTH INSURANCE Currently Active

+--------------------------------------------------------------------------

Prescription Claims Office Information

Company Name: BIG LOSS INSURANCE Street 3:

Street: 123 STREET City/State: ANYTOWN, WY 5180

Street 2: Phone:

Fax:

Appeals Office Information

Company Name: BIG LOSS INSURANCE Street 3:

Street: 123 STREET City/State: ANYTOWN, WY 5180

Street 2: Phone:

Fax:

+---------Enter ?? for more actions------------------------------------------\>\>\>

CC Change Insurance Co. EX Exit

Select Action: Next Screen// NEXT SCREEN

Insurance Company Editor May 29, 2014@13:47:43 Page: 5 of 8

Insurance Company Information for: BIG LOSS INSURANCE

Type of Company: HEALTH INSURANCE Currently Active

+--------------------------------------------------------------------------

Inquiry Office Information

Company Name: BIG LOSS INSURANCE Street 3:

Street: 123 STREET City/State: ANYTOWN, WY 5180

Street 2: Phone:

Fax:

Associated Insurance Companies

This insurance company is not defined as either a Parent or a Child.

+---------Enter ?? for more actions------------------------------------------\>\>\>

CC Change Insurance Co. EX Exit

Select Action: Next Screen// NEXT SCREEN

Insurance Company Editor May 29, 2014@13:47:45 Page: 6 of 8

Insurance Company Information for: BIG LOSS INSURANCE

Type of Company: HEALTH INSURANCE Currently Active

+--------------------------------------------------------------------------

Provider IDs

Billing Provider Secondary ID

Additional Billing Provider Secondary IDs

VA-Laboratory or Facility Secondary IDs

ID Parameters

Attending/Rendering Provider Secondary ID Qualifier (1500):

Attending/Rendering Provider Secondary ID Qualifier (UB-04):

Attending/Rendering Secondary ID Requirement: NONE REQUIRED

Referring Provider Secondary ID Qualifier (1500): UPIN

+---------Enter ?? for more actions------------------------------------------\>\>\>

CC Change Insurance Co. EX Exit

Select Action: Next Screen// NEXT SCREEN

Insurance Company Editor May 29, 2014@13:47:46 Page: 7 of 8

Insurance Company Information for: BIG LOSS INSURANCE

Type of Company: HEALTH INSURANCE Currently Active

+--------------------------------------------------------------------------

Referring Provider Secondary ID Requirement: NONE

Use Att/Rend ID as Billing Provider Sec. ID (1500): NO

Use Att/Rend ID as Billing Provider Sec. ID (UB-04): NO

Always use main VAMC as Billing Provider (1500)?: NO

Always use main VAMC as Billing Provider (UB-04)?: NO

Transmit no Billing Provider Sec. ID for the Electronic Plan Types:

Payer: PAYER1

VA National ID: VA10 CMS National ID:

Deactivated: NO

Payer Application: eIV

Nationally Enabled: YES FSC Auto-Update: YES

Locally Enabled: YES

Payer Application: IIU

Nationally Enabled: YES Receive IIU Data: NO

Locally Enabled: YES

+---------Enter ?? for more actions------------------------------------------\>\>\>

CC Change Insurance Co. EX Exit

Select Action: Next Screen// NEXT SCREEN

Insurance Company Editor May 29, 2014@13:47:47 Page: 8 of 8

Insurance Company Information for: BIG LOSS INSURANCE

Type of Company: HEALTH INSURANCE Currently Active

+--------------------------------------------------------------------------

Remarks

Synonyms

----------Enter ?? for more actions------------------------------------------\>\>\>

CC Change Insurance Co. EX Exit

Select Action: Quit//

## Process Insurance Buffer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB INSURANCE SUPERVISOR security key is required to use the Reject Entry and Accept Entry actions. Adding new insurance companies requires the IB INSURANCE COMPANY ADD security key.

This option is used to process and manage the Insurance Buffer through the use of the following screens and actions.

## Insurance Buffer List Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen contains the list of all Insurance Buffer file entries that have not yet been processed by authorized insurance personnel.

| Action               | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process Entry Action | Opens the Insurance Buffer Process screen for a selected buffer entry. The buffer entry can then be compared against existing insurance records, viewed, edited, rejected, or accepted.                                                                                                                                                                                                                                            |
| Reject Entry Action  | Allows the user to reject a selected buffer entry without any changes to the existing permanent insurance records. This also results in the buffer entries insurance and patient data being deleted, leaving a stub record in the Buffer file for tracking and reporting purposes. The permanent Insurance files are not modified by this action. If the patient has no active insurance, then any bills on hold will be released. |
| Expand Entry Action  | Opens the Insurance Buffer Entry screen for a selected buffer entry. This screen displays the complete buffer entry and allows the data to be edited.                                                                                                                                                                                                                                                                              |
| Add Action           | Allows the user to create then edit a new Insurance Buffer entry.                                                                                                                                                                                                                                                                                                                                                                  |
| Sort List            | Re-sorts the list of unprocessed buffer entries on the Insurance Buffer List screen by a selected data element.                                                                                                                                                                                                                                                                                                                    |

<span id="_Toc143780854" class="anchor"></span>Table : Common Actions

## Insurance Buffer Process Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen contains the information and actions needed to process a buffer entry. The screen display includes data to assist in matching the buffer entry with any existing insurance records. There are two versions of this screen:

1.  Patient (list is broken into 2 sections).
2.  Insurance Company.

| Action                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accept Entry Action         | Allows the user to accept the buffer data and transfer the insurance information from the buffer entry into the permanent insurance records. New insurance records can be created, or existing Insurance records can be updated with the buffer data. The new / updated Insurance record is flagged as verified. The insurance and patient data are deleted from the buffer entry leaving only a stub record for tracking and reporting purposes. If a new policy is added for the patient, the on-hold date of any patient bills is updated to the current date. |
| Reject Entry Action         | Allows the user to reject the buffer entry without any changes to the existing permanent insurance records. This also results in the buffer entries insurance and patient data being deleted, leaving a stub record in the Buffer file for tracking and reporting purposes. The permanent insurance files are not modified by this action. If the patient has no active insurance, any bills on hold are released.                                                                                                                                                |
| Compare Entry Action        | Displays the buffer entry and a user-selected Insurance Policy side by side to compare and determine if a match exists. It is also possible to edit the buffer entry data within this action. The display and editing are broken into three parts: Insurance Company data, Group / Plan data, and Patient Policy data.                                                                                                                                                                                                                                            |
| Expand Entry Action         | Opens the Insurance Buffer Entry screen for the buffer entry. It displays the complete buffer entry and allows the data to be edited.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Insurance Co/Patient Action | Toggles between the two versions of the Insurance Buffer Process screen: Patient or Insurance Company. If an Insurance Company is selected the Insurance Company version of the screen is displayed, if no company is selected the Patient version of the screen is displayed.                                                                                                                                                                                                                                                                                    |

<span id="_Toc143780855" class="anchor"></span>Table : Report Descriptions

## Insurance Buffer Entry Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays all data defined for a buffer entry and allows that data to be edited.

| Action                     | Description                                                                                                                                                                                            |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Insurance Co Edit Action   | Edits the Insurance Company specific data in the buffer entry.                                                                                                                                         |
| Group/Plan Edit Action     | Edits the Insurance Group / Plan specific data in the buffer entry.                                                                                                                                    |
| Patient Policy Edit Action | Edits the Patient Policy specific data in the buffer entry.                                                                                                                                            |
| All Edit Action            | Edits all three types of data in the buffer entry: Insurance Company, Group / Plan, and Patient Policy.                                                                                                |
| Verify Entry Action        | Option to flag the buffer entry as verified before it is accepted. If the buffer entry is later accepted, the person that uses this action is added as the verifier in the permanent insurance policy. |

<span id="_Toc143780856" class="anchor"></span>Table : Parameter Descriptions

Sample Screens

Insurance Buffer List Nov 05, 1998 09:44:09 Page: 1 of 1

Buffer File entries not yet processed. (sorted by Patient Name)

Patient Name Insurance Company Subscr Id S Entered iIECH

1 IBpatient,one XXXX GEHA XXX I 10/09/98 I

2 \*IBpatient,two XXXX HARTFORD XXXXXXXX I 09/15/98 i C

3 IBpatient,three XXXX BLUE CROSS/BLUE S XXXXX I 09/29/98 i

4 IBpatient,four XXXX GHI P 09/30/98 i

5 IBpatient,five XXXX HARTFORD I 09/30/98 i

Enter ?? for more actions

Process Entry EE Expand Entry Sort List

Reject Entry Add Entry X Exit

Select Action: Quit//

Insurance Buffer Process Nov 05, 1998 11:01:21 Page: 1 of 1

IBpatient,one XXX-XX-XXXX DOB: JUN 2,1926 AGE: 72

HARTFORD (2222 SOUTH STREET, ANYTOWN, CA)

-HARTFORD 000-CHAMPUS 00606666 PATIEN

Patient's Existing Insurance

Insurance Company Group \# Subscriber Id Holder Effective Expires

1 HARTFORD 000 XXXXXXXX SPOUSE 01/01/97

2 BC/BS OF ALBANY 415 XXXXXXXX PATIEN

Any Group/Plan that may match Group Name or Group Number

Insurance Company Group Name Group Number

3 HARTFORD 2222 South St CHAMPUS PRIM 000

Enter ?? for more actions

Accept Entry Compare Entry Insurance Co/Patient

Reject Entry EE Expand Entry X Exit

Select Action: Quit//

## Manually Added HPIDs to Billing Claim Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report generates a list of Health Plan Identifier (HPID) numbers that have been added directly to claims. It allows billing staff to track the instances when an HPID number is added to a third-party claim and to generate an ad-hoc report of authorized claims with this entry information. Only HPIDs that have been manually added will appear on this report.

The user will be prompted for the date range, report format, and device. The date range pertains to when the HPID was manually added to the claim.

This output displays the patient name, last 4 of SSN, payer, HPID, claim number, username, date HPID added, Professional ID, and Institutional ID.

Sample Output

MANUALLY ADDED HPIDS TO BILLING CLAIM REPORT AUG 02, 2015@19:59 Page: 1

PT NAME SSN PAYER HPID CLAIM \# USER NAME DATE HPID ADDED PROF ID INST ID

------------------------------------------------------------------------------------------------------------------------------------

IBPATIENT,ONE 1111 BLUE CROSS 7414615XXX XXX-XXXXXXX IBUSER,ONE 12/02/2014 1234567XXX 0987654XXX

IBPATIENT,ONE 1111 BLUE CROSS 7399982XXX XXX-XXXXXXX IBUSER,ONE 01/15/2015 1234567XXX 0987654XXX

IBPATIENT,ONE 1111 BLUE CROSS 7947434XXX XXX-XXXXXXX IBUSER,ONE 01/22/2015 1234567XXX 0987654XXX

IBPATIENT,ONE 1111 BLUE CROSS 7947434XXX XXX-XXXXXXX IBUSER,ONE 01/22/2015 1234567XXX 0987654XXX

IBPATIENT,ONE 1111 BLUE CROSS 7467061XXX XXX-XXXXXXX IBUSER,ONE 01/23/2015 1234567XXX 0987654XXX

IBPATIENT,ONE 1111 BLUE CROSS 7947434XXX XXX-XXXXXXX IBUSER,ONE 02/05/2015 1234567XXX 0987654XXX

IBPATIENT,TWO 9341 BLUE CROSS 7462706XXX XXX-XXXXXXX IBUSER,ONE 02/09/2015 1234567XXX 0987654XXX

IBPATIENT,TWO 9341 BLUE CROSS 7444643XXX XXX-XXXXXXX IBUSER,ONE 02/09/2015 1234567XXX 0987654XXX

IBPATIENT,TWO 9341 BLUE CROSS 7908996XXX XXX-XXXXXXX IBUSER,ONE 02/09/2015 1234567XXX 0987654XXX

## Expire Group Plan (XPIR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Patient Insurance Menu (PI) option is used to specify an expiration date for all subscribers in a plan, effectively terminating the plan, without having to move the subscribers to a different plan. This option offers the user the option to inactivate the plan as part of the expiration or to allow the plan to remain active.

Sample Screens/Prompts

EXPIRE ALL SUBSCRIBERS WITHIN A GROUP PLAN

You can use this option to specify an expiration date for all subscriber policies in a group plan without moving the subscribers to another group plan. If the group plan status is currently “active,” you can also choose to “inactivate” the group plan.

Select INSURANCE COMPANY:

You may select an existing Plan from a list or enter a specific Plan.

Do you wish to enter a specific plan? NO

- If the user response is NO, the Group Plan Lookup screen displays:

Figure : Group Plan Lookup – User Response of NO

![](ib-2-integrated-billing-version-2-user-manual/002.png)

- If the user response is YES, the following prompts display:

Figure : Group Plan Lookup – User Response of YES

![](ib-2-integrated-billing-version-2-user-manual/003.png)

- When the user selects a Group Plan, the following prompts display:

Collecting Subscribers . . .

This group plan has \## subscribers. All subscribers will be expired.

Do you want to expire all subscribers’ policies for this plan? //YES

Enter expiration date (applies to all subscribers in this plan):

You selected to expire \## subscriber(s) with Expiration Date \<MMM dd, yyyy\> for:

Insurance Company \<INSURANCE COMPANY NAME\>

Plan Name \<GROUP NAME\> Number \<GRP NUM XXXXX\>

Please note that the policy will be EXPIRED in the patient profile!!

Okay to continue? //YES

Expiring Policies . . .

Done. XX Subscribers’ policies were expired as of \<MMM dd, yyyy\>.

A Bulletin was sent to you and members of ‘IB NEW INSURANCE’ Mail Group.

= = = = = = = = = = = = = = = = = = = = = =

EXPIRE ALL SUBSCRIBERS WITHIN A GROUP PLAN

= = = = = = = = = = = = = = = = = = = = = =

- One of the following messages may display if there are subscribers (policies) that were not/could not be expired:

These \# entries could not be processed, they’ll need to be adjusted manually.

Patient Name/ID Whose Employer Effective Expires

\<patient name XXXX\> \<relation\> \<employer\> \<date\> \<date\>

Examine the entries that could not be processed.

Press RETURN to continue.

-or-

After processing, no changes were needed, no policies were expired.

Press RETURN to continue.

= = = = = = = = = = = = = = = = = = = = = =

EXPIRE ALL SUBSCRIBERS WITHIN A GROUP PLAN

= = = = = = = = = = = = = = = = = = = = = =

- If the group plan is active, the inactivate plan prompt, shown below, displays. The following warning displays with the inactivate plan prompt if there are subscribers (policies) that were not/could not be expired:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Warning

There are still active subscribers

that will need to be adjusted manually.

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Do you wish to inactivate plan \<GROUP NAME\>? //N

- If user response is YES, the following displays:

The \<GROUP NAME\> plan has been inactivated.

- If user response is NO, the following displays:

The \<GROUP NAME\> plan is still active.

- If the group plan is inactive, the following prompt displays:

Please note the \<GROUP NAME\> plan is already inactive.

= = = = = = = = = = = = = = = = = = = = = =

EXPIRE ALL SUBSCRIBERS WITHIN A GROUP PLAN

= = = = = = = = = = = = = = = = = = = = = =

## Release of Information Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA Mission Act of 2018 modified the requirement for a signed Release of Information (ROI) when billing sensitive diagnoses. A signed ROI is not required for any bill for a sensitive diagnosis and a date of service on or after January 28, 2019. A date of service prior to January 28, 2019, will still require a signed ROI for a sensitive diagnosis.

This report provides a list of ROI for sensitive diagnosis medication and the associated expiration dates. The ROI report is designed to sort by expiration date, in reverse chronological order.

This report is formatted to print at 132 columns.

Sample Output

BEGINNING EXPIRATION DATE: T-180// (MAY 07, 2015)

ENDING EXPIRATION DATE: T+60// (JAN 02, 2016)

Select one of the following:

A ACTIVE

I INACTIVE

B BOTH

Display (A)ctive or (I)active or (B)oth ROI Status:: Both// BOTH

Export the report to Microsoft Excel (Y/N)? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// 0;132 VIRTUAL TELNET

Please wait...

Release of Information Expiration Report Page: 1

Date Range: 05/07/2015 - 01/02/2016 Run Date: Nov 03, 2015@12:38:35

---------------------------------------------------------------------------------------------------------------------------------

Date of Eff. Exp. Date

Patient Name Death Date Date St Added Entered By Insurance Name Drug Name

---------------------------------------------------------------------------------------------------------------------------------

PATIENT,ONE 12/16/15 01/02/16 A 12/30/15 USER,ONE ABC INSURANCE DRUG ONE

PATIENT,TWO 01/01/15 12/31/15 A 05/24/13 USER,FOUR ABC INSURANCE DRUG TWO

PATIENT,TWO 01/01/15 12/31/15 A 02/13/13 USER,ONE ABC INSURANCE DRUG ONE

PATIENT,THREE 01/01/15 12/31/15 A 05/28/15 USER,TWO XYZ INSURANCE DRUG THREE

\*\*\* END OF REPORT \*\*\*

## Insurance Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Insurance Reports menu provides the options to run the following reports:

| Report | Description                                   |
|--------|-----------------------------------------------|
| ABUF   | Insurance Buffer Activity                     |
| AR     | eIV Ambiguous Policy Report                   |
| AU     | User Edit Report                              |
| CV     | Coverage Limitations Report                   |
| EBUF   | Insurance Buffer Employee                     |
| ID     | Generate Insurance Company Listings           |
| IFIU   | Interfacility Ins. Update Report              |
| IN     | Patients with Unidentified Insurance          |
| IP     | eIV Inactive Policy Report                    |
| IR     | Ins Company Link Report                       |
| IU     | eIV Patient Insurance Update Report           |
| LC     | List Inactive Ins. Co. Covering Patients      |
| LP     | List Plans by Insurance Company               |
| LR     | Payer Link Report                             |
| MD     | Insurance Plans Missing Data Report           |
| NC     | Verification of No Coverage Report            |
| NE     | Active Policies with no Effective Date Report |
| NV     | List New not Verified Policies                |
| PDOD   | eIV Payer Date of Death Report                |
| PR     | eIV Payer Report                              |
| PT     | Insurance Payment Trend Report                |
| RR     | eIV Response Report                           |
| SOUR   | Source of Information Report                  |
| SR     | eIV Statistical Report                        |
| UNKI   | Inpatients w/Unknown or Expired Insurance     |
| UNKO   | Outpatients w/Unknown or Expired Insurance    |
| WNR    | Patients Without MEDICARE (WNR) Insurance     |
| WO     | Patients with or without Insurance Report     |

<span id="_Toc143780857" class="anchor"></span>Table : Screen Descriptions

### List Plans by Insurance Company

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides insurance information from both a plan and subscriber perspective. It is designed to generate lists of plans by the insurance company and lists of subscribers (policies) by insurance plan. It can be used to generate plan and subscriber lists to be used for the database clean-up efforts. Once the database integrity has been restored, the report can be used to generate a list of subscribers to plans or companies.

This report is formatted to print at 132 columns.

Sample ScreenInsurance Plan Lookup Sep 19, 1995 13:29:50 Page: 1 of 1

All Plans for: ABC INS Phone: XXX-XXX-XXXX

123 MAIN Ave. Precerts: XXX-XXX-XXXX

ANYTOWN, CA 00098

\# + =\> Indiv. Plan \* =\> Inactive Plan Pre- Pre- Ben

Group Name Group Number Type of Plan UR? Ct? ExC? As?

1 AE 93932 MEDICAL EXPEN NO YES YES YES

2 NYS 12343221 MEDI-CAL YES YES YES YES

3 KROGER 112222 MAJOR MEDICAL NO YES NO YES

4 RETIRED 4321 MAJOR MEDICAL YES YES NO YES

Enter ?? for more actions

SP Select Plan

Select Action: Quit// sp=1 4 Select Plan

Would you like to select any other plans? NO// \<RET\>Sample Output

LIST OF PLANS BY INSURANCE COMPANY MAR 12, 2015@13:19 Page: 1

---------------------------------------------------------------------------------------------------

\+ =\>INDIV. PLAN \* =\> INACTIVE

Filters: Active Insurance, Active Group Plans

INSURANCE COMPANY TWO

PO BOX XXXXXX FTF= 1(YRS) GROUP PLAN TOTAL= 4

ANYTOWN, MO SUBSCRIBER TOTAL= 1000

64106-7711

GROUP NUMBER GROUP NAME TYPE OF PLAN ELEC PLAN FTF

PART A PART A MEDICARE MEDICARE 1(YRS)

SUBSCRIBERS = 250

PART B PART B MEDICARE MEDICARE 1(YRS)

SUBSCRIBERS = 20

+PART A RR PART A RR MEDICARE MEDICARE 1(YRS)

SUBSCRIBERS = 1

PART B RR PART B RR MEDICARE MEDICARE 1(YRS)

SUBSCRIBERS = 250

\*INSURANCE COMPANY THREE

PO BOX XXXXXX FTF= 1(YRS)

ANYTOWN, MO GROUP PLAN TOTAL= 5

66666-5555 SUBSCRIBER TOTAL= 1000

GROUP NUMBER GROUP NAME TYPE OF PLAN ELEC PLAN FTF

PART A PART A MEDICARE MEDICARE 1(YRS)

SUBSCRIBERS = 250

\*PART B PART B MEDICARE MEDICARE 1(YRS)

SUBSCRIBERS = 20

PART A RR PART A RR MEDICARE MEDICARE 1(YRS)

SUBSCRIBERS = 5

PART B RR PART B RR MEDICARE MEDICARE 1(YRS)

SUBSCRIBERS = 250

\*\*\*\*\*End of Report\*\*\*\*

### List New not Verified Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List New Not Verified Policies option is used to produce a list by the patient of new insurance entries that have not been verified. After running this report, use the Verify Coverage action of the Patient Insurance Info View/Edit option to verify coverage for individual patients.

Specify a date range and patient name range to limit the parameters of the report.

Information provided on the output includes patient name and ID#, insurance company name, subscriber ID, the person who made the entry, and date entered. A total count is also provided.

REPORT OF NEW, NOT VERIFIED INSURANCE ENTRIES FROM: 8/01/93 TO: 12/01/93 DEC 16,1993 15:05 PAGE 1

PATIENT PATIENT ID INSURANCE CO SUBSCRIBER ID WHO ENTERED DATE ENTERED

---------------------------------------------------------------------------------------------------------

IBpatient,one XXXXXXXX XYZ INS XXXXXXX NANCY AUG 17,1993

IBpatient,two XXXXXXXX BLUE CROSS BLUE SHIELD XXXXXX BETH SEP 17,1993

IBpatient,three XXXXXXXX XYZ INS XXXX ELLEN OCT 12,1993

COUNT 3

### Insurance Plans Missing Data Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Insurance Plans Missing Data option creates a list of insurance plans missing specified information.

This report can display plans that are missing group number, type of plan, timely filing time frame, electronic plan type, coverage limitations, BIN, and PCN.

Sample Screen

1\. List All 1365 Active Ins. Companies

2\. List Only Active Ins. Companies That You Select

SELECT 1 or 2:

Display Active Group(s) missing Group Number? YES// YES

Display Active Group(s) missing Type of Plan? YES//YES

Display Active Group(s) missing Timely Filing Time Frame? YES//YES

Display Active Group(s) missing Electronic Plan Type? YES//YES

Display Active Group(s) missing Coverage Limitations? YES//YES

Display Active Group(s) missing BIN? YES//YES

Display Active Group(s) missing PCN? YES//YES

DEVICE: HOME//

Sample Output

INSURANCE PLANS MISSING DATA MAR 12, 2015@13:19 Page: 1 of 1

Missing Data: Group \#, Plan Type, FTF, Elec Plan, BIN, PCN, Coverage Limitation

MEDICARE (WNR) PO BOX xxxxx ANYTOWN, MO 64444-1111

GROUP \# GROUP NAME TYPE OF PLAN ELEC PLAN FTF

-------- ---------- ----------- --------- ---

XXXXXXXX PART B MEDICARE MEDICARE 1(YRS)

PART B PART B MEDICARE MEDICARE XXXXXXX

PART A RR XXXXXXXX MEDICARE MEDICARE XXXXXXX

PART B RR PART B XXXXXX MEDICARE XXXXXXX

PART G PART G MEDICARE XXXXXXXXX 1(YRS)

PART A RR XXXXXXXX MEDICARE MEDICARE XXXXXXX

Coverage Effective Date Covered?

-------- -------------- --------

INPATIENT XXXXXXXX BY DEFAULT

PART G PART G MEDICARE XXXXXXXXX 1(YRS)

PART A RR XXXXXXX MEDICARE MEDICARE XXXXXXX

CAREMARK PO BOX 13999 ANYTOWN, MO 64106-7711 PRESCRIPTION ONLY

GROUP \# GROUP NAME TYPE OF PLAN ELEC PLAN FTF BIN PCN

-------- ---------- ----------- --------- --- --- ---

XXXXXXXX PART B PRESCRIPTION PRESCRIPTION 1(YRS) XXX XXXXXX

XXXXXXXX PART B PRESCRIPTION PRESCRIPTION 1(YRS) 123654 XXXX

PART B PART B PRESCRIPTION PRESCRIPTION 1(YRS) XXX XXXX

\*\*\*\*\*End of Report\*\*\*\*

### eIV Payer Date of Death Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The eIV Payer Date of Death Report (PDOD) option creates a report so that the Insurance Verifier can forward information to the VA registration offices including a Patient’s date of death. VistA Registration file may or may not have the date of death for the patient Information from the report can be used by VAMC Registration offices. The report can be found on the Insurance Reports Menu Option Path: Patient Insurance Menu (PI) \> Insurance Reports (INSR). The shortcut is PDOD.

This report is formatted to print at 132 columns.

Sample Screen

eIV Payer Date of Death Report

Electronic Insurance Verification responses are received daily.

Please select a Date range in which Date of Death eIV responses were received

to determine the appropriate patient Date of Death information.

eIV RESPONSE RECEIVED DATE:

Earliest Date Received: T (JUN 03, 2020)

Latest Date Received: Today// T (JUN 03, 2020)

PAYER SELECTION:

Run for (A)ll Payers or (S)elected Payers: A// ll

DECEASED OR NOT DECEASED IN VISTA:

Select one of the following:

1 Patient is not deceased in VistA

2 Patient is deceased in VistA

3 Both

Select the type of patient to display: 3// Both

Select one of the following:

1 Patient Name

2 Payer Name

Select the primary sort field: 1// Patient Name

(E)xcel Format or (R)eport Format: Report//

Sample Output

eIV Payer Date of Death Report Mar 23, 2020@07:02:16 Page: 1

Date Range: 01/01/2015-03/23/2020 All Payers, Patients Deceased and Not Deceased in VistA

Patient Name Last 4 SSN DOB VISTA DOD VISTA Payer Name Trace \# DOD Payer

-------------------------------------------------------------------------------------------------

IBPATIENT,ONE XXXX 02/02/1922 AETNA 12345678 02/02/2020

IBPATIENT,TWO XXXX 02/02/1922 CIGNA 12345678 02/02/2020

IBPATIENT,THREE XXXX 01/01/1948 06/18/2019 AETNA 12345678 01/13/2020

IBPATIENT,FOUR XXXX 05/05/1955 07/26/1992 CMS 12345678 01/03/2020

\*\*\* END OF REPORT \*\*\*

### Source of Information Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Source of Information Report (SOUR) option creates a report to help the user calculate an accurate Return on Investment based on the source of information assigned to the patient policy. It includes only those specific policies associated with the parameters selected by the user during the report generation prompts.

Sample Screen

This report will print bills and payments within the user-selected

date range that are associated to an insurance policy with a source

of information equal to the user-selected criteria.

Select one of the following:

B Billed Date

C Collected Date

Report by (B)ill Date or by (C)ollected Date?: // b Billed Date

Starting Billed Date: Mar 01, 2020// 1/1/15 (JAN 01, 2015)

Ending Billed Date: Mar 23, 2020// 1/15/15 (JAN 15, 2015)

\*\*\* Selected Billed Date range from Jan 01, 2015 to Jan 15, 2015 \*\*\*

Enter Sources of Information to include one at a time.

Include Source of Information (\<RETURN\> for ALL):

Select one of the following:

D Detailed

S Summary

Print (D)etailed or (S)ummary report?: Summary// d Detailed

Select one of the following:P PatientI InsuranceB Billed AmountC Collected AmountD DateS Source of InformationSort the report by: Source of Information// i Insurance

Select one of the following:

E Excel

R Report

(E)xcel Format or (R)eport Format: : Report//

If you selected a long report period it is

recommended that this report be queued.

\*\*\* This report is 132 characters wide \*\*\*

DEVICE: HOME// HOME (CRT)

Sample Output for a Summary Report

SOURCE OF INFORMATION REPORT Mar 23, 2020@10:08:31 PAGE 2

FOR THE BILLED DATE RANGE: Jan 01, 2015 TO Jan 30, 2015 TYPE: SUMMARY

SOURCE OF INFORMATION: ALL

-------------------------------------------------------------------------------

Source Outpt Bill Cnt Outpt Bill Amt Outpt Pay Cnt Outpt Pay Amt

ICB CARD READER 1,799 687,120.85 210 53,914.03

CONTRACT SERVICE 109 14,954.70 3 209.37

Outpt Total 4,456 2,028,736.61 732 266,160.82

Grand Total

Source Bill Cnt Bill Amt Pay Cnt Pay Amt

INTERVIEW 312 125,865.86 34 9,768.97

DATA MATCH 30 11,911.72 4 1,517.63

PRE-REGISTRATION 761 265,755.33 97 31,003.11

eIV 1,468 1,006,248.30 407 231,808.44

HMS 121 59,114.81 23 7,986.85

ICB CARD READER 1,815 691,775.97 211 54,000.25

CONTRACT SERVICE 110 15,319.16 3 209.37

Grand Total 4,617 2,175,991.15 779 336,294.62

Type \<Enter\> to continue or '^' to exit:

Sample Output for a Detail Report

SOURCE OF INFORMATION REPORT Mar 23, 2020@10:05:56 PAGE 1

FOR THE BILLED DATE RANGE: Jan 01, 2015 TO Jan 30, 2015 TYPE: DETAILED

SOURCE OF INFORMATION: ALL

SORT: Source of Information

..................................................... Inpatient Bills Entered .....................................................

Patient Name SSN Bill Num Insurance Company Bill Amt Bill Date Coll Amt Coll Date F/P/N Source

IBPATIENT,ONE XXXX XXXXXXX LIFE INVESTORS 364.46 Jan 23, 2015 0.00 N CONTRACT SERVICE

IBPATIENT,TWO XXXX XXXXXXX SINCLAIR HEALTH SERVI 538.89 Jan 13, 2015 86.22 Jan 26, 2015 P ICB CARD READER

IBPATIENT,THREE XXXX XXXXXXX BCBS WY\* 277.73 Jan 21, 2015 0.00 N ICB CARD READER

IBPATIENT,FOUR XXXX XXXXXXX BCBS WY\* 192.95 Jan 21, 2015 0.00 N ICB CARD READER

IBPATIENT,FIVE XXXX XXXXXXX BCBS WY\* 277.73 Jan 21, 2015 0.00 N ICB CARD READER

IBPATIENT,SIX XXXX XXXXXXX BCBS WY\* 277.73 Jan 21, 2015 0.00 N ICB CARD READER

IBPATIENT,SEVEN XXXX XXXXXXX BCBS WY\* 192.95 Jan 21, 2015 0.00 N ICB CARD READER

IBPATIENT,EIGHT XXXX XXXXXXX BCBS WY\* 195.87 Jan 21, 2015 0.00 N ICB CARD READER

IBPATIENT,NINE XXXX XXXXXXX BCBS WY\* 538.89 Jan 21, 2015 0.00 N ICB CARD READER

IBPATIENT,TEN XXXX XXXXXXX BCBS WY\* 192.95 Jan 21, 2015 0.00 N ICB CARD READER

IBPATIENT,ELEVEN XXXX XXXXXXX BCBS WY\* 277.73 Jan 21, 2015 0.00 N ICB CARD READER

IBPATIENT,TWELVE XXXX XXXXXXX BCBS WY\* 277.73 Jan 21, 2015 0.00 N ICB CARD READER

\* Next to bill indicates bill is canceled and not used in totals

### Interfacility Ins. Update Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report shows the relationship between the insurance companies in file \#36 and the payers in file \#365.12. The Interfacility Insurance Update Activity report can be run by picking the IFIU option from the Patient Insurance Menu (PI).

This option displays either all sent or received interfacility insurance update records. The report can be generated as a summary or detailed to provide insurance details.

This report is formatted to print at 132 columns for a detailed report.

Sample Screen

Summary or Detailed:// d Detailed

To view what your facility sent to other VAMCs choose SENT.

To view what your facility received from other VAMCs choose RECEIVED.

Report Type - (S)ent or (R)eceived Report// r Received

To know which records filed to buffer and which did not,

select "YES" to include processing status.

Include processing status? YES// y YES

Receiving Date Range:

Earliest Date Received: 6/11/2021// (JUN 11, 2021)

Latest Date Received: TODAY// (JUN 11, 2021)

Select Originating Facility: ALL//

(E)xcel Format or (R)eport Format: Report//

Select one of the following:

D Date Received

P Patient Name

F Facility Originated From

Sort the report by: d Date Received

\*\*\* This report is 132 characters wide \*\*\*

DEVICE: HOME// ;132 HOME (CRT)

Sample Output for a Summary Report

Interfacility Ins. Update Report-Summary Mar 08, 2021@12:49:45 Page: 1

Date Range: 02/16/2021 - 03/08/2021 Sent to other Facilities

-------------------------------------------------------------------------------

Total Number of Transmissions Sent 4

Total Facilities 3

BATTLE CREEK VAMC (XXX) 2

BECKLEY VAMC (XXX) 1

BEDFORD VAMC (XXX) 1

\*\*\* END OF REPORT \*\*\*Sample Output for a Detailed Report

Interfacility Ins. Update Report-Detail Oct 28, 2021@07:55:07 Page: 1

Date Range: 10/25/2021 - 10/28/2021 All Facilities, Received from other Facilities Primary sort: Date

Last Originating Date

Patient Name 4 SSN Insurance Company Subscriber ID COB Facility Received Processing Status

-----------------------------------------------------------------------------------------------------------------------------------

IBSUB,ACTIVE XXXX AETNA XXXXXXXX P CHARLESTON (XXX) 10/25/21 DUPLICATE

IBSUB,TWOTRLRS XXXX MEDICARE (WNR) XXXXXXXXXX CHARLESTON (XXX) 10/25/21 VISITED TOO LONG AGO

IBSUB,ACTIVE XXXX AETNA XXXXXXXX P CW BILL YOU (XXX) 10/26/21 DUPLICATE

IBSUB,ACTIVE XXXX AETNA XXXXXXXX P CW BILL YOU (XXX) 10/26/21 DUPLICATE

IBSUB,ACTIVE XXXX CIGNA XXXXXXXX S CW BILL YOU (XXX) 10/26/21 DUPLICATE

\*\*\* END OF REPORT \*\*\*

### Ins Company Link Report (aka “Insurance Company Link Report”)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report shows the relationship between the insurance companies in file \#36 and the payers in file \#365.12.

Sample Screen

Insurance Company Link Report

In order for an Insurance Company to be eligible for electronic insurance

eligibility communications via the eIV software or to transmit active

insurance to another VAMC via IIU, the Insurance Company needs to be

linked to an appropriate payer from the National EDI Payer list.

The National EDI Payer list contains the names of the payers that are

currently participating with the eIV and/or IIU process.

This report option provides information to assist with finding unlinked

insurance companies or payers, which can subsequently be linked through the

INSURANCE COMPANY EDIT option.

Select one of the following:

1 Unlinked insurance companies

2 Linked insurance companies

Select type of insurance companies to display: // 2 Linked insurance companies

Select one of the following:

1 ALL insurance companies

2 Keyword search in insurance companies

3 Select insurance companies

Select companies to display: // 3 SELECTED insurance companies

Select INSURANCE COMPANY: ACORDIA

1 ACORDIA PO BOX 2451 CHARLESTON WEST VIRGINIA Y

2 ACORDIA NATIONAL PO BOX 3262 CHARLESTON WEST VIRGINIA Y

CHOOSE: (1-2): 1 ACORDIA PO BOX 2451 CHARLESTON WEST VIRGINIA Y

Select another INSURANCE COMPANY: ACORDIA

1 ACORDIA PO BOX 2451 CHARLESTON WEST VIRGINIA Y

2 ACORDIA NATIONAL PO BOX 3262 CHARLESTON WEST VIRGINIA Y

CHOOSE: (1-2): 2 ACORDIA NATIONAL PO BOX 3262 CHARLESTON WEST VIRGINIA

Y

Select another INSURANCE COMPANY:

(E)xcel Format or (R)eport Format: Report//

Select one of the following:

1 Insurance Company Name

2 Payer Name

3 VA National Payer ID

Select the primary sort field: 1// Insurance Company Name

\*\*\* This report is 132 characters wide \*\*\*

DEVICE: HOME//

Sample Output

Insurance Company Link Report Mar 10, 2021@14:15:33 Page: 1

Linked Insurance Companies - Selected

Insurance Company: \# Active eIV Nationally IIU Nationally eIV Locally Prof/Inst EDI#

Payer Name Groups VA ID Enabled Enabled Enabled

------------------------------------------------------------------------------------------------------------------------------------

ACORDIA 1 PO BOX XXXX CITYXX, WV XXXXX XXXXX/XXXXX

WELLS FARGO THIRD PARTY(CHIP PE VAXXX YES YES XXXXX/XXXXX

ACORDIA NATIONAL 7 PO BOX 3262 CITYXX, WV XXXXX XXXXX/XXXXX

WELLS FARGO THIRD PARTY(CHIP PE VAXXX YES YES XXXXX/XXXXX

\*\*\* END OF REPORT \*\*\*

Type \<Enter\> to continue or '^' to exit:

### Payer Link Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To be eligible for electronic insurance eligibility communications via the eIV and IIU software, participating Insurance Companies must be linked to a payer from the National EDI Payer list. The National EDI Payer list contains the names of the payers that are currently participating in the eIV and IIU process.

This report provides information based on the relationship that the users set up in VistA between the insurance companies and the payers. This report can assist with finding insurance companies that are linked to the wrong payer. Also, the report can assist with identifying unlinked insurance companies or payers. Additionally, this report will indicate the payer's locally active status.

This report shows the relationship between the insurance companies in file \#36 and the payers in file \#365.12.

Sample Screen

Payer Link Report

In order for an Insurance Company to be eligible for electronic insurance

eligibility communications via the eIV software or to transmit active insurance

to another VAMC via IIU, the Insurance Company needs to be linked to an

appropriate payer from the National EDI Payer list. The National EDI Payer

list contains the names of the payers that are currently participating with

the eIV and/or IIU process.

This report provides access to the following information:

\- A list of all payers with current eIV and IIU settings.

\- A list of all payers with associated linked insurance company detail.

\- A list of all payers with no insurance companies linked.

Include deactivated payers? YES//

Select a Payer (RETURN for ALL Payers):

(E)xcel Format or (R)eport Format: Report//

eIV Payer list - displays those payers who can send and receive

HIPAA 270/271 transactions for verification.

IIU Payer list - displays those payers who are eligible to exchange

between VAMCs for active insurance.

Both - includes any payer that is defined as either eIV or IIU

or both applications.

Select one of the following:

1 eIV Payer List

2 IIU Payer List

3 Both

Select a report option: 3// Both

Select one of the following:

1 Unlinked Payers

2 Linked Payers

3 ALL Payers

Select the type of payers to display: 3// ALL Payers

Select one of the following:

1 List linked insurance company detail

2 Do not list linked insurance company detail

Select company detail option: 1// List linked insurance company detail

Select one of the following:

1 Payer Name

2 VA National Payer ID

3 Nationally Enabled Status

4 Locally Enabled Status

5 \# of Linked Insurance Companies

Select the primary sort field: 1// Payer Name

\*\*\* This report is 132 characters wide \*\*\*

DEVICE: HOME//

Sample Output

Payer Link Report All EIV Payers, With Ins. Co. Detail Mar 25, 2021@10:09:04 Page: 1

\# Linked Nationally Locally Auto Prof/Inst. Also

Payer Name: VA ID Ins. Co. Enabled Enabled Update EDI# IIU

----------------------------------------------------------------------------------------------------------------------------------

1199 NATIONAL BENEFIT FUND VAXXXX 0 YES YES NO XXXXX/XXXXX NO

AARP HEALTH PLAN VAXXX 1 YES YES YES XXXXX/XXXXX NO

Linked Insurance Companies Address City, State, Zip code

AARP UNITEDHEALTHCARE AARP HEALTHCARE OPTIONS CITY, GA XXXXX-XXXX XXXXX/XXXXX

ACORDIA NATIONAL-MOHWK/HCKRY SPRVAXXXX 0 NO YES NO NO

ACS BENEFIT SERVICES VAXXXX 0 YES NO NO XXXXX/XXXXX NO

ADVANTRA (TX, NM, AZ) VAXXX 0 YES YES NO XXXXX/XXXXX NO

AETNA VAX 41 YES YES YES XXXXX/XXXXX YES

Linked Insurance Companies Address City, State, Zip code

AETNA P.O. BOX XXXXXX CITY, TX XXXXX-XXXX XXXXX/XXXXX

AETNA GLOBAL BENEFITS PO BOX XXXXX CITY, FL XXXXX-XXXX

### Coverage Limitations Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report generates a list of coverage limitations by company and group.

Sample Screen

Coverage Limitations Report

This report will generate a list of coverage limitations by company and

group. You must select one, multiple, or all insurance companies and anywhere

from one to all of the plans under each company. The results can be filtered

by coverage limitation status.

1 - List All 1293 Ins. Companies

2 - List Only Ins. Companies That You Select

SELECT 1 or 2: 2 List Only Ins. Companies That You Select

1 - Select ACTIVE Insurance Companies

2 - Select INACTIVE Insurance Companies

3 - Select BOTH

Select 1 or 2 or 3: 1// 1 ACTIVE

1 - Select Insurance Companies that Begin with: XXX

2 - Select Insurance Companies that Contain: XXX

3 - Select Insurance Companies in Range: XXX - YYY

Select 1, 2 or 3: 1// 2 Contains

Select Insurance Companies that contain: aarp

Insurance Company Selection Jan 04, 2022@09:44:41 Page: 1 of 1

Insurance Companies that contain: aarp

Showing Active Insurance Companies

0 Insurance Companies selected

Name A/I Street Address

1 AARP UNITEDHEALTHCARE A AARP HEALTHCARE OPTIONS

1\> AARP UNITEDHEALTHCARE A

AARP HEALTHCARE OPTIONS

Enter ?? for more actions \>\>\>

SE Select Ins Co NE New Search SH Show Selections

DE Deselect Ins Co EX Exit

Select Action: Quit// SE Select Ins Co

Select Insurance Company(s): (1-1): 1

Insurance Company Selection Jan 04, 2022@09:44:46 Page: 1 of 1

Insurance Companies that contain: aarp

Showing Active Insurance Companies

1 Insurance Companies selected

Name A/I Street Address

1\> AARP UNITEDHEALTHCARE A AARP HEALTHCARE OPTIONS

Enter ?? for more actions \>\>\>

SE Select Ins Co NE New Search SH Show Selections

DE Deselect Ins Co EX Exit

Select Action: Quit// QUIT

1 - List All 99 Group Plans

2 - List Only Group Plans That You Select

SELECT 1 or 2: 1 List All 99 Group Plans

1 - Select ACTIVE Group Plans

2 - Select INACTIVE Group Plans

3 - Select BOTH

Select 1 or 2 or 3: 1// 1 ACTIVE

1 - Select GROUP NAME

2 - Select GROUP NUMBER

3 - Select BOTH

Select 1 or 2 or 3: 3 BOTH

1 - Select Group(s) that Begin with: XXX

2 - Select Group(s) that Contain: XXX

3 - Select Group(s) in Range: XXX - YYY

4 - Select Group(s) that are BLANK

Select 1, 2, 3 or 4: 2 Contains

Select Group(s) that contain: 1

1 - Select Coverage Status COVERED

2 - Select Coverage Status NOT COVERED

3 - Select Coverage Status CONDITIONAL

4 - Select Coverage Status BY DEFAULT (blank status)

5 - Show all Coverage Statuses

Select 1, 2, 3, 4 or 5: 5 ALL

(E)xcel Format or (R)eport Format: Report//

We recommend you queue this report as it will take awhile.

\*\*\* You will need a 132 column printer for this report. \*\*\*

DEVICE: HOME// ;132 HOME (CRT)

Sample Output

Coverage Limitations Report

COVERAGE LIMITATION REPORT JAN 04, 2022@10:08 Page: 1

-----------------------------------------------------------------------------------------------------------------------------------

\+ =\>INDIV. PLAN \* =\> INACTIVE

Filters: Selected Insurances, All Group Plans, Contains = 1, All Coverage Statuses

COMPANY GROUP NAME GROUP NUMBER CATEGORY EFFECTIVE DATE COVERED? LIMIT COMMENTS?

AARP UNITEDHEALTHCARE AARP HEALTHCARE OPTIONS, CITY, GA XXXXX-XXXX

GROUP NAME GRP NUM XXXX \<\< MEDIGAP PLAN F \>\>

INPATIENT CONDITIONAL YES

OUTPATIENT BY DEFAULT

PHARMACY 01/01/2001 NO

DENTAL BY DEFAULT

MENTAL HEALTH BY DEFAULT

LONG TERM CARE BY DEFAULT

PROSTHETICS BY DEFAULT

VISION BY DEFAULT

\<NO GROUP NAME\> GRP NUM XXX \<\< MEDIGAP PLAN C \>\>

INPATIENT BY DEFAULT

OUTPATIENT BY DEFAULT

PHARMACY 06/01/1993 NO

DENTAL BY DEFAULT

Type \<Enter\> to continue or '^' to exit:

# Billing Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*Documentation for the Unbilled Amounts Menu, which was released to the field as patch IB\*2\*19, has been included in this section of the manual as a matter of convenience. The Unbilled Amounts Menu \[IBT UNBILLED MENU\] need not be assigned to the Billing Supervisor Menu. It may be assigned to any menu in Integrated Billing, or a user’s secondary menu, as deemed appropriate by IRMS.

## Insurance Buffer Activity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides a summary of the activity within the Insurance Buffer for a specified date range. Counts, percentages, and average processing times are included for both processed and unprocessed entries. The report can be printed with totals only or by month within the selected date range.

Sample Output

INS BUFFER ACTIVITY REPORT Apr 17, 2001 - Nov 05, 2001 11/5/21 11:06 PAGE 1

------------------------------------------------------------------------------

TOTALS

AVERAGE LONGEST SHORTEST

STATUS COUNT PERCENT \# DAYS \# DAYS \# DAYS

------------------------------------------------------------------------------

ENTERED 24 66.6% 39.0 146.0 0.0

ACCEPTED 5 13.8% 22.6 108.9 0.2

REJECTED 7 19.4% 62.6 146.0 3.0

------------------------------------------------------------------------------

NOT PROCESSED 24 66.6% 37.3 146.0 0.0

PROCESSED 12 33.3% 42.8 146.0 0.2

TOTAL 36 100.0% 39.0 146.0 0.0

0 New Companies (0%), 1 New Group/Plans (2%), 1 New Patient Policy (2%)

## Management Reports (Billing) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Statistical Report (IB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report lists the total number of Integrated Billing actions by action type along with the total charge by type for a date range. Integrated Billing actions include inpatient copayments by treating specialty, inpatient, and NHCU per diems; and NHCU, outpatient, and pharmacy copayments.

Net statistics compute the current status for each new entry in the selected date range to calculate the net totals. Net totals are derived from the last update for a parent (even when the update is not within the date range) using the following formula: new entries (+) updates within the date range (-) cancellations.

The gross statistics count only the entries in the date range. It is possible that the net and gross statistics may not match. For example, if a charge was canceled after the selected date range of the report but before the report ran, the net figures would reflect this, but the gross figures would not.

Sample OutputINTEGRATED BILLING STATISTICAL REPORT

INTEGRATED BILLING STATISTICAL REPORT

for

CHEYENNE VAMC (XXX)

From: JAN 01, 2018

To: OCT 25, 2018

Date Printed: OCT 25, 2018

Page: 1

--------------------------

NET TOTALS BY ACTION TYPE

(INPT) NEW

NUMBER ENTRIES: 6

DOLLAR AMOUNT: \$4389.4

(OPT) NEW

NUMBER ENTRIES: 9

DOLLAR AMOUNT: \$275

(PER DIEM) NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$252

(RX) NEW

NUMBER ENTRIES: 13

DOLLAR AMOUNT: \$173

MTF (INPT) NEW

NUMBER ENTRIES: 14

DOLLAR AMOUNT: \$8049.2

MTF (OPT) NEW

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$113

MTF (PER DIEM) NEW

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$350

MTF (RX) NEW

NUMBER ENTRIES: 6

DOLLAR AMOUNT: \$127

(INPT) NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$2400

(OPT) NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$115

(PER DIEM) NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$30

(RX) NEW

NUMBER ENTRIES: 10

DOLLAR AMOUNT: \$164

(INPT) NEW

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$3880.2

(OPT) NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$65

(PER DIEM) NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$100

(RX) NEW

NUMBER ENTRIES: 8

DOLLAR AMOUNT: \$174

FEE SERVICE (OPT) NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$30

INPT COPAY (MED) NEW

NUMBER ENTRIES: 13

DOLLAR AMOUNT: \$10268

INPT PER DIEM NEW

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$10900

LTC INPT NHCU NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$1166

OPT COPAY NEW

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$215

TRICARE INPT COPAY NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$190

TRICARE OPT COPAY NEW

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$67

TRICARE RX COPAY NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$42

SERV NSC RX COPAY NEW

NUMBER ENTRIES: 0

DOLLAR AMOUNT: \$0

CC INPT CNH NEW

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$2037

CC INPT RESPITE NEW

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$3007

CC OPT ADHC NEW

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$60

CC OPT RESPITE NEW

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$165

CCN INPT CNH NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$3652

CCN INPT RESPITE NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$3483

CCN OPT ADHC NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$80

CCN OPT RESPITE NEW

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$50

CHOICE INPT CNH NEW

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$2716

CHOICE INPT RESPITE NEW

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$3007

CHOICE OPT ADHC NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$115

CHOICE OPT RESPITE NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$80

NSC RX COPAY NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$36

SC RX COPAY NEW

NUMBER ENTRIES: 0

DOLLAR AMOUNT: \$0

GROSS TOTALS BY ACTION TYPE

(INPT) NEW

NUMBER ENTRIES: 9

DOLLAR AMOUNT: \$7108.6

(OPT) NEW

NUMBER ENTRIES: 11

DOLLAR AMOUNT: \$305

(PER DIEM) NEW

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$302

(RX) NEW

NUMBER ENTRIES: 34

DOLLAR AMOUNT: \$849

MTF (INPT) NEW

NUMBER ENTRIES: 14

DOLLAR AMOUNT: \$8049.2

MTF (OPT) NEW

NUMBER ENTRIES: 6

DOLLAR AMOUNT: \$163

MTF (PER DIEM) NEW

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$350

MTF (RX) NEW

NUMBER ENTRIES: 9

DOLLAR AMOUNT: \$193

(INPT) NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$2400

(OPT) NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$115

(PER DIEM) NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$30

(RX) NEW

NUMBER ENTRIES: 10

DOLLAR AMOUNT: \$164

(INPT) NEW

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$4112.4

(OPT) NEW

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$145

(PER DIEM) NEW

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$150

(RX) NEW

NUMBER ENTRIES: 9

DOLLAR AMOUNT: \$184

FEE SERVICE (OPT) NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$45

INPT COPAY (MED) NEW

NUMBER ENTRIES: 13

DOLLAR AMOUNT: \$10268

INPT PER DIEM NEW

NUMBER ENTRIES: 6

DOLLAR AMOUNT: \$10910

LTC INPT NHCU NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$1166

OPT COPAY NEW

NUMBER ENTRIES: 16

DOLLAR AMOUNT: \$765

TRICARE INPT COPAY NEW

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$316

TRICARE OPT COPAY NEW

NUMBER ENTRIES: 8

DOLLAR AMOUNT: \$340

TRICARE RX COPAY NEW

NUMBER ENTRIES: 9

DOLLAR AMOUNT: \$634

SERV NSC RX COPAY NEW

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$32

CC INPT CNH NEW

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$2037

CC INPT RESPITE NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$3580

CC OPT ADHC NEW

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$75

CC OPT RESPITE NEW

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$165

CCN INPT CNH NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$3652

CCN INPT RESPITE NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$3483

CCN OPT ADHC NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$80

CCN OPT RESPITE NEW

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$50

CHOICE INPT CNH NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$3902

CHOICE INPT RESPITE NEW

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$4153

CHOICE OPT ADHC NEW

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$130

CHOICE OPT RESPITE NEW

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$130

NSC RX COPAY NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$36

SC RX COPAY NEW

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$16

(INPT) CANCEL

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$2719.2

(OPT) CANCEL

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$30

(PER DIEM) CANCEL

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$50

(RX) CANCEL

NUMBER ENTRIES: 21

DOLLAR AMOUNT: \$676

MTF (OPT) CANCEL

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$50

MTF (RX) CANCEL

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$66

(INPT) CANCEL

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$232.2

(OPT) CANCEL

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$95

(PER DIEM) CANCEL

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$50

(RX) CANCEL

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$10

FEE SERVICE (INPT) CANCEL

NUMBER ENTRIES: 12

DOLLAR AMOUNT: \$11767.2

FEE SERVICE (OPT) CANCEL

NUMBER ENTRIES: 14

DOLLAR AMOUNT: \$280

INPT COPAY (MED) CANCEL

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$6048

INPT PER DIEM CANCEL

NUMBER ENTRIES: 7

DOLLAR AMOUNT: \$166

LTC FEE OPT ADHC CANCEL

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$45

LTC INPT NHCU CANCEL

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$52

LTC INPT RESPITE CANCEL

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$776

OPT COPAY CANCEL

NUMBER ENTRIES: 16

DOLLAR AMOUNT: \$730

TRICARE INPT COPAY CANCEL

NUMBER ENTRIES: 4

DOLLAR AMOUNT: \$291

TRICARE OPT COPAY CANCEL

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$285

TRICARE RX COPAY CANCEL

NUMBER ENTRIES: 6

DOLLAR AMOUNT: \$592

SERV INPT PER DIEM CANCEL

NUMBER ENTRIES: 9

DOLLAR AMOUNT: \$240

SERV NSC RX COPAY CANCEL

NUMBER ENTRIES: 5

DOLLAR AMOUNT: \$43

CC INPT RESPITE CANCEL

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$573

CC OPT ADHC CANCEL

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$15

CHOICE INPT CNH CANCEL

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$1186

CHOICE INPT RESPITE CANCEL

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$1146

CHOICE OPT ADHC CANCEL

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$15

CHOICE OPT RESPITE CANCEL

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$50

NSC RX COPAY CANCEL

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$24

SC RX COPAY CANCEL

NUMBER ENTRIES: 2

DOLLAR AMOUNT: \$16

(OPT) UPDATE

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$15

FEE SERVICE (OPT) UPDATE

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$15

SERV NSC RX COPAY UPDATE

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$11

ADMISSION

NUMBER ENTRIES: 1

DOLLAR AMOUNT: \$0

ADMISSION

NUMBER ENTRIES: 17

DOLLAR AMOUNT: \$0

ADMISSION

NUMBER ENTRIES: 3

DOLLAR AMOUNT: \$0

### Most used Outpatient CPT Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will list the most common ambulatory procedures and ambulatory surgeries performed within a date range for the selected clinic(s). This list may be used to help select which codes to include when building CPT check-off sheets through the Build CPT Check-off Sheet option under the Ambulatory Surgery Maintenance Menu.

The user can sort by clinic or procedure. When sorting by procedure, also include full procedure descriptions.

All reports provide the CPT code and procedure, a count of each procedure that has been entered for a clinic visit, the number billed, the OPC status, and the charge amount. The status and charge amount given are as of the current date. If no charge amount is shown, the procedure is not a billable procedure.

This output requires 132 column margin width.

Depending on the date range chosen, this report could be quite lengthy. Queue this to print during non-work hours.

Sample Output

CLINIC CPT USAGE FOR JAN 1,1991 - JAN 1,1992 APR 16, 1992 11:22 PAGE 1

ALL DIVISIONS AND CLINICS

AMBULATORY PROCEDURE COUNT \#BILLED OPC STATUS CHARGE

---------------------------------------------------------------------------------------------------------

XXXXX REMOVE FOREIGN BODY 38 38 NATIONALLY ACTIVE 256.50

INCISION AND REMOVAL OF FOREIGN BODY, SUBCUTANEOUS TISSUES;

COMPLICATED

XXXXX SURGICAL CLEANSING OF SKIN 56 NATIONALLY ACTIVE

DEBRIDEMENT OF EXTENSIVE ECZEMATOUS OR INFECTED SKIN; UP TO 10% OF

BODY SURFACE

XXXXX REPAIR OF WOUND OR LESION 89 34 NATIONALLY ACTIVE 394.20

REPAIR, COMPLEX, EYELIDS, NOSE, EARS AND / OR LIPS; 2.6 CM TO 7.5 CM

XXXXX AMPUTATION FOLLOW-UP SURGERY 29 394.20

AMPUTATION, ARM THROUGH HUMERUS; SECONDARY CLOSURE OR SCAR REVISION

XXXXX REPAIR LIP 1 1 NATIONALLY ACTIVE 394.20

REPAIR LIP, FULL THICKNESS; OVER ONE HALF VERTICAL HEIGHT, OR

COMPLEX

XXXXX REMOVE FOREIGN BODY FROM EYE 18 15 INACTIVE 343.80

REMOVAL OF FOREIGN BODY, INTRAOCULAR; FROM ANTERIOR CHAMBER OR LENS

XXXXX INCISION, SECONDARY CATARACT 36 NATIONALLY ACTIVE

DISCISSION OF SECONDARY MEMBRANEOUS CATARACT (OPACIFIED POSTERIOR

LENS CAPSULE AND / OR ANTERIOR HYALOID; STAB INCISION TECHNIQUE

(ZIEGLER OR WHEELER KNIFE)

XXXXX BONE MARROW BIOPSY 12 NATIONALLY ACTIVE

BONE MARROW BIOPSY, NEEDLE OR TROCAR;

### Insurance Buffer Employee

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report provides a summary of entries and actions in the Insurance Buffer by employee for a specified date range. It can be printed for those employees who create buffer entries (primarily non-insurance personnel) or for those employees who verify and process (accept/reject) buffer entries (primarily insurance personnel). The report can also be printed for one specific employee or all employees. Counts, percentages, and average processing times are included and can be printed with totals only or by month.

Sample Output

INS BUFFER EMPLOYEE REPORT Apr 17, 1998 - Nov 05, 1998 11/5/98 11:13 PAGE 1

--------------------------------------------------------------------------------

LASTNAME, FIRSTNAME TOTALS

AVERAGE LONGEST SHORTEST

STATUS COUNT PERCENT \# DAYS \# DAYS \# DAYS

-----------------------------------------------------------------------------

ACCEPTED 2 25.0% 0.0 0.2 0.2

REJECTED 6 75.0% 72.5 146.0 21.7

TOTAL 8 100.0% 72.5 146.0 0.2

0 New Companies (0%), 0 New Group/Plans (0%), 1 New Patient Policy (12%)

INSURANCE BUFFER EMPLOYEE REPORT Apr 17, 1998 - Nov 05, 1998 11/5/98 11:13 PAGE 2

--------------------------------------------------------------------------------

LASTNAME, FIRSTNAME TOTALS

AVERAGE LONGEST SHORTEST

STATUS COUNT PERCENT \# DAYS \# DAYS \# DAYS

-----------------------------------------------------------------------------

ACCEPTED 8 88.8% 105.0 105.0 105.0

REJECTED 1 11.1% 0.0 3.0 3.0

TOTAL 9 100.0% 105.0 105.0 3.0

0 New Companies (0%), 2 New Group/Plans (22%), 0 New Patient Policies (0%)

INSURANCE BUFFER EMPLOYEE REPORT Apr 17, 1998 - Nov 05, 1998 11/5/98 11:13 PAGE 3

--------------------------------------------------------------------------------

TOTALS

AVERAGE LONGEST SHORTEST

STATUS COUNT PERCENT \# DAYS \# DAYS \# DAYS

-----------------------------------------------------------------------------

ACCEPTED 10 58.8% 22.6 108.9 0.2

REJECTED 7 41.1% 62.6 146.0 3.0

TOTAL 17 100.0% 39.0 108.9 0.2

0 New Companies (0%), 2 New Group/Plans (11.7%), 1 New Patient Policies (5%)

### New Companies (0%), 0 New Group/Plans (0%), 1 New Patient Policy (20%) Clerk Productivity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clerk Productivity option allows the user to print a report for bills entered, authorized, or printed within a selected date range. The report is sorted alphabetically by the clerk who first entered, authorized, or printed the bill.

The user can print either a full or summary report. If the user selects to print a full report, select specific clerk(s) and rate type(s) to include.

A summary report will list the clerk, rate type, and the count and dollar amount of bills entered for each rate type for each clerk. A subtotal is provided for each clerk. The total amount for the report is also displayed.

The full report will list the clerk, rate type, date entered, current status, bill number, total charges, patient name, and patient ID for each bill included in the report. The full report should be printed at 132 column margin width.

Depending on the date range and other specifications opted for, this report could be quite lengthy. Queue the report to print during off hours.

Sample Output

CLERK PRODUCTIVITY REPORT FOR JUN 1,1995 - NOV 26,1995 NOV 26,1995 13:02 PAGE 1

BILL TOTAL

ENTERED/EDITED BY RATE TYPE DATE ENTERED CURRENT STATUS NUMBER AMOUNT NAME PATIENT ID

--------------------------------------------------------------------------------------

JOHN REIMBURSABLE INS. NOV 10,1995 ENTERED/NOT REV XXXXXX IBpatient,one XXX-XX-XXXX

REIMBURSABLE INS. NOV 17,1995 ENTERED/NOT REV XXXXXX IBpatient,two XXX-XX-XXXX

REIMBURSABLE INS. NOV 17,1995 ENTERED/NOT REV XXXXXX IBpatient,three XXX-XX-XXXX

------- ---------

SUBTOTAL 0.00

SUBCOUNT 3

ANDREW REIMBURSABLE INS. SEP 7,1995 ENTERED/NOT REV XXXXXX IBpatient,one XXX-XX-XXXX

REIMBURSABLE INS. SEP 7,1995 AUTHORIZED XXXXXX 00.00 IBpatient,two XXX-XX-XXXX

REIMBURSABLE INS. SEP 7,1995 ENTERED/NOT REV XXXXXX IBpatient,three XXX-XX-XXXX

REIMBURSABLE INS. SEP 7,1995 ENTERED/NOT REV XXXXXX IBpatient,four XXX-XX-XXXX

REIMBURSABLE INS. SEP 7,1995 ENTERED/NOT REV XXXXXX IBpatient,five XXX-XX-XXXX

REIMBURSABLE INS. SEP 7,1995 ENTERED/NOT REV XXXXXX IBpatient,six XXX-XX-XXXX

REIMBURSABLE INS. SEP 7,1995 ENTERED/NOT REV XXXXXX IBpatient,seven XXX-XX-XXXX

REIMBURSABLE INS. SEP 7,1995 ENTERED/NOT REV XXXXXX IBpatient,eight XXX-XX-XXXX

REIMBURSABLE INS. SEP 7,1995 ENTERED/NOT REV XXXXXX IBpatient,nine XXX-XX-XXXX

REIMBURSABLE INS. SEP 7,1995 ENTERED/NOT REV XXXXXX IBpatient,ten XXX-XX-XXXX

REIMBURSABLE INS. NOV 23,1995 ENTERED/NOT REV XXXXXX IBpatient,one XXX-XX-XXXX

REIMBURSABLE INS. NOV 25,1995 ENTERED/NOT REV XXXXXX IBpatient,two XXX-XX-XXXX

------- ---------

SUBTOTAL 5000.00

SUBCOUNT 12

CHARLES REIMBURSABLE INS. SEP 28,1995 ENTERED/NOT REV XXXXXX IBpatient,one XXX-XX-XXXX

------- ---------

SUBTOTAL 0.00

SUBCOUNT 1

PAUL REIMBURSABLE INS. SEP 10,1995 AUTHORIZED XXXXXX 163.00 IBpatient,two XXX-XX-XXXX

------- ---------

SUBTOTAL 163.00

SUBCOUNT 1

LINDA REIMBURSABLE INS. JUN 10,1995 ENTERED/NOT REV XXXXXX IBpatient,three XXX-XX-XXXX

REIMBURSABLE INS. JUN 10,1995 ENTERED/NOT REV XXXXXX 163.00 IBpatient,four XXX-XX-XXXX

------- ---------

SUBTOTAL 163.00

SUBCOUNT 2

BETH REIMBURSABLE INS. SEP 15,1995 CANCELLED XXXXXX 163.00 IBpatient,five XXX-XX-XXXX

------- ---------

SUBTOTAL 163.00

SUBCOUNT 1

------- ---------

TOTAL 5489.00

COUNT 20

### Rank Insurance Carriers By Amount Billed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Rank Insurance Carriers By Amount Billed option is used to generate a listing of insurance carriers ranked by the total amount billed. The user will be prompted for a date range from which bills should be selected and the number of carriers to be ranked.

11. Insurance carriers that have been inactivated will be flagged as such on this report. If an inactivated company is associated with an active company to which all patients’ policies have been recorded, the amount billed to the inactive company is credited to the active company.

This option no longer allows the user to transmit the report to the MCCR Program Office. Now, the IRM Service has the capability to transmit the report electronically to the Program Office. A patch will be issued with specific instructions should this report be required to be transmitted.

Sample Output

Ranking Of The Top 9 Insurance Carriers By Total Amount Billed

Facility: ALBANY (XXX) Run Date: 05/24/95

Date Range: 10/01/93 thru 05/24/95 Page: 1

\*\* - denotes an inactive company

=============================================================================

Rank Insurance Carrier Total Amt Billed

=============================================================================

1\. HEALTH INSURANCE LTD. \$215,868.78

23 3RD ST

Suite 450

ANYTOWN, NEW YORK 12181

2\. ABC INS \$35,843.63

123 Ave Of The Moons

ANYTOWN, CALIFORNIA 00098

3\. GHI \$4,902.00

675 THIRD AVE

ANYTOWN, NEW YORK 12345

4\. ABC INS \$4,048.06

789 UBIQUITOUS STREET

ANYTOWN, UTAH 44432

5\. ABC INS \$3,153.24

567 RAIN AVE.

ANYTOWN, IOWA 33321

6\. XYZ INS \$2,862.43

123 MAIN STREET

ANYTOWN, NEW YORK 33343

7\. ABC INS \$1,576.00

123 MASON STREET

ANYTOWN, NEW YORK 11234

8\. STRAIT INSURANCE \$950.00

98 PARK AVE

ANYTOWN, TEXAS 43222

9\. TRAVELERS-RICHMOND \$482.69

1234 THOMAS ST.

ANYTOWN, VIRGINIA 12345

Total Amount Billed to all Ranked Carriers: \$269,686.83

### Billing Rates List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Billing Rates List option will print a list of billing rates for a selected date range. It is an efficient way to verify that all billing rate entries have been entered correctly.

The output generated by this option displays the CHAMPVA, Health Care Finance Administration (HCFA) ambulatory surgery rates, Medicare deductibles, and copayments. The effective date, amount (basic rate), and additional amount will be shown for each rate, if applicable. Certain ambulatory surgeries may be billed at the HCFA rate. The amount shown (if any) in the Additional Amount column is an extra amount that may be charged for all procedures within that rate group. The amount shown under Inpatient Per Diem and NHCU Per Diem is the daily charge for Category C patients.

Any billing rate that is effective for any date within the selected range is displayed. If more than one rate was effective within the date range, both rates are displayed.

Sample Output

JUN 11,1997 \*\*\*Billing Rates Listing\*\*\* PAGE 1

Rates in effect from: JAN 01, 1997

to: JUN 11, 1997

=============================================================================

CHAMPVA LIMIT

Effective Date Amount Additional Amount

OCT 01, 1991 \$25

CHAMPVA SUBSISTENCE

Effective Date Amount Additional Amount

OCT 01, 1994 \$9.50

HCFA AMB. SURG. RATE 1

Effective Date Amount Additional Amount

JAN 01, 1992 \$285

HCFA AMB. SURG. RATE 2

Effective Date Amount Additional Amount

JAN 01, 1992 \$382

Sample Output

JUN 11,1997 \*\*\*Billing Rates Listing\*\*\* PAGE 2

Rates in effect from: JAN 01, 1997

to: JUN 11, 1997

=============================================================================

HCFA AMB. SURG. RATE 3

Effective Date Amount Additional Amount

JAN 01, 1992 \$438

HCFA AMB. SURG. RATE 4

Effective Date Amount Additional Amount

JAN 01, 1992 \$539

HCFA AMB. SURG. RATE 5

Effective Date Amount Additional Amount

JAN 01, 1992 \$615

HCFA AMB. SURG. RATE 6

Effective Date Amount Additional Amount

JAN 01, 1992 \$580 \$200

JUN 11,1997 \*\*\*Billing Rates Listing\*\*\* PAGE 3

Rates in effect from: JAN 01, 1997

to: JUN 11, 1997

=============================================================================

HCFA AMB. SURG. RATE 7

Effective Date Amount Additional Amount

JAN 01, 1992 \$853

HCFA AMB. SURG. RATE 8

Effective Date Amount Additional Amount

JAN 01, 1992 \$705 \$200

HCFA AMB. SURG. RATE 9

Effective Date Amount Additional Amount

JAN 01, 1992 \$0

INPATIENT PER DIEM

Effective Date Amount Additional Amount

OCT 01, 1990 \$10

Sample Output

JUN 11,1997 \*\*\*Billing Rates Listing\*\*\* PAGE 4

Rates in effect from: JAN 01, 1997

to: JUN 11, 1997

=============================================================================

MEDICARE DEDUCTIBLE

Effective Date Amount Additional Amount

JAN 01, 1996 \$736

NHCU PER DIEM

Effective Date Amount Additional Amount

OCT 01, 1990 \$5

NSC PHARMACY COPAY

Effective Date Amount Additional Amount

OCT 01, 1992 \$2

JUN 09, 1997 \$5.00 \$2.00

SC PHARMACY COPAY

Effective Date Amount Additional Amount

OCT 01, 1990 \$2

### Revenue Code Totals by Rate Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Revenue Code Totals by Rate Type option prints the total amount billed by revenue code for a selected rate type and date range.

Circular 10-91-012 requires that revenue code 100 be used for the \$10.00 hospital per diem and revenue code 550 be used for the \$5.00 nursing home per diem. The purpose of this report is to allow sites to calculate the total amount billed for \$5 (revenue code 550) and \$10 (revenue code 100) Means Test per diems for input to Automated Management Information System (AMIS) segments 295 and 296.

Print a list of all revenue codes (for the date range) with the associated patient name, patient ID, bill \#, and individual amount or a summary list that provides the total amount and the total number of bills for each code.

12. Because more than one revenue code may appear on a bill, the total number of bills does not equal the sum of the number of bills containing a specific revenue code.

Sample Output

Revenue Code Totals for MEANS TEST/CAT. C JUN 3, 1992@15:34:31 PAGE1

For Bills First Printed JUN 1, 1992 to JUN 3, 1992

Patient Pt. ID. Bill No. Rev. Code Amount

-----------------------------------------------------------------------------

IBpatient,one XXX-XX-XXXX XXXXXX 510 \$30.00

IBpatient,two XXX-XX-XXXX XXXXXX 100 \$50.00

IBpatient,three XXX-XX-XXXX XXXXXX 001 \$652.00

IBpatient,four XXX-XX-XXXX XXXXXX 550 \$155.00

IBpatient,five XXX-XX-XXXX XXXXXX 100 \$150.00

IBpatient,six XXX-XX-XXXX XXXXXX 550 \$90.00

----------------------------------------------

REVENUE CODE TOTALS

Revenue Code: 001 .......... \$652.00 1 Bills

Revenue Code: 100 .......... \$200.00 2 Bills

Revenue Code: 510 \$30.00 1 Bills

Revenue Code: 550 \$245.00 2 Bills

--------------

\$1,127.00 6 Bills

### Bill Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Bill Status Report option is used to print a listing of bills and bill status for a specified date range. The user can opt to include all statuses or a single status. The report may be sorted by the event date (the date beginning the bill's episode of care), bill date (the date the bill was initially printed), or entered date (the date the bill was first entered).

The following data items will be provided in the first portion of the report for each bill listed: bill number, patient name, and patient ID#, event date, initials of the person who entered the bill, rate type, Means Test category, charges, and bill status with the date of that status. If the user opts to sort by bill date or entered date, the bills are grouped for each date (billed or entered) of the selected range. The second portion of the report provides summary totals. The dollar amount and the total number of bills for each bill type and for each status are included. Grand totals are also provided.

For bills that have been disapproved during the authorization process, the report will show \*REVIEWED/DISAPP (will appear only for bills prior to this version of the IB software) or \*AUTHORIZED/DISAPP after the status. The bill status will be followed by the initials of the user responsible for that status and his/her DUZ number. This is a number that uniquely identifies the user to the system. If a bill is pending (i.e., not printed or canceled), the bill status will be preceded by an asterisk (\*) on the report.

Sample Output

Date/Time Printed: DEC 16,1993@09:14

Medical Care Cost Recovery Bill Status Report for period covering JUN 1, 1993 through JUN 16, 1993 Page 1

---------------------------------------------------------------------------------------------------------------------------------

EVENT ENTRD MT

BILL NO. PATIENT NAME PT.ID DATE BY RATE TYPE CATEGORY CHARGES BILL STATUS

==================================================================================================================================

XXXXXX IBpatient,one XXXX 06/01/93 ARH REIM INS-OPT N/A \$936.40 \* AUTHORIZED 09/07/93 (XXX/XXXXX)

XXXXXX IBpatient,two XXXX 06/02/93 ARH REIM INS-OPT A \$442.20 \* AUTHORIZED 09/07/93 (XXX/XXXXX)

XXXXXX IBpatient,three XXXX 06/03/93 ARH MT/CAT C-OPT N/A \$30.00 PRINTED 09/07/93 (XXX/XXXXX)

XXXXXX IBpatient,four XXXX 06/03/93 ARH REIM INS-OPT R \$633.10 PRINTED 11/19/93 (XXX/XXXXX)

XXXXXX IBpatient,five XXXX 06/04/93 ARH REIM INS-OPT N/A \$623.60 \* AUTHORIZED 09/07/93 (XXX/XXXXX)

XXXXXX IBpatient,six XXXX 06/07/93 ARH REIM INS-OPT N/A \$0.00 \* ENTERED 09/07/93 (XXX/XXXXX)

XXXXXX IBpatient,seven XXXX 06/07/93 ARH CRIME-OPT N/A \$0.00 \* AUTHORIZED 09/07/93 (XXX/XXXXX)

XXXXXX IBpatient,eight XXXX 06/09/93 ARH REIM INS-OPT N \$150.00 \* ENTERED 09/07/93 (XXX/XXXXX)

XXXXX IBpatient,nine XXXX 06/09/93 ARH REIM INS-OPT A \$128.00 \* ENTERED 09/07/93 (XXX/XXXXX)

XXXXXX IBpatient,ten XXXX 06/10/93 LR REIM INS-OPT N/A \$491.80 \* ENTERED 06/10/93 (LR/700)

\* Denotes that the bill status is not Printed or Cancelled

Date/Time Printed: DEC 16,1993@09:14

Medical Care Cost Recovery Bill Status Report for period covering JUN 1, 1993 through JUN 16, 1993 Page 2

---------------------------------------------------------------------------------------------------------------------------------

REPORT STATISTICS

=================================================================================================================================

CRIME-OPT .................... \$0.00 1 BILLS

MT/CAT C-OPT .................... \$30.00 1 BILLS

REIM INS-OPT .................... \$3,405.10 8 BILLS

----------------- -------------

\$3,435.10 10 BILLS

AUTHORIZED .................... \$2,002.20 4 BILLS

ENTERED .................... \$769.80 4 BILLS

PRINTED .................... \$663.10 2 BILLS

----------------- -------------

\$3,435.10 10 BILLS

### Rate Type Billing Totals Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Rate Type Billing Totals Report option is used to obtain a listing of all billing totals for each rate type for a specified date range. The date range is selected by event date (the date beginning the bill's episode of care) or bill date (the date the bill was initially printed).

The report is generated in two sections. The first section divides all the bills for each rate type (Category C, Workman's Compensation, Tort Feasor, etc.) into the following categories: initiated, pending, printed, and canceled. The exact number of bills and dollar amount for each category is provided. The total amounts (sum of all rate types) are also given for each category.

The second section of the report is a breakdown of all the pending billing records (the pending category in the first section). All the pending bills for each rate type are divided into the following categories: no action, reviewed, and authorized. The exact number of bills and the dollar amount for each category is provided. The total amounts (sum of all rate types) are also given for each category.

The margin width of this output is 132.

Sample Output

Date/Time Printed: JUL 14,1988@07:46

Billing Summary Report for period covering JAN 3,1988 through MAR 1,1988 (by Event Date)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

INITIATED \| PENDING \| PRINTED \| CANCELLED \|

BILL TYPE Number Dollars\| Number Dollars\| Number Dollars\| Number Dollars\|

====================================================================================================

CRIME VICTIM 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

DENTAL 1 \$127.00 \| 0 \$0.00 \| 0 \$0.00 \| 1 \$127.00 \|

HUMANITARIAN 1 \$0.00 \| 1 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

INTERAGENCY 1 \$7,200.00 \| 0 \$0.00 \| 1 \$7,200.00 \| 0 \$0.00 \|

MEANS TEST/CAT. C 13 \$11,964.00 \| 8 \$11,284.00 \| 4 \$160.00 \| 1 \$520.00 \|

MEDICARE ESRD 1 \$124,900.00 \| 1 \$124,900.00 \| 0 \$0.00 \| 0 \$0.00 \|

NO FAULT INS. 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

REIMBURSABLE INS. 20 \$138,852.00 \| 6 \$12,190.00 \| 8 \$102,985.00 \| 6 \$23,677.00 \|

SHARING AGREEMENT 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

TORT FEASOR 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

UNKNOWN 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

WORKERS' COMP. 1 \$2,250.00 \| 0 \$0.00 \| 1 \$2,250.00 \| 0 \$0.00 \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TOTALS 38 \$285,293.00 \| 16 \$148,374.00 \| 14 \$112,595.00 \| 8 \$24,324.00 \|

Date/Time Printed: JUL 14,1988@07:46

Summary of Pending Bill Authorizations for period covering JAN 3,1988 through MAR 1,1988 (by Event Date)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TOTAL PENDING \| NO ACTION \| REVIEWED \| AUTHORIZED \|

BILL TYPE Number Dollars\| Number Dollars\| Number Dollars\| Number Dollars\|

======================================================================================

CRIME VICTIM 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

DENTAL 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

HUMANITARIAN 1 \$0.00 \| 1 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

INTERAGENCY 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

MEANS TEST/CAT. C 8 \$11,284.00 \| 3 \$0.00 \| 0 \$0.00 \| 5 \$11,284.00 \|

MEDICARE ESRD 1 \$124,900.00 \| 1 \$124,900.00 \| 0 \$0.00 \| 0 \$0.00 \|

NO FAULT INS. 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

REIMBURSABLE INS. 6 \$12,190.00 \| 2 \$0.00 \| 3 \$12,140.00 \| 1 \$50.00 \|

SHARING AGREEMENT 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

TORT FEASOR 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

UNKNOWN 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

WORKERS' COMP. 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \| 0 \$0.00 \|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PENDING TOTALS 16 \$148,374.00 \| 7 \$124,900.00 \| 3 \$12,140.00 \| 6 \$11,334.00 \|

### Insurance Payment Trend Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to analyze payment trends among insurance companies and track receivables that are due to the facility. Many different criteria may be specified to limit the selection of bills such as rate type, inpatient or outpatient bills, open or closed bills, treatment dates, bill printed dates, and insurance companies.

The report may be run for a single insurance company or a range of companies. In addition, the user may analyze any specialized subset of bills by selecting an additional field from the BILL/CLAIMS file (#399) and specifying a range of values for that field.

The Insurance Payment Trend Report displays the Payer’s Name/TIN in the Header on the Summary and Main reports using the Payer TIN and Name stored in the (835).

The Insurance Payment Trend Report displays the 835 indicator (%) in front of the Patient Name if an 835 (ERA) is attached to the reported claim.

Sample Output

REIMBURSABLE INS. PAYMENT TREND REPORT - OUTPATIENT BILLING MAY 06, 2014 PAGE 1

DATE BILL PRINTED: 05/05/14 - 05/06/14

> **NOTE:** '\*' after the Bill No. denotes a CLOSED bill

BILL PATIENT DATE DATE BILL \#

AMOUNT AMOUNT AMOUNT AMOUNT PERC

NUMBER NAME (AGE) BILL FROM - TO PRINTED CLOSED DAYS

BILLED COLLECTED UNPAID PENDING COLL

-------------------------------------------------------------------------------

M A I N R E P O R T

INSURANCE CARRIER: AARP/\<PAYER TIN\>

P.O. BOX 819

ANYTOWN, GEORGIA 30374018 Phone: XXX XXX-XXXX

Group \#42

XXXXXX %\<Patient Name\> 04/07/14 04/07/14 05/06/14 ACTIVE 0

19.11 0.00 19.11 19.11 0.00

The user has the option to run a detailed report for all claims that meet the report criteria or to print summary statistics only. The detailed report includes the bill number, patient name and age (as of the bill event date), the bill from and to dates, the date the bill was printed (authorized), the date the bill closed, the number of days the bill has been open (the difference between the DATE PRINTED and the DATE BILL CLOSED fields), the amounts billed, collected, unpaid, remaining open, and percentage collected. The AMOUNT PENDING column has been added to differentiate the number of unpaid dollars and the number of dollars that are still pending collection. If the bill is not closed, the amount pending is the same as the amount unpaid. If the bill is closed (signified by an asterisk next to the bill number), the amount pending is zero.

The report is sorted alphabetically by insurance company name and a subtotal for the number of bills, amount billed, the amount collected, amount unpaid, amount pending, and percentage collected is given for each company. If the user opts only to print summary statistics, only these subtotals are printed. Also included, for either the detailed or summary report, are the grand totals for these categories. A margin width of 132 cols. is required for this output.

The DATE BILL CLOSED field will always have an entry. If the bill is not actually closed, the Accounts Receivable status of the bill will appear on the report in the DATE BILL CLOSED column. If a bill is closed, an asterisk (\*) will appear after the bill number. If a bill is rejected, a c will display next to that bill number.

Sample Output for a Range of Insurance Companies

REIMBURSABLE INS. PAYMENT TREND REPORT -- COMBINED INPATIENT AND OUTPATIENT BILLING NOV 26, 1993 PAGE: 1

DATE BILL PRINTED: 01/01/92 - 03/04/92 Note: '\*' after the Bill Number denotes a CLOSED bill

DISCHARGE STATUS: ALL VALUES

BILL PATIENT DATE DATE BILL \# AMOUNT AMOUNT AMOUNT AMOUNT PERCENT

NUMBER NAME/ (AGE) BILL FROM - TO PRINTED CLOSED DAYS BILLED COLLECTED UNPAID PENDING COLLECTED

--------------------------------------------------------------------------------------

PRIMARY INSURANCE CARRIER: ABC

123 Ave Of The Moons

ANYTOWN, CALIFORNIA 00098 Phone: XXX-XXX-XXXX

XXXXXX IBpatient,one (49) 02/07/92 02/07/92 02/07/92 NEW BILL 658 200.00 100.00 100.00 100.00 50.00

--------- --------- --------- --------- -------

TOTAL NUMBER OF BILLS: 1 200.00 100.00 100.00 100.00 50.00

PRIMARY INSURANCE CARRIER: ABC

789 UBIQUITOUS STREET

ANYTOWN, UTAH 44432

XXXXXX IBpatient,two (33) 04/09/91 04/14/91 02/06/92 NEW BILL 659 2770.00 0.00 2770.00 2770.00 0.00

--------- --------- --------- --------- -------

TOTAL NUMBER OF BILLS: 1 2770.00 0.00 2770.00 2770.00 0.00

PRIMARY INSURANCE CARRIER: STRAIT INSURANCE

98 PARK AVE

ANYTOWN, TEXAS 43222

XXXXXX IBpatient,three (45) 02/05/91 02/05/91 02/18/92 11/26/93 647 950.00 702.50 247.50 0.00 75.00

--------- --------- --------- --------- -------

TOTAL NUMBER OF BILLS: 1 950.00 702.50 247.50 0.00 75.00

GRAND TOTAL NUMBER OF BILLS: 3

GRAND TOTAL AMOUNT BILLED: 3920.00

GRAND TOTAL AMOUNT COLLECTED: 802.50

GRAND TOTAL AMOUNT UNPAID: 3117.50

GRAND TOTAL AMOUNT PENDING: 2870.00

PERCENTAGE COLLECTED: 20.47

Sample Output for a Single Insurance Company

REIMBURSABLE INS. PAYMENT TREND REPORT -- COMBINED INPATIENT AND OUTPATIENT BILLING SEP 27, 1995 PAGE: 1

DATE BILL PRINTED: 01/01/95 - 09/27/95 Note: '\*' after the Bill Number denotes a CLOSED bill

BILL PATIENT DATE DATE BILL \# AMOUNT AMOUNT AMOUNT AMOUNT PERC

NUMBER NAME/ (AGE) BILL FROM - TO PRINTED CLOSED DAYS BILLED COLLECTED UNPAID PENDING COLL

--------------------------------------------------------------------------------------

PRIMARY INSURANCE CARRIER: ABC

123 AVE OF THE MOONS

LOS ANGELES, CALIFORNIA 00098 Phone: 618-555-9871

XXXXXX IBpatient,one (70) 06/22/95 07/10/95 09/20/95 NEW BILL 1 194.00 0.00 194.00 194.00 0.00

XXXXXX IBpatient,two (70) 07/17/95 07/31/95 09/20/95 NEW BILL 1 194.00 0.00 194.00 194.00 0.00

XXXXXX IBpatient,three (46) 01/01/92 07/02/92 03/28/95 NEW BILL 177 4460.00 0.00 4460.00 4460.00 0.00

XXXXXX IBpatient,four (68) 10/22/93 10/22/93 03/15/95 NEW BILL 190 178.00 0.00 178.00 178.00 0.00

---------- --------- -------- --------- -----

TOTAL NUMBER OF BILLS: 4 5026.00 0.00 5026.00 5026.00 0.00

GRAND TOTAL NUMBER OF BILLS: 4

GRAND TOTAL AMOUNT BILLED: 5026.00

GRAND TOTAL AMOUNT COLLECTED: 0.00

GRAND TOTAL AMOUNT UNPAID: 5026.00

GRAND TOTAL AMOUNT PENDING: 5026.00

PERCENTAGE COLLECTED: 0.00

### Unbilled BASC for Insured Patient Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Unbilled BASC for Insured Patient Appointments report lists all BASC (billable ambulatory surgical code) procedures for scheduled appointments of insured patients that could not be matched with BASC procedures entered on a bill for the patient for a selected date range. The match is based on the appointment date in Scheduling and the procedure date in Billing. The purpose of this report is to find all CPTs that were entered in Scheduling but never brought into Billing.

The list is printed in alphabetical order by patient name and provides the patient ID, appointment date, CPT code, and procedure.

Sample Output

PATIENT NAME PATIENT ID APPOINTMENT DATE BILLABLE AMBULATORY PROCEDURE

--------------------------------------------------------------------------------------

IBpatient,one XXX-XX-XXXX MAR 27,1992 XXXXX REMOVE THIGH PRESSURE SORE

XXXXX REMOVE THIGH PRESSURE SORE

IBpatient,two XXX-XX-XXXX MAR 3,1992 XXXXX BONE MARROW BIOPSY

IBpatient,three XXX-XX-XXXX MAR 7,1992 XXXXX CLEANSING OF SKIN/TISSUE

IBpatient,four XXX-XX-XXXX MAR 13,1992 XXXXX AMPUTATION FOLLOW-UP SURGERY

### ROI Expired Consent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will list the ROI Special Consents that will expire within a user-specified date range.

Sample Output

ROI Special Consent To Expire Feb 01, 2013 - Apr 01, 20133/26/13 11:40 PAGE 1

Patient Effective Expiration

--------------------------------------------------------------------------------

IBpatient,one Jun 26, 2012 Mar 31, 2013

IBpatient,one Jun 26, 2012 Apr 01, 2013

IBpatient,five Mar 01, 2013 Mar 31, 2013

IBpatient,six Jan 01, 2013 Mar 20, 2013

IBpatient,nine Jan 01, 2013 Apr 01, 2013

IBpatient,nine Feb 01, 2013 Mar 20, 2013

## Medication Copayment Income Exemption Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Print Charges Canceled Due to Income Exemption

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables the user to print a report that lists patients and medication copayment charges that are canceled due to the income exemption (charges to patients determined to be exempt from the medication copayment requirement).

The user is prompted for a date range. The start date defaults to the effective date of the medication copayment legislation (Public Law 102-568), October 30, 1992, and the to date defaults to the date of the conversion completion.

This report should be reconciled periodically with the Accounts Receivable Medication Co-Pay Exemption Report (Medication Co-Pay Exemption Report option) to ensure the accuracy of patients' accounts.

Initially, this report will print a list of charges canceled during the installation/conversion process. Later, this report may be used to list charges automatically canceled. This occurs when a patient with a status of NON-EXEMPT due to no income data becomes EXEMPT due to income below the threshold level.

This report includes the patient’s name and ID, prescription date and number, cancel date and IB number, bill number and amount, patient count, and the dollar total. The user can also print a Conversion Quick Status Report with the listing that includes data such as the dates the conversion started and completed, the total number of patients checked, the number of patients exempt and non-exempt, the number of bills checked, dollar amount checked, total bills canceled, and amount canceled.

Queue this report to print during non-work hours as it may be very lengthy. The output for this option requires 132 columns.

Sample Output

Medication Copayment Exemption Conversion Status

Conversion was started on: FEB 4, 1993@11:18:28

The conversion completed on: FEB 4, 1993@18:19:01

Elapse time for Conversion was: 7 Hours, 0 Minutes, 33 Seconds

Last Patient DFN Checked == 91

1\. Total Patients Checked == 7455

Exempt Patients == 2069

Non-Exempt Patients == 5386

2\. Total Number of Bills checked == 36568

Dollar Amount Checked == \$ 86252

No. of Exempt Bills Checked == 14218

Exempt Dollar amount == \$ 33426

No. of Non-Exempt Bills Checked == 22350

Non-exempt Dollar amount == \$ 52826

3\. Total Bills Actually canceled == 14113

Amount Actually canceled == \$ 33158

Rx Copay Income Exemption Report MAR 4, 1993 11:18:43 Page 1

Cancel Cancel Original

Name Pt. ID Rx Date Rx/Refill Date IB Number Bill No. Amount

-------------------------------------------------------------------------------------------------

IBpatient,one XXX-XX-XXXX 02/01/93 XXXXXX 02/02/93 XXXXXX XXX-XXXXXX \$2

02/01/93 XXXXXX 02/02/93 XXXXXX XXX-XXXXXX \$2

--------------

Count = 2

Amount = \$ 4

IBpatient,two XXX-XX-XXXX 01/26/93 XXXXXX/1 01/27/93 XXXXXX XXX-XXXXXX \$4

01/26/93 XXXX 01/27/93 XXXXXX XXX-XXXXXX \$2

--------------

Count = 2

Amount = \$ 6

IBpatient,three XXX-XX-XXXX 01/26/93 XXXXXX 01/27/93 XXXXXX XXX-XXXXXX \$2

01/26/93 XXXXXX/1 01/27/93 XXXXXX XXX-XXXXXX \$2

--------------

Count = 2

Amount = \$ 4

======================================

Total Patient Count = 3

Total Rx Count = 6

Total Dollar amount = \$ 14

### Edit Copay Exemption Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to edit IB form letters. The user is prompted to edit the header field. This text is automatically centered at the top of the letter (it is not necessary to center text) and must be edited to the facility's name and address. There is a limit of six lines of text.

The second field, the MAIN BODY, contains the text of the letter including the signer's title. Because the person signing this letter may be site-specific, it might be necessary to edit the signer's title.

The default for the starting address line (patient address) is 15. This may be edited to any number between 10 and 25. This feature is provided to account for slight differences in printers and automated letter folders at each site.

When editing the IB Income Test Reminder letter, the user is prompted for a reprint date, whether to exclude domiciliary patients, and to schedule the days on which the letters are to print. The days selected to print the letters represent the mornings the user wants to pick up the letters from the printer. For example, if Monday is chosen, the letters print Sunday evening and are ready to be picked up on Monday morning. The user can prevent the letters from being printed by answering YES to the Do you wish to stop this job from running? prompt.

After editing is completed, test print one letter. If the user opts to test print, a prompt to select a patient and device will appear. The letter is queueable to any printer.

Sample Letter

Department of Veterans Affairs Medical Center

113 Holland Avenue

ANYTOWN, New York 12208

DEC 14, 1995

In Reply Refer To:

XXX-XX-XXXX

ONE IBPATIENT

54 BROADWAY

ANYTOWN, MA XXXXX

The VA is required by law to charge Veterans who receive medications

on an outpatient basis for the treatment of nonservice-connected

conditions, a copayment of \$2.00 for each 30-day (or less) supply

of medication provided. Based on the income information requested

each year, some Veterans may be exempt from the copayment.

Our records indicate that your medication copayment exemption

status will expire on December 31, 1995.

To update your income information so we may review your

copayment exemption status, please call XXX-XXXX xXXXX

to set up an appointment to provide us with current

income information.

Chief, MAS

### Inquire to Medication Copay Income Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to print a brief or full inquiry of exemptions for a patient. The brief inquiry is used to view past and/or present exemptions, and the full inquiry is used to view the entire audit history of all changes to a patient's exemption status.

Both inquiries provide the patient’s name and current status. The brief inquiry provides the following information on all active exemptions for the selected patient: effective date, type, status, reason, how the entry was added, and when. The full inquiry provides the following information for each exemption for the patient: effective date, status, whether active or inactive, how the entry was added, by whom and when, type, and reason for exemption.

13. Programmers: For users whose FileMan Access ="@" (DUZ(0)="@"), the full inquiry feature will display the patient internal entry number and the billing exemption internal entry number to aid in problem resolution.

All Medal of Honor recipients will be exempt from Medication Copayment (Public Law 114-315).

Sample Output

Billing Exemption Inquiry MAR 5, 1993 13:10:46 Page 1

IBpatient,one XXXX Currently: NON-EXEMPT-INCOME\>PENSION 02/10/93

-----------------------------------------------------------------------------

Effective Date: FEB 10, 1993 Type: COPAY INCOME EXEMPTION

Status: NON-EXEMPT Reason: NO INCOME DATA

Active: NO, INACTIVE User: ALAN

How Added: SYSTEM When Added: FEB 10, 1993@15:14:12

Effective Date: FEB 10, 1993 Type: COPAY INCOME EXEMPTION

Status: EXEMPT Reason: HARDSHIP

Active: NO, INACTIVE User: MICHAEL

How Added: MANUAL When Added: FEB 11, 1993@09:17:06

Charges Canceled: FEB 10, 1993 To: FEB 11, 1993

Effective Date: FEB 10, 1993 Type: COPAY INCOME EXEMPTION

Status: NON-EXEMPT Reason: INCOME\>PENSION

Active: NO, INACTIVE User: MICHAEL

How Added: SYSTEM When Added: FEB 11, 1993@09:55:38

Effective Date: FEB 10, 1993 Type: COPAY INCOME EXEMPTION

Status: EXEMPT Reason: HARDSHIP

Active: NO, INACTIVE User: PETER

How Added: MANUAL When Added: FEB 11, 1993@09:56:22

Charges Canceled: FEB 10, 1993 To: FEB 11, 1993

Effective Date: FEB 10, 1993 Type: COPAY INCOME EXEMPTION

Status: NON-EXEMPT Reason: INCOME\>PENSION

Active: NO, INACTIVE User: STEPHEN

How Added: SYSTEM When Added: FEB 11, 1993@10:00:37

Effective Date: FEB 10, 1993 Type: COPAY INCOME EXEMPTION

Status: EXEMPT Reason: HARDSHIP

Active: NO, INACTIVE User: PETER

How Added: MANUAL When Added: FEB 11, 1993@10:00:49

Charges Canceled: FEB 10, 1993 To: FEB 11, 1993

Effective Date: FEB 10, 1993 Type: COPAY INCOME EXEMPTION

Status: NON-EXEMPT Reason: INCOME\>PENSION

Active: NO, INACTIVE User: PETER

How Added: SYSTEM When Added: FEB 17, 1993@15:28:39

Sample Brief Output for Medal of Honor Exemption

Medication Copayment Income Exemption Status

IBPATIENT,MOH XXXX Currently: EXEMPT-MEDAL OF HONOR 01/30/19

EFFECTIVE TYPE STATUS REASON ADDED BY/ON

--------------------------------------------------------------------------------

01/30/19 RX COPAY EXEMPT MEDAL OF HONOR SYSTEM/ 01/30/19

Medication Copayment Exemption Status Currently computes to: EXEMPT

Patient awarded Medal of Honor

Sample Full Output for Medal of Honor Exemption

Billing Exemption Inquiry FEB 11, 2019 16:36:41 Page 1

IBPATIENT,MOH XXXX Currently: EXEMPT-MEDAL OF HONOR 02/11/19

--------------------------------------------------------------------------------

\*\*Effective Date: FEB 11, 2019 Type: COPAY INCOME EXEMPTION

Status: EXEMPT Reason: MEDAL OF HONOR

Active: YES, ACTIVE User: IBTEST,USER

How Added: SYSTEM When Added: FEB 11, 2019@16:06:19

Patient DFN: XXXXXXX Ex. Number: XXXXXX

Effective Date: FEB 11, 2019 Type: COPAY INCOME EXEMPTION

Status: NON-EXEMPT Reason: INCOME\>PENSION

Active: NO, INACTIVE User: IBTEST,USER

How Added: SYSTEM When Added: FEB 11, 2019@14:50

Patient DFN: XXXXXXX Ex. Number: XXXXX

### Manually Change Copay Exemption (Hardships)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is designed to grant and/or remove hardship waivers for patients who request the new copay income test. It may also be used to grant exemptions to Means Test patients; however, if MAS grants a hardship waiver to the Means Test by changing a patient's Means Test status from Category C to Category A, a hardship exemption is automatically generated.

A message or alert is generated anytime a hardship exemption is granted or removed. If the USE ALERTS site parameter is set to NO (or the field is left unanswered), a mail bulletin is generated; if set to YES, an alert is generated. A sample mail bulletin is provided in the example.

The system attempts to keep the effective date of the exemption the same as the effective date of the income test by defaulting to the effective date of the last exemption at the Select Effective Date prompt. Only the date of previous exemptions or the current date may be entered at this prompt.

Occasionally, the creation of a patient's exemption may be interrupted unexpectedly. In such cases, this option may be used to detect copay exemption discrepancies and correct/update the patient's exemption status.

Once a waiver is granted, the exemption is good for one year from the date it is granted. An electronic signature code is required to grant a hardship waiver.

Sample Output

Subj: Medication Copayment Exemption Status Change \[#547\] 20 Apr 93 14:53

11 Lines

From: INTEGRATED BILLING PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

--------------------------------------------------------------------------

The following Patient's Medication Copayment Exemption Status has changed:

Patient: IBpatient,one PT. ID: XXX-XX-XXXX

Old Status: NON-EXEMPT - NO INCOME DATA Dated 03/09/93

New Status: EXEMPT - HARDSHIP Dated 03/10/93

Patient has been given a Hardship Exemption.

by: MARK/(Manual)

on: MAR 10, 1993 @ 14:53:40

Select MESSAGE Action: DELETE (from IN basket)//

### Letters to Exempt Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print the letters to be sent to patients who have been determined to be exempt from the medication copay. A range of patients and exemption effective dates may be specified. No letters will print for deceased patients, non-Veterans, and patients who are SC\>50%.

When this option is initially run, the user is prompted would like to store the results of the search in a template. If the answer YES, a search template, IB EXEMPTION LETTER, is created. This data may be accessed through the Print File Entries option in FileMan. For each subsequent search, the user is prompted to delete the results of the previous search. If YES, the previous search template is deleted, and an option of storing the results of the search. Only one IB EXEMPTION LETTER search template may exist at a time.

Medication copayment exemptions based on annual income must be re-evaluated yearly on the anniversary of a patient's copayment test. If a patient is exempt due to income below the threshold, a renewal date is shown below the in reply heading of the letter. The patient must complete a new copay income test by the renewal date, or he/she will no longer be considered exempt from the pharmacy copayment requirement.

This letter is designed to be one page and to print to a pin fed printer, on plain paper, in either 10 or 12 pitch. The default is set to start the address on line 15; however, this may be edited through the Edit Copay Exemption Letter option. If address line three contains data, that data prints at the end of address line two. If defined, temporary addresses are used.

IB\*2.0\*385 is part of VistA host file DG_53_P858.KID and provides Integrated Billing (IB) enhancements to support the Veterans Financial Assessment (VFA) Project. The VFA Project eliminates the annual means test renewal requirement for Veterans subject to means testing. Prior to the implementation of VFA, means test with a status of MT COPAY EXEMPT, GMT COPAY REQUIRED, or PENDING ADJUDICATION were considered expired 365 days from the effective date. Means tests with these statuses will no longer expire and will be considered current when the means test effective date is less than one year old from the VFA start date and forward. The VFA START DATE is a new field in the MAS PARAMETER File set to 1/1/2013 during the installation of the VFA host file.

14. The VFA Project did not include nor make any enhancements to copay exemption tests.

The following business rules pertain to exemptions letters where the billing exemption record was based on current means tests:

Exemptions letters based on a current means test will not include the renewal date. The letter should not state the means test needs to be re-evaluated yearly on the means test anniversary date.

Sample Letter

Department of Veterans Affairs Medical Center

113 Holland Avenue

ANYTOWN, NY 12208

MAY 5, 1993

In Reply Refer To:

XXX-XX-XXXX

Renewal Date: MAY 3, 1994

ONE IBPATIENT

77 MAIN ST

ANYTOWN, ME XXXXX

Public Law 102-568 enacted on October 29, 1992, provided for an exemption

to the prescription copayment for those Veterans who had income levels

less than the maximum rate of VA pension. Charges established before

October 29, 1992, were not exempted by the legislation.

We have reviewed your income and eligibility information contained in our

records and determined that you are eligible for the exemption. We are

currently reviewing your account and will make the appropriate adjustments

to it in the near future. If you are eligible for a refund for payments

made on charges established since October 29, 1992, we will forward you a

check. While we are reviewing your account we will not be sending out a

statement.

Medication copayment exemptions based upon annual income must be

re-evaluated yearly on the anniversary of your means test or copayment

test. If a renewal date is shown below the 'in reply' heading you must complete a new copay income test by that date or you will no longer be considered exempt from the pharmacy copayment requirement.

Please do not send in any more payments until we have completed this review

and forwarded a statement to you.

FINANCE OFFICER

### List Income Thresholds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to print an output that lists the income thresholds used in the medication copayment income exemption process sorted by type of threshold and effective date.

If the default of FIRST is accepted at the start date prompt, first to last is assumed.

This output requires 132 columns.

Sample Output

Medication Copayment Income Thresholds MAR 15,1993 08:29 PAGE 1

EFFECTIVE 1 2 3 4 5 6 7 8 ADDITIONAL

DATE BASE RATE DEPENDENT DEPENDENTS DEPENDENTS DEPENDENTS DEPENDENTS DEPENDENTS DEPENDENTS DEPENDENTS AMOUNT

--------------------------------------------------------------------------------------

TYPE: PENSION PLUS A&A

DEC 1,1992 12187.00 14548.00 15844.00 17140.00 18436.00 19732.00 21028.00 22324.00 23620.00 1296.00

### Print Patient Exemptions or Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to print a list of copayment exemption statistics. Both exempt and non-exempt patients are included.

The user is given the option to print a detailed patient listing or a summary. The detailed report may be sorted by either exemption status or exemption reason. The information given includes the patient’s name, patient ID, primary eligibility code, status, the reason for exemption/non-exemption, and status date. This data is followed by a summary showing subtotals for each exemption reason and totals for exempt and non-exempt patients. If the user opts to Print Summary Only, the detailed portion of the output is omitted. Deceased patients are not included in the summary provided with the detailed listing; however, if print the summary only is selected, deceased patients are included. Exemptions will now include Medal of Honor (Public Law 114-315).

When printing only a summary, sorting by the EXEMPTION STATUS default reduces the time required to produce the report.

The detailed patient listing requires 132 columns. Queue this output to print during non-work hours as it may be very lengthy.

Sample Output

Patient Medication Copayment Exemption Report FEB 11, 2019@11:24 PAGE 1BI

PATIENT PT ID PRIMARY ELIGIBILITY STATUS REASON STATUS DATE

-------------------------------------------------------------------------------------------------

IBPATIENT,ONE XXX-XX-XXXX NSC EXEMPT MEDAL OF HONOR JAN 25,2019

IBPATIENT,TWO XXX-XX-XXXX NSC EXEMPT MEDAL OF HONOR JAN 25,2019

IBPATIENT,THREE XXX-XX-XXXX SERVICE CONNECTED 50 EXEMPT SC\>50 JAN 2,2019

IBPATIENT,FOUR XXX-XX-XXXX SERVICE CONNECTED 50 EXEMPT SC\>50 JAN 1,2019

IBPATIENT,FIVE XXX-XX-XXXX AID & ATTENDANCE EXEMPT IN RECEIPT OF A&A JAN 1,2019

IBPATIENT,SIX XXX-XX-XXXX NSC EXEMPT DIS. RETIREMENT JAN 17,2019

IBPATIENT,SEVEN XXX-XX-XXXX NSC EXEMPT DIS. RETIREMENT JAN 10,2019

IBPATIENT,EIGHT XXX-XX-XXXX NSC EXEMPT DIS. RETIREMENT JAN 5,2019

IBPATIENT,NINE XXX-XX-XXXX NSC EXEMPT HARDSHIP JAN 5,2019

IBPATIENT,TEN XXX-XX-XXXX HUMANITARIAN EXEMPT NON-VETERAN JAN 29,2019

IBPATIENT,ELEVEN XXX-XX-XXXX HUMANITARIAN EXEMPT NON-VETERAN JAN 25,2019

====================================================

Exempt Status:

CATASTROPHICALLY DISABLED = 1

FORMER POW = 1

IN RECEIPT OF A&A = 18

IN RECEIPT OF HB = 6

IN RECEIPT OF PENSION = 10

INCOME\<PENSION = 19

MEDAL OF HONOR = 77

NON-VETERAN = 8

SC\>50 = 44

Total Exempt Patients = 184

Statistics and report DO NOT include deceased patients.

### Reprint Single Income Test Reminder Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to generate an Income Test reminder letter for a patient whose effective copay exemption is based upon income.

If the patient is currently non-exempt due to no income data reported, a letter may be generated if the patient’s previous exemption status is based on income.

IB\*2.0\*385 is part of VistA host file DG_53_P858.KID and provides Integrated Billing (IB) enhancements to support the Veterans Financial Assessment (VFA) Project. The VFA Project eliminates the annual means test renewal requirement for Veterans subject to means testing. Prior to the implementation of VFA, means test with a status of MT COPAY EXEMPT, GMT COPAY REQUIRED, or PENDING ADJUDICATION were considered expired 365 days from the effective date. Means tests with these statuses will no longer expire and will be considered current when the means test effective date is less than one year old from the VFA start date and forward. The VFA START DATE is a new field in the MAS PARAMETER File set to 1/1/2013 during the installation of the VFA host file.

15. The VFA Project did not include nor make any enhancements to copay exemption tests.

The following business rules pertain to reminder letters where the billing exemption record was based on current means tests:

Reminder Letters

The user will receive a warning when the Veteran's current medication copayment exemption is based on a current means test. The user is returned to the (menu or select patient prompt) and the letter is not printed.

Sample Letter

Department of Veterans Affairs Medical Center

113 Holland Avenue

ANYTOWN, New York 12208

DEC 14, 1995

In Reply Refer To:

XXX-XX-XXXX

ONE IBPATIENT

00 BROADWAY

ANYTOWN, MA XXXXX

The VA is required by law to charge Veterans who receive medications

on an outpatient basis for the treatment of nonservice-connected

conditions, a copayment of \$2.00 for each 30-day (or less) supply

of medication provided. Based on the income information requested

each year, some Veterans may be exempt from the copayment.

Our records indicate that your medication copayment exemption

status will expire on December 31, 1995.

To update your income information so we may review your

copayment exemption status, please call XXX-XXXX xXXXX

to set up an appointment to provide us with current

income information.

Chief, MAS

### Add Income Thresholds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit the income thresholds used in the medication copayment income exemption.

The thresholds are determined and released by VBA (Veterans Benefits Administration) on December 1<sup>st</sup> of each year. These are the same thresholds used for A&A pensions.

Once the ADDITIONAL DEPENDENT AMOUNT is entered, the amount for each additional dependent can be automatically calculated when the copayment income exemptions are built. However, if the amount for each additional dependent does not have to be calculated, the exemption can be built much faster; therefore, it is advantageous to enter the amount for each dependent.

If the new income thresholds are released or entered after the normal effective date, this package was designed to note exemptions created with thresholds over one year old and to allow automatic recompilation of just those exemptions.

### Print / Verify Patient Exemption Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will search the BILLING EXEMPTIONS file (#354.1) and compare the currently stored active exemption for each patient against what the system calculates to be the correct exemption status for the patient based on current data from the MAS files.

Once a date range is selected, the user is asked whether to update each incorrect exemption status. If NO, a list of discrepancies is printed without updating the incorrect statuses. If YES, the same report will print, and the statuses are updated. Initially, the report should be run without updating the exemptions.

The Manually Change Copay Exemptions (Hardship) option may also be used to update exemptions to the correct status one patient at a time.

Print/Verify Patient Exemption Status option will identify existing patients with incorrect exemptions that should be Medal of Honor exemptions and update the status of Medal of Honor recipients (Public Law 114-315).

This output requires 132 columns. Queue to print during non-work hours as it can be quite lengthy.

Sample Output

Medication Copayment Exemption Problem Report FEB 11, 2019 16:49 Page 1

Patient PT. ID Error Current Exemption Computed ExemptionAction

--------------------------------------------------------------------------------------

IBPATIENT,ONE XXX-XX-XXXX Exemption incorrect 10/08/18 NO INCOME DATA 01/11/17 INCOME\>PENSION Nothing Updated

IBPATIENT,TWO XXX-XX-XXXX Exemption incorrect 01/08/19 INCOME\>PENSION INCOME\<PENSION Nothing Updated

IBPATIENT,THREE XXX-XX-XXXX Exemption incorrect 01/02/19 NO INCOME DATA 12/28/16 INCOME\>PENSION Nothing Updated

IBPATIENT,FOUR XXX-XX-XXXX Exemption incorrect 01/04/19 02/11/19 MEDAL OF HONOR Nothing Updated

There were 4 discrepancies found in 2107 exemptions checked.

## MCCR System Definition Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MCCR System Definition Menu is locked with the IB SUPERVISOR security key.

### Enter / Edit Automated Billing Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit Automated Billing Parameters option is used to enter or edit the parameters that control automated third-party billing. Only entries in the Claims Tracking module will be billed automatically. Currently, only inpatient stays, outpatient encounters, and prescription refills are included in automated billing.

The following table lists a brief description of the parameters:

<table>
<caption><p><span id="_Toc143780858" class="anchor"></span>Table : Common Actions</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AUTO BILLER FREQUENCY</td>
<td>Number of days between each execution of the automated biller. For example, if the auto biller should run once a week, enter 7; if it should run every night, enter 1. If this field is left blank, the auto biller will never run.</td>
</tr>
<tr class="even">
<td>INPATIENT STATUS (AB)</td>
<td>This is the status that a PTF record must be in before the automated biller will attempt to create an inpatient bill. The PTF record must be closed before an automated bill can be created.</td>
</tr>
<tr class="odd">
<td>AUTOMATE BILLING</td>
<td>This parameter controls the automated creation of bills. If this field is set to YES, the bills will be automatically created for possible billable events with no user interaction. If this field is left blank, the earliest auto bill date must be added to each event in Claims Tracking before a bill is automatically created by the auto biller.</td>
</tr>
<tr class="even">
<td>BILLING CYCLE</td>
<td><p>This is the maximum number of days allowed to be billed on a single bill. If this field is left blank, the date range will default to the event date through the end of the month in which the event took place or for inpatient interim bills, the next month after the last interim bill.</p>
<p>Claims Tracking events may be added to the list of events for which an auto bill should be created by adding a date to the earliest auto bill date in Claims Tracking. Events may be removed from the auto biller list by adding a reason not billable or deleting the earliest auto bill date.</p></td>
</tr>
<tr class="odd">
<td>DAYS DELAY</td>
<td><p>This field controls the number of days after the end of the BILLING CYCLE that a bill should be created. This parameter is used at two different points to determine if a bill should be created. The first is when the Claims Tracking entry is first created. At that time, the EARLIEST AUTO BILL DATE will be set to the current date plus the number of DAYS DELAY. The second time this parameter is used is when the auto biller is trying to set up a date range for the events bill. In that case, DAYS DELAY is added to the BILLING CYCLE to determine if the correct amount of time has elapsed for the bill to be created.</p>
<p>For example, if DAYS DELAY is 3 and BILLING CYCLE is 10, a bill will not be created for at least 13 days after the initial entry was created in Claims Tracking. Inpatients are slightly different. If an inpatient is discharged, the auto biller will try to create a bill for that stay DAYS DELAY after the discharge date. The auto biller cannot, however, create a bill until the PTF record is closed. Therefore, the actual delay before bill creation for inpatient bills may be longer than DAYS DELAY.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc143780858" class="anchor"></span>Table : Common Actions

## Charge Master Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enter / Edit Charge Master

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used for the maintenance of Third-Party rates and charges. It contains the List Manager screens, which display all rate elements/fields. It also includes enter and edit actions so each element can be updated. All edit actions within these screens require the IB SUPERVISOR key.

| Screen                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Introduction Screen    | This screen displays a brief description of the elements of the Charge Master that may be viewed / edited through this option. The user can display / edit rate types, billing rates, charge sets, and rate schedules.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Rate Type Screen       | This is a display / edit screen for Billing Rate Types. All Rate Types currently defined are displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Billing Rates Screen   | This is a display / edit screen for Billing Rates. All Billing Rates currently defined are displayed. Part of the definition of a Billing Rate includes what types of items the rate’s charges are associated with (Billable Item) and how the charge should be calculated (Charge Method).                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Charge Set Screen      | This is a display / edit screen for Charge Sets. All Charge Sets currently defined will be displayed. These sets define a sub-set of charges for a Billing Rate. The editing of Charge Sets is restricted to non-critical elements if there are Charge Items defined for the set. Since Revenue Code and Bed section are required to add charges to a bill, the Default Revenue Code and Default Bed section are required unless these are defined for each individual Charge Item in the Set.                                                                                                                                                                                                                                           |
| Charge Item Screen     | This is a display / edit screen for Charge Items. These are the actual records of the item and its corresponding charge. This screen displays items that have active charges in a specified date range for the selected Charge Set. All active Charge Items are displayed for a Charge Set with a Billable Item of Bed section. However, this screen has been specifically limited to displaying either one CPT or one AWP item at a time. The Effective Date is required for all entries and controls when the charge is active. Each item entry overrides any previously effective charge for the item. A Revenue Code is only required if the Revenue Code for the item is different from the Default Revenue Code of the Charge Set. |
| Billing Regions Screen | This is a display / edit screen for Billing Regions. All Billing Regions currently defined will be displayed. Billing Regions can be set up that show the set of divisions that are billed the same charges for a Billing Rate. A Billing Region need only be defined if the charges for a rate vary by region/locality/division and more than one Region will be billed at the site. Currently, only Billing Rates based on CPT charges may vary by region.                                                                                                                                                                                                                                                                             |
| Rate Schedule Screen   | This is a display / edit screen for Rate Schedules. These schedules link charges and types of bills to be added to. All Rate Schedules currently defined are displayed. Rate Schedules must be defined for both inpatient and outpatient charges for a Rate Type and all Charge Sets that may be charged to that type of bill should be added. A Charge Set can be set up to be automatically added to bills or to require user input before the charges are added. The effective dates should only be added if there is a specific date that billing to the payer can start or stop.                                                                                                                                                    |

<span id="_Toc143780859" class="anchor"></span>Table : Common Actions

Sample OutputRATE SCHEDULE LISTRATE SCHEDULE List OCT 25, 2018@17:16 PAGE 1

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: CC MTF REIMB INS

CC-DOD-INPT INPAT INPATIENT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CC-DOD-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 2

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CC-DOD-OPT OUTPA OUTPATIENT DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 3

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 4

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 5

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

CC-DOD-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CC NO-FAULT AUTO

CC-NF-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 6

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CC-NF-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

CC-NF-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 7

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 8

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 9

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 10

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CC-NF-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CC REIMB INS

CC-RI-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CC-RI-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 11

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CC-RI-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 12

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 13

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 14

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

CC-RI-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CC TORT FEASOR

CC-TF-INPT INPAT JAN 7,2004 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 15

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CC-TF-SNF INPAT SKILLED NU JAN 7,2004 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

CC-TF-OPT OUTPA JAN 7,2004 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 16

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

--------------------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 17

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 18

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 19

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CC-TF-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CC WORKERS' COMP

CC-WC-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CC-WC-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 20

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CC-WC-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 21

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 22

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 23

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

CC-WC-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CCN NO-FAULT AUTO

CCN-NF-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 24

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CCN-NF-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

CCN-NF-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 25

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 26

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 27

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 28

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CCN-NF-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CCN REIMB INS

CCN-RI-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CCN-RI-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 29

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CCN-RI-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 30

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 31

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 32

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

CCN-RI-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CCN TORT FEASOR

CCN-TF-INPT INPAT JAN 7,2004 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 33

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CCN-TF-SNF INPAT SKILLED NU JAN 7,2004 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

CCN-TF-OPT OUTPA JAN 7,2004 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 34

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 35

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 36

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 37

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CCN-TF-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CCN WORKERS' COMP

CCN-WC-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CCN-WC-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 38

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CCN-WC-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 39

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 40

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 41

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

CCN-WC-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CHAMPVA

CVA-INPT INPAT JAN 1,2010 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 42

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CVA-SNF INPAT SKILLED NU JAN 1,2010 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

CVA-OPT OUTPA JAN 1,2010 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 43

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 44

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 45

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 46

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CVA-RX OUTPA PRESCRIPTI JAN 1,2010 YES RX COST YES

CHAMPVA RX COST+5 OUTPA PRESCRIPTI DEC 31,2009 YES RX COST YES

CHAMPVA OPT OUTPA OUTPATIENT DEC 31,2009 CMAC 389 C1 WYO YES

CMAC 314 C1 COLO YES

CMAC 314 FAC/PHYS YES

CMAC 314 FAC/NONPHYS

CMAC 389 FAC/PHYS YES

CMAC 389 FAC/NONPHYS

CMAC 314 NONFAC/PHYS

CMAC 314 NONFAC/NONPHYS

CMAC 389 NONFAC/PHYS

CMAC 389 NONFAC/NONPHYS

RATE TYPE: CHAMPVA REIMB. INS.

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 47

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CVA RI-INPT INPAT JAN 1,2010 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CVA RI-SNF INPAT SKILLED NU JAN 1,2010 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

CHAMPVA REIMB INS INPAT INPATIENT DEC 19,2003 DEC 31,2009 RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT FAC PR 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 48

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN 442GC

RC-PHYSICIAN 442GD

RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS ML 442GD YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS PR 442GD YES

RC-INPT ANC 442 YES

RC-INPT ANC ICU 442 YES

RC-INPT R&B 442 YES

RC-INPT R&B ICU 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 49

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CVA RI-OPT OUTPA JAN 1,2010 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 50

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 51

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 52

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

CVA RI-RX OUTPA PRESCRIPTI JAN 1,2010 YES RX COST YES

CHAMPVA REINS COST+5 OUTPA PRESCRIPTI DEC 31,2009 YES RX COST YES

CHAMPVA REIMB INS OUTPA OUTPATIENT DEC 18,2003 RC-OPT FAC 442 YES

RC-PHYSICIAN 442 YES

RC-PHYSICIAN 442GB YES

RC-PHYSICIAN 442GC YES

RC-PHYSICIAN 442GD YES

RC-PHYSICIAN 442X1 YES

CHAMPVA REIMB INS OUTPA OUTPATIENT DEC 19,2003 DEC 31,2009 RC-PHYSICIAN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 53

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN 442GB YES

RC-PHYSICIAN 442GC YES

RC-PHYSICIAN 442GD YES

RC-PHYSICIAN 442X1 YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS ML 442GC YES

RC-PHYSICIAN FS ML 442GD YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN OPT PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT FAC PR 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 54

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: CHOICE NO-FAULT AUTO

CCC-NF-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CCC-NF-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 55

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CCC-NF-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 56

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 57

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 58

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

CCC-NF-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CHOICE REIMB INS

CCC-RI-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 59

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CCC-RI-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

CCC-RI-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 60

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 61

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 62

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 63

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CCC-RI-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CHOICE TORT FEASOR

CCC-TF-INPT INPAT JAN 7,2004 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CCC-TF-SNF INPAT SKILLED NU JAN 7,2004 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 64

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CCC-TF-OPT OUTPA JAN 7,2004 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 65

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 66

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 67

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

CCC-TF-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CHOICE WORKERS' COMP

CCC-WC-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 68

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

CCC-WC-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

CCC-WC-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 69

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 70

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 71

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 72

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CCC-WC-RX OUTPA JAN 1,2018 RX COST YES

RATE TYPE: CRIME VICTIM

CV-INPT INPAT INPATIENT TL-INPT (NPF) YES

TL-INPT (PF) YES

CV-OPT OUTPA TL-OPT VST YES

TL-RX FILL YES

TL-OPT VST PM&RS

TL-OPT VST POLYTRAUMA

RATE TYPE: DENTAL

DNTL-OPT DENTAL OUTPA TL-OPT DENTAL YES

RATE TYPE: DENTAL REIMB. INS.

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 73

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

HR-OPT DENTAL OUTPA TL-OPT DENTAL YES

RATE TYPE: DOD BLIND REHABILITATION

DOD-BR-INPT INPAT INPATIENT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

DOD-BR-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 74

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

DOD-BR-OPT OUTPA OUTPATIENT DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 75

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 76

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 77

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE TYPE: DOD DISABILITY EVALUATION

DOD-DIS EXAM-OPT OUTPA OUTPATIENT DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 78

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 79

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 80

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 81

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE TYPE: DOD SPINAL CORD INJURY

DOD-SCI-INPT INPAT INPATIENT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

DOD-SCI-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 82

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN SNF MN 442 YES

DOD-SCI-OPT OUTPA OUTPATIENT DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 83

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 84

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 85

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE TYPE: DOD TRAUMATIC BRAIN INJURY

DOD-TBI-INPT INPAT INPATIENT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 86

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

DOD-TBI-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

DOD-TBI-OPT OUTPA OUTPATIENT DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 87

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 88

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 89

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 90

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: FEE REIMB INS

FR-INPT INPAT INPATIENT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

FR-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 91

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

FR-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 92

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 93

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

FR-RX OUTPA MAR 18,2011 RX COST YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 94

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: HUMANITARIAN

HMN-INPT INPAT INPATIENT TL-INPT (INCLUSIVE) YES

HMN-OPT OUTPA AUG 12,2013 TL-OPT VST YES

TL-RX FILL YES

TL-OPT VST PM&RS

TL-OPT VST POLYTRAUMA

HMN-RX OUTPA AUG 13,2013 DEC 31,2013 YES RX COST YES

HMN-OPT OUTPA AUG 13,2013 TL-OPT VST YES

TL-OPT VST PM&RS

TL-OPT VST POLYTRAUMA

HMN-RX OUTPA JAN 1,2014 DEC 31,2014 YES RX COST YES

HMN-RX OUTPA JAN 1,2015 DEC 31,2015 YES RX COST YES

HMN-RX OUTPA JAN 1,2016 DEC 31,2016 YES RX COST YES

HMN-RX OUTPA JAN 1,2017 DEC 31,2017 YES RX COST YES

HMN-RX OUTPA JAN 1,2018 YES RX COST YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 95

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: HUMANITARIAN REIMB. INS.

HR-INPT INPAT INPATIENT TL-INPT (INCLUSIVE) YES

HR-OPT OUTPA AUG 12,2013 TL-OPT VST YES

TL-RX FILL YES

TL-OPT VST PM&RS

TL-OPT VST POLYTRAUMA

HR-OPT OUTPA AUG 13,2013 TL-OPT VST YES

TL-OPT VST PM&RS

TL-OPT VST POLYTRAUMA

HR-RX OUTPA AUG 13,2013 DEC 31,2013 RX COST YES

HR-RX OUTPA JAN 1,2014 DEC 31,2014 RX COST YES

HR-RX OUTPA JAN 1,2015 DEC 31,2015 RX COST YES

HR-RX OUTPA JAN 1,2016 DEC 31,2016 RX COST YES

HR-RX OUTPA JAN 1,2017 RX COST YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 96

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: INELIGIBLE

INELIG-INPT INPAT INPATIENT TL-INPT (INCLUSIVE) YES

INELIG-OPT OUTPA OUTPATIENT AUG 12,2013 TL-OPT VST YES

TL-RX FILL YES

TL-OPT VST PM&RS

TL-OPT VST POLYTRAUMA

INELIG-RX OUTPA OUTPATIENT AUG 13,2013 DEC 31,2013 YES RX COST YES

INELIG-OPT OUTPA OUTPATIENT AUG 13,2013 TL-OPT VST YES

TL-OPT VST PM&RS

TL-OPT VST POLYTRAUMA

INELIG-RX OUTPA OUTPATIENT JAN 1,2014 DEC 31,2014 YES RX COST YES

INELIG-RX OUTPA OUTPATIENT JAN 1,2015 DEC 31,2015 YES RX COST YES

INELIG-RX OUTPA OUTPATIENT JAN 1,2016 DEC 31,2016 YES RX COST YES

INELIG-RX OUTPA OUTPATIENT JAN 1,2017 DEC 31,2017 YES RX COST YES

INELIG-RX OUTPA OUTPATIENT JAN 1,2018 YES RX COST YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 97

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: INELIGIBLE REIMB. INS.

IR-INPT INPAT INPATIENT TL-INPT (INCLUSIVE) YES

IR-OPT OUTPA AUG 12,2013 TL-OPT VST YES

TL-RX FILL YES

TL-OPT VST PM&RS

TL-OPT VST POLYTRAUMA

IR-OPT OUTPA AUG 13,2013 TL-OPT VST YES

TL-OPT VST PM&RS

TL-OPT VST POLYTRAUMA

IR-RX OUTPA AUG 13,2013 DEC 31,2013 RX COST YES

IR-RX OUTPA JAN 1,2014 DEC 31,2014 RX COST YES

IR-RX OUTPA JAN 1,2015 DEC 31,2015 RX COST YES

IR-RX OUTPA JAN 1,2016 DEC 31,2016 RX COST YES

IR-RX OUTPA JAN 1,2017 RX COST YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 98

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: INTERAGENCY

IA-INPT INPAT INPATIENT IA-INPT

IA-OPT OUTPA DEC 31,2013 IA-OPT VST

IA-RX FILL

IA-OPT VST PM&RS

IA-OPT VST POLYTRAUMA

IA-RX OUTPA JAN 1,2014 DEC 31,2014 YES RX COST YES

IA-OPT OUTPA JAN 1,2014 IA-OPT VST

IA-OPT VST PM&RS

IA-OPT VST POLYTRAUMA

IA-OPT DENTAL

IA-RX OUTPA JAN 1,2015 DEC 31,2015 YES RX COST YES

IA-RX OUTPA JAN 1,2016 DEC 31,2016 YES RX COST YES

IA-RX OUTPA JAN 1,2017 DEC 31,2017 YES RX COST YES

IA-RX OUTPA JAN 1,2018 YES RX COST YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 99

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: NO FAULT INS.

NF-INPT INPAT INPATIENT AUG 31,1999 TL-INPT (NPF) YES

TL-INPT (PF) YES

NF-INPT INPAT SEP 1,1999 DEC 18,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-SNF 442

RC-PHYSICIAN 442 YES

NF-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

NF-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 100

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

NF-OPT OUTPA AUG 31,1999 TL-OPT VST YES

TL-RX FILL YES

NF-OPT OUTPA SEP 1,1999 DEC 18,2003 RC-OPT FAC 442 YES

RC-PHYSICIAN 442 YES

RC-OPT FAC 442GB YES

RC-PHYSICIAN 442GB YES

RC-OPT FAC 442GC YES

RC-PHYSICIAN 442GC YES

RC-OPT FAC 442GD YES

RC-PHYSICIAN 442GD YES

RC-OPT FAC 442X1 YES

RC-PHYSICIAN 442X1 YES

NF-RX OUTPA SEP 1,1999 DEC 18,2003 TL-RX FILL YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 101

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

---------------------------------------------------------------------------------------------------------------------------------

NF-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 102

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 103

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 104

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

NF-RX OUTPA DEC 19,2003 MAR 17,2011 TL-RX FILL YES

NF-RX OUTPA MAR 18,2011 DEC 31,2011 YES RX COST YES

NF-RX OUTPA JAN 1,2012 DEC 31,2012 YES RX COST YES

NF-RX OUTPA JAN 1,2013 DEC 31,2013 YES RX COST YES

NF-RX OUTPA JAN 1,2014 DEC 31,2014 YES RX COST YES

NF-RX OUTPA JAN 1,2015 DEC 31,2015 YES RX COST YES

NF-RX OUTPA JAN 1,2016 DEC 31,2016 YES RX COST YES

NF-RX OUTPA JAN 1,2017 DEC 31,2017 YES RX COST YES

NF-RX OUTPA JAN 1,2018 YES RX COST YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 105

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: REIMBURSABLE INS.

RI-INPT INPAT INPATIENT AUG 31,1999 TL-INPT (NPF) YES

TL-INPT (PF) YES

RI-INPT INPAT SEP 1,1999 DEC 18,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-SNF 442

RC-PHYSICIAN 442 YES

RI-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

RI-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 106

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RI-OPT OUTPA AUG 31,1999 TL-OPT VST YES

TL-RX FILL YES

RI-OPT OUTPA SEP 1,1999 DEC 18,2003 RC-OPT FAC 442 YES

RC-PHYSICIAN 442 YES

RC-OPT FAC 442GB YES

RC-PHYSICIAN 442GB YES

RC-OPT FAC 442GC YES

RC-PHYSICIAN 442GC YES

RC-OPT FAC 442GD YES

RC-PHYSICIAN 442GD YES

RC-OPT FAC 442X1 YES

RC-PHYSICIAN 442X1 YES

RI-RX OUTPA PRESCRIPTI SEP 1,1999 DEC 18,2003 TL-RX FILL YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 107

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RI-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 108

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 109

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 110

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

--- -------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RI-RX OUTPA DEC 19,2003 MAR 17,2011 TL-RX FILL YES

RI-RX OUTPA MAR 18,2011 DEC 31,2011 YES RX COST YES

RI-RX OUTPA JAN 1,2012 DEC 31,2012 YES RX COST YES

RI-RX OUTPA JAN 1,2013 DEC 31,2013 YES RX COST YES

RI-RX OUTPA JAN 1,2014 DEC 31,2014 YES RX COST YES

RI-RX OUTPA JAN 1,2015 DEC 31,2015 YES RX COST YES

RI-RX OUTPA JAN 1,2016 DEC 31,2016 YES RX COST YES

RI-RX OUTPA JAN 1,2017 DEC 31,2017 YES RX COST YES

RI-RX OUTPA JAN 1,2018 YES RX COST YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 111

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RATE TYPE: SHARING AGREEMENT

SHARING AGREEMENT OUTPA OUTPATIENT YES CMAC 389 C1 WYO YES

CMAC 314 C1 COLO YES

CMAC 314 FAC/PHYS YES

CMAC 314 FAC/NONPHYS

CMAC 389 FAC/PHYS YES

CMAC 389 FAC/NONPHYS

CMAC 314 NONFAC/PHYS

CMAC 314 NONFAC/NONPHYS

CMAC 389 NONFAC/PHYS

CMAC 389 NONFAC/NONPHYS

RATE TYPE: TORT FEASOR

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 112

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

TF-INPT INPAT INPATIENT JAN 6,2004 TL-INPT (NPF) YES

TL-INPT (PF) YES

TF-INPT INPAT JAN 7,2004 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

TF-SNF INPAT SKILLED NU JAN 7,2004 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 113

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

TF-OPT OUTPA JAN 6,2004 TL-OPT VST YES

TL-RX FILL YES

TF-OPT OUTPA JAN 7,2004 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 114

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 115

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 116

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

TF-RX OUTPA JAN 7,2004 MAR 17,2011 TL-RX FILL YES

TF-RX OUTPA MAR 18,2011 DEC 31,2011 YES RX COST YES

TF-RX OUTPA JAN 1,2012 DEC 31,2012 YES RX COST YES

TF-RX OUTPA JAN 1,2013 DEC 31,2013 YES RX COST YES

TF-RX OUTPA JAN 1,2014 DEC 31,2014 YES RX COST YES

TF-RX OUTPA JAN 1,2015 DEC 31,2015 YES RX COST YES

TF-RX OUTPA JAN 1,2016 DEC 31,2016 YES RX COST YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 117

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

TF-RX OUTPA JAN 1,2017 DEC 31,2017 YES RX COST YES

TF-RX OUTPA JAN 1,2018 YES RX COST YES

RATE TYPE: TRICARE

TRICARE Inpt INPAT INPATIENT OCT 1,2005 DEC 31,2007 CMAC 389 FAC/NONPHYS YES

CMAC 389 FAC/PHYS YES

CMAC 389 NONFAC/NONPHYS YES

CMAC 389 NONFAC/PHYS YES

TR-INPT INPAT INPATIENT JAN 1,2008 RC-INPT ANC 442 YES

RC-INPT ANC ICU 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT FAC PR 442 YES

RC-INPT R&B 442 YES

RC-INPT R&B ICU 442 YES

RC-PHYSICIAN INPT MN 442 YES

RC-PHYSICIAN INPT PR 442 YES

TR-SNF INPAT SKILLED NU JAN 1,2008 RC-SNF FAC HR 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 118

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-SNF FAC ML 442 YES

RC-SNF FAC PR 442 YES

RC-SNF INC 442 YES

RC-PHYSICIAN SNF MN 442 YES

RC-PHYSICIAN SNF PR 442 YES

TR-RX OUTPA PRESCRIPTI JAN 1,2006 JAN 22,2012 YES RX COST YES

TR-RX OUTPA PRESCRIPTI JAN 23,2012 DEC 31,2013 YES RX COST YES

TR-RX OUTPA PRESCRIPTI JAN 1,2014 FEB 19,2015 YES RX COST YES

TR-RX OUTPA PRESCRIPTI FEB 20,2015 DEC 31,2015 YES RX COST YES

TR-RX OUTPA PRESCRIPTI JAN 1,2016 DEC 31,2016 YES RX COST YES

TR-RX OUTPA PRESCRIPTI JAN 1,2017 DEC 31,2017 YES RX COST YES

TRICARE Opt OUTPA OUTPATIENT DEC 31,2007 CMAC 389 C1 WYO YES

CMAC 389 C1 (PC) WYO

CMAC 389 C1 (TC) WYO

CMAC 389 C2 WYO

CMAC 389 C3&4 WYO

CMAC 389 C4 (PC) WYO

CMAC 314 C1 COLO YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 119

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CMAC 314 C1 (PC) COLO

CMAC 314 C1 (TC) COLO

CMAC 314 C2 COLO

CMAC 314 C3&4 COLO

CMAC 314 C4 (PC) COLO

CMAC 314 C4 (TC) COLO

CMAC 314 FAC/PHYS YES

CMAC 314 FAC/NONPHYS

CMAC 389 FAC/PHYS YES

CMAC 389 FAC/NONPHYS

CMAC 314 NONFAC/PHYS

CMAC 314 NONFAC/NONPHYS

CMAC 389 NONFAC/PHYS

CMAC 389 NONFAC/NONPHYS

TR-OPT OUTPA OUTPATIENT JAN 1,2008 RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT FAC PR 442 YES

RC-OPT MISC 442

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 120

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS ML 442GC YES

RC-PHYSICIAN FS ML 442GD YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

TR-RX OUTPA PRESCRIPTI JAN 1,2018 YES RX COST YES

RATE TYPE: TRICARE DENTAL

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 121

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

TR-DENTAL OUTPA OUTPATIENT DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 122

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 123

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 124

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

RATE TYPE: TRICARE PHARMACY

TR-PHARM OUTPA JAN 1,2018 RX COST YES

RATE TYPE: TRICARE REIMB. INS.

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 125

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

TRRI-INPT INPAT INPATIENT JAN 1,2008 RC-INPT ANC 442 YES

RC-INPT ANC ICU 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT FAC PR 442 YES

RC-INPT R&B 442 YES

RC-INPT R&B ICU 442 YES

RC-PHYSICIAN INPT MN 442 YES

RC-PHYSICIAN INPT PR 442 YES

TRRI-SNF INPAT SKILLED NU JAN 1,2008 RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-SNF FAC PR 442 YES

RC-SNF INC 442 YES

RC-PHYSICIAN SNF MN 442 YES

RC-PHYSICIAN SNF PR 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 126

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

TRRI-RX OUTPA PRESCRIPTI JAN 1,2006 JAN 22,2012 YES RX COST YES

TRRI-RX OUTPA PRESCRIPTI JAN 23,2012 DEC 31,2013 YES RX COST YES

TRRI-RX OUTPA PRESCRIPTI JAN 1,2014 FEB 19,2015 YES RX COST YES

TRRI-RX OUTPA PRESCRIPTI FEB 20,2015 DEC 31,2015 YES RX COST YES

TRRI-RX OUTPA PRESCRIPTI JAN 1,2016 DEC 31,2016 YES RX COST YES

TRRI-RX OUTPA PRESCRIPTI JAN 1,2017 DEC 31,2017 YES RX COST YES

TRICARE Ins Opt OUTPA OUTPATIENT DEC 31,2007 CMAC 389 C1 WYO YES

CMAC 389 C1 (PC) WYO

CMAC 389 C1 (TC) WYO

CMAC 389 C2 WYO

CMAC 389 C3&4 WYO

CMAC 389 C4 (PC) WYO

CMAC 389 C4 (TC) WYO

CMAC 314 C1 (PC) COLO

CMAC 314 C1 COLO YES

CMAC 314 C1 (TC) COLO

CMAC 314 C2 COLO

CMAC 314 C3&4 COLO

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 127

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

CMAC 314 C4 (PC) COLO

CMAC 314 C4 (TC) COLO

CMAC 314 FAC/PHYS YES

CMAC 314 FAC/NONPHYS

CMAC 389 FAC/PHYS YES

CMAC 389 FAC/NONPHYS

CMAC 314 NONFAC/PHYS

CMAC 314 NONFAC/NONPHYS

CMAC 389 NONFAC/PHYS

CMAC 389 NONFAC/NONPHYS

TRRI-OPT OUTPA OUTPATIENT JAN 1,2008 RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT FAC PR 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN OPT PR 442 YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS ML 442GC YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 128

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN FS ML 442GD YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

TRRI-RX OUTPA PRESCRIPTI JAN 1,2018 YES RX COST YES

RATE TYPE: WORKERS' COMP.

WC-INPT INPAT INPATIENT AUG 31,1999 TL-INPT (NPF) YES

TL-INPT (PF) YES

WC-INPT INPAT SEP 1,1999 DEC 18,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RC-SNF 442

RC-PHYSICIAN 442 YES

WC-INPT INPAT DEC 19,2003 RC-INPT R&B 442 YES

RC-INPT ANC 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 129

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-INPT FAC PR 442 YES

RC-INPT FAC HR 442 YES

RC-INPT FAC ML 442 YES

RC-INPT R&B ICU 442 YES

RC-INPT ANC ICU 442 YES

RC-PHYSICIAN INPT PR 442 YES

RC-PHYSICIAN INPT MN 442 YES

WC-SNF INPAT SKILLED NU DEC 19,2003 RC-SNF INC 442 YES

RC-SNF FAC PR 442 YES

RC-SNF FAC HR 442 YES

RC-SNF FAC ML 442 YES

RC-PHYSICIAN SNF PR 442 YES

RC-PHYSICIAN SNF MN 442 YES

WC-OPT OUTPA AUG 31,1999 TL-OPT VST YES

TL-RX FILL YES

WC-OPT OUTPA SEP 1,1999 DEC 18,2003 RC-OPT FAC 442 YES

RC-PHYSICIAN 442 YES

RC-OPT FAC 442GB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 130

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN 442GB YES

RC-OPT FAC 442GC YES

RC-PHYSICIAN 442GC YES

RC-OPT FAC 442GD YES

RC-PHYSICIAN 442GD YES

RC-OPT FAC 442X1 YES

RC-PHYSICIAN 442X1 YES

WC-RX OUTPA SEP 1,1999 DEC 18,2003 TL-RX FILL YES

WC-OPT OUTPA DEC 19,2003 RC-PHYSICIAN FS PR 442GB YES

RC-PHYSICIAN FS PR 442GC YES

RC-PHYSICIAN FS PR 442GD YES

RC-PHYSICIAN FS MN 442GD YES

RC-PHYSICIAN FS ML 442GD YES

RC-OPT FAC PR 442 YES

RC-OPT FAC HR 442 YES

RC-OPT FAC ML 442 YES

RC-OPT MISC 442

RC-PHYSICIAN OPT PR 442 YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 131

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-PHYSICIAN OPT MN 442 YES

RC-PHYSICIAN FS MN 442GB YES

RC-PHYSICIAN FS ML 442GB YES

RC-PHYSICIAN FS MN 442GC YES

RC-PHYSICIAN FS ML 442GC YES

RC-OPT FAC PR 442GD YES

RC-OPT FAC HR 442GD YES

RC-OPT FAC ML 442GD YES

RC-OPT MISC 442GD

RC-PHYSICIAN OPT PR 442GD YES

RC-PHYSICIAN OPT MN 442GD YES

RC-OPT FAC PR 442GC YES

RC-OPT FAC HR 442GC YES

RC-OPT FAC ML 442GC YES

RC-OPT MISC 442GC

RC-PHYSICIAN OPT PR 442GC YES

RC-PHYSICIAN OPT MN 442GC YES

RC-OPT FAC PR 442HK YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 132

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

RC-OPT FAC HR 442HK YES

RC-OPT FAC ML 442HK YES

RC-OPT MISC 442HK

RC-PHYSICIAN OPT PR 442HK YES

RC-PHYSICIAN OPT MN 442HK YES

RC-OPT FAC PR 442GB YES

RC-OPT FAC HR 442GB YES

RC-OPT FAC ML 442GB YES

RC-OPT MISC 442GB

RC-PHYSICIAN OPT PR 442GB YES

RC-PHYSICIAN OPT MN 442GB YES

RC-OPT FAC PR 442MA YES

RC-OPT FAC HR 442MA YES

RC-OPT FAC ML 442MA YES

RC-OPT MISC 442MA

RC-PHYSICIAN OPT PR 442MA YES

RC-PHYSICIAN OPT MN 442MA YES

RC-PHYSICIAN FS PR 442QB YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 133

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

------------- --------------------------------------------------------------------------------------------------------

RC-PHYSICIAN FS MN 442QB YES

RC-PHYSICIAN FS ML 442QB YES

RC-PHYSICIAN FS PR 442QA YES

RC-PHYSICIAN FS MN 442QA YES

RC-PHYSICIAN FS ML 442QA YES

RC-OPT FAC PR 442QA YES

RC-OPT FAC HR 442QA YES

RC-OPT FAC ML 442QA YES

RC-OPT MISC 442QA

RC-PHYSICIAN OPT PR 442QA YES

RC-PHYSICIAN OPT MN 442QA YES

RC-OPT FAC PR 442QB YES

RC-OPT FAC HR 442QB YES

RC-OPT FAC ML 442QB YES

RC-OPT MISC 442QB

RC-PHYSICIAN OPT PR 442QB YES

RC-PHYSICIAN OPT MN 442QB YES

WC-RX OUTPA DEC 19,2003 MAR 17,2011 TL-RX FILL YES

RATE SCHEDULE List OCT 25, 2018@17:16 PAGE 134

BILL BILL EFFECTIVE INACTIVE CHARGES AUTO

NAME TYPE SERVICE DATE DATE ADJUSTED CHARGE SET ADD

-----------------------------------------------------------------------------------------------------------------------

WC-RX OUTPA MAR 18,2011 DEC 31,2011 YES RX COST YES

WC-RX OUTPA JAN 1,2012 DEC 31,2012 YES RX COST YES

WC-RX OUTPA JAN 1,2013 DEC 31,2013 YES RX COST YES

WC-RX OUTPA JAN 1,2014 DEC 31,2014 YES RX COST YES

WC-RX OUTPA JAN 1,2015 DEC 31,2015 YES RX COST YES

WC-RX OUTPA JAN 1,2016 DEC 31,2016 YES RX COST YES

WC-RX OUTPA JAN 1,2017 DEC 31,2017 YES RX COST YES

WC-RX OUTPA JAN 1,2018 YES RX COST YES

BILLING RATE LIST

----------------------------------------------------------------

BILLING RATE List OCT 25, 2018@17:26 PAGE 1

CHARGE

NAME ABBREVIATION DISTRIBUTION BILLABLE ITEM METHOD

-----------------------------------------------------------------------------------

INTERAGENCY IA NATIONAL BEDSECTION COUNT

RC FACILITY HR RC F/HR NATIONAL CPT HOURS

RC FACILITY ML RC F/ML NATIONAL CPT MILES

RC FACILITY PER DIEM RC F/PD NATIONAL BEDSECTION COUNT

RC FACILITY PR RC F/PR NATIONAL CPT COUNT

RC INPATIENT FACILITY RC INPT NATIONAL DRG COUNT

RC MISCELLANEOUS RC MISC NATIONAL MISCELLANEOUS COUNT

RC PHYSICIAN ML RC P/ML NATIONAL CPT MILES

RC PHYSICIAN MN RC P/MN NATIONAL CPT MINUTES

RC PHYSICIAN PR RC P/PR NATIONAL CPT COUNT

RC SKILLED NURSING/SUB-ACUTE RC SN/SA NATIONAL MISCELLANEOUS COUNT

TORTIOUSLY LIABLE TORT NATIONAL BEDSECTION COUNT

TORTIOUSLY LIABLE MISC TORT MIS NATIONAL MISCELLANEOUS COUNT

TP INPATIENT TP INPT NATIONAL DRG COUNT

TP OUTPATIENT TP OPT NATIONAL CPT COUNT

VA COST VA COST NATIONAL VA COST

AMBULATORY SURGERY ASC LOCAL CPT COUNT

AVERAGE WHOLESALE PRICE AWP LOCAL NDC \# QUANTITY

CMAC CMAC LOCAL CPT COUNT

SHARING AGREEMENT SHARING LOCAL CPT COUNT

Charge Set ListCHARGE SET List OCT 25, 2018@17:19 PAGE 1

DEFAULT

REVENUE DEFAULT

NAME BILLABLE EVENT CHARGE TYPE CODE BEDSECTION REGION

--------------------------------------------------------------------------------------

BILLING RATE: CMAC

CMAC 314 FAC/PHYS PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI CMAC 314

CMAC 314 FAC/NONPHYS PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI CMAC 314

CMAC 389 FAC/PHYS PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI CMAC 389

CMAC 389 FAC/NONPHYS PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI CMAC 389

CMAC 314 NONFAC/PHYS PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI CMAC 314

CMAC 314 NONFAC/NONPHYS PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI CMAC 314

CMAC 389 NONFAC/PHYS PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI CMAC 389

CMAC 389 NONFAC/NONPHYS PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI CMAC 389

CMAC 389 C1 WYO PROCEDURE 510 UTPATIENT VISI REGION 389

CMAC 389 C2 WYO PROCEDURE 510 OUTPATIENT VISI REGION 389

CMAC 389 C3&4 WYO PROCEDURE 510 OUTPATIENT VISI REGION 389

CMAC 389 C1 (PC) WYO PROCEDURE 510 OUTPATIENT VISI REGION 389

CMAC 389 C1 (TC) WYO PROCEDURE 510 OUTPATIENT VISI REGION 389

CMAC 389 C4 (PC) WYO PROCEDURE 510 OUTPATIENT VISI REGION 389

CMAC 389 C4 (TC) WYO PROCEDURE 510 OUTPATIENT VISI REGION 389

CMAC 314 C1 COLO PROCEDURE 510 OUTPATIENT VISI REGION 314

CMAC 314 C1 (PC) COLO PROCEDURE 510 OUTPATIENT VISI REGION 314

CMAC 314 C1 (TC) COLO PROCEDURE 510 OUTPATIENT VISI REGION 314

CMAC 314 C2 COLO PROCEDURE 510 OUTPATIENT VISI REGION 314

CMAC 314 C3&4 COLO PROCEDURE 510 OUTPATIENT VISI REGION 314

CMAC 314 C4 (PC) COLO PROCEDURE 510 OUTPATIENT VISI REGION 314

CMAC 314 C4 (TC) COLO PROCEDURE 510 OUTPATIENT VISI REGION 314

BILLING RATE: INTERAGENCY

IA-INPT INPATIENT BEDSECTION STAY 001 GENERAL MEDICAL

IA-OPT VST OUTPATIENT VISIT DATE 510

IA-OPT DENTAL OUTPATIENT VISIT DATE 512

IA-OPT VST PM&RS OUTPATIENT VISIT DATE 500

IA-OPT VST POLYTRAUMA OUTPATIENT VISIT DATE 500

IA-RX FILL PRESCRIPTION FILL 250

BILLING RATE: RC FACILITY HR

RC-INPT FAC HR 442 PROCEDURE INSTITUTIONAL 240 GENERAL MEDICAL RC 442 - ANYTOWN, WY

RC-SNF FAC HR 442 PROCEDURE INSTITUTIONAL 240 SKILLED NURSING RC 442 - ANYTOWN, WY

RC-OPT FAC HR 442 PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442 - ANYTOWN, WY

RC-OPT FAC HR 442GD PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GD - ANYTOWN, CO

RC-OPT FAC HR 442GC PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GC - ANYTOWN, CO

RC-OPT FAC HR 442HK PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442HK - ANYTOWN, MOC, WY

RC-OPT FAC HR 442GB PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GB - ANYTOWN, NE

RC-OPT FAC HR 442MA PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442MA - ANYTOWN, WY (DE

RC-OPT FAC HR 442QA PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442QA - RAWLINS VA CLINIC,

RC-OPT FAC HR 442QB PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442QB - TORRINGTON VA MOBIL

BILLING RATE: RC FACILITY ML

RC-INPT FAC ML 442 PROCEDURE INSTITUTIONAL 240 GENERAL MEDICAL RC 442 - ANYTOWN, WY

RC-SNF FAC ML 442 PROCEDURE INSTITUTIONAL 240 SKILLED NURSING RC 442 - ANYTOWN, WY

RC-OPT FAC ML 442 PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442 - ANYTOWN, WY

RC-OPT FAC ML 442GD PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GD - ANYTOWN, CO

RC-OPT FAC ML 442GC PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GC - ANYTOWN, CO

RC-OPT FAC ML 442HK PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442HK - ANYTOWN MOC, WY

RC-OPT FAC ML 442GB PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GB - ANYTOWN, NE

RC-OPT FAC ML 442MA PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442MA - ANYTOWN, WY (DE

RC-OPT FAC ML 442QA PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442QA - RAWLINS VA CLINIC,

RC-OPT FAC ML 442QB PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442QB - TORRINGTON VA MOBIL

BILLING RATE: RC FACILITY PER DIEM

RC-SNF INC 442 INPATIENT BEDSECTION STAY INSTITUTIONAL 101 SKILLED NURSING RC 442 - ANYTOWN, WY

BILLING RATE: RC FACILITY PR

RC-OPT FAC 442 PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442 - ANYTOWN, WY

RC-OPT FAC 442GB PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GB - ANYTOWN, NE

RC-OPT FAC 442GC PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GC - ANYTOWN, CO

RC-OPT FAC 442GD PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GD - ANYTOWN, CO

RC-OPT FAC 442X1 PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442X1 - ANYTOWN, NE

RC-INPT FAC PR 442 PROCEDURE INSTITUTIONAL 240 GENERAL MEDICAL RC 442 - ANYTOWN, WY

RC-SNF FAC PR 442 PROCEDURE INSTITUTIONAL 240 SKILLED NURSING RC 442 - ANYTOWN, WY

RC-OPT FAC PR 442 PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442 - ANYTOWN, WY

RC-OPT FAC PR 442GD PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GD - ANYTOWN, CO

RC-OPT FAC PR 442GC PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GC - ANYTOWN, CO

RC-OPT FAC PR 442HK PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442HK - ANYTOWN MOC, WY

RC-OPT FAC PR 442GB PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442GB - ANYTOWN, NE

RC-OPT FAC PR 442MA PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442MA - ANYTOWN, WY (DE

RC-OPT FAC PR 442QA PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442QA - RAWLINS VA CLINIC,

RC-OPT FAC PR 442QB PROCEDURE INSTITUTIONAL 510 OUTPATIENT VISI RC 442QB - TORRINGTON VA MOBIL

BILLING RATE: RC INPATIENT FACILITY

RC-INPT R&B 442 INPATIENT DRG INSTITUTIONAL 101 GENERAL MEDICAL RC 442 - ANYTOWN, WY

RC-INPT ANC 442 INPATIENT DRG INSTITUTIONAL 240 GENERAL MEDICAL RC 442 - ANYTOWN, WY

RC-INPT R&B ICU 442 INPATIENT DRG INSTITUTIONAL 200 ICU RC 442 - ANYTOWN, WY

RC-INPT ANC ICU 442 INPATIENT DRG INSTITUTIONAL 240 ICU RC 442 - ANYTOWN, WY

BILLING RATE: RC MISCELLANEOUS

RC-OPT MISC 442 UNASSOCIATED INSTITUTIONAL 912 PARTIAL HOSPITA RC 442 - ANYTOWN, WY

RC-OPT MISC 442GD UNASSOCIATED INSTITUTIONAL 912 PARTIAL HOSPITA RC 442GD - ANYTOWN, CO

RC-OPT MISC 442GC UNASSOCIATED INSTITUTIONAL 912 PARTIAL HOSPITA RC 442GC - ANYTOWN, CO

RC-OPT MISC 442HK UNASSOCIATED INSTITUTIONAL 912 PARTIAL HOSPITA RC 442HK - ANYTOWN MOC, WY

RC-OPT MISC 442GB UNASSOCIATED INSTITUTIONAL 912 PARTIAL HOSPITA RC 442GB - ANYTOWN, NE

RC-OPT MISC 442MA UNASSOCIATED INSTITUTIONAL 912 PARTIAL HOSPITA RC 442MA - ANYTOWN, WY (DE

RC-OPT MISC 442QA UNASSOCIATED INSTITUTIONAL 912 PARTIAL HOSPITA RC 442QA - RAWLINS VA CLINIC,

RC-OPT MISC 442QB UNASSOCIATED INSTITUTIONAL 912 PARTIAL HOSPITA RC 442QB - TORRINGTON VA MOBIL

BILLING RATE: RC PHYSICIAN ML

RC-PHYSICIAN FS ML 442GD PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GD - ANYTOWN, CO

RC-PHYSICIAN FS ML 442GB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GB - ANYTOWN, NE

RC-PHYSICIAN FS ML 442GC PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GC - ANYTOWN, CO

RC-PHYSICIAN FS ML 442QB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442QB - TORRINGTON VA MOBIL

RC-PHYSICIAN FS ML 442QA PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442QA - RAWLINS VA CLINIC,

BILLING RATE: RC PHYSICIAN MN

RC-PHYSICIAN FS MN 442GD PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GD - ANYTOWN, CO

RC-PHYSICIAN INPT MN 442 PROCEDURE PROFESSIONAL 960 GENERAL MEDICAL RC 442 - ANYTOWN, WY

RC-PHYSICIAN SNF MN 442 PROCEDURE PROFESSIONAL 960 SKILLED NURSING RC 442 - ANYTOWN, WY

RC-PHYSICIAN OPT MN 442 PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442 - ANYTOWN, WY

RC-PHYSICIAN FS MN 442GB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GB - ANYTOWN, NE

RC-PHYSICIAN FS MN 442GC PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GC - ANYTOWN, CO

RC-PHYSICIAN OPT MN 442GD PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GD - ANYTOWN, CO

RC-PHYSICIAN OPT MN 442GC PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GC - ANYTOWN, CO

RC-PHYSICIAN OPT MN 442HK PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442HK - CHEYENNE MOC, WY

RC-PHYSICIAN OPT MN 442GB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GB - ANYTOWN, NE

RC-PHYSICIAN OPT MN 442MA PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442MA - ANYTOWN, WY (DE

RC-PHYSICIAN FS MN 442QB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442QB - TORRINGTON VA MOBIL

RC-PHYSICIAN FS MN 442QA PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442QA - RAWLINS VA CLINIC,

RC-PHYSICIAN OPT MN 442QA PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442QA - RAWLINS VA CLINIC,

RC-PHYSICIAN OPT MN 442QB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442QB - TORRINGTON VA MOBIL

BILLING RATE: RC PHYSICIAN PR

RC-PHYSICIAN 442 PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442 - ANYTOWN, WY

RC-PHYSICIAN 442GB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GB - ANYTOWN, NE

RC-PHYSICIAN 442GC PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GC - ANYTOWN, CO

RC-PHYSICIAN 442GD PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GD - ANYTOWN, CO

RC-PHYSICIAN 442X1 PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442X1 - ANYTOWN, NE

RC-PHYSICIAN FS PR 442GB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GB - ANYTOWN, NE

RC-PHYSICIAN FS PR 442GC PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GC - ANYTOWN, CO

RC-PHYSICIAN FS PR 442GD PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GD - ANYTOWN, CO

RC-PHYSICIAN INPT PR 442 PROCEDURE PROFESSIONAL 960 GENERAL MEDICAL RC 442 - ANYTOWN, WY

RC-PHYSICIAN SNF PR 442 PROCEDURE PROFESSIONAL 960 SKILLED NURSING RC 442 - ANYTOWN, WY

RC-PHYSICIAN OPT PR 442 PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442 - ANYTOWN, WY

RC-PHYSICIAN OPT PR 442GD PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GD - ANYTOWN, CO

RC-PHYSICIAN OPT PR 442GC PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GC - ANYTOWN, CO

RC-PHYSICIAN OPT PR 442HK PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442HK - ANYTOWN, WY

RC-PHYSICIAN OPT PR 442GB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442GB - ANYTOWN, NE

RC-PHYSICIAN OPT PR 442MA PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442MA - ANYTOWN, WY (DE

RC-PHYSICIAN FS PR 442QB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442QB - TORRINGTON VA MOBIL

RC-PHYSICIAN FS PR 442QA PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442QA - RAWLINS VA CLINIC,

RC-PHYSICIAN OPT PR 442QA PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442QA - RAWLINS VA CLINIC,

RC-PHYSICIAN OPT PR 442QB PROCEDURE PROFESSIONAL 510 OUTPATIENT VISI RC 442QB - TORRINGTON VA MOBIL

BILLING RATE: RC SKILLED NURSING/SUB-ACUTE

RC-SNF 442 UNASSOCIATED INSTITUTIONAL 100 SKILLED NURSING RC 442 - ANYTOWN, WY

BILLING RATE: TORTIOUSLY LIABLE

TL-INPT (INCLUSIVE) INPATIENT BEDSECTION STAY 001

TL-INPT (NPF) INPATIENT BEDSECTION STAY 240

TL-INPT (PF) INPATIENT BEDSECTION STAY 960

TL-OPT VST OUTPATIENT VISIT DATE 510

TL-OPT DENTAL OUTPATIENT VISIT DATE 512

TL-OPT VST PM&RS OUTPATIENT VISIT DATE 500

TL-OPT VST POLYTRAUMA OUTPATIENT VISIT DATE 500

TL-X FILL PRESCRIPTION FILL 250 PRESCRIPTIO

BILLING RATE: TORTIOUSLY LIABLE MISC

TL-MT OPT COPAY UNASSOCIATED 510

BILLING RATE: TP INPATIENT

TP-INPT INPATIENT DRG TP 442 ANYTOWN, WY

BILLING RATE: TP OUTPATIENTTP-OPT 666 PROCEDURE TP 666 ANYTOWN, WY

TP-OPT PROCEDURE TP 442 ANYTOWN, WY

BILLING RATE: VA COST RX COST PRESCRIPTION FILL 250 RESCRIPTION

PI COST PROSTHETICS ITEM 274 OUTPATIENT VISI

Billing Region ListBILLING REGION List OCT 25, 2018@17:28 PAGE 1

REGION DIVISION

----------------------------------------------------------------

CMAC 314 FORT COLLINS

GREELEY

CHEYENNE MOC

CMAC 389 CHEYENNE VAMROC

RC 442 - ANYTOWN, WY CHEYENNE VAMROC

RC 442GB - ANYTOWN, NE SIDNEY

RC 442GC - ANYTOWN, CO FORT COLLINS

RC 442GD - ANYTOWN, CO GREELEY

RC 442HK - ANYTOWN MOC, WY CHEYENNE MOC

RC 442MA - ANYTOWN, WY (DE IDES - F.E. WARREN AFB

RC 442QA - RAWLINS VA CLINIC, RAWLINS

RC 442QB - TORRINGTON VA MOBIL

RC 442X1 - ANYTOWN, NE

REGION 314 FORT COLLINS

GREELEY

CHEYENNE MOC

REGION 389 CHEYENNE VAMROC

TP 442 ANYTOWN, WY

TP 666 ANYTOWN, WY

### Print Charge Master

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides reports for all elements of the Charge Master and maintenance of Third-Party rates. The full Charge Item report could be lengthy if many items have been added, such as CMAC (CHAMPUS Maximum Allowable Charges) charges.

Sample Output

RATE TYPE LIST MAY 27,1997 08:48 PAGE 1

NSC

THIRD STATEMENT

PARTY ACCOUNTS RECEIVABLE WHO'S REIMB ON UB

NAME BILL NAME INACTIVE ABBREVIATION BILL? CATEGORY RESPONSIBLE INS? BILLS

--------------------------------------------------------------------------------------------------------------------------------

CHAMPUS CHAMPUS CHAMPUS YES CHAMPUS INSURER YES YES

CHAMPVA REIMB. INS. REIMBURSABLE INS. REIM INS YES CHAMPVA THIRD PARTY INSURER YES YES

CRIME VICTIM THIRD PARTY CRIME YES CRIME OF PER.VIO. INSURER NO YES

DENTAL DENTAL DENTAL NO EMERGENCY/HUMANITARI PATIENT YES YES

HUMANITARIAN HUMANITARIAN HUMAN NO EMERGENCY/HUMANITARI PATIENT NO NO

INTERAGENCY INTERAGENCY INTER YES INTERAGENCY OTHER (INST YES

MEANS TEST/CAT. C MEANS TEST/CAT. C NO MT/CAT C NO C (MEANS TEST) PATIENT NO YES

MEDICARE ESRD MEDICARE ESRD MEDICARE YES INTERAGENCY OTHER (INST NO YES

MILITARY MILITARY NO MIL YES INTERAGENCY OTHER (INST YES

NO FAULT INS. NO FAULT INS. NO FAULT YES REIMBURS.HEALTH INS. INSURER NO YES

REIMBURSABLE INS. REIMBURSABLE INS. REIM INS YES REIMBURS.HEALTH INS. INSURER YES YES

SHARING AGREEMENT SHARING AGREEMENT SHARING YES SHARING AGREEMENTS OTHER (INST YES

### Activate Revenue Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Activate Revenue Codes option allows sites to activate revenue codes used for third-party billing.

The revenue codes are provided by the National Uniform Billing Committee. The full set of 999 codes is sent to each site. All codes have an INACTIVE status when received. The site chooses which codes to use for billing purposes by activating the codes through this option. Some of the codes are reserved for national assignment (no definition yet). These reserve codes cannot be activated. Only activated revenue codes may be selected during the billing process.

Adding or deleting codes from the REVENUE CODE file is NOT allowed.

### Enter / Edit Billing Rates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit Billing Rates option is used to edit billing rates for per diem rates; the Medicare deductible (this is the only place the Medicare deductible is entered); the HCFA ambulatory surgery rates, pharmacy copayment amounts, and CHAMPVA subsistence rates that are used in the automatic calculation of costs when preparing a third-party bill.

Although the option allows entry of new rates, it should only be used for editing and for the entry of duplicate rates. Duplicate rates are those where two different rates are used for the same revenue code/bed section/effective date dependent on the payor. All other new billing rates should be entered through the Fast Enter New Billing Rates option.

If YES is answered at the NON-STANDARD RATE prompt, that billing rate will only be used with insurance companies where the selected revenue code has been listed in the DIFFERENT REVENUE CODES TO USE field of the INSURANCE COMPANY file.

The user may enter an additional amount as well as the basic amount to be charged for all rates. This is a fixed additional dollar amount that will be added to the basic charge after it has been computed. An example would be the additional charge of \$200 added to HCFA Ambulatory Surgery rate groups for inter-ocular lens implants.

Accuracy in entering billing rates is critical. Incorrect entries will result in erroneous bills. After new rates are entered, it is suggested to print the Billing Rates List (Billing Rates List option on the Management Reports Menu) and verify that all entries are correctly recorded.

### Flag Stop Codes / Dispositions / Clinics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient encounters recorded in the Scheduling package as either registrations or stand-alone stop codes will be billed automatically as those events are checked out. The Flag Stop Codes/Dispositions/Clinics option is used to flag/unflag those stop codes and dispositions that should not be billed. The option may also be used to flag clinics where Means Test billing is not appropriate.

If the user makes more than one selection, an opportunity to review the selections and deselect any, if necessary. All selections will be assigned the same effective date and billable status.

16. Once a selection has been flagged as non-billable, it may later be flagged as billable if it is subsequently determined it would be appropriate to continue billing.

### Flag Stop Codes / Clinics for Third-Party

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Non-billable* stop codes or clinics are those that should not be billed to a Third-Party payer. By default, if a stop code or clinic is non-billable, it will not be billed by the auto biller; and therefore, is non-auto billable.

*Non-auto billable* stop codes or clinics are those that may be billable to a Third-Party payer, but the auto biller should not be used for billing. These are visits that need more research than can be performed by the auto biller to determine if billable.

These parameters are flagged by date, may be inactivated, and reactivated.

### Insurance Company Entry / Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Insurance Company Entry/Edit option is used to enter new insurance companies into the INSURANCE COMPANY file and edit data on existing companies. An insurance company must be in the INSURANCE COMPANY file before it can be entered into a patient's record.

When entering new insurance companies, the user will be prompted for the company street address, city, and whether the company will reimburse for treatment.

The following sections are lists of the actions found on the screen in this option and a brief description of each. Once an action has been selected, \<??\> may be entered at most of the prompts that appear for lists of acceptable responses or instructions on how to respond.

#### Insurance Company Editor Screen

Once the insurance company is selected, this screen is displayed listing the following groups of information for that company: billing parameters, main mailing address, inpatient claims office data, outpatient claims office data, prescription claims office data, appeals office data, inquiry office data, remarks, and synonyms.

<table>
<caption><p><span id="_Toc143780860" class="anchor"></span>Table : Common Actions</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 24%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym</th>
<th>Description</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BP</td>
<td>Billing Parameters</td>
<td>Allows the user to add / edit the billing parameters for the selected insurance company.</td>
</tr>
<tr class="even">
<td>MM</td>
<td>Main Mailing Address</td>
<td>Allows the user to add / edit the company's main mailing address. The address entered here will automatically be entered for the other office addresses.</td>
</tr>
<tr class="odd">
<td>IC</td>
<td>Inpt Claims Office</td>
<td>Allows the user to add / edit the company's inpatient claims office name, address, phone, and fax numbers.</td>
</tr>
<tr class="even">
<td>OC</td>
<td>Opt Claims Office</td>
<td>Allows the user to add / edit the company's outpatient claims office name, address, phone, and fax numbers.</td>
</tr>
<tr class="odd">
<td>PC</td>
<td>Prescr Claims Of</td>
<td>Allows the user to add / edit the company's prescription claims office name, address, phone, and fax numbers.</td>
</tr>
<tr class="even">
<td>AO</td>
<td>Appeals Office</td>
<td>Allows the user to add / edit the company's appeals office name, address, phone, and fax numbers.</td>
</tr>
<tr class="odd">
<td>IO</td>
<td>Inquiry Office</td>
<td>Allows the user to add / edit the company's inquiry office name, address, phone, and fax numbers.</td>
</tr>
<tr class="even">
<td>RE</td>
<td>Remarks</td>
<td>Allows the user to enter comments concerning the selected insurance company.</td>
</tr>
<tr class="odd">
<td>SY</td>
<td>Synonyms</td>
<td>Allows the user to add / edit any synonyms for the selected company.</td>
</tr>
<tr class="even">
<td>EA</td>
<td>Edit All</td>
<td>Lists editable fields line by line for quick data entry.</td>
</tr>
<tr class="odd">
<td>IA</td>
<td>(In)Activate Company</td>
<td><p>Allows the user to activate / inactivate the selected insurance company. This may be used to inactivate duplicate companies in the system. When an insurance company is no longer valid, it is important to inactivate the company rather than delete it from the system. The IB INSURANCE SUPERVISOR security key is required. Once a company has been inactivated, it may not be selected when entering billing information.</p>
<p>The user may also obtain a report of patients insured by a given company through this action.</p></td>
</tr>
<tr class="even">
<td>CC</td>
<td>Change Insurance Co.</td>
<td>Allows the user to change to another company without returning to the beginning of the option.</td>
</tr>
<tr class="odd">
<td>DC</td>
<td>Delete Company</td>
<td>Allows the user to delete an entry from the Insurance Company (#36) file. If claims have been submitted to the company, another company must be selected in which to point all claims and receivables information.</td>
</tr>
<tr class="even">
<td>PL</td>
<td>Plans (accesses Insurance Plan List screen)</td>
<td>Allows the user to display and change plan attributes associated with the insurance company.</td>
</tr>
</tbody>
</table>

<span id="_Toc143780860" class="anchor"></span>Table : Common Actions

#### Insurance Plan List Screen

This screen lists all plans (active and inactive, group and individual) for the selected insurance company.

| Acronym | Description                                                | Action                                                                                                                  |
|---------|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| VP      | View/Edit Plan (accesses the View/Edit Plan screen)        | Allows the user to display / change plan detailed information.                                                          |
| IP      | Inactive Plan                                              | Allows the user to inactivate an insurance plan or move subscribers from multiple insurance plans into one master plan. |
| AB      | Annual Benefits - (accesses Annual Benefits Editor screen) | Used to enter annual benefits data for the selected policy.                                                             |

<span id="_Toc143780861" class="anchor"></span>Table : Common Actions

#### Annual Benefits Editor Screen

Once the benefit year is selected, this screen is displayed listing all the benefits for the selected insurance policy and benefit year. Benefit categories may include inpatient benefits, outpatient benefits, mental health, home health care, hospice, rehabilitation, and IV management.

| Acronym | Description        | Action                                                                       |
|---------|--------------------|------------------------------------------------------------------------------|
| PI      | Policy Information | Allows entry / edit of maximum out-of-pocket and ambulance coverage.         |
| IP      | Inpatient          | Allows entry / edit of inpatient benefits data.                              |
| OP      | Outpatient         | Allows entry / edit of outpatient benefits data.                             |
| MH      | Mental Health      | Allows entry / edit of mental health inpatient and outpatient benefits data. |
| HH      | Home Health        | Allows entry / edit of home health care benefits data.                       |
| HS      | Hospice            | Allows entry / edit of hospice benefits data.                                |
| RH      | Rehab              | Allows entry / edit of rehabilitation benefits data.                         |
| IV      | IV Mgmt.           | Allows entry / edit of intravenous management benefits data.                 |
| EA      | Edit All           | Lists editable fields line by line for quick data entry.                     |
| CY      | Change Year        | Allows the user to change to another benefit year.                           |

<span id="_Toc143780862" class="anchor"></span>Table : Data Descriptions

#### View / Edit Plan Screen

This screen displays plan information for viewing/editing including utilization review info, plan coverage limitations, annual benefit dates, user information, and plan comments.

| Acronym | Description                                                | Action                                                                                                                |
|---------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| PI      | Policy Information                                         | Allows entry / edit of maximum out-of-pocket and ambulance coverage.                                                  |
| UI      | UR Info                                                    | Allows entry / edit of utilization review information.                                                                |
| CV      | Add/Edit Coverage                                          | Allows the user to add, edit, or delete (unwanted) coverage limitations for a specific plan.                          |
| PC      | Plan Comments                                              | Allows editing of comments for the plan.                                                                              |
| IP      | Inpatient                                                  | Allows entry / edit of inpatient benefits data.                                                                       |
| AB      | Annual Benefits - (accesses Annual Benefits Editor screen) | Used to enter annual benefits data for the selected policy.                                                           |
| CP      | Change Plan                                                | Allows the user to select another plan for this insurance company without having to exit back to the previous screen. |

<span id="_Toc143780863" class="anchor"></span>Table : Parameter Group and Key

Sample Screen

Insurance Company Editor Nov 26, 2014@12:19:25 Page: 1 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

------------------------------------------------------------------------------

Billing Parameters

Signature Required?: YES Type Of Coverage: HEALTH INSURANCE

Reimburse?: WILL NOT REIMBURSE Billing Phone:

Mult. Bedsections: YES Verification Phone:

One Opt. Visit: NO Precert Comp. Name:

Diff. Rev. Codes: Precert Phone:

Amb. Sur. Rev. Code:

Rx Refill Rev. Code:

Filing Time Frame: (1 YEAR(S))

EDI Parameters

Transmit?: YES-LIVE Insurance Type: GROUP POLICY

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:24:58 Page: 2 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Inst Payer Primary ID: Prof Payer Primary ID:

Inst Payer Sec ID Qual: Prof Payer Sec ID Qual:

Inst Payer Sec ID: Prof Payer Sec ID:

Inst Payer Sec ID Qual: Prof Payer Sec ID Qual:

Inst Payer Sec ID: Prof Payer Sec ID:

Bin Number: Prnt Sec/Tert Auto Claims:

HPID/OEID: Prnt Med Sec Claims w/o MRA: YES

Main Mailing Address

Street: City/State:

Street 2: Phone:

Street 3: Fax:

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:26:11 Page: 3 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Inpatient Claims Office Information

Company Name: INSURANCE COMPANY Street 3:

Street: City/State:

Street 2: Phone:

Fax:

Outpatient Claims Office Information

Company Name: INSURANCE COMPANY Street 3:

Street: City/State:

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:26:53 Page: 4 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Street 2: Phone:

Fax:

Prescription Claims Office Information

Company Name: INSURANCE COMPANY Street 3:

Street: City/State:

Street 2: Phone:

Fax:

Appeals Office Information

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:27:16 Page: 5 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Company Name: INSURANCE COMPANY Street 3:

Street: City/State:

Street 2: Phone:

Fax:

Inquiry Office Information

Company Name: INSURANCE COMPANY Street 3:

Street: City/State:

Street 2: Phone:

Fax:

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:27:39 Page: 6 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Associated Insurance Companies

This insurance company is not defined as either a Parent or a Child.

Provider IDs

Billing Provider Secondary ID

Additional Billing Provider Secondary IDs

VA-Laboratory or Facility Secondary IDs

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:27:51 Page: 7 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

ID Parameters

Attending/Rendering Provider Secondary ID Qualifier (1500):

Attending/Rendering Provider Secondary ID Qualifier (UB-04):

Attending/Rendering Secondary ID Requirement: NONE REQUIRED

Referring Provider Secondary ID Qualifier (1500): UPIN

Referring Provider Secondary ID Requirement: NONE

Use Att/Rend ID as Billing Provider Sec. ID (1500): NO

Use Att/Rend ID as Billing Provider Sec. ID (UB-04): NO

Always use main VAMC as Billing Provider (1500)?: NO

Always use main VAMC as Billing Provider (UB-04)?: NO

Transmit no Billing Provider Sec. ID for the Electronic Plan Types:

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:28:12 Page: 8 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

Payer Information: e-IV

Payer Name: Payer A

VA National ID: VA1 CMS National ID:

Payer Application: eIV FSC Auto-Update: YES

Nationally Enabled: YES Deactivated: NO

Locally Enabled: YES

Remarks

+---------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//

Insurance Company Editor Nov 26, 2014@12:28:30 Page: 9 of 9

Insurance Company Information for: INSURANCE COMPANY

Type of Company: HEALTH INSURANCE Currently Active

+-----------------------------------------------------------------------------

6/05 Will not pay for Omeprazole/Prilosec..jc

1/1/04 All XXXXX are combined to this one this year and an all inclusive

\# is xxx-xxx-xxxx..ID# are changing over to W + 9 digits now too..jc

This insurance carrier entry and phone number is inclusive for the

'Bxxxxx Company'. mdm

Synonyms

XXX

----------Enter ?? for more actions------------------------------------------\>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Quit//

### List Flagged Stop Codes / Dispositions / Clinics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Flagged Stop Codes/Dispositions/Clinics option is used to generate a list of all stop codes, dispositions, and clinics That have been flagged as not being billable for Means Test billing.

The user is prompted for the effective date of the list and a device. The output contains a separate page for non-billable dispositions, stop codes, and clinics.

Sample Output

LIST OF NON-BILLABLE DISPOSITIONS

As Of: 12/16/93

Page: 1

Run Date: 12/16/93

=============================================================================

DEAD ON ARRIVAL

=============================================================================

LIST OF NON-BILLABLE CLINIC STOP CODES

As Of: 12/16/93

Page: 2

Run Date: 12/16/93

=============================================================================

EMPLOYEE HEALTH

=============================================================================

LIST OF NON-BILLABLE CLINICS

As Of: 12/16/93

Page: 3

Run Date: 12/16/93

=============================================================================

ALLERGY RESEARCH

#### List Flagged Stop Codes / Clinics for Third-Party

This output is used to generate a list of all stop codes and clinics that are flagged through the Flag Stop Codes/Clinics for Third-Party option as *non-billable* or *non-auto billable*. These flags can be deactivated and reactivated through the above-mentioned option.

*Non-billable* stop codes or clinics are those that should not be billed to a Third-Party payer. By default, if a stop code or clinic is non-billable, it will not be billed by the auto biller; and therefore, is non-auto billable.

*Non-auto billable* stop codes or clinics are those that may be billable to a Third-Party payer, but the auto biller should not be used for billing. These are visits that may need more research than can be performed by the auto biller to determine if billable.

Sample Output

LIST OF CLINIC STOP CODES FLAGGED FOR THIRD PARTY BILLING

As Of: 10/01/96

Page: 1

Run Date: 10/01/96

=============================================================================

NON-BILLABLE

AMPUTATION CLINIC CARDIAC SURGERY

CARDIOVASCULAR NUCLEAR MED CWT SUBSTANCE ABUSE

CWT/TR-HCMI CWT/TR-SUBSTANCE ABUSE

EMPLOYEE HEALTH ENT

RMS COMPENSATED WORK THERAPY RMS COMPENSATED WORK THERAPY

RMS INCENTIVE THERAPY RMS INCENTIVE THERAPY

RMS VOCATIONAL ASSISTANCE RMS VOCATIONAL ASSISTANCE

TELEPHONE TRIAGE TELEPHONE/ALCOHOL DEPENDENCE

TELEPHONE/ANCILLARY TELEPHONE/DENTAL

TELEPHONE/DIAGNOSTIC TELEPHONE/DIALYSIS

TELEPHONE/DRUG DEPENDENCE TELEPHONE/GENERAL PSYCHIATRY

TELEPHONE/MEDICINE TELEPHONE/PROSTHETICS/ORTHOTIC

Enter RETURN to continue or '^' to exit: \<RET\>

=============================================================================

LIST OF CLINIC STOP CODES FLAGGED FOR THIRD PARTY BILLING

As Of: 10/01/96

Page: 2

Run Date: 10/01/96

=============================================================================

TELEPHONE/PTSD TELEPHONE/REHAB AND SUPPORT

TELEPHONE/SPECIAL PSYCHIATRY TELEPHONE/SUBSTANCE ABUSE

TELEPHONE/SURGERY

NOT AUTO BILLED

GENERAL MEDICINE

=============================================================================

LIST OF CLINICS FLAGGED FOR THIRD PARTY BILLING

As Of: 10/01/96

Page: 3

Run Date: 10/01/96

=============================================================================

NON-BILLABLE

No clinics are flagged as NON-BILLABLE

NOT AUTO BILLED

GENERAL MEDICAL

### Billing Rates List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Billing Rates List option will print a list of billing rates for a selected date range. It is an efficient way to verify that all billing rate entries have been entered correctly.

The output generated by this option displays the CHAMPVA, Health Care Finance Administration (HCFA) ambulatory surgery rates, Medicare deductibles, and copayments. The effective date, amount (basic rate), and additional amount will be shown for each rate, if applicable. Certain ambulatory surgeries may be billed at the HCFA rate. The amount shown (if any) in the Additional Amount column is an extra amount that may be charged for all procedures within that rate group. The amount shown under Inpatient Per Diem and NHCU Per Diem is the daily charge for Category C patients.

Any billing rate that is effective for any date within the selected range is displayed. If more than one rate was effective within the date range, both rates are displayed.

Sample Output

JUN 11,1997 \*\*\*Billing Rates Listing\*\*\* PAGE 1

Rates in effect from: JAN 01, 1997

to: JUN 11, 1997

=============================================================================

CHAMPVA LIMIT

Effective Date Amount Additional Amount

OCT 01, 1991 \$25

CHAMPVA SUBSISTENCE

Effective Date Amount Additional Amount

OCT 01, 1994 \$9.50

HCFA AMB. SURG. RATE 1

Effective Date Amount Additional Amount

JAN 01, 1992 \$285

HCFA AMB. SURG. RATE 2

Effective Date Amount Additional Amount

JAN 01, 1992 \$382

JUN 11,1997 \*\*\*Billing Rates Listing\*\*\* PAGE 2

Rates in effect from: JAN 01, 1997

to: JUN 11, 1997

=============================================================================

HCFA AMB. SURG. RATE 3

Effective Date Amount Additional Amount

JAN 01, 1992 \$438

HCFA AMB. SURG. RATE 4

Effective Date Amount Additional Amount

JAN 01, 1992 \$539

HCFA AMB. SURG. RATE 5

Effective Date Amount Additional Amount

JAN 01, 1992 \$615

HCFA AMB. SURG. RATE 6

Effective Date Amount Additional Amount

JAN 01, 1992 \$580 \$200

JUN 11,1997 \*\*\*Billing Rates Listing\*\*\* PAGE 3

Rates in effect from: JAN 01, 1997

to: JUN 11, 1997

============================================================================

HCFA AMB. SURG. RATE 7

Effective Date Amount Additional Amount

JAN 01, 1992 \$853

HCFA AMB. SURG. RATE 8

Effective Date Amount Additional Amount

JAN 01, 1992 \$705 \$200

HCFA AMB. SURG. RATE 9

Effective Date Amount Additional Amount

JAN 01, 1992 \$0

INPATIENT PER DIEM

Effective Date Amount Additional Amount

OCT 01, 1990 \$10

JUN 11,1997 \*\*\*Billing Rates Listing\*\*\* PAGE 4

Rates in effect from: JAN 01, 1997

to: JUN 11, 1997

============================================================================

MEDICARE DEDUCTIBLE

Effective Date Amount Additional Amount

JAN 01, 1996 \$736

NHCU PER DIEM

Effective Date Amount Additional Amount

OCT 01, 1990 \$5

NSC PHARMACY COPAY

Effective Date Amount Additional Amount

OCT 01, 1992 \$2

JUN 09, 1997 \$5.00 \$2.00

SC PHARMACY COPAY

Effective Date Amount Additional Amount

OCT 01, 1990 \$2

### MCCR Site Parameter Enter / Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MCCR Site Parameter Enter/Edit option allows the user to define and edit the MCCR site-specific billing parameters. The parameters are displayed upon entering the option and are divided into groups for editing. Each group is labeled with a number to the left of the data items. Some values may be filled in by the system.

- Group 1: The medical center name is automatically filled in and is not editable. The federal tax number is the tax ID# assigned to the medical center and is a required field. There may be more than one Blue Cross/Blue Shield provider number assigned to a site for different categories of care. The main Blue Cross/Blue Shield provider number should be entered here. This is a required field. The Medicare provider number is furnished to the facility by Medicare. The MAS Service Pointer is Medical Administration Service the way it is entered in the HOSPITAL SERVICE file. The default division will appear as the default to the division question when entering Billable Ambulatory Surgical Codes on a bill.
- Group 2: The name and title of bill signer will appear on the third-party billing form. The billing supervisor name does not appear on the form. This is used in conjunction with the Bill Cancellation and Bill Disapproval Mail Groups. If these groups are not specified, the billing supervisor will be one of the few recipients of both messages.
- Group 3: The Multiple Form Types parameter should be set to YES if the facility uses more than one health insurance billing form. UB forms and HCFA-1500 are the forms currently available. If this field is left blank or answered NO, only UB forms will be allowed. Beginning with version 1.5 of Integrated Billing, the review step of creating a bill has been eliminated. If the CAN INITIATOR AUTHORIZE parameter is set to YES and the initiator holds the IB AUTHORIZE security key, the initiator of the bill will be allowed to authorize the bill. If this parameter is set to NO, another user who holds the IB AUTHORIZE key will have to authorize the bill.

  The CAN CLERK ENTER NON-PTF CODES parameter affects editing of diagnosis and procedure codes on inpatient bills. If this parameter is set to YES, diagnosis and procedure codes not found in the PTF record may be entered into the billing record. The ASK HINQ IN MCCR parameter, if set to YES, will allow the billing clerk to enter a request in the HINQ Suspense file while entering a bill for a patient whose eligibility has not been verified. If set to YES, the USE OP CPT SCREEN parameter will allow the Current Procedural Terminology Codes Screen for outpatient bills to be displayed on Billing Screen 5. The date range of this listing will be determined by the OP VISIT DATE(S) on file in the bill. If there are none, the STATEMENT COVERS FROM and TO dates will be used to determine which CPT codes can be selected for inclusion in the bill.

  When billing Billable Ambulatory Surgical Codes (BASC), the entry at the DEFAULT AMB SURG REV CODE parameter will be the default revenue code stored in the bill. If this is not appropriate for any insurance company, the AMBULATORY SURG. REV. CODE field in the Insurance Company file may be entered and used for that insurance company entry.

  CPT procedures may be stored as ambulatory procedures in the Scheduling Visits file (using the Add/Edit Stop Code option) and stored in the billing record as procedures to print on a bill. There is now a two-way sharing of information between these two files. If the TRANSFER PROCEDURES TO SCHED parameter is answered YES, as CPT procedures that are also ambulatory procedures are entered into a bill, the user will be prompted to indicate whether it should also be transferred to the Scheduling Visits file. Conversely, the USE OP CPT SCREEN parameter allows importing of ambulatory procedures into a bill. Only CPT procedures that are either Billable Ambulatory Surgical Codes or nationally or locally active ambulatory procedures may be transferred.

  The per diem start date is the date that the facility informed Category C patients of the new per diem charges and began per diem billing. This field represents the earliest date the hospital or nursing home per diem charge may be billed to a Category C patient. This billing is mandated by Public Law 101-508, which was implemented on November 5, 1990.
17. Per diem billing will not occur if this field is blank.

    A default revenue code, diagnosis code, and CPT procedure code can be set to be used on every bill that has prescription refills. The revenue code default will be overridden by the PRESCRIPTION REFILL REV. CODE for an insurance company if one exists. Only activated revenue codes can be entered.

    Set the SUPPRESS MT INS BULLETIN parameter to YES to suppress the bulletin sent when any Means Test charge covered by the patient's health insurance is billed.
- Group 4: This number is the revenue code for total charges. If the HOLD MT BILLS W/INS parameter is answered YES, automated Category C bills will automatically be placed on hold if the patient has active insurance. The bills may be released to Accounts Receivable after claim disposition from the insurance company. The next parameter allows the user to enter remarks to appear on every printed UB billing form type. The UB-92 Address Col and HCFA 1500 Addr Col parameters determine where the mailing address will begin printing on the billing form. The cancellation remark is the message that will be sent to Fiscal Service every time a bill is canceled in MAS.

  The next two parameters in this group allow mail groups to be set up so that whenever a bill is canceled or disapproved, members of these groups are notified via electronic mail. If these groups are not specified, only the billing supervisor, the user who canceled/disapproved, and the initiator of the bill (for disapproval message only) will be notified. The Copay Background Error group is the mail group that will receive mail messages from the IBE filer when an unsuccessful attempt to file is detected. The Category C Billing mail group members will receive messages when Means Test t/ Category C billing processing errors have been encountered, and when movements and Means Tests for Category C patients have been edited or deleted. The mail groups must have been established through MailMan to be entered at these prompts.
- Group 5: The agent cashier's mailing symbol, complete address, and telephone number are specified here. The street address will not appear on the screen. All billing payments made to the site should be received at the agent cashier's office.

  The default form type is the form most used at the facility (UB-82 or UB-92). All new bills and all follow-up bills will be printed on this form unless the primary insurer has the other UB form defined as the form type. The default form type parameter helps to control the transition between the UB-82 and the UB-92.

  The MCCR System Definition Menu and this option is locked with the IB SUPERVISOR security key.

  If necessary, please refer to the Data Supplement at the end of this option documentation for an explanation of the required response for each parameter.

Sample Screen

MEDICAL CARE COST RECOVERY PARAMETER ENTER/EDIT

=========================================================================

\[1\] Medical Center Name: SAN DIEGO Federal Tax \# : XX-XXXXXXX

Default BC/BS \# : 10297XXX84123 Medicare Number : XXXXXXXX

MAS Service Pointer: MEDICAL ADMIN. Default Division : SAN DIEGO

\[2\] Bill Signer Name : HARVEY Title: CHIEF, MAS

Billing Supervisor : PATRICIA

\[3\] Multiple Form Types: YES Initiator Authorize: YES

Use Non-PTF Codes? : UNSPECIFIED Ask Hinq in MCCR?: UNSPECIFIED

Use OP CPT Screen? : UNSPECIFIED Default ASC Rev. Cd: 490

Xfer Proc to Sched?: YES Per Diem Start Date: NOV 5, 1990

Default RX Rev. Cd : 257 Suppress MT Ins Bulletin: UNSPECIFIED

Default RX Dx Cd : V68.1 Default RX CPT Cd: 99070

\[4\] '001' for Total? : YES Hold MT Bills W/Ins: YES

Remark on each bill: TEST BILL UB-92 Address Col: UNSPECIFIED

Cancellation Remark: TESTING HCFA 1500 Addr Col: 25

Cancelled Mailgroup: PTF Disap. Mailgroup: PTF

Copay Mailgroup : IB ERROR Cat C Mailgroup: IB CAT C

\[5\] Agent Cashier : ISC-04

Phone : XXX-XXX-XXXX Default Form Type : UB-92

Enter 1-5 to EDIT, or '^' to QUIT:

DATA SUPPLEMENT

| Data                           | Description                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AGENT CASHIER MAIL SYMBOL      | Mailing symbol of agent cashier at the facility.                                                                                                                                                                                                                                                                                                                          |
| AGENT CASHIER STREET ADDRESS   | Mailing address of agent cashier at the facility.                                                                                                                                                                                                                                                                                                                         |
| AGENT CASHIER CITY             |                                                                                                                                                                                                                                                                                                                                                                           |
| AGENT CASHIER STATE            |                                                                                                                                                                                                                                                                                                                                                                           |
| AGENT CASHIER ZIP CODE         |                                                                                                                                                                                                                                                                                                                                                                           |
| AGENT CASHIER PHONE NUMBER     | Telephone number of agent cashier at the facility.                                                                                                                                                                                                                                                                                                                        |
| ASK HINQ IN MCCR               | YES or NO: Allow billing clerk to enter a request in the HINQ Suspense file while entering a bill for a patient whose eligibility is not verified.                                                                                                                                                                                                                        |
| BILL CANCELLATION MAIL GROUP   | Specify the mail group to notify whenever a third-party bill is canceled.                                                                                                                                                                                                                                                                                                 |
| BILL DISAPPROVED MAIL GROUP    | Specify the mail group to notify whenever a third-party bill is disapproved.                                                                                                                                                                                                                                                                                              |
| BILLING SUPERVISOR NAME        | Name of billing supervisor at the facility.                                                                                                                                                                                                                                                                                                                               |
| BLUE CROSS/SHIELD PROVIDER \#  | Main provider number (3 - 13 characters).                                                                                                                                                                                                                                                                                                                                 |
| CAN CLERK ENTER NON-PTF CODES  | YES or NO - Can diagnosis and procedure codes not found in the PTF record be entered into the billing record.                                                                                                                                                                                                                                                             |
| CAN INITIATOR AUTHORIZE        | YES or NO - Beginning with Version 1.5 of Integrated Billing, the review step of creating a bill has been eliminated. If this parameter is answered YES and the initiator holds the IB AUTHORIZE key, the initiator of the bill will be allowed to authorize the bill. If this field is answered NO, another user who holds the IB AUTHORIZE key must authorize the bill. |
| CANCELLATION REMARK FOR FISCAL | Remark (reason for cancellation, 3-75 characters) that will be sent to Fiscal Svc. every time a bill is canceled in MAS.                                                                                                                                                                                                                                                  |
| CATEGORY C BILLING MAIL GROUP  | Members of this mail group will receive messages when Means Test / Category C billing processing errors have been encountered, and when movements and Means Tests for Category C patients have been edited or deleted.                                                                                                                                                    |
| COPAY BACKGROUND ERROR GROUP   | This is the mail group that will receive mail messages from the IBE filer when an unsuccessful attempt to file is detected.                                                                                                                                                                                                                                               |
| DEFAULT AMB SURG REV CODE      | When billing BASCs (Billable Ambulatory Surgical Codes), this will be the default revenue code stored in the bill. If this is not appropriate for any insurance company, the AMBULATORY SURG. REV. CODE field in the Insurance Company file may be used for that insurance company entry.                                                                                 |
| DEFAULT DIVISION               | This field will appear as the default answer to the division question when entering Billable Ambulatory Surgeries on a bill.                                                                                                                                                                                                                                              |
| DEFAULT FORM TYPE              | Enter the form type most used at the facility. Choose from UB-82 or UB-92.                                                                                                                                                                                                                                                                                                |
| DEFAULT RX REFILL CPT          | Enter a CPT procedure code that should be printed on every bill that contains RX refills. If entered, this procedure will automatically be added to every bill that has a prescription refill.                                                                                                                                                                            |
| DEFAULT RX REFILL DX           | Enter a diagnosis code that should be added to every RX refill bill. If entered, this diagnosis will automatically be added to every bill that has a prescription refill.                                                                                                                                                                                                 |
| DEFAULT RX REFILL REV CODE     | Enter the revenue code that should be used for RX refills. This default will be overridden by the PRESCRIPTION REFILL REV. CODE for an insurance company if one exists. Only activated revenue codes can be selected.                                                                                                                                                     |
| FEDERAL TAX NUMBER             | Enter the federal tax number for the facility in NN-NNNNNNN format.                                                                                                                                                                                                                                                                                                       |
| HCFA 1500 ADDRESS COLUMN       | This is the column the mailing address should begin printing on row 1 of the HCFA-1500 form.                                                                                                                                                                                                                                                                              |
| HOLD MT BILLS W/INS            | If this parameter is answered YES, the automated Category C bills will automatically be placed on hold for patients with active insurance. The bills may be released to Accounts Receivable after claim disposition from the insurance company.                                                                                                                           |
| MAS SERVICE POINTER            | Medical Administration Service as it is entered in the HOSPITAL SERVICE file.                                                                                                                                                                                                                                                                                             |
| MEDICARE PROVIDER NUMBER       | Provided by Medicare to the facility (1-8 characters). This number will print in Form Locator 7 on the UB-82 form.                                                                                                                                                                                                                                                        |
| MULTIPLE FORM TYPES            | YES or NO - Set this field to YES if the facility uses more than one type of health insurance form. The UB forms and the HCFA-1500 are the form types currently available. If this parameter is set to NO or left blank, only UB forms will be allowed.                                                                                                                   |
| NAME OF CLAIM FORM SIGNER      | Name of person responsible for signing.                                                                                                                                                                                                                                                                                                                                   |
| PER DIEM START DATE            | This is the date that the facility informed Category C patients of the new per diem charges and began per diem billing. Per diem billing will not occur if this field is left blank.                                                                                                                                                                                      |
| PRINT '001' FOR TOTAL CHARGES  | YES or NO - Print '001' (revenue code for total charges) next to total charges on third-party bill.                                                                                                                                                                                                                                                                       |
| REMARKS TO APPEAR ON EACH FORM | Facility specific remarks to print on every UB type bill.                                                                                                                                                                                                                                                                                                                 |
| SUPPRESS MT INS BULLETIN       | YES or NO - Set this parameter to YES to suppress the bulletin sent when any Means Test charge covered by the patient's health insurance is billed.                                                                                                                                                                                                                       |
| TITLE OF CLAIM FORM SIGNER     | Title of person responsible for signing.                                                                                                                                                                                                                                                                                                                                  |
| TRANSFER PROCEDURES TO SCHED   | YES or NO - If this parameter is answered.                                                                                                                                                                                                                                                                                                                                |
| UB-92 ADDRESS COLUMN           | This is the column the mailing address should begin printing on the UB-92.                                                                                                                                                                                                                                                                                                |
| USE OP CPT SCREEN              | YES or NO - Allow Current Procedural Terminology Codes Screen to appear when editing procedure codes on Screen 5. The screen will list CPT codes for the dates associated with the bill.                                                                                                                                                                                  |

<span id="_Toc143780864" class="anchor"></span>Table : Parameter Descriptions

### Purge Insurance Buffer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a Buffer entry is processed, most of the data is immediately deleted from that entry leaving only a stub entry for tracking and reporting purposes. This option deletes Insurance Buffer entries that were processed (accepted or rejected) before the selected date. A minimum of 1 year of buffer processed records is maintained online; therefore, the latest selectable date is one year prior to the current date.

Sample Screen

INSURANCE BUFFER PURGE

This option will purge Buffer file records Processed before a given date.

When a Buffer record is Processed a stub entry remains in the Buffer file

for tracking and reporting purposes. This option deletes all stub entries

of Buffer records processed at least a year ago. Once a record is purged,

it can not be retrieved and will no longer be included in Buffer reports.

To maintain a record of the Buffer activity, consider printing the Buffer

reports for the date range you are going to be purging.

Purge Buffer Records Processed Before: Nov 05, 1997// 6/1/97 (JUN 01, 1997)

Ok to Purge Buffer records Processed before Jun 01, 1997? y YES

Purge of Insurance Buffer queued for this evening at 8:00pm.

### MCCR Site Parameter Display / Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter Group                     | Security Key Required                |
|-------------------------------------|--------------------------------------|
| IB Site Parameters                  | IB PARAMETER EDIT                    |
| Claims Tracking Parameters          | IB PARAMETER EDIT; IB PARAMETER EDIT |
| Third-Party Auto Billing Parameters | IB PARAMETER EDIT                    |
| Insurance Verification              | IB SUPERVISOR                        |
| MCCR SITE PARAMETERS                | IB PARAMETER EDIT                    |

<span id="_Toc143780865" class="anchor"></span>Table : IB Site Parameters

This option consolidates parameters from the Enter/Edit IB Site Parameters, MCCR Site Parameter Enter/Edit, Claims Tracking Parameter Edit, and Enter/Edit Automated Billing Parameters options. The initial screen lists three parameter groups.

The following table lists the screens, the actions provided, and a brief description of each action. Actions shown in *italics* access other screens.

#### MCCR Site Parameters Screen

| Parameter                           | Description                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| IB Site Parameters                  | Accesses the IB Site Parameter screen that displays general Integrated Billing site parameters.                                          |
| Claims Tracking Parameters          | Accesses the Claims Tracking Parameters screen that displays parameters specific to the set-up and control of Claims Tracking functions. |
| Third-Party Auto Billing Parameters | Accesses the Automated Billing Parameters screen that displays the control parameters for the Third-Party Automated Biller.              |
| Insurance Verification              | Accesses the IV site parameters screen. More details regarding the IV site parameters are provided in the eIV User Guide, Section 2.     |

<span id="_Toc143780866" class="anchor"></span>Table : Claims Tracking Parameters

#### IB Site Parameters Screen

Descriptions for most of the parameters included on this screen can be found in the Enter/Edit IB Site Parameters and MCCR Site Parameter Enter/Edit option documentation. The following table is a description of the six parameters (group 12) used to configure the Tricare Pharmacy billing interfaces that are user set. The other seven parameters in this group that appear on the right-hand side of the screen are set by the system.

| Parameter       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rx Billing Port | This is the logical port that is opened to establish a Transmission Control Protocol / Internet Protocol (TCP / IP) connection with the RNA package to submit Pharmacy claims. This is normally a number between 2000 and 10000. The number that is selected is programmed into the RNA package, as this is the port that the RNA package constantly polls for input from VistA. The Billing port must be entered to start the billing engine.   |
| AWP Update Port | This is the logical port that is opened to establish a TCP/IP connection with the RNA package to receive AWP updates. This is normally a number between 2000 and 10000. This number is also programmed into the RNA package, as it is the port through which the RNA package transmits the AWP updates. This port number must be different from the Billing port number, or the background job to receive AWP updates will not be queued to run. |
| TCP/IP Address  | This is the TCP / IP address used to reach the RNA package. This address is usually determined by the facility systems manager and supplied to RNA on the Plan Installation Worksheet. This address must be entered to start the billing engine.                                                                                                                                                                                                 |
| Task UCI, VOL   | This is UCI and Volume set on which the queued background jobs should run. If this field has no value (i.e., for Alpha sites), the jobs will be queued to run on the current UCI and Volume.                                                                                                                                                                                                                                                     |
| AWP Charge Set  | This is the Charge Set within the Charge Master that was used to load the AWP. The interface must know which Charge Set should be used to extract a unit price for a specific NDC number (drug). A valid Charge Set must be entered to start the billing engine.                                                                                                                                                                                 |
| Prescriber ID   | This is the DEA number assigned to the facility, which should determine prior to the installation of the RNA package. This number must be submitted with the Pharmacy Billing transaction. The number must be entered to start the billing engine.                                                                                                                                                                                               |
| Edit Set        | This action allows the user to view/edit the fields included in the 12 sets displayed.                                                                                                                                                                                                                                                                                                                                                           |

<span id="_Toc143780867" class="anchor"></span>Table : Automated Billing Parameters

#### Claims Tracking Parameters Screen

Descriptions of the parameters included on this screen can be found in the Claims Tracking Parameter Edit option documentation.

| Parameter     | Description                                                                                                                                                     |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tracking      | Allows the user to edit the data displayed under the Tracking Parameters heading. These parameters control which episodes of care are added to Claims Tracking. |
| Random Sample | Allows the user to edit the data displayed under the Random Sample Parameters heading. These parameters control the selection of random samples.                |
| General       | Allows the user to edit the data displayed under the General Parameters heading.                                                                                |
| Edit All      | Allows the user to edit all data displayed on the Claims Tracking Parameters screen.                                                                            |

<span id="_Toc143780868" class="anchor"></span>Table : Common Actions

#### Automated Billing Parameters Screen

Descriptions of the parameters included on this screen can be found in the Enter/Edit Automated Billing Parameters option documentation.

| Parameter    | Description                                                                                                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General      | Allows the user to edit the data displayed under the General Parameters heading.                                                                                                              |
| Inpatient    | Allows the user to edit the data displayed under the Inpatient Admission heading. These parameters control when inpatient episodes of care are processed by the Third-Party automated biller. |
| Outpatient   | Allows the user to edit the data displayed under Outpatient Visit the heading. These parameters control when outpatient visits are processed by the Third-Party automated biller.             |
| Prescription | Allows the user to edit the data displayed under the Prescription Refill heading. These parameters control when prescription refills are processed by the Third-Party automated biller.       |

<span id="_Toc143780869" class="anchor"></span>Table : Common Actions

Sample Screens

MCCR Site Parameters May 13, 1996 10:45:52 Page: 1 of 1

Display/Edit MCCR Site Parameters.

Only authorized persons may edit this data.

IB Site Parameters Claims Tracking Parameters

Facility Definition General Parameters

Mail Groups Tracking Parameters

Patient Billing Random Sampling

Third-Party Billing HCSR Parameters

Provider Id

EDI Transmission

Third-Party Auto Billing Parameters Insurance Verification

General Parameters General Parameters

Inpatient Admission eIV Parameters

Outpatient Visit eIV Batch Extracts

Prescription Refill IIU Parameters Enter ?? for more actions

IB Site Parameter CT Claims Tracking EX Exit Action

CT Claims Tracking IV Ins. Verification

Select Action: Quit//

IB Site Parameters Mar 10, 1998 11:49:27 Page: 1 of 3

Only authorized persons may edit this data.

\[1\] Copay Background Error Mg: IB ERROR

Copay Exemption Mailgroup: IB ERROR

Use Alerts for Exemption : NO

\[2\] Hold MT Bills w/Ins : YES \# of Days Charges Held: 90

Suppress MT Ins Bulletin : NO

Cat C Mailgroup : IB CAT C

Per Diem Start Date : 01/01/91

\[3\] Disapproval Mailgroup

Cancellation Mailgroup :

Cancellation Remark : CANCELLED BY MAS

\[4\] New Insurance Mailgroup : IB NEW INSURANCE

Unbilled Mailgroup : IB UNBILLED AMOUNTS

Auto Print Unbilled List : NO

<u>+ Enter ?? for more actions</u>

EP Edit Set EX Exit Action

Select Action: Next Screen// MCCR System Definition Menu

Claims Tracking Parameters May 13, 1996 10:52:27 Page: 1 of 1

Only authorized persons may edit this data.

Tracking ParametersRandom Sample Parameters

Track Inpatient: ALL PATIENTS Medicine Sample: 5

Track Outpatient: INSURED ONLY Medicine Admissions: 5

Track Rx: ALL PATIENTS Surgery Sample: 5

Track Prosthetics: INSURED ONLY Surgery Admissions: 5

Reports Can Add CT: YES Psych Sample: 0

Psych Admissions: 5

General Parameters

Initialization Date: 09/01/94

Use Admission Sheet: YES

Header Line 1: ALBANY VAMC

Header Line 2: 113 HOLLAND AVE

Header Line 3: ANYTOWN, NY 12305

Enter ?? for more actions

TP Tracking RS Random Sample GP General

EA Edit All EX Exit Action

Select Action: Quit//

Automated Billing Parameters May 13, 1996 10:54:11 Page: 1 of 1

Only authorized persons may edit this data.

GENERAL PARAMETERSINPATIENT ADMISSION

Auto Biller Frequency: 1 Automate Billing: YES

Date Last Completed: 04/30/96 Billing Cycle: 20

Inpatient Status: Closed Days Delay: 1

OUTPATIENT VISITPRESCRIPTION REFILL

Automate Billing: YES Automate Billing: YES

Billing Cycle: 10 Billing Cycle: 3

Days Delay: 1 Days Delay: 1

Enter ?? for more actions

GP General IP Inpatient OP Outpatient

RX Prescription EX Exit Action

Select Action: Quit//

#### Re-Generate Average Bill Amounts

This option is used to rebuild and store the monthly and yearly counts and dollar amounts of inpatient and outpatient bills for a single month. This data will overwrite any previously stored data.

If a past month is selected, the monthly totals for that month are recomputed and the subsequent yearly totals are updated. Previous months' data is also calculated, when required, to obtain yearly values. This information is used to compute the average bill amount for the Unbilled Amounts Report.

Once the average bill amounts are calculated, the Unbilled Amounts Report is automatically generated, via electronic mail, for the selected month. This mail message is sent to the mail group specified in the UNBILLED MAIL GROUP field of the IB SITE PARAMETERS file.

### Re-Generate Unbilled Amounts Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to regenerate the Unbilled Amounts Report for a single month. This recomputes the unbilled care for the month and updates the unbilled amounts. To simply view previously computed data, please use the View Unbilled Amounts option.

Sample Output

Unbilled Inpatient Patient Listing for: 01/95 Page 1 Mar 20, 1995@10:40:09

Claims

Patient Name Pt. ID. Date of Care Tracking ID Eligibility Insurance Companies

-----------------------------------------------------------------------------------------------------

IBpatient,one XXX-XX-XXXX Nov 27, 1993@11:22 XXXXXX NON-SERVICE CONN GHI,BIG TREE I

IBpatient,two XXX-XX-XXXX Mar 29, 1994@13:00 XXXXXX SC, LESS THAN 50 BLUE CROSS

IBpatient,three XXX-XX-XXXX Mar 24, 1994@07:34 XXXXXX HUMANITARIAN EME HEALTH INS

IBpatient,four XXX-XX-XXXX Sep 01, 1993@17:07 XXXXX SC, 50% TO 100% GHI

### Send Test Unbilled Amounts Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to send a test mail message to the mail group receiving the unbilled amounts messages. This option should be used prior to reporting problems to assist sites in determining whether the mail groups are set up correctly. The mail group to receive the message should be specified in the UNBILLED MAIL GROUP (6.25) field in the IB SITE PARAMETERS file (350.9).

Sample Message

Subj: UNBILLED AMOUNTS Report for Oct. 2099 \[#121659\] 06 Jul 95 09:38

20 Lines

From: INTEGRATED BILLING PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

-----------------------------------------------------------------------------

The Unbilled Amounts for Oct. 2099 has successfully completed for

ALBANY (XXX).

Test Data Only, Test Data Only, Test Data Only

Inpatient Care

Number of Unbilled Inpt Cases : 1,111

Average Inpt. Bill Amount : \$9,999.99

Total Unbilled Inpt Care : \$11,109,988.89

Outpatient Care:

Number of Unbilled Opt Cases : 33,333

Average Opt. Bill Amount : \$222.22

Total Unbilled Opt. Care : \$7,407,259.26

Total Unbilled Amount all care : \$18,517,248.15

Enter RETURN to continue or '^' to exit: \<RET\>

Subj: UNBILLED AMOUNTS Report for Oct. 2099 \[XXXXXX\] Page 2

-----------------------------------------------------------------------------

> **NOTE:** Average bill Amount is based on Bills Authorized during the 12

months preceding the month of this report.

> **NOTE:** Number of cases is insured cases in Claims Tracking that are

not billed (or bill not authorized) but appear to be billable.

Select MESSAGE Action: IGNORE (in IN basket)//

### View Unbilled Amounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to view previously computed unbilled amounts without having to re-compile the data.

Sample Output

Unbilled Amounts Report Page 1 Mar 22, 1995@09:09:28

-----------------------------------------------------------------------------

Inpatient Care: 02/95

Number of Unbilled Inpt. Cases: 54

Average Inpt. Bill Amount: \$5,552.22

Total Inpatient Unbilled: \$299,819.88

Outpatient Care: 02/95

Number of Unbilled Opt. Cases: 192

Average Opt. Bill Amount: \$179.00

Total Outpatient Unbilled: \$34,368.00

Inpatient Care: 01/95

Number of Unbilled Inpt. Cases: 16

Average Inpt. Bill Amount: \$5,832.75

Total Inpatient Unbilled: \$93,324.00

Outpatient Care: 01/95

Number of Unbilled Opt. Cases: 0

Average Opt. Bill Amount: \$178.93

Total Outpatient Unbilled: \$0.00

### Third-Party Joint Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides information needed to answer questions from insurance carriers regarding specific bills or episodes of care. This information is presented in List Manager Screens.

Because the same actions are available on most screens, and most screens can be accessed from any other screen; these Common Actions are listed first and are not repeated under each screen description. Only actions specific to a screen are included with that screen description.

The user may QUIT from any screen; this will bring the user back one level or screen. EXIT is also available on most screens. EXIT returns the user to the menu. For more information on the use of the List Manager utility, please refer to the appendix at the end of this manual.

Actions *shown in italics* access other screens.

| Acronym | Description         | Action                                                                                                                                                              |
|---------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BC      | Bill Charges        | Accesses the Bill Charges screen.                                                                                                                                   |
| DX      | Bill Diagnoses      | Accesses the Bill Diagnoses screen.                                                                                                                                 |
| PR      | Bill Procedures     | Accesses the Bill Procedures screen.                                                                                                                                |
| CI      | Go to Claim Screen  | Returns the user to the Claim Information screen. Available on all screens that may be opened from the Claim Information screen.                                    |
| AR      | Account Profile     | Accesses the AR Account Profile screen.                                                                                                                             |
| CM      | Comment History     | Accesses the AR Comment History screen.                                                                                                                             |
| IR      | Insurance Reviews   | Accesses the Insurance Reviews / Contacts screen.                                                                                                                   |
| HS      | Health Summary      | Displays a Health Summary report. The information displayed on the Health Summary is site specified through the MCCR Site Parameter Display/Edit option.            |
| AL      | Go to Active List   | Returns the user to the Third-Party Active Bills screen if that screen was accessed upon entering this option; otherwise, this action returns the user to the menu. |
| VI      | Insurance Company   | Accesses the Insurance Company screen.                                                                                                                              |
| VP      | Policy              | Accesses the Patient Policy Information screen.                                                                                                                     |
| AB      | Annual Benefits     | Accesses the Annual Benefits screen.                                                                                                                                |
| EL      | Patient Eligibility | Accesses the Patient Eligibility screen.                                                                                                                            |
| EX      | Exit Action         | Exits the option.                                                                                                                                                   |

<span id="_Toc143780870" class="anchor"></span>Table : Common Actions

#### Third-Party Active Bills Screen

This is the first screen displayed if a patient’s name is entered at the first prompt. It lists all active third-party bills for the specified patient in order of date created. All bills created in the Integrated Billing Third-Party Billing module can be found on this screen or the Inactive Bills screen.

| Acronym | Description       | Action                                                                                                         |
|---------|-------------------|----------------------------------------------------------------------------------------------------------------|
| IL      | Inactive Bills    | Accesses the Inactive Bills screen.                                                                            |
| PI      | Patient Insurance | Accesses the Patient Insurance screen.                                                                         |
| CP      | Change Patient    | Allows the user to choose another patient and re-display the Third-Party Active Bills screen for that patient. |

<span id="_Toc143780871" class="anchor"></span>Table : Common Actions

#### Inactive Bills Screen

This screen lists inactive bills for a specified patient. All bills created in the Integrated Billing Third-Party Billing module are found on this screen or the Third-Party Active Bills screen. Bills are displayed beginning with the most recent statement from date.

<table>
<caption><p><span id="_Toc143780872" class="anchor"></span>Table : Common Actions</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 24%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym</th>
<th>Description</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CD</td>
<td>Change Dates</td>
<td><p>Allows the user to change the bills listed by</p>
<p>changing the most recent <strong>statement from</strong> date to be displayed.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc143780872" class="anchor"></span>Table : Common Actions

#### Patient Insurance Screen

This screen displays the list of insurance policies for a patient. It is based on the Patient Insurance Management screen of the Patient Insurance Info View/Edit option. It is only available from the Third-Party Active Bills screen.

#### Claim Information Screen

This screen contains bill data and status information to provide an overall status of the bill. This is the primary claim screen for the inquiry, and many actions are provided to expand on the details of the claim.

If a policy has been updated but the bill has not, those changes are not reflected on this screen. Updated or current insurance information may be viewed using the three insurance screens.

| Acronym | Description | Action                                                                                                                                                                                                                                                   |
|---------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CB      | Change Bill | Allows the user to change the bill being displayed. If the user entered a patient name at the first prompt of this option, only bills for that patient may be selected. If the user entered a bill number at the first prompt, any bill may be selected. |

<span id="_Toc143780873" class="anchor"></span>Table : Common Actions

#### Bill Charges Screen

This screen displays a bill's charge information as it would print on the bill. For UB-92 bills, this closely corresponds to Form Locators 42-49; therefore, any prosthetic items, Rx refills, or additional diagnoses and procedures are included. For HCFA 1500 bills, this closely corresponds to Block 24.

#### Bill Diagnosis Screen

This screen displays all diagnoses assigned to the bill, in the order printed.

#### Bill Procedures Screen

This screen lists all procedures assigned to a bill, in the order printed.

#### AR Account Profile Screen

This screen provides the financial history of a claim's account. This includes the current status of the bill in both IB and AR, as well as the payment or transaction history of the bill from Accounts Receivable. This screen is loosely based on the Profile of Accounts Receivable option.

| Acronym | Description         | Action                                                                 |
|---------|---------------------|------------------------------------------------------------------------|
| VT      | Transaction Profile | Accesses the AR Transaction Profile screen for a selected transaction. |

<span id="_Toc143780874" class="anchor"></span>Table : Common Actions

#### AR Transaction Profile Screen

This screen displays detailed account transaction information for individual claim transactions. It is loosely based on the Accounts Receivable Transaction Profile option.

#### AR Comment History Screen

This screen displays AR comments for the claim's account.

| Acronym | Description    | Action                                                                                                                                                            |
|---------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AD      | Add AR Comment | Allows the user to add an AR Transaction Comment to the bill being displayed. Comment transactions may not be added to a bill that has not been authorized in IB. |

<span id="_Toc143780875" class="anchor"></span>Table : Common Actions

#### Insurance Reviews / Contacts Screen

This screen displays all insurance reviews and contacts for the episodes of care on a bill. It is based on the Insurance Reviews/Contacts screen of the Claims Tracking Insurance Review Edit option. The primary difference between the two screens is that this screen consolidates all contacts for each episode being billed on a claim, while the Claims Tracking screen displays the contacts for a single episode of care.

| Acronym | Description     | Action                                                                                                                                                                                                                                                                                             |
|---------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VR      | Reviews/Appeals | Displays expanded information on a selected insurance contact. The screen accessed by this action will depend on the type of contact selected. If the contact is an appeal or denial, the Expanded Appeals / Denials screen is opened; otherwise, the Expanded Insurance Reviews screen is opened. |

<span id="_Toc143780876" class="anchor"></span>Table : IB Site Parameters

#### Expanded Appeals / Denials Screen

This screen displays expanded information on insurance appeals and denials listed on the Insurance Review/Contacts screen. This screen is based on the Expanded Appeals/Denials screen of the Claims Tracking Appeal/Denial Edit option.

#### Expanded Insurance Reviews Screen

This screen displays expanded information on insurance reviews listed on the Insurance Reviews/Contacts screen. This screen is based on the Expanded Insurance Reviews screen of the Claims Tracking Insurance Review Edit option.

#### Insurance Company Screen

This screen displays extended information on an Insurance Company. It is based on the Insurance Company Editor screen of the Insurance Company Entry/Edit option. This screen may be entered from the Patient Insurance screen or any of the bill-specific screens. Once a bill is selected, this screen displays only information related to the insurance carriers assigned to that bill.

#### Patient Policy Information Screen

This screen displays extended information on insurance policies. It is based on the Patient Policy Information screen of the Patient Insurance Info View/Edit option. This screen may be entered from either the Patient Insurance screen or from any of the bill-specific screens. Once a bill is selected, this screen will only display information related to the insurance policies assigned to the bill.

#### Annual Benefits Screen

This screen displays extended information on the annual benefits of insurance policies. It is based on the Annual Benefits Editor screen of the Patient Insurance Info View/Edit option. This screen may be entered from the Patient Insurance screen or any of the bill-specific screens. Once a bill has been chosen, this screen displays information related to the insurance policies assigned to that bill.

#### Patient Eligibility Screen

This screen displays the current information on the patient's eligibility for care and service connection status. It is loosely based on the Eligibility Inquiry for Patient Billing option. This screen is available from the Third-Party Active Bills screen and the bill-specific screens.

If this screen is accessed from one of the bill-specific screens, such as the Claim Information screen, the standard list of bill screen actions will be available from this screen.

If this screen is accessed from the Patient Insurance screen, no other screens are, and the user must return to a previous screen to access other screens.

Sample Screens

Third-Party Active Bills May 31, 1995 @10:07:11 Page 1 of 1

IBpatient,one XXXX NSC

Bill \# From To Type Stat Rate Insurer Orig Amt Curr Amt

1 XXXXXX 04/20/92 04/20/92 O/P/O BI REIM INS HEALTH 0.00 0.00

2 XXXXXX 04/20/92 04/24/92 O/P/O PC REIM INS HEALTH 698.30 698.30

3 XXXXXX \* 11/16/93 11/17/93 O/P/O N REIM INS + HEALTH 199.00 199.00

4 XXXXXX 02/16/94 02/16/94 O/P/I PC REIM INS + HEALTH 196.00 196.00

5 XXXXXX \* 03/01/94 03/15/94 O/P/O BI REIM INS + HEALTH 0.00 0.00

6 XXXXXX \* 03/14/94 03/15/94 O/P/R BI REIM INS + ABC 0.00 0.00

7 XXXXXX \* 03/02/94 03/03/94 O/P/P BI REIM INS ABC 0.00 0.00

8 XXXXXX \* 03/06/94 03/07/94 O/I/O N REIM INS ABC 356.00 356.00

9 XXXXXX 05/01/94 05/31/94 I/P/I BI REIM INS HEALTH 0.00 0.00

10 XXXXXX 06/01/94 06/05/94 I/P/P BI REIM INS HEALTH 0.00 0.00

11 XXXXXX \* 03/03/94 03/31/94 I/I/P A REIM INS + HEALTH 11221.00 856.45

12 XXXXXX 08/30/94 09/30/94 I/P/I BI REIM INS ABC 0.00 0.00

\+ \| \* Cat C Charges on Hold \| + 2nd/3rd Carrier \|

CI Claim Information IL Inactive Bills PI Patient Insurance

CP Change Patient HS Health Summary EL Patient Eligibility

Select Action: Next Screen//

Inactive Bills May 17, 1996 13:30:26 Page: 1 of 2

IBpatient,one XXXX \*\* All Inactive Bills \*\* (9)

Bill \# From To Type Stat Rate Insurer Orig Amt Curr Amt

1 XXXXXX 06/01/94 06/05/94 I/P/I CC REIM INS + ABC 935.00 0.00

2 XXXXXX 06/01/94 06/05/94 I/P/R CB REIM INS + HEALTH 0.00 0.00

3 XXXXXX 05/07/94 05/12/94 I/P/R CB REIM INS HEALTH 0.00 0.00

4 XXXXXX \* 03/02/94 03/03/94 O/P/P CB REIM INS 0.00 0.00

5 XXXXXX \* 03/02/94 03/03/94 O/P/R CB REIM INS 0.00 0.00

6 XXXXXX 02/16/94 02/16/94 O/P/O CB REIM INS 0.00 0.00

7 XXXXXX 04/14/92 04/20/92 O/P/O CB REIM INS ABC 1026.02 1026.02

8 XXXXXX 02/08/90 02/08/90 O/P/R CC REIM INS BC/BS 26.00 0.00

9 XXXXXX 02/07/90 02/07/90 O/P/R CC REIM INS BC/BS 26.00 0.00

\+ \|\* Cat C Charges on Hold \|+ 2nd/3rd Carrier \|

CI Claim Information AL Go to Active List CD Change Dates

EX Exit Action

Select Action: Next Screen//

Sample ScreensClaim Information Dec 12, 2013@08:10:10 Page: 1 of 3

XXXXXXXX PXXXX DOB: XX/XX/XX Subsc ID: XXXXXXXXX

--------------------------------------------------------------------------------

Insurance Demographics

Bill Payer: CAREMARK 6XXXXX

Claim Address: PO BOX XXXXX

ANYTOWN, AZ XXXXX

Claim Phone: XXX-XXX-XXXX

Subscriber Demographics

Group Number: GRP PLN 1605501

Group Name: GICRX

Subscriber ID: XXXXXXXXX

Employer: BIG COMPANY

Insured's Name: IB,SPOUSE

Relationship: SPOUSE

+---------\|% EEOB \| Enter ?? for more actions\|----------------------------------

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CB Change Bill HS Health Summary EL Patient Eligibility

ED EDI Status AL Go to Active List EB Expand Benefits

RX ECME Information EX Exit

Select Action: Next Screen// NEXT SCREEN

Sample Screens

Claim Information Dec 12, 2013@08:10:21 Page: 2 of 3

XXXXXXX PATIENT,IB PXXXX DOB: XX/XX/XX Subsc ID: XXXXXXXXX

+-------------------------------------------------------------------------------

Claim Information

Bill Type: OUTPATIENT Charge Type:

Time Frame: ADMIT THRU DISCHARGE Service Dates: 01/31/12 - 01/31/12

Rate Type: REIMBURSABLE INS. Orig Claim: 12.85

AR Status: COLLECTED/CLOSED Balance Due: 0.00

Sequence: PRIMARY

Purch Svc: NO

ECME No: XXXXXXXXXXXX

ECME Ap No: XXXXXXXXXXXXXXXXXXXX

NPI: XXXXXXXXXX

HPID: XXXXXXXXXX

+---------Enter ?? for more actions---------------------------------------------

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CB Change Bill HS Health Summary EL Patient Eligibility

ED EDI Status AL Go to Active List EB Expand Benefits

RX ECME Information EX Exit

Select Action: Next Screen// NEXT SCREEN

Claim Information Dec 12, 2013@08:10:24 Page: 3 of 3

XXXXXXXXX PATIENT,IB PXXXX DOB: XX/XX/XX Subsc ID: XXXXXXXXX

+-------------------------------------------------------------------------------

Entered: 01/31/12 by IB,TESTER

Authorized: 01/31/12 by IB,TESTER

First Printed: 01/31/12 by IB,TESTER

Related Prescription Copay Information

Rx: XXXXXXX Chg: \$8.00 Status: On Hold Bill:

----------Enter ?? for more actions---------------------------------------------

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CB Change Bill HS Health Summary EL Patient Eligibility

ED EDI Status AL Go to Active List EB Expand Benefits

RX ECME Information EX Exit

Select Action: Quit//

Sample ScreensPatient Insurance May 31, 1995 @10:07:11 Page 1 of 1

Insurance Management for Patient: IBpatient,one XXXX

Insurance Co. Type of Policy Group Holder Effect. Expires

1 HEALTH INS LTD GN 48923222 SELF 01/01/87

2 ABC MAJOR MEDICAL AE 76899354 SPOUSE 10/1/90 19/30/95

3 XYZ INS INDEMNITY T109 OTHER 10/1/94 01/01/95

4 BC/BS MAJOR MEDICAL GN 392043 SELF 01/01/90 12/31/92

VI Insurance Company VP Policy AB Annual Benefits

AL Go to Active List EX Exit Action

Select Action: Quit//

Bill Charges May 31, 1995 @10:07:11 Page 1 of 1

XXXXXX IBpatient,one XXXX DOB: XX/XX/XX Subsc ID: XXXXXXXX

11/16/93 - 11/17/93 ADMIT THRU DISCHARGE Orig Amt: 199.00

OUTPATIENT VISIT

500 OUTPATIENT SVS 178.00 1 178.00

PRESCRIPTION

257 DRGS/NONSCRPT 21.00 1 21.00

001 TOTAL CHARGE 199.00

OP VISIT DATE(S) BILLED: NOV 16, 1993

PRESCRIPTION REFILLS:

30948 NOV 17, 1993 ABBOCATH-T 18G 1.25 IN

QTY: 20 for 10 days supply

Bill Remark: This is a demonstration bill created for Joint Billing Inquiry.

Enter ?? for more actions

DX Bill Diagnosis AR Account Profile VI Insurance Company

PR Bill Procedures CM Comment History VP Policy

CI Go to Claim Screen IR Insurance Reviews AB Annual Benefits

HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensBill Charges May 31, 1995 @10:07:11 Page 1 of 1

XXXXXX IBpatient,one XXXX DOB: XX/XX/XX Subsc ID: XXXXXXXX

03/02/94 - 03/31/94 INTERIM - FIRST CLAIM Orig Amt: 11221.00

30 DAYS INPATIENT CARE

INTERMEDIATE CARE

101 ALL INCL R&B 246.00 30 7380.00

240 ALL INCL ANCIL 48.00 30 1440.00

960 PRO FEE 49.00 30 1470.00

274 PROSTH/ORTH DEV 931.00 1 931.00

001 TOTAL CHARGE 11221.00

PROSTHETIC ITEMS:

Sep 18, 1994 WHEELCHAIR

Sep 21, 1994 CANE-ALL OTHER

Enter ?? for more actions

DX Bill Diagnosis AR Account Profile VI Insurance Company

PR Bill Procedures CM Comment History VP Policy

CI Go to Claim Screen IR Insurance Reviews AB Annual Benefits

HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensBill Diagnosis May 17, 1996 14:07:56 Page: 1 of 1

XXXXXX IBpatient,one XXXX DOB: XX/XX/XX Subsc ID: XXXXXXXX

11/16/93 - 11/17/93 ADMIT THRU DISCHARGE CLAIM Orig Amt: 199.00

1\) 490. BRONCHITIS NOS

2\) 030.1 TUBERCULOID LEPROSY

3\) 101. VINCENT'S ANGINA

4\) 330.1 CEREBRAL LIPIDOSES

5\) 461.0 AC MAXILLARY SINUSITIS

6\) 310.0 FRONTAL LOBE SYNDROME

7\) 200.01 RETICULOSARCOMA HEAD

Enter ?? for more actions

BC Bill Charges AR Account Profile VI Insurance Company

PR Bill Procedures CM Comment History VP Policy

CI Go to Claim Screen IR Insurance Reviews AB Annual Benefits

HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensBill Procedures May 17, 1996 14:12:58 Page: 1 of 1

XXXXXX IBpatient,one XXXX DOB: XX/XX/XX Subsc ID: XXXXXXXX

11/16/93 - 11/17/93 ADMIT THRU DISCHARGE CLAIM Orig Amt: 199.00

XXXXX SURGICAL CLEANSING OF SKIN 11/16/93

XXXXX ADDITIONAL CLEANSING OF SKIN 11/16/93

XXXXX REPAIR SUPERFICIAL WOUND(S) 11/16/93

Enter ?? for more actions

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

CI Go to Claim Screen IR Insurance Reviews AB Annual Benefits

HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensAR Account Profile May 31, 1995 @10:07:11 Page: 1 of 1

XXXXXX IBpatient,one XXXX DOB: XX/XX/XX Subsc ID: XXXXXXXX

AR Status: ACTIVE Orig Amt: 11221.00 Balance Due: 856.45

04/01/94 IB Status: Printed (Last) 11221.00 11221.00

1 1578 05/07/94 PAYMENT (IN PART) 7856.21 3364.79

2 1598 07/07/94 PAYMENT (IN PART) 2508.34 856.45

3 1601 07/08/94 COMMENT 0.00 856.45

Total Collected: 10364.55

Percent Collected: 92.37%

Enter ?? for more actions

BC Bill Charges VT Transaction Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensAR Transaction Profile May 31, 1995 @10:07:11 Page 1 of 1

XXXXXX IBpatient,one XXXX DOB: XX/XX/XX Subsc ID: XXXXXXXX

AR Status: ACTIVE Orig Amt: 11221.00 Balance Due: 856.45

TRANS. NO: 1578 TRANS. TYPE: PAYMENT (IN PART)

TRANS. DATE: 05/07/94 DATE POSTED: 05/10/94 (ARH)

TRANS. AMOUNT: 7856.21 RECEIPT \#: XXXXXXXX

BALANCE COLLECTED

------------- ---------------

PRINCIPLE: 3364.79 7856.21

INTEREST: 0.00 0.00

ADMINISTRATIVE: 0.00 0.00

MARSHALL FEE: 0.00 0.00

COURT COST: 0.00 0.00

-------- ---------

TOTAL: 3364.79 7856.21

FY: 94 PR AMT: 3364.79 FY TR AMT: 7856.21

COMMENTS: Date of Deposit: MAY 10, 1994

Enter ?? for more actions

CI Go to Claim Screen AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensAR Comment History May 17, 1996 14:21:37 Page: 1 of 1

XXXXXX IBpatient,one XXXX DOB: 5 XX/XX/XX Subsc ID: XXXXXXX

AR Status: CANCELLED Orig Amt: 1026.02 Balance Due: 1026.02

1582 04/21/92 Copy of bill sent. FOLLOW-UP DT: 05/12/92

Carrier did not receive initial bill.

1594 05/20/92 Bill canceled, wrong form type. FOLLOW-UP DT: 06/01/92

Carrier refuses to process this type of bill on a UB-92. They are requiring the HCFA 1500 form.

Enter ?? for more actions

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis AD Add AR Comment VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensInsurance Reviews/Contacts May 31, 1995 @10:07:11 Page: 1 of 1

Insurance Review Entries for: XXXXXX IBpatient,one XXXX

Date Ins. Co. Type Contact Action Auth. No. Days

OUTPATIENT VISIT of AMBULATORY SURGERY OFFICE on 11/16/93

1 11/30/93 HEALTH INS LIMITED 1st Appeal-Clin APPROVED AU XXXXX

2 11/17/93 HEALTH INS LIMITED OPT DENIAL 0

PRESCRIPTION REFILL of XXXXX on 11/17/93

3 11/17/93 HEALTH INS LIMITED OPT APPROVED RN XXXXXXX

Service Connected: NO Previous Spec. Bills: TORT \>\>\>

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures VR Reviews/Appeals AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensExpanded Appeals/Denials May 31, 1995 @10:07:11 Page 1 of 2

Insurance Appeal/Denial for: IBpatient,one XXXX ROI: NOT REQUIRED

Visit Information Action Information

Visit Type: OUTPATIENT VISIT Type Contact: INITIAL APPEAL

Visit Date: 03/09/94 9:00 am Appeal Type: CLINICAL

Clinic: AMBULATORY SURGERY Case Status: OPEN

Appt. Status: CHECKED OUT No Days Pending:

Appt. Type: REGULAR Final Outcome:

Special Cond:

Clinical Information Appeal Address Information

Provider: Ins. Co. Name: HEALTH INS LIMITED

Provider: Alternate Name:

Diagnosis: Street line 1: HIL - APPEALS OFFICE

Diagnosis: Street line 2: 1099 THIRD AVE, SUITE

Special Cond: Street line 3:

City/State/Zip: ANYTOWN, NY 12345

Insurance Policy Information

Ins. Co. Name: HEALTH INS LIMITED Subscriber Name: IBpatient,one

Group Number: GN 48923222 Subscriber ID: XXXXXXXX

Whose Insurance: VETERAN Effective Date: 01/01/87

Pre-Cert Phone: XXX-XXX-XXX E Expiration Date:

User Information Contact Information

Entered By: EMPLOYEE Contact Date: 04/01/94

Entered On: 11/16/93 3:30 pm Person Contacted: SPOUSE

Last Edited By: Contact Method: PHONE

Last Edited On: Call Ref. Number: RN XXXXXXX

Review Date: 06/02/95

Comments

Policy should cover treatment.

Service Connected Conditions:

Service Connected: NO

NO SC DISABILITIES LISTED

Enter ?? for more actions \>\>\>

CI Go to Claim Screen AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensExpanded Insurance Reviews May 31, 1995 @10:07:11 Page 1 of 2

Insurance Review Entries for: IBpatient,one XXXX ROI: NOT REQUIRED

Contact Information Action Information

Contact Date: 11/17/93 Type Contact: OUTPATIENT TREATMEN

Person Contacted: Steve Opt Treatment: RX REFILL

Contact Method: PHONE Action: APPROVED

Call Ref. Number: RN XXXXXXX Auth. Number: RN XXXXXXX

Review Date: 06/02/95

Insurance Policy Information

Ins. Co. Name: HEALTH INS LIMITED Subscriber Name: IBpatient,one

Group Number: GN 48923222 Subscriber ID: XXXXXXXX

Whose Insurance: VETERAN Effective Date: 01/01/87

Pre-Cert Phone: XXX-XXXX Expiration Date:

Appeal Address Information User Information

Ins. Co. Name: HEALTH INS LIMITED Entered By: EMPLOYEE

Alternate Name: Entered On: 11/17/93 12:54 pm

Street line 1: HIL - APPEALS OFFICE Last Edited By: EMPLOYEE

Street line 2: 1099 THIRD AVE, SUITE 301 Last Edited On: 11/20/93 12:55 pm

Street line 3:

City/State/Zip: ANYTOWN, NY 12345

Comments

One refill of prescription approved.

Service Connected Conditions:

Service Connected: NO

NO SC DISABILITIES LISTED

Enter ?? for more actions \>\>\>

CI Go to Claim Screen AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensInsurance Company May 17, 1996 15:25:42 Page: 1 of 5

Insurance Company Information for: HEALTH INS LIMITED Primary

Type of Company: HEALTH INSURANCE Currently Active

Billing Parameters

Signature Required?: YES Attending Phys. ID: AT PH ID VAXXXXXXX

Reimburse?: WILL REIMBURSE Hosp. Provider No.:

Mult. Bedsections: YES Primary Form Type:

Diff. Rev. Codes: Billing Phone:

One Opt. Visit: NO Verification Phone:

Amb. Sur. Rev. Code: Precert Comp. Name: ABC INSURANCE

Rx Refill Rev. Code: Precert Phone: XXX-XXX-XXXX E

Filing Time Frame:

Main Mailing Address

Street: 2345 CENTRAL AVENUE City/State: ANYTOWN, NY 12345

Street 2: FREAR BUILDING Phone: XXX-XXXX

Street 3: Fax: XXX-XXXX

Inpatient Claims Office Information

Street: 2345 CENTRAL AVENUE City/State: ANYTOWN, NY 12345

Street 2: FREAR BUILDING Phone: XXX-XXXX

Street 3: Fax: XXX-XXXX

Outpatient Claims Office Information

Street: 789 3RD STREET City/State: ANYTOWN, NY 12345

Street 2: Phone: XXX-XXX-XXXX

Street 3: Fax: XXX- XXX-XXXX

Prescription Claims Office Information

Company Name: GHI PROCESSING Street 3:

Street: 1933 CORPORATE DRIVE City/State: ANYTOWN, NY 39332

Street 2: TANGLEWOOD PARK Phone: XXX-XXXX

Fax:

Appeals Office Information

Street: HIL - APPEALS OFFICE City/State: ANYTOWN, NY 12345

Street 2: 1099 THIRD AVE, SUITE 301 Phone: XXX-XXXX

Street 3: Fax: XXX-XXXX

Inquiry Office Information

Street: 2345 CENTRAL AVENUE City/State: ANYTOWN, NY 12345

Street 2: FREAR BUILDING Phone: XXX-XXXX

Street 3: Fax: XXX-XXXX

RemarksSynonyms

Enter ?? for more actions \>\>\>

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

Sample Screens

Patient Policy Information Dec 12, 2013@08:13:21 Page: 1 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

--------------------------------------------------------------------------------

Insurance Company

Company: MEDICARE (WNR)

Street: PO BOX 10066

Street 2: HEALTH CARE FINANCING

City/State: ANYTOWN, MD 21207

Billing Ph: (XXX)XXX-XXXX

Precert Ph: (XXX)XXX-XXXX

Plan Information

Is Group Plan: YES

Group Name: MEDICARE PART A

Group Number: XXXXXXXXXXX

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:30 Page: 2 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DoD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

BIN:

PCN:

Type of Plan: MEDICARE (M)

Plan Category: MEDICARE PART A

Electronic Type: MEDICARE A or B

Plan Filing TF: 1 YEAR (1 YEAR(S))

ePharmacy Plan ID:

ePharmacy Plan Name:

ePharmacy Natl Status:

ePharmacy Local Status:

Utilization Review Info Effective Dates & Source

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:31 Page: 3 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DoD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Require UR: NO Effective Date: 01/01/13

Require Amb Cert: NO Expiration Date:

Require Pre-Cert: NO Source of Info: INTERVIEW

Exclude Pre-Cond: NO Policy Not Billable: NO

Benefits Assignable: YES

Subscriber Information

Whose Insurance: VETERAN

Subscriber Name: IBSUB,TWOTRLRS

Relationship: SELF

Primary ID: XXXXXXXXXX

Coord. Benefits: PRIMARY

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:31 Page: 4 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DoD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Subscriber's Employer Information

Employment Status: Emp Sponsored Plan: No

Employer: Claims to Employer: No, Send to Insurance

Street: Retirement Date:

City/State:

Phone:

Primary Provider:

Prim Prov Phone:

Subscriber's Information (use Subscriber Update Action)

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:32 Page: 5 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DoD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Subscriber's DOB: XX/XX/XX

Str 1: PALMER HOUSE HEALTH CARE

Str 2: SHEARER ST

City: ANYTOWN

St/Zip: MA 01069

SubDiv:

Country:

Phone: XXX-XXX-XXXX

Subscriber's Sex: MALE

Subscriber's Branch: ARMY

Subscriber's Rank:

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:36 Page: 6 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DoD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Insurance Company ID Numbers (use Subscriber Update Action)

Subscriber ID: XXXXXXXXXX

Plan Coverage Limitations

Coverage Effective Date Covered? Limit Comments

-------- -------------- -------- --------------

INPATIENT 07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

OUTPATIENT 07/01/1998 NO

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:37 Page: 7 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DoD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

01/01/1998 NO

11/01/1996 NO

PHARMACY 08/29/2008 NO

07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

DENTAL 07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

MENTAL HEALTH 07/01/1998 NO

01/01/1998 NO

11/01/1996 NO

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:38 Page: 8 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DoD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

LONG TERM CARE 07/01/1998 NO

01/01/1998 NO

PROSTHETICS 07/01/1998 NO

01/01/1998 NO

VISION 07/01/1998 NO

User Information Insurance Contact (last)

Entered By: IB,TESTER Person Contacted:

Entered On: 06/05/13 Method of Contact: PHONE

Last Verified By: Contact's Phone:

Last Verified On: Call Ref. No.:

Last Updated By: IB,TESTER Contact Date: SEP 24, 2013

Last Updated On: 09/24/13

+---------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// NEXT SCREEN

Patient Policy Information Dec 12, 2013@08:13:39 Page: 9 of 9

For: IBSUB,TWOTRLRS XXX-XX-XXXX DoD:XX/XX/XXXX

MEDICARE (WNR) Insurance Company \*\* Plan Currently Active \*\*

+-------------------------------------------------------------------------------

Comment -- Group Plan

This is a long group comment. This area can hold much more than 80

Characters in the field.

Comment -- Patient Policy

<u>Dt Entered Entered By Method Person Contacted</u>

09/25/15 IBCLERK,TWO PHONE USER-A

JUST A COMMENT AND NOTHING ELSE

+09/25/15 IBCLERK,TWO PHONE USER-A

THIS IS A COMMENT THAT IS LONGER THAN 77 CHARACTERS TO TEST THE WRAP INDICATO

Personal Riders

Rider \#1: DENTAL COVERAGE

----------Enter ?? for more actions---------------------------------------------

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

SU Subscriber Update PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Quit//

Sample ScreensAnnual Benefits May 17, 1996 15:39:23 Page: 1 of 3

Annual Benefits for: ABC Ins. Co Primary

Policy: GN 48923222 Ben Yr: MAR 01, 1993

Policy Information

Max. Out of Pocket: \$ 500

Ambulance Coverage (%): 85 %

Inpatient

Annual Deductible: \$ 500 Drug/Alcohol Lifet. Max: \$

Per Admis. Deductible: \$ 100 Drug/Alcohol Annual Max: \$

Inpt. Lifetime Max: \$ Nursing Home (%):

Inpt. Annual Max: \$ Other Inpt. Charges (%):

Room & Board (%):

Outpatient

Annual Deductible: \$ 50 Surgery (%):

Per Visit Deductible: \$ 50 Emergency (%): 85%

Lifetime Max: \$ Prescription (%): 80%

Annual Max: \$ Adult Day Health Care?: UNK

Visit (%): Dental Cov. Type: PERCENTAGE AMOU

Max Visits Per Year: Dental Cov. (%): 48%

Mental Health Inpatient Mental Health Outpatient

MH Inpt. Max Days/Year: MH Opt. Max Days/Year:

MH Lifetime Inpt. Max: \$ MH Lifetime Opt. Max: \$

MH Annual Inpt. Max: \$ MH Annual Opt. Max: \$

Mental Health Inpt. (%): Mental Health Opt. (%):

Home Health Care Hospice

Care Level: Annual Deductible: \$

Visits Per Year: Inpatient Annual Max.: \$

Max. Days Per Year: Lifetime Max.: \$

Med. Equipment (%): Room and Board (%):

Visit Definition: Other Inpt. Charges (%):

Rehabilitation IV Management

OT Visits/Yr: IV Infusion Opt?: UNK

PT Visits/Yr: IV Infusion Inpt?: UNK

ST Visits/Yr: IV Antibiotics Opt?: UNK

Med Cnslg. Visits/Yr: IV Antibiotics Inpt?: UNK

User Information

Entered By: EMPLOYEE

Entered On: 02/02/94

Last Updated By: EMPLOYEE

Last Updated On: 02/18/94

Enter ?? for more actions \>\>\>

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EL Patient Eligibility

AL Go to Active List EX Exit Action

Select Action: Quit//

Sample ScreensPatient Eligibility May 20, 1996 07:45:44 Page: 1 of 1

XXXXXX IBpatient,one XXXX DOB: XX/XX/XX Subsc ID:

Means Test: CATEGORY A Insured: Yes

Date of Test: 08/24/94 A/O Exposure:

Co-pay Exemption Test: Rad. Exposure:

Date of Test:

Primary Elig. Code: NSC

Other Elig. Code(s): EMPLOYEE

AID & ATTENDANCE

Service Connected: No

Rated Disabilities: BONE DISEASE (0%-NSC)

DEGENERATIVE ARTHRITIS (40%-NSC)

Enter ?? for more actions

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CI Go to Claim Screen HS Health Summary EX Exit Action

AL Go to Active List

Select Action: Quit//

### Fast Enter of New Billing Rates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB SUPERVISOR security key is required to edit.

This option is designed to allow quick entry of new rates into the Charge Master for Interagency and Tortiously Liable Billing Rates. This option should only be used for the annual updated Interagency and Tortiously Liable Rates. The charges will be asked for by charge type category: inpatient, outpatient, prescription, outpatient dental, Cat C copayment. Enter all charges for a category, then move to the next section for the next category. For example, when first prompted for Inpatient Charges. When the user has entered all inpatient bed sections and related charges, a \<RET\> entered at the Select Inpatient Bed section prompt will bring the user to the next charge type, Outpatient, and so on until the user has entered the charges for all charge types.

Revenue codes may be edited through the Enter/Edit Charge Master option.

### Delete Charges from the Charge Master

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB SUPERVISOR security key is required to edit.

This option is used to delete charges from a Charge Set that are no longer needed. All charges that are inactive or that have been replaced before the specified date are deleted. A report of charges that *will be* deleted based on the date entered can be printed before the actual deletion to confirm the charges should be deleted.

Sample Output

Charges (to be deleted) in TL-OPT DENTAL set (ALL CHARGES IN SET) May 28, 1997 09:49 Page 1

Charge Item Effective Inactive Charge Rev Cd

------------------------------------------------------------------------------

CHARGE SET: TL-OPT DENTAL

OUTPATIENT DENTAL 10/01/92 97.00

OUTPATIENT DENTAL 10/01/93 102.00

OUTPATIENT DENTAL 10/01/94 119.00

OUTPATIENT DENTAL 10/01/95 104.00

OUTPATIENT DENTAL 10/01/96 121.00

5 Charges to be deleted

Enter RETURN to continue or '^' to exit:

### Inactivate / List Inactive Codes in Charge Master

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option searches the charges in the Charge Master for inactive CPT codes. It then inactivates all charges associated with those inactive CPT codes. To confirm the charges should be inactivated, a report of charges for inactive CPT codes may be printed.

Sample Output

Charges for Inactive CPT's May 29, 1997 13:47 Page 1

Charge Item Effective Inactive Charge Set Charge Rev Cd

-----------------------------------------------------------------------------

00806 02/01/95 AMB SURG REGION 394.00 333

11701 02/01/95 AMB SURG REGION 343.34

11701 - 54 05/01/96 AMB SURG REGION 34.20

25146 - 66 02/01/95 AMB SURG REGION 942.00

25153 05/01/96 AMB SURG REGION 234.23

5 Charges for Inactive CPT's

# IRM System Manager's Integrated Billing Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purge Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first option in the Purge Menu, Purge Update File, is used to delete all CPT entries from the temporary file, UPDATE BILLABLE AMBULATORY SURGICAL CODE (#350.41), after transferred to the permanent file, BILLABLE AMBULATORY SURGICAL CODES (#350.4). This is usually done yearly, after a HCFA update of the CPT codes.

The remainder of the options in this menu are used to archive and purge billing data. The files that may be archived and subsequently purged are the INTEGRATED BILLING ACTION file (#350) (pharmacy copayment transactions only), the CATEGORY C BILLING CLOCK file (#351), and the BILL/CLAIMS file (#399).

Billing data from the current and one previous fiscal year, at a minimum, must be maintained online; however, the user may opt to maintain data from additional fiscal years, if desired.

The following criteria must be met to purge billing data.

<table>
<caption><p><span id="_Toc143780877" class="anchor"></span>Table : Common Actions</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>INTEGRATED BILLING ACTION File</p>
<p>(pharmacy copayment actions)</p></td>
<td>The prescription that caused the action to be created must have been purged from the pharmacy database before the action may be archived. In addition, the bill must be closed in Accounts Receivable. The date the bill was closed is the date used to determine whether it will be included.</td>
</tr>
<tr class="even">
<td>CATEGORY C</td>
<td>Only clocks with a status of CLOSED or</td>
</tr>
<tr class="odd">
<td>BILLING CLOCK file</td>
<td>CANCELLED and a clock end date prior to the selected time frame are included.</td>
</tr>
<tr class="even">
<td>BILL/CLAIMS file</td>
<td>The bill must be closed in Accounts Receivable. The date the bill was closed is the date used to determine whether it will be included.</td>
</tr>
</tbody>
</table>

<span id="_Toc143780877" class="anchor"></span>Table : Common Actions

There are three steps involved in the archiving and purging of these files.

1.  A search is conducted to find all entries that may be archived through the Find Billing Data to Archive option. The user selects which of the three files to include in the search. The entries found are temporarily stored in a sort (search) template in the SORT TEMPLATE file (#.401). An entry is also made to the IB ARCHIVE/PURGE LOG file (#350.6). This log may be viewed through the Archive/Purge Log Inquiry and List Archive/Purge Log Entries options.

    The List Search Template Entries option allows the user to view the contents of a search template. The user may delete entries from the search template using the Delete Entry from Search Template option.
4.  The entries are archived using the Archive Billing Data option. It is highly recommended to archive the entries to paper (print to a non-slave printer) as there is currently no functionality to retrieve or restore data that has been archived.
5.  The data is purged from the database using the Purge Billing Data option. The search template containing the purged entries is also deleted. An electronic signature code and the XUMGR security key are required to archive and purge data.

### Select Default Device for Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to select the default devices on which third-party claim forms will print. The devices entered through this option will appear as the default devices when using options that generate these forms. Separate devices may be entered for each type of form.

The user will be prompted for the form type. To avoid making duplicate entries of the same form type, it is suggested to type \<??\> at this prompt to first view the selections.

The user will then be prompted for a default printer (in Billing) and a follow-up printer (in Accounts Receivable). The user must enter an Accounts Receivable default device for follow-ups for every form except the UB-82.

In order to utilize the Print Authorized Bills option on the Third-Party Billing Menu, the user must set up billing default printers for each form type through this option. Any form type not set up with a billing default printer will not print when utilizing the Print Authorized Bills option.

The billing default printer must be added for the BILL ADDENDUM form type for the addendums to automatically print for every HCFA-1500 bill with prescription refills or prosthetic items.

### Display Integrated Billing Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Display Integrated Billing Status option allows the user to view data from the IB SITE PARAMETER file and pertinent information about the status of the IB background filer. For further explanation of the IB site parameters, please refer to the Enter/Edit IB Site Parameters option documentation.

One or more of the following messages may appear:

- The Integrated Billing filer has more than 10 transactions in the queue.
- The Integrated Billing filer is not running and has transactions to file.
- The Integrated Billing filer is late. It hasn't run since {date/time}.

If the second message appears, use the Start the Integrated Billing Background Filer option to start the filer. If the first or third message appear, recheck the status in a few minutes. If the message(s) persists or the Number of Transactions in Queue increases, use the Start the Integrated Billing Background Filer option to start the filer.

### Enter / Edit IB Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit IB Site Parameters option allows the user to enter or edit the INTEGRATED BILLING SITE PARAMETER file.

The following is a list of the parameters that may be entered/edited through this option. It should be noted that modification of these parameters may affect the performance of the Integrated Billing background filer.

| Parameter                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FACILITY NAME                 | The name of the facility from the INSTITUTION file (there must be a station number associated with this entry). This value will be used by IFCAP in determining the bill number.                                                                                                                                                                                                                                                                                                              |
| FILE IN BACKGROUND            | If set to YES, the background filer will run as a background job. If set to NO or left blank, filing will occur as applications pass data to Integrated Billing.                                                                                                                                                                                                                                                                                                                              |
| FILER UCI, VOL                | The UCI and volume set where the user want the IBE filer to run. It is recommended that the filer run on the volume set that contains either the IB globals or the PRC globals. VAX sites should leave this field blank.                                                                                                                                                                                                                                                                      |
| FILER HANG TIME               | The number of seconds that the filer will remain idle after finishing all transactions and before checking for more transactions to file. The filer will shut itself down after 200 hangs with no activity detected. If this field is left blank, the default value is two.                                                                                                                                                                                                                   |
| COPAY BACKGROUND ERROR GROUP  | The mail group to receive mail messages from the IBE filer when an unsuccessful attempt to file is detected. IB ERROR will be entered during installation and will appear as a default the first time this option is used; however, it may be edited to any mail group.                                                                                                                                                                                                                   |
| COPAY EXEMPTION MAIL GROUP    | The mail group to receive the copay exemption messages. The mail group specified as the Copay Background Error Group will be entered during installation and will appear as the default the first time this option is used. It may be edited to any mail group.                                                                                                                                                                                                                               |
| USE ALERTS                    | If the facility has Version 7 or higher of Kernel installed, select whether to use alerts or bulletins for internal messages in Integrated Billing. The same mail group (Copay Background Error Group) will receive both alerts and bulletins. This functionality is only available for the Medication Copayment Exemption software; however, if this is a desirable feature it may be expanded in the future. If this field is left unanswered, it defaults to NO and IB will use bulletins. |
| CATEGORY C BILLING MAIL GROUP | Members of this mail group will receive messages when Means Test / Category C billing processing errors have been encountered and when movements and Means Tests for Category C patients have been edited or deleted. IB CAT C will be entered during installation and will appear as a default the first time this option is used; however, it may be edited to any mail group.                                                                                                          |
| PER DIEM START DATE           | The date that the facility informed Category C patients of the new per diem charges and began per diem billing. This field represents the earliest date for which the hospital (\$10.00) or nursing home (\$5.00) per diem charge may be billed to a Category C patient as mandated by Public Law 101-508 (implemented on November 5, 1990). Per diem billing will not occur if this field is left blank.                                                                                     |
| MEANS TEST BILLING MAIL GROUP | Members of this mail group will receive bulletins when Means Test billing processing errors have been encountered, and when movements and Means Tests have been edited or deleted for Veterans that require Means Test charges.                                                                                                                                                                                                                                                               |
| IB MEANS TEST                 | Members of this mail group will receive messages to review the charge(s) for a patient with a National Category 1 High Risk for Suicide flag that were activated or inactivated on the previous day.                                                                                                                                                                                                                                                                                          |

<span id="_Toc143780878" class="anchor"></span>Table : Acronyms and Abbreviations

Sample Screen

Subj: IB SHRPE 'HRfS' IB charges review for 6/20/2018 \[XXXXXXX\] 06/20/18@18:24

11 linesFrom: INTEGRATED BILLING PACKAGE In 'IN' basket. Page 1

The following patient had the HRfS (Cat I) flag activated/inactivated,

and the following charges created on 6/19/2018 should be reviewed by

IB revenue staff:

Patient: IBPATIENT,BEIGHT Pt. ID: XXXXX

User: XXXXXXXXX

XXXXXXXX-THROAT LO-1 : XXX-XXXXXXX

OPT COPAYMENT : XXX-XXXXXXX

XXXXXXX-HALOPERIDO-1 : Pending

XXXXXXX-MICONAZOLE-1 (r): XXX-XXXXXXX

### Inquire an IB Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inquire an IB Action option provides a display of a captioned inquiry for a specified IB action. The purpose of this inquiry is to provide a quick reference of all the fields for all IB actions for a reference number.

### Patient IB Action Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient IB Action Inquiry option provides a brief display of IB actions for a selected patient and date range. The purpose of this inquiry is to provide a quick reference of all the fields for all IB actions for a patient.

### Repost IB Action to Filer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Repost IB Action to Filer option allows Integrated Billing action entries that did not successfully pass to Accounts Receivable to be reposted to the IB filer.

Though this option will seldom, if ever, be used, it allows transactions with a status of COMPLETE (which do not have an Accounts Receivable transaction number assigned) to be reposted.

If there is not enough data to repost the action or if the number selected already has an Accounts Receivable transaction number assigned to it, an appropriate message will be displayed, and the first prompt will be repeated. If the reposting is successful, the user will simply return to the first prompt.

### Start the Integrated Billing Background Filer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a filer job has terminated unexpectedly, this option may be used to force a filer to start running.

If a filer is currently running, the following message will be displayed:

\<\<\<\<WARNING!!! Filer appears to have been started on (date/time)\>\>\>\>

The user will then be given the option of starting a second filer.

### Stop the Integrated Billing Background Filer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may be used to shut down the IB background filer. The filer will cease when it has finished processing all its known transactions. Processing with Accounts Receivable will then be accomplished in the foreground.

When the user shutdown the filer through this option, the FILE IN BACKGROUND site parameter is automatically edited to NO. The IB engine will file in the foreground until that parameter is edited to YES through the Enter/Edit IB Site Parameters option.

### Verify RX Co-Pay Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Verify RX Co-Pay Links option compares the soft link stored in Integrated Billing with the pointer in the PRESCRIPTION file pointing back to Integrated Billing to provide a display/printout of all integrated billing actions that do not verify for a selected range of reference numbers.

Means Test charges may appear on this report if listed in the B cross-reference when there is no actual entry for the reference (this should rarely happen) or if the Means Test charge has no soft link.

This option should be used as a tool for resolving problems. False errors may be reported for several legitimate occurrences, such as the RX was deleted, or the copay canceled.

The Cerner entries for Rx Co-Pay use an HL7 connection. The Logical Link is IBARXCVDF. Failure of a message to or from Cerner will generate an error in the HL7 Log, but will still appear in this list. There is no other difference with the Cerner Rx Co-Pay process than the method of communication to Cerner.

Sample Output

Verify Integrated Billing links to Pharmacy APR 10, 1991 Page:1

Verify IB Reference Number 5001 to 50010

REF. NO. PATIENT SSN RX# REFILL IB LINK

CHARGE ID TRANS ERROR MESSAGE

-----------------------------------------------------------------------------

XXXX IBpatient,one XXXX RX#XXX 120 52:125

XXX-XXXXXX X RX ENTRY MISSING IB NODE

XXXX IBpatient,two XXXX RX#XXXXXX 51 52:111125;1:1

XXX-XXXXXX X RX ENTRY MISSING IB NODE

XXXX IBpatient,three XXXX RX#XXXXXX 1 52:111128;1:1

XXX-XXXXXX X RX ENTRY MISSING IB NODE

XXXX IBpatient,four XXXX RX#XXXXXX 99991 52:111199;1:1

XXX-XXXXXX X RX ENTRY MISSING IB NODE

XXXX IBpatient,five XXXX RX#XXX 120 52:125

XXX-XXXXXX X RX ENTRY MISSING IB NODE

XXXX IBpatient,six XXXX RX#XXXXXX 51 52:111125;1:1

XXX-XXXXXX X RX ENTRY MISSING IB NODE

XXXX IBpatient,seven XXXX RX#XXXXXX 1 52:111128;1:1

XXX-XXXXXX X RX ENTRY MISSING IB NODE

XXXX IBpatient,eight XXXX RX#XXXXXX 1 52:111128;1:1

XXX-XXXXXX X IB CROSS-REFERENCE BUT NO ENTRY

XXXXX IBpatient,nine XXXX RX#XXXXXX 99991 52:111199;1:1

XXX-XXXXXX X RX ENTRY MISSING IB NODE

### Forms Output Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays a list of local forms defined for the site and the associated actions allow the user to add local forms and data elements and to override specific fields on a local form associated with the national one. It also allows the user to define a local SCREEN 9 for bill data entry.

#### List of Local Forms Screen

<u>Add Local Form</u>

This action allows the user to define local output billing forms and local input data screens that are not supported nationally but are needed for specific insurance companies or bill types. It provides the ability to create new forms/screens from scratch, as well as provides for two ways to easily create a new form copy based on an existing nationally released form.

The WANT TO ASSOCIATE THIS FORM WITH A NATIONAL FORM? field allows the user to associate a new local form with a nationally released form without copying any data. This association allows each site to create a local form, but only require modifications to the fields of the form that are different from the nationally released definitions. Any form field definition that is not changed on the local form will continue to use the standard national definition. Any changes from the national definition, however, will be stored as local entries that, when a bill is generated using this local form definition, will override the nationally released definition for these changed fields only. This way, data changes can be made without the site having to take responsibility for maintaining the entire form. Only forms that have the same BASE FILE NUMBER and FORM TYPE can be copied. Any local changes made must be tracked carefully as the site will be responsible for maintaining any locally modified fields should future changes become necessary. Since unmodified fields still rely on the national form for definition, any changes made via a nationally released update to unmodified fields on the form will be automatically incorporated into a local form definition associated with a national form definition.

The WANT TO COPY ALL FIELDS FROM AN EXISTING FORM? field allows a straight copy, where the field definitions for a selected form are all copied into new entries referencing the new local form. Any local form created via an unassociated copy will have NO link back to the national form once the copy is completed.

Since no changes to nationally released software will be made to these local entries, the user is free to modify the new form definition in whatever way needed and is responsible for all changes that are made or will need to be made in the future.

<u>Form View/Edit</u>

Allows the user to view and edit a selected form. This action brings the user to the Detailed View of Local Form Screen. See below.

<u>Add/Edit Local Data Elements</u>

Allows the user to define local data elements that are not supported nationally but are needed to be included on one or more local billing form(s). Nationally released data element definitions CANNOT be modified via this action.

<u>View Data Element</u>

Allows the user to view the description, extract code, and other attributes of any data element defined at the site, both national and local.

<u>Test Form</u>

Allows the user to test the output of a selected form.

#### Detailed View of Local Form Screen

<u>Edit Local Form Demographics</u>

Allows the user to edit the name, description, pre and post processing logic and the extract and output logic for local forms.

<u>Delete A Local Form</u>

Allows the user to delete a locally defined form. When the form is deleted, all form fields and form field definitions (not data element definitions) associated with that form are also deleted.

<u>Edit Form Fields</u>

Allows the user to edit the field content defined for a local form associated with a national form that has local override field content definitions; or to edit any local, unassociated form field's form position data and field content definitions. This action brings the user to the Bill Form Fields Screen. See below.

<u>Switch Form</u>

Allows the user to switch between forms without exiting the option.

#### Bill Form Fields Screen

<u>Add Local/Override Field</u>

Allows the user to add fields to a local unassociated form and allows the addition of ‘override’ fields for local modifications to any form.

<u>Delete Local Form Field</u>

Allows the user to delete the 'override' form field content definitions for a local form associated with a national form or to delete any fields defined for an unassociated local form that do not have override fields defined (the user must delete any override fields first).

<u>Edit Local Form Field</u>

Allows the user to edit the field content for a local form such as page or sequence, first line number, starting column or piece, maximum number of lines, short description, etc.

<u>Local Field Content Definition</u>

Allows the user to edit the override form field content definitions for a local form associated with a national form, or to edit the form field content of any field on an unassociated local form.

<u>Add/Edit Local Data Elements</u>

Allows the user to define local data elements that are not supported nationally but are needed to be included on one or more local billing form(s). Nationally released data element definitions CANNOT be modified via this action.

<u>View Data Element</u>

Allows the user to view the description, extract code, and other attributes of any data element defined at the site, both national and local.

<u>View Form Fields</u>

Allows the user to view the composition of a local ‘override’ or national form field for a local form. This includes both the form field's form position data as well as the associated form field content definition.

Example 1 - CUSTOM BILL PRINT

The site needs to print the total charge, not unit charge, in Block 24F on the HCFA 1500.

1.  If there is not currently a local form defined for the HCFA 1500, use the ADD A LOCAL FORM option to add a form that will become the local HCFA 1500. Base file will be 399, print form type will be P (printed). Respond Yes to associate with national form question and choose the HCFA 1500 as the parent form. Give it a form length of 66 and enter a short description like Local 1500. Since this form is now associated with the national HCFA 1500 form, all the fields will default to the definition provided by the national HCFA 1500 form when the bills are printed. The only time to change the pre and post processing, edit or output routines, is if the user does not want the national defaults, but wants to write on the users own. Be very careful of any change to these executable fields.
6.  Select View Form and, if prompted for selection, enter the local HCFA 1500 form sequence \# from the list displayed. This will display the general characteristics of this form.
7.  Choose the Edit Form Fields action (FF). This will display a list of the form fields that make up this form.
8.  Press return for NEXT SCREEN until the field CHARGES (BX-24F) appears in the field list.
9.  The charge field is a data element that is not able to be extracted on its own. Its value depends on the "line" within box 24 that it will print on because it depends on revenue, code, date, etc. This kind of data element is considered part of a "group" element and that group element must be extracted before any of its group member data element can be output. The group data element for charges is N-HCFA 1500 SERVICES (PRINT). If the user utilizes the View Data Element option and enter this group element name, it sets up the array, IBXSAVE ("BOX24”, line \#) for later use by its group member elements. The user will also see that the 9th "^" piece of this array is the \# of units. This is a calculate only field (no output from it when it is processed).
10. Select the Add Local/Override Field option and enter the sequence number of the CHARGES field.
11. Respond Yes to OK? prompt and to the copy over from the original field question. This is always a good idea so the user can see what the original format of the field was.
12. Leave the data element field the same and do not enter an insurance company or bill type unless the user wants to restrict this change to a specific insurance company and/or bill type.
13. Now change the format field to multiply the value of charges (in variable IBXDATA (line \#)) by the value of the units on the corresponding line \# (in the 9th "^" piece of IBXSAVE ("BOX24”, line \#)).

    Replace \$J(IBXDATA(Z) With \$J(IBXDATA(Z)\*\$P(\$G(IBXSAVE("BOX24",Z)),"^",9)
14. Now modify the format description to reflect the change just made, and the override of the field is complete.
15. To make the formatter print the local copy of the HCFA 1500, use the IRM menu option, Select Default Device for Forms, and enter the name of the local form as the value of the PRINT FORM field. The next time a HCFA 1500 bill prints, it will print the charges as total charges, not a unit charge.

Example 2 - LOCAL SCREEN 9

The site needs to print the provider's phone number in Form Locator 11 on the UB-92 for inpatient bills for insurance company Blue Cross of East Wherever and this data is not currently captured in VistA.

There are several steps involved in this task. First, the user must set up a local field for this data in the bill/claims file and define a local data element in the forms data element file, then create or modify a local Screen 9 to enable the clerks to input this data for this insurance company's bills. The user then needs to edit the local UB-92 print form to include this data in Form Locator 11 for this insurance company and attach this local Screen 9 to the national UB-92 bill form. Only the steps for the creation of local Screen 9 are included here.

1.  Use FileMan to add a local form field, numbered at least 10000 and stored on a numeric node of at least 10000 for this new data element. These are the only kind of fields that can be INPUT on a local Screen 9 (any field can be displayed).
16. Using the output formatter, select the Add/Edit Local Data Elements action. Enter a name for this new data element. Only national fields can start with N-, so any other name is valid. Set the base file to 399 and the type of element to F (FileMan). Type the name that the user gave the local field in step 1 as the FileMan field reference. Make sure the user types it correctly as no edit checks are made on the field at this point. For FileMan return format, use I if the user wants the raw data returned or E if the user wants FileMan to return it in display format. Then enter a description of the field to identify the list of local data elements.
17. Again, using the output formatter, if there is not currently a local form defined for local Screen 9 for the national UB-92 form, use the ADD A LOCAL FORM option to add this form. Base file will be 399, print form type will be S (screen). Respond No to associate with national form question and to the copy fields form another form question. Enter a short description. For now, do not put any code in the form pre and post processing fields. Code can be written to do edits for the data on the screen that will prevent it from being authorized unless the edits are passed (post-processing). The pre-processing is used to set up any variables that may be needed to process this screen. The pre-processing is executed before the screen is displayed; the post-processing takes place after the standard authorize edits are executed upon leaving the bill.
18. Select View Form (VF) and, if prompted for selection, enter the local UB-92 screen form sequence \#. This will display the general characteristics of this form.
19. Choose the Edit Form Fields action (FF). This will display a list of the form fields that make up this form or, if a new form, will display No fields currently defined for this form.
20. Choose Add Local/Override Field action (AF). If there are any fields already defined for this screen, there will be a prompt to allow the user to override an existing field. Respond No if this question is asked. Respond 1 for page/seq then enter the number of the line on the screen where the user wants to prompt for this field to appear and the column the prompt should start in. Skip max \# of lines since this data element can have only one value per bill. Enter a length for the field and it should be long enough to hold the data and its prompt if one is desired. Leave pad as none and edit status as editable. Give it an edit group number that is different from any other group that may already be on the screen. For this data element, assume the field will be output exactly as it is stored, so no format code is needed.
21. Now follow steps 1-3 in the first example but use the UB-92 national form wherever it says to use the HCFA 1500.
22. Press return for NEXT SCREEN until the field FORM LOCATOR 11 (FL-11/1) appears in the field display area.
23. Select the Add Local/Override Field action and enter the sequence number of the FORM LOCATOR 11 (FL-11/1) field.
24. Respond Yes to OK? prompt and No to the copy over from the original field question. This is OK in this case because the new data element is a single-valued field that has absolutely nothing to do with the field it is overriding.
25. Enter the name of the local data element for the provider phone number in the data element field. Enter the BLUE CROSS of EAST WHEREVER insurance company name at the insurance company prompt. Enter bill type as inpatient to restrict this change to a specific bill type for this one insurance company. There is no need to enter Format code or description as we're assuming the data is displayed the same way it is stored in the database. If the user wants it displayed with dashes, but store just the numeric, reformat it using M code here. Make sure there is a FileMan input transform on the data field to strip out the dashes before it stores it. This will now be the override field output for inpatient bills for the BL CR of EAST WHEREVER insurance company's form locator 11.
26. To make the formatter print the local copy of the UB-92 and to associate this local Screen 9 with the UB-92 form type, use the IRM menu option, Select Default Device For Forms, and enter the name of the local form as the value of the PRINT FORM field and the name of the local UB-92 Screen 9 as the local form just created/edited.
27. The next time a UB-92 bill is entered/edited whose insurance company is BL CROSS of EAST WHEREVER, there will be a Screen 9 available to allow entry of the provider phone \#. This field will also print on the UB-92 as the first line in Form Locator 11 when the bill is printed.

## Purge Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purge Update File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XUMGR security key is required to access this option.

The Purge Update File option is used to delete all CPT entries in the temporary file, UPDATE BILLABLE AMBULATORY SURGICAL CODE (#350.41) that have been successfully transferred to the permanent file, BILLABLE AMBULATORY SURGICAL CODE (#350.4). Upon completion, a total number of entries deleted is provided.

If the UPDATE BILLABLE AMBULATORY SURGICAL CODE file is not purged, the next file transfer through the Run Amb. Surg. Update option, all entries previously transferred successfully will show as errors under: Codes already have entries for given effective date and Codes unable to transfer.

### Archive Billing Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XUMGR security key and an electronic signature code are required to complete the archive process.

This option is used to archive data contained in search templates. Search templates are created from the INTEGRATED BILLING ACTION file (#350) (pharmacy copayment transactions only), the CATEGORY C BILLING CLOCK file (#351), and/or the BILL/CLAIMS file (#399) using the Find Billing Data to Archive option. Select which of the files to archive.

It is recommended the user archive the entries to paper (print to a device) as there is currently no functionality to retrieve or restore archived data.

The archive process is automatically queued. All data elements in the file for each entry in the search template are archived.

The user will be notified of the results via electronic mail. The ARCHIVE/PURGE LOG file (#350.6) is updated when the purge is completed. The log \# provided in the mail message may be used for inquiries to this file.

Sample Message

Subj: INTEGRATED BILLING ARCHIVING OF BILLING DATA \[#109348\] 24 Jun 92 15:32 8 Lines

From: INTEGRATED BILLING PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

--------------------------------------------------------------------------------------

The subject job has yielded the following results:

Archive Archive \# Records

File Log# Begin Date/Time End Date/Time Archived

------------------------------------------------------------------------------

CATEGORY C BILLING CLOCK 120 06/24/92@15:29:26 06/24/92@15:51:07 235

BILL/CLAIMS 121 06/24/92@15:51:10 06/24/92@16:32:39 463

Select MESSAGE Action: IGNORE (in IN basket)//

Sample Outputs

Archived CATEGORY C BILLING CLOCK JUN 24, 1992@15:29:28 Page: 1

------------------------------------------------------------------------------

REFERENCE NUMBER: 50045 PATIENT: IBpatient,one

CLOCK BEGIN DATE: JAN 11, 1986 STATUS: CLOSED

1ST 90 DAY INPATIENT AMOUNT: 1738.00 NUMBER INPATIENT DAYS: 2

CLOCK END DATE: JAN 10, 1987

REFERENCE NUMBER: 50178 PATIENT: IBpatient,two

CLOCK BEGIN DATE: MAR 16, 1989 STATUS: CANCELLED

1ST 90 DAY INPATIENT AMOUNT: 754.00 NUMBER INPATIENT DAYS: 1

CLOCK END DATE: MAR 17, 1989 USER ADDING ENTRY: JOHN

DATE ENTRY ADDED: MAR 19, 1989

Archived BILL/CLAIMS JUN 24, 1992@15:30:30 Page: 1

------------------------------------------------------------------------------

ACCOUNTS RECEIVABLE NUMBER: XXX-XXXXX BILL NUMBER: XXXXX

PATIENT NAME: IBpatient,one EVENT DATE: NOV 3, 1988

LOCATION OF CARE: HOSPITAL (INCLUDES CLINIC) - INPT. OR OPT.

BILL CLASSIFICATION: OUTPATIENT

TIMEFRAME OF BILL: ADMIT THRU DISCHARGE CLAIM

RATE TYPE: MEANS TEST/CAT. C WHO'S RESPONSIBLE FOR BILL?: PATIENT

STATUS: PRINTED STATUS DATE: JAN 30, 1990

PRIMARY BILL: XXXXXX SC AT TIME OF CARE: YES

FORM TYPE: UB-82

MAILING ADDRESS NAME: ONE IBPATIENT

MAILING ADDRESS STREET: 123 MAIN STREET

MAILING ADDRESS CITY: ANYTOWN MAILING ADDRESS STATE: ANYTOWN

MAILING ADDRESS ZIP CODE: 12208

NUMBER: 500 REVENUE CODE: 500

CHARGES: 127.00 UNITS OF SERVICE: 1

TOTAL: 127.00 BEDSECTION: OUTPATIENT VISIT

DATE ENTERED: NOV 3, 1988

ENTERED/EDITED BY: RICHARD

INITIAL REVIEW: YES INITIAL REVIEW DATE: NOV 3, 1988

INITIAL REVIEWER: RICHARD

SECONDARY REVIEW: YES SECONDARY REVIEW DATE: NOV 3, 1988

SECONDARY REVIEWER: RICHARD

AUTHORIZE BILL GENERATION?: YES AUTHORIZATION DATE: NOV 3, 1988

AUTHORIZER: RICHARD DATE FIRST PRINTED: NOV 3, 1988

FIRST PRINTED BY: RICHARD

DATE LAST PRINTED: NOV 3, 1988 LAST PRINTED BY: RICHARD

STATEMENT COVERS FROM: NOV 3, 1988 STATEMENT COVERS TO: NOV 3, 1988

IS THIS A SENSITIVE RECORD?: NO BC/BS PROVIDER \#: XXXXXXXX

TOTAL CHARGES: 127.00 FISCAL YEAR 1: 89

FY 1 CHARGES: 127.00

### Archive / Purge Log Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XUMGR security key is required to access this option.

This option is used to provide a full inquiry of any entry in the IB ARCHIVE/PURGE LOG file (#350.6). Once the user enters the log \#, all fields in the file for the selected entry will be displayed.

This output may be used to determine the status of a search template, whether archiving or purging has been completed, and who completed the search and/or archive/purge. The number of records, log status, initiator, and begin and end time for each of the three stages of the process (if applicable) are provided. The number of records found, archived, or purged will differ if records are deleted from the search template between processing steps.

Sample Output

LOG \#: 121 BILL/CLAIMS JUN 24, 1992@17:38:16

=============================================================================

Search Template : IB ARCHIVE/PURGE \#121

\# Records Purged : 33

Log Status : CLOSED

Search Begin Date/Time : JUN 24, 1992@14:51:38

Search End Date/Time : JUN 24, 1992@15:24:08

Search Initiator : EMPLOYEE

Archive Begin Date/Time : JUN 24, 1992@15:40:10

Archive End Date/Time : JUN 24, 1992@16:15:39

Archive Initiator : EMPLOYEE

Purge Begin Date/Time : JUN 24, 1992@16:32:47

Purge End Date/Time : JUN 24, 1992@17:10:05

Purge Initiator : EMPLOYEE

### Delete Entry from Search Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once an entry meets the search criteria to be archived and subsequently purged and has been included in a search template, this option may be used to remove the entry from the template and prevent it from being purged. This option might be used for entries that meet the search criteria but because of unusual circumstances must be maintained online.

If more than one search template exists, it will be displayed for selection. Once selected, all records in that template will be displayed. The user will then be allowed to choose which records to delete from the template.

### Find Billing Data to Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge Menu and this option are locked with the XUMGR security key.

This option is used to identify records that meet the criteria to be archived and purged from the INTEGRATED BILLING ACTION file (#350), the CATEGORY C BILLING CLOCK file (#351), and the BILL/CLAIMS file (#399). Entries that are selected to be archived and subsequently purged are placed in a search (sort) template in the SORT TEMPLATE file (#.401). These entries may be viewed/printed through the List Search Template Entries option.

The user opts to which of the three files to include in the search and specifies a different archive/purge time frame for each file; however, a minimum of the current plus one previous fiscal year must be maintained online. In cases where interim claims exist, the claim may only be archived/purged if the final claim can be archived/purged.

The following criteria must be met for the prescription, clock, or bill to be included.

| File                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INTEGRATED BILLING ACTION File (pharmacy copay actions) | The prescription that caused the action to be created must have been purged from the pharmacy database before the action may be archived. In addition, the bill must be closed in Accounts Receivable. The date the bill was closed is the date used to determine whether it will be included.                                                                                                                  |
| BILLING CLOCK File                                      | Only clocks with a status of CLOSED or CANCELLED and a clock end date prior to the selected time frame are included.                                                                                                                                                                                                                                                                                            |
| BILL/CLAIMS File                                        | The bill must be closed in Accounts Receivable. The date the bill was closed is used to determine whether it will be included. The search is automatically queued, and the user is notified of the results via electronic mail. An entry is made in the ARCHIVE/PURGE LOG file (#350.6) each time a search template is created. The log \# provided in the mail message may be used for inquiries to this file. |

<span id="_Toc143780879" class="anchor"></span>Table : Military Time Conversion Table

Sample Message

Subj: INTEGRATED BILLING SEARCH OF BILLING DATA \[XXXXXXX\] 16 Dec 93 14:41

8 Lines

From: INTEGRATED BILLING PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

-----------------------------------------------------------------------------

The subject job has yielded the following results:

Search Search \# Records

File Log# Begin Date/Time End Date/Time Found

------------------------------------------------------------------------------

CATEGORY C BILLING CLOCK 154 12/16/93@14:40:50 12/16/93@14:40:54 82

BILL/CLAIMS 155 12/16/93@14:40:55 12/16/93@14:40:58 1

Select MESSAGE Action: IGNORE (in IN basket)//

### List Archive / Purge Log Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XUMGR security key is required to access this option.

This option is used to list all log entries in the IB ARCHIVE/PURGE LOG file (#350.6). Entries are listed in the order added to the file. A new entry is filed each time a new search template is created through the Find Billing Data to Archive option. The log number, archive file, date created, initiator, and status is provided for each entry.

For a more detailed display on specific entries, please use the Archive/Purge Log Inquiry option.

Sample Output

INTEGRATED BILLING ARCHIVE/PURGE LOG ENTRIES JUN 25,1992 07:57 PAGE 1

DATE

LOG# ARCHIVE FILE CREATED INITIATOR STATUS

-----------------------------------------------------------------------------

1 INTEGRATED BILLING ACTION 05/01/92 IBpatient,one CLOSED

2 CATEGORY C BILLING CLOCK 05/01/92 IBpatient,two CANCELLED

3 CATEGORY C BILLING CLOCK 05/01/92 IBpatient,three CLOSED

4 BILL/CLAIMS 05/01/92 IBpatient,four CLOSED

5 INTEGRATED BILLING ACTION 06/01/92 IBpatient,five CLOSED

6 CATEGORY C BILLING CLOCK 06/01/92 IBpatient,six CLOSED

7 BILL/CLAIMS 06/01/92 IBpatient,seven CLOSED

8 INTEGRATED BILLING ACTION 07/02/92 IBpatient,eight CLOSED

9 CATEGORY C BILLING CLOCK 07/02/92 IBpatient,nine CANCELLED

10 BILL/CLAIMS 07/02/92 IBpatient, ten CLOSED

### List Search Template Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A search template is created in the SORT TEMPLATE file (#.401) each time the Find Billing Data to Archive option is used. The List Search Template Entries option is used to list all entries in a search template that are scheduled to be archived and subsequently purged. This list may be used to review entries and ensure entries are included in the archive/purge of the file. If the user has an entry that meets the purge criteria, but due to unusual circumstances must be maintained online, it may be deleted from the search template through the Delete Entry from Search Template option.

If more than one template exists, these templates will be listed for selection. The output may be sorted by patient as well as an additional specified field. \<??\> may be entered for a list of appropriate fields for selection and additional commands that may be used to customize the list. The selectable fields differ depending on the file. The user will be prompted to enter a range for patient name(s) and the additional field (if selected). If the user accepts the default of FIRST, the system will assume to include all entries.

The fields included in the display will depend on which of the three files the template is created from. The patient’s name and status are displayed for all three files. The INTEGRATED BILLING ACTION file (#350) also displays a brief description of the pharmacy prescription and the date it was added to the field. The CATEGORY C BILLING CLOCK file (#351) displays the clock begin and end dates. The BILL/CLAIMS file (#399) displays the rate type and status date.

Sample Output

CATEGORY C BILLING CLOCK SEARCH TEMPLATE JUN 23,1992 16:35 PAGE 1

CLOCK BEGIN CLOCK END

PATIENT DATE STATUS DATE

-----------------------------------------------------------------------------

IBpatient,one JUN 28,1988 CLOSED JUN 27,1989

IBpatient,two MAY 30,1989 CANCELLED MAY 29,1990

IBpatient,three MAR 15,1989 CLOSED MAR 14,1990

IBpatient,four SEP 1,1988 CLOSED AUG 31,1989

IBpatient,five JAN 2,1989 CLOSED JAN 1,1990

### Purge Billing Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to purge data from the INTEGRATED BILLING ACTION file (#350) (pharmacy copayment transactions only), the CATEGORY C BILLING CLOCK file (#351), and/or the BILL/CLAIMS file (#399). For entries to be purged, they must first be stored in a search template created by the Find Billing Data to Archive option and archived through the Archive Billing Data option. If there is more than one search template created and archived, select which file(s) to purge.

The XUMGR security key and an electronic signature code are required to complete the purge process. The purge is automatically queued, all data elements in the file for each entry in the search template are purged, and the search template is deleted.

The user will be notified of the results via electronic mail. The ARCHIVE/PURGE LOG file (#350.6) is updated when the archive is completed. The log \# provided in the mail message may be used for inquiries to this file.

Sample Message

Subj: INTEGRATED BILLING PURGING OF BILLING DATA \[XXXXXXX\] 24 Jun 92 15:41

8 Lines

From: INTEGRATED BILLING PACKAGE in 'IN' basket. Page 1 \*\*NEW\*\*

---------------------------------------------------------------------------

The subject job has yielded the following results:

Purge Purge \# Records

File Log# Begin Date/Time End Date/Time Purged

-----------------------------------------------------------------------------

CATEGORY C BILLING CLOCK 120 06/24/92@15:35:56 06/24/92@15:50:29 235

BILL/CLAIMS 121 06/24/92@15:50:47 06/24/92@16:41:05 463

Select MESSAGE Action: IGNORE (in IN basket)//

## Charge Master IRM Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Host File into Charge Master

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows new rates and charges to be added to the Charge Master form host files. This is only available for specific rates and charges. The Host file must be in a predefined format to be read correctly.

The following is a list of available choices.

- Load CMAC into XTMP - Upload the CMAC from a host file.
- Load AWP into XTMP - Upload Average Wholesale Price list from a host file.
- Assign Charge Set - Assign charges loaded into XTMP to Charge Sets.
- Check Data Validity - Check files waiting to be loaded into the Charge Master for data validity.
- Load into Charge Master - Check files waiting to be loaded into the Charge Master for data validity and upload files.
- Delete XTMP files - Delete files in XTMP.

### Rate Schedule Adjustment Enter / Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the enter/edit of the Rate Schedule Adjustment field (#363.10). This field causes all charges for a schedule to be adjusted by a site defined amount. It requires M-code that is executed to provide the adjusted amounts and therefore, requires programmer access (DUZ(0)="@").

This Adjustment will have an immediate effect on the charges of the Rate Schedule. The user can confirm the adjustment with a YES response, deny the adjustment with a NO response, or enter ^ to exit the option and not change the adjustment.

### RC Change Facility Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows a site to change the Facility Designation of a division for which charges have been installed from Provider Based to Non-provider Based or vice versa. This entails multiple steps to inactivate the existing charges and then calculate and load the new charges.

### Start the CHAMPUS Rx Billing Engine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used by IRM personnel to queue the background filer. Several parameters must be set before this job can be queued to run; if not set, the job will not be queued. This job will cause four jobs to be queued. The first job is the background filer itself. After this job has been queued and has successfully opened a TCP/IP channel with the RNA system, this job will queue off a secondary filer job. If the first job aborts in any way, the secondary filer will assume the responsibilities of the primary filer and spawn another secondary filer. The option also directly queues a second job to open a separate TCP/IP channel with the RNA system to receive updates of the Average Wholesale Pricelist (AWP). This update is normally received weekly. The AWP Update job will also spawn a secondary job, in a manner like the background filer, which will take over for the primary AWP update job if that job aborts.

18. After the AWP Update is received, members of the IB CHAMP RX START mail group will receive an alert notifying the user that the update has completed.

### Stop the CHAMPUS Rx Billing Engine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may be used to gracefully shut down the billing engine if a planned system shutdown is scheduled to occur, or if the RNA system is scheduled to be shutdown. The option sets a flag that calls for both the background filer and AWP update engine to stop running. The secondary jobs for both jobs will shut down as well.

### Edit the CIDC Insurance Switch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB SUPERVISOR security key is required to access this option.

This option is used to edit the Clinical Indicators Data Capture (CIDC) insurance switch. The CIDC switch controls how CIDC will function in related VistA applications.

Depending on how the parameter is set, users who hold a PROVIDER KEY will, or will not be prompted with CIDC questions.

The following list are the parameters for the CIDC switch. The default is set to ‘0’. Changing this default parameter will affect how other CIDC related applications interact with both Providers and Back Door users.

- 0 = Do not prompt any patients (CIDC prompts do not appear).
- 1 = Prompt patients only with active billable insurance (CIDC prompts appear; conditional).
- 2 = Prompt for all patients (CIDC prompts appear).

# APPENDIX A – Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides definitions and explanations for terms and acronyms relevant to the content presented within this document. For additional terms and acronyms, include references to other VA acronym and glossary repositories (e.g., VA Acronym Lookup and OIT Master Glossary).

| Acronym or Term           | Definition / Explanation                                                                                                                                                                                                                                                                                                        |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC                        | Add Charges                                                                                                                                                                                                                                                                                                                     |
| Admission Sheet           | Worksheet commonly used in front of inpatient charts with a workspace available for concurrent reviews.                                                                                                                                                                                                                         |
| ALOS                      | Average Length of Stay.                                                                                                                                                                                                                                                                                                         |
| AMIS                      | Automated Management Information System                                                                                                                                                                                                                                                                                         |
| AR                        | Accounts Receivable                                                                                                                                                                                                                                                                                                             |
| Automated Biller          | Utility that establishes third-party bills with no user intervention.                                                                                                                                                                                                                                                           |
| AWP                       | Average Wholesale Pricelist                                                                                                                                                                                                                                                                                                     |
| Background Filer          | A background job that accumulates charges and causes adjustment transactions to a bill.                                                                                                                                                                                                                                         |
| BASC                      | Billable Ambulatory Surgical Code.                                                                                                                                                                                                                                                                                              |
| Billing Clock             | A 365-day period, usually beginning when a patient is Means Tested and is placed in Category C, through which a patient's Means Test charges are tracked. An inpatient's Medicare deductible copayment entitles the patient to 90 days of hospital/nursing home care. These 90 days must fall within the 365-day billing clock. |
| CMAC                      | CHAMPUS Maximum Allowable Charges                                                                                                                                                                                                                                                                                               |
| Category C Patient        | Those patients responsible for making copayments as a result of Means Test legislation.                                                                                                                                                                                                                                         |
| CC                        | Community Care                                                                                                                                                                                                                                                                                                                  |
| CHAMPUS                   | Civilian Health and Medical Program of the Uniformed Services; former TRICARE                                                                                                                                                                                                                                                   |
| CHAMPVA                   | Civilian Health and Medical Program of the Department of Veterans Affairs                                                                                                                                                                                                                                                       |
| Check-off Sheet           | A site-configurable printed form containing CPT codes, descriptions, and dollar amounts (optional). Each check-off sheet may be assigned to an individual clinic or multiple clinics.                                                                                                                                           |
| CIDC                      | Clinical Indicators Data Capture                                                                                                                                                                                                                                                                                                |
| Claims Tracking           | Module that allows for the tracking of an episode of care, from scheduling through final disposition of the bill.                                                                                                                                                                                                               |
| Collateral Visit          | A visit by a non-Veteran patient whose appointment is related to or associated with a patient's treatment.                                                                                                                                                                                                                      |
| Continuous Patients       | Continuously hospitalized at the same level of care Patient since July 1, 1986.                                                                                                                                                                                                                                                 |
| Converted Charges         | During the conversion, the BILLS/CLAIMS file (#399) is checked to ensure that each outpatient visit has been billed. For each visit without an established bill, one is established and given a status of CONVERTED.                                                                                                            |
| Copayment                 | The charges, required by legislation, that a patient is billed for services or supplies.                                                                                                                                                                                                                                        |
| CPT                       | Current Procedural Terminology - A coding method developed by the American Hospital Association to assign code numbers to procedures that are used for research, statistical, and reimbursement purposes.                                                                                                                       |
| CSA                       | Claim Status Awaiting Resolution                                                                                                                                                                                                                                                                                                |
| Diagnosis Code            | A numeric or alpha-numeric classification of the terms describing medical conditions, causes, or diseases.                                                                                                                                                                                                                      |
| DOS                       | Date of Service.                                                                                                                                                                                                                                                                                                                |
| EDI                       | Electronic Data Interchange (EDI).                                                                                                                                                                                                                                                                                              |
| eIV                       | Electronic Insurance Verification.                                                                                                                                                                                                                                                                                              |
| Encounter Form            | A paper form used to display data pertaining to an out-patient visit and used to collect additional data pertaining to that visit.                                                                                                                                                                                              |
| ERA                       | Electronic Remittance Advice.                                                                                                                                                                                                                                                                                                   |
| FI                        | Fiscal Intermediary – the company with which a Tricare patient holds Tricare insurance coverage).                                                                                                                                                                                                                               |
| Form Locator              | A block on the UB-82 or UB-92 bill form.                                                                                                                                                                                                                                                                                        |
| FR                        | Facility Revenue.                                                                                                                                                                                                                                                                                                               |
| HCFA                      | Health Care Finance Administration.                                                                                                                                                                                                                                                                                             |
| HCFA-1500                 | AMA approved health insurance claim form used for outpatient third-party billings.                                                                                                                                                                                                                                              |
| HINQ                      | Hospital Inquiry.                                                                                                                                                                                                                                                                                                               |
| HPID                      | Health Plan Identifier.                                                                                                                                                                                                                                                                                                         |
| IB                        | Integrated Billing.                                                                                                                                                                                                                                                                                                             |
| ICD                       | International Classification of Disease.                                                                                                                                                                                                                                                                                        |
| ICD-9                     | International Classification of Diseases, Ninth Modification: A coding system designed by the World Health Organization to assign code numbers to diagnoses and procedures for statistical, research, and reimbursement purposes.                                                                                               |
| ICD-10                    | International Classification of Diseases, Tenth Modification A coding system designed by the World Health Organization to assign code numbers to diagnoses and procedures for statistical, research, and reimbursement purposes.                                                                                                |
| IIU                       | Interfacility Insurance Update.                                                                                                                                                                                                                                                                                                 |
| Integrated Billing Action | The billing record of an event or an increase/decrease in the charges related to an event. An event is any billable goods or services provided by the VA.                                                                                                                                                                       |
| InterQual Criteria        | A method of evaluating appropriateness of care.                                                                                                                                                                                                                                                                                 |
| IVM                       | Income Verification Match.                                                                                                                                                                                                                                                                                                      |
| Locality Rate Modifier    | The Geographic Wage Index that is used to account for wage differences in different localities when calculating the ambulatory surgery charge. It is multiplied by the wage component to get the final geographic wage component of the charge.                                                                                 |
| LTC                       | Long-Term Care.                                                                                                                                                                                                                                                                                                                 |
| MAS                       | Medical Administration Service.                                                                                                                                                                                                                                                                                                 |
| MCCF                      | Medical Care Collections Fund.                                                                                                                                                                                                                                                                                                  |
| MCCR                      | Medical Care Cost Recovery - The collection of monies by the Department of Veterans Affairs (VA).                                                                                                                                                                                                                               |
| Means Test                | A financial report used to determine if a patient may be required to make copayments for care.                                                                                                                                                                                                                                  |
| MISSION                   | Maintaining Internal Systems and Strengthening Integrated Outside Networks Act.                                                                                                                                                                                                                                                 |
| MOH                       | Medal of Honor.                                                                                                                                                                                                                                                                                                                 |
| MRW                       | Medicare Remittance Advice Worklist.                                                                                                                                                                                                                                                                                            |
| NDC                       | National Drug Code.                                                                                                                                                                                                                                                                                                             |
| NHCU                      | Nursing Home Care Unit.                                                                                                                                                                                                                                                                                                         |
| OEID                      | Other Entity Identifier.                                                                                                                                                                                                                                                                                                        |
| OIT                       | Office of Information and Technology.                                                                                                                                                                                                                                                                                           |
| OTH                       | Other Than Honorable.                                                                                                                                                                                                                                                                                                           |
| PDOD                      | Payer Date of Death Report.                                                                                                                                                                                                                                                                                                     |
| PI                        | Patient Insurance.                                                                                                                                                                                                                                                                                                              |
| Principal Diagnosis       | Condition, established after study, to be chiefly responsible for the patient's admission.                                                                                                                                                                                                                                      |
| Provider                  | A person, facility, organization, or supplier that furnishes health care services.                                                                                                                                                                                                                                              |
| PTF                       | Patient Treatment File.                                                                                                                                                                                                                                                                                                         |
| QM                        | Quality Management.                                                                                                                                                                                                                                                                                                             |
| Reimbursable Insurance    | Health insurance that will reimburse VA for the cost of medical care provided to its subscribers.                                                                                                                                                                                                                               |
| Revenue Code              | A code on a third-party bill identifying a specific accommodation, ancillary service, or billing calculation.                                                                                                                                                                                                                   |
| ROI                       | Release of Information.                                                                                                                                                                                                                                                                                                         |
| SSN                       | Social Security Number.                                                                                                                                                                                                                                                                                                         |
| Stop Code                 | A three-digit number corresponding to an additional stop / service a patient received in conjunction with a clinic visit. Stop code entries are used so that medical facilities may receive credit for the services rendered during a patient visit.                                                                            |
| TAS                       | Transaction Applications Suite.                                                                                                                                                                                                                                                                                                 |
| TCP/IP                    | Transmission Control Protocol / Internet Protocol.                                                                                                                                                                                                                                                                              |
| Third-Party Billings      | Instances where a party other than the patient is charged.                                                                                                                                                                                                                                                                      |
| TPJI                      | Third-Party Joint Inquiry.                                                                                                                                                                                                                                                                                                      |
| UB-82                     | AMA-approved health insurance claim form previously used for third-party billings.                                                                                                                                                                                                                                              |
| UB-92                     | AMA-approved health insurance claim form used for third-party billings.                                                                                                                                                                                                                                                         |
| UC                        | Urgent Care - A visit to a local health care facility approved by VA for non-emergent health situations authorized under the MISSION Act of 2018 legislation.                                                                                                                                                                   |
| UR                        | Utilization Review - A review carried out by allied health personnel at predetermined times during the hospital stay to assess the appropriateness of care.                                                                                                                                                                     |
| VA                        | Department of Veterans Affairs.                                                                                                                                                                                                                                                                                                 |
| VACO                      | VA Central Office.                                                                                                                                                                                                                                                                                                              |
| VBA                       | Veterans Benefits Administration.                                                                                                                                                                                                                                                                                               |
| VFA                       | Veterans Financial Assessment Project.                                                                                                                                                                                                                                                                                          |
| VHA                       | Veterans Health Administration.                                                                                                                                                                                                                                                                                                 |
| VistA                     | Veterans Health Information System and Technology Architecture.                                                                                                                                                                                                                                                                 |
| VAMC                      | VA Medical Center.                                                                                                                                                                                                                                                                                                              |
| Wage Percentage           | The percentage of the rate group unit charge that is the wage component to be used in calculating the HCFA charge for ambulatory surgical procedures.                                                                                                                                                                           |
| XPIR                      | Expire Group Plan.                                                                                                                                                                                                                                                                                                              |

<span id="_Toc143780880" class="anchor"></span>Table : List Manager Actions

# APPENDIX B – Military Time Conversion Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Standard       | Military   |
|----------------|------------|
| 12:00 MIDNIGHT | 2400 HOURS |
| 11:00 PM       | 2300 HOURS |
| 10:00 PM       | 2200 HOURS |
| 9:00 PM        | 2100 HOURS |
| 8:00 PM        | 2000 HOURS |
| 7:00 PM        | 1900 HOURS |
| 6:00 PM        | 1800 HOURS |
| 5:00 PM        | 1700 HOURS |
| 4:00 PM        | 1600 HOURS |
| 3:00 PM        | 1500 HOURS |
| 2:00 PM        | 1400 HOURS |
| 1:00 PM        | 1300 HOURS |
| 12:00 NOON     | 1200 HOURS |
| 11:00 AM       | 1100 HOURS |
| 10:00 AM       | 1000 HOURS |
| 9:00 AM        | 0900 HOURS |
| 8:00 AM        | 0800 HOURS |
| 7:00 AM        | 0700 HOURS |
| 6:00 AM        | 0600 HOURS |
| 5:00 AM        | 0500 HOURS |
| 4:00 AM        | 0400 HOURS |
| 3:00 AM        | 0300 HOURS |
| 2:00 AM        | 0200 HOURS |
| 1:00 AM        | 0100 HOURS |

# APPENDIX C – List Manager Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Manager is a tool that displays a list of items in a screen format and provides the following functionality:

- Browse through the list.
- Select items that need action.
- Act against those items.
- Select other List Manager actions without leaving the option.

Actions(s) are entered by typing the name(s) or mnemonics(s) at the Select Action prompt. Where applicable, multiple actions may be selected with one entry by separating actions with a semicolon (;). For example, the single entry AL;CI would cause the software to advance through two separate actions (Appointment Lists and Check In).

Select an action and entry number by using an equals sign (=).

- CI=1: will process entry 1 for check-in.
- CI=3 4 5: will process entries 3, 4, 5 for check-in.
- CI=1-3 : will process entries 1, 2, 3 for check-in.

In addition to the various actions that may be available specific to the option the user is working in, List Manager provides generic actions applicable to any List Manager screen. Enter double question marks (??) at the Select Action prompt for a list of all actions available. On the following page is a list of generic List Manager actions with a brief description. The mnemonic for each action is shown in brackets (\[ \]) following the action name. Entering the mnemonic is the quickest way to select an action.

| Action                         | Action                                                                       |
|--------------------------------|------------------------------------------------------------------------------|
| Next Screen \[+\]              | Move to the next screen.                                                     |
| Previous Screen \[-\]          | Move to the previous screen.                                                 |
| Up a Line \[UP\]               | Move up one line.                                                            |
| Down a Line \[DN\]             | Move down one line.                                                          |
| Shift View to Right \[\>\]     | Move the screen to the right if the screen width is more than 80 characters. |
| Shift View to Left \[\<\]      | Move the screen to the left if the screen width is more than 80 characters.  |
| First Screen \[FS\]            | Move to the first screen.                                                    |
| Last Screen \[LS\]             | Move to the last screen.                                                     |
| Go to Page \[GO\]              | Move to any selected page in the list.                                       |
| Re Display Screen (RD)         | Redisplay the current screen.                                                |
| Print Screen \[PS\]            | Prints the header and the portion of the list currently displayed.           |
| Print List \[PL\]              | Prints the list of entries currently displayed.                              |
| Search List \[SL\]             | Finds the selected text in the list of entries.                              |
| Auto Display (On/Off) \[ADPL\] | Toggles the menu of actions to be displayed / not displayed automatically.   |
| Quit \[QU\]                    | Exits the screen.                                                            |

[^1]: When the Patient Policy Information Screen is accessed by either the Third-Party Joint Inquiry \[IBJ Third-Party Joint Inquiry\] option or any of the Claims Tracking Editing options, the patient policy comments are in view only mode. User will not be able to edit, add, or deleted comments.