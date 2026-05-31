---
title: '''CPRS User Manual: GUI Version (Updated OR*3.0*499)'''
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: ''
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3.0
patch_id: CPRS*3.0
group_key: CPRS:CPRS:3.0
file_numbers:
- '27.11'
- '100'
- '200'
- '8991.9'
security_keys:
- CTRL
- GMV MANAGER
- ORELSE
- OREMAS
- ORES
- PROVIDER
- YSCL AUTHORIZED
menu_options: 2
description: Revision HistoryThis table lists the history for each revision of this document by row in descending order
audience: End users (clinical / administrative, per package)
keywords: []
page_count: 0
word_count: 74123
section_count: 0
table_count: 4
figure_count: 0
appendix_count: 4
has_toc: false
is_stub: false
pub_date: June 2023
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/cprsguium.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/cprsguium.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=61
audit_applied: '2026-05-31'
master_source: 'CPRS User Manual: GUI Version (Updated OR*3.0*499)'
master_pub_date: June 2023
consolidated_from: 2 versions
prior_versions:
- 'CPRS User Manual: GUI Version (Updated OR*3.0*626)'
consolidated_title: 'cprs user manual: gui version'
---

Computerized Patient Record System (CPRS)

User Guide: GUI Version

![](cprs-user-manual-gui-version-updated-or-3-0-499/001.png)

June 2023

Office of Information & Technology (OIT)

Revision History

<table>
<caption>Revision HistoryThis table lists the history for each revision of this document by row in descending order</caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 30%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version/Patch</th>
<th>Page</th>
<th>Change</th>
<th>Project Manager</th>
<th>Technical Writer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>06/2023</td>
<td>OR*3*499</td>
<td>233, 239, 250, 254, 322, 328, 334, 339, 358, 361, 562</td>
<td><p>Added OR ZIP CODE MESSAGE <strong>warning</strong> and updated DEA required dialogs.</p>
<ul>
<li><p>Ordering <a href="#_Toc112615110">Inpatient Medications <u>Simple Dose</u></a></p></li>
<li><p>Ordering <a href="#_Toc112615111">Inpatient Medications <u>Complex Dose</u></a></p></li>
<li><p><a href="#_Toc112615117">Outpatient Medications <u>Simple Dose</u></a></p></li>
<li><p><a href="#_Toc112615118">Outpatient Medications <u>Complex Dose</u></a></p></li>
<li><p><a href="#OrderingInpatientSimple"><u>Ordering Inpatient Medications (Simple Dose)</u></a></p></li>
<li><p><u>Ordering Inpatient Medications (Complex Dose)</u></p></li>
<li><p><a href="#OrderingClinicSimple"><u>Ordering Simple Clinic Medications</u></a></p></li>
<li><p><a href="#OrderingClinicComplex"><u>Ordering Complex Clinic Medication Orders</u></a></p></li>
<li><p><u>Ordering Outpatient Medications (Simple Dose)</u></p></li>
<li><p><a href="#OrderingOutpatientComplex"><u>Ordering Outpatient Medications (Complex Dose)</u></a></p></li>
<li><p><u>Appendix D – Error Messages and Troubleshooting</u></p></li>
</ul></td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>05/2023</td>
<td>OR*3.0*593</td>
<td><a href="#Smart_Note_593"><strong><u>170</u></strong></a></td>
<td><p>Added note for SMART alerts enabled/not enabled</p>
<p>Removed references and instructions for copying existing orders for medications/infusions</p></td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>09/2022</td>
<td>OR*3.0*405</td>
<td></td>
<td><p>Added a <strong><u><a href="#clozapine_origin_note">note defining where the Clozapine requirements</a></u></strong> came from.</p>
<p>Indications: Added screen captures or steps for indications in Medication Orders:</p>
<ul>
<li><p><a href="#Ind_overview"><strong><u>Indications Overview</u></strong></a></p></li>
<li><p><a href="#Ind_simp_dose_Inpt_meds_graphic"><strong><u>Medication Order inpatient simple dose screen capture</u></strong></a></p></li>
<li><p><a href="#Ind_simp_dose_Inpt_meds_step"><strong><u>Medication Order inpatient simple dose added indication step</u></strong></a></p></li>
<li><p><a href="#Ind_comples_dose_Inpt_meds_capture"><strong><u>Medication Order inpatient complex dose screen capture</u></strong></a></p></li>
<li><p><a href="#Ind_comples_dose_Inpt_meds_step"><strong><u>Medication Order inpatient complex dose added indications step</u></strong></a></p></li>
<li><p><a href="#Ind_simp_dose_outpt_meds_capture"><strong><u>Medication Order outpatient simple dose screen capture</u></strong></a></p></li>
<li><p><a href="#Ind_simp_dose_outpt_meds_step"><strong><u>Medication Order outpatient simple dose added indication step</u></strong></a></p></li>
<li><p><a href="#Ind_cmpl_dose_outpt_meds_step"><strong><u>Medication Order complex dose indication capture</u></strong></a></p></li>
<li><p><a href="#Ind_Non_VA_meds_step"><strong><u>Non-VA Meds added optional indications step</u></strong></a></p></li>
<li><p><a href="#Ind_MEDS_jnpt_simple_meds_capture"><strong><u>Ordering Medications simple dose indications capture</u></strong></a></p></li>
<li><p><a href="#Ind_MEDS_jnpt_simple_meds_step"><strong><u>Ordering Medications simple dose added indications step</u></strong></a></p></li>
<li><p><a href="#Ind_Ordering_simple_clinic_Meds_step"><strong><u>Ordering Clinic Medications simple dose added indications step</u></strong></a></p></li>
<li><p><a href="#Ind_Ordering_complex_clinic_Meds_step"><strong><u>Ordering Complex Clinic Medications added indications step</u></strong></a></p></li>
<li><p><a href="#Ind_Ord_continuous_clinic_infuse_capt"><strong><u>Ordering Continuous Clinic Infusion order capture with indications</u></strong></a></p></li>
<li><p><a href="#Ind_Ord_continuous_clinic_infuse_step"><strong><u>Ordering Continuous Clinic Infusion order step for indication</u></strong></a></p></li>
<li><p><a href="#Ind_Ord_intermitnt_clinic_infuse_capt"><strong><u>Ordering Intermittent Clinic Infusion capture with indications</u></strong></a></p></li>
<li><p><a href="#Ind_Ord_intermitnt_clinic_infuse_step"><strong><u>Ordering Intermittent Clinic Infusion added step for indications</u></strong></a></p></li>
<li><p><a href="#Ind_Ord_Outpt_simple_dose_capt"><strong><u>Ordering Outpatient Meds simple dose capture with indications</u></strong></a></p></li>
<li><p><a href="#Ind_ORD_outpt_simple_med_step"><strong><u>Ordering Outpatient Meds simple dose added a step for indications</u></strong></a></p></li>
<li><p><strong><u><a href="#Ind_Ord_Outpt_complex_dose_capt">Ordering Outpatient Meds complex dose added a capture with indications</a></u></strong></p></li>
<li><p><a href="#Ind_Ord_Outpt_complex_dose_step"><strong><u>Ordering Outpatient Meds complex dose added a step for indications</u></strong></a></p></li>
<li><p><a href="#Ind_Non_VA_meds_2nd_step"><strong><u>Indication added to the Documenting Non-VA meds</u></strong></a></p></li>
<li><p><a href="#Ind_Ord_continuous_infuse_capt"><strong><u>Continuous Infusion Order capture with indication</u></strong></a></p></li>
<li><p><a href="#Ind_Ord_continuous_infuse_step"><strong><u>Continuous Infusion Order step for an indication</u></strong></a></p></li>
<li><p><a href="#Ind_Ord_intermit_infuse_capt"><strong><u>Intermittent Infusion Order capture with indication</u></strong></a></p></li>
<li><p><strong><u>Intermittent Infusion Order capture with indication</u></strong></p></li>
</ul>
<p>NSR 20170302 –Added <a href="#change_refills"><strong><u>functionality</u></strong></a> that lets a user change various attributes when renewing an outpatient medication order</p>
<p>NSR 20090509 – Park a Prescription:</p>
<ul>
<li><p>Added a <a href="#park_description"><strong><u>Park a Prescription section</u></strong></a>.</p></li>
<li><p>Put "parked" updates in the <a href="#Parked_Meds_View"><strong><u>Sorting the Medications View</u></strong></a>, and <strong><a href="#Parked_Orders_View"><u>Viewing Orders on the Orders Tab</u></a></strong> sections.</p></li>
<li><p>Updated the screenshots in the following sections:</p>
<ul>
<li><p><a href="#Parked_Meds_Screenshot"><strong><u>Simple Dose</u></strong></a>,</p></li>
<li><p><a href="#Parked_Meds_Screenshot_complex"><strong><u>Complex Dose</u></strong></a> section for Ordering Outpatient Medications,</p></li>
<li><p><a href="#Parked_Meds_Screenshot_2"><strong><u>Simple Dose</u></strong></a> section for Ordering Outpatient Medications</p></li>
</ul></li>
<li><p>Fixed an error on a screenshot in the <strong><u><a href="#Park_inp_meds">Ordering Inpatient Medications (Simple Dose).</a><br />
</u></strong></p></li>
<li><p>Updated all three screenshots in the <a href="#antimicrobial_quick_orders_updates"><strong><u>Antimicrobial Medication Quick Orders</u></strong></a> section</p></li>
<li><p>Updated the <a href="#Refill_Orders_Dialog"><strong><u>Refill Orders dialog</u></strong></a> screenshot and instructions.</p></li>
</ul>
<p>Added the <a href="#PDMP_button_reminder_dialog_template"><strong><u>Accessing a PDMP Button on a Reminder Dialog Template</u></strong></a> section. Fixed the <strong><u><a href="#AOD_report_screenshot">AOD report screenshot</a>.</u></strong></p>
<p>NSRs 20070920, 20071211, 20100825, 20101203 - Drug-Allergy Order Check Screen Changes:</p>
<ul>
<li><p>Updated the screenshots and descriptions in the following sections:</p>
<ul>
<li><p><strong><a href="#RevSign_Order_Checks_Screenshot"><u>Review/Sign Changes Dialog</u></a></strong> section,</p></li>
<li><p><strong><u><a href="#RevSign_Order_Checks_Screenshot2">Sign Selected Orders Command</a></u></strong> section,</p></li>
<li><p><a href="#RevSign_Order_Checks_Screenshot3"><strong><u>Signing Orders before Selecting a New Patient or Exiting CPRS</u></strong></a> section,</p></li>
<li><p><strong><u><a href="#enter_allergy_updated_method_one">Entering Allergies-Method One</a></u></strong> section;</p></li>
<li><p><strong><u><a href="#Order_Checking_screenshot1">Order Check on Acceptance Dialog</a></u></strong> section,</p></li>
<li><p><strong><u><a href="#RevSign_Order_Checks_Screenshot4">Order Checks Dialog on Signature Actions</a></u></strong> section,</p></li>
<li><p>Meds Tab <u><a href="#display_change_meds">- <strong>Will the Display Change?</strong></a></u> section (updated the initial paragraphs and two screenshots),</p></li>
<li><p><u><a href="#Order_Checking_screenshot3"><strong>Order Check on Acceptance Dialog</strong></a></u> section,</p></li>
<li><p><a href="#RevSign_Order_Checks_Screenshot5"><strong><u>Order Checks Dialog on Signature Actions</u></strong></a> section (also updated the <a href="#allergy_assess"><strong><u>allergy assessment</u></strong></a> paragraph),</p></li>
<li><p>Orders tab <u><a href="#display_change_orders">- <strong>Will the Display Change?</strong></a></u> - section (updated the initial paragraphs, two screenshots and deleted one screen capture),</p></li>
<li><p><strong><u><a href="#enter_allergy_updated_orders_tab">Enter Allergy- Orders Tab</a></u></strong> section.</p></li>
</ul></li>
</ul>
<p>NSR 20130903 – Added a section on <a href="#Immunization_Skin_Test_Section"><strong><u>documenting a patient's immunizations and skin tests</u></strong></a></p>
<p>NSR 20080226 – Added a section on <a href="#Method_Four"><strong><u>doing allergy assessments after you discontinue an order</u></strong></a></p>
<p>NSR 20081008 – Added <a href="#Notifications_processed"><strong><u>general</u></strong></a> and <a href="#Notifications_processed_details"><strong><u>detailed</u></strong></a> descriptions of processed alerts on the Processed Alerts tab.<br />
<br />
Updated the following screenshots:</p>
<ul>
<li><p><a href="#patient_select_screen_1"><strong><u>Selecting a Patient</u></strong></a></p></li>
<li><p><a href="#patient_select_screen_2"><strong><u>Provider-centric view of notifications</u></strong></a></p></li>
<li><p><a href="#Notification_Defer_Option_1"><strong><u>Defer notification</u></strong></a></p></li>
<li><p><a href="#Notification_Defer_Option_2"><strong><u>Notification successfully deferred message</u></strong></a></p></li>
<li><p><a href="#Notification_Order"><strong><u>Notifications sorted by date</u></strong></a></p></li>
<li><p><a href="#Notification_forwarded"><strong><u>Notification with forwarded comment</u></strong></a></p></li>
<li><p><a href="#Notification_combat_veteran"><strong><u>Notification for combat veteran</u></strong></a></p></li>
</ul>
<p>Removed a screenshot about hovering over <a href="#Deleted_forwarded_notification"><strong><u>forwarded notifications</u></strong></a></p>
<p>NSR 20170512 – Added instructions on how to document complex non-VA medication orders from the <a href="#VA_Meds_Complex_Doses_Meds_Tab"><strong><u>Meds</u></strong></a> and <a href="#VA_Meds_Complex_Doses_Orders_Tab"><strong><u>Orders</u></strong></a> tabs.<br />
<br />
Changed the name of the "Documenting Non-VA Medication Information" section to "Documenting Non-VA Medication Information for Simple Doses" in the <a href="#VA_Meds_Simple_Doses_Meds_Tab"><strong><u>Meds</u></strong></a> and <a href="#VA_Meds_Simple_Doses_Orders_Tab"><strong><u>Orders</u></strong></a> tabs sections.</p></td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>09/2022</td>
<td>OR*3*569</td>
<td></td>
<td>Under <a href="#Atomic_Pathology_Orders_Overview"><strong>Anatomic Pathology Orders</strong></a>, removed Note regarding availability</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>01/2022</td>
<td>OR*3.0*581</td>
<td></td>
<td>Redacted hyperlinks and addresses as needed and made changes to address VDL rules.</td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>01/2022</td>
<td>OR*3.0*537</td>
<td></td>
<td><p>Remove UAP caution notes in section <a href="#remove_UAP">Using the Unified Action Profile View</a> and <a href="#remove_UAP2">Using the Discharge Meds View</a> - (CAUTION: This functionality is delivered with an On/Off switch parameter (OR UNIFIED ACTION PROFILE OFF). The default setting is Off. Do not switch this feature On until CPRS v.32 (OR*3.0*539) has been released and successfully installed.)</p>
<p>Removed verbiage from <a href="#remove_UAPnote">UAP note</a> (Note: The UAP is not currently available; however, it will be available in the near future. Sites will be notified when this feature becomes available.)</p></td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>10/2021</td>
<td>OR*3*498</td>
<td><a href="#Other_Parameters"><strong><u>144</u></strong></a><br />
<br />
<br />
<br />
<a href="#Meds_Tab_Date_Ranges"><strong><u>145</u></strong></a><br />
<br />
<br />
<a href="#Meds_Tab_Updates"><strong><u>205</u></strong></a></td>
<td>In the General Tab section, updated the <a href="#Other_Parameters"><strong><u>Other Parameters</u></strong></a> screenshot<br />
<br />
Updated the <a href="#Meds_Tab_Date_Ranges"><strong><u>Meds Tab Date Ranges</u></strong></a> section<br />
<br />
In the <a href="#Meds_Tab_Updates"><strong><u>Meds Tab section</u></strong></a> - Updated the sort method and date range information and screenshot</td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>09/2021</td>
<td>OR*3.0*570</td>
<td></td>
<td>Updated the sections about <a href="#flagging_an_order"><strong><u>Flagging</u></strong></a> and <a href="#Unflagging_an_Order"><strong><u>Unflagging orders</u></strong></a>.</td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>09/2021</td>
<td>OR*3.0*513</td>
<td></td>
<td>Under the Patient Inquiry Button section, added <a href="#Display_Caregiver"><strong><u>Display Caregiver Information</u></strong></a> and a new screen capture of the <a href="#Patient_Inquiry_Dialog_Example"><strong>Patient Inquiry Dialog</strong></a></td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>6/28/2021</td>
<td>OR*3*539</td>
<td><p><u><a href="#drug_class_cross_checking"><strong>184-185</strong></a><br />
<br />
<br />
</u><br />
<strong><a href="#Options_dialog"><u>139</u></a>, <a href="#Notifications_tab"><u>146</u></a></strong>, <a href="#Order_Checks_tab"><strong><u>148</u></strong></a>, <a href="#Notes_tab"><strong><u>152</u></strong></a>, <a href="#Reports_tab"><strong><u>154</u></strong></a>, <a href="#Graphs_surrogates_copy_paste_tabs"><strong><u>157-163</u></strong></a>, <strong><u><a href="#Copy_paste_tab">473</a><br />
</u><br />
</strong></p>
<p><a href="#Method_One_Eight"><strong><u>186</u></strong></a>, <a href="#Historical_allergy_note"><strong><u>188</u></strong></a>, <a href="#Method_one_eighteen"><strong><u>189</u></strong></a>, <a href="#Remove_observed"><strong><u>280</u></strong></a>, <a href="#Historical_allergy_updates_1"><strong><u>281</u></strong></a></p>
<p><strong><a href="#Allergy_Check_Enhancement_1"><u>189</u></a>, <a href="#Allergy_Check_Enhancement_2"><u>281-282</u></a>, <a href="#Womens_Health"><u>522</u></a></strong></p>
<p><a href="#Similar_providers_1"><strong><u>37</u></strong></a>, <a href="#Similar_providers_2"><strong><u>172</u></strong></a></p>
<p><a href="#template_required_fields"><u>484</u></a></p>
<p><a href="#Atomic_Pathology_Orders_Overview"><u>385</u></a></p>
<p><a href="#flagging_an_order"><u>438</u></a>, <a href="#Unflagging_an_Order"><u>440</u></a></p>
<p><a href="#Improving_Custom_Tree_View"><u>450</u></a></p>
<p><a href="#VBECS_Date_Time_wanted_ALL"><u>370</u></a></p>
<p><u><a href="#Nature_of_Order_Review_sign">116</a>, <a href="#Nature_of_Order_Sign_Selected">124</a>, <a href="#Nature_of_Order_Sign_before_exit">133</a></u></p>
<p><a href="#non_VA_Meds_label_change"><u>257</u></a></p>
<p><u><a href="#reports_message_more_data">544</a><br />
<br />
</u></p>
<p><u><br />
</u><a href="#UAP_note">254</a></p></td>
<td><p>Added documentation related to the following NSRs:</p>
<p>NSR 20060710 – Added the notification and screenshot about <strong><u><a href="#drug_class_cross_checking">Drug Class cross-checking</a><br />
<br />
</u></strong>NSR 20071216 – <a href="#Options_Surrogates_Section"><strong><u>Updated the Surrogate Management functionality</u></strong> –</a> Removed the old <a href="#Removed_Surrogate_Settings"><strong><u>Surrogate Settings</u></strong></a> section - Rearranged the <a href="#Notifications_tab"><strong><u>Notifications</u></strong></a> section - updated all Options screenshots<br />
<br />
NSR 20120404—updated the adverse reaction reporting file modification for <strong><a href="#historical_allergies"><u>historical allergies</u></a>.</strong> Fixed the <a href="#Method_One_Eight"><strong><u>numbering</u></strong></a> in the Entering Allergies-Method One section.</p>
<p>NSR 20070203-Added allergy check enhancement instructions to these sections: Entering Allergies-Method One <a href="#Allergy_Check_Enhancement_1"><strong><u>(#19 to #21)</u></strong></a> and Entering New Allergies <a href="#Allergy_Check_Enhancement_2"><strong><u>(#16 to #18)</u></strong></a>.<br />
Added <strong><u><a href="#Womens_Health">Women's Health: Potentially Unsafe Medications</a></u></strong> and <a href="#Active_meds_with_allergies"><strong><u>Active Meds with Allergies</u></strong></a> to the Outpatient Medications Report section.</p>
<p>Added a <a href="#Active_meds_with_allergies_note"><strong><u>note</u></strong></a> about the Active Meds with Allergies Report.</p>
<p>NSR 20110606 – Added the Confirm Provider with Similar Names instructions to these sections: <a href="#Similar_providers_1"><strong><u>Entering Encounter Provider and Location</u></strong></a> and <a href="#Similar_providers_2"><strong><u>Entering or Changing Encounter Information</u></strong></a>.</p>
<p>NSR 20100706: Added descriptions of new features to help identify Template Required Fields and navigate to them: <a href="#template_required_fields"><u>Navigating Template Required Fields</u></a>.</p>
<p>NSR 20140511: Added a section about the new Anatomic Pathology order dialog<u>: <a href="#Atomic_Pathology_Orders_Overview">Anatomic Pathology Orders</a></u>. Added a "Note" disclaimer at the beginning of the section and outlined it in red.</p>
<p>NSR 20071103 and 20110719: Added some information to <a href="#flagging_an_order"><u>Flagging an Order</u></a> and added an <u>Unflagging an Order</u> section.</p>
<p>NSR 20070817: Added a section about <a href="#Improving_Custom_Tree_View"><u>improvement for Custom Tree View</u></a></p>
<p>PSPO 1970: Updated VBECS section to indicate that the Date/Time Wanted applies to all Blood Components. Label changed to <a href="#VBECS_Date_Time_wanted_ALL"><u>For All Components--Date/Time Wanted</u></a>.</p>
<p>Added screen captures showing the Nature of Order change where the default can be removed (no preselection), Verbal, Telephone, or Policy with the <a href="#Nature_of_Order_Review_sign"><u>Review/Sign Changes process</u></a>, the <a href="#Nature_of_Order_Sign_Selected"><u>Sign/Selected Order process</u></a>, and the <a href="#Nature_of_Order_Sign_before_exit"><u>Sign before Exiting process</u></a>.</p>
<p>PSPO 934: <a href="#non_VA_Meds_label_change"><u>"(Documentation)" added to the labels for Non-VA medications to clarify that providers are only documenting what the patient is taking</u></a></p>
<p><u>PSPO 308/321: <a href="#reports_message_more_data">Added text to report display to let user know that there is additional data if the user set a maximum number of items returned.</a><br />
<br />
</u>NSR 20130714: Added a disclaimer to the beginning of the <a href="#UAP_note"><strong><u>United Action Profile</u></strong></a> section and outlined it in red.</p></td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>6/17/2021</td>
<td>OR*3*546</td>
<td>Various, follow links</td>
<td><p>Added a Note to subsection: <u>Viewing Inactive Flag History</u>, regarding OTH Button Labels (OTH-90 and OTH-EXT) displayed when a patient has an inactive flag.</p>
<p><a href="#Other_than_Honorable"><strong><u>Other Than Honorable</u></strong></a> subsection: replaced image due to verbiage updates for MST. Added image of an OTH pop up window with a local message.</p></td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>04/28/2021</td>
<td>OR*3.0*542</td>
<td>64</td>
<td><p>Added new Subsection: <a href="#HistoryofActionsTaken"><u>History of Actions Taken</u></a> for Active Nat Cat1 Flags.</p>
<p>Created a Subsection for <a href="#PRFNotes"><u>PRF Notes</u></a> – no edits were made to the text.</p></td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>03/15/2021</td>
<td>OR*3.0*437</td>
<td>Various, follow links</td>
<td><p>Added three (3) new subjections:</p>
<ol type="1">
<li><blockquote>
<p>Inactive PRF</p>
</blockquote></li>
<li><blockquote>
<p>Viewing Inactive Flags</p>
</blockquote></li>
<li><blockquote>
<p>Presumptive Psychosis</p>
</blockquote></li>
</ol>
<p><u>Inactive PRF History</u></p>
<p><u>Viewing Inactive Flag History</u></p>
<p><u>Presumptive Psychosis</u></p></td>
<td>Redacted</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>03/02/2021</td>
<td>OR*3*524</td>
<td>Global</td>
<td>Updated dates on the Title page and footers.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/02/2021</td>
<td>OR*3*524</td>
<td><a href="#Cover_Sheet_Vitals"><u>156</u></a></td>
<td>Added updated <a href="#Cover_Sheet_vitals"><u>Cover Sheet</u></a> screen capture—the Vitals Pane now displays the vital measurements, first in metric conversion, and then in standard, or English conversion.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/02/2020</td>
<td>OR*3*519</td>
<td><p>48</p>
<p>496</p></td>
<td><p>Added <u><a href="#_Prescription_Drug-Monitoring_Progra"><strong>v31MA Prescription Drug-Monitoring Programs (PDMP)</strong></a></u> section to the manual.</p>
<p>Added Prescription Drug-Monitoring Programs (<a href="#PDMP"><strong>PDMP</strong></a>) to Glossary</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/05/2020</td>
<td>OR*3*528</td>
<td><a href="#preferred_name_patient_inquiry_button"><u>32</u></a>, <a href="#preferred_name_patient_inquiry_screen"><u>35</u></a></td>
<td>Added information about a patient's preferred name on the Patient Inquiry <a href="#preferred_name_patient_inquiry_button"><strong><u>button</u></strong></a> and <u><a href="#preferred_name_patient_inquiry_screen"><strong>screen</strong></a>.</u></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/30/2020</td>
<td>OR*3*377</td>
<td>various</td>
<td><p>Merged content from OR*3*533 and OR*3*525 into manual.</p>
<p>Updated dates on the Title page and footers.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/11/2020</td>
<td>OR*3*533</td>
<td>Near Global (over 80 screen shots display provider names)</td>
<td><p>On screenshots that display a provider, listed whether or not the provider's NPI would display.</p>
<p>Added these notes:</p>
<p>"If a provider has an NPI, it will not display on the screen."</p>
<p>"If a provider has an NPI, it will display on the screen. See the "National Provider Identifier (NPI) Display in CPRS" section for an example of an NPI displaying on a screen."</p>
<p>Updated dates on the Title page and footers.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/3/2020</td>
<td><blockquote>
<p>OR*3*533</p>
</blockquote></td>
<td><a href="#Page7"><u>7</u></a></td>
<td>Added the <a href="#Page7"><u>National Provider Identifier (NPI) Display in CPRS</u></a> section.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/2020</td>
<td><blockquote>
<p>OR*3*525</p>
</blockquote></td>
<td><a href="#Remote_Data_View_Note"><u>44</u></a></td>
<td><p>Added <a href="#Remote_Data_View_Note"><strong><u>Note: The Remote Data View Button (RDV) will always be active</u></strong></a></p>
<p>Updated dates on Title page and footers</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>06/2020</td>
<td><blockquote>
<p>OR*3*377</p>
</blockquote></td>
<td><p><a href="#Diet_orders_changes_for_NPO"><u>303</u></a></p>
<p><a href="#Support_for_Womens_Health"><u>170</u></a></p>
<p><a href="#notes_copy_paste"><u>487</u></a></p>
<p><a href="#OTH"><u>46</u></a></p>
<p><a href="#Veteran_health_library"><u>143</u></a></p>
<p><a href="#notif_Patient_centric"><u>11</u></a></p>
<p><a href="#consult_template_lock_31b"><u>467</u></a></p>
<p><a href="#Consults_RAS_Comm_Error_31b"><u>506</u></a></p>
<p><u><a href="#Cover_Sheet_customize">176</a></u></p>
<p><a href="#Diet_orders_discharge_affects_of"><u>303</u></a></p>
<p>various</p></td>
<td><p>Added sections regarding NPO order cancellation and discontinuing.</p>
<p>Added an overview of support for Women's Health in CPRS</p>
<p>Added a section about the auditing of Copied and pasted text.</p>
<p>Added information about the Other than Honorable (OTH) button that shows the episode of care and the remaining days in the current episode.</p>
<p>Added information about how to the Veterans Health Library (VHL)</p>
<p>Patient-centric Notification information added.</p>
<p>Consult Template locked</p>
<p>Consult communication error</p>
<p>Cover Sheet Customization: How sites can customize the Cover Sheet.</p>
<p>Diet Orders: Discharge effects on diet orders</p>
<p>Removed reference to the EXCEPT conjunction, which is no longer valid.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/30/2020</td>
<td><blockquote>
<p>OR*3*515</p>
</blockquote></td>
<td><a href="#Custom_Order_View"><strong><u>235</u></strong></a></td>
<td>Added <strong><a href="#Custom_Order_View"><u>Note for the addition of new filters to the Custom Order View</u></a>.</strong> Also updated the screen capture.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/21/2020</td>
<td><blockquote>
<p>OR*3*497</p>
</blockquote></td>
<td><a href="#COVID_19"><strong><u>84</u></strong></a></td>
<td>Added updated criteria that triggers the different COVID-19 Banner messages.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>4/09/2020</td>
<td><blockquote>
<p>OR*3*485</p>
</blockquote></td>
<td><a href="#COVID_19"><strong><u>84</u></strong></a></td>
<td>Added a section about the COVID-19 identifier in CPRS.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/12/2019</td>
<td><blockquote>
<p>OR*3*514</p>
</blockquote></td>
<td><p><a href="#Patient_Inquiry_Example"><strong><u>34</u></strong></a></p>
<p><a href="#Patient_Inquiry_Example_continued"><strong><u>36</u></strong></a></p></td>
<td><p>Under <a href="#_Patient_Inquiry_Button"><u>Patient Inquiry Button</u></a>, updated the <a href="#Patient_Inquiry_Screen_2">Patient Inquiry screen captures</a> that now display the new items that have been added to the Patient Inquiry dialog. The new items are the ENROLLMENT PRIORITY (#.07) field, ENROLLMENT SUBGROUP (.12) field, and the ENROLLMENT STATUS (#.04) field. These new fields are from the PATIENT ENROLLMENT (#27.11) file. The Status field will display as 'Category' in order to be consistent with how the information is displayed in VistA.</p>
<p>Revised Date on Title Page and in footers</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>09/20/2019</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td>All</td>
<td><p>Formatted complete document for 508 compliance.</p>
<p>Removed extra spaces between paragraphs.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>07/12/2019</td>
<td><blockquote>
<p>OR*3*427</p>
</blockquote></td>
<td><p><a href="#ClozapineRequirements"><u>172</u></a></p>
<p><a href="#ClozapineMonitorGuidelines"><u>249</u></a></p>
<p><a href="#ClozapineRenewal"><u>250</u></a></p>
<p><a href="#YSCLAUTHORIZED"><u>291</u></a></p></td>
<td><p>Added reference to ordering clozapine</p>
<p>Updated information for clozapine monitoring treatment per new FDA guidelines.</p>
<p>Added note for Clozapine renewal.</p>
<p>Added note for YSCL AUTHORIZED key</p>
<p>Updated title page, footer, and table of contents.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>04/16/2019</td>
<td>OR*3.0*444</td>
<td><p>284 -292,</p>
<p>299</p></td>
<td><p>Added information about two new views available from the Orders tab: Unified Action Profile and Discharge Meds Review.</p>
<p>Section 508 Conformance: Added missing alt text to images and added header rows to table that repeat across pages.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/1/2019</td>
<td>OR*3.0*472</td>
<td><p>34, 35, 42</p>
<p>38, 39</p></td>
<td><p>Updated for Disruptive Behavior Reporting System (DBRS) data sets now displayed on National Category 1 Behavioral PRFs (through patch OR*3.0*472)</p>
<p>Updated for inclusion of Facility data on Progress Notes Properties box, flag actions section, and the ability to now sort flags by the column title (through patch TIU*1.0*318)</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/03/2019</td>
<td>OR*3*493</td>
<td><p>376</p>
<p>390</p></td>
<td><p>Updated the Order Details window to include Unique Consult ID (UCID).</p>
<p>The Consult Order Detail display was updated to display the Unique Consult ID.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/07/2018</td>
<td>OR*3.0*490</td>
<td>384 - 390</td>
<td>Added the COMMUNITY CARE Direct Schedule or Administrative Consultants section.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/26/2018</td>
<td>OR*3.0*435</td>
<td><p>179-182,</p>
<p>184-189,</p>
<p>258-261,</p>
<p>263-265,</p>
<p>270-273</p>
<p>276-279</p></td>
<td><p>Updated information about the "Give additional dose now" option to reflect that, when using this option, two orders are created, and the priority is automatically set for each.</p>
<p>Updated sections on inpatient medication orders and clinic medication orders with information on using the "Give additional dose now" option.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/07/2018</td>
<td>GMRA*4.0*59</td>
<td>210, 304</td>
<td>Added Notes to allergy/adverse reaction procedures to describe the Mark Patient Chart email bulletin.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/05/2018</td>
<td>OR*3.0*441</td>
<td>291-293, 395-396</td>
<td>Added information about the display of Flagged Order comments and Ward Comments on the Orders tab and the ability to track and manage antimicrobial Quick Orders.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td><span id="Revision_History" class="anchor"></span>3/16/2018</td>
<td>OR*3.0*452</td>
<td><a href="#Title_Page">Title Page</a>, <a href="#Revision_History">Revision History</a>, 246, 266, 267, 268, 270 and 367</td>
<td>An update for Cost Tier Copay was made to the User Guide. Tier information was added to the dosage. Previously, the User Guide display for Outpatients did not show the Tier information.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/15/2017</td>
<td>OR*3.0*429</td>
<td>217, 219</td>
<td><p>Changes for problems list features:</p>
<ol type="1">
<li><p><a href="#GMPL_49_explan_coding_systems">Added edits to the discussion of coding systems for problems.</a></p>
<p><a href="#GMPL_49_Adding_a_new_problem">Updated the section on Adding a new Problem</a></p></li>
</ol></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/26/2017</td>
<td>OR*3.0*434</td>
<td>91</td>
<td><a href="#JLV">Clarified some information about the renaming the JLV button.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/17/2017</td>
<td>OR*3.0*434</td>
<td>315</td>
<td><a href="#RTC_overview">Added to the note to ensure that users know that Return to Clinic features need both the CPRS and Scheduling patch to work correctly.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/1/2017</td>
<td>OR*3.0*434</td>
<td>378</td>
<td><a href="#consult_tracking_consult_toolbox">Added information about using the Consult Toolbox along with Consult tracking.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/26/2017</td>
<td>OR*3.0*434</td>
<td>72, 193</td>
<td>Added information about new information on the Patient Inquiry dialog, showing <a href="#patient_demo_new_health_ins_info_any_tab">what can be seen from any tab</a> and in <a href="#pat_demo_new_health_ins_info_cover_sheet">the section that explains about the Cover Sheet</a>.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/26/2017</td>
<td>OR*3.0*434</td>
<td>315</td>
<td><a href="#RTC_overview">Added information about Return to Clinic orders.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/17/2017</td>
<td>OR*3.0*434</td>
<td>3</td>
<td><a href="#sign_in_2FA">Added information about logging in to CPRS using your PIV card, also known as two-factor authentication (2FA).</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/29/2016</td>
<td>OR*3.0*434</td>
<td>43</td>
<td><a href="#JLV">Added information about the Joint Legacy Viewer or JLV.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/9/2017</td>
<td>OR*3.0*420</td>
<td>191, 193, 195, 196, 198, 199, 200, 254, 256, 261, 263, 290, 291, 293, 296</td>
<td>Updated medication ordering sections to indicate that lab results for the most recent lab test associated with a selected medication (Orderable Item) can be displayed in the Information field in the Inpatient Medications and Outpatient Medications dialogs.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/24/2016</td>
<td>OR*3.0*269</td>
<td>143, 168, 223</td>
<td>Added information about the display of the <a href="#allergies_severity_field">severity field when entering allergies</a> and the <a href="#allergies_remote_display">remote allergy display</a> by entering allergies and the one <a href="#RDI_REMOTE_order_check_orders_part2">through entering orders</a>.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/2/2014</td>
<td>OR*3.0*350</td>
<td>76</td>
<td><a href="#CIDC_SC_and_camp_lejeune">Added information about the new Camp Lejeune treatment factor that will be available when patch OR*3.0*407 is released.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/30/2014</td>
<td>OR*3.0*350</td>
<td>15</td>
<td><a href="#Alert_nonRenew_RX_request">Added a note to explain that if set up, providers may receive a request for a NonRenewable RX that they can act on to extend the therapy using Copy to New Order because they cannot use Renew.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/17/2014</td>
<td>OR*3.0*350</td>
<td>28</td>
<td><a href="#primary_care_button_PCMM">Added to the section about primary care information to include the additional information that the updates to PCMM will bring to the detailed display.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/10/2014</td>
<td>OR*3.0*350</td>
<td>232</td>
<td><a href="#diet_orders_on_new_orders">Added to the diet orders section to include that when diet orders are entered it will show the current diet if one exists and any delayed diet orders that have been entered.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/13/2014</td>
<td>OR*3.0*350</td>
<td>311</td>
<td><a href="#order_supplies">Added a section describing the new Supply order dialog</a>.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/14/2014</td>
<td>OR*3.0*350</td>
<td>380, 382, 385, 386</td>
<td>Changed the name of the Earliest Appropriate Date field to the Clinically Indicated Date field for <a href="#CID_Consult_consults_tab">Consults ordered from the Consults tab</a>, <a href="#CID_Consult_orders_tab">Consults ordered from the Orders tab</a>, <a href="#CID_Proc_consults_tab">Procedures ordered from the Consults tab</a>, and <a href="#CID_Proc_orders_tab">Procedures ordered from the Orders tab</a>.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/13/2014</td>
<td>OR*3.0*350</td>
<td>278</td>
<td>Added a section for <a href="#clinic_Infusion_overview">Clinic Infusions</a> on the Orders tab.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/13/2014</td>
<td>OR*3.0*350</td>
<td>267</td>
<td><a href="#Clinic_Med_Orders">Added a section for Clinic Medications on the Orders tab.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/14/2014</td>
<td>OR*3.0*350</td>
<td>399</td>
<td><a href="#Lab_display_overvw_changes">Added information about the new changes and reports to labs.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/4/2013</td>
<td>OR*3.0*312</td>
<td>419</td>
<td><a href="#avail_rprts_on_reports_tab_all_meds">Added the All Medications report to the list of Available reports.</a> Also, under Dept. of Defense reports, designated which reports have DOD Remote data only and which have both VA and DOD remote data.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>2/12/2013</td>
<td>OR*3.0*306</td>
<td>438</td>
<td><a href="#DEA_troubleshooting">Added Appendix B that deals with DEA error messages and troubleshooting.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/8/2012</td>
<td>OR*3.0*306</td>
<td>53</td>
<td><a href="#graphing_labs_most_recent">Added information about graphing the most recent items. Selecting a lab test shows all results for the test.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/8/2012</td>
<td>OR*3.0*306</td>
<td>52, 61</td>
<td><a href="#graphing_merged_labs">graphing_merged_labs</a>Adding information about merging lab tests for graphs under <a href="#graphing_labs_most_recent">Most Recent</a> or under the <a href="#graphing_merge_labs_settings">setting display options</a>.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/8/2012</td>
<td>OR*3.0*306</td>
<td>403</td>
<td><a href="#most_recent_lab_graph">Added a remark about the most recent bring up all tests for a specific test.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/3/2012</td>
<td>OR*3.0*306</td>
<td>64</td>
<td><a href="#Digital_Signatures">Added new information about digital signatures.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>4/17/2012</td>
<td>OR*3.0*306</td>
<td>30</td>
<td><a href="#MHTC_primary_care_button_dialog">Added a new screen capture for the Primary Care button with the team, primary care provider, associate provider, attending physician, inpatient provider, and mental health treatment coordinator displayed on the button.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/26/11</td>
<td>OR*3.0*306</td>
<td>320</td>
<td><a href="#procedure_snomed_orders_tab">Added information about the Provisional Diagnosis for Procedures using SNOMED CT codes if the dialog is set to use the lexicon to search for diagnoses from the Orders tab.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/26/11</td>
<td>OR*3.0*306</td>
<td>387</td>
<td><a href="#procedure_snomed">Added information about the Provisional Diagnosis for Procedures using SNOMED CT codes if the dialog is set to use the lexicon to search for diagnoses from the Consults tab.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/26/11</td>
<td>OR*3.0*306</td>
<td>320</td>
<td><a href="#consults_snomed_orders_tab">Added information about the Provisional Diagnosis for Consults using SNOMED CT codes if the dialog is set to use the lexicon to search for diagnoses from the Orders tab.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/26/11</td>
<td>OR*3.0*306</td>
<td>384</td>
<td><a href="#consults_snomed">Added information about the Provisional Diagnosis for Consults using SNOMED CT codes if the dialog is set to use the lexicon to search for diagnoses from the Consults tab.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/26/11</td>
<td>OR*3.0*306</td>
<td>150, 349</td>
<td><a href="#problems_snomed_updates">Added information about the Problems tab now using SNOMED Concept Terms (SNOMED CT).</a> <a href="#encounter_SNOMED">The Encounter form Other Diagnosis button also uses SNOMED concepts from the Problem List subset.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>8/3/11</td>
<td>OR*3.0*340</td>
<td>24, 30, 126, 127, 411</td>
<td>Added several items to show where the Mental Health Treatment Coordinator will display in CPRS from the 1) <a href="#MHTC_pat_inquiry_button">Patient Inquiry button</a>, 2) <a href="#MHTC_primary_care_button_dialog">the dialog displayed when the Primary Care button is selected</a>, 3) <a href="#MHTC_pat_inquiry_button_aditnal_pat_info">Getting Additional Patient information</a>, 4) <a href="#MHTC_pat_inquiry_display_from_button">the additional patient screen capture</a>, and 5) <a href="#MHTC_pat_inquiry_display_from_report">the same screen capture from the Reports tab.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/20/12</td>
<td>OR*3.0*348</td>
<td>35</td>
<td><a href="#Patient_Record_Flag_suicide_update">Added material about the new Category I High Risk of Suicide patient record flag.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/18/11</td>
<td>OR*3.0*280</td>
<td>436</td>
<td><a href="#JAWS_run_JAWS_before_CPRS">Added a small section to remind the user that JAWS should be started first and then CPRS launched and that the user must have administrator rights on the workstation JAWS will run on.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/18/11</td>
<td>OR*3.0*280</td>
<td>430</td>
<td><a href="#JAWS_ctrl_tab_examples">Added examples of when to use Ctrl + Tab to exit a field.</a></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/3/10</td>
<td>OR*3.0*280</td>
<td>125</td>
<td><a href="#tools_options_graphs_tab">Added a small section showing the Tools | Options</a> <a href="#_Toc17877476">dialog Graphs tab.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">11/9/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280 (No change was made in this version, only a text change in the manual.)</a></td>
<td><a href="#_Toc17877476">387</a></td>
<td><a href="#_Toc17877476"><span>Added a small section about forwarding a consult.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">9/14/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">236, 244</a></td>
<td><a href="#_Toc17877476">Added a small message about the tubefeeding dialog and when the amount will calculate and added a dialog for <span>inpatients</span> and <span>outpatients</span>.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">9/9/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">195, 202, 261, 292</a></td>
<td><a href="#_Toc17877476">Added a small item about how the quantity field is reset based on changing some criteria for <span>complex inpatient medication</span> and <span>complex outpatient medication</span> orders from the Meds tab. On the Orders tab, the <span>inpatient medication complex order</span> and the <span>outpatient medication complex order</span> was also updated.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">8/24/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">131 - 136</a></td>
<td><a href="#_Toc17877476">Added to the note about "Give additional dose now" and a new screen capture showing the new, clearer text for <span>medications inpatient ordering simple dose,</span> <span>medications complex doses</span>, <span>ordering simple dose</span>, and <span>ordering complex doses</span>.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">8/11/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">113</a></td>
<td><a href="#_Toc17877476"><span>Added a warning about removing pending notifications.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">8/11/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">104</a></td>
<td><a href="#_Toc17877476"><span>Added a section about the expanded Tools menu items and the addition of submenus.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">8/5/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">20</a></td>
<td><a href="#_Toc17877476"><span>Added a section about the CPRS time out.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">8/4/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">343</a></td>
<td><a href="#_Toc17877476"><span>Added a section about changing a note title and the dialog for retaining text when the user changes a note title.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">8/2/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">330</a></td>
<td><a href="#_Toc17877476"><span>Updated the screen captures of the Notes tab.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">7/20/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">433</a></td>
<td><a href="#_Toc17877476"><span>Added the keyboard combination for Release Hold on the Meds tab.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">7/20/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">208</a></td>
<td><a href="#_Toc17877476"><span>Added a small section about releasing a hold from the Meds tab.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">7/13/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">329</a></td>
<td><a href="#_Toc17877476"><span>Added a note detailing that a key or a parameter setting determines if a user can manually release orders.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">7/12/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">40</a></td>
<td><a href="#_Toc17877476"><span>The Patient Record Flag dialog has been updated, including the number of items after each Category label.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">7/12/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">102</a></td>
<td><a href="#_Toc17877476"><span>CPRS remembers the last printer used. You can configure a printer and use it for the entire session or change printers as needed.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">7/2/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">28</a></td>
<td><a href="#_Toc17877476"><span>The Primary Care button now displays the associate provider also.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">7/1/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">301</a></td>
<td><a href="#_Toc17877476"><span>Added some text to describe additional changes to the VBECS dialog.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">6/8/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">159</a></td>
<td><a href="#_Toc17877476"><span>Added text and a screen capture for date ranges on the Meds tab.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">6/8/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">299</a></td>
<td><a href="#_Toc17877476"><span>Several changes have been made to VBECS and the changes are documented starting on this page.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">6/8/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">41</a></td>
<td><a href="#_Toc17877476"><span>The VistaWeb button changes color when remote data is available.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">6/8/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">403</a></td>
<td><a href="#_Toc17877476"><span>Updated the Most Recent Labs section with the new items in the display and with a new screen capture.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">6/1/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">161</a></td>
<td><a href="#_Toc17877476"><span>Added a section updating order checks to include Clinical Reminder order checks and other order checking changes.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">5/20/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">304</a></td>
<td><a href="#_Toc17877476"><span>Added items about new Additive Frequency field on Continuous Infusion orders.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">4/23/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">172, 197, 251</a></td>
<td><a href="#_Toc17877476">Updated the Meds tab <span>inpatient instructions</span> and <span>outpatient instructions</span> to talk about how CPRS determines which routes to display. Made the same update for <span>inpatient</span> and outpatient meds on the Orders tab. Also updated the graphic showing the Inpatient Medication dialog.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">4/12/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">72</a></td>
<td><a href="#_Toc17877476"><span>Updated the screen captures that show Combat Veteran status on the Consults dialog. Includes several dialogs over several pages.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">4/6/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">n/a</a></td>
<td><a href="#_Toc17877476"><span>Updated the Requesting a New Procedure from the Consults Tab section to include information on the Earliest Appropriate Date.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">4/5/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">383</a></td>
<td><a href="#_Toc17877476"><span>Updated the Creating a New Consult from the Consults Tab section to include information on the Earliest Appropriate Date.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">4/5/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">321</a></td>
<td><a href="#_Toc17877476"><span>Updated the Ordering a Consults section to include information on the Earliest Appropriate Date.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">3/31/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">320</a></td>
<td><a href="#_Toc17877476"><span>Updated the Ordering a Consults section to include information on the Earliest Appropriate Date.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">2/8/10</a></td>
<td><a href="#_Toc17877476">OR*3.0*280</a></td>
<td><a href="#_Toc17877476">161, 117</a></td>
<td><a href="#_Toc17877476">Added a new section that discusses the new site-defined Clinical Reminder order checks in the <span>Medications section</span> and one in the <span>Orders section</span>.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">5/11/09</a></td>
<td><a href="#_Toc17877476">OR*3.0*296</a></td>
<td><a href="#_Toc17877476">331</a></td>
<td><a href="#_Toc17877476"><span>Corrected an error. To receive lab results when available, the user must have the ORDERER-FLAGGED RESULTS notification enabled.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">1/21/09</a></td>
<td><a href="#_Toc17877476">OR*3.0*296</a></td>
<td><a href="#_Toc17877476">304, 310</a></td>
<td><a href="#_Toc17877476">Added notes to explain that changing the IV type also changes fields in the Infusions dialog for <span>Continuous to Intermittent orders</span> and <span>from Intermittent to Continuous orders</span>.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">1/21/09</a></td>
<td><a href="#_Toc17877476">OR*3.0*296</a></td>
<td><a href="#_Toc17877476">350</a></td>
<td><a href="#_Toc17877476"><span>Added a short paragraph about reminder evaluation.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">9/23/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*296</a></td>
<td><a href="#_Toc17877476">382</a></td>
<td><a href="#_Toc17877476"><span>Corrected the section on completing a consults from the Consults tab.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">9/18/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*296</a></td>
<td><a href="#_Toc17877476">299</a></td>
<td><a href="#_Toc17877476"><span>Made minor changes in the VBECS section regarding the default number of days for Type and Screen tests to be valid and some small changes.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">9/18/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*296</a></td>
<td><a href="#_Toc17877476">70</a></td>
<td><a href="#_Toc17877476"><span>Added a section that shows where the new Combat Veteran markers are in CPRS.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">8/11/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">412</a></td>
<td><a href="#_Toc17877476"><span>Added a note that the only circumference/girth value DoD is sending CPRS is the head measurement and it is only measured in inches.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">4/28/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">53, 54, 55, 56, 58, 63</a></td>
<td><a href="#_Toc17877476">Described some changes to graphing, including: <span>free-text values and comments</span>, <span>a new graphic</span>, <span>date ranges</span>, <span>configuring personal or public default inpatient and outpatient dates</span>, <span>views that use lab groups</span>, and <span>exporting data</span>.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">4/1/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">369</a></td>
<td><a href="#_Toc17877476"><span>Expanded template field section and added information about the screen reader stop and continue field template codes.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">4/1/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">360</a></td>
<td><a href="#_Toc17877476"><span>Added a brief description of a search animation that developers added for templates and that template searches should be much faster.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">3/28/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">18</a></td>
<td><a href="#_Toc17877476"><span>Described the dialog that displays when a user opens the chart, changes a patient's location from inpatient to outpatient or vice versa, and refreshes the patient chart before entering orders.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">3/26/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">160, 213</a></td>
<td><a href="#_Toc17877476">Added a note on how users can right-click select items and bring up the popup menu on the <span>Meds tab</span> and the <span>Orders tab</span>.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">3/26/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">213</a></td>
<td><a href="#_Toc17877476"><span>Added a section about using the Refill action on the Meds tab.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">3/13/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">215</a></td>
<td><a href="#_Toc17877476"><span>Expanded information about sorting the Orders tab view. Mostly definitions of the views.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">2/26/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">24</a></td>
<td><a href="#_Toc17877476"><span>Added content to what is included in patient inquiry information, including the new cell phone and secondary next of kin information.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">2/26/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">77</a></td>
<td><a href="#_Toc17877476">Added small comment about sending critical order checks to ancillary packages in the order checks section of the <span>Meds tab</span> and the <span>Orders tab</span>.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">2/21/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">348</a></td>
<td><a href="#_Toc17877476"><span>Added the Encounter item on the Action menu.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">2/20/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">27</a></td>
<td><a href="#_Toc17877476"><span>Added a note about where the focus will go, depending on whether the user is a provider, in the Provider &amp; Location for Current Activities dialog.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">2/20/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">378</a></td>
<td><a href="#_Toc17877476"><span>Added information about how alerts are sent when actions are taken on a consult.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">2/6/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">353</a></td>
<td><a href="#_Toc17877476"><span>Added information about the new Mental Health .dll and the requirements for use.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">1/15/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">332</a></td>
<td><a href="#_Toc17877476"><span>Added text about flags being automatically unflagged when processed if parameter is set.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">1/8/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">420</a></td>
<td><a href="#_Toc17877476"><span>Revised the section on fonts including the recommendation that magnifier software be used for fonts larger than 18 point.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">1/8/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">299</a></td>
<td><a href="#_Toc17877476"><span>Added a section about the new blood products ordering feature (VBECS).</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">1/4/08</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">75, 81, 151</a></td>
<td><a href="#_Toc17877476">Added information about the service connected condition Shipboard Hazard and Defense (SHD) and Southwest Asia Conditions (SWAC) on the <span>problem list</span> and the <span>sign orders</span> dialogs.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">12/18/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">209, 333</a></td>
<td><a href="#_Toc17877476">Added notes about outpatient medication order comments not begin carried over on <span>renew</span>, <span>copy</span>, and <span>change</span> actions. <span>Also added a note that comments are carried forward when transferring outpatient medications to inpatient medications.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">11/28/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">233</a></td>
<td><a href="#_Toc17877476"><span>Added a screen capture and note about possible conflict for delayed diet or outpatient meal orders.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">11/27/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">14</a></td>
<td><a href="#_Toc17877476"><span>Added instructions and screen captures for displaying forwarded comment on notifications.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">11/26/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">101, 394</a></td>
<td><a href="#_Toc17877476">Added a note about selecting cosigners in the <span>Additional Signers</span> section and the <span>Discharge Summary</span> section.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">11/21/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">4</a></td>
<td><a href="#_Toc17877476"><span>Added a short section Conventions section with a small discussion of dates and time, including the conversion of 00:00 to 00:01.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">11/21/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">23</a></td>
<td><a href="#_Toc17877476"><span>Added notes about rejoining and breaking context being disabled after a CCOW error.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">11/21/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">412</a></td>
<td><a href="#_Toc17877476"><span>Updated items referencing content of items in reports (Pulse Ox and HDR All Outpatient).</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">11/20/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">141, 231</a></td>
<td><a href="#_Toc17877476"><span>Added a note and a new screen capture to show the active allergies button and to explain that the user can no longer change the allergy originator.</span> <span>Also, added this note to the orders section.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">11/7/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">40</a></td>
<td><a href="#_Toc17877476"><span>Update the patient record flag pop-up to show the new items to make Category I flags more noticeable and altered the caption slightly.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">10/30/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">327</a></td>
<td><a href="#_Toc17877476"><span>Added a note about transfer events not being available for delayed orders if the patient is in an observation location.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">10/26/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">314</a></td>
<td><a href="#_Toc17877476"><span>Edited the steps for the Imaging orders relating to the new Reason for Study field and separating the Clinical History field. Also put in new screen capture of Imaging dialog.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">10/23/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">333</a></td>
<td><a href="#_Toc17877476"><span>Put in note about messages that might be received if HDR or DoD data is not available.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">10/8/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">211</a></td>
<td><a href="#_Toc17877476"><span>Add information to clarify what happens to unsigned, unreleased orders when discontinued.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">9/18/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td></td>
<td><a href="#_Toc17877476"><span>Added information about Health Summary feedback when HDR data is not available for some reason.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">9/18/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">403</a></td>
<td><a href="#_Toc17877476"><span>Changed the Most Recent section in Labs to let users know that if no time is defined for a lab test, instead of displaying the date and time, only the date will display.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">8/30/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">353</a></td>
<td><a href="#_Toc17877476"><span>Added section about the new JAWS files.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">8/21/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">188</a></td>
<td><a href="#_Toc17877476"><span>Added a section on sorting the Meds tab.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">8/21/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">189, 250</a></td>
<td><a href="#_Toc17877476">Added a small section about the new Clozapine requirement in the <span>Meds tab</span> section and the <span>Orders tab</span> section.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">8/20/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">226</a></td>
<td><a href="#_Toc17877476"><span>Added some information about quick orders in CPRS.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">8/16/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">8, 117</a></td>
<td><a href="#_Toc17877476"><span>Added some text about Personal patient list visibility.</span> <span>Added information about Personal List visibility and made the instructions into steps.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">6/26/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">77, 85</a></td>
<td><a href="#_Toc17877476">Added information about the new order location dialog used when patient status changes from outpatient to inpatient or vice versa: on <span>Review/Sign changes</span> and <span>Sign Selected</span> commands.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">6/26/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">302</a></td>
<td><a href="#_Toc17877476"><span>Infusion order changes.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">5/14/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">78</a></td>
<td><a href="#_Toc17877476"><span>Added steps for order checks during signature.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">3/27/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*232</a></td>
<td><a href="#_Toc17877476">various</a></td>
<td><a href="#_Toc17877476">Changed dates and removed review comments.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">2/16/07</a></td>
<td><a href="#_Toc17877476">OR*3.0*232</a></td>
<td><a href="#_Toc17877476">166, 222</a></td>
<td><a href="#_Toc17877476">Updated a screen capture in the <span><u>remote order check section in the Meds tab area</u></span> and in the <span>remote order check section in the Writing Orders area.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">10/31/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">194, 201, 202, 204, 208, 260, 267, 293, 295, 298</a></td>
<td><a href="#_Toc17877476">Added a new section about order checks under Medications for <span><u>inpatient medications simple dose</u></span>, <span><u>inpatient medications complex dose</u></span>, <span><u>outpatient medications simple dose</u></span>, <span><u>outpatient medications complex dose</u></span>, <span><u>non-VA medications</u></span>. The same information is included under orders for <span><u>inpatient medications simple dose</u></span>, <span><u>inpatient medications complex dose</u></span>, <span><u>outpatient medications simple dose</u></span>, <span><u>outpatient medications complex dose</u></span>, <span><u>non-VA medications</u></span>.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">10/30/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">313</a></td>
<td><a href="#_Toc17877476"><span>Added a note explaining that the user will be alerted if lab collection types will be automatically changed.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">10/30/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">209</a></td>
<td><a href="#_Toc17877476"><span>Added the step where the user will indicate whether the pending and original orders should be discontinued when discontinuing a pending renewal order.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">10/18/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">383</a></td>
<td><a href="#_Toc17877476">Added a note about how to get Consults details to find the reason for request from the <span><u>Notes tab</u></span> and from the <span><u>Consults tab</u></span>.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">9/13/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*232</a></td>
<td><a href="#_Toc17877476">184, 222</a></td>
<td><a href="#_Toc17877476">Updated a screen capture in the <span><u>remote order check section in the Meds tab area</u></span> and in the <span>remote order check section in the Writing Orders area.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">8/29/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">6</a></td>
<td><a href="#_Toc17877476"><span><u>Included note about CPRS not auto-selecting patient name unless the name is unique based on what the user types.</u></span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">8/29/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*243</a></td>
<td><a href="#_Toc17877476">184, 191, 258, 265</a></td>
<td><a href="#_Toc17877476">Added an explanation of when CPRS will not display an Expected First Dose for inpatient <span><u>simple</u></span> and <span><u>complex medications on the Meds</u></span> tab and <span><u>simple</u></span> and <span><u>complex medications on the Orders</u></span> tab.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">6/9/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*232</a></td>
<td><a href="#_Toc17877476">169, 222</a></td>
<td><a href="#_Toc17877476">Updated the <span><u>remote order check section in the Meds tab area</u></span> and in the <u><span>remote order check section in the Writing Orders area</span>.</u></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">4/5/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">79, 85</a></td>
<td><a href="#_Toc17877476">Added information about the user choosing where to have unsigned IMO order to be administered if the patient is admitted during the ordering session.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">4/3/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">131</a></td>
<td><a href="#_Toc17877476">Reminder evaluation warnings.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">4/3/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">342</a></td>
<td><a href="#_Toc17877476">Added a small blurb about the Show Details button that can be used when selecting a Progress Note title to resolve a consult.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">3/31/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">21</a></td>
<td><a href="#_Toc17877476">Added information about the My HealtheVet/Patient Insurance and Flag button being available and the new View | Information menu items that allows access to these items even if the screen is resized too small to show them.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">3/29/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">161, 220</a></td>
<td><a href="#_Toc17877476">Added a section on order checks that also talks about when a clinician would have to enter a justification for overriding the order check. This information was also included in the Orders section so that users can find it.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">3/27/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">213</a></td>
<td><a href="#_Toc17877476">How to see a custom order view of IMO orders for a patient.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">3/27/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">n/a</a></td>
<td><a href="#_Toc17877476">Made changes to the section that discusses Inpatient Medications for Outpatients on the Meds tab.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">3/27/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">N/A</a></td>
<td><a href="#_Toc17877476">Made changes to the section that discusses Inpatient Medications for Outpatients on the Orders tab.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">3/21/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">7</a></td>
<td><a href="#_Toc17877476">Added small section regarding the sorting order of characters such as ñ.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">3/3/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">140, 143, 145</a></td>
<td><a href="#_Toc17877476">Added updates about allergies: the bulletin sent message, signs and symptoms, and the Entered in Error parameter.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">3/2/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">420</a></td>
<td><a href="#_Toc17877476">Added to the "<span>Reports"</span> section information about graphing from the Reports tab.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">2/28/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">338</a></td>
<td><a href="#_Toc17877476">Added information about finding the notes in the current view that contain specific text.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">2/28/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">233</a></td>
<td><a href="#_Toc17877476">Added a note about inpatient diets being canceled and replaced when a new diet is entered.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">2/24/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">49</a></td>
<td><a href="#_Toc17877476">To the "Available from Any Tab" section, added information about the graphing tool.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">1/30/06</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">33</a></td>
<td><a href="#_Toc17877476">Added information about the Patient Insurance and My HealtheVet buttons.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">1/30/06</a></td>
<td><a href="#_Toc17877476">n/a</a></td>
<td><a href="#_Toc17877476">12</a></td>
<td><a href="#_Toc17877476">Made minor change to the keyboard sorting for notifications.</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476">12/01/05</a></td>
<td><a href="#_Toc17877476">OR*3.0*215</a></td>
<td><a href="#_Toc17877476">40</a></td>
<td><a href="#_Toc17877476"><span>Added information on VistAWeb and updated RDV screen shots.</span></a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
<td><a href="#_Toc17877476">REDACTED</a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476">8/2/05</a></td>
<td></td>
<td><p><a href="#_Toc17877476"><span>OR*3.0*215</span></a></p>
<p><a href="#_Toc17877476"><span>196</span></a></p></td>
<td><a href="#_Toc17877476"><span><span><strong>Error! Bookmark not defined.</strong></span></span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>5/16/05</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*215</span></a></td>
<td><a href="#_Toc17877476"><span>233, 241</span></a></td>
<td><a href="#_Toc17877476"><span>Added information about writing orders for outpatient meals.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>5/12/05</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*215</span></a></td>
<td><a href="#_Toc17877476"><span>34, 342</span></a></td>
<td><a href="#_Toc17877476"><span>Updated Patient Record Flag information to reflect changes involved with creating a link from the progress note to the patient record flag when writing the progress note. The link information for a single note can be viewed using the note detailed display. Also, added a step about linking when selecting a PRF progress note.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>4/12/05</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*215</span></a></td>
<td><a href="#_Toc17877476"><span>336</span></a></td>
<td><a href="#_Toc17877476"><span>Added information about getting TIU note details that show PRF link information for the specific note.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>3/31/05</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*231</span></a></td>
<td><a href="#_Toc17877476"><span>197, 206, 252, 288, 297</span></a></td>
<td><a href="#_Toc17877476"><span>The route field for medication orders no longer must be selected from the list. Changes include inpatient meds from the Meds tab, outpatient meds from the Meds tab, non-VA Meds from the Meds tab, inpatient meds from the Orders tab, outpatient meds from the Orders tab, and Non-VA meds from the Orders tab.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>3/8/05</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*231</span></a></td>
<td><a href="#_Toc17877476"><span>197, 206, 254, 288, 297</span></a></td>
<td><a href="#_Toc17877476"><span>Added notes about auto-completion of medication, dosage, route, and schedule fields in CPRS. Changes include inpatient meds from the Meds tab, outpatient meds from the Meds tab, non-VA Meds from the Meds tab, inpatient meds from the Orders tab, outpatient meds from the Orders tab, and Non-VA meds from the Orders tab.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>12/29/04</span></a></td>
<td><a href="#_Toc17877476"><span>n/a</span></a></td>
<td><a href="#_Toc17877476"><span>Various</span></a></td>
<td><a href="#_Toc17877476"><span>Updated graphics and other references to patient and provider identifiers to comply with SOP.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>11/29/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td></td>
<td><a href="#_Toc17877476"><span><span>Updated instructions for creating JAWS configuration files.</span></span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>11/24/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>various</span></a></td>
<td><a href="#_Toc17877476"><span>Additional revisions</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>11/16/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>various</span></a></td>
<td><a href="#_Toc17877476"><span>Added edits from various reviews</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>11/4/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>various</span></a></td>
<td><a href="#_Toc17877476"><span>Made minor revisions based on team feedback.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>10/29/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*222</span></a></td>
<td><a href="#_Toc17877476"><span>334</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a brief reference to the Group Notes Application.</span></span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>10/25/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>132, 229</span></a></td>
<td><a href="#_Toc17877476"><span>Made revisions to the sections that deal with entering allergies.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>9/3/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>n/a</span></a></td>
<td><a href="#_Toc17877476"><span><span>Revised the section describing when service connection and treatment factor exemption button display.</span></span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>8/10/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>305</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a new screen shot and instructions for the new Duration/Total Volume field for IV Fluids.</span></span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>7/26/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>39</span></a></td>
<td><a href="#_Toc17877476"><span><span>Editing the Patient Record Flag section to remove references to the information on the Patient Selection screen that was removed.</span></span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>6/11/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>147</span></a></td>
<td><a href="#_Toc17877476"><span>Revised Postings information to reflect the way users create postings for allergies, as opposed to the way users create other types of postings.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>6/9/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>132</span></a></td>
<td><a href="#_Toc17877476"><span>Updated information about entering allergies from the <strong>Orders</strong> tabs and added information about entering allergies from the <strong>Cover Sheet</strong> tab.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>6/9/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>193, 195, 201, 278</span></a></td>
<td><a href="#_Toc17877476"><span>Updated information in sections that discuss entering inpatient medications for outpatients (IMO orders): specifically, deleted information stating that CPRS displays IMO orders as inpatient medication orders and added information about new Meds tab and Orders tab IMO displays. Also added information about how CPRS handles ADT movements for IMO orders.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>6/3/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>69</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added official text to explain service connection and treatment factors.</span></span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>5/27/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>194, 196, 254, 262</span></a></td>
<td><a href="#_Toc17877476"><span>Added new instructions regarding the removal of free text schedules and the ability to create customized day-of-week/administration time schedule for inpatient medications using the new Other schedule item on the <span>Meds tab for simple</span> dose or <span>complex dose</span> and from the <span>Orders tab for simple dose</span> or <span>complex dose</span>.</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>5/12/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>109</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added information about the user setting the date ranges for Encounters.</span></span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>5/3/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>115</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a screen shot for the new option on the Lists/Teams tab of the Options</span> <span>Also added information and screen captures for creating and maintaining a Personal Diagnosis List.</span></span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>3/16/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*195</span></a></td>
<td><a href="#_Toc17877476"><span>n/a</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added overview of Clinical Indicators Data Capture changes to the GUI.</span></span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
<td><a href="#_Toc17877476"><span>REDACTED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>4/1/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>205, 296</span></a></td>
<td><a href="#_Toc17877476"><span>Added information about order checks for non-VA meds entered on the <span>Meds tab</span> and the <span>orders tab</span>.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>3/30/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>391</span></a></td>
<td><a href="#_Toc17877476"><span>Added section about the surgery tab in CPRS.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>3/24/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>11</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added information about sorting Notifications using the keyboard only.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>3/3/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>229</span></a></td>
<td><a href="#_Toc17877476"><span>Modified content in the "Entering Allergies from the Orders Tab" section to reflect recent changes in the Adverse Reaction Tracking package. (Users can no longer enter free-text allergies.)</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>2/20/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>159</span></a></td>
<td><a href="#_Toc17877476"><span><span>Replaced Meds tab screen shot with one showing Non-VA, Inpatient, and Outpatient Meds.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>2/5/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>40</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added change to describe what type of remote data users can get (including Clinical Reports).</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>2/4/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*187</span></a></td>
<td><a href="#_Toc17877476"><span>315</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a change to the instructions and the screen capture about to how to place radiology/imaging orders to reflect the Pregnant field being mandatory.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>2/4/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*187</span></a></td>
<td><a href="#_Toc17877476"><span>110</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a note that setting a default tab that CPRS should open to when changing patients or logging in again will not take effect without first exiting and logging back in to CPRS.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>2/2/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*187</span></a></td>
<td><a href="#_Toc17877476"><span>6</span></a></td>
<td><a href="#_Toc17877476"><span><span>Clarified that patient selection displays a list of possible matches when last names and last 4 digits of the social security number match.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>1/28/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>216</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added information about the Recently Expired Orders view selection on the Orders tab.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>1/28/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>10, 11, 17</span></a></td>
<td><a href="#_Toc17877476"><span>Added <span>general information about removing notifications</span> and <span>sorting</span>. Also, added a note about <span>Remove button only removing those notifications placed in the ORB REMOVE parameter.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>1/26/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>39</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added text and screen shot for the new Patent Record Flag pop-up box.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>1/26/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>347</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a screen shot and text about Combat Veteran exemption on the Encounter form.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>1/26/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>11 - 16</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added screenshots and information regarding the Combat Veteran co-pay exemption</span> and <span>the qualifications for Combat Veteran status</span> on the signing dialogs.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>1/22/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>296</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added an overview and instructions for entering Non-VA medications into CPRS.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>1/14/04</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*190</span></a></td>
<td><a href="#_Toc17877476"><span>229</span></a></td>
<td><a href="#_Toc17877476"><span>Updated information about creating allergy orders to reflect ART changes to CPRS GUI version 24.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>9/16/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*191</span></a></td>
<td><a href="#_Toc17877476"><span>412, 417</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a note about DoD Consults information</span> <span>and the actual listing of the report.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>8/05/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*187</span></a></td>
<td></td>
<td><a href="#_Toc17877476"><span>Added to the <span>Meds tab</span> and <span>Orders</span> tab sections instructions for ordering inpatient medications for outpatients. This functionality is new with CPRS version 23. Added a note about sites' ability to specify inpatient medication order stop dates. The note also mentions sites' ability to specify the status of inpatient medication orders when patients are transferred. Also added a note explaining what happens if users change their clinic selection after they have started an order.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>7/30/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*187</span></a></td>
<td><a href="#_Toc17877476"><span>27, 101, 321, 322, 342, 384, 397</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added information about new functionality that makes it easier to distinguish between providers who have identical given names and surnames</span>.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>8/27/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*202</span></a></td>
<td><a href="#_Toc17877476"><span>384</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a note about provisional diagnosis and inactive codes.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>8/27/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*202</span></a></td>
<td><a href="#_Toc17877476"><span>348</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a note and graphics as an example of a diagnosis or procedure code that needs to be changed on the Encounter form.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>8/27/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*202</span></a></td>
<td><a href="#_Toc17877476"><span>156, 158</span></a></td>
<td><a href="#_Toc17877476"><span>Added note about inactive problem codes for <span>adding a new problem</span>, <span>annotating a problem</span>, and <span>verifying a problem</span>.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>8/26/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*202</span></a></td>
<td><a href="#_Toc17877476"><span>20, 125</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added Code Set Versioning overview.</span> <span>Added a brief note about inactive codes on the Cover sheet</span>.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>8/19/03</span></a></td>
<td></td>
<td><a href="#_Toc17877476"><span>34</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added an overview of Patient Record Flags and a section on how to view flags.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>7/1/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*163</span></a></td>
<td><a href="#_Toc17877476"><span>64</span></a></td>
<td><a href="#_Toc17877476"><span><span>Minor edits to PKI information.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>6/17/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*173</span></a></td>
<td><a href="#_Toc17877476"><span>10</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added information on comments for forwarded Notifications</span>.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>5/27/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*173</span></a></td>
<td><a href="#_Toc17877476"><span>103</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added instructions on how to print multiple Notes, Consults, or Discharge Summaries.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>5/27/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*173</span></a></td>
<td><a href="#_Toc17877476"><span>195, 199, 258, 265</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added changes for Give Additional Dose Now on Med tab for simple orders</span> and <span>for complex orders</span>. Also, <span>added the changes to Give Additional Dose Now for Simple orders on the Orders tab</span> <span>and Give Additional Dose Now for Complex inpatient dosages on the orders tab.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>5/27/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*173</span></a></td>
<td><a href="#_Toc17877476"><span>10</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added sections about sorting notifications and alerts by column headings and the addition to the CPRS GUI of the Forward, Remove, and Renew actions familiar to List Manager users.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>5/27/03</span></a></td>
<td></td>
<td><a href="#_Toc17877476"><span>356</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added information about creating additional patient data object in the CPRS Template Editor.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>5/19/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*173</span></a></td>
<td><a href="#_Toc17877476"><span>21</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added information about CCOW and application synchronization.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>5/16/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*180</span></a></td>
<td><a href="#_Toc17877476"><span>412</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added entry that Allergies will be included as part of the Federal Health Information Exchange (FHIE) project.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>3/1/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*149</span></a></td>
<td><a href="#_Toc17877476"><span>420</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added <em>Appendix A – Accessibility, which</em> contains information about how to change the font size and window color in CPRS, as well as how to set up a JAWS configuration file.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="#_Toc17877476"><span>331</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a description of the "Flagged" indicator to</span> the <em>Flagging an Order</em> section.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><a href="#_Toc17877476"><span>211</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a new description</span> of how unsigned orders are displayed on the Orders tab.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><a href="#_Toc17877476"><span>219</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added a note about viewing results and the results history using the right-click menu on the orders tab</span>.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>2/13/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*163</span></a></td>
<td><a href="#_Toc17877476"><span>64</span></a></td>
<td><a href="#_Toc17877476"><span><span>Added overview and instructions for digital signatures for VA/DEA Digital signature (PKI) pilot project.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>2/4/03</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*160</span></a></td>
<td><a href="#_Toc17877476"><span><span>412</span></span></a></td>
<td><a href="#_Toc17877476"><span><span>Added notations of reports that will be included as part of the Federal Health Information Exchange (FHIE) project.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>10/6/02</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*141</span></a></td>
<td></td>
<td><a href="#_Toc17877476"><span><span>Orders tab changes and event-delayed orders</span>.</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>6/4/02</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*148</span></a></td>
<td></td>
<td><a href="#_Toc17877476"><span><span>CPT modifiers can now be selected on the Visit tab of the Encounter form. A new screen shot was added to reflect this change.</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>5/21/02</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*148</span></a></td>
<td></td>
<td><a href="#_Toc17877476"><span><span>Added Surgery tab documentation</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>5/21/02</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*148</span></a></td>
<td></td>
<td><a href="#_Toc17877476"><span><span>Added Clinical Procedures documentation</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>5/21/02</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*148</span></a></td>
<td></td>
<td><a href="#_Toc17877476"><span><span>Added documentation for the Copay/Millennium Bill phase II changes to the Problems tab</span></span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>5/8/2002</span></a></td>
<td><a href="#_Toc17877476"><span>OR*3.0*148</span></a></td>
<td></td>
<td><a href="#_Toc17877476"><span><span>Updated information about Remote Data Views and Reports, including Department of Defense remote data. Added information about problem list</span></span></a></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Revision HistoryThis table lists the history for each revision of this document by row in descending order

[[  
](#OR_signature_key_update)](#_Toc17877476)

[[The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update all the information connected with any patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient's allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.](#_Toc17877464)](#_Toc17877476)

[[CPRS documentation is also available on the VistA intranet. The intranet version is constantly updated and may contain more current information than this print version. CPRS documentation is available on the VistA intranet.](#_Toc17877464)](#_Toc17877476)

[[Instructions, procedures, and other information are available from the CPRS online help file. You may access the help file by clicking Help \| Contents from the menu bar or by pressing the F1 key while you have any CPRS dialog open. Much of the information in this User Manual is also in the CPRS online help.](#_Toc17877464)](#_Toc17877476)

[[CPRS was designed to run in both the Microsoft Windows operating environment and on text-based terminals. The terminal or text-based version of CPRS (also known as the List Manager version) is not described in this manual. This manual describes the Windows version of CPRS.](#_Toc17877464)](#_Toc17877476)

[[This manual is organized in the way most people will use the CPRS GUI. It begins with how to log on to the system and then how to select a patient. The manual continues with an explanation of the features that are available from each CPRS tab.](#_Toc17877464)](#_Toc17877476)

[[We hope this organization will help you understand the basic layout of the CPRS GUI and provide you with information about the specific tasks you will perform.  
](#_Toc17877464)](#_Toc17877476)

[[Throughout CPRS, some items are always or almost always the same. This section deals with a few of these conventions in the CPRS GUI interface.](#_Toc17877464)](#_Toc17877476)

[[In some cases, users can also enter a date with no known time (T@U). CPRS used to assign a time of 00:00 to this entry, but now, it will not put a time in for this case.  
](#_Toc17877464)](#_Toc17877476)

[[  
](#_Toc17877464)](#_Toc17877476)

1.  
2.  
3.  
4.  

[[  
](#_Toc17877464)](#_Toc17877476)

[[After you log in to CPRS, the Patient Selection screen, shown below, is the first thing to appear. You should now select a patient record to view.](#_Toc17877464)](#_Toc17877476)

<span id="patient_select_screen_1" class="anchor"></span>

1.  

> [[If you are just opening CPRS, skip to step 2. Otherwise, select File \| Select New Patient...Note: If you have just entered orders or documents that are unsigned, a screen will pop up asking you to review and sign the changes.](#_Toc17877464)](#_Toc17877476)

2.  
- 
- 
- 

[[Do one of the following: Type the patient's full social security number with or without dashes (000-44-4444 or 000444444) or type the full social security number with "P" as the last character (000-44-4444p, or 000444444p).Type part of the patient's last name or the patient's entire name (e.g. "CPRSp" or "CPRSpatient,One").Type the first letter of the patient's last name and the last four digits of the patient's Social Security number (c4444).CPRS will try to match what you entered to a patient and highlight that patient. The patient's name and other information will appear below the Cancel button.](#_Toc17877464)](#_Toc17877476)

> [[Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a patient name if the user types enough characters to uniquely identify a name in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user explicitly selects an item using the mouse or the keyboard.](#_Toc17877464)](#_Toc17877476)

3.  

> [[Verify that the correct patient is highlighted. If the correct patient is highlighted, click OK. If the correct patient is not highlighted, scroll through to find the correct patient, highlight the name, and then click OK.Note: If CPRS finds more than one patient with the same last name and same last four digits of the social security numbers, a box will popup listing possible matches. Select the correct patient and click OK.](#_Toc17877464)](#_Toc17877476)

[[When you select OK, CPRS opens to the Cover Sheet (unless you have set it to open to a different tab).](#_Toc17877464)](#_Toc17877476)

[[You can also use the radio buttons under the Patient List heading (located on the left-side of the window) to group the patient list according to provider, team, specialty, clinic, or ward. When you select a specific list for a provider, team, specialty, clinic, or ward, CPRS will display the associated patients in the Patients list box, followed by a line, and then the comprehensive patient list. You can then scroll to find the name. Your Clinical Coordinator will usually create the lists for the teams, wards, and so on.](#_Toc17877464)](#_Toc17877476)

- 
- 

[[Tools \| Graphing \| Select/Define \| Select PersonTools \| Options \| Notes \| Notes \| Default Cosigner The screenshots in this manual that display a provider's name have not been updated with NPI data. However, there will be a note near the screenshot that tells whether or not the NPI will display.](#_Toc17877464)](#_Toc17877476)

[[Note that Piña is after Pizzelo. This is because VistA sorts these characters based on their numeric values in the character set that VistA uses. For example, in that table, the number for lowercase "a" might be 97, "z" might be 122, and "ñ" might be 241. Characters other than the uppercase and lowercase Latin alphabetic characters and numbers, such as ñ or the tilde (~) will display wherever their numeric equivalent falls, which is generally after z.  
](#_Toc17877464)](#_Toc17877476)

[[When you select a patient record to open, you may receive one or more of the following messages:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
- 

[[You or your Clinical Coordinator can create patient lists or team lists that simplify tasks such as reviewing patient charts, ordering, and signing orders and notes. These lists can be based on wards, clinics, teams, or other groups. Users can create their own personal Patient Lists in the CPRS GUI. When the user creates the list, the user designates if the list can be viewed only by the owner (the person creating the list) or by all CPRS users. Clinical Application Coordinators (CACs) can create and manage general patient lists through the List Manager interface (the character-based version of CPRS).](#_Toc17877464)](#_Toc17877476)

[[With patient lists you can:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 

[[To make it easier for you to locate your patients, CPRS enables you to set a default patient list. This is the list that will appear when you launch CPRS. For example, if you work in a specific ward, you can set the default patient list to be the list for that ward.](#_Toc17877464)](#_Toc17877476)

[[To set the default patient list, use these steps:](#_Toc17877464)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  

> [[If you are just opening CPRS, skip to step 2. Otherwise, select File \| Select New Patient.... In the Patient Selection screen, select the category in which you want to search for a patient's record by clicking the option button in front of the category (Default, Providers, Teams, Specialties, Clinics, Wards, or All). In the list box below the option button, click the item that narrows the search further (such as a specific ward). If you select something other than All, CPRS sorts the patient list and divides the list into two parts: The names above the line are the names for the category and item you selected; the names below the line make up a comprehensive patient list. To save the patient list as your default list, click Save Patient List Settings. If you selected "Clinics" in step 2, a dialog that resembles Figure A will appear.![](cprs-user-manual-gui-version-updated-or-3-0-499/009.png)](#_Toc17877464)](#_Toc17877476)

> [[This dialog enables the user to save kinds of clinic lists](#_Toc17877464)](#_Toc17877476)

7.  

> [[Select "Save For All Days of Week" to set the clinic as the default patient list for all days of the week.-or-](#_Toc17877464)](#_Toc17877476)

> [[select "Save For Current Day Only" if you wish to set the clinic as the default for only the current day of the week.](#_Toc17877464)](#_Toc17877476)

8.  

> [[Press OK.](#_Toc17877464)](#_Toc17877476)

[[Notifications are messages that provide information or prompt you to act on a clinical event. Clinical events, such as a critical lab value or a change in orders, trigger a notification to be sent to all recipients identified by the triggering package (such as Lab, CPRS, or Radiology).](#_Toc17877464)](#_Toc17877476)

[[There are two different listings for N<span id="notif_Patient_centric" class="anchor"></span>otifications, Provider-centric and patient-centric. Provider-centric notifications are shown on the Patient selection screen and all pertain to the user that is logged in. The user brings up Patient-centric notifications or alerts in their own dialog box by selecting an item from the File menu.](#_Toc17877464)](#_Toc17877476)

- 

[[Provider-centric: The listing on the Patient Selection screen shows all notifications for the provider  
  
](#_Toc17877464)](#_Toc17877476)

<span id="patient_select_screen_2" class="anchor"></span>

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/010.png)](#_Toc17877464)](#_Toc17877476)

[[Provider-centric view of Notifications on the Patient Selection screen.](#_Toc17877464)](#_Toc17877476)

- 
- [[Action alerts: When you process notifications that require an action, such as signing an order, CPRS brings up the chart tab and the specific item (such as a note requiring a signature) that requires action.](#_Toc17877464)](#_Toc17877476)
- [[Informational alerts: CPRS places an "I" before "information-only" notifications. Once you view (process) information-only notifications, CPRS deletes them.](#_Toc17877464)](#_Toc17877476)
- [[Long Text Information alerts: CPRS places an "L" before a long alert. Long alerts have more text than will fit on one line as alerts are normally displayed. Processing the alert will bring up a dialog with additional actions.](#_Toc17877464)](#_Toc17877476)
- [[Removing notifications is the same as deleting them. A new parameter (ORB REMOVE) enables you site to identify which notifications can be removed without processing.](#_Toc17877464)](#_Toc17877476)
- [[Renewing notifications is useful when a user is processing a view alert, such as an abnormal lab result, and decides that the alert should not go away after the user views it. In this case, the user can renew the alert and it will still be there the next time the user logs in to CPRS.](#_Toc17877464)](#_Toc17877476)
- [[Forwarding notifications enables users to send an alert to someone else at the site. The user can choose from the list of names that is in your site's New Person file.](#_Toc17877464)](#_Toc17877476)
- [[Deferring notifications enables a user to defer a notification for a period of time from 5 minutes to 14 days. Deferring will remove the notification from the display for the designated period of time, after which, it will display again. Users can defer notifications as many times as they choose until the system removes them.](#_Toc17877464)](#_Toc17877476)

[[<span id="Notification_Defer_Option_1" class="anchor"></span>  
![](cprs-user-manual-gui-version-updated-or-3-0-499/013.png)  
Example of the Defer Patient Notification option](#_Toc17877464)](#_Toc17877476)

<span id="Notification_Defer_Option_2" class="anchor"></span>

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/014.png)  
A dialog shows that the notification was successfully deferred](#_Toc17877464)](#_Toc17877476)

[[  
](#_Toc17877464)](#_Toc17877476)

[[To enable users to decide which of their Notifications or Alerts they would like to process first, the format for displaying Notifications in the CPRS GUI has been changed to columns that enable users to sort their Notifications based on column heading:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 

[[Info (information alerts are preceded with an "I") Patient name (alphabetical or reverse alphabetical) Location (patient location, if known, alphabetical or reverse alphabetical) Urgency (valued HIGH, Moderate, or low as indicated by the CPRS parameter ORB URGENCY. TIU alerts are given a Moderate urgency value. Other alerts without a parameter value are given an urgency of low.) Alert Date/Time (date/time the alert was triggered, newest to oldest or oldest to newest) Message (alert message or text, alphabetical or reverse alphabetical) Forwarded By/When (sorts alerts alphabetically and then by time for the same forwarding person) <span id="Notification_Order" class="anchor"></span>  
![](cprs-user-manual-gui-version-updated-or-3-0-499/015.png)](#_Toc17877464)](#_Toc17877476)

[[This graphic shows the alerts sorted by date. Clicking a heading will sort the alerts by that heading](#_Toc17877464)](#_Toc17877476)

[[When the user exits CPRS or changes patients, CPRS stores which column the user sorted by and sorts by that column again when the Patient Selection/Notifications screen is next displayed. By default, after the user changes patients or enters CPRS again, the column that is saved will sort in ascending alphabetical order (A-Z) except for the Date/Time column that will sort by most recent date/time to oldest.](#_Toc17877464)](#_Toc17877476)

[[  
](#_Toc17877464)](#_Toc17877476)

[[To sort Notifications using the mouse, click the column heading you want to sort by. To reverse the sort order, click the same heading again. For example, a user could decide to sort by date and time. Normally, the most recent alerts are listed first. The user could click the column heading to reverse the order and have the oldest alerts displayed first. Clicking the column heading again would list the most recent alerts first.](#_Toc17877464)](#_Toc17877476)

[[Users who do not use the mouse can sort Notifications in ascending order (alphabetical order or most recent Date/Time) using the keyboard only. When users sort using the Ctrl + \<key\> combination, CPRS will recognize either upper or lowercase letters (this feature is not case-sensitive). Users can sort Notifications using the following Ctrl + \<key\> combinations:](#_Toc17877464)](#_Toc17877476)

| [[Key Combination](#_Toc17877464)](#_Toc17877476) | [[Column Sorted](#_Toc17877464)](#_Toc17877476) |
|-------------------------------------------------------|-----------------------------------------------------|
| [[Ctrl + I](#_Toc17877464)](#_Toc17877476)            | [[Info](#_Toc17877464)](#_Toc17877476)              |
| [[Ctrl + P](#_Toc17877464)](#_Toc17877476)            | [[Patient](#_Toc17877464)](#_Toc17877476)           |
| [[Ctrl + L](#_Toc17877464)](#_Toc17877476)            | [[Location](#_Toc17877464)](#_Toc17877476)          |
| [[Ctrl + U](#_Toc17877464)](#_Toc17877476)            | [[Urgency](#_Toc17877464)](#_Toc17877476)           |
| [[Ctrl + D](#_Toc17877464)](#_Toc17877476)            | [[Alert Date/Time](#_Toc17877464)](#_Toc17877476)   |
| [[Ctrl + M](#_Toc17877464)](#_Toc17877476)            | [[Message](#_Toc17877464)](#_Toc17877476)           |
| [[Ctrl + F](#_Toc17877464)](#_Toc17877476)            | [[Forwarded By/When](#_Toc17877464)](#_Toc17877476) |

[[Note: A limitation exists in the programming environment that does not allow the user to user the same key combination to then reverse the sort. Making this change would not be trivial and will not be addressed the CPRS GUI at this time.](#_Toc17877464)](#_Toc17877476)

[[  
](#_Toc17877464)](#_Toc17877476)

[[Users may also want to view comments associated with forwarded alerts. To view a comment, simply place the cursor over the alert, leave it still for a few seconds, and the comment will display. Move the mouse and the comment will no longer be displayed.  
<span id="Deleted_forwarded_notification" class="anchor"></span>](#_Toc17877464)](#_Toc17877476)

[[To bring up the forwarded comment in a separate dialog, highlight the notification with the comment and select the Show Comment button. CPRS will display a dialog similar to the one shown below:](#_Toc17877464)](#_Toc17877476)

[[<span id="Notification_forwarded" class="anchor"></span>  
![](cprs-user-manual-gui-version-updated-or-3-0-499/016.png)](#_Toc17877464)](#_Toc17877476)

[[When the user clicks the Show Comment button for a notification that has a forwarded comment, the comment shows in a dialog.](#_Toc17877464)](#_Toc17877476)

[[Note: If the provider has an NPI, it will not display on the "Forwarded by" screen.](#_Toc17877464)](#_Toc17877476)

[[  
](#_Toc17877464)](#_Toc17877476)

- 
- 

[[You can specify the date range for the alerts. You can limit the number of alerts in the table.  
![](cprs-user-manual-gui-version-updated-or-3-0-499/017.png)](#_Toc17877464)](#_Toc17877476)

[[Example of the Processed alerts tab in the Patient Selection dialog](#_Toc17877464)](#_Toc17877476)

[[To process notifications, use these steps:](#_Toc17877464)](#_Toc17877476)

1.  
2.  - 
    - 
    - 

> [[Bring up the Patient Selection screen, either by launching CPRS or if you are already running CPRS, selecting File \| Select New Patient. Decide which notifications to process. To process all information notifications (items preceded by an I.), click Process Info. To process all notifications, select Process All. To process specific notifications, highlight one or more notifications, and then select Process. You can also process a notification by double clicking on it.Note: To select a number of notifications in a row, click the first item, hold down the Shift key, and click the last item. All items in the range will be selected. To select multiple items that are not in a row, click one, hold down the Control key, and click the other specific notifications.](#_Toc17877464)](#_Toc17877476)

3.  

> [[Process the notification by completing the necessary task, such as signing an overdue order or viewing information notifications. Note: For Audio Renewal requests that cannot be automatically renewed for some reason, CPRS has a new notification. The Nonrenewable RX Request for notification is an action alert that takes the user to the orders tab. The user can then use the Copy to New Order feature (because the order cannot be renewed) if they want to continue the medication therapy for the patient. If providers receive an alert for a patient they no longer see, they can Forward the alert to the appropriate provider. Who receives the alert is based on the set up for the alert. Contact your CAC or similar personnel if you are repeatedly getting alerts for the wrong patients. If you want to renew or forward this notification to someone else, right click the Next button and select either Renew or Forward as shown in the graphic below. If you selected Forward, proceed to step 5. If you selected Renew, go to step 6.](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/018.png)](#_Toc17877464)](#_Toc17877476)

[[This above graphic shows the pop-up menu items available by right-clicking the Next button](#_Toc17877464)](#_Toc17877476)

[[](#_Toc17877464)](#_Toc17877476)

4.  

> [[Select the individuals that you want to receive this notification.Note: If the provider has an NPI, it will display on the screen below. See the "National Provider Identifier (NPI) Display in CPRS" section for an example of an NPI displaying on a screen.](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/019.png)](#_Toc17877464)](#_Toc17877476)

[[The Forward Alert dialog](#_Toc17877464)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
5.  
6.  
7.  

[[In the field labeled Select or enter name, type the first few letters of the person's last name. Find the person's name in the list and click it to add it to the list of recipients. Repeat steps a and b until all those you want to forward this notification to are listed under Currently selected recipients. Type a comment if needed (comment length is limited to 180 characters including spaces). Click OK. When finished with the current Notification, go to the next notification by clicking the Next button on the status bar. Process the remaining notifications using steps 3-5. When finished, you may select a new patient (File \| Select New Patient…) or exit CPRS (File \| Exit).](#_Toc17877464)](#_Toc17877476)

[[<span id="Notifications_processed_details" class="anchor"></span>To specify the date range for processed notifications, and the maximum number of processed alerts to display, use these steps:](#_Toc17877464)](#_Toc17877476)

1.  - 1.  
      2.  
      3.  

> [[You can specify the date range and maximum number by clicking on either the Tools – Options tab or the Processed tab in the Patient Selection dialog:If you click the Tools – Options tab:On the Notifications tab, click the Processed Alerts Settings button.On the Processed Alerts Preferences screen, enter a value in the Show Log Data for (days) and/or Max \# of records to show field and click OK.  
> Note: To set the values to the defaults, click the Defaults button. Click OK on the Notifications tab.![](cprs-user-manual-gui-version-updated-or-3-0-499/020.png)  
> Processed Alerts Preferences screen  
> ](#_Toc17877464)](#_Toc17877476)

- 1.  1.  
  2.  1.  

> [[If you click the Processed tab in the Patient Selection dialog:If you want to edit the date range, click the Date Range button:On the Range Selector screen, select a value from the Start and/or Stop Date dropdown and click OK. To set the values back to the defaults, click the Reset button.If you want to change the maximum number of alerts that will display on the Processed tab, click the Max \# of Alerts button:On the Processed Alerts Preferences screen, enter a value in the Enter Max \# of Alerts to Review field and click OK. ![](cprs-user-manual-gui-version-updated-or-3-0-499/021.png)](#_Toc17877464)](#_Toc17877476)

> [[Date Range and Max \# of Alerts buttons on the Processed tab](#_Toc17877464)](#_Toc17877476)

[[To remove notifications, use these steps:](#_Toc17877464)](#_Toc17877476)

1.  
2.  

> [[Bring up the Patient Selection screen, either by launching CPRS or if you are already running CPRS, selecting File \| Select New Patient. Highlight the notifications that you want to remove. Note: To select a number of notifications in a row, click the first item, hold down the Shift key, and click the last item. All items in the range will be selected. To select multiple items that are not in a row, click one, hold down the Control key, and click the other specific notifications.](#_Toc17877464)](#_Toc17877476)

> [[Warning: Once you remove these notifications you cannot get them back. Be careful that you really want to remove or delete these notifications before you proceed.](#_Toc17877464)](#_Toc17877476)

3.  

> [[Click Remove. Note: A new parameter ORB REMOVE enables sites to specify which notifications can be removed in this way. If the notification is not removed, you will have to process the notification.](#_Toc17877464)](#_Toc17877476)

[[To forward a notification to another user, use these steps:](#_Toc17877464)](#_Toc17877476)

1.  
2.  

> [[Bring up the Patient Selection screen, either by launching CPRS or if you are already running CPRS, selecting File \| Select New Patient. Highlight the notifications that you want to forward and click Forward. Note: To select a number of notifications in a row, click the first item, hold down the Shift key, and click the last item. All items in the range will be selected. To select multiple items that are not in a row, click one, hold down the Control key, and click the other specific notifications.When the dialog shown below displays for each notification, select the recipients' names for this notification.](#_Toc17877464)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will display on the screen below. See the "National Provider Identifier (NPI) Display in CPRS" section for an example of an NPI displaying on a screen.](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/022.png)](#_Toc17877464)](#_Toc17877476)

3.  
4.  
5.  
6.  
7.  

[[In the field labeled Select or enter name, type the first few letters of the person's last name. Find the person's name in the list and click it to add it to the list of recipients. Repeat steps 4 and 5 until all those you want to forward this notification to are listed under Currently selected recipients. Type a comment if needed (comment length is limited to 180 characters including spaces). Select OK. Repeat the above steps as necessary for additional notifications you want to forward.](#_Toc17877464)](#_Toc17877476)

[[This dialog appears after a refresh when the patient's location has been changed, but no orders have been written yet. The reason for this is that sometimes it can be difficult to make sure the patient's location is correct when the location has changed  
](#_Toc17877464)](#_Toc17877476)

[[  
](#_Toc17877464)](#_Toc17877476)

[[For Consults and Procedures, only active codes will be allowed for the following functions:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 

[[CPRS GUI will only display codes that were active in the reminder date range.](#_Toc17877464)](#_Toc17877476)

[[If a program has a time out and it is idle for a specific amount of time, it will be closed. A time out ensures that a record can be accessed by others who might need it if someone has opened the record, but is not using it.](#_Toc17877464)](#_Toc17877476)

[[IRM can set a different time out or idle value for CPRS (such as 10 minutes) through a CPRS GUI parameter. If CPRS is open but not used for the time specified in the parameter, CPRS will display the dialog informing you that it is going to close in the number of seconds IRM set, count down to zero, and then close.](#_Toc17877464)](#_Toc17877476)

- 
- 

[[To keep CPRS running, select Don't Close CPRS. To close CPRS immediately, select Close CPRS.If only one CPRS session is open, the dialog looks like this:](#_Toc17877464)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/029.png)](#_Toc17877464)](#_Toc17877476)

[[  
](#_Toc17877464)](#_Toc17877476)

[[If multiple sessions are open, the dialog looks like this, including the identification of which session is about to close:](#_Toc17877464)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/030.png)](#_Toc17877464)](#_Toc17877476)

[[Because CPRS makes the session that is about to close active, users need to make sure they are in the correct chart after the user responds to this dialog.  
](#_Toc17877464)](#_Toc17877476)

[[  
](#_Toc17877464)](#_Toc17877476)

[[There are several items located at the top of the CPRS window that are available from any tab. These items are:](#_Toc17877464)](#_Toc17877476)

- [[the CCOW icon](#_Toc17877464)](#_Toc17877476)
- [[the Patient Inquiry button](#_Toc17877464)](#_Toc17877476)
- [[the Encounter Provider and Location button](#_Toc17877464)](#_Toc17877476)
- [[the Primary Care button](#_Toc17877464)](#_Toc17877476)
- [[the Patient Insurance/My HealtheVet button (which is hidden if the patient has no insurance nor My HealtheVet information)](#_Toc17877464)](#_Toc17877476)
- [[the Flag button](#_Toc17877464)](#_Toc17877476)
- [[the Vista Web button, the Remote Data button](#_Toc17877464)](#_Toc17877476)
- [[the Reminders button](#_Toc17877464)](#_Toc17877476)
- [[the Postings button](#_Toc17877464)](#_Toc17877476)
- 
- 

[[a context vault, which is a server on the VA LAN that tracks context for each clinical workstation desktop components installed on each workstation that will use CCOW To allow VistA GUI applications to use context management, the developers must make the necessary changes to HL7 messages for each application to allow synchronization. Current plans call for the following applications to be CCOW compliant:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
1.  
2.  
3.  

[[Give focus to the application that you want to join context by either clicking on that application window or by holding down the Alt key and pressing tab until you highlight the appropriate application and then release the keys. Choose File \| Rejoin patient link. If you want the other open applications to synchronize with the current patient in the application that has focus, choose Set new context. Or, if you want the current application to synchronize with the patient the other applications have open, choose Use Existing Context.To break context between applications, follow these steps:](#_Toc17877464)](#_Toc17877476)

[[Note: If a context error occurs, the Rejoin patient link menu item will not be available for the rest of the current CPRS session. It will be available again when the user closes CPRS and then launches CPRS again.](#_Toc17877464)](#_Toc17877476)

1.  
2.  

[[Give focus to the application that you want to remove from context by either clicking on that application window or by holding down the Alt key and pressing tab until you highlight the appropriate application and then release the keys. Choose File \| Remove from link.](#_Toc17877464)](#_Toc17877476)

[[  
](#_Toc17877464)](#_Toc17877476)

[[The Patient Inquiry button is located on the left side of the chart directly below the menu bar. The Patient Inquiry button displays the following information:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

[[Patient name Status (inpatient or outpatient) Social Security number (or identification number if assigned by the site) Date of birth Age Display Caregiver information (if available). The primary, secondary, and general caregiver(s) will display if they are present and considered active.![](cprs-user-manual-gui-version-updated-or-3-0-499/038.png)](#_Toc17877464)](#_Toc17877476)

[[The Patient Inquiry button](#_Toc17877464)](#_Toc17877476)

[[<span id="preferred_name_patient_inquiry_button" class="anchor"></span>If the patient's preferred name has been entered into VistA, it will display in parentheses after the patient's first name on the Patient Inquiry button, as shown below:  
](#_Toc17877464)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/039.png)  
Patient Inquiry button for a patient with a preferred name](#_Toc17877464)](#_Toc17877476)

[[If you select the Patient Inquiry button, the Patient Inquiry dialog appears. The Patient Inquiry dialog includes additional information such as the patient's mailing address, telephone numbers (including the patient's home, work, and cell phone numbers), admission information, and other relevant data, such as provider information (including the patient's mental health treatment coordinator (MHTC) contact information, displaying in two locations on the Patient Inquiry form) and primary and secondary next-of-kin entries. Caregiver information also displays (if available)—this includes the primary, secondary, and general caregiver(s) if they are present and considered active.](#_Toc17877464)](#_Toc17877476)

[[The Mental Health Treatment Coordinator is the liaison between the patient and the mental health system at a VA site. There is only one MHTC per patient, and the MHTC is the key coordinator for behavioral health services care. While in the detailed display, you can select a new patient, print the detailed display, or close the detailed display.](#_Toc17877464)](#_Toc17877476)

[[  
](#_Toc17877464)](#_Toc17877476)

[[The Patient Inquiry dialog also shows information that can be printed including demographic information, Permanent & Total Disabled status, and Health Benefit Plans currently assigned to the Veteran.  
](#_Toc17877464)](#_Toc17877476)

[[<span id="preferred_name_patient_inquiry_screen" class="anchor"></span>If a patient's preferred name has been entered into VistA, it will display in parentheses next to the patient's first name, as shown below:  
  
![](cprs-user-manual-gui-version-updated-or-3-0-499/042.png)](#_Toc17877464)](#_Toc17877476)

[[Patient Inquiry screen for a Patient with a Preferred Name](#_Toc17877464)](#_Toc17877476)

[[The preferred name will display only on the Patient Inquiry button and screen. It will not display on any other CPRS GUI screen or report.  
](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

[[If an encounter provider or location has not been assigned, CPRS will prompt you for this information when you try to enter progress notes, create orders, and perform other tasks.](#_Toc17877464)](#_Toc17877476)

[[To enter or change the Encounter provider, follow these steps:](#_Toc17877464)](#_Toc17877476)

1.  

> [[If you are already in the Provider & Location for Current Activities dialog skip to step 2. Otherwise, from any chart tab, click the Provider / Encounter box located in the top center portion of the dialog. Note: These instructions are written as if the user must select a provider. If the user making the selection is a provider, the user will be selected by default and the cursor will go to the New Visit tab if no visit is defined, or to the Clinic Appointments tab if one is defined. If the user is not a provider, the cursor will go to the Encounter Provider field so that the user can select the provider for the encounter.](#_Toc17877464)](#_Toc17877476)

2.  

> [[In the Encounter Provider list box, locate and select the provider for this encounter. Note: To help you distinguish between providers, CPRS displays their titles (if available). When two or more providers have identical names, CPRS also displays:](#_Toc17877464)](#_Toc17877476)

> [[o The service/section and site division (if any) associated with these providers; site divisions are displayed based on the following rules:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 

> [[When no division is listed for a provider, no division is displayed. If only one division is listed, this division is displayed. If the site has multiple divisions or more than one division is listed and one of these listed divisions is marked as Default, CPRS displays the division marked as Default. If more than one division is listed for a provider and none is marked as Default, CPRS does not display division information for this provider. o Providers who are listed in the New Person file as Visitors are screened out from the provider list. (These screened-out providers are listed as Visitors because their entries were created as a result of a Remote Data View.)](#_Toc17877464)](#_Toc17877476)

3.  
4.  
5.  
6.  
7.  

[[Improvements are coming to the display of provider and team information that users see on the Primary Care button and in the detailed display that the user can view by selecting the Primary Care button. This section will show the display as it currently is and how it will look after patch OR\*3.0\*387 (also referred to as PCMM Web) is full deployed. The patch deployment will be phased and may take up to a year.](#_Toc17877464)](#_Toc17877476)

[[When patch OR\*3.0\*387 is installed, users will immediately see changes in the Primary Care detailed display. Any changes to the items on the Primary Care button itself will be included in a later version of CPRS.](#_Toc17877464)](#_Toc17877476)

[[To the immediate right of the Visit Encounter button is the Primary Care button on which, for an inpatient, CPRS displays might display as many as six items of information if all are assigned to this patient:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

[[the Primary Care Management Module (PCMM) or primary care team (outpatient team) primary care provider or PCP (outpatient provider) the associate provider (outpatient provider) the (Inpatient) attending provider the (Inpatient) provider the mental health treatment coordinator (for both an inpatient or an outpatient) Definitions of different providers:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
- 

[[For outpatients, CPRS might display up to four items:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 

[[  
](#_Toc17877464)](#_Toc17877476)

[[When the OR\*3.0\*387 (also known as PCMM Web) is deployed, you will see changes in the Primary Care detailed display.](#_Toc17877464)](#_Toc17877476)

[[It is anticipated that there will be changes to the information displayed on the Primary Care button with the release of CPRS GUI v31b.](#_Toc17877464)](#_Toc17877476)

[[If the patient is not an inpatient, the inpatient information will not display. Inpatient information displays in the following format:](#_Toc17877464)](#_Toc17877476)

- 
- 

[[Primary Care Team information for an outpatient could include the following:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 

> [[Primary Care Provider: PCP Name, PCP Phone, Pager Associate Provider: AP Name, AP Phone, Pager Administrative POC: Team Role, Admin POC Name, Admin POC Phone, Pager Clinical POC: Team Role, Clinical POC Name, Clinical POC Phone, Pager Note: The Associate Provider will only display if one is explicitly assigned to the patient. If not, it will not display.](#_Toc17877464)](#_Toc17877476)

[[There are several messages that can display if information is missing. Here are a few items to consider:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 

[[Note: Any additional Non-VA Providers will be displayed here.  
Example Detailed Display Formats](#_Toc17877464)](#_Toc17877476)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><a href="#_Toc17877476"><span>PRIMARY CARE</span></a></p>
<p><a href="#_Toc17877476"><span>LOCAL – Station Name (#) or</span></a></p>
<p><a href="#_Toc17877476"><span>LOCAL – VAMC Station Name (#) || Station Name (#)</span></a></p>
<p><a href="#_Toc17877476"><span><strong>{</strong> Inpatient Attending: [Name]||PHONE: [Phone #]||PAGER: [Pager]</span></a></p>
<p><a href="#_Toc17877476"><span>Inpatient Provider: [Name]||PHONE: [Phone #]||PAGER: [Pager] <strong>}</strong></span></a></p>
<p><a href="#_Toc17877476"><span>PACT: {PENDING:} [Primary Care Team Name]</span></a></p>
<p><a href="#_Toc17877476"><span>Primary Care Provider: [PCP Name]||PHONE: [PCP Phone]||PAGER:</span></a></p>
<p><a href="#_Toc17877476"><span>[Pager]}</span></a></p>
<p><a href="#_Toc17877476"><span>Associate Provider: [AP Name]||PHONE: [AP Phone]||PAGER: [Pager]</span></a></p>
<p><a href="#_Toc17877476"><span>Administrative POC: [Team Role]||[Admin POC Name]||PHONE: [Admin POC Phone]||PAGER: [Pager]</span></a></p>
<p><a href="#_Toc17877476"><span>Clinical POC: [Team Role]||[Clinical POC Name]||PHONE: [Clinical POC Phone]||PAGER: [Pager]</span></a></p>
<p><a href="#_Toc17877476"><span>{LOCAL or REMOTE – Station Name (#)}</span></a></p>
<p><a href="#_Toc17877476"><span>MH: MH Treatment Team Name]</span></a></p>
<p><a href="#_Toc17877476"><span>(MHTC) [MH Treatment Role Name]||[MH Treatment Coordinator</span></a></p>
<p><a href="#_Toc17877476"><span>Name]||PHONE: [Phone]||PAGER: [Pager]</span></a></p>
<p><a href="#_Toc17877476"><span>{LOCAL or REMOTE – Station Name (#)}</span></a></p>
<p><a href="#_Toc17877476"><span>OEF/OIF/OND: [OEF/OIF/OND Team Name]</span></a></p>
<p><a href="#_Toc17877476"><span>LEAD COORDINATOR: [Lead Coordinator Name]||PHONE: [Phone]||PAGER: [Pager]</span></a></p>
<p><a href="#_Toc17877476"><span>{LOCAL or REMOTE – Station Name (#)}</span></a></p>
<p><a href="#_Toc17877476"><span>SP: [Specialty Team Name]</span></a></p>
<p><a href="#_Toc17877476"><span>[Team Role Name]||[ Team Member XXX Name]||PHONE: [Phone]||PAGER: [Pager]</span></a></p>
<p><a href="#_Toc17877476"><span>Non-VA: [Non-VA Role||Specialty Name]||[Provider Name]||PHONE: [Phone]||[City], [ST]</span></a></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

[[Note: If the provider has an NPI, it will not display on the screen above.  
](#_Toc17877464)](#_Toc17877476)

[[To help address <span id="OTH" class="anchor"></span>veterans with high risk for suicide, the VA provides two types of eligibility for former servicemembers with Other than Honorable (OTH) discharge types seeking mental health care:](#_Toc17877464)](#_Toc17877476)

- 
- 

> [[OTH-90 care type - Provides one or more 90-day episodes of care within a 365-day period for those who have an OTH discharge. OTH-EXT care type - Provides care with no time limit for those who have an OTH discharge.](#_Toc17877464)](#_Toc17877476)

> [[Note:  The OTH buttons will display only if patches DG\*5.3\*952 and DG\*5.3\*977 are installed and the necessary criteria are met. If the patches are not installed, the OTH button will not display.](#_Toc17877464)](#_Toc17877476)

> [[The OTH-EXT care type will display in the OTH button only if patch DG\*5.3\*977 is installed.  
> ](#_Toc17877464)](#_Toc17877476)

[[Note: Patch OR\*3.0\*546 introduces the ability to add a local message for OTH-90 patients. Messages are entered in VistA (Graphical User Interface (GUI) Parameters menu option) by Clinical Care Coordinators and are displayed in CPRS. The figure below is an example of the OTH-90 pop-up window with a local message.  
  
![](cprs-user-manual-gui-version-updated-or-3-0-499/051.png)  
  
  
To display the OTH popup window dialog box:](#_Toc17877464)](#_Toc17877476)

1.  
2.  

> [[Select the OTH button.After viewing the information, close the dialog by selecting the "OK" button.](#_Toc17877464)](#_Toc17877476)

[[Note: A tooltip provides detailed information.](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
1.  
3.  

> [[Select the OTH-EXT button.After viewing the information, close the dialog by selecting the "OK" button.](#_Toc17877464)](#_Toc17877476)

> [[Note: A tooltip provides detailed information.](#_Toc17877464)](#_Toc17877476)

- 

[[If the user hovers the mouse over the 'OTH-EXT' label on the button "Other Than Honorable, click for details" will be displayed.](#_Toc17877464)](#_Toc17877476)

[[Presumptive Psychosis (PP) patients are registered as Service Connected (less than 50%) Veterans with an Honorable or General discharge and who meet other PP workaround criteria. To identify these patients a PP button will display using the same real estate as the OTH button (left of the Flag button).](#_Toc17877464)](#_Toc17877476)

> [[Note: The PP button will display only if patches DG\*5.3\*1029 and OR\*3.0\*437 are installed *and* the necessary criteria are met. If the patches are not installed, the PP button will not display.](#_Toc17877464)](#_Toc17877476)

1.  
2.  
3.  

[[Authorized users (licensed prescribers and pharmacists) and delegates are able to access the PDMP query functionality.](#_Toc17877464)](#_Toc17877476)

[[The Prescription Drug-Monitoring Program (PDMP) enhancement to CPRS allows authorized users (prescribers and pharmacists) and licensed delegates to submit on demand PDMP queries for use in patient care related decision making when prescribing controlled substances to Veterans. The process allows the user to:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 

> [[View and retrieve controlled substance prescription monitoring data from external sources and within patients electronic medical recordsAutomatically generate patient progress notes Query and easily utilize prescription and patient prescription history on an ad-hoc and recurring basisPerform audit functions that ensure compliance.](#_Toc17877464)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/060.png)CPRS Cover Sheet displaying the PDMP Query Button](#_Toc17877464)](#_Toc17877476)

[[<span id="Hover_for_date" class="anchor"></span>Note: Hover over (put your cursor over) the PDMP Query button from the ribbon bar to display the last query completed date. The completed date is the date when the last STATE PRESCRIPTION DRUG MONITORING PROGRAM note was signed and completed). If a previous PDMP note was never completed for this patient, it will display "Last query completed: Unknown."](#_Toc17877464)](#_Toc17877476)

[[Authorized Prescribers (with a DEA \#) and Pharmacists (with an NPI \#) can initiate a PDMP query using their own credentials.](#_Toc17877464)](#_Toc17877476)

[[To request a PDMP Query, follow these steps:](#_Toc17877464)](#_Toc17877476)

1.  

[[From the ribbon bar, click on the PDMP Query button, it will change to PDMP Cancel. The query will run in the background, and the user can continue to work in CPRS while the query is running. After a few seconds, the PDMP Cancel button will change to PDMP Results.Note: You can also select PDMP from the Tools drop-down menu.](#_Toc17877464)](#_Toc17877476)

[[PDMP Query - requests the query](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/061.png)](#_Toc17877464)](#_Toc17877476)

> [[PDMP Cancel - indicates the query is in progress—clicking it cancels the query](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/062.png)](#_Toc17877464)](#_Toc17877476)

[[Note: Retrieving the results may take a while as the query searches all 50 states' databases (through a third party PDMP gateway). This process is outside of CPRS's control.](#_Toc17877464)](#_Toc17877476)

> [[PDMP Results - validates the query is completed](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/063.png)](#_Toc17877464)](#_Toc17877476)

2.  

[[Click on the PDMP Results button to display the PDMP report. The Prescription Drug Monitoring Program Results report displays in a separate window.Note: If encounter information has not been entered, the encounter information dialog will appear before the PDMP report is displayed. You must complete the encounter information dialog before proceeding.](#_Toc17877464)](#_Toc17877476)

[[Note: Retrieving the report may take a while as it must be retrieved through a third party PDMP gateway. This process is outside of CPRS's control.](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/064.png)](#_Toc17877464)](#_Toc17877476)

[[PDMP Results Report](#_Toc17877464)](#_Toc17877476)

> [[The report allows the user to review the PDMP results and to automatically generate a note to document any findings. It has three sections: Demographics, Summary, and Prescriptions. The bottom of the report displays the date of the last PDMP Query (which is the same date as the date previously noted in the [<u>hover over Note</u>](#Hover_for_date) for the PDMP Query), Four (4) statement selections, as well as the Cancel Without Update and Done and Create Note buttons.](#_Toc17877464)](#_Toc17877476)

[[Note: You must select at least one of the Statements. Clicking the Done and Create Note button without selecting a Statement, will produce the error message: "At least one option should be selected."](#_Toc17877464)](#_Toc17877476)

> [[Each of the four (4) Provider Statement selections is described below:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
3.  

> [[Prescription(s) filled outside the VA are noted and will be addressed as follows:Selecting this statement will produce a text box to enter comments of up to 250 characters (required) and the following Non-VA Meds reminder statement displays below the text box: "Please be sure to record any active/chronic medications discovered from PDMP query in the Non-VA Medications section of the Meds Tab in CPRS."Click the Done and Create Note button.A STATE PRESCRIPTION DRUG MONITORING PROGRAM progress note will automatically be created in the background. Click on the Notes tab at the bottom of the Cover Sheet to view the Progress Note with today's date.](#_Toc17877464)](#_Toc17877476)

[[Note: For a Progress Note example, refer to [Example of a Progress Note](#Example_of_Progress_Note) at the end of this section.](#_Toc17877464)](#_Toc17877476)

4.  

> [[Select the PDMP note. From the top menu, select Action, and click 'Sign Note Now.' The 'Sign Note Now' window displays.![](cprs-user-manual-gui-version-updated-or-3-0-499/065.png)](#_Toc17877464)](#_Toc17877476)

> [[Sign Note Now Window](#_Toc17877464)](#_Toc17877476)

5.  

[[If you are registered with the State PMP as a Delegate using your va.gov email address, you can run a query as a delegate of an authorized PDMP user.](#_Toc17877464)](#_Toc17877476)

[[To request a PDMP Query, follow these steps:](#_Toc17877464)](#_Toc17877476)

1.  
2.  

[[From the ribbon bar, click on the PDMP Query button.![](cprs-user-manual-gui-version-updated-or-3-0-499/067.png)You will be prompted to Select Authorized User from the pop-up dialog. The encounter provider (if they are an authorized PDMP user) is selected by default.![](cprs-user-manual-gui-version-updated-or-3-0-499/068.png)](#_Toc17877464)](#_Toc17877476)

> [[Select Authorized User](#_Toc17877464)](#_Toc17877476)

3.  

> [[Click Accept. PDMP Query changes to PDMP Cancel. The query will run in the background, and the user can continue to work in CPRS while the query is running. After a few seconds, the PDMP Cancel button will change to PDMP Results.PDMP Cancel - indicates the query is in progress—clicking it cancels the query](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/069.png)](#_Toc17877464)](#_Toc17877476)

[[Note: Retrieving the results may take a while as the query searches all 50 states' databases (through a third party PDMP gateway). This process is outside of CPRS's control.](#_Toc17877464)](#_Toc17877476)

> [[PDMP Results - validates the query is completed](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/070.png)](#_Toc17877464)](#_Toc17877476)

4.  

[[Click on the PDMP Results button to display the PDMP report. The Prescription Drug Monitoring Program Results report displays in a separate window.Note: If encounter information has not been entered, the encounter information dialog will appear before the PDMP report is displayed. You must complete the encounter information dialog before proceeding.](#_Toc17877464)](#_Toc17877476)

[[Note: Retrieving the report may take a while as it must be retrieved through a third party PDMP gateway. This process is outside of CPRS's control.](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/071.png)](#_Toc17877464)](#_Toc17877476)

> [[PDMP Results Report](#_Toc17877464)](#_Toc17877476)

> [[The report allows the user to review the PDMP results and to automatically generate a note to document any findings. The report has three sections: Demographics, Summary, and Prescriptions. The bottom of the report displays the date of the last PDMP Query (which is the same date as the date previously noted in the [<u>hover over Note</u>](#Hover_for_date) for the PDMP Query), Two (2) statement selections, as well as the Cancel Without Update and Done and Create Note buttons.](#_Toc17877464)](#_Toc17877476)

[[Note: You must select at least one of the Statements, clicking the Done and Create Note button without selecting a Statement, will produce the error message: "At least one option should be selected."](#_Toc17877464)](#_Toc17877476)

> [[Each of the two (2) Delegate Statement selections is described below:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
1.  

[[Prescription(s) that have been filled outside the VA in the last 90 days are noted.Selecting this statement will produce a text box to enter comments of up to 250 characters (optional) and the following Non-VA Meds reminder statement displays below the text box: "Please be sure to record any active/chronic medications discovered from PDMP query in the Non-VA Medications section of the Meds Tab in CPRS."Click the 'Done and Create Note button.' A STATE PRESCRIPTION DRUG MONITORING PROGRAM progress note will automatically be created in the background. Note: For a Progress Note example, refer to Example of a Progress Note at the end of this section.](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/072.png)](#_Toc17877464)](#_Toc17877476)

> [[Sign Note Now Window](#_Toc17877464)](#_Toc17877476)

2.  
- 
- 
- 
- 

[[The PDMP report will open automatically as soon as it is available.The report is opened as a modeless window, so that the report and reminder dialog template can be interacted with simultaneously.The radio buttons on the bottom of the report will not display and the 'STATE PRESCRIPTION DRUG MONITORING PROGRAM note will not automatically generate. Note: To ensure that the PDMP query is captured for compliance measurement, the site's CAC must ensure that the template is attached to the STATE PRESCRIPTION DRUG MONITORING PROGRAM note title. The template should contain the necessary field elements so that the user can record their findings from the report.The user may close the report either by selecting the 'Close' button, by closing the local reminder dialog template itself, or by selecting another patient.  
![](cprs-user-manual-gui-version-updated-or-3-0-499/074.png)](#_Toc17877464)](#_Toc17877476)

[[Example of a PDMP button in a Reminder Dialog Template](#_Toc17877464)](#_Toc17877476)

[[  
![](cprs-user-manual-gui-version-updated-or-3-0-499/075.png)](#_Toc17877464)](#_Toc17877476)

[[Example of a Report Generated by a PDMP Button in a Reminder Dialog Template](#_Toc17877464)](#_Toc17877476)

[[A PDMP Health Summary Report, PDMP AOD ALL, was created to generate a PDMP Accounting of Disclosure (AOD) report. This component lists the PDMP Accounting of Disclosures for instances where a PDMP query was initiated from within CPRS and patient's data was shared outside of the VA. It will also include cases where a PDMP note was manually created to document a PDMP query made directly on a state's PDMP portal.](#_Toc17877464)](#_Toc17877476)

[[Note: For more information, refer to [*<u>Viewing a Health Summary</u>*](#_Viewing_a_Health).](#_Toc17877464)](#_Toc17877476)

<span id="AOD_report_screenshot" class="anchor"></span>

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/076.png)](#_Toc17877464)](#_Toc17877476)

[[Example of an Accounting of Disclosure (AOD) report  
](#_Toc17877464)](#_Toc17877476)

[[Patient Record Flags are divided into types: Category I (national) and Category II (local). Category I Patient Record Flags are the most critical and are transmitted to all facilities, ensuring that these flags are universally available. Category II Patient Record Flags are local only, belonging only to the site that created them; they are not shared between sites.](#_Toc17877464)](#_Toc17877476)

[[CPRS has two Category I Patient Record Flags: a Behavioral flag for violent or potentially violent patients and a High Risk for Suicide flag. The Office of Information created the Behavioral flag to help VHA properly protect its employees and maintain a safe environment for health care–they also now contain information regarding Disruptive Behavior Reporting System Cases for the patient ('DBRS number' and 'Other DBRS data'). The High Risk for Suicide flag aims to identify patients who might be at higher risk of taking their own lives. The Office of Information defines and distributes Category I flags through national patches and the definition of the flag cannot be edited by local sites.](#_Toc17877464)](#_Toc17877476)

[[Each Category I flag assignment to a specific patient's record is owned by a single facility. The facility that placed the Category I flag on the patient's record would normally own and maintain the flag. The site that owns the Category I flag is the only site that can:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 

[[review whether to remove or continue the flag edit the flag inactivate the flag reactivate the flag mark the flag as entered in error change ownership of the flag Enter/edit DBRS data (only on a National Category I Behavioral flag) enter a Patient Record Flag Category I progress note for the flag However, ownership of a Category I flag assignment can be transferred. If a patient received the majority of care at a different VA facility than the one that assigned the flag, the site giving the majority of care could request that ownership of the flag be transferred to the that site. The owning site could then change the ownership to the second site through the PRF software in List Manager.](#_Toc17877464)](#_Toc17877476)

[[Category II flags are local. Each site can create and maintain its own set of local flags that are not transmitted to other sites. However, the purpose of Category II flags is similar to Category I—to provide important patient information to health care providers. For example, a site could create a Patient Record Flags Cat II – Diabetes flag or a Category II Infectious Disease flag.](#_Toc17877464)](#_Toc17877476)

[[In VHA Directive 2010-053, dated December 3, 2010, titled: *Patient Record Flags*, VHA advised sites to create and use Patient Record Flags sparingly so that users will notice flags and pay careful attention to them. Creating a large number of flags for many different reasons might lessen the impact of flags and cause staff to miss important information. Both Category I flags and Category II flags require a progress note to document the reason for placing a flag on the patient's record.](#_Toc17877464)](#_Toc17877476)

[[Some sites may have two different groups of users who work with Patient Record Flags: administrative users who create, maintain, and assign flags and the clinical users that document why the flag was placed on the patient's record. Authorized users can define Category II flags and edit their definitions. They assign and maintain the flag on a patient's record using the assignment actions in the PRF software through the List Manager interface: new assignment, continue, inactivate, mark as entered in error, and reactivate. (Additional documentation for PRF creation, assignment, and maintenance is available in the *Patient Record Flags User Guide*.)](#_Toc17877464)](#_Toc17877476)

[[Before users can write progress notes that document PRF, PRF progress note titles must be set up correctly. Each PRF progress note title must be associated with a specific flag definition, and users must be assigned to the appropriate user classes to write specific kinds of notes. Also, someone must have assigned the flag to the patient.](#_Toc17877464)](#_Toc17877476)

[[For users to write a progress note and correctly link the note to a flag action, sites must complete the following set up:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 
- 

[[Currently, there are two Category I flags: Behavioral and High Risk for Suicide. The Progress Note titles for documenting the two flags are:](#_Toc17877464)](#_Toc17877476)

- 
- 

[[Patient Record Flag Category I (for the Behavioral flag) Patient Record Flag Category I – High Risk for Suicide To help sites that will be creating local Category II flags, four partially customizable Progress Note titles have been distributed:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
- 

[[Patient Record Flag Category II – Risk, Fall Patient Record Flag Category II – Risk, Wandering Patient Record Flag Category II – Research Study Patient Record Flag Category II – Infectious Disease Clinical Application Coordinators (CACs) can customize these titles by changing the text after the dash using TIU utilities. For example, the first title could be changed from "Patient Record Flag Category II – Risk, Fall" to "Patient Record Flag Category II – Behavioral, Drug Seeking" or other titles sites create. CACs can also create their own titles, but the title must follow the naming convention "Patient Record Flag Category II – *other text*" where *other text* is the text specific to the local note title.](#_Toc17877464)](#_Toc17877476)

- 
- 
- 

[[Marking PRF as entered in error terminates the flag's display in the patient's record. However, if there was a progress note linked to the flag, the progress note is still in the patient's record. If the flag was entered in error, an authorized TIU user should retract or retract and reassign the linked progress note.](#_Toc17877464)](#_Toc17877476)

[[Note: Users should be aware that although the flag does not display, a history of this flag is kept in the Patient Record Flag software and users can reactivate the flag. To prevent users from entering notes on previous, inaccurate PRF actions, all previous PRF actions are hidden when a flag is marked as entered in error.](#_Toc17877464)](#_Toc17877476)

[[Patient Record Flags are displayed in the applications that use the patient look up, including the CPRS GUI. In the CPRS GUI, there are three places where users can see if a patient has PRF:](#_Toc17877464)](#_Toc17877476)

- 
- 
- 
1.  

> [[Select a patient from the Patient Selection screen by either double-clicking on a patient name or highlighting the name and pressing the \<Enter\> key. Note: When the record loads, CPRS checks to see if the record is sensitive and displays a warning to the user that the user must acknowledge to proceed. Then, if the record has one or more flags, CPRS displays a pop-up box with the patient's record flags title. The first flag is highlighted and the narrative details displayed below. If CPRS displays the pop-up box, the user must close this box before CPRS will load the patient chart.  
> ](#_Toc17877464)](#_Toc17877476)

2.  

> [[Then, select the Flag title to view the narrative by clicking the flag name or highlighting the flag name with the tab and arrow keys and pressing \<Tab\> (note that the number of flags in each category is listed after the category label). Note: If the provider has an NPI, it will not display on the screens below.](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/081.png)](#_Toc17877464)](#_Toc17877476)

> [[This graphic shows the Patient Record Flag pop-up box listing the patient's flags, the narrative for the highlighted flag, and the links to any signed, linked progress notes documenting the reasons for the flag. Using the Flag button or clicking on a flag title on the Cover Sheet also displays this pop-up box. Category I flags are in the orange field, they blink, and the text changes color from white to black and back. Category II flags are in the field below](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/082.png)](#_Toc17877464)](#_Toc17877476)

> [[This screen capture shows a Patient Record Flag dialog with associated Behavioral flag and Disruptive Behavior Reporting System information](#_Toc17877464)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen above.](#_Toc17877464)](#_Toc17877476)

3.  
4.  

[[To view the linked progress note, select the appropriate link in the lower part of the dialog. When finished, select Close. When finished viewing the narrative, close the narrative box by choosing Close or pressing \<Enter\>. To view a Patient Record Flag when already viewing a record, use the following steps:](#_Toc17877464)](#_Toc17877476)

1.  
2.  
3.  

[[Go the Cover Sheet by clicking the Cover Sheet tab or pressing Ctrl + S or use the Flag button by clicking Flag or pressing tab until you highlight the Flag button and press \<Enter\>. Select the flag title to see the narrative details by clicking the title or using the Up and Down arrows to highlight the name and pressing \<Enter\>. When finished, close the box by clicking Close or pressing \<Enter\>.](#_Toc17877464)](#_Toc17877476)

1.  

> [[Select a patient from the Patient Selection screen by either double-clicking on a patient name or highlighting the name and pressing the \<Enter\> key. Note: When the record loads, CPRS checks to see if the record is sensitive and displays a warning to the user that the user must acknowledge to proceed. Then, if the record has one or more flags, CPRS displays a pop-up box with the patient's record flags title. The first flag is highlighted and the narrative details displayed below. If CPRS displays the pop-up box, the user must close this box before CPRS will load the patient chart.  
> ](#_Toc17877464)](#_Toc17877476)

2.  

> [[Then, select the Flag title to view the narrative by clicking the flag name or highlighting the flag name with the tab and arrow keys and pressing \<Tab\> (note that the number of flags in each category is listed after the category label). Note: If the provider has an NPI, it will not display on the screens below.](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/088.png)](#_Toc17877464)](#_Toc17877476)

> [[This graphic shows the Patient Record Flag pop-up box listing the patient's flags, the narrative for the highlighted flag, and the links to any signed, linked progress notes documenting the reasons for the flag. Using the Flag button or clicking on a flag title on the Cover Sheet also displays this pop-up box. Category I flags are in the orange field, they blink, and the text changes color from white to black and back. Category II flags are in the field below](#_Toc17877464)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/089.png)](#_Toc17877464)](#_Toc17877476)

> [[This screen capture shows a Patient Record Flag dialog with associated Behavioral flag and Disruptive Behavior Reporting System information](#_Toc17877464)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen above.](#_Toc17877464)](#_Toc17877476)

3.  
4.  

[[To view the linked progress note, select the appropriate link in the lower part of the dialog. When finished, select Close. When finished viewing the narrative, close the narrative box by choosing Close or pressing \<Enter\>. To view a Patient Record Flag when already viewing a record, use the following steps:](#_Toc17877464)](#_Toc17877476)

1.  
2.  
3.  

[[Users may view Inactive PRF History for Patients who have an Inactive Flag assignment. The Inactive Flag displays only for the following National Category 1 (one) flags:](#_Toc17877464)](#_Toc17877476)

- 
- 

| [[Field Name](#_Toc17877464)](#_Toc17877476)          | [[Description](#_Toc17877464)](#_Toc17877476)                                                                          |
|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [[Flag Name](#_Toc17877464)](#_Toc17877476)               | [[This field identifies flag assignment for High Risk for Suicide or Missing Patient only.](#_Toc17877464)](#_Toc17877476) |
| [[Initial Assignment Date](#_Toc17877464)](#_Toc17877476) | [[Date and time stamp of the initial flag assignment.](#_Toc17877464)](#_Toc17877476)                                      |
| [[Originating Site](#_Toc17877464)](#_Toc17877476)        | [[Identifies the site who initiated the flag assignment](#_Toc17877464)](#_Toc17877476)                                    |
| [[Owner Site](#_Toc17877464)](#_Toc17877476)              | [[Identifies the site who owns the flag assignment](#_Toc17877464)](#_Toc17877476)                                         |

[[Flag Assignment actions are organized by the site. Actions displayed are: Inactivate, Reactivate, and Continue with the date/time stamp of the action in descending order (newest to oldest). Since there is not a scroll bar on the patient chart pop-up, when there are more actions available than can be displayed, users will see the following disclaimer: *\*\*\*Additional information is in VistA\*\*\](#_Toc17877464)](#_Toc17877476)

[[To view Inactive Flag History for PP or OTH Patients, follow the steps below:](#_Toc17877464)](#_Toc17877476)

1.  
2.  
3.  
4.  

[[Locate/Search for PatientNavigate to OTH or PP/Inactive Flag buttonClick on OTH or PP/Inactive Flag buttonReview OTH/PP eligibility and Inactive Flag History. \*Note: OTH-90 button label only displays when the patient has an inactive flag; otherwise, button label reads OTH with the number of days remaining.](#_Toc17877464)](#_Toc17877476)

[[If the Remote Data button is blue, other facilities have data for the current patient  
What Does the List of Sites Represent?](#_Toc17877604)](#_Toc17877476)

[[If you click the Remote Data button, a drop-down list appears with the name(s) of sites where the patient has been seen. This list is based on either:](#_Toc17877604)](#_Toc17877476)

- 
- 

[[Sites that have been specifically designated for your facility to access. These sites are assigned in a parameter that your Clinical Applications Coordinator (CAC) can set up. All sites where the patient has been seen and HDR and Department of Defense remote data if it is available. What Kind of Data Can I View?](#_Toc17877604)](#_Toc17877476)

[[Currently with CPRS, you can view some lab and health summary components. There are limitations to what you can view.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
1.  
2.  
3.  
4.  
5.  

> [[After opening the patient's record, see if the text on the Remote Data button is blue. If the text is blue, the patient has remote data. Select the tab you want remote data from (e.g. Labs or Reports). Select the Remote Data button to display a list of sites that have remote data for the patient. Select the sites you want to view remote data from by selecting the check box in front of the site name or select All and select the Remote Data button again to close the list. Select the report or lab you would like to view from the Available Reports or Lab Results section on the left side of the screen (click the "+" sign in order to expand a report heading).Note: With the exception of the DoD Consults report, choosing a Department of Defense (DoD) report does not limit you to DoD data. For example, if you choose Microbiology under Dept. of Defense, you will get DoD data and remote VAMC data. You do not have to run a separate report to get VA data.](#_Toc17877604)](#_Toc17877476)

> [[It may take a few minutes to retrieve the data. While CPRS retrieves the data, the message "Transmission in Progress" is displayed.](#_Toc17877604)](#_Toc17877476)

> [[Depending on how the report or lab is configured, CPRS will return the remote data in one of two ways.](#_Toc17877604)](#_Toc17877476)

- 

> [[Text Format with Site Tabs If the remote data is in text format, the data from each remote site will be displayed under a separate site tab. To view data from a particular site, select the appropriate tab.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/095.png)](#_Toc17877604)](#_Toc17877476)

> [[Site tabs organize remote data from different sites](#_Toc17877604)](#_Toc17877476)

- 

> [[Table format If the report or lab is available in table format, CPRS will return data from all of the sites in a single table. The "facility" column indicates where the data in a particular row was collected. The table can be sorted by facility or by any other column heading (alphabetically, numerically, or by date) by selecting the appropriate heading. Selecting the heading again will sort the table in inverse order.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/096.png)](#_Toc17877604)](#_Toc17877476)

> [[Remote data is displayed in a table format](#_Toc17877604)](#_Toc17877476)

> [[6. To see detailed information about a particular item in the table, click that item. If detailed information is available, it will be displayed in the bottom half of the screen. To select multiple rows, press and hold the Shift or Control key.](#_Toc17877604)](#_Toc17877476)

> [[If you click the button, you will see a tree view of the patient's reminders such as the one shown below. The icons that appear on the Reminders button are also used in the tree view to identify the various types of reminders.](#_Toc17877604)](#_Toc17877476)

[[The Icon Legend  
](#_Toc17877604)](#_Toc17877476)

[[Postings contain critical patient-related information about which hospital staffs need to be aware. The Postings button is visible on all tabs of the CPRS GUI window and is always located in the upper right corner of the window](#_Toc17877604)](#_Toc17877476)

[[If a patient record contains postings, the Postings button displays one or more of the following letters: C, W, A,D, P, and L. These letters correspond to the six types of postings described below.](#_Toc17877604)](#_Toc17877476)

- 

> [[C (Crisis Notes) – Cautionary information about critical behavior or patient health. Example: Suicidal attempts or threats.](#_Toc17877604)](#_Toc17877476)

- 

> [[W (Warnings) – Notifications that inform medical center staff about possible risks associated with patients. Example: Patient can be violent.](#_Toc17877604)](#_Toc17877476)

- 
- 

> [[A (Adverse Reactions/Allergies) – Posting that displays information about medications, foods, and other items to which patients are allergic or to which they may have an adverse reaction. CPRS creates these postings automatically when users enter allergies.D (Directives) – Also called advanced directives, directives are recorded agreements that a patient and/or family have made with the clinical staff.Example: DNR (Do Not Resuscitate) directive on file.](#_Toc17877604)](#_Toc17877476)

- 
- 

> [[P (Pregnant) – Indicates that the patient is currently pregnant.L (Lactating) – Indicates that the patient is currently lactating or nursing.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/105.png)](#_Toc17877604)](#_Toc17877476)

> [[The Postings button](#_Toc17877604)](#_Toc17877476)

[[CPRS offers two ways to View a posting. You can view a posting by clicking the Postings button from any chart tab, or you can select a specific posting from the Cover Sheet tab.](#_Toc17877604)](#_Toc17877476)

[[To view a posting by using the Postings button, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select the Postings button or select View \| Postings from the Cover Sheet tab. The Patient Postings dialog appears. The Patient Postings dialog contains all postings for the selected patient. The postings are divided into two categories. Allergies are listed in the top half of the dialog and crisis notes, warning notes, and directives are listed in the bottom half.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/106.png)](#_Toc17877604)](#_Toc17877476)

> [[The Patient Postings dialog](#_Toc17877604)](#_Toc17877476)

1.  [[Select a posting to see a detailed explanation.](#_Toc17877604)](#_Toc17877476)

[[CPRS displays a new window that contains the full text of the posting.](#_Toc17877604)](#_Toc17877476)

2.  [[When you are finished reading the posting, select Close.](#_Toc17877604)](#_Toc17877476)

[[To view a specific posting from the Cover Sheet, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select a posting from the Postings or Allergies / Adverse Reactions area of the Cover Sheet. CPRS displays a new window that contains the full text of the posting.](#_Toc17877604)](#_Toc17877476)

2.  

[[When you are finished reading the posting, select Close.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[The messages will be pulled from the function finding found text in the reminder definition linked to the banner. These messages will change as the reminder definition is updated. The status document will be found on the following page:](#_Toc17877604)](#_Toc17877476)

[[REDACTED](#_Toc17877604)](#_Toc17877476)

[[There are three error messages that users could see instead of a status.](#_Toc17877604)](#_Toc17877476)

- [[Non-existent patient](#_Toc17877604)](#_Toc17877476)
- [[No reminder definition is defined](#_Toc17877604)](#_Toc17877476)
- [[Reminder evaluation failure, status: \<error text\>](#_Toc17877604)](#_Toc17877476)

[[If you see one of these error messages, please record the patient name and call the help desk for assistance.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[CPRS graphing uses different representations for different types of items. Following is a brief discussion of selected items and their corresponding representations.](#_Toc17877604)](#_Toc17877476)

[[Admissions and Visits: CPRS graphing displays visits and admissions on the horizontal (date/time) axis as lines or bars that indicate the duration of the visits and admissions. Bars representing hospital admissions begin at the date and time of admission and end at the date and time of discharge. Visit representations begin at the appointment date and time and end at the date and time of the visit's end. Because visit durations are often short, visit representations are typically vertical lines, rather than bars. When visit durations are unavailable, CPRS graphing uses its default duration of one hour.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/108.png)](#_Toc17877604)](#_Toc17877476)

[[Events: CPRS graphing displays as single events all items that are not laboratory tests, vitals measurements, medications (inpatient, non-VA, or outpatient), or visits. Like representations for admissions and visits, representations for single events use only the horizontal axis. CPRS graphing uses triangle shaped representations to mark these items. (Color, shape, and height differentiate item markers.) It graphs administration times for BCMA medications as events.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/109.png)](#_Toc17877604)](#_Toc17877476)

[[Medications: As it does with admissions and visits, CPRS graphing displays medications as bars that indicate a period of time. In the case of outpatient medications, bars begin on the horizontal axis at the release date of the medications. End dates are based on the following calculation: medication release date + number of days' supply = end date. For inpatient and non-VA medications, bars begin at medication start times and dates and end at medication stop times and dates. In the case of non-VA medications, if no stop date exists, CPRS graphing uses the current date as the stop date.](#_Toc17877604)](#_Toc17877476)

> [[CPRS graphing differentiates multiple medications by color and vertically offsets them to ensure the visibility of overlapping bars.](#_Toc17877604)](#_Toc17877476)

[[Important: Healthcare professionals have no reliable way to determine whether patients do or do not take their outpatient medications. Use caution when graphing relationships between outpatient medications and other items.](#_Toc17877604)](#_Toc17877476)

[[Vitals: CPRS graphing displays vitals measurements as points on two axes. If more than one measurement exists for a given date and time, CPRS graphing connects measurements for like items with a line.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/110.png)](#_Toc17877604)](#_Toc17877476)

[[Labs: CPRS graphing also displays as points on two axes laboratory tests that have results with numerical values. Lines connect like items.](#_Toc17877604)](#_Toc17877476)

> [[CPRS graphing displays lab tests with non-numerical results (positive and negative results, for example) as points on the horizontal axis. It does not connect like items that have non-numerical results. To keep them out of the way of numerical data, CPRS graphing displays non-numerical results above or below the numerical values and line. Values beginning with \> are located at the top margin; others are graphed at the bottom margin. Free-text values display by default as do comments. To hide or show free-text values, click on the "free-text values:" label. Comments are displayed in yellow boxes on the date axis, while the \*\*comments label shows that there are comments. Clicking this label will show details of all items on the graph.](#_Toc17877604)](#_Toc17877476)

> [[CPRS graphing includes reference ranges in graphs of laboratory test results. Reference ranges are displayed as dashed horizontal lines.](#_Toc17877604)](#_Toc17877476)

> [[A lab test from different specimens or having different reference ranges will display in separate graphs with the appropriate reference range. If the Merge Labs setting is used then the lab tests will be graphed as a single test (with a warning that different reference ranges are present).](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/111.png)](#_Toc17877604)](#_Toc17877476)

[[The following sections explain how to:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

[[CPRS displays its graphing functionality as a detached window or a group of panes embedded within the Reports tab. (CPRS supports one detached instance of the graphing window and one Reports-tab instance per session.)You can resize and move the detached window, which enables you to set up graphs as a reference that you can view as you navigate your patient's chart in CPRS](#_Toc17877604)](#_Toc17877476)

[[You can start CPRS graphing in any of the following ways:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[From any tab: click Tools on the main menu and then click Graphing. CPRS displays the detached graphing window. From any tab: simultaneously press the \<Ctrl\> and \<G\> keys. CPRS displays the detached graphing window. On the Reports tab: click Graphing (local only) under Available Reports. CPRS displays embedded graphing panes. On the Labs tab: click Graph under Lab Results. CPRS displays the detached graphing window. On the Labs tab: click Most Recent under Lab Results and then click on any test displaying lab results.  
](#_Toc17877604)](#_Toc17877476)

[[CPRS graphing offers many options for selecting and displaying graphed data. For example, you can:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[Select a date range Create, edit, delete, and rename predefined views (personal or public)—or save collections of items for reuse Display individual or multiple items in a single graph Display graphs in one single or two separate panes Use the Graph Settings dialog box to specify data sources and display options Following are instructions for using these options to create customized graphs.](#_Toc17877604)](#_Toc17877476)

[[You can set several display options directly from the main window, including the following options:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[Select Date Range… in the Date Range list. This sets the date range for the current view.Keep in mind the following information when selecting a new date range:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[Each graph in the display area (or split-pane areas) can include one or multiple items.](#_Toc17877604)](#_Toc17877476)

[[To create graphs that include only one item on each set of axes:](#_Toc17877604)](#_Toc17877476)

- 

[[Select the Individual Graphs checkbox (located in the upper left-hand section of the main graphing display). To create graphs that include multiple items on each set of axes:](#_Toc17877604)](#_Toc17877476)

- 

[[Cancel the selection of the Individual Graphs checkbox. While you can graph one or more vitals and lab measurements on the same set of axes, you cannot graph vitals and lab measurements on a set of axes that includes other types of items.  
](#_Toc17877604)](#_Toc17877476)

[[CPRS graphing offers a split-pane display that enables you to create separate graphs in the top and bottom panes. Each pane includes its own Individual Graphs check box, View tab, and Item tab.](#_Toc17877604)](#_Toc17877476)

[[To create a split-pane display:](#_Toc17877604)](#_Toc17877476)

- 

[[Select the Split Views check box located in the lower left-hand section of the main window.To return to a single-pane display:](#_Toc17877604)](#_Toc17877476)

- 

[[Take the following steps to resize panes and item-selection columns:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[CPRS graphing provides predefined graphs through its View tab, which is located in the upper left-hand pane of the main window. This tab includes all predefined views from the following sources:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[Public views you or others—your site's IRM staff, for example—have created. (Only authorized users can create public views.) Private views you have created. Personal Lab Groups that you have created. These lab groups are defined in the Lab Worksheet report.Users can now also access other users' personal views and lab groups that they have defined to build new views. Users with proper authority can save personal views as public views by simply renaming and saving as a public view. Users can also save public views as a personal view and then alter it to suit their personal preferences.](#_Toc17877604)](#_Toc17877476)

[[To display view definition, users do this:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Highlight the view name. Select View Definition from the pop-up menu. The definition with them display in a pane below View list.](#_Toc17877604)](#_Toc17877476)

[[Take the following steps to create new views:](#_Toc17877604)](#_Toc17877476)

1.  1.  1.  

> [[Access the Define Views or Select Items and Define Views dialog box using one of the following four methods: On the CPRS main menu, click Tools and then click Options. CPRS displays the Options dialog box. On the Graphs tab, click View Definitions. CPRS displays the Define Views dialog box. -or-](#_Toc17877604)](#_Toc17877476)

2.  

> [[Click Select/Define on the right-click menu from the graphing window. CPRS displays the Select Items and Define Views dialog box. -or-](#_Toc17877604)](#_Toc17877476)

3.  

> [[Click Select/Define at the bottom of the graphing window. CPRS displays the Select Items and Define Views dialog box. -or-](#_Toc17877604)](#_Toc17877476)

4.  1.  
3.  [[On the CPRS Reports tab, click Graphing (local only) in the Available Reports list. CPRS displays embedded graphing functionality. Click the Select/Define button. CPRS displays the Select Items and Define Views dialog box.Select All Items in the Select Items using area located at the top of the dialog.](#_Toc17877604)](#_Toc17877476)
4.  [[Select a data source from the Source list. CPRS displays in the Items list all items associated with this source.](#_Toc17877604)](#_Toc17877476)
5.  [[If you know you want to include all items, double-click the source to add it—and its associated items—to the Items for Graphing list. You can also add all items for the source by clicking the ![](cprs-user-manual-gui-version-updated-or-3-0-499/115.png) button.](#_Toc17877604)](#_Toc17877476)

> [[-or-](#_Toc17877604)](#_Toc17877476)

> [[Double-click individual items you want to add to the Items for Graphing list. You can also select individual items by highlighting them and then clicking the \> button.](#_Toc17877604)](#_Toc17877476)

> [[Other tips for adding items to the Items for Graphing list:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
6.  [[Select Drug Class in the Source list to make available for selection *all* drugs (inpatient, outpatient, non-VA, and BCMA). Select Medication, BCMA; Medication, Inpatient; Medication, Outpatient; or Medication, Non-VA to display only medications for these sources. For example, if you want to select a specific outpatient medication, click Medication, Outpatient and then add the medication to the Items for Graphing list. In the Source list, Anatomic Pathology and Microbiology include sub sources. When you select the primary sources (Anatomic Pathology or Microbiology), CPRS graphing displays their sub sources in its Items list. If you add to the Items for Graphing list sub sources from the Items list, you automatically add all items associated with the sub sources. To add individual items associated with sub sources, select the sub sources from the Source list. CPRS moves all selected items to the Items for Graphing list. If you select duplicate items from different sources, CPRS merges the duplicate items when you add them to the Items for Graphing list.(Optional) You can remove items from the Items for Graphing list by double-clicking them. You can also use the \< button or the \<\< button to remove items.](#_Toc17877604)](#_Toc17877476)
7.  [[Repeat steps 2–5 until you have selected all items that you want to include in your view.](#_Toc17877604)](#_Toc17877476)
8.  [[Select Save Personal to save these items in a personal view or, if you are authorized to do so, click Save Public to save the items in a view that is available to all users.](#_Toc17877604)](#_Toc17877476)
9.  [[In the Save your Personal View or Save this Public View dialog box, type a name for your new view. CPRS saves view names in all capital letters and displays them using title caps. Therefore, you cannot use capitalization schemes to save different views that have the same name. You must give each view a new name unless you plan to overwrite an existing view.](#_Toc17877604)](#_Toc17877476)
10. [[Select OK.](#_Toc17877604)](#_Toc17877476)

[[Your view is now available on the Source list in the Select/Define and Select Items and Define Views dialog boxes. It is also available on the View list.](#_Toc17877604)](#_Toc17877476)

[[Take the following steps to edit predefined views:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
9.  

[[Take the following steps to delete predefined views:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

[[Take the following steps to rename a predefined view:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
1.  
2.  
3.  
4.  
5.  

> [[1. Select the Settings button located on the bottom bar of the main window.](#_Toc17877604)](#_Toc17877476)

> [[-or-](#_Toc17877604)](#_Toc17877476)

> [[Select Settings on the right-click menu.](#_Toc17877604)](#_Toc17877476)

> [[-or-](#_Toc17877604)](#_Toc17877476)

[[You can specify which sources CPRS graphing uses to display items by taking the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[To save changes for future CPRS sessions:](#_Toc17877604)](#_Toc17877476)

> [[• Select the Personal or Public buttons in the Save as Default area. You can save settings as public defaults only if you are authorized to do so.](#_Toc17877604)](#_Toc17877476)

[[CPRS applies defaults only after you close and subsequently restart CPRS. When you do this, CPRS applies your personal default settings. It applies public default settings only if you have not saved personal default settings.](#_Toc17877604)](#_Toc17877476)

[[You can create graphs from the main window and from the Select Items and Define Views dialog box.](#_Toc17877604)](#_Toc17877476)

- 

[[In the Item or View list, click the item or view you want to graph.To graph multiple items, take the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

[[CPRS graphing automatically scales graphs to fit the pane. However, you can resize the main window, or resize the pane. (See "Resizing Panes and Item-Selection Columns" on p.113 of this manual.)](#_Toc17877604)](#_Toc17877476)

> [[To split numerical items in your graph from event-based items:](#_Toc17877604)](#_Toc17877476)

- 

[[Select Split Numerics/Events on the right-click or popup menu.](#_Toc17877604)](#_Toc17877476)

> [[To reverse your split-screen view:](#_Toc17877604)](#_Toc17877476)

- 

[[Select Swap on the right-click or popup menu.](#_Toc17877604)](#_Toc17877476)

> [[To move a particular item from the bottom to the top of a split-pane view, or vice-versa, or to separate a particular item from a multiple-item graph:](#_Toc17877604)](#_Toc17877476)

- 

[[Point to the item and select Move on the right-click or popup menu. If you are separating an item from a single-pane view, CPRS graphing automatically displays the item in the bottom pane of a split-pane view.](#_Toc17877604)](#_Toc17877476)

> [[To move all items from the top to the bottom pane of a split view, or vice-versa:](#_Toc17877604)](#_Toc17877476)

- 

[[Point to an unpopulated area of the pane containing the graphs you want to move and select Move from the right-click menu.](#_Toc17877604)](#_Toc17877476)

> [[To remove a graphed item:](#_Toc17877604)](#_Toc17877476)

- 

[[Point to the item and select the Remove selection on the right-click menu.](#_Toc17877604)](#_Toc17877476)

> [[To remove all graphed items:](#_Toc17877604)](#_Toc17877476)

- 

[[Point to an unpopulated area of the pane from which you want to remove all graphed items and select the Remove selection from the right-click menu.](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select Patient Items in the Select Items using area located at the top of the dialog.Select a source from the Source list. If the patient you've selected has items from this data source, CPRS displays the items under the source's name in the Items list. Otherwise, it displays only the source's name.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  

[[Double-click individual items you want to include in the Items for Graphing list. You can also add items to this list by using the \> and \> buttons. (The \> button adds individual items to the Items for Graphing list, and the \> button adds all items.)(Optional) Use the \< and \<\< button to remove items from the Items for Graphing list. You can also double-click items on this list to remove them.Repeat steps 2–4 as necessary to add items from additional sources. Select Close and Display.CPRS displays the resulting graph (or graphs) in the main window. (See "Adjusting the Display" on p.121 of this manual for information about adjusting this display.) It also displays graphed items (selected and sorted at the top) in the Item list and the temporary view in the View list. Temporary views are available for creating subsequent graphs only during the current CPRS session.](#_Toc17877604)](#_Toc17877476)

[[CPRS graphing offers several options for displaying details associated with graphed items. The following list describes these options.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

> [[Hints: If you have selected Hints in the Graph Settings dialog box, hover hints containing summary information appear when you point to graphed items. Values: If you have selected Values in the Graph Settings dialog box—or if you've selected Values on the right-click menu—CPRS graphing displays informational labels for each graphed item. Display details: When you click on a graphed item, CPRS graphing displays details associated with the item. Click on legend: When you click on a graph's legend, CPRS graphing displays a limited-data listing for all items that appear on the legend. Display point details on right-click menu: CPRS graphing displays all results associated with specific types of points when you right-click on the points and then click Details. For example, if you right-click on a point that represents a vitals measurement for the selected patient—his body temperature on July 24, 2000, say—and then click Details, CPRS graphing displays the results of all vitals measurements entered for July 24, 2000.](#_Toc17877604)](#_Toc17877476)

- 

[[Display all details via the right-click menu: CPRS graphing displays details for all graphed items when you when you right-click on an unpopulated area of the graph and then click Details on the right-click menu.  
](#_Toc17877604)](#_Toc17877476)

[[CPRS graphing's zoom feature provides a way to visually expand areas of interest. To enable this feature for the horizontal axis, select the Zoom, Horizontal checkbox in the Graph Settings dialog box. To simultaneously expand areas of interest along the vertical axis, select Zoom, Vertical in the Graph Settings dialog box or Vertical Zoom on the right-click menu.](#_Toc17877604)](#_Toc17877476)

[[Take the following steps to visually expand areas of interest:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

[[Point to the upper left-hand corner of the area you want to visually expand. Click and hold the left mouse button. Drag the mouse pointer downward and to the right until you have described the entire area of interest. Release the mouse button. CPRS graphing expands the horizontal and (if applicable) vertical axes of all graphs accordingly. In its information bar, CPRS graphing displays the new (zoomed) date range. (Optional) Repeat steps 1–3 as needed to further expand the area of interest.](#_Toc17877604)](#_Toc17877476)

[[To instantly return all graphs to their original state:](#_Toc17877604)](#_Toc17877476)

- 

[[Select Reset Display on the right-click menu. Alternately, you can return all graphs to their original state by taking the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

[[Point to any area on a graph. Click and hold the left mouse button. Drag the mouse pointer upward and to the left. Release the mouse button.](#_Toc17877604)](#_Toc17877476)

[[To step backward through the zoom process (reverse the process by increments):](#_Toc17877604)](#_Toc17877476)

- 

[[Select Zoom Back on the right-click menu. (When you've stepped backward through the entire zoom process, this menu selection is unavailable.)](#_Toc17877604)](#_Toc17877476)

[[The graphing tool relies on Microsoft Word's copy, paste, and print features. If Word is not installed on your machine; these features are not available for you to use.](#_Toc17877604)](#_Toc17877476)

[[To copy all of the graphs in the main window—including graphs that lie outside your scrolled view:](#_Toc17877604)](#_Toc17877476)

- 

[[Select Copy on the right-click menu.](#_Toc17877604)](#_Toc17877476)

[[To paste copied graphs into any application that accepts copied images from the system clipboard:](#_Toc17877604)](#_Toc17877476)

- 
- 

[[Select Print on the right-click menu.](#_Toc17877604)](#_Toc17877476)

> [[• After the selected data has been displayed in a graph, select File \| Export Data.](#_Toc17877604)](#_Toc17877476)

[[Excel will then be launched and the data from the graph will be displayed in the spreadsheet.  
](#_Toc17877604)](#_Toc17877476)

[[CPRS now has two types of signatures: electronic and digital. Electronic signatures, which have been available for some time, require an electronic signature code that can be created at your site. Digital signatures in CPRS are now required to comply with new Drug Enforcement Agency's (DEA) regulations for identifying a prescriber that orders outpatient controlled substances.](#_Toc17877604)](#_Toc17877476)

[[There are three different levels of keys that influence what can be done with orders, including which dialog CPRS brings up when signing orders. Although actual practice at each site may vary, the three levels are usually referred to in these ways:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[OREMAS is the clerk key ORELSE is the nurse key ORES is the provider key In CPRS, users who hold the ORES key have additional privileges and are sometimes required to enter more information than those who hold the ORELSE or OREMAS key. ORES key holders (usually an ordering provider) must enter information regarding service connection, environmental conditions or specific treatment factors, such as ionizing radiation, Agent Orange, etc.](#_Toc17877604)](#_Toc17877476)

[[This section describes the differences between electronic and digital signatures, gives an overview of service connection and treatment factors, and then gives the steps for the various ways users will sign orders. For example, users can sign orders several different ways:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[Review / Sign Changes…enables users to sign all orders from the current ordering session. Using this method, the user could write a number of orders and create documents and then sign all items at the same time. Sign selected…enables users to highlight one or more orders and then sign them. When the dialog displays, only the selected orders or documents will display for signature. Select New Patient brings up the signature dialog that includes all unsigned orders for the current patient before opening another patient record. The orders are broken into three groups, the user's orders from this ordering session, the user's unsigned orders for the patient from previous ordering sessions, and unsigned orders for the patient written by other users. The user can then select and deselect the orders to be signed. Exiting the chart (closing CPRS) brings up the same dialog as selecting a new patient (see above). CPRS provides three methods for signing orders and documents. You can sign orders and documents together from the Review / Sign Changes dialog or you can sign orders and documents separately using the Sign Selected Orders and Sign Documents Now commands.](#_Toc17877604)](#_Toc17877476)

> [[By completing the two-factor authentication protocol at this time, you are legally signing the prescription(s) and authorizing the transmission of the above information to the pharmacy for dispersing. The two-factor authentication protocol may only be completed by the practitioner whose name and DEA registration number appear above.  
> ](#_Toc17877604)](#_Toc17877476)

[[CPRS displays order information in several places where users will be able to see that an outpatient controlled substance order was digitally signed.](#_Toc17877604)](#_Toc17877476)

- 

> [[Cover Sheet: If the order has been digitally signed, the detailed order display from right-clicking the order on the Cover Sheet where it currently shows "Elec Signature:" will show "Dig Signature:" Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/118.png)](#_Toc17877604)](#_Toc17877476)

> [[This graphic is a detailed display of an order on the CPRS Cover Sheet. Note the text change from "Elec. Signature," to "Dig Signature"  
> ](#_Toc17877604)](#_Toc17877476)

- 

> [[Orders Tab and Meds Tab: If the order has been digitally signed, the detailed order display from right-clicking the order on the Orders tab or from selecting it and choosing Details from the View menu where it currently shows "Elec Signature:" will show "Dig Signature:"Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/119.png)](#_Toc17877604)](#_Toc17877476)

> [[The above graphic shows the detailed display of an order off the Meds or Orders tab. The text has been changed from "Elec Signature," to "Dig Signature"](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[Upon electronic signature, providers will need to deal with the various exemptions for copayment for qualified veterans. To help providers better understand service connection and treatment factors, the following information is provided.](#_Toc17877604)](#_Toc17877476)

[[The provider must make a clinical decision to determine if an encounter is for a SC condition or one of a number of special categories. If the veteran is being treated during the encounter for a condition that the provider believes is for SC or a special category, the provider should check "Yes" next to the appropriate category on the encounter form. The veteran will not be billed for the encounter if "Yes" is checked. Medication(s) for one of these conditions should be indicated during the outpatient medication ordering process. The veteran will not be charged a copayment for a medication that is for SC or a special category.](#_Toc17877604)](#_Toc17877476)

[[The Special Categories included are:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 

[[Combat Veteran (CV) Agent Orange (AO)Ionizing Radiation (IR) Southwest Asia Conditions (SWAC) – includes Gulf War veterans Shipboard Hazard and Defense (SHD) Military Sexual Trauma (MST) Head and Neck Cancer (HNC), after nasopharyngeal radium treatment in service.](#_Toc17877604)](#_Toc17877476)

[[To qualify for the Combat Veteran (CV) exemption, the veteran must have served in combat operations after the Gulf War or in combat against a hostile force after November 11, 1998. In addition, the condition for which the veteran is treated must be related to that combat, the veteran must have registered as a combat veteran, and be within two years of separation from active military service. Finally, the condition must not be already considered to be service related or that exemption should apply.](#_Toc17877604)](#_Toc17877476)

[[Note: The Combat Veteran exemption is valid for two years from the date of separation from military service, not the registration date. For example, if a veteran registers for Combat Veteran status 18 months after the date of his or her separation, the veteran would be eligible for Combat Veteran exemption for six months only. For further details, see VHA Directive 2002049, Combat Veterans Are Eligible for Medical Services for 2-Years after Separation from Military Service Notwithstanding Lack of Evidence for Service Connection.](#_Toc17877604)](#_Toc17877476)

[[To help users better identify Combat Veteran eligible patients so that appropriate care and prioritization occur for them, CPRS has added several items where Combat Veteran status is more clearly shown. This is especially true in Consults. These markers are shown in various places in CPRS, such as the Patient Selection screen, the buttons available from any tab, the Consults dialog and details, the SF-513 form, etc.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

> [[Patient Selection Screen: When the user selects a patient with Combat Veteran status, CPRS indicates that patient is a combat veteran by displaying the letters CV and a date below the normal demographic information on the Patient Selection screen and above the Save Patient List Settings button. The marker is shown in the screen capture below surrounded by a red box.  
> <span id="Notification_combat_veteran" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/121.png)  

> New Service Consult/Request Notifications: The lower portion of the Patient Selection screen is the list of notifications for the user that is logged in. For a new consult or procedure request for a veteran with Combat Veteran status, the letters CV and the date display behind the abbreviated patient identifier in the Patient column. The Combat Veteran notification marker is shown in the above screen capture outlined in red. Combat Veteran Button and Consult Details: Available from any CPRS tab, the Combat Veteran button displays the letters CV and the expiration date of Combat Veteran status. The Button displays when the selected patient has Combat Veteran status. The button shares space with the Flag button. The Combat Veteran button only displays for patients with the status, otherwise, the Flag button is whole. To get details, the user selects the button to display the Combat Veteran Details dialog. See *Combat Veteran Details Dialog* below. When the user selects the consults from the tree view, the consults details show in the pane to the right. In this view, the Combat Veteran status is shown underneath the primary eligibility.Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/122.png)](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

> [[Combat Veteran Details Dialog: When the user selects the Combat Veteran button, the Combat Veteran Details dialog displays with the following items: Service Branch Status Separation Date Expiration Date OEF/OIF (If the patient served in Operation Enduring Freedom (OEF) or Operation Iraqi Freedom (OIF) ![](cprs-user-manual-gui-version-updated-or-3-0-499/123.png)  
> ](#_Toc17877604)](#_Toc17877476)

- 

> [[Consult Order Dialog: The Combat Veteran status and expiration date display near the top of the Consult Order dialog. Note: If the provider has an NPI, it will display on the screen below. See the "National Provider Identifier (NPI) Display in CPRS" section for an example of an NPI displaying on a screen.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/124.png)  
> ](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

> [[SF-513 Form: Several changes were made to this form: At the top of the page on the SF-513, the Combat Veteran marker displays with the demographic information. The patient's name was moved to the top of this form. When printed, the patient's identifying information will be printed at the top of each page. When printed, a page number will be printed at the bottom of each page. Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/125.png)](#_Toc17877604)](#_Toc17877476)

[[Agent Orange (AO) is an herbicide that was used in Vietnam between 1962 and 1971 to remove unwanted plant life that provided cover for enemy forces. The VA has recognized the following conditions as associated with but not necessarily caused by exposure to Agent Orange:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- [[AL Amylodosis Diabetes (type 2) Chloracne or other acne form disease consistent with chloracne (must occur within one year of exposure to AO). Ischemic Heart Disease Parkinson's Disease Porphyria cutanea tarda (must occur within one year of exposure to AO). Acute and subacute peripheral neuropathy. (For purposes of this section, the term acute and subacute peripheral neuropathy means temporary peripheral neuropathy that appears within weeks or months of exposure to an herbicide agent and resolves within two years of the date of onset.) Numerous cancers: Prostate cancer](#_Toc17877604)](#_Toc17877476)
- [[Hodgkin's disease.](#_Toc17877604)](#_Toc17877476)
- [[Multiple myeloma.](#_Toc17877604)](#_Toc17877476)
- [[Non-Hodgkin's lymphoma.](#_Toc17877604)](#_Toc17877476)
- [[Respiratory cancers (cancer of the lung, bronchus, larynx, or trachea). (Must occur within 30 years of exposure to Agent Orange.)](#_Toc17877604)](#_Toc17877476)
- [[Soft-tissue sarcoma (other than osteosarcoma, chondrosarcoma, Kaposi's sarcoma, or mesothelioma).](#_Toc17877604)](#_Toc17877476)
- [[Chronic lymphocytic leukemia](#_Toc17877604)](#_Toc17877476)

[[Atomic veterans may have been exposed to ionizing radiation in a variety of ways at various locations. Veterans exposed at a nuclear device testing site (the Pacific Islands, e.g., Bikini, NM, NV, etc.) or in Hiroshima and/or Nagasaki, Japan, may be included. Atomic veterans with exposure to ionizing radiation are entitled to receive treatment for conditions for this exposure. VA has recognized the following conditions by statute or regulation as being associated with radiation exposure:](#_Toc17877604)](#_Toc17877476)

[[Conditions Associated with Ionizing Radiation:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[All cancers/malignancies Posterior subcapsular cataracts Non-malignant thyroid nodular disease Parathyroid adenoma Tumors of the brain and central nervous systemNote: Atomic veterans do not have to receive an Ionizing Radiation Registry Exam to have these special treatment eligibilities.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Veterans with conditions recognized by VA as associated with Project 112/ SHAD, shipboard and land-based biological and chemical testing conducted by the United States (U.S.) military between 1962 and 1973 are eligible for enrollment in priority group 6, unless eligible for enrollment in a higher priority. In addition, veterans receive care at no charge for care and medications provided for treatment of conditions related to exposure.](#_Toc17877604)](#_Toc17877476)

[[VA is authorized by law to provide counseling services to women and men veterans who experienced incidents of sexual trauma while they served on active duty in the military. This Law defines a sexual trauma as sexual harassment, sexual assault, rape and other acts of violence. It further defines sexual harassment as repeated unsolicited, verbal or physical contact of a sexual nature, which is threatening in nature.](#_Toc17877604)](#_Toc17877476)

[[The provider must make a clinical decision to determine if a visit or medication is for MST. If the veteran is being treated for any condition during this episode of care that the provider believes is for MST; the visit should be checked as related on the encounter form and the medication should be designated as for MST. This will mean that the veteran does not have to pay a copayment for the visit or the medication.](#_Toc17877604)](#_Toc17877476)

[[From the 1950s to the 1980s, people living or working at the U.S. Marine Corps Base Camp Lejeune (CL), NC, were exposed to drinking water contaminated with industrial solvents, benzene, and other chemicals. Veterans and family members who served on active duty or resided at Camp Lejeune for 30 days or more between Aug. 1, 1953 and Dec. 31, 1987 may be eligible for VA health benefits for 15 conditions:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Esophageal cancer Breast cancer Kidney cancer Multiple myeloma Renal toxicity Female infertility Scleroderma Non-Hodgkin's lymphoma Lung cancer Bladder cancer Leukemia Myelodysplastic syndromes Hepatic steatosis Miscarriage Neurobehavioral effects On August 6, 2012, President Obama signed into law the "Honoring America's Veterans and Caring for Camp Lejeune Families Act of 2012" (P. L. 112-154). This law provides health care for Veterans who served on active duty at Camp Lejeune and reimbursement for health care to family members who resided at Camp Lejeune for not fewer than 30 days between August 1, 1953 and December 31, 1987. The law authorizes care for 15 medical conditions, even if there is insufficient medical evidence to conclude that such illnesses or conditions are attributable to the Veterans' military service or family members' residence at Camp Lejeune.](#_Toc17877604)](#_Toc17877476)

[[Note: The Camp Lejeune environmental indicator will not be available until the release of patch OR\*3.0\*407.](#_Toc17877604)](#_Toc17877476)

- 
- 

[[Associate all of the orders with a single location by selecting the appropriate button above the list of orders. The buttons will read All location where location is the name of the clinic or ward location. In the above screen capture the buttons read All MICU and All Mental Health Clinic. Individually associate each order with one of the two locations. At the end of each order is a column to select the location for each order. If the user is keeping the patient's chart open, such as selecting File \| Review / Sign changes… and this dialog appears, the "Where would you like to continue processing patient data?" prompt displays enabling the user to choose either the ward location or the clinic location. This prompt does not appear if the user is exiting the chart or switching patients.  
](#_Toc17877604)](#_Toc17877476)

[[To sign orders and documents with the Review / Sign Changes dialog, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  - 
    - 
    - 
2.  

> [[Do one of the following:Select File \| Review / Sign Changes.... to sign orders or documents and stay in the current patient record. Choose File \| Select New Patient to sign orders or documents and select a new patient. Choose File \| Exit to sign orders and documents and exit CPRS. (Conditional) This step will only be necessary if CPRS displays order checks similar to what is shown below: <span id="RevSign_Order_Checks_Screenshot" class="anchor"></span>  
> ![](cprs-user-manual-gui-version-updated-or-3-0-499/127.png)](#_Toc17877604)](#_Toc17877476)

> [[In this screen capture, CPRS displays a conflict between ordered medications. Users should review each item carefully before completing the order. Each order that has a high-level order check requires you to select that order and an override reason for it. All orders with an "Action is required" status require an override reason in order to be signed. These order checks are designated by the "\*Checks marked with \*\*\*\* require reason to override" text in red and the order check text in blue. The Accept button will not activate until all orders have been viewed, and all override reasons have been entered as needed.](#_Toc17877604)](#_Toc17877476)

> [[If CPRS displays order checks, carefully review the order checks and take the appropriate action below:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[To redo the orders to avoid a possible interaction, select Return to Orders. This will cancel the signature process, but not the order. If the orders should not be placed, check the cancel check box in front of the orders that should not be placed and select Cancel Checked Order(s). If the possible interactions are not a problem, type a reason for override if necessary (required only for some order checks) and select Continue.After performing step 1 and addressing any order checks in step 2, one of the Review/Sign Changes dialogs shown below will appear. Each item that requires a signature will have a check box in front of it.](#_Toc17877604)](#_Toc17877476)

> [[Note: All non-controlled substances orders will be checked for signature when the dialog displays. To sign controlled substances orders, the user must check the box for each order individually.](#_Toc17877604)](#_Toc17877476)

> [[<span id="Nature_of_Order_Review_sign" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/128.png)](#_Toc17877604)](#_Toc17877476)

> [[Figure A: This is for providers that can sign orders by policy, such as nurses or clerks. Note that the default method for release to service can be set by the site to Verbal, Telephone, or Policy. Or the site can leave the default blank forcing the user to select the method.](#_Toc17877604)](#_Toc17877476)

> [[  
> Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/129.png)](#_Toc17877604)](#_Toc17877476)

> [[Figure B: The Review/Sign changes dialog may have additional elements depending on the nature of the patient. In this case, the provider can sign controlled substances orders and the patient's conditions are not service-connected](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/130.png)](#_Toc17877604)](#_Toc17877476)

> [[Figure C: In this example of the Review/Sign Changes dialog, the provider can sign controlled substance orders, and the patient has either Combat Veteran status or service-connected conditions for which the provider must indicate the orders pertain](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[Deselect any items under the All Orders Except Controlled Substance Orders pane that you do not want to sign by clicking the check box to the left of the order or document. If the Review / Sign Changes dialog resembles Figure A, enter your electronic signature code and click Sign. The documents and orders will now be signed. If the Review / Sign Changes dialog resembles Figure B or Figure C and contains question marks, continue to step 5.](#_Toc17877604)](#_Toc17877476)

5.  

> [[To select Controlled Substance order to sign, place a check mark in the box to the left each Controlled Substance order to sign by clicking in the check box, or tabbing to it and pressing the \<Space bar\>. Note: When the user checks the box to the left of any Controlled Substance order for signature, the phrase "SMART card required" displays next to the label Controlled Substance Orders.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screens below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/131.png)](#_Toc17877604)](#_Toc17877476)

> [[This is what the dialog looks like before controlled substance outpatient orders are checked for signature.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/132.png)](#_Toc17877604)](#_Toc17877476)

> [[After the controlled substances orders are checked, the "smart card required" text and the text the provider must acknowledge display](#_Toc17877604)](#_Toc17877476)

6.  

> [[The question marks inside the boxes in Figure B indicate that you need to specify how that order is related to the medical condition in that column. (SC = Service Connected Condition, CV=Combat Veteran, AO=Agent Orange Exposure, IR=Ionizing Radiation Exposure, SWAC=Southwest Asia Conditions, SHD=Shipboard Hazard and Defense, MST=Military Sexual Trauma, and HNC=Head or Neck Cancer). If you place a check in a box, you are indicating that a medication order is related to the condition in that column. If you create an empty box, you are indicating that the medication order is not related to the condition in that column. You must either check or uncheck every box that contains a question mark before you can sign the order. Note: Definitions for service connection and treatment factors are available to users by hovering the cursor over the term or using the appropriate keyboard shortcut as shown in the list below:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 

> [[Service connection (SC) ......................... Alt + c Combat Veteran (CV) ............................. Alt + v Agent Orange (AO) ................................. Alt + o Ionizing Radiation (IR) ............................ Alt + r Southwest Asia Conditions (SWAC) ....... Alt + a Shipboard Hazard and Defense (SHD) .. Alt + h Military Sexual Trauma (MST) ................ Alt + m Head and/or Neck Cancer (HNC) ........... Alt + n You can toggle the check boxes by:](#_Toc17877604)](#_Toc17877476)

- 

> [[Clicking an individual check box. This will toggle the box between checked and unchecked.](#_Toc17877604)](#_Toc17877476)

- 

> [[Pressing the appropriate Copay button ( ![](cprs-user-manual-gui-version-updated-or-3-0-499/133.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/134.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/135.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/136.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/137.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/138.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/139.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/140.png) )](#_Toc17877604)](#_Toc17877476)

> [[This will toggle all the check boxes in that column.](#_Toc17877604)](#_Toc17877476)

- 

> [[Pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/141.png) button. This will toggle all the check boxes on the screen.](#_Toc17877604)](#_Toc17877476)

7.  

> [[If you have not already done so, insert your PIV or smart card. Note: If you do not insert your PIV or smart card before attempting to sign the selected Controlled Substance orders, you will see the following two dialogs:](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/142.png)](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/143.png)](#_Toc17877604)](#_Toc17877476)

8.  
9.  

> [[When you have removed all of the question marks from the dialog, enter your electronic signature code (the button will change from Don't Sign to Sign) and click Sign. (Conditional) If your PIV card is already set up, you will not see the Digital Signing Setup dialog and you can proceed to step 10. If your PIV or Smart card is not yet linked to your VistA account, you will need to set it up before you can sign outpatient controlled substance medication orders. To set up your PIV card to order outpatient controlled substance orders, select Yes. Note: If the provider has an NPI, it will not display on the screens below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/144.png)](#_Toc17877604)](#_Toc17877476)

> [[You may then be asked to enter your PIN](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/145.png)](#_Toc17877604)](#_Toc17877476)

> [[Then, the signature process will proceed](#_Toc17877604)](#_Toc17877476)

10. 
11. 

> [[If the Order Check dialog appears, deal with any problems in the dialog: such as entering a reason for override, cancelling specific orders, etc. When ready, select the Accept Orders button. When prompted, enter your PIN to sign the Controlled Substance orders and select OK or press \<Enter\>. ![](cprs-user-manual-gui-version-updated-or-3-0-499/146.png)](#_Toc17877604)](#_Toc17877476)

> [[Warning: Do NOT enter an incorrect PIN five (5) consecutive times! If you enter the incorrect PIN five (5) consecutive times, your card will be until you visit a PIV issuing station.](#_Toc17877604)](#_Toc17877476)

> [[If you enter the incorrect PIN three (3) times, CPRS temporarily locks your PIV card for 15 minutes. Then, it will allow you to try again. However, you only have two (2) more attempts to get the correct PIN. If you get to five (5) consecutive incorrect PIN entries, the PIV card will be locked and you will have to go to a PIV station to unlock the card.](#_Toc17877604)](#_Toc17877476)

- 
- 

[[Associate All of the orders with a single location by selecting the appropriate button above the list of orders. The buttons will read All *location* where location is the name of the clinic or ward location. In the above screen capture, the buttons read All MICU and All Mental Health Clinic. Individually associate each order with one of the two locations. At the end of each order is a column to select the location for each order.If the user is keeping the patient's chart open, such as selecting File \| Review / Sign changes… and this dialog appears, the "Where would you like to continue processing patient data?" prompt displays enabling the user to choose either the ward location or the clinic location. This prompt does not appear if the user is exiting the chart or switching patients.](#_Toc17877604)](#_Toc17877476)

[[To sign a number of orders, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. Highlight the orders you want to sign. To select a range of items, click the order at the beginning of the range; then hold down the \<Shift\> key and click the order at the end of the range. To select multiple, individual orders, select the first order, hold down the CTRL key, and click the next order.](#_Toc17877604)](#_Toc17877476)

3.  

[[Select Action \| Sign Selected… -or-](#_Toc17877604)](#_Toc17877476)

[[right-click and select Sign…](#_Toc17877604)](#_Toc17877476)

4.  

[[(Conditional) This step will only be necessary if CPRS displays order checks similar to what is shown below:  
<span id="RevSign_Order_Checks_Screenshot2" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/148.png)](#_Toc17877604)](#_Toc17877476)

[[In this screen capture, CPRS displays a conflict between ordered medications. Users should review each item carefully before completing the order. Each order that has a high-level order check requires you to select that order and select an override reason for it. All orders with an "Action is required" status require an override reason in order to be signed. These order checks are designated by the "\*Checks marked with \*\*\*\* require reason for override" text in red and the order check text in blue. The Accept button will not activate until all orders have been viewed, and all override reasons have been entered as needed.](#_Toc17877604)](#_Toc17877476)

5.  
1.  
2.  
3.  

[[If CPRS displays order checks, carefully review the order checks and take the appropriate action below: To redo the orders to avoid a possible interaction, select Return to Orders. This will cancel the signature process, but not the order. If the orders should not be placed, check the cancel check box in front of the orders that should not be placed and select Cancel Checked Order(s). If the possible interactions are not a problem, type a reason for override if necessary (required only for some order checks) and select Continue. After performing step 1 and addressing any order checks in step 2, one of the Review/Sign Changes dialogs shown below will appear. Each item that requires a signature will have a check box in front of it.](#_Toc17877604)](#_Toc17877476)

[[Note: All non-controlled substances orders will be checked for signature when the dialog displays. To sign controlled substances orders, the user must check the box for each order individually.](#_Toc17877604)](#_Toc17877476)

> [[<span id="Nature_of_Order_Sign_Selected" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/149.png)](#_Toc17877604)](#_Toc17877476)

> [[Figure A: This is for providers that can sign orders by policy, such as nurses or clerks. Note that the default method for release to service can be set by the site to Verbal, Telephone, or Policy. Or the site can leave the default blank forcing the user to select the method.](#_Toc17877604)](#_Toc17877476)

[[Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

6.  

[[If the Electronic Signature dialog resembles Figure A, enter your electronic signature code (if necessary) and select Sign. The orders will now be signed. If the Electronic Signature dialog resembles Figure B or Figure C and contains blue question marks, continue to step 6.](#_Toc17877604)](#_Toc17877476)

1.  [[To select Controlled Substance order to sign, place a check mark in the box to the left each Controlled Substance order to sign by clicking in the check box, or tabbing to it and pressing the \<Space bar\>.](#_Toc17877604)](#_Toc17877476)
7.  

[[The question marks inside the boxes in Figure B indicate that you need to specify how that order is related to the medical condition in that column. (SC = Service Connected Condition, CV=Combat Veteran, AO=Agent Orange Exposure, IR=Ionizing Radiation Exposure, Southwest Asia Conditions (SWAC), Shipboard Hazard and Defense (SHD), MST=Military Sexual Trauma, and HNC=Head and/or Neck Cancer). If you place a check in a box, you are indicating that a medication order is related to the condition in that column. If you create an empty box, you are indicating that the medication order is not related to the condition in that column. You must either check or uncheck every *box that contains a question mark before you can sign the order.*Note: Definitions for service connection and treatment factors are available to users by hovering the cursor over the term or using the appropriate keyboard shortcut as shown in the list below:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 

[[Service connection (SC) ......................... Alt + c Combat Veteran (CV) ............................. Alt + v Agent Orange (AO) ................................. Alt + o Ionizing Radiation (IR) ............................ Alt + r Southwest Asia Conditions (SWAC) ....... Alt + a Shipboard Hazard and Defense (SHD) .. Alt + h Military Sexual Trauma (MST) ................ Alt + m Head and/or Neck Cancer (HNC) ........... Alt + n You can toggle the check boxes by:](#_Toc17877604)](#_Toc17877476)

- 

> [[Clicking an individual check box. This will toggle the box between checked and unchecked.](#_Toc17877604)](#_Toc17877476)

- 

> [[Pressing the appropriate Copay button. (![](cprs-user-manual-gui-version-updated-or-3-0-499/154.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/155.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/156.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/157.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/158.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/159.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/160.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/161.png))](#_Toc17877604)](#_Toc17877476)

> [[This will toggle all the check boxes in that column.](#_Toc17877604)](#_Toc17877476)

- 

> [[Pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/162.png) button. This will toggle all the check boxes on the screen.](#_Toc17877604)](#_Toc17877476)

8.  

[[To select Controlled Substance order to sign, place a check mark in the box to the left each Controlled Substance order to sign by clicking in the check box, or tabbing to it and pressing the \<Space bar\>. Note: When the user checks the box to the left of any Controlled Substance order for signature, the phrase "SMART card required" displays next to the label Controlled Substance Orders.](#_Toc17877604)](#_Toc17877476)

9.  
10. 
11. 
2.  [[When you have removed all of the question marks from the dialog, enter your electronic signature code (the button will change from Don't Sign to Sign) and click Sign. (Conditional) If your PIV card is already set up, you will not see the Digital Signing Setup dialog and you can proceed to step 11. If your PIV or Smart card is not yet linked to your VistA account, you will need to set it up before you can sign outpatient controlled substance medication orders. To set up your PIV card to order outpatient controlled substance orders, select Yes. Note: If the provider has an NPI, it will not display on the screens below.](#_Toc17877604)](#_Toc17877476)
12. 

[[If the Order Check dialog appears, deal with any problems in the dialog: such as entering a reason for override, cancelling specific orders, etc. When ready, select the Accept Orders button.  
](#_Toc17877604)](#_Toc17877476)

13. 

[[Whenever a user leaves a patient chart whether to select a new patient or to exit CPRS completely, CPRS prompts the user to sign unsigned orders that the user has privileges to sign. The dialog that CPRS displays may be different than the Review/Sign Changes… or Sign Selected dialogs based on the parameter settings. By changing the parameters settings, the dialog may display one or more of the following categories of unsigned orders:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[My Unsigned Orders - This Session My Unsigned Orders - Previous Sessions Others' Unsigned Orders - All Sessions Sometimes during the ordering process, the status of a patient changes from outpatient to inpatient or vice versa. This might happen because an outpatient was admitted to the facility or because an inpatient was sent to a clinic for treatment. When written unsigned orders exist and the patient's status changes, the user must indicate which location the orders are associated with.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

- 
- 

[[Associate All of the orders with a single location by selecting the appropriate button above the list of orders. The buttons will read All *location* where location is the name of the clinic or ward location. In the above screen capture the buttons read All MICU and All Mental Health Clinic. Individually associate each order with one of the two locations. At the end of each order is a column to select the location for each order.If the user selects File \| Review / Sign changes… and this dialog appears, the "Where would you like to continue processing patient data?" prompt displays enabling the user to choose either the ward location or the clinic location. This prompt does not appear if the user is exiting the chart or switching patients.](#_Toc17877604)](#_Toc17877476)

[[To sign a number of orders, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. Highlight the orders you want to sign. To select a range of items, click the order at the beginning of the range; then hold down the \<Shift\> key and click the order at the end of the range. To select multiple, individual orders, select the first order, hold down the CTRL key, and click the next order.](#_Toc17877604)](#_Toc17877476)

3.  

[[Select Action \| Sign Selected… -or-](#_Toc17877604)](#_Toc17877476)

[[right-click and select Sign…](#_Toc17877604)](#_Toc17877476)

4.  

[[(Conditional) This step will only be necessary if there are conflicts with the orders, as shown below: <span id="RevSign_Order_Checks_Screenshot3" class="anchor"></span>  
![](cprs-user-manual-gui-version-updated-or-3-0-499/169.png)](#_Toc17877604)](#_Toc17877476)

[[In this screen capture, CPRS displays conflicts between ordered medications. Users should review each item carefully before completing the order. If an order check is larger than the cell's available space, the user can either hover with the mouse to the get the full text, use the arrow keys to highlight the order check if using the keyboard or use an accessibility product for the visually challenged. Some order checks require an override reason. These order checks are designated by the "\*Order Check requires Reason for Override" text in red and the order check text in blue.](#_Toc17877604)](#_Toc17877476)

[[If CPRS displays order checks, carefully review the order checks and take the appropriate action below:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[<span id="Nature_of_Order_Sign_before_exit" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/170.png)](#_Toc17877604)](#_Toc17877476)

> [[Figure A: This is for providers that can sign orders by policy, such as nurses or clerks. Note that the default method for release to service can be set by the site to Verbal, Telephone, or Policy. Or the site can leave the default blank forcing the user to select the method.](#_Toc17877604)](#_Toc17877476)

5.  
6.  
7.  

[[The question marks inside the check boxes in Figure B indicate that you need to specify how that order is related to the medical condition in that column. (SC = Service Connected Condition, CV=Combat Veteran, AO=Agent Orange Exposure, IR=Ionizing Radiation Exposure, Southwest Asia Conditions (SWAC), Shipboard Hazard and Defense (SHD), MST=Military Sexual Trauma, and HNC=Head and/or Neck Cancer). If you place a check in a box, you are indicating that a medication order is related to the condition in that column. If you create an empty box, you are indicating that the medication order is not related to the condition in that column. You must either check or uncheck every box that contains a question mark before you can sign the order. Note: Definitions for service connection and treatment factors are available to users by hovering the cursor over the term or using the appropriate keyboard shortcut as shown in the list below:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 

[[Service connection (SC) ......................... Alt + c Combat Veteran (CV) ............................. Alt + v Agent Orange (AO) ................................. Alt + o Ionizing Radiation (IR) ............................ Alt + r Southwest Asia Conditions (SWAC) ....... Alt + a Shipboard Hazard and Defense (SHD) .. Alt + h Military Sexual Trauma (MST) ................ Alt + m Head and/or Neck Cancer (HNC) ........... Alt + n You can toggle the check boxes by:](#_Toc17877604)](#_Toc17877476)

- 

[[Clicking an individual check box. This will toggle the box between checked and unchecked.](#_Toc17877604)](#_Toc17877476)

- 

> [[Pressing the appropriate Copay button. (![](cprs-user-manual-gui-version-updated-or-3-0-499/175.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/176.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/177.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/178.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/179.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/180.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/181.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/182.png))](#_Toc17877604)](#_Toc17877476)

[[This will toggle all the check boxes in that column.](#_Toc17877604)](#_Toc17877476)

- 

[[Pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/183.png) button. This will toggle all the check boxes on the screen.](#_Toc17877604)](#_Toc17877476)

3.  [[To select Controlled Substance order to sign, place a check mark in the box to the left each Controlled Substance order to sign by clicking in the check box, or tabbing to it and pressing the \<Space bar\>.](#_Toc17877604)](#_Toc17877476)

[[Note: When the user checks the box to the left of any Controlled Substance order for signature, the phrase SMART card required displays next to the label Controlled Substance Orders.](#_Toc17877604)](#_Toc17877476)

4.  [[If you have not already done so, insert your PIV or smart card.](#_Toc17877604)](#_Toc17877476)
8.  
9.  
10. 

[[The Review/Sign Changes dialog may contain the service connection and treatment factor (formerly called the "Copay") buttons (![](cprs-user-manual-gui-version-updated-or-3-0-499/189.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/190.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/191.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/192.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/193.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/194.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/195.png)![](cprs-user-manual-gui-version-updated-or-3-0-499/196.png) ) if the current patient has outpatient medication orders that need to be signed and certain additional conditions are met. The additional conditions are explained below.](#_Toc17877604)](#_Toc17877476)

[[Note: These buttons will not display until after December 31, 2001 and PSO\*7\*71 is released and installed.](#_Toc17877604)](#_Toc17877476)

- 

> [[To qualify for the Combat Veteran (CV) exemption, the veteran must have served in combat operations after the Gulf War or in combat against a hostile force after November 11, 1998. In addition, the condition for which the veteran is treated must be related to that combat, the veteran must have registered as a combat veteran, and be within two years of separation from active military service. Finally, the condition must not be already considered to be service related or that exemption should apply. Note: The Combat Veteran exemption is valid for two years from the date of separation from military service, not the registration date. For example, if a veteran registers for Combat Veteran status 18 months after the date of his or her separation, the veteran would be eligible for Combat Veteran exemption for six months only. For further details, see *VHA Directive 2002-049, Combat Veterans Are Eligible for Medical Services for 2-Years after Separation from Military Service Notwithstanding Lack of Evidence for Service Connection*. If a patient is a veteran *and* 50% service connected *or greater,* then the Copay buttons will not be displayed on the Review / Sign Changes dialog.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

> [[If a patient is a veteran *and* 50% service connected *or greater,* then the Copay buttons will not be displayed on the Review / Sign Changes dialog. If a patient is a veteran *and* less than 50% service connected *and* the patient is exempt from copay then the Copay buttons will not be displayed. If a patient is a veteran *and* less than 50% service connected, *and* the patient is *not exempt* from copay then the Pharmacy package checks to see if the drug specified in the medication order is marked as supply or investigational. If the drug is marked as supply or investigational, the Copay buttons will not appear. However, if the drug specified in the order is not marked as supply or investigational, then CPRS checks if the patient has any other exemptions (Service Connected Condition, Combat Veteran, Agent Orange Exposure, Ionizing Radiation Exposure, Southwest Asia Conditions, Shipboard Hazard and Defense, Head and/or Neck Cancer or Military Sexual Trauma). If a patient has any of these exemptions, then CPRS displays the buttons.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Notes or DC/Summ tab. Select the note or discharge summary that you would like to sign. Select Action \| Sign Note Now (or Sign Discharge Summary Now). -or-](#_Toc17877604)](#_Toc17877476)

> [[right-click in the document area and select Sign Note Now (or Sign Discharge Summary Now).](#_Toc17877604)](#_Toc17877476)

4.  
5.  

[[With the Add to Signature List command, you can place notes or discharge summaries for the same patient on a list where you can simultaneously sign them.](#_Toc17877604)](#_Toc17877476)

[[To add a note or discharge summary to your signature list, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Click the Notes or DC/Summ tab. Select the note or discharge summary that you would like to add to your signature list. Choose Action \| Add to Signature List. The note or discharge summary will be added to your signature list. To sign all of the notes or discharge summaries on your signature list select File \| Review / Sign Changes.](#_Toc17877604)](#_Toc17877476)

[[With the View Unsigned Notes or View Unsigned Discharge Summaries command you can view all the notes and discharge summaries that you have not yet signed.](#_Toc17877604)](#_Toc17877476)

[[To view unsigned notes or discharge summaries, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Click the Notes or DC/Summ tab. Select either View \| Unsigned Notes, View \| Uncosigned Notes, View \| Unsigned Summaries or View \| Uncosigned Summaries. The unsigned notes or discharge summaries will appear in the detail portion of the window.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Notes or DC/Summ tab. Select a signed note or discharge summary. Select Action \| Identify Additional Signers -or-](#_Toc17877604)](#_Toc17877476)

> [[right-click in the main text area and select Identify Additional Signers.](#_Toc17877604)](#_Toc17877476)

4.  

> [[To identify a signer, locate the person's name (scroll or type in the first few letters of the last name) and click it. Note: For a Discharge Summary, if a user requires a cosigner (such as a student or other type of clinician), that user's name should not appear in the list of potential cosigners. Additionally, for all types of documents, to help users distinguish between providers, CPRS displays their titles (if available). When two or more providers have identical names, CPRS also displays:](#_Toc17877604)](#_Toc17877476)

- - 
  - 
  - 
  - 
- 
5.  
6.  
7.  

[[You can print most reports, notes, and detailed displays from within the CPRS GUI.](#_Toc17877604)](#_Toc17877476)

[[To print graphics and charts, you will need to print to a Windows printer. To print text documents, you can print to either a Windows printer or a VistA printer. The printer language used by Windows printers can accommodate graphics, while the language used by VistA printers cannot.](#_Toc17877604)](#_Toc17877476)

[[The ability to print multiple Progress Notes, Consults, and Discharge Summaries has been added to the CPRS GUI. This feature is available from those tabs only.](#_Toc17877604)](#_Toc17877476)

[[To print multiple Notes, Consults, or Discharge Summaries, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Go to the appropriate tab (Notes, Consults, or DC/Summ) by clicking on the tab or using the keyboard commands to locate the tab. Select File \| Print Selected Items… to bring up the dialog shown below. ![](cprs-user-manual-gui-version-updated-or-3-0-499/198.png)](#_Toc17877604)](#_Toc17877476)

> [[This graphic shows a number of Progress Notes that can be printed and several highlighted](#_Toc17877604)](#_Toc17877476)

3.  

> [[Select the documents you want to print. Note: To select a number of items in a row, click the first item, hold down the Shift key, and click the last item. All items in the range will be selected. To select multiple items that are not in a row, click one, hold down the Control key, and click the other specific notifications.](#_Toc17877604)](#_Toc17877476)

4.  

[[Select OK.  
](#_Toc17877604)](#_Toc17877476)

[[The Lab Test Information menu option displays information about various lab tests.](#_Toc17877604)](#_Toc17877476)

[[To display lab test information:](#_Toc17877604)](#_Toc17877476)

1.  

[[Select Tools \| Lab Test Information.  
](#_Toc17877604)](#_Toc17877476)

> [[The Lab Test Description dialog will display.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/199.png)](#_Toc17877604)](#_Toc17877476)

> [[The Lab Test Description dialog](#_Toc17877604)](#_Toc17877476)

2.  

> [[Select a lab test from the panel on the left side of the dialog. A description of the lab test you selected will be displayed in the right side of the dialog.](#_Toc17877604)](#_Toc17877476)

[[You can change many of the settings that control the way CPRS works. The Options choice on the Tools menu contains dialogs that allow you to change which notifications and order checking messages you get, manage team and personal lists, assign your default patient selection settings, and modify your default tab preferences. To access the personal preferences settings, click Tools \| Options from any CPRS tab.](#_Toc17877604)](#_Toc17877476)

[[The Options dialog consists of a number of tabs, each of which allows access to a category or type of preference settings.](#_Toc17877604)](#_Toc17877476)

[[  
![](cprs-user-manual-gui-version-updated-or-3-0-499/200.png)](#_Toc17877604)](#_Toc17877476)

[[<span id="Options_dialog" class="anchor"></span>The Tools \| Options dialog  
](#_Toc17877604)](#_Toc17877476)

[[The General tab includes the Date Range Defaults…button which allows you to limit the date range for lab results as well as appointments and visits that appear on the cover sheet, the Clinical Reminders… button which allows you to configure and arrange which clinical reminders are displayed on the cover sheet, and the Other Parameters…button which allows you to set which tab is active when CPRS starts, set the date range for items on the Meds tab, and set the date range for Encounter appointments. The buttons on the General tab are explained in more detail below.](#_Toc17877604)](#_Toc17877476)

[[Click Clinical Reminders… to configure and arrange which clinical reminders are displayed on the Cover Sheet.](#_Toc17877604)](#_Toc17877476)

[[Based on the setting of the parameter ORQQPX NEW REMINDER PARAMS, you see one of two dialogs for configuring and arranging clinical reminders on your coversheet. If this parameter is set to "Off," you will see the "Clinical Reminders on Cover Sheet" dialog. If the parameter is set to "On," you will see the "Clinical Reminders and Reminder Categories Displayed on Cover Sheet" dialog. Your Clinical Coordinator sets the ORQQPX NEW REMINDERS PARAMS parameter.](#_Toc17877604)](#_Toc17877476)

[[To select the clinical reminders you want displayed on the Cover Sheet, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  - 
    - 

> [[From the Clinical Reminders on Cover Sheet dialog, highlight an item in the "Reminders not being displayed:" field. Select the arrow button ( \> ) to add the clinical reminder to the "Reminders being displayed:" field. (Hold down the control key to select more than one reminder at a time.) The reminders in this field will be displayed on the Cover Sheet. Select the arrow button ( \> ) to remove an item. To control how the reminders are displayed on the Cover Sheet, do one of the following: click the "Display Order" option (at the bottom of the dialog) to display the reminders in their current order. To move a reminder up or down the list, select the reminder and click either the up or down arrow. click the "Alphabetical" option (at the bottom of the dialog) to display the reminders in alphabetical order. ![](cprs-user-manual-gui-version-updated-or-3-0-499/202.png)](#_Toc17877604)](#_Toc17877476)

> [[Clinical Reminders on Cover Sheet dialog](#_Toc17877604)](#_Toc17877476)

[[The Level column of the "Cover Sheet Reminders (Cumulative List)" field displays the originating authority of the Reminder, which can include System, Division, Location, User Class, and User. Reminders on this list that display a small gray padlock icon at the beginning of the line cannot be removed. These Reminders are mandatory. The Seq (Sequence) column defines the order in which the Reminders will be displayed on the Cover Sheet. If there are two or more Reminders with the same sequence number, the Reminders will be listed by level (System, Division, Service, Location, User class, User).](#_Toc17877604)](#_Toc17877476)

[[Select this drop-down box and select a location. The Reminders assigned to that location appear on the Cumulative List.](#_Toc17877604)](#_Toc17877476)

[[This field displays all of the Reminders and Categories available to the user. Notice that the reminder name is in parentheses after the print name. Categories are groups of related Reminders that can be added as a group. Individual reminders within a category can be removed from the User Level Reminders field. Highlight a Reminder or Category from the field and click the right arrow to add them to the User Level Reminders field.  
](#_Toc17877604)](#_Toc17877476)

[[Once you have made all of the desired changes to the Reminders that will be displayed on the Cover Sheet, select OK.  
](#_Toc17877604)](#_Toc17877476)

[[To set the initial chart tab, Meds tab date range, or Encounter date range preferences select Other Parameters.](#_Toc17877604)](#_Toc17877476)

[[Select the drop-down field and select the chart tab with which CPRS should open. Select the check box if you want CPRS to remain on the last selected tab when you change patients.  
<span id="Other_Parameters" class="anchor"></span>](#_Toc17877604)](#_Toc17877476)

[[There are three date ranges that can be configured for the Meds tab:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[Overall Meds Default: Default date range for the Meds tab. It is used if no date range is defined for Inpatient Meds or Outpatient/Non-VA Meds  
Inpatient Meds: Date range for inpatient medications. If no date range is defined for Inpatient Meds, the Overall Meds Default date range will be used.  
Outpatient / Non-VA Meds: Date range for outpatient and non-VA medications. If no date range is defined for Outpatient/Non-VA Meds, the Overall Meds Default date range will be used for outpatient and non-VA medications.To enter the Meds Tab date ranges, perform the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
- 
- 
- 

> [[Enter a State Date by doing one of the following: Typing a date (e.g. 6/21/01 or June 21, 2001). Typing a date formula (e.g. t-200). Pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/206.png) button to bring up a calendar and select a date. Note: In most cases, users should use relative dates, such as T and T-120, when entering them in the Tools \| Options dialog. If the user enters specific dates, they will remain even if the user changes patients. Specific dates will not change until the user changes them.](#_Toc17877604)](#_Toc17877476)

4.  
- 
- 
- 
5.  

[[Enter a Stop Date by doing one of the following: Typing a date (e.g. 6/21/01 or June 21, 2001). Typing a date formula (e.g. t-200). Pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/207.png) button to bring up a calendar and select a date.  
When you have entered the dates, go to another option on this dialog or select OK.](#_Toc17877604)](#_Toc17877476)

[[This option enables users to set the date range for Encounter appointments that CPRS displays on the Cover Sheet and the Encounter form. The two values are based on today's date and represent how many days in the past and how many days in the future the user may set for CPRS to display appointments.](#_Toc17877604)](#_Toc17877476)

[[To set these values, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[In the Start Date field, type or use the arrows to select a number of days in the past CPRS should display appointments. In the Stop Date field, type or use the arrows to select a number of days in the future CPRS should display appointments. Note: Your site can set a parameter to give you a warning if you select an appointment too far in the future. CPRS will display a warning to let you know that you may be going against local policy. This message is just a warning and you may proceed.](#_Toc17877604)](#_Toc17877476)

3.  

[[This tab allows you to change your notification options. Click the check box if you wish to have MailMan send you a bulletin for flagged orders.  
  
![](cprs-user-manual-gui-version-updated-or-3-0-499/208.png)](#_Toc17877604)](#_Toc17877476)

[[<span id="Notifications_tab" class="anchor"></span>The Notifications tab  
](#_Toc17877604)](#_Toc17877476)

[[Please use care when using this button to remove pending notifications, especially if you are designated as a surrogate for another user, as patient care may be delayed until the original provider returns.](#_Toc17877604)](#_Toc17877476)

[[To remove pending notifications, if necessary, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  

[[Select the Remove Pending Notifications button and then on Yes on the Warning dialog to clear all of your current pending notifications. (This button is enabled only if you are authorized to use it.) ![](cprs-user-manual-gui-version-updated-or-3-0-499/209.png)](#_Toc17877604)](#_Toc17877476)

2.  

[[If you are sure you want to remove the pending notifications, select Yes.](#_Toc17877604)](#_Toc17877476)

[[Click the Display Sort drop-down field to select the sort method for your notifications. Choices include Patient, Type, and Urgency.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[If the surrogate has processed an alert, it is ignored. If the surrogate has not processed an alert originally intended for the user, it is returned to the originally intended recipient. If the unprocessed alert was also sent to the surrogate as an initial recipient, then the alert is also retained by the surrogate. If the alert was *forwarded* to the surrogate, *but meant only to be sent to* the original user, then the alert is electronically removed from the surrogate's notification list. *Any* unprocessed alerts that are retained by the surrogate will require manual intervention to remove them. There is no difference in how informational vs. action notifications are managed with respect to surrogacy. The above rules are applicable regardless of the type of notification.](#_Toc17877604)](#_Toc17877476)

[[Click the check box next to any order check to enable or disable it. Order checks with "Mandatory" in the Comment column cannot be turned off or disabled. Click the heading to sort order checks so that you can see which are turned on and which are turned off.](#_Toc17877604)](#_Toc17877476)

[[  
![](cprs-user-manual-gui-version-updated-or-3-0-499/210.png)](#_Toc17877604)](#_Toc17877476)

[[<span id="Order_Checks_tab" class="anchor"></span>This dialog indicates that the Duplicate Drug Order check is mandatory and cannot be turned off  
](#_Toc17877604)](#_Toc17877476)

[[The Lists/Teams tab allows you to set defaults for selecting patients. It also contains your personal lists and the teams of which you are a member.  
![](cprs-user-manual-gui-version-updated-or-3-0-499/211.png)](#_Toc17877604)](#_Toc17877476)

[[The Lists/Teams tab](#_Toc17877604)](#_Toc17877476)

[[Click Source Combinations… to edit or create a list of sources from which your patients can be selected. You can change your combinations by adding or removing specific wards, clinics, providers, specialties or lists.](#_Toc17877604)](#_Toc17877476)

[[To create a source combination:](#_Toc17877604)](#_Toc17877476)

11. [[Click a radio button in the "Select source by" group.](#_Toc17877604)](#_Toc17877476)
12. [[Click an entry in the selection field below the "Select source by" group.](#_Toc17877604)](#_Toc17877476)
13. [[Click Add.](#_Toc17877604)](#_Toc17877476)
14. [[Repeat steps 1 through 3 for each desired source.](#_Toc17877604)](#_Toc17877476)
15. [[When all desired entries are in the Combinations field, click OK.](#_Toc17877604)](#_Toc17877476)
1.  
2.  
3.  
4.  

> [[Select Personal Lists... to edit or create list of patients. To create a list, select New List... In the New Personal List dialog, type in a name for your list. Then, indicate whether the list will by visible only to you by selecting the Myself only radio button or allow all users to see the list by selecting the All CPRS users radio button. Locate the appropriate patients by selecting the appropriate category under the "Select patients by" group: Patient, Ward, Clinic, Provider, Specialty, Other. When a category is selected, CPRS displays the items for the category. For example, if you choose Clinic, CPRS displays the list of clinics.](#_Toc17877604)](#_Toc17877476)

5.  
6.  
7.  
8.  
9.  
10. 

[[Select the item within the category that you want to use. For example, if you have a patient and you know the patient is in a specific clinic, select that clinic. The Patients to add field lists all of the patients that can be added from the particular selection method. Highlight the patient names in this field and click Add (which moves the highlighted patient or patients into the Patients on Personal List pane. To add all patients, select Add All to copy all the patients under the Patient to add pane. Repeat steps 4-6 until you have added all the patients you want to your new personal list. Review the list. If changes need to be made, use the steps 4-6 to add new names. To remove names, highlight them under the Patients on Personal List pane and select Remove. To remove all the names under Patients on Personal List pane, select Remove All. If needed, select whether the list should be for Myself only or for All CPRS users. When you have all the patients that you want on the list, select Save Changes if you plan to make other changes on the Personal List dialog such as creating one or more additional Personal Lists. If you are finished creating personal lists for now, select OK. To edit a personal list, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[On the Lists/Team tab, select Personal Lists…. In the Personal Lists dialog, select the list under the Personal Lists pane that you want to edit. To add patients to the list, locate the appropriate patients by selecting the appropriate category under the "Select patients by" group: Patient, Ward, Clinic, Provider, Specialty, Other. When a category is selected, CPRS displays the items for the category. For example, if you choose Clinic, CPRS displays the list of clinics.](#_Toc17877604)](#_Toc17877476)

4.  
5.  
6.  
7.  
8.  
9.  

[[  
![](cprs-user-manual-gui-version-updated-or-3-0-499/215.png)](#_Toc17877604)](#_Toc17877476)

[[<span id="Notes_tab" class="anchor"></span>The Notes tab](#_Toc17877604)](#_Toc17877476)

[[You may select a personal list of document titles to be displayed for several different types of documents. Click the drop-down button on the Document class field and select the class of document for which you would like to create a list. When you have selected a document class, the Document titles field is automatically populated with all available choices. Highlight one and click Add. Hold down the Control key to select more than one title at a time. To select a title from your list as your default, highlight it and click Set as Default. Click Save Changes if you will be making more changes on this dialog before you click OK.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/217.png)](#_Toc17877604)](#_Toc17877476)

[[The Document Titles dialog  
](#_Toc17877604)](#_Toc17877476)

[[This tab allows you to set the date ranges and the maximum number of occurrences for CPRS reports. You can change the settings for all reports or for individual reports.](#_Toc17877604)](#_Toc17877476)

[[  
![](cprs-user-manual-gui-version-updated-or-3-0-499/218.png)](#_Toc17877604)](#_Toc17877476)

[[<span id="Reports_tab" class="anchor"></span>The Reports tab](#_Toc17877604)](#_Toc17877476)

[[This option allows you to set a start date, a stop date, and a maximum number of occurrences for all CPRS reports.](#_Toc17877604)](#_Toc17877476)

[[When this dialog appears follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select Tools \| Options. Select the Reports tab. Select the Select All Reports… button. After you press the Set All Reports… button the "Change Default Settings For Available CPRS Reports" dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/219.png)](#_Toc17877604)](#_Toc17877476)

> [[The Change Default Setting For Available CPRS Reports dialog](#_Toc17877604)](#_Toc17877476)

4.  - 
    - 
    - 
5.  
6.  

> [[Change the value in the Start Date and Stop Date fields by selecting the appropriate field and by doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001). entering a date formula (e.g. t-200). pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/220.png) button to bring up a calendar. After you have entered a start and stop date, you can change the maximum number of occurrences (if necessary) by selecting the Max field. Select OK. A confirmation dialog box will appear.](#_Toc17877604)](#_Toc17877476)

7.  
8.  
1.  

> [[Place the cursor in the "Type the first few letters of the report you are looking for:" field (located at the top of the dialog box) and type the name of the report that you would like to change -or-](#_Toc17877604)](#_Toc17877476)

> [[use the scroll bars to find the report.](#_Toc17877604)](#_Toc17877476)

2.  1.  
    2.  
    3.  
3.  
4.  

> [[Change the value in the Start Date and/or Stop Date field by clicking in the appropriate column and doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001). entering a date formula (e.g. t-200). pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/222.png) button to bring up a calendar. After you have entered a start and stop date, you can change the maximum number of occurrences (if necessary) by clicking in the Max field. Click Apply to save your changes -or-](#_Toc17877604)](#_Toc17877476)

> [[click OK to save your changes and close the dialog box.](#_Toc17877604)](#_Toc17877476)

5.  
- 
- 
1.  
2.  
3.  
4.  

> [[Select Tools \| Options. Select the Surrogates tab. To set a default surrogating period, check the Use default Start and Stop dates when entering a new surrogate checkbox. Enter a value from 1 to 30 in the Default surrogating period (1..30 days) text box.  
> Note: The Use default Start and Stop dates when entering a new surrogate checkbox is optional. Click on the Add Surrogate button or double click the Dbl-click here to add surrogate button. After you press the Add Surrogate button the "Surrogate Management" dialog will appear. Red highlighting has been added for emphasis. In the screenshot below, the default Start Date is the current date and is listed in the Start dropdown. The default Stop Date that you have selected is listed in the Stop dropdown.](#_Toc17877604)](#_Toc17877476)

> [[If you have set a default surrogating period, you can change the Start and Stop dates.  

> If you have not set a default surrogating period, the Start and Stop dropdowns in the "Surrogate Management" dialog will be blank.](#_Toc17877604)](#_Toc17877476)

> [[If you change the Start and Stop dates, you will not be able to select a past date, but you can select the present date or any date in the future.  

> ![](cprs-user-manual-gui-version-updated-or-3-0-499/225.png)](#_Toc17877604)](#_Toc17877476)

> [[The Surrogate Management dialog  
> ](#_Toc17877604)](#_Toc17877476)

5.  
6.  

> [[Select a surrogate in the Name dropdown.If desired, change the value in the Start and Stop fields by pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/226.png) calendar button and entering a date and time. Listed below is an example of a calendar. It will show you all the acceptable start dates and times. The Midnight button sets the time to midnight and the Now button sets the time to the current time.  

> ![](cprs-user-manual-gui-version-updated-or-3-0-499/227.png)  
> Example of a Calendar  
> ](#_Toc17877604)](#_Toc17877476)

7.  
8.  
9.  

> [[Click OK. On the Surrogates Management screen, click Apply. Click OK to close the Options screen. Listed below is a surrogate that has been added. The exclamation mark indicates that there is information that has not been applied. The Cancel button closes the Options window without saving changes.](#_Toc17877604)](#_Toc17877476)

> [[  
> ![](cprs-user-manual-gui-version-updated-or-3-0-499/228.png)](#_Toc17877604)](#_Toc17877476)

[[Example of a Surrogate who has been added  
](#_Toc17877604)](#_Toc17877476)

[[To edit a surrogate, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  

[[Select Tools \| Options. Select the Surrogates tab. Click on a surrogate.Click on the Edit Surrogate button and update the surrogate information. (You will see a Surrogate Management popup that lets you update the Name and the Start and Stop date/times.) Click Apply to save your changes.Click OK to close the Options window.To remove a surrogate, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[Select Tools \| Options. Select the Surrogates tab. Click on a surrogate.Click on the Remove Surrogate button.You will see a popup that asks you to confirm that you want to remove the surrogate.  

> ![](cprs-user-manual-gui-version-updated-or-3-0-499/229.png)  
> Remove Surrogate popup  
> ](#_Toc17877604)](#_Toc17877476)

5.  
6.  
7.  

[[This tab allows you to determine how pasted Notes will display in CPRS.](#_Toc17877604)](#_Toc17877476)

> [[  

> ![](cprs-user-manual-gui-version-updated-or-3-0-499/230.png)](#_Toc17877604)](#_Toc17877476)

[[The Copy/Paste Tab](#_Toc17877604)](#_Toc17877476)

[[To determine how pasted Notes will display in CPRS, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  1.  
    2.  
    3.  
8.  
9.  

[[Select Tools \| Options. Select the Copy/Paste tab. Check the "Copy/Paste viewing is currently disabled" checkbox. After the checkbox gets checked, the wording will change to "Copy/Paste viewing is currently enabled."In the "How text is identified on the note" section, select the attributes for pasted text by checking one or more of the following boxes:  
Bold  
Italics  
Underline  
Highlight If you select "Highlight", you may also use the default color or choose a different color. To select a different color, select the drop-down arrow and choose one of the following colors:  
Black  
Maroon  
Green  
Olive  
Navy  
Purple  
Teal  
Gray  
Silver  
Red  
Lime  
Yellow  
Blue  
Fuchsia  
Aqua  
WhiteIf you would like to see the differences between what the author pasted into the note and what was edited, check the "Difference Identifier Toggle".If you check the "Difference Identifier Toggle", you may select the following:Select the attributes for edited text by checking one of more of the following boxes:  
Bold  
Italics  
Underline  
Text ColorIf you select "Text Color", you may use the default color or choose a different color. To select a different color, select the drop-down arrow and choose one of the following colors:  
Black  
Maroon  
Green  
Olive  
Navy  
Purple  
Teal  
Gray  
Silver  
Red  
Lime  
Yellow  
Blue  
Fuchsia  
Aqua  
WhiteEnter the character limit. The default number of characters is 5000.Click Apply to save your changes.Click OK to close the Options window.](#_Toc17877604)](#_Toc17877476)

[[Listed below is an example of Copy/Paste viewing that is set to enabled. The pasted text will be highlighted in lime and the Difference Identifier Toggle has been enabled. The edited text will be in aqua and the character limit will be 50.](#_Toc17877604)](#_Toc17877476)

[[  
![](cprs-user-manual-gui-version-updated-or-3-0-499/231.png)  
Example of Copy/Paste text viewing enabled  
](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[CPRS now offers support for items related to Women's Health, including the System for Mammogram Results Tracking (SMART) and order checking for items that are teratogenic or potentially unsafe for breastfed infants.](#_Toc17877604)](#_Toc17877476)

- [[new alerts](#_Toc17877604)](#_Toc17877476)
- [[a new alert dialog that is patient-centric rather than provider-centric](#_Toc17877604)](#_Toc17877476)
- [[new reminder dialogs and TIU templates](#_Toc17877604)](#_Toc17877476)
- [[creates a progress note](#_Toc17877604)](#_Toc17877476)
- [[files health factors](#_Toc17877604)](#_Toc17877476)
- [[when available, updates the BCCCR](#_Toc17877604)](#_Toc17877476)

[[Teratogens are drugs (including medications), chemicals, or other exposures, like radiation, that can interfere with normal embryonic/fetal development and thus, may lead to birth defects or pregnancy loss. In addition, there is a group of medications that pose a potential risk to breast-fed infants.](#_Toc17877604)](#_Toc17877476)

[[CPRS has enhanced order checks to alert providers if something is ordered for a woman that is pregnant or breast feeding that is teratogenic.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[CoversheetImmunization tab in the Encounter formReminder Dialogs.You can document a patient's skin tests from these locations in CPRS:](#_Toc17877604)](#_Toc17877476)

- 
- 

[[Regardless of the location from where you start recording the immunization/skin test, CPRS will always take you to the Enter Immunization or Enter Skin Test screen, which has the following sections:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[Immunization/Skin Test Evaluation Statuses: Lists the immunizations or skin tests.  
Immunization/Skin Test List: Shows the immunizations or skin tests that are in the patient record. If you have accessed the Enter Immunization screen from the coversheet, the Immunization List will be filled in only when a user is currently entering an immunization. If you have accessed the Enter Immunization screen from the Immunization tab in the Encounter form, the Immunization List will always contain a patient's immunizations.  
Immunization/Skin Test Selection: Allows you to select an immunization/skin test and a documentation type.  
Editor/Detail Viewer: Displays the fields associated with a specific document/skin test type and allows you to edit them. After you access the Enter Immunization/Skin Test screen, you will be able to add, edit, delete, or view an immunization/skin test.](#_Toc17877604)](#_Toc17877476)

[[The examples below show what the Enter Immunization screen looks like when you open it from the Coversheet, and what the Enter Skin Test screen looks like when you open it from the Encounter form.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/232.png)  
Example of the Enter Immunization screen  
  
](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/233.png)  
Example of the Enter Skin Test screen  
  
](#_Toc17877604)](#_Toc17877476)

[[When documenting an immunization from the cover sheet, a progress note will automatically be generated, with a standard text for the Immunization entry.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
1.  
2.  
3.  
1.  
1.  1.  1.  
    2.  1.  
2.  
3.  
4.  

> [[On the Enter Immunization/Skin Test screen:If you are adding an immunization:On the Enter Immunization screen, select a Documentation Type and an Immunization in the Immunization Selection section.If you are adding a skin test:On the Enter Skin Test screen, select a Documentation Type and a Skin Test in the Skin Test Selection Section.Fill in all required fields (marked with an asterisk) for the selected Documentation Type.Click Save.Click Finish. Administered and historical vaccines will be listed on the CPRS Coversheet. Contraindicated and refused vaccines will not be listed on the Coversheet. However, they will be listed on the Encounter Form Immunizations tab. If a vaccine was contraindicated, you will get a warning message when you click Finish.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
1.  
2.  
3.  
1.  
2.  

[[On the Enter Immunization/Skin Test screen, right-click on an immunization/skin test in the Immunization/Skin Test Evaluation Statuses section and select either View Information or Clinical Maintenance from the dropdown.  
> **NOTE:** View Information and Clinical Maintenance display the same information about the patient's immunization history. However, View Information displays the information on the right-hand side of the Immunization Evaluation Statuses section while Clinical Maintenance displays the information on a separate screen and allows you to print it.Click Finish.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

- [[Active Problems](#_Toc17877604)](#_Toc17877476)
- [[Allergies](#_Toc17877604)](#_Toc17877476)
- [[Postings](#_Toc17877604)](#_Toc17877476)
- [[Active Medications](#_Toc17877604)](#_Toc17877476)
- [[Clinical Reminders](#_Toc17877604)](#_Toc17877476)
- [[Recent Lab Results](#_Toc17877604)](#_Toc17877476)
- [[Vitals](#_Toc17877604)](#_Toc17877476)
- [[Appointments](#_Toc17877604)](#_Toc17877476)
- [[Immunizations](#_Toc17877604)](#_Toc17877476)
- [[Women's Health](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

- 

> [[Select New Patient This menu item opens the Patient Selection dialog.](#_Toc17877604)](#_Toc17877476)

- 

> [[Update/Provider/Location This menu item opens the Provider & Location for Current Activities dialog. This dialog enables you to change the clinician or location associated with an encounter.](#_Toc17877604)](#_Toc17877476)

- 

> [[Review/Sign Changes This menu item enables you to view the orders you have placed that require an electronic signature, select the orders you want to sign at this time, and enter your electronic signature code (if you are an authorized signer).](#_Toc17877604)](#_Toc17877476)

[[The CPRS Windows interface mimics the paper chart of a patient's record, but CPRS makes locating information easier. With the Patient Selection screen, you can quickly bring up a record for any patient on the system. The Cover Sheet summarizes important information about the patient. Along the bottom of this dialog or page are a number of tabs that will quickly take you to the part of the chart you need to see. For example, you might want to see progress motes, Problems, Summaries, Medications, Lab Tests, or place new orders:](#_Toc17877604)](#_Toc17877476)

[[To go to a different part of the patient chart, click the appropriate tab at the bottom of the chart or choose View \| Chart Tab, and then select the desired tab.](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select the Patient ID box. The Patient Inquiry dialog will appear. The Patient Inquiry dialog includes additional information such as the patient's mailing address, telephone numbers (including the patient's home, work, and cell phone numbers), admission information, and other relevant data, such as provider information and primary and secondary next of kin entries. If the patient is assigned to a mental health treatment coordinator (MHTC), the provider's name, position and phone numbers will display as well. While in the detailed display, you can select a new patient, print the detailed display, or close the detailed display.](#_Toc17877604)](#_Toc17877476)

2.  
3.  

> [[To print a copy of the Patient Inquiry dialog, select Print. To close the Patient Inquiry window and return to the Cover Sheet, select Close. -or-](#_Toc17877604)](#_Toc17877476)

> [[select a new patient by selecting Select New Patient.](#_Toc17877604)](#_Toc17877476)

1.  

> [[If you are already in the Provider / Encounter dialog skip to step 2. Otherwise, from any chart tab, click the Provider / Encounter box located in the top center portion of the dialog. Note: These instructions are written as if the user must select a provider. If the user making the selection is a provider, the user will be selected by default and the cursor will go to the New Visit tab if no visit is defined, or to the Clinic Appointments tab if one is defined. If the user is not a provider, the cursor will go to the Encounter Provider field so that the user can select the provider for the encounter.](#_Toc17877604)](#_Toc17877476)

2.  
3.  
- 
- 
- 
4.  
5.  
6.  
7.  

[[CPRS uses the new Vitals Lite component to view and enter the following vitals and measurements:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

> [[Body Mass Index (BMI): This value is calculated using the following formula: BMI = Weight in Kilograms/\[(Height in Meters) x (Height in Meters)\]](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[Users can view vitals in CPRS by launching Vitals Lite from the Cover Sheet. Users can then review vitals using the graph and table of vitals.](#_Toc17877604)](#_Toc17877476)

[[The values for vitals display as points on the graph connected by line to show trends. A legend above the graph lets the user know what each set of points, distinguished by a shape and color, represents.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[To get the view they want, users can customize the Vitals Lite display using the following controls:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[As the user moves the slider, the entries move also. If there are enough entries and the user moves the slider far enough to the left, the entries will go off the screen. If the user moves the slider all the way to the right, only the most recent entry will be displayed.](#_Toc17877604)](#_Toc17877476)

[[To view vitals from the CPRS Cover Sheet, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
16. [[Select a vital entry displayed on the Cover Sheet. CPRS will bring up Vitals Lite. The default date range includes today and goes six months in the past.](#_Toc17877604)](#_Toc17877476)
17. [[To graph a category, click on the corresponding row in the table.](#_Toc17877604)](#_Toc17877476)
18. [[From this point, you can customize the display of vitals by doing one or more of the following:](#_Toc17877604)](#_Toc17877476)
1.  [[To choose a different date range, users can double-click a time frame from the predefined options on the left side or double click Date Range to define a custom date range. If you choose a predefined date range, skip to step b. If you choose Date Range, enter a start date by either typing a date in the field (you must enter the month, day, and year separately using the mouse or arrow keys to select them) or use the following steps:](#_Toc17877604)](#_Toc17877476)
    1.  
    2.  
    3.  
    4.  
2.  [[Click the down arrow next to Start with Date to display the date dialog. Click the buttons on the top of the dialog to find the appropriate month and year. (You can also click on the month and select the month from a list and then click on the year and choose the year). Repeat steps 1 and 2 for the Go to Date. Click OK when you have the appropriate date. To use the graph options, right-click where the default date ranges are and select Show/Hide Graph Options. You can then enable or disable, the zoom feature, display of the values, three-dimensional display, and the time scale. These options are discussed below:](#_Toc17877604)](#_Toc17877476)
- 
- 
1.  [[Values: To display the values, place a check in the Values checkbox by clicking it or using Alt + v. To remove the values, remove the check mark. Allow ZoomTo enable the zoom feature, place a check mark in the Enable Zoom checkbox by clicking it or using Alt + z.](#_Toc17877604)](#_Toc17877476)
2.  [[Then, to zoom in on section of the graph, click and drag the mouse from right to left and above to below over the area and release the mouse button.](#_Toc17877604)](#_Toc17877476)
3.  [[To return to the full view, click and drag from right to left.](#_Toc17877604)](#_Toc17877476)
- [[3D: To make the graph display in a slightly three-dimensional (3D) view, place a check mark in the 3D checkbox by clicking it or using Alt + 3. To return to a two-dimensional view, remove the check mark.](#_Toc17877604)](#_Toc17877476)
- [[Time Scale: To view the entire selected date range on the graph, check the Time Scale checkbox. Clear the checkbox to view the data points in evenly spaced intervals.](#_Toc17877604)](#_Toc17877476)
3.  [[To view more vitals if available in the date range you selected, use the slider under the graph and above the table or use the arrows keys. The oldest entries are farthest right while the most recent entries are the farthest to the left.](#_Toc17877604)](#_Toc17877476)
5.  [[When you are finished, click the Close button (the X in the upper right corner).](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[Users can enter vitals and measurements from the Cover Sheet or the Encounter form's Vitals tab. A template must be available for users to enter vitals.](#_Toc17877604)](#_Toc17877476)

[[To enter vitals with the new Vitals Lite in CPRS, a template that defines which vital measurements display on the Vitals Entry form must be available. These templates are not created through CPRS, but through the VitalsManager application. To use the VitalsManager application, a user must hold the GMV MANAGER key.](#_Toc17877604)](#_Toc17877476)

[[A GMV MANAGER key holder can define in the template which vitals or measurements display for entry when the user selects Enter Vitals. In defining the template, the key holder can also set default qualifiers for each vital or measurement. The user entering the vitals can change the qualifiers, but a default can be set to make recording the vitals more efficient. Templates can be defined at the following levels:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[System Division Location User For User level templates to display, a GMV MANAGER key holder must check the Allow User Templates checkbox.](#_Toc17877604)](#_Toc17877476)

[[The dialog to enter vitals displays the following patient information:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Unavailable checkbox that records if the vitals cannot be taken. The text for this checkbox may be very small with only the U displaying. Refused checkbox that records if the patient refused to have the vital taken. The text for this checkbox may be very small with only the R displaying. Name shows vital or measurement name. Value field is where the user enters the numeric value. Units show what unit of measurement, such as inches or centimeters, is being used. A checkbox on the top right of the dialog enables users to switch between drop-down lists and checkboxes to change the units. Qualifiers show a drop-down arrow that will bring up a small window with the defined qualifiers for that vital or measurement. If a default qualifier has been defined, it will display to the right of the button. If the user changes the qualifiers, the text to the right of the button changes.The dialog also has a checkbox to designate that the patient was on pass and vitals could not be taken.](#_Toc17877604)](#_Toc17877476)

[[For more information on how to create and save templates and the other options that for Vitals Lite, please see the Vitals/Measurements documentation by going to <http://www.va.gov/vdl> and selecting Vitals/Measurements.](#_Toc17877604)](#_Toc17877476)

[[Once a template has been defined, user can enter vitals and measurements. Users can choose to display or hide the template list and the most recent vitals recorded.](#_Toc17877604)](#_Toc17877476)

[[To enter a patient's vitals, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  1.  
    2.  
    3.  
5.  
6.  - 
    - 
    - 
7.  
8.  
9.  

[[From the Cover Sheet, select a vitals entry and then select Enter Vitals using the button or the pop-up menu. On the Encounter form, select the Vitals tab and select Enter Vitals. If prompted, enter a location and then select OK. Bring up the Vitals Lite Enter dialog by selecting the Enter Vitals button or bringing up the pop-up menu and selecting Enter Vitals. If necessary, select the appropriate template by doing the following: If it is not displayed, show the Templates pane by selecting Exp. View in the upper right of the dialog. Select the level at which the template resides: System, Division, Location, User (user will only display if it has been set to display). Select the appropriate template. To view the most recent vitals if they are not displayed, select the Latest V. (for Vitals) button. Select it again to hide them. If you cannot take the vitals, place check marks in the appropriate boxes. These boxes might be: Patient on Pass – use this if the patient is on pass. Unavailable – there is a check box by each vital sign or measurement. Refused – there is a checkbox by each vital sign or measurement. If necessary, change the units for the vital. Enter a vitals value for the patient by placing the cursor in the appropriate field and typing a value. Repeat steps 4 and 5 as needed. When finished, check over the entries and select either Save or Save and Exit.  
](#_Toc17877604)](#_Toc17877476)

[[Through Vitals Lite, users can now mark a vitals entry as entered in error. The user selects one or more vitals entries from a specific date and then must select a reason before marking them as entered in error.](#_Toc17877604)](#_Toc17877476)

[[To mark vitals entries as entered in error, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[To bring up the vitals screen from the Cover Sheet, select a vitals entry using the mouse or appropriate keystrokes.Display the dialog by selecting Entered in Error using the button or the popup menu. ![](cprs-user-manual-gui-version-updated-or-3-0-499/250.png)](#_Toc17877604)](#_Toc17877476)

> [[Through the vitals Entered in Error dialog, users can select the erroneous entries and mark them as entered in error](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  

> [[Enter the date of the erroneous entry. In the list that displays, highlight the vitals entries that are incorrect. To select multiple entries, hold down the Ctrl key and click each entry to select it, or hold down the Shift key and while clicking the last entry to select a range. Select a Reason. Select Mark as Entered in Error. Note: If the provider has an NPI, it will not display on the screen above.](#_Toc17877604)](#_Toc17877476)

1.  

[[In the Allergies/Adverse Reactions pane on the Cover Sheet tab, CPRS displays a list of causative agents associated with patients' allergies or adverse reactions. If patients have causative agents listed in this pane, CPRS also displays the word *Allergies* in the Postings pane and the letter A (for allergies) on the Postings button. To view more information about allergies or adverse reactions associated with the causative agents listed in the Allergies/Adverse Reactions pane, simply click on the causative agent in which you are interested. CPRS then displays a comprehensive listing of the details associated with this causative agent.](#_Toc17877604)](#_Toc17877476)

[[You can obtain less comprehensive information about allergies and adverse reactions by clicking the word *Allergies* in the Postings pane. When you do this, CPRS displays information about the causative agents, severity, and signs/symptoms associated with patients' allergies and adverse reactions. From the Cover Sheet tab, you can also:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[You can enter a new allergy or adverse reaction from the Cover Sheet tab in either of two ways:](#_Toc17877604)](#_Toc17877476)

- 
- 

[[Take the following steps to enter new allergies using the first of the two methods mentioned above:](#_Toc17877604)](#_Toc17877476)

1.  
19. [[Move your mouse arrow to a location anywhere within the Allergies/Adverse Reactions pane. Right click to display a pop-up menu.](#_Toc17877604)](#_Toc17877476)
20. [[From this menu, select Enter new allergy. CPRS displays the Allergy Reactant Lookup dialog.](#_Toc17877604)](#_Toc17877476)
21. [[In the Enter causative agent for Allergy or Adverse Drug Reaction field, type the first three characters (minimum) of the causative agent's name.](#_Toc17877604)](#_Toc17877476)
22. [[Click Search. CPRS displays a list of possible matches.](#_Toc17877604)](#_Toc17877476)
23. [[<span id="drug_class_cross_checking" class="anchor"></span>If you click on any drug ingredient listed in the Drug Ingredients File dropdown, you will get a notification that Drug Class cross checking will not occur. However, if you check the checkbox next to the notification, you will be able to enter the drug ingredient, as shown below (the notification is highlighted in red for emphasis):  
      
    ![](cprs-user-manual-gui-version-updated-or-3-0-499/251.png)  
    ](#_Toc17877604)](#_Toc17877476)
24. [[If the causative agent you typed does not match any of the agents currently available for your site, CPRS displays the Causative Agent Not On File dialog, from which you can select one of the following three options:](#_Toc17877604)](#_Toc17877476)

> [[Note: The patient's chart will not be updated unless you choose a causative agent that is on file.](#_Toc17877604)](#_Toc17877476)

> [[a. Yes: Use this option to request that the causative agent be added to your site's ALLERGIES file. When you click Yes, CPRS displays the Enter Optional Comments dialog, which enables you to type additional comments (optional), such as the signs or symptoms that occurred as a result of contact with this causative agent, or whether you observed these symptoms firsthand. After you type your comments, click Continue. CPRS then sends to members of your site's GMRA Request New Reactant mail group a message that includes the following items:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

> [[The causative agent you attempted to enter The name of the patient for whom you attempted to make this entry Your name, title, and contact information Your comments (if any) Note: When the bulletin is sent, a message such as the following will display. This message also informs the user that the allergy was NOT entered into the patient's record.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/252.png)](#_Toc17877604)](#_Toc17877476)

> [[This message box informs the user that the bulletin has been sent, but no information has been added to the chart](#_Toc17877604)](#_Toc17877476)

> [[Members of your site's GMRA Request New Reactant mail group will review this message and, if appropriate, add the causative agent to your site's ALLERGIES file.](#_Toc17877604)](#_Toc17877476)

> [[Note: If your site's IRM staff has not yet added members to your site's GMRA Request New Reactant mail group, CPRS displays the following message:](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/253.png)](#_Toc17877604)](#_Toc17877476)

> [[CPRS displays this message if your IRM staff has not yet added members to the GMRA Request New Reactant mail group](#_Toc17877604)](#_Toc17877476)

2.  
3.  

> [[No: Clicking No enables you to try an alternate spelling or trade name for your causative agent, or to type another causative agent. Cancel: Use this option if you want to cancel your allergy entry. ![](cprs-user-manual-gui-version-updated-or-3-0-499/254.png)](#_Toc17877604)](#_Toc17877476)

> [[The Causative Agent Not On File dialog](#_Toc17877604)](#_Toc17877476)

25. [[<span id="Method_One_Eight" class="anchor"></span>If the causative agent you typed matches an agent that is currently available for your site, select the agent. (Click + to expand a heading.)](#_Toc17877604)](#_Toc17877476)

> [[Note: With CPRS GUI 24 or later, you may not add free-text causative agents. If you select an item under the "Add new free-text allergy" heading, CPRS displays the *Causative Agent Not On File* dialog. (See Step 6 above.)](#_Toc17877604)](#_Toc17877476)

26. [[Select OK.](#_Toc17877604)](#_Toc17877476)

> [[The Enter Allergy or Adverse Reaction dialog appears. <span id="enter_allergy_updated_method_one" class="anchor"></span>](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/255.png)](#_Toc17877604)](#_Toc17877476)

> [[The Enter Allergy or Adverse Reaction dialog](#_Toc17877604)](#_Toc17877476)

> [[  
> Note: You can view a patient's current allergies or adverse reactions by selecting the Active Allergies button. Also, the user previously could change the Originator, but this is no longer allowed. The originator is the user logged in.](#_Toc17877604)](#_Toc17877476)

> [[Note: If a provider has an NPI, it will display on the screen above. See the "National Provider Identifier (NPI) Display in CPRS" section for an example of an NPI displaying on a screen.](#_Toc17877604)](#_Toc17877476)

27. [[Use the Observed or Historical radio button to indicate whether the entry is for an observed or historical allergy, respectively. (If you point your mouse at either of these option buttons, CPRS displays a hover hint that defines observed and historical.)](#_Toc17877604)](#_Toc17877476)

> [[Note: Observed or Historical used to have a default, but the user must now select the appropriate choice. CPRS does not allow you to select future dates for observed allergy/adverse reaction entries.](#_Toc17877604)](#_Toc17877476)

> [[Note: When you select Observed for a drug reaction, CPRS generates a Progress Note. Once this note is signed by the user entering the allergy or by an administrative update user, the note will be viewable by all users.](#_Toc17877604)](#_Toc17877476)

28. [[Select the Nature of Reaction (Allergy, Pharmacological, or Unknown).](#_Toc17877604)](#_Toc17877476)

> [[The Nature of Reaction can be Allergy, Pharmacologic, or Unknown. An allergic reaction occurs because the patient is sensitive to a causative agent, regardless of the amount the patient is exposed to. A pharmacologic (nonallergic) reaction occurs when the patient is sensitive to an agent under certain conditions, such as exposure to a large amount. Unknown is provided if you are not sure what Nature of Reaction (mechanism) to enter.](#_Toc17877604)](#_Toc17877476)

> [[Note: Allergies are a subset of adverse reactions. All allergies are adverse reactions, but not all adverse reactions are allergies.](#_Toc17877604)](#_Toc17877476)

29. [[If you are entering an observed allergy, use the Reaction Date/Time and Severity boxes to select a reaction date, time, and severity. (The Severity box is not visible for historical allergies. If the Severity box is visible, CPRS displays a ? button at its side. If you click this button, CPRS displays text explaining severity selections.)](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/256.png)](#_Toc17877604)](#_Toc17877476)

> [[In the Enter Allergy or Adverse Reaction dialog, the Severity field shows what levels of severity the user can select](#_Toc17877604)](#_Toc17877476)

30. [[Using the Signs/Symptoms box, select one or more signs or symptoms. The signs and symptoms you select appear in the Selected Symptoms pane.](#_Toc17877604)](#_Toc17877476)

> [[<span id="Historical_allergy_note" class="anchor"></span>Note: You must enter at least one Sign/Symptom or enter a comment of at least four characters when documenting a historical allergy/adverse drug reason. Signs and symptoms must be selected from the Signs/Symptoms list. Users cannot enter free-text entries.](#_Toc17877604)](#_Toc17877476)

31. [[To associate a date and time with a symptom (optional), click to select the symptom in the Selected Symptoms pane.](#_Toc17877604)](#_Toc17877476)
32. [[Click the Date/Time button located below the Selected Symptoms pane. CPRS displays the Select Date/Time dialog, from which you can select the date and time that the symptom first appeared.](#_Toc17877604)](#_Toc17877476)

> [[Note: If you mistakenly enter a sign or symptom but have not yet accepted it by selecting OK, select the symptom in the Selected Symptoms pane and click the Remove button located beneath the pane.](#_Toc17877604)](#_Toc17877476)

33. [[Type comments for the allergy in the Comments box.](#_Toc17877604)](#_Toc17877476)
34. [[If you have marked the allergy or adverse reaction on the patient's identification (ID) band (or if you know that someone else has), select the ID Band Marked check box.](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS activates the ID Band Marked check box only for inpatients and then only if your site's IRM staff has set a parameter indicating that your site wants to track this information. Depending on whether your IRM staff has set related parameters, if you do *not* select activated ID Band Marked check box, the system may send a bulletin notifying a mail group that the patient's allergy or adverse reaction is not marked on his or her ID band.](#_Toc17877604)](#_Toc17877476)

35. [[<span id="Method_one_eighteen" class="anchor"></span>Select OK.](#_Toc17877604)](#_Toc17877476)

> [[Note: When you click OK, CPRS generates an email bulletin to the GMRA MARK CHART mail group. The bulletin provides a reminder that the patient chart must be updated with the allergy/adverse reaction information displayed in the bulletin message.](#_Toc17877604)](#_Toc17877476)

1.  

> [[<span id="Allergy_Check_Enhancement_1" class="anchor"></span>If the newly entered allergy is related to existing pending and active orders, then the Existing Medication Allergy dialog is displayed for each order discovered, as shown below:![](cprs-user-manual-gui-version-updated-or-3-0-499/257.png)](#_Toc17877604)](#_Toc17877476)

2.  
3.  

> [[An Existing Medication Allergy will result in the NEW ALLERGY ENTERED/ACTIVE MED notification being sent to the default providers defined in the ORB PROVIDER RECIPIENTS parameter. Those providers who are able to receive the notification are displayed. Note, if a default provider recipient is unable to receive the notification they will not be listed.The person entering the new allergy will also be able to select Optional Recipients to receive the NEW ALLERGY ENTERED/ACTIVE MED notification. CPRS displays the newly entered causative agent in the Allergies/Adverse Reactions pane. If you highlight the causative agent, CPRS displays all of the information you just entered about the associated allergy or adverse reaction. CPRS also displays the letter A (for allergies) on the Postings button and the word *Allergies* in the Postings pane. If you select the word *Allergies* in the Postings pane, CPRS displays selected information about all of the patient's active allergies and adverse reactions, including the allergy or adverse reaction you just entered.](#_Toc17877604)](#_Toc17877476)

[[Take the following steps to enter a new allergy using the second of the two methods mentioned above:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Add New button. CPRS displays the Allergy Reactant Lookup dialog.](#_Toc17877604)](#_Toc17877476)

3.  

[[A user can do an allergy assessment when discontinuing a medication order:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Click on either the Meds or Orders tab. Right-click on a medication order and then, select Discontinue Order on the dropdown. If a visit location hasn't been selected, the Location for Current Activities screen will appear, and you will need to select a Visit Location and Date/Time of Visit. On the Discontinue Order screen, select Allergy/Adverse Drug Reaction on the Reason for Discontinue list, and then, click OK. ![](cprs-user-manual-gui-version-updated-or-3-0-499/259.png)](#_Toc17877604)](#_Toc17877476)

> [[Example of the Discontinue Order screen](#_Toc17877604)](#_Toc17877476)

4.  

> [[On the List of allergies currently recorded for the patient screen, click on the Yes button.![](cprs-user-manual-gui-version-updated-or-3-0-499/260.png)  
> Example of the List of allergies currently recorded for the patient screen](#_Toc17877604)](#_Toc17877476)

5.  

[[You can enter no-known-allergies (NKA) assessments for patients who have no active allergies by taking the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[CPRS offers two methods for marking allergies as having been entered in error. To mark an allergy as entered in error, the user must have the parameter OR ALLERGY ENTERED IN ERROR appropriately set.](#_Toc17877604)](#_Toc17877476)

[[Take the following steps to use the first method:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[In the Allergies/Adverse Reactions pane, place your mouse pointer over an erroneously entered causative agent and right-click to display a menu. From this menu, select Mark selected allergy as entered in error.  
> CPRS displays the Mark Allergy/Adverse Reaction Entered In Error dialog.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/262.png)](#_Toc17877604)](#_Toc17877476)

> [[*The* Mark Allergy/Adverse Reaction Entered in Error dialog](#_Toc17877604)](#_Toc17877476)

3.  

> [[If your site has enabled the Comments feature, you may (optionally) type comments in the Comments (optional) text box. Note: If your site has not enabled the *Comments* feature, CPRS disables the dialog, which in this case is named Comments (disabled).](#_Toc17877604)](#_Toc17877476)

4.  
5.  

> [[Select OK. CPRS displays an Are you Sure? dialog. If you are sure the causative agent was entered in error, click Yes. CPRS removes the causative agent from the Allergies/Adverse Reactions pane and from the list of allergies it displays when you click Allergies in the Postings pane. Note: CPRS also generates a Progress Note when an allergy is marked entered in error. When this note is signed by the user who marked the allergy as entered in error or by an administrative update user, the note will be viewable by all CPRS users.](#_Toc17877604)](#_Toc17877476)

[[Take the following steps to use the second method:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Click a causative agent (or highlight using the Tab and arrow keys and press \<Enter\>) that appears in the Allergies/Adverse Reactions pane. CPRS displays a dialog that contains detailed information about the allergy or adverse reaction. This dialog includes four buttons.](#_Toc17877604)](#_Toc17877476)

2.  

> [[Select the Entered in Error button. CPRS displays the Mark Allergy/Adverse Reaction Entered In Error dialog.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[If your site has enabled the Comments feature, you may (optionally) type comments in the Comments (optional) dialog.Select OK. CPRS displays an Are you Sure? dialog.](#_Toc17877604)](#_Toc17877476)

5.  

> [[If you are sure the causative agent was entered in error, select Yes. CPRS removes the causative agent from the Allergies/Adverse Reactions pane and from the list of allergies it displays when you select *Allergies* in the Postings pane.](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS also generates a Progress Note when an allergy is marked entered in error. When this note is signed by the user who marked the allergy as entered in error or by an administrative update user, the note will be viewable by all CPRS users.](#_Toc17877604)](#_Toc17877476)

[[Postings contain critical patient-related information about which hospital staffs need to be aware. The Postings button is visible on all tabs of the CPRS GUI window and is always located in the upper right corner of the window.](#_Toc17877604)](#_Toc17877476)

[[To view a posting using the Postings (CWAD) button, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select the Postings button (available from any tab) to display the Patient Postings dialog. ![](cprs-user-manual-gui-version-updated-or-3-0-499/263.png)](#_Toc17877604)](#_Toc17877476)

> [[The Patient Postings dialog](#_Toc17877604)](#_Toc17877476)

2.  
3.  

[[From the Patient Postings dialog, select the posting in which you are interested and view the details.When finished, select Close. To view the posting from the Cover Sheet, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[You create the following types of postings by creating progress notes using note titles that your site's IRM staff has configured for this purpose. (Check with your site's IRM staff if you don't know which note titles create which types of postings.)](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

[[Clinical Warning (which is the same as Warning) Crisis Note Directive WarningPregnantLactatingFor example, to create a posting for a crisis note, take the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

[[  
](#_Toc17877604)](#_Toc17877476)

[[The problems list on the Problems tab displays a patient's current and historical health care problems entered by clinicians. The problems list allows each identified problem to be traced through the VISTA system.](#_Toc17877604)](#_Toc17877476)

[[If a problem is service connected, the problem's service-connected status is displayed in parentheses in the Description column.](#_Toc17877604)](#_Toc17877476)

[[Service-Connected Condition Abbreviations](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 

[[SC – Service-Connected Condition AO - Agent Orange Exposure IR - Ionizing Radiation Exposure SWAC - Southwest Asia Conditions SHD – Shipboard Hazard and DefenseMST - Military Sexual Trauma HNC – Head or Neck Cancer![](cprs-user-manual-gui-version-updated-or-3-0-499/264.png)](#_Toc17877604)](#_Toc17877476)

> [[The problems list on the Problems tab can be configured to show active, inactive, both active and inactive combined, or removed problems. Treatment factors, SNOMED CT codes, and ICD codes display right after the problem text](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[Problems in CPRS are represented using two systems: Systematized Nomenclature of Medicine Clinical Terms (SNOMED CT) codes and International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) codes. SNOMED CT terminology is the designated national standard for Problem List for clinically expressing problems and to support interoperability and data exchange within VA, DoD, and external partners. ICD-10-CM codes are primarily used for reimbursement purposes. Previously, only ICD codes were used to define problems. SNOMED CT should help providers better define problems, while also mapping to ICD codes in the background.](#_Toc17877604)](#_Toc17877476)

[[Depending on the method for documenting a problem, the problem represented in SNOMED CT may or may not be linked to an ICD-10-CM code(s). If the user selects a problem from the National Problem Selection List, the problem will be linked to ICD-10-CM code(s). If the user selects a problem from within the Lexicon Utility, the problem will be linked to an R69 code (an unspecified problem).](#_Toc17877604)](#_Toc17877476)

[[The Problem List application passes all patients' problems to the Encounter Form. These problems can be viewed under the Problem List Item section of the Diagnosis tab and may be utilized for Encounter check out. However, if the problem is linked to an inactive code or represented in ICD-9-CM, the system requires the user to update the problem. Updates may require the user to link the problem to an active SNOMED CT or ICD-10-CM code.](#_Toc17877604)](#_Toc17877476)

[[You can control which problems appear on the problems list by defining specific criteria. For example, you can specify that only inactive problems associated with a specific clinic appear on the problems list.](#_Toc17877604)](#_Toc17877476)

[[To control which problems appear on the problems list, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[From the Problems tab, click any of the options listed in the View options field (Active, Inactive, Both active and inactive, or Removed) -or-](#_Toc17877604)](#_Toc17877476)

> [[select View \| Active Problems, View \| Inactive Problems, View \| Both Active/Inactive Problems, or View \| Removed Problems.](#_Toc17877604)](#_Toc17877476)

> [[The appropriate problems will appear on the problems list.](#_Toc17877604)](#_Toc17877476)

> [[If you would like to filter the problems list further, continue with step 2.](#_Toc17877604)](#_Toc17877476)

2.  

> [[Select View \| Filters…. The Problem List View Filters dialog appears.](#_Toc17877604)](#_Toc17877476)

3.  1.  
    2.  
    3.  
    4.  

> [[Select the criteria for the problems that you want to display on the problems list by doing some or all of the following: Select either Outpatient or Inpatient from the Primary View option group. Select a status from the Status drop-down list. Move the appropriate source services or source clinics to the Selected Service(s) or Selected Clinic(s) field by clicking the \> button.  
> Choose a provider from the Selected Provider drop-down list. Note: If the provider has an NPI, it will display on the screen below. See the "National Provider Identifier (NPI) Display in CPRS" section for an example of an NPI displaying on a screen.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/265.png)](#_Toc17877604)](#_Toc17877476)

> [[You can use the Problem List View Filters dialog to select the criteria for the problems that you want to display on the Problems tab](#_Toc17877604)](#_Toc17877476)

1.  
1.  
2.  

> [[Select the Problems tab. Select the New Problem -or-](#_Toc17877604)](#_Toc17877476)

> [[select Action \| New Problem…](#_Toc17877604)](#_Toc17877476)

3.  

[[If the user is set up to use the National Problem Selection List the National Problem Categories with the associated problem are displayed based on the category. If the problem is not found within the category, skip to step 4 by selecting Other Problem to bring up the Problem List Lexicon Search dialog. The Problem List Lexicon Search dialog enables users to search for the term that best describes the patient's problem. SNOMED codes are used to define the problems.](#_Toc17877604)](#_Toc17877476)

4.  
5.  

[[  
](#_Toc17877604)](#_Toc17877476)

6.  

> [[If the user does not find the desired term using the Extend Search they may choose to enter a free text entry, the user may choose to do the following actions![](cprs-user-manual-gui-version-updated-or-3-0-499/270.png)](#_Toc17877604)](#_Toc17877476)

[[To refine your search, select No and return to step 4. To use this term, select Yes and go to step 7.](#_Toc17877604)](#_Toc17877476)

> [[o Terms Found But Not Adequate: If the extended search displays terms, but not the one you want, you will need to decide whether to enter a free-text term or revise your search.](#_Toc17877604)](#_Toc17877476)

> [[To begin the search again using another term, return to step 4 and use another term to identify the problem.](#_Toc17877604)](#_Toc17877476)

> [[To enter a free-text term, select the Freetext Term button. The Unresolved Entry dialog will display as shown below:](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/271.png)](#_Toc17877604)](#_Toc17877476)

> [[This dialog shows when the system does not find any terms that match the text entered by the provider or when the provider selects the Freetext button because an adequate term is not displayed. From the Unresolved Entry dialog, the provider can choose to use the term as entered, and if needed, request that it be added as a new term](#_Toc17877604)](#_Toc17877476)

> [[To use this term, you first need to decide if you want to request that the term you entered be added as a new term. To request a new term, you need to check the Request New Term check box and add a comment if needed. If not, leave the check box unchecked. Then, to add this term to the Problem List as entered, select Yes and go to step 10.](#_Toc17877604)](#_Toc17877476)

> [[Note: If you request a new term, a bulletin is sent to a local group for review. This group will then forward the request if it concurs that a new term is needed.](#_Toc17877604)](#_Toc17877476)

> [[o No Terms Found: If the extended search finds no terms, the Unresolved Entry dialog will display as shown below. To try another search, select No and return to step 4.](#_Toc17877604)](#_Toc17877476)

> [[The New Problem form will appear.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/272.png)](#_Toc17877604)](#_Toc17877476)

> [[The New Problem form](#_Toc17877604)](#_Toc17877476)

7.  
1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  

[[To annotate a problem, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Problems tab. Select a problem from the problems list. Select Action \| Annotate... or right-click the problem and select Annotate... from the pop-up menu. Note: If you try to select a problem that has an inactive diagnosis or procedure code, you will be prompted to select a problem with an active code.](#_Toc17877604)](#_Toc17877476)

4.  
5.  

[[To change a problem on a patient's problem list, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

> [[Select the Problems tab. Select a problem from the problems list. Select Action \| Change…. Enter the desired changes. Add or remove a comment (if desired). Note: A comment can be as many as 60 characters (including spaces) in length.](#_Toc17877604)](#_Toc17877476)

6.  

> [[Select OK. Note: When you view the details of a problem, you will see who changed the problem and when.](#_Toc17877604)](#_Toc17877476)

[[To inactivate a problem on a patient's problem list, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[To remove a problem from a patient's problem list, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Problems tab. Select a problem from the problems list. Select Action \| Remove or right-click the problem and click Remove. Note: Deleted problems are not actually removed from the database. Rather, a deleted problem is flagged with a hidden tag. The hidden tag prevents the problem from appearing on any reports or lists.](#_Toc17877604)](#_Toc17877476)

[[To verify a problem on a patient's problem list, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Problems tab. Select a problem from the problems list. Select Action \| Verify or right-click the problem and click Verify on the pop up menu. Note: If you try to select a problem that has an inactive diagnosis or procedure code, you will be prompted to select a problem with an active code.](#_Toc17877604)](#_Toc17877476)

> [[The Meds tab  
> ](#_Toc17877604)](#_Toc17877476)

[[If you would like to view additional information about a medication, double click the medication entry or select a medication and choose View \| Details.](#_Toc17877604)](#_Toc17877476)

[[You can view the administration history for a medication in three ways:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Inpatient MedicationsOutpatient MedicationsClinic MedicationsClinic InfusionsNon-VA Documentation (not a required field)Supply Items (not a required field)](#_Toc17877604)](#_Toc17877476)

- 

[[Once the order has been placed, the indication will show on the Order Details.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/275.png)](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[The Indication displays on reports where the SIG is displayed. There is an example below.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/276.png)](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[When the user opens the order dialog by selecting an item from the Write Orders pane or from an order menu In the order dialog when the user selects Accept Order When the user selects a sign action—before the user signs CPRS uses three kinds of order checks: site-defined Clinical Reminder order checks, nationally released local orders checks, and remote orders checks between sites.](#_Toc17877604)](#_Toc17877476)

[[CPRS enables sites to create their own order checks based on the Clinical Reminders features. Sites will define a group of orderable items for which certain rules apply. If the rules apply to the situation, the site can define text that will display in the order check window. Sites can also set the order check to require an override.](#_Toc17877604)](#_Toc17877476)

[[Clinical Reminder order checks are defined at the site by those who normally work on the Clinical Reminders package. The set-up of a Clinical Reminders Order Check consists of two parts:](#_Toc17877604)](#_Toc17877476)

- 
- 

[[Creating a group of orderable items to which the rules should apply. Creating the rules that will be applied to the orderable item when accepting an order in CPRS. It will be possible to have the same orderable item in multiple groups. Each rule assigned to the different groups will be evaluated when placing the orderable item in CPRS. The order check groups and the rule will be stored in the Reminder Order Check file. Rules can either be defined to run against a reminder term or a reminder definition. A reminder term is beneficial when the request is to evaluate the presence of specific data (See Example \#1). A reminder definition is beneficial if you need the full functionality of a reminder definition to determine if the rule should show in the order check form (See Example \#2). The user setting up the Clinical Reminder order check can define only one or the other.](#_Toc17877604)](#_Toc17877476)

[[Note: Sites should evaluate all requests to create a Clinical Reminder Order Check to determine the importance of adding it. The more reminders that are used in an order check, the more they could affect the performance of the order check system.  
](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
1.  
2.  
3.  
4.  
5.  

[[Create a reminder definition that is applicable to the patient if the patient age is 65 or greater and the patient has a CR serum 2.0 or greater. Create an Orderable Item Group that contains all orderable items for the Glyburide. Create a Rule that contains the definition created in step 1. Set the rule to trigger the order check if the reminder definition is applicable to the patient. Create the text that should appear in the order check window. Set the order text to display the finding output in the order check text.  
](#_Toc17877604)](#_Toc17877476)

[[Clinical Reminder Order checks are defined with a testing field. If the order check is being tested, the Clinical Application Coordinator (CAC) or similar person sets this field in the Clinical Reminders order check definition to True. Then, only users who have the Clinical Reminder Test order check set to Yes will receive the order check—allowing a small number of users to test the order check before it is enabled for all users in the facility.  
](#_Toc17877604)](#_Toc17877476)

[[These nationally released order checks are available on a local CPRS system:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Allergy-Contrast Media Interaction Allergy-Drug Interaction Aminoglycoside Ordered Biochem Abnormality For Contrast Media Clinical Reminder Live Clinical Reminder Test Clozapine Appropriateness Critical Drug Interaction CT & MRI Physical Limitations Dangerous Meds For Pt \> 64 Dispense Drug Not Selected Drug Dosage Duplicate Drug Duplicate Drug Class Order Duplicate Opioid Medications Duplicate Order Error Message Estimated Creatinine Clearance Glucophage-Contrast Media Glucophage-Lab Results Lab Order Freq Restrictions Missing Lab Tests For Angiogram Procedure No Allergy Assessment Order Checking Not Available Polypharmacy Recent Barium Study Recent Oral Cholecystogram Renal Functions Over Age 65 Significant Drug InteractionSeveral parameters that each site controls determine how these order checks behave.](#_Toc17877604)](#_Toc17877476)

[[For medication orders, if a possible problem is found, CPRS displays the order check window, such as seen below when the user selects Accept:](#_Toc17877604)](#_Toc17877476)

[[<span id="Order_Checking_screenshot1" class="anchor"></span>  
![](cprs-user-manual-gui-version-updated-or-3-0-499/279.png)](#_Toc17877604)](#_Toc17877476)

[[When accepting a medication order, order checks are performed to identify potential problems](#_Toc17877604)](#_Toc17877476)

[[The Order Checking dialog separates each order check text, which is numbered using the "1 of 2, 2 of 2" type of format. If an allergy assessment has been done, the Perform Allergy Assessment button will be inactive.](#_Toc17877604)](#_Toc17877476)

[[If the clinician chooses to sign the order, CPRS displays the following dialog:  
  
<span id="RevSign_Order_Checks_Screenshot4" class="anchor"></span>  
![](cprs-user-manual-gui-version-updated-or-3-0-499/280.png)](#_Toc17877604)](#_Toc17877476)

[[In this screen capture, CPRS displays conflicts between ordered medications. Users should review each item carefully before completing the order. If an order check is larger than the cell's available space, the user can either hover with the mouse to the get the full text, use the arrow keys to highlight the order check if using the keyboard or use an accessibility product for the visually challenged. Some order checks require an override reason. These order checks are designated by the "\*Checks marked with \*\*\*\* require reason for override" text in red and the order check text in blue.  
](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

[[Allergy Contrast Media Interaction Allergy-Drug Interaction Critical Drug Interaction Duplicate Drug Class Order Duplicate Drug Order Significant Drug InteractionWhich Items Are NOT Used in Remote Order Checks?](#_Toc17877604)](#_Toc17877476)

[[Some items are not used in remote order checking because they are not stored in the HDR. Others have a high annoyance factor and therefore were not included at the request of field sites. The following items are not included in remote order checks:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[Inpatient Medications Non-VA Meds Supply items Local drugs that are not matched to the National Drug File Note: The HDR-Hx and HDR-IMS contain prescriptions with drugs that are not matched to the National Drug File (NDF). This prescription data should be used in remote order checking for duplicate drug classes. Because the National Drug File is updated regularly, these missing order checks could be resolved whenever the NDF is updated. Some drugs may never be matched, especially drugs used in research.](#_Toc17877604)](#_Toc17877476)

[[With RDI, if there is a problem with an order check, CPRS displays the information to the user potentially in two separate dialogs. The first dialog displays the allergy order checks:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 

[[It displays the facility name where the allergy was recorded, the reactant, signs, severity, and symptoms.For remote allergies, the user is required to give a reason for overriding order checks. The user is also able to write a local comment on a remote facility allergy. Allergies are sorted by clinical danger level:In cases where allergy severity and symptoms are identical in one or more order checks, a single consolidated order check will display. The sort order hierarchy is: First by Severity (Highest to Lowest).Second by Causative Agent.Last by Local and Remote locations. The second dialog displays the following information:](#_Toc17877604)](#_Toc17877476)

- 
- 

[[Medication orders include the last refill date and the quantity. Remote medication order checks display the facility name where the medication was prescribed. Local medication order checks do not display the facility name. ![](cprs-user-manual-gui-version-updated-or-3-0-499/281.png)](#_Toc17877604)](#_Toc17877476)

[[The screen capture above shows order checks with remote facility names listed.](#_Toc17877604)](#_Toc17877476)

[[  
![](cprs-user-manual-gui-version-updated-or-3-0-499/282.png)](#_Toc17877604)](#_Toc17877476)

[[If CPRS receives no data from the HDR, it will display the message "Remote Order Checking not available – checks done on local data only," as shown in the screen capture above.](#_Toc17877604)](#_Toc17877476)

[[CPRS shows this message once during an ordering session when it cannot communicate with the HDR and then does not show it again until the user begins another ordering session. However, after displaying the message, CPRS continues to attempt communication with the HDR. If CPRS reaches the HDR, remote order checks will appear when orders are placed.](#_Toc17877604)](#_Toc17877476)

[[To use remote order checking, your site must enable a parameter to access HDR data. This parameter is set for the entire facility.](#_Toc17877604)](#_Toc17877476)

[[Order checks from CPRS can happen several times during a CPRS ordering session:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[A parameter that sites can set controls how long HDR data is stored locally and is considered "fresh" and can be used for order checks before the data will be retrieved again from the HDR. The default time for this parameter is 120 minutes or two hours, but each site can change the time in that parameter.  
](#_Toc17877604)](#_Toc17877476)

[[CPRS enables users to get different views of the medications a patient is taking based on different sorting criteria. CPRS remembers the value selected by the user for the Meds tab sort. The first time a user signs into CPRS 27 the Meds tab will default to the original sort. The sort name will be display on the meds tab.](#_Toc17877604)](#_Toc17877476)

[[The first format is the existing functionality and is sorted by Location, then by Status Group, then by Stop Date/Expiration Date. The existing functionality uses the following status groups:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Pending NON VERIFIED NON-VERIFIED PENDING Active/Hold ACTIVEON CALLREFILLREINSTATEDRENEWED SUSPENDED HOLD PROVIDER HOLDDONE DRUG INTERACTIONS Expired EXPIRED Discontinued/Deleted DATE OF DEATH ENTEREDDELETEDDISCONTINUEDDISCONTINUED (EDIT)DISCONTINUED (RENEWAL)DISCONTINUED BY PROVIDERPURGE<span id="Parked_Meds_View" class="anchor"></span>PARKED  
](#_Toc17877604)](#_Toc17877476)

[[The first new view is sorted by Status Group, then by Status, then by Location, then by Drug Name. The first new view uses the following Status Groups:](#_Toc17877604)](#_Toc17877476)

- - 
  - 
  - 
  - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 

[[ACTIVEActive Refill HoldSuspendedProvider Hold On CallParked PENDING Non-verifiedDrug InteractionsIncomplete Pending DISCONTINUED Done Expired Discontinued Deleted Discontinued By Provider Discontinued (Edit) Reinstated Renewed The second new Meds tab view within CPRS is sorted alphabetically by Drug:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[Sort by drug name Status active Status recent expired (using ORCH context meds stop date) Medications will sort Inpatient, Outpatient, and Non-VA meds. Each group will sort in their own section on the CPRS Meds tab.](#_Toc17877604)](#_Toc17877476)

[[To sort the medications, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
- 
- 
- 
1.  
2.  
3.  
4.  

[[If a default medication route is defined in the orderable item file, CPRS displays only the default medication route for the Unit Dose orderable item in the medication route selection list. If there is no default medication route defined for the orderable item, CPRS displays all possible medication routes for the dosage form to the provider for selection. If there is only one possible medication route, it will be used as the default. If a medication route name or its abbreviation is not included in the selection list, a user may type it in. Also, medications that are not in the formulary display in the list with the letters "NF" after the name or synonym, which is also displayed. CPRS checks for nonformulary dosages (e.g., the VA formulary may not have a 2.5 MG pill, but it may have a 5.0 MG pill) and for non-formulary orderable items (e.g., the VA may not carry a specific kind of allergy medication).](#_Toc17877604)](#_Toc17877476)

[[See Section <u>New Clozapine Requirements</u> for more information about ordering clozapine.](#_Toc17877604)](#_Toc17877476)

[[Note: If the user attempts to order inpatient medications for an inpatient from an outpatient location, CPRS discontinues the order process and returns the user to original Orders or Meds tab display.](#_Toc17877604)](#_Toc17877476)

[[To write a new simple dose Inpatient Medications order, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select the Meds tab and then select Action \| New Medication. -or-  

> select the Orders tab and bring up the inpatient dialog by selecting the appropriate item in the Write Orders pane. CPRS displays the Medication Order dialog as show in the graphic below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/283.png)](#_Toc17877604)](#_Toc17877476)

> [[The Inpatient Medications order dialog allows you to select from a list of personal quick orders or medications](#_Toc17877604)](#_Toc17877476)

2.  

> [[Locate the desired medication or medication quick order by typing characters in the Medication field. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

3.  

> [[Select the quick order or medication name. Once the name is selected, CPRS displays a second dialog to select the items for the rest of the order. In the top field of the second dialog, the generic medication name and the synonym (usually a brand name) are displayed. The lab results for the most recent lab test associated with the selected medication are displayed in the Information field, if an associated lab test was performed within the last 365 days.](#_Toc17877604)](#_Toc17877476)

> [[Note: A CAC or ADPAC will need to set the OR CPRS LAB DISPLAY ENABLED parameter to ON to activate the lab results display at a site.](#_Toc17877604)](#_Toc17877476)

> [[To view associated lab results for Quick Orders, a TIU OBJECT must be inserted into the Quick Order. For more information, refer to the Text Integration Utility (TIU) Clinical Coordinator & User Manual. This functionality will work for generalized Quick Orders only (orders assigned to Order Menus). It is not currently implemented for personal Quick Orders.](#_Toc17877604)](#_Toc17877476)

> [[The lab results functionality will not work properly for multidivisional facilities or any sites that use different lab test names at different sites, as only one lab test name can be associated with each drug. To successfully implement this functionality, all facilities/divisions that share a VistA system must use the same name for each monitored lab test.](#_Toc17877604)](#_Toc17877476)

> [[<span id="Ind_simp_dose_Inpt_meds_graphic" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/284.png)](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS now uses a look up from Pharmacy to determine whether the selected medication is a controlled substance that requires the signature of a provider with a DEA or VA number. For controlled substances, CPRS displays a message—"Order for controlled substance could not be completed. Provider does not have a current, valid DEA# on record and is ineligible to sign the order"—as shown in the graphic below. CPRS allows orders for controlled substances only when selected providers are able to sign the orders. You may need to exit the dialog, change the provider selection, and then reenter the dialog. See *Appendix D: Error Messages and Troubleshooting* for a full list of error messages related to controlled substance ordering.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/285.png)](#_Toc17877604)](#_Toc17877476)

> [[You must have a DEA# to order certain medications](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS requires a patient to have a valid address if the selected outpatient medication is a controlled substance that requires the signature of a provider with a DEA number. For outpatient controlled substances, CPRS displays a message – "Controlled substance prescriptions require a patient address. Please contact administrative support to update patient address information." if the patient does not have a valid address. The contact information in the display may be customized using the Enter/Edit Missing ZIP Code Message option in the GUI Parameters menu.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/286.png)](#_Toc17877604)](#_Toc17877476)

> [[Controlled substance prescriptions require a patient address.](#_Toc17877604)](#_Toc17877476)

4.  

> [[In the Dosage field and select or type a dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. Also, the associated cost of the drug is displayed to the right of the dosage.](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

> [[Once a dosage is selected, any lab test results displayed in the Information field are replaced by the National Standard Orderable Item information.](#_Toc17877604)](#_Toc17877476)

5.  
6.  

> [[In the Route field, enter the appropriate route (a default route may have been set up) by either selecting one from the list or typing in a valid route. In the Schedule pane, select an existing schedule from the list or, to use a day-of-week/administration time schedule not on the list, select OTHER (you can also click the Non-Standard? link and then click OK on the dialog that displays). When the user selects a schedule, the administration times may display under the "Give additional dose now" text. The administration times will display if they have been defined for the ward or if there is a default as long as the order is not a PRN order.](#_Toc17877604)](#_Toc17877476)

7.  
1)  
2)  

> [[If you selected an existing schedule, skip to step 8. If you selected OTHER, the Order with Schedule 'OTHER' dialog appears. Take the following steps: Select one or more checkboxes by the appropriate days of the week. If the schedule requires specific administration times skip to steps c and d. To select a schedule from the list, highlight the schedule and select Add. Note: Users can assign either a schedule from the list or specific administration times, but not both. Also, because the user is specifying days of the week and a schedule, the list will contain only schedules less than 24 hours (for example, Q36H will not be in the list).](#_Toc17877604)](#_Toc17877476)

3)  
4)  

> [[To use a specific administration time, select the hour and minutes (if the user only selects the hour, the minutes will default to zero) and select Add. Repeat step c until you have entered all required administration times. Warning: The administration times in the Schedule field apply to each day of the week that is listed, such as TU-TH-SA@08002000, for example. To create a schedule such as TU@0800 TH@2000, users would have to enter two separate orders using the complex medication order dialog. Also, users may not enter a schedule that only has administration times and PRN but no days.](#_Toc17877604)](#_Toc17877476)

5)  
- 
- 
- 
6)  
7)  

> [[If you make a mistake while selecting an administration time or schedule, do one of the following to remove it: For a single administration time, highlight the hour and minutes in the Set Administration Time fields and select Remove (so to remove 08:00, you would have to select that time in the Set Administration Time fields not in the Schedule text box.) To remove the schedule, highlight the schedule and select Remove. To remove the entire schedule and begin again with step a, select Reset. Review the Schedule field. When you have the correct schedule, select OK. ![](cprs-user-manual-gui-version-updated-or-3-0-499/287.png)](#_Toc17877604)](#_Toc17877476)

> [[The *Order with Schedule 'OTHER'* dialog allows you to enter a customized day-of-week and/or administration-time schedule. The user can enter specific administration times or select a schedule from the available list](#_Toc17877604)](#_Toc17877476)

8.  

> [[Select PRN if necessary. PRN will display in the schedule field if the PRN checkbox is checked or if the schedule is defined in the Pharmacy files as a PRN schedule.](#_Toc17877604)](#_Toc17877476)

9.  
10. 
11. 

> [[<span id="Ind_simp_dose_Inpt_meds_step" class="anchor"></span>Enter an Indication. If indications have been set up, there will be items in the drop-down list, the most common indication on top. If no indications have been set up, you can type an indication Add comments (optional). CPRS displays the date and time of the expected first dose if it can determine one. (For example, CPRS cannot show an expected first dose for "on call" or schedules with PRN. On the complex tab, it will not try to determine an expected first dose after a THEN because the first item must be completed.) If you want to give an additional dose now, select the Give additional dose now check box. Note: Ensure the "Give additional dose now" and the regular order you entered do not overmedicate the patient. "Give additional dose now" is not available for ONCE, ONE-TIME, or NOW orders. It is also not available for delayed orders.](#_Toc17877604)](#_Toc17877476)

> [[When you select the Give additional dose now check box, CPRS creates two new orders. Depending on your version of CPRS, the order priority and dosing schedule may be set automatically or may require manual adjustments. The pop-up messages displayed will also vary.](#_Toc17877604)](#_Toc17877476)

1.  

> [[The dosing schedule and priority are set automatically for each order. The first order is scheduled for immediate administration (NOW) and is assigned the priority ASAP. The second order is given the priority ROUTINE and will be administered following the dosing schedule that you defined. A warning displays that is similar to the following example. Note: If your site does not use the priority ASAP, then an alternative priority (for example, STAT) will display in place of ASAP.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/288.png)](#_Toc17877604)](#_Toc17877476)

> [[Warning displayed when "Give additional dose now" is selected](#_Toc17877604)](#_Toc17877476)

1.  
2.  1.  

> [[Check the warning message to ensure that the orders you created are what you expected. If the orders are acceptable, then click OK. If not, click Cancel to clear the Give additional dose now check box. Click the drop-down arrow and then select a value for the Priority field. When Give additional dose now is selected, the Priority field is automatically set to ASAP (or a site-specific alternative). If you select a value for the Priority field before you select the Give additional dose now checkbox, a message notifies you that the selected priority will be changed to the "Give additional dose now" priority settings. ![](cprs-user-manual-gui-version-updated-or-3-0-499/289.png)](#_Toc17877604)](#_Toc17877476)

> [[CPRS displays a notification that "Give additional dose now" overrides any previously selected priority](#_Toc17877604)](#_Toc17877476)

2.  
12. 

> [[The default value of ASAP can be changed by selecting a different value from the Priority field before submitting the order. If the Priority field is empty when the order is submitted, it will revert to the default values for "Give additional dose now." Select Accept Order. Note: If you do not complete the mandatory items or if the information is incorrect, CPRS sends a message that tells you the information is incorrect and shows you the correct type of response.](#_Toc17877604)](#_Toc17877476)

13. - 
    - 
14. 

> [[(Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following: To proceed, select Accept Order. To stop the ordering process and return to the dialog, Cancel Order. Enter another medication order or click Quit. Note: CPRS requires a signature before it sends the order to pharmacy. You can either sign the order now or wait until later. When using Give additional dose now, it is recommended that you sign the order immediately to send the order to the inpatient pharmacy. You only need to sign once for both orders created when Give additional dose now is selected.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the user attempts to order inpatient medications for an inpatient from an outpatient location, CPRS discontinues the order process and returns the user to original Orders or Meds tab display.](#_Toc17877604)](#_Toc17877476)

[[In a complex dose order, the user must define specific characteristics for the order. Because the dose can affect the quantity, for example, changing certain fields may cause the quantity field to either recalculate or reset to zero to force the user to enter the quantity.](#_Toc17877604)](#_Toc17877476)

[[To write a new complex dose Inpatient Medications order, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  

[[Select the Meds tab and select Action \| New Medication. -or-](#_Toc17877604)](#_Toc17877476)

[[select the Orders tab and bring up the inpatient *Medication Order* dialog by selecting the appropriate item in the Write Orders pane.](#_Toc17877604)](#_Toc17877476)

2.  

> [[Locate the desired medication or medication quick order by typing characters in the Medication field. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

3.  

[[Select the quick order or medication name. Once the name is selected, CPRS displays a second dialog to select the items for the rest of the order. In the top field of the second dialog, the generic medication name and the synonym (usually a brand name) are displayed. The lab results for the most recent lab test associated with the selected medication are displayed in the Information field, if an associated lab test was performed within the last 365 days.](#_Toc17877604)](#_Toc17877476)

> [[Note: A CAC or ADPAC will need to set the OR CPRS LAB DISPLAY ENABLED parameter to ON to activate the lab results display at a site.](#_Toc17877604)](#_Toc17877476)

> [[To view associated lab results for Quick Orders, a TIU OBJECT must be inserted into the Quick Order. For more information, refer to the *Text Integration Utility (TIU) Clinical Coordinator & User Manual*. This functionality will work for generalized Quick Orders only (orders assigned to Order Menus). It is not currently implemented for personal Quick Orders.](#_Toc17877604)](#_Toc17877476)

> [[The lab results functionality will not work properly for multidivisional facilities or any sites that use different lab test names at different sites, as only one lab test name can be associated with each drug. To successfully implement this functionality, all facilities/divisions that share a VistA system must use the same name for each monitored lab test.](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS now uses a look up from Pharmacy to determine whether the selected medication is a controlled substance that requires the signature of a provider with a DEA or VA number. For controlled substances, CPRS displays a message—"Order for controlled substance could not be completed. Provider does not have a current, valid DEA# on record and is ineligible to sign the order"—as shown in the graphic below. CPRS allows orders for controlled substances only when selected providers are able to sign the orders. You may need to exit the dialog, change the provider selection, and then reenter the dialog. See *Appendix D: Error Messages and Troubleshooting* for a full list of error messages related to controlled substance ordering.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/290.png)](#_Toc17877604)](#_Toc17877476)

> [[You must have a DEA# to order certain medications](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS requires a patient have a valid address if the selected outpatient medication is a controlled substance that requires the signature of a provider with a DEA number. For outpatient controlled substances, CPRS displays a message – "Controlled substance prescriptions require a patient address. Please contact administrative support to update patient address information." if the patient does not have a valid address. The contact information in the display may be customized using the Enter/Edit Missing ZIP Code Message option in the GUI Parameters menu.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/291.png)](#_Toc17877604)](#_Toc17877476)

> [[Controlled substance prescriptions require a patient address](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select the Complex dose tab. Note: After you begin a complex order, you must remain on the Complex tab until you finish the order. Do not attempt to start from or switch back to the Dosage tab. If you do, all complex dosages will be erased and you will be forced to start again.](#_Toc17877604)](#_Toc17877476)

5.  

[[In the Dosage field, select or type the appropriate dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

[[Once a dosage is selected, any lab test results displayed in the Information field are replaced by the National Standard Orderable Item information.](#_Toc17877604)](#_Toc17877476)

6.  
7.  
8.  
1.  
2.  

> [[In the Route field, enter the appropriate delivery route for the medication (a default route could have been set up) by either selecting one from the list or by typing a valid route. In the Schedule field, select an existing schedule from the list or, to use a day-of week/administration time schedule not on the list, select OTHER. If you entered an existing schedule, skip to step 9. If you selected OTHER, CPRS displays the Order with Schedule 'OTHER' dialog. Take the following steps: Select one or more checkboxes by the appropriate days of the week. If the schedule requires specific administration times skip to steps c and d. To select a schedule from the list, highlight the schedule and select Add. Note: Users can assign either a schedule from the list or specific administration times, but not both. If launched from the Complex tab, the Day-of-Week Schedule builder does not display one-time schedules in the schedule list. Also, because the user is specifying days of the week and a schedule, the list will contain only schedules less than 24 hours (for example, Q36H will not be in the list).](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[To use a specific administration time, select the hour and minutes (if the user only selects the hour, the minutes will default to zero) and select Add. Repeat step c until you have entered all required administration times. Warning: The administration times in the Schedule field apply to each day of the week that is listed, such as TU-TH-SA@08002000, for example. To create a schedule such as TU@0800 TH@2000, users would have to enter two separate orders using the complex medication order dialog. Also, users may not enter a schedule that only has administration times and PRN but no days.](#_Toc17877604)](#_Toc17877476)

5.  
- 
- 
- 
6.  
7.  

> [[If you make a mistake while selecting an administration time or schedule, do one of the following to remove it: For a single administration time, highlight the hour and minutes in the Set Administration Time fields and select Remove (so to remove 08:00, you would have to select that time in the Set Administration Time fields not in the schedule text box.) To remove the schedule, highlight the schedule and select Remove. To remove the entire schedule and begin again with step a, select Reset. Review the Schedule field. When you have the correct schedule, select OK. ![](cprs-user-manual-gui-version-updated-or-3-0-499/292.png)](#_Toc17877604)](#_Toc17877476)

> [[The *Order with Schedule 'OTHER'* dialog allows you to enter a customized day-of-week and/or administration-time schedule. The user can enter specific administration times or select a schedule from the available list](#_Toc17877604)](#_Toc17877476)

9.  

[[Select PRN if necessary. PRN will display in the schedule field if the PRN checkbox is checked or if the schedule is defined in the Pharmacy files as a PRN schedule.](#_Toc17877604)](#_Toc17877476)

10. 
11. 

> [[Select the Duration field. Enter a number and select units (the default unit is days) a patient should use the specified dose. Add the appropriate conjunction: And, Then, or no conjunction for the final line. Note: The conjunction "Then" requires a duration to be added.](#_Toc17877604)](#_Toc17877476)

12. 

[[Select the Dosage field in the next row and select a dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

13. 
14. 

> [[CPRS fills in the Route and Schedule fields. If necessary, change the values in Route and Schedule fields. Enter the duration and a conjunction (or no conjunction for the final line). Note: Your site's IRM staff may have specified rules governing the status of inpatient medication orders when patients are transferred from one ward or service to another. It may have also specified the number of days an inpatient medication order remains active. Please check with your site's IRM staff for information about these rules.](#_Toc17877604)](#_Toc17877476)

15. 

> [[Repeat steps 12-14 until you have completed the complex dose. Note: You can also add or remove a row in the complex dosage. If you add a row, CPRS places the new row above the selected row. To add a row, click the gray area in front of the row and click Add Row. To delete a row, click the gray area in front of the row to be deleted and click Delete Row.](#_Toc17877604)](#_Toc17877476)

16. 
17. 

[[<span id="Ind_comples_dose_Inpt_meds_step" class="anchor"></span>Enter an Indication. If indications are defined, you can choose one from the drop-down list. If none are defined or the correct indication is not in the list, type in the appropriate indication.Add comments (optional). CPRS displays the expected date and time of the first dose. (For example, CPRS cannot show an expected first dose for "on call" or schedules with PRN. On the complex tab, it will not try to determine an expected first dose after a THEN because the first item must be completed.)](#_Toc17877604)](#_Toc17877476)

18. 
19. 
20. 
21. 

[[The default value of ASAP can be changed by selecting a different value from the Priority field before submitting the order. If the Priority field is empty when the order is submitted, it will revert to the default values for "Give additional dose now." Click Accept Order. Note: If you do not complete the mandatory items or if the information is incorrect, CPRS sends a message telling you that the information is incorrect and showing you the correct type of response.](#_Toc17877604)](#_Toc17877476)

22. 
- 
- 
23. 

[[(Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following: To proceed, select Accept Order. To stop the ordering process and return to the dialog, Cancel Order. Enter another medication order or click Quit. Note: You must sign the order before CPRS sends it to the Pharmacy package. You can either sign the order now or wait until later. When using Give additional dose now, it is recommended that you sign the order immediately to send the order to the inpatient pharmacy. You need only sign once for both orders created when Give additional dose now is selected.  
](#_Toc17877604)](#_Toc17877476)

[[To successfully write inpatient-medication orders for outpatients, the outpatients must meet at least one of the following criteria:](#_Toc17877604)](#_Toc17877476)

- 
- 
6.  [[Select the Visit tab.](#_Toc17877604)](#_Toc17877476)
7.  [[Select New.](#_Toc17877604)](#_Toc17877476)
8.  [[Select OK.](#_Toc17877604)](#_Toc17877476)

[[In addition, before you can use the Meds tab to place IMO orders, your site's IRM staff must set up the new-medication order dialog to include inpatient medications.](#_Toc17877604)](#_Toc17877476)

[[See the [<u>New Clozapine Requirements section</u>](#_New_Clozapine_Requirements) for more information about ordering clozapine.](#_Toc17877604)](#_Toc17877476)

[[Take the following steps to write IMO orders:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[Select the Meds tab From the main menu, select Action \| New Medication or click to select the area within the Inpatient Medications window, then right click and select New Medication from the shortcut menu. (You can also place inpatient-medication orders for outpatients via the Orders tab. For detailed instructions, see "Ordering Inpatient Medications for Outpatients" in the "Orders" section of this manual.) CPRS prompts you to select a location for current activities. Select a scheduled (current or future) appointment at an authorized hospital/clinic location, or create a new visit in an authorized hospital/clinic location using the default time for new visits (NOW). CPRS displays one or more new medication dialogs. These dialogs are site—and sometimes user—specific. For example, the person who manages information resources at your site may have set the ORWDX NEW MEDS parameter (which controls the new-medication order dialog) to display a list of your inpatient and outpatient quick orders.![](cprs-user-manual-gui-version-updated-or-3-0-499/300.png)](#_Toc17877604)](#_Toc17877476)

> [[New-medication dialogs can vary widely. This sample dialog enables a specific user to select from a list of his inpatient and outpatient quick orders, among other things](#_Toc17877604)](#_Toc17877476)

> [[However, the person who manages information resources at your site could also define a generic dialog for all applicable users.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/301.png)](#_Toc17877604)](#_Toc17877476)

> [[This new-medication order dialog offers a variety of options that are not user-specific](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select an inpatient medication. Once the name is selected, CPRS displays a second dialog to select the items for the rest of the order. In the top field of the second dialog, the generic medication name and the synonym (usually a brand name) are displayed.](#_Toc17877604)](#_Toc17877476)

6.  

> [[To place a simple-dose or complex-dose order for this medication, follow the steps outlined in the "Simple Dose" or "Complex Dose" sections of this manual, respectively. On the Meds tab, CPRS displays IMO orders sorted at the top of the Inpatient Medications window with corresponding authorized hospital/clinic locations in the Location column.](#_Toc17877604)](#_Toc17877476)

[[Users can also change and renew inpatient medication orders for outpatients](#_Toc17877604)](#_Toc17877476)

[[(IMO) if the user is ordering from an authorized IMO location. If the patient's location is not an authorized IMO location (even if the patient is an inpatient), users will not be able to change or renew the IMO orders. To change inpatient medication orders for outpatients, follow the instructions in the "Changing Orders" section of this manual, respectively.](#_Toc17877604)](#_Toc17877476)

[[Outpatient medication orders can be written as simple doses or complex doses. Users must enter a medication name, dosage, route, and schedule. For outpatient medications, dosage, schedule, and route can be free-text entries, but the medication must be chosen from the list of options. The route can be typed in, but to be accepted, it must be a valid route that is in the MEDICATION ROUTES file \#51.2.](#_Toc17877604)](#_Toc17877476)

[[CPRS displays unit dose routes based on the following rules:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

[[If a default medication route is defined in the orderable item file, CPRS displays only the default medication route for the Unit Dose orderable item in the medication route selection list. If there is no default medication route defined for the orderable item, CPRS displays all possible medication routes for the dosage form to the provider for selection. If there is only one possible medication route, it will be used as the default. If a medication route name or its abbreviation is not included in the selection list, a user may type it in. Also, medications that are not in the formulary display in the list with the letters "NF" after the name or synonym, which is also displayed. CPRS checks for nonformulary dosages (e.g., the VA formulary may not have a 2.5 MG pill, but it may have a 5.0 MG pill) and for non-formulary orderable items (e.g., the VA may not carry a specific kind of allergy medication).](#_Toc17877604)](#_Toc17877476)

[[To write a new simple dose Outpatient Medications order, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Locate the medication name or quick order name in the list box by typing characters in the Medication field. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

3.  

[[The lab results functionality will not work properly for multidivisional facilities or any sites that use different lab test names at different sites, as only one lab test name can be associated with each drug. To successfully implement this functionality, all facilities/divisions that share a VistA system must use the same name for each monitored lab test.  
<span id="Parked_Meds_Screenshot" class="anchor"></span>](#_Toc17877604)](#_Toc17877476)

4.  
5.  
6.  

[[Enter a Route by either selecting one from the list or typing in a valid route. Enter a Schedule (select PRN, if desired). Note: Outpatient orders for supply items do not require a route.](#_Toc17877604)](#_Toc17877476)

7.  

[[CPRS puts in the default days' supply and calculates the quantity based on the formula Days Supply x Schedule = Quantity. If necessary, highlight and change the numbers in these fields. Note: If you change a number, CPRS will attempt to recalculate the other field, if possible.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 
13. 
14. 
- 
- 

> [[Enter the number of refills. Select where the patient should pick up the medication. Select the Priority. <span id="Ind_simp_dose_outpt_meds_step" class="anchor"></span>Enter an Indication. If indications are defined, they will display in the drop-down list for you to select or you may type in an indication.You can also add a comment if desired. Select Accept Order. (Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following: To proceed, select Accept Order. To stop the ordering process and return to the dialog, Cancel Order. If you are finished ordering outpatient medications, select Quit.](#_Toc17877604)](#_Toc17877476)

> [[Note: The order must be signed before it is sent to pharmacy. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[In a complex dose order, the user must define specific characteristics for the order. Because the dose can affect the quantity, for example, changing certain fields may cause the quantity field to either recalculate or reset to zero to force the user to enter the quantity.](#_Toc17877604)](#_Toc17877476)

[[To write a new Outpatient Medications order, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Locate the medication name or quick order name in the list box by typing characters in the Medication field. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

[[Select the Complex dose tab. Note: Once you begin a complex order, you must remain on the Complex tab until you finish that order. Do not attempt to start from or switch back to the Dosage tab. If you do, all complex dosages will be erased and you will be forced to start again.](#_Toc17877604)](#_Toc17877476)

[[Once a dosage is selected, any lab test results displayed in the Information field are replaced by the National Standard Orderable Item information.](#_Toc17877604)](#_Toc17877476)

5.  

[[Select the Dosage field and select the appropriate dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

[[Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard. The tier level represents medication copayment classes for Outpatient Pharmacy charges that are dependent on the medication class. It is used to determine the charge rate for copayments.](#_Toc17877604)](#_Toc17877476)

6.  

[[Enter a Route by either selecting one from the list or typing in a valid route. Note: Outpatient orders for supply items do not require a route.](#_Toc17877604)](#_Toc17877476)

7.  
8.  
9.  

[[Select the Schedule cell and enter how often the medication should be taken (select PRN if desired). Select the Duration cell and enter a number and select units (days is the default) a patient should use the specified dose. Add the appropriate conjunction: And, Then, or no conjunction for the final line. Note: The conjunction "Then" requires a duration to be added.](#_Toc17877604)](#_Toc17877476)

10. 

[[Select in the dosage field in the next row and select a dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

11. 
12. 
13. 

[[CPRS will fill in the Route and Schedule fields. If necessary, select and change the Route and Schedule cells. Enter a duration and a conjunction (no conjunction on the final line). Repeat steps 5-12 until you have completed the complex dose. Note: You can also add or remove a row in the complex dosage. If you add a row, the new row will be placed above the selected row. To add a row, click the gray area in front of the row and click Add Row. To delete a row, click the gray area in front of the row to be deleted and click Delete Row.](#_Toc17877604)](#_Toc17877476)

14. 

[[CPRS puts in the default days supply and calculates the quantity based on the Days Supply x Schedule = Quantity. If necessary, highlight and change the number in these fields. Note: If you change a number, CPRS will attempt to recalculate the other field, if possible.](#_Toc17877604)](#_Toc17877476)

15. 
16. 
17. 
18. 

[[Enter the number of refills. Select where the patient should pick up the medication and the Priority. <span id="Ind_cmpl_dose_outpt_meds_step" class="anchor"></span>Enter an Indication. If indications are defined, they will display in the drop-down list for you to select or you may type in an indication.You can also add a comment if desired. Under certain circumstances, a check box may appear under the Days Supply field. If the medication is service-connected, make sure the box is checked.](#_Toc17877604)](#_Toc17877476)

19. 
20. 
- 
- 
21. 

[[Select Accept Order. (Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following: To proceed, select Accept Order. To stop the ordering process and return to the dialog, Cancel Order. If you are finished ordering outpatient medications, select Quit. Note: The order must be signed before it is sent to pharmacy. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[The Joint Commission on Accreditation of Healthcare Organizations (JCAHO) has indicated that all medications, including herbal supplements, over-the-counter (OTC) non-prescription medications, and medications prescribed by providers outside the VA (collectively known as "Non-VA medications") should be documented in the medical record. CPRS, Outpatient Pharmacy, and Inpatient Medications developers have made changes that enable users to enter this information into the medical record so that providers have a better picture of the medications the patient is taking and that order checks against these medications can occur.](#_Toc17877604)](#_Toc17877476)

[[Documenting Non-VA Medications will trigger the following order checks:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

> [[Duplicate Drug (shows as Duplicate Order check) Duplicate Drug Class Critical Drug Interaction Significant Drug Interaction Allergy checks Note: For Non-VA medications, inpatient orders are not checked against documented non-VA medications and the allergy check is slightly different. The duplicate drug class check will not be triggered for two pure herbal medications, such as ginger and gingko. All pure herbal medications belong to the same drug class (HA000). If these checks were made, every time a clinician entered a pure herbal medication, the user would receive a duplicate drug class warning. Allergy checks will still occur for non-VA medications that do not belong to this drug class.](#_Toc17877604)](#_Toc17877476)

[[For users to be able to document these medications through CPRS, they must be in the CPRS Orderable Items file so that they appear when the user chooses Non-VA Medications (Documentation) from the Write Orders pane. The Pharmacy patch (PSS\*1.0\*68) enables sites to mark items as Non-VA Medications. Initially, all Pharmacy orderable items that are marked as "outpatient" and are not supply items will be automatically made Non-VA medications also. Subsequently, Pharmacy coordinators can use the Pharmacy option Drug Enter/Edit \[PSS DRUG ENTER/EDIT\] to identify items as Non-VA Meds or remove the designation.](#_Toc17877604)](#_Toc17877476)

[[Note: For more information about how to get Non-VA Medications added to the appropriate file, please see "Section 5.1: Communicating New Non-VA Meds Entries to the Pharmacist" in the *Herbal/OTC/Non-VA Meds Documentation Release Notes* that will be located on the VistA Documentation Library at <http://www.va.gov/vdl> under the Outpatient Pharmacy listings.](#_Toc17877604)](#_Toc17877476)

[[Remember that documenting Non-VA Medications is not the same as placing orders. Users simply enter information to provide a more complete view of what the patient is taking. However, once the items are available in the CPRS Orderable Items file, the process for documenting Non-VA Medications is similar to entering other orders, but there are a few differences:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[Almost any CPRS user can document the Non-VA medication information. However, sites can restrict access for those holding the OREMAS key by using the OR OREMAS NON-VA MEDS parameter. For more information about this parameter, please see the *CPRS Technical Manual: GUI Version*. Electronic signature is not required for Non-VA Medication (Documentation) items. Users can document a Non-VA medication even if they only have partial information. The only required information is the non-VA or herbal medication name. The Medication name must be one that can be selected from the list. The Dosage, Route, and Schedule fields are optional and will accept free-text entries. Non-VA medications are listed separately on the orders tab and the designation Non-VA Meds (Documentation) is displayed at the beginning of the entry in the Service column of the grid. Users may pick a reason why the patient is taking the Non-VA medication. For the reason/statement that users should enter, developers sent out four reasons or statements at the package level of the parameter GUI Non-VA Med Statements/Reasons that were agreed upon by a workgroup:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[Non-VA medication not recommended by VA provider. Non-VA medication recommended by VA provider. Patient wants to buy from Non-VA pharmacy. Medication prescribed by Non-VA provider. Authorized users can enter their own reasons/statements in the parameter by entering new statements at the System or Division level for this parameter. For more information about changing this parameter, see the *CPRS Technical Manual: List Manager*.](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[If you are not already there, go to the Orders tab by either clicking Orders or pressing Ctrl + O. In the Write Orders list, select Non-VA Medications (Documentation). Note: If encounter information has not been entered, the encounter information dialog will appear before the Medication Order dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

3.  1.  

> [[In the Document Herbal/OTC/Non-VA Medications dialog, select the medication or herbal supplement by Typing a few letters of name. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

2.  

> [[Selecting the correct name or synonym (often a brand name) from the list by double-clicking it or highlighting it and pressing \<Enter\>. You may need to scroll down to find the name. Note: If you do not know other information such as dosage, route, or schedule, you may enter only the name of the medication or herbal supplement.](#_Toc17877604)](#_Toc17877476)

4.  

> [[Enter a dosage (if known). The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

5.  
6.  
7.  
8.  
9.  
10. 
11. 
12. 
13. 
- 
- 
14. 
15. 

> [[Enter a route (if known). Enter a schedule, including PRN if necessary (if known). <span id="Ind_Non_VA_meds_step" class="anchor"></span>(Not required) Enter an Indication. If indications are defined, they will display in the drop-down list for you to select or you may type in an indication.Enter any comments. If you want to enter one, select one or more Statements/Explanations as to why the patient is taking the medication or supplement (optional). Enter a start date (if known). Review the information entered in the text box at the bottom of the dialog. Place the information into the patient's record by clicking Accept Order or by tabbing to Accept Order and pressing \<Enter\>. (Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following: To proceed, select Accept Order. To stop the ordering process and return to the dialog, Cancel Order.To document additional Non-VA Medications into the patient's record, repeat steps 3-12. When you are through documenting Non-VA medications, exit the dialog using the Quit button. Note: Non-VA Meds do not require an electronic signature, but they will be presented at the end of the current CPRS session on the Sign screen. You can do the normal signing process or if you only have Non-VA meds, you might get OK and Cancel buttons on a dialog instead of the normal Sign screen. You cannot click on the checkbox in front of a Non-VA Med to deselect and not approve it. Non-VA Meds because they do not require electronic signature will be automatically entered when you click OK or enter your electronic signature.](#_Toc17877604)](#_Toc17877476)

[[When you start documenting non-VA medication information for a complex dose, you need to remain on the Complex tab until you click the Accept Order button. If you switch to the Dosage tab, all complex dosages will be erased.](#_Toc17877604)](#_Toc17877476)

[[To document Non-VA medication information for a complex dose, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Click on the Meds tab and then, click on the Action menu in the toolbar.Select Document Non-VA Meds from the Action menu.Note: If encounter information has not been entered, the encounter information dialog will appear. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

16. 
22. 
23. 

> [[In the Document Herbal/OTC/Non-VA Medications dialog, select the medication or herbal supplement from the dropdown. If you enter a few characters in the Name field, you will immediately see a list of names in the dropdown that contain those characters.Select the Complex tab.Enter the appropriate dosage in the Dosage field. Note: The dosage must begin with a numerical value (for example, 0.5). The dosage cannot begin with a decimal (for example, .5) and the ^ character is not allowed.](#_Toc17877604)](#_Toc17877476)

24. 
25. 
26. 
27. 

> [[Enter a Route by either selecting a value from the dropdown or entering a value. Select a value from the Schedule dropdown. Check the PRN checkbox, if necessary.In the Duration field, enter a numeric value and select the units a patient should use for the specified dose (day is the default).In the add/then dropdown, select a direction and a conjunction (no conjunction on the final line). Note: If you select the "then" conjunction, you are required to add a duration.](#_Toc17877604)](#_Toc17877476)

28. 
29. 
30. 
31. 

> [[In the next row, enter a dosage in the Dosage field. If necessary, change the values in the Route and Schedule fields. In the add/then dropdown, enter a duration and a conjunction (no conjunction on the final line). Repeat steps 5 through 12 until you have completed the complex dose. Note: To add a row, click on the area where you want to place the new row and then, click on the Insert Row button. To remove a row, click on the row to be deleted and then, click on the Remove Row button.](#_Toc17877604)](#_Toc17877476)

32. 
33. 
34. 
35. 
36. 
37. 
38. 
39. 

> [[Enter an Indication (optional). If indications are defined, they will display in the drop-down list or you may type in an indication.Add a comment (optional). Select one or more Statements/Explanations as to why the patient is taking the medication or supplement (optional).Enter a Start Date, if known. A Start Date can be a date in the past.Review the information entered in the textbook at the end of the dialog.Click the Accept Order button.(Conditional) If the non-VA medication may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and either click the Accept Order button or the Cancel Order button.When you finish documenting non-VA medications, click the Quit button.Note: Non-VA Meds do not require an electronic signature. At the end of the current CPRS session, you will see the Review/Sign Changes window and will be able to click on the OK or Cancel button without signing the order. After you click the OK button, you may see the Order Checks screen if there is a potential conflict between a non-VA med and an existing inpatient or outpatient order.](#_Toc17877604)](#_Toc17877476)

[[This action enables a user to release the hold that someone has placed on a medication order.](#_Toc17877604)](#_Toc17877476)

[[To release the hold on a medication, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Meds tab. Locate and highlight the medication that you want to release from being held. Select Action \| Release Hold… Note: If the order has expired, you should see a message that says, "Cannot be released from Hold. Reason: This Order has Expired."](#_Toc17877604)](#_Toc17877476)

[[Only active orders may be placed on hold. Orders placed on hold will continue to show under the ACTIVE heading on the profiles until it is removed from hold. An entry is placed in the order's Activity Log recording the person who placed/removed the order from hold and when the action was taken.](#_Toc17877604)](#_Toc17877476)

[[To place a medication on hold, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
- 
- 
- 
- 
- 
1.  1.  
    2.  
2.  
3.  
4.  

[[Click on either the Meds or Orders tab:If you clicked on the Meds tab, click on Action and then, click on New Medication. If you clicked on the Orders tab, click on Outpatient Meds in the Write Orders table.On the Location for Current Activities screen, select a Visit Location and Date/Time of Visit and click OK.On the Outpatient Medications or Medications Orders screen, fill in all required fields: Medication, Dosage, Route, Schedule, Indication, Days Supply, Quantity, Refills and Priority. In the Pick Up area, select the Park radio button. Click Accept Order. After the order has been accepted, it will be in the Pending status until the pharmacist processes the order, at which point it will become Active/Parked.To park an existing prescription, do the following:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[Click on either the Orders or Meds tab.Right-click on an active outpatient medications order and then, click on Park. On the Park Orders screen (the confirmation screen), click OK. The order will get into the Active/Parked status. To unpark a prescription, do the following:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[Click on either the Orders or Meds tab.Right-click on an Active/Parked outpatient order and then, click on Unpark – Generates a request to Fill/Refill.On the Un-Park Orders screen (the confirmation screen), click OK. An unparked order will go into an Active/Suspense status.](#_Toc17877604)](#_Toc17877476)

[[Active orders may be renewed. In addition, inpatient medication orders that have expired in the last four days and outpatient medication orders that have expired in the last 120 days may be renewed.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the original order had comments, the comments do not carry over when the user renews an order. This is to prevent comments that should only apply to the original order from mistakenly being carried forward with the renewed order.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  

> [[Click on either the Orders or Meds tab.In the Outpatient Medications or Out Meds table, right-click on an order in the Active, Active-Susp or Active-Parked status.Click Renew on the dropdown menu. If a visit location hasn't been selected, the Location for Current Activities screen will appear, and you will need to select a Visit Location and Date/Time of Visit. On the Renew Orders screen, click the order to be renewed and then, click the Change Days Supply/Quantity/Refills/Pick Up button. On the Change Refills for Outpatient Medication screen, update the Days Supply, Qty, Refills and/or Pick-Up values and click OK.  
> Note: If you edit the Days Supply, the system will attempt to update the quantity based on the formula, Days Supply x Schedule = Quantity.On the Renew Orders screen, click OK.  
> ![](cprs-user-manual-gui-version-updated-or-3-0-499/309.png)  
> Example of the Renew Orders and Change Refills for Outpatient Medication screens](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Select the order or orders you want to discontinue. Select Action \| Discontinue/Cancel. A dialog may appear asking for the clinician's name and the location (encounter information).](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select the name of the clinician (you may need to scroll through the list), select the encounter location, and then select OK. Another dialog will appear asking for the reason why the order is being discontinued.](#_Toc17877604)](#_Toc17877476)

5.  
6.  
- 
- 
- 

[[To change an order:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Select the order to highlight it. Select Action \| Change... or right-click the order and click Change.... Note: If the provider or location has not been defined, you will be prompted for that information.](#_Toc17877604)](#_Toc17877476)

4.  

> [[Complete the changes as appropriate in the dialog box that appears on the screen. Note: The original order's comments are not brought forward on a change to prevent inadvertently using a comment that was only for the original order.](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select Accept. Note: You may sign the order now or later.](#_Toc17877604)](#_Toc17877476)

[[When you select the Meds tab, you see a list of medications that have been ordered for this patient. You can get a more detailed display of each order by double clicking the order.](#_Toc17877604)](#_Toc17877476)

> [[Note: You can also review or add medication orders from the Orders tab.](#_Toc17877604)](#_Toc17877476)

[[When ordering medications, you can order Outpatient Pharmacy or Inpatient Meds, which includes IV Fluids and Unit Dose.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[Click the Meds tab. Select the outpatient medications you want to transfer. Hold down the CTRL key to select more than one medication. Hold down the Shift key and click the first and last medications to select a range. Select Action \| Transfer to Inpatient. Enter the necessary information for the first order and click Accept. Note: Provider comments are brought forward for editing if necessary. Sometimes, provider comments give needed instructions to the patient.](#_Toc17877604)](#_Toc17877476)

5.  

> [[Repeat step 4 as needed for the selected medications. Note: When finished, you can sign the orders now or wait until later.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[Select the Meds tab. Select the inpatient medications you want to transfer. Hold down the CTRL key to select more than one medication. Hold down the Shift key and click the first and last medications to select a range. Select Action \| Transfer to Outpatient.  
](#_Toc17877604)](#_Toc17877476)

> [[CPRS displays the Copy Medication Orders dialog.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/310.png)](#_Toc17877604)](#_Toc17877476)

> [[The Copy Medication Orders dialog](#_Toc17877604)](#_Toc17877476)

4.  
5.  

> [[If you would like to release the copied order(s) immediately, check the "Released copied orders immediately" option. If you would like to delay the release of the copied order(s), select one of the options in the "Delay release of copied orders until" group. Select OK. The Medication Order dialog displays.](#_Toc17877604)](#_Toc17877476)

6.  
7.  

[[Users can order a refill of outpatient medications if:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[The medication is an outpatient medication. The provider originally wrote the order with refills and there are refills remaining. The expiration date is in the past. To order an outpatient medication refill, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[Go to the Meds tab. Select the medications you wish to refill that meet the above criteria. Select Action \| Refill… or right-click on the orders and select Refill… from the popup.  
](#_Toc17877604)](#_Toc17877476)

> [[The following dialog displays. Note: The Refill Orders dialog in CPRS does not allow you to choose Park. A pharmacist would need to update the prescription to Parked when they get the refill request.  
> <span id="Refill_Orders_Dialog" class="anchor"></span>  
> ![](cprs-user-manual-gui-version-updated-or-3-0-499/311.png)](#_Toc17877604)](#_Toc17877476)

> [[In the Refill Orders dialog, CPRS displays the medications the user selected to refill and enables the user to choose the pickup method](#_Toc17877604)](#_Toc17877476)

4.  
5.  

[[The Unified Action Profile (UAP) view on the Orders tab displays existing inpatient and outpatient medication orders from the local site on a single page. Using this view, a clinician can record decisions for all orders assigned to a patient to ensure that the correct medication orders are continued for the patient upon discharge.](#_Toc17877604)](#_Toc17877476)

[[Previously, when preparations were made to discharge a patient, the clinician had to switch views from inpatient to outpatient medication forms. The UAP enables the clinician to review all medication orders at one time. This view simplifies order reconciliation and reduces the time and effort required from the clinician when making decisions on each active inpatient and outpatient order.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[From the CPRS Orders tab, click Write Delayed Orders. The Release Orders window displays. Select the Delay release of new order(s) until radio button. Select DISCHARGE from the Event Delay List.  
> Adjust the Effective Date if necessary and then click OK. ![](cprs-user-manual-gui-version-updated-or-3-0-499/312.png)](#_Toc17877604)](#_Toc17877476)

> [[Write Delayed Orders button displays the Release Orders window](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen above.](#_Toc17877604)](#_Toc17877476)

> [[The view changes to the Delayed DISCHARGE Orders view. The Discharge Patient (Delayed DISCHARGE) dialog box displays with DISCHARGE as the selected event.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/313.png)](#_Toc17877604)](#_Toc17877476)

> [[Discharge Patient (Delayed DISCHARGE) dialog box](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen above.](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select a Discharge Type (e.g., REGULAR) and then click Accept Order. The Delayed Discharge order displays on the Orders tab. The Service column displays the service "A/D/T" after the order is configured. The Delayed Discharge order remains unsigned until after the UAP review decisions are completed and all medication orders for the patient are ready to be signed.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/314.png)](#_Toc17877604)](#_Toc17877476)

> [[Unsigned Delayed Discharge Order](#_Toc17877604)](#_Toc17877476)

> [[Note: To perform the following actions, the UAP view must be turned On by a CAC or OI&T staff member. If UAP is not displayed in the View menu, then the feature is turned Off. Refer to the *CPRS Technical Manual: GUI Version* for details. <span id="remove_UAPnote" class="anchor"></span>](#_Toc17877604)](#_Toc17877476)

[[To use the UAP view to reconcile all inpatient and outpatient medications when preparing a patient for discharge:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select United Action Profile (UAP) from the View menu.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/315.png)](#_Toc17877604)](#_Toc17877476)

> [[Unified Action Profile (UAP) option displays on the View menu](#_Toc17877604)](#_Toc17877476)

> [[The Unified Action Profile view is displayed and ready for you to take action on each inpatient and outpatient medication.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/316.png)](#_Toc17877604)](#_Toc17877476)

> [[Unified Action Profile on the CPRS Orders tab](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen above.](#_Toc17877604)](#_Toc17877476)

> [[Example: Infusion Orders – ALL SERVICES view vs. UAP view](#_Toc17877604)](#_Toc17877476)

> [[The following Infusion order is displayed in the ALL SERVICES view. The asterisk indicates that the order was changed by the pharmacist.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/317.png)](#_Toc17877604)](#_Toc17877476)

> [[The ALL SERVICES view displaying the Infusion order with the asterisk and list of orderable items](#_Toc17877604)](#_Toc17877476)

> [[In the UAP view, the Infusion order components are intentionally reorganized for sorting purposes to facilitate medication reconciliation. The asterisk is hidden; the first orderable additive item in the ORDER file, INSULIN, is listed first and the Infusion is displayed in the medication list accordingly. The solution (DEXTROSE) is ignored for sorting purposes.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/318.png)](#_Toc17877604)](#_Toc17877476)

> [[UAP displaying the Infusion order without asterisk and sorted by first orderable additive item](#_Toc17877604)](#_Toc17877476)

2.  

> [[Right click on a medication order and then select an available reconciliation action from the popup list. ![](cprs-user-manual-gui-version-updated-or-3-0-499/319.png)](#_Toc17877604)](#_Toc17877476)

> [[List of reconciliation actions displayed in the UAP view](#_Toc17877604)](#_Toc17877476)

> [[Note: Infusion orders cannot be continued, changed, or renewed using UAP because CPRS does not convert inpatient infusion orders to an outpatient order when preparing for discharge. To prevent issues with discharge medication orders, these options are grayed when performing UAP medication reconciliation for an inpatient Infusion order.](#_Toc17877604)](#_Toc17877476)

3.  

> [[Complete required information in the secondary window that displays when a reconciliation action is selected. Not all selected actions will display a secondary window. Selecting certain actions, such as Change, will open the Copy Orders window. When this window displays, the Delay release of copied orders radio button is selected by default. Select DISCHARGE from the list of suggested events, and then click OK.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/320.png)](#_Toc17877604)](#_Toc17877476)

> [[Copy Orders window](#_Toc17877604)](#_Toc17877476)

> [[When DISCHARGE is selected, the view automatically reverts to](#_Toc17877604)](#_Toc17877476)

> [[Delayed Discharge Orders. Additional secondary windows, such as Outpatient Medications, open for configuring the Delayed Discharge medication order.](#_Toc17877604)](#_Toc17877476)

> [[The decision made for each inpatient and outpatient medication is displayed in the UAP "Reviewed" column. Information regarding whether an order was reviewed using the UAP, and who last reviewed it, is added to the order record in the Orders file (#100) in VistA.](#_Toc17877604)](#_Toc17877476)

> [[Note: When a reconciliation action is canceled before it is complete (for example, if you click Cancel in the Copy Orders window), then no decision is recorded for the selected medication. The action is briefly displayed in the UAP "Reviewed" column, but after processing the display toggles back to the UAP view, the UAP "Reviewed" column is cleared, and no decision is recorded in VistA.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/321.png)](#_Toc17877604)](#_Toc17877476)

> [[The UAP Reviewed column shows the decision made for a medication](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen above.](#_Toc17877604)](#_Toc17877476)

> [[After completing the UAP review, use the Discharge Meds view to see a complete list of outpatient medications prescribed for the patient at the time of discharge (refer to Using the Discharge Meds View on page 290).](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[To use the Discharge Meds view of all prescribed medications for a patient being discharged:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select Discharge Meds from the View menu on the Orders tab. ![](cprs-user-manual-gui-version-updated-or-3-0-499/322.png)](#_Toc17877604)](#_Toc17877476)

> [[Discharge Meds option displays on the View menu](#_Toc17877604)](#_Toc17877476)

> [[The Discharge Meds Review is displayed.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/323.png)](#_Toc17877604)](#_Toc17877476)

> [[Discharge Meds Review on the CPRS Orders tab](#_Toc17877604)](#_Toc17877476)

2.  
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

> [[Active Orders (including pending, recent activity) – This view includes orders that have a status of HoldFlaggedPendingActiveScheduledPartial ResultsUnreleased Renewed<span id="Parked_Orders_View" class="anchor"></span>Parked Recent activity also includes the following if their status changed in the number of hours you site defines in a system parameter:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 

[[In which display group CPRS places the IV medication orders depends on how the pharmacist finishes it. After CPRS v. 27, IV orders entered through the Infusion dialog should display under the Infusion display group, while those entered through the Unit Dose dialog should display under the Inpatient display group (Inpt. Meds). However, the key is how the pharmacist finishes the order. If the pharmacist finishes the order as a Unit Dose medication, it will display under the Inpatient display group. If finished as an IV order, then CPRS displays the order under the Infusion display group.](#_Toc17877604)](#_Toc17877476)

[[To create a specific view of the orders, users have the Custom Order View menu option. When the user selects Custom Order View, the dialog should display with the settings of the current view.](#_Toc17877604)](#_Toc17877476)

[[To view orders on the Orders tab, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Orders tab. Select View \| Active Orders (includes pending, recent activity), View \| Current Orders (active/pending status only), View \| Auto DC/Release Event Orders, View \| Expiring Orders, View \| Unsigned Orders, or View \| Recently Expired Orders. -or-](#_Toc17877604)](#_Toc17877476)

> [[Select the type of order you want to view from the View Orders pane on the left side of the Orders tab.](#_Toc17877604)](#_Toc17877476)

> [[Note: If you select View \| Auto DC/Release Event Orders the *Auto DC/Release Event Orders* dialog box appears, select the release event associated with the orders you would like to view and click OK.](#_Toc17877604)](#_Toc17877476)

> [[If you select View \| Recently Expired Orders, the parameter ORWOR EXPIRED ORDERS stores the number of hours in the past that CPRS will look for expired orders. A coordinator can set this value for your site.](#_Toc17877604)](#_Toc17877476)

> [[The appropriate orders will appear on the Orders tab.](#_Toc17877604)](#_Toc17877476)

> [[If you would like to filter the orders further, continue with step 3.](#_Toc17877604)](#_Toc17877476)

3.  

> [[Select View \| Custom Order View… The *Custom Order View* dialog box appears. The settings in the dialog should match what is currently displayed on the Orders tab.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/325.png)](#_Toc17877604)](#_Toc17877476)

> [[The Custom Order View dialog. To view Inpatient Medication for Outpatient orders, users can expand the All Services service/section and then select Clinic Orders or they can expand All Services, expand Pharmacy, and then select Clinic Orders](#_Toc17877604)](#_Toc17877476)

4.  
- 
- 
- 
- 
- 
5.  

> [[Select the criteria for the orders that you want to display on the Orders tab by taking some or all of the following steps: Select an order status from the left pane. (Click + to expand a heading.) Select a service or section from the right pane. (Click + sign to expand a heading.) If you want to limit the orders to a specific date range, select the Only List Orders Placed During Time Period checkbox and enter a from and through date. Click ![](cprs-user-manual-gui-version-updated-or-3-0-499/326.png) to choose a date from a calendar. Click Reverse Chronological Sequence if you want the oldest orders to appear at the top of the Orders tab. Click Group Orders by Service if you want the orders to be sorted according to the service they are associated with. Select OK. The orders that meet the criteria you specified on the Custom Order View dialog will appear on the Orders tab. The criteria for the displayed orders will appear above the Service column.](#_Toc17877604)](#_Toc17877476)

> [[Note: If all of the active orders are not displayed on the Orders tab, the ![](cprs-user-manual-gui-version-updated-or-3-0-499/327.png) icon appears below the Postings button (on the right side of the screen).](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> <span id="Custom_Order_View" class="anchor"></span>

> [[Note: The Custom Order View status selection screen modified an existing option and added a new option:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Unverified Inpatient by anyone previously named "Unverified by Anyone"Unverified Outpatient by anyoneWhen any option, under and including "Unverified Outpatient by anyone," is selected, it will include outpatient orders (except outpatient medications and Non-VA medications), so these patient orders are not missed. Clinic medication and infusion orders will be included in results for inpatient and outpatient views.](#_Toc17877604)](#_Toc17877476)

> [[When showing search results, the top of the Orders tab view will display the search criteria that was selected.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/328.png)](#_Toc17877604)](#_Toc17877476)

> [[The Orders tab can be customized to display specific orders](#_Toc17877604)](#_Toc17877476)

> [[Using the right-click menu on the Orders tab, if the user selects several items and the right-clicks either on the items or elsewhere in the list, CPRS displays a popup menu. When the user selects an action from the popup menu, the action applies to all selected items. For example, if the user selects three orders and selects Discontinue, the dialog appears with those three orders listed for discontinuation.](#_Toc17877604)](#_Toc17877476)

> [[However, if no items are selected (highlighted in blue) and the user right-clicks on an item, it is selected and the popup menu appears.](#_Toc17877604)](#_Toc17877476)

> [[The Orders tab popup menu includes the following items:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Details… Results Results History… Change… Change Release Event Discontinue… Refill… Renew… Sign…](#_Toc17877604)](#_Toc17877476)

[[To view the results of an order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Highlight the appropriate order. Select View \| Results. The results of the order will be displayed.](#_Toc17877604)](#_Toc17877476)

> [[Note: You can also right-click on the appropriate order and select Results… from the right-click menu.](#_Toc17877604)](#_Toc17877476)

[[To view a history of results, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Highlight the appropriate order. Select View \| Results History… The results history will be displayed. Note: You can also right-click on the appropriate order and select Results History… from the right-click menu.](#_Toc17877604)](#_Toc17877476)

[[To set a default view for the Orders tab, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Customize the Orders tab by following the steps above. Select View \| Save as Default View. The *Save Default Order View* dialog box appears.](#_Toc17877604)](#_Toc17877476)

3.  

[[Select OK. The current view will be set as the default view for the Orders tab.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[When the user opens the order dialog by selecting an item from the Write Orders pane or from an order menu. For medication orders, CPRS does allergy checking only at the moment when the user selects the orderable item.In the order dialog when the user selects Accept Order. Note: Allergy checking has been removed from Accept Order and moved to Orderable Items selection. When the user selects a sign action—before the user signs the order CPRS uses three kinds of order checks: site-defined Clinical Reminder order checks, nationally released local orders checks, and remote orders checks between sites.](#_Toc17877604)](#_Toc17877476)

[[CPRS enables sites to create their own order checks based on the Clinical Reminders features. Sites will define a group of orderable items for which certain rules apply. If the rules apply to the situation, the site can define text that will display in the order check window. Sites can also set the order check to require an override.](#_Toc17877604)](#_Toc17877476)

[[Clinical Reminder order checks are defined at the site by those who normally work on the Clinical Reminders package. The set-up of a Clinical Reminders Order Check consists of two parts:](#_Toc17877604)](#_Toc17877476)

- 
- 
1.  
2.  
3.  
4.  
5.  

> [[Create a reminder term that looks for the presence of a diagnosis of narrow angle glaucoma. (May need to look at multiple files depending on your site practice) Create an Orderable Item Group that contains all orderable items for any OTC Antihistamines. Create a Rule that contains the term created in step 1. Set the rule to trigger the order check if the reminder term is evaluated at True.Create the text that should appear in the order check window.Example of the Output in CPRS:](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/330.png)](#_Toc17877604)](#_Toc17877476)

> [[This is an example of a Clinical Reminders order check](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

> [[Create a reminder definition that is applicable to the patient if the patient age is 65 or greater and the patient has a CR serum 2.0 or greater. Create an Orderable Item Group that contains all orderable items for the Glyburide. Create a Rule that contains the definition created in step 1. Set the rule to trigger the order check if the reminder definition is applicable to the patient. Create the text that should appear in the order check window. Set the order text to display the finding output in the order check text. Example of the output in CPRS](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/331.png)](#_Toc17877604)](#_Toc17877476)

> [[This is an example of a Clinical Reminders order checks that uses a rule and contains part of the definition](#_Toc17877604)](#_Toc17877476)

> [[Description of solution: We needed a reminder definition to match patients older than 64 who had a lab test with the results greater than 2. In this example we set the rule up to display both the order check text and the definition evaluation text. The text "Glyburide Contraindicated" is the display name. The text "Avoid glyburide in patients with a calculated creatinine clearance \< 50 ml/min or a creating 2 or greater. If an oral sulfonylurea is required, consider glipizide," is defined by the site. The rest of the text is returned from the reminder definition evaluation.  
> ](#_Toc17877604)](#_Toc17877476)

[[Clinical Reminder Order checks are defined with a testing field. If the order check is being tested, the Clinical Application Coordinator (CAC) or similar person sets this field in the Clinical Reminders order check definition to True. Then, only users who have the Clinical Reminder Test order check set to Yes will receive the order check—allowing a small number of users to test the order check before it is enabled for all users in the facility.](#_Toc17877604)](#_Toc17877476)

[[These nationally released order checks are available on a local CPRS system:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Allergy-Contrast Media Interaction Allergy-Drug Interaction Aminoglycoside Ordered Biochem Abnormality For Contrast Media Clinical Reminder Live Clinical Reminder Test Clozapine Appropriateness Critical Drug Interaction CT & MRI Physical Limitations Dangerous Meds For Pt \> 64 Dispense Drug Not Selected Drug Dosage Duplicate Drug Class Order Duplicate Drug Order Duplicate Opioid Medications Duplicate Order Error Message Estimated Creatinine Clearance Glucophage-Contrast Media Glucophage-Lab Results Lab Order Freq Restrictions Missing Lab Tests For Angiogram Procedure No Allergy Assessment Order Checking Not Available Polypharmacy Recent Barium Study Recent Oral Cholecystogram Renal Functions Over Age 65 Significant Drug Interaction Several parameters that each site controls determine how these order checks behave.](#_Toc17877604)](#_Toc17877476)

[[For medication orders, if a possible problem is found, CPRS displays the order check window, such as seen below when the user selects Accept:](#_Toc17877604)](#_Toc17877476)

[[<span id="Order_Checking_screenshot3" class="anchor"></span>  
  
![](cprs-user-manual-gui-version-updated-or-3-0-499/332.png)](#_Toc17877604)](#_Toc17877476)

[[When accepting a medication order, order checks are performed to identify potential problems](#_Toc17877604)](#_Toc17877476)

[[The Order Checking dialog format separates the order check texts and each order check is numbered using the "(1 of 2)" type format. Since an allergy assessment has been performed, the Perform Allergy Assessment button is disabled.](#_Toc17877604)](#_Toc17877476)

[[If the clinician chooses to sign the order, CPRS displays the following dialog:](#_Toc17877604)](#_Toc17877476)

<span id="RevSign_Order_Checks_Screenshot5" class="anchor"></span>

- 
- 
- 
- 
- 
- 

[[Allergy Contrast Media Interaction Allergy-Drug Interaction Critical Drug Interaction Duplicate Drug Class Order Duplicate Drug Order Significant Drug Interaction  
Which Items Are NOT Used in Remote Order Checks?](#_Toc17877604)](#_Toc17877476)

[[Some items are not used in remote order checking because they are not stored in the HDR. Others have a high annoyance factor and therefore were not included at the request of field sites. The following items are not included in remote order checks:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[It displays the facility name where the allergy was recorded, the reactant, signs, severity, and symptoms.For remote allergies, the user is required to give a reason for overriding order checks. The user is also able to write a local comment on a remote facility allergy. Allergies are sorted by clinical danger level:In cases where allergy severity and symptoms are identical in one or more order checks, a single consolidated order check will display. The sort order hierarchy is: First by Severity (Highest to Lowest).Second by Causative Agent.Last by Local and Remote locations. The second dialog displays the following information:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[Beginning to write/copy/change orders – When a user selects an order menu to begin writing orders, CPRS requests some order checks, such as polypharmacy, renal function, or creatinine clearance, for example. On order acceptance – When the user selects Accept, CPRS requests the order checks. Signature of orders – When a user signs the order, CPRS requests order checks.How Long Is the Data Used?](#_Toc17877604)](#_Toc17877476)

[[A parameter that sites can set controls how long HDR data is stored locally and is considered "fresh" and can be used for order checks before the data will be retrieved again from the HDR. The default time for this parameter is 120 minutes or two hours, but each site can change the time in that parameter.](#_Toc17877604)](#_Toc17877476)

[[A quick order is a predefined order that a user can select. It has a value for some or all of the fields for the specific type of order selected. For example, on an outpatient medication order, the user might define the type of medication, dosage, route, and schedule, quantity, and number of refills. If the user does not define a value for one or more mandatory fields, CPRS will display the dialog for the user to fill in the missing values. Quick orders can be created for many different types of orders. There are two types of quick orders: personal and shared.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Fill out an order dialog for a medication, lab, or other order that you frequently place, but DO NOT select Accept. With the order dialog still up, select Options \| Save as Quick Order…. In the Add Quick Orders (type) dialog, where type is the package or type of order, such as Labs, Outpatient meds, etc., enter a name for the quick order and select OK. Note: You cannot save personal quick orders with the same name, even if the capitalization is different.](#_Toc17877604)](#_Toc17877476)

[[To manage personal quick orders, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
1.  
2.  
3.  
4.  
4.  1.  
    2.  
    3.  
5.  1.  
    2.  
    3.  
6.  

[[Shared quick orders are created in VistA by someone like a Clinical Applications Coordinator (CAC). These quick orders can be made available to all CPRS users by placing them on order menus, and can be used in order sets.](#_Toc17877604)](#_Toc17877476)

1.  

[[Navigate to the Add New Order menu and then select ANTIMICROBIALS (or the equivalent option defined by your site CAC). The ANTIMICROBIAL QUICK ORDERS menu displays. <span id="antimicrobial_quick_orders_updates" class="anchor"></span>  
![](cprs-user-manual-gui-version-updated-or-3-0-499/337.png)](#_Toc17877604)](#_Toc17877476)

2.  
3.  

[[Review the medication details and note the "Pharmacy Confirmation \#" displayed in the Comments field. This confirmation number is added automatically whenever an antimicrobial drug quick order is placed. ![](cprs-user-manual-gui-version-updated-or-3-0-499/339.png)](#_Toc17877604)](#_Toc17877476)

[[Outpatient Medications form with Pharmacy Confirmation Number](#_Toc17877604)](#_Toc17877476)

4.  
5.  

[[Although allergies and adverse reactions are not orders and CPRS does not display them on the Orders tab, you can enter allergies and adverse reactions from the Orders tab. You can also enter allergies from the Cover Sheet tab. (See "Entering Allergies" in the Assessing, Entering, and Reviewing Allergies/Adverse Reactions" section of this manual.)](#_Toc17877604)](#_Toc17877476)

[[To enter allergies or adverse reactions from the Orders tab, take the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
36. [[Select the Orders tab. Select Allergies from the Write Orders pane.](#_Toc17877604)](#_Toc17877476)

> [[The Allergy Reactant Lookup dialog appears.](#_Toc17877604)](#_Toc17877476)

> [[Note: Your site may have defined and configured other order menus to include allergy-entry dialogs. Regardless of the allergy-entry menu you select, if you haven't entered encounter information, the Location for Current Activities dialog appears before the Allergy Reactant Lookup dialog appears. You must complete the Location for Current Activities dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

2.  
37. [[Type the causative agent in the search field. (You must enter the first three letters (minimum) of the agent's name.) Select Search.](#_Toc17877604)](#_Toc17877476)

> [[Matching agents appear in the Select from one of the following items pane. If the causative agent you typed does not match any of the agents currently available for your site, CPRS displays the Causative Agent Not On File dialog, from which you can select one of the following options:](#_Toc17877604)](#_Toc17877476)

> [[Note: The patient's chart will not be updated unless you choose a causative agent that is on file.](#_Toc17877604)](#_Toc17877476)

> [[a. Yes: Use this option to request that the causative agent be added for your site. When you click Yes, CPRS displays the Enter Optional Comments dialog, which enables you to type additional comments (optional), such as the signs or symptoms that occurred as a result of contact with this causative agent, or whether you observed these symptoms firsthand. After you type your comments, click Continue. CPRS then sends to members of your site's GMRA Request New Reactant mail group a message that includes the following items:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

> [[The causative agent you attempted to enter The name of the patient for whom you attempted to make this entry Your name, title, and contact information Your comments Note: When the bulletin is sent, a message such as the following will display. This message also informs the user that the allergy was NOT entered into the patient's record.](#_Toc17877604)](#_Toc17877476)

> [["Members of your site's GMRA Request New Reactant mail group will review this message and, if appropriate, add the causative agent to your site's ALLERGIES file."](#_Toc17877604)](#_Toc17877476)

> [[  
> ](#_Toc17877604)](#_Toc17877476)

> [[Note: If your site's IRM staff has not yet added members to your site's GMRA Request New Reactant mail group, CPRS displays the following message:](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/340.png)](#_Toc17877604)](#_Toc17877476)

> [[CPRS displays this message if your IRM staff has not yet added members to the GMRA Request New Reactant mail group](#_Toc17877604)](#_Toc17877476)

2.  
3.  

> [[No: Use this option if you want to try an alternate spelling or trade name for your causative agent, or if you want to type another causative agent. Cancel: Use this option if you want to cancel your allergy order. ![](cprs-user-manual-gui-version-updated-or-3-0-499/341.png)](#_Toc17877604)](#_Toc17877476)

> [[The Causative Agent Not On File dialog](#_Toc17877604)](#_Toc17877476)

38. [[If the causative agent you typed matches an agent that is currently available for your site, select the agent. (Click + to expand a heading.)](#_Toc17877604)](#_Toc17877476)

> [[Note: With CPRS GUI 24 or later, you may not add free-text causative agents. If you select an item under the "Add new free-text allergy" heading, CPRS displays the Causative Agent Not On File dialog. (See Step 4 above.)](#_Toc17877604)](#_Toc17877476)

39. [[Select OK.](#_Toc17877604)](#_Toc17877476)

> [[  
> ](#_Toc17877604)](#_Toc17877476)

> [[The Enter Allergy or Adverse Reaction dialog appears.<span id="enter_allergy_updated_orders_tab" class="anchor"></span>](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/342.png)  
> The Enter Allergy or Adverse Reaction dialog](#_Toc17877604)](#_Toc17877476)

> [[Note: You can view a patient's current allergies or adverse reactions by clicking the Active Allergies button. Also, CPRS no longer allows the user to change the allergy Originator.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will display on the screen above. See the "National Provider Identifier (NPI) Display in CPRS" section for an example of an NPI displaying on a screen.](#_Toc17877604)](#_Toc17877476)

40. [[Use the Observed or Historical option button to indicate whether the entry is for an observed or historical allergy, respectively. (When you point your mouse at either of these buttons, CPRS displays a hover hint explaining the observed and historical options.)](#_Toc17877604)](#_Toc17877476)

> [[Note: Observed or Historical used to have a default, but the user must now select the appropriate choice. CPRS does not allow you to select future dates for <span id="Remove_observed" class="anchor"></span>allergy/adverse reaction entries.](#_Toc17877604)](#_Toc17877476)

> [[Note: When you select Observed for a drug reaction, CPRS generates a Progress Note. Once this note is signed by the user entering the allergy or by an administrative update user, the note will be viewable by all users.](#_Toc17877604)](#_Toc17877476)

41. [[Select the Nature of Reaction (Allergy, Pharmacological, or Unknown).](#_Toc17877604)](#_Toc17877476)

> [[The Nature of Reaction (also known as mechanism) can be Allergy, Pharmacologic, or Unknown. An allergic reaction occurs because the patient is sensitive to a causative agent, regardless of the amount the patient is exposed to. A pharmacologic (non-allergic) reaction occurs when the patient is sensitive to an agent under certain conditions, such as exposure to a large amount. Unknown is provided if you are not sure what mechanism to enter.](#_Toc17877604)](#_Toc17877476)

> [[Note: Allergies are a subset of the world of adverse reactions. All allergies are adverse reactions, but not all adverse reactions are allergies.](#_Toc17877604)](#_Toc17877476)

42. [[<span id="Historical_allergy_updates_1" class="anchor"></span>If you are entering an observed or historical allergy, use the Reaction Date/Time and Severity boxes to select a reaction date, time, and severity. These are required for observed but optional for historical allergies. (When the Severity box is visible, CPRS displays a ? button next to it. If you click this button, CPRS displays text that provides information about available severity selections.)](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS does not allow you to enter future dates for observed reactions.](#_Toc17877604)](#_Toc17877476)

43. [[Using the Signs/Symptoms box, select one or more signs or symptoms. The signs and symptoms you select appear in the Selected Symptoms pane.](#_Toc17877604)](#_Toc17877476)

> [[<span id="historical_allergies" class="anchor"></span>Note: You must enter at least one Sign/Symptom or enter a comment of at least four characters when documenting a historical allergy/adverse drug reason.](#_Toc17877604)](#_Toc17877476)

44. [[To associate a date and time with a symptom optional), click to select the symptom in the Selected Symptoms pane.](#_Toc17877604)](#_Toc17877476)
45. [[Select the Date/Time button located below the Selected Symptoms pane.](#_Toc17877604)](#_Toc17877476)

> [[CPRS displays the Select Date/Time dialog, from which you can select the date and time that the symptom first appeared.](#_Toc17877604)](#_Toc17877476)

> [[Note: If you mistakenly entered a sign or symptom but have not yet accepted it by selecting OK, select the symptom in the Selected Symptoms pane and click the Remove button located beneath the pane.](#_Toc17877604)](#_Toc17877476)

46. [[Type comments for the allergy in the Comments box.](#_Toc17877604)](#_Toc17877476)
47. [[If you have marked the allergy or adverse reaction on the patient's identification (ID) band (or if you know someone else has), select the ID Band Marked check box.](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS activates the ID Band Marked check box only for inpatients and then only if your site's IRM staff has set a parameter indicating your site wants to track this information. Depending on whether your IRM staff has set related parameters, if you do *not* select activated ID Band Marked check box, the system may send a bulletin notifying a mail group that the patient's allergy or adverse reaction is not marked on his or her ID band.](#_Toc17877604)](#_Toc17877476)

48. [[Select OK.](#_Toc17877604)](#_Toc17877476)

> [[Note: When you click OK, CPRS generates an email bulletin to the GMRA MARK CHART mail group. The bulletin provides a reminder that the patient chart must be updated with the allergy/adverse reaction information displayed in the bulletin message.](#_Toc17877604)](#_Toc17877476)

4.  

> [[<span id="Allergy_Check_Enhancement_2" class="anchor"></span>If the newly entered allergy is related to existing pending and active orders, then the Existing Medication Allergy dialog is displayed for each order discovered, as shown in the screenshot below:![](cprs-user-manual-gui-version-updated-or-3-0-499/343.png)](#_Toc17877604)](#_Toc17877476)

5.  
6.  

> [[An Existing Medication Allergy will result in the NEW ALLERGY ENTERED/ACTIVE MED notification being sent to the default providers defined in the ORB PROVIDER RECIPIENTS parameter. Those providers who are able to receive the notification are displayed. Note, if a default provider recipient is unable to receive the notification they will not be listed.The person entering the new allergy will also be able to select Optional Recipients to receive the NEW ALLERGY ENTERED/ACTIVE MED notification.Note: Although CPRS does not display allergy-related assessments on the Orders tab, you can also enter an assessment of no known allergies (NKA) from the Orders tab.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[To enter a no-known allergies assessment from the Orders tab, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Orders tab. Select Allergies from the Write Orders pane. The Allergy Reactant Lookup dialog appears.](#_Toc17877604)](#_Toc17877476)

> [[Note: Your site may have defined and configured other order menus to include allergy-entry dialogs. Regardless of the allergy-entry menu you select, if you haven't entered encounter information, the Location for Current Activities dialog appears before the Allergy Reactant Lookup dialog appears. You must complete the Location for Current Activities dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[Select the No Known Allergies check box in the lower portion of the dialog box. Select OK. Note: You can also enter a no-known-allergies assessment from the Cover Sheet tab.  
> ](#_Toc17877604)](#_Toc17877476)

1.  
- [[The NPO orderable item will be added to the Auto-DC Rules with the CPRS v31b installation. With this change, the auto-DC rules will prevent the discontinuation of the NPO diet orders for the following event types:Specialty transfer (S)](#_Toc17877604)](#_Toc17877476)
- [[OR (O)](#_Toc17877604)](#_Toc17877476)
- [[Transfer (T)](#_Toc17877604)](#_Toc17877476)

> [[and the NPO diet remains intact.](#_Toc17877604)](#_Toc17877476)

2.  
3.  
4.  
5.  
6.  

[[When NPO diet orders are attempted to be manually discontinued, CPRS prevents that action from being taken and displays the dialog box to the user with text "NPO Diet cannot be discontinued."CPRS disallows all diet orders to have an Expiration Date/Time when ordered and prevent automatic reinstatement of a previous diet. If a new diet order is desired, a new diet must be ordered to replace the active diet order.When ordering NPO, if a patient is currently on tube-feeding, the provider is displayed the dialog box "The patient currently has an active tubefeeding order \<display the current tube-feeding order here\>"The Cancel Future Order Prompt from the tubefeeding order dialog has been removed. A conversion routine has been created to remove the prompt from any Quick Order. Additionally, Quick Orders will no longer allow the features of Auto Accept or Verify.Accepting a tubefeeding order will prompt one of two different messages depending on the current diet status of the patient. If there is no existing order, the user will be prompted to enter a new diet order. If an existing diet order is present, the user will be prompted to keep the current diet or enter a new diet order.](#_Toc17877604)](#_Toc17877476)

[[The Nutrition and Food Service (N&FS) VistA package manages all diet-related order processing. The auto-discontinue process cannot discontinue active diet orders.](#_Toc17877604)](#_Toc17877476)

[[If the diet is to be replaced, then a new diet should be ordered.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[Also, the rules for auto-discontinuing (auto-dc) orders can be affected by how different VistA packages handle discontinuing and how the package communicates with CPRS. Depending on the set up and parameters, the results may be different that a user might expect.](#_Toc17877604)](#_Toc17877476)

[[Note: If discharging/readmitting patients the Nutrition & Food Service package will auto-dc diet orders upon discharge. Plan to print diet lists pre-discharge so that patient's current diet and standing orders can be manually re-entered/re-ordered upon admission.](#_Toc17877604)](#_Toc17877476)

#### [[To place a regular diet order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane. -or- select View \| Active Orders (includes pending, recent activity). Select Diet in the Write Orders list box. If there is a conflict, ensure that the order you are entering will not create a problem with a current or delayed diet order. The Diet Order dialog box appears.](#_Toc17877604)](#_Toc17877476)

> [[Note: The diet order may be labeled differently or may not be available from your Write Orders list box.](#_Toc17877604)](#_Toc17877476)

> [[Note: The encounter information dialog may appear before the Diet Order dialog if you have not entered encounter information. If the encounter information dialog appears, enter the necessary information and select OK.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/346.png)](#_Toc17877604)](#_Toc17877476)

> [[The Diet Order dialog allows you to order several different types of diets](#_Toc17877604)](#_Toc17877476)

5.  

> [[Choose a diet from the Available Diet Components list box on the Diet tab. (Quick orders are at the top of the list). The component that you select will be displayed in the Selected Diet Components field. You can remove the component by selecting it and clicking Remove.](#_Toc17877604)](#_Toc17877476)

6.  - 
    - 
    - 
7.  
8.  
9.  

> [[Enter the effective date and time and the expiration date and time by doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001). entering a date formula (e.g. t-200). clicking the ![](cprs-user-manual-gui-version-updated-or-3-0-499/347.png) button to bring up a calendar. Select a delivery method from the Delivery field. Type in any special instructions. Select Accept Order. Note: The order must be signed before it is sent. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[To place a tube feeding diet order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane. -or-](#_Toc17877604)](#_Toc17877476)

> [[select View \| Active Orders (includes pending, recent activity).](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[Select Diet in the Write Orders list box. If there is a conflict, ensure that the order you are entering will not create a problem with a current or delayed diet order. The Diet Order dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[Note: The diet order may be labeled differently or may not be available from your Write Orders field.](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog appears before the *Diet Order* dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select the Tube feeding tab. ![](cprs-user-manual-gui-version-updated-or-3-0-499/348.png)](#_Toc17877604)](#_Toc17877476)

> [[The Tube feeding tab on the *Diet Order* dialog](#_Toc17877604)](#_Toc17877476)

6.  
7.  

> [[Select a tube feeding product from the list. Select a strength and a quantity from the grid on the right side of the dialog. CPRS will automatically complete the Amount field if it needs to multiply as a result of the schedule. If there is a problem with the Quantity, CPRS displays a dialog to help the user know how to enter an acceptable value:](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/349.png)](#_Toc17877604)](#_Toc17877476)

> [[Note: You can remove a product by selecting the product and clicking Remove.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 

[[Early/Late Tray orders must be associated with an existing diet order. Once these orders have been placed, they are separate from the order with which they are associated. These orders do not discontinue automatically if the existing order is discontinued.](#_Toc17877604)](#_Toc17877476)

[[To place an early / late tray diet order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[Select the Orders tab. Select the active orders view from the View Orders pane -or- select View \| Active Orders (includes pending, recent activity). Select Diet in the Write Orders list box.  
](#_Toc17877604)](#_Toc17877476)

4.  

> [[If there is a conflict, ensure that the order you are entering will not create a problem with a current or delayed diet order. The *Diet Order* dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[Note: The diet order may be labeled differently or may not be available from your Write Orders list box.](#_Toc17877604)](#_Toc17877476)

> [[Note: The encounter information dialog may appear before the Diet Order dialog if you have not entered encounter information. If the encounter information dialog appears, enter the necessary information and click OK.](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select the Early / Late Tray tab. ![](cprs-user-manual-gui-version-updated-or-3-0-499/350.png)](#_Toc17877604)](#_Toc17877476)

> [[The Early / Late Tray tab](#_Toc17877604)](#_Toc17877476)

6.  

[[Select Breakfast, Lunch, or Evening from the Meal option group. The appropriate meal times will appear in the Meal Times option group.](#_Toc17877604)](#_Toc17877476)

7.  
8.  
- 
- 
- 
9.  
10. 

[[To place an isolations/precautions order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane –or-](#_Toc17877604)](#_Toc17877476)

> [[select View \| Active Orders (includes pending, recent activity).](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[Select Diet in the Write Orders list box. If there is a conflict, ensure that the order you are entering will not create a problem with a current or delayed diet order. The *Diet Order* dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[Note: The diet order may be labeled differently or may not be available from your Write Orders field.](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog appears before the *Diet Order* dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select the Isolations / Precautions tab. ![](cprs-user-manual-gui-version-updated-or-3-0-499/352.png)](#_Toc17877604)](#_Toc17877476)

> [[The Isolations / Precautions tab on the Diet Order dialog box](#_Toc17877604)](#_Toc17877476)

6.  
7.  
8.  

[[To place an additional diet order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. Select the active orders view from the View Orders pane -or-](#_Toc17877604)](#_Toc17877476)

[[select View \| Active Orders (includes pending, recent activity).](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  

[[Select the Additional Order tab. ![](cprs-user-manual-gui-version-updated-or-3-0-499/353.png)](#_Toc17877604)](#_Toc17877476)

[[The Additional Diet Order tab](#_Toc17877604)](#_Toc17877476)

6.  
7.  
1.  
2.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane -or-](#_Toc17877604)](#_Toc17877476)

> [[select View \| Active Orders (includes pending, recent activity).](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  

> [[Select Dietetic Orders from the Write Orders pane. Select Outpatient Recurring Meal. Select the appropriate diet under Available Diets or if the default is correct, you may simply use it. Select the appropriate time (Breakfast, Lunch, or Dinner) under Recurring Meal. The default is none selected.](#_Toc17877604)](#_Toc17877476)

7.  
8.  
9.  
10. 
11. 
12. 
13. 
1.  
2.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane -or-](#_Toc17877604)](#_Toc17877476)

> [[select View \| Active Orders (includes pending, recent activity).](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  
7.  
8.  
9.  
10. 

[[Select Dietetic Orders from the Write Orders pane. Select the Outpatient Special Meal menu item. Select the appropriate diet under Available Diets, or if the default is correct, you may simply use it. Select the appropriate time (Breakfast, Lunch, or Dinner) under Recurring Meal. The default is none selected. Select the method of Delivery. Review the order text in the field at the bottom of the dialog for accuracy. Select Accept Order. When finished, select Quit.](#_Toc17877604)](#_Toc17877476)

[[Outpatient tube feeding orders must be associated with a recurring meal. If no recurring meal has been ordered for the selected patient, CPRS displays a message informing the user and the user cannot order tube feeding.](#_Toc17877604)](#_Toc17877476)

[[To place a tube feeding diet order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane. -or- select View \| Active Orders (includes pending, recent activity).Select Dietetic Orders in the Write Orders list box. The Diet Order dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[Note: The diet order may be labeled differently or may not be available from your Write Orders field.](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog appears before the *Diet Order* dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select the Tube feeding tab. ![](cprs-user-manual-gui-version-updated-or-3-0-499/356.png)](#_Toc17877604)](#_Toc17877476)

> [[The Tube feeding tab on the *Diet Order* dialog](#_Toc17877604)](#_Toc17877476)

5.  
6.  

> [[Select a tube feeding product from the list.  
> Enter strength and a quantity in the grid on the right side of the dialog.CPRS will automatically complete the Amount field if it needs to be multiplied as a result of the schedule. If there is a problem with the Quantity, CPRS displays a dialog to help the user know how to enter an acceptable value:](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/357.png)](#_Toc17877604)](#_Toc17877476)

> [[Note: You can remove a product by selecting the product and clicking Remove.](#_Toc17877604)](#_Toc17877476)

7.  
8.  
9.  
10. 
1.  
2.  
3.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane -or- select View \| Active Orders (includes pending, recent activity). Select Dietetic Orders in the Write Orders list box. The *Diet Order* dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[Note: The diet order may be labeled differently or may not be available from your Write Orders list box.](#_Toc17877604)](#_Toc17877476)

> [[Note: The encounter information dialog may appear before the Diet Order dialog if you have not entered encounter information. If the encounter information dialog appears, enter the necessary information and select OK.](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select the Early / Late Tray tab. ![](cprs-user-manual-gui-version-updated-or-3-0-499/358.png)](#_Toc17877604)](#_Toc17877476)

> [[The Early / Late Tray tab](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select Breakfast, Lunch, or Evening from the Meal option group. The appropriate meal times display in the Meal Times option group.](#_Toc17877604)](#_Toc17877476)

6.  
7.  
8.  

[[To place an isolations / precautions order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane -or- select View \| Active Orders (includes pending, recent activity). Select Dietetic Orders in the Write Orders list box. The *Diet Order* dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[Note: The diet order may be labeled differently or may not be available from your Write Orders field.](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog appears before the *Diet Order* dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select the Isolations / Precautions tab. ![](cprs-user-manual-gui-version-updated-or-3-0-499/359.png)](#_Toc17877604)](#_Toc17877476)

> [[The Isolations / Precautions tab on the *Diet Order* dialog box](#_Toc17877604)](#_Toc17877476)

5.  
6.  
7.  

[[To place an additional order for outpatient meals, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane -or- select View \| Active Orders (includes pending, recent activity). Select Dietetic Orders in the Write Orders list box. The Diet Order dialog box will appear](#_Toc17877604)](#_Toc17877476)

> [[Note: The diet order may be labeled differently or may not be available from your Write Orders field.](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog appears before the *Diet Order* dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select the Additional Order tab. ![](cprs-user-manual-gui-version-updated-or-3-0-499/360.png)](#_Toc17877604)](#_Toc17877476)

> [[The Additional Diet Order tab](#_Toc17877604)](#_Toc17877476)

5.  
6.  
7.  

[[Using CPRS, providers can order inpatient and outpatient medications with simple doses or complex doses. Providers can place medications orders for unit dose or infusion orders for inpatients. Also, CPRS enables providers to quickly order medications that will be given in clinics.](#_Toc17877604)](#_Toc17877476)

[[There are a few items that deal with how CPRS works that providers need to be aware of when ordering medications, such as](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[the need for inpatient mediations to have a valid schedule, including the option to use the schedule builder a possible error if there is mismatch between the CPRS order number and the pharmacy order number how CPRS displays unit dose routes how CPRS displays non-formulary drugs requirements for Clozapine treatmentThis section then goes through how to order medications for inpatients, outpatients, and patients seen in clinic. The various sections will also include how to write medication orders for unit dose and infusion orders.](#_Toc17877604)](#_Toc17877476)

[[Inpatient medication orders now require a valid schedule. If users do not find the appropriate schedule in the list, they can choose to create a day-of week/administration time schedule using the new Schedule Builder. This feature also works for renewing and changing inpatient medication orders. The procedure for ordering medications is described below.](#_Toc17877604)](#_Toc17877476)

[[Note: Because a valid schedule is required, if you attempt to modify an existing medication order that does not have a valid schedule, you will receive a message box stating that and will have to enter a valid schedule.](#_Toc17877604)](#_Toc17877476)

[[When a user takes actions on an order, such as renewing, changing, or discontinuing it, an infrequent error sometimes occurs where the order number in CPRS and the order in Pharmacy do not match. In this case, CPRS displays a warning that there is an "invalid pharmacy order number" and instructing the user to contact someone in the Pharmacy service to complete the action.](#_Toc17877604)](#_Toc17877476)

[[CPRS displays unit dose routes based on the following rules:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

[[Also, medications that are not in the formulary display in the list with the letters "NF" after the name or synonym, which is also displayed. CPRS checks for nonformulary dosages (e.g., the VA formulary may not have a 2.5 MG pill, but it may have a 5.0 MG pill) and for non-formulary orderable items (e.g., the VA may not carry a specific kind of allergy medication).](#_Toc17877604)](#_Toc17877476)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 20%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc17877476"><span><strong>ANC Level</strong></span></a></th>
<th><a href="#_Toc17877476"><span><strong>ANC Monitoring</strong></span></a></th>
<th><a href="#_Toc17877476"><span><strong>Frequency of ANC lab tests</strong></span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc17877476"><span>Normal range</span></a></td>
<td><a href="#_Toc17877476"><span>ANC ≥ 1500 cmm</span></a></td>
<td><p><a href="#_Toc17877476"><span>Weekly (W) for patients 1 – 6 months on therapy</span></a></p>
<p><a href="#_Toc17877476"><span>Bi-weekly (B) for patients 6 – 12 months on therapy</span></a></p>
<p><a href="#_Toc17877476"><span>Monthly (M) for patients &gt;12 months on therapy</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>Mild neutropenia</span></a></td>
<td><a href="#_Toc17877476"><span>1000 – 1499 cmm</span></a></td>
<td><a href="#_Toc17877476"><span>ANC labs 3 times weekly until ANC stabilizes to 1500 cmm or greater</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>Moderate neutropenia</span></a></td>
<td><a href="#_Toc17877476"><span>500 – 999 cmm</span></a></td>
<td><a href="#_Toc17877476"><span>ANC labs Daily until ANC stabilizes to 1000 cmm or greater, then 3 times weekly until ANC stabilizes to 1500 cmm or greater</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>Severe neutropenia</span></a></td>
<td><a href="#_Toc17877476"><span>&lt; 500 cmm</span></a></td>
<td><a href="#_Toc17877476"><span>ANC labs Daily until ANC stabilizes to 1000 cmm or greater, then 3 times weekly until ANC stabilizes to 1500 cmm or greater</span></a></td>
</tr>
</tbody>
</table>

[[Note: The ANC unit of measure is expressed as cells per cubic millimeter (cmm) which is equivalent to cu mm, mm<sup>3</sup> or µL.](#_Toc17877604)](#_Toc17877476)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc17877476"><span>Absolute Neutrophil Count (ANC) is lab test of choice</span></a></th>
<th><p><a href="#_Toc17877476"><span>Per the REMS document, "the WBC count is required in order to calculate the ANC; however, ANC is a more relevant indicator of drug-induced neutropenia than WBC count."</span></a></p>
<p><a href="#_Toc17877476"><span>New and enhanced functionality is based on the presence of an ANC result in the last 7 days.</span></a></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc17877476"><span>ANC less than 1000 cmm</span></a></td>
<td><a href="#_Toc17877476"><span>The FDA recommends that clozapine treatment be discontinued if the ANC is less than 1000 cmm; however, with correct documentation and justification by the provider, the NCCC Director has the discretion to continue treatment through a National Override.</span></a></td>
</tr>
</tbody>
</table>

- 
- 
- 

[[Patients on a 7-day monitoring frequency have no refills available. Patients on a 14-day monitoring frequency can receive a full 14-day supply or a 7-day supply and ONE refill. Patients on a 28-day monitoring frequency can receive EITHER a full 28day supply, or a 14-day supply and ONE refill, or a 7-day supply and THREE refills. CPRS now prevents the user from renewing outpatient and inpatient clozapine orders.](#_Toc17877604)](#_Toc17877476)

[[<span id="ClozapineRenewal" class="anchor"></span>Note: Clozapine orders should not be renewed and each order for clozapine should be entered as a new order. Renewal of clozapine is not allowed in CPRS from the Orders tab of the chart and renew is also blocked in the VistA Pharmacy Software. CPRS currently allows clozapine renewal from the CPRS Meds tab. This is a known issue and users should not attempt to renew orders for clozapine.](#_Toc17877604)](#_Toc17877476)

[[The FDA defines Normal – sometimes referred to as "safe" or "passing" ANC results – as equal to or greater than 1500 cmm. When the system identifies that the ANC results are Normal and a matching WBC is present, the provider completes the prescription/order which is sent as a Pending Order to pharmacy. There are no message updates in CPRS for a Normal ANC result.](#_Toc17877604)](#_Toc17877476)

[[The FDA defines Mild neutropenia as an ANC result from 1000 to 1499 cmm. New ANC lab test monitoring guidelines for Mild neutropenia are presented to the ordering provider in a new CPRS message:](#_Toc17877604)](#_Toc17877476)

[[Test ANC labs 3x weekly until levels stabilize to greater than or equal to 1500 cmm.](#_Toc17877604)](#_Toc17877476)

[[When a National Override for Moderate or Severe Neutropenia has been approved by the NCCC and is in effect, modified CPRS screens display, including instructions for testing ANC.](#_Toc17877604)](#_Toc17877476)

1.  

> [[Non-emergency If this is not an emergency, the provider will request a National Override to dispense the clozapine at the patient's normal frequency. When the National Override is authorized and recorded in the local VistA system, the provider reenters the order and a Pending prescription/order to dispense clozapine at the patient's normal frequency is sent.](#_Toc17877604)](#_Toc17877476)

> [[For example, this may be used when:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
2.  

> [[The patient's last blood test was done at another facility and isn't in the local VistA system, but the provider has seen the results The provider feels it is unnecessary – perhaps the patient is at end of life or some other medical condition – and there is no need to keep drawing blood Emergency 4-day supply – Special Conditions Local Override In an emergency where a 4-day supply is needed, the provider may choose to use a Special Conditions Local Override which optionally allows a one-time 4-day emergency supply to be dispensed for specific prescriber-approved reasons.](#_Toc17877604)](#_Toc17877476)

> [[Note: A written prescription or order is *required*. Special Conditions Local Override is not supported in CPRS – no Pending Order is available.](#_Toc17877604)](#_Toc17877476)

[[If the patient is an Outpatient, the prescriber-approved reason must be one of the following:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[Weather-related conditions Mail order delay Inpatient going on leave If the patient is an Inpatient, the prescriber-approved reason will be:](#_Toc17877604)](#_Toc17877476)

> [[1. IP Order Override with Outside Lab Results](#_Toc17877604)](#_Toc17877476)

> [[When there is No ANC result for the last 7 days, a new CPRS screen displays notifying the provider of the missing results. The top part of the new CPRS message indicates the option to request a National Override when the condition is not an emergency and clozapine is to be dispensed at the patient's normal frequency.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/361.png)](#_Toc17877604)](#_Toc17877476)

> [[If this is an emergency, the bottom part of the new CPRS message is dependent on whether this is an Outpatient or and Inpatient.  
> ](#_Toc17877604)](#_Toc17877476)

[[If this is an Outpatient, the second part of the message is to instruct the provider to write a prescription and include an approved reason from the list.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/362.png)](#_Toc17877604)](#_Toc17877476)

[[If this is an Inpatient, the second part of the message is to instruct the provider to write an order and include the single approved reason – IP Order Override with Outside Lab Results.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/363.png)](#_Toc17877604)](#_Toc17877476)

[[When there is an ANC result in the last 7 days but no matching WBC, regardless of whether it is a normal result or indicates mild or moderate to severe neutropenia, the system will address the 'No Matching WBC' condition first. A warning message to the provider will require a National Override in order to dispense clozapine. The system can only address one condition at a time.](#_Toc17877604)](#_Toc17877476)

[[Note: A Matching WBC result is collected at the same draw date/time as the ANC.](#_Toc17877604)](#_Toc17877476)

[[An Emergency Registration Override is typically warranted for the following reasons:](#_Toc17877604)](#_Toc17877476)

49. [[The patient has a current NCCC registration at another VistA facility](#_Toc17877604)](#_Toc17877476)
    - 
    - 
50. [[Inpatient transferred from another facility Outpatient from another facility becomes an inpatient The patient has never been registered at the local facility](#_Toc17877604)](#_Toc17877476)
51. [[The patient status has changed from Active to Discontinued](#_Toc17877604)](#_Toc17877476)
52. [[An Outpatient with a prescription that had previously been filled outside of the VA or at another VA facility arrives during NCCC non-duty hours](#_Toc17877604)](#_Toc17877476)

[[Note: If the user attempts to order inpatient medications for an inpatient from an outpatient location, CPRS discontinues the order process and returns the user to original Orders or Meds tab display.](#_Toc17877604)](#_Toc17877476)

[[To write a new inpatient medication order with a simple dose, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select the Orders tab and select the appropriate item in the Write Orders pane.  

> The Inpatient Medications dialog appears.![](cprs-user-manual-gui-version-updated-or-3-0-499/364.png)](#_Toc17877604)](#_Toc17877476)

> [[The Inpatient Medications order dialog allows you to select from a list of personal quick orders or medication](#_Toc17877604)](#_Toc17877476)

2.  

> [[Locate the medication name or quick order name in the list box by typing characters in the Medication field. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

3.  

> [[Select the quick order or medication name using the mouse or keyboard. The lab results for the most recent lab test associated with the selected medication are displayed in the Information field, if an associated lab test was performed within the last 365 days.](#_Toc17877604)](#_Toc17877476)

> [[Note: A CAC or ADPAC will need to set the OR CPRS LAB DISPLAY ENABLED parameter to ON to activate the lab results display at a site.](#_Toc17877604)](#_Toc17877476)

> [[To view associated lab results for Quick Orders, a TIU OBJECT must be inserted into the Quick Order. For more information, refer to the Text Integration Utility (TIU) Clinical Coordinator & User Manual. This functionality will work for generalized Quick Orders only (orders assigned to Order Menus). It is not currently implemented for personal Quick Orders.](#_Toc17877604)](#_Toc17877476)

> [[The lab results functionality will not work properly for multidivisional facilities or any sites that use different lab test names at different sites, as only one lab test name can be associated with each drug. To successfully implement this functionality, all facilities/divisions that share a VistA system must use the same name for each monitored lab test.](#_Toc17877604)](#_Toc17877476)

> [[<span id="Park_inp_meds" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/365.png)](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS now uses a look up from Pharmacy to determine whether the selected medication is a controlled substance that requires the signature of a provider with a DEA number. For controlled substances, CPRS displays a message—"Order for controlled substance could not be completed. Provider does not have a current, valid DEA# on record and is ineligible to sign the order"—as shown in the graphic below. CPRS allows orders for controlled substances only when selected providers are able to sign the orders. You may need to exit the dialog, change the provider selection, and then reenter the dialog. See *Appendix D: Error Messages and Troubleshooting* for a full list of error messages related to controlled substance ordering.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/366.png)](#_Toc17877604)](#_Toc17877476)

> [[You must have a DEA# to order certain medications](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS requires a patient have a valid address if the selected outpatient medication is a controlled substance that requires the signature of a provider with a DEA number. For outpatient controlled substances, CPRS displays a message – "Controlled substance prescriptions require a patient address. Please contact administrative support to update patient address information." if the patient does not have a valid address. The contact information in the display may be customized using the Enter/Edit Missing ZIP Code Message option in the GUI Parameters menu.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/367.png)](#_Toc17877604)](#_Toc17877476)

> [[Controlled substance prescriptions require a patient address](#_Toc17877604)](#_Toc17877476)

4.  

> [[Selected the Dosage field and select a dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

> [[Once a dosage is selected, any lab test results displayed in the Information field are replaced by the National Standard Orderable Item information.](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

5.  
6.  

> [[Enter a Route by either selecting one from the list or typing in a valid route (a default route may have been set up). In the Schedule pane, select an existing schedule from the list or, to use a day-of-week/administration time schedule not on the list, select OTHER (you can also click the Day-of-Week link and then click OK on the dialog that displays). When the user selects a schedule, the administration times may display under the "Give additional dose now" text for a simple dose. The administration times will display if they have been defined for the ward or if there is a default as long as the schedule is not a PRN schedule.](#_Toc17877604)](#_Toc17877476)

7.  
1.  
2.  

> [[If you selected an existing schedule, skip to step 8. If you selected OTHER, CPRS displays the *Order with Schedule 'OTHER*' dialog. Take the following steps: Select one or more checkboxes by the appropriate days of the week. If the schedule requires specific administration times skip to steps c and d. To select a schedule from the list, highlight the schedule and select Add. Note: Users can assign either a schedule from the list or specific administration times, but not both. Also, because the user is specifying days of the week and a schedule, the list will contain only schedules less than 24 hours (for example, Q36H will not be in the list).](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[To use a specific administration time, select the hour and minutes (if the user only selects the hour, the minutes will default to zero) and select Add. Repeat step c until you have entered all required administration times. Warning: The administration times in the Schedule field apply to each day of the week that is listed, such as TU-TH-SA@08002000, for example. To create a schedule such as TU@0800 TH@2000, users would have to enter two separate orders using the complex medication order dialog. Also, users may not enter a schedule that only has administration times and PRN but no days.](#_Toc17877604)](#_Toc17877476)

5.  - 
    - 
    - 
6.  
7.  

> [[If you make a mistake while selecting an administration time or schedule, do one of the following to remove it: For a single administration time, highlight the hour and minutes in the Set Administration Time fields and select Remove (so to remove 08:00, you would have to select that time in the Set Administration Time fields not in the Schedule text box.)To remove the schedule, highlight the schedule and select Remove. To remove the entire schedule and begin again with step a, select Reset. Review the Schedule field. When you have the correct schedule, select OK. ![](cprs-user-manual-gui-version-updated-or-3-0-499/368.png)](#_Toc17877604)](#_Toc17877476)

> [[The *Order with Schedule 'OTHER'* dialog allows you to enter a customized day-of-week and/or administration-time schedule. The user can enter specific administration times or select a schedule from the available list](#_Toc17877604)](#_Toc17877476)

8.  

> [[Select PRN if necessary. PRN will display in the schedule field if the PRN checkbox is checked or if the schedule is defined in the Pharmacy files as a PRN schedule.](#_Toc17877604)](#_Toc17877476)

9.  
10. 

> [[<span id="Ind_MEDS_jnpt_simple_meds_step" class="anchor"></span>Enter an Indication. If indications are defined, they will display in the drop-down list for you to select or you may type in an indication Enter comments (optional). The date and time that the patient is scheduled to receive the first dose of the medication appears under the Comments field. (For example, CPRS cannot show an expected first dose for "on call" or schedules with PRN. On the complex tab, it will not try to determine an expected first dose after a THEN because the first item must be completed.) If you want the patient to receive an additional dose now, check the Give additional dose now check box.](#_Toc17877604)](#_Toc17877476)

> [[When you select the Give additional dose now check box, CPRS creates two new orders. Depending on your version of CPRS, the order priority and dosing schedule may be set automatically or may require manual adjustments. The pop-up messages displayed will also vary.](#_Toc17877604)](#_Toc17877476)

> [[The dosing schedule and priority are set automatically for each order. The first order is scheduled for immediate administration (NOW) and is assigned the priority ASAP. The second order is given the priority ROUTINE and will be administered following the dosing schedule that you defined. A warning displays that is similar to the following example.](#_Toc17877604)](#_Toc17877476)

> [[Note: If your site does not use the priority ASAP, then an alternative priority (for example, STAT) will display in place of ASAP.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/369.png)](#_Toc17877604)](#_Toc17877476)

> [[Warning displayed when "Give additional dose now" is selected](#_Toc17877604)](#_Toc17877476)

10. 
11. 

> [[Check the warning message to ensure that the orders you created are what you expected. If the orders are acceptable, then click OK. If not, click Cancel to clear the Give additional dose now check box. Select a value for the Priority field. When Give additional dose now is selected, the Priority field is automatically set to ASAP (or a site-specific alternative). If you select a value for the Priority field before you select the Give additional dose now checkbox, a message notifies you that the selected priority will be changed to the "Give additional dose now" priority settings.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/370.png)](#_Toc17877604)](#_Toc17877476)

> [[CPRS displays a notification that "Give additional dose now" overrides any previously selected priority](#_Toc17877604)](#_Toc17877476)

> [[The default value of ASAP can be changed by selecting a different value from the Priority field before submitting the order. If the Priority field is empty when the order is submitted, it will revert to the default values for "Give additional dose now."](#_Toc17877604)](#_Toc17877476)

12. 

> [[Select Accept Order. Note: If you do not complete the mandatory items or if the information is incorrect, CPRS sends a message telling you that the information is incorrect and showing you the correct type of response.](#_Toc17877604)](#_Toc17877476)

13. - 
    - 
14. 

> [[(Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following: To proceed, select Accept Order. To stop the ordering process and return to the dialog, Cancel Order. Enter another medication order -or-](#_Toc17877604)](#_Toc17877476)

> [[select Quit.](#_Toc17877604)](#_Toc17877476)

> [[Note: You must sign the order before CPRS sends it to Pharmacy. You can either sign the order now or wait until later. When using Give additional dose now, it is recommended that you sign the order immediately to send the order to the inpatient pharmacy. You only need to sign once for both orders created when Give additional dose now is selected.](#_Toc17877604)](#_Toc17877476)

1.  

> [[Click the Meds tab and select Action \| New Medication… -or-](#_Toc17877604)](#_Toc17877476)

> [[click the Orders tab and select the appropriate item under the Write Orders list box.](#_Toc17877604)](#_Toc17877476)

> [[The Inpatient Medications dialog box displays.](#_Toc17877604)](#_Toc17877476)

1.  

> [[In the Medication Order dialog, locate the medication name or quick order name in the list box by typing characters in the Medication field. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

2.  

> [[Select the quick order or medication name using the mouse or keyboard. Once the name is selected, CPRS displays a second dialog to select the items for the rest of the order. In the top field of the second dialog, the generic medication name and the synonym (usually a brand name) are displayed.](#_Toc17877604)](#_Toc17877476)

> [[The lab results for the most recent lab test associated with the selected medication are displayed in the Information field, if an associated lab test was performed within the last 365 days.](#_Toc17877604)](#_Toc17877476)

> [[Note: A CAC or ADPAC will need to set the OR CPRS LAB DISPLAY ENABLED parameter to ON to activate the lab results display at a site.](#_Toc17877604)](#_Toc17877476)

> [[To view associated lab results for Quick Orders, a TIU OBJECT must be inserted into the Quick Order. For more information, refer to the *Text Integration Utility (TIU) Clinical Coordinator & User Manual*. This functionality will work for generalized Quick Orders only (orders assigned to Order Menus). It is not currently implemented for personal Quick Orders.](#_Toc17877604)](#_Toc17877476)

> [[The lab results functionality will not work properly for multi-divisional facilities or any sites that use different lab test names at different sites, as only one lab test name can be associated with each drug. To successfully implement this functionality, all facilities/divisions that share a VistA system must use the same name for each monitored lab test.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the selected medication is a controlled substance that requires the signature of a provider with a DEA number, the *Order not completed* dialog appears. CPRS allows orders for controlled substances only when selected providers are able to sign the orders. You may need to exit the *Medication Order* dialog, change the provider selection, and then reenter the dialog.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/371.png)](#_Toc17877604)](#_Toc17877476)

> [[You must have a DEA# to order certain medications](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS requires a patient have a valid address if the selected outpatient medication is a controlled substance that requires the signature of a provider with a DEA number. For outpatient controlled substances, CPRS displays a message – "Controlled substance prescriptions require a patient address. Please contact administrative support to update patient address information." if the patient does not have a valid address. The contact information in the display may be customized using the Enter/Edit Missing ZIP Code Message option in the GUI Parameters menu.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/372.png)](#_Toc17877604)](#_Toc17877476)

> [[Controlled substance prescriptions require a patient address](#_Toc17877604)](#_Toc17877476)

3.  

> [[Select the Complex tab. Note: After you begin a complex dose medication order, you must remain on the Complex tab until you finish the order. If you switch to the Dosage tab, CPRS clears all complex dosages and you will be forced to start again.](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select the Dosage field and select the appropriate dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

> [[Once a dosage is selected, any lab test results displayed in the Information field are replaced by the National Standard Orderable Item information.](#_Toc17877604)](#_Toc17877476)

53. [[Enter a Route by either selecting one from the list or typing in a valid route.](#_Toc17877604)](#_Toc17877476)
5.  

> [[In the Schedule pane, select an existing schedule from the list or, to use a day-of-week/administration time schedule not on the list, select OTHER. When the user selects a regular schedule that does not have PRN, the administration times may display in the Schedule column. The administration times will display if they have been defined for the ward or if there is a default.](#_Toc17877604)](#_Toc17877476)

6.  1.  
    2.  

> [[If you selected an existing schedule, skip to step 9. If you selected OTHER, CPRS displays the Order with Schedule 'OTHER' dialog. Take the following steps: Select one or more checkboxes by the appropriate days of the week. If the schedule requires specific administration times skip to steps c and d. To select a schedule from the list, highlight the schedule and select Add. Note: Users can assign either a schedule from the list or specific administration times, but not both. If launched from the Complex tab, the Day-of-Week Schedule builder does not display one-time schedules in the schedule list. Also, because the user is specifying days of the week and a schedule, the list will contain only schedules less than 24 hours (for example, Q36H will not be in the list).](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[To use a specific administration time, select the hour and minutes (if the user only selects the hour, the minutes will default to zero) and select Add. Repeat step c until you have entered all required administration times. Warning: The administration times in the Schedule field apply to each day of the week that is listed, such as TU-TH-SA@08002000, for example. To create a schedule such as TU@0800 TH@2000, users would have to enter two separate orders using the complex medication order dialog. Also, users may not enter a schedule that only has administration times and PRN but no days.](#_Toc17877604)](#_Toc17877476)

5.  - 
    - 
    - 
6.  
7.  

> [[If you make a mistake while selecting an administration time or schedule, do one of the following to remove it: For a single administration time, highlight the hour and minutes in the Set Administration Time fields and select Remove (so to remove 08:00, you would have to select that time in the Set Administration Time fields not in the Schedule text box.) To remove the schedule, highlight the schedule and select Remove. To remove the entire schedule and begin again with step a, select Reset. Review the Schedule field. When you have the correct schedule, select OK. ![](cprs-user-manual-gui-version-updated-or-3-0-499/373.png)](#_Toc17877604)](#_Toc17877476)

> [[The *Order with Schedule 'OTHER'* dialog allows you to enter a customized day-of-week and/or administration-time schedule. The user can enter specific administration times or select a schedule from the available list](#_Toc17877604)](#_Toc17877476)

7.  

> [[If necessary, select PRN. PRN will display in the schedule field if the PRN checkbox is checked or if the schedule is defined in the Pharmacy files as a PRN schedule.](#_Toc17877604)](#_Toc17877476)

8.  
9.  

> [[Select the Duration field and select the amount of time that the patient should use the specified dose. In the then/and field, select the appropriate conjunction for the order. Note: The conjunction "Then" requires a duration to be added.](#_Toc17877604)](#_Toc17877476)

10. 

> [[Select the next row in the Dosage field and type or select a dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

11. 
12. 

> [[CPRS fills in the Route and Schedule fields. You can change the values in these fields if necessary. Select a duration and a conjunction (then or and) except on the final row. Note: Your site's IRM staff may have specified rules governing the status of inpatient medication orders when patients are transferred from one ward or service to another. It may have also specified the number of days an inpatient medication order remains active. Please check with your site's IRM staff for information about these rules.](#_Toc17877604)](#_Toc17877476)

13. 

> [[Repeat steps 12-14 until you have completed the complex dose. Note: You can also add or remove a row in the complex dose. To add a row, click the gray area in front of the row and click Add Row (CPRS places the new row above the selected row). To delete a row, click the gray area in front of the row you wish to delete and click Delete Row.](#_Toc17877604)](#_Toc17877476)

14. 
15. 

> [[Enter an Indication. If indications are defined, they will display in the drop-down list for you to select or you may type in an indication.Add comments (optional). The date and time that the patient is scheduled to receive the first dose of the medication appears under the Comments field. (For example, CPRS cannot show an expected first dose for "on call" or schedules with PRN. On the complex tab, it will not try to determine an expected first dose after a THEN because the first item must be completed). If you want the patient to receive an additional dose now, select the Give additional dose now check box.](#_Toc17877604)](#_Toc17877476)

> [[If you select the check box, the Give Additional Dose Now for Complex Order warning dialog box appears, as shown below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/374.png)](#_Toc17877604)](#_Toc17877476)

> [[CPRS displays a warning to providers who select "Give additional dose now" when placing a complex order](#_Toc17877604)](#_Toc17877476)

> [[When you select the Give additional dose now check box, CPRS creates two new orders. Depending on your version of CPRS, the order priority and dosing schedule may be set automatically or may require manual adjustments. The pop-up messages displayed will also vary.](#_Toc17877604)](#_Toc17877476)

> [[The dosing schedule and priority are set automatically for each order. The first order is scheduled for immediate administration (NOW) and is assigned a priority of ASAP (or a site-specific alternative). The second order is given the priority ROUTINE and follows the regular dosing schedule that you defined when placing the order.](#_Toc17877604)](#_Toc17877476)

> [[If you select a value for the Priority field before you select the Give additional dose now checkbox, a message notifies you that the selected priority will be changed to the "Give additional dose now" priority settings.](#_Toc17877604)](#_Toc17877476)

> [[Note: If your site does not use the priority ASAP, then an alternative priority (for example, STAT) will display in place of ASAP.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/375.png)](#_Toc17877604)](#_Toc17877476)

> [[Warning displayed when "Give additional dose now" is selected](#_Toc17877604)](#_Toc17877476)

16. 
17. 

> [[Check the orders and then select OK to close the warning dialog.Choose a priority from the Priority drop-down list. When Give additional dose now is selected, the Priority field is automatically set to ASAP (or a site-specific alternative). If you select a value for the Priority field before you select the Give additional dose now checkbox, a message notifies you that the selected priority will be changed to the "Give additional dose now" priority settings.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/376.png)](#_Toc17877604)](#_Toc17877476)

> [[CPRS displays a notification that "Give additional dose now" overrides any previously selected priority](#_Toc17877604)](#_Toc17877476)

18. 

> [[Select Accept Order. Note: If you do not complete the mandatory items, or if the information is incorrect, CPRS sends a message to tell you that the information is incorrect and shows you the correct type of response.](#_Toc17877604)](#_Toc17877476)

19. - 
    - 
20. 

> [[(Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following: To proceed, select Accept Order. To stop the ordering process and return to the dialog, Cancel Order. Enter another medication order -or-](#_Toc17877604)](#_Toc17877476)

> [[select Quit.](#_Toc17877604)](#_Toc17877476)

> [[Note: You must sign the order before CPRS sends it to the Pharmacy package. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

> [[When using Give additional dose now, it is recommended that you sign the order immediately to send the order to the inpatient pharmacy. You need only sign once for both orders created when Give additional dose now is selected.](#_Toc17877604)](#_Toc17877476)

[[To write a simple Clinic Medication order, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. From the Write Orders pane, select Clinic Medications.Note: Depending on how menus are set up at your particular site, you may need to select a different option from the Write Orders pane. Many sites have customized the items in the Write Orders pane. Check with your CAC (or the person who manages information resources at your site) if you have trouble locating the Clinic Medications item.](#_Toc17877604)](#_Toc17877476)

[[Note: The following prompts will be slightly different based on the patient's location. You will be asked to verify that you want to write Clinic Medications and to ensure that the encounter location is a clinic location.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  

[[To continue ordering Clinic Medications, select Yes and continue to the next step. To stop the Clinic Medications process, choose No. (Conditional) If the patient's current location is not a clinic, you will be asked if you want to change the patient's location. In the Clinic Medications dialog, locate the medication name or quick order name in the list box by typing characters in the Medication field. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

7.  
8.  

[[Select the appropriate Dosage from the list if displayed. If it is not displayed, you can enter a free-text dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

9.  
10. 

[[Enter the Route by either selecting one from the list or typing in a valid route (a default route may have been set up). In the Schedule pane, select an existing schedule from the list or, to use a day-of week/administration time schedule not on the list, select OTHER (you can also click the Day of-Week link and then click OK on the dialog that displays). When the user selects a schedule, the administration times may display under the "Give additional dose now" text for a simple dose. The administration times will display if they have been defined for the ward or if there is a default as long as the schedule is not a PRN schedule.](#_Toc17877604)](#_Toc17877476)

11. 
1.  
2.  

> [[If you selected an existing schedule, skip to step 12. If you selected OTHER, CPRS displays the Order with Schedule 'OTHER' dialog. Take the following steps: Select one or more checkboxes by the appropriate days of the week. If the schedule requires specific administration times skip to steps c and d. To select a schedule from the list, highlight the schedule and select Add. Note: Users can assign either a schedule from the list or specific administration times, but not both. Also, because the user is specifying days of the week and a schedule, the list will contain only schedules less than 24 hours (for example, Q36H will not be in the list).](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[To use a specific administration time, select the hour and minutes (if the user only selects the hour, the minutes will default to zero) and select Add. Repeat step c until you have entered all required administration times. Warning: The administration times in the Schedule field apply to each day of the week that is listed, such as TU-TH-SA@08002000, for example. To create a schedule such as TU@0800 TH@2000, users would have to enter two separate orders using the complex medication order dialog. Also, users may not enter a schedule that only has administration times and PRN but no days.](#_Toc17877604)](#_Toc17877476)

5.  - 
    - 
    - 
6.  
7.  

> [[If you make a mistake while selecting an administration time or schedule, do one of the following to remove it: For a single administration time, highlight the hour and minutes in the Set Administration Time fields and select Remove (so to remove 08:00, you would have to select that time in the Set Administration Time fields not in the Schedule text box.) To remove the schedule, highlight the schedule and select Remove. To remove the entire schedule and begin again with step a, select Reset. Review the Schedule field. When you have the correct schedule, select OK. ![](cprs-user-manual-gui-version-updated-or-3-0-499/382.png)](#_Toc17877604)](#_Toc17877476)

> [[The *Order with Schedule 'OTHER'* dialog allows you to enter a customized day-of-week and/or administration-time schedule. The user can enter specific administration times or select a schedule from the available list](#_Toc17877604)](#_Toc17877476)

12. 

[[Select PRN if necessary. PRN will display in the schedule field if the PRN checkbox is checked or if the schedule is defined in the Pharmacy files as a PRN schedule.](#_Toc17877604)](#_Toc17877476)

13. 
14. 
15. 
16. 
17. 
18. 
19. 
- 
- 
20. 
1.  
2.  

[[Select the Orders tab. From the Write Orders pane, select Clinic Medications. Note: Depending on how menus are set up at your site, you may need to select a different option from the Write Orders pane. Many sites have customized the items in the Write Orders pane. Check with your CAC (or the person who manages information resources at your site) if you have trouble locating the Clinic Medications item.](#_Toc17877604)](#_Toc17877476)

[[Note: The following prompts will be slightly different based on the patient's location. You will be asked to verify that you want to write Clinic Medications and to ensure that the encounter location is a clinic location.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  

[[To continue ordering Clinic Medications, select Yes and continue to the next step. To stop the Clinic Medications process, choose No. (Conditional) If the patient's current location is not a clinic, you will be asked if you want to change the patient's location. In the Clinic Medications dialog, locate the medication name or quick order name in the list box by typing characters in the Medication field. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

7.  
8.  

[[Select the Complex tab. Note: After you begin a complex dose medication order, you must remain on the Complex tab until you finish the order. If you switch to the Dosage tab, CPRS clears all complex dosages and you will be forced to start again.](#_Toc17877604)](#_Toc17877476)

9.  

[[Select the Dosage field and select the appropriate dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

[[Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

10. 

[[Enter a Route by either selecting one from the list or typing in a valid route. When the user selects a regular schedule that does not have PRN, the administration times may display in the Schedule column. The administration times will display if they have been defined for the ward or if there is a default.](#_Toc17877604)](#_Toc17877476)

11. 
1.  
2.  

> [[If you selected an existing schedule, skip to step 13. If you selected OTHER, CPRS displays the Order with Schedule 'OTHER' dialog. Take the following steps: Select one or more checkboxes by the appropriate days of the week. If the schedule requires specific administration times skip to steps c and d. To select a schedule from the list, highlight the schedule and select Add. Note: Users can assign either a schedule from the list or specific administration times, but not both. If launched from the Complex tab, the Day-of-Week Schedule builder does not display one-time schedules in the schedule list. Also, because the user is specifying days of the week and a schedule, the list will contain only schedules less than 24 hours (for example, Q36H will not be in the list).](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[To use a specific administration time, select the hour and minutes (if the user only selects the hour, the minutes will default to zero) and select Add. Repeat step c until you have entered all required administration times. Warning: The administration times in the Schedule field apply to each day of the week that is listed, such as TU-TH-SA@08002000, for example. To create a schedule such as TU@0800 TH@2000, users would have to enter two separate orders using the complex medication order dialog. Also, users may not enter a schedule that only has administration times and PRN but no days.](#_Toc17877604)](#_Toc17877476)

5.  - 
    - 
    - 
6.  
7.  

[[If you make a mistake while selecting an administration time or schedule, do one of the following to remove it: For a single administration time, highlight the hour and minutes in the Set Administration Time fields and select Remove (so to remove 08:00, you would have to select that time in the Set Administration Time fields not in the Schedule text box.) To remove the schedule, highlight the schedule and select Remove. To remove the entire schedule and begin again with step a, select Reset. Review the Schedule field. When you have the correct schedule, select OK. ![](cprs-user-manual-gui-version-updated-or-3-0-499/388.png)](#_Toc17877604)](#_Toc17877476)

[[The Order with Schedule 'OTHER' dialog allows you to enter a customized day-of-week and/or administration-time schedule. The user can enter specific administration times or select a schedule from the available list](#_Toc17877604)](#_Toc17877476)

12. 

[[If necessary, select PRN. PRN will display in the schedule field if the PRN checkbox is checked or if the schedule is defined in the Pharmacy files as a PRN schedule.](#_Toc17877604)](#_Toc17877476)

13. 
14. 

[[Select the Duration field and select the amount of time that the patient should use the specified dose. In the then/and field, select the appropriate conjunction for the order. Note: The conjunction "Then" requires a duration to be added.](#_Toc17877604)](#_Toc17877476)

15. 

[[Select the next row in the Dosage field and type or select a dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

16. 
17. 

[[CPRS fills in the Route and Schedule fields. You can change the values in these fields if necessary. Select a duration and a conjunction (then or and) except on the final row. Note: Your site's IRM staff may have specified rules governing the status of inpatient medication orders when patients are transferred from one ward or service to another. It may have also specified the number of days an inpatient medication order remains active.](#_Toc17877604)](#_Toc17877476)

[[Please check with your site's IRM staff for information about these rules.](#_Toc17877604)](#_Toc17877476)

18. 

[[Repeat steps 15-18 until you have completed the complex dose. Note: You can also add or remove a row in the complex dose. To add a row, click the gray area in front of the row and click Add Row (CPRS places the new row above the selected row). To delete a row, click the gray area in front of the row you wish to delete and click Delete Row.](#_Toc17877604)](#_Toc17877476)

19. 
20. 

[[<span id="Ind_Ordering_complex_clinic_Meds_step" class="anchor"></span>Enter an Indication. If indications are defined, they will display in the drop-down list for you to select or you may type in an indication. Add comments (optional). The date and time that the patient is scheduled to receive the first dose of the medication appears under the Comments field. (For example, CPRS cannot show an expected first dose for "on call" or schedules with PRN. On the complex tab, it will not try to determine an expected first dose after a THEN because the first item must be completed).](#_Toc17877604)](#_Toc17877476)

21. 
22. 
23. 
24. 

[[Select Accept Order. Note: If you do not complete the mandatory items, or if the information is incorrect, CPRS sends a message to tell you that the information is incorrect and shows you the correct type of response.](#_Toc17877604)](#_Toc17877476)

9.  [[(Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following:](#_Toc17877604)](#_Toc17877476)
- [[To proceed, select Accept Order.](#_Toc17877604)](#_Toc17877476)
- [[To stop the ordering process and return to the dialog, Cancel Order.](#_Toc17877604)](#_Toc17877476)
25. 

[[Users can also change and renew Clinic Medication orders from a clinic location. If the patient's location is not a clinic location, users will not be able to change or renew the Clinic Medication orders. To change Clinic Medication orders, follow the instructions in the "Changing Orders" section of this manual.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[In the Infusion Order dialog, the order type—Continuous or Intermittent— affects whether some fields are available or visible. The two types of IVs are defined as follows:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[Continuous infusion orders run at a specified rate. As the user selects a solution and/or additive, the items from that list are displayed to the right under Solution/Additive. For continuous infusion orders the only optional fields are the Comments and the Duration or Total Volume fields. The schedule field is not available.](#_Toc17877604)](#_Toc17877476)

[[The Additive Frequency field enables users to select which IV bag the additive should be placed:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[Bag/Day: The additive should be put in one bag for 24 hours, normally the first bag. All Bags: The additive should be placed in all bags given to the patient. See Comments: The provider wants something other than the above options and will put appropriate instructions in the Comments box. Note: If the user selects "See Comments" for the Additive Frequency but does not enter appropriate instructions in the Comments box, Pharmacy may interpret that as All Bags.](#_Toc17877604)](#_Toc17877476)

[[To order continuous Clinic Infusions, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. From the Write Orders pane, select Clinic Infusions. Note: Depending on how menus are set up at your site, you may need to select a different option from the Write Orders pane. Many sites have customized the items in the Write Orders pane. Check with your CAC (or the person who manages information resources at your site) if you have trouble locating the Clinic Infusions item.](#_Toc17877604)](#_Toc17877476)

[[Note: The following prompts will be slightly different based on the patient's location. You will be asked to verify that you want to write Clinic Infusions and to ensure that the encounter location is a clinic location.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  

> [[To continue ordering Clinic Medications, select Yes and continue to the next step. To stop the Clinic Medications process, choose No. (Conditional) If the patient's current location is not a clinic, change the patient's location to the appropriate clinic. The Clinic Infusion Order dialog displays.](#_Toc17877604)](#_Toc17877476)

[[<span id="Ind_Ord_continuous_clinic_infuse_capt" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/394.png)](#_Toc17877604)](#_Toc17877476)

[[The Infusion Order dialog for continuous infusion orders does not use a schedule, but it does have an infusion rate. For continuous infusion orders, the new Additive Frequency field enables providers to indicate into which IV bag the additive should be placed](#_Toc17877604)](#_Toc17877476)

54. [[Select the needed solutions from the Solutions tab.](#_Toc17877604)](#_Toc17877476)
6.  
- 
- 
- 

[[Select an additive from the list (if necessary) and edit the strength if needed. Repeat for additional additives if necessary. How users can edit the strength field will depend on the values for strength defined in the pharmacy files as follows: If a single strength is defined, users cannot edit the field. If multiple values for strength are defined in the pharmacy files, the field will have a drop-down list from which users can choose a strength. If no values have been defined, users can type in a strength. If a strength includes a decimal point, the value must begin with a number: so, .5 is not valid, but 0.5 is. The solution and additives you select will appear in the Solution/Additive grid.](#_Toc17877604)](#_Toc17877476)

[[Note: To remove an additive or a solution, select the solution or additive and select Remove.](#_Toc17877604)](#_Toc17877476)

7.  
8.  
- 
- 
- 
9.  
10. 
11. 
12. 
13. 
14. 

[[Enter an infusion rate in ml/hr. Select a Priority. (Optional) Enter a number for the duration or total volume of fluids for this order. Select the appropriate unit (liters-L, milliliters-ml, days, or hours). Note: If you change the units, the value in the Duration or the Total Volume field will be removed and you will need to enter it again. This is a safety feature to ensure the patient does not receive a dangerous amount of fluid.](#_Toc17877604)](#_Toc17877476)

15. 
16. 
17. 
18. 
19. 
20. 

[[<span id="Ind_Ord_continuous_clinic_infuse_step" class="anchor"></span>Enter an Indication for the medication. If they have been entered, you can use the drop-down list and select the indication or you can type an indication in the field. Enter any comments (if necessary). Review the order text at the bottom of the dialog to ensure that it is correct. Select Accept Order. Review order check items and respond appropriately. If the order should not be entered because of a possible interaction, select Cancel. If the order is okay to accept, select Accept Order. To enter additional Clinic Infusion orders, repeat steps 6-19 as needed. To finish, select Quit. For an outpatient, when you select quit, the encounter location will remain with the current clinic. For an inpatient, when you select Quit, the encounter location will go back to the location where the patient was before you began entering Clinic Infusion orders. Note: The order must be signed before it is sent. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. From the Write Orders pane, select Clinic Infusions. Note: Depending on how menus are set up at your particular site, you may need to select a different option from the Write Orders pane. Many sites have customized the items in the Write Orders pane. Check with your CAC (or the person who manages information resources at your site) if you have trouble locating the Clinic Infusions item.](#_Toc17877604)](#_Toc17877476)

[[Note: The following prompts will be slightly different based on the patient's location. You will be asked to verify that you want to write Clinic Infusions and to ensure that the encounter location is a clinic location.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  

> [[To continue ordering Clinic Medications, select Yes and continue to the next step. To stop the Clinic Medications process, choose No. (Conditional) If the patient's current location is not a clinic, change the patient's location to the appropriate clinic.The Clinic Infusion Order dialog displays.](#_Toc17877604)](#_Toc17877476)

[[<span id="Ind_Ord_intermitnt_clinic_infuse_capt" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/397.png) The Infusion Order dialog for continuous infusion orders does not use a schedule, but it does have an infusion rate. For continuous infusion orders, the new Additive Frequency field enables providers to indicate into which IV bag the additive should be placed](#_Toc17877604)](#_Toc17877476)

6.  
7.  

> [[Select a solution from the Solutions tab. Select an additive from the list (if necessary) and edit the Volume/Strength. Repeat for additional additives if necessary. The solution and additives you select will appear in the Solution/Additive grid.](#_Toc17877604)](#_Toc17877476)

[[Note: To remove an additive or a solution, select the solution or additive and click Remove.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 

[[Select a schedule from the list or create one using the Day-of-Week schedule builder. Note: When a user writes an intermittent infusion order with a schedule of ONCE, the following will happen in CPRS:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[The DURATION field will be disabled. The Give Additional Dose Now option will be disabled. Expected First Dose and Administration Times will not be displayed. Note: When a user writes an intermittent infusion order with a schedule of On Call or a PRN, the following will happen in CPRS:](#_Toc17877604)](#_Toc17877476)

- 
55. [[Expected First Dose and Administration Times will not be displayed. If you selected an existing schedule, skip to step 14. If you selected OTHER, CPRS displays the Order with Schedule 'OTHER' dialog. Take the following steps:](#_Toc17877604)](#_Toc17877476)
1.  
2.  

> [[Select one or more checkboxes by the appropriate days of the week. If the schedule requires specific administration times skip to steps c and d. To select a schedule from the list, highlight the schedule and select Add. Note: Users can assign either a schedule from the list or specific administration times, but not both.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[To use a specific administration time, select the hour and minutes (if the user only selects the hour, the minutes will default to zero) and select Add. Repeat step c until you have entered all required administration times. Warning: The administration times in the Schedule field apply to each day of the week that is listed, such as TU-TH-SA@08002000, for example. To create a schedule such as TU@0800 TH@2000, users would have to enter two separate orders using the complex medication order dialog. Also, users may not enter a schedule that only has administration times and PRN but no days.](#_Toc17877604)](#_Toc17877476)

5.  - 
    - 
    - 
6.  
7.  
11. 
12. 
13. 

[[If you make a mistake while selecting an administration time or schedule, do one of the following to remove it: For a single administration time, highlight the hour and minutes in the Set Administration Time fields and select Remove (so to remove 08:00, you would have to select that time in the Set Administration Time fields not in the Schedule text box.) To remove the schedule, highlight the schedule and select Remove. To remove the entire schedule and begin again with step a, select Reset. Review the Schedule field. When you have the correct schedule, select OK. If necessary, select the PRN checkbox. Enter the number for the duration over which to infuse the medication. Move to the next field and select the unit of time (the units can be only Minutes or Hours) over which the infusion should be given. For example, you might enter 30 for the number, move to the next field, and then select minutes to define infuse over 30 minutes.](#_Toc17877604)](#_Toc17877476)

14. 
15. 
16. 

[[Select the Priority. Enter a number for the duration or total volume. Move to the next field and select the appropriate unit (liters-L, milliliters-ml, days, hours, or doses). Note: If you change the units, the value in the Duration or the Total Volume field will be removed and you will need to enter it again. This is a safety feature to ensure the patient does not receive a dangerous amount of fluid.](#_Toc17877604)](#_Toc17877476)

17. 

[[If necessary, select the Give additional dose now checkbox. Note: Make sure that you are careful about using give additional-dose-now functionality. When you click the check box, CPRS creates two new orders and sends it to Inpatient Medications. Make sure the "Give additional dose now" and the regular order with the original schedule you entered do not overmedicate the patient. "Give additional dose now" is not available for ONCE, ONE-TIME, or NOW orders. It is also not available for delayed orders.](#_Toc17877604)](#_Toc17877476)

18. 
19. 
20. 
21. 
22. 

[[<span id="Ind_Ord_intermitnt_clinic_infuse_step" class="anchor"></span>Enter an Indication. If they have been entered, you can use the drop-down list and select the indication or you can type an indication in the field. Enter any comments (if necessary). Review the order text at the bottom of the dialog to ensure that it is correct. If the order text is correct, select Accept Order. Review order check items and respond appropriately. If the order should not be entered because of a possible interaction, select Cancel. If the order is okay to accept, select Accept Order.  
](#_Toc17877604)](#_Toc17877476)

23. 

[[To enter additional Clinic Infusion orders, repeat steps 6-19 as needed. To finish, select Quit. For an outpatient, when you select quit, the encounter location will remain with the current clinic. For an inpatient, when you select Quit, the encounter location will go back to the location where the patient was before you began entering Clinic Infusion orders. Note: The order must be signed before it is sent. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  

> [[If necessary, select an appropriate clinic encounter location and time. If necessary, select the Unit Dose radio button. If necessary, designate the injection site using the Injection Site drop-down box to locate and select the site (i.e., ARM, LEFT UPPER or THIGH, LEFT).Enter the Action Date/Time for the administration (you can use T for today, N for now, or enter a specific date and time, such as DEC 10, 2014@13:10).Place your cursor in the Scan Medication Bar Code field (the colored rectangle in front of the field will turn from red to green indicating that it is ready to receive data) and scan the medication,-or-](#_Toc17877604)](#_Toc17877476)

> [[To manually enter the medication, place your cursor in the Scan Medication Bar Code field (the colored rectangle in front of the field will turn from red to green indicating that it is ready to receive data) and type part or the entire medication name and press \<Enter\>.](#_Toc17877604)](#_Toc17877476)

7.  
8.  

[[In the Multiple Drugs for Selected Order dialog, select the appropriate drug by either clicking on the drug name or using the up and down arrow buttons to highlight the name and pressing \<OK\>. Select the Order button. In the Clinic Medications dialog that displays, do the following:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

[[Enter a dosage, either picking from the list or typing a dosage in. Select a route. Select a schedule (Now or Stat). (Optional) Enter a comment. If the information is correct, select the Accept Order button. If the information is not correct, correct it or select the Quit button to cancel the order. Note: If you select Quit, the information is removed and a dialog displays the message that the order was canceled. Select OK. You are then returned to the Order Manager dialog as if you are just beginning the process.](#_Toc17877604)](#_Toc17877476)

9.  
10. 
11. 
12. 
10. [[Select One Step Clinic Admin. (This can be done from the Orders tab Write Orders pane, if an option is available, the Orders tab Action menu, the Meds tab Action menu, or from a progress note).](#_Toc17877604)](#_Toc17877476)
11. [[If necessary, select an appropriate clinic appointment or clinic and time for the encounter.](#_Toc17877604)](#_Toc17877476)
12. [[Select the IV radio button.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/400.png)](#_Toc17877604)](#_Toc17877476)

13. [[Select the IV type from the drop-down box: Admixture, Piggyback, or Syringe.](#_Toc17877604)](#_Toc17877476)

> [[Depending on which IV type you choose, you will need to make selections under the IV's section. Selecting Admixture does not affect the other fields, but selecting Piggyback will activate the Schedule field and selecting Syringe will active the Intermittent Syringe field.](#_Toc17877604)](#_Toc17877476)

14. [[If you selected Piggyback, you must select a schedule of either NOW or STAT.](#_Toc17877604)](#_Toc17877476)
15. [[If you selected Syringe, you must designate whether this is an Intermittent Syringe by choosing YES or NO from the Int. Syringe drop-down.](#_Toc17877604)](#_Toc17877476)
16. [[Select an injection site from the drop-down list.](#_Toc17877604)](#_Toc17877476)
17. [[Enter a date and time when the medication was administered.](#_Toc17877604)](#_Toc17877476)

> [[You can use N for Now, T for today, or you can set a specific date and time, such as 12/11/2014@13:35 (for December 11, 2014 at 1:35 p.m.).](#_Toc17877604)](#_Toc17877476)

18. [[Enter the medication and the solution, if necessary. Place your cursor in the Scan Medication Bar Code field (the colored rectangle in front of the field will turn from red to green indicating that it is ready to receive data) and scan the medication,](#_Toc17877604)](#_Toc17877476)

> [[-or-](#_Toc17877604)](#_Toc17877476)

> [[To manually enter the medication, place your cursor in the Scan Medication Bar Code field (the colored rectangle in front of the field will turn from red to green indicating that it is ready to receive data) and type part or the entire medication name and press \<Enter\>.](#_Toc17877604)](#_Toc17877476)

19. 
20. 

[[In the Multiple Drugs for Selected Order dialog, select the appropriate drug by either clicking on the drug name or using the up and down arrow buttons to highlight the name and pressing \<OK\>. Repeat this step for the solution or medication if necessary. ![](cprs-user-manual-gui-version-updated-or-3-0-499/401.png)](#_Toc17877604)](#_Toc17877476)

[[This screen capture shows the Multiple Drugs for Selected Order dialog that displays if a user is manually entering a medication instead of scanning it](#_Toc17877604)](#_Toc17877476)

21. [[Select the Order button.](#_Toc17877604)](#_Toc17877476)
22. [[Enter the additional information for the IV type you chose below:](#_Toc17877604)](#_Toc17877476)
- 
- 
- 
23. [[Admixture: In the Clinic Infusion Orders dialog, enter the Volume/Strength, Route, Infusion Rate, and a comment (optional) and select Accept Order. Piggyback: In the Clinic Infusion Orders dialog, enter the Volume/Strength, Route, Schedule (NOW or STAT). Optionally you can enter a comment (optional) and designate over what period of time the IV should be administered. Then, select Accept Order. Syringe: In the Clinic Infusion Orders dialog, enter the Volume/Strength, Route, Infusion Rate, and a comment (optional) and select Accept Order.If any order checks display, review and act on them appropriately If you have more IV medications to order, repeat steps 3-12 until all medications have been ordered.](#_Toc17877604)](#_Toc17877476)
24. [[When ready, select the Review/Sign button.](#_Toc17877604)](#_Toc17877476)
25. [[Review the orders to be signed.](#_Toc17877604)](#_Toc17877476)
26. [[If the orders are correct, enter your electronic signature and select the OK button.](#_Toc17877604)](#_Toc17877476)
27. [[If another order dialog displays, review and take appropriate action, either accepting the order or canceling the order.](#_Toc17877604)](#_Toc17877476)

[[The order displays under the Orders Tab in CPRS. You may need to change the view to see the order. If you do not see the order under the Clinic Medications or Clinic Infusions headings, please use the View \| Custom View menu option in CPRS and selected Completed/Expired option for Pharmacy. The items should display there.](#_Toc17877604)](#_Toc17877476)

> [[1. Select the Meds tab and select Action \| New Medication…](#_Toc17877604)](#_Toc17877476)

> [[-or- select the Orders tab and click the appropriate item under the Write Orders list.](#_Toc17877604)](#_Toc17877476)

> [[The Outpatient Medications dialog appears (as shown in the graphic below).](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/402.png)](#_Toc17877604)](#_Toc17877476)

> [[The Outpatient Medications order dialog](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog will appear before the Medication Order dialog box. You must complete the encounter information dialog box before proceeding.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the selected medication is a controlled substance that requires the signature of a provider with a DEA number, the *Order not completed* dialog appears. Before an order for a controlled substance can be entered, the provider selected for the encounter must be able to sign the order. You may need to exit the Medication Order dialog, change the provider, and reenter the Medication Order dialog.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/403.png)](#_Toc17877604)](#_Toc17877476)

> [[You must have a DEA# to order certain medications](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS requires a patient have a valid address if the selected outpatient medication is a controlled substance that requires the signature of a provider with a DEA number. For outpatient controlled substances, CPRS displays a message – "Controlled substance prescriptions require a patient address. Please contact administrative support to update patient address information." if the patient does not have a valid address. The contact information in the display may be customized using the Enter/Edit Missing ZIP Code Message option in the GUI Parameters menu.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/404.png)](#_Toc17877604)](#_Toc17877476)

> [[Controlled substance prescriptions require a patient address](#_Toc17877604)](#_Toc17877476)

> [[<span id="YSCLAUTHORIZED" class="anchor"></span>Note: Provider must have YSCL AUTHORIZED to order clozapine. Currently, CPRS will allow a provider without authorization key to place clozapine order. For example, if PROVIDER, TWO is logged in, they do not have the YSCL AUTHORIZED key, change the encounter provider to PROVIDER, ONE (they do have the key), then place the Clozapine order, it shows up on Orders screen, then sign the order using PROVIDER, TWO. Now the signed order shows PROVIDER, TWO and it is Pending the pharmacist is able to complete the order, making it Active. \*\*Even though CPRS allows the order to go through, this action should not be done.](#_Toc17877604)](#_Toc17877476)

2.  

> [[In the Medication Order dialog, locate the medication name or quick order name in the list box by typing characters in the Medication field. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

3.  

> [[Select the quick order or medication name using the mouse or keyboard. The lab results for the most recent lab test associated with the selected medication are displayed in the Information field, if an associated lab test was performed within the last 365 days.](#_Toc17877604)](#_Toc17877476)

> [[Note: A CAC or ADPAC will need to set the OR CPRS LAB DISPLAY ENABLED parameter to ON to activate the lab results display at a site.](#_Toc17877604)](#_Toc17877476)

> [[To view associated lab results for Quick Orders, a TIU OBJECT must be inserted into the Quick Order. For more information, refer to the *Text Integration Utility (TIU) Clinical Coordinator & User Manual*. This functionality will work for generalized Quick Orders only (orders assigned to Order Menus). It is not currently implemented for personal Quick Orders.](#_Toc17877604)](#_Toc17877476)

> [[The lab results functionality will not work properly for multidivisional facilities or any sites that use different lab test names at different sites, as only one lab test name can be associated with each drug. To successfully implement this functionality, all facilities/divisions that share a VistA system must use the same name for each monitored lab test.](#_Toc17877604)](#_Toc17877476)

[[<span id="Parked_Meds_Screenshot_2" class="anchor"><span id="Ind_Ord_Outpt_simple_dose_capt" class="anchor"></span></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/405.png)](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select the dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

> [[Once a dosage is selected, any lab test results displayed in the Information field are replaced by the National Standard Orderable Item information.](#_Toc17877604)](#_Toc17877476)

> [[The tier level represents medication copayment classes for Outpatient Pharmacy charges that are dependent on the medication class. It is used to determine the charge rate for copayments.](#_Toc17877604)](#_Toc17877476)

5.  

[[Enter a Route by either selecting one from the list or typing in a valid route. Note: Outpatient orders for supply items do not require a route.](#_Toc17877604)](#_Toc17877476)

6.  
7.  

> [[Choose a schedule from the Schedule field. (Select PRN, if desired.) CPRS completes the default days supply field and calculates the quantity field based on the formula days supply x schedule = quantity. If necessary, highlight and change the numbers in these fields. Note: If you change a number, CPRS will attempt to recalculate the other field. If you check PRN, be sure that the quantity field is correct before accepting the order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 
13. 
14. 
15. - 
    - 
16. 

> [[Enter the number of refills. Select the location where the patient should pick up the medication from the Pick Up field. Choose a priority. <span id="Ind_ORD_outpt_simple_med_step" class="anchor"></span>Enter an Indication. If they have been entered, you can use the drop-down list and select the indication or you can type an indication in the field.Add comments in the Comments field (if desired). Under certain circumstances, a check box may appear under the Days Supply field. If the medication is service-connected, make sure the box is checked Select Accept Order. (Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following: To proceed, select Accept Order. To stop the ordering process and return to the dialog, Cancel Order. If you are finished ordering outpatient medications, select Quit. Note: The order must be signed before it is sent to the Pharmacy package. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select the Meds tab and select Action \| New Medication… -or-](#_Toc17877604)](#_Toc17877476)

2.  

> [[Select the Orders tab and select the appropriate item under the Write Orders list box. CPRS will display the Medication Order dialog. Note: If encounter information has not been entered, the encounter information dialog will appear before the Medication Order dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

3.  

> [[In the Medication Order dialog, locate the medication name or quick order name in the list box by typing characters in the Medication field. Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select the quick order or medication name using the mouse or keyboard. Once the name is selected, CPRS displays a second dialog to select the items for the rest of the order. In the top field of the second dialog, the generic medication name and the synonym (usually a brand name) are displayed.](#_Toc17877604)](#_Toc17877476)

> [[The lab results for the most recent lab test associated with the selected medication are displayed in the Information field, if an associated lab test was performed within the last 365 days.](#_Toc17877604)](#_Toc17877476)

> [[Note: A CAC or ADPAC will need to set the OR CPRS LAB DISPLAY ENABLED parameter to ON to activate the lab results display at a site.](#_Toc17877604)](#_Toc17877476)

> [[To view associated lab results for Quick Orders, a TIU OBJECT must be inserted into the Quick Order. For more information, refer to the *Text Integration Utility (TIU) Clinical Coordinator & User Manual*. This functionality will work for generalized Quick Orders only (orders assigned to Order Menus). It is not currently implemented for personal Quick Orders.](#_Toc17877604)](#_Toc17877476)

> [[The lab results functionality will not work properly for multi-divisional facilities or any sites that use different lab test names at different sites, as only one lab test name can be associated with each drug. To successfully implement this functionality, all facilities/divisions that share a VistA system must use the same name for each monitored lab test.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the selected medication is a controlled substance that requires the signature of a provider with a DEA, the Order not completed dialog will appear. Before an order for a controlled substance can be entered, the provider selected for the encounter must be able to sign the order. You may need to exit the Medication Order dialog, change the provider, and then reenter the Medication Order dialog.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/406.png)](#_Toc17877604)](#_Toc17877476)

> [[You must have a DEA# to order certain medications](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS requires a patient to have a valid address if the selected outpatient medication is a controlled substance that requires the signature of a provider with a DEA number. For outpatient controlled substances, CPRS displays a message – "Controlled substance prescriptions require a patient address. Please contact administrative support to update patient address information." if the patient does not have a valid address. The contact information in the display may be customized using the Enter/Edit Missing ZIP Code Message option in the GUI Parameters menu.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/407.png)](#_Toc17877604)](#_Toc17877476)

> [[Controlled substance prescriptions require a patient address](#_Toc17877604)](#_Toc17877476)

5.  

> [[Click the Complex dose tab. Note: Once you begin a complex medication order, you must remain on the Complex tab until you finish the order. If you switch tabs, all complex dosages will be erased, and you will be forced to start the order again.<span id="Parked_Meds_Screenshot_complex" class="anchor"></span>](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/408.png)](#_Toc17877604)](#_Toc17877476)

> [[You can enter a complex medication order from the Medication Order dialog](#_Toc17877604)](#_Toc17877476)

6.  

> [[Click the Dosage field and select the appropriate dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

> [[Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

> [[Once a dosage is selected, any lab test results displayed in the Information field are replaced by the National Standard Orderable Item information.](#_Toc17877604)](#_Toc17877476)

7.  

> [[Enter a Route by either selecting one from the list or typing in a valid route. Note: Outpatient orders for supply items do not require a route.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 

> [[Enter a schedule in the Schedule field. (Select PRN if desired). Select the Duration cell and enter a number and select units (days is the default) a patient should use the specified dose. Enter the appropriate conjunction in the then or and field except on the final row. Note: The conjunction "Then" requires a duration to be added.](#_Toc17877604)](#_Toc17877476)

11. 

> [[Select the Dosage field in the next row and select a dosage. The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. Also, the character "^" may not be entered in the Dosage field. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

12. 

> [[Repeat steps 5-9 until you have completed the complex dose. Note: You can add or remove a row in the complex dosage. To add a row, click the gray area in front of the row and click Add Row. (The new row will be placed above the selected row.) To delete a row, click the gray area in front of the row to be deleted and click Delete Row.](#_Toc17877604)](#_Toc17877476)

13. 

> [[CPRS will display a default value in the Days Supply and Quantity fields. The quantity is calculated based on the formula Days Supply x Schedule = Quantity. If necessary, you can change the value in these fields. Note: If you change a number, CPRS will attempt to recalculate the other field.](#_Toc17877604)](#_Toc17877476)

14. 
15. 
16. 
17. 
18. 
19. 
20. 
- 
- 
21. 

> [[Enter the number of refills. Select the location where the patient should pick up the medication from the Pick Up field. <span id="Ind_Ord_Outpt_complex_dose_step" class="anchor"></span>Enter an Indication. If they have been entered, you can use the drop-down list and select the indication or you can type an indication in the field. Add comments if necessary. Under certain circumstances, a check box may appear under the Days Supply field. If the medication is service-connected, make sure the box is checked. Select Accept Order. (Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following: To proceed, select Accept Order. To stop the ordering process and return to the dialog, Cancel Order. If you are finished ordering outpatient medications, select Quit. Note: The order must be signed before it is sent. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[The Joint Commission on Accreditation of Healthcare Organizations (JCAHO) has indicated that all medications, including herbal supplements, over-the-counter (OTC) non-prescription medications, and medications prescribed by providers outside the VA (collectively known as "Non-VA medications") should be entered in the medical record. CPRS, Outpatient Pharmacy, and Inpatient Medications developers have made changes that enable users to enter this information into the medical record so that providers have a better picture of the medications the patient is taking and that order checks against these medications can occur. Entering Non-VA Medications will trigger the following order checks:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[Duplicate Drug (shows as Duplicate Order check) Duplicate Drug Class Critical Drug Interaction Significant Drug Interaction Allergy checks Note: For Non-VA meds, inpatient orders are not checked against Non-VA medications and the allergy check is slightly different. The duplicate drug class check will not be triggered for two pure herbal medications, such as ginger and gingko. All pure herbal medications belong to the same drug class (HA000). If these checks were made, every time a clinician entered a pure herbal medication, the user would receive a duplicate drug class warning. Allergy checks will still occur for non-VA medications that do not belong to this drug class.](#_Toc17877604)](#_Toc17877476)

[[For users to be able to enter these medications through CPRS, they must be in the CPRS Orderable Items file so that they appear when the user chooses the new order sheet. The Pharmacy patch (PSS\*1.0\*68) enables sites to mark items as Non-VA Medications. Initially, all Pharmacy orderable items that are marked as "outpatient" and are not supply items will be automatically made Non-VA medications. Subsequently, Pharmacy coordinators can use the Pharmacy option Drug Enter/Edit \[PSS DRUG ENTER/EDIT\] to identify items as Non-VA Meds or remove the designation.](#_Toc17877604)](#_Toc17877476)

[[Note: For more information about how to get Non-VA Medications added to the appropriate file, please see "Section 5.1: Communicating New Non-VA Meds Entries to the Pharmacist" in the *Herbal/OTC/Non-VA Meds Documentation Release Notes* that will be located on the VistA Documentation Library at <http://www.va.gov/vdl> under the Outpatient Pharmacy listings.](#_Toc17877604)](#_Toc17877476)

[[Remember that entering Non-VA Medications is not the same as placing orders. Users simply enter information to provide a more complete view of what the patient is taking. However, once the items are available in the CPRS Orderable Items file, the process for entering Non-VA Medications is similar to entering other orders, but there are a few differences:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[Almost any CPRS user can enter Non-VA medication information. However, sites can restrict access for those holding the OREMAS key by using the OR OREMAS NON-VA MEDS parameter. For more information about this parameter, please see the CPRS Technical Manual: GUI Version. Users can enter Non-VA medication even if they only have partial information. The only required information is the non-VA or herbal medication name. The Medication name must be one that can be selected from the list. The Dosage, Route, and Schedule fields are optional and will accept free-text entries. Non-VA medications are listed separately on the orders tab and the designation "Non-VA Med" is displayed at the beginning of the entry. Users may to pick a reason why the patient is taking the Non-VA medication. For the reason/statement that users should enter, developers sent out four reasons or](#_Toc17877604)](#_Toc17877476)

[[statements at the package level of the parameter GUI Non-VA Med Statements/Reasons that were agreed upon by a workgroup:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[Non-VA medication not recommended by VA provider. Non-VA medication recommended by VA provider. Patient wants to buy from Non-VA pharmacy. Medication prescribed by Non-VA provider. Authorized users can enter their own reasons/statements in the parameter by entering new statements at the System or Division level for this parameter. For more information about changing this parameter, see the *CPRS Technical Manual: List Manager*.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[Previously, the designation "Non-VA Meds" caused some confusion as to whether providers were ordering or documenting outside medication. Therefore, throughout CPRS the name has been changed to "Non-VA Medications (Documentation)" or "Non-VA Meds (Documentation)". When the user selects the Non-VA Medications (Documentation) option, the dialog displays the items that were marked as Non-VA Meds and copied into the CPRS Orderable Items file.](#_Toc17877604)](#_Toc17877476)

[[To enter Non-VA medication information, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[If you are not already there, go to the Orders tab by either clicking Orders or pressing Ctrl + O. In the Write Orders list, select Meds, Non-VA. Note: If encounter information has not been entered, the encounter information dialog will appear before the Medication Order dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

3.  1.  

> [[In the Document Herbal/OTC/Non-VA Medications dialog, select the medication or herbal supplement by Typing a few letters of the name or its synonym (if your site uses synonyms). Note: CPRS now only auto-selects (highlights in blue and places that entry in the field) a medication, dosage, route, or schedule if the user types enough characters to uniquely identify an item in the list. If the user does not enter enough characters to uniquely identify an item, CPRS waits until the user manually selects an item using the mouse or the keyboard.](#_Toc17877604)](#_Toc17877476)

2.  

> [[Selecting the correct name from the list by double-clicking it or highlighting it and pressing \<Enter\>. You may need to scroll down to find the name. Note: If you do not know other information such as dosage, route, or schedule, you may enter only the name of the medication or herbal supplement.](#_Toc17877604)](#_Toc17877476)

4.  

> [[Enter a dosage (if known). The dosage may not begin with a decimal, for example .5; it must begin with a numerical value, 0.5 for example. (The associated cost is displayed to the right of the dosage.)](#_Toc17877604)](#_Toc17877476)

5.  
6.  
7.  
8.  
9.  
10. 
11. 
12. 
13. - 
    - 
14. 
15. 

> [[Enter a route (if known). Enter a schedule, including PRN if necessary (if known). <span id="Ind_Non_VA_meds_2nd_step" class="anchor"></span>(Optional) Enter an Indication. If they have been entered, you can use the drop-down list and select the indication or you can type an indication in the field.Enter any comments. If you want to enter one, select one or more Statements/Explanations as to why the patient is taking the medication or supplement. Enter a start date (if known). Review the information entered in the text box at the bottom of the dialog. Place the information into the patient's record by clicking Accept Order or by tabbing to Accept Order and pressing \<Enter\>. (Conditional) If the medication ordered may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and decide if the medication should be ordered. Do one of the following: To proceed, select Accept Order. To stop the ordering process and return to the dialog, Cancel Order. To enter additional Non-VA Medications into the patient's record, repeat steps 3-12. When you are through entering Non-VA medications, exit the dialog using the Quit button. Note: Non-VA Meds do not require an electronic signature, but they will be presented at the end of the current CPRS session on the Sign screen. You can do the normal signing process or if you only have Non-VA meds, you might get OK and Cancel buttons on a dialog instead of the normal Sign screen. You cannot click on the checkbox in front of a Non-VA Med to deselect and not approve it. Non-VA Meds because they do not require electronic signature will be automatically entered when you click OK or enter your electronic signature.](#_Toc17877604)](#_Toc17877476)

[[When you start documenting non-VA medication information for a complex dose, you need to remain on the Complex tab until you click the Accept Order button. If you switch to the Dosage tab, all complex dosages will be erased.](#_Toc17877604)](#_Toc17877476)

[[To document Non-VA medication information for a complex dose, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[From the Orders tab, select Non-VA Meds in the Write Orders table.Note: If encounter information has not been entered, the encounter information dialog will appear. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

17. 
40. 
41. 

> [[In the Document Herbal/OTC/Non-VA Medications dialog, select the medication or herbal supplement from the dropdown. If you enter a few characters in the Name field, you will immediately see a list of names in the dropdown that contain those characters.Select the Complex tab.Enter the appropriate dosage in the Dosage field. Note: The dosage must begin with a numerical value (for example, 0.5). The dosage cannot begin with a decimal (for example, .5) and the "^" character is not allowed.](#_Toc17877604)](#_Toc17877476)

42. 
43. 
44. 
45. 

> [[Enter a Route by either selecting a value from the dropdown or entering a value. Select a value from the Schedule dropdown. Check the PRN checkbox, if necessary.In the Duration field, enter a numeric value and select the units a patient should use for the specified dose (day is the default).In the add/then dropdown, select a direction and a conjunction (no conjunction on the final line). Note: If you select the "then" conjunction, you are required to add a duration.](#_Toc17877604)](#_Toc17877476)

46. 
47. 
48. 
49. 

> [[In the next row, enter a dosage in the Dosage field. If necessary, change the values in the Route and Schedule fields. In the add/then dropdown, enter a duration and a conjunction (no conjunction on the final line). Repeat steps 4 through 11 until you have completed the complex dose. Note: To add a row, click on the area where you want to place the new row and then, click on the Insert Row button. To remove a row, click on the row to be deleted and then, click on the Remove Row button.](#_Toc17877604)](#_Toc17877476)

50. 
51. 
52. 
53. 
54. 
55. 
56. 
57. 

> [[Enter an Indication (optional). If indications are defined, they will display in the drop-down list or you may type in an indication.Add a comment (optional). Select one or more Statements/Explanations as to why the patient is taking the medication or supplement (optional).Enter a Start Date, if known. A Start Date can be a date in the past.Review the information entered in the textbook at the end of the dialog.Click the Accept Order button.(Conditional) If the non-VA medication may be contraindicated because of allergies, drug interactions, or duplicate orders, CPRS will display the Order Check window. Carefully review all order checks and either click the Accept Order button or the Cancel Order button.When you finish documenting non-VA medications, click the Quit button.Note: Non-VA Meds do not require an electronic signature. At the end of the current CPRS session, you will see the Review/Sign Changes window and will be able to click on the OK or Cancel button without signing the order. After you click the OK button, you may see the Order Checks screen if there is a potential conflict between a non-VA med and an existing inpatient or outpatient order.](#_Toc17877604)](#_Toc17877476)

[[CPRS enables providers to order blood products. The Blood Components and Diagnostic Test Orders dialog has three tabs: Patient Information, Orders, and Lab Results. Because this dialog is modal, meaning that it stays on top of CPRS, these tabs enable the provider to have the necessary information at the time of ordering.](#_Toc17877604)](#_Toc17877476)

[[If the user selects an item under the Order tab's Write Orders pane or from an order menu, the Blood Components and Diagnostic Test Order Form dialog opens to the Patient Information tab. But, if the user selects a quick order that is not an auto accept quick order or elects to edit or copy an existing order, the dialog will open to the Blood Bank Orders tab.](#_Toc17877604)](#_Toc17877476)

[[The Patient Information tab displays identifying information for the selected patient (name, social security number, and blood type), along with the following information:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- - 
  - 
  - 
- 
- 
- 
- - 
  - 

[[On the Blood Bank Orders tab, providers can place orders for blood components and diagnostic tests that need to be done before the components can be given to the patient. As with many types of orders, the user can create personal quick orders for blood components and tests the user frequently orders.](#_Toc17877604)](#_Toc17877476)

[[On this dialog the user specifies:](#_Toc17877604)](#_Toc17877476)

- - 
  - 
  - 
  - 
  - 
  - 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Blood Components – The list of items comes from CPRS from a parameter and shows what blood products can be offered. Items might include: Red blood cells Fresh frozen plasmaPlateletsCryoprecipitate Whole blood Other Modifiers – The modifiers are controlled by a parameter that is set at each site. It might include things such as washed, irradiated, etc. <span id="VBECS_Date_Time_wanted_ALL" class="anchor"></span>For All Components--Date/Time Wanted\* - The date and time when the blood components should be ready that enables the user to order the blood for a future date, such as for a surgery. Urgency\* – This list comes from CPRS and might include items such as Routine, Pre-op, ASAP, or STAT. The urgency applies to all items listed under the Selected Components and Tests area. Surgery (conditional) – If the user selects Pre-Op for the urgency, the Surgery field becomes active and the provider can select the surgery to be performed from the drop-down list or enter it manually. If the surgery is not listed, the provider may enter a surgery (the field accepts free-text) because this is not a comprehensive list of surgeries. Reason for Request\* – The user can choose a reason from the drop-down list (sites define items in the list using a parameter) or type a free-text entry. This reason for request applies to the entire order. Comment\* – If the provider has information that should be passed on with the order, the comments can be added in this field. The comments apply to the entire order. (This is a required field if the user selects the Blood Component "Other.") Diagnostic Tests – The items on this list comes from CPRS and enable the provider to request specific tests associated with blood component ordering. When the user selects this item, the fields under blood components are then cleared. The user can see those items again by highlighting the blood component under Selected Blood Components and Tests. Collection Type\* – The collection type determines how the specimen should be collected: Lab collect, Ward collect, Send patient to Lab, or Immediate collect, for example. Collection Date/Time\* – The date and time enable the user to specify when the sample should be collected. Items required to order each blood component or diagnostic test are marked with an asterisk (\*) after the name of the field, such as Reason for Request\*.  
](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

[[Date/Time Wanted for ALL componentsdiagnostic test Collection Type diagnostic test Collection Date/Time Comments Reason for Request Urgency The Date/Time Wanted for All Component (as the name implies) applies to all blood components and defaults for the diagnostic tests. Modifiers apply only to blood components.](#_Toc17877604)](#_Toc17877476)

[[Also, when the user moves the focus to either the Blood Components or the Diagnostic Tests area, values for the last item entered in that area display so that the user can edit the values. If the user wants to edit another item, the user must select it from the Selected Components and Test area first.](#_Toc17877604)](#_Toc17877476)

[[Each site can configure some areas of the Blood Component and Diagnostic Test Order Form dialog. A CPRS parameter lets sites decide if the Blood Component area or the Diagnostic Test area is shown on the left of the dialog. The other area then displays next to the first area on the right of the dialog.](#_Toc17877604)](#_Toc17877476)

[[Sites can also customize the order of the following lists:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[The Blood Components The Diagnostic Tests The Reason for Request The order of items in these lists is controlled by parameters set by Clinical Application Coordinators (CACs). CACs can therefore put the most used items earlier in the list.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[Go to the Orders tab, by clicking on the tab or pressing Ctrl + O. Under Write Orders, select Blood Bank (or whatever your site names the VBECS item). Review the Patient Information tab for pertinent information.Select the Blood Bank Orders tab. The following dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/409.png)](#_Toc17877604)](#_Toc17877476)

> [[This dialog enables users to electronically enter orders for blood products and diagnostic tests, view information about blood products related to this patient, and view lab information, if available, related to the blood product or test selected. The location of the Diagnostic Tests and Blood Components areas might be switched at different sites because this can be configured at each site. Date/Time Wanted applies to all components.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select the needed blood component from the drop-down list. (When the user selects a blood component or a diagnostic test, the quick order field is no longer displayed). Note: For some blood components, a message may appear under the Diagnostic Test drop-down list indicating that a diagnostic test, such as a type and screen, is needed. However, you may want to complete all the fields for the blood component first. Otherwise, you will have to switch back to fill out the needed fields. Also, if there are lab results, they will now be on the Lab Results Available tab.](#_Toc17877604)](#_Toc17877476)

6.  
7.  
8.  
9.  
10. 
11. 

> [[Enter the quantity. (Optional) Select a modifier from the list if needed. Indicate when all blood product components are needed by accepting the default of Now, typing in date, or using the calendar control (the button with three dots) to select a date and time. Select the urgency from the drop-down list. If you select Pre-Op, you must select a surgery from the drop-down list. If you select Pre-Op and choose a surgery, the Reason for Request field is automatically populated with the surgery. However, you can also type in a reason for request. (It must be less than 76 characters.) Note: If you select a surgery that is listed in the MSBOS as not requiring blood components, CPRS displays a dialog warning that no blood is required for the surgery. The MSBOS contains a list of how many units of blood are generally used for the specified surgery.](#_Toc17877604)](#_Toc17877476)

12. 
13. 

> [[Under Comment, type any needed comments. If a diagnostic test is needed, select the appropriate test under Diagnostic tests. Note: When you choose a diagnostic test, the fields relating to the blood component are cleared. If you want to see or edit them again, highlight the blood component under the Blood Component and Diagnostic Test area.](#_Toc17877604)](#_Toc17877476)

14. 

> [[Select the collection type from the drop-down list. Note: Which collection type the user selects first affects the default start time that displays. If Ward Collect is selected first, the default is NOW and stays NOW even if Send Patient is then selected. If Send Patient is selected first, then the default is TODAY and stays TODAY even if Ward Collect is then selected. Immediate collect defaults to a time 10 minutes in the future.](#_Toc17877604)](#_Toc17877476)

15. 
16. 
17. 
18. 
19. 

[[Enter the time and date for the specimen collection. To order more blood components, repeat steps 5-12. To order additional diagnostic tests, repeat steps 13-15. When you have finished, review the order text at the bottom of the dialog. When you have the order defined as wanted, select Accept Order. Note: For nursing administration orders, sites will have to create their own orders.](#_Toc17877604)](#_Toc17877476)

[[To create blood component and diagnostic test personal quick orders, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

> [[Follow steps 1-18 above. Instead of selecting Accept Order, go to the main CPRS window and select Options \| Save as Quick Order…. In the Add Quick Order (Blood Bank) dialog, type the name for your personal quick order. If you want to change where the order will appear in the list, highlight the order and use the arrow buttons on the left of the dialog to move it up or down in the list. Select OK. After creating the personal quick order, the next time you open the Blood Components and Diagnostic Tests Order Form, your personal quick orders will be listed in the first field.](#_Toc17877604)](#_Toc17877476)

> [[Note: For nursing administration orders, sites will have to create their own orders.](#_Toc17877604)](#_Toc17877476)

[[To place blood bank orders using personal quick orders, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[Go to the Orders tab, by clicking on the tab or pressing Ctrl + O. Under Write Orders, select Blood Bank (or whatever your site names the VBECS item). Select the Blood Bank Orders tab. Select the appropriate personal quick order from the drop-down list. Note: If you inadvertently select the wrong quick order, you can choose Remove All or Cancel to exit the dialog and then reenter the dialog.](#_Toc17877604)](#_Toc17877476)

5.  
6.  

> [[Make any changes or additions as needed. Remember that to change part of an order you must highlight that item in the list first. When finished, select Accept Order. Note: For nursing administration orders, sites will have to create their own orders.](#_Toc17877604)](#_Toc17877476)

[[The Lab Results tab enables clinicians to view the lab results associated with the selected blood component. If there are lab results in the system when the user selects a blood component, the tab name changes to Lab Results Available. This tab then shows the results from the lab tests designated in VBECS by the administrator at each site. So, for example, the user might see different lab test results based on whether the user selected whole blood or platelets.](#_Toc17877604)](#_Toc17877476)

[[Note: The most recent results are displayed, but these results may be from tests done some time in the past. Users should use good judgment as to whether they should order a new test.](#_Toc17877604)](#_Toc17877476)

[[There are several different kinds of infusion orders, including intravenous (IV), epidural, IV piggyback, etc.](#_Toc17877604)](#_Toc17877476)

[[In the Infusion Order dialog, the order type—Continuous or Intermittent— affects whether some fields are available or visible. The two types of IVs are defined as follows:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[Continuous infusion orders run at a specified rate. As the user selects a solution and/or additive, the items from that list are displayed to the right under Solution/Additive. For continuous infusion orders the only optional fields are the Comments and the Duration or Total Volume fields. The schedule field is not available.](#_Toc17877604)](#_Toc17877476)

[[With the CPRS GUI v.28, a new Additive Frequency field was added to the Infusion Order dialog. Users must select from this field into which IV bag the additive should be placed:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

> [[1 Bag/Day: The additive should be put in one bag for 24 hours, normally the first bag. All Bags: The additive should be placed in all bags given to the patient. See Comments: The provider wants something other than the above options and will put appropriate instructions in the Comments box. Note: If the user selects "See Comments" for the Additive Frequency but does not enter appropriate instructions in the Comments box, Pharmacy may interpret that as All Bags.](#_Toc17877604)](#_Toc17877476)

[[To order continuous infusion orders, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane -or- select View \| Active Orders (includes pending, recent activity). Select Infusion (or your site's equivalent) in the Write Orders list box. Note: The Infusion item may be labeled differently or may not be available from your Write Orders list box.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

> [[The Infusion Order dialog displays as shown below.](#_Toc17877604)](#_Toc17877476)

> [[<span id="Ind_Ord_continuous_infuse_capt" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/410.png)](#_Toc17877604)](#_Toc17877476)

> [[The Infusion Order dialog for continuous infusion orders does not use a schedule, but it does have an infusion rate. For continuous infusion orders, the new Additive Frequency field enables providers to indicate into which IV bag the additive should be placed](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog will appear before the Infusion Order dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

4.  
5.  - 
    - 
    - 

> [[Select the needed solutions from the Solutions tab. Select an additive from the list (if necessary) and edit the strength if needed. Repeat for additional additives if necessary. How users can edit the strength field will depend on the values for strength defined in the pharmacy files as follows: If a single strength is defined, users cannot edit the field. If multiple values for strength are defined in the pharmacy files, the field will have a drop-down list from which users can choose a strength. If no values have been defined, users can type in a strength. If a strength includes a decimal point, the value must begin with a number: so, .5 is not valid, but 0.5 is. The solution and additives you select will appear in the Solution/Additive grid.](#_Toc17877604)](#_Toc17877476)

> [[Note: To remove an additive or a solution, select the solution or additive and select Remove.](#_Toc17877604)](#_Toc17877476)

6.  
7.  - 
    - 
    - 
8.  
9.  

> [[Enter a volume and strength in the Solution/Additive grid (if necessary). Select the Additive Frequency from the list: 1 Bag/Day: The additive should be put in one bag for 24 hours, normally the first bag. All Bags: The additive should be placed in all bags given to the patient. See Comments: The provider wants something other than the above options. Enter the appropriate instructions in the Comments box. Select a Route (such as intravenous, epidural, IV piggyback, etc.) If the desired route is not available, select the Other option in the list of routes to bring the expanded med route form that lists all possible IV routes. In the Type field, select Continuous. Note: If you change the IV Type from Continuous to Intermittent, the Schedule field becomes available and the Infusion Rate field becomes the Infusion over Time field.](#_Toc17877604)](#_Toc17877476)

> [[Note: For a definition of Continuous and Intermittent orders, select the IV Type Help link and a message box will display with a short definition of what the terms mean.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/411.png)](#_Toc17877604)](#_Toc17877476)

10. 
11. 
12. 
13. 

> [[Enter an infusion rate in ml/hr. Select a Priority. (Optional) Enter a number for the duration or total volume of fluids for this order. Select the appropriate unit (liters-L, milliliters-ml, days, or hours). Note: If you change the units, the value in the Duration or the Total Volume field will be removed and you will need to enter it again. This is a safety feature to ensure the patient does not receive a dangerous amount of fluid.](#_Toc17877604)](#_Toc17877476)

14. 
15. 
16. 
17. 
18. 

> [[<span id="Ind_Ord_continuous_infuse_step" class="anchor"></span>Enter an Indication. If they have been entered, you can use the drop-down list and select the indication or you can type an indication in the field. Enter any comments (if necessary). Review the order text at the bottom of the dialog to ensure that it is correct. Select Accept Order. Enter another order -or-](#_Toc17877604)](#_Toc17877476)

> [[Select Quit.](#_Toc17877604)](#_Toc17877476)

> [[Note: The order must be signed before it is sent. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane -or- select View \| Active Orders (includes pending, recent activity). Select Infusion (or your site's equivalent) in the Write Orders list box. Note: The IV fluids item may be labeled differently or may not be available from your Write Orders list box.](#_Toc17877604)](#_Toc17877476)

> [[The Infusion Order dialog displays as shown below.](#_Toc17877604)](#_Toc17877476)

> [[<span id="Ind_Ord_intermit_infuse_capt" class="anchor"></span>![](cprs-user-manual-gui-version-updated-or-3-0-499/413.png)](#_Toc17877604)](#_Toc17877476)

> [[The Infusion Order dialog for intermittent infusion orders](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog will appear before the Infusion Order dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select a solution from the Solutions tab. After you select a solution, CPRS automatically moves to the Additives tab.](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select an additive from the list (if necessary). Repeat for additional additives if necessary. The solution and additives you select will appear in the Solution/Additive grid.](#_Toc17877604)](#_Toc17877476)

> [[Note: To remove an additive or a solution, select the solution or additive and click Remove.](#_Toc17877604)](#_Toc17877476)

6.  
7.  
8.  

> [[Enter a volume and strength in the Solution/Additive grid (if necessary). Select the Route (for example, intravenous, epidural, IV piggyback, etc.) from the drop-down list. If the desired route is not available select the Other option in the list of routes to bring the expanded med route form that list all possible IV routes. In the Type drop-down box, select Intermittent. Note: If you change the IV Type from Intermittent to Continuous, the Schedule field becomes unavailable (greyed out) and the Infusion over Time field becomes the Infusion Rate field.](#_Toc17877604)](#_Toc17877476)

> [[Note: For a definition of Continuous and Intermittent orders, select the IV Type Help link and a message box will display with a short definition of what the terms mean.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/414.png)](#_Toc17877604)](#_Toc17877476)

9.  

> [[Select a schedule from the list or create one using the Day-of-Week schedule builder. Note: When a user writes an intermittent infusion order with a schedule of ONCE, the following will happen in CPRS:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

> [[The DURATION field will be disabled. The Give Additional Dose Now option will be disabled Expected First Dose and Administration Times will not be displayed Note: When a user writes an intermittent infusion order with a schedule of On Call or a PRN, the following will happen in CPRS:](#_Toc17877604)](#_Toc17877476)

- 
10. 
1.  
2.  

> [[Expected First Dose and Administration Times will not be displayed If you selected an existing schedule, skip to step 13. If you selected OTHER, CPRS displays the Order with Schedule 'OTHER' dialog. Take the following steps: Select one or more checkboxes by the appropriate days of the week. If the schedule requires specific administration times skip to steps c and d. To select a schedule from the list, highlight the schedule and select Add. Note: Users can assign either a schedule from the list or specific administration times, but not both.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[To use a specific administration time, select the hour and minutes (if the user only selects the hour, the minutes will default to zero) and select Add. Repeat step c until you have entered all required administration times. Warning: The administration times in the Schedule field apply to each day of the week that is listed, such as TU-TH-SA@08002000, for example. To create a schedule such as TU@0800 TH@2000, users would have to enter two separate orders using the complex medication order dialog. Also, users may not enter a schedule that only has administration times and PRN but no days.](#_Toc17877604)](#_Toc17877476)

5.  - 

> [[If you make a mistake while selecting an administration time or schedule, do one of the following to remove it: For a single administration time, highlight the hour and minutes in the Set Administration Time fields and select Remove (so to remove 08:00, you would have to select that time in the Set Administration Time fields not in the Schedule text box.) o To remove the schedule, highlight the schedule and select Remove.](#_Toc17877604)](#_Toc17877476)

- 
6.  
7.  
11. 
12. 
13. 

> [[To remove the entire schedule and begin again with step a, select Reset. Review the Schedule field. When you have the correct schedule, select OK. If necessary, select the PRN checkbox. Enter the number for the duration over which to infuse the medication. Move to the next field and select the unit of time (the units can be only Minutes or Hours) over which the infusion should be given. For example, you might enter 30 for the number, move to the next field, and then select minutes to define infuse over 30 minutes.](#_Toc17877604)](#_Toc17877476)

14. 
15. 
16. 

> [[Select the Priority. Enter a number for the duration or total volume. Move to the next field and select the appropriate unit (liters-L, milliliters, days, hours, or doses). Note: If you change the units, the value in the Duration or the Total Volume field will be removed and you will need to enter it again. This is a safety feature to insure the patient does not receive a dangerous amount of fluid.](#_Toc17877604)](#_Toc17877476)

17. 

> [[If necessary, select the Give additional dose now checkbox. Note: Make sure that you are careful about using give-additional-dose now functionality. When you click the check box, CPRS creates two new orders and sends it to Inpatient Medications. Make sure the "Give additional dose now" and the regular order with the original schedule you entered do not overmedicate the patient. "Give additional dose now" is not available for ONCE, ONE-TIME, or NOW orders. It is also not available for delayed orders.](#_Toc17877604)](#_Toc17877476)

18. 
19. 
20. 
21. 
22. 

> [[Enter an Indication. If they have been entered, you can use the drop-down list and select the indication or you can type an indication in the field.Enter any comments (if necessary). Review the order text at the bottom of the dialog to ensure that it is correct. If the order text is correct, select Accept Order. Enter another order -or-](#_Toc17877604)](#_Toc17877476)

> [[Select Quit.](#_Toc17877604)](#_Toc17877476)

> [[Note: The order must be signed before it is sent. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[Ordering supplies has changed a little in CPRS. Previously, supplies were included in the Medication Order dialog. This was not an ideal situation because those who might only be tasked with ordering supplies might inadvertently select a medication. In addition, nurses and clerk might also have to have additional permissions to order supplies that would allow them to order medications as well.](#_Toc17877604)](#_Toc17877476)

[[To place simple supply orders, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
9.  
10. 
11. 
12. 

[[Ordering supplies has changed a little in CPRS. Previously, supplies were included in the Medication Order dialog. This was not an ideal situation because those who might only be tasked with ordering supplies might inadvertently select a medication. In addition, nurses and clerk might also have to have additional permissions to order supplies that would allow them to order medications as well.](#_Toc17877604)](#_Toc17877476)

[[To place complex supply orders, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
9.  
10. 
11. 
12. 
13. 
14. 
15. 
16. 
17. 
18. 
19. 

[[To place an order for a lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane -or- select View \| Active Orders (includes pending, recent activity). Select Lab Tests in the Write Orders list. Note: The lab tests order may be labeled differently or may not be available from your Write Orders field.](#_Toc17877604)](#_Toc17877476)

> [[The Order a Lab Test dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/415.png)](#_Toc17877604)](#_Toc17877476)

> [[The Order a Lab Test dialog](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog will appear before the Order a Lab Test dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

4.  
5.  
6.  
7.  
8.  
9.  

> [[Select the desired lab test in the Available Lab Tests list box. If desired, change the default values for the Collection Sample, Specimen, and/or Urgency fields. If you cannot change a field, the text label (to the left of the field) will be dimmed. Select the collection type. Choose a collection date and time. Complete the How Often? and How Long? fields (if necessary). Select Accept Order. Note: If you have selected an inpatient order with a collection type of "lab collect" or "immediate collect" and if a continuous schedule was selected (such as QD or QWEEKLY) and a child order falls on a day when the lab cannot perform the collection (for example, weekends or holidays), CPRS displays a message telling the user that the collection type will be changed to "ward collect" or of any such changes to child orders.](#_Toc17877604)](#_Toc17877476)

10. 

> [[Enter another lab test -or-](#_Toc17877604)](#_Toc17877476)

> [[select Quit.](#_Toc17877604)](#_Toc17877476)

> [[Note: The Lab Test order must be signed before it is sent. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[Atomic Pathology (AP) laboratory service now has a mechanism for clinicians to provide required patient-specific, procedure-specific, and specimen-specific information to facilitate specimen processing by pathologists.](#_Toc17877604)](#_Toc17877476)

[[A new Anatomic Pathology Order Dialog is available with the following available order types:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Bone MarrowBronchial BiopsyBronchial CytologyDermatologyFine Needle AspirateGastrointestinal EndoscopyGeneral FluidGynecology (Pap Smear)Renal BiopsyTissue ExamUrineUrology, Bladder/UreterUrology, Prostate  
](#_Toc17877604)](#_Toc17877476)

[[When opening the Anatomic Pathology order dialog, you must first select one of the available order types, such as seen below, for example Bone Marrow, Bronchial Biopsy, etc. ](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/416.png)  
Because each order type may require different information, different order dialog fields display when the user selects an order type.  ](#_Toc17877604)](#_Toc17877476)

[[](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/417.png)](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  

[[Order-specific fields such as Urgency and Collection Date/Time.List of Specimens for this order.The Current Specimen being viewed in box 4.Specimen-specific fields, such as the Specimen Description/Anatomic Site and Collection Sample.Button to delete the current specimen.Several Multiple tabs to enter free text fields, such as Clinical History.](#_Toc17877604)](#_Toc17877476)

[[In box 2 above, the Current Specimen List:](#_Toc17877604)](#_Toc17877476)

- 

> [[Some dialogs have a "+" button at the top of the list of specimens. Click this button to add an additional specimen.![](cprs-user-manual-gui-version-updated-or-3-0-499/418.png)](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

> [[Other dialogs have a dropdown list. When first selecting these dialog types, the dropdown list will automatically open. Select an entry from the list to create your first specimen.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/419.png)](#_Toc17877604)](#_Toc17877476)

- 

> [[To add an additional specimen, you must click on the down arrow button to open the list of types. Select an option from the dropdown list to add an additional specimen.![](cprs-user-manual-gui-version-updated-or-3-0-499/420.png)](#_Toc17877604)](#_Toc17877476)

- 

> [[To navigate between specimens, click the entry in the list. The current specimen is shown on the right.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/421.png)](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[After the order is accepted, it can be viewed on the Orders tab. Users must sign the order before it will be available in the Lab package.](#_Toc17877604)](#_Toc17877476)

[[The order number and the lab number are both available in the CPRS Order Details display.](#_Toc17877604)](#_Toc17877476)

[[After the order is completed, your local site will need to follow your procedures for creating a requisition and specimen label. One possibility is to print the order details and use them in place of the SF 515 as a requisition. While this is one possibility, the site will need to choose how to handle printing the requisition and labeling the specimen.](#_Toc17877604)](#_Toc17877476)

[[To place an order for a Bone Marrow lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list.Note: The orders listed in the Write Orders pane vary from site to site.](#_Toc17877604)](#_Toc17877476)

56. [[If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location.](#_Toc17877604)](#_Toc17877476)
57. [[Choose the Date/Time of the visit.](#_Toc17877604)](#_Toc17877476)
58. [[Select OK.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

59. [[Select Bone Marrow in the Available Lab Tests list box. The Bone Marrow dialog displays as shown below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/431.png)Bone Marrow dialog](#_Toc17877604)](#_Toc17877476)

60. [[Select the Specimen Description on the left side of the dialog box and choose a specimen. If this is the first specimen, use the +key located above the Specimen Description field. Use the drop-down list for subsequent specimens.](#_Toc17877604)](#_Toc17877476)

[[Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

61. [[If desired, change the default values for Urgency and/or Collection Date/Time fields. These are required fields.](#_Toc17877604)](#_Toc17877476)
62. [[If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person entering the order.](#_Toc17877604)](#_Toc17877476)
63. [[Select the Surgeon/Physician field and choose a surgeon/physician.](#_Toc17877604)](#_Toc17877476)
64. [[If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces.](#_Toc17877604)](#_Toc17877476)
65. [[Select the Source. Choose a source for the specimen (Left Anterior Iliac Crest,Left Posterior Iliac Crest,Right Anterior Iliac Crest,Right Posterior Iliac Crest, or Sternum).](#_Toc17877604)](#_Toc17877476)

[[Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
66. [[Select the Specimen Type. Choose a specimen type (Aspirate or Core Biopsy).](#_Toc17877604)](#_Toc17877476)

[[Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
67. [[If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces.](#_Toc17877604)](#_Toc17877476)
- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

68. [[Select the Clinical History tab. Enter the patient's history in the Clinical History field. This is a required field that allows letters, numbers, punctuation, and spaces.](#_Toc17877604)](#_Toc17877476)
69. [[Select the Pre-Operative Diagnosis tab. Enter the patient's pre-operative diagnosis in the Pre-Operative Diagnosis field. This is a required field that allows letters, numbers, punctuation, and spaces.](#_Toc17877604)](#_Toc17877476)
70. [[Select Accept Order.](#_Toc17877604)](#_Toc17877476)
71. [[Preview the order.](#_Toc17877604)](#_Toc17877476)
72. [[If desired, modify the order by selecting the Back button, or select the Accept Order button to accept the order.](#_Toc17877604)](#_Toc17877476)
73. [[If desired, enter another lab test.](#_Toc17877604)](#_Toc17877476)

[[To place an order for a Bronchial Biopsy lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list.If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location.Choose the Date/Time of the visit. Select OK.Select Bronchial Biopsy in the Available Lab Tests list box. The Bronchial Biopsy dialog displays.Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the +key located above the Specimen Description field. Use the drop-down list for subsequent specimens.Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 

[[If desired, change the default values for Urgency and/or Collection Date/Time fields. (These are required fields).If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person performing the procedure.Select the Surgeon/Physician field. Choose a surgeon/physician.If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces.Select the Source. Choose a source for the specimen (Bronchial, Left Lower Lobe (LLL) Bronchial, Left Upper Lobe (LUL) Bronchial, Lingula, Main Stem Bronchus, Right Lower Lobe (RLL) Bronchial, Right Middle Lobe (RML) Bronchial, or Right Upper Lobe (RUL) Bronchial).Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
13. 

[[Select the Specimen Type. Choose a specimen type (EBUS-TBNA, Endobronchial Biopsy, or Transbronchial Biopsy).Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
14. 
- [[Select the Station. Choose a station(Station 10, Station 2, Station 4, or Station 7).If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
15. 
- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
16. 
- [[If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

17. 
18. 
19. 
20. 
21. 
22. 
23. 

[[Select the Clinical History tab. Enter the patient's history in the Clinical History field. This is a required field that allows letters, numbers, punctuation, and spaces.Select the Pre-Operative Diagnosis tab. Enter the patient's pre-operative diagnosis in the Pre-Operative Diagnosis field. This is a required field that allows letters, numbers, punctuation, and spaces.If desired, select the Operative Findings tab. Enter the patient's operative findings in the Operative Findings field. This is an optional field that allows letters, numbers, punctuation, and spaces.If desired, select the Post-Operative Findings tab. Enter the patient's Post-Operative Findings. This is an optional field that allows letters, numbers, punctuation, and spaces.Select Accept Order. Preview the order.If desired, modify the order by selecting the Back button, or select the Accept Order button to accept the order.  
](#_Toc17877604)](#_Toc17877476)

24. 

[[To place an order for a Bronchial Cytology lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list.If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location. Choose the Date/Time of the visit. Select OK.Select Bronchial Cytology in the Available Lab Tests list box. The Bronchial Cytology dialog displays.Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the +key located above the Specimen Description field. Use the drop-down list for subsequent specimens.Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 

[[If desired, change the default values for Urgency and/or Collection Date/Time fields. (These are required fields).If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person performing the procedure.Select the Surgeon/Physician field. Choose a surgeon/physician.If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces.Select the Source. Choose a source for the specimen (Bronchial, Left Lower Lobe (LLL) Bronchial, Left Middle Lobe (LML) Bronchial, Left Upper Lobe (LUL) Bronchial, Lingula, Main Stem, Right Lower Lobe (RLL) Bronchial, Right Middle Lobe (RML) Bronchial, or Right Upper Lobe (RUL) Bronchial).Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
13. 

[[Select the Specimen Type. Choose a specimen type (Bronchial-Alveolar Lavage (BAL), Brushing, Sputum, Wang Needle, or Washing).Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
14. 
- [[If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

15. 
16. 
17. 
18. 
19. 
20. 

[[To place an order for a Dermatology lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list.If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location.Choose the Date/Time of the visit. Select OK.Select Dermatology in the Available Lab Tests list box. The Dermatology dialog displays. Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the +key located above the Specimen Description field. Use the drop-down list for subsequent specimens.Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 
- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
13. 

[[Select the Specimen Type. Choose a specimen type (Biopsy, Excision, MOHS, Punch Biopsy 2 mm, Punch Biopsy 3 mm, Punch Biopsy 4 mm, Punch Biopsy 5 mm, Punch Biopsy 6 mm, Punch Biopsy 7 mm, or Punch Biopsy 8 mm, Shave Biopsy, or Shave ED&C).Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

[[Note: If a particular Punch Biopsy size is not available, you may enter it in the Specimen Description field. If information is already in the Specimen Description field, enter the Punch Biopsy size at the very end of the field and use a comma after the last character in the field before entering the information.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
14. 
15. 
- [[Select the Laterality. Choose the laterality (Left, Midline, or Right).If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

16. 
17. 
18. 
19. 
20. 
21. 
22. 
23. 

[[To place an order for a Fine Needle Aspirate lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list. Note: The orders listed in the Write Orders pane vary from site to site.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  
7.  

[[If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location. Choose the Date/Time of the visit. Select OK. Select Fine Needle Aspirate in the Available Lab Tests list box. The Fine Needle Aspirate dialog displays. Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the + key located above the Specimen Description field. Use the drop-down list for subsequent specimens. Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 
- [[If desired, change the default values for Urgency and/or Collection Date/Time fields. These are required fields. If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person entering the order. Select the Surgeon/Physician. Choose a surgeon/physician. If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces. If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

13. 

[[Select the Specimen Type. Choose a specimen type (Needle Core Biopsy, Needle Washing, or Slide). Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
14. 
15. 
1.  
4.  [[Select the Laterality. Choose the laterality (Left, Midline, or Right). Select the Clinical History tab. Enter the patient's history in the Clinical History field. This is a required field. Select a Collection Technique. Choose the collection technique (CT, Fluoroscopy, or Ultrasound). If desired, select Additional Clinical History. Enter information for additional clinical history. This field allows letters, numbers, punctuation, and spaces.](#_Toc17877604)](#_Toc17877476)
16. 
17. 
18. 
19. 
20. 

[[To place an order for a Gastrointestinal Endoscopy lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list. Note: The orders listed in the Write Orders pane vary from site to site.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  
7.  

[[If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location. Choose the Date/Time of the visit. Select OK. Select Gastrointestinal Endoscopy in the Available Lab Tests list box. The Gastrointestinal Endoscopy dialog displays. Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the + key located above the Specimen Description field. Use the drop-down list for subsequent specimens. Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 

[[If desired, change the default values for Urgency and/or Collection Date/Time fields. These are required fields. If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person entering the order. Select the Surgeon/Physician. Choose a surgeon/physician. If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces. Select the Technique. Choose the technique (Biopsy, Brushing, EMR, FNA, Hot Biopsy, or Hot Snare). Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
13. 

[[Select the Specimen Type. Choose a specimen type (Erosion, Lesion, Mass, Polyp, Random, or Ulcer). Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
14. 
- [[If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

15. 
1.  
2.  
16. 
17. 
18. 
19. 
20. 

[[To place an order for a General Fluid lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list. If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location. Choose the Date/Time of the visit. Select OK. Select General Fluid in the Available Lab Tests list box. The General Fluid dialog displays. Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the + key located above the Specimen Description field. Use the drop-down list for subsequent specimens. Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 

[[If desired, change the default values for Urgency and/or Collection Date/Time fields. (These are required fields). If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person performing the procedure. Select the Surgeon/Physician. Choose a surgeon/physician. If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces. When Synovial Cytologic Material is selected as a specimen, choose the Source for the specimen (Elbow, Knee, or Toe). The General Fluid dialog when Synovial Cytologic Material is selected as a specimen will display as shown below. Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
13. 

[[When Pleural Cytologic Material is selected as the specimen, choose the Laterality for the specimen of either Left or Right. The General Fluid dialog when Pleural Cytologic Material is selected as a specimen will display as shown below. Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
14. 
- [[If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

> [[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

15. 
16. 
17. 
18. 
19. 
20. 

> [[Select the Clinical History tab. Enter the patient's history in the Clinical History field. This is a required field that allows letters, numbers, punctuation, and spaces. Select the Pre-Operative Diagnosis tab. Enter the patient's pre-operative diagnosis in the Pre-Operative Diagnosis field. This is a required field that allows letters, numbers, punctuation, and spaces. Select Accept Order. Preview the order. If desired, modify the order by selecting the Back button, or select the Accept Order button to accept the order. If desired, enter another lab test. -or- Select Accept Order.](#_Toc17877604)](#_Toc17877476)

> [[-or-](#_Toc17877604)](#_Toc17877476)

> [[Select Quit.](#_Toc17877604)](#_Toc17877476)

> [[Note: The Lab Test order must be signed before it is sent to VistA to be accessioned and processed. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[To place an order for a Gynecology (PAP Smear) lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list. If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location. Choose the Date/Time of the visit. Select OK. Select Gynecology (PAP Smear) in the Available Lab Tests list box. The Gynecology (PAP Smear) dialog displays. ![](cprs-user-manual-gui-version-updated-or-3-0-499/432.png)](#_Toc17877604)](#_Toc17877476)

> [[Gynecology (PAP Smear) dialog](#_Toc17877604)](#_Toc17877476)

7.  

[[Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the + key located above the Specimen Description field. Use the drop-down list for subsequent specimens. Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 
13. 
- [[If desired, change the default values for Urgency and/or Collection Date/Time fields. (These are required fields). If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person performing the procedure. Select the Surgeon/Physician. Choose a surgeon/physician. If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces. Select the Specimen Type. Choose a specimen type of either Slide or Thin Prep/Liquid Based. If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

14. 1.  
    2.  

> [[Select the Clinical History tab. Enter the patient's history in the Clinical History field. This is a required field. If desired, select Visit Type. Enter a visit type of Screening or Medically Indicated/Diagnostic. Select Menstrual Status. Choose the menstrual status (date of Last Menstrual Period, Postmenopausal, or Unknown). This is a required field. Note: If Postmenopausal is selected, you must select a Hormone Therapy as it will be required.](#_Toc17877604)](#_Toc17877476)

3.  

> [[If desired, select Hormone Therapy. Enter a hormone therapy (Hormone Replacement Therapy, No Hormone Therapy, or Vaginal Cream (Hormonal)).](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete any entry. Deleting an entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
  1.  

> [[If desired, select Applicable History. Enter the patient's applicable history (Abnormal Bleeding, Hormones/Birth Control, Hysterectomy, IUD, Not Menstruating, Post Partum, Pregnant, Prior Abnormal PAP Smear, or Radiation/Chemotherapy).](#_Toc17877604)](#_Toc17877476)

2.  
15. 
16. 
17. 

[[If desired, select Additional ClinicalHistory. Enter information for additional clinical history. This field allows letters, numbers, punctuation, and spaces. Select Accept Order. Preview the order. If desired, modify the order by selecting the Back button, or select the Accept Order button to accept the order.  
](#_Toc17877604)](#_Toc17877476)

18. 

> [[If desired, enter another lab test. -or- Select Accept Order.](#_Toc17877604)](#_Toc17877476)

> [[-or-](#_Toc17877604)](#_Toc17877476)

> [[Select Quit.](#_Toc17877604)](#_Toc17877476)

> [[Note: The Lab Test order must be signed before it is sent to VistA to be accessioned and processed. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[To place an order for a Renal Biopsy lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  

> [[Select the Orders tab. Select Anatomic Pathology from the Write Orders list. If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location. Choose the Date/Time of the visit. Select OK. Select Renal Biopsy in the Available Lab Tests list box. The Renal Biopsy dialog displays as shown below. ![](cprs-user-manual-gui-version-updated-or-3-0-499/433.png)](#_Toc17877604)](#_Toc17877476)

> [[Renal Biopsy dialog](#_Toc17877604)](#_Toc17877476)

7.  

[[Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the + key located above the Specimen Description field. Use the drop-down list for subsequent specimens. Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 

[[If desired, change the default values for Urgency and/or Collection Date/Time fields. (These are required fields). If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person performing the procedure. Select the Surgeon/Physician. Choose a surgeon/physician. If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces. Select the Specimen Type. Choose a specimen type (IR Core Biopsy, Open Wedge Biopsy, or Percutaneous Core Biopsy). Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
13. 

[[Select the Laterality. Choose a laterality of either Left or Right. Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
14. 
- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
15. 
- [[If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

16. 
1.  
2.  
3.  
4.  
17. 
18. 
19. 
20. 
21. 
22. 
23. 

[[To place an order for a Tissue Exam lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list. If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location. Choose the Date/Time of the visit. Select OK. Select Tissue Exam in the Available Lab Tests list box. The Tissue Exam dialog displays as shown below. Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the + key located above the Specimen Description field. Use the drop-down list for subsequent specimens. Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 

[[If desired, change the default values for Urgency and/or Collection Date/Time fields. (These are required fields). If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person performing the procedure. Select the Surgeon/Physician. Choose a surgeon/physician. If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces. Select the Procedure. Choose a procedure for the specimen (Biopsy, Cervical Biopsy, Cervix Resection, Cone Biopsy, Endocervical Curettage (ECC), Endometrial w/Pipelle Curettage, Excision, Fallopian Tube(s) Resection, LEEP, Myomas Resection, Nephrectomy, Ovary(s) Resection, Prostectomy, Resection, Uterus Resection, Vaginal Biopsy, or Vulvar Biopsy). Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
13. 
- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
14. 
15. 

[[If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion. Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

16. 
17. 
18. 
19. 
20. 
21. 
22. 
23. 

[[To place an order for a Urine lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list. If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location. Choose the Date/Time of the visit. Select OK. Select Urine in the Available Lab Tests list box. The Urine dialog displays. Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the + key located above the Specimen Description field. Use the drop-down list for subsequent specimens. Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 
13. 
- [[If desired, change the default values for Urgency and/or Collection Date/Time fields. (These are required fields). If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person performing the procedure. Select the Surgeon/Physician. Choose a surgeon/physician. If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces. Select the Specimen Type. Choose a specimen type (Bladder Wash, Catheterized Urine, Ileal Conduit, Left Ureter Wash, Right Ureter Wash, or Voided). If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

14. 
1.  
2.  
3.  
15. 
16. 
17. 
18. 
19. 

[[To place an order for a Urology, Bladder/Ureter lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list. Note: The orders listed in the Write Orders pane vary from site to site.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  
7.  

[[If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location. Choose the Date/Time of the visit. Select OK. Select Urology, Bladder/Ureter in the Available Lab Tests list box. The Urology, Bladder/Ureter dialog displays. Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the + key located above the Specimen Description field. Use the drop-down list for subsequent specimens. Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 

[[If desired, change the default values for Urgency and/or Collection Date/Time fields. These are required fields. If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person entering the order. Select the Surgeon/Physician. Choose a surgeon/physician. If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces. Select the Specimen Type. Choose a specimen type (Biopsy, CystectomyPartial CystectomyTotal, Excision, NephrectomyPartial, NephrectomyTotal, or TURBT). Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
13. 

[[Select the Laterality. Choose a laterality of either Left or Right. Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
14. 
15. 
- [[If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

16. 
17. 
18. 
19. 
20. 
21. 
22. 
23. 

[[To place an order for a Urology, Prostate lab test, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Select the Orders tab. Select Anatomic Pathology from the Write Orders list. Note: The orders listed in the Write Orders pane vary from site to site.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  

[[If the patient is an outpatient, select a Visit Location in the Location for Current Activities box and choose a visit location. Choose the Date/Time of the visit. Select OK. Select Urology, Prostate in the Available Lab Tests list box. Note: The dialog displayed will change based upon the specimen selected. The dialog shown below will display when either Left Testis or Right Testis is selected as a specimen.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/434.png)](#_Toc17877604)](#_Toc17877476)

> [[Urology, Prostate dialog](#_Toc17877604)](#_Toc17877476)

7.  

[[Select the Specimen Description on the left side of the dialog box. Choose a specimen description. If this is the first specimen, use the + key located above the Specimen Description field. Use the drop-down list for subsequent specimens. Note: At least one specimen along with a specimen description is required to process an order.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 
11. 
12. 
1.  

[[If desired, change the default values for Urgency and/or Collection Date/Time fields. These are required fields. If desired, enter your name in the Specimen Submitted By field. This is an optional field that is intended for the name of the person entering the order. Select the Surgeon/Physician. Choose a surgeon/physician. If desired, enter a comment in the Order comment field. This is an optional field that allows letters, numbers, punctuation, and spaces. Select the Specimen Type. Choose a specimen type (Left Testis, Prostate, Right Testis, or Vas Deferens). When Left Testis or Right Testis is selected as a specimen, select Specimen Type. Choose a specimen type of Orchiectomy. The Urology, Prostate dialog when either Left Testis or Right Testis is selected as a specimen will display as shown below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/435.png)](#_Toc17877604)](#_Toc17877476)

> [[Left Testis (or Right Testis) selected as a specimen](#_Toc17877604)](#_Toc17877476)

2.  

> [[When Prostate is selected as a specimen, select Specimen Type. Choose a specimen type (Prostate Needle Biopsy, Prostatectomy, Radical Prostatectomy, Simple Resection, Orchiectomy, TURP or Vasectomy). The Urology, Prostate dialog when Prostate is selected as a specimen will display as shown below. ![](cprs-user-manual-gui-version-updated-or-3-0-499/436.png)](#_Toc17877604)](#_Toc17877476)

> [[Prostate selected as a specimen](#_Toc17877604)](#_Toc17877476)

3.  

[[When Vas Deferens is selected as a specimen, select Specimen Type. Choose a specimen type of Vasectomy. The Urology, Prostate dialog when Vas Deferens is selected as a specimen will display as shown below. Note: The selection made in this field will appear in the Specimen Description field above.](#_Toc17877604)](#_Toc17877476)

- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/437.png)](#_Toc17877604)](#_Toc17877476)

> [[Vas Deferens selected as a specimen](#_Toc17877604)](#_Toc17877476)

13. 
- [[If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)
14. 
- [[If desired, enter a description for the specimen in the Specimen Description field. This is a required field with a maximum character length of 75 which includes letters, numbers, punctuation, and spaces. If desired, select the X button to delete the entry. Deleting the entry will result in a CPRS Patient Chart Warning dialog box; select the Yes button to confirm the deletion or select the No button to cancel the deletion.](#_Toc17877604)](#_Toc17877476)

[[Note: If you delete a specimen and there are multiple specimens, the specimen numbers will be reordered in the Specimen Description list.](#_Toc17877604)](#_Toc17877476)

15. 
1.  
16. 
17. 
18. 
19. 
20. 
21. 
22. 

[[The Reason for Study and the Clinical History fields are now two separate entries. Developers made this change to support a new system. The Reason for Study field is now required and has a limit of 64 characters (numbers, letters, space, and punctuation). The Clinical History field is optional and has no character limit.](#_Toc17877604)](#_Toc17877476)

[[To order any type of imaging, such as an x-ray or a nuclear medicine exam or procedure, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
74. [[Select the Orders tab. Select the active orders view from the View Orders pane -or- select View \| Active Orders (includes pending, recent activity).](#_Toc17877604)](#_Toc17877476)
75. [[Select Imaging in the Write Orders list box.](#_Toc17877604)](#_Toc17877476)

> [[Note: The imaging order may be labeled differently or may not be available from your Write Orders field.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[The Order an Imaging Procedure dialog displays as shown below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/438.png)](#_Toc17877604)](#_Toc17877476)

> [[Order an Imaging Procedure dialog](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog will appear before the Order an Imaging Procedure dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

76. [[Select the desired imaging type in the Imaging Type field.](#_Toc17877604)](#_Toc17877476)
77. [[Select a procedure from the Imaging Procedure list box.](#_Toc17877604)](#_Toc17877476)
78. [[Select an available modifier from the Available Modifiers field.](#_Toc17877604)](#_Toc17877476)

> [[The modifier(s) you select will be displayed in the Selected Modifiers field.](#_Toc17877604)](#_Toc17877476)

> [[Note: You can remove a modifier by selecting the modifier and clicking Remove.](#_Toc17877604)](#_Toc17877476)

79. [[Enter a reason for the exam in the Reason for Study field. (This is a required field that allows a maximum of 64 characters—which includes letters, numbers, punctuation, and spaces.)](#_Toc17877604)](#_Toc17877476)
80. [[(Optional) If wanted, enter the history in the Clinical History field (If you enter anything, it must be at least two consecutive alphanumeric characters).](#_Toc17877604)](#_Toc17877476)
81. [[If necessary, change the Requested Date, Urgency, Transport, and Category fields.](#_Toc17877604)](#_Toc17877476)

> [[Note: The Date Desired previously defaulted to TODAY, but this default has been removed from most orders. The user will need to enter the Date Desired.](#_Toc17877604)](#_Toc17877476)

82. [[Complete the Submit To field (if necessary).](#_Toc17877604)](#_Toc17877476)
83. [[Check the Isolation checkbox (if necessary).](#_Toc17877604)](#_Toc17877476)
84. [[Select the appropriate response (Yes, No, or Unknown) in the Pregnant field.](#_Toc17877604)](#_Toc17877476)
85. [[Select the time that the PreOp is scheduled by doing one of the following:](#_Toc17877604)](#_Toc17877476)
- 
- 

> [[entering a date (e.g. 6/21/01 or June 21, 2001)entering a date formula (e.g. t-200) o pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/439.png) button to bring up a calendar](#_Toc17877604)](#_Toc17877476)

86. [[Select Accept Order.](#_Toc17877604)](#_Toc17877476)
87. [[Enter another order -or- click Quit.](#_Toc17877604)](#_Toc17877476)
- 
- 
1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
9.  
10. 
11. 

[[On the CPRS Orders tab under the Write Orders pane, select Return to Clinic. In the Return to Clinic dialog, if you have saved a Quick Order that you would like to use, select the down arrow and then select the quick order. If not, proceed to step 3. Select the Clinic field's drop-down box's arrow and then the appropriate clinic name. (This is a required field.) In the Date field, select the date. (This is a required field.) If the appointment is time-sensitive, select the Time Sensitive check box. Selecting the Time Sensitive check box will change the order text in the Order Sig from "on or around" to "no later than."If you want more than one appointment, place the cursor in the Number of Appointments field, enter the number of appointments. In the Interval in day(s) field, enter the number of days between appointments. If the field is active, you can select the Prerequisites field, you can select one or more prerequisites, such as lab work or imaging, that should precede the appointments. In the Comments field, type in any comments that should go with the orders. In the More Information field, additional information displays for the user to see. Review the Order Sig to ensure that it is as you need it. Note: If the order is one that the user will reuse frequently, the user can save it as a personal quick order. To save this as a quick order, go to the menu bar and select Options \| Save as Personal Quick Order.](#_Toc17877604)](#_Toc17877476)

[[Then, the order will display in the Quick order field the next time the dialog is opened.](#_Toc17877604)](#_Toc17877476)

12. 
- 
- 
- 
- 

[[To order a consult from the Orders tab follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane -or-](#_Toc17877604)](#_Toc17877476)

> [[select View \| Active Orders (includes pending, recent activity).](#_Toc17877604)](#_Toc17877476)

3.  

> [[Select Consult in the Write Orders list. Note: The consults order may be labeled differently or may not be available from your Write Orders field.](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog will appear before the Order a Consult dialog. You must complete the encounter information dialog before proceeding.  
> ](#_Toc17877604)](#_Toc17877476)

> [[The Order a Consult dialog displays as shown below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/443.png)](#_Toc17877604)](#_Toc17877476)

> [[The Order a Consult dialog](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select a type of consult from the Consult to Service/Specialty field. When you select the Consult Service or Specialty, several things may happen:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
5.  
6.  

> [[If the service has some prerequisites, a dialog will display stating what those are and will allow you to print the information, continue to place the consult order, or cancel the order. In addition, any predefined text or template will display to help the user fill out the Reason for Request field. The Provisional Diagnosis field becomes active as well. Select the urgency from the Urgency field. Select an individual from the Attention field. Note: To help you distinguish between providers, CPRS displays their titles (if available). When two or more providers have identical names, CPRS also displays:](#_Toc17877604)](#_Toc17877476)

> [[o The service/section and site division (if any) associated with these providers; site divisions are displayed based on the following rules:](#_Toc17877604)](#_Toc17877476)

- 
- 
- - 

> [[When no division is listed for a provider, no division is displayed. If only one division is listed, this division is displayed. If the site has multiple divisions or more than one division is listed and one of these listed divisions is marked as Default, CPRS displays the division marked as Default. If more than one division is listed for a provider and none is marked as Default, CPRS does not display division information for this provider. o Providers who are listed in the New Person file as Visitors are screened out from the provider list. (These screened-out providers are listed as Visitors because their entries were created as a result of a Remote Data View.)](#_Toc17877604)](#_Toc17877476)

7.  

> [[If needed, designate a different Clinically Indicated Date. Note: The Clinically Indicated Date field does not apply to Prosthetics consults services, and the field is not available when the user selects a Prosthetic service.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 

> [[Choose inpatient or outpatient from the "Patient will be seen as an:" option group. Choose a location from the Place of Consultation drop-down box. Enter a provisional diagnosis. Note: If a user tries to enter a diagnosis with an inactive code, CPRS will bring up a message indicating that the code must be changed and giving the user the chance to choose a diagnosis with an active code.](#_Toc17877604)](#_Toc17877476)

> [[For each consult, this field is either set up to require that](#_Toc17877604)](#_Toc17877476)

- [[The user type in an answer (the box will be white and the](#_Toc17877604)](#_Toc17877476)
- [[Lexicon button unavailable), or](#_Toc17877604)](#_Toc17877476)
- [[The user must select a response must be from the Lexicon (the field will be yellow and the Lexicon button is available).](#_Toc17877604)](#_Toc17877476)

> [[CPRS will search for diagnoses that contain the search term. The matching terms will display in the bottom portion of the Problem List Lexicon Search dialog. The search now looks for SNOMED Concepts Terms (SNOMED CT) items. Most items will also be mapped to an ICD-9-CM code. The list will show the SNOMED concept text, the SNOMED code, and the ICD-9-CM code if the term is mapped to one.](#_Toc17877604)](#_Toc17877476)

> [[If you do not see the appropriate problem listed, select the Extend Search button. The Extend Search button extends the search to the ICD-9-CM clinical hierarchy to find additional terms.](#_Toc17877604)](#_Toc17877476)

11. 

> [[Enter a reason for the request in the Reason for Request field. Sites can help users by putting in predetermined boilerplate text, text with TIU objects, and/or it could be linked to a template that users can fill out. Users can then add to the text already present. Or the field may be left blank for the user to fill in the reason. However, a reason for request is required and the consult cannot be saved without a reason for request.](#_Toc17877604)](#_Toc17877476)

12. 
13. 

> [[Select Accept Order. Enter another Consult -or-](#_Toc17877604)](#_Toc17877476)

> [[select Quit.](#_Toc17877604)](#_Toc17877476)

> [[Note: You may sign the consult now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[To order a procedure, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[Locate and select the procedure in the Procedure list. When you select the Consult Service or Specialty, several things may happen:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
4.  
5.  

[[If the service has some prerequisites, a dialog will display stating what those are and will allow you to print the information, continue to place the consult order, or cancel the order. In addition, any predefined text or template will display to help the user fill out the Reason for Request field. The Provisional Diagnosis field becomes active as well. Select the urgency from the Urgency field. Select an individual from the Attention field. Note: To help you distinguish between providers, CPRS displays their titles (if available). When two or more providers have identical names, CPRS also displays:](#_Toc17877604)](#_Toc17877476)

- - 
  - 
  - 
  - 
- 
6.  

[[The service/section and site division (if any) associated with these providers; site divisions are displayed based on the following rules: When no division is listed for a provider, no division is displayed. If only one division is listed, this division is displayed. If the site has multiple divisions or more than one division is listed and one of these listed divisions is marked as Default, CPRS displays the division marked as Default. If more than one division is listed for a provider and none is marked as Default, CPRS does not display division information for this provider. Providers who are listed in the New Person file as Visitors are screened out from the provider list. (These screened-out providers are listed as Visitors because their entries were created as a result of a Remote Data View.) If needed, designate a different Clinically Indicated Date. Note: The Clinically Indicated Date field does not apply to Prosthetics consults services, and the field is not available when the user selects a Prosthetic service.](#_Toc17877604)](#_Toc17877476)

7.  

> [[If necessary, select a service that will perform the procedure by using the down arrow to open the list and then selecting the service. Often, the service is already defined. However, sometimes, the user has the chance to choose.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 

> [[Select whether the patient is an inpatient or outpatient. Select a place of consultation from the Place of Consultation drop-down list. Enter a provisional diagnosis in the Provisional Diagnosis field. For each procedure, this field is either set up to require that](#_Toc17877604)](#_Toc17877476)

- [[the user type in an answer (the box will be white and the Lexicon button unavailable), or](#_Toc17877604)](#_Toc17877476)
- [[the user must select a response must be from the Lexicon (the field will be yellow and the Lexicon button is available).](#_Toc17877604)](#_Toc17877476)
- [[CPRS will search for diagnoses that contain the search term. The matching terms will display in the bottom portion of the Problem List Lexicon Search dialog. The search now looks for SNOMED Concepts Terms (SNOMED CT) items. Most items will also be mapped to an ICD-9-CM code. The list will show the SNOMED concept text, the SNOMED code, and the ICD-9-CM code if the term is mapped to one.](#_Toc17877604)](#_Toc17877476)
- [[If you do not see the appropriate problem listed, select the Extend Search button. The Extend Search button extends the search to the ICD-9-CM clinical hierarchy to find additional terms.](#_Toc17877604)](#_Toc17877476)

[[Note: If a user tries to enter a diagnosis with an inactive code, CPRS will bring up a message indicating that the code must be changed and giving the user the chance to choose a diagnosis with an active code.](#_Toc17877604)](#_Toc17877476)

11. 

> [[Enter a reason for this request in the Reason for request field. Sites can help users by putting in predetermined boilerplate text, text with TIU objects, and/or it could be linked to a template that users can fill out. Users can then add to the text already present. Or the field may be left blank for the user to fill in the reason. However, a reason for request is required and the consult cannot be saved without a reason for request.](#_Toc17877604)](#_Toc17877476)

12. 
13. 

[[Select Accept Order. Enter another order -or- select Quit. Note: The order must be signed before it is sent. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[This section gives steps to place an order directing staff to collect vitals with a certain frequency over a time period. To record vitals and measurements, staff should use the new Vitals package or the Vitals Lite interface in CPRS.](#_Toc17877604)](#_Toc17877476)

[[To enter a vitals order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane -or-](#_Toc17877604)](#_Toc17877476)

> [[select View \| Active Orders (includes pending, recent activity).](#_Toc17877604)](#_Toc17877476)

3.  

> [[Select Vitals in the Write Orders list box. The VITAL SIGNS dialog appears.](#_Toc17877604)](#_Toc17877476)

> [[Note: The vitals order may be labeled differently or may not be available from your Write Orders list.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/445.png)](#_Toc17877604)](#_Toc17877476)

> [[The VITAL SIGNS dialog box](#_Toc17877604)](#_Toc17877476)

> [[Note: If encounter information has not been entered, the encounter information dialog will appear before the VITAL SIGNS dialog. You must complete the encounter information dialog before proceeding.](#_Toc17877604)](#_Toc17877476)

4.  
5.  
- 
- 
- 
6.  
7.  
- 
- 
- 
8.  
9.  

[[Text only orders such as Parameters, Activity, Patient Care, and Free Text orders are different kinds of orders that are placed for nursing and ward staff to take action on. They print only at the patient's ward/location, and are not transmitted electronically to other services.](#_Toc17877604)](#_Toc17877476)

[[Examples of text only orders include:](#_Toc17877604)](#_Toc17877476)

| [[Order Type](#_Toc17877604)](#_Toc17877476) | [[Order](#_Toc17877604)](#_Toc17877476)                                 |
|--------------------------------------------------|-----------------------------------------------------------------------------|
| [[Parameters](#_Toc17877604)](#_Toc17877476)     | [[Vital signs](#_Toc17877604)](#_Toc17877476)                               |
| [[Activity](#_Toc17877604)](#_Toc17877476)       | [[Bed rest, ambulate, up in chair](#_Toc17877604)](#_Toc17877476)           |
| [[Patient Care](#_Toc17877604)](#_Toc17877476)   | [[Skin and wound care, drains, hemodynamics](#_Toc17877604)](#_Toc17877476) |
| [[Free text](#_Toc17877604)](#_Toc17877476)      | [[Immunizations](#_Toc17877604)](#_Toc17877476)                             |

[[Predefined nursing orders (quick orders) may be available under various submenus.](#_Toc17877604)](#_Toc17877476)

[[To place a text only order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Orders tab. Select the active orders view from the View Orders pane. Select Text Only Order in the Write Orders list box. The Word Processing Order dialog displays.](#_Toc17877604)](#_Toc17877476)

> [[Note: The text only order may be labeled differently or may not be available from your Write Orders list.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/448.png)](#_Toc17877604)](#_Toc17877476)

> [[The Text Only Order dialog](#_Toc17877604)](#_Toc17877476)

4.  
5.  - 
    - 
    - 

[[Enter the text for the order in the Order field. Enter a start date and time by doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001). entering a date formula (e.g. t-200). pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/449.png) button to bring up a calendar.  
](#_Toc17877604)](#_Toc17877476)

6.  - 
    - 
    - 
7.  
8.  

> [[Enter a stop date and time by doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001). entering a date formula (e.g. t-200). pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/450.png) button to bring up a calendar. Select Accept Order. Enter another order -or-](#_Toc17877604)](#_Toc17877476)

> [[select Quit.](#_Toc17877604)](#_Toc17877476)

[[An event-delayed order is an order that is executed only after a predefined event (known as a release event) occurs. A release event can be an event such as an admission, discharge, or transfer. For example, you can write an event-delayed diet order that will not execute until a patient is transferred to a specific ward.](#_Toc17877604)](#_Toc17877476)

[[A CAC defines the release events at your site. (For more information on defining release events, see Appendix F of the *CPRS List Manager Technical Manual* or the Event-Delayed Orders topic in the *CPRS GUI Technical Manual*). Once a CAC has defined a release event, you can write an order that will not execute until that release event occurs.](#_Toc17877604)](#_Toc17877476)

[[To write an event-delayed order, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Orders tab. Select the Write Delayed Orders button located below the View Orders pane.The *Release Orders* dialog box appears. The available release events will appear in a list. Your list may contain a highlighted default release event and a common release event list. Your CAC defines the default release event and the common release event list. (For more information about defining a default release event and a common release event list, please see the Event-Delayed Orders topic in the *CPRS GUI Technical Manual* or Appendix F in the *CPRS List Manager Technical Manual*).](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/451.png)](#_Toc17877604)](#_Toc17877476)

> [[Your CAC can define a default release event and a common release event list](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[Select Delay Release of New Order(s) until. Select the appropriate release event. Note: If the patient's location has a treating specialty of "observation" and the user tried to write delayed orders, the "transfer" event should not appear in the selection list. The reason is that orders are discontinued on transfer. The result would be if a patient were in an observation location, and delayed orders were written when the patient was moved out of observation, the orders would be cancelled.  
> ](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select OK. If the *Copy active orders for selected event* dialog box appears, continue to step 5. Otherwise, the *Release Orders* dialog will close and the name of the release event will now appear below the Write Delayed Orders button. Enter the order as you normally would.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/452.png)](#_Toc17877604)](#_Toc17877476)

> [[The Copy active orders for selected event dialog box](#_Toc17877604)](#_Toc17877476)

6.  
7.  

> [[Select the active orders that you would like to delay in the Copy active orders for selected release event dialog box. These orders will be delayed until the release event specified at the top of the dialog occurs. You can press and hold Shift to select a range of orders or you can press and hold ctrl to select multiple individual orders. Select OK. The *Ordering Information* dialog box appears. This dialog contains the release event that you have selected. Make sure that you selected the correct release event.](#_Toc17877604)](#_Toc17877476)

8.  
9.  

> [[Select OK.Enter the order as you normally would. Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/453.png)](#_Toc17877604)](#_Toc17877476)

> [[The name of the release event appears below the Write Delayed Orders button and above the list of orders](#_Toc17877604)](#_Toc17877476)

[[If an order is not signed, you can change the order's current release event or assign a release event to a regular order. However, once an order has been signed, you cannot make further changes.](#_Toc17877604)](#_Toc17877476)

[[To assign or change a release event, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Orders tab. Select the type of order you would like to change from the View Orders pane. The orders for the type you select will be displayed in the details pane on the right side of the screen.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[Highlight the order you would like to change from the details pane. Select Action \| Change Release Event -or-](#_Toc17877604)](#_Toc17877476)

> [[right-click on the order and select Change Release Event from the right click menu.](#_Toc17877604)](#_Toc17877476)

> [[The *Change Release Event* dialog box displays. The current release event will be highlighted.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/454.png)](#_Toc17877604)](#_Toc17877476)

> [[The current release event is highlighted in the *Change Release Event* dialog](#_Toc17877604)](#_Toc17877476)

> [[Note: If the release event cannot be changed, the *Unable to be Released to Service* dialog box appears. The reason that the release event cannot be changed is listed at the bottom of the dialog box. Press OK to close the dialog box.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/455.png)](#_Toc17877604)](#_Toc17877476)

> [[This dialog box will appear if an order's release event cannot be changed](#_Toc17877604)](#_Toc17877476)

5.  

> [[To change the release event, select another event and click Change. To simply remove the existing event, click Remove. A confirmation dialog appears.](#_Toc17877604)](#_Toc17877476)

6.  

[[Click OK to confirm your changes.](#_Toc17877604)](#_Toc17877476)

[[Note: Each site can set a parameter that determines if the user must hold a key or if a parameter setting will determine which users can release delayed orders.](#_Toc17877604)](#_Toc17877476)

[[To release an event-delayed order manually (before the release event occurs), follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

> [[Select the Orders tab. Select the type of order you would like to release from the View Orders pane. The corresponding orders will appear on the right side of the screen. Highlight the order you would like to release from the details pane on the right side of the screen. Select Action \| Release Delayed Orders -or-](#_Toc17877604)](#_Toc17877476)

> [[right-click on the order and select Release Delayed Orders.](#_Toc17877604)](#_Toc17877476)

> [[Note: You must sign an order before it can be released.](#_Toc17877604)](#_Toc17877476)

> [[The Release to Service dialog box will appear.](#_Toc17877604)](#_Toc17877476)

6.  
7.  

[[To view an event-delayed order after it has been released, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Orders tab. Select View \| Auto-DC/Release Event Orders The Auto-DC/Release Event Orders dialog appears.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[Choose the event the order is associated with. Select OK. The appropriate orders will appear on the Orders tab.](#_Toc17877604)](#_Toc17877476)

[[To notify a user when the results of an order are available, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[Select the Orders tab. Select the desired type of order in the View Orders list box. Select an order from the list of orders on the right-hand side of the screen. Select Action \| Alert when Results.... The Alert when Results dialog displays.](#_Toc17877604)](#_Toc17877476)

5.  

> [[Choose an alert recipient from the Alert Recipient drop-down field. Note: A recipient must have the ORDERER-FLAGGED RESULTS notification/alert enabled in order to receive the alert.](#_Toc17877604)](#_Toc17877476)

6.  

[[Select OK.  
](#_Toc17877604)](#_Toc17877476)

[[With CPRS, users can <span id="flagging_an_order" class="anchor"></span>flag an order to draw attention to it. When an order is flagged, the word "Flagged" will appear in the Orders column and the Service or Event column for the flagged order displays red. Below some points about flags are further explained.](#_Toc17877604)](#_Toc17877476)

- [[Multiple recipients: CPRS enables users to send the flag to multiple individuals. The user flagging the order can choose from a list of possible recipients and those recipients will receive an alert that the order has been flagged.](#_Toc17877604)](#_Toc17877476)

[[Note: A recipient must have the FLAG ORDER FOR CLARIFICATION notification/alert enabled to receive the alert.](#_Toc17877604)](#_Toc17877476)

- [[No Action Alert: The user flagging the order can also check the No Action Alert checkbox to receive an alert if none of the recipients acts on the flag before the specified time. When the user checks the No Action Alert checkbox, the time in the field is the default time that is controlled by a parameter. Your site can set a default time or leave it empty. If the sites do not enter a default time, the default time is 24 hours. However, the site can set the default time to a different amount of time, such as 8 hours, or 4 hours, or whatever your site chooses. But, when the user checks the No Action Alert, the user can change the time.](#_Toc17877604)](#_Toc17877476)
- [[Flag Information in Order Details: CPRS records the name of the person who flagged the order and the date and time that it was flagged. CPRS also tracks comments on the flag and who unflags an order with the date and time.](#_Toc17877604)](#_Toc17877476)
- [[Reason for Flag when Processing: When the user processes the order, CPRS displays the reason for the flag in the order text on the Orders tab.](#_Toc17877604)](#_Toc17877476)

[[To flag an order, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[Select the Orders tab. Select the desired type of orders in the View Orders list box. Select the individual order that you would like to flag from the list of orders on the right side of the screen.  
](#_Toc17877604)](#_Toc17877476)

4.  

> [[Select Action \| Flag.... The Flag Order dialog displays.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/456.png)](#_Toc17877604)](#_Toc17877476)

> [[The Flag Order dialog with the red rectangle added showing that multiple providers can be added as recipients.](#_Toc17877604)](#_Toc17877476)

5.  
6.  

> [[Enter a reason for the flag in the Reason for Flag field. Users can choose a reason from the drop-down list, choose a reason and add additional text, or enter their own text. The Reason for flag field has a 240-character limit. Choose alert recipients from the Alert Recipient drop-down field. To locate names, type part of the name and the list will scroll and you can select the right name and move the name to the recipient pane on the right. Repeat the process until you have all the names you want in the recipient pane on the right. Note: A recipient must have the FLAG ORDER FOR CLARIFICATION notification/alert enabled to receive the alert.](#_Toc17877604)](#_Toc17877476)

7.  
8.  
9.  

> [[If you want to receive an alert if no one acts on the flag, check the Create a No Action Alert check box. Enter the time after which you want to receive the alert. You can accept the default and move to the next step. Or you can set the time you want by selecting the button with three dots to bring up the Calendar component and select a date and time, then move to the next step. Select OK. Note: If the OR FLAGGED & WARD COMMENTS parameter is turned On, flagged Order comments and Ward comments will display directly in the Order column. This parameter is turned Off by default; a CAC must activate it for your site. Refer to the *CPRS Technical Manual: GUI Version* for details on how to activate this parameter.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/457.png)](#_Toc17877604)](#_Toc17877476)

> [[CPRS Orders tab with a flagged order comment displayed in the Order column](#_Toc17877604)](#_Toc17877476)

[[CPRS has enabled sites to restrict which users can unflag an order.](#_Toc17877604)](#_Toc17877476)

[[For a user to unflag an order, the user must meet one of the requirements:](#_Toc17877604)](#_Toc17877476)

- [[the user is assigned the ORES key](#_Toc17877604)](#_Toc17877476)
- [[the user is assigned another security key that the site designates (the sit can determine which keys can unflag orders)](#_Toc17877604)](#_Toc17877476)
- [[the user who flagged the order](#_Toc17877604)](#_Toc17877476)
- [[the user is a flag order recipient](#_Toc17877604)](#_Toc17877476)
1.  
2.  
3.  
4.  
5.  

[[Select the Orders tab.  Select the order you want to unflag. Select Action \| Unflag.  Enter a reason (must be at least 4 characters).  Select OK.   ](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[There are several other changes that are explained in the POE Release Notes.  
](#_Toc17877604)](#_Toc17877476)

[[From the Notes tab you can create new progress notes for a patient and view existing progress notes and documents. You can also create templates to allow you to quickly and efficiently enter progress notes. Documents on the Notes tab are organized in a tree structure on the left side of the screen.](#_Toc17877604)](#_Toc17877476)

[[To view the text of a progress note, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Notes tab. Select a document title from the left side of the screen. (Click the "+" sign to expand a heading.) Note: If a note has an addendum, the ![](cprs-user-manual-gui-version-updated-or-3-0-499/459.png) icon will appear in front of the note title. You may view the addendum by clicking the "+" sign to expand the note title and then selecting the appropriate addendum.](#_Toc17877604)](#_Toc17877476)

> [[The text of the progress note will be displayed on the right side of the screen as shown below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/460.png)](#_Toc17877604)](#_Toc17877476)

> [[The list of notes for the selected patient is displayed in the tree view on the left of the dialog. Above the tree view, CPRS displays the sorting of the list (last 100 signed notes in this case). Next to the label of the sorting, CPRS displays the total number of notes the patient has. The text of a document is displayed on the right side of the Notes tab](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

3.  

> [[(Optional) To view additional details of the progress note, such as editing history, patient record flag links, associated problems, select View \| Details.Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/461.png)](#_Toc17877604)](#_Toc17877476)

> [[This screen shows an example of a progress note's detailed display](#_Toc17877604)](#_Toc17877476)

[[To view all the progress notes under a specific heading, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Notes tab. Double-click the heading that you would like to view. The notes that are related to that heading will appear in a table on the right side of the screen.](#_Toc17877604)](#_Toc17877476)

3.  

[[To view a specific note, select the note from the table. You can also sort the table by clicking on the column you wish to sort by (click the column again to sort the table in inverse order).Note: If a provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/462.png)](#_Toc17877604)](#_Toc17877476)

> [[CPRS Notes Dialog viewing notes under a specific heading](#_Toc17877604)](#_Toc17877476)

[[CPRS allows you to control which documents appear on the Notes tab. From the View menu you can specify that only the following note types appear on the tab:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[All signed notes Signed notes by a particular author Signed notes for a particular date range Uncosigned notes Unsigned notes In addition, you can use the View \| Custom View option to further customize the Notes tab.  
](#_Toc17877604)](#_Toc17877476)

[[To view all signed notes, all unsigned notes, or all uncosigned notes, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Notes tab. Select View \| Signed Notes (All), View \| Uncosigned Notes, or View \| Unsigned Notes. The appropriate progress notes will appear on the Notes tab.](#_Toc17877604)](#_Toc17877476)

[[If you would like to further limit the notes that are displayed on the Notes tab, continue with the "Additional Customization" topic (below).](#_Toc17877604)](#_Toc17877476)

[[To view all signed notes by a specific author, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Notes tab. Select View \| Signed Notes by Author. The List Signed Notes by Author dialog displays.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will display on the screen below. See the "National Provider Identifier (NPI) Display in CPRS" section for an example of an NPI displaying on a screen.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/463.png)](#_Toc17877604)](#_Toc17877476)

> [[The List Signed Notes by Author dialog](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  

> [[Select the author of the note(s) that you would like to view. In the Sort Order option group, select Ascending (oldest first) to view the oldest notes first, or Descending (newest first) to view the newest notes first. Select OK. The appropriate notes will appear on the Notes tab.](#_Toc17877604)](#_Toc17877476)

[[If you would like to further limit the notes that are displayed on the notes tab, continue with the "Additional Customization" topic (below).  
](#_Toc17877604)](#_Toc17877476)

[[To view all signed notes by a specific author, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Notes tab. Select View \| Signed Notes by Date Range. The List Signed Notes by Date Range dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/464.png)](#_Toc17877604)](#_Toc17877476)

> [[The List Signed Notes by Date Range dialog](#_Toc17877604)](#_Toc17877476)

3.  - 
    - 
    - 
4.  - 
    - 
    - 
5.  

> [[Enter a beginning date by doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001). entering a date formula (e.g. t-200). pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/465.png) button to bring up a calendar. Enter an ending date by doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001). entering a date formula (e.g. t-200). pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/466.png) button to bring up a calendar. Select OK. The appropriate notes will be displayed on the Notes tab.  
> ](#_Toc17877604)](#_Toc17877476)

[[If you would like to further limit the notes that are displayed on the Notes tab, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[From the Notes tab, select View \| Custom View. The List Selected Documents dialog will appear.](#_Toc17877604)](#_Toc17877476)

> [[Note: If a provider has an NPI, it will display on the screen below. See the "National Provider Identifier (NPI) Display in CPRS" section for an example of an NPI displaying on a screen.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/467.png)](#_Toc17877604)](#_Toc17877476)

> [[The List Selected Documents dialog](#_Toc17877604)](#_Toc17877476)

2.  

> [[Select the criteria for the documents that you want to display on the Notes tab by doing some or all of the following: Note: You cannot set all of the fields at the same time. For example, if you choose one of the options for "all notes," then you are given the option of a date range because that conflicts with the other choice.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[Select a status from the left side of the window. Enter the maximum number of notes that you would like to display in the Max Number to Return field. Select an author or expected cosigner from the Author or Expected Cosigner field.  
](#_Toc17877604)](#_Toc17877476)

4.  - 
    - 
    - 
5.  
6.  
7.  
8.  
9.  

> [[Select a beginning and ending date by doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001) entering a date formula (e.g. t-200) pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/468.png) button to bring up a calendarSelect a sort order from the Note Tree View option group. If you would like to group the notes, make a selection from the Group By drop-down list. If you would like to further sort the notes that have been grouped in step f, select the criteria to sort by in the Sort By drop-down list. If you would like the subject of the notes to be displayed in the tree view, check the "Show subject in list" check box. If you would like to limit the notes that are displayed to notes that contain specific text in the title or in the subject line, click the appropriate check box and enter the text in the Contains field.Note: You can erase the contents of the List Selected Documents dialog by clicking the Clear Sort/Group/Search button.](#_Toc17877604)](#_Toc17877476)

3.  

> [[Click OK. The notes that meet the criteria you specified will appear on the Notes tab.](#_Toc17877604)](#_Toc17877476)

[[CPRS enables users to set a maximum number of notes that should display when the Notes tab loads. The purpose of defining a maximum number of notes is to avoid loading a large amount of information that might slow performance. When there is a value in the Max Number to Return field (2b above), CPRS has some additional features on the tree view: a "Show More" item and another display category called "Older signed notes with recent addenda".](#_Toc17877604)](#_Toc17877476)

1)  
2)  

[[Show More: If the user has more notes available than the maximum allowed, a "Show More" entry displays in the tree view. If the user double clicks "Show More", CPRS downloads another set of notes as the initial maximum. If there are still more notes available, "Show More" appears again until there are no more notes to display.For example, if the selected patient has 300 total notes and the Maximum Number of Notes is set to 30, when the Notes tab initially opens, 30 Notes will be downloaded, and their information displayed in the tree view. A Show More item will display at the end of the tree view because there are more notes. If the user selects Show More, another 30 notes will be downloaded and listed. If the user selects Show More again, another 30 notes and the Show More item will display. This will continue until all the notes have been listed. ![](cprs-user-manual-gui-version-updated-or-3-0-499/469.png)Older signed notes with recent addenda: Sometimes one or more notes outside the maximum range will have an addendum inside the range. These notes are added to the bottom of the list, under the date of the parent note. In this example, the last two notes have recent addenda but are well outside the range of the rest of the notes. This makes it appear that there are no notes between the last normal note (dated April 2019) and the older parent note with the recent addendum (dated March 2009).![](cprs-user-manual-gui-version-updated-or-3-0-499/470.png)To prevent the appearance of a gap in notes, these older notes are now separated from the rest of the notes after the "Show More" entry, marked with the label "Older signed notes with recent addenda".![](cprs-user-manual-gui-version-updated-or-3-0-499/471.png)As shown above, both Show More and Older signed notes with recent addenda can be in the tree view.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[On the notes tab, select View \| Search for Text (Within Current View). In the List Signed Notes by Author dialog, enter the text for which CPRS should search. Press OK. CPRS will then search the current view of notes and filter the tree view so that only those notes with the exact text are displayed.](#_Toc17877604)](#_Toc17877476)

[[To set a default view for the Notes tab, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Customize the Notes tab by following the steps above. Select View \| Save as Default View. A warning dialog will appear.](#_Toc17877604)](#_Toc17877476)

3.  

[[Select OK. The current view will be set as the default view for the Notes tab.](#_Toc17877604)](#_Toc17877476)

[[To create a new progress note, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Notes tab. Select the New Note button. The Progress Note Properties dialog displays.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
- 
- 
- 
5.  

[[Select a title for the progress note from the Progress Note Title drop-down list. If necessary, select a date and time for the progress note by doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001) entering a date formula (e.g. t-200) pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/473.png) button to bring up a calendar If necessary, select an author for the progress note. Note: To help you distinguish between providers, CPRS displays their titles (if available). When two or more providers have identical names, CPRS also displays:](#_Toc17877604)](#_Toc17877476)

- - 
  - 
  - 
  - 
- 

> [[The service/section and site division (if any) associated with these providers; site divisions are displayed based on the following rules: When no division is listed for a provider, no division is displayed. If only one division is listed, this division is displayed. If the site has multiple divisions or more than one division is listed and one of these listed divisions is marked as Default, CPRS displays the division marked as Default. If more than one division is listed for a provider and none is marked as Default, CPRS does not display division information for this provider. Providers who are listed in the New Person file as Visitors are screened out from the provider list. (These screened-out providers are listed as Visitors because their entries were created as a result of a Remote Data View.) Note: Occasionally a problem occurs if a cosigner's access lapses and they have become "disusered". If this occurs, you can click OK and proceed with that selection or click Cancel and choose another cosigner.](#_Toc17877604)](#_Toc17877476)

6.  

> [[If the note is to resolve a consult or to document a patient record flag, select the consult number or the patient record flag action to which the note should be linked. To help users select the correct consult when a title that will resolve a consult is selected and a consult is available to resolve, a Show Details button that brings up the details of the consult is available. Note: If the user attempts to change the characteristics of a PRF note and has highlighted an action that reads Yes under note, CPRS assumes that the user is trying to link to an already linked action and will not allow the change to continue. However, if the user removes the highlight from the Yes action, the changes can occur.](#_Toc17877604)](#_Toc17877476)

7.  
8.  
- 
- 
- 
1.  
2.  
3.  
4.  

> [[Select OK. In the main text box, enter the content of the note using one or more of the methods below:Copy and paste from other documentsType in text Insert predefined text from templates. Select the Templates drawer. Locate the template you need. Double-click the template, drag-and-drop the template into the document, or right-click and select Insert Template. (It will be placed where the cursor is.) Repeat steps b and c as needed. Note: If you need to view the consult details while writing a note, bring up the popup menu by right-clicking in the note editing pane and choosing View Consult Details or using the shortcut Shift+Ctrl+U.](#_Toc17877604)](#_Toc17877476)

9.  

[[After you enter the note, if you select Encounter, you can enter encounter information for the visit. Diagnosis, procedure, and Visit Type are required. The check boxes are based on the Encounter Form defined for the Progress Note Title you select. When you click on Other Diagnoses or Other Procedures, a Lexicon look up (terms with their corresponding ICD or CPT codes) is displayed for you to choose from.](#_Toc17877604)](#_Toc17877476)

> [[Note: When finished, you can continue working or select an item from the Action menu, such as Sign Note Now..., Save Without Signature, or Add to Signature List.](#_Toc17877604)](#_Toc17877476)

[[To change a progress note title, use these steps:](#_Toc17877604)](#_Toc17877476)

> [[Note: Progress Notes can only be edited if they have not been signed. Signed notes cannot be editing. To add to a note, an addendum would have to be created.](#_Toc17877604)](#_Toc17877476)

1.  

> [[When in a note that you have already started, select the Change… button. The Progress Note Properties dialog displays in which the user should select the note title, author, and date.](#_Toc17877604)](#_Toc17877476)

2.  

> [[Select the appropriate note title, author, and/or date. The Clear Previous Boilerplate Text dialog displays as shown below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/474.png)](#_Toc17877604)](#_Toc17877476)

3.  

[[To keep the text in the note, select No. To remove the text, select Yes. To edit a progress note, follow these steps:](#_Toc17877604)](#_Toc17877476)

> [[Note: Progress Notes can only be edited if they have not been signed. Signed notes cannot be editing. To add to a note, an addendum would have to be created.](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Notes tab. Select a document title from the left side of the screen. (Click the "+" sign to expand a heading.) Note: If a note has an addendum, the ![](cprs-user-manual-gui-version-updated-or-3-0-499/475.png) icon will appear in front of the note title. You may view the addendum by clicking the "+" sign to expand the note title and then selecting the appropriate addendum.](#_Toc17877604)](#_Toc17877476)

> [[The text of the progress note will be displayed on the right side of the screen.](#_Toc17877604)](#_Toc17877476)

3.  

[[Select Action \| Edit Progress Note… You can now edit the progress note.](#_Toc17877604)](#_Toc17877476)

[[To find specific text in a progress note, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Notes tab. Select a document title from the left side of the screen. (Click the "+" sign to expand a heading.) The text of the progress note will be displayed on the right side of the screen.](#_Toc17877604)](#_Toc17877476)

> [[Note: If a note has an addendum, the ![](cprs-user-manual-gui-version-updated-or-3-0-499/476.png) icon will appear in front of the note title. You may view the addendum by clicking the "+" sign to expand the note title and then selecting the appropriate addendum.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

3.  

> [[Right-click the text of the progress note and select Find in Selected Note. The Find dialog appears.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/477.png)](#_Toc17877604)](#_Toc17877476)

[[The Find dialog allows you to replace text in a progress note](#_Toc17877604)](#_Toc17877476)

4.  

> [[Enter the text that you want to find. Note: Check the Match whole world only or Match case check boxes to search using these options.](#_Toc17877604)](#_Toc17877476)

5.  

> [[Select Find Next. If the text is found, it will be highlighted in the progress note.](#_Toc17877604)](#_Toc17877476)

6.  

[[When finished, close the dialog.](#_Toc17877604)](#_Toc17877476)

[[To replace specific text in a progress note, follow these steps:](#_Toc17877604)](#_Toc17877476)

> [[Note: Users can edit only unsigned progress notes. Once a note is signed, it cannot be edited.](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Notes tab. Select a document title from the left side of the screen. (Click the "+" sign to expand a heading.) The text of the progress note will be displayed on the right side of the screen.](#_Toc17877604)](#_Toc17877476)

> [[Note: If a note has an addendum, the ![](cprs-user-manual-gui-version-updated-or-3-0-499/478.png) icon will appear in front of the note title. You may view the addendum by clicking the "+" sign to expand the note title and then selecting the appropriate addendum.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[Select Action \| Edit Progress Note…. Right-click the text of the progress note and select Replace Text. The Replace dialog displays.](#_Toc17877604)](#_Toc17877476)

5.  

[[Enter the text you wish to replace in the Find what field.  
](#_Toc17877604)](#_Toc17877476)

6.  

> [[Enter the new text in the Replace with field. ![](cprs-user-manual-gui-version-updated-or-3-0-499/479.png)](#_Toc17877604)](#_Toc17877476)

[[The Replace dialog allows you to replace text in a progress note](#_Toc17877604)](#_Toc17877476)

> [[Note: Check the Match whole world only or Match case check boxes to search using these options.](#_Toc17877604)](#_Toc17877476)

7.  

> [[Select either Find Next, Replace, or Replace All. If the text is found it will be highlighted (if you selected Find Next) or changed (if you selected Replace or Replace All).](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 

[[Service connection Provider name Location Date Diagnosis Procedure Visit Information CPRS shows the encounter provider and location for the visit on the Visit Encounter box, identified in the graphic by the pointer. You can access this box from any chart tab.](#_Toc17877604)](#_Toc17877476)

[[If a provider or location has not been assigned, CPRS will prompt you for this information when you try to enter progress notes, create orders, and perform other tasks.  
](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[In order to receive workload credit, you must enter encounter form data when you create a new progress notes, complete a consult, or write a discharge summary.](#_Toc17877604)](#_Toc17877476)

> [[Note: Once a note, summary, or consult has been completed, you can only change encounter information directly through Patient Care Encounter (PCE.)](#_Toc17877604)](#_Toc17877476)

[[To enter encounter form data, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

> [[Select the appropriate tab: Notes, Consults, or D/C Summ. Select New Note on the Notes tab, or locate the appropriate consult or discharge summary. For the latter two, skip step 3. Type in a title for the note or summary or select one from the list and press \<Enter\>. On the Notes tab, select the Encounter button, Action \| Encounter, or Edit Encounter Information from the right-click pop-up menu. On the Consults and D/C Summ tabs, only the Edit Encounter Information item is available on the pop-up menu. Select the tab where you want to enter information (Type of Visit, where you can also enter the primary and secondary providers, Diagnoses, where you can have diagnoses automatically be added to the Problem List, Procedures, Vitals, Immunizations, Skin Tests, Patient Ed., Health Factors, or Exams). Note: To enter vitals, follow this manual's instructions under <u>Recording</u> <u>Vitals</u>.](#_Toc17877604)](#_Toc17877476)

6.  

> [[Click the appropriate category in the list box on the left and then click the check boxes by the appropriate items in the list box on the right. If the section name you want is not shown or the list boxes are empty, use the search feature. To search, click on the Other \<Tab Name\>. (Each tab's button will be labeled differently.) Locate and double-click the needed item. Some tabs have a simple list to choose from. Diagnoses and Procedures have a search function. On these tabs, you need to enter the beginning of a term and click Search before double-clicking. Note: If a user tries to enter a diagnosis or procedure that has an inactive code associated with it, CPRS will not accept that selection and will request that the user change it. Also, although it is based on ICD-9-CM codes, the Other Diagnosis… button will now search the SNOMED Concept Terms (SNOMED CT) Problem List dataset, which should enable clinicians to better find the term they need. If the list does not show the item you are looking for, you can select the Extend Search button to search the ICD-9-CM file. All terms returned by this search must map to ICD-9-CM codes so you may not see a code that has a related SNOMED CT term and code, but you will see an ICD-9-CM code. If a provider enters a diagnosis with or problem that has a 799.9 code (something undefined), a notice will be sent to the Standards and Terminology Service and a new mapping will be created. When available, the 799.9 code will automatically be updated to the new code.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/481.png)](#_Toc17877604)](#_Toc17877476)

> [[This screen shows a diagnosis on the Encounter form with an inactive code](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/482.png)](#_Toc17877604)](#_Toc17877476)

> [[If a user selects a diagnosis or procedure with an inactive code, the above dialog will display telling the user that the code is inactive and that the user should change it](#_Toc17877604)](#_Toc17877476)

> [[Note: The Type of Visit and Vitals tabs are different. Type of Visit has no button, and Vitals has a Historical Vitals Details button that brings up a dialog containing a graph and a listing of past vitals taken.](#_Toc17877604)](#_Toc17877476)

7.  

> [[Enter any additional information as needed. Several tabs have additional features, such as drop-down lists for results of exams, severity of problems, and so on.](#_Toc17877604)](#_Toc17877476)

8.  
9.  

[[Fill in information for other tabs as needed by repeating steps 2-6. When finished, select OK.](#_Toc17877604)](#_Toc17877476)

[[When a user opens a patient record, CPRS starts a job to evaluate whether the patient has reminders that are due, available, etc. While the evaluation is in process, a magnifying glass goes in a circle on the Reminder button. When the magnifying glass stops, and a clock icon appears, the reminders evaluation is complete.](#_Toc17877604)](#_Toc17877476)

[[You can find out if a patient has reminders by doing one of the following:](#_Toc17877604)](#_Toc17877476)

- 

> [[Selecting the Reminders button near the top right of the CPRS form. When you click this button, a dialog with a reminders tree view will be displayed. The reminders button may display one of five icons. When it displays a red clock, the patient has reminders due. ![](cprs-user-manual-gui-version-updated-or-3-0-499/483.png)](#_Toc17877604)](#_Toc17877476)

> [[The Reminders button indicates whether there are reminders for the current patient](#_Toc17877604)](#_Toc17877476)

- 

> [[Looking on the coversheet that has an area specifically for reminders. Note: If under Due Date, the user sees Error or CNBD (which stands for "could not be determined"), a problem occurred while the reminders were being evaluated. You should contact your reminders coordinator.](#_Toc17877604)](#_Toc17877476)

- 

[[After you begin a new progress note, you will see the reminders drawer. If you click the drawer, a tree view of due, applicable, and other reminders will be displayed. The Due category automatically expands when you open the Reminders drawer, while the Applicable and Other categories do not.](#_Toc17877604)](#_Toc17877476)

> [[Note: Before you can process a reminder, a CAC or someone else must create a dialog in a similar position at your site. A dialog image over the clock or question mark icon shows that a reminder has an associated dialog.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

[[Clinical Maintenance—shows the possible resolutions and the findings associated with the reminder.Education Topic Definition—lists the education topics that have been defined for a reminder. You can select a topic to view the desired education outcome and any standards. Reminder Inquiry—shows the reminder definition describing which patients are selected for this reminder. Reference Information—lists Web sites with additional information. Evaluate Reminder–tells you if a reminder is due, applicable or other. Reminder Icon Legend–displays icon legend screen with icons and meanings. Each of these options brings up a window. When you are finished with the window, click Close. For more information on Clinical Reminders, refer to the *Clinical Reminders Manager Manual* and *Clinical Reminders Clinician Guide.*](#_Toc17877604)](#_Toc17877476)

[[Text and PCE data for the reminder that you are currently processing are in bold.  
](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[Required fields are no longer checked on a Reminder dialog unless at least one entry has been made on the dialog. This allows users to skip Reminders that are not intended for processing. Reminder dialog groups can now be set to NONE OR ONE SELECTION, which allows up to one entry in a group, but does not require an entry. PX\*1.5\*2 is required to change the reminder dialog definition. Required prompts and template fields will be marked with an asterisk (\*) to indicate that they are required. A message at the bottom of the Reminder dialog states "\* Indicates a Required Field." Reminder dialogs have a Visit Info button. It opens a dialog that allows the user to enter service-connected information, as well as the vital sign entry date and time. If service-connected information is required for the encounter and note title, this dialog automatically appears when you click Finish.](#_Toc17877604)](#_Toc17877476)

[[To process a reminder for a patient, complete the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[If you have not already, begin a new progress note by clicking the Notes tab, then New Note, and then select a note title. (If prompted, enter the encounter location and provider.) Click the Reminders drawer or the Reminders button to open a tree view of the reminders for this patient. Click the plus sign to expand the tree hierarchy where needed and then click the reminder you will process. You will then be presented with the dialog for processing reminders. Note: If you click the Reminders button, choose Action \| Process Reminders Due to begin with the first reminder due.](#_Toc17877604)](#_Toc17877476)

4.  
5.  
6.  
7.  
8.  

[[After you have entered all the information, you can finish processing the reminders.](#_Toc17877604)](#_Toc17877476)

[[When you finish, the following things will happen:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[When sites install CPRS v27 and the Mental Health dynamic link library (YS_MHA.dll), mental health providers will have enhanced mental health assessment tools. Mental health providers can use these tools through Reminders in CPRS if the following have occurred:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[With the CPRS GUI, you can create document templates to make writing or editing progress notes, completing consults, or writing discharge summaries quicker and easier. In addition, you can import or export templates and convert Microsoft Word files to document templates.](#_Toc17877604)](#_Toc17877476)

[[The Austin FSC Healthcare Claims Processing (HCP) Referral & Authorization System (RAS) requested an enhancement to make a TIU template used on a consult request as read-only. This action makes the template and all its associated template fields unavailable for edit—they can be viewed in the editors, but no values may be changed. RAS depends on specific text elements appearing in certain consult templates. If these templates are modified by a site, the messaging between RAS and VistA Consults/Request Tracking can be disrupted.](#_Toc17877604)](#_Toc17877476)

[[These templates should not be edited by facilities and as such will be locked during the installation of CPRS GUI v31b.](#_Toc17877604)](#_Toc17877476)

[[You can create and use your own templates, or you can use shared templates created by your Clinical Coordinator.](#_Toc17877604)](#_Toc17877476)

[[Authorized users can create personal templates. You can copy and paste text into a template, type in new content, add template fields, or copy a shared template into your personal templates folder. A shared template that you simply copy into your personal templates folder without changing continues to be updated whenever the original template is changed or modified in the Shared Templates folder. Once you personalize or change the copy of the shared template in your personal templates field, the icon used to represent it changes and it becomes a personal template. From that moment on, the personal template is not related to the shared template and is not updated with the original. In the tree view, personal template and folder icons have a folded upper right corner.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  

[[Open the Template Editor by selecting from the Notes, Consults, or DC/Summ tab by selecting Options \| Edit Shared Templates…. Verify that Edit Shared Templates is checked. Expand the tree view of Shared Templates and then Patient Data Objects by clicking on the plus sign beside each. Click on the existing object above which you want your new object to be. Click New Template and edit the name of the template. Place the cursor in the Template Boilerplate box and select Edit \| Insert Patient Data Object or right-click and select Insert Patient Data Object to bring up a dialog containing a list of TUI objects. Click the appropriate TIU object (that was probably just created). Click Apply or OK to make the new object available in GUI templates.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

1.  

> [[Open the Template Drawer on the Notes tab by clicking on it. The available templates will be displayed in a tree view.](#_Toc17877604)](#_Toc17877476)

2.  

> [[Right-click on any template and select Mark as Default from the right-click menu. ![](cprs-user-manual-gui-version-updated-or-3-0-499/489.png)](#_Toc17877604)](#_Toc17877476)

> [[You can set a template as your default template with a right click menu option](#_Toc17877604)](#_Toc17877476)

[[To make child templates unavailable from the template drawer, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

[[Click this check box to make individual parts of a dialog as display only. When a template is display only, the check box is removed and the item is used for information or instructions.](#_Toc17877604)](#_Toc17877476)

[[Click on this check box and the template will display only the first line of text followed by an ellipsis (...). The ellipsis indicates that more text exists. Hold the cursor over the line of text and a Hint box displays the complete text. This feature gives you the ability to have long paragraphs of text that do not take up a lot of room on the template. If selected, the entire paragraph is be inserted into the note.](#_Toc17877604)](#_Toc17877476)

[[Clicking on this check box affects the way that children items are displayed on the template. When selected, this feature gives the ability to show hierarchical structure in the dialog. All of the subordinate items for the selected item are indented.](#_Toc17877604)](#_Toc17877476)

[[Clicking on this check box affects the way that children items are displayed on the template. Click on this check box if you want to allow only one of the subordinate items to be selectable. Clicking on this check box changes the check boxes into radio buttons so that only one item can be selected at a time. To deselect all items, click on the one that is selected and the radio button will be cleared.](#_Toc17877604)](#_Toc17877476)

[[Clicking on this check box affects the way that children items are displayed on the template. Click on this option to have subordinate items appear only if the parent item is selected. This feature allows for custom user input. The user only sees the options related to the items selected. This feature requires boiler plated text at the parent level.](#_Toc17877604)](#_Toc17877476)

[[A check box in the Template Editor named "Allow Long Lines" allows template lines to be up to 240 characters in length. This feature mainly accommodates template field markup.](#_Toc17877604)](#_Toc17877476)

[[When you create templates, you can go directly into the Template Editor. There, you can type in text, and add Template Fields. If you are in a document and type in something you will use repeatedly, you simply select that text, right-click, select Create New Template, and the editor comes up with the selected text in the editing area. You can create individual templates, group templates, dialog templates, folders, or link templates to Reminder dialogs. Template dialogs are resizable.](#_Toc17877604)](#_Toc17877476)

[[Templates contain text, TIU objects, and Template Fields that you can place in a document.](#_Toc17877604)](#_Toc17877476)

[[Group templates contain text and TIU objects and can also contain other templates. If you place a group template in a document, all text and objects in the group template and all the templates it contains (unless they are excluded from the group template) will be placed in the document. You can also expand the view of the group template and place the individual templates it contains in a document one at a time.](#_Toc17877604)](#_Toc17877476)

[[Dialog templates are like group templates in that they contain other templates. You can place a number of other templates under a dialog template. Then, when you drag the dialog template into your document, a dialog appears that has a checkbox for each template under the Dialog template. The person writing the document can check the items they want and click OK to place them in the note.](#_Toc17877604)](#_Toc17877476)

[[Folders are used to group and organize templates and assist in navigating the template tree view. For example, you could create a folder called "radiology" for all of the templates relating to radiology.](#_Toc17877604)](#_Toc17877476)

[[Reminder dialogs can be linked to templates. This allows you to place orders and enter PCE information, Vitals information, and mental health data from a template. (Refer to Creating Reminder Dialogs for this procedure.)](#_Toc17877604)](#_Toc17877476)

[[You can use file cabinets and folders to group similar templates together to make them easier to find and use. For example, you may want to place all of the pulmonary templates together rather than listing the templates in alphabetical order.](#_Toc17877604)](#_Toc17877476)

[[To add a template to a Note, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[From the Notes tab, create a new note by clicking on New Note. Complete the Progress Note Properties dialog. Click OK. The Progress Note Properties dialog will close and the Templates Drawer will appear above the Reminder Drawer.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/490.png)](#_Toc17877604)](#_Toc17877476)

> [[The Templates Drawer](#_Toc17877604)](#_Toc17877476)

1.  

> [[Click the Templates drawer The available templates will appear.](#_Toc17877604)](#_Toc17877476)

2.  
3.  

> [[Select the template that you would like to use (click the + to expand a heading) Drag the template into the detail area of the note -or- double click on the template  
> ](#_Toc17877604)](#_Toc17877476)

> [[-or-](#_Toc17877604)](#_Toc17877476)

> [[right click on the template and select Insert Template.](#_Toc17877604)](#_Toc17877476)

[[Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/491.png)](#_Toc17877604)](#_Toc17877476)

> [[Drag the template into the detail area of the note](#_Toc17877604)](#_Toc17877476)

[[Searches for templates used to take some time, but changes included with CPRS v.27 should improve the template search speed.](#_Toc17877604)](#_Toc17877476)

[[To search for a template, use the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Right-click in the tree view (in either the Template Editor or the Templates drawer). Select the appropriate option: Find Templates, Find Personal Templates, or Find Shared Templates (depending on which tree view you are in). A search field will appear.](#_Toc17877604)](#_Toc17877476)

[[Note: You may want to narrow your search by using the Find Options feature.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[Enter the word or words you want to find and check the appropriate boxes. Select Find. Note: If the search lasts longer a few seconds, a dialog displays letting the user know that CPRS is still looking for the template. This dialog has an animation of a flashlight and there is a Cancel button is the user wishes to cancel the search.](#_Toc17877604)](#_Toc17877476)

5.  
6.  

[[To preview a template before inserting it into your document, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Right-click the template in the Templates drawer on the Notes tab. Select Preview/Print Template. The preview dialog will appear.](#_Toc17877604)](#_Toc17877476)

[[Note: You can print a copy of the template by pressing the Print button.](#_Toc17877604)](#_Toc17877476)

[[To delete a document template, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Click the Notes, Consults, or D/C Summ tab. Select Options \| Edit Templates -or-](#_Toc17877604)](#_Toc17877476)

> [[if the Templates drawer is open, right-click in the drawer and select Edit Templates.](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  

[[To speed document creation, you can create personal templates consisting of text, Template Fields, and Patient Data Objects. You can use the templates to create progress notes, complete consults, and write discharge summaries.](#_Toc17877604)](#_Toc17877476)

[[To create a personal document template, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Click the Notes, Consults, or D/C Summ tab. Start the Template Editor by selecting Options \| Create New Template -or-](#_Toc17877604)](#_Toc17877476)

> [[Select the text that you would like to save as a template, right-click the text, and select Copy into New Template.](#_Toc17877604)](#_Toc17877476)

3.  

> [[Type in a name for the new template in the Name field under Personal Template Properties. Note: Template names must begin with a letter or a number, be between 3 and 30 characters in length (including spaces), and cannot be named "New Template."](#_Toc17877604)](#_Toc17877476)

4.  
5.  

> [[Click the drop-down button in the Template Type field and select Template. Enter the content for the template by copying and pasting from documents outside CPRS, typing in text, and/or inserting Template Fields. Note: After you enter the content, you can right-click in the Template Boilerplate area to select spell check, grammar check, or check for errors (which looks for invalid Template Fields).](#_Toc17877604)](#_Toc17877476)

6.  
7.  
8.  

> [[Place the template in the tree view in the desired location. (To do this, click the plus sign next to an item to view its subordinate objects and then drag and-drop the template to its desired location. You can also move the template by using the arrows below the personal templates tree view.) Click Apply to save the template. Click OK to save and exit the editor. Note: You are not required to click Apply after each template, but it is recommended. If you click Cancel, you will lose all changes you have made since the last time you clicked Apply or OK.](#_Toc17877604)](#_Toc17877476)

[[You can create group templates which contain other templates. You can then place the entire group template in the note, which brings in the text and Template Fields from all templates in that group, or expands the tree view in the Templates drawer and places the individual templates under the group template in the note.](#_Toc17877604)](#_Toc17877476)

[[To create a personal Group Template, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Click the Notes, Consults, or D/C Summ tab Select Options \| Create New Template -or-](#_Toc17877604)](#_Toc17877476)

> [[Select the text that you would like to save as a template, right-click the text, and select Copy into New Template.](#_Toc17877604)](#_Toc17877476)

3.  

> [[Enter a name for the new template in the Name field under Personal Template Properties. Note: Template names must begin with a letter or a number, be between 3 and 30 characters in length (including spaces), and cannot be named "New Template."](#_Toc17877604)](#_Toc17877476)

4.  
5.  

> [[Click the drop-down button in the Template Type field and select Group Template. Enter the text and Template Fields to create content in the main text area of the group template, if desired. (You can enter content by copying and pasting from documents outside CPRS, typing in text, and/or inserting Template Fields.) Note: After you enter the content, you can right-click in the Template Boilerplate area to select spell check, grammar check, or Check Boilerplate for Errors, which looks for invalid Template Fields.](#_Toc17877604)](#_Toc17877476)

> [[Note: You can also create additional templates under the Group Template that you just created. To do this, simply highlight the appropriate group template and click New Template. Then complete the steps for creating a new template outlined above.](#_Toc17877604)](#_Toc17877476)

6.  
7.  
8.  

> [[Place the template in the tree view in the desired location. (To do this, click the plus sign next to an item to view its subordinate objects and then drag and-drop the template to its desired location. You can also move the template by using the arrows below the personal templates tree view.) Click Apply to save the template. Click OK to exit the template editor. Note: You are not required to click Apply after each template, but it is recommended. If you click Cancel, you will lose all changes you have made since the last time you clicked Apply or OK.  
> ](#_Toc17877604)](#_Toc17877476)

[[Clinical Coordinators and others who are authorized to edit shared templates and who are also members of the appropriate user class (specified in the EDITOR CLASS field, \#.07 of the TIU TEMPLATE file \#8927) may see the Document Titles, Consult Reasons for Request, and/or the Procedure Reasons for Request template folders. These folders allow you to associate a template with a progress note title, a procedure, or a type of consult. After an association is created, the appropriate template content is inserted in either the body of a note (when a new note is started) or in the Reason for Request field (when a new consult or procedure is ordered).](#_Toc17877604)](#_Toc17877476)

[[To associate a template with a document title, type of consult, or a procedure, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Create a new template (by following the instructions above for either the personal template or the group template) -or-](#_Toc17877604)](#_Toc17877476)

> [[edit an existing template by selecting Options \| Edit Templates….from the Notes, Consults, or D/C Summ tab.](#_Toc17877604)](#_Toc17877476)

2.  
3.  
4.  
5.  
6.  

> [[Click the Edit Shared Templates check box located in the lower left hand corner of the Template Editor window. Select the template you would like to associate from the Personal Templates section of the Template Editor window. Drag and drop the template into either the Document Titles, Consult Reasons for Request, or Procedure Reasons for Request folder in the Shared Templates area of the window. Select the template that you just moved (click "+" to expand a heading) in the Shared Templates area of the window. Select a procedure from the Associated Procedure drop-down list -or-](#_Toc17877604)](#_Toc17877476)

> [[select a consult service from the Associated Consult Service drop-down list.](#_Toc17877604)](#_Toc17877476)

7.  

[[Click OK. The template is now associated.](#_Toc17877604)](#_Toc17877476)

[[When you order a consult or a procedure, the associated template text will appear in the Reason for Request field. When you enter a new progress note the associated template text will appear in the text of the note.](#_Toc17877604)](#_Toc17877476)

[[You can import existing template files (.txml), Microsoft Word files (Word 97 or higher), or XML files into the CPRS Template Editor.](#_Toc17877604)](#_Toc17877476)

[[To import a template, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Start the Template Editor. Browse to the file cabinet or folder where you would like to store the imported template (click "+" to expand a heading). Note: To import a template to the Shared Templates area of the screen, you must be authorized to edit shared temples *and* place a checkmark in the Edit Shared Templates check box (located in the lower left side of the Template Editor).](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  

> [[Select Tools \| Import Template. Select the file you would like to import and click Open. The template will appear in the Template Editor. If you press OK, the template will be imported without the new fields. If you press Cancel, the import process will be cancelled. Note: If you do not have authorization to edit template fields, you may see this dialog.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/492.png)](#_Toc17877604)](#_Toc17877476)

> [[The template field warning dialog](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
1.  

> [[Select Options \| Create New Template on the Notes, Consults, or D/C Summ tab to bring up the Template Editor -or-](#_Toc17877604)](#_Toc17877476)

> [[Select the text that you would like to save as a template, right-click the text, and select Copy into New Template.](#_Toc17877604)](#_Toc17877476)

2.  

> [[Enter a name for the new template in the Name field under Personal Template Properties. Note: Template names must begin with a letter or a number, be between 3 and 30 characters in length (including spaces), and cannot be named "New Template."](#_Toc17877604)](#_Toc17877476)

3.  
4.  

> [[Click the drop-down button in the Template Type field and select Dialog. Enter the text and Template Fields to create content in the main text area of the template, if desired. You can enter content by copying and pasting from documents outside CPRS, typing in text, and/or inserting Template Fields. Note: After you enter the content, you can right-click in the Template Boilerplate area to select spell check, grammar check, or Check Boilerplate for Errors, which looks for invalid Template Fields.](#_Toc17877604)](#_Toc17877476)

> [[Note: You can also create additional templates under the Group Template that you just created. To do this, simply highlight the appropriate group template and click New Template. Then complete the steps for creating a new template outlined above.](#_Toc17877604)](#_Toc17877476)

5.  
6.  
7.  

> [[Place the template in the tree view in the desired location. (To do this, click the plus sign next to an item to view its subordinate objects and then drag and-drop the template to its desired location. You can also move the template by using the arrows below the personal templates tree view.) Click Apply to save the template. Click OK to exit the template editor. Note: You are not required to click Apply after each template, but it is recommended. If you click Cancel, you will lose all changes you have made since the last time you clicked Apply or OK.](#_Toc17877604)](#_Toc17877476)

[[Templates can be linked to Reminder dialogs that are listed in the TIU Reminder Dialogs parameter. This enables you to use templates to place orders, enter PCE information, and enter vital signs and mental health data. If there are no Reminder Dialogs in the TIU Reminders Dialog parameter, the Reminder Dialog template type will not be available.](#_Toc17877604)](#_Toc17877476)

[[To create a Reminder Dialog, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select Options \| Create New Template… on the Notes, Consults, or D/C Summ tab. The Template Editor will appear.](#_Toc17877604)](#_Toc17877476)

2.  

> [[Type in a name for the new template in the Name field under Personal Template Properties. Note: Template names must begin with a letter or a number, be between 3 and 30 characters in length (including spaces) and cannot be named "New Template."](#_Toc17877604)](#_Toc17877476)

3.  
4.  
5.  
6.  
7.  

[[Click the drop-down button in the Template Type field and select Reminder Dialog. Click the drop-down button in the Dialog field and select the Reminder Dialog desired. Place the template in the tree view in the desired location. (To do this, click the plus sign next to an item to view its subordinate objects and then drag and-drop the template to its desired location. You can also move the template by using the arrows below the personal templates tree view.) Click Apply to save the template. Click OK to exit the editor. Note: You do not have to click Apply after each template, but it is recommended because if you click Cancel, you will lose all changes you have made since the last time you clicked Apply or OK.](#_Toc17877604)](#_Toc17877476)

[[Folders are simply containers that allow you to organize and categorize your templates. For example, you might want to create a folder for templates about diabetes or one for templates about mental health issues.](#_Toc17877604)](#_Toc17877476)

[[To create a personal template folder, complete the following steps:](#_Toc17877604)](#_Toc17877476)

1.  

> [[Select Options \| Create New Template on the Notes, Consults, or D/C Summ tab to bring up the Template Editor -or-](#_Toc17877604)](#_Toc17877476)

> [[Select the text that you would like to save as a template, right-click the text, and select Copy into New Template.](#_Toc17877604)](#_Toc17877476)

2.  
3.  
4.  

[[In the Name field under Personal Template Properties, enter a name for the new folder. For ease of use, you should create a name that describes the content of the template. Click the template type: Folder. Drag-and-drop relevant templates into the template folder that you have created. Note: It is recommended that you click Apply after adding a template to save your changes. If you accidentally click Cancel, you will lose all the changes you have made since the last time you clicked Apply or OK.](#_Toc17877604)](#_Toc17877476)

[[Template Notes can be used to describe what is in the template or to track changes to the template.](#_Toc17877604)](#_Toc17877476)

[[To add or display Template Notes, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

> [[Click the Notes tab. Click Options *\|* Edit Templates. Select the shared or personal template for which you wish to add or change the Template Notes. Click the Show Template Notes check box at the bottom of the dialog. The *Template Notes* field appears below the *Template Boilerplate* field. Add or change the note as much as you wish. Note: If the template you wish to edit is a shared template and you have the authority to edit it, you will need to click the Edit Shared Templates check box on the lower left corner of the Template Editor dialog.](#_Toc17877604)](#_Toc17877476)

[[To add or display Template Notes from the Template Drawer, complete the following steps:](#_Toc17877604)](#_Toc17877476)

1.  

[[Select Options \| Edit Templates… from the Notes, Orders, or D/C Summ tab. The Template Editor will appear.](#_Toc17877604)](#_Toc17877476)

2.  
3.  
4.  

> [[Select the shared or personal template for which you wish to add or change the Template Notes. Click the Show Template Notes check box at the bottom of the dialog. The *Template Notes* field appears below the *Template Boilerplate* field. Add or change the note as much as you wish. Note: If the template you wish to edit is a shared template and you have the authority to edit it, you will need to click the Edit Shared Templates check box on the lower left corner of the Template Editor dialog.](#_Toc17877604)](#_Toc17877476)

[[To copy text from a template to any text field, complete the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

> [[Open a new note, consult or discharge summary. Select a note, consult or discharge summary title. Click the Notes tab Click the Templates drawer button. Expand either the Shared Template or Personal Templates tree. Right-click the desired template. Click Copy Template Text (or press Control+C) to copy the text to the clipboard. Note: You can paste the copied text into any text field by right clicking in the desired field and selecting Paste.](#_Toc17877604)](#_Toc17877476)

[[You can reduce the time required to complete a note, consult, or discharge summary by adding template fields to your templates and dialogs. Information that you would normally have to look up can be pulled directly into your note, consult, or discharge summary from the template fields in your templates.](#_Toc17877604)](#_Toc17877476)

[[To view the predefined characteristics of the template fields:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

[[Select the Notes, Consults, or D/C Summ tab. Select Options \| Edit Template Fields. Select the desired template field in the Template Fields list on the left side of the dialog. The field is copied to the Name field on the right side of the dialog and all of the existing elements of the field are displayed. Click Preview to see how the Template Field will appear on a template or click OK to complete the procedure. To create a new template field:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  - 
    - 
    - 
    - 
    - 
    - 
    - 
    - 

[[Select the Notes, Consults, or D/C Summ tab. Select Options \| Edit Template Fields. Select New. Type a unique name for the new template field. Select a Type: Edit BoxCombo BoxButtonCheck boxesRadio buttons Date Number Hyperlink  
](#_Toc17877604)](#_Toc17877476)

- 
- 
6.  
7.  
8.  
9.  

[[Once you have decided which Template fields to use or you have defined the Template Field that you need, you can add them into a template. With the Template field in the Template, you can quickly and easily select the items you wish to add to a note, consult or discharge summary.](#_Toc17877604)](#_Toc17877476)

[[Developers added two new template fields to CPRS v.27 to enable sites to better serve their visually impaired users:](#_Toc17877604)](#_Toc17877476)

- 
- 
1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
9.  
10. 
11. 

> [[From the Notes, Consults or D/C Summ tab, click Options \| Edit Templates... or Create Templates, Edit Shared Templates, or Create New Shared Template... From the Template Editor, select the template to which you wish to add a Template Field. Insert the cursor at the place in the Template Boilerplate field where you wish to insert the Template Field. From the toolbar, click Edit \| Insert Template Field or right-click in the template and select Insert Template Field. On the Insert Template Field dialog, type the first few letters of the desired field or scroll through the list until the desired field is located. Click the field you wish to insert. Click Insert Field. Repeat steps 5 through 7 for each additional Template Field you wish to insert. Click Done when you have added all of the desired template fields. From the tool bar, click Edit \| Preview/Print Template or right-click in the template and select Preview/Print Template. This will preview the template. If the template does not display with the desired appearance, you may continue to edit it. On the Template Editor dialog, click OK to save the changes to the template. Note: The Insert Template Field dialog is non-modal and can be used as a boilerplate if desired.](#_Toc17877604)](#_Toc17877476)

[[<span id="_Toc126154779" class="anchor"></span>Navigating Template <span id="template_required_fields" class="anchor"></span>Required Fields](#_Toc17877604)](#_Toc17877476)

> [[To aid in the completion of template dialogs, a navigation bar is available to assist with finding and completing "required" fields. This navigation bar will allow the user to quickly access all required fields in the template dialog. The navigation bar provides a count of all unanswered required fields and provides navigation buttons to allow the user to jump directly to the required field. In addition to the \* used to identify required fields, all incomplete required fields will be highlighted within the template. Once the required field is filled in, the counter will reduce and the highlight for the field will be removed.](#_Toc17877604)](#_Toc17877476)

[[Note: Sites can decide to turn off these additional features for required fields. If you do not see these features, it could be that the features, they could be disabled.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/496.png)](#_Toc17877604)](#_Toc17877476)

> [[This progress note template shows required fields with asterisks and yellow highlighting. On this dialog, there is a Required Fields without Values field and a navigation bar.](#_Toc17877604)](#_Toc17877476)

[[<span id="_Toc126154780" class="anchor"></span>Required Fields Settings](#_Toc17877604)](#_Toc17877476)

> [[Users can set preferences for the navigation bar location (Top, Left, Right, and Bottom) and whether the new highlight feature displays and the highlight color.](#_Toc17877604)](#_Toc17877476)

> [[Navigation Bar Location: The user can set the navigation bar position in three ways:](#_Toc17877604)](#_Toc17877476)

- [[a context menu (right-click menu) on the navigation bar itself, then select the location](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/497.png)Right-click on the Navigation bar to select where it displays.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

- [[a context menu (right click menu on the main dialog, then select Set Highlighting Preferences, then select the location on the dialog that displays (This method and the following one bring up the same dialog.)](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/498.png)Users can select Required Fields preferences.](#_Toc17877604)](#_Toc17877476)

- [[Going to Tools \|Options \| Notes tab, then select the Required Fields button, and then selecting the location.](#_Toc17877604)](#_Toc17877476)

> [[Enable/Disable Highlight and Setting the Highlight Color: The user can enable or disable the highlight and navigation bar features in two ways:](#_Toc17877604)](#_Toc17877476)

- [[The user also can enable/disable the highlighting within the template by accessing the Right Click (Context) menu associated with the body of the template, the user will see an option to Highlight Required Fields. When checked highlighting is enabled, while when it is unchecked the highlighting is disabled. The user can also select the highlight color.](#_Toc17877604)](#_Toc17877476)
- [[Another way to bring up the dialog is to select Tools \|Options \| Notes tab and then select the Required Fields button](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/499.png)](#_Toc17877604)](#_Toc17877476)

> [[Here, you will be able to enable/disable highlighting, change the highlight color, and change the Navigation Bar position.](#_Toc17877604)](#_Toc17877476)

- [[unnecessary duplication of information](#_Toc17877604)](#_Toc17877476)
- [[lengthening of notes and making chart reading more difficult](#_Toc17877604)](#_Toc17877476)
- [[slowing the retrieval of notes by the workstation](#_Toc17877604)](#_Toc17877476)
- [[improving accuracy of the note and the patient information](#_Toc17877604)](#_Toc17877476)

[[To help sites better audit what text is copied and pasted into clinical documents, CPRS defines](#_Toc17877604)](#_Toc17877476)

- [[who can view pasted text](#_Toc17877604)](#_Toc17877476)
- [[what constitutes tracked pasted text](#_Toc17877604)](#_Toc17877476)
- [[how CPRS will display pasted text](#_Toc17877604)](#_Toc17877476)
- [[how the person auditing can turn on or off the display of pasted text](#_Toc17877604)](#_Toc17877476)
- [[how the auditor can view the pasted text](#_Toc17877604)](#_Toc17877476)
- [[CHIEF, MIS](#_Toc17877604)](#_Toc17877476)
- [[CHIEF, HIMS](#_Toc17877604)](#_Toc17877476)
- [[PRIVACY ACT OFFICER](#_Toc17877604)](#_Toc17877476)

[[In addition, sites can give other user classes the ability to view copy/paste data.](#_Toc17877604)](#_Toc17877476)

[[<span id="_Toc126154783" class="anchor"></span>  
](#_Toc17877604)](#_Toc17877476)

- [[Minimum Number of Words: To be considered a paste, there must be at least the specified number of words. For example, if it is set at 15 words and a user pastes 14, CPRS will not identify it as a paste. The default is 5 words.](#_Toc17877604)](#_Toc17877476)
- [[Percentage Check: Because providers often edit text after it is pasted, CPRS checks what percentage of the original paste is in the document. For example, if this percentage is set at 85 percent and the user pastes some text but then edits it so that only 75 percent of the original text remains, it will not display as pasted text. The default is 90% unless changed by your site.](#_Toc17877604)](#_Toc17877476)
- [[Role: Until, the author and cosigner can see highlighted pasted text. After the note is signed, only users in specific user classes will see the pasted text.](#_Toc17877604)](#_Toc17877476)
- [[Exclude Note Title: Site can specify notes that will not be tracked for copy/paste.](#_Toc17877604)](#_Toc17877476)
- [[Exclude Application: Sites can specify that specified applications are not tracked for copy/paste. One application (netspeak.exe) is already included in this parameter.](#_Toc17877604)](#_Toc17877476)
- [[After Signature: While the author of a note is writing the note or editing it, CPRS will identify pasted text with highlighting or other methods as set by the user, if it meets the criteria above. If the author or cosigner of the document signs the document and they are not in the designated user class that can view pasted text, the pasted text will no longer be identified for them as pasted. In other words, if it is highlighted, it will no longer be highlighted and the area showing the pastes will not display it. The pastes can still be identified to auditors in CPRS.](#_Toc17877604)](#_Toc17877476)
- [[Within the Same Note: When text is copied and pasted from within the same note.](#_Toc17877604)](#_Toc17877476)
- [[Lines with 2 words or less: Lines with 2 words or less are not highlighted, but they are tracked.](#_Toc17877604)](#_Toc17877476)

[[  
<span id="_Toc126154784" class="anchor"></span>Setting How Pasted Text Will Display to Auditors, Authors, and Cosigners](#_Toc17877604)](#_Toc17877476)

[[CPRS has several options to determine how pasted text will display to reviewers, those who are in user classes that can view copied and pasted text. The user can select one method or combine all of them:](#_Toc17877604)](#_Toc17877476)

- [[Bold](#_Toc17877604)](#_Toc17877476)
- [[Italics](#_Toc17877604)](#_Toc17877476)
- [[Underline](#_Toc17877604)](#_Toc17877476)
- [[Highlight](#_Toc17877604)](#_Toc17877476)
1.  
2.  
3.  
1.  

[[In CPRS, bring up the Options dialog by selecting Tools \| Options.Select the Copy/Paste tab.Under the "How text is identified on the note" section, select which attributes or combination of attributes you want to identify pasted text by checking the box for each attribute:Bold ItalicsUnderlineHighlight](#_Toc17877604)](#_Toc17877476)

[[  
![](cprs-user-manual-gui-version-updated-or-3-0-499/500.png)](#_Toc17877604)](#_Toc17877476)

[[<span id="Copy_paste_tab" class="anchor"></span>From the Tools \| Options dialog on the Copy/Paste tab, the auditing user can choose any combination of the way CPRS should display the options.](#_Toc17877604)](#_Toc17877476)

4.  
5.  
5.  
6.  

[[If you select Highlight, you may also use the default color or choose a different color. To select a different color, select the drop-down arrow and choose the color:Black  
Maroon  
Green  
Olive  
Navy  
Purple  
Gray  
SilverRedLimeYellowBlueFuchsiaAquaWhiteIf you would like to see in the detailed display the original text that was replaced, check the Display differences between what was paste in details pane check box.When done, select OK.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
13. 
4.  

[[On the Notes tab, if you have been assigned as a user who can audit and there is text that has been pasted into the note you are viewing, you will see a new Pasted Data pane below the main note pane. To view what text has been pasted, select an item from the list under Pasted Data by clicking it or tabbing to it. When an item is highlighted, such as when the user selects a date, the pasted text will display in the pane to the right of the list and it will be displayed as the user defined on the Notes tab of the Options dialog. In the pane to the right of the Pasted Data List, the user can see the following information about the pasted text:Date: The date the paste was madeUser: Which user pasted the dataFrom: The Source (if VistA the source will be known, if from outside VistA, it may just read from outside)Copied from Patient: This will tell what patient the data was copied from if known.Percentage: What percentage of the original text was pasted.Pasted Text: This displays the text that was pasted. This is especially useful for user who might have visual difficulties.To view other pasted entries, simply select the appropriate item (or date) in the list.  
](#_Toc17877604)](#_Toc17877476)

[[Consults are requests from one clinician to a hospital, service or specialty for a procedure or other service.](#_Toc17877604)](#_Toc17877476)

[[The Consults process involves the following steps. A single individual or service does not take all of the steps.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
9.  
10. 
11. 

> [[The clinician orders a consult. From within the patient's CPRS medical record, the clinician enters an order for a consultation or procedure. The ordering clinician may first have to enter Encounter Information. The consult service receives an alert and a printed SF 513. The receiving service can then accept the consult, forward it to another service, or send it back to the originating clinician for more information. The consult service accepts or rejects the consult request. To accept the consult, the service uses the receive action. The service can also discontinue or cancel the consult. Cancelled consults can be edited and resubmitted by the ordering clinician. A consult service clinician sees the patient. The consult service enters results and comments. Resulting is primarily handled through TIU. The originating clinician receives a CONSULT/REQUEST UPDATED alert that the consult is complete. The results can now be examined and further action taken on behalf of the patient. The SF 513 report becomes part of the patient's medical record. A hard copy can be filed and the electronic copy is on line for paperless access. Results from the Medicine package can be attached to complete consults involving procedures. This function is available through the GUI for the Consults package, but will only be seen when the supporting Consults patch GMRC\*3.0\*15 is installed. The absence of these patches will result only in the function not being present. If Consults patch GMRC\*3.0\*18 has been installed, the Edit/Resubmit action is available for cancelled consults. The consult must be "resubmittable" and the user must be authorized to resubmit consults. The Consults tab has a list of consults in a tree view similar to the ones found on the Notes tab and the Discharge Summary tab. However, the list view feature is not available due to differences in the tabs functions. Consults are differentiated from procedures in the tree by the type of icon displayed. Consults are represented by a notepad, while procedures are represented by a caduceus-like symbol. Right-click in the Consults text and you may select the "Find in Selected Consult" option from the popup menu. This option allows you to search the displayed text. A "Replace Text" option is also available, but it is only active when a consult is being edited.  
> The field below the list of consults displays a list of documents related to the highlighted consult or procedure. These related documents are also in a tree view. Note: If the provider has an NPI, it will not display on the screen below](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/502.png)](#_Toc17877604)](#_Toc17877476)

> [[The Consults tab](#_Toc17877604)](#_Toc17877476)

[[Changing the view of the Consults tab allows you to focus the list of consults on one of several criteria. Focusing the list will speed up the selection process. You may change the Consults view to only include the following problems:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[All Consults Consults by Status Consults by Service Consults by Date Range To change the view, click View on the menu and select the desired list items.  
](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Consults tab. Select the consult you would like to view from the All Consults list. The text of the consult will appear in the details pane. Any notes associated with that consult or procedure will appear in the Related Documents pane. To view the text of a related note, click on the note.](#_Toc17877604)](#_Toc17877476)

> [[Note: The All Consults list shows the date, status (p=pending, c=complete, dc=discontinued, and x=cancelled), and title of each consult. An asterisk preceding the title tells you that there are significant findings for that consult. If a note listed in the related documents pane is a CP-class document, the *Date/Time Performed* and *Procedure Summary Code* fields will appear in the full text of the document.](#_Toc17877604)](#_Toc17877476)

> [[Below is an example of a detailed display of a Consult](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/506.png)](#_Toc17877604)](#_Toc17877476)

> [[This screen capture shows a detailed view of a consult](#_Toc17877604)](#_Toc17877476)

[[Note: If the provider has an NPI, it will not display on the screen above](#_Toc17877604)](#_Toc17877476)

[[When CPRS displays a request for a new consult, the user can take several actions from the Consult Tracking menu item:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 

> [[Receive\* – When the request arrives at the specified service, the designated person, such as a clerk, can use Receive to change the consult status to active. Schedule – The service can schedule a consult, which makes the consult available to be resulted. Cancel (Deny) – A consult service may cancel or deny a consult request because of incomplete information or for some other reason. The consult requester is then notified that the consult was canceled so that the requester can take appropriate action. Discontinue\* – The user can discontinue a consult if it is no longer needed. Forward\* – The user can forward a consult if the user is not the appropriate person for the consult. Add Comment\* – The user can add comments and designate to whom the comment should go in an alert. Significant Findings\* – The user can add significant findings and designate them as such. Administratively Complete\*– Allows completion of a consult without creation of a new progress note. *\* These actions are supported by the Consult Toolbox, which automates and assists the user's ability to enter common actions. Right click in the comment area and select the desired type of action.*](#_Toc17877604)](#_Toc17877476)

[[Many of the above actions send an alert to the recipients for the service and/or back to the requester to let them know that the status of the request has changed or that some has taken some action on the request.](#_Toc17877604)](#_Toc17877476)

[[CPRS alert recipients follow these rules:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 

[[Note: Until Clinical Procedures 1.0 is released, completion of all consults and procedures will continue to function as it does currently. After the installation and implementation of Clinical Procedures 1.0, any procedure defined as a Clinical Procedure will be completed using a document from the "Clinical Procedures" TIU class, which has some unique properties. In addition, to complete a Clinical Procedure, a person must be defined as an interpreter (update user) for the consult service to which the Clinical Procedure was directed.  
](#_Toc17877604)](#_Toc17877476)

[[To complete a consult from the Consults tab, complete the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Consults tab. Select Action \| Consult Results \| Complete/Update Results.Note: If this visit is undefined, you will be prompted for encounter type and location, clinician, date, and type of visit, such as Ambulatory, Telephone, or Historical.](#_Toc17877604)](#_Toc17877476)

3.  

> [[In the Consult Note Properties dialog, select Progress Note Title (e.g., General, SOAP, Warning, etc.). For titles that require entry of a cosigner, another field will display where the user can enter the information. Note: If the provider has an NPI, it will display on the screen below. See the "National Provider Identifier (NPI) Display in CPRS section for an example of an NPI displaying on a screen](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/511.png)](#_Toc17877604)](#_Toc17877476)

> [[In the Consult Note Properties dialog, the user selects the items for the note that will complete the consult, including the Note title, the date and time (if not when the user began the note), and the author, which should default to the user if the user is a provider](#_Toc17877604)](#_Toc17877476)

4.  
5.  
6.  

> [[If necessary, change the note date by selecting the button next to the date and entering a new date or by typing in a new date and time directly in the field. If necessary, change the note author by selecting the author from the Author drop-down list. Enter any additional information, such as an associated consult or an expected cosigner. Completing these steps will allow the note to be automatically saved. Note: Occasionally a problem occurs if a cosigner's access lapses and they have become "disusered." If this occurs, you can click OK and proceed with that selection or click Cancel and choose another cosigner.](#_Toc17877604)](#_Toc17877476)

7.  
8.  

> [[Select OK. Create your note by typing text, using templates, and including any test results. Note: If you need to view the consult details while writing a note, bring up the popup menu by right-clicking in the note editing pane and choosing View Consult Details or using the shortcut Shift+Ctrl+U.](#_Toc17877604)](#_Toc17877476)

9.  

> [[From the Action menu, select either Sign Note Now or Save without Signature. Note: The *Date/Time Performed* and *Procedure Summary Code* fields must also be completed on the first CP document that completes the procedure request. Completing the *Date/Time Performed* and *Procedure Summary Code* fields is optional on subsequent CP documents.](#_Toc17877604)](#_Toc17877476)

[[To create a new consult from the Consults tab, complete the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[Go to the Consults tab. Select the New Consult button. If the Provider and Location for Current Activities dialog opens, fill in the Visit Location and other information, and select OK. Select a service from in the Consult to Service/Specialty window. When you select the Consult Service or Specialty, several things may happen:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
5.  
6.  

> [[If the service has some prerequisites, a dialog will display stating what those are and will allow you to print the information, continue to place the consult order, or cancel the order. In addition, any predefined text or template will display to help the user fill out the Reason for Request field. The Provisional Diagnosis field becomes active as well.Select the urgency from the Urgency field. Select the person to whom you are sending the consult from the Attention field. Note: To help you distinguish between providers, CPRS displays their titles (if available). When two or more providers have identical names, CPRS also displays:](#_Toc17877604)](#_Toc17877476)

> [[o The service/section and site division (if any) associated with these providers; site divisions are displayed based on the following rules:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

> [[When no division is listed for a provider, no division is displayed. If only one division is listed, this division is displayed. If the site has multiple divisions or more than one division is listed and one of these listed divisions is marked as Default, CPRS displays the division marked as Default. If more than one division is listed for a provider and none is marked as Default, CPRS does not display division information for this provider. o Providers who are listed in the New Person file as Visitors are screened out from the provider list. (These screened-out providers are listed as Visitors because their entries were created as a result of a Remote Data View.)](#_Toc17877604)](#_Toc17877476)

7.  

> [[If necessary, enter a different Clinically Indicated Date. Note: The Clinically Indicated Date field does not apply to Prosthetics consults services, and the field is not available when the user selects a Prosthetic service.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 

> [[Select whether the consult is for an inpatient or an outpatient. Select the Place of Consultation from the list. Enter a Provisional Diagnosis For each consult, this field is either set up to require that](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

> [[The user type in an answer (the box will be white and the Lexicon button unavailable), or The user must select a response from the Lexicon (the field will be yellow and the Lexicon button is available).CPRS will search for diagnoses that contain the search term. The matching terms will display in the bottom portion of the Problem List Lexicon Search dialog. The search now looks for SNOMED Concepts Terms (SNOMED CT) items. Most items will also be mapped to an ICD-9-CM code. The list will show the SNOMED concept text, the SNOMED code, and the ICD-9-CM code if the term is mapped to one. If you do not see the appropriate problem listed, select the Extend Search button. On the Consults tab, the Extend Search button extends the search to the ICD-9-CM clinical hierarchy to find additional terms. Note: If a user tries to enter a diagnosis with an inactive code, CPRS will bring up a message indicating that the code must be changed and giving the user the chance to choose a diagnosis with and active code.](#_Toc17877604)](#_Toc17877476)

- 
11. 

> [[Beginning on October 1, 2014, CPRS will use ICD-10-CM codes when providers use the Lexicon to enter a provisional diagnosis for new consult requests.Fill in a Reason for Request. Sites can help users by putting in predetermined boilerplate text, text with TIU objects, and/or it could be linked to a template that users can fill out. Users can then add to the text already present. Or the field may be left blank for the user to fill in the reason. However, a reason for request is required and the consult cannot be saved without a reason for request.](#_Toc17877604)](#_Toc17877476)

12. 
13. 

> [[Select Accept Order. If finished ordering consults for this patient, select Quit. You may sign the order now from the Orders tab or wait until later.](#_Toc17877604)](#_Toc17877476)

[[To request a new procedure from the Consults tab, complete the following steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

[[Select the Consults Tab. Select the New Procedure button. If the Provider & Location for Current Activities dialog opens, fill in contact information, and select OK. Locate and select the procedure in the Procedure list. When you select the Consult Service or Specialty, several things may happen:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
5.  
6.  

[[If the service has some prerequisites, a dialog will display stating what those are and will allow you to print the information, continue to place the consult order, or cancel the order. In addition, any predefined text or template will display to help the user fill out the Reason for Request field. The Provisional Diagnosis field becomes active as well.Select the urgency from the Urgency field. Select an individual from the Attention field. Note: To help you distinguish between providers, CPRS displays their titles (if available). When two or more providers have identical names, CPRS also displays:](#_Toc17877604)](#_Toc17877476)

- - 
  - 
  - 
  - 
- 
7.  

[[The service/section and site division (if any) associated with these providers; site divisions are displayed based on the following rules: When no division is listed for a provider, no division is displayed. If only one division is listed, this division is displayed. If the site has multiple divisions or more than one division is listed and one of these listed divisions is marked as Default, CPRS displays the division marked as Default. If more than one division is listed for a provider and none is marked as Default, CPRS does not display division information for this provider. Providers who are listed in the New Person file as Visitors are screened out from the provider list. (These screened-out providers are listed as Visitors because their entries were created as a result of a Remote Data View.)If needed, designate a different Clinically Indicated Date. Note: The Clinically Indicated Date field does not apply to Prosthetics consults services, and the field is not available when the user selects a Prosthetic service. If necessary, select a service that will perform the procedure by using the down arrow to open the list and then selecting the service.](#_Toc17877604)](#_Toc17877476)

[[Often, the service is already defined. However, sometimes, the user has the chance to choose.](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 

[[Select whether the patient is an inpatient or outpatient. Select a place of consultation from the Place of Consultation drop-down list. Enter a provisional diagnosis in the Provisional Diagnosis field. For each procedure, this field is either set up to require that](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

> [[the user type in an answer (the box will be white and the Lexicon button unavailable), or the user must select a response must be from the Lexicon (the field will be yellow and the Lexicon button is available). CPRS will search for diagnoses that contain the search term. The matching terms will display in the bottom portion of the Problem List Lexicon Search dialog. The search now looks for SNOMED Concepts Terms (SNOMED CT) items. Most items will also be mapped to an ICD-9-CM code. The list will show the SNOMED concept text, the SNOMED code, and the ICD-9-CM code if the term is mapped to one.If you do not see the appropriate problem listed, select the Extend Search button. On the Consults tab, the Extend Search button extends the search to the ICD-9-CM clinical hierarchy to find additional terms. Note: If a user tries to enter a diagnosis with an inactive code, CPRS will bring up a message indicating that the code must be changed and giving the user the chance to choose a diagnosis with and active code.](#_Toc17877604)](#_Toc17877476)

- 

[[Beginning on October 1, 2014, CPRS will use ICD-10-CM codes when providers use the Lexicon to enter a provisional diagnosis for new procedure requests.  
](#_Toc17877604)](#_Toc17877476)

11. 

[[Enter a reason for this request in the Reason for request field. Sites can help users by putting in predetermined boilerplate text, text with TIU objects, and/or it could be linked to a template that users can fill out. Users can then add to the text already present. Or the field may be left blank for the user to fill in the reason. However, a reason for request is required and the consult cannot be saved without a reason for request.](#_Toc17877604)](#_Toc17877476)

12. 

> [[Select Accept Order. Enter another order -or-](#_Toc17877604)](#_Toc17877476)

> [[select Quit.](#_Toc17877604)](#_Toc17877476)

[[Note: The order must be signed before it is sent. You can either sign the order now or wait until later.](#_Toc17877604)](#_Toc17877476)

[[At times, a clinician or service might receive a consult and decide that the consult should be done by someone else. In this case, the user can forward the consult to the appropriate user. To forward a consult, the user can enter the following criteria](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

> [[The service to which the consult should be sent (required) Any needed comments (optional) The Urgency (required) When the action is taken (optional , Now is default) Who is responsible for the action (who made the decision to forward the consult—required) To whom the consult will be forwarded, if known (optional) ![](cprs-user-manual-gui-version-updated-or-3-0-499/512.png)](#_Toc17877604)](#_Toc17877476)

> [[From the Forward Consult dialog, the user enters the necessary information to send the consult to a more appropriate service or person](#_Toc17877604)](#_Toc17877476)

[[Note: If the provider has an NPI, it will display on the screen above. See the "National Provider Identifier (NPI) Display in CPRS section for an example of an NPI displaying on a screen.](#_Toc17877604)](#_Toc17877476)

[[To forward a consult, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

[[If not already on it, go to the Consults tab by selecting the tab or choosing View \| Chart tab \| Consults (or Ctrl + t). In the Forward Consult dialog under To service, select the consult service to which the consult will be sent. Type in some letters in the service name and scroll to find it, and use the plus sign to expand grouper items. Add comments if needed. Select the Urgency from the drop-down list. Select the date and time of the action (forwarding). The default is Now. Select the Responsible Person (the person who made the decision to forward the consult.) This is a required field. In the Attention field, select the name of the person to whom the consult should go, if known. Otherwise, this can be left blank.](#_Toc17877604)](#_Toc17877476)

[[<span id="Consults_RAS_Comm_Error_31b" class="anchor"></span>The Austin FSC Healthcare Claims Processing (HCP) Referral & Authorization System (RAS) depends on specific text elements appearing in certain consult templates. If these templates are modified by a site, the messaging between RAS and VistA Consults/Request Tracking can be disrupted.](#_Toc17877604)](#_Toc17877476)

[[In Consults, a MailMan error message is generated when there is a communication issue between RAS and VistA. This message has been improved to include the HCPS support mail group as a recipient. In addition, the message body will now include the consult number and facility name from where the consult originated. These new elements will assist HCPS support with more rapid resolution of communication errors.](#_Toc17877604)](#_Toc17877476)

1.  

> [[On Consults tab of CPRS, click on New Consult. The Provider & Location for Current Activities dialog box displays.![](cprs-user-manual-gui-version-updated-or-3-0-499/513.png)](#_Toc17877604)](#_Toc17877476)

2.  
3.  
4.  

> [[Select a provider from the Encounter Provider section. From the New Visit tab, select a location from the Visit Location section. Click OK. The Order a Consult dialog box displays. ![](cprs-user-manual-gui-version-updated-or-3-0-499/514.png)](#_Toc17877604)](#_Toc17877476)

> [[Note: If a provider has an NPI, it will display on the screens listed in instructions \#1 and \#4 above. See the "National Provider Identifier (NPI) Display in CPRS section for an example of an NPI displaying on a screen.  
> ](#_Toc17877604)](#_Toc17877476)

5.  

> [[From the Consult to Service/Specialty section, select the Community Care Direct Schedule or Administrative specialty required. A consult template displays.![](cprs-user-manual-gui-version-updated-or-3-0-499/515.png)](#_Toc17877604)](#_Toc17877476)

6.  
7.  

> [[Complete the consult template.  
> Click OK. The completed fields display in the Reason for Request of the Consult Order Dialog.![](cprs-user-manual-gui-version-updated-or-3-0-499/516.png)](#_Toc17877604)](#_Toc17877476)

8.  
9.  

> [[Complete all required order dialog fields. Click Accept Order. The consult is created on the Consults tab of CPRS.![](cprs-user-manual-gui-version-updated-or-3-0-499/517.png)](#_Toc17877604)](#_Toc17877476)

10. 

> [[Select the Orders tab in CPRS. The new order will show as pending in bold or unreleased in blue. ![](cprs-user-manual-gui-version-updated-or-3-0-499/518.png)](#_Toc17877604)](#_Toc17877476)

11. 

> [[Click File\>Refresh Patient. The Review/Sign Changes dialog box displays. ![](cprs-user-manual-gui-version-updated-or-3-0-499/519.png)](#_Toc17877604)](#_Toc17877476)

> [[NOTE: Select New Patient and Review/Sign Changes will also cause this dialog box to display, as would exiting CPRS.](#_Toc17877604)](#_Toc17877476)

12. 

> [[Click OK to refresh the screen. The Status column now displays as pending and is no longer bold font. ![](cprs-user-manual-gui-version-updated-or-3-0-499/520.png)](#_Toc17877604)](#_Toc17877476)

> [[NOTE: There are some users that hold both the OR ADMIN RBP TO CC and the OREMAS security keys. In this case the Review/Sign Changes dialog box is slightly different.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/521.png)](#_Toc17877604)](#_Toc17877476)

13. 
14. 

[[Select the Hold until Signed radio button. Click OK to refresh the screen.  
](#_Toc17877604)](#_Toc17877476)

[[Discontinuing a COMMUNITY CARE -DS or -ADMIN Consult with the Admin Key:](#_Toc17877604)](#_Toc17877476)

| [[![](cprs-user-manual-gui-version-updated-or-3-0-499/522.png)](#_Toc17877604)](#_Toc17877476) | [[Discontinuing a Consult should always be done on the Consults tab. NEVER ATTEMPT TO DO THIS ON THE ORDERS TAB](#_Toc17877604)](#_Toc17877476) |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|

1.  

> [[From the Consults tab in CPRS, click on the consult in the left-hand panel to select it. ![](cprs-user-manual-gui-version-updated-or-3-0-499/523.png)](#_Toc17877604)](#_Toc17877476)

2.  

> [[From the Action menu, select Consult Tracking, and then Discontinue. The Discontinue Consult: Comments dialog box displays. ![](cprs-user-manual-gui-version-updated-or-3-0-499/524.png)](#_Toc17877604)](#_Toc17877476)

3.  

> [[In the Discontinue Consult dialog box, enter comments in the Comments field. ![](cprs-user-manual-gui-version-updated-or-3-0-499/525.png)](#_Toc17877604)](#_Toc17877476)

4.  

> [[Click OK. The consult detail now shows that the consult has been discontinued. ![](cprs-user-manual-gui-version-updated-or-3-0-499/526.png)](#_Toc17877604)](#_Toc17877476)

> [[NOTE: The Admin Key can be used in conjunction with other security keys and there are several scenarios for this process. To see detailed steps to create and discontinue Community Care -DS and -ADMIN consults see Admin Key Training Guide (VDL\>CPRS: Consult/Request Tracking\>oc_adminkey_tg.docx).](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Surgery tab. Select a report title from the All Surgery Cases section of the window. Click the "+" sign to expand a heading (if necessary).  
> The text of the report will be displayed in the right side of the window. Note: If the provider has an NPI, it will not display on the screen below](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/530.png)](#_Toc17877604)](#_Toc17877476)

> [[A report displayed on the CPRS Surgery tab](#_Toc17877604)](#_Toc17877476)

[[To search a surgery report for specific text, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

> [[Select the Surgery tab. Select a report title from the All Surgery Cases section of the window. Right-click in the right-hand section of the window. Select Find in Selected Document. Type in the text you wish to find in the "Find what" field of the Find dialog box. Select Find Next. The appropriate text will be highlighted if it is found in the surgery report.![](cprs-user-manual-gui-version-updated-or-3-0-499/531.png)](#_Toc17877604)](#_Toc17877476)

> [[To find specific text in a surgery report, right-click in the right-hand section of the window](#_Toc17877604)](#_Toc17877476)

[[You can limit the surgery cases that appear on the Surgery tab. You can specify that only surgery cases from a specific date or date range appear on the tab, or you can specify that all available surgery cases appear.](#_Toc17877604)](#_Toc17877476)

[[To limit the surgery cases displayed to a specific date range, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Surgery tab. Select View \| Custom View. The List Selected Cases dialog box appears.](#_Toc17877604)](#_Toc17877476)

> [[![](cprs-user-manual-gui-version-updated-or-3-0-499/532.png)](#_Toc17877604)](#_Toc17877476)

> [[The List Selected Cases dialog](#_Toc17877604)](#_Toc17877476)

3.  - 
    - 
    - 
4.  - 
    - 
    - 
5.  
6.  
7.  
8.  
9.  
10. 
11. 
12. 

[[Select a beginning date by selecting in the appropriate field and doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001). entering a date formula (e.g. t-200). pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/533.png) button to bring up a calendar. Select an ending date by selecting in the appropriate field and doing one of the following: entering a date (e.g. 6/21/01 or June 21, 2001). entering a date formula (e.g. t-200). pressing the ![](cprs-user-manual-gui-version-updated-or-3-0-499/534.png) button to bring up a calendar. Enter a maximum number of occurrences in the Max Number to Return field. Select a surgery case sort order (ascending or descending). Select a category to group the surgery cases by (from the Group By dropdown list). Select a case report sort order (ascending or descending). Select a category to sort case reports by (from the Sort By drop-down list). Select OK. The appropriate surgery cases will appear in the left side of the screen. Click the "+" sign to expand a heading (if necessary). To view all the surgery cases for a patient, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

[[Depending on the configuration of your site and your access permission, you may be able to sign certain surgery reports.](#_Toc17877604)](#_Toc17877476)

[[To sign a surgery report, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Select the Surgery tab. Select a surgery report from the All Surgery Cases section of the window. Select Action \| Sign Report Now… -or-](#_Toc17877604)](#_Toc17877476)

> [[right click in the right-side of the window and select Sign Report Now.](#_Toc17877604)](#_Toc17877476)

4.  
5.  

[[Depending on the configuration of your site and your access permission, you may be able to make addenda to certain surgery reports.](#_Toc17877604)](#_Toc17877476)

[[To make an addendum to a surgery report, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

[[Select the Surgery tab. Select a surgery report from the All Surgery Cases section of the window. Select Action \| Make Addendum… Type the text for the addendum.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[Select a grouping node (for example "All signed notes") in the tree to display a second list of all the documents falling under that grouping node. This second list can be sorted by clicking on the column headings (Date, Title, Author, Location).  
](#_Toc17877604)](#_Toc17877476)

[[Changing the view of the Discharge Summary tab allows you to focus the list of summaries on one of several criteria. Focusing the list will speed up the selection process.](#_Toc17877604)](#_Toc17877476)

[[You may change the Discharge Summaries List view to only include the following summaries:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 

[[  
](#_Toc17877604)](#_Toc17877476)

[[To view a discharge summary, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  - 
    - 
    - 
    - 
    - 
    - 

> [[Select the D/C Summ tab. Select the summary in the list box. To sort the list, select View and the appropriate choice below: Signed Summaries (All) Signed Summaries by Author Signed Summaries by Date Range Uncosigned Summaries Unsigned Summaries Custom View Note: To set one of these views as the default, select View \| Save as Default.](#_Toc17877604)](#_Toc17877476)

4.  

[[You can enter discharge summaries through CPRS. The document templates and TIU titles that your site can create should make creating these documents much faster and easier.](#_Toc17877604)](#_Toc17877476)

[[To write a discharge summary, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
88. [[Select the D/C Summ tab. Select New Summary or select Action \| New Discharge Summary.](#_Toc17877604)](#_Toc17877476)

> [[Note: If this visit is undefined, CPRS prompts for encounter type and location, clinician, date and type of visit, such as Ambulatory, Telephone, or Historical.](#_Toc17877604)](#_Toc17877476)

2.  
89. [[In the Discharge Summary Properties dialog, select Discharge Summary Title (e.g., General, SOAP, Warning, etc.). Additional items will appear on the dialog for titles that require entry of a cosigner or an associated consult. If necessary, change the note date by clicking the button next to the date and entering a new date.](#_Toc17877604)](#_Toc17877476)
90. [[If necessary, change the note author by selecting the author from the Author drop-down list.](#_Toc17877604)](#_Toc17877476)

> [[Note: To help you distinguish between providers, CPRS displays their titles (if available). When two or more providers have identical names, CPRS also displays:](#_Toc17877604)](#_Toc17877476)

> [[o The service/section and site division (if any) associated with these providers; site divisions are displayed based on the following rules:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

> [[When no division is listed for a provider, no division is displayed. If only one division is listed, this division is displayed. If the site has multiple divisions or more than one division is listed and one of these listed divisions is marked as Default, CPRS displays the division marked as Default. If more than one division is listed for a provider and none is marked as Default, CPRS does not display division information for this provider. o Providers who are listed in the New Person file as Visitors are screened out from the provider list. (These screened-out providers are listed as Visitors because their entries were created as a result of a Remote Data View.)](#_Toc17877604)](#_Toc17877476)

91. [[Enter the attending physician.](#_Toc17877604)](#_Toc17877476)
92. [[Select the admission related to this Discharge Summary.](#_Toc17877604)](#_Toc17877476)
93. [[Enter any additional information, such as an expected cosigner. Completing these steps will allow the note to be automatically saved.](#_Toc17877604)](#_Toc17877476)

> [[Note: For a Discharge Summary, if a user requires a cosigner (such as a student or other type of clinician), that user's name should not appear in the list of potential cosigners. Also, occasionally a problem occurs if a cosigner's access lapses and they have become "disusered." If this occurs, you can click OK and proceed with that selection or click Cancel and choose another cosigner.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  

[[Select OK. Create the summary content by typing in text, copying and pasting, and/or inserting templates into the document. Select the template drawer if it is not open. Locate the appropriate templates. Double-click the template (You can also drag-and-drop or right-click the template and select Insert Template) and modify as needed. When finished entering text, you may (optional) right-click in the text area and select Check Spelling and Check Grammar. When complete, decide when you will sign the summary and choose the appropriate option. Click Add to Signature List (to place it with other orders or documents you need to sign for this patient). You can also click Save Without Signature or Sign Discharge Summary Now to sign the summary immediately.  
](#_Toc17877604)](#_Toc17877476)

[[Through CPRS, you can review lab test results in many formats. Based on user feedback, CPRS has made some changes to the Labs tab display, including adding two new reports, replacing one report, a new order for items in the Lab Results pane, and some changes to the display of the reports.](#_Toc17877604)](#_Toc17877476)

[[Two new items have been added:](#_Toc17877604)](#_Toc17877476)

- 
- 

[[The Lab Status report has been replaced by the Lab Orders (All) report.  
](#_Toc17877604)](#_Toc17877476)

[[With CPRS version 30.B, the order of reports in the Lab Results pane, where the users select which lab report they want to view, is different. The two new reports will be the top two items listed—unless your site has customized the order of the items.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Lab Overview (Collected Specimens) Note: The first item in the list could be different at your site. A new parameter enables sites to set which report they want to appear first in the list. This will also affect the data that displays when the user first goes to the Labs tab.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[Pending Lab Orders Most Recent All Tests by Date Selected Tests by Date Worksheet Graph Microbiology Anatomic Pathology – All Reports Blood Bank Lab Orders (All) Cumulative Note: Items in bold have changed order. The two new reports are the first two items in the list and Cumulative has moved to the bottom. Lab Orders (All) is new and replaces the Lab Status report.  
](#_Toc17877604)](#_Toc17877476)

[[To view lab test results, use these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[Select the Labs tab. In the Lab Results pane, select the type of results you want to see. For some selections, you must determine which test results you want to see. If the Select Lab Test dialog appears, you need to choose the tests you want to see.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

[[The Lab Order (Collected Specimens) report will show which Lab Order have been collected.](#_Toc17877604)](#_Toc17877476)

[[This report shows items that are pending so that healthcare givers will know what lab orders are pending so that others are not ordered.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 

[[The Collection Date/Time Test name Result/Status Flag (L for abnormal low, H for abnormal High, and each may have an asterisk (\*) if the result is critical) Units Reference range Additional information includes the specimen type, accession number, and the provider who ordered the lab test, the report release date and time, and the name of the lab performing the test.](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[The Worksheet is similar to the Selected Test by Date report. It does not display microbiology results, but it has many features for viewing lab results. It is very useful for displaying particular types of patterns of results.](#_Toc17877604)](#_Toc17877476)

[[Tests can be selected individually or by test groups. Any number of tests can be displayed. When selecting a panel test, such as CBC, the panel will be expanded to show the individual tests. Tests can be restricted to only display results for a specific specimen type. For example, displaying glucose results only on CSF can be accomplished by selecting the specimen CSF and then selecting the test Glucose.](#_Toc17877604)](#_Toc17877476)

[[Test groups allow you to combine tests in any manner. For example, a test group could combine CWBC, BUN, Creatinine, and Platelet count. You can save those test groups for later use. You can also select test groups that other users have created. You cannot exchange or delete other's test groups, only your own. Test groups are limited to seven tests, but you may have an unlimited number of test groups. To define your own test groups, select those tests you want and click the New button. If more than seven tests are selected, the New button will be disabled. If you want to delete a test group, deselect it and click the Delete button. If you want to replace an existing test group with other tests, select the test group, make any changes to the tests to be displayed and click the Replace button.  
](#_Toc17877604)](#_Toc17877476)

[[Selecting the Graph option brings up CPRS graphing in a separate window. For more information about graphing, please see CPRS Graphing.  
](#_Toc17877604)](#_Toc17877476)

[[These reports display only the results from these portions of the laboratory.](#_Toc17877604)](#_Toc17877476)

[[The Lab Order (All) report displays the status on current orders.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/546.png)](#_Toc17877604)](#_Toc17877476)

[[The View menu on the Labs tab is different from most of the other tabs in that the menu options do not sort or focus the listed items. The menu items are a way to open different windows and displays with information the clinician may need to see in conjunction with the lab results.](#_Toc17877604)](#_Toc17877476)

[[From the Labs tab, click View \| Reminders to display the Available Reminders dialog for the currently selected patient. The Available Reminders dialog allows you to review all reminders including the ones that apply to the currently selected patient.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/550.png)](#_Toc17877604)](#_Toc17877476)

[[A patient's available reminders are displayed on the Available Reminders dialog  
](#_Toc17877604)](#_Toc17877476)

[[To display a report, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[Select the Reports tab. See if the text on the Remote Data button is blue. If the text is blue, the patient has remote data. To view remote data, which may include Department of Defense data, click the Remote Data button to display a list of sites that have remote data for the selected patient. If you do not want remote data, skip to step 5. Select All if you want data from all the sites listed or click the check box in front of the site names you want to view remote data from and close the Remote Data button by clicking the button again. Note: If there is a problem getting the remote data, the following messages should give the user some feedback. For text reports only, CPRS adds a comment that describes the problem where the report would normally be. For 'grid' type reports, the error comment is put in the first column (after the facility name) of the report. Information is also included when the Remote Data button is used to display the list of sites that have data.](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
5.  

> [[\<No HDR Data Included\> - Use "HDR Reports" menu for HDR Data. \<No HDR Data\> - This site is not a source for HDR Data. \<No DoD Data\> - Use "Dept. of Defense Reports" Menu to retrieve data from DoD. \<ERROR\> - Unable to communicate with Remote siteSelect the report you want to view from the Available Reports box (click the "+" sign to expand a heading). Note: The next section, "Available Reports on the Reports Tab," lists the location of each report when they are exported. The list is configurable and your list may be different.](#_Toc17877604)](#_Toc17877476)

> [[Choosing a Department of Defense (DoD) report does not limit you to DoD data. For example, if you choose Microbiology under Dept. of Defense, you will get DoD data and remote VA data. You do not have to run a separate report to get VA data.](#_Toc17877604)](#_Toc17877476)

6.  

[[If necessary, select a date range from the Date Range box located in the lower left corner of the screen. The report should be displayed either after step 5 or step 6. You can then scroll through and read the report. If the report is in tabular form, click a row to reveal details about that row. (To select more than one row, press and hold the Control or Shift key.)](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/552.png)](#_Toc17877604)](#_Toc17877476)

[[The All Outpatient Medications report is displayed on the Reports tab  
](#_Toc17877604)](#_Toc17877476)

- - 
- - 
  - 
  - 
- - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
- - 

> [[Clinical Reports Allergies (can contain remote data from Department of Defense) Patient information Demographics Insurance DisabilitiesVisits / Admissions Adm./Discharge Expanded ADT (can contain remote data from Department of Defense) Discharge Diagnosis Discharges Future Clinic Visits Past Clinic Visits ICD Procedures ICD Surgeries Transfers Treating Specialty Comp & Pen Exams Dietetics Generic Diet Nutritional Status Supp. Feedings Tube Feeding Dietetics Profile Nutritional Assessment Discharge Summary (can contain remote data from Department of Defense) Laboratory Blood Availability Blood Transfusion Blood Bank Report Anatomic Pathology (can contain remote data from Department of Defense) Lab Orders (can contain remote data from Department of Defense) Chem & Hematology (can contain remote data from Department of Defense) Microbiology (can contain remote data from Department of Defense) Medicine/CP Abnormal Brief Report Full Captioned Full Report Procedures (local only) Procedures Orders Orders Current Daily Order Summary Order Summary for a Date Range Chart Copy Summary Outpatient Encounters / GAF Scores Education Education Latest Exam Latest GAF Scores Health Factors Immunizations Outpatient Diagnosis Outpatient Encounter Skin Tests Treatment Provided Pharmacy All Medications Note: The All Medications report includes All Inpatient and Outpatient Pharmacy data for a patient. The user can limit the data in the report by using date range parameters. To determine the data that is included, based on date range selection, the logic first looks for Last Fill Date, then Issue Date, then Order date (depends on if the date exists for the drug/RX being screened).](#_Toc17877604)](#_Toc17877476)

> [[The report is initially sorted by STATUS, beginning with Active, followed by Discontinued, followed by Expired (alphabetically within each of those three groups). Users can also sort the by selecting a column header, thus sorting by that column.](#_Toc17877604)](#_Toc17877476)

- 
- 

> [[Active OutpatientOutpatient Medications (can contain remote data from Department of Defense) Note: This report was previously called All Outpatient, but has been changed to Outpatient Medications because the user can now set a date range instead of getting all data for the patient. To determine the data that is included, based on date range selection, the logic first looks for Last Fill Date, then Issue Date, then Order date (depends on if the date exists for the drug/RX being screened).](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 

> [[Outpatient RX Profile Active IV All IV Unit Dose Med Admin History (BCMA) Med Admin Log (BCMA) Herbal/OTC/Non-VA Meds<span id="Womens_Health" class="anchor"></span>Women's Health: Potentially Unsafe Medications <span id="Active_meds_with_allergies" class="anchor"></span>Active Meds With AllergiesNote: The Active Meds With Allergies report displays all "Active" Pharmacy related Orders which have an interaction with an entered allergy for the patient.](#_Toc17877604)](#_Toc17877476)

- - 
  - 
  - 
- - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
- - 
  - 
  - 
- - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
- 
- 
- 
- - 
  - 
  - 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- - 
  - 

[[If a report is available in a table view, the table can be sorted alphabetically, numerically, or by date.](#_Toc17877604)](#_Toc17877476)

[[To sort data in a report table:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  

> [[Select the column heading you wish to sort by. The table will be sorted alphabetically (A-Z), numerically (0-9), or by date (most recent-least recent). If you click the column heading again, the table will be sorted in inverse order (Z-A, 9-0, or least recent-most recent). To perform a secondary sort, click another column heading. Note: If you hold the pointer over the table, a hover hint will appear with the criteria used to sort the table.](#_Toc17877604)](#_Toc17877476)

> [[Note: If the provider has an NPI, it will not display on the screen below.](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/554.png)](#_Toc17877604)](#_Toc17877476)

[[You can easily sort report data in a tabular view](#_Toc17877604)](#_Toc17877476)

[[  
](#_Toc17877604)](#_Toc17877476)

[[To copy data from a report, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  

> [[From the Reports tab, select the report you would like to copy data from. If the report is in text format, select the text you would like to copy and then right-click -or-](#_Toc17877604)](#_Toc17877476)

> [[if the report is in table format, click the row that contains the data you would like to copy (to select more than one row, press and hold either the Shift or Control key). After you have selected the appropriate rows, right click the area or row you have selected.](#_Toc17877604)](#_Toc17877476)

3.  
4.  

[[Select Copy (text format) or Copy Data From Table (table format). You can now paste the data into another area in CPRS or into another program. ![](cprs-user-manual-gui-version-updated-or-3-0-499/556.png)](#_Toc17877604)](#_Toc17877476)

[[You can copy data from a report by right-clicking and selecting Copy](#_Toc17877604)](#_Toc17877476)

[[Health Summaries provide important information to users about a patient's condition. With Remote Data Views (RDV), users may be able to access remote Health Summary information from other facilities or the Department of Defense (DoD). If the patient has DoD data, but it is not available, CPRS will provide feedback for the text or grid type reports.](#_Toc17877604)](#_Toc17877476)

[[CPRS adds a comment that describes the problem where the data from the remote report would normally be. For 'grid' type reports, the error comment is put in the first column (after the facility name) of the report. Here are some examples of the comments that could show up, depending on the type of query and what the user has selected:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 

[[\<No HDR Data Included\> - Use "HDR Reports" menu for HDR Data. \<No HDR Data\> This site is not a source for HDR Data. \<No DoD Data\> - Use "Dept. of Defense Reports" Menu to retrieve data from DoD. \<ERROR\> - Unable to communicate with Remote site In addition to this text, error messages will also be shown after each remote site listed under the (blue) Remote Data View button, when appropriate.](#_Toc17877604)](#_Toc17877476)

[[To display a Health Summary, follow these steps:](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  

[[Select a patient after you enter the CPRS system. Select the Reports tab. Under the Available Reports box on the left side of the screen, click the "+" sign in order to expand the Health Summary heading. Select a Health Summary by clicking on the summary that you would like to see. After you have selected a summary, the appropriate data is displayed on the right side of the screen. Use the scroll bar on the right to scroll through the different sections of the Health Summary.  
](#_Toc17877604)](#_Toc17877476)

[[This appendix discusses the features of CPRS that allow people who are blind, who have limited vision, or who have limited dexterity to use the software effectively. The features discussed include changing the font and window sizes, changing the background color, configuring a screen reader, and keyboard equivalents for common CPRS commands.](#_Toc17877604)](#_Toc17877476)

[[CPRS supports 8, 10, 12, 14, and 18 point font sizes. Font sizes larger than 18 point, make CPRS difficult for the user to navigate. If the user requires font sizes larger than 18 point, then the use of font magnification software, such as Windows Magnifier or other similar tools is recommended.](#_Toc17877604)](#_Toc17877476)

[[Changing the size of the fonts used in CPRS is a two-step process. The instructions in "<u>CPRS Windows and Dialog Boxes</u>" will change the size of most of the fonts displayed in CPRS windows and dialog boxes. However, to change the font size used for CPRS menus and Windows alert boxes, you will also need to follow the steps in "<u>CPRS Menus and Windows Alert boxes.</u>"](#_Toc17877604)](#_Toc17877476)

[[You can adjust the font size for most windows and dialog boxes that appear in CPRS. If you change the font size, some screen components will be resized to fit the new font size. If this occurs, you will need to manually resize some dialog boxes and screen components. CPRS will save the dimensions for the resized components so you will only have to resize them once.](#_Toc17877604)](#_Toc17877476)

[[To change the font size for CPRS windows and dialog boxes, follow these steps:](#_Toc17877604)](#_Toc17877476)

> [[1. Select Edit \| Preferences \| Fonts and choose the appropriate font size. The font size will be changed.](#_Toc17877604)](#_Toc17877476)

> [[Note: The menu fonts and alert box fonts will not be changed until you follow the steps in <u>CPRS Menus and Windows Alert boxes</u> (below).](#_Toc17877604)](#_Toc17877476)

[[To change the font size used for CPRS menus and Windows alert boxes, follow these steps:](#_Toc17877604)](#_Toc17877476)

[[Note: The steps below will change the font used in menus and Windows boxes for ALL of the applications on your computer.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  

> [[Click Start \| Settings \| Control Panel. Double-click on the Display icon.  
> Click the Appearance tab. ![](cprs-user-manual-gui-version-updated-or-3-0-499/557.png)](#_Toc17877604)](#_Toc17877476)

4.  
5.  
6.  
7.  
8.  
9.  
10. 

[[To change the background color of CPRS windows and dialog boxes, follow these steps:](#_Toc17877604)](#_Toc17877476)

[[Note: The steps below will change the background color of windows and dialog boxes for ALL applications on your computer.](#_Toc17877604)](#_Toc17877476)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

> [[Click Start \| Settings \| Control Panel. Double-click on the Display icon. The *Display Properties* dialog box will appear. Click the Appearance tab. From the Item drop-down list box, select Window. Select a color from the Color drop-down list box.  
> Click Apply. ![](cprs-user-manual-gui-version-updated-or-3-0-499/558.png)](#_Toc17877604)](#_Toc17877476)

8.  
9.  
10. 

> [[The Appearance tab of the Display Properties dialog box If necessary, repeat steps 4-6 to change the display settings for another item. Press OK.![](cprs-user-manual-gui-version-updated-or-3-0-499/559.png) In this example, the Window color has been changed to a high contrast selection  
> ](#_Toc17877604)](#_Toc17877476)

[[![](cprs-user-manual-gui-version-updated-or-3-0-499/560.png)  
](#_Toc17877604)](#_Toc17877476)

[[Contents Alt-H-C](#_Toc17877604)](#_Toc17877476)

[[About CPRS Alt-H-A](#_Toc17877604)](#_Toc17877476)

[[Details Alt-V-D](#_Toc17877604)](#_Toc17877476)

[[Administration History Alt-V-H](#_Toc17877604)](#_Toc17877476)

[[Save as Quick Order Alt-O-S](#_Toc17877604)](#_Toc17877476)

[[Edit Common List Alt-O-E](#_Toc17877604)](#_Toc17877476)

[[<span id="_Toc126154851" class="anchor"></span>  
](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 

[[For JAWS and CPRS to work together, it is best to launch JAWS first before launching CPRS. If JAWS has been closed for a while, but CPRS has remained open, it would be best to shut down CPRS, start JAWS and then relaunch CPRS. Starting JAWS first will help ensure that the two applications communicate correctly.](#_Toc17877604)](#_Toc17877476)

[[Also, to run JAWS, the user must have administrative rights on the workstation JAWS will be used on.  
](#_Toc17877604)](#_Toc17877476)

[[This section includes general information regarding signing outpatient controlled substance orders for the Electronic Prescribing of Controlled Substance features (ePCS), errors the user might see, and some possible causes.](#_Toc17877604)](#_Toc17877476)

[[Possible hardware problems:](#_Toc17877604)](#_Toc17877476)

- 
- 

[[The card reader is not working. To check, try the user's card in another workstation's card reader.The card is damaged or broken. To check, insert the card into a reader that you know works.What does a user need in order to be able to digitally sign outpatient controlled substances prescriptions?](#_Toc17877604)](#_Toc17877476)

[[Providers must have the following to be able to prescribe outpatient controlled substance medication orders:](#_Toc17877604)](#_Toc17877476)

- 
- 
- 
- 
- 
- 
- 
- 
- 

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 45%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><a href="#_Toc17877476"><span><strong>Error Message</strong></span></a></th>
<th><a href="#_Toc17877476"><span><strong>Cause</strong></span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc17877476"><span>1.</span></a></td>
<td><a href="#_Toc17877476"><span>Order for controlled substance could not be completed. Provider does not have a current, valid DEA# on record and is ineligible to sign the order.</span></a></td>
<td><p><a href="#_Toc17877476"><span>There is no DEA Number in file 200 for this provider, or this provider does not have a VA#, or this provider's VA# could not be used because either the facility DEA number is expired, or the provider is not a VA provider (only VA providers may use VA numbers). Contact your CAC or support person who can check on this for you.</span></a></p>
<p><a href="#_Toc17877476"><span><strong>Note: With patch OR*3*499, a provider must have a DEA number in the NEW DEA#'s multiple field to order controlled substances. DEA numbers in the obsolete DEA NUMBER field are ignored.</strong></span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>2.</span></a></td>
<td><p><a href="#_Toc17877476"><span>Order for controlled substance could not be completed.</span></a></p>
<p><a href="#_Toc17877476"><span>Provider is not authorized to prescribe medications in Federal Schedule X [X is one of 2, 2N, 3, 3N, 4, or 5].</span></a></p></td>
<td><p><a href="#_Toc17877476"><span>In the provider's ePCS set up, they have not been assigned permission to write for the specified schedule. Your CAC should know who is responsible for assigning the schedules.</span></a></p>
<p><a href="#_Toc17877476"><span>If a provider is using their individual DEA number, the schedules associated with the DEA number in the DEA NUMBERS file (#8991.9) are used to determine privileges. If using VA# or an institutional DEA number to order controlled substances, the provider's personal schedules in file 200 are used to determine permissions.</span></a></p>
<p><a href="#_Toc17877476"><span><strong>Note: With patch OR*3*499, if a provider has more than one DEA number, the error message specifically applies to the DEA number flagged 'Use for Inpatient Orders' in the DEA NUMBERS file (#8991.9).</strong></span></a></p></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>3.</span></a></td>
<td><p><a href="#_Toc17877476"><span>Order for controlled substance could not be completed.</span></a></p>
<p><a href="#_Toc17877476"><span>Provider does not have a valid Detoxification/Maintenance ID number on record and is ineligible to sign the order.</span></a></p></td>
<td><p><a href="#_Toc17877476"><span>The provider does not have a Detoxification/Maintenance number in file 200 or there is a problem with it. Contact your ADPAC or CAC to find out who enters credentialing information through the Data Entry for ePrescribing Controlled Substances application to get this corrected.</span></a></p>
<p><a href="#_Toc17877476"><span><strong>Note: With patch OR*3*499, if a provider has more than one DEA number, the error message specifically applies to the DEA number flagged 'Use for Inpatient Orders' in the DEA NUMBERS file (#8991.9).</strong></span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>4.</span></a></td>
<td><p><a href="#_Toc17877476"><span>Order for controlled substance could not be completed.</span></a></p>
<p><a href="#_Toc17877476"><span>Provider's DEA# expired on DATE [ex:JAN 01, 2012] and no VA# is assigned. Provider is ineligible to sign the order.</span></a></p></td>
<td><p><a href="#_Toc17877476"><span>The text is clear. The provider's DEA number has expired and the provider does not have a VA number. Contact your ADPAC or CAC to find out who enters credentialing information through the Data Entry for ePrescribing Controlled Substances application to get this corrected.</span></a></p>
<p><a href="#_Toc17877476"><span><strong>Note: With patch OR*3*499, if a provider has more than one DEA number, the error message specifically applies to the DEA number flagged 'Use for Inpatient Orders' in the DEA NUMBERS file (#8991.9).</strong></span></a></p></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>5.</span></a></td>
<td><p><a href="#_Toc17877476"><span>Order for controlled substance could not be completed.</span></a></p>
<p><a href="#_Toc17877476"><span>Provider's Detoxification/Maintenance ID number expired due to an expired DEA# on DATE [ex: JAN 01, 2012].</span></a></p>
<p><a href="#_Toc17877476"><span>Provider is ineligible to sign the order.</span></a></p></td>
<td><p><a href="#_Toc17877476"><span>Again, the error text gives a good explanation. The provider has a valid Detoxification/Maintenance number, but because the user's DEA number has expired, the Detox/Maintenance number cannot be used. Contact your ADPAC or CAC to find out who enters credentialing through the Data Entry for ePrescribing Controlled Substances application to get this corrected.</span></a></p>
<p><a href="#_Toc17877476"><span><strong>Note: With patch OR*3*499, if a provider has more than one DEA number, the error message specifically applies to the DEA number flagged 'Use for Inpatient Orders' in the DEA NUMBERS file (#8991.9).</strong></span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>6.</span></a></td>
<td><p><a href="#_Toc17877476"><span>Digital Signing of Controlled</span></a></p>
<p><a href="#_Toc17877476"><span>Substances is currently disabled for your site.</span></a></p></td>
<td><a href="#_Toc17877476"><span>The prescriber tries to sign and the ePCS switch (OR EPCS SITE PARAMETER) is disabled for the site.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>7.</span></a></td>
<td><a href="#_Toc17877476"><span>You are not currently permitted to digitally sign Controlled Substances.</span></a></td>
<td><a href="#_Toc17877476"><span>The prescriber tries to sign and the ePCS switch (OR EPCS USERS PARAMETER) is disabled for the signer.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>8.</span></a></td>
<td><a href="#_Toc17877476"><span>Problem getting PIN. Cannot Digitally Sign.</span></a></td>
<td><a href="#_Toc17877476"><span>There are issues reading the PIV or smart card/retrieving the PIN. Contact your CAC or ADPAC for assistance.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>9.</span></a></td>
<td><a href="#_Toc17877476"><span>Card has been locked. Cannot Digitally Sign.</span></a></td>
<td><p><a href="#_Toc17877476"><span>The card is locked in CPRS after 3 failed attempts at PIV PIN entry. This error occurs when the user attempts to sign while the card is locked. It will be automatically unlocked after 15 minutes.</span></a></p>
<p><a href="#_Toc17877476"><span><strong>Warning:</strong> Be careful! 5 consecutive incorrect PIN entry attempts will lock the card and you will have to go to your PIV office station to reinstate or create a new card!</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>10.</span></a></td>
<td><a href="#_Toc17877476"><span>Digital Signing has been cancelled.</span></a></td>
<td><a href="#_Toc17877476"><span>The digital signature process has been cancelled by CPRS. This error usually shows after another problem has occurred.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>11.</span></a></td>
<td><a href="#_Toc17877476"><span>Could not digitally sign. An error has occurred: Hash generation failed.</span></a></td>
<td><a href="#_Toc17877476"><span>The system has issues creating the hash. The hash is created using the data from the order and a specific value. This process is repeated in Pharmacy during finishing and the hash values are compared to see if anything has been changed.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>12.</span></a></td>
<td><a href="#_Toc17877476"><span>Please verify that you are logged on to the CPRS system and that your PIV card is inserted. There is a possible mismatch between your VistA last name and the last name of the certificate on your card. If it matches and you are still experiencing issues, please contact your card issuer for assistance.</span></a></td>
<td><p><a href="#_Toc17877476"><span>When a user tries to link his/her PIV card to another VistA user logged into CPRS, a series of error messages will appear after PIN entry</span></a></p>
<p><a href="#_Toc17877476"><span>Contact your CAC or ADPAC for assistance.</span></a></p></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>13.</span></a></td>
<td><a href="#_Toc17877476"><span>CPRS was not able to link your VistA account to a PIV card.</span></a></td>
<td><p><a href="#_Toc17877476"><span>When a user tries to link his/her PIV card to another VistA user logged into CPRS, a series of error messages will appear after</span></a></p>
<p><a href="#_Toc17877476"><span>PIN entry</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>14.</span></a></td>
<td><a href="#_Toc17877476"><span>89802006^Smart Card Reader not found</span></a></td>
<td><a href="#_Toc17877476"><span>As stated, the card reader was not found. Contact your local IRM shop.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>15.</span></a></td>
<td><a href="#_Toc17877476"><span>Problems with verifying certificate chain of authority</span></a></td>
<td><p><a href="#_Toc17877476"><span>Network problems connecting to the verifying servers Tumbleweed may not be installed on the PKI Verify Server machine or the workstation or is not installed correctly.</span></a></p>
<p><a href="#_Toc17877476"><span>Contact your CAC or ADPAC for assistance.</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>16.</span></a></td>
<td><a href="#_Toc17877476"><span>Valid Certificate not found</span></a></td>
<td><a href="#_Toc17877476"><span>No valid certificate to use was found on the card. Contact your CAC or ADPAC for assistance.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>17.</span></a></td>
<td><a href="#_Toc17877476"><span>Returned from CertSignData with failure</span></a></td>
<td><a href="#_Toc17877476"><span>Obtained a valid certificate, but failed to sign data correctly. Contact your CAC or ADPAC for assistance.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>18.</span></a></td>
<td><p><a href="#_Toc17877476"><span>Certificate not valid:</span></a></p>
<p><a href="#_Toc17877476"><span>89802019^Before Cert effective date.</span></a></p></td>
<td><a href="#_Toc17877476"><span>The current date when the user tries to sign is before the certificate's effective date. Contact your CAC or ADPAC for assistance.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>19.</span></a></td>
<td><p><a href="#_Toc17877476"><span>Certificate not valid:</span></a></p>
<p><a href="#_Toc17877476"><span>89802020^Certificate expired.</span></a></p></td>
<td><p><a href="#_Toc17877476"><span>The certificate on the card has expired.</span></a></p>
<p><a href="#_Toc17877476"><span>The PIV card needs to be renewed.</span></a></p>
<p><a href="#_Toc17877476"><span>Contact your PIV office.</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>20.</span></a></td>
<td><a href="#_Toc17877476"><span>Could not acquire context Last Error value was "specific message for the error"</span></a></td>
<td><a href="#_Toc17877476"><span>Often means that the ActivClient on that machine needs to be reinstalled. First, the user should try to digitally sign from another workstation, and if that works, then it is probably ActivClient or the card reader hardware.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>21.</span></a></td>
<td><a href="#_Toc17877476"><span>Invalid PIN entry - You only have ## attempts left before it is locked.</span></a></td>
<td><p><a href="#_Toc17877476"><span>This error message displays when the user enters an incorrect PIN one or two times. The message tells the user how many times another incorrect PIN can be entered before CPRS locks ordering for the card. The order will be left unsigned.</span></a></p>
<p><a href="#_Toc17877476"><span>Warning! If a user incorrectly enters the PIN 5 consecutive times, the card will be completely locked and will require the full PIV station to reinstate or create a new card!</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>22.</span></a></td>
<td><a href="#_Toc17877476"><span>That was three (3) unsuccessful tries, the Card Reader is Locked</span></a></td>
<td><p><a href="#_Toc17877476"><span>The user entered an incorrect PIN three consecutive times. CPRS locks access to the card. The order will be left unsigned.</span></a></p>
<p><a href="#_Toc17877476"><span><strong>Warning!</strong> If a user incorrectly enters the PIN 5 consecutive times, the card will be completely locked and will require the full PIV station to reinstate or create a new card!</span></a></p></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>23.</span></a></td>
<td><a href="#_Toc17877476"><span>PIN Entry was cancelled</span></a></td>
<td><a href="#_Toc17877476"><span>The user cancelled PIN entry and stopped the digital signature process. The order will be left unsigned.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>24.</span></a></td>
<td><a href="#_Toc17877476"><span>Unable to read the information from your card. Possible mismatch between your VistA last name and the last name of the certificate on your card.</span></a></td>
<td><p><a href="#_Toc17877476"><span>No matching certificate found when trying to get the SAN from the PIV card to link.</span></a></p>
<p><a href="#_Toc17877476"><span>Contact your CAC or ADPAC for assistance.</span></a></p></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>25.</span></a></td>
<td><a href="#_Toc17877476"><span>Revocation failed - error: "specific text for the error"</span></a></td>
<td><p><a href="#_Toc17877476"><span>The revocation server that checks to see if a certificate has been revoked or expired couldn't be reached over the network.</span></a></p>
<p><a href="#_Toc17877476"><span>Contact your CAC or ADPAC for assistance.</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>26.</span></a></td>
<td><a href="#_Toc17877476"><span>Could not open the Cert Store</span></a></td>
<td><p><a href="#_Toc17877476"><span>This appears to be a problem with ActivClient. Please check ActivClient and reinstall if necessary.</span></a></p>
<p><a href="#_Toc17877476"><span>Contact your CAC or ADPAC for assistance.</span></a></p></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>27.</span></a></td>
<td><a href="#_Toc17877476"><span>Did not find a Cert</span></a></td>
<td><p><a href="#_Toc17877476"><span>This error comes from other programs outside of CPRS. The cause may not be as easily determined as other errors.</span></a></p>
<p><a href="#_Toc17877476"><span>Contact your CAC or ADPAC for assistance.</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>28.</span></a></td>
<td><a href="#_Toc17877476"><span>89802010^Signature Error – "specific text for the error"</span></a></td>
<td><a href="#_Toc17877476"><span>This error comes from other programs outside of CPRS. The cause may not be as easily determined as other errors.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>29.</span></a></td>
<td><a href="#_Toc17877476"><span>89802009^Signature Check failed</span></a></td>
<td><p><a href="#_Toc17877476"><span>This error comes from other programs outside of CPRS. The cause may not be as easily determined as other errors.</span></a></p>
<p><a href="#_Toc17877476"><span>Contact your CAC or ADPAC for assistance.</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc17877476"><span>30.</span></a></td>
<td><p><a href="#_Toc17877476"><span>Digital signature verification failed:</span></a></p>
<p><a href="#_Toc17877476"><span>"specific text for the error"</span></a></p></td>
<td><p><a href="#_Toc17877476"><span>This error comes from other programs outside of CPRS. The cause may not be as easily determined as other errors.</span></a></p>
<p><a href="#_Toc17877476"><span>Contact your CAC or ADPAC for assistance.</span></a></p></td>
</tr>
<tr class="odd">
<td><a href="#_Toc17877476"><span>31.</span></a></td>
<td><a href="#_Toc17877476"><span>Keyset error</span></a></td>
<td><p><a href="#_Toc17877476"><span>This error appears to relate a bad SAN being stored for the user.</span></a></p>
<p><a href="#_Toc17877476"><span>Contact your CAC or ADPAC for assistance.</span></a></p></td>
</tr>
</tbody>
</table>

[[  
](#_Toc17877604)](#_Toc17877476)