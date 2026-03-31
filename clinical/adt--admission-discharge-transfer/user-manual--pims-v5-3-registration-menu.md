---
title: PIMS Version 5.3 User Manual - Registration Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Registration Menu
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: archive
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - patient
  - date
  - test
  - address
  - means
  - edit
  - table
  - status
  - registration
  - veteran
page_count: 0
word_count: 56221
section_count: 69
table_count: 4
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: October 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/pims_reg_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/pims_reg_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=327"
---

---
title: |
  ADT Module/Registration Menu

  PIMS Version 5.3

  User Manual
---

![](pims-version-5-3-user-manual-registration-menu/001.png)

October 2024

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p>Table 1: Description of the Actions Available through the Patient Enrollment Option</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 41%" />
<col style="width: 19%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description (Patch # if applicable)</th>
<th>Project Manager</th>
<th>Technical Writer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10/24/2024</td>
<td><p>DG*5.3*1104 Update the following sections to include COMPACT Act Start date, Number of remaining days, End date and Source of Crisis End:</p>
<p><strong>2.19</strong> Patient Inquiry</p>
<p><strong>4.2</strong> Patient Enrollment</p>
<p><strong>4.14</strong> Eligibility Inquiry for Patient Billing</p>
<p><strong>4.17</strong> Load/Edit a Patient</p>
<p><strong>4.19</strong> Patient Inquiry</p>
<p><strong>4.20.4</strong> Patient Inquiry</p>
<p><strong>4.23</strong> Register a Patient</p></td>
<td>VA PM</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>10/23/2024</td>
<td>DG*5.3*1121 – Updated Enterprise search example to reflect up-to-date prompts (p. 78); updated Data Group 4 of PATIENT DEMOGRAPHIC DATA SCREEN &lt;1&gt; to indicate that pager number is now read-only (p. 103); updated Data Group 1 and Data Group 2 of APPLICANT/SPOUSE EMPLOYMENT DATA SCREEN &lt;4&gt; to indicate these data groups are now read-only (p. 125– 126); added Persian Gulf to Data Group 3 of MILITARY SERVICE DATA SCREEN &lt;6&gt; (p.142).</td>
<td>Booz Allen Hamilton PM</td>
<td>Booz Allen Hamilton TW</td>
</tr>
<tr class="odd">
<td>12/18/2023</td>
<td><p>DG*5.3*1095 Updated the following sections to include COMPACT Act administrative eligibility:</p>
<p><strong>2.19</strong> Patient Inquiry</p>
<p><strong>4.19</strong> Patient Inquiry</p>
<p><strong>4.20.4</strong> Patient Inquiry</p></td>
<td>VA PM</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>12/11/2023</td>
<td>DG*5.3*1103 – Added TERA to Data Group 3 of MILITARY SERVICE DATA SCREEN &lt;6&gt; (<strong>p.</strong> <a href="#TERA_indicator">Error! Bookmark not defined.</a>).</td>
<td>Booz Allen Hamilton PM</td>
<td>Booz Allen Hamilton TW</td>
</tr>
<tr class="odd">
<td>10/19/2023</td>
<td>DG*5.3*1098: Added UNCHARACTERIZED to the SERVICE DISCHARGE TYPE list in Data Group 1 of MILITARY SERVICE DATA SCREEN &lt;6&gt; (p. 105); updated display and description of CLAIM NUMBER and CLAIM FOLDER LOCATION in Data Group 1 of ELIGIBIILTY STATUS DATA SCREEN &lt;7&gt; (p. 113 and p. 116); updated Data Group 3 of ELIGIBIILTY STATUS DATA SCREEN &lt;7&gt; to include WORLD WAR II secondary eligibility (p. 118).</td>
<td>Booz Allen Hamilton PM</td>
<td>Booz Allen Hamilton TW</td>
</tr>
<tr class="even">
<td>07/24/2023</td>
<td>DG*5.3*1093: Updated PATIENT DATA SCREEN &lt;2&gt; Data Group 6 to indicate Indian Attestation data is read-only (p. 88 and 89).</td>
<td>Booz Allen Hamilton PM</td>
<td>Booz Allen Hamilton TW</td>
</tr>
<tr class="odd">
<td>04/20/2023</td>
<td>DG*5.3*1090: Updated MILITARY SERVICE DATA SCREEN &lt;6&gt; DATA GROUP 3, ENVIRONMENT FACTORS, for Agent Orange and Radiation Exposure data (p. 108).</td>
<td>Booz Allen Hamilton PM</td>
<td>Booz Allen Hamilton TW</td>
</tr>
<tr class="even">
<td>02/27/2023</td>
<td>DG*5.3*1085: Updated entry of Preferred Language information to remove requirement for entry of date and time (p. 76 and 79).</td>
<td>Booz Allen Hamilton PM</td>
<td>Booz Allen Hamilton TW</td>
</tr>
<tr class="odd">
<td>12/27/2022</td>
<td>DG*5.3*1082: Updated Presumptive Psychosis Patient Registration Section 2.8 to indicate functionality is moved to the VHA Enrollment System (p. 4); added PRESUMPTIVE PSYCHOSIS ELIGIBLE information to COMPENSATION AND PENSION SCREEN &lt;7&gt; EXPANSION Date Group 3 (p. 118); updated “Enrollment System” to “VHA Enrollment System” throughout document.</td>
<td>Booz Allen Hamilton PM</td>
<td>Booz Allen Hamilton TW</td>
</tr>
<tr class="even">
<td>09/12/2022</td>
<td>DG*5.3*1081: Updated INELIGIBLE/MISSING DATA SCREEN &lt;10&gt; Data Group 1 to indicate that Ineligible Date and Reason fields are not editable and are received from the VHA Enrollment System (p. 127).</td>
<td>Booz Allen Hamilton PM</td>
<td>Booz Allen Hamilton TW</td>
</tr>
<tr class="odd">
<td>08/08/2022</td>
<td>DG*5.3*1064: Megabus Act – Indian Copay: Added Group 6 to PATIENT DATA, SCREEN &lt;2&gt; (p. 88 and 89 – 90).</td>
<td>Booz Allen Hamilton PM</td>
<td>Booz Allen Hamilton TW</td>
</tr>
<tr class="even">
<td>07/05/2022</td>
<td>DG*5.3*1075: Updated RADIATION EXPOSURE METHOD in Data Group 3 on MILITARY SERVICE DATA SCREEN &lt;6&gt;, p. 107; Added note regarding eligibility verified in VHA Enrollment System, p. 108; Added information on Aid &amp; Attendance, Housebound, and VA Pension labels, p. 110; Added default values in Data Group 2 on COMPENSATION AND PENSION SCREEN &lt;7&gt; EXPANSION, p. 115 – 116.</td>
<td>Booz Allen Hamilton PM</td>
<td>Booz Allen Hamilton TW</td>
</tr>
<tr class="odd">
<td>02/22/2021</td>
<td>DG*5.3*1067: Added RELATION TYPE and RELATION NOTE to EMERGENCY CONTACT DATA SCREEN &lt;3&gt; Data Groups 1 – 5<br />
(p. 90 – 93).</td>
<td>Liberty ITS PM</td>
<td>Liberty ITS TW</td>
</tr>
<tr class="even">
<td>02/01/2022</td>
<td>DG*5.3*1073 – Update to the Enter/Edit Patient Security Level section</td>
<td>HPS T3 ADMIN</td>
<td>HPS T3 ADMIN</td>
</tr>
<tr class="odd">
<td>11/22/2021</td>
<td>DG*5.3*1059:Added new read only fields that will displayed when using Patient Inquiry.</td>
<td>IAM PM</td>
<td>IAM TW</td>
</tr>
<tr class="even">
<td>10/11/2021</td>
<td>DG*5.3*1061: COMPACT Act – For Screen &lt;7&gt;, added COMPACT ACT ELIGIBLE and SPECIAL TX AUTHORITY CARE to Data Group 3 (p. 117) and added Data Group 3.3 (p. 118).</td>
<td>Liberty ITS PM</td>
<td>Liberty ITS TW</td>
</tr>
<tr class="odd">
<td>09/23/2021</td>
<td>DG*5.3*1056: Replaced “Permanent Mailing Address” with “Mailing Address” throughout the document.</td>
<td>Liberty ITS PM</td>
<td>Liberty ITS TW</td>
</tr>
<tr class="even">
<td>08/18/2021</td>
<td><p>DG*5.3*1047: Added new report: <u>Potential Presumptive Psychosis Patient Report</u>.</p>
<p>Added Note for the <u>Presumptive Psychosis Reconciliation Report</u>.</p>
<p>Added Note for the <u>Former OTH Patient Eligibility Change Report</u></p></td>
<td>Liberty ITS PM</td>
<td>Liberty ITS TW</td>
</tr>
<tr class="odd">
<td>06/30/2021</td>
<td>DG*5.3*1044: Added Space Force to MILITARY SERVICE DATA SCREEN &lt;6&gt; Data Group 1 SERVICE COMPONENT (p. 103).</td>
<td>Liberty ITS PM</td>
<td>Liberty ITS TW</td>
</tr>
<tr class="even">
<td>06/30/2021</td>
<td><p>DG*5.3*1027 Updated Section 4.1, “Disposition an Application” for “Registration Only” patients (p. 10).</p>
<p>DG*5.3*1027: Updated description for Enroll Patient (EP) in Table 1 due to message change. Updated because ‘to complete’ changes the meaning (p.11).</p>
<p>DG*5.3*993: Registration Only Enrollment Status: Updated Load/Edit Patient Data to indicate that new patient records may not be entered into the system with the Load/Edit Patient Data option (p. 27).</p>
<p>DG*5.3*1027 “Enrollment Application Date” has been modified to “Application Date” (p. 61, p. 78)</p></td>
<td>Liberty ITS PM</td>
<td>Liberty ITS TW</td>
</tr>
<tr class="odd">
<td>06/17/2021</td>
<td>DG*5.3*1035: Added new report: <u>Presumptive Psychosis Patient Detail Report</u></td>
<td>Liberty ITS PM</td>
<td>Liberty ITS TW</td>
</tr>
<tr class="even">
<td>04/28/2021</td>
<td><p>DG*5.3*1034: Added new report: <u>Presumptive Psychosis Reconciliation Report</u></p>
<p>Updated <u>Former OTH Patient Eligibility Change Report</u> and <u>Former OTH Patient Detail Report</u> to include inpatient care.</p></td>
<td>Liberty ITS PM</td>
<td>Liberty ITS TW</td>
</tr>
<tr class="odd">
<td>04/26/2021</td>
<td><p>DG*5.3*1018: Added Blue Water Navy to Priority Group 6 determination rules footnote (p. 46).</p>
<p>Added Blue Water Navy to Data Group 3 ENVIRONMENT FACTORS/AGENT ORANGE EXPOSURE LOCATION on MILITARY SERVICE DATA SCREEN &lt;6&gt; (p. 107).</p></td>
<td>Liberty ITS PM</td>
<td>Liberty ITS TW</td>
</tr>
<tr class="even">
<td>12/16/2020</td>
<td><p>DG*5.3*1025: Added Former OTH Patient Eligibility Change Report to section 4.29 on p 69.</p>
<p>Former OTH Patient Detail Report to Other Than Honorable Reports Menu option to section 4.30 on p 70.</p>
<p>Updated menu options in section 5.3 on p 74.</p></td>
<td>Liberty ITS PM</td>
<td>Liberty ITS TW</td>
</tr>
<tr class="odd">
<td>12/02/2020</td>
<td><p>DG*5.3*1014: Standardized the patient data displayed on the VistA Registration screens and sub-screens banner to include the patient’s Preferred Name. The patient data occupies two separate lines in the banner (p. 76 – 133).</p>
<p>Updated the display of PATIENT DEMOGRAPHIC DATA, SCREEN &lt;1&gt; screen (p. 76), PATIENT DATA, SCREEN &lt;2&gt; screen (p. 87), and MILITARY SERVICE DATA, SCREEN &lt;6&gt; screen (p. 98) in order to accommodate the additional line of patient data in the banner.</p>
<p>Updated EDIPI note per revised display (p. 3, p. 75, p. 76).</p>
<p>Added DATA GROUP [2] to ADDITIONAL ELIGIBILITY VERIFICATION DATA, SCREEN &lt;11.5&gt; and added new CCP Collateral Data &lt;11.5.2&gt; screen (p. 130).</p>
<p>Updated process flow information to accommodate UAM address validation steps (p. 27, p. 53, p. 62, p. 72, p. 79, p. 81, p. 83). Added Address Validation &lt;1.2&gt; screen (p. 86).</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>09/09/2020</td>
<td>DG*5.3*1016: Updated section “5.3 Other Than Honorable Former Service members” specifically added text describing additional sending of ‘Reevaluate patient’s eligibility’ Mailman message.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/24/2020</td>
<td><p>DG*5.3*993 – Updated section 2.17 Load/Edit Patient Data to indicate that the option is only used to edit a patient record, p. 5.</p>
<p>Added patient enrollment status requirements to section 4.1 Disposition an Application, p. 10-11</p>
<p>Update to section 4.2 Patient Enrollment: “This option displays a patient’s enrollment information.”, p. 11</p>
<p>Under 4.2 Patient Enrollment: Updated Enroll Patient Description in Table 1: Description of the Actions Available through the Patient Enrollment Option, p. 11</p>
<p>Added REGISTRATION ONLY reason functionality information in 4.6 Collateral Patient Register, p. 16</p>
<p>Added “Patient is Registration Only” to reasons a Copay Test cannot be added, p. 19</p>
<p>Updated 4.17 Load/Edit Patient Data section to denote that new patient records cannot be entered, and existing patient information may be edited, p. 27</p>
<p>Added “Registration only record” to “Reasons a Copay Test cannot be added” under 4.18.1 Add a New Means Test, p. 30</p>
<p>Updated enrollment prompts for registration process under Section 4.23: Register a Patient, p. 61-62</p>
<p>Updated Section 4.23 Register a Patient: “A Means Test and Copay Test are not required if the patient's Enrollment Status is REGISTRATION ONLY”, p. 63</p>
<p>Sentence removed from Section 4.23 Register a Patient due to DG 993 update: "If the enrollment information for the selected patient is not returned by the end of the registration process, you can enroll the patient via the Patient Enrollment option.”, p. 64</p>
<p>Updated Section 4.23 Register a Patient: "If a Veteran does not wish to enroll, the Enrollment Status is set to the NOT ENROLLED status of REGISTRATION ONLY. Nonveterans are also set to the NOT ENROLLED status of REGISTRATION ONLY.", p. 65</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/10/2020</td>
<td><p>DG*5.3*997: Updated EMERGENCY CONTACT DATA, SCREEN &lt;3&gt; to include foreign address fields for all associate types, p. 87 - 90.</p>
<p>Added Primary/Other Eligibility considerations for caregiver, p.114.</p>
<p>Added ADDITIONAL ELIGIBILITY VERIFICATION DATA, SCREEN &lt;11.5&gt; and Caregiver Data &lt;11.5.1&gt; screen, p. 127 – 128.</p>
<p>Updated Hardships Section 2.18.7 to remove allowance for editing or deleting Hardships, p. 6; Updated resolutions to Hardship-related inconsistency messages in Table 5 to indicate Hardships are to be edited in the VHA Enrollment System, p. 40-41; Updated Hardships Section 4.18.7 to remove allowance for editing or deleting hardships, p. 46; Revised description of how hardships are expired, p. 46.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/19/2020</td>
<td><p>DG*5.3*977: Updated/added Section “2.8: Presumptive Psychosis Patient Registration,” p 4; specifically, the following:</p>
<p>--Added Presumptive Psychosis indicator to ELIGIBILITY STATUS DATA SCREEN.</p>
<p>--Added Presumptive Psychosis Categories to ELIGIBILITY STATUS SCREEN.</p>
<p>--Added Presumptive Psychosis Report Menu options.</p>
<p>Updated/added Section “4.8: Presumptive Psychosis Reports” (p 17-18), as well as sub-sections for each Presumptive Psychosis Report (sub-sections 4.8.1 – 4.8.5, pp 17-18).</p>
<p>Updated Section “5.3: Other Than Honorable Former Service Members,” pp 70 – 71; specifically, added text describing MST-related functions (p 71).</p>
<p>In Appendix A, updated the “Data Group 3” section to include “EXTENDED MH OTH” as a new care type for Priority Group 3 (p 109).</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>05/15/2020</td>
<td>DG*5.3*996: Updated Grant Hardship List Manager action to remove Hardship Review Date prompt, p. 45.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>03/27/2020</td>
<td>DG*5.3*1011 - EMERGENCY RESPONSE - PANDEMIC WORKLOAD REPORTING: Updated EMERGENCY RESPONSE INDICATOR (Data Group 5 of PATIENT DATA SCREEN &lt;2&gt;) to indicate the only available selection is P for (Pandemic) (p. 85).</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>03/25/2020</td>
<td>DG*5.3*1006: Changed “Veteran Medical Benefit Plan” and “VMBP” to “VHA Profile”, “VHA Profiles”, or “VHAP” throughout document; updated Eligibility Verification Data Screen &lt;11&gt; Data Group [5] to read “VHAP”, p. 116 and 118; updated VMBP &lt;11.1A&gt;, &lt;11.3&gt;, &lt;11.3.1&gt;, and &lt;11.4&gt; screens to read “VHAP”,<br />
p. 118 – 119; updated VHAP &lt;11.3&gt; and VHAP &lt;11.3.1&gt; screens to display both date and time in the date field, p. 118.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>01/24/2020</td>
<td>DG*5.3*985: Updated PATIENT DEMOGRAPHIC DATA SCREEN &lt;1&gt; screen to include Preferred Name Data Group [6], p. 73 and p. 75. Updated descriptions of Data Group 1 and Data Group 2 on the EMERGENCY CONTACT DATA SCREEN &lt;3&gt; to indicate display of next-of-kin’s work and phone prompts for K-ADDRESS SAME AS PATIENT’S – YES, p. 85.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>01/16/2020</td>
<td><p>DG*5.3*952: Added Section 5.3 for patients seeking emergent mental health services, pp. 70-71.</p>
<p>Added information on OTH security keys, p. 71.</p>
<p>Added EXPANDED MH CARE TYPE and EXPANDED MH CARE NON-ENROLLEE information to ELIGIBILITY STATUS DATA SCREEN explanation, p. 109-110.</p>
<p>Added Inconsistency #89 – PAT TYPE/OTH ELIG INCONSISTENT, p. 110.</p>
<p>Updates based on HPS IOC Exit feedback, such as, removing number list from title page.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/02/2019</td>
<td>DG*5.3*972: Added MOH Indicator, MOH Award Date, and MOH Status Date to Check Query Status section of Table 1 Description of the Actions Available through the Patient Enrollment Option, p. 13. Added “Patient is awarded Medal of Honor” to reasons a Copay Test cannot be added, p. 17. Added “Veteran is NOT awarded Medal of Honor” to conditions under which a patient may apply for a Copay Test, p. 20. Added Camp Lejeune eligibility and MOH Indicator, MOH Award Date, MOH Status Date, MOH Copayment Exemption Date to Eligibility Inquiry for Patient Billing output display, p. 24. Added “MOH Indicator is “YES” to Reasons a Copay Test cannot be added, p. 28. Added “is NOT awarded Medal of Honor” to conditions under which a Means Test is required, p. 35. Added MEDAL OF HONOR AWARD DATE, MEDAL OF HONOR STATUS DATE, and MEDAL OF HONOR COPAYMENT EXEMPTION DATE to Military Service Data Screen &lt;6&gt;, p. 92, p. 95 and p. 103.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/16/2019</td>
<td>DG*5.3*987: Changed “Health Benefit Plan” to “Veteran Medical Benefit Plan” and “HBP” to “VMBP” throughout document; updated Eligibility Verification Data Screen &lt;11&gt; Data Group [5] to read “Veteran Medical Benefit Plan (VMBP):”, p. 118; added information on the “zz” indicator for inactive VMBPs, p. 120; updated Health Benefit Plan &lt;11.1A&gt;, &lt;11.3&gt;, and &lt;11.4&gt; screens to read “VMBP”, p. 120 – 121; updated VMBP &lt;11.3&gt; screen Action to read “ASSIGN” instead of “ADD”, p. 120; added VMBP &lt;11.3.1&gt; screen, p. 120; converted text of Health Benefit Plan names to UPPERCASE in VMBP &lt;11.4&gt; screen, p. 121.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/05/2018</td>
<td><p>DG*5.3*941: New address type of Residential and Patient Address updates to Patient Demographic Data Screen &lt;1&gt; and Additional Patient Demographic Data Screen &lt;1.1&gt;, pp. 73 – 83. Updated help data for Military Service Data, Screen &lt;6&gt;, p. 95.</p>
<p>References to Bad Address Indicator updated to reflect new location on Screen &lt;1.1&gt; Data Group 2, p. 43 and p. 67.</p>
<p>EAS*1.0*151: Updated View Patient Address Section 4.28 to include Permanent Mailing Address and Address Start and End Dates for Temporary and Confidential Addresses, p. 67.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/24/2018</td>
<td>DG*5.3*947: Early Separation Reason and system display updates to Military Service Data Screen &lt;6&gt; and &lt;6.1&gt;, pgs. 89, 90, 92, and 94 – 95.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/06/2018</td>
<td><p>DG*5.3*935: Future Discharge Date Updates to Military Service Data Screen &lt;6&gt; and &lt;6.1&gt;, pgs. 88 – 90 and 92</p>
<p>Add Member ID to VistA Registration Banner - Every option that displays the patient’s information header will now also display the Electronic Data Interchange Personal Identifier (EDIPI), p. 3, p. 72, and p 73</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>09/06/2017</td>
<td>DG*5.3*940 Added “Permanent and Total Disabled” field value to Patient Inquiry sections 2.18, p. 6; 4.18, p. 48, and 4.19.4, p. 52; Added new enrollment status “CLOSED APPLICATION” with “ABANDONED APPLICATION” as the reason for closed application to Patient Enrollment Section 4.2, p. 14</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>09/06/2017</td>
<td>DG*5.3*936 ESCC Health Benefit Plan: Updates to Patient Inquiry sections 2.18, p. 6; 4.18, p. 47; 4.19.4, p. 52; and Eligibility Verification Data Screen &lt;11&gt;, p. 109</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>09/06/2017</td>
<td>DG*5.3*925 Enrollment System Community Care (ESCC) Add/Edit Address: Updates to Patient Demographic Data Screen &lt;1&gt;, p. 73; “Mailing” was added to Temporary Address throughout except for Tables 8 and 9, pages 70 and 71; and “Mailing” was added to Permanent Address throughout except for Patient Address Update, pages 9 and 71 and report content on page 64 and in Tables 8 and 9, pages 70 and 71</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>05/01/2017</td>
<td>DG*5.3*939 ESM Manage Date of Death in VistA: Updates to Patient Data Screen &lt;2&gt;, p 80</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/14/2017</td>
<td>DG*5.3*907 – Updated for Self-Identified Gender Identity and Birth Sex label, P 27, 72, and 73-74</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/2017</td>
<td>DG*5.3*903 – Add My HealtheVet Pre-register Information, p. 51, My HealtheVet Engagement Alert/Prompts, p. 52, My HealtheVet Registration Socialization Questions, p. 52, My HealtheVet Registration Fields Status and Updates, p 55, My HealtheVet Registration Fields Consistency Check, p. 56 .</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/2016</td>
<td><p>DG*5.3*926 documentation updates:</p>
<p>Added SUPPORTING DOCUMENT TYPE field (#.357) to Section “4.10, Death Entry”</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/29/2016</td>
<td><p>DG_5_3_887 and SD_5_3_619</p>
<p>Update made to PATIENT DEMOGRAPHIC DATA SCREEN, Appendix A, Registration Supplement, to show MUNVDE Preferred Language enhancement, pages 72 and 77</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>03/21/2016</td>
<td>DG*5.3*909 – Update Patient Enrollment and Register Patient screens to show new Camp Lejeune Data – section 4.2, pp. 13-14 and Appendix A, MILITARY SERVICE DATA SCREEN &lt;6&gt;, p. 89</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>01/07/2016</td>
<td><p>SQA review confirming DG*5.3*915 and DG*5.3*865 updates</p>
<p>TW review</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/17/2015</td>
<td>TW review: DG_53_P891</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/17/2015</td>
<td><p>Applied a template with numbered headings</p>
<p>Made corrections with direction from JG and UM for 865</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/17/2015</td>
<td>DG*5.3*891 host file, including DG*5.3*871, DG*5.3*901, DG*5.3*906,</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/17/2015</td>
<td>Updated with DG*5.3*865 enhancements for entering/editing an Email Address</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/8/2015</td>
<td><p>DG*5.3*915 - Enhancement to Register a Patient [DG REGISTER PATIENT] option to utilize the new Enterprise Registration processes improving the Veterans' experience at VA facilities by allowing new local patients to be looked up directly in the Master Veteran Index (MVI).</p>
<p>• Data from the new patient's MVI record is automatically imported into the local site as well as an attempt to obtain ESR data when possible.</p>
<p>• New process also allows for lookup and import of Department of Defense (DoD) data if the patient is a new patient to the VA system.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/5/2014</td>
<td><p>DG*5.3*858 – ESR 3.10</p>
<p>Veterans Financial Assessment – Discontinue Annual Means Test Renewal</p>
<p>Update to Overview Means Test User Menu options:</p>
<p>Add a New Means Test</p>
<p>Complete a Required Means Test</p>
<p>Edit an Existing Means Test</p>
<p>Hardships</p>
<p>Update to options:</p>
<p>Adjudicate a Means Test</p>
<p>Complete a Required Means Test</p>
<p>Edit an Existing Means Test</p>
<p>Hardships</p>
<p>Report – All Patients Flagged with a Bad Address</p>
<p>Supplement for Bad Address Indicator:</p>
<p>Screen 1, Data Group 4</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/10/2013</td>
<td><p>DG*5*3*867 - Caregiver Newborn Claims Processing</p>
<p>Added new Registration Supplement for Newborn.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/25/2012</td>
<td><p>DG*5.3*851 – ESR 3.8 Permanent Address Modifications</p>
<p>Update to options for functionality:</p>
<p>LOAD/EDIT PATIENT DATA</p>
<p>REGISTER A PATIENT</p>
<p>PREREGISTER A PATIENT</p>
<p>Update to Registration Supplement for temporary and confidential Addresses:</p>
<p>Screen 1, Data Group 5</p>
<p>Screen 1.1, Data Group 1</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>5/29/2012</td>
<td><p>DG*5.3*842 – ESR 3.6 VBA Pension Data Sharing</p>
<p>Minor updates to</p>
<p>ELIGIBILITY STATUS DATA, SCREEN &lt;7&gt;</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/26/2012</td>
<td><p>DG*5.3*842 – ESR 3.6 VBA Pension Data Sharing</p>
<p>Updated screen shots:</p>
<p>MILITARY SERVICE DATA, SCREEN &lt;6&gt;</p>
<p>ELIGIBILITY STATUS DATA, SCREEN &lt;7&gt;</p>
<p>Added new Pension and Dental fields to the Check Query Status list.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/26/2012</td>
<td><p>DG*5.3*841 changes (PL163-111)</p>
<p>Added Medal of Honor Data Group 9 to Screen &lt;6&gt;.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/19/2012</td>
<td><p>DG*5.3*797 changes</p>
<p>Added definitions for new Service Discharge Types: Dishonorable-VA and Honorable-VA.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/5/2011</td>
<td><p>DG*5.3*797 changes</p>
<p>TW Review, minor formatting</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/1/2011</td>
<td><p>DG*5.3*797 changes</p>
<p>Edit working of the Unsupported CV End Date Report description.</p>
<p>Updated Registration Screen 6</p>
<p>Added Screen 6.1 and 6.2</p>
<p>Added Service Discharge Types to include Dishonorable-VA and Honorable-VA</p>
<p>Added MSDS description of MSE changes</p>
<p>Removed second and third military service episodes</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/23/2011</td>
<td><p>DG*5.3*838</p>
<p>New field added</p>
<p>PATIENT file (#2)</p>
<p>SOURCE DESIGNATION field (#27.03)</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/25/2011</td>
<td><p>DG*5.3*840</p>
<p>New fields added to Patient and Patient Enrollment:</p>
<p>PATIENT file (#2)</p>
<p>CURRENT MOH INDICATOR field (#.541) PATIENT file (#2)</p>
<p>MEDAL OF HONOR INDICATED? field (#50.23) PATIENT ENROLLMENT file (#27.11)</p>
<p>Edited Copayment and Means Test Exemptions/Add a New Means Test sections regarding Catastrophically Disabled and Medal of Honor changes.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/27/2011</td>
<td><p>DG*5.3*754 – ESR 3.1 Changes</p>
<p>Removed Date of Death parameter (Enroll. App. Date) in the Death Entry section.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/18/2010</td>
<td><p>DG*5.3*754 – ESR 3.1 Changes</p>
<p>Added additional parameters to the Enroll Patient table entry in the Patient Enrollment section.</p>
<p>Added additional Date of Death parameters in the Death Entry section.</p>
<p>Added additional Date of Birth parameters to Screen 1, Data Group 1 section.</p>
<p>Added additional Date of Death condition to the Screen 7, Data Group 1 section for P&amp;T Effective Date, DATE RULED INCOMPETENT (CIVIL), DATE RULED INCOMPETENT (VA)</p>
<p>Added additional parameter to the Screen 10, Data Group 1 section for INELIGIBLE DATE.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/5/2009</td>
<td><p>DG*5.3*754 – ESR 3.1 Changes</p>
<p>Added new Special Treatment Authority Expiration date info for AO and SWAC to the Means Test User Menu section.</p>
<p>Updated Additional Patient Demographic Data screen 1.1 w/Confidential Phone.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/10/2009</td>
<td><p>DG*5.3*803 – Priority Group 8 Changes</p>
<p>Updated the GMT Thresholds Lookup by ZIP Code section with the new priority 8 sub-categories ‘b’ and ‘d’.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/24/2009</td>
<td><p>DG*5.3*808 – Enrollment VistA Changes Release 2 (EVC R2)</p>
<p>Removed reference to Rated Disability mail message sent in Registration Supplement, Screen 11, Data Group 4</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/30/2009</td>
<td><p>DG*5.3*688 – Enrollment VistA Changes Release 2 (EVC R2)</p>
<p>Updated Registration screens 1, 1.1, 6, 7, 8, 9 in Registration Supplement</p>
<p>Removed Copy Data function from income tests</p>
<p>Updated the following options: Patient Inquiry</p>
<p>Report-All Address Changes with Rx</p>
<p>Report-All Address Changes</p>
<p>View Patient Address</p>
<p>Added “Modify Means Test Data Collection – Means Test Version Indicator” to Overview Section</p>
<p>Changed “environmental contaminants” to “SW Asia Conditions”</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/29/2009</td>
<td>Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC)</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/29/2008</td>
<td>Updated Registration Supplement Section with missing information</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/14/2008</td>
<td>Minor Formatting Changes</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/11/2007</td>
<td><p>DG*5.3*653 – Enrollment VistA Changes Release 1 (EVC R1) Added Pseudo SSN Report (Patient) option.</p>
<p>Added Pseudo SSN Report for Means Test Dependents option.</p>
<p>Updated Registration Screens 1, 7, and 8 in the Registration Supplement section.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/19/2007</td>
<td><p>DG*5.3*657 – Update Data Entry Consistency Checks</p>
<p>Updated data group fields for Screens 6 &amp; 7 in the Registration Supplement section.</p>
<p>Added Pseudo SSN note to Overview and Registration Supplement sections.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/27/2006</td>
<td><p>DG*5.3*583 – Enable Upload of Claim Folder Location</p>
<p>Added list of acceptable Claim Folder Locations and Preferred Facilities.</p>
<p>Updated Patient Enrollment Option.</p>
<p>Updated Screen 7, Data Group 1, in Registration Supplement section.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/3/2006</td>
<td>DG*5.3*659 - Updated dependent effective date description for Screen 8 and radiation exposure method for Screen 6 in Registration Supplement section</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/23/2006</td>
<td>DG*5.3*716 – Revised Data Group 1 on Screen 11 in Registration Supplement section</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/4/2006</td>
<td>DG*5.3*689 – Enhancements to Registration Supplement Military Service Data Screen 6</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>9/13/2006</td>
<td>DG*5.3*673 – Added new registration menu Screen 6 – Military Service Data - for OEF/OIF in Registration Supplement section</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>7/14/2006</td>
<td>DG*5.3*694 – Added Invalid State/Inactive County Report option</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/7/2006</td>
<td><p>DG*5.3*611 – Fix Means Test Display</p>
<p>Updated Add a New Means Test, Add a Copay Exemption Test, Complete a Required Means Test, Edit a Copay Exemption Test, and Edit an Existing Means Test options</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/26/2006</td>
<td><p>DG*5.3*695 – Revised the following options for Permanent Address Update:</p>
<p>Register a Patient</p>
<p>Load/Edit Patient Data</p>
<p>Preregister a Patient.</p>
<p>Revised Patient Address Update option narrative for logical flow.</p>
<p>Revised Patient Demographics Screen &lt;1&gt; Date Group 4 in Registration Supplement section.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>2/21/2006</td>
<td><p>DG*5.3*672 – Enrollment VistA Changes Early Release</p>
<p>Updated table in Patient Enrollment option.</p>
<p>Updated screen example and Data Group 13 of Screen 6 in Registration Supplement section.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/9/2005</td>
<td><p>DG*5.3*658 – Address Updates</p>
<p>Added Patient Address Update option.</p>
<p>Added prompt to update permanent address through the following options:</p>
<p>Register a Patient</p>
<p>Load/Edit Patient Data</p>
<p>Preregister a Patient.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/14/2005</td>
<td>DG*5.3*655 – Remove Income Test Inconsistency Checks Updated Means Test User Menu options</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/26/2005</td>
<td><p>DG*5.3*677 – Emergency Response, Hurricane Katrina Project</p>
<p>Updated Patient Inquiry and Registration Screen 2 in Registration Supplement Section</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/12/2005</td>
<td><p>DG*5.3*624 – 10-10EZ 3.0 enhancements</p>
<p>Changed Printing Prompt Sequence in Financial Assessment Applications.</p>
<p>Added note for Roll-Up Means Test Dollar Amounts (GAI and NW) to conform with amounts on Feb 2005 VistA-Printed 10-10EZ/EZR Forms.</p>
<p>Added 10-10 Print – Means Test Selection (Test Director Defect #108) Selection List info under Register a Patient section.</p>
<p>Added “Print 1010EZ/EZR” as an available option under the Patient Enrollment section.</p>
<p>Added updates based on revised business rules for evaluating child(ren)’s Income Available to veteran and how it affects the Gross Annual Income dollar amounts printed on the 10-10EZ/EZR and displayed in the Child(ren)’s column on the Previous Calendar Year Gross Income Screen 2.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/26/2005</td>
<td>DG*5.3.*638 - Preventing Catastrophic Edits enhancements</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/21/2005</td>
<td>DG*5.3.*633 - Added All Patients flagged with a Bad Address option</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/28/2005</td>
<td>DG*5.3*563 - Date of Death enhancements</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/21/2005</td>
<td>Added 2 options - Percentage of Patients Pre-Registered Report and Report-All Address Change with Rx</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/5/2005</td>
<td><p>DG*5.3*628 - HVE Follow-up enhancements</p>
<p>Removal of AO Exposure Location Change Bulletin</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/23/2004</td>
<td>Manual updated to comply with SOP 192-352 Displaying Sensitive Data</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/5/2004</td>
<td>DG*5.3*564 - HEC VistA enhancements</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

Table 1: Description of the Actions Available through the Patient Enrollment Option

Table of Contents

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
  - [Modify Means Test Data Collection - Means Test Version Indicator](#modify-means-test-data-collection-means-test-version-indicator)
- [Registration Menu](#registration-menu)
  - [Disposition an Application](#disposition-an-application)
  - [Patient Enrollment](#patient-enrollment)
  - [Purple Heart Request History](#purple-heart-request-history)
  - [Purple Heart Status Report](#purple-heart-status-report)
  - [Add/Edit/Delete Catastrophic Disability](#addeditdelete-catastrophic-disability)
  - [Collateral Patient Register](#collateral-patient-register)
  - [Combat Vet Status Report](#combat-vet-status-report)
  - [Presumptive Psychosis Patient Registration](#presumptive-psychosis-patient-registration)
  - [Copay Exemption Test User Menu](#copay-exemption-test-user-menu)
    - [Add a Copay Exemption Test](#add-a-copay-exemption-test)
    - [Copay Exempt Test Needing Update at Next Appt.](#copay-exempt-test-needing-update-at-next-appt)
    - [Edit an Existing Copay Exemption Test](#edit-an-existing-copay-exemption-test)
    - [List Incomplete Copay Exemption Test](#list-incomplete-copay-exemption-test)
    - [View a Past Copay Test](#view-a-past-copay-test)
  - [Death Entry](#death-entry)
  - [Delete a Registration](#delete-a-registration)
  - [Disposition Log Edit](#disposition-log-edit)
  - [Edit Inconsistent Data for a Patient](#edit-inconsistent-data-for-a-patient)
  - [Eligibility Inquiry for Patient Billing](#eligibility-inquiry-for-patient-billing)
  - [Eligibility Verification](#eligibility-verification)
  - [Enter/Edit Patient Security Level](#enteredit-patient-security-level)
  - [Load/Edit Patient Data](#loadedit-patient-data)
  - [Means Test User Menu](#means-test-user-menu)
    - [Add a New Means Test](#add-a-new-means-test)
    - [Adjudicate a Means Test](#adjudicate-a-means-test)
    - [Complete a Required Means Test](#complete-a-required-means-test)
    - [Document Comments on a Means Test](#document-comments-on-a-means-test)
    - [Edit an Existing Means Test](#edit-an-existing-means-test)
    - [GMT Thresholds Lookup by Zip Code](#gmt-thresholds-lookup-by-zip-code)
    - [Hardships](#hardships)
    - [Pseudo SSN Report for Means Test Dependents](#pseudo-ssn-report-for-means-test-dependents)
    - [View a Past Means Test](#view-a-past-means-test)
  - [Patient Inquiry](#patient-inquiry)
  - [Preregistration Menu](#preregistration-menu)
    - [Display Preregistration Call List](#display-preregistration-call-list)
    - [Outputs for Preregistration](#outputs-for-preregistration)
    - [Supervisor Preregistration Menu](#supervisor-preregistration-menu)
    - [Patient Inquiry](#patient-inquiry-1)
    - [Preregister a Patient](#preregister-a-patient)
  - [Print Patient Wristband](#print-patient-wristband)
  - [Pseudo SSN Report (Patient)](#pseudo-ssn-report-patient)
  - [Register a Patient](#register-a-patient)
  - [Report - All Address Change with Rx](#report-all-address-change-with-rx)
  - [Report - All Address Changes](#report-all-address-changes)
  - [Report - All Patients flagged with a Bad Address](#report-all-patients-flagged-with-a-bad-address)
  - [Report - Patient Catastrophic Edits](#report-patient-catastrophic-edits)
  - [Unsupported CV End Dates Report](#unsupported-cv-end-dates-report)
  - [View Patient Address](#view-patient-address)
  - [View Registration Data](#view-registration-data)
- [Other Options](#other-options)
  - [Invalid State/Inactive County Report](#invalid-stateinactive-county-report)
  - [Patient Address Update](#patient-address-update)
- [Registration Menu Options](#registration-menu-options)
  - [Disposition an Application](#disposition-an-application-1)
  - [Patient Enrollment](#patient-enrollment-1)
  - [Purple Heart Request History](#purple-heart-request-history-1)
  - [Purple Heart Status Report](#purple-heart-status-report-1)
  - [Add/Edit/Delete Catastrophic Disability](#addeditdelete-catastrophic-disability-1)
  - [Collateral Patient Register](#collateral-patient-register-1)
  - [Combat Vet Status Report](#combat-vet-status-report-1)
  - [Presumptive Psychosis Reports](#presumptive-psychosis-reports)
    - [Presumptive Psychosis Fiscal Year Report](#presumptive-psychosis-fiscal-year-report)
    - [Presumptive Psychosis Gender Report](#presumptive-psychosis-gender-report)
    - [Presumptive Psychosis Patient Profile Report](#presumptive-psychosis-patient-profile-report)
    - [Potential Presumptive Psychosis Patient Report](#potential-presumptive-psychosis-patient-report)
    - [Presumptive Psychosis Status Report](#presumptive-psychosis-status-report)
    - [Presumptive Psychosis Statistical Report:](#presumptive-psychosis-statistical-report)
    - [Presumptive Psychosis Reconciliation Report](#presumptive-psychosis-reconciliation-report)
    - [Presumptive Psychosis Patient Detail Report](#presumptive-psychosis-patient-detail-report)
  - [Copay Exemption Test User Menu](#copay-exemption-test-user-menu-1)
    - [Add a Copay Exemption Test](#add-a-copay-exemption-test-1)
    - [Copay Exempt Test Needing Update at Next Appt.](#copay-exempt-test-needing-update-at-next-appt-1)
    - [Edit an Existing Copay Exemption Test](#edit-an-existing-copay-exemption-test-1)
    - [List Incomplete Copay Exemption Test](#list-incomplete-copay-exemption-test-1)
    - [View a Past Copay Test](#view-a-past-copay-test-1)
  - [Death Entry](#death-entry-1)
  - [Delete a Registration](#delete-a-registration-1)
  - [Disposition Log Edit](#disposition-log-edit-1)
  - [Edit Inconsistent Data for a Patient](#edit-inconsistent-data-for-a-patient-1)
  - [Eligibility Inquiry for Patient Billing](#eligibility-inquiry-for-patient-billing-1)
  - [Eligibility Verification](#eligibility-verification-1)
  - [Enter/Edit Patient Security Level](#enteredit-patient-security-level-1)
  - [Load/Edit Patient Data](#loadedit-patient-data-1)
  - [Means Test User Menu](#means-test-user-menu-1)
    - [Add a New Means Test](#add-a-new-means-test-1)
    - [Adjudicate a Means Test](#adjudicate-a-means-test-1)
    - [Complete a Required Means Test](#complete-a-required-means-test-1)
    - [Document Comments on a Means Test](#document-comments-on-a-means-test-1)
    - [Edit an Existing Means Test](#edit-an-existing-means-test-1)
    - [GMT Thresholds Lookup by Zip Code](#gmt-thresholds-lookup-by-zip-code-1)
    - [Hardships](#hardships-1)
    - [Pseudo SSN Report for Means Test Dependents](#pseudo-ssn-report-for-means-test-dependents-1)
    - [View a Past Means Test](#view-a-past-means-test-1)
  - [Patient Inquiry](#patient-inquiry-2)
  - [Preregistration Menu](#preregistration-menu-1)
    - [Display Preregistration Call List](#display-preregistration-call-list-1)
    - [Outputs for Preregistration](#outputs-for-preregistration-1)
    - [Supervisor Preregistration Menu](#supervisor-preregistration-menu-1)
    - [Patient Inquiry](#patient-inquiry-3)
    - [Preregister a Patient](#preregister-a-patient-1)
    - [My HealtheVet Engagement Alert/Prompts](#my-healthevet-engagement-alertprompts)
  - [Print Patient Wristband](#print-patient-wristband-1)
  - [Pseudo SSN Report (Patient)](#pseudo-ssn-report-patient-1)
  - [Register a Patient](#register-a-patient-1)
  - [Report - All Address Change with Rx](#report-all-address-change-with-rx-1)
  - [Report - All Address Changes](#report-all-address-changes-1)
  - [Report - All Patients flagged with a Bad Address](#report-all-patients-flagged-with-a-bad-address-1)
  - [Report - Patient Catastrophic Edits](#report-patient-catastrophic-edits-1)
  - [Unsupported CV End Dates Report](#unsupported-cv-end-dates-report-1)
  - [Former OTH Patient Eligibility Change Report](#former-oth-patient-eligibility-change-report)
  - [Former OTH Patient Detail Report](#former-oth-patient-detail-report)
  - [View Patient Address](#view-patient-address-1)
  - [View Registration Data](#view-registration-data-1)
- [Other Options](#other-options-1)
  - [Invalid State/Inactive County Report](#invalid-stateinactive-county-report-1)
  - [Patient Address Update](#patient-address-update-1)
  - [Other Than Honorable Former Service Members](#other-than-honorable-former-service-members)
This menu contains those options related to the processing of patient applications for care. This includes creation and editing of patient records, assigning a sensitive security level to certain patient records in order to restrict user access, registration and disposition, determination of need for and performance of Means Tests and Copay Tests, and updating eligibility status on a patient.
Central to just about all functions in the ADT system is the creation of patient records in your computer. This is usually accomplished through the Register a Patient option at the time a patient applies for care at your facility. If a patient is not applying for care, but you wish to enter them into your database, you should do so using the Load/Edit Patient Data option rather than Register a Patient.
The information necessary to create a patient's record is gathered and displayed via a series of formatted data screens. You see these screens in several other registration-related options, as well as Register A Patient and Load/Edit Patient Data. The information that is gathered on each patient depends upon their patient type assignment; i.e., non-service connected, service connected, employee, etc. There are a number of exported patient types. Your site also has the ability to enter its own. For each patient type, various Registration Screens may be turned OFF and ON depending upon what information is needed for that particular patient type. You find this more fully explained in the documentation pertaining to those options that utilize the screens.

## Modify Means Test Data Collection - Means Test Version Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Means Test version indicator is created and supports the display and collection of Means Test information for both the 1010EZ form prior to February 2005 and the 1010EZ form from February 2005. These modifications (outlined in Patches IVMB\*2\*860 and IVMB \*2\*886) support the February 2005 form. The Means Test information collected prior to installation of this patch continues to be collected, printed, and displayed in the February 2005 format.

Listed below, the following modifications created to display the Means Test version indicator VistA Options:

Load/Edit Patient \[DG LOAD PATIENT DATA\]

Register a Patient \[DG REGISTER PATIENT\]

Add a New Means Test \[DG MEANS TEST ADD\]

Complete a Required Means Test \[DG MEANS TEST COMPLETE\]

Edit an Existing Means Test \[DG MEANS TEST EDIT\]

View a Past Means Test \[DG MEANS TEST VIEW TEST\]

Purge Duplicate Income Tests \[DG CLEANUP INCOME TEST DUPES\]

Add a Copay Exemption Test \[DG CO PAY TEST ADD\]

Edit an Existing Copay Exemption Test \[DG CO PAY TEST EDIT\]

View a Past Copay Test \[DG CO PAY TEST VIEW TEST\]

The benefits for supporting the Means Test version indicator includes the following elements:

- Income Available Response collected for Dependent Child(ren) now supports collection of children Net Worth Dollar Amounts. Children Net Worth Dollar amounts are collected with the new form.
- A limit of 19 dependent children is collected for a Means Test. This limit applies to those dependents with relationships of son, daughter, step-son, and step-daughter.
- The collection of Previous Calendar Year Gross Annual Income with February 2005 Data format is changed to collect 3 data elements rather than the 10 data elements collected with the pre-February 2005 format.
- Means Test data collection collects the Gross Medical Expenses dollar amount, within Deductible Expenses, labeled as "Total Non-Reimbursed Medical Expenses.”
- February 2005 1010EZ form Means Test data collection no longer requires a spouse or dependent child (associated with the Means Test) to collect funeral and burial expenses.
- The collection of Previous Calendar Year Net Worth with February 2005 Data format is changed to collect 3 data elements rather than the 5 data elements collected with the pre-February 2005 format.
- The system continues to display the summary Income, Net Worth, and Deductible Expenses amounts in the February 2005 data collection format as was displayed with the pre-February 2005 data collection format. The system continues to calculate the summary Income, Net Worth, and Deductible Expense amounts in the February 2005 data collection format with the same formulas as with the existing data collection format.
- Entry of Means Test information in the February 2005 data collection format produces the same Means Test status that results when the Means Test information is entered with the existing data collection format.
- The "Copy Data" function is removed from the Means Test user interface for both February 2005 form and pre-February 2005 form. The "Copy Data" function is still performed by the Means Test system when done automatically. For example, if the Primary Eligibility Code changes from Non-Service Connected to Service Connected, a Pharmacy Copay test is automatically created. When this "automatic" copy occurs, the Annual Income information is checked for the data collection form. If that data is in pre-February 2005 form, it is converted to the February 2005 form to match the newly created Pharmacy Copay Test.

# Registration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following menus/options are included in the Registration menu.

A Registration Supplement is provided giving examples of each of the registration screens and descriptions of the data elements that are prompted for when using them.

PSEUDO SSN NOTE: For every option that displays the patient’s SSN, if the patient has a Pseudo SSN on file, the message \*\*Pseudo SSN\*\* displays next to the SSN.

Electronic Data Interchange Personal Identifier (EDIPI NOTE): For every option that displays the patient’s information header, the Electronic Data Interchange Personal Identifier (EDIPI) displays before the SSN. The display of the EDIPI is optional and this will only display if the patient has this information on file. Refer to the Patient Demographic Data Screen \<1\> on page 76.

## Disposition an Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter the final outcome of a registration; i.e., whether the patient was admitted, scheduled for a return visit, treated with no further care necessary, etc.

## Patient Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enroll patients that are eligible for care. This option is also used to expand an enrollment history record and update a patient's preferred facility.

## Purple Heart Request History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists the history entries of all updates to the Purple Heart Indicator, Status, and Remarks fields for an individual patient.

## Purple Heart Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists all patients who have a current Purple Heart status of *Pending* or *In Process*.

## Add/Edit/Delete Catastrophic Disability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter, edit, delete, and view a patient’s catastrophic disability (CD) information.

## Collateral Patient Register

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter a collateral patient into the system. The patient selected cannot be a veteran.

## Combat Vet Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a listing of veterans who have had their CV status entered, edited or deleted during a user specified time frame.

## Presumptive Psychosis Patient Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation of patch DG\*5.3\*1082, VistA users will no longer be prompted to enter this data; functionality has been moved to the VHA Enrollment System.

## Copay Exemption Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add a Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows adding a new Copay Test into the system.

### Copay Exempt Test Needing Update at Next Appt.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to generate a listing of future appointments listing Copay Exemption Tests that require updating.

### Edit an Existing Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to make changes to data in existing Copay Tests.

### List Incomplete Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to generate a listing of patients who have an incomplete Copay Test on file.

### View a Past Copay Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to view past Copay Test data.

## Death Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter, edit, or delete date of death information for a patient record.

## Delete a Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to delete a registration that was not dispositioned.

## Disposition Log Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to edit information appearing on the Disposition Log for selected patients.

## Edit Inconsistent Data for a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to run the Consistency Checker for a selected patient, edit their inconsistent/unspecified data, and update the INCONSISTENT DATA file accordingly.

## Eligibility Inquiry for Patient Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a quick reference to patient information used in determining appropriate patient billing.

## Eligibility Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter/edit a patient's eligibility data, as well as update their verification status without accessing their entire record.

## Enter/Edit Patient Security Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to restrict user access to computer records of certain patients by flagging them as sensitive. Access to such records is tracked and logged by the system.

## Load/Edit Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to edit a patient record.

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add a New Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to add a means test if the patient is subject to means testing and a means test does not exist for the current income year. You must hold the DG MEANSTEST security key in order to use this option.

### Adjudicate a Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows entry of final outcome of Means Tests referred to Adjudication. You must hold the DG MEANSTEST security key in order to use this option.

### Complete a Required Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows completion of Means Tests for patients in a required status, whose names appear on the Means Test List. The user may only complete the required means test if the test is less than 1 year old.

### Document Comments on a Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to add/edit/delete free-text comments on a selected Means Test.

### Edit an Existing Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to make changes to and/or view data in existing Means Tests that are less than 1 year old. A message asking the user to add a new means test displays if the test is older than 1 year old. You must hold the DG MEANSTEST security key in order to use this option.

### GMT Thresholds Lookup by Zip Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays GMT threshold values for valid zip code.

### Hardships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to grant hardships for the current income year Means Test.

### Pseudo SSN Report for Means Test Dependents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to print a report of dependents, sorted by patient, who have Pseudo SSNs.

### View a Past Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows viewing of past Means Tests data.

## Patient Inquiry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays current patient information including basic demographic information (including sexual orientation, sexual orientation free text, pronoun and pronoun description), inpatient status, future appointments, “Permanent and Total Disabled” field value, COMPACT Act Status, Episode Start date, Residential Remaining Days, End date and Source of Crisis End code, and VHA Profile (VHAP) currently assigned to the Veteran. Sexual Orientation, Sexual Orientation Free Text, Pronoun and Pronoun Description information is Read Only.

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Display Preregistration Call List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the Preregistration Call List in List Manager screen format.

### Outputs for Preregistration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Calling Statistics Report

This option prints the Preregistration Call Statistics report that provides a breakdown of the current entries in the PRE-REGISTRATION CALL LOG file (#41.43).

#### Percentage of Patients Preregistered Report

This option prints a report containing information on the number and percentages of preregistered patients for a user-defined date range.

#### Print Preregistration Audits

This option prints a report of audits from the PATIENT file that have to do with preregistration.

#### Source of Information Report

This report sorts through insurance policies in the patient file and print patients, bills, and payments with an insurance policy source of information equal to the user-selected criteria.

### Supervisor Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Add New Appointments to Call List

This option lets you add patients to the Preregistration Call List based on patient appointments on a user-specified search date.

#### Clear the Call List

This option deletes all entries in the PRE-REGISTRATION CALL LIST file (#41.42) regardless of the call status.

#### Purge Call Log

This option purges all entries prior to a user-specified date from the PRE-REGISTRATION CALL LOG file (#41.43).

#### Purge Contacted Patients

This option purges patients who were already contacted from the Preregistration Call List.

### Patient Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays registration information for a selected patient, including any preregistration items, and the Bad Address Indicator.

### Preregister a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lets you preregister a selected patient through the use of the Load/Edit process without using the Preregistration Call List.

## Print Patient Wristband

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print a patient wristband with barcoded social security number.

## Pseudo SSN Report (Patient)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to print a report that lists patients with Pseudo SSNs. It can be printed for veterans, non-veterans or both, and for all Pseudo SSN Reasons or a specific Pseudo SSN Reason.

## Register a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to create and/or edit a patient record while generating a registration (Application for Health Benefits). This registration must subsequently be dispositioned.

## Report - All Address Change with Rx

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists those patients with active pharmacy prescriptions whose primary address fields were changed during the previous 24 hours.

## Report - All Address Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be run from the Registration Menu or scheduled via Task Manager. If a patient’s mailing address is changed during the previous 24 hours, the report lists the patient mailing address as of now and the patient mailing address as of 24 hours ago. The output is sent to the DG DAILY ADDRESS CHANGE mail group.

## Report - All Patients flagged with a Bad Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists those patients flagged with a bad address indicator.

## Report - Patient Catastrophic Edits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print a report for a user-selected date range that provides a listing of patients who were flagged as having a potential catastrophic edit alert created for supervisory review.

## Unsupported CV End Dates Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HEC calculates and shares the CV End Date with VistA sites. Because VistA may not have Military Service Data (MSD) to support this determination, there may be some inconsistencies created at the VistA Site. This option runs a report helping the sites identify CV End Dates without the supporting MSD.

## View Patient Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows a user to view the patient's address along with the address change date, address change source, address change site (if applicable), and Bad Address Indicator.

## View Registration Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to view the data contained in a patient's record. Editing is not permitted through this option.

# Other Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Invalid State/Inactive County Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to create a report that lists patient records where the address fields contain invalid states and/or inactive counties.

## Patient Address Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to update the patient’s mailing address, temporary mailing address, or both.

The Patient Address Update \[DG ADDRESS UPDATE\] option resides in the OPTION \#19 file. At the discretion of the sites, this option may be placed on menus that belong to packages other than Registration.

# Registration Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Disposition an Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to record the final outcome of a patient’s application for health benefits (i.e., whether they were admitted, scheduled for a return visit, no treatment was necessary). Patients having open registrations (registrations that were not dispositioned) may not be reregistered until dispositioning is accomplished. You may obtain a list of those dispositions that are open or pending determination through the Pending/Open Disposition List option under the ADT Outputs menu.

- If applicable, you are afforded the opportunity to complete a Means Test.
- If the number of hours between registration and disposition is greater than the amount of time specified in the PIMS site parameter, TIME FOR LATE DISPOSITION, the “Reason for Late Disposition” prompt displays.

Following data entry, the system dispositions the application.

If the patient’s ENROLLMENT STATUS is REGISTRATION ONLY, the default value for the “TYPE OF BENEFIT APPLIED FOR:” prompt is set to “OUTPATIENT MEDICAL” and the default for “TYPE OF CARE APPLIED FOR:” prompt is set to “ALL OTHER”.

If the patient’s ENROLLMENT STATUS is REGISTRATION ONLY, and the “Do you want to be examined in the Medical Center today?” was answered “NO” or is blank, the default value for the STATUS prompt is set to “APPLICATION WITHOUT EXAM” and the default for “Select the type of disposition:” prompt is set to “CANCEL WITHOUT EXAM”.

If the patient’s ENROLLMENT STATUS is REGISTRATION ONLY, and the “Do you want to be examined in the Medical Center today?” was answered “YES”, the default value for the STATUS prompt is set to 10/10 VISIT.

An UNSCHEDULED (1010) VISIT OE/RR NOTIFICATION may display with V. 2.5 of Order Entry/Results Reporting. The disposition must have a change in status from APPOINTMENT W/O EXAM to 10/10 or UNSCHEDULED, in order for a notification to display. The notification only displays for patients who are defined in an OE/RR LIST entry and only displays to users defined in that list entry. Refer to the Order Entry/Results Reporting documentation for more information concerning OE/RR notifications, if needed.

When dispositioning a patient to admission, a warning displays and the admission process is bypassed if the patient is currently an inpatient or a lodger. If the patient is a lodger, he/she must be checked out as a lodger prior to being dispositioned. This can be accomplished through the Lodger Check-out option found in the Bed Control menu.

Depending on the type of disposition selected, other PIMS functionality may be accessed (i.e., Make Appointment). Refer to the appropriate option documentation, if necessary.

The eligibility code and period of service are now required before a registration can be dispositioned. These elements were previously checked at registration.

The validation logic performs the same validation checks as the Austin database to identify errors before they are transmitted. The validator (or edit checker) reviews the entire encounter rather than stopping after the first error is found. You may get the opportunity to correct these errors through this option.

The Veterans Healthcare Eligibility Reform Act of 1996, PL 104-262, prohibits providing care for veterans who are not enrolled after November 1, 1998 (with limited exceptions). The Disposition an Application option displays current enrollment information for the patient.

A preliminary priority value is calculated on an initial enrollment application if the patient wishes to enroll. In the case of EGT Type 2 (STOP NEW ENROLLMENTS THIS CYCLE), if the preliminary priority is at or below the latest EGT setting for a new enrollee or below the latest EGT for a current enrollee, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” is assigned. In the case of EGT Type 1 (ANNUAL FISCAL YEAR) or EGT Type 3 (MID-CYCLE), if the preliminary priority is below the latest EGT setting, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” is assigned. If the preliminary priority cannot be calculated or is calculated above the latest EGT setting, a preliminary Enrollment Category of “In Process” and a preliminary Enrollment Status of “Unverified” is assigned.

At verification, the HEC recalculates these fields based on a Master Veteran Record containing all nationally available patient data.

## Patient Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays a patient’s enrollment information. It is also used to expand an enrollment history record and update a patient’s preferred facility. The screens that may be displayed while utilizing this option are *Enrollment*, *Priority Factors*, and *Enrollment History*.

> **NOTE:** Actions that display on the screens enclosed in parentheses ( ) are not available for selection.

A preliminary priority value is calculated on an initial enrollment application. In the case of EGT Type 2 (STOP NEW ENROLLMENTS THIS CYCLE), if the preliminary priority is at or below the latest EGT setting for a new enrollee or below the latest EGT for a current enrollee, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” shall be assigned. In the case of EGT Type 1 (ANNUAL FISCAL YEAR) or EGT Type 3 (MID-CYCLE), if the preliminary priority is below the latest EGT setting, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” shall be assigned. If the preliminary priority cannot be calculated or is calculated above the latest EGT setting, a preliminary Enrollment Category of “In Process” and a preliminary Enrollment Status of “Unverified” shall be assigned. At verification, the HEC recalculates these fields based on a Master Veteran Record containing all nationally available patient data.

The CE Cease Enrollment functionality in this option was disabled. Veterans now sign a form declaring they want to cancel/decline, which is then faxed to the HEC for processing.

With the release of DG\*5.3\*906, Enrollment Enhancements – ACA – Affordable Care Act, the Cancel/Decline Reason code of “ACA Preference” is received from the HEC and viewable on the Patient Enrollment screen.

The following is a description of the actions available through this option.

<table>
<caption><p>Table 2: CD Option-Specific and Approved List Manager Actions and Mnemonics</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 18%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>Short Name</th>
<th>Full Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EP</td>
<td>Enroll Patient</td>
<td>This action is disabled. Users can no longer enroll a patient. Use the VHA Enrollment System to complete the enrollment process.</td>
</tr>
<tr class="even">
<td>PF</td>
<td>Preferred Facility</td>
<td><p>User can edit the treatment facility preferred by the patient when the SOURCE DESIGNATION is null, VistA, or PCP Inactive.</p>
<p><strong>Note:</strong> The Preferred Facility is locked when the SOURCE DESIGNATION is ESR or PCP Active.</p>
<p>The preferred facility must be an active facility and preferred facility type must be one of the following:</p>
<blockquote>
<p>Acronym Description</p>
<p>CBOC (Community Based Outpatient Clinic)</p>
<p>HCS (Health Care System)</p>
<p>HEALTHCARE (VA Boston Health Care System)</p>
<p>M&amp;ROC (Medical and Regional Office Center)</p>
<p>MOC (Mobile Outpatient Clinic)</p>
<p>MORC (Mobile Outreach Clinic)</p>
<p>NETWORK (VA Healthcare Network Upstate NY)</p>
<p>NHC (Nursing Home Care)</p>
<p>OC (Outpatient Clinic - Independent)</p>
<p>OCMC (Outpatient Clinic - Subordinate)</p>
<p>OCS (Outpatient Clinic Substation)</p>
<p>OPC (Out Patient Clinic)</p>
<p>ORC (Outreach Clinic)</p>
<p>RO-OC (Regional Office - Outpatient Clinic)</p>
<p>SATELLITE (Satellite Outpatient Clinic)</p>
<p>SOC (Satellite Outpatient Clinic)</p>
<p>VAMC (VA Medical Center)</p>
<p>VANPH (Neural Psychiatric Hospital)</p>
<p>VA ROSEBERG (VA Roseburg Health Care System)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>EH</td>
<td>Expand History</td>
<td>User can scroll through the enrollment history screens. This action is only available if the selected patient is already enrolled.</td>
</tr>
<tr class="even">
<td>SQ</td>
<td>Send Query</td>
<td>User can transmit an enrollment query. The software asks if you want to be notified when the query returns. The notification information is then displayed on the status bar.</td>
</tr>
<tr class="odd">
<td>CD</td>
<td>Catastrophic Disability</td>
<td>Works the same as the Add/Edit/Delete Catastrophic Disability menu option.</td>
</tr>
<tr class="even">
<td>SP</td>
<td>Select Patient</td>
<td>User can select another patient without leaving the Patient Enrollment option.</td>
</tr>
<tr class="odd">
<td>AU</td>
<td>View Upload Audit</td>
<td>Displays fields in the PATIENT file (#2) that are changed when a transaction is uploaded from the HEC.</td>
</tr>
<tr class="even">
<td>PZ</td>
<td>Print 1010EZ/EZR</td>
<td>User can print the 10-10EZ or 10-10EZR</td>
</tr>
<tr class="odd">
<td>QS</td>
<td>Check Query Status</td>
<td><p>User can check the status of an outstanding enrollment/eligibility query. The status bar displays the status of the last enrollment/eligibility query sent for the selected patient.</p>
<p>If HEC has an enrollment record for the patient being enrolled, the reply contains the patient's enrollment record.</p>
<p>If HEC has eligibility data on file, that data is also included in the query reply. The data is automatically uploaded for all fields in the PATIENT ENROLLMENT file (#27.11) and to the following fields in the PATIENT file (#2) (unless a problem is detected).</p>
<p>Eligibility Status Date</p>
<p>Eligibility Status</p>
<p>Eligibility Verif. Method</p>
<p>Date of Death</p>
<p>Claim Number</p>
<p>Claim Folder Location*</p>
<p>POW Status Indicated?</p>
<p>SC Award Date</p>
<p>Total Annual VA Check Amount</p>
<p>Veteran Y/N?</p>
<p>Service Connected?</p>
<p>Service Connected Percentage</p>
<p>Receiving a VA Pension?</p>
<p>Pension Award Effective Date</p>
<p>Pension Award Reason</p>
<p>Pension Terminated Date</p>
<p>Pension Terminated Reason 1</p>
<p>Pension Terminated Reason 2</p>
<p>Pension Terminated Reason 3</p>
<p>Pension Terminated Reason 4 Receiving A&amp;A Benefits?</p>
<p>Receiving Housebound Benefits?</p>
<p>Receiving VA Disability?</p>
<p>Military Disability Retirement</p>
<p>Discharge Due to Disability</p>
<p>Agent Orange Expos. Indicated?</p>
<p>Agent Orange Expos. Location</p>
<p>Radiation Exposure Indicated?</p>
<p>SW Asia Conditions</p>
<p>Camp Lejeune</p>
<p>Camp Lejeune Date</p>
<p>Camp Lejeune Change Site</p>
<p>Camp Lejeune Source Primary Eligibility Code</p>
<p>Patient Eligibilities</p>
<p>P&amp;T</p>
<p>Unemployable</p>
<p>Rated Incompetent?</p>
<p>Ineligible Date</p>
<p>Ineligible Reason</p>
<p>Ineligible VARO Decision</p>
<p>Eligible For Medicaid?</p>
<p>Preferred Facility</p>
<p>Rated Disabilities (VA) multiple, field .3721, multiple 2.04</p>
<p>Rated Disabilities (VA)</p>
<p>Disability %</p>
<p>Service Connected</p>
<p>Catastrophic Disability</p>
<p>Review Date</p>
<p>Decided By</p>
<p>Facility Making Determination</p>
<p>Date of Decision</p>
<p>Medal of Honor (MOH) Indicator</p>
<p>MOH Award Date</p>
<p>MOH Status Date</p>
<p>Source Designation</p>
<p>Class II Dental Indicator</p>
<p>Dental Appl Due Before Date</p></td>
</tr>
</tbody>
</table>

Table 2: CD Option-Specific and Approved List Manager Actions and Mnemonics

\* Marked for deletion

\*\* Uploaded data replaces existing data

For information about how a veteran's priority is derived, refer to the Enrollment Priority Algorithm portion of the ADTBE.pdf file. To upload patient demographic information, use the Demographics Upload option on the IVM Upload Menu. Refer to the IVM V. 2.0 User Manual for information about using this option, if necessary.

With the release of DG\*5.3\*940, VistA will receive, store, and display the new enrollment status “CLOSED APPLICATION” with “ABANDONED APPLICATION” as the reason for closed application. The new REASON FOR CLOSED APPLICATION field is a set of codes with current value of either null or 1 for “ABANDONED APPLICATION”.

With the release of DG\*5.3\*1104, Patient Enrollment screen \<2\> will display the COMPACT Status: Eligible, Not Eligible, or Undetermined. <span class="mark"></span>

## Purple Heart Request History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purple Heart Request History option is used to view the history of a Purple Heart request for an individual patient. The only prompts are for patient name and device.

Information provided includes station and division (at multi-divisional facilities), patient name and social security number, current Purple Heart indicator, status, remarks, and name of the individual who updated the information.

The STATUS field may contain the following values.

- Pending - set when the Current Purple Heart Indicator contains a YES value.
- In Process - set when message received from the HEC (Health Eligibility Center).
- Confirmed - set when confirmation message is received from the HEC.

The REMARKS field only contains a value if the CURRENT PURPLE HEART INDICATOR field is NO.

## Purple Heart Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to view a list of all patients with current Purple Heart requests with a status of *Pending* or *In Process*. The report is sorted by number of days since the last status change in either ascending or descending order (user-selected). The only prompts are for sort order and device.

Information provided includes station and division (at multi-divisional facilities), and for each request, patient name and social security number, days pending, and date pending. Totals are provided at the end of the report.

## Add/Edit/Delete Catastrophic Disability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add/Edit/Delete Catastrophic Disability option is used by holders of the proper security keys to add, edit, delete, and view a patient’s CD information created at their facility.

The DGENCD ADD/EDIT security key allows users to add and edit Catastrophic Disability Evaluations. The CD DELETE security allows users to delete Catastrophic Disability Evaluations.

CD can also be accessed from the Patient Enrollment option by entering CD from the list manager screen. A local user can add a CD evaluation only if:

- User holds the DGENCD ADD/EDIT security key
- CD evaluation does not currently exist for this person
- Current CD evaluation with a Method of Determination = Medical Record Review exists for this person

A local user can delete a CD evaluation only if: User holds the CD DELETE security key.

The local user can delete or edit a local CD evaluation with the Method of Determination = Physical Exam and Catastrophically Disabled? = YES, only if they answer a prompt saying they are making this change due to an entry error in the existing CD evaluation.

When CD information stored at their facility is edited or deleted, a mail message is sent to members of the DGEN ELIGIBILITY ALERT mail group.

The following is a list of the available CD option-specific and approved List Manager Actions and Mnemonics.

| Action                           | Mnemonic | Description                                                                                     |
|----------------------------------|----------|-------------------------------------------------------------------------------------------------|
| Add/Edit Catastrophic Disability | AE       | Users who hold the DGENCD ADD/EDIT security key can add a CD evaluation or edit an existing one |
| Delete Catastrophic Disability   | DE       | Users who hold the CD DELETE security key can delete an existing CD evaluation                  |

Table 3: CD Option-Specific and Approved List Manager Actions and Mnemonics Common to All Options

| Action                | Mnemonic | Description                                         |
|-----------------------|----------|-----------------------------------------------------|
| Next Screen           | \+       | Go to the next page of the list                     |
| Previous Screen       | –        | Go to the previous page of the list                 |
| Up a Line             | UP       | Move up one line in the list                        |
| Down a Line           | DN       | Move down one line in the list                      |
| Shift View to Right   | \>       | Move the display to see to the right                |
| Shift View to Left    | \<       | Move the display to see to the left                 |
| First Screen          | FS       | Go to the first page of the list                    |
| Last Screen           | LS       | Go to the last page of the list                     |
| Go to Page            | GO       | Go to a particular page in the list                 |
| Re Display Screen     | RD       | Clear and re-display the current screen             |
| Print Screen          | PS       | Print only the content of the current screen        |
| Print List            | PL       | Print the entire list                               |
| Search List           | SL       | Search the entire list for …                        |
| Auto Display (On/Off) | ADPL     | Turns on/off display of actions at bottom of screen |
| Quit                  | Q        | Quits the Application                               |

Table 4: Inconsistency Messages Caused by Data Entry Omissions or Mistakes

## Collateral Patient Register

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter a collateral patient into your system. A collateral patient is a non-veteran patient whose appointment is related to or associated with a veteran's treatment. The patient selected must have an eligibility code of COLLATERAL OF VET and a period of service of OTHER NON-VETERAN.

You may enter new patients as collaterals or designate patients already in your database as collaterals. If you enter a patient already in your database, the system checks data in the patient's file to determine if the patient meets the conditions that qualify the patient as a collateral patient. If the requirements are not met, a message is displayed on your screen and you are not permitted to proceed.

When entering a new patient as a collateral, the option prompts for the SELF-REPORTED REGISTRATION ONLY REASON, and the system sets the Enrollment Status to REGISTRATION ONLY.

You may also use this option to edit information pertaining to a collateral patient. In these cases, the existing information is shown as defaults.

## Combat Vet Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a listing of veterans who have had their CV status entered, edited or deleted during a user specified time frame. This option is included in the \[DG REGISTRATION MENU\] Registration Menu. Below is an example:

COMBAT VETERAN STATUS CHANGED REPORT Date: JUL 25, 2003

JUL 18, 2003 TO JUL 25, 2003 Page: 1

NAME SSN CV END DATE

PRIORITY GROUP

===================== ================= =============

SAMPLE, PT1 \###-##-####P MAY 28, 2005

NONE

SAMPLE, PT2 \###-##-#### DELETED!!!!

NONE

SAMPLE, PT3 \###-##-#### DELETED!!!!

1

SAMPLE, PT4 \###-##-#### JUN 04, 2002

3

## Presumptive Psychosis Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a listing of available Presumptive Psychosis Reports:

- Presumptive Psychosis Fiscal Year Report
- Presumptive Psychosis Gender Report
- Presumptive Psychosis Patient Profile Report
- Presumptive Psychosis Status Report
- Presumptive Psychosis Statistical Report

> **NOTE:** In order to make these new reports available to users, the menu \[DG PRESUMP. PSYCHOSIS REPORTS\] needs to be added as user’s either primary or secondary menu. If it was added to the secondary menu, then the user needs to enter the word “PRESUMPTIVE” to access the reports menu above.

### Presumptive Psychosis Fiscal Year Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides the number of male and female patients treated in fiscal year/quarter/month under the Presumptive Psychosis authority with a user-defined period. Totals are provided at the end of the report.

### Presumptive Psychosis Gender Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides the number of males, number of females, and total number of patients treated under the Presumptive Psychosis authority with a user-specified date range.

### Presumptive Psychosis Patient Profile Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides the following details of the patients treated under the Presumptive Psychosis authority:

- PATIENT NAME 
- PATIENT ID
- SERVICE SEPARATION DATE            
- DISCHARGE TYPE   
- PERIOD OF SERVICE     
- PRIMARY ELIGIBILITY  
- ENROLLMENT CATEGORY

This option provides a list of all patients treated under the Presumptive Psychosis authority who had an Outpatient Encounter with the STATUS = CHECKED OUT for a selected division within the user-specified date range.

Users can select a single division or multiple divisions.

This report can be sorted by division with a user-specified date range.

### Potential Presumptive Psychosis Patient Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a list of patients who are registered in VistA using all but one of the Presumptive Psychosis ‘workaround’ fields; these patients are missing the Presumptive Psychosis Category located in in VistAs patient registration screen seven (7).

Registration and Eligibility staff use this report to assign the correct Presumptive Psychosis category.

The date range entered is used to select the “last episode of care” and/or “released prescriptions”. The patient will not display on the report if there is no episode of care or released prescription within the date range.

### Presumptive Psychosis Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides the date and Presumptive Psychosis Category assigned to the patient eligible for Presumptive Psychosis authority.

This option provides a list of all patients treated under the Presumptive Psychosis authority and who had an Outpatient Encounter with the STATUS = CHECKED OUT for a selected division within the user-specified date range.

Users can select a single division or multiple divisions.

This report can be sorted by division with a user-specified date range.

### Presumptive Psychosis Statistical Report:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides the total number of patients treated under a different Presumptive Psychosis category and total number of patients seen under the Presumptive Psychosis authority with a user-specified date range.

### Presumptive Psychosis Reconciliation Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a list of patients registered under Presumptive Psychosis authority who have had episodes of care within the user specified date range.

The date range entered is used to select the “last episode of care” and/or “released prescriptions”. The patient will not display on the report if there is no episode of care or released prescription within the date range.

> **NOTE:** This is a stand-alone report that can be added manually to a user menu upon request.

### Presumptive Psychosis Patient Detail Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Generates a report of an individual patient treated under Presumptive Psychosis authority within the user specified date range.

> **NOTE:** This is a stand-alone report that can be added manually to a user menu upon request.

## Copay Exemption Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add a Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** With the installation of the Enrollment VistA Changes Release 2 (EVC R2) software (DG\*5.3\*688, IVM\*2.0\*115, and EAS\*1.0\*70), all Copay Tests added with this option are created in the FEB 2005 format.

The Add a Copay Exemption Test option is used to enter a new Copay Test into the system. Only one date of test should exist for a patient annually. The following rules apply to adding a Copay Test.

- Date of test cannot be before 10/29/92
- Date of test cannot be before the last date of test
- New date of test cannot be added if one exists in the last 365 days, unless it is a new calendar year

A Copay Test cannot be added for the following reasons:

- Patient is not a veteran.
- Patient does not have a Primary Eligibility Code.
- Patient is Service Connected 50-100%.
- Patient eligibility is NSC or SC 0% and Means Test options must be used instead of Copay options.
- Patient is receiving Aid and Attendance, automatically exempted.
- Patient is receiving Housebound Benefits, automatically exempted.
- Patient is receiving a VA Pension, automatically exempted.
- Patient is in a DOM ward, automatically exempted.
- Patient is an inpatient, automatically exempted.
- Patient was a POW, automatically exempted.
- Patient is Unemployable, automatically exempted.
- Patient is Catastrophically Disabled.
- Patient is awarded Medal of Honor.
- Patient is Registration only.

The Copay Exemption Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. After editing, each screen is refreshed with the new values. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Copay Exemption Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form.

If the veteran declines to provide financial information, the system:

- Bypasses the copay test screens
- Assigns a Copay Exemption Test status of NON-EXEMPT, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

#### Screen 1 – Marital Status/Dependents

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

The Marital Status/Dependents screen is used to enter data on the veteran's spouse and dependent children. Name, social security number, sex, and date of birth must be entered for the veteran's spouse and dependent children if it was not already filled in through registration. Spouse’s maiden name, address and telephone number may optionally be entered. The total allowed number of dependents is one (1) spouse and nineteen (19) children. Dependent’s (Child’s) address information may be optionally entered as well. This information is extremely important, as it is critical in determining the annual income thresholds for the veteran.

The system identifies whether the Spouse and/or Dependent Child(ren) were marked as included in the Copay Test with an “\*” in the column titled “MT”. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an “\*” in the column titled “Address”.

Spouse and dependent children income collection is dependent on several factors. The spouse's income need only be entered if the spouse lived with the veteran last calendar year or, if they did not live together, the veteran contributed to the spouse's support. The amount contributed to child support may be entered if the dependent did not live with the veteran last calendar year and “Yes” is entered for question, “Did you contribute to the child’s support?”. Dependent children income is only required if the child had income available to the veteran the last calendar year. The following is a brief explanation of some of the actions that may be taken.

- DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Copay Test.
- DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be used to delete duplicate dependents. In order to delete a dependent, they must be removed from every Copay Test (using the RE protocol).
- ED - Expand Dependent moves to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

#### Screen 2 - Previous Calendar Year Gross Income

The Previous Calendar Year Gross Income screen is used to enter income information, such as military retirement, total employment income, and social security. Some fields may be filled in from information collected in registration. Depending on the information entered on Screen 1, this screen may display with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/ dependents). When the Spouse and/or Dependent Child(ren) are marked (\*) as being included in the Copay Test and the child(ren)’s income is marked as available to the veteran, the system displays the Spouse and Children columns on the screen. If the Spouse and Children columns are not marked (no asterisk), the columns do not display.

> **NOTE:** The same rules apply to the printed 10-10EZ and 10-10EZR forms. The system does not print the Previous Calendar Year Gross Annual Income amounts for the Spouse and/or Dependent Child(ren) when they are not marked with an asterisk, as included in the Copay Test, regardless of whether or not the child(ren)’s income was marked as available to the veteran.

The required information is prompted for each column shown. The item number(s) you select for editing, may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three display.

#### Screen 3 - Deductible Expenses

The Deductible Expenses screen is used to enter any medical, funeral/burial expenses, and children's educational expenses. A child's educational expenses can only be claimed if the child had total employment income.

The Total Non-Reimbursed Medical Expenses (FEB 2005 format) amount is editable for the Means Test originating site. It is Display-Only for all others. When the veteran’s Copay Test data is updated by the VHA Enrollment System application, the Total Reimbursed Medical Expenses amount and all Copay Test data is Display-Only for all sites of record. The calculated Adjusted Medical Expenses amount is Display-Only for all sites of record.

- You may choose to print the 10-10EZR form when the Copay Test is completed.
- To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.
- Access to this option is limited to holders of the DG MEANSTEST security key.

### Copay Exempt Test Needing Update at Next Appt.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Copay Exempt Test Needing Update At Next Appt. option is used to generate a listing of future appointments for a selected date range. The output lists copay exemption tests that require updating by appointment time.

You may select to report one/many/all divisions and one/many/all clinics. The output includes the date range, report run date, clinic name, and division. Patient name, patient ID, appointment date/time, Copay Test status, and date of last Copay Test are provided for each patient listed.

### Edit an Existing Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit an Existing Copay Exemption Test option is used to make changes to data in existing Copay Tests. It may also be used to complete Copay Tests on patients. Only the latest Copay Test may be edited.

The Copay Exemption Test information is based on the last calendar year and is entered through a series of screens, if the veteran agrees to provide financial information. After editing, each screen is refreshed with the new values. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Copay Exemption Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

- Bypasses the copay test screens
- Assigns a Copay Exemption Test status of NON-EXEMPT, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

The Edit an Existing Copay Exemption Test option operates similarly to the Add a Copay Exemption Test option. Edit an Existing Copay Exemption Test option is the only option that allows changes to completed Copay Tests. After these changes are entered, the system re-determines the patient's Copay status and changes it, if necessary.

The date(s) and name(s) of individual(s) making changes is recorded by the system and may be seen through the View Copay Exemption Test Editing Activity option.

A patient may apply for a Copay Test under the following conditions.

- An existing Copay Exemption Test may be edited for patients who meet the following criteria:
1.  Applicant is a veteran
2.  Applicant's primary or other eligibility does NOT contain:
1.  service connected 50% to 100% or
2.  aid and attendance or
3.  housebound or
4.  VA pension
- Primary eligibility is NSC and a Means Test is not required
- Veteran is NOT awarded Medal of Honor
- Applicants who answered NO to receiving A&A, HB, or pension
- Applicants, who did not answer YES to: Veteran Catastrophically Disabled?
- Applicants, who previously qualified and applied for a Copay exemption, still qualify, and were not Copay Tested in the past year

If these criteria change, a Copay Test status of NO LONGER APPLICABLE is assigned to the Copay Test. Tests with this status CANNOT be edited.

The following is a brief explanation of some of the actions that may be taken on Screen 1 - Marital Status/Dependents.

- DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Copay Test.
- DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality is used to delete duplicate dependents. In order to delete a dependent, the dependent must be removed from every Copay Test (using the RE protocol).
- ED - Expand Dependent moves to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran).

> **NOTE:** Expand Dependent may also be used to display the dependent demographic data, including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

Depending on the information entered on Screen 1, Screen 2 may display with one column - veteran; two columns - veteran/spouse; or three columns - veteran/spouse/dependents. The required information is prompted for each column shown. The item number(s) selected for editing, may be preceded by V (veteran), S (spouse), or C (children), in order to select those specific fields; otherwise, the fields for all three display.

- Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.
- You may print the 10-10EZR form when the Copay Test is complete.
- To print the 10-10EZ form, you must first answer “No” or “N” to the question: “Print 10-10EZR? Yes//”.
- Because the Copay Exemption Tests (before FEB 2005 format) Gross Annual Income (GAI) and Net Worth (NW) money categories in VistA do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA printing software does:
1.  Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar amount in block “*3. LIST OTHER INCOME AMOUNTS (Social Security, compensation, pension, interest, dividends.) EXCLUDING WELFARE.*” of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
- \[1\] Social Security (Not SSI) +
- \[2\] U.S. Civil Service +
- \[3\] U.S. Railroad Retirement +
- \[4\] Military Retirement +
- \[5\] Unemployment Compensation +
- \[6\] Other Retirement +
- \[8\] Interest, Dividend, Annuity +
- \[9\] Worker’s Comp or Black Lung
3.  Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar amount in block “*1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)*” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
- \[1\] Cash, Amts in Bank Accts +
- \[2\] Stocks and Bonds
4.  Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar amount in block “*3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)*” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
- \[4\] Other Property or Assets
- \[5\] Debts

You may not edit or delete a Copay Exemption Test that was created at another VAMC and distributed by the HEC.

Access to this option is limited to holders of the DG MEANSTEST security key.

### List Incomplete Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Incomplete Copay Exemption Test option is used to generate a listing of patients who have an incomplete Copay Test on file. The patient name, patient ID number, source of test, and date of test are provided. The patients are listed in alphabetical order on the output.

You are prompted for the Copay Test status, a date range, and a device.

### View a Past Copay Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View a Past Copay Test option is used to view past Copay Tests data. The option does not allow editing. You are prompted for the patient's name and the date of the Copay Test to view. A question mark (?) entered at the date prompt provides a list of the selected patient's Copay Test dates.

If certain circumstances exist for the selected patient, messages may display. A message is printed if no detailed income information is on file for the veteran, or if the veteran's Copay Test status is NO LONGER APPLICABLE. Since income data can be entered/edited through registration, once a Copay Test has this status, the income data being viewed may differ from that originally entered as part of the Copay Test.

You can view the following three Copay Test screens through this option.

1.  Screen 1 - Marital Status/Dependents
2.  Screen 2 - Previous Calendar Year Gross Income
3.  Screen 3 - Deductible Expenses

## Death Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Death Entry option is used to enter, edit, or delete date of death information entered at your site for a patient. If you attempt to enter an inpatient, you are prompted to discharge the patient through the Bed Control Menu. You must hold the DG DETAIL security key in order to access this option.

When a date of death is entered or updated, the system prompts you to provide the source of notification and the supporting document type for the date of death. Once the date of death, the source of notification and the supporting document type are entered, the software records the date of last entry or update on the DATE OF DEATH field and information about the local submitter (user) making the entry or change.

The date of death must be precise.

- It cannot be prior to the P&T date (if a P&T date is on file)
- It cannot be prior to the Date Ruled Incompetent (VA) (if one is on file)
- It cannot be prior to the Date Ruled Incompetent (Civil) (if one is on file)

Once a date of death is entered into the system, the message "\[PATIENT DIED ON {date}\] PATIENT HAS DIED" displays whenever the patient's name is entered through other options.

You can use this option to delete a date of death entered in error at your site by entering “@” at the “DATE OF DEATH: \[date\]//” prompt, and responding “Yes” when asked, “Are you sure you want to delete the Date of Death?” This deletes the entries for the specified patient in the DATE OF DEATH (#.351), DEATH ENTERED BY (#.352), SOURCE OF NOTIFICATION (#.353) and SUPPORTING DOCUMENT TYPE (#.357) fields of the PATIENT (#2) file. It updates the DATE OF DEATH LAST UPDATED (#.354) field with the date and time the date of death was deleted. It updates the LAST EDITED BY (#.354) field with the User ID of the user who deleted the date of death.

The MVI (Master Veteran Index) becomes the authoritative source for Date of Death information. If the Date of Death was received by VistA with the Last Edited By field entry of someone other than a defined user at the site, i.e., Postmaster, a message is received when trying to edit the Date of Death field. The message reads “YOU MAY NOT EDIT DATE OF DEATH IF IT WAS NOT ENTERED BY A USER AT THIS SITE”.

When you enter, edit, or delete a date of death through this option, a MailMan message is sent to members of the mail group identified in the DEATH GROUP (#500) field in the MAS PARAMETERS (#43) file; to notify them of future clinic appointments and/or scheduled admissions for the patient. It also includes source of notification for date of death, date of last entry or update, and local submitter/user information. Future admissions are automatically cancelled, but clinic appointments must be cancelled through the appropriate Scheduling option. When the date of death is the same as the discharge date, the mail message indicates that the patient died while an inpatient.

## Delete a Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete a Registration option is used to delete patient registrations that were not dispositioned.

When a registration is deleted using this option, all information on the selected patient remains on file. The system only removes records of the patient registered on that particular date.

You may enter double question marks (??) at the "PATIENT NAME" prompt to obtain a list of patients with open registrations. Once the patient name is entered, information concerning the undispositioned registration displays.

## Disposition Log Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Disposition Log Edit option is used to edit the disposition record of a patient registration.

The system displays each data field of the disposition record for editing. The values that were entered at the time of registration and disposition display as defaults. You may accept the default or enter new information. Based on the information entered/edited through this option, the system re-categorizes the registration in the appropriate AMIS 401-420 segment.

An UNSCHEDULED (1010) VISIT OE/RR NOTIFICATION may display with V. 2.5 of Order Entry/Results Reporting. The disposition must have a change in status from APPOINTMENT W/O EXAM to 10/10 or UNSCHEDULED, in order for a notification to display. The notification displays only for patients who are defined in an OE/RR LIST entry and displays only to users defined in that list entry. Refer to the Order Entry/Results Reporting documentation for more information concerning OE/RR notifications, if needed.

The validation logic performs the same validation checks as the Austin database to identify errors before they are transmitted. The validator (or edit checker) reviews the entire encounter rather than stopping after the first error is found. You may get the opportunity to correct these errors through this option.

You are prompted to indicate if treatment was related to Military Sexual Trauma (MST), only if the patient’s MST Status is YES.

## Edit Inconsistent Data for a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to edit data for patients who were identified as having missing/inconsistent data in their files through the use of the Consistency Checker. The data items display for updating. If you do not hold the DG ELIGIBILITY security key, you are not able to edit certain data items. Those items display followed by an asterisk (\*). Items that are displayed with two asterisks (\*\*) can only be updated using the appropriate PIMS menu options. When updating is complete, the system again searches the patient's file for any remaining inconsistent/unspecified data items.

The Consistency Checker feature provides a method of better assuring accuracy of the data contained in patients' records. It looks at data items to assure entries are consistent with entries in other data fields. It also checks certain data items to be sure they were not left blank. Your site may or may not choose to use this feature by setting the CONSISTENCY CHECKER field in the MAS Parameter Entry/Edit option. Further, your site may specify from a list of data items, those that the Consistency Checker checks. Some items, however, are automatically set by the PIMS software to be checked/not checked. Specifying the data elements is accomplished through the Determine Inconsistencies to Check/Don't Check option. If your site has the Consistency Checker turned OFF, you are not able to fully utilize this option.

Each of the inconsistent/unspecified data elements are prompted for updating. Refer to the Registration Supplement if you need assistance in responding to these prompts. At the conclusion of updating, the consistency checker runs once again to check for any remaining inconsistent/unspecified data elements.

The Consistency Checker places the names of those patients whose records contain inconsistent/unspecified data in the INCONSISTENT DATA file (#38.5). When the data is corrected through this option, the names are automatically removed from the file. Names contained in this file display on the Inconsistent Data Elements Report.

Although the process of updating the INCONSISTENT DATA file is automatic when using this option, it is not automatic when data is entered/edited through other PIMS options (except options that utilize the load/edit registration screens). Three options found on the Inconsistency Supervisor Menu of the Supervisor ADT menu are dedicated to keeping the INCONSISTENT DATA file up to date for such records. It is important to note that entries in the INCONSISTENT DATA file may not be accurate. Inconsistent data can be updated through options that do not involve the Consistency Checker (i.e., FileMan). By using the options available on the Inconsistency Supervisor Menu, the INCONSISTENT DATA file can be kept up to date.

Whenever inconsistent/unspecified data items remain in a patient's file, either by selecting not to edit it or not holding the DG ELIGIBILITY key, a MailMan message is generated. This message is sent to the Inconsistency Edit mail group specified through the Bulletin Selection option. There are three possible messages that may be sent: an initial message when inconsistencies are first found, a reminder message if inconsistencies were reported more than seven days ago and remain unresolved, and an updated message if inconsistencies were previously reported (and not updated) and additional inconsistencies were found. If an initial MailMan message was sent within the past seven days and no new inconsistencies were found, no MailMan message is sent.

## Eligibility Inquiry for Patient Billing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Eligibility Inquiry for Patient Billing option provides a quick reference to patient information used in determining appropriate patient billing. The output may display the following elements, where applicable.

- Means Test - status and date last Means Test performed
- health insurance - insurance company, policy number, group number, holder
- agent orange and ionizing radiation exposure
- Camp Lejeune eligibility
- Acute Suicidal Crisis open episode status
- MOH Indicator, MOH Award Date, MOH Status Date, MOH Copayment Exemption Date
- Medicaid eligibility
- primary and other eligibility codes
- service-connected percentage
- rated disabilities

Once the patient name is entered, the output is automatically displayed.

## Eligibility Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Eligibility Verification option is used to enter/edit/verify data pertaining to a patient's rated disabilities and service record. It allows for entry, edit, and viewing of the following registration screens, as applicable, according to site parameters set up by PATIENT TYPE.

PATIENT DEMOGRAPHIC DATA 1

ADDITIONAL PATIENT DEMOGRAPHIC DATA 1.1

PATIENT DATA 2

MILITARY SERVICE DATA 6

ELIGIBILITY STATUS DATA 7

FAMILY DEMOGRAPHIC DATA 8

INCOME SCREENING DATA 9

INELIGIBLE/MISSING DATA 10

ELIGIBILITY VERIFICATION DATA 11

Entry/edit of most of the data in this option is restricted to holders of the DG ELIGIBILITY security key once eligibility is verified. Until it is verified, it may be entered/edited by any user; after verification, all users may view but only those with the security key may edit. Verification of data takes place through the ELIGIBILITY VERIFICATION DATA (Screen 11) and must be accomplished by a holder of the DG ELIGIBILITY security key.

This option works in the same manner as the Register a Patient and Load/Edit Patient Data options. A patient name is entered, and the various screens appropriate for that patient are presented. Registration screens 1, 1.1, 2, and 7 always display. The display of screens 6, and 8 through 11 vary depending on PATIENT TYPE. This is due to your site's ability to turn these screens OFF and ON during the registration process depending upon whether the information collected through them is pertinent to the PATIENT TYPE. If necessary, you may refer to the Registration Supplement for further explanation of this function.

You may edit the data shown on the screens by selecting the number(s) of the data group(s) you want to edit; move to another screen by entering up-arrow screen number \<^#\> to specify the screen; move to the next screen by entering a \<RET\>; or quit by entering an up-arrow \<^\>. Should you select to enter/edit data, each appropriate field of the data group selected is prompted. Any previously entered data is shown as a default. When editing is complete, the screen redisplays with the newly entered data shown.

If your site has the Consistency Checker function turned ON, the system performs a check for inconsistent/unspecified data elements at the conclusion of the verification process. If any inconsistent/unspecified data elements are found, you get the opportunity to make the necessary corrections. If the Consistency Checker is not turned ON, the message "CONSISTENCY CHECKER TURNED OFF!!" displays at the conclusion of the process.

## Enter/Edit Patient Security Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit Patient Security Level option is used to assign/remove a level of sensitivity to a patient record. Use of this option enters the patient into the DG SECURITY LOG file. Any access of a sensitive patient record is tracked in this file. The DG SECURITY LOG file also contains the name of the person who assigned the security and when the security was assigned.

With the initialization of ADT V. 3.6, all existing patients with an eligibility code of employee were automatically entered into the security log as sensitive by the system. This is not automatic for employee patients subsequently entered into the system.

Accessing a sensitive patient record can trigger sending different messages and bulletins.

Only holders of the DG SENSITIVITY security key may access this option.

## Load/Edit Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Load/Edit Patient Data option is used to enter, edit, and view information contained in a patient's record without making a registration entry in the Disposition Log or creating a 10/10 Form (Application for Health Benefits). You may also make HINQ inquiries and print patient data cards. The records of existing patients may be edited, but new patient records may not be entered into the system with this option.

After you select this option, patient demographic, enrollment, eligibility, COMPACT Act episode of care data, and emergency response indicator(s) information displays. If the patient is deceased, date of death information (including source of notification for date of death, date of last entry or update, and local submitter/user information) also displays. The date of death information is Read Only.

If the user chooses not to upload the date of death from the HEC, a mail message is sent to the members of the DGEN ELIGIBILITY ALERT mail group telling them to contact the HEC to explain why they did not accept the date of death.

Prior to entering patient data, the mailing address is displayed and the user is asked, *Do you want to edit the Patient's Mailing Address?*

- If the user answers YES, the system prompts each address field and the user is allowed to update the patient’s mailing address information.
  - The address entered by the user is then sent to the Universal Address Module (UAM) Validation Service and the results of the address validation are displayed to the user. The user selects the address they want to store and press enter.
  - The old and the new address information is displayed and the system asks the user *Are you sure that you want to save the above changes?*
  - If the user answers YES, the system displays “Change saved”, the patient’s mailing address change date/time stamp is updated, and a trigger is set to send a message to the HEC.

> **NOTE:** It takes an actual change to the mailing address to update the mailing address change date/time stamp. If there were no changes to the mailing address information, and the user responds YES; no updates are made to the mailing address fields or mailing address change date/time stamp and a message is not triggered to the HEC.

5.  If the user answers NO, the system displays “Change aborted”. Neither the patient’s mailing address information nor the mailing address change date/time stamp is updated and a message is not triggered to the HEC.
- If the user answers NO at the *Do you want to edit the Patient's Mailing Address?* prompt, the system does not prompt the user for address information and the system continues the Load/Edit Patient Data process.

Entry/edit of a patient's record is done via a series of formatted data screens. There are a total of fifteen screens distributed with the PIMS Package. Screens 12-14 are informational only. The enter/edit process is not the same for every patient, nor for every user due to several variables that exist in the system. Your site has the ability to create its own additional screen, in order to capture certain information it may need or to capture information in a different format. It has the ability to turn certain data screens ON and OFF according to Patient Type. Within the screens, it may specify which data groups may be entered/edited. The DG ELIGIBILITY security key also plays a role in your ability to enter/edit data. Depending upon whether or not eligibility was verified, certain information may only be edited by a user holding this security key.

In order to prevent catastrophic edits to a patient’s identity, four patient identity fields were established. They are patient name (first and/or last name components), social security number, date of birth, and birth sex. If modifications are made to two or more of these fields within one edit session, a warning alert displays. If you proceed with the edits, an alert with the potential patient catastrophic edits is forwarded to your site’s ADPAC and appropriate supervisor for review and action. In addition, the after edits of the patient identification fields displays an asterisk to highlight the edited fields that were modified when the alert was generated. The alerts remain on file for one year.

The HIGH INTENSITY field in the MAS Parameters is provided to assist you in the identification of those fields that may/may not be edited. If this field is set to YES at your facility, the number next to those data groups that may be edited, in boldface type; those that are un-editable do not (excluding Screen 8). For those sites not using High Intensity, numbers of data groups that may be edited are enclosed in \[ \]s, while those that are un-editable are enclosed in \< \>s (excluding Screen 8).

The Registration Supplement provides an example of each data screen and a description of each associated field. Refer to Appendix A: Registration Supplement when entering or editing patient information.

If your site has the Consistency Checker function turned ON, the system performs a check for inconsistent/unspecified data elements at the conclusion of the entry/edit process. If any inconsistent/unspecified data elements are found, you get the opportunity to make the necessary corrections.

The system also determines a patient’s need for Means Testing and Copay Testing and, if necessary, allow you to complete the required test. For the Copay Test, the veteran has to request the test. For instructions on Means Test, refer to the Add a New Means Test or Complete a Required Means Test options. For instructions on Copay Test, refer to the Add a New Copay Test option.

Screen 8 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items. The following is a brief explanation of some of the actions listed on this screen.

- DD - In order to edit the dependent demographics, the selected dependent has to be active.
- DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality is used to delete duplicate dependents. In order to delete a dependent, they must be removed from every Means Test.
- ED - Expand Dependent moves to another screen. It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).
- MT - Used to enter/edit last year's marital status for the veteran.
- AD - This protocol is not selectable from the registration screens.
- RE - This protocol is not selectable from the registration screens.

With the installation of the Veteran Identification Card (VIC) software, the prompt “Download VIC data?” was added, to allow you to download the selected patient’s demographic data to the photo capture station. The existing “EMBOSS DATA CARD?” prompt was changed to “EMBOSS (OLD) DATA CARD?”.

Catastrophically Disabled Review Date displays after patient demographic and eligibility data.

A query is automatically sent to the Health Eligibility Center (HEC) when this option is utilized. This query determines if a Means Test or Copay Exemption Test (with Income Screening information) was completed for the veteran for a specified income year. The HEC processes the query, and if there is a completed Means Test or Copay Exemption Test (with Income Screening information), the HEC transmits the Primary test and any Hardship determinations to the VAMC that sent the query.

The veteran’s Long Term Care (LTC) copayment status and last test date display when using this option.

- If the last test is over a year old, the message “\*\*NEW TEST REQUIRED\*\*” displays.
- If the veteran did not agree to pay the copayments, the following ineligible message displays.

> Patient INELIGIBLE to Receive LTC Services -- Did Not Agree to Pay Copayments

## Means Test User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add a New Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** With the installation of the Enrollment VistA Changes Release 2 (EVC R2) software (DG\*5.3\*688, IVM\*2.0\*115, and EAS\*1.0\*70), all Means Tests added with this option are created in the FEB 2005 format.

The Add a New Means Test option is used to enter a new Means Test into the system. Only one date of test should exist for a patient annually. The following rules apply to adding a Means Test.

- the date of test cannot be before 7/1/86
- the date of test cannot be before the last date of test
- a new date of test cannot be added if one exists in the last 365 days, unless it is a new calendar year

Reasons a Copay Test cannot be added:

- primary eligibility is NOT NSC or 0% service-connected non-compensable
- receives disability retirement from the military
- is eligible for Medicaid
- is on a domiciliary ward
- was Means Tested in the past year
- is a Purple Heart recipient
- is Catastrophically Disabled
- MOH Indicator is “YES”
- Registration Only record

The Means Test information is based on the last calendar year and is entered through a series of screens, when the veteran agrees to provide financial information. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Means Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

When the veteran declines to provide financial information, the system:

- Bypasses the means test screens
- Assigns a means test status of MT COPAY REQUIRED, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “NO, I DO NOT WISH TO PROVIDE INFORMATION…” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If it is necessary to refer the case to adjudication, the system prompts *Do you wish to send this case to adjudication?*

- If YES is entered, the veteran is placed in MT Copay Required status until determination is returned from adjudication.
- If NO is entered, the system makes the final determination that the veteran is MT Copay Required.

If the veteran's Means Test status is PENDING ADJUDICATION, the veteran is tentatively placed in MT Copay Required status and must agree to pay the deductible.

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

Screen1  
MaritalStatus/Dependents is used to enter data on the veteran's spouse and dependent children. Name, social security number, sex, and date of birth must be entered for the veteran's spouse and dependent children, if not already filled in through registration. Spouse’s maiden name, address and telephone number may optionally be entered. The total allowed number of dependents is one (1) spouse and nineteen (19) children. Dependent’s (Child’s) address information may be optionally entered as well. This information is extremely important as it is critical in determining the annual income thresholds for the veteran.

The system identifies whether the Spouse and/or Dependent Child(ren) were marked as included in the Means Test with an “\*” in the column titled “MT”. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an “\*” in the column titled “Address”.

Spouse and dependent children income collection is dependent on several factors. The spouse's income need only be entered, if the spouse lived with the veteran last calendar year or, if they did not live together, the veteran contributed to the spouse's support. The amount contributed to child support may be entered if the dependent did not live with the veteran last calendar year and “Yes” is entered for question, *Did you contribute to the child’s support?*. Dependent children income is only required if the child had income that was available to the veteran last calendar year. The following is a brief explanation of some of the actions that may be taken.

- DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Means Test.
- DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality is used to delete duplicate dependents. In order to delete a dependent, they must be removed from every Means Test (using the RE protocol).
- ED - Expand Dependent moves to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

Screen2  
PreviousCalendarYearGrossIncome is used to enter income information, such as military retirement, total employment income, and social security. Some fields may be filled in from information collected in registration. Depending on the information entered on Screen 1, this screen may display with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/dependents). When the Spouse and/or Dependent Child(ren) are marked (\*) as included in the Means Test and the child(ren)’s income was marked as available to the veteran, the system displays the Spouse and Children columns on the screen. If they are not marked (no asterisk), they do not display.

> **NOTE:** The same rules apply to the printed 10-10EZR and 10-10EZ forms. The system does not print the Previous Calendar Year Gross Annual Income amounts for the Spouse and/or Dependent Child(ren) when they are not marked with an asterisk, as included in the Means Test, regardless of whether or not the child(ren)’s income was marked as available to the veteran.

The required information is prompted for each column shown. The item number(s) you select for editing may be preceded by V (veteran), S (spouse), or C (children) to select the specific fields; otherwise, the fields for all three display.

Screen3  
DeductibleExpenses is used to enter any medical, funeral/burial expenses, and children's educational expenses. A child's educational expenses can only be claimed if the child had total employment income.

The Total Non-Reimbursed Medical Expenses (FEB 2005 format) amount is editable for the Means Test originating site. It is Display-Only for all others. When the veteran’s Means Test data is updated by the VHA Enrollment System application, the Total Reimbursed Medical Expenses amount and all Means Test data is Display-Only for all sites of record. The calculated Adjusted Medical Expenses amount is Display-Only for all sites of record.

Screen4  
PreviousCalendarYearNetWorth is used to enter such information as stocks and bonds, real property, bank accounts, and debts. Depending on the information entered on Screen 1, this screen may display with one column (veteran) or up to three columns (veteran/spouse/dependent children). When the Spouse and/or Dependent Child(ren) are marked (\*) as included in the Means Test, the system displays the Spouse and/or Dependent Child(ren) column on the screen. If they are not marked (no asterisk), it does not display. The same rules apply to the printed 10-10EZ and 10-10EZR forms. The system does not print the Previous Calendar Year Net Worth amount~~s~~ for the Spouse and/or Dependent Children when they are not marked with an asterisk as included in the Means Test.

The item number(s) you select for editing may be preceded by V (veteran) or S (spouse) or C (Children) to select those specific fields; otherwise, the fields for all display. The required information is prompted for each column shown.

When adding a Means Test, completion of the test is optional; however, the marital and dependent children sections must be completed, in order to complete the Means Test. For MT Copay Exempt veterans, the net worth must also be entered. If you choose not to complete the Means Test, it may be completed later through either option, Complete a Required Means Test or Edit an Existing Means Test.

You may choose to print the 10-10EZR form when the Means Test is completed or print the prior Means Test (if one exists) at the beginning of the option.

> **NOTE:** To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.

Access to this option is limited to holders of the DG MEANSTEST security key.

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

### Adjudicate a Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Adjudicate a Means Test option is used to enter the patient's Means Test category into the system when the determination is returned from Adjudication. Only patients who currently have the Means Test status of PENDING ADJUDICATION and less than 1 year old from the means test effective, date may be selected.

A patient's Means Test may be referred to Adjudication for Means Test Category determination when income alone places the veteran in MT Copay Exempt status, but income plus net worth (property) is equal to or greater than the allowable threshold.

If a change is made that involves the MT Copay Required Means Test status, a bulletin may be generated informing the user and advising review of the MT Copay Required charges for the selected patient.

Access to this option is limited to holders of the DG MEANSTEST security key.

### Complete a Required Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Complete a Required Means Test option is used to complete Means Tests generated through registration or by other circumstances. Only Means Test records with a status of REQUIRED and less than 1 year old from the effective date may be completed.

The Means Test information is based on the last calendar year and is entered through a series of screens if the veteran agrees to provide financial information. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Means Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

- Bypasses the means test screens
- Assigns a means test status of MT COPAY REQUIRED, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If it is necessary to refer the case to adjudication, the system prompts *Do you wish to send this case to adjudication?*

- If YES is entered, the veteran is placed in MT Copay Required status until determination is returned from adjudication.
- If NO is entered, the system makes the final determination that the veteran is MT Copay Required.

If the veteran's Means Test status is PENDING ADJUDICATION, the veteran is tentatively placed in MT Copay Required status and must agree to pay the deductible.

If the veteran does not agree to pay the deductible, a message is printed in the signature block for the deductible on the 10-10EZ.

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

Screen1  
MaritalStatus/Dependents is used to enter data on the veteran's spouse and dependent children. Name, social security number, sex, and date of birth must be entered for the veteran's spouse and dependent children, if not already filled in through registration. Spouse’s maiden name, address and telephone number may optionally be entered. The total allowed number of dependents is one (1) spouse and nineteen (19) children. Dependent’s (Child’s) address information may be optionally entered as well. This information is extremely important as it is critical in determining the annual income thresholds for the veteran.

The system identifies whether the Spouse and/or Dependent Child(ren) are marked as included in the Means Test with an “\*” in the column titled “MT”. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an “\*” in the column titled “Address”.

Spouse and dependent children income collection is dependent on several factors. The spouse's income need only be entered, if the spouse lived with the veteran during the last calendar year or, if they did not live together, the veteran contributed to the spouse's support. The amount contributed to child support may be entered, if the dependent did not live with the veteran last calendar year and “Yes” is entered for question, “Did you contribute to the child’s support?”. Dependent children income is only required if the child had income that was available to the veteran last calendar year. The following is a brief explanation of some of the actions that may be taken.

- DD - In order to edit the dependent demographics, the selected dependent has to be active and associated with the Means Test.
- DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality should be used to delete duplicate dependents. In order to delete a dependent, they must be removed from every Means Test (using the RE protocol).
- ED - Expand Dependent moves to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).

Screen2  
PreviousCalendarYearGrossIncome is used to enter income information such as military retirement, total employment income, and social security. Some fields may be filled in from the information collected in registration. Depending on the information entered on Screen 1, this screen may display with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/dependents). When the Spouse and/or Dependent Child(ren) are marked as included in the Means Test and the child(ren)’s income is marked as available to the veteran, the system displays the Spouse and Children columns on the screen. If they are not marked (no asterisk), they do not display.

> **NOTE:** The same rules apply to the printed 10-10EZR and 10-10EZ forms. The system does not print the Previous Calendar Year Gross Annual Income amounts for the Spouse and/or Dependent Child(ren) when they are not marked with an asterisk, as included in the Means Test, regardless of whether or not the child(ren)’s income was marked as available to the veteran.

The item number(s) you select for editing, may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three display. The required information is prompted for each column shown.

Screen3  
DeductibleExpenses is used to enter any medical, funeral/burial expenses, and children's educational expenses. A child's educational expenses can only be claimed, if the child had total employment income available.

The Gross Medical Expenses amount (Before FEB 2005 format) or Total Non-Reimbursed Medical Expenses (FEB 2005 format) amount is editable only by the Means Test originating site. It is Display-Only for all others. When the veteran’s Means Test data is updated by the VHA Enrollment System application, the Gross Medical Expenses amount or Total Non-Reimbursed Medical Expenses amount and all Means Test data is Display-Only for all sites of record. The calculated Adjusted Medical Expenses amount is Display-Only for all sites of record.

For Means Tests done prior to the existence of the Gross Medical Expenses amount, the system re-calculates and presents the Gross Medical Expenses amount from the patient’s existing Medical Expenses amount. For these historical Means Tests, the existing Medical Expenses amount becomes the Adjusted Medical Expenses amount. If and when the Gross Medical Expenses amount is updated, the system automatically re-calculates the Adjusted Medical Expenses amount.

Screen4  
PreviousCalendarYearNetWorth is used to enter such information as stocks and bonds, real property, bank accounts, and debts. Depending on the information entered on Screen 1, this screen may display with one column (veteran) or up to three columns (veteran/spouse/dependent children). When the Spouse and/or Dependent Child(ren) are marked (\*) as included in the Means Test, the system displays the Spouse and/or Dependent Child(ren) column on the screen. If they are not marked (no asterisk), it does not display. The same rules apply to the printed 10-10EZ and 10-10EZR forms. The system does not print the Previous Calendar Year Net Worth amount~~s~~ for the Spouse and/or Dependent Children when they are not marked with an asterisk as included in the Means Test.

> **NOTE:** The Previous Calendar Year Net Worth screen (Before FEB 2005 format) does not support the entry of separate Dependent Child(ren) net worth dollar amounts (i.e., have a column for Children). Consequently, a negative Income Available response does not affect the display or printing of the Net Worth dollar amounts on the printed 10-10EZ/EZR forms.  
  
Any Means Test data collected from a mailed registration form or during a walk-in/face-to-face presentation of a veteran for Dependent Child(ren) Net Worth is manually added into the Veteran amounts and entered as a totaled dollar amount.  
  
Any Means Test data collected from an on-line submission of a 10-10EZ application of a veteran for Dependent Child(ren) Net Worth is automatically added into the Veteran totaled Net Worth amounts by the EAS software.

The item number(s) you select for editing may be preceded by V (veteran), S (spouse) and C (children) to select those specific fields; otherwise, the fields for all display. The required information is prompted for each column shown.

Completion of the Means Test through this option is mandatory. The Means Test status automatically updates, once editing is complete.

You may choose to print the 10-10EZR form when the Means Test is completed.

> **NOTE:** To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.

Because the Means Tests (before FEB 2005 format) Gross Annual Income (GAI) and Net Worth (NW) money categories in VistA do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA printing software does:

- Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar amount in block “3. LIST OTHER INCOME AMOUNTS (Social Security, compensation, pension, interest, dividends.) EXCLUDING WELFARE.” of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
1.  \[1\] Social Security (Not SSI) +
6.  \[2\] U.S. Civil Service +
7.  \[3\] U.S. Railroad Retirement +
8.  \[4\] Military Retirement +
9.  \[5\] Unemployment Compensation +
10. \[6\] Other Retirement +
11. \[8\] Interest, Dividend, Annuity +
12. \[9\] Worker’s Comp or Black Lung
- Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar amount in block “1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
1.  \[1\] Cash, Amts in Bank Accts +
13. \[2\] Stocks and Bonds
- Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar amount in block “3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
1.  \[4\] Other Property or Assets +
14. \[5\] Debts

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

### Document Comments on a Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Document Comments on a Means Test option is used to add/edit/delete comments to an existing Means Test. This allows the user to enter any pertinent information concerning the selected Means Test, such as efforts made to obtain Means Test information.

You are prompted for the patient name and the Means Test date. The latest Means Test date displays as the default. A question mark (?) may be entered to obtain a list of Means Test dates for that patient. Comments may be added through a word-processing field. Existing comments can be edited or deleted.

### Edit an Existing Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit an Existing Means Test option is used to make changes to data in existing Means Tests less than 1 year old from the effective date. It may also be used to complete Means Tests on patients identified through Registration as requiring Means Testing. Only the latest Means Test may be edited. A Means Test that was verified by the HEC and its corresponding original VAMC Means Test are both un-editable. If you choose such a Means Test, the system displays a message containing this information. However, this option lets you view or print such a test.

The Means Test information is based on the last calendar year and is entered through a series of screens, if the veteran agrees to provide financial information. Based on the financial information entered and the income thresholds established, the system:

- Determines the appropriate Means Test status for the patient
- Prints an “X” next to the paragraph that begins “*YES, I WILL PROVIDE SPECIFIC INCOME AND/OR ASSET INFORMATION TO ESTABLISH MY ELIGIBILITY FOR CARE. …*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

If the veteran declines to provide financial information, the system:

- Bypasses the means test screens
- Assigns a means test status of MT COPAY REQUIRED, which means that the veteran is required to pay a copayment
- Prints an “X” next to the paragraph that begins “*NO, I DO NOT WISH TO PROVIDE INFORMATION…*” in the FINANCIAL DISCLOSURE section of the 10-10EZ or 10-10EZR form

The Edit an Existing Means Test option operates similarly to the Add a New Means Test and Complete a Required Means Test options; however, it is the only option that allows changes to Completed Means Tests. After these changes are entered, the system re-determines the patient's Means Test category and changes it, if necessary. If additional information is needed to make a determination or if it is necessary to refer the case to adjudication, the system prompts accordingly.

The date(s) and name(s) of individual(s) making changes is recorded by the system and may be seen through the View Means Test Editing Activity option.

A Means Test is required under the following conditions.

- primary eligibility is NSC or 0% service-connected non-compensable
- does not receive disability retirement from the military
- is not eligible for Medicaid
- is not on a domiciliary ward
- was not Means Tested in the past year
- is NOT awarded Medal of Honor
- is NOT a Purple Heart recipient
- is NOT catastrophically disabled

Should these criteria change (excluding the last two), a Means Test status of NO LONGER REQUIRED is assigned to the Means Test. Tests with this status cannot be edited.

Depending on the information entered on Screen 1, Screen 2 may display with one column - veteran; two columns - veteran/spouse; or three columns - veteran/spouse/dependents. The item number(s) you select for editing, may be preceded by V (veteran), S (spouse), or C (children) to select those specific fields; otherwise, the fields for all three display.

Screen 4 may display with one or two columns (Before FEB 2005 format) or three columns (FEB 2005 format). The item number(s) you select for editing may be preceded by V (veteran) or S (spouse) or C (children) to select those specific fields; otherwise, the fields for all display. The required information is prompted for each column shown.

Screen 1 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

You may print the 10-10EZR form when the Means Test is complete.

> **NOTE:** To print the 10-10EZ form, you must first answer “No” or “N” to the question, “Print 10-10EZR? Yes//”.

Because the Means Tests (before FEB 2005 format) Gross Annual Income (GAI) and Net Worth (NW) money categories in VistA do not exactly match the money categories on the paper Feb 2005 10-10EZ/EZR forms, the VistA printing software does:

- Add the following VistA screen money categories (separately for veteran, spouse and each dependent child) and print the totaled dollar amount in block “3. LIST OTHER INCOME AMOUNTS (Social Security, compensation, pension, interest, dividends.) EXCLUDING WELFARE.” of the Previous Calendar Gross Annual Income section of the 10-10EZ and 10-10EZR forms:
1.  \[1\] Social Security (Not SSI) +
15. \[2\] U.S. Civil Service +
16. \[3\] U.S. Railroad Retirement +
17. \[4\] Military Retirement +
18. \[5\] Unemployment Compensation +
19. \[6\] Other Retirement +
20. \[8\] Interest, Dividend, Annuity +
21. \[9\] Worker’s Comp or Black Lung
- Add the following VistA screen money categories (separately for veteran and spouse) and print the totaled dollar amount in block “1. CASH AMOUNT IN BANKS (e.g., checking and savings accounts, certificates of deposit, individual retirement accounts, stocks and bonds)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
1.  \[1\] Cash, Amts in Bank Accts +
22. \[2\] Stocks and Bonds
- Subtract the following VistA screen money categories (separately for veteran and spouse) and print the resulting dollar amount in block “3. VALUE OF OTHER PROPERTY OR ASSETS (e.g., art, rare coins, collectables) MINUS THE AMOUNT YOU OWE ON THESE ITEMS. INCLUDE VALUE OF FARM, RANCH OR BUSINESS ASSETS. Exclude household effects and family vehicles.)” of the Previous Calendar Net Worth section of the 10-10EZ and 10-10EZR forms:
1.  \[4\] Other Property or Assets +
23. \[5\] Debts

Access to this option is limited to holders of the DG MEANSTEST security key.

#### How to Correct Means Test Inconsistency Errors

There are two types of conditions that cause the inconsistency messages.

1.  Data entry omissions or mistakes (error numbers 1-4 in Table 1)
4.  Erroneous or corrupted data filed in the records (error numbers 5-17 in Table 2)

> **NOTE:** Only the Primary site for the Means Test can correct the inconsistent data.

<table>
<caption><p>Table 5: Inconsistency Messages Caused by Erroneous or Corrupted Data</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 36%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>Error Name</th>
<th>Description</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p>Dependent (&lt;dependent type&gt;) transmitted without SSN</p></li>
</ol></td>
<td><p>A dependent is added to an Income Test without entering the Social Security Number (SSN). The dependent's relationship is displayed in the message to facilitate its update.</p>
<p>Examples:</p>
<ul>
<li><p>Dependent (SON) transmitted without SSN</p></li>
<li><p>Dependent (DAUGHTER) transmitted without SSN</p></li>
<li><p>Dependent (STEPDAUGHTER) transmitted without SSN</p></li>
</ul></td>
<td><ol type="1">
<li><p>Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p></li>
<li><p>From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Dependent Demographic (DD) action to enter the SSN for the dependent who generated the inconsistency message.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li><p>Two dependents transmitted with same SSN</p></li>
</ol></td>
<td>Data values in the SOCIAL SECURITY NUMBER field (#.09) in the INCOME PERSON file (#408.13) for at least two dependents are identical.</td>
<td><ol type="1">
<li><p>Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p></li>
<li><p>From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Dependent Demographic (DD) action to check the SSN for each of the dependents listed on the test.</p></li>
<li><p>Update the invalid SSN for the dependent who generated the inconsistency message.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="3" type="1">
<li><p>Should not have income data if Child Had Income is “NO”</p></li>
</ol></td>
<td><ul>
<li><p>The dependent is not the spouse,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>The INCOME AVAILABLE TO YOU field (#.12) in the INCOME RELATION file (#408.22) is “NO”,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>Any of the income or net worth fields in the INDIVIDUAL ANNUAL INCOME file (#408.21) for the dependent contain any amount. (Any entry including a zero [$0] is a valid amount.)</p></li>
</ul>
<p>When the INCOME AVAILABLE TO YOU field (#.12) is set to “NO”, and there are income and net worth entries for the dependent, the amounts are not visible on either the INCOME or NET WORTH screens.</p></td>
<td><ol type="1">
<li><p>Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p></li>
<li><p>From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Dependent Demographic (DD) action to change the INCOME AVAILABLE TO YOU field to “YES”.</p></li>
<li><p>Go to the GROSS INCOME (#2) and NET WORTH (#4) screens and delete the amounts entered for the dependent.</p></li>
<li><p>Go back to the MARITAL STATUS/DEPENDENTS SCREEN (#1); use the Dependent Demographic (DD) action to change the INCOME AVAILABLE TO YOU field (#.12) back to “NO”.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="4" type="1">
<li><p>No income data allowed if spouse didn't live w/vet &amp; Veteran did not provide support</p></li>
</ol></td>
<td><ul>
<li><p>The data value in the INCOME RELATION file (#408.22) LIVED WITH PATIENT field (#.06) is "NO", <strong>and</strong></p></li>
<li><p>The DID YOU PROVIDE SUPPORT field (#.21) value is “NO”,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>Any of the income or net worth fields in the INDIVIDUAL ANNUAL INCOME file (#408.21) for the spouse contain any amount. Any entry including a zero ($0) is a valid amount.</p></li>
</ul>
<p>When the LIVED WITH PATIENT field is set to “NO”, and DID YOU PROVIDE SUPPORT is “NO”, and there are income and net worth entries for the dependent, the amounts are not visible on either the INCOME or NET WORTH screens.</p></td>
<td><ol type="1">
<li><p>Use the appropriate menu option (from the Means Test User Menu, Edit an Existing Means Test, or from the Copay Exemption Test Menu, Edit an Existing Copay Exemption Test).</p></li>
<li><p>From the MARITAL STATUS/DEPENDENTS SCREEN (#1), use the Marital/Dependent Info (MT) action to change the LIVED WITH PATIENT to “YES”.</p></li>
<li><p>Go to the GROSS INCOME (#2) and NET WORTH (#4) screens and delete the amounts entered for the spouse.</p></li>
<li><p>Go back to the MARITAL STATUS/DEPENDENTS SCREEN (#1) and use the Marital/Dependent Info (MT) action to change the LIVED WITH PATIENT to “NO”.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
</tbody>
</table>

Table 5: Inconsistency Messages Caused by Erroneous or Corrupted Data

Checks 5 through 9 in the table below are performed for Means Tests and Copay Exemption Tests when one or more of the following fields in the ANNUAL MEANS TEST file (#408.31) contains data:

- HARDSHIP? Field (#.2)
- HARDSHIP REVIEW DATE Field (#.21)
- SITE GRANTING HARDSHIP Field (#2.04)
- HARDSHIP EFFECTIVE DATE Field (#2.01)

<table>
<caption><p>Table 6: Types of Reports with Descriptions</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 39%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th>Error Name</th>
<th>Description</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol start="5" type="1">
<li><p>Missing Hardship Indicator</p></li>
</ol></td>
<td><ul>
<li><p>The Hardship Indicator, HARDSHIP? field (#.2) is NULL,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>At least one of the other Hardship-related fields contains data.</p></li>
</ul>
<p>If any of the following three fields has an entry, a value must be entered in all three:</p>
<ul>
<li><p>HARDSHIP?</p></li>
<li><p>SITE GRANTING HARDSHIP</p></li>
<li><p>HARDSHIP EFFECTIVE DATE</p></li>
</ul>
<p>The HARDSHIP REVIEW DATE field is <strong>not</strong> a part of the criteria for this inconsistency message.</p></td>
<td>Use the VHA Enrollment System to edit the Hardship record to enter the missing data.</td>
</tr>
<tr class="even">
<td><ol start="6" type="1">
<li><p>Missing Site Granting Hardship</p></li>
</ol></td>
<td><p>The SITE GRANTING HARDSHIP field (#2.04) is NULL, and at least one of the other Hardship-related fields contains data.</p>
<p>If any of the following three fields has an entry, a value must be entered in all three:</p>
<ul>
<li><p>HARDSHIP?</p></li>
<li><p>SITE GRANTING HARDSHIP</p></li>
<li><p>HARDSHIP EFFECTIVE DATE</p></li>
</ul>
<p>The HARDSHIP REVIEW DATE field is <strong>not</strong> a part of the criteria for this inconsistency message.</p></td>
<td>Use the VHA Enrollment System to edit the Hardship record to enter the missing data.</td>
</tr>
<tr class="odd">
<td><ol start="7" type="1">
<li><p>Missing Hardship Effective Date</p></li>
</ol></td>
<td><ul>
<li><p>The HARDSHIP EFFECTIVE DATE field (#2.01) is NULL,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>The year in the DATE OF TEST field (#.01) is the year 2000 or later,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>At least one of the other Hardship-related fields contains data.</p></li>
</ul>
<p>Starting in the year 2000, all hardships must have an effective date.</p>
<p>If any of the following three fields has an entry, a value must be entered in all three:</p>
<ul>
<li><p>HARDSHIP?</p></li>
<li><p>SITE GRANTING HARDSHIP</p></li>
<li><p>HARDSHIP EFFECTIVE DATE</p></li>
</ul>
<p>The HARDSHIP REVIEW DATE field is <strong>not</strong> a part of the criteria for this inconsistency message.</p></td>
<td>Use the VHA Enrollment System to edit the Hardship record to enter the missing data.</td>
</tr>
<tr class="even">
<td><ol start="8" type="1">
<li><p>Invalid Hardship Effective Date</p></li>
</ol></td>
<td><ul>
<li><p>The date in the HARDSHIP EFFECTIVE DATE field (#2.01) could not be converted into FileMan format, <strong>and</strong></p></li>
<li><p>At least one of the other Hardship-related fields contains data.</p></li>
</ul></td>
<td>Use the VHA Enrollment System to edit the Hardship record to enter the missing data.</td>
</tr>
<tr class="odd">
<td><ol start="9" type="1">
<li><p>Hardship Effective Date earlier than Means Test Date</p></li>
</ol></td>
<td><ul>
<li><p>The HARDSHIP EFFECTIVE DATE field (#2.01) is <strong>not</strong> NULL,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>The date is prior to the date in the DATE OF TEST field (#.01) in the ANNUAL MEANS TEST file (#408.31),</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>At least one of the other Hardship-related fields contains data.</p></li>
</ul></td>
<td>Use the VHA Enrollment System to edit the Hardship record to enter the missing data.</td>
</tr>
<tr class="even">
<td><ol start="10" type="1">
<li><p>Source of Test must be identified</p></li>
</ol></td>
<td><p>The SOURCE OF INCOME TEST field (#.23) in the ANNUAL MEANS TEST file (#408.31) does <strong>not</strong> contain one of the following values found in the SOURCE OF INCOME TEST file (#408.34):</p>
<ul>
<li><p>VAMC (#1)</p></li>
<li><p>IVM (#2)</p></li>
<li><p>DCD (#3)</p></li>
<li><p>OTHER FACILITY (#4)</p></li>
</ul></td>
<td><ol type="1">
<li><p>From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p></li>
<li><p>Press &lt;Enter&gt;.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="11" type="1">
<li><p>Site Conducting Test must be identified</p></li>
</ol></td>
<td><p>The SITE CONDUCTING TEST field (#2.05) in the ANNUAL MEANS TEST file (#408.31) is NULL</p>
<p><strong>and</strong></p>
<p>the SOURCE OF INCOME TEST field (#.23) is OTHER FACILITY.</p></td>
<td>The means test can only be corrected at the site where it was entered/completed.</td>
</tr>
<tr class="even">
<td><ol start="12" type="1">
<li><p>Incorrect Means Test Status for Test-Determined Status</p></li>
</ol></td>
<td><ul>
<li><p>The INCOME field (#.04) in the ANNUAL MEANS TEST file (#408.31) is greater than the THRESHOLD A field (#.12),</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>The HARDSHIP? field (#.2) is "NO" or NULL,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>the ADJUDICATION DATE/TIME field (#.1) is NULL,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>The TEST-DETERMINED STATUS field (#2.03) is neither MT COPAY REQUIRED ("C") nor PENDING ADJUDICATION ("P").</p></li>
</ul></td>
<td><ol type="1">
<li><p>From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p></li>
<li><p>Press &lt;Enter&gt;.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="13" type="1">
<li><p>Invalid Means Test Status for Test-Determined Status</p></li>
</ol></td>
<td><p>The TEST-DETERMINED STATUS field (#2.03) in the ANNUAL MEANS TEST file (#408.31) does not contain a valid value:</p>
<ul>
<li><p>MT COPAY EXEMPT (A)</p></li>
<li><p>MT COPAY REQUIRED (C)</p></li>
<li><p>PENDING ADJUDICATION (P)</p></li>
<li><p>GMT COPAY REQUIRED (G)</p></li>
</ul>
<p>This is caused when there is an error in the calculation of the Test-Determined Status due to corruption in the Means Test data.</p></td>
<td><ol type="1">
<li><p>From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p></li>
<li><p>Press &lt;Enter&gt;.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="14" type="1">
<li><p>Income plus net worth not greater than threshold value-incorrect status</p></li>
</ol></td>
<td><ul>
<li><p>The INCOME field (#.04) in the ANNUAL MEANS TEST file (#408.31) is not greater than the THRESHOLD A field (#.12),</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>The NET WORTH field (#.05) added to the INCOME is not greater than the THRESHOLD,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>The TEST-DETERMINED STATUS field (#2.03) is MT COPAY REQUIRED ("C").</p></li>
</ul></td>
<td><ol type="1">
<li><p>From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p></li>
<li><p>Press &lt;Enter&gt;.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="15" type="1">
<li><p>Copay Test Status should be &lt;calculated status&gt;</p></li>
</ol></td>
<td><p>The Copay Exemption Status is calculated based on income and net worth, then compared to the TEST-DETERMINED STATUS field (#2.03) in the ANNUAL MEANS TEST file (#408.31).</p>
<p>This message is returned when the calculated status does not equal the TEST-DETERMINED STATUS.</p></td>
<td><ol type="1">
<li><p>From the Copay Exemption Test Menu, use the Edit an Existing Copay Exemption Test option to view the data on each of the Income Test screens.</p></li>
<li><p>Press &lt;Enter&gt;.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="16" type="1">
<li><p>Invalid Copay Test Status for Test-Determined Status</p></li>
</ol></td>
<td><p>The TEST-DETERMINED STATUS field (#2.03) in the ANNUAL MEANS TEST file (#408.31) does not contain one of the following values:</p>
<ul>
<li><p>EXEMPT (E)</p></li>
<li><p>NON-EXEMPT (M)</p></li>
</ul></td>
<td><ol type="1">
<li><p>From the Copay Exemption Test Menu, use the Edit an Existing Copay Exemption Test option to view the data on each of the Income Test screens.</p></li>
<li><p>Press &lt;Enter&gt;.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="17" type="1">
<li><p>Income does not exceed child exclusion amount-educational expense not allowed</p></li>
</ol></td>
<td><ul>
<li><p>The dependent is not the spouse,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>the EDUCATIONAL EXPENSES field has an amount,</p></li>
</ul>
<p><strong>and</strong></p>
<ul>
<li><p>The CHILD INCOME EXCLUSION for the Income Year is not less than the TOTAL INCOME FROM EMPLOYMENT</p></li>
</ul>
<p>This message displays only when the Means Test process fails to delete the EDUCATIONAL EXPENSES from the INDIVIDUAL ANNUAL INCOME record for the child.</p>
<p>The normal processing of the Post-Secondary Education Expenses for a child between the ages of 18 and 23 are:</p>
<ul>
<li><p>If the TOTAL INCOME FROM EMPLOYMENT is above the CHILD INCOME EXCLUSION threshold found in the MAS PARAMETERS file (#43), the expenses can be entered.</p></li>
<li><p>When the income amount is modified to be below this threshold, the EDUCATIONAL EXPENSES are deleted from the INDIVIDUAL ANNUAL INCOME record for the child.</p></li>
</ul></td>
<td><ol type="1">
<li><p>From the Means Test User Menu, use the Edit an Existing Means Test option to view the data on each of the Means Test screens.</p></li>
<li><p>Press &lt;Enter&gt;.</p></li>
<li><p>Re-complete the test.</p></li>
</ol></td>
</tr>
</tbody>
</table>

Table 6: Types of Reports with Descriptions

### GMT Thresholds Lookup by Zip Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 23, 2002, former President Bush signed into law H.R. 3477, The Department of Veterans Affairs Health Care Programs Enhancement Act of 2001. Section 202 of this Act requires the implementation of U.S. Department of Housing and Urban Development (HUD) Indices to determine geographic income thresholds in support of more discrete Means Testing. A new GMT copayment status identifies veterans who qualify for a reduced inpatient copayment rate. The effective date of the regulation to support this legislation is November 1, 2002. Like traditional Means Test thresholds, the GMT Thresholds are applied in a retrospective manner (i.e., HUD Indices published in Calendar Year 2002 is used for Means Tests performed in Calendar Year 2003). Information about HUD income limits is available on the Data Sets Page of the HUD User Web Site at <u>http://www.huduser.org/datasets/il.html.</u>

The GMT Thresholds are uploaded into VistA annually, along with the traditional Means Test threshold values, in a patch released in December of each year. They are activated on January 1<sup>st</sup> of each year. The indices from previous years are stored indefinitely in both VistA and HEC systems. For information about the implementation of HUD Indices, refer to the GMT Installation Guide and GMT Technical Manual.

> **NOTE:** On January 17, 2003, VA discontinued enrolling new Priority Group 8 veterans into the VA health care system based on VA’s inability to provide timely and quality health care to all enrolled veterans. The new relaxed Priority Group 8 enrollment restrictions allow certain PG8 veterans to be enrolled in the VA health care system, if their household income does not exceed the current VA income thresholds (Means Test threshold and/or Geographical Means Test threshold) by more than 10%. These changes do not open enrollment to all PG8 veterans, however. For more details, visit the [VA Health Care Eligibility & Enrollment](http://www.va.gov/healthbenefits/) Web site.

The GMT software provides the following functionality.

- Automatically populates City, State, and County fields of the Patient Demographics Screen when ZIP Code is entered during patient registration or edit of patient demographic data (load/edit), unless the Bad Address Indicator is set. (Refer to Screen \<1.1\> Data Group 2, in the Registration Supplement of this manual for more information about the Bad Address Indicator.)
- State and County fields can only be edited by users who hold the EAS GMT COUNTY EDIT security key.
- Automatic Address Changes from HEC clears the Bad Address Indicator field (if it was set). (Refer to Screen \<1.1\> Data Group 2, in the Registration Supplement of this manual for more information about the Bad Address Indicator.)
- A conversion of veterans based on their existing financial assessment information is run at the HEC. An ongoing process assigns veterans to the appropriate medical care copayment and enrollment priority group upon completion of a financial assessment.
- NSC and non-compensable 0% SC veterans with current income above the MT Threshold and below the applicable GMT Threshold are placed in the new Means Test status “GMT Copayment Required”. These veterans are assigned to Enrollment Priority Group 7 (unless Catastrophically Disabled \[CD\] or exposed to Agent Orange[^1], Ionizing Radiation, or SW Asia Conditions[^2]). Veterans who are in GMT Copay Required status must submit income for yearly testing.
- Veterans who are subject to the full inpatient medical care copayment and placed in Enrollment Priority Group 8 (unless CD or exposed to toxic substances) include:
1.  Veterans with income greater than the GMT threshold plus 10% where GMTT\>MTT
24. Veterans declining to provide income info
25. Veterans with income greater than the MT threshold plus 10% who live in an area where the GMT threshold is less than or equal to the MT threshold
26. Veterans with income less than the MTT threshold but with a Net Worth greater than \$80K
27. Veterans with income above the MT threshold plus 10% whose income info is over one year old at the time the GMT software is installed.
- Although this does not affect the GMT functionality, all user viewable references to Category A and Category C Means Test statuses in enrollment-related software was modified to reflect the following changes:
1.  Category A (Cat A) is now MT Copay Exempt
28. Category C (Cat C) is now MT Copay Required.
- Modifies a variety of reports and data screens to display the new subcategories ‘b’ and ‘d’ for Enrollment Priority Group 8 and GMT Copayment Required status
- Provides a new user option, GMT Thresholds Lookup by ZIP Code, which displays GMT Threshold values for a valid user-specified ZIP Code
- Adds a new field, Hardship Reason, to the Hardship Determinations Screen

This option is used to display GMT Threshold values for a valid Postal Code (a.k.a. ZIP Code). The only user prompt is “ZIP Code:”, and a response is required. You must enter a ZIP Code or a city name to generate an output, or a caret (^) to return to the menu. If you enter a city name and the software finds multiple cities with the same name, it returns a list of the cities with their corresponding ZIP Codes from which you can make your selection.

The software returns the following information for a valid ZIP Code.

- ZIP Code
- County Name
- State
- Income year in which the GMT Thresholds apply
- Federal Information Processing Standard (FIPS) \[County\] Code
- Number of family members in household
- GMT Threshold dollar amounts for up to eight members in household
- Family size adjustments information for all income limits
- The formula for determining GMT Threshold dollar amounts for households with more than eight family members

### Hardships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option replaces the Change a Patient’s Means Test Category option. It allows the user to grant hardships for the current Means Test when the test is less than 1 year old from the effective date.

Hardship Determinations continue to be the responsibility of the VAMCs; however, they are sent to the HEC and distributed nationally along with the Primary Means Test to all VAMCs that the veteran has visited. Once granted, a Hardship is in effect until it expires on December 31 of the calendar year in which it was granted or is manually expired in the VHA Enrollment System. The VAMC that granted the hardship retains the original Means Test Status when the status changes. For example, if a Hardship determination changes the original status from MT Copay Required to MT Copay Exempt, the new status (Exempt) is stored as the Means Test status. The original status (MT Copay Required) is then stored as Test Determined Status.

After the GMT conversion runs at the HEC, if a veteran's Means Test status is MT Copay Required, the user is prompted to enter the status (GMT Copay Required or MT Copay Exempt) and a Hardship Reason.

The Hardship Determinations screen provides the following List Manager actions for Grant Hardship.

- Grant Hardship  
  Allows you to grant hardships for current Means Tests for the selected patient and prompts for Hardship Effective Date. Once granted, a hardship remains in effect until a new Means Test is completed.
- Edit Hardship  
  Allows you to edit hardships for current Means Tests for the selected patient and prompts for Hardship Effective Date and Hardship Review Date. Only the VAMC that determines the hardship can edit or delete it*.*
- Delete Hardship  
  Allows you to delete hardships for current Means Tests for the selected patient. Only the VAMC that determines the hardship can edit or delete it. When a hardship is deleted, no record of it is retained in the database.
- Edit Comments  
  Allows you to add, edit, and delete comments related to hardships for current Means Tests for the selected patient.

Access to this option is limited to holders of the DG MEANSTEST security key.

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

### Pseudo SSN Report for Means Test Dependents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pseudo SSN Report for Means Test Dependents is used to print a report of spouses and/or dependents, sorted by patient, who have Pseudo SSNs. You can choose to print the report for one or all Pseudo SSN reasons.

The output includes:

- Report title and page number
- Whether the report includes one or all Pseudo SSN reasons
- Report date
- Patient name and SSN
- Dependent/spouse name and relationship to patient
- Dependent/spouse Pseudo SSN
- Dependent/spouse Pseudo SSN reason
- A summary at the end of the report provides the following information:
1.  If you chose to print the report for a specific Pseudo SSN reason, the summary provides the total number of dependents with Pseudo SSNs.
29. If you chose to print the report for all Pseudo SSN reasons, the summary provides the total number of dependents with Pseudo SSNs and the number of dependents/spouses for each of the reason(s) selected.

### View a Past Means Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View a Past Means Test option is used to view past Means Tests data. The option does not allow editing. You are prompted for the patient's name and the date of the Means Test you want to view. Double question marks (??) entered at the date prompt, provide you with a list of the patient's Means Test dates from which to choose.

If certain circumstances exist for the selected patient, messages may display. A message is printed if no detailed income information is on file for the veteran, or if the veteran's Means Test status is NO LONGER REQUIRED. Because income data can be entered/edited through registration, once a Means Test has this status, the income data viewed may differ from that originally entered as part of the Means Test.

You are able to view the following four Means Test screens through this option.

- Screen 1-Marital Status/Dependents
- Screen 2-Previous Calendar Year Gross Income
- Screen 3-Deductible Expenses
- Screen 4-Previous Calendar Year Net Worth

The option may display the dependent totals not converted. Totals not converted only display under the following conditions.

- Converted totals exist and Means Test income is 0 or greater
- For a spouse - the veteran is married, but detailed income information is not available
- For dependent children - the veteran has dependent children, but detailed income information is not available

Refer to the Edit an Existing Means Test option for instructions on how to correct Means Test inconsistency errors.

## Patient Inquiry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Inquiry option is used to view the following kinds of information for a selected patient: demographic, primary care, enrollment, preregistration, and such items as bad address indicator, foreign address, date of death (including source of notification for date of death, date of last entry or update, and local submitter/user information), “Permanent and Total Disabled” field value, COMPACT Act Status, Episode Start date, Residential Remaining Days, End date and Source of Crisis End code, VHAP, sexual orientation, sexual orientation free text, pronoun and pronoun description currently assigned to the Veteran. Sexual Orientation, Sexual Orientation Free Text, Pronoun and Pronoun Description information is Read Only.

A full or abbreviated inquiry may display depending upon how the PIMS parameter, ABBREVIATED INQUIRY, is set at your facility.

Editing of the information is not allowed through this option.

The veteran’s Long Term Care (LTC) copayment status and last test date displays when using this option. If the last test is over a year old, the message “\*\*NEW TEST REQUIRED\*\*” displays. If the veteran did not agree to pay the copayments, the following ineligible message displays.

Patient INELIGIBLE to Receive LTC Services -- Did Not Agree to Pay Copayments

## Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Display Preregistration Call List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the Preregistration Call List in List Manager screen format. This is a list of the patients to be contacted before their clinic appointments for the purpose of updating their patient information. The information displayed might vary depending on how certain parameters in the MAS PARAMETERS file (#43) (e.g., Multi-divisional, Sort Method, etc.) are set at your facility. (Use the MAS Parameter Entry/Edit option to set the applicable parameters for your facility.)

This option is locked with the DGPRE EDIT security key.

In addition to PATIENT NAME, PHONE, and SSN, the following columns display in the Preregistration Call List:

HIST Provides a history of whether or not the patient has been contacted  
successfully by telephone.  
(Enter ? at the “STATUS OF CALL:  
CONNECTED//” prompt for a list of acceptable codes.) The codes for  
as many as the last four calls are displayed.

SVC Indicates the hospital service (e.g., Medicine, Surgery, Psychiatry, etc.)  
associated with the clinic in which the patient has an appointment.

STAMP Contains the date/time on which the patient information was last  
updated in the Load/Edit screens through the use of the various  
preregistration options. The date/time is displayed in this column only  
if you answered YES to the “Date/Time stamp this patient? YES//”  
prompt.

DIVISION Contains the name of the division associated with the patient’s clinic  
appointment. The division name displays only if the  
Multi-divisional parameter is set to YES. This column is not visible on  
the initial Preregistration Call List screen. If greater than signs (\>\>\>)  
appear on the status bar, you can scroll to the right of the screen using  
your right arrow key (→) to view this column.

The following user actions are available at the bottom of the screen.

CP Call Patient - Lets you edit patient information via Load/Edit Screens 1  
through 5 and enter the call status for a selected patient. (If you need  
assistance with editing the information on these screens, refer to the  
user documentation for the Load/Edit Patient Data option.) You also have  
the option to apply a date/time stamp to the selected patient before returning  
to the Preregistration Call List screen. This action works the same as the  
Preregister a Patient menu option.

EH Edit History - Lets you edit information pertaining to whether or not  
the patient was successfully contacted by telephone and edit the call  
status. You can use this action to change, but not delete, log entries.

> **NOTE:** You can only use this action after using the CP action.

XH Expand History - Displays information pertaining to the calling  
history for a selected patient, including the date and time of the call,  
name of the person who made the call, and call status.

> **NOTE:** You can only use this action after using the CP action.

IN Patient Inquiry - Lets you enter an inquiry for a selected patient  
without leaving the Preregistration Call List screen. Works the same  
as the Patient Inquiry menu option.

### Outputs for Preregistration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Calling Statistics Report

This option generates the Preregistration Call Statistics report, which provides a breakdown of the current entries in the PRE-REGISTRATION CALL LOG file (#41.43) by call status. The prompts ask for beginning and ending dates and a device if the Multi-divisional parameter in the MAS PARAMETERS file (#43) is set to NO. (Use the MAS Parameter Entry/Edit option to set this parameter.)

If the Multi-divisional parameter is set to YES, the “Select division: ALL//” prompt also displays. If you accept the ALL default, the next prompt asks for a device. If you select a specific division, the “Select another division:” prompt displays and repeats after your entry, allowing you to select multiple divisions (up to a maximum of 20). Press \<RET\> to indicate that you are finished making your selections and proceed to the “DEVICE: HOME//” prompt.

Before using this option, multi-divisional facilities should ensure that each clinic has an associated division. (You can do this by entering a division name at the “DIVISION:” prompt while using the Set up a Clinic option in the Scheduling Supervisor Menu.)

This option uses NO DIVISION SPECIFIED as a sort value. If you accept the ALL default at the “Select division: ALL//” prompt, the output shows NO DIVISION SPECIFIED as the division name for statistics whose clinics are NOT associated with a division.

#### Percentage of Patients Pre-Registered Report

The Percentage of Patients Pre-Registered Report prints the following data for a user-defined date range.

- Number of unique outpatients treated
- Number of unique outpatients pre-registered within the pre-registration time frame
- Percentage of unique outpatients pre-registered within the pre-registration time frame
- Number of unique outpatients pre-registered past the pre-registration time frame
- Number of unique outpatients never pre-registered
- Number of clinic exclusions and eligibility exclusions

It is recommended that this report be queued to run after normal business hours.

#### Print Preregistration Audits

This option prints the number of changes to patient demographic and insurance data that were made during the preregistration process for a user-specified date range. The applicable audits in the PATIENT file (#2) must be turned on for this option to work. The MCCR Reengineering Group recommends that you ask your IRM Service to turn on the audits for the following fields:

.05 MARITAL STATUS

.111 STREET ADDRESS \[LINE 1\]

.112 STREET ADDRESS \[LINE 2\]

.114 CITY

.115 STATE

.117 COUNTY

.131 PHONE NUMBER \[RESIDENCE\]

.132 PHONE NUMBER \[WORK\]

.211 K-NAME OF PRIMARY NOK

.2191 K2-NAME OF SECONDARY NOK

.3111 EMPLOYER NAME

.31115 EMPLOYMENT STATUS

.351 DATE OF DEATH

.361 PRIMARY ELIGIBILITY CODE

The output includes the fields that were changed, the name of the user(s) who made the changes, and the number of changes made by each user.

#### Source of Information Report

This option prints the Pre-Registration Source Report that lists the following information for a user-specified date range.

- Patient insurance policies that were added using the preregistration options and have a source of information equal to PRE-REGISTRATION (on Screen 5 of the Load/Edit Patient Data option).
- Inpatient and outpatient bills generated during the user-specified date range based on preregistration insurance policies and payments collected during the user-specified date range against those bills.

> **NOTE:** Bills and payments listed in the report could be against preregistration policies that were added outside of the user-specified date range.

The output generated by this option varies depending on which of the following report formats you select at the “Type of report to print: summary//” prompt.

<table>
<caption><p>Table 7: Scenarios for a Patient Marked Sensitive, including Actions Taken at RS and LST</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Type of Report</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Detailed</td>
<td><ol type="1">
<li><p>Provides detailed information for the following activities during the user-specified date range</p></li>
</ol>
<ul>
<li><p>Patient insurance policies added through preregistration options</p></li>
</ul>
<ul>
<li><p>Inpatient bills entered against preregistration policies</p></li>
<li><p>Inpatient payments collected against preregistration policies</p></li>
<li><p>Outpatient bills entered against preregistration policies</p></li>
<li><p>Outpatient payments collected against preregistration policies</p></li>
</ul>
<ol start="2" type="1">
<li><p>Provides total count for each activity</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Summary</td>
<td><p>Prints a one-page report showing only the totals</p>
<p>No patient-specific information is provided</p></td>
</tr>
</tbody>
</table>

Table 7: Scenarios for a Patient Marked Sensitive, including Actions Taken at RS and LST

### Supervisor Preregistration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Add New Appointments to Call List

This option lets you add patients to the Preregistration Call List based on patient appointments for a user-specified search date. The default response to the “Enter Appointment date to search:” prompt is TODAY plus the value of the DAYS TO PULL APPOINTMENT field (#1100.05) in the MAS PARAMETERS file (#43). (Use the MAS Parameter Entry/Edit option to set the value of this field.)

#### Clear the Call List

This option deletes all entries in the PRE-REGISTRATION CALL LIST file (#41.42) regardless of the call status. There are no prompts associated with this option. Once the option is selected, the number of entries deleted displays.

#### Purge Call Log

This option purges all entries prior to a user-specified date from the PRE-REGISTRATION CALL LOG file (#41.43). You are asked to enter a purge date and to verify that you want to purge all entries prior to the date you entered.

#### Purge Contacted Patients

This option purges patients who were already contacted and who have a call status of CONNECTED from the Preregistration Call List. There are no prompts associated with this option. Once the option is selected, the number of entries purged displays.

### Patient Inquiry 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays registration information for a selected patient including any preregistration items, bad address indicator, foreign address, emergency response indicator, date of death (including source of notification for date of death, date of last entry or update, and local submitter/user information), “Permanent and Total Disabled” field value, COMPACT Act Status, Episode Start date, Residential Remaining Days, End date and Source of Crisis End code, VHAP, sexual orientation, sexual orientation free text, pronoun and pronoun description currently assigned to the Veteran. The date of death, VHAP, Sexual Orientation, Sexual Orientation Free Text, Pronoun and Pronoun Description information is Read Only.

The patient selected does not have to be in the PRE-REGISTRATION CALL LIST file (#41.42) to be selected.

### Preregister a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to perform the following tasks:

- Preregister any selected patient in the PATIENT file (#2) using the Load/Edit process (without using the Preregistration Call List).
- Enter the call status for a selected patient. (If you enter a status of CONNECTED, you can edit patient information via Load/Edit Screens 1 through 5. If you need assistance with editing the information on these screens, refer to the user documentation for the Load/Edit Patient Data option.)
- Apply a date/time stamp to the selected patient before returning to the Preregistration Call List screen.
- If the "Enable My HealtheVet Prompts?" (#1100.07) field in MAS Parameters (#43) file is enabled, the "Increase Engagement in MyHeatheVet" prompts will be displayed when Preregistering patients to do the following:
  - Track the patient's registration status in My HealtheVet.
  - If the patient is not registered, prompt the clerk to query the veteran as to their interest.
  - Inform the patient of My HealtheVet benefits, and based on their interest, help them register in My HealtheVet, authenticate for a premium account, and setup Secure Messaging.
- Edit the patient’s mailing address information. Prior to entering patient data, the mailing address displays and the user is asked, *Do you want to edit the Patient's Mailing Address?*
  - If the user answers YES, the system prompts each address field and the user is allowed to update the patient’s mailing address information.
    - The address entered by the user is then sent to the UAM Validation Service and the results of the address validation are displayed to the user. The user selects the address they want to store and press enter.
    - The old and the new address information is displayed and the system asks the user *Are you sure that you want to save the above changes?*
    - If the user answers YES, the system displays “Change saved”, the patient’s mailing address change date/time stamp is updated, and a trigger is set to send a message to the HEC.
    - If the user answers NO, the system displays “Change aborted”. Neither the patient’s mailing address information nor the mailing address change date/time stamp is updated and a message is not triggered to the HEC.

> **NOTE:** It takes an actual change to the mailing address to update the mailing address change date/time stamp. If there were no changes to the mailing address information, and the user responds YES; no updates are made to the mailing address fields or mailing address change date/time stamp and a message is not triggered to the HEC.

- If the user answers NO at the *Do you want to edit the Patient's Mailing Address?* prompt, the system does not prompt the user for address information and the system continues the Preregister a Patient process.

When using this option, the primary medical center division is used as the division. This option is locked with the DGPRE EDIT security key.

> **NOTE:** This option works the same as the CP action on the Preregistration Call List screen in the Display Preregistration Call List option.

### My HealtheVet Engagement Alert/Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The My HealtheVet Engagement functionality will only display when the Enable My HealtheVet Prompts? (#1100.07) field in the MAS PARAMETER (#43) file is enabled.

If enabled, once the patient name is entered, an alert displays for the registration clerk. The alert indicates that the patient needs to answer My HealtheVet (MHV) registration questions. Any previous actions taken on behalf of a returning patient also display along with the date the actions occurred.

The alert, actions taken, and subsequent registration questions are displayed only under the following conditions:

1.  Any of the three My HealtheVet Registration Status fields are unanswered or further action(s) needs to be taken.
2.  Any of the three My HealtheVet Registration Status fields were recorded as No, at least six months ago.

The registration clerk is asked to inquire if the patient was successful in creating their My HealtheVet account, if the alert is triggered by an on-going action.

3.  If the Answer is No, the registration clerk is directed to the list of available actions.
4.  If the answer is Yes, the registration clerk is directed to the Registration Status display.
5.  If the alert is triggered by a pending action associated with Authenticated or Secure Messaging, the action(s) taken are displayed. The registration clerk is directed to the My HealtheVet Registration Status display after selecting “Return” to continue.

My HealtheVet Registration Socialization Questions

To determine the patient’s My HealtheVet registration status, the following question displays for the registration clerk to read verbatim to the patient.

Has a health care team member encouraged you to register online for My Healthevet?

The registration clerk records the patient’s response by choosing one of the following menu selections:

1.  Yes - I have already registered on My HealtheVet
2.  Yes - I would like to register on My HealtheVet
3.  Yes - But I do not want to register right now
4.  No - No one has spoken to me/I don't know about MyHealtheVet
5.  No - I am not interested in registering on My HealtheVet
6.  No - I don't have computer / mobile device / internet access

The Preregister a Patient, My HealtheVet socialization process continues depending on the patient’s response.

1\. Yes – I have already registered on My HealtheVet

> The registration clerk reads the following prompt:

> We are strongly encouraging patients to register online for a My

> HealtheVet account. With My HealtheVet, you can refill VA prescriptions,

> view lab results and medical records, and use Secure Messaging with your

> health care team.

> After reading the prompt, the registration clerk clicks “Return” to continue to the My HealtheVet Registration Fields status screen.

2\. Yes – I would like to register on My HealtheVet

> The registration clerk reads the following prompt:

> We are strongly encouraging patients to register online for a My

> HealtheVet account. With My HealtheVet, you can refill VA prescriptions,

> view lab results and medical records, and use Secure Messaging with your

> health care team.

> After reading the prompt, the registration clerk selects “Return” to continue to the list of possible actions that could be taken on behalf of the patient.

> The registration clerk should provide assistance to the patient and record the action number taken. For example, the registration clerk could enter “1” if they helped the patient create a My HealtheVet account.

> After the action taken is recorded and displayed, the registration clerk may change their selection by entering “(A)dd another, (D)elete an action, or \<RET\>” to save and exit.

> Once the registration clerk is satisfied with their selection and clicks “\<RET\>” to save and exit, the preregistration process continues.

3\. Yes – But I do not want to register right now.

> The registration clerk reads the following prompt:

> We are strongly encouraging patients to register online for a My

> HealtheVet account. With My HealtheVet, you can refill VA prescriptions,

> view lab results and medical records, and use Secure Messaging with your

> health care team.

> I will give you some easy-to-follow instructions so that you can register

> at home. Once registered, you will need to return to your VA medical center

> or clinic and sign the My HealtheVet authentication form, VA Release of

> Information (ROI) form (10-5345a-MHV). A government issued photo ID is

> required. (Instructions for optional online Authentication process are

> also available)

> After reading the message, the registration clerk clicks “Return” to continue to the list of possible actions that could be taken on behalf of the patient.

> The actions and the selection process are the same as in the previous selection “2. Yes – I would like to register on My HealtheVet.”

> Once the registration clerk is satisfied with their selection and clicks “\<RET\>” to save and exit, the preregistration process continues.

4\. No – No one has spoken to me/I don't know about MyHealtheVet.

> The registration clerk reads the following prompt:

> We are strongly encouraging patients to register online for a My

> HealtheVet account. With My HealtheVet, you can refill VA prescriptions,

> view lab results and medical records, and use Secure Messaging with your

> health care team.

> I will give you some easy-to-follow instructions so that you can register

> at home. Once registered you will need to return to a VA clinic and sign a

> My HealtheVet authentication form, VA Release of Information (ROI) form

> (10-5345a-MHV). A government issued photo ID is required. (Instructions

> for optional online Authentication process are also available)"

> After reading the message, the registration clerk clicks “Return” to continue to the list of possible actions that could be taken on behalf of the patient.

> The list of actions and the selection process are the same as in the previous selection “2. Yes – I would like to register on My HealtheVet.” Once the registration clerk is satisfied with their selection and clicks “\<RET\>” to save and exit, the preregistration process continues.

5\. No - I am not interested in registering on My HealtheVet

> The registration clerk reads the following prompt:

> We are strongly encouraging patients to register online for a My

> HealtheVet account. With My HealtheVet, you can refill VA prescriptions,

> view lab results and medical records, and use Secure Messaging with your

> health care team.

> After reading the message, the registration clerk clicks “Return” to continue.

> The registration clerk asks the patient the following question and records the response:

> How does the patient feel now about registering in My HealtheVet?

> a\) Patient is not interested.

> b\) Patient is interested.

1.  If the answer is “a) Patient is not interested,” the registration clerk records “a” at the “Select a response” prompt and clicks “Return” to continue to the My HealtheVet Registration Status display.
2.  If the answer is “b) Patient is interested,” the registration clerk records “b” at the “Select a response” prompt and clicks “Return” to continue to the list of possible actions that could be taken on behalf of the patient.

> The list of actions and the selection process are the same as in the previous selection “2. Yes – I would like to register on My HealtheVet.” Once the registration clerk is satisfied with their selection and clicks “\<RET\>” to save and exit, preregistration continues.

6.  No - I don't have computer / mobile device / Internet access

> The registration clerk reads the following prompt:

> Do family or friends, who have a computer/mobile device/ Internet access,

> ever help with your VA appointments or medications? You can also log on

> to any public library computer to use My HealtheVet. Imagine that you are

> out of town and you need a copy of your health records or medications -

> with a My HealtheVet account, you can access that information from any

> computer/mobile device as long as there is Internet access.

> After reading the message, the registration clerk clicks “Return” to continue.

> The registration clerk then determines the answer to the following question from the patient and records the response:

> How does the patient feel now about registering in My HealtheVet?

> a\) Patient is not interested.

> b\) Patient is interested.

1.  If the answer is “a) Patient is not interested,” the registration clerk records “a” at the “Select a response” prompt and clicks “Return” to continue to the My HealtheVet Registration Status display.
2.  If the answer is “b) Patient is interested,” the registration clerk records “b” at the “Select a response” prompt and clicks “Return” to continue to the list of possible actions that could be taken on behalf of the patient.

> The list of actions and the selection process are the same as in the previous selection “2. Yes – I would like to register on My HealtheVet.” Once the registration clerk is satisfied with their selection and clicks “\<RET\>” to save and exit, preregistration continues.

My HealtheVet Registration Fields Status and Updates

Following the My HealtheVet Alert and socialization questions, or directly after entering the Patient Name as part of Preregistration, the status of the My Healthevet Registration fields (listed below) are displayed, unless there is an action pending, along with a prompt to edit or continue preregistration.

\[1\] Registered:

\[2\] Authenticated:

\[3\] Secure Messaging:

Select an Registration step, or RETURN to continue:

If the preregistration clerk clicks “RETURN,” preregistration continues.

The Registration, Authenticated, and Secure Messaging fields are numbered, if the previous registration field has a status of Yes. For example, if Registered and Authenticated are Yes, the display above is shown with all three fields being directly editable. However, if Authenticated is unanswered, Action, or No, only Registered and Authenticated fields can be edited.

\[1\] First My HealtheVet Registration Status – Registered

Is the patient registered on My HealtheVet (Yes/No)?

3.  If the response is Yes, the registration clerk is directed to the next Registration status field – Authenticated.
4.  If the response is No, the registration clerk must select a reason from the list of reasons displayed. If a closely matching reason is not available, the registration clerk should select “Other” and enter a reason up to 250 characters in length (something must be entered). Once the reason is entered, the My HealtheVet Registration Status displays the selected reason below “Registered.”

\[2\] Second My HealtheVet Registration Status Field – Authenticated

> With a Premium My HealtheVet account, patients can view VA appointments, lab results, access portions of their VA medical record and use Secure Messaging"

> Select (Y) YES if patient already has a Premium My HealtheVet account.

> Select (A) ACTION if patient wants to upgrade to Premium My HealtheVet account.

> Select (N) NO if patient refuses to upgrade to a Premium My HealtheVet account.

5.  If the response is Yes, the registration clerk is directed to the next Registration status field, “Secure Messaging.”
6.  If the response is No or Action, the following is displayed instructing the registration clerk to provide information to the patient:

> Please read the following to the patient:

> Upgrade to a Premium My HealtheVet account to view parts of your VA health record and use Secure Messaging. This requires one-time in-person identity verification (show government issued photo ID). Read and sign VA Release of Information form (10-5345a-MHV). Present a government issued photo ID, required. Instructions for optional on-line authentication process are also available.

7.  If the registration clerk assists the patient with authentication, the clerk should enter the response of Yes for “Authenticated” after providing assistance.
8.  If the response is No, the registration clerk must select a reason from the list of reasons displayed. If a closely matching reason is not available, the registration clerk should select “Other” and enter a reason up to 250 characters in length (something must be entered). Once the reason is entered, the My HealtheVet Registration Status displays the selected reason below “Authenticated.”
9.  If the response is Action, the registration clerk must select an action from the list of actions presented. Once the action is entered, the preregistration process continues. If the patient is preregistered in the future, the My HealtheVet Alert displays with the action selected.

\[3\] Third My HealtheVet Registration Status Field – Secure Messaging

> Please read the following to the patient:

> With Secure Messaging, Veterans can communicate online with VA health care teams about health, medication questions, request prescription renewals, and/or appointments."

> Select (Y) YES if patient already uses Secure Messaging.

> Select (A) ACTION if patient would like to use Secure Messaging.

> Select (N) NO if patient declines to use Secure Messaging.

> Secure Messaging? (Yes/No/(A)ction): YES//

10. If the response is Yes, the registration clerk is returned to the My HealtheVet Registration Status display where they may select “RETURN” to continue with preregistration.
11. If the registration clerk assists the patient with opting in for secure messaging, the clerk should enter the response of Yes for “Secure Messaging” after providing assistance.
12. If the response is No, the registration clerk must select a reason from the list of reasons displayed. If a closely matching reason is not available, the registration clerk should select “Other” and enter a reason up to 250 characters in length (something must be entered). Once the reason is entered, the My HealtheVet Registration Status displays the selected reason below “Secure Messaging.”
13. If the response is Action, the registration clerk must select an action from the list of actions presented. Once the action is entered, the preregistration process continues. If the patient is preregistered in the future, the My HealtheVet Alert displays with the action selected.

My HealtheVet Registration Fields Consistency Check

The VistA Consistency Checker identifies any unanswered field (Registered, Authenticated, or Secure Messaging) or if the My HealtheVet registration fields (Authenticated or Secure Messaging) have actions.

If the “MY HEALTHEVET REGISTRATION STATUS ABSENT/MISSING” check displays (i.e., 315- MHV REGISTRATION STATUS ABSENT) and the registration clerk completes the My HealtheVet Registration fields, the clerk should indicate “Yes,” they want to complete the identified inconsistencies. The process for completing the fields is the same as in the My HealtheVet Registration Fields Status and Updates section.

## Print Patient Wristband

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Patient Wristband option is used to generate a patient wristband with barcoded social security number. The wristband contains the patient name, primary long ID (usually the social security number), date of birth, religion, and an allergy flag (YES or a blank line for NO). Whether or not wristbands print for a division and whether or not the ward location prints on the wristband is determined by site parameters.

If you choose to print a wristband, you are prompted for a device and whether or not you want to queue your request. Requests must be sent to a barcode printer.

Wristbands may be printed only for inpatients. The print wristband functionality is also available in the Admit a Patient and Transfer a Patient options.

## Pseudo SSN Report (Patient)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pseudo SSN Report (Patient) option is used to print a report of patients with Pseudo SSNs. You can choose to print the report for the following:

- All veterans, all non-veterans, or both

> and

- One or all Pseudo SSN reasons

If you chose to print the report for both veterans and non-veterans, they display in the following sub-reports, sorted by Pseudo SSN Reason:

- Report for Non-Veterans
- Report for Veterans

The report *does not* include:

- Deceased patients
- Non-user enrollees
- Patients without an Integration Control Number (ICN)

The output includes:

- Report title and page number
- Whether the report is for veterans, non-veterans, or both
- Report date
- Patient name
- Pseudo SSN
- Birth date
- Primary eligibility code
- Pseudo SSN reason
- Subtotal for each Pseudo SSN Reason
- Total number of patients with a Pseudo SSN

## Register a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Register a Patient option is used to process a patient’s application for health benefits, enter/edit information in their file, and perform a variety of registration-related functions. Necessary registration data is gathered and a corresponding entry is made automatically in the Disposition Log. This entry must receive subsequent dispositioning through the Disposition an Application option or the registration should be deleted through the Delete a Registration option. A new patient's record may be established or an existing one edited. Should you wish to enter a new patient into the database or edit an existing patient's record without creating an entry in the Disposition Log, you should use the Load/Edit Patient Data option.

Figure 1 shows a basic example of an Enterprise Search. At the initial prompt ‘Select PATIENT NAME:’ you may select an existing patient or enter a new patient’s name. If a single match to existing patient is found you will be prompted to confirm that is the patient you want. If multiple matches are found you will have the chance to select an existing patient record. If no matches are found or you do not select an existing record from the prior two possible options you will be asked if you want to do an Enterprise Search. If no Enterprise Search is selected you are returned to the ‘Select PATIENT NAME:’ prompt.

If you answer YES that you want to do an Enterprise Search you will be presented with several demographic/trait prompts for the search. An Enterprise Search will be conducted to query the MVI. If no matching patient is found on the MVI, then a second search is automatically triggered to search DoD records. Any matches found from the searches will be presented for selection. If a record is selected the data from the source (either MVI or DoD) will be automatically populated into the registration record. If any of the results returned are at or above the IDENTITY MATCH criteria, you must either select one of the records presented or have the key DG MVI ADD PT to override and add a patient record without selection.

Records that are returned from the Enterprise Search of the MVI or DoD systems are displayed in the closest match order based upon score.

The following is an example of an Enterprise search.

Select PATIENT NAME: DGPATIENT,ONE

Do you want to do an Enterprise Search? Y \<Enter\> (Yes)

Patient name components--

FAMILY (LAST) NAME: DGPATIENT//

GIVEN (FIRST) NAME: ONE//

MIDDLE NAME:

SUFFIX:

Patient identifiers--

SOCIAL SECURITY NUMBER: REDACTED \<Enter\>

DATE OF BIRTH: 9/4/67 \<Enter\> (SEP 04, 1967)

SEX: MALE \<Enter\>

PATIENT TYPE: NSC VETERAN

PATIENT VETERAN (Y/N)?: YES YES

PATIENT SERVICE CONNECTED?: NO NO

MOTHER'S MAIDEN NAME:

PLACE OF BIRTH \[CITY\]:

PLACE OF BIRTH \[STATE\]:

MULTIPLE BIRTH INDICATOR:

PHONE NUMBER \[RESIDENCE\]:

Searching the MVI...

--- Records meet the MATCH criteria ---

   ICN               NAME                            SSN        DOB         SEX

1\) 1000004068V922305 DGPATIENT,ONE               REDACTED  9/4/67      M

Enter the Number to display the details: 1 \<Enter\>

Please wait...

     ICN         : 1000004068V922305

     Name        : DGPATIENT,ONE

     SSN         : REDACTED

     DOB         : Sep 04, 1967

     Gender      : M

     MMN         : DG_MOTHERS_MAIDEN_NAME

     POB City    : SAN FRANCISCO

     POB State   : CA

     POB Country : USA

Would you like to see another record? NO//

Would you like to select a patient from above Enterprise Search? YES// YES \<Enter\>

Enter the Number to select the patient: 1 \<Enter\>

DGPATIENT,ONE DGPATIENT,ONE       9-4-67    REDACTED     NO     NSC VETERAN     

Press ENTER to continue

Enrollment/Eligibility Query sent ...

Please verify or update the following information:

MULTIPLE BIRTH INDICATOR:

Select ALIAS:

Other possible results returned from an Enterprise Search:

- If no patients are found on the MVI or if the connection to the MVI is down, the Registration user will be prompted to add the patient based upon the data previously entered.

The following is an example of a patient not found on the MVI or connection to the MVI is down.

Searching the MVI...

No records found on the MVI.

   ARE YOU ADDING 'DGPATIENT,ONE' AS A NEW PATIENT (THE 6268TH)? No//
- If too many matches are returned from the Enterprise Search, then the user is prompted to provide updated (more specific) search criteria to return a more limited search result list from which to select.
- If the matches returned are above the Auto Link threshold, then the user must select one of the patients returned from the query (Auto Link threshold or Potential Match threshold) or hold the security key, DG MVI ADD PT, to override the selection.
- The following question will be asked if the patient is unknown to ES or if the patient previously answered NO to DO YOU WISH TO ENROLL?:
- DO YOU WANT TO ENROLL?
- If YES is entered, the following questions will be asked:
- APPLICATION DATE: NOW//
- If you press Enter, NOW will be selected. Otherwise you may enter a date. The Application Date must be a precise date, cannot be a date prior to the Date of Birth, cannot be a date after the Date of Death, cannot be a date prior to 10/1/1996 and cannot be a date in the future.
- DO YOU WANT AN APPT. WITH A VA DOCTOR/PROVIDER AS SOON AS AVAILABLE?: YES//
- If NO is entered for the DO YOU WANT TO ENROLL? question, the following required question will be asked:
- SELF-REPORTED REGISTRATION ONLY REASON:

Registration process continues as normal…

After you’ve selected a patient record, patient demographic, enrollment, eligibility, COMPACT Act episode of care data, and emergency response indicator(s) information displays. If the patient record contains a date of death, the following prompt displays: “PATIENT EXPIRED \[date\]...WANT TO CONTINUE? No//”. This prompt requires a response. If you respond with “No”, you return to the menu. If you respond with “Yes”, date of death information (including source of notification for date of death, date of last entry or update, and local submitter/user information) also displays. The date of death information is Read Only.

For existing patients in the PATIENT (#2) file; prior to entering patient data, the mailing address displays and the user is asked, *Do you want to edit the Patient's Mailing Address?*

- If the user answers YES, the system prompts each address field and the user is allowed to update the patient’s mailing address information.
  - The address entered by the user is then sent to the UAM Validation Service and the results of the address validation are displayed to the user. The user selects the address they want to store and press enter.
  - The old and the new address information is displayed and the system asks the user *Are you sure that you want to save the above changes?*
  - If the user answers YES, the system displays “Change saved”, the patient’s mailing address change date/time stamp is updated, and a trigger is set to send a message to the HEC.

> **NOTE:** It takes an actual change to the mailing address to update the mailing address change date/time stamp. If there were no changes to the mailing address information, and the user responds YES; no updates are made to the mailing address fields or mailing address change date/time stamp and a message is not triggered to the HEC.

- If the user answers NO, the system displays “Change aborted”. Neither the patient’s mailing address information nor the mailing address change date/time stamp is updated and a message is not triggered to the HEC.
- If the user answers NO at the *Do you want to edit the Patient's Mailing Address?* prompt, the system does not prompt the user for address information and the system continues the Register a Patient process.

Entry/edit of a patient's record is done via a series of formatted data screens. There are a total of fifteen screens distributed with the PIMS package. Screens 12-14 are informational only. The enter/edit process is not the same for every patient, nor for every user due to several variables that exist in the system. Your site has the ability to create its own additional screen in order to capture certain information it may need or to capture information in a different format. It has the ability to turn certain data screens ON and OFF according to patient type. Within the screens, it may specify which data groups may be entered/edited. The DG ELIGIBILITY security key also plays a role in your ability to enter/edit data. Depending upon whether eligibility was verified, certain information may only be edited by a user holding this security key.

In order to prevent catastrophic edits to a patient’s identity, four patient identity fields were established. They are patient name (first and/or last name components), social security number, date of birth, and sex. If modifications are made to two or more of these fields within one edit session, a warning alert displays. If you proceed with the edits, an alert with the potential patient catastrophic edits is forwarded to your site’s ADPAC and appropriate supervisor for review and action. In addition, the after edits of the patient identification fields display an asterisk to highlight the edited fields that were modified when the alert was generated. The alerts remain on file for one year.

The HIGH INTENSITY field in the MAS parameters was provided to assist you in the identification of the fields that may/may not be edited. If this field was set to YES at your facility, the number next to those data groups which may be edited are in boldface type; those which are un-editable do not (excluding Screen 8). For those sites not using High Intensity, numbers of data groups that may be edited are enclosed in \[ \]s, while those that are un-editable are enclosed in \< \>s (excluding Screen 8).

The Registration Supplement provides an example of each data screen and a description of each associated field. Refer to this Supplement when entering or editing patient information, if necessary.

If your site has the Consistency Checker turned ON, the system performs a check for inconsistent/unspecified data elements at the conclusion of the entry/edit process. If any are found, you are given the opportunity to make the necessary corrections.

You may now register a patient without the eligibility code or period of service entered. Check for these elements at disposition.

As previously mentioned, this option also allows you to perform several registration-related functions.

- You may make a HINQ inquiry and emboss a patient data card. With the installation of the Veteran Identification Card (VIC) software, the prompt “Download VIC data?” was added to allow you to download the selected patient’s demographic data to the photo capture station. The existing “EMBOSS DATA CARD?” prompt was changed to “EMBOSS (OLD) DATA CARD?”.
- If Record Tracking is running at your facility, you are able to create records for new patients and print corresponding barcode labels. If the patient already has records in the Record Tracking system, you are able to issue a request for these records to the file room. The “Select Admitting Area” prompt must be answered, in order to request records.
- The system determines a patient's need for Means Testing and Copay Testing and, if necessary, allow you to complete the required test. If the patient’s Enrollment Status is REGISTRATION ONLY, neither a Means Test nor a Copay test are required. For the Copay Test, the veteran has to request that the test be completed. For instructions on Means Test, refer to the Add a New Means Test or Complete a Required Means Test options. For instructions on Copay Test, refer to the Add a New Copay Test option.
- At the conclusion of the registration process, you are prompted to print the 10-10EZ form.
1.  Because the financial information that is printed on the 10-10EZ or 10-10EZR form is taken from a means test associated with the patient, and because a patient may have several means test entries during his/her course of care, the ‘PRINT 10-10EZ?’ and ‘PRINT 10-10EZR?’ prompts present a selection list of means test entries associated with the patient. The selection list of means test entries contain future Means Tests and future Co-Pay Exemption Tests that are not Primary. The selection list also contains the most current Means Test, Co-Pay Exemption Test, and LTC Co-Pay Exemption Test that are Primary.
30. If data for the patient does not exist in the VistA patient database, a message displays informing the user that the forms are not printed.

The system assigns a status to every patient registration. Available statuses are: 10-10 VISIT, UNSCHEDULED, and APPLICATION WITHOUT EXAM. Determination of the status is based upon whether the patient is currently followed in a clinic for the same condition and if the patient is to be examined in the medical center that day.

All necessary data from a registration is collected for entry into the AMIS 400 series reports. The REGISTRATION ELIGIBILITY CODE and SC% AT REGISTRATION fields were included to allow sites flexibility in the grouping of their AMIS 400 series reports.

An UNSCHEDULED (1010) VISIT OE/RR NOTIFICATION may display with v2.5 of Order Entry/Results Reporting. The patient must have been examined. The notification only displays for patients who are defined in an OE/RR LIST entry and only display to users defined in that list entry. Refer to the Order Entry/Results Reporting documentation for more information concerning OE/RR notifications, if needed.

Screen 8 of this option uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items. The following is a brief explanation of some of the actions listed on this screen.

- DD - In order to edit the dependent demographics, the selected dependent has to be active.
- DP - Delete Dependent functionality requires that the user hold the DG DEPDELETE security key. This functionality is used to delete duplicate dependents. In order to delete a dependent, they must be removed from every Means Test.
- ED - Expand Dependent moves you to another screen. It is used to edit the effective date (date the person became a dependent of the veteran). It may also be used to display the dependent demographic data including SSN, DOB, Status, Address, Sex, Maiden (Name), Effective Date and Phone (Number).
- MT - Used to enter/edit last year's marital status for the veteran.
- AD - This protocol is not selectable from the registration screens.
- RE - This protocol is not selectable from the registration screens.

At the beginnin*g* of the registration process, “Enrollment/Eligibility Query sent ...” displays on your screen to notify you that the software sent an enrollment query for the selected patient to the patient database at the Health Eligibility Center (HEC).

When patient demographic data is retrieved for a patient who was marked as “Sensitive”, by the HEC the following table describes the actions that are taken at the Requesting Site (RS).

<table>
<caption><p>Table 8: For US and US Possessions only, Field Column in the Report may Include Data in One or More of the Fields from the PATIENT File (#2)</p></caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>Scenario</th>
<th>Actions Taken at RS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sensitive Patient Flag (SPF) received from HEC &amp; flagged “Sensitive” at LST</td>
<td><ol type="1">
<li><p>Patient demographic data for “Sensitive” designated patients at the LST is retrieved and filed directly into the RS’s local database.</p></li>
<li><p>Indicators, flags, and/or file entries that identify the patient as “Sensitive” are <strong>not</strong> retrieved.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>SPF received from HEC &amp; not flagged “Sensitive” at LST</td>
<td><ol type="1">
<li><p>Patient demographic data for “Non-Sensitive” designated patients at the LST is retrieved and filed directly into the RS’s local database.</p></li>
<li><p>Indicators, flags, and/or file entries that identify the patient as “Sensitive” are <strong>not</strong> retrieved.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>SPF not received from HEC &amp; flagged “Sensitive” at LST</td>
<td><ol type="1">
<li><p>Patient demographic data for “Sensitive” designated patients at the LST is retrieved and filed directly into the RS’s local database.</p></li>
<li><p>Indicators, flags, and/or file entries that identify the patient as “Sensitive” are retrieved and filed at the RS.</p></li>
<li><p>A “Sensitive Patient Data Retrieved” notification mail message is automatically sent to a new mail group and to the local user at the RS who registered the patient.</p></li>
<li><p>A mail bulletin is also sent to the ISO to provide notification that a sensitive patient record was accessed and create the appropriate entry in the existing Security Log File audit trail.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>SPF not received from HEC &amp; not flagged “Sensitive” at LST</td>
<td><ol type="1">
<li><p>Patient demographic data for “Non-Sensitive” designated patients at the LST is retrieved and filed directly into the RS’s local database.</p></li>
<li><p>Indicators, flags, and/or file entries that identify the patient as “Sensitive” are <strong>not</strong> retrieved.</p></li>
</ol></td>
</tr>
</tbody>
</table>

Table 8: For US and US Possessions only, Field Column in the Report may Include Data in One or More of the Fields from the PATIENT File (#2)

When patient demographic data is retrieved for a patient who has a Date of Death recorded at the LST, a message displays on the screen that Date of Death information was retrieved. The Date of Death information is not automatically filed into the requesting site’s database; instead, it is placed into a mail message and sent to the RO mail group.

The Veterans Healthcare Eligibility Reform Act of 1996, PL 104-262, prohibits providing care for veterans who are not enrolled after November 1, 1998 (with limited exceptions). The Register a Patient option displays enrollment information and provides the ability to enroll the patient in the VHA Enrollment System. If a Veteran does not wish to enroll, the Enrollment Status is set to the NOT ENROLLED status of REGISTRATION ONLY. Nonveterans are also set to the NOT ENROLLED status of REGISTRATION ONLY.

A preliminary priority value is calculated on an initial enrollment application. In the case of EGT Type 2 (STOP NEW ENROLLMENTS THIS CYCLE), if the preliminary priority is at or below the latest EGT setting for a new enrollee or below the latest EGT for a current enrollee, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” shall be assigned. In the case of EGT Type 1 (ANNUAL FISCAL YEAR) or EGT Type 3 (MID-CYCLE), if the preliminary priority is below the latest EGT setting, a preliminary Enrollment Category of “Not Enrolled” and a preliminary Enrollment Status of “Rejected - Initial Application by VAMC” shall be assigned. If the preliminary priority cannot be calculated or is calculated above the latest EGT setting, a preliminary Enrollment Category of “In Process” and a preliminary Enrollment Status of “Unverified” shall be assigned. At verification, the HEC recalculates these fields based on a Master Veteran Record containing all nationally available patient data.

A query is automatically sent to the Health Eligibility Center (HEC) when a patient registration is completed through this option. This query determines if a Means Test or Copay Exemption Test (with Income Screening information) was completed for the veteran for a specified income year. The HEC processes the query, and if there is a completed Means Test or Copay Exemption Test (with Income Screening information), the HEC transmits the Primary test and any Hardship determinations to the VAMC that sent the query.

The veteran’s Long Term Care (LTC) copayment status and last test date displays when using this option. If the last test is over a year old, the message “\*\*NEW TEST REQUIRED\*\*” displays. If the veteran did not agree to pay the copayments, the following ineligible message displays.

Patient INELIGIBLE to Receive LTC Services -- Did Not Agree to Pay Copayments

## Report - All Address Change with Rx

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Report - All Address Change with Rx option lists those patients with active pharmacy prescriptions whose primary address fields were changed during the previous 24 hours.

The output is sent to the DG DAILY ADDRESS CHANGE mail group. If the mail group is not populated, the following message displays when running the option.

“DG DAILY ADDRESS CHANGE does not have a member. Report not sent.”

The output may contain the following information.

- Patient’s name and last four numbers of SSN
- Name of the user who made the last change(s) and date/time the last change(s) were made
- Source of change (VAMC, HEC, etc.)
- Mailing address as of 24 hours ago
- Mailing address as of now
- Foreign address changes
- Home and work phone numbers
- Count indicating total number of records listed on the report

It is recommended that this report be queued to run after normal business hours.

## Report - All Address Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a patient’s mailing address is changed during the previous 24 hours, this report lists the patient mailing address as of now and the patient mailing address as of 24 hours ago. It is run from the Registration Menu, or scheduled via Task Manager (TaskMan). If run from the Registration Menu, you are prompted to enter a start time (or accept the default “NOW”); the task is queued to run at that time.

From the Registration Menu

Select the Report - All Address Changes option. You are prompted to enter a start time (or accept the default “NOW”); the task is queued to run at that time.

From Task Manager

1.  Select the TaskMan Management Menu.
5.  Select Schedule/Unschedule Options.
6.  Enter DG ALL ADDRESS CHANGE REPORT as the option to schedule or reschedule. Verify that this is the correct option.
7.  In the Edit Option Schedule Screen, press Enter to navigate between fields.
8.  In the QUEUED TO RUN AT WHAT TIME: field, enter the date/time you want this option to be started by TaskMan.
9.  In the RESCHEDULING FREQUENCY: field, enter the value that represents how frequently you want TaskMan to automatically reschedule the report. For example, enter 24H if you want the report to run every 24 hours, 1D if you want the report to run at the same time every day, etc.
10. In the COMMAND: field, enter SAVE to save your changes, then EXIT to return to the “Select OPTION to schedule or reschedule:” prompt.

The output is sent to the DG DAILY ADDRESS CHANGE mail group (but is not annotated as a new message). Remember to populate this mail group with the staff that should receive this mail message. The output contains the following information:

- Patient’s name and last four numbers of SSN
- Name of the user who made the last change(s) and date/time the last change(s) were made
- Source of change (VAMC, HEC, etc.)
- Mailing address as of 24 hours ago
- Mailing address as of now
- Foreign address changes
- Notification if patient has active pharmacy prescription(s)

## Report - All Patients flagged with a Bad Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option produces a report listing all patients for whom a Bad Address Indicator (Undeliverable, Homeless, or Other) is entered. It includes the patient’s name and the last four digits of the patient’s social security number.

The Bad Address Indicator applies to the address at which the patient resides. It is entered during the patient registration process on Screen 1 - Patient Demographic Data. Setting this field prevents a bad address from being shared with HEC and other VAMC facilities. It is also used to block the sending of Means Test Renewal Letters.

> **NOTE:** The Veterans Financial Assessment Project removed the requirement for veterans to complete an annual means test. The Means Test Renewal Letter options were disabled with EAS\*1\*106 released in host file DG_53_P858.

Once the Bad Address Indicator is set, incoming “newer” addresses and/or address updates manually entered by VAMC site staff automatically removes the Bad Address Indicator and allow the “updated” address to be transmitted to HEC and other VAMC facilities.

The only prompt is for Device. It is recommended that you queue this report to print, as it may be quite lengthy.

## Report - Patient Catastrophic Edits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print a report for a user-selected date range (up to one year), which provides a listing of patients who were flagged as having a potential catastrophic edit alert created for supervisory review.

In order to prevent catastrophic edits to a patient’s identity, four patient identity fields were established. They are patient name (first and/or last name components), social security number, date of birth, and sex. If modifications are made to two or more of these fields within one edit session, a warning alert displays. If you proceed with the edits, an alert with the potential patient catastrophic edits is forwarded to your site’s ADPAC and appropriate supervisor for review and action. The DG CATASTROPHIC EDIT security key is required, in order to receive and review the alerts. If this key is not assigned, the alerts are forwarded to personnel holding the DG SUPERVISOR security key. The alerts remain on file for one year.

You may choose to print a detailed or summary report. The summary report includes the number of potential catastrophic edit alerts posted, alerts reviewed, and alerts determined to be catastrophic. In the detailed report you may choose to display all alerts, only those not reviewed, or only those with catastrophic edit. In the detailed report each applicable patient’s data displays.

You must hold the DG SUPERVISOR security key to access this option.

## Unsupported CV End Dates Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Eligibility Center (HEC) calculates and shares the CV End Date with the VAMCs to support the CV determination. This option runs a report that helps the VAMCs to identify CV End Dates without the supporting MSD.

The report has the following fields:

- Veteran’s DFN
- Veteran’s Name and SSN
- CV End Date

The report may be sorted by:

- Veteran’s DFN
- Veteran’s Name

A bulletin is sent to the members of the DGEN ELIGIBILITY ALERT mail group at the veteran’s VAMCs of record to update the veteran’s CV Eligibility information when there is a change to the CV Eligibility End Date at the HEC.

The following is an example of the Unsupported CV End Date Bulletin.

> **NOTE:** The Veteran’s DFN displays in the Subject line to help you correlate the data in the bulletin to the data in the Unsupported CV End Date Report.

Subj: DFN: 7171686 - CV END DATE IS UNSUPPORTED \[#33613\]

25 Jun 2004 12:56:20 -0500 (EST) 23 lines

From: \<ADTEMPLOYEE,ONE@PENMGR.REDACTED\> In 'IN' basket. Page 1 \*New\*

------------------------------------------------------------------------------

A New Combat Vet Eligibility End Date has been determined at HEC for

the following patient:

Name: ADTpatient,One

SSN: 000168000

CV End Dt: Jun 20, 2006

This new Combat Vet Eligibility End was determined using the following

Military Service and Conflict Information from Site \# 500:

Branch of Service\[Last\]: ARMY

Service Number\[Last\]: 000168000

Service Entry Date\[Last\]: Feb 01, 2002

Service Separation Date\[Last\]: Jun 21, 2004

Service Discharge Type\[Last\]: HONORABLE

Conflict Location: PERSIAN GULF WAR

Conflict Indicator: YES

Conflict From Date: Aug 02, 2002

Conflict To Date: Feb 21, 2004

Please update your records to reflect the above information or contact the

site listed above if this information is inaccurate.

## Former OTH Patient Eligibility Change Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is available under DGEN ENROLLMENT REPORTS Menu and used to identify Former Service Members whose Primary Eligibility changed from EXPANDED MH CARE NON-ENROLLEE to a new Primary Eligibility as determined by Veterans Benefits Administration (VBA) post adjudication.

The report has the following fields:

- Patient Name
- DOB
- PID (Patient Indicated Date)
- OTH Reg Date  
- New Elig Code   
- SC% 
- Eligibility Change Date  
- Station ID 

OTH Reg Date is the date when the patient was registered as Expanded MH Care Non-Enrollee under Other Than Honorable (OTH) authority and Eligibility Change Date is the date when patient’s eligibility changed post VBA adjudication.

> **NOTE:** The date range entered is used to select the “episode of care” and/or “released prescriptions”

for OTH Patients that have been adjudicated at the time the report is run. Therefore, it is possible

to have an active OTH eligibility when the episode of care occurred.

> **NOTE:** For integrated sites, all division(s) where the patient was treated are displayed, and for non-integrated sites only the parent facility station IDs are displayed.

## Former OTH Patient Detail Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is available under DGEN ENROLLMENT REPORTS Menu for VA Medical Center (VAMC) Enrollment/Eligibility staff access and contains Former Service Member’s eligibility change, episodes of care (outpatient, inpatient, and prescriptions) information.

This report is used by the Health Administration Services/Benefits Assistance Service (HAS/BAS)/Billing staff to review current eligibility, past episodes of care (outpatient/inpatient) and prescriptions provided to Former Service Member with Other Than Honorable discharge and determine whether they should be back-billed for treatments occurred during pending VBA adjudication period based on VBA outcomes.

## View Patient Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to view a patient's mailing address and address change information. The user is prompted to select a patient's name and print device. The output includes the following information:

- Patient Name
- Mailing Address
1.  If the selected patient has a temporary and/or confidential and/or residential address, the system asks if you would like to view it.
31. If the selected patient only has a mailing address on file, the screen display includes verification that the patient has no temporary, confidential, or residential address on file.
- Address Change Date
- Address Change Source (Mailing and Residential Address only)
- Address Change Site
- Bad Address Indicator (Mailing Address only. Refer to Screen \<1.1\> Data Group 2, in the Registration Supplement of this manual for more information about the Bad Address Indicator.)
- Address Start Date (Temporary and Confidential Address only)
- Address End Date (Temporary and Confidential Address only)

## View Registration Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Registration Data option allows you to view the registration information contained in a patient's record. You are not able to edit a patient's data using this option.

As with the entry/edit of this information, viewing is accomplished in a series of screens. There are fifteen screens distributed with the PIMS package. Your site has the ability to create its own screen in order to collect certain needed data or capture data in a different format. You may turn certain data screens ON and OFF according to patient type. Within the screens, you may specify which data groups should be editable.

You may move from screen to screen either by entering \<^#\> to specify the screen number you wish to move to, \<RET\> to move to the next screen, \<?\> to access its HELP screen, or \<^\> to quit.

# Other Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Invalid State/Inactive County Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to create a report that lists patient records whose address fields contain invalid states and/or inactive counties according to the following criteria.

- A state is considered invalid, and displays on the report, if the AAC RECOGNIZED field (#2.1) in the STATE file (#5) is set to “No”  
  OR  
  The first character of the state name is “Z”
- A county is considered inactive, and displays on the report, if it has a date in the INACTIVE DATE field (#5) in the COUNTY sub-file (#5.01) of the STATE file (#5)  
  OR  
  The county is in a state whose AAC RECOGNIZED field (#2.1) in the STATE file (#5) is set to “No”
- An address is considered a US or US Possession, if the US STATE OR POSSESSION field (#2.2) in the STATE file (#5) is set to “Yes”
- An address is considered foreign if the US STATE OR POSSESSION field (#2.2) is set to “No” or blank

> **NOTE:** Even if the address is considered foreign, it displays on the report only if the AAC RECOGNIZED field (#2.1) in the STATE file (#5) is set to “No” for that particular entry.

If you run the report for the purpose of resolving the discrepancies, it displays; be sure to use the appropriate resources to verify the correctness of the changes you wish to make. Edit the fields in the PATIENT file (#2) by using the Load/Edit Patient Data option on the Registration Menu. This report may take a long time to generate; you should queue it to print at a later time.

PATIENT file (#2) fields reported at your site as containing incorrect state data should be edited only to states recognized by the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)). PATIENT file (#2) fields reported as containing inactive counties should be edited only to counties that have no inactive date and are connected to states that are recognized by the AITC.

You can choose to run the report for U.S. and U.S. Possessions Only, Foreign Addresses Only, or Both. If you choose “Both”, you receive outputs for both U.S. and U.S. Possessions Only and Foreign Addresses Only. Each time you run the report, you receive a VA MailMan message containing summary data. The report includes the following information for all output criteria:

- Report title (“Report of States Not Recognized by AITC and Inactive Counties”)
- Report subtitle (“U.S. and U.S. Possessions Only” and/or “Foreign Addresses Only”)
- Page number(s)
- Patient Name
- Patient SSN
- Field\*
- State/County

\*The Field column in the report may include data in one or more of the fields from the PATIENT file (#2) listed in the following tables.

| Field Number | Field Name                       | Displays on the Report as     |
|--------------|----------------------------------|-------------------------------|
| .093         | PLACE OF BIRTH \[STATE\]         | Place of Birth                |
| .115         | STATE                            | Mailing Address - State       |
| .117         | COUNTY                           | Mailing Address - County      |
| .1215        | TEMPORARY STATE                  | Temporary Address - State     |
| .12111       | TEMPORARY COUNTY                 | Temporary Address - County    |
| .1415        | CONFIDENTIAL ADDRESS STATE       | Confidential Address - State  |
| .14111       | CONFIDENTIAL ADDRESS COUNTY      | Confidential Address - County |
| .1654        | INELIGIBLE TWX STATE             | Ineligible TWX                |
| .1659        | MISSING PERSON TWX STATE Missing | Person TWX                    |
| .217         | K-STATE                          | Next of Kin                   |
| .2197        | K2-STATE                         | Next of Kin 2                 |
| .256         | SPOUSE'S EMPLOYER'S STATE        | Spouse's Employer             |
| .2917        | STATE (VA)                       | VA Guardian                   |
| .2927        | STATE (CIVIL)                    | Civil Guardian                |
| .3117        | EMPLOYER STATE                   | Employer                      |
| .3317        | E2-STATE                         | Emergency Contact 2           |
| .337         | E-STATE                          | Emergency Contact             |
| .347         | D-STATE                          | Designee                      |
| 2.06         | INS TYPE-EMPLOYER CLAIMS STATE   | Insurance Type - Emp Claims   |
| 3.09         | INS TYPE-INSURED'S STATE         | Insurance Type - Insured's    |
| 13           | INS TYPE-AGENT'S STATE           | Insurance Type - Agent's      |
| 35           | INS TYPE-A-STATE                 | Attorney                      |

Table 9: For Foreign Addresses only, Field Column in the Report may Include Data in One or More of the Fields from the PATIENT File (#2)

| Field Number | Field Name                 | Appears on the Report as     |
|--------------|----------------------------|------------------------------|
| .115         | STATE                      | Mailing Address - State      |
| .1215        | TEMPORARY STATE            | Temporary Address - State    |
| .1415        | CONFIDENTIAL ADDRESS STATE | Confidential Address - State |

Table 10: Required Fields for Residential Address

## Patient Address Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Address Update option is used to update a patient’s mailing address, temporary mailing address, or both. If you choose to update both, you must update the mailing address first, then the temporary mailing address.

After each mailing address update:

- The address entered by the user is sent to the UAM Validation Service and the results of the address validation are displayed to the user. The user selects the address they want to store and press enter.
- The old and the new address information is displayed and the system asks the user *Are you sure that you want to save the above changes?*
- If the user answers YES, the system displays “Change saved”, the patient’s mailing address change date/time stamp is updated, and a trigger is set to send a message to the HEC.
- If the user answers NO, the change is aborted and no data is saved.

This option does not update the ADDRESS CHANGE DT/TM field (#.118) of the PATIENT file (#2) if no changes were made to the Mailing Address. It may be placed on other applications’ menus, so users can update the patient’s mailing address, temporary mailing address, or both, directly from the menus of their applications.

## Other Than Honorable Former Service Members

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Former service members who received an Other Than Honorable (OTH) character of discharge can receive VA mental health care while awaiting VBA adjudication.

OTH patients are registered (in VistA Registration screen 7) using a primary eligibility of EXPANDED MH CARE NON-ENROLLEE. Once that primary eligibility is selected, the system will prompt the registration specialist for an EXPANDED MH CARE TYPE.

- There are two options of ‘Expanded MH Care Type’ from which to select: OTH-90 and OTH-EXT (for OTH Extended).
- The registration clerk must select a value for ‘Expanded MH Care Type’ if the selected Primary eligibility is EXPANDED MH CARE NON-ENROLLEE.

If a patient meets the eligibility criteria for either OTH-90 or OTH-EXT, an ‘OTH’ version of the MST Screening Clinical Reminder will be created for the patient within CPRS as Due Now on their patient chart.

- If the patient is initially registered as OTH-90, and the ‘OTH’ version of the MST Screening Clinical Reminder is answered positively in CPRS, VistA will automatically change the patient’s registration EXPANDED MH CARE TYPE value from OTH-90 to OTH-EXT (Registration screen 7). Once the automatic update to the patient’s registration is complete, a Mailman message will be sent to the DGEN ELIGIBILITY group at the sites the patient is registered in, letting them know the system changed the patient’s Expanded MH Care Type value.
- If the patient’s registration is automatically updated as in scenario (a) above, but later the ‘OTH’ version of the MST Screening Clinical Reminder is processed *again* manually for the patient and this time answered No or Declined to Answer, a Mailman message will be sent to the DGEN ELIGIBILITY group at the sites the patient is registered in, alerting them that the eligibility for this patient needs to be re-assessed.
- If the patient’s registration is automatically updated as in scenario (a) above, the system will set: the ELIGIBILITY STATUS to VERFIED on Registration screen 7;

> STATUS DATE to be the date the system automatically changed the record from OTH-90 to OTH-EXT;

> STATUS ENTERED BY to blank (no value) if the Provider could not be determined by CPRS and sent to VistA at the point the MST update was made, else it will contain the full name of the Provider sent over by CPRS.

- If a patient is registered as a NON OTH patient and if they screen positively for MST, but then the patient’s eligibility is manually changed to OTH-EXT and if screened again for MST but answer negatively or decline to answer, then a Mailman message will be sent to the DGEN ELIGIBILITY group at the site the patient is registered to alert them that the eligibility for this patient needs to be re-assessed.

Additional information may be found under “Appendix A – Registration Supplement”

Registration screen 7, Data Group 3 (see EXPANDED MH CARE TYPE).

The OTH options are in the Other Than Honorable Patient’s Menu \[DG OTH MENU\] found in the Registration Menu \[DG REGISTRATION MENU\]. The Other Than Honorable Patient’s Menu \[DG OTH MENU\] contains the following options:

- OTH Management \[DG OTH MANAGEMENT\]
- Patient Inquiry (OTH) \[DG OTH PATIENT INQUIRY\]
- Other Than Honorable Reports ... \[DG OTH REPORTS MENU\]

The Other Than Honorable Reports available to be run in the DG OTH REPORTS MENU are:

- Tracking Report (OTH-90) \[DG OTH 90-DAY PERIOD\]
- Authorization Reports (OTH-90) \[DG OTH OTH90 AUTH REPORTS\]
- Other Than Honorable MH Status Report \[DG OTH MH STATUS REPORT\]
- Potential 'OTH' Patient Report \[DG OTH POTENTIAL OTH\]
- Former OTH Patient Eligibility Change Report \[DG OTH FSM ELIG. CHANGE REPORT\]
- Former OTH Patient Detail Report \[DG OTH FSM DETAIL REPORT\]

OTH Security Keys

> The OTH Management \[DG OTH MANAGEMENT\] option allows users to add additional 90-day periods for OTH patients. A 90-day period is an episode of care for an OTH patient.

> DG OTH ADD PERIOD security key - Allows a user to add an additional 90-day period 

> DG OTH MANAGER security key - Allows a user to back date a period

> Note: A security key is not needed to access OTH Management \[DG OTH MANAGEMENT\] option, but the keys are needed to perform specific actions within the option.

<span id="_Toc48821847" class="anchor"></span>Appendix A: Registration Supplement

The collecting of patient registration data is done via a series of formatted data screens. There are fifteen of these screens distributed with the Patient Information Management System (PIMS) package. The first eleven are dedicated to gathering the patient's registration information. This information makes up the patient's "file" in your computer. Screens 12-14 are for information purposes only and the data contained on them is not editable. They provide past admission and application information, as well as the patient's clinic enrollments and a listing of future appointments. Each screen also has an associated HELP screen that may be accessed by entering a \<?\> at the prompt on each screen. Following is a list of the fifteen screens.

Screen \#1 PATIENT DEMOGRAPHIC DATA

Screen \#1.1 ADDITIONAL PATIENT DEMOGRAPHIC DATA

Screen \#2 PATIENT DATA

Screen \#3 EMERGENCY CONTACT DATA

Screen \#4 APPLICANT/SPOUSE EMPLOYMENT DATA

Screen \#5 INSURANCE DATA

Screen \#6 MILITARY SERVICE DATA

Screen \#7 ELIGIBILITY STATUS DATA

Screen \#8 FAMILY DEMOGRAPHIC DATA

Screen \#9 INCOME SCREENING DATA

Screen \#10 INELIGIBLE/MISSING DATA

Screen \#11 ELIGIBILITY VERIFICATION DATA

Screen \#12 ADMISSION INFORMATION

Screen \#13 APPLICATION INFORMATION

Screen \#14 APPOINTMENT INFORMATION

Screen \#15 SPONSOR DEMOGRAPHIC INFORMATION

The registration or load/editing process varies from patient to patient and user to user. This is due to several factors: the patient type, your site parameters, whether certain data was verified, and whether you hold the DG ELIGIBILITY security key.

For each new patient entered into the system, you are prompted to enter a patient type. Patient types are distributed with the package. Patient type determines (in part) which screens are presented during the registration process, as well as which data items on the screens are available for entry/edit. Screens 1, 1.1, 2, 4, 5, 7, 12, 13, 14, and 15 are always presented. The presentation of Screens 3, 6, 8, 9, 10, and 11 varies, because your site has the ability to turn these screens OFF and ON according to patient type. This was done to allow sites flexibility in the collection of their patient data. For example, a site may not want to collect military service data for a collateral patient. Therefore, the Military Service Data Screen is turned OFF for that patient type.

Your site is also able to set up an additional registration screen should it wish to capture certain data in a different format. The fields displayed on this screen must already exist in the system (PATIENT file (#2)), so the data prompts associated with such a screen would be familiar to you. This screen, if set up, always displays at the end of the registration process.

Certain data such as an applicant's name, SSN, date of birth, eligibility, monetary benefits, and service record are subject to verification. The verification must be performed by someone with the DG ELIGIBILITY security key. Up until the time of verification, any user is able to enter/edit data pertaining to these categories. After verification, the data may be viewed by all users; however, only those who hold the DG ELIGIBILITY security key are able to edit this data.

PSEUDO SSN Note: For every option that displays the patient’s SSN, if the patient has a Pseudo SSN on file, the message “\*\*Pseudo SSN\*\*" displays next to the SSN.

Electronic Data Interchange Personal Identifier (EDIPI NOTE): For every option that displays the patient’s information header, the Electronic Data Interchange Personal Identifier (EDIPI) displays before the SSN. The display of the EDIPI is optional and this will only display if the patient has this information on file.

Each screen (excluding Screen 8) is set up in numbered data groups. If the number of the data group displays in brackets \[ \], you are able to enter/edit its data. If it displays in arrows \< \>, you cannot enter/edit. A High Intensity feature was also supplied. If this feature is turned ON (through the MAS Parameter Entry/Edit option of the ADT System Definition menu), those data groups that you may edit are highlighted on your screen, while those that are not editable are not highlighted. The system determines which information is editable by user and patient type.

Screen 8 uses the List Manager utility. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.

For the purposes of this Supplement, all non-informational screens and data groups are shown as being "available"; that is, their corresponding numbers are surrounded by brackets \[ \]. Keep in mind that this may not be the case when you are actually working on the system.

No defaults are shown in this Supplement. If you are editing the record of an existing patient, previously entered information displays as a default. You may enter a \<RET\> to accept the default value.

The following are examples of each Registration Data Screen, along with definitions of each of the data groups and associated fields. Information that is subject to verification is indicated. Fields that are indented are prompted, based upon the entry made at the primary prompt (the prompt under which the field is indented). Much of the time, data entered into these fields is deleted when changing or deleting the entry at the primary prompt. This is explained for each appropriate data grouping or field.

Preferred Language Enhancement

The VistA Admit, Discharge, and Transfer (ADT) and Scheduling Packages support the capture of the preferred language preferences of the Veteran. This data facilitates better treatment for the Veteran by allowing precise verbal communication through use of interpreters if necessary. The Register a Patient \[DG REGISTER PATIENT\] and the Make Appointment \[SDM\] options require the input of the patient's preferred language. The LANGUAGE file (#.85) was updated with the VA FileMan release 22.2 and contains the complete list of ISO standard languages.

Screen capture of the Patient Demographic Data Screen \<1\>: In the patient information header, the Electronic Data Interchange Personal Identifier (EDIPI) displays before the SSN. With the release of patch DG\*5.3\*941, Patient Demographic Data Screen \<1\> and Additional Patient Demographic Data Screen \<1.1\> are redesigned to accommodate a new address type of Residential Address. This address is used by Enrollment and Eligibility to retain the geographic residence of an applicant or patient. It supports the Enrollment System Community Care program's need to determine geographic distance from a treatment facility. A new field “Coding Accuracy Support System (CASS) Certified” was added to all address types to store whether postal addresses meet United States Postal Service (USPS) format standards. The addresses will be validated and CASS indicators for the validation statuses are visible via FileMan.

PATIENT DEMOGRAPHIC DATA SCREEN \<1\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

===============================================================================

INELIGIBLE/MISSING MESSAGE MAY BE DISPLAYED HERE

\[1\] Name: \[6\] Preferred Name:

DOB:

SS:

Family: Birth Sex: MBI:

Given: \[2\] Alias:

Middle:

Prefix:

Suffix:

Degree:

Self-Identified Gender Identity:

\[3\] Remarks:

\[4\] Cell Phone: Pager \#:

Email Address:

\[5\] Pref Lang: Date/Time:

\<RET\> to CONTINUE, 1-6 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATA GROUP 1

Once a patient's eligibility is verified, the information contained in this data group may not be edited by anyone not holding the DG ELIGIBILITY security key. Up until the time of eligibility verification, any user may enter/edit these fields. After verification, it is available for viewing to all users; however, only holders of the DG ELIGIBILITY security key are able to enter/edit the information.

In order to prevent catastrophic edits to a patient’s identity, four patient identity fields were established. They are patient name (first and/or last name components), social security number, date of birth, and birth sex. If modifications are made to two or more of these fields within one edit session, a warning alert displays. If you proceed with the edits, an alert with the potential patient catastrophic edits is forwarded to your site’s ADPAC and appropriate supervisor for review and action. In addition, the after edits of the patient identification fields display an asterisk to highlight the edited fields that were modified when the alert was generated. The alerts remain on file for one year.

- FAMILY (LAST) NAME - Enter the applicant's last name
- GIVEN (FIRST) NAME - Enter the applicant's first name
- MIDDLE NAME - Enter the applicant's middle name
- PREFIX - Enter applicant’s name prefix, such as Mr or Mrs
- SUFFIX - Enter applicant’s name suffix, such as JR, SR, II, III
- DEGREE - Enter applicant’s academic degree, such as BA, BS, MD, or PhD
- SOCIAL SECURITY NUMBER - Answer with the individual’s social security number must be 9 numbers in length)
1.  The SSN is sent to the Social Security Administration (SSA) for verification. After the SSN status is verified by the SSA, it can only be edited by members of the Identity Management Data Quality Team, and VERIFIED displays next to the SSN. If the SSN status is Invalid per SSA, INVALID displays next to the SSN.
32. If a valid SSN is not known, enter P at the “SOCIAL SECURITY NUMBER” prompt for the system to automatically assign a Pseudo SSN. You must then enter a Pseudo SSN reason. You should make every effort to obtain the patient’s actual SSN.
- DATE OF BIRTH - Enter the applicant's date of birth  
  Date of Birth cannot be a date after the Ineligible date and cannot be a date after the Application Date.
- BIRTH SEX - M for MALE (default), F for FEMALE
- MULTIPLE BIRTH INDICATOR (MBI) - Is this applicant part of a multiple birth? N for NO (default), Y for YES - part of multiple birth
- SELF-IDENTIFIED GENDER IDENTITY - Select the code that specifies the patient's preferred gender. This SELF IDENTIFIED GENDER value indicates the patient's view of their Gender Identity, if they choose to provide it.

  You may enter a \<?\> to select from a list of available entries:

  M - Male

  F - Female

  TM - Transmale/Transman/Female-to-Male

  TF - Transfemale/Transwoman/Male-to-Female

  O – Other

  N - Individual chooses not to answer

DATA GROUP 2

- ALIAS - Alternate name (if any) the applicant uses (2-30 characters)  
  An entry in this field is automatically cross-referenced and the applicant may be called up using this alias. This is a multiple field; you are returned to this prompt repeatedly until no more entries are made. For each entry, the following is prompted.
- ALIAS SSN - Alternate social security number applicant uses, if any.

DATA GROUP 3

REMARKS - You may enter a free text comment (3-60 characters) regarding the patient.

- If a patient was declared ineligible, a remark to indicate this is automatically inserted into this field.
- If a patient's enrollment status is REJECTED, a remark to indicate this, is automatically inserted into this field.

DATA GROUP 4

This data group allows you to enter, edit, and delete a Veteran’s cell phone number, pager number, and email address. If the Email Address Indicator is set to “YES”, the email address is required. If entered, an “@” character is required in order for the email address to be accepted and stored.

- PHONE NUMBER \[CELLULAR\] – Enter the telephone number \[4 – 20 characters\] for this applicant’s cellular phone. The entry may contain numbers \[0-9\], parentheses \[( )\], dashes \[-\], periods \[.\], and spaces. Alpha characters \[A-Z\] are not allowed. Cellular phone number is not required.
- PAGER NUMBER – The applicant’s pager number \[4 – 20 characters\] is not editable and appears only if populated. The entry may contain numbers \[0-9\], parentheses \[( )\], dashes \[-\], periods \[.\], and spaces. Alpha characters \[A-Z\] are not allowed. Pager number is not required.
- EMAIL ADDRESS INDICATOR - Enter “YES” or “NO”. The Email Address Indicator and its associated date/time stamp do not display on Screen \<1\>, but are stored in the PATIENT (#2) file.
- EMAIL ADDRESS – Email address is required if the Email Address Indicator is set to “YES”. Email address cannot be entered if the Email Address Indicator is not set to “YES”.  
  > Enter the applicant’s email address \[1 – NN characters\] if the Email Address Indicator is set to “Y” (YES). If entered, the address must contain an “@” character. Email address is not required.

DATA GROUP 5

This data group allows you to enter the Preferred Language for the patient.

DATA GROUP 6

This data group allows you to enter the Preferred Name for the patient. The Preferred Name field identifies the name that the patient would prefer to be referenced by during interactions at the medical facility. It is 1-25 characters in length and may contain only alphabetical characters and spaces.

ADDITIONAL PATIENT DEMOGRAPHIC DATA SCREEN \<1.1\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

===========================================================++++++======

\[1\] Residential Address: \[2\] Mailing Address:

3456 WEST POLIUS LANE 3456 WEST POLIUS LANE

POSITION DRAW 2345 POSITION DRAW 2345

RM 234 RM 442

LAKEWOOD RANCH,FL 34211 LAKEWOOD RANCH,FL 34211

UNITED STATES UNITED STATES

County: MANATEE (081) County: MANATEE (081)

Phone: REDACTED Bad Addr:

Office: UNANSWERED

\[3\] Temporary Mailing Address: \[4\] Confidential Mailing Address:

NO TEMPORARY MAILING ADDRESS NONE ON FILE

Phone: NOT APPLICABLE Phone: NOT APPLICABLE

From/To: NOT APPLICABLE From/To: NOT APPLICABLE

Categories: NOT APPLICABLE

\<RET\> to CONTINUE, 1-4 or ALL to EDIT, ^N for screen N or '^' to QUIT: 1

RESIDENTIAL COUNTRY: UNITED STATES// UNITED STATES USA United States

RESIDENTIAL ADDRESS \[LINE 1\]: 3456 WEST POLIUS LANE

Replace

RESIDENTIAL ADDRESS \[LINE 2\]: POSITION DRAW 2345// POSITION DRAW 2345

RESIDENTIAL ADDRESS \[LINE 3\]: RM 234// RM 234

RESIDENTIAL ZIP+4: 34211// 34211

Select one of the following:

1 BRADENTON\*

2 LAKEWOOD RCH

3 LAKEWOOD RANCH

RESIDENTIAL CITY: LAKEWOOD RANCH//

STATE: FLORIDA

COUNTY: MANATEE

PHONE NUMBER \[RESIDENCE\]: REDACTED// REDACTED

PHONE NUMBER \[WORK\]:

\[NEW RESIDENTIAL ADDRESS\]

3456 WEST POLIUS LANE

POSITION DRAW 2345

RM 234

LAKEWOOD RANCH,FLORIDA 34211

UNITED STATES

County: MANATEE 081

If address is ready for validation enter \<RET\> to continue, 'E' to Edit

or '^' to quit:

Press ENTER to continue:

\[OLD RESIDENTIAL ADDRESS\]

3456 WEST POLIUS LANE

POSITION DRAW 2345

RM 234

LAKEWOOD RANCH,FLORIDA 34211

UNITED STATES

County: MANATEE 081

\[NEW RESIDENTIAL ADDRESS\]

3456 WEST POLIUS LANE

POSITION DRAW 2345

RM 234

LAKEWOOD RANCH,FLORIDA 34211

UNITED STATES

County: MANATEE 081

Are you sure that you want to save the ADDRESS changes? YES

Change saved.

Press ENTER to continue:

\[OLD PHONE NUMBERS\]

Phone: REDACTED

Office:

\[NEW PHONE NUMBERS\]

Phone: REDACTED

Office:

Are you sure that you want to save the PHONE changes? YES

Change saved.

Press ENTER to continue:

Copy the Residential Address to the Mailing Address? NO// YES

Residential Address to copy to the Mailing Address:

3456 WEST POLIUS LANE

POSITION DRAW 2345

RM 234 County: MANATEE(081)

LAKEWOOD RANCH,FL 34211

UNITED STATES

Are you sure you want to copy? // YES

Copy completed.

Press ENTER to continue:

DATA GROUP 1

The following rules apply when editing patient residential address information via the following options:

- Load/Edit Patient Data
- Register a Patient
- Preregister a Patient
- Patient Address Update

> **NOTE:** Manila, Philippines is exempt from these rules; you are able to edit all the patient residential address fields without the ZIP Code linking features.

- If a specific ZIP Code corresponds to a geographical location on file, a list of city choices is provided; an asterisk (\*) indicates the USPS default city for that ZIP Code.
- If a city name has a standard USPS abbreviation, the standard abbreviation is listed and then saved when selected.
- With the EAS GMT COUNTY EDIT key you are allowed to edit state and county and/or enter a ZIP Code that is not currently in POSTAL CODE file (#5.12) as the patient's ZIP Code (without adding the ZIP Code to file (#5.12)), or enter free text city name.\*
- If more than one state and county correspond to a ZIP Code, you are allowed to edit the STATE and COUNTY fields (even if you do not have the EAS GMT COUNTY EDIT key).

> \* The EAS GMT COUNTY EDIT security key should be assigned to the appropriate individuals at your facility.

After address edits are completed via the Load/Edit Patient Data, Register a Patient, Preregister a Patient, or Patient Address Update options, the address entered by the user is sent to the UAM Validation Service and the results of the address validation are displayed to the user. The user selects the address they want to store and press enter. The old and the new address information is displayed and the system asks the user *Are you sure that you want to save the above changes?*

- If the user answers YES, the system displays “Change saved”.
- If the user answers “NO”, or enters a single caret (^) or double caret (^^) in response to the confirmation question, all changes are aborted.
- If you enter single caret (^) or double caret (^^) during the editing of any field in the patient residential address, “EXIT NOT ALLOWED ??” displays, and the same field is prompted until you provide valid input.

For a residential address to be valid, the required fields must be present (see the table below for the list of required fields). Additionally, the address must not be a Post Office Box or General Delivery address. The following conditions would cause the validation of the residential address to fail:

- Address Line 1 starts with “P.O.” in any form – upper, lower, or mixed case; with or without the period.
- Address Line 1 starts with the word “Post Office” in upper, lower, or mixed case.
- Address Line 1 starts with the word “Box” immediately followed by a number.
- Address Line 1 contains the words “General Delivery” in upper, lower, or mixed case.

The following exceptions are allowed:

- The residential address is in Alaska or Hawaii.
- The residential address is in one of the United States territories (Guam, American Samoa, CNMI (Mariana Islands), U.S. Virgin Islands, and Philippines).

After answering the address confirmation message, the user is prompted to confirm phone number changes. The user is shown the “before change” and “after change” values for the phone number (residence) and phone number (work) display. The changes are saved if you answer “YES” in response to the confirmation message. If you time out, answer “NO”, or enter a single caret (^) or double caret (^^) in response to the confirmation question, the phone changes are aborted.

After completing the Group 1 editing, you are prompted to copy the residential address to the mailing address. This prompt is only presented if a valid residential address exists. If you answer “YES” you are shown the address that will be copied and asked to confirm. If you answer “YES”, the residential address is copied to the mailing address.

- RESIDENTIAL COUNTRY – Enter the country code, postal code, or description of the country where the patient’s residential address is located. If entering an Army/Air Force Post Office (APO) or a Fleet Post Office (FPO) address, select United States as the country. If you enter a country other than the United States, the software prompts for Province and Postal Code. Both Province and Postal Code are free text fields.
- RESIDENTIAL ADDRESS \[LINE 1\], \[LINE 2\] \[LINE 3\] – Prepopulated with the values saved in the PATIENT file (#2) if the patient has corresponding address fields saved in the PATIENT file (#2); no user entry required. Line 3 displays only if an entry exists in Line 2.
- RESIDENTIAL ZIP+4 – Prepopulated with the values saved in the PATIENT file (#2) if the patient has corresponding address fields saved in the PATIENT file (#2); no user entry required.
- RESIDENTIAL CITY – Prepopulated with the values saved in the PATIENT file (#2) if the patient has corresponding address fields saved in the PATIENT file (#2); no user entry required.
- RESIDENTIAL STATE – Prepopulated by the ZIP Code linking feature, following the zip-linking rules; no user entry required.
- RESIDENTIAL COUNTY - Prepopulated by the ZIP Code linking feature, following the zip-linking rules; no user entry required.
- PHONE NUMBER \[RESIDENCE\] - Enter applicant's residence telephone number.
- PHONE NUMBER \[WORK\] - Enter applicant's work telephone number (4-20 characters).

<table>
<caption><p>Table 11: Required Fields for Temporary Address</p></caption>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th>Required Fields for DOMESTIC Residential Address</th>
<th>Required Fields for FOREIGN Residential Address</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p>STREET ADDRESS [LINE 1]</p></li>
<li><p>CITY</p></li>
<li><p>STATE</p></li>
<li><p>ZIP</p></li>
<li><p>COUNTY</p></li>
<li><p>COUNTRY</p></li>
</ol></td>
<td><ol type="1">
<li><p>STREET ADDRESS [LINE 1]</p></li>
<li><p>CITY</p></li>
<li><p>COUNTRY</p></li>
</ol></td>
</tr>
</tbody>
</table>

Table 11: Required Fields for Temporary Address

DATA GROUP 2

The following rules apply when editing patient mailing address information via the following options:

- Load/Edit Patient Data
- Register a Patient
- Preregister a Patient
- Patient Address Update

> **NOTE:** Manila, Philippines is exempt from these rules; you are able to edit all the patient mailing address fields without the ZIP Code linking feature.

- If the mailing address is empty and there is a residential address on file, you are prompted to copy the residential address to the mailing address. If you answer “YES”, the residential address is copied to the mailing address. If you answer “NO”, the copy does not occur and you are prompted to enter the address fields.
- If a specific ZIP Code corresponds to a geographical location on file, a list of city choices is provided; an asterisk (\*) indicates the USPS default city for that ZIP Code.
- If a city name has a standard USPS abbreviation, the standard abbreviation is listed and then saved when selected.
- With the EAS GMT COUNTY EDIT key you are allowed to edit state and county and/or enter a ZIP Code that is not currently in POSTAL CODE file (#5.12) as the patient's ZIP Code (without adding the ZIP Code to File \#5.12), or enter free text city name.\*
- If more than one state and county correspond to a ZIP Code, you are allowed to edit the STATE and COUNTY fields (even if you do not have the \*EAS GMT COUNTY EDIT key).

> \* The EAS GMT COUNTY EDIT security key should be assigned to the appropriate individuals at your facility.

After address edits are completed via the Load/Edit Patient Data, Register a Patient, Preregister a Patient, or Patient Address Update options, the address entered by the user is sent to the UAM Validation Service and the results of the address validation are displayed to the user. The user selects the address they want to store and press enter. The old and the new address information is displayed and the system asks the user *Are you sure that you want to save the above changes?*

- If the user answers YES, the system displays “Change saved”, the patient’s mailing address change date/time stamp is updated, and a trigger is set to send a message to the HEC.
- If the user answers “NO”, or enters a single caret (^) or double caret (^^) in response to the confirmation question, all changes are aborted.
- If you enter single caret (^) or double caret (^^) during the editing of any field in the patient residential address, “EXIT NOT ALLOWED ??” displays, and the same field is prompted until you provide valid input.

After the confirmation message you are prompted to copy the mailing address to the residential address. This prompt is only presented if the mailing address is a valid residential address. See the residential address validation rules described above in Group 1. If you answer “YES” you are shown the address that will be copied and asked to confirm. If you answer “YES” the mailing address is copied to the residential address.

- COUNTRY – Enter the country code, postal code, or description of the country where the patient’s mailing address is located. If entering an Army/Air Force Post Office (APO) or a Fleet Post Office (FPO) address, select United States as the country. If you enter a country other than the United States, the software prompts for Province and Postal Code. Both Province and Postal Code are free text fields.
- STREET ADDRESS \[LINE 1\], \[LINE 2\] \[LINE 3\] – Prepopulated with the values saved in the PATIENT file (#2) if the patient has corresponding address fields saved in the PATIENT file (#2); no user entry required. Line 3 displays only if an entry exists in Line 2.
- ZIP+4 – Prepopulated with the values saved in the PATIENT file (#2) if the patient has corresponding address fields saved in the PATIENT file (#2); no user entry required.
- CITY – Prepopulated with the values saved in the PATIENT file (#2) if the patient has corresponding address fields saved in the PATIENT file (#2); no user entry required.
- STATE – Prepopulated by the ZIP Code linking feature, following the ZIP Code linking rules; no user entry required.
- COUNTY – Prepopulated by the ZIP Code linking feature, following the ZIP Code linking rules; no user entry required.
- BAD ADDRESS INDICATOR - Applies to the address at which the patient resides. Setting this field prevents a bad address from being shared with HEC and other VAMC facilities. It also is used to block Means Test Renewal Letters from being sent.

> **NOTE:** The Veterans Financial Assessment Project removed the requirement for Veterans to complete an annual means test. The Means Test Renewal Letter options were disabled with EAS\*1\*106 released in Host file DG_53_P858.

Once the Bad Address Indicator is set, incoming “newer” addresses and/or address updates manually entered by VAMC site staff automatically remove the Bad Address Indicator and allow the “updated” address to be transmitted to HEC and other VAMC facilities.

When a bad address is indicated at the LST, no address information is returned from the LST to the local site.

This field should be manually set as follows (if applicable):

- NULL – indicating the Veteran’s address is assumed to be good
- UNDELIVERABLE – mail sent to this address was returned or is otherwise known to be undeliverable
- HOMELESS – Veteran has no known address
- ADDRESS NOT FOUND – for use by ESR only
- OTHER – reason other than Undeliverable, Homeless, or Address Not Found

  DATA GROUP 3

This data group allows you to enter a temporary mailing address for the applicant. If a temporary mailing address is already on file and “NO" is answered at the first prompt, the START DATE and END DATE is automatically deleted. The address remains on file but can only be viewed/edited when “YES” is answered at the first prompt. To delete all temporary mailing address data, answer “NO” at the first prompt and “YES” at the following prompt: “Do you want to delete all temporary mailing address data?". To retain all data on file, enter a single caret (^) at the primary prompt.

TEMPORARY MAILING ADDRESS ACTIVE? - YES/NO - If “YES”, the following fields are also prompted.

- TEMPORARY MAILING ADDRESS START DATE - Beginning date applicant is at temporary mailing address.
- TEMPORARY MAILING ADDRESS END DATE - Ending date applicant is at temporary mailing address.
- TEMPORARY MAILING ADDRESS COUNTRY: UNITED STATES// - Enter the country code, postal code, or description of the country where the patient’s temporary mailing address is located. If entering an Army/Air Force Post Office (APO) or a Fleet Post Office (FPO) address, select United States as the country. If you enter a country other than the United States, the software prompts for Temporary Province and Temporary Postal Code. Both Temporary Province and Temporary Postal Code are free text fields.
- TEMPORARY STREET \[LINE 1\] \|
- TEMPORARY STREET \[LINE 2\] \|
- TEMPORARY STREET \[LINE 3\] \|Enter applicant's temporary mailing address/phone
- TEMPORARY ZIP+4 If a specific ZIP Code corresponds to a geographical location on file, a list of city choices are provided; an asterisk (\*) indicates the USPS default city for that ZIP Code.
- TEMPORARY CITY \|
- TEMPORARY STATE \|
- TEMPORARY MAILING ADDRESS COUNTY \|
- TEMPORARY PHONE NUMBER \|

<table>
<caption><p>Table 12: Required Fields for Confidential Address</p></caption>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th>Required Fields for DOMESTIC Temporary Address</th>
<th>Required Fields for FOREIGN Temporary Address</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p>STREET ADDRESS [LINE 1]</p></li>
<li><p>CITY</p></li>
<li><p>STATE</p></li>
<li><p>ZIP</p></li>
<li><p>COUNTY</p></li>
<li><p>COUNTRY</p></li>
</ol></td>
<td><ol type="1">
<li><p>STREET ADDRESS [LINE 1]</p></li>
</ol>
<ol start="7" type="1">
<li><p>CITY</p></li>
<li><p>COUNTRY</p></li>
</ol></td>
</tr>
</tbody>
</table>

Table 12: Required Fields for Confidential Address

> Note: You cannot exit these fields or jump to another field using the caret (^); you must enter the required information.

DATA GROUP 4

This data group allows you to enter a confidential address for the applicant. A confidential address is an alternative mailing address to be used for the mailing of confidential correspondence types designated by the Veteran. If a confidential address is already on file and “NO” is answered at the first prompt, the START DATE and END DATE are automatically deleted. The address remains on file but may only be viewed/edited when “YES” is answered at the first prompt. To delete all confidential address data, answer “NO” at the first prompt and “YES” at the following prompt: "Do you want to delete all confidential address data?" To retain all data on file, enter a single caret (^) at the primary prompt.

CONFIDENTIAL ADDRESS ACTIVE? - YES/NO - If “YES”, the following fields are also prompted.

- CONFIDENTIAL ADDRESS START DATE - Date to start using confidential address.
- CONFIDENTIAL ADDRESS END DATE - Date to stop using confidential address.
- CONFIDENTIAL ADDRESS CATEGORY - Enter the categories of mail that the Veteran sends to the confidential address. This is a multiple field. You return to this prompt repeatedly until no more categories are entered. You may enter a \<?\> to select from a list of available entries.
- CONFIDENTIAL ADDRESS COUNTRY: UNITED STATES// - Enter the country code, postal code, or description of the country where the patient’s confidential address is located. If entering an Army/Air Force Post Office (APO) or a Fleet Post Office (FPO) address, select United States as the country. If you enter a country other than the United States, the software prompts for Confidential Province and Confidential Postal Code. Both Confidential Province and Confidential Postal Code are free text fields.
- CONFIDENTIAL STREET \[LINE 1\] \|
- CONFIDENTIAL STREET \[LINE 2\] \|Enter applicant's confidential address
- CONFIDENTIAL STREET \[LINE 3\] \|
- CONFIDENTIAL ADDRESS ZIP CODE If a specific ZIP Code corresponds to a geographical location on file, a list of city choices are provided; an asterisk (\*) indicates the USPS default city for that ZIP Code.
- CONFIDENTIAL ADDRESS CITY \|
- CONFIDENTIAL ADDRESS STATE \|
- CONFIDENTIAL ADDRESS COUNTY \|
- CONFIDENTIAL PHONE NUMBER \|

<table>
<caption>Table listing the required fields fordomestic and foreign addresses under confidential addresses</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Fields for DOMESTIC Confidential Address</strong></th>
<th><strong>Required Fields for FOREIGN Confidential Address</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p>STREET ADDRESS [LINE 1]</p></li>
<li><p>CITY</p></li>
<li><p>STATE</p></li>
<li><p>ZIP</p></li>
<li><p>COUNTY</p></li>
<li><p>COUNTRY</p></li>
</ol></td>
<td><ol type="1">
<li><p>STREET ADDRESS [LINE 1]</p></li>
<li><p>CITY</p></li>
<li><p>COUNTRY</p></li>
</ol></td>
</tr>
</tbody>
</table>

Table listing the required fields fordomestic and foreign addresses under confidential addresses

> Note: You cannot exit these fields or jump to another field using the caret (^); you must enter the required information.

When an address is entered or edited by the user, that address is passed to the UAM Address Validation Service. The service will return one or more addresses from which the user can select. This list is provided via the Address Validation \<1.2\> screen.

Address Validation \<1.2\>

DGPATIENT,ONE (JUNIOR) FEB 02, 1912

XXX-XX-XXXX NSC VETERAN

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\[1\] XXX MAIN STREET

CHICAGO,ILLINOIS 60606

UNITED STATES

(User Entered Address)

\[2\] XXX MAIN STREET

SUITE 200

CHICAGO,ILLINOIS 60606-1234

UNITED STATES

Delivery Point: CONFIRMED Confidence Score: 100

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\+ Next Screen - Prev Screen ?? More Actions

SEL Select Address

Select Action:SEL//

DATA GROUP 1

The address entered by the user is displayed as the first address.

DATA GROUP 2

Addresses returned by the UAM Address Validation Service are listed below the user-entered address.

For domestic addresses, the UAM Address Validation Service includes Delivery Point field which is displayed below the address.

All addresses include a Confidence Score displayed below the address.

If the user exits the screen, the user-entered address is selected by default.

The only action available is the SEL action, which allows the user to select one of the addresses from the list.

PATIENT DATA SCREEN \<2\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

=================================================================

\[1\] Marital: POB:

Religion: Father:

SCI: Mother:

Mom's Maiden:

\[2\] Previous Care Date Location of Previous Care

\[3\] Ethnicity:

Race:

\[4\] Date of Death Information

Date of Death: Source of Notification:

Updated Date/Time: Last Edited By:

\[5\] Emergency Response:

\<6\> Indian

\<RET\> to CONTINUE, 1,2,3,5 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATA GROUP 1

- MARITAL STATUS - Enter the appropriate marital status for the applicant. You may enter a \<?\> to obtain a list of choices.
- RELIGIOUS PREFERENCE - Enter applicant's religion or code. You may enter a \<?\> to obtain a list of choices.
- PLACE OF BIRTH \[CITY\] - Enter city (or foreign country if born outside U.S.) where applicant was born (2-20 characters).
- PLACE OF BIRTH \[STATE\] - Enter state or state code where applicant was born. You may enter a \<?\> to select from available list.
- FATHER'S NAME - Enter name of applicant's father in “LAST,FIRST MIDDLE SUFFIX” format.
- MOTHER'S NAME - Enter name of applicant's mother in “LAST,FIRST MIDDLE SUFFIX” format.
- MOTHER'S MAIDEN NAME - Enter maiden name (last name prior to marriage) of applicant's mother (3-35 characters).
- SPINAL CORD INJURY - Is the applicant a spinal cord injury patient? Enter the appropriate value. You may enter a \<?\> to obtain a current list of choices.

DATA GROUP 2

This group is used to enter the past two dates and locations of the applicant's last VA care (aside from the facility to which the veteran is applying). When YES is answered at the initial prompt (REC'D VA CARE PREVIOUSLY), the locations/dates are prompted. Deletion of data in these two fields is automatic if NO is subsequently entered at the initial prompt.

- REC'D VA CARE PREVIOUSLY - YES/NO - Has applicant received care previously in a VA facility? If YES, the following is prompted.
1.  MOST RECENT LOCATION OF CARE - Name or number of VA facility at which patient received most recent episode of care (other than facility to which the veteran is applying). Enter a \<?\> for a list of selectable names/numbers.
33. MOST RECENT DATE OF CARE - Date of most recent episode of care in another VA facility
34. 2ND MOST RECENT LOCATION - Name or number of VA facility at which patient received 2nd most recent episode of care (other than facility to which the veteran is applying). If an entry is made, the following is also prompted.
35. 2ND MOST RECENT DATE OF CARE - Date of 2nd most recent episode of care in another VA facility.

DATA GROUP 3

- ETHNICITY INFORMATION - From available list, the ethnicity that best identifies the patient
- RACE INFORMATION - From available list, the race that best identifies the patient

DATA GROUP 4

DATE OF DEATH INFORMATION

The following date of death information is displayed if applicable and is for display purposes only. Data entry/edit is through the Discharge a Patient and Death Entry options.

- DATE OF DEATH - Date and time of death
- SOURCE OF NOTIFICATION - Source who made notification of date of death  
  (with the release of DG\*5.3\*901 – Date of Death Enhancements, entering the Source of Notification in VistA is restricted to Inpatient at VAMC (1), Death Certification on File (3) or NCA (7))
- SUPPORTING DOCUMENTATION TYPES – Supporting Documentation Type used to inform of the Patient’s Death (with the release of DG\*5.3\*939 4 types have been restricted from display to the user: BENEFICIARY SUPPORT TOOL, MILITARY PERSONNEL SOURCES, NCA FILE, SSA DMF).
- UPDATED DATE/TIME - Date and time date of death information last updated
- LAST EDITED BY - Name of local user who last edited date of death information

DATA GROUP 5

EMERGENCY RESPONSE INDICATOR - Select the appropriate emergency response indicator. Currently, the only available selection is P (for Pandemic). This field is optional and may be left blank.

DATA GROUP 6

INDIAN: This read-only field displays Indian Attestation data when it has been populated. It displays UNANSWERED when the Indian Attestation data is NULL.

EMERGENCY CONTACT DATA SCREEN \<3\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==================================================================

\[1\] NOK: DGPATIENT,SON \[2\] NOK-2: DGPATIENT,DAUGHTER

Relation: SON Relation: DAUGHTER

ADDRESS LINE\[1\] ADDRESS LINE\[1\]

ADDRESS LINE\[2\] ADDRESS LINE\[2\]

ADDRESS LINE\[3\] ADDRESS LINE\[3\]

CITY CITY,STATE ZIP CODE

PROVINCE POSTAL CODE UNITED STATES

FOREIGN COUNTRY

Phone: \###-###-#### Phone: \###-###-####

Work Phone: \###-###-#### Work Phone: \###-###-####

\[3\] E-Cont.: DGPATIENT,THREE \[4\] E2-Cont.: UNANSWERED

Relation: SON Relation: UNANSWERED

ADDRESS LINE\[1\]

ADDRESS LINE\[2\]

ADDRESS LINE\[3\]

CITY

PROVINCE POSTAL CODE

FOREIGN COUNTRY

Phone: \###-###-#### Phone: UNANSWERED

Work Phone: \###-###-#### Work Phone: UNANSWERED

\[5\] Designee: DGPATIENT,FOUR Relation: SON

ADDRESS LINE\[1\]

ADDRESS LINE\[2\]

ADDRESS LINE\[3\]

CITY,STATE ZIP CODE

UNITED STATES

Phone: \###-###-#### Work Phone: \###-###-####

\<RET\> to CONTINUE, 1-5 or ALL to EDIT, ^N for screen N or '^' to QUIT: 4

E2-NAME OF SECONDARY CONTACT: DGPATIENT,FIVE

E2-RELATIONSHIP TO PATIENT: STEP-DAUGHTER

E2-COUNTRY: USA// CANADA CAN Canada

E2-STREET ADDRESS \[LINE 1\]: ADDRESS LINE\[1\]

E2-STREET ADDRESS \[LINE 2\]: ADDRESS LINE\[2\]

E2-STREET ADDRESS \[LINE 3\]: ADDRESS LINE\[3\]

E2-CITY: CITY

E2-PROVINCE: PROVINCE

E2-POSTAL CODE: POSTAL CODE

E2-PHONE NUMBER: \###-###-####

E2-WORK PHONE NUMBER: \###-###-####

Each associate type displays the Country field at the bottom of the address fields. For a foreign address (i.e., Country is not United States) the address displayed will show only the City field below the street address and the Postal Code and Province fields below the City.

When editing any associate address, the user is first prompted for the Country. The entry of the Country follows the same process and validation rules that are enforced in the ADDITIONAL PATIENT DEMOGRAPHIC DATA, SCREEN \<1.1\>.

The country defaults to "USA” and is validated against the COUNTRY CODE file. This is a required field, but the user may exit the prompt by entering in the "^" character. This exits the editing process and refreshes the screen.

If the country entered is not “USA”, the entry/edit of the Address Lines and City follow the current process. The user is then prompted for the Province. The field is not required; may be deleted; is Free Text; and, if entered, must be between 1-20 characters. The user is then prompted for the Postal Code. The field is not required; may be deleted; is Free Text; and, if entered, must be between 1-10 characters.

> **NOTE:** Data entered into these fields are filed immediately into the database.

DATA GROUP 1

K-NAME OF PRIMARY NOK - Name of applicant's next-of-kin (3-35 characters). If an entry is made in this field, the following fields are also prompted. When the entry in this field is deleted, all entries in the following fields are also deleted. Deletion of data in the following fields may not be accomplished, unless the entry in this field is first deleted.

- K-RELATIONSHIP TO PATIENT - Relationship of patient's next of kin (1-30 characters)
- K-ADDRESS SAME AS PATIENT'S - YES/NO - If YES, the applicant's information is automatically inserted in the next-of-kin address fields and automatically updated when the applicant's address is updated. The next-of-kin’s work and phone prompts, K-PHONE NUMBER and K-WORK PHONE NUMBER, are displayed. If NO, the following fields are prompted.
1.  K-STREET ADDRESS \[LINE 1\] \|
36. K-STREET ADDRESS \[LINE 2\] \|
37. K-STREET ADDRESS \[LINE 3\] \| Address/telephone number of
38. K-CITY \| Applicant's primary next-of-kin
39. K-STATE or K-PROVINCE \|
40. K-ZIP CODE or K-POSTAL CODE \|
41. K-COUNTRY \|

DATA GROUP 2

No entry may be made into this data group, unless a primary next-of-kin was entered (Data Group 1).

- K2-NAME OF SECONDARY NOK - Name of applicant's secondary next-of-kin (3-35 characters). If an entry is made in this field, the following fields are also prompted and data contained in them are automatically deleted upon deletion of the entry in this field.
- K2-RELATIONSHIP TO PATIENT - Relationship of applicant's secondary next-of-kin (1-30 characters)
- K2-ADDRESS SAME AS PATIENT'S - YES/NO - If YES, the applicant's address information is automatically inserted in the following fields and updated accordingly as the applicant's address is updated. The next-of-kin’s work and phone prompts, K2-PHONE NUMBER and K2-WORK PHONE NUMBER, are displayed. If NO, the following fields are prompted.
1.  K2-STREET ADDRESS \[LINE 1\] \|
2.  K2-STREET ADDRESS \[LINE 2\] \|
3.  K3-STREET ADDRESS \[LINE 3\] \|
4.  K2-CITY \| Address/phone of applicant’s secondary
5.  K2-STATE or K2-PROVINCE \| Next-of-kin
6.  K2-ZIP CODE or K2-POSTAL CODE \|
7.  K2-COUNTRY \|

DATA GROUP 3

E-EMER. CONTACT SAME AS NOK - YES/NO - Is the person to contact in the event of emergency, the same as the patient's next-of-kin? If YES, the information on file for the applicant's primary next-of-kin is automatically inserted in the following fields and updated accordingly, as the next-of-kin information is updated. If NO, the following fields are also prompted.

E-NAME

- E-RELATIONSHIP TO PATIENT \|
- E-STREET ADDRESS \[LINE 1\] \|
- E-STREET ADDRESS \[LINE 2\] \| Name/relationship/address/phone number of
- E-STREET ADDRESS \[LINE 3\] \| primary individual to contact in event of
- E-CITY \| emergency
- E-STATE or E-PROVINCE \|
- E-ZIP CODE or E-POSTAL CODE \|
- E-COUNTRY \|
- E-PHONE NUMBER \|
- E-WORK PHONE \|

DATA GROUP 4

No entry may be made in this data group unless a primary emergency contact was specified in Data Group 3.

E2-NAME OF SECONDARY CONTACT - Name of secondary individual to contact in the event of an emergency. If an entry is made in this field, the following fields are also prompted.

- E2-RELATIONSHIP TO PATIENT \|
- E2-STREET ADDRESS \[LINE 1\] \|
- E2-STREET ADDRESS \[LINE 2\] \|
- E2-STREET ADDRESS \[LINE 3\] \| Name/relationship/address/telephone number of
- E2-CITY \| Secondary individual to contact in the event of an
- E2-STATE or E2-PROVINCE \| Emergency
- E2-ZIP CODE or E2-POSTAL CODE \|
- E2-COUNTRY \|
- E2-PHONE NUMBER \|
- E2-WORK PHONE \|

DATA GROUP 5

D-DESIGNEE SAME AS NOK - YES/NO - Is the individual designated to receive patient's funds and affects the same as the next-of-kin? If YES, the next-of-kin information is automatically inserted in the following fields and updated accordingly, as the next-of-kin information is updated. If NO, the following fields are prompted.

D-NAME OF DESIGNEE

- D-RELATIONSHIP TO PATIENT \|
- D-STREET ADDRESS \[LINE 1\] \|
- D-STREET ADDRESS \[LINE 2\] \| Name/relationship/address/telephone number of
- D-STREET ADDRESS \[LINE 3\] \| Individual designated to receive patient’s funds
- D-CITY \| And effects
- D-STATE or D-PROVINCE \|
- D-ZIP CODE or D-POSTAL CODE \|
- D-COUNTRY \|
- D-PHONE NUMBER \|
- D-WORK PHONE \|

APPLICANT/SPOUSE EMPLOYMENT DATA SCREEN \<4\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==================================================================

\[1\] Employer: \[2\] Spouse's:

Occupation:

Status:

Retired Dt.: Retired Dt.:

\<RET\> to CONTINUE, 1-2 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATA GROUP 1

This data group is not editiable in VistA.

- OCCUPATION – This field contains the applicant's occupation (1-30 characters).
- EMPLOYMENT STATUS - If this field is not populated or is populated with an entry other than NOT EMPLOYED, UNKNOWN, or RETIRED the following fields may also be populated and displayed. The data contained in these fields are automatically deleted if the entry in this field is changed to UNEMPLOYED or if there is no entry.
- EMPLOYER NAME – Name of applicant's employer (1-30 characters). If this field is populated, the following fields may also be displayed. The data contained in these fields are automatically deleted if there is no entry in the field or if the field is changed to UNEMPLOYED.
- EMPLOYER STREET \[LINE 1\] \|
- EMPLOYER STREET \[LINE 2\] \|
- EMPLOYER STREET \[LINE 3\] \|
- EMPLOYER CITY \| Name/address/phone of employer
- EMPLOYER STATE \|
- EMPLOYER ZIP+4 \|
- EMPLOYER PHONE NUMBER \|
- EMPLOYMENT RETIREMENT DATE – The optional Veteran Date of Retirement is only populated when the Employment Status value is ‘RETIRED’. This date is the date the Veteran applicant retired from their place of employment. The data contained in this field is automatically deleted if the entry in the Veteran applicant’s Employment Status field is changed from ‘RETIRED’ to any other valid response.

DATA GROUP 2

This data group is not editable in VistA and is populated only if the applicant has a marital status of MARRIED.

- SPOUSE'S OCCUPATION – The spouse's occupation (1-30 characters).
- SPOUSE'S EMPLOYMENT STATUS – If this field is not populated or is populated with an entry other than NOT EMPLOYED, UNKNOWN, or RETIRED the following fields may also be populated and displayed. The data contained in these fields are automatically deleted if there is no entry in the field or if the field is changed to UNEMPLOYED.
- SPOUSE'S EMPLOYER NAME – Name of spouse's employer (3-20 characters). If this field is populated the following fields may be populated and displayed. The data contained in these fields is automatically deleted upon deletion of the entry in this field.
- SPOUSE'S EMP STREET \[LINE 1\] \|
- SPOUSE'S EMP STREET \[LINE 2\] \|
- SPOUSE'S EMP STREET \[LINE 3\] \|
- SPOUSE'S EMP CITY \| Address/telephone number of spouse’s employer
- SPOUSE'S EMP STATE \|
- SPOUSE'S EMP ZIP+4 \|
- SPOUSE'S EMP PHONE NUMBER \|
- SPOUSE’S EMPLOYMENT RETIREMENT DATE – The optional Spouse’s Date of Retirement is only prompted when the Employment Status value is ‘RETIRED’. Enter the date the veteran’s spouse retired from his/her place of employment. The data contained in this field is automatically deleted if the entry in the Spouse’s Employment Status field is changed from ‘RETIRED’ to any other valid response.

INSURANCE DATA SCREEN \<5\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

============================================================================

\[1\] Covered by Health Insurance:

Insurance Co. Subscriber ID Group Holder Effective Expires

========================================================================

\[2\] Eligible for MEDICAID:

\[3\] Medicaid Number:

\<RET\> to CONTINUE, 1-3 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATA GROUP 1

Entry of insurance policy information for the patient uses the Integrated Billing package software.

- COVERED BY HEALTH INSURANCE - YES/NO/UNKNOWN – If YES is answered, the following displays.

> COVERED BY HEALTH INSURANCE changed to “NO”.

> This option adds or edits insurance information in the Insurance Buffer File. This is a temporary file that will hold all new insurance information until authorized insurance personnel can coordinate this new information with the patient’s existing insurance. You may add a new Buffer entry or edit a Buffer entry that you previously created for this patient if that entry has not yet been processed by insurance personnel.

> Please enter all available insurance information.

- Select INSURANCE COMPANY - Enter the name of the applicant's health insurance company. The insurance company must be active in your site's INSURANCE COMPANY file.
1.  Add a new Insurance Buffer entry for this patient? YES//
42. PHONE NUMBER - Company phone number
43. BILLING PHONE NUMBER - Phone number of the company’s billing office
44. PRECERTIFICATION PHONE NUMBER - If this company requires pre-certification of insurance coverage to be completed prior to a patient being treated, enter the phone number of the pre-cert office.
45. STREET ADDRESS \[LINE 1\] - Address of insurance company
46. STREET ADDRESS \[LINE 2\]
47. CITY
48. STATE
49. ZIP CODE
- GROUP NAME - Name the insurance company uses to identify the group plan (2-20 characters)
- GROUP NUMBER - Number that identifies this group policy (2-17 characters)
- BANKING IDENTIFICATION NUMBER - Enter the plan’s banking identification number (BIN) (1-10 characters)
- PROCESSOR CONTROL NUMBER (PCN) - Enter the plan’s processor control number (PCN) (1-20 characters)
- TYPE OF PLAN - Enter the type of insurance that best describes this policy. You may enter a \<?\> to obtain a current list of choices.
- EFFECTIVE DATE - Enter effective date of insurance policy for this patient.
- EXPIRATION DATE - Enter expiration date of insurance policy (leave blank if policy does not expire on a specific date).
- PT. RELATIONSHIP TO INSURED - Relationship of the patient to person holding insurance policy. You may enter a \<?\> to obtain a current list of choices.
- SUBSCRIBER PRIMARY ID - Enter the unique identification number assigned by the company (3-20 characters). You may enter \<??\> for an explanation of what number may be required here.
- NAME OF INSURED - Enter the name of the individual for whom this policy was issued. If the “PT. Relationship to the Insured” is 'Patient', this field defaults to the patient’s name.
- INSURED’S DOB: - Enter the date of birth of the person who holds the policy. Leave blank if the veteran is the patient and holds the policy.
- INSURED’S SEX: - Enter the sex of the person who holds the policy.
- PATIENT PRIMARY ID - This is the patient's primary ID number for this insurance company. Enter this field when the patient and the subscriber are different and the patient has a unique ID number.

DATA GROUP 2

Eligible for MEDICAID - YES/NO - Is the patient eligible for Medicaid coverage?

DATA GROUP 3

MEDICAID NUMBER - Enter the patient’s assigned Medicaid number, 3-30 characters.

With the release of DG\*5.3\*797, Military Service Data Sharing (MSDS) Project, the Military Service Data Screens were changed. ESR becomes the authoritative source for Military Service Episode (MSE) data. The verified data is shared from ESR to all VistA sites of record for the veteran. The ESR-verified MSE cannot be edited by VistA except to add new episodes. A new MILITARY SERVICE EPISODE sub-file (#2.3216) was added to the PATIENT file (#2) to support an unlimited number of MSEs per veteran. MSEs already on file for a veteran when the new MSE sub-file is added, remains in the patient record in the old locations in the data dictionary for historical purposes. A new Screen 6.2 was added to display these old MSEs by selecting the View History action on Screen 6.1.

Previously, “1” was used to enter MSEs. Now the user is taken to Screen 6.1 to Add/Edit/Delete or View History. The ESR-verified MSEs sent to VistA, cannot be edited or deleted by VistA users. MSEs received from ESR are identified by \<\> on Screen 6.1 and cannot be selected to edit or delete. MSEs entered by the VistA site are identified by \[ \] on Screen 6.1 and can be edited or deleted. You are no longer required to enter MSEs in date order, and MSEs still cannot overlap. All required data entry and Registration consistency checks still pertain to VistA entered MSEs. Consistency checks are not performed on ESR-verified MSEs.

With the release of DG\*5.3\*935, the FUTURE DISCHARGE DATE field (#.08) was added to sub-file MILITARY SERVICE EPISODE (#.3216) of the PATIENT file (#2) file. If Future Discharge Date is not null, it will always display below the associated MSE on the MILITARY SERVICE DATA SCREEN \<6\>. This field is not editable and is received from the VHA Enrollment System.

With the release of DG\*5.3\*947, the REASON FOR EARLY SEPARATION field (#.09) was added to sub-file MILITARY SERVICE EPISODE (#.3216) of the PATIENT file (#2). If Reason for Early Separation is not null, it will always display below the associated MSE on the MILITARY SERVICE DATA SCREEN \<6\>. This field is not editable and is received from the VHA Enrollment System.

Verify the SHOW SERVICE SCREEN? (#6) field in the TYPE OF PATIENT (#391) file is set to "Yes" for Active Duty patients, in order for the Future Discharge Date to display when received from the VHA Enrollment System. Up to three MSEs are shown on Screen 6. If there are more, \<more episodes\> will display below the list of MSEs.

MILITARY SERVICE DATA SCREEN \<6\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==========================================================================

\[1\] Service Branch/Component Service \# Entered Separated Discharge

------------------------ --------- ------- --------- ---------

ARMY UNKNOWN 01/01/2015 UNKNOWN UNKNOWN

Future Discharge Date: 10/11/2017

MARINE CORPS/REGULAR 22222 05/05/2010 05/05/2014 HONORABLE

Early Separation Reason: DISABILITY, OTHER

ARMY/REGULAR 11111 01/01/2006 01/01/2010 HONORABLE

\<more episodes\>

\[2\] Conflict Locations: \< None Specified \>

\[3\] Environment Factors: \< None Specified \>

\[4\] POW: NO From: To: War:

\[5\] Combat: From: To: Loc:

\[6\] Mil Disab Retirement: Dischrg Due to Disab:

\[7\] Dent Inj: Teeth Extracted:

\[8\] Purple Heart:

\<9\> Medal of Honor: YES Award Date: 01/12/2018 Status Date: 01/17/2018

MOH Copayment Exemption Date: 01/12/2018

\<RET\> to CONTINUE, 1-8 or ALL to EDIT, ^N for screen N or '^' to QUIT:

MILITARY SERVICE DATA SCREEN \<6.1\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

Service Branch/Component Service \# Entered Separated Discharge

\<1\> ARMY UNKNOWN 06/01/2015 UNKNOWN UNKNOWN

Future Discharge Date: 10/25/2017

\[2\] MARINE CORPS/REGULAR 22222 05/05/2010 05/05/2015 HONORABLE

Early Separation Reason: DISABILITY, OTHER

\[3\] ARMY/REGULAR 11111 01/01/2006 01/01/2010 HONORABLE

\[4\] ARMY/REGULAR 33333 01/01/2005 12/01/2005 HONORABLE

\[5\] ARMY/REGULAR 66666 01/01/2004 12/01/2004 HONORABLE

\[6\] MARINE CORPS/RESERVE 99999 01/01/1990 01/01/1995 HONORABLE

Enter ?? for more actions

AD Add DE Delete

ED Edit VH View History

Select Action:Quit//

To add a new Military Service Episode, select AD to add

Select Action:Quit// AD Add

SERVICE BRANCH: ARMY

SERVICE COMPONENT: REG REGULAR

SERVICE NUMBER: SS REDACTED

SERVICE ENTRY DATE: 6/5/2016 (JUN 05, 2016)

When adding an MSE, if the user enters a Service Entry Date or a Service Separation Date that overlaps with an FDD record, the following error message will display, stating that an overlap has been entered:

Date overlaps with a record that has a Future Discharge Date.

SERVICE ENTRY DATE: 6/5/2008 (JUN 05,2008)

SERVICE SEPARATION DATE: 7/10/2011 (JUL 10, 2011)

SERVICE DISCHARGE TYPE: HON

1 HONORABLE

2 HONORABLE-VA

CHOOSE 1-2: 1 HONORABLE

To Edit a VistA entered Military Service Episode, select ED to edit

Select Action:Quit// ED Edit

Select Episode: 1

SERVICE BRANCH: ARMY// NAVY

\*\* WARNING - BRANCH OF SERVICE WAS CHANGED SO THE COMPONENT WAS DELETED

SERVICE COMPONENT: REG REGULAR

SERVICE NUMBER: REDACTED//

SERVICE ENTRY DATE: JUN 5,1986// 6/6/1986 (JUN 06, 1986)

SERVICE SEPARATION DATE: JUL 10,1989// 7/11/1989 (JUL 11, 1989)

SERVICE DISCHARGE TYPE: HONORABLE//

If a user selects an ESR-verified military service episode to edit, the following message is displayed:

“Select an episode to edit.

Only numbers in square brackets \[ \] are selectable.”

Please contact the HECAlert mail group or the HEC if you need to update

this information.

To Delete a VistA entered Military Service Episode, select DE to delete

Select Action:Quit// DE Delete

Select Episode: 1

Are you sure you want to delete this military service episode? NO// YES

If a user selects an ESR-verified military service episode to delete, the following message is displayed:

Select an episode to delete.

Only numbers in square brackets \[ \] are selectable.

Please contact the HECAlert mail group or the HEC if you need to update

this information.

Selecting VH View History, will take the user to Screen 6.2

VISTA MILITARY SERVICE DATA SCREEN \<6.2\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

Service Branch/Component Service \# Entered Separated Discharge

Select Action:Quit//

When entering ?, ??, ??? or an invalid value at the prompt, help for Screen 6 is displayed.

MILITARY SERVICE DATA SCREEN \<6\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==========================================================================

\[1\] Service Branch/Component Service \# Entered Separated Discharge

------------------------ --------- ------- --------- ---------

ARMY UNKNOWN 01/01/2015 UNKNOWN UNKNOWN

Future Discharge Date: 10/11/2017

MARINE CORPS/REGULAR 22222 05/05/2010 05/05/2014 HONORABLE

Early Separation Reason: DISABILITY, OTHER

ARMY/REGULAR 11111 01/01/2006 01/01/2010 HONORABLE

\<more episodes\>

\[2\] Conflict Locations: \< None Specified \>

\[3\] Environment Factors: \< None Specified \>

\[4\] POW: NO From: To: War:

\[5\] Combat: From: To: Loc:

\[6\] Mil Disab Retirement: Dischrg Due to Disab:

\[7\] Dent Inj: Teeth Extracted:

\[8\] Purple Heart:

\<9\> Medal of Honor: YES Award Date: 01/12/2018 Status Date: 01/17/2018

MOH Copayment Exemption Date: 01/12/2018

\<10\> Class II Dental Indicator: YES Dental Appl Due Before Date: 07/02/2011

\<RET\> to CONTINUE, 1-8 or ALL to EDIT, ^N for screen N or '^' to QUIT: ??

                    MILITARY SERVICE DATA, SCREEN \<6\> HELP

===============================================================================

Enter '^' to stop the display and edit of data, '^N' to jump to screen \#N (see

listing below), \<RET\> to continue on to the next available screen or enter

the field group number(s) you wish to edit using commas and dashes as

delimiters.  Those groups enclosed in brackets "\[\]" are editable while those

enclosed in arrows "\<\>" are not.  Enter 'ALL' to edit all editable data

elements on the screen.

DATA GROUPS ON SCREEN 6

\[1\]  Service History                    \[2\]  Conflict Locations

\[3\]  Exposure Factors                   \<4\>  Prisoner of War

\[5\]  Combat                             \<6\>  Military Retirement/Disability

\[7\]  Dental History                     \[8\]  Purple Heart Recipient

\<9\>  Medal of Honor                     \<10\> Class II Dental Indicator

AVAILABLE SCREENS

\[^1\]  Patient Demographic Data          \[^1.1\] Additional Patient Demographic Data

\[^2\]  Patient Data                      \[^3\]  Contact Data

\[^4\]  Employment Data                   \[^5\]  Insurance Data

\[^6\]  Service Record Data               \[^7\]  Eligibility Data

\[^10\] Missing/Ineligible Data           \[^11\] Eligibility Verification Data

\[^12\] Admission Info Data               \[^13\] Application Info Data

\[^14\] Appointment Info Data             \[^15\] Sponsor Demographics Data

Press \<RETURN\> KEY TO EXIT SCREEN 6 HELP

Entry/edit of data contained in the various data groups of this screen is restricted to holders of the DG ELIGIBILITY security key, once the applicant's eligibility is verified. Prior to eligibility verification, any user may enter/edit data on this screen. After verification, the data may be viewed by all users, but only edited by holders of the DG ELIGIBILITY security key. All date fields entered must include, at a minimum, a month and a year. Any changes to existing dates to less precise dates is not allowed.

DATA GROUP 1

- SERVICE BRANCH - Name, number or abbreviation of applicant's branch of service. Enter a \<?\> for a list from which to select. If no entry is made in this field, you return to the screen. All fields (except service number) are required to complete Data Group 1.
- SERVICE COMPONENT - Name, number or abbreviation of veteran’s service component relating to the veteran’s most current branch of service. Enter a \<?\> for a list from which to select. All fields (except service number and service component) are required to complete Data Group 1. If a branch of service is changed or deleted, its associated service component is also deleted, and a warning displays on your screen.
1.  You may choose to enter a service component after selecting a branch of service if it pertains to one of the following groups:
- Army
- Navy
- Marine Corps
- Air Force
- Coast Guard
- Public Health Service
- NOAA
- Space Force
50. A Service Component is based upon one of the following factors:
- Regular
- Activated Reserve
- Activated National Guard
51. Activated Reserve is accepted only if the branch of service is one of the following:
- Army
- Navy
- Marine Corps
- Air Force
- Coast Guard
- Space Force
52. Activated National Guard is accepted only if the branch of service is one of the following:
- Army
- Air Force
- Space Force
- FILIPINO VETERAN PROOF - (This prompt displays only if branch of service entered was Filipino Commonwealth (F. Commonwealth), Filipino Guerilla Forces (F. Guerilla,) or New Filipino Scout (F. Scout New)). Documentation provided is to establish US Citizenship, lawful permanent residency, and/or VA Compensation at full-dollar rate for a Filipino Veteran. Enter a \<?\> for a list from which to select. The proof (abbreviated) displays in parenthesis to the right of the Service Branch field.
- SERVICE NUMBER - Applicant's service number (1-15 characters)  
  If same as social security number, enter SS.
- SERVICE ENTRY DATE - Entry date for episode of service.
- SERVICE SEPARATION DATE - Separation date for episode of service.
- SERVICE DISCHARGE TYPE - Discharge Type for episode of service.  
  You may enter a \<?\> to obtain a current list of choices. With the release of DG\*5.3\*797, MSDS Project, two new Discharge Types were added to the TYPE OF DISCHARGE file (#25) to be consistent with the discharge types sent to ESR from VADIR/BIRLS. With the release of DG\*5.3\*1098, the discharge type UNCHARACTERIZED was added to the TYPE OF DISCHARGE file (#25).
1.  Honorable
53. Dishonorable
54. General
55. Other Than Honorable
56. Undesirable
57. Bad Conduct
58. Dishonorable-VA – Dishonorable for VA purposes means that for the VBA, there is another reason or circumstance VBA determined the Veteran “Dishonorable” for VA purposes. The Veteran is not eligible for enrollment in the VA Health Care Program. If SC conditions exist, they may be treated for the SC conditions only.
59. Honorable-VA – Honorable for VA purposes means that for the VBA, even though their DD-214 says “General” or “Other Than Honorable”, there is another reason or circumstance the VBA determined that the Veteran is “Honorable” for VA purposes.
60. UNCHARACTERIZED
- FUTURE DISCHARGE DATE – The date that an active duty Service Member is expected to be discharged. Provision of Branch of Service, Service Entry Date, and Future Discharge Date allow Service Members to apply for Department of Veterans Affairs (VA) health benefits enrollment before they are discharged from the military. With the release of DG\*5.3\*935, the Future Discharge Date is sent from the VHA Enrollment System via an HL7 message. The Future Discharge Date cannot be entered, edited, or deleted via a VistA user template or option. This date is completely controlled by the VHA Enrollment System and is displayed for viewing purposes.
- EARLY SEPARATION REASON - Explains why a Service Member was discharged early and displays if the separation was due to disability, hardship, or early-out reason. With the release of DG\*5.3\*947, the Reason for Early Separation field is received from ES in ORF-Z11/ORU-Z11 HL7 messages in the ZMH segment. The Reason for Early Separation cannot be edited or deleted by VistA users and will not be sent back to ES in a Z07 message. This field is completely controlled by the VHA Enrollment System and is displayed for viewing purposes. Early separation reasons include the following:
1.  PARENTHOOD OR CUSTODY OF MINOR CHILDREN
2.  REDUCTION IN FORCE
3.  ATTEND CIVILIAN SCHOOL
4.  SURVIVING FAMILY MEMBER - SOLE SURVIVORSHIP
5.  HARDSHIP
6.  HOLIDAY EARLY RELEASE PROGRAM
7.  DISABILITY, SEVERANCE PAY, COMBAT RELATED (ENHANCED)
8.  DISABILITY, SEVERANCE PAY, NON COMBAT (ENHANCED)
9.  DISABILITY, SEVERANCE PAY (ENHANCED)
10. DISABILITY, AGGRAVATION (ENHANCED)
11. DISABILITY, OTHER (ENHANCED)
12. DISABILITY, SEVERANCE PAY, COMBAT RELATED
13. DISABILITY, SEVERANCE PAY
14. DISABILITY, SEVERANCE PAY, NON COMBAT
15. DISABILITY, AGGRAVATION
16. DISABILITY, OTHER
17. DISABILITY, PERMANENT (ENHANCED)
18. DISABILITY, TEMPORARY (ENHANCED)
19. DISABILITY, PERMANENT
20. DISABILITY, TEMPORARY

DATA GROUP 2

CONFLICT LOCATIONS - This data group provides a collection of data fields that allow you to enter conflict FROM and TO dates and Operation Enduring and Iraqi Freedom (OEF/OIF) source. When you select this data group from Screen 6, you can add/edit/delete the conflict information via the CONFLICT LOCATIONS sub screen. You can only edit OEF/OIF data entered by your site; you cannot edit any OEF/OIF data received from the HEC. You can add multiple OEF and OIF Conflict Locations to a patient’s record.

- The following rules apply to OEF/OIF Conflict Locations start and end dates:
1.  The Start date for each OEF Conflict Location must be greater than or equal to 09/01/2001
2.  The End date for each OEF Conflict Location must be greater than 09/11/2001
3.  The Start date for each OIF Conflict Location must be greater or equal to 03/01/2003
4.  The End for each OIF Conflict Location date must be greater than 03/19/2003
5.  The Start date for each UNKNOWN OEF/OIF Conflict Location must be greater than or equal to 09/01/2001
6.  The End date for each UNKNOWN OEF/OIF Conflict Location must be greater than 09/11/2001
- OEF/OIF Start and End dates entered at the site must fall within the patient’s dates of military service, and cannot overlap any other OEF, OIF, or UNKNOWN OEF/OIF conflict, with the following exception:  
    
  OEF or OIF Conflict Location may be entered if the Start and End dates match exactly to those of an UNKNOWN OEF/OIF Conflict Location on file. This triggers the HEC system to automatically change the UNKNOWN OEF/OIF to the corresponding OEF or OIF episode when processing the HL7 Z07 transmission from VistA to HEC. The results are sent to all sites of record and the UNKNOWN OEF/OIF episode is deleted from VistA.
- When OEF or OIF Conflict Location is added to a patient’s record, the DATE/TIME STAMP is recorded.
1.  LEBANON SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the LEBANON SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted. Entries in the following fields must be after 10/1/83.
- LEBANON FROM DATE - Beginning date of service in Lebanon
- LEBANON TO DATE - Ending date of service in Lebanon
61. GRENADA SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the GRENADA SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted. Entries in the following fields must be between 10/23/83 and 11/21/83.
- GRENADA FROM DATE - Beginning date of service in Grenada
- GRENADA TO DATE - Ending date of service in Grenada
62. PANAMA SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the PANAMA SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted. Entries in the following fields must be between 12/20/89 and 1/31/90.
- PANAMA FROM DATE - Beginning date of service in Panama
- PANAMA TO DATE - Ending date of service in Panama
63. SOMALIA SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the SOMALIA SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted. Entries in the following fields must be after 09/28/92.
- SOMALIA FROM DATE - Beginning date of service in Somalia
- SOMALIA TO DATE - Ending date of service in Somalia
64. YUGOSLAVIA SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the YUGOSLAVIA SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted. Entries in the following fields must be 6/22/92 or later.
- YUGOSLAVIA FROM DATE - Beginning date of service in Yugoslavia
- YUGOSLAVIA TO DATE - Ending date of service in Yugoslavia
65. VIETNAM SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the VIETNAM SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted. Entries in the following fields must be between 02/28/61 and 05/07/75.
- VIETNAM FROM DATE - Beginning date of service in Vietnam
- VIETNAM TO DATE - Ending date of service in Vietnam
66. PERSIAN GULF SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the PERSIAN GULF SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted. Entries in the following fields must be 8/2/90 or later.
- PERSIAN GULF FROM DATE - Beginning date of service in Persian Gulf
- PERSIAN GULF TO DATE - Ending date of service in Persian Gulf

DATA GROUP 3

ENVIRONMENT FACTORS - This data group provides a collection of data fields that allow you to enter environmental factor exposure methods. When you select this data group from Screen 6, you can add/edit/delete the following environmental factors exposure methods via the ENVIRONMENTAL FACTORS sub screen except as noted below.

- AGENT ORANGE EXPOS. INDICATED - YES/NO/UNKNOWN - If YES, only AO Exposure Location is required. All remaining fields are optional. Entries cannot be deleted as long as the AGENT ORANGE EXPOS. INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted. Agent Orange Exposure data is no longer editable in VistA. All entry/edit/delete functions must be performed in the VES. Data in VistA is view only.
1.  AGENT ORANGE REGISTRATION DATE - Date applicant was registered, as exposed to Agent Orange.
2.  AGENT ORANGE EXAM DATE - Date applicant was examined for Agent Orange exposure.
3.  AGENT ORANGE REGISTRATION \# - Agent Orange Registration \# assigned to applicant.
2.  AGENT ORANGE EXPOSURE LOCATION - Location where patient was exposed to Agent Orange: Blue Water Navy, Vietnam, Korean DMZ, Thailand(U.S. or Royal Thai MIL BASE), Laos, Cambodia(Mimot or Krek, Kampong Cham), Guam, American Samoa, or Territorial Waters, Johnston Atoll, or Other.
- RADIATION EXPOSURE INDICATED - YES/NO/UNKNOWN - Only RADIATION EXPOSURE INDICATED is required. All remaining fields are optional. Entries cannot be deleted as long as the RADIATION EXPOSURE INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted. Radiation Exposure Indicated data is no longer editable in VistA. All entry/edit/delete functions must be performed in the VES. Data in VistA is view only.
1.  RADIATION EXPOSURE METHOD – Method by which the patient was exposed to Ionizing Radiation: Hiroshima/Nagasaki, ATMOS NUCLR Testing, H/N and ATMOS Testing, UNDERGRD NUCLR Testing, EXPOS AT NUCLR Facility, Enewatak, EXPOS IN Palomares B52, Thule AFB B52, or Other.
67. RADIATION REGISTRATION DATE - Date applicant was registered, as exposed to radiation.
- SW ASIA CONDITIONS - YES/NO/UNKNOWN – If YES, veteran claims need for care of conditions related to service in SW Asia. If NO, veteran did not serve in SW Asia or does not claim need for care of conditions related to service in SW Asia. If UNKNOWN, veteran served in SW Asia but is unsure of whether conditions may be related to that service. If YES, the following two prompts display.
1.  SW ASIA COND. REGISTRATION DATE: Date on which this patient was registered as being exposed to conditions related to service in SW Asia (must be after 8/1/90). If the year is omitted, the system uses the current year.
68. SW ASIA COND. EXAM DATE: Date patient was examined for exposure to conditions related to service in SW Asia. Date must be before current date.

SW Asia Theater of Operations is defined as Iraq, Kuwait, Saudi Arabia, the neutral zone between Iraq and Saudi Arabia, Bahrain, Qatar, the United Arab Emirates, Oman, the Gulf of Aden, the Gulf of Oman, the Persian Gulf, the Arabian Sea, the Red Sea, and the airspace above these locations.

- DID YOU RECEIVE NOSE OR THROAT RADIUM TREATMENTS IN THE MILITARY? - YES/NO/UNKNOWN - Does this patient claim to have received nose and/or throat radium treatment while in the military? If YES, the following two prompts display when the veteran's service entry dates precede the dates in the question text.
- DID YOU SERVE AS AN AVIATOR IN THE MILITARY BEFORE JAN 31, 1955? - YES/NO
69. DID YOU HAVE SUBMARINE TRAINING IN THE MILITARY BEFORE JAN 1, 1965? - YES/NO
- If the user holds the DGNT VERIFY security key, the following is prompted.  
  > DO YOU WANT TO VERIFY NOW? - YES/NO - If YES, the following is prompted.
- NOSE AND THROAT RADIUM TREATMENT VERIFIED BY: - (M) Military Medical Record, (S) Qualifying Military Service, (N) Not Qualified. If "M" or "S", the following is prompted.
70. HAS VETERAN BEEN DIAGNOSED WITH CANCER OF THE HEAD AND/OR NECK? - YES/NO
- CAMP LEJEUNE? - YES/NO – Is there sufficient evidence that this patient has been housed at Camp Lejeune for a minimum of 30 days between and inclusive of August 1, 1953 and December 31, 1987 ?
- TERA: – YES/NO/UNKNOWN – Indicates whether the patient claims exposure to Toxic Exposure Risk Activity (TERA). This field is not editable in VistA.
- Persian Gulf: - YES/NO/UNKNOWN – Indicates whether the patient was deployed to the Persian Gulf. This field is not editable.

DATA GROUP 4

POW STATUS INDICATED - YES/NO/UNKNOWN - If YES, all POW fields are required to complete the POW data group. Entries cannot be deleted as long as the POW STATUS INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted. These fields cannot be edited after the patient’s eligibility is verified by the HEC. If NO is received from ESR, the POW fields are deleted and the veteran is re-evaluated for enrollment.

- POW CONFINEMENT LOCATION - War in which applicant was a POW
- POW FROM DATE - Beginning date applicant was a POW
- POW TO DATE - Ending date applicant was a POW

DATA GROUP 5

- COMBAT SERVICE INDICATED - YES/NO/UNKNOWN - If YES, all fields are required to complete the data group. Entries cannot be deleted as long as the COMBAT SERVICE INDICATED field remains YES. If this field is changed to NO, entries in the following fields are automatically deleted.
1.  COMBAT SERVICE LOCATION - War in which applicant saw combat
2.  COMBAT FROM DATE - Beginning date applicant was in combat
3.  COMBAT TO DATE - Ending date applicant was in combat
- MILITARY DISABILITY RETIREMENT: Enter ‘Y’ if this veteran applicant is receiving disability retirement pay from the Military instead of VA compensation. Enter ‘N’ if this veteran applicant is not receiving disability retirement pay from the Military instead of VA compensation. Once eligibility is verified by the HEC, this field is no longer editable by VistA users. Send updates and/or requests to the HEC. When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in this field.
- DISCHARGE DUE TO DISABILITY: Enter ‘Y’ if this veteran applicant was discharged from the military for a disability incurred or aggravated in the line of duty. Enter ‘N’ if this veteran applicant was not discharged from the military for a disability incurred or aggravated in the line of duty. Once eligibility is verified by the HEC, this field is no longer editable by VistA users. Send updates and/or requests to the HEC. When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in this field.

DATA GROUP 7

- SERVICE DENTAL INJURY - YES/NO - Did the applicant have a dental injury while in service? If YES, SERVICE TEETH EXTRACTED is defaulted to NO. The remaining fields are optional.
- SERVICE TEETH EXTRACTED - YES/NO - Did the applicant have teeth extracted while in service?  
  Select DATE OF DENTAL TREATMENT - At this field, enter the date of the applicant's dental treatment. If it is a date that was not entered in the past for the applicant, you are prompted for confirmation that you are entering a new date of dental treatment. This is a multiple field. You are returned to this prompt repeatedly until no more dates are entered. For each date entered, the following two fields are prompted before returning you to this prompt.
1.  CONDITION - Dental condition treated, place of treatment, and from whom the treatment was received
71. DATE CONDITION FIRST NOTICED - Date the dental condition was first noticed
- CURRENT PH (purple heart) INDICATOR - YES/NO/NULL - If YES, the STATUS field is automatically set to PENDING and adds this field to further display of Screen 6. If NO, the REMARKS field is automatically set to VAMC and adds this field to further display of Screen 6. If YES or NO is entered, you are prompted for DIVISION at multi-divisional sites.

This data group becomes inactive if the CURRENT PH INDICATOR field is answered and the consistency check is completed.

- STATUS - Values include Pending, In Process, Confirmed. This field is not editable by the user.
- REMARKS - Values include Unacceptable Documentation, No Documentation Received, Entered in Error, Unsupported Purple Heart, VAMC, Undeliverable Mail. This field is not editable by the user. This field contains a value only if the CURRENT PH INDICATOR field is NO.

DATA GROUP 9

CURRENT MOH Indicator – YES/NO/NULL – Indicates whether Veteran is awarded Medal of Honor. The Current MOH Indicator field is received by VistA from ESR. It is not editable by the user.

MOH AWARD DATE – Date – The MOH AWARD DATE is the date the Medal of Honor was awarded. The date is received by VistA from ESR. It is displayed on Screen 6 and is not editable by the user.

MOH STATUS DATE – Date – The MOH STATUS DATE is the date the Medal of Honor Indicator was last modified. The date is received by VistA from ESR. It is displayed on Screen 6 and is not editable by the user.

MOH COPAYMENT EXEMPTION DATE – Date – The MOH COPAYMENT EXEMPTION DATE is the date the Veteran is eligible for exemption from payments for healthcare, prescriptions, and long-term care. This date is displayed in VistA REE for manual billing reconciliation and information purposes only. The date is determined by the VistA REE system.

DATA GROUP 10

The Class II Dental Indicator is “display only”.

The Class II Dental Application Due Before Date is “display only”.

The Class II Dental Application Due Before Date is displayed, only if the Class II Dental Indicator field is YES.

Users may enter the following VA Pension data:

- Receiving a VA Pension?
- Pension Award Effective Date
- Pension Award Effective Reason

ELIGIBILITY STATUS DATA SCREEN \<7\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

===============================================================================

\[1\] Patient Type: NSC VETERAN Veteran: YES

Svc Connected: NO SC Percent: N/A

Rated Incomp.: UNANSWERED

Claim Number: UNANSWERED

Folder Loc.: UNANSWERED

\[2\] Aid & Attendance: NO Housebound: NO

VA Pension: YES

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED Amount: UNANSWERED

\[3\] Primary Elig Code: NSC, VA PENSION

Other Elig Code(s): NO ADDITIONAL ELIGIBILITIES IDENTIFIED

Period of Service: PERSIAN GULF WAR

\[4\] Service Connected Conditions as stated by applicant

---------------------------------------------------

NONE STATED

\<RET\> to CONTINUE, 1-4 or ALL to EDIT, ^N for screen N or '^' to QUIT: 2

COMPENSATION AND PENSION, SCREEN \<7\> EXPANSION

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

===============================================================================

Aid & Attendance: NO

Housebound: NO

VA Pension: YES

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED

Amount: UNANSWERED

RECEIVING A&A BENEFITS?: NO//

RECEIVING HOUSEBOUND BENEFITS?: NO//

RECEIVING A VA PENSION?: YES//

PENSION AWARD EFFECTIVE DATE: 1/1/2008 (JAN 01, 2008)

PENSION AWARD REASON: ??

Enter the Pension Award Reason only if VA Pension (#.36235) field

is equal to "Yes". VistA users are only allowed to enter a

Pension Award Reason of "Original Award" (106). This field is

optional. If Pension Award Reason is entered, an Award Date

must be entered.

Choose from:

Original Award

PENSION AWARD REASON: Original Award

RECEIVING VA DISABILITY?:

TOTAL ANNUAL VA CHECK AMOUNT:

GI INSURANCE POLICY?:

ELIGIBILITY STATUS DATA SCREEN \<7\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

===============================================================================

\[1\] Patient Type: NSC VETERAN Veteran: YES

Svc Connected: NO SC Percent: N/A

Rated Incomp.: UNANSWERED

Claim Number: UNANSWERED

Folder Loc.: BOSTON-RO

\[2\] Aid & Attendance: NO Housebound: NO

VA Pension: YES Pension A/T Date: JAN 1,2008

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED Amount: UNANSWERED

\[3\] Primary Elig Code: NSC, VA PENSION

Other Elig Code(s): NO ADDITIONAL ELIGIBILITIES IDENTIFIED

Period of Service: PERSIAN GULF WAR

\[4\] Service Connected Conditions as stated by applicant

---------------------------------------------------

NONE STATED

\<RET\> to CONTINUE, 1-4 or ALL to EDIT, ^N for screen N or '^' to QUIT:

When the HEC sends authoritative VA Pension data, it locks the record from editing and displays a message to the user.

The following rule applies to locking the VA Pension Data:

If no Pension Award Termination information is received and the Pension Award Reason is null or any value other than “Original Award”, the VA Pension Indicator is locked from editing; however, the user is able to edit the Pension Award Effective Date and Pension Award Reason”.  
The user may only select “Original Award”.

> **NOTE:** The ELIGIGILITY DATA, SCREEN \<7\> Group \[1\] will not display the labels "Claim Number:" and "Folder Loc.:" when the CLAIM NUMBER field (#.313) and the CLAIM FOLDER LOCATION field (#.314) from the PATIENT file (#2) are BOTH null.

COMPENSATION AND PENSION SCREEN \<7\> EXPANSION

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

===============================================================================

Aid & Attendance: UNANSWERED

Housebound: UNANSWERED

VA Pension: YES

Pension Award Effective Date: AUG 1,2010

Pension Award Reason: Benefit Change to Compensation

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED

Amount: UNANSWERED

RECEIVING A&A BENEFITS?:

RECEIVING HOUSEBOUND BENEFITS?:

Pension Award Date and Pension Award Reason are editable only if VA Pension Indicator is Yes and Pension Award Reason is not 'Original Award'. For any other assistance, use the HEC Alert process.

PENSION AWARD EFFECTIVE DATE: AUG 1,2010// 12/01/09 (DEC 01, 2009)

PENSION AWARD REASON: Benefit Change to Compensation // Original Award

RECEIVING VA DISABILITY?: NO//

TOTAL ANNUAL VA CHECK AMOUNT: 12000//

GI INSURANCE POLICY?:

When VA Pension termination information is received from HEC, it is displayed on the Screen 7 Expansion screen and locked from editing.

COMPENSATION AND PENSION SCREEN \<7\> EXPANSION

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

===============================================================================

Aid & Attendance: NO

Housebound: NO

VA Pension: NO

Pension Terminated Date: SEP 9,2011

Pension Terminated Reason 1: Apportionment Terminated

Pension Terminated Reason 2: CONV - Disability Not Shown by Evidence

Pension Terminated Reason 3: Failed to Furnish Requested Evidence

Pension Terminated Reason 4: Terminated-Other

VA Disability: UNANSWERED

Total Check Amount: NOT APPLICABLE

GI Insurance: UNANSWERED

Amount: UNANSWERED

RECEIVING A&A BENEFITS?: NO//

RECEIVING HOUSEBOUND BENEFITS?: NO//

Pension Award Date and Pension Award Reason are editable only if VA Pension Indicator is Yes and Pension Award Reason is not 'Original Award'. For any other assistance, use the HEC Alert process.

RECEIVING VA DISABILITY?:

GI INSURANCE POLICY?:

Entry/edit of data contained in the various data groups of this screen is restricted to holders of the DG ELIGIBILITY security key, once the applicant's eligibility is verified. (The PERIOD OF SERVICE field of Data Group 3 may not be edited by a user not holding the DG ELIGIBILITY security key, if the applicant's eligibility or service record (or both) was verified.) Prior to eligibility verification, any user may enter/edit data on this screen. After verification, the data may be viewed by all users, but only edited by holders of the DG ELIGIBILITY security key.

DATA GROUP 1

- TYPE - This field always contains a default; the entry that was made initially upon entering the patient into the data base or when the MAS V. 4.0 conversion was run, which automatically assigned a patient type to each existing patient. You may change the patient's type at this prompt. Any changes may alter the availability of certain screens and/or editing of certain data depending upon site parameters. Enter a \<?\> for a list of patient types from which to select. When the VETERAN (Y/N) field is changed from YES to NO, the data values in some fields are deleted (set to null); however, this field is not changed automatically.
- VETERAN (Y/N) - This field always contains a default; the entry that was made when the patient was initially entered into the database. You may change the patient's veteran status at this prompt. Such a change may alter the availability of certain screens and/or editing of certain data depending upon site parameters.
- SERVICE CONNECTED - YES/NO - Does the patient have any conditions for which he has received a service-connected rating from the Dept. of Veterans Affairs? If YES, the following is also prompted. The data contained in the following field is automatically deleted if this field is changed to NO. When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in this field.
- SERVICE CONNECTED PERCENTAGE - Applicant's total combined SC percentage. When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in this field.
1.  P&T - YES/NO - Is the patient rated permanently and totally disabled by the VA due to a service-connected condition?
72. P&T Effective Date – Enter the effective date the patient was awarded P&T disability status by VARO. This field is optional; however, if a date is entered, it must be a precise date (day/month/year must be included) and cannot be after the date of death. If P&T is changed from YES to NO or it is deleted, this field is deleted. This field cannot be edited after the patient’s eligibility was verified by the HEC.
73. SC AWARD DATE: - Date on which service connection is effective based on VBA decision. Can be obtained from either HINQ or the award letter. When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in this field.
- RATED INCOMPETENT?: - YES/NO - Used by AMIE. If YES, the following is also prompted. The data contained in the following fields are automatically deleted if this field is changed to NO. When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in all fields in this data group.
1.  DATE RULED INCOMPETENT (CIVIL) - Enter the date the patient was ruled incompetent to handle his funds by civil authorities. Date Ruled Incompetent (Civil) cannot be after the Date of Death.
74. DATE RULED INCOMPETENT (VA) - Enter the date the patient was ruled incompetent to handle his funds by the VA. Date Ruled Incompetent (VA) cannot be after the Date of Death.
- CLAIM NUMBER - Applicant's claim number, if any. Users cannot enter or edit the Claim Number: or Claim Folder Loc. in data group \[1\]. Users will not be prompted for Claim Number: or Claim Folder Loc. when entering new patients..
- CLAIM FOLDER LOCATION – Location of the applicant's claim folder (institution name or station number) only if it is an active facility and it has one of the following facility types in support of ESR:
1.  RO (Regional Office)
2.  RO&IC (Regional Office and Insurance Center)
3.  RO-OC (Regional Office - Outpatient Clinic)
4.  RPC (Record Processing Center)
5.  M&ROC (Medical and Regional Office Center)
6.  M&ROC (M&RO) (Medical and Regional Office Center)

    Users cannot enter or edit the Claim Number: or Claim Folder Loc. in data group \[1\]. Users will not be prompted for Claim Number: or Claim Folder Loc. when entering new patients.

DATA GROUP 2

Depending upon site parameters set forth in the Patient Type Update option, Supervisor ADT menu, the system may require the applicant to be a veteran, in order to make entries into these fields.

- RECEIVING A&A BENEFITS - YES/NO/UNKNOWN - Is applicant in receipt of Aid and Attendance? When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in this field.
- RECEIVING HOUSEBOUND BENEFITS - YES/NO/UNKNOWN - Is applicant in receipt of Housebound benefits? When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in this field.
- RECEIVING A VA PENSION - YES/NO/UNKNOWN - Is applicant in receipt of a VA pension? When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in this field.
- PENSION AWARD EFFECTIVE DATE - What is the effective date of the original award of the VA Pension Benefit or the latest date of change to the VA Pension Award?
1.  Editing of The Pension Award Effective Date is allowed only if the VA Pension Indicator is set to YES. Users are allowed to change the “Pension Award Effective Date” only if the “Pension Award Reason” is changed to “Original Award” from some other value.
75. Pension Award Effective Date must be less than or equal to the current system date.
76. The Pension Award Effective Date is not a required field (even if Pension Indicator is set to YES)
- PENSION AWARD REASON - What is the reason for the Pension Award? Select from the available choices. The Pension Award Reason is not a required field.
- PENSION TERMINATION DATE – This field is displayed when updated by the HEC and is not editable by the user.
- PENSION TERMINATION REASON 1 through 4 – These fields are displayed when updated by the HEC and are not editable by the user.
- RECEIVING VA DISABILITY - YES/NO/UNKNOWN - Is applicant in receipt of VA disability monies? When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in this field.
- TOTAL ANNUAL VA CHECK AMOUNT: - If this applicant is receiving A&A, Housebound, Pension, and/or disability payments from the VA (at least one of the questions relating to the above must be answered YES), enter the annual amount received. Once monetary benefits are verified, only users who hold the designated security key may enter/edit this field. This field may not be deleted as long as receipt of VA funds is indicated and is automatically deleted if all of the above are changed to NO. If you enter a monthly amount either precede or follow it with an asterisk (\*) and it is multiplied out by the system. When the VETERAN (Y/N)? field is changed from YES to NO, the data values are deleted (set to Null) in this field.
- GI INSURANCE POLICY - YES/NO/UNKNOWN - Does applicant have GI Insurance? If YES, the following field is prompted. The data entered is automatically deleted if NO is later entered in this field.  
  AMOUNT OF GI INSURANCE - Dollar/cents amount of GI Insurance (between 0-9999999)

DATA GROUP 3

PRIMARY ELIGIBILITY CODE - Eligibility code based on the applicant's veteran/non-veteran status. System only allows entry of eligibility codes compatible with previously entered data. A \<?\> may be entered for a list of selectable eligibility codes for the patient being entered. An entry in this field is required in order to process a patient's application for health benefits. If an entry of "Allied Veteran" or "Other Federal Agency" is made, the following is prompted. When the VETERAN (Y/N) field is changed from YES to NO, the data values in some fields are deleted (set to null); however, this field is not changed automatically. It is possible that the ELIGIBILITY TYPE field (#4) of the ELIGIBILITY CODE file (#8) still refers to a Veteran. This results in an Inconsistency \# 19 - ELIG/NONVET STAT INCONSISTENT. You must assign the correct PRIMARY ELIGIBILITY to remove the inconsistency.

If the entry is set to COLLATERAL OF VET, check if the eligibility is related to a caregiver by reviewing ADDITIONAL ELIGIBLITY VERIFICATION DATA, SCREEN \<11.5\> and/or CAREGIVER DATA, SCREEN \<11.5.1\>. If data exists for a caregiver, then DO NOT REMOVE the eligibility from the record; it must remain on the record either as a Primary Eligibility for a Patient Type of COLLATERAL or as an Other Eligibility for a Veteran.  
  
If the entry is EXPANDED MH CARE NON-ENROLLEE, then the user will be prompted to enter the EXPANDED MH CARE TYPE. (See EXPANDED MH CARE TYPE below.) The PATIENT TYPE must be NON-VETERANS (OTHER). Using the incorrect PATIENT TYPE for a patient with this primary eligibility code results in inconsistency \# 89 - PAT TYPE/OTH ELIG INCONSISTENT. The ELIGIBILITY STATUS for this primary eligibility must have a value of VERIFIED.  
  
Also, if the PATIENT ELIGIBILITIES multiple (#361) contains any of the following, that eligibility is removed:

1.  SC LESS THAN 50%
2.  SERVICE CONNECTED 50% to 100%
3.  NSC, VA PENSION
4.  AID & ATTENDANCE
5.  HOUSEBOUND
6.  ALLIED VETERAN
- AGENCY/ALLIED COUNTRY - Name of federal agency or allied country under whose auspices applicant is applying for care. Enter a \<?\> for a list of choices.
- Select ELIGIBILITY - This entry always contains a default, the entry made at the PRIMARY ELIGIBILITY field. Enter any other eligibility code(s) under which applicant is entitled to care. Entry must be compatible with previously entered data. You may enter a \<?\> for a list from which to select.
- ELIGIBILITY - This entry always contains a default, the entry at the Select ELIGIBILITY field. Edit the eligibility code here, if necessary.
- COMPACT ACT ELIGIBLE, PRESUMPTIVE PSYCHOSIS ELIGIBLE, WORLD WAR II and SPECIAL TX AUTHORITY CARE are assigned via the VHA Enrollment System as secondary eligibilities only. While VistA users are not prohibited from entering them as secondary eligibilities, the VHA Enrollment System calculates eligibility and returns the authoritative eligibilities.
- EXPANDED MH CARE TYPE - This entry is the descriptor for the primary eligibility code for Other Than Honorable (OTH) patients seeking mental health care services while awaiting VBA adjudication. “EMERGENT MH OTH” and “EXTENDED MH OTH’ are the only types available.

  Note: This prompt will only display when the user enters EXPANDED MH CARE NON-ENROLLEE as the patient’s primary eligibility.
- PERIOD OF SERVICE - Applicant's period of service eligibility code must be answered in order to respond to this prompt. Response must be compatible with eligibility code. Enter a \<?\> for a list of applicable periods of service from which to choose. Only holders of the DG ELIGIBILITY security key may edit this field. Once eligibility verification is completed, you are unable to edit this field if the applicant's service record was verified.
- PRESUMPTIVE PSYCHOSIS – The Presumptive Psychosis Category will display if one has been assigned to the patient by the HEC in the VHA Enrollment System.

DATA GROUP 3.2

If the SHAD Exposure Indicator is set to “YES”, Data Group 3.2 displays. This indicator can be modified only by the HEC. If the indicator is changed to “NO” or deleted by the HEC, Data Group 3.2 no longer displays.

DATA GROUP 3.3

The read-only text “COMPACT Act Elig: ELIGIBLE” is displayed if the patient is enrolled or the COMPACT ACT ELIGIBLE eligibility is assigned to the patient by the VHA Enrollment System. Otherwise, Data Group 3.3 is not displayed.

DATA GROUP 4

Select SERVICE CONNECTED CONDITIONS - Enter the conditions for which the applicant claims service connection.

- SERVICE CONNECTED CONDITIONS - This entry always contains a default, the entry at the Select SERVICE CONNECTED CONDITIONS field. Edit the eligibility code here, if necessary.
- PERCENTAGE: - Enter percent of service connection.

The INCOME DATA MISSING field (#.301) is no longer generated for the following conditions:

- SERVICE CONNECTED less than 50%
- SERVICE CONNECTED PERCENTAGE is 10% or greater
- NSC VA PENSION
- AID & ATTENDANCE

Dependents Module Date/Time Page: 1 of 1

FAMILY DEMOGRAPHIC DATA SCREEN \<8\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

<u>MT Patient/Dependent Relationship Active Address</u>

1 Patient Name SELF \* \*

Married Last Year:

Enter ?? for more actions

DA Spouse/Dependent Add MT Marital/Dependent Info

ES Spouse Demographic AD Add to Means/Copay Test

DD Dependent Demographic RE Remove from Means/Copay Test

DP Delete Dependent ED Expand Dependent

Select Action: Quit//

An \* (asterisk) in the "Active" column indicates the individual is an active dependent.

An \* (asterisk) in the "MT" column identifies whether the Spouse and/or Dependent Child(ren) were marked as included in the Means Test. The system also identifies whether the Spouse and/or Dependent Child(ren) have an address available by displaying an “\*” in the column titled “Address”.

SSN – After the SSN status is verified by the SSA, it can only be edited by members of the Identity Management Data Quality Team, and VERIFIED displays next to the SSN. If the SSN status is INVALID per SSA, INVALID is displayed next to the SSN.

DA SPOUSE/DEPENDENT ADD - Allows the user to add a new dependent (spouse or other).  
Do you want to add (S)pouse or (D)ependent: - If spouse selected, the following fields is prompted.

- SPOUSE'S NAME \| Demographic information for the veteran’s spouse
- SPOUSE'S SEX \|
- SPOUSE'S DATE OF BIRTH \|
- SPOUSE'S SSN \| If entering a Pseudo SSN, you must also enter a Pseudo
- \| SSN Reason
- EFFECTIVE DATE \| Date this individual became a dependent of the veteran
- \| For spouse, date of marriage
- SPOUSE’S MAIDEN NAME
- SPOUSE’S STREET ADDRESS SAME AS PATIENT’S
- SPOUSE’S STREET ADDRESS \[LINE 1\]
- SPOUSE’S STREET ADDRESS \[LINE 2\]
- SPOUSE’S STREET ADDRESS \[LINE 3\]
- SPOUSE’S CITY
- SPOUSE’S STATE
- SPOUSE’S ZIP+4
- SPOUSE’S PHONE NUMBER

Changes were made to the INCOMPLETE PHONE NUMBER field (#61). The system automatically checks for the following fields: NULL PHONE NUMBER \[RESIDENCE\] (#131), NULL PHONE \[WORK\] NUMBER (#132).

The information generated from this field displays the following options:

- Patient is EMPLOYED FULL TIME
- Patient is EMPLOYED PART TIME
- Patient is SELF EMPLOYED

If Dependent selected, the following fields are prompted.

- CHILD'S NAME \| Demographic information for each
- CHILD'S SEX \| Of the veteran's dependents
- CHILD'S DATE OF BIRTH \|
- CHILD'S SSN \| If entering a Pseudo SSN, you must also enter a Pseudo
- \| SSN Reason
- RELATIONSHIP \|
- EFFECTIVE DATE \| For a child, date of birth or adoption
- \| For a stepchild, date of marriage to the child’s parent
- CHILD’S STREET ADDRESS SAME AS PATIENT’S
- CHILD’S STREET ADDRESS SAME AS SPOUSE’S
- CHILD’S STREET ADDRESS \[LINE 1\]
- CHILD’S STREET ADDRESS \[LINE 2\]
- CHILD’S STREET ADDRESS \[LINE 3\]
- CHILD’S CITY
- CHILD’S STATE
- CHILD’S ZIP+4

ES SPOUSE DEMOGRAPHIC - Allows the user to edit demographic data related to the spouse

- NAME
- SEX
- DATE OF BIRTH
- SOCIAL SECURITY NUMBER
- EFFECTIVE DATE: (date - date)
- Date {dependent name} no longer a dependent: (date - date)
- SPOUSE’S MAIDEN NAME
- SPOUSE’S STREET ADDRESS SAME AS PATIENT’S
- SPOUSE’S STREET ADDRESS \[LINE 1\]
- SPOUSE’S STREET ADDRESS \[LINE 2\]
- SPOUSE’S STREET ADDRESS \[LINE 3\]
- SPOUSE’S CITY
- SPOUSE’S STATE
- SPOUSE’S ZIP+4
- SPOUSE’S PHONE NUMBER

DD DEPENDENT DEMOGRAPHIC - Allows the user to edit demographic data related to dependents. There must be an existing dependent on file (other than the spouse) to select this protocol. The selected dependent has to be active.

- NAME
- SEX
- DATE OF BIRTH
- SOCIAL SECURITY NUMBER
- RELATIONSHIP
- EFFECTIVE DATE: (date - date)
- DEPENDENT’S STREET ADDRESS SAME AS PATIENT’S
- DEPENDENT’S STREET ADDRESS SAME AS SPOUSE’S
- DEPENDENT’S STREET ADDRESS \[LINE 1\]
- DEPENDENT’S STREET ADDRESS \[LINE 2\]
- DEPENDENT’S STREET ADDRESS \[LINE 3\]
- DEPENDENT’S CITY
- DEPENDENT’S STATE
- DEPENDENT’S ZIP+4

DP DELETE DEPENDENT - Allows the user to delete a dependent (mainly duplicate dependents). You must hold the DG DEPDELETE security key to use this protocol. In order to delete a dependent, they must be removed from every Means Test (using the RE protocol). There are no prompts associated with this protocol.

MT MARITAL/DEPENDENT INFO - Allows the user to enter/edit last year's marital status  
MARRIED LAST CALENDAR YEAR (Y/N)

AD ADD TO MEANS/COPAY TEST

RE REMOVE FROM MEANS/COPAY TEST  
These protocols are not selectable from the registration screens.

ED EXPAND DEPENDENT - This protocol was moved to another screen (Expand Dependent). It is used to edit the effective date (date the person became a dependent of the veteran).

- Select EFFECTIVE DATE - Select the effective date you wish to edit
- EFFECTIVE DATE: {date}// - Enter correct date
- ACTIVE - If this change in status makes the dependent effective, enter 1 or YES for active. If the change makes the individual no longer dependent, enter 0 or NO.
- Options
1.  SPOUSE’S MAIDEN NAME
77. SPOUSE’S STREET ADDRESS SAME AS PATIENT’S
78. SPOUSE’S STREET ADDRESS \[LINE 1\]
79. SPOUSE’S STREET ADDRESS \[LINE 2\]
80. SPOUSE’S STREET ADDRESS \[LINE 3\]
81. SPOUSE’S CITY
82. SPOUSE’S STATE
83. SPOUSE’S ZIP+4
84. SPOUSE’S PHONE NUMBER
85. DEPENDENT’S STREET ADDRESS SAME AS PATIENT’S
86. DEPENDENT’S STREET ADDRESS SAME AS SPOUSE’S \| <u>When Veteran has</u>

> <u>Spouse flagged as</u>

> <u>Active</u>

87. DEPENDENT’S STREET ADDRESS \[LINE 1\]
88. DEPENDENT’S STREET ADDRESS \[LINE 2\]
89. DEPENDENT’S STREET ADDRESS \[LINE 3\]
90. DEPENDENT’S CITY
91. DEPENDENT’S STATE
92. DEPENDENT’S ZIP+4

How Screen 9 displays is dependent on the Means Test version.

For patients with their last Means Test in the “FEB 2005 format”, Screen 9 displays as follows.

INCOME SCREENING DATA SCREEN \<9\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

===============================================================================

Income data for (YEAR). Means Test is complete for that calendar year!

This data must be edited through the Means test module!

Veteran Total

-----------------------------------------------

\[1\] Total Employment Income

(Wages, Bonuses, Tips): - -

\[2\] Net Income from Farm,

Ranch, Property, Bus.: - -

\[3\] Other Income Amounts

(Soc. Sec., Compensation,

Pension, Interest, Div.): - -

Total 1-3 --\> \$0.00

(YEAR) Estimated "Household" Taxable Income:

\<RET\> to CONTINUE, ^N for screen N or '^' to QUIT: ^

DATA GROUP 1

Total Employment Income (Wages, Bonuses, Tips) - Gross annual income during the last calendar year from employment (wages, bonuses, tips, etc.), excluding income from farm, ranch, property, or business.

DATE GROUP 2

Net Income from Farm, Ranch, Property, Bus. - Net income from farm, ranch, property, or business received during the last calendar year.

DATA GROUP 3

Other Income Amounts (Soc. Sec., Compensation, Pension, Interest, Div.) - Income from Social Security, compensation, pension, interest, dividends (excluding welfare).

For patients with their last Means Test in the “Before FEB 2005 format”, Screen 9 displays as follows:

INCOME SCREENING DATA SCREEN \<9\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

===============================================================================

> **NOTE:** Income data for (YEAR). Means Test is complete for that calendar year!This data must be edited through the Means Test module!

Veteran Total

------------------------------------------

\[1\] Social Security (Not SSI) - -

\[2\] U.S. Civil Service - -

\[3\] U.S. Railroad Retirement - -

\[4\] Military Retirement - -

\[5\] Unemployment Compensation - -

\[6\] Other Retirement - -

\[7\] Total Employment Income - -

\[8\] Interest,Dividend,Annuity - -

\[9\] Workers Comp or Black Lung - -

\[10\] All Other Income - -

Total 1-10 --\> \$0.00

{YEAR} Estimated “Household” Taxable Income: \$

\<RET\> to CONTINUE, 1-10 or ALL to EDIT, ^N for screen N, or '^' to QUIT

(To edit only veteran income, precede selection with 'V' \[ex. 'V1-3'\]):

Entries may be made in the fields contained on this screen up until monetary benefits are verified. Once monetary benefits are verified, a user must hold the DG ELIGIBILITY security key in order to enter/edit these fields. This screen may display with one column (veteran), two columns (veteran/spouse), or three columns (veteran/spouse/dependents) depending on previously entered information. The appropriate fields are prompted for each column shown.

The “{YEAR} Estimated “Household” Taxable Income: \$” field is filled in if the information was entered through the 10-10EZ or 1010EZR form. This information is used to make preliminary or prima facie financial eligibility determinations.

DATA GROUP 1

SOCIAL SECURITY (NOT SSI) - Annual amount of social security received during the previous calendar year. Do not include SSI.

DATA GROUP 2

U.S. CIVIL SERVICE - Annual amount of U.S. Civil Service received during the previous calendar year.

DATA GROUP 3

U.S. RAILROAD RETIREMENT - Annual amount of U.S. Railroad Retirement received during the previous calendar year.

DATA GROUP 4

MILITARY RETIREMENT - Annual amount of military retirement received during the previous calendar year.

DATA GROUP 5

UNEMPLOYMENT COMPENSATION - Annual amount of unemployment compensation received during the previous calendar year.

DATA GROUP 6

OTHER RETIREMENT - Annual amount of other retirement received during the previous calendar year, includes company, state, local, etc.

DATA GROUP 7

TOTAL INCOME FROM EMPLOYMENT - Total annual amount of income from employment received during the previous calendar year, includes wages, salary, earnings, and tips.

DATA GROUP 8

INTEREST, DIVIDEND, ANNUITY - Annual amount of interest, dividend, or annuity income received during the previous calendar year.

DATA GROUP 9

WORKERS COMP. OR BLACK LUNG - Annual amount of worker's compensation or Black Lung benefits received during the previous calendar year.

DATA GROUP 10

ALL OTHER INCOME - Annual amount of all other income received during the previous calendar year. Net income from operation of a farm or other business is countable. If the veteran, veteran's spouse, or children receive a salary from the business, report it in Data Group 7 - TOTAL INCOME FROM EMPLOYMENT.

> **NOTE:** Depreciation is not a deductible expense.

INELIGIBLE/MISSING DATA SCREEN \<10\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==================================================================

\<1\> Ineligible Date: JUN 23,2020

Reason: UNANSWERED

\[2\] Missing Date: TWX Source:

TWX City: TWX State:

Reason:

\<RET\> to CONTINUE, 1-2 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

DATA GROUP 1

Ineligible Date and Reason fields are not editable and are received from the Enrollment System

DATA GROUP 2

Entry/edit of the fields on this screen may be accomplished by any user up until the applicant's eligibility is verified. Following verification of the applicant's eligibility, you must hold the DG ELIGIBILITY security key in order to enter/edit these fields. Viewing of the information is possible by all users.

MISSING PERSON DATE - Date individual was declared "missing". If an entry is made in this field, the following fields are also prompted. Data contained in the following fields is automatically deleted if the entry in this field is deleted.

- MP TWX SOURCE - Source of TWX declaring individual "missing". You may enter a \<?\> to obtain a current list of choices.
- MP TWX CITY - City from which "missing" TWX came (3-30 characters).
- MP TWX STATE - State or state code from which "missing" TWX came. Must be in STATE file. Enter a \<?\> for a list.
- MISSING OR INELIGIBLE - Free text comment concerning ineligible/missing individual.

ELIGIBILITY VERIFICATION DATA SCREEN \<11\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==================================================================

\[1\] Eligibility Status: Status Date:

Status Entered By:

Interim Response:

Verif. Method:

\[2\] Money Verified:

\[3\] Service Verified:

\[4\] Rated Disabilities: SC%: EFF. DATE OF COMBINED SC&:

\[5\] VHA Profiles (VHAP): (None Specified)

\<RET\> to CONTINUE, 1-5 or ALL to EDIT, ^N for screen N, or '^' to QUIT:

The purpose of this screen is to allow verification of an applicant's eligibility, monetary benefits and service record. Accordingly, you must hold the DG ELIGIBILITY security key in order to enter/edit any of the fields contained on it. Depending upon site parameters, this screen may be available for viewing to all users.

DATA GROUP 1

- ELIG. STATUS - Status of patient’s eligibility. You may enter a \<?\> to obtain a current list of choices. You can edit this field if the Eligibility Status is PENDING VERIFICATION or PENDING REVERIFICATION, regardless of the Verification Source. You cannot edit this field when the Eligibility Status is VERIFIED and the Verification Source is HEC.
- ELIG. STATUS DATE - Effective date of eligibility status
- ELIG. INTERIM RESPONSE - If an interim response was received concerning applicant's eligibility, enter date of receipt.
- ELIG. VERIF. METHOD - Enter method in which applicant's eligibility was verified. This is a free text field (2-50 characters).

DATA GROUP 2

MONETARY BEN. VERIFY DATE - An entry in this field indicates that the applicant's monetary benefits were verified. Enter the date monetary benefits were verified.

DATA GROUP 3

SERVICE VERIFICATION DATE - An entry in this field indicates the applicant's service record was verified. Enter the date the service record was verified.

DATA GROUP 4

SERVICE CONNECTED PERCENTAGE - Enter or verify the percentage of combined service connection as a number from 0-100.

Select RATED DISABILITIES (VA) - Enter the condition(s) or corresponding VA code(s) for which the applicant was verified as being service connected. This is a multiple field that repeats until no more entries are made. For each entry made, the following fields are also prompted. If the patient is non-service connected, you may still make entries into this field to record any disabilities the patient may have that were rated by the VA.

VistA users with the appropriate security key may edit the Rated Disabilities field.

The screen display for this entry reflects the disability followed by the SC/NSC percentage, whichever is appropriate.

- DISABILITY % - Enter the rating percentage for this disability. An entry of YES is not allowed for applicants with a patient type of non-service-connected.
- SERVICE CONNECTED - Choose from: 0 NO  
  1 YES

DATA GROUP 5

VHAP – Screen 11 displays the number of VHAPs on file. Selecting “5” displays the following additional data for viewing only. No changes or additions are allowed.

A "zz" indicator is added to the display of any current VHAPs that are inactive. The Veteran's current VHAPs are displayed in Registration options that display the VHAP \<11.1\> screen, and Patient Inquiry \[DG PATIENT INQUIRY\] option.

VHAP \<11.1A\> Oct 01, 2014@15:20:25 Page: 1 of 1

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

Current VHAP

\<1\> zz VETERAN PLAN - AAAAAA

\<2\> VETERAN FULL MED BENEFITS TX AND RX COPAY EXMT

\<3\> VETERAN FULL MED BENEFITS TX GMT COPAY REQ AND RX COPAY REQ

Additional display options include View Detail, which allows the user to view the full definition of each available VHAP, and View History, which displays all VHAPs associated with the Patient record and indicates when each was last assigned (added) or unassigned (deleted). View All History displays all the VHAPs and Expand Entry provides additional details about the selected profile.

Enter ?? for more actions \>\>\>

VH View History VD View All VHAP Detail

VHAP \<11.3\> Jul 15, 2015@11:23:18 Page: 1 of 1

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

Action Date/Time Profile

ASSIGN JUL 15,2015@12:51:47 VA/DOD PLAN - TRICARE

ASSIGN JUL 15,2015@14:08:44 VETERAN BENEFICIARY PLAN - CHAMPVA

EP Expand Entry

Select Action:Quit//

VistA REE displays the VHAP \<11.3.1\> screen when the user selects Expand Entry from View History on the VHAP \<11.3\> screen.

VHAP \<11.3.1\> Sep 15, 2019@11:23:18 Page: 1 of 2

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

Action Date/Time Profile

ASSIGN SEP 15,2019@08:00 VETERAN - FULL MEDICAL BENEFITS TREATMENT GMT COPAY

REQUIRED & RX COPAY REQUIRED

Description

All enrolled Veterans have a comprehensive medical benefits package, which VA

administers through an annual patient enrollment system. Veterans who meet

Veteran status for VA healthcare benefits and must complete a Means Test to

determine their copay status for their inpatient, outpatient services and

medications.

\+ + Next Screen - Prev Screen ?? More Actions

Select Action:Next Screen//

VHAP \<11.4\> Jul 15, 2015@11:26:53 Page: 1 of 3

Patient: PATIENT, NAME (SSN) NSC VETERAN

VHAP View All Detail

\[1\] ACTIVE DUTY AND SHARING AGREEMENTS

\[2\] ALLIED BENEFICIARIES

\[3\] APPLICANT IN PROCESS

\[4\] ASSISTED REPRODUCTIVE TECHNOLOGY

\[5\] BENEFICIARY CHAMPVA

\[6\] BENEFICIARY CHILDREN OF WOMEN OF VIETNAM VETERANS

\[7\] BENEFICIARY NEWBORN

\[8\] BENEFICIARY SPINA BIFIDA

\[9\] CAREGIVER GENERAL

\[10\] CAREGIVER PRIMARY FAMILY

\[11\] CAREGIVER SECONDARY FAMILY

\[12\] COMPREHENSIVE EXTENDED CARE SERVICES COPAY EXEMPT

\[13\] EMPLOYEE ONLY

\[14\] EXTENDED CARE SERVICES HUMANITARIAN

\[15\] HIGH RISK VETERAN

\[16\] HUMANITARIAN

\[16\] VETERAN BENEFICIARY PLAN - CAREGIVER (SECONDARY FAMILY CAREGIVER)

\+ Enter ?? for more actions \>\>\>

EP Expand Entry

Select Action:Next Screen// EP Expand Entry

Select : (1-16): 10

TRICARE Plan is a regionally managed health care program for active duty and retired members of the uniformed services, their families and survivors. VA bills TRICARE for Nonservice-connected medical treatment. There are four options for health care: TRICARE Prime, TRICARE Extra, TRICARE Standard and TRICARE for Life. Each of these options has specific benefits, exclusions, copayment and deductible requirements.

ADDITIONAL ELIGIBILITY VERIFICATION DATA, SCREEN \<11.5\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==========================================================================

\[1\] Caregiver Status Data: (3 entries)

\[2\] Community Care Program (CCP) Collateral Data:

\<RET\> to CONTINUE, 1 or ALL to EDIT, ^N for screen N or '^' to QUIT:

DATA GROUP 1

Caregiver Status Data -Displays the number of sponsors associated with the caregiver. The number of sponsors displays when the data is retrieved via an RPC from MPI. If there are zero sponsors, the label displays a "0" for the number of entries. If a connection with MPI cannot be established, a warning message is displayed instead of the number of sponsors: (WARNING: MPI CONNECTION NOT AVAILABLE - Systems will be updated automatically when MPI is available. No further action needed to update). Select this group to view caregiver data.

If data exists for a caregiver, then DO NOT REMOVE the eligibility from the record; it must remain on the record either as a Primary Eligibility for a Patient Type of COLLATERAL or as an Other Eligibility for a Veteran.

Caregiver Data \<11.5.1\>

Caregiver Data \<11.5.1\> MAR 11, 2020@09:14 PAGE: 1 of 1

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==========================================================================

CAREGIVER'S SPONSOR NAME L4SSN SUBTYPE STATUS STATUS DATE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\<1\> SPONSORONE,ONE XXXX PRIMARY BENEFIT END FEB 24,2020

\<2\> SPONSORTWO,TWO XXXX PRIMARY APPROVED FEB 22,2020

\<3\> SPONSORTHREE,THREE XXXX SECONDARY APPROVED FEB 21,2020

--------------------------------------------------------------------------

Enter ?? for more actions

Select Action:Quit//

This screen shows the caregiver’s sponsor name, last four of SSN, subtype, status, and status date.

CAREGIVER'S SPONSOR NAME: The name of the Veteran that the caregiver is providing personal care services, including first name, last name, and middle. The sponsor must be a Veteran.

L4SSN: The last four digits of the sponsor's Social Security Number.

SUBTYPE: The type of caregiver that the sponsor is associated with; one of three types: PRIMARY, SECONDARY, or GENERAL. The Program of Comprehensive Assistance to Family Caregivers (PCAFC) has a Primary Family Caregiver and a Secondary Family Caregiver; the Program of General Caregivers Support Services (PGCSS) has General Family Caregivers.

STATUS: One of five types, including:

1.  In Process: The caregiver will appear in this status until they are approved or denied for the Caregiver program. They will be in this status when the health record is made. During this period, evaluations are being conducted with Caregiver Support Coordinator (CSC)/field staff. A registrant will stay in this status until they are approved or denied for the Caregiver program.
2.  Denied: The caregiver applied to participate in the Caregiver program but was denied based on the evaluations conducted by the CSCs.
3.  Approved: The caregiver has been approved after completing the training and evaluations in the Computerized Patient Record System (CPRS). They are marked as approved in Caregiver Record Management Application (CARMA).
4.  Revoked: A caregiver who has previously been approved for the Caregiver program is removed from the Caregiver program for a reason decided upon by the CSCs staff.
5.  Benefit End: A caregiver who was revoked has reached their benefit end date. CARMA sends this status to trigger the termination of their caregiver VHA Profile (VHAP).

STATUS DATE: The Date that the caregiver "Status" has been applied to the caregiver record. The entry shall be used to display the sponsors in medical record/status date order (descending order).

DATA GROUP 2

Community Care Program (CCP) Collateral Data – select this group to view, add, edit, or remove Community Care Program data.

> **NOTE:** A COLLATERAL OF VET eligibility must be assigned prior to the selection of this group and the addition of any CCPs to a record.

CCP Collateral Data \<11.5.2\>

CCP Collateral Data \<11.5.2\> Jul 02, 2020@12:18:56 Page: 1 of 1

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

CCP Name Effective Date

\[1\] Marriage/Family Counseling JUN 27,2020

\[2\] Marriage/Family Counseling JUN 15,2020

\+ Next Screen - Prev Screen ?? More Actions

AD Add ED Edit RE Remove

CCP Name: The name of the CCP that can be assigned based on authorization and eligibility requirements. Four CCPs are available for selection: ART/IVF, Newborn, Marriage/Family Counseling, and VHA Transplant Program.

Effective Date: The date that the CCP is assigned. This entry shall be used to display the CCPs in descending order. The date entered cannot be a future date. If the CCP Marriage/Family Counseling or VHA Transplant Program has been added more than one time to a record, the Effective Date must be unique; otherwise a dialog will be presented to the user: "Effective Date for this CCP entry must be unique. The Effective Date entered is the same date as a previous entry for a particular CCP."

ADMISSION INFORMATION SCREEN \<12\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==================================================================

\<1\> Admission Date: Admit Ward:

Admit Diagnosis:

Discharge Date:

Discharge Type:

\<RET\> to CONTINUE, ^N for screen N, or '^' to QUIT:

This screen displays the patient's four most recent admissions in reverse order. For each admission, the following data is shown:

- Admission Date
- Admission Diagnosis
- Discharge Date
- Discharge Type
- Admission Ward

If the applicant has no admission data – the veteran was never admitted or previous admissions occurred prior to use of the VistA software - the following message displays:

NO ADMISSION DATA ON FILE FOR THIS PATIENT!

APPLICATION INFORMATION SCREEN \<13\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==================================================================

\<1\> Registered:

Applied for:

Dispositioned:

Type of Disp.:

\<RET\> to CONTINUE, ^N for Screen N, or '^' to QUIT:

This screen displays the applicant's four most recent applications for care in reverse order. For each application, the following data is shown:

- date/time of registration; employee who registered the applicant; employee's DUZ number (unique number that identifies a user to the system)
- type of benefit applied for
- date/time of disposition; employee who dispositioned the applicant and their DUZ number
- type of disposition

If the applicant has no application data – the veteran never applied for care or previous applications occurred prior to use of the VistA software - the following message displays:

NO APPLICATION DATA ON FILE FOR THIS PATIENT!

APPOINTMENT INFORMATION SCREEN \<14\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==================================================================

\<1\> Enrollment Clinics:

\<2\> Pending Appts:

\<RET\> to CONTINUE, ^N for screen N, or '^' to QUIT:

This screen displays each clinic in which the patient is actively enrolled and the clinic name and date/time of all pending appointments.

If the applicant is not actively enrolled in any clinics or has no pending appointments, one of the following messages displays next to the appropriate data group:

NOT ACTIVELY ENROLLED IN ANY CLINICS AT THIS TIME

NO PENDING APPOINTMENTS ON FILE

SPONSOR DEMOGRAPHIC INFORMATION SCREEN \<15\>

PATIENT NAME (PREFERRED NAME) DATE OF BIRTH

EDIPI SSN TYPE

==================================================================

\[1\] Sponsor Information:

Primary Care Team: Phone \#:

\<RET\> to QUIT, 1 or ALL to EDIT, ^N for Screen N, or '^' to QUIT:

This screen displays sponsor information. It displays for every patient although the purpose of the screen is to enter sponsorship information for those patients who are treated under the coverage of someone else (the sponsor). This would usually be through the Tricare Program or CHAMPVA Program. These patients are usually dependents of active duty military personnel, survivors of military personnel, or military retirees.

If a sponsor is already in the PATIENT file (#2), you may not edit the sponsor name and date of birth. For new sponsors, you are prompted to first add the person as a sponsor and then as the sponsor of the patient. For existing sponsors, you are asked only if you want to make that person the sponsor of the patient.

The primary care team and phone# data elements are not entered through this screen. If available, this information is automatically filled in from the Primary Care Management Module of the Scheduling software. This is the name and phone number of the patient’s primary care provider.

If sponsor or team information is not found, the following messages display:

*No Sponsor Information AvailableNo team assignment information found*

DATA GROUP 1

Select SPONSOR - Enter the name of the person who has the coverage under the patient who is being treated. This is a multiple field; you are returned to this field repeatedly until no more sponsors are entered. (A patient may have more than one sponsor; e.g., both parents are military retirees.) The first two indented fields are prompted only if the sponsor is a non-patient (not in the PATIENT file (#2).

- SPONSOR PERSON DATE OF BIRTH - Enter the sponsor’s date of birth.
- SPONSOR PERSON SOCIAL SECURITY NUMBER - Enter the sponsor’s SSN.
- MILITARY STATUS - Choose A (Active Duty) or R (Retired).
- BRANCH - Enter the branch of service for the sponsor. You may enter a \<?\> for a current list of choices.
- RANK - Enter the military rank of the sponsor (3-20 characters).
- FAMILY PREFIX - The patient’s relationship to the sponsor. This is a free text field; however, it is recommended you use the DoD convention for sponsor relationship codes. You may enter \<??\> for HELP, for a list of choices.
- SPONSOR TYPE - Choose T (TRICARE) or C (CHAMPVA).
- EFFECTIVE DATE - Effective date of sponsorship
- EXPIRATION DATE - Expiration date of sponsorship

<span id="_Toc48821848" class="anchor"></span>Appendix B: Registration Supplement for Newborns

Note the following items when entering data into the Load/Edit Patient Data or Register a Patient screens for newborn infants of women veterans.

Refer to the Care for Newborn of Women Veterans, procedure guide, for detailed information regarding the entry of newborn patients.

- When screen 2 displays, the system automatically defaults the value for Marital to “NEVER MARRIED”. The default value displays only for a patient with a date of birth that is less than one year prior to the current date.
- When screen 4 displays, the system automatically defaults the value for Status to “NOT EMPLOYED”. The default value displays only for a patient with a date of birth that is less than one year prior to the current date.
- On screen 7 enter the following values:
1.  Patient Type: NEWBORN OF VETERAN
93. Primary Elig Code: COLLATERAL OF VET
94. Period of Service: OTHER NON-VETERANS
- When screen 8 displays the system automatically defaults the value for Married Last Year to “No”. The default value displays only for a patient with a date of birth that is less than one year prior to the current date.
- The inconsistency check process verifies whether a sponsor was entered for the newborn. If no sponsor was entered for the newborn, the following inconsistency displays and the user is given the opportunity to return to screen 15 to correct the data:  
  313- NEWBORN REQUIRES SPONSOR
- The inconsistency check process verifies whether the newborn’s sponsor has an appropriate eligibility status. If the newborn’s sponsor does not have an appropriate eligibility status, the following inconsistency displays:  
  314- NEWBORN NEEDS ELIGIBLE SPONSOR

[^1]: <sup>∗</sup> New Special Treatment Authority Expiration date fields for both Agent Orange and SW Asia Conditions were added to the MAS PARAMETERS file (#43). The initial value of these fields will be null or empty. A subsequent patch will be released to populate the date fields once the expiration of the Special Treatment Authority is scheduled to expire. The assigning of Priority Group 6 determination rules to these newly enrolled veterans whose AO Indicator is "Y" and Location is *Vietnam* or *Blue Water Navy* and/or their SWAC exposure indicator is "Y" will be ignored if the Special Treatment Authority Expiration Date fields are not null.

    A subsequent patch will be released to populate these date fields once the expiration of the Special Treatment Authority is scheduled to expire.

[^2]: