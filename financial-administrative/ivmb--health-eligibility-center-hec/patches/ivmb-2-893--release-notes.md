---
title: IVMB*2*893 Continuous Enrollment Enhancements Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Continuous Enrollment Enhancements
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*893
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - enrollment
  - veteran
  - enrolled
  - rules
  - record
  - status
  - date
  - continuous
  - table
  - eligibility
page_count: 0
word_count: 1076
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p893_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/ivmb_2_p893_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

Health eligibility center

Atlanta, GA

continuous enrollment enhancements

Release Notes

IVMB\*2\*893

September 2006

Health Systems Design & Development

Table of Contents

[Introduction [1](#introduction)](#introduction)

[Enhanced Continuous Enrollment Rules [3](#enhanced-continuous-enrollment-rules)](#enhanced-continuous-enrollment-rules)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Enhanced Continuous Enrollment Rules](#enhanced-continuous-enrollment-rules)
Continuous Enrollment rules are invoked when a veteran is being assigned a base Enrollment Priority Group (PG) that is numerically greater than or equal to the base priority of the Enrollment Group Threshold (EGT). Currently, the EGT is set at PG 8, so when a record is determined to be PG 8, continuous enrollment rules are invoked to determine the sub-priority group (only if EGT setting is Enrollment Decision).
The rules are very complicated, and are therefore not covered here, but the overarching premise is
- If a veteran’s enrollment is based on valid eligibility factors, *and*
  - These factors change over time as a normal course, *and*
  - The veteran now qualifies for PG 8
    - The veteran is en rolled in PG 8a or 8c
    - The veteran remains enrolled (i.e., is continuously enrolled)
- If the veteran’s enrollment is based on one or more factors that are later found to be erroneous
  - The veteran is enrolled in PG 8e or 8g
  - The veteran’s enrollment is discontinued
Some examples are provided in the following table:
<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 30%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>Original Valid Eligibility Factor(s)</th>
<th>What Changed</th>
<th>Results after invoking Continuous Enrollment Rules</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Veteran is NSC, MT Copay Required, and Combat Veteran.</p></li>
<li><p>Enrolled on January 15, 2005, in PG 6</p></li>
<li><p>Combat Veteran End Date is June 1, 2006</p></li>
</ul></td>
<td>Combat Veteran eligibility expired June 2, 2006</td>
<td><ul>
<li><p>PG changed to 8c</p></li>
<li><p>Continuously enrolled</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Veteran is 10% SC</p></li>
<li><p>Enrolled in PG 3</p></li>
</ul></td>
<td>VBA readjusts award down to 0%</td>
<td><ul>
<li><p>PG changed to 8a</p></li>
<li><p>Continuously enrolled</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>NSC Veteran applies for enrollment on March 15, 2003</p></li>
<li><p>Enrolled in PG 5 (based on Means Test [MT] Copay Exempt status)</p></li>
</ul></td>
<td><ul>
<li><p>Subsequent means tests place the veteran in a MT Copay Required status.</p></li>
<li><p>The MT that qualified the veteran for enrollment is converted to a MT Copay Required Status by IVM</p></li>
</ul></td>
<td><ul>
<li><p>PG changed to 8e</p></li>
<li><p>Enrollment is discontinued</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Veteran is enrolled as 10% SC</p></li>
<li><p>Enrolled in PG 3</p></li>
</ul></td>
<td>The HEC later confirms that the veteran has no service-connected disabilities and corrects the record.</td>
<td><ul>
<li><p>PG changed to 8g</p></li>
<li><p>Enrollment is discontinued</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>0% SC noncompensable, MT Copay Required veteran</p></li>
<li><p>Enrolled in PG 6 based on an assertion of Agent Orange Exposure while in service in Vietnam</p></li>
</ul></td>
<td><ul>
<li><p>The veteran is subsequently found not to have served in Vietnam</p></li>
<li><p>The Agent Orange Exposure indicator is changed to NO</p></li>
</ul></td>
<td>PG changed to 8e</td>
</tr>
</tbody>
</table>

# Enhanced Continuous Enrollment Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To determine a veteran’s current enrollment record for the purpose of continuous enrollment, ignore any records with an enrollment status in the following list and look to the most recent record that is not in one of these statuses:

- Pending Means Test Required
- Pending Purple Heart Unconfirmed
- Pending Eligibility Status Unverified
- Pending Other
- Pending No Eligibility Code
- Deceased
- Not Eligible; Ineligible Date
- Not Eligible; Refused to Pay Copay

Once the current enrollment record has been determined, the following rules will be executed in this order:

1.  If the enrollment record is in a REJECTED enrollment status due to a manual override \[at the HEC\] (i.e., Enrollment Status Override =YES), it will remain in a REJECTED status unless the veteran is assigned to an enrollment priority group that is being accepted for enrollment,

> OR

> Until a new EGT is set that could qualify the veteran for enrollment

> OR

> The record in a REJECTED enrollment status is manually overridden \[at the HEC\] to ENROLLED

2.  If the enrollment record is in a REJECTED enrollment status, it will stay REJECTED as long as the veteran stays in an enrollment priority group that is not being accepted for new enrollment.
3.  If the enrollment record is in a VERIFIED enrollment status due to a manual override \[at the HEC\] (i.e., Enrollment Status Override =YES), the veteran will remain ENROLLED until a new EGT is set that could disqualify the veteran from enrollment

> OR

> The record in an ENROLLED category is manually overridden \[at the HEC\] to a REJECTED enrollment status

4.  If the enrollment record is in a CANCEL/DECLINED enrollment status on or after the EGT Effective Date, it will be treated the same as a record in a REJECTED enrollment status. The veteran will not be continuously enrolled as long as s/he stays in an enrollment priority group that is not being accepted for new enrollments.
5.  If the current enrollment record does not meet any of the conditions in Rules 1-4 above, the veteran’s enrollment records will be evaluated from most current to earliest, with the following rules applied in this order:
- If the earliest Effective Date of Change is prior to the EGT Effective Date, the veteran will be continuously enrolled.
- If there is any Enrollment Application Date prior to the EGT Effective Date, the veteran will be continuously enrolled.
  6.  If the enrollment record is in a NOT ELIGIBLE/REFUSED COPAY enrollment status on or after the EGT Effective Date

> AND

> The veteran has been sent a 601B or 601C Letter in the following statuses:

> 0-Send to AAC

> 1-Sent to AAC

> 2-Mailed by HEC

> 3-Reject at HEC

> 4-Reject by AAC

> 5-Error by AAC

> 6-Return by post office

> 7-Mailed by AAC

> 8-Sent to HEC printer

> 9-Address changed and mailed by AAC

> AND

> Agree to Pay Deductible is being changed from NO to YES

> THEN

> The decision is to REJECT enrollment

7.  If the veteran has ever had a verified enrollment record with an eligibility in the following list, s/he will be continuously enrolled:
- SC 10% or greater

> AND

> SC% is changed to SC 0% non compensable (total check amount \$0 or null)

- Aid & Attendance = YES

> AND

> A&A is now not YES

- Housebound = YES

> AND

> Housebound is now not YES

- VA Pension = YES

> AND

> VA Pension is now not YES

- AO indicator = YES

> AND

> Location = DMZ was entered prior to Enrollment System Redesign (ESR) V. 3.0 implementation

- The CV End Date expires on or after the Enrollment Application Date (or, in the absence of an Application Date, the earliest Effective Date of Change)

> AND

> The CV End Date has not been removed

- The veteran is enrolled due to a Means Test that qualifies for enrollment,

> AND

> A subsequent income year Means Test was added or edited that would place the veteran in a priority group that is not being enrolled

8.  If the enrollment record history does not support any of Rules1-7 above,

> AND

> The base priority is numerically greater than the EGT threshold,

> THEN

> The decision is to REJECT enrollment