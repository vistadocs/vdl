---
title: MPI/PD Version 1 VISTA User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: VISTA
app_code: MPIF
app_name: Master Patient Index
section: INF
app_status: active
pkg_ns: MPIF
patch_ver: 1
patch_id: MPIF*1
group_key: "MPIF:MPIF:1"
file_numbers: 
  - 985
  - 991
security_keys: []
menu_options: 35
description: 
audience: 
keywords: 
  - patient
  - strong
  - class
  - view
  - primary
  - blockquote
  - identity
  - person
  - colspan
  - even
page_count: 0
word_count: 55295
section_count: 9
table_count: 149
figure_count: 0
appendix_count: 6
has_toc: False
is_stub: False
pub_date: April 1999
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index_(MPI)/rg1_0_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index_(MPI)/rg1_0_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=16"
---

---
title: |
  Master Patient Index  
  Patient Demographics (MPI/PD)

  Version 1.0

  User Manual
---

![](mpi-pd-version-1-vista-user-manual/001.png)

April 1999

Office of Information and Technology (OI&T)

Revision History

<span id="_Toc247320305" class="anchor"></span>Table ‑. Documentation Revision History

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 68%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/2018</td>
<td><p>Documentation updates are listed by patch designation and RTC Story.</p>
<p>Software enhancements for this release comprise Patch MPI*1.0*123/Story #782858 (VETS360).</p>
<p>Field, EMAIL ADDRESS (#36.1), added to the following tables:</p>
<ul>
<li><p>“Table 3‑1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)”</p></li>
<li><p>“Table E-1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)”</p></li>
</ul></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>4/2018</td>
<td>Corrected references to Self Identified Gender identity in MPI-PD VistA Manuals and HC IdM Manuals based on feedback from the VA Lesbian, Gay, Bisexual, and Transgender (LGBT) Health Program.</td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>1/2018</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story.</p>
<p>Software enhancements for this release comprise companion VistA Patches RG*1.0*69 and DG*5.3*950/RTC Story #603957 (Relabel of Gender to Birth Sex) and other updates as requested:</p>
<p>The following figures were relabeled:</p>
<ul>
<li><p>Figure 5‑10. Patient MPI/PD Data Inquiry─Example of inquiry showing patient with Self-Identified Gender Identity and Period of Service displayed</p></li>
<li><p>Figure 5‑11. Patient MPI/PD Data Inquiry─Example of inquiry showing patient with an SSN Verification Status: Verified</p></li>
<li><p>Figure 5‑12. Patient MPI/PD Data Inquiry—Partial example of inquiry showing patient with pseudo SSN</p></li>
<li><p>Figure 5‑13. Patient MPI/PD Data Inquiry—Partial example showing Bad Address Indicator data</p></li>
<li><p>Figure 5‑14. Patient MPI/PD Data Inquiry—Foreign address fields</p></li>
<li><p>Figure 5‑16. Display Remote Patient Data Query—Foreign address fields</p></li>
<li><p>Figure 5‑17. DoD Identifiers Populated for a Patient Display in the Patient MPI/PD Data Inquiry Option</p></li>
<li><p>Figure 5‑19. DoD Identifiers are Displayed from the Remote Query Sent to Selected Treating Facility</p></li>
<li><p>Figure 5‑23. Display Remote Patient Data Query</p></li>
<li><p>Figure 5‑24. Display Remote Patient Data Query—Partial example query showing person with pseudo SSN</p></li>
<li><p>Figure 5‑25. Display Only Query when person exists in PATIENT File (#2)</p></li>
<li><p>Figure 5‑26. Display Only Query when person does not exist in PATIENT file (#2)</p></li>
<li><p>Figure 5‑27. Display Only Query with an Open Data Management Case</p></li>
<li><p>Figure 5‑28. Primary View Display from MPI [RG PRIMARY VIEW FROM MPI] option.</p></li>
</ul>
<p>Reference CA #R17575307FY18. Changed the default response from YES to NO for the Issue REQUEST FOR RECORDS? prompt in “Figure 7‑5. Register a Patient- Add new person, and connect to MVI for first time.”</p></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>10/2017</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story.</p>
<p>Software enhancements for this release comprise companion VistA Patch DG*5.3*944/RTC <u>Story 504382</u> (<u>Sub-Story: 513042</u>): “Add new fields (POB Country and POB Province [not Person Type]) to the PATIENT file, Add trigger to the new fields in the PATIENT file, Enable Auditing on fields in PATIENT file (#2) new fields”</p>
<ul>
<li><p>Added the following new fields to “Table 3‑1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)” and “Table E-1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file):”</p></li>
</ul>
<ul>
<li><blockquote>
<p>PLACE OF BIRTH COUNTRY (#9.1)</p>
</blockquote></li>
<li><blockquote>
<p>PLACE OF BIRTH PROVINCE (#9.2)</p>
</blockquote></li>
<li><blockquote>
<p>PERSON TYPE (#150)</p>
</blockquote></li>
<li><blockquote>
<p>PERSON TYPE (#.054, .01)</p>
</blockquote></li>
</ul>
<ul>
<li><p>Updated screen shot in “Figure 5‑7. Patient Audit File Print for selected fields” to reflect new fields being audited.</p></li>
<li><p>Added the following new fields to “Table 6‑1. Data elements monitored in the PATIENT file (#2) for changes:”</p></li>
</ul>
<ul>
<li><blockquote>
<p>PLACE OF BIRTH COUNTRY (#2,.0931)</p>
</blockquote></li>
<li><blockquote>
<p>PLACE OF BIRTH PROVINCE (#2,.0932)</p>
</blockquote></li>
</ul></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>5/2017</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story.</p>
<p>Software enhancements for this release comprise companion VistA Patches DG*5.3*937, RG*1.0*67 and MPIF*1.0*65.</p>
<p>RTC Story 445457/Sub-Stories:</p>
<ul>
<li><blockquote>
<p>455445: “Add new field at the Primary View level #985, Enable audit on new field at the Primary View level #985.”</p>
</blockquote></li>
</ul>
<blockquote>
<p>The following fields have been added to the Primary View of the MPI (see “Table 3‑1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)” and “Table E-1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)”:</p>
</blockquote>
<ul>
<li><blockquote>
<p>DEATH STATUS (#118)</p>
</blockquote></li>
<li><blockquote>
<p>PREFERRED NAME (#300)</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>455414: “Add new field to the PATIENT file, Add trigger to the new field in the PATIENT file, Enable Auditing on field in PATIENT file (#2) new field.”</p>
</blockquote></li>
</ul>
<blockquote>
<p>The following new fields have been added to the PATIENT (#2) file and are utilized by the MPI. (See “Table 6‑1. Data elements monitored in the PATIENT file (#2) for changes”):</p>
</blockquote>
<ul>
<li><blockquote>
<p>PREFERRED NAME (#.2405)</p>
</blockquote></li>
<li><blockquote>
<p>SUPPORTING DOCUMENT TYPE (#.357)</p>
</blockquote></li>
</ul>
<p>Story 455449: “Add new field to PDAT display on VistA.”</p>
<ul>
<li><blockquote>
<p>Added the PREFERRED NAME field (#300) to the display in the MPI/PD Patient Data option. (See “Figure 5‑10. Patient MPI/PD Data Inquiry─Example of inquiry showing patient with Self-Identified Gender Identity and Period of Service displayed.”)</p>
</blockquote></li>
</ul></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>12/2016</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story. Software enhancements for this release comprise companion VistA Patches DG*5.3*926, MPIF*1.0*64 and RG*1.0*65.</p>
<p>Patch DG*5.3*926 documentation updates:</p>
<p>RTC Story 323008: Enhance VistA Source of Notification field in the PATIENT file (#2):</p>
<ul>
<li><blockquote>
<p>The following fields were added to “Table 3‑1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)” and “Table E-1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)” ), stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file):</p>
</blockquote></li>
</ul>
<ul>
<li><p>SSA VERIFICATION STATUS (#108)</p></li>
<li><p>ID INTEROPERABLTY PERSON TYPE (#109)</p></li>
<li><p>LEVEL OF ASSURANCE (#110)</p></li>
<li><p>DEATH INDICATOR (Y/N)? (#111)</p></li>
<li><p>NOTIFICATION PROVIDER (#113)</p></li>
<li><p>SUPPORTING DOCUMENT TYPE (#114)</p></li>
<li><p>DATE OF DEATH OPTION USED (#115)</p></li>
<li><p>DISCHARGED DATE/TIME (#116)</p></li>
<li><p>DATE OF DEATH OVERRIDE REASON (#117)</p></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>12/2015</td>
<td>Patch DG*5.3*915 documentation update, only. Updated glossary entry for Registration Process.</td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>9/2015</td>
<td><p>Patch RG*1.0*62 documentation updates:</p>
<ul>
<li><p>Healthcare Identity Management (HC IdM) has requested the removal/deletion of Primary View Rejects (PVRs) and PVR functionality:</p></li>
</ul>
<ul>
<li><blockquote>
<p>Exception #234 (Primary View Reject) are no longer being logged.</p>
</blockquote></li>
<li><blockquote>
<p>A post-init process executed and marked all existing unresolved 234 exceptions as Resolved.</p>
</blockquote></li>
<li><blockquote>
<p>The menu option MPI/PD Exception Handling [RG EXCEPTION HANDLING] was removed, since it is no longer needed.</p>
</blockquote></li>
<li><blockquote>
<p>Removed “Appendix C: Exceptions and Bulletins.” All subsequent appendices were moved up.</p>
</blockquote></li>
</ul>
<ul>
<li><p>New option and associated RPC:</p>
<ul>
<li><blockquote>
<p>A new option named ToolKit POC User Setup [RG TK POC USER SETUP] was created and placed on the MPI/PD Patient Admin Coordinator Menu [RG ADMIN COORD MENU] to set up Visitor Records on the MPI to support POC (Point of Contact) remote view access.</p>
</blockquote></li>
<li><blockquote>
<p>This new option calls a new RPC named MPI TK POC USER SETUP, which will access the MPI to establish a Visitor Record in the NEW PERSON file (#200).</p>
</blockquote></li>
</ul></li>
</ul>
<ul>
<li><blockquote>
<p>In support of the new Date of Death (DOD) requirements to the MPI, the following fields from the PATIENT (#2) file will be added to the OBX message segment of the ADT-A08 HL7 message (See “Table 6‑1. Data elements monitored in the PATIENT file (#2) for changes.”):</p>
</blockquote></li>
</ul>
<ul>
<li><p>DEATH ENTERED BY (#.352)</p></li>
<li><p>SOURCE OF NOTIFICATION (#.353)</p></li>
<li><p>DATE OF DEATH LAST UPDATED (#.354)</p></li>
<li><p>LAST EDITED BY (#.355)</p></li>
</ul>
<p>These fields have been enabled for auditing.</p>
<p>Patch DG*5.3*902 documentation updates:</p>
<ul>
<li><blockquote>
<p>The menu text display for the field named SELF-IDENTIFIED GENDER was changed to “Self-Identified Gender Identity” in the following MPI/PD options:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Patient MPI/PD Data Inquiry</p>
</blockquote></li>
<li><blockquote>
<p>Remote Patient Data Query Menu ...</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>The following new fields have been added to the PATIENT (#2) file and are utilized by the MPI. (See “Table 6‑1. Data elements monitored in the PATIENT file (#2) for changes.”):</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>FULL ICN (#991.1)</p>
</blockquote></li>
<li><blockquote>
<p>FULL ICN HISTORY (#991.91)</p>
</blockquote></li>
</ul>
<blockquote>
<p>Both fields contain the complete Integration Control Number (ICN) value, which includes the Identifier, Delimiter, Checksum, and optional Encryption Scheme.</p>
</blockquote>
<ul>
<li><blockquote>
<p>The following fields have been added to the Primary View of the MPI (see “Table 3‑1. Primary View Identity Traits” and “<a href="#Table_E1">Table E-1. Primary View Identity Traits</a>.”) and are stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file):</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>IDENTITY THEFT ACTIVATION (#102)</p>
</blockquote></li>
<li><blockquote>
<p>IDENTITY THEFT DEACTIVATION (#103)</p>
</blockquote></li>
<li><blockquote>
<p>DEATH ENTERED BY (#104)</p>
</blockquote></li>
<li><blockquote>
<p>SOURCE OF NOTIFICATION (#105)</p>
</blockquote></li>
<li><blockquote>
<p>DATE OF DEATH LAST UPDATED (#106)</p>
</blockquote></li>
<li><blockquote>
<p>DEATH LAST EDITED BY (#107)</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Additional changes for Increment 13:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Updated Index and Glossary.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>10/2014</td>
<td><p>Documentation updates:</p>
<p>Patch DG*5.3*876:</p>
<ul>
<li><p>The following field was added to the VistA PATIENT file (#2). This field specifies the patient’s self-identified gender identity.</p>
<ul>
<li><blockquote>
<p>SELF IDENTIFIED GENDER (#.024)</p>
</blockquote></li>
</ul></li>
</ul>
<p>Prompt Message:  Select the code that specifies the patient's preferred gender.</p>
<ul>
<li><p>Note: New field has been turned on for auditing in the PATIENT file (#2) for MPI/PD.</p></li>
<li><blockquote>
<p>The following VistA PATIENT file (#2) fields were added to the Patient MPI/PD Data Inquiry option [RG EXCEPTION TF INQUIRY] so that if they exist, will be viewable upon execution: </p>
</blockquote>
<ul>
<li><blockquote>
<p>SELF IDENTIFIED GENDER (#.024)</p>
</blockquote></li>
<li><blockquote>
<p>PERIOD OF SERVICE (#.323).</p>
</blockquote></li>
</ul></li>
<li><blockquote>
<p>The following new fields on the MPI: PATIENT TYPE (#391) and VETERAN Y/N (#1901) were already being displayed on the extended data screen on the local Vista PDAT.</p>
</blockquote>
<ul>
<li><blockquote>
<p>TYPE (#391)</p>
</blockquote></li>
<li><blockquote>
<p>VETERAN (Y/N)? (#1901)</p>
</blockquote></li>
</ul></li>
</ul>
<p>Patch RG*1.0*61:</p>
<ul>
<li><p>The Add/Edit Point of Contact [RG UPDATE POINT OF CONTACT] option was removed from the CORD MPI/PD Patient Admin Coordinator Menu [RG ADMIN COORD MENU] and placed out-of-order as part of the MVI Increment 12 release.</p></li>
</ul>
<p>Additional changes for Increment 12:</p>
<ul>
<li><blockquote>
<p>HC IdM recommended changes to name references: 1) MPI to MVI (where appropriate) and 2) Patient to Person (where appropriate).</p>
</blockquote>
<ul>
<li><blockquote>
<p>The term “Patient” is used when the reference is to VistA PATIENT file (#2). The “MPI” nomenclature is used to display these test data occurrences because the MPI component of the MVI interacts with the PATIENT file (#2). </p>
</blockquote></li>
<li><blockquote>
<p>All other references are made to “Person” and to the MVI (which overall includes the MPI, PSIM, and TK).</p>
</blockquote></li>
</ul></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>7/2013</td>
<td><p>Documentation updates:</p>
<p>Patch DG*5.3*863:</p>
<ul>
<li><blockquote>
<p>When a patient's current residential address is located in a foreign country (e.g., for a Department of Defense (DoD) patient) the following foreign address fields, from the VistA PATIENT file (#2), are displayed in the Patient MPI/PD Data Inquiry and Display Remote Patient Data Query options:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>PROVINCE field #.1171</p>
</blockquote></li>
<li><blockquote>
<p>POSTAL CODE field #.1172</p>
</blockquote></li>
<li><blockquote>
<p>COUNTRY field #.1173</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>The Patient MPI/PD Data Inquiry [RG EXCEPTION TF INQUIRY] and Display Remote Patient Data Query [RG REMOTE PDAT DISPLAY] options display the full INTEGRATION CONTROL NUMBER (ICN), which includes the following data from the PATIENT file (#2):</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>INTEGRATION CONTROL NUMBER field (#991.01)</p>
</blockquote></li>
<li><blockquote>
<p>a "V" separator character</p>
</blockquote></li>
<li><blockquote>
<p>ICN CHECKSUM field (#991.02)</p>
</blockquote></li>
</ul>
<blockquote>
<p>Example: 1008000002<strong>V</strong>340972</p>
</blockquote>
<ul>
<li><blockquote>
<p>The obsolete COORDINATING MASTER OF RECORD (CMOR) references have been removed from the following locations.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Registration: Load/Edit Patient Data [DG LOAD PATIENT DATA]</p>
</blockquote></li>
<li><blockquote>
<p>Register a Patient [DG REGISTER PATIENT] screen</p>
</blockquote></li>
<li><blockquote>
<p>PATIENT HAS EXPIRED mail message generated when DATE OF DEATH is entered for a patient.</p>
</blockquote></li>
</ul>
<p>Patch RG*1.0*60:</p>
<ul>
<li><blockquote>
<p>Include Alias multiples in VistA side Audit reports. The Patient Audit File Print and Single Patient Audit File Print options include AUDIT data in the display for multiple subfields within the PATIENT (#2) file, specifically the ALIAS (2.01) subfield, ALIAS (.01) and ALIAS SSN (#1) fields.</p>
</blockquote></li>
<li><blockquote>
<p>An obsolete report will be removed from the Management Reports [RG MGT REPORTS] menu.  The National ICN Statistics [RG NATIONAL ICN STATISTICS] report is deleted. RG NATIONAL ICN STATISTICS will be distributed as DELETE AT SITE</p>
</blockquote></li>
</ul>
<p>Patch MPIF*1.0*57:</p>
<ul>
<li><blockquote>
<p>The Display Only Query option displays the full INTEGRATION CONTROL NUMBER (ICN), which includes the following data from the PATIENT file (#2):</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>INTEGRATION CONTROL NUMBER field (#991.01)</p>
</blockquote></li>
<li><blockquote>
<p>a "V" separator character</p>
</blockquote></li>
<li><blockquote>
<p>ICN CHECKSUM field (#991.02)</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Updated: Appendix A: <em>VHA DIRECTIVE 1906 "DATA QUALITY REQUIREMENTS FOR HEALTHCARE IDENTITY MANAGEMENT AND MASTER VETERAN INDEX FUNCTIONS"</em></p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>7/2012</td>
<td><p>Documentation updates <em><u>not</u></em> related to a patch release:</p>
<ul>
<li><p>Replaced VistA Logo w/VA Seal on title page.</p></li>
<li><p>Updated appendix titled: "Data Stored on the MPI in Austin" to reflect current MPI VETERAN/CLIENT file (#985).</p></li>
<li><p>Updated appendix and table titled: "Primary View Identity Traits" to reflect Primary View of the MPI.</p></li>
<li><p>Updated Glossary based on HC IdM feedback.</p></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>1/2012</td>
<td><p>Documentation updates:</p>
<ul>
<li><p>As of Patch RG*1*59, the following two fields were added to the VistA PATIENT file (#2) in support of the Defense Eligibility Enrollment Reporting System (DEERS). These fields are used by the Master Veteran Index to support the linking of patient records across VA and DoD.</p></li>
</ul>
<ul>
<li><p>TEMPORARY ID NUMBER (#991.08)</p></li>
<li><p>FOREIGN ID NUMBER (#991.09)</p></li>
</ul>
<blockquote>
<p><strong>NOTE:</strong> Both new fields are turned on for auditing in the PATIENT file (#2) for MPI/PD VistA.</p>
</blockquote>
<ul>
<li><blockquote>
<p>The TEMPORARY ID NUMBER (#991.08) and FOREIGN ID NUMBER (#991.09) fields have been added to the VistA Patient MPI/PD Data Inquiry [RG EXCEPTION TF INQUIRY] option. The fields are displayed if they are populated for the selected patient record. The fields are also shown on the Display Remote Patient Data Query [RG REMOTE PDAT DISPLAY] option if populated.</p>
</blockquote></li>
<li><blockquote>
<p>The obsolete CMOR and CMOR History sections of the Patient MPI/PD Data Inquiry [RG EXCEPTION TF INQUIRY] option have been removed. These fields were also removed from the Display Remote Patient Data Query [RG REMOTE PDAT DISPLAY] option.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>08/02/11</td>
<td><p>Two updates <em><u>not</u></em> generated from a patch release:</p>
<ul>
<li><p>The appendix titled: <em>“MPI/PD Business Rules”</em> has been updated to remove the CMOR references and renamed to <em>“MPI Glossary of Working Concepts.”</em></p></li>
<li><p>Reviewed documentation to update for current organizational references and standards.</p></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>12/17/10</td>
<td><p>Updates via Patch DG*5.3*825:</p>
<p>Added the following text to the PIMS screen captures listed below “User will be prompted for the Alias SSN if the Alias Name is added; however, the Alias SSN is optional:”</p>
<ul>
<li><p>Figure 7‑1: No match found, patient is added to MPI</p></li>
<li><p>Figure 7‑2: Exact Match found on MPI. PATIENT file (#2) updated</p></li>
<li><p>Figure 7‑3: Load/Edit Patient Data–Add patient to PATIENT file (#2) and MPI for first time</p></li>
<li><p>Figure 7‑4: Load/Edit Patient Data—Select patient for processing already having ICN and CMOR</p></li>
<li><p>Figure 7‑5: Register a Patient- Add new patient, and connect to MPI for first time</p></li>
<li><p>Figure 7‑8: Computer dialogue displayed if MPI direct connection becomes unavailable</p></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>07/2010</td>
<td><p>48BUpdates via Patch RG*1*57:</p>
<p>MPI_CR1893(MPI_CodeCR1982) as they apply to this documentation:</p>
<ul>
<li><blockquote>
<p>Upon logon to the system, members of the RG CIRN DEMOGRAPHIC ISSUES Mail Group now only see the one notification alerting users if there are Primary View Reject exceptions that need to be reviewed (Potential Matches Returned are obsolete).</p>
</blockquote></li>
<li><blockquote>
<p>The "PMR Potential Match Rev" action has been removed from the MPI/PD Exception Handling [RG EXCEPTION HANDLING] option.</p>
</blockquote></li>
<li><blockquote>
<p>All exceptions of type "Potential Matches Returned (218)" with the status NOT PROCESSED have been marked PROCESSED in the MPI/PD Exception Handling [RG EXCEPTION HANDLING] option.</p>
</blockquote></li>
<li><blockquote>
<p>On the Management Reports menu, the Unresolved Exception Summary option now only shows totals for Primary View Reject exceptions.</p>
</blockquote></li>
</ul>
<p>NOTE: The Potential Matches Returned exception in the VistA Exception Handler was made obsolete via VistA Patch MPIF*1*52 in that the logging of Potential Matches Returned exceptions was removed from the VistA HL7 message processor routines.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>11/2009</td>
<td>Final updates to documentation implementing feedback from Product Support (PS) for national release.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>8/2009</td>
<td><p>Updates via Patch RG*1*54:</p>
<ul>
<li><blockquote>
<p>MPI_CR1680(MPI_CodeCR1736) The Display Only Query needs to be able to handle upper and lower case data entry. Updated the Display Only Query screen capture and descriptive text to reflect this.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>7/2009</td>
<td>MPI_CodeCR1713: Identity Management Data Quality (IMDQ) name change to Healthcare Identity Management (HC IdM).</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>7/2009</td>
<td><p>Updates via Patch DG*5.3*712:</p>
<ul>
<li><blockquote>
<p>Healthcare Identity Management (HC IdM) requested that BAD ADDRESS INDICATOR field (#.121) be added to the fields monitored and stored on the MPI for use by the matching logic. This VistA field has been added to the existing VistA field trigger mechanism.</p>
</blockquote></li>
<li><blockquote>
<p>MPI_CR1502 (MPI_CodeCR1520) The Patient MPI/PD Data Inquiry option has been updated to display a Bad Address Indicator data, if available. This update is being released with Patch DG*5.3*712. The data is derived from the BAD ADDRESS INDICATOR field (#.121) in the PATIENT file (#2).</p>
</blockquote></li>
<li><blockquote>
<p>A new style cross-reference has been added to the following three fields in the VistA PATIENT file (#2) so that when the field is edited, that information is included in the ADT/HL7 PIVOT file (#391.71) in order to update the Master Patient Index:</p>
</blockquote></li>
</ul>
<ul>
<li><p>BAD ADDRESS INDICATOR (#.121)</p></li>
<li><p>EMAIL ADDRESS (#.133)</p></li>
<li><p>PHONE NUMBER [CELLULAR] (#.134)</p></li>
</ul>
<ul>
<li><blockquote>
<p>Obsolete MPI Options Removed from the OPTION file (#19):</p>
</blockquote></li>
</ul>
<ul>
<li><p>Patient Data Review [VAFC EXCEPTION HANDLER]</p></li>
<li><p>Purge Patient Data Reviews [VAFC PDR PURGE]</p></li>
</ul>
<ul>
<li><blockquote>
<p>Healthcare Identity Management (HC IdM) requested that AUDITING be turned on for the ALIAS (#2.01) multiple, and the ALIAS (#.01) and ALIAS SSN (#1) fields in the PATIENT file (#2).</p>
</blockquote></li>
<li><blockquote>
<p>Identity Management Data Quality (IMDQ) name change to Healthcare Identity Management (HC IdM).</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>1/2009</td>
<td><p>MPI_CR1073(MPI_CodeCR1429): 3.2.2 - Master Patient Index/Patient Demographics (MPI/PD) VistA Enhancements released with Patch MPIF*1*52:</p>
<ul>
<li><blockquote>
<p>Prevent logging of local exceptions for potential matches.</p>
</blockquote></li>
<li><blockquote>
<p>Auto-resolve existing VistA Potential Match exceptions.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Remove from the MPI/PD Exception Handler the action for resolving a Potential Match Exception and all associated screens and actions. This functionality will be supported by the IMDQ Toolkit.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>1/2009</td>
<td><p>50BMPI_CR1024 (MPI_CodeCR1381): Enhancement Display Only Query Display−IMDQ reported that place of birth state is showing up with the gender on the display only query when there isn't a place of birth city released with Patch MPIF*1*52. Updated the following screen captures in the Display Only Query option (Edits in Red in the manual):</p>
<ul>
<li><blockquote>
<p>Figure 5‑40: Display Only Query when Patient exists in Patient File</p>
</blockquote></li>
<li><blockquote>
<p>Figure 5‑41: Display Only Query when patient does not exist in PATIENT file (#2)</p>
</blockquote></li>
<li><blockquote>
<p>Figure 5‑42: Display Only Query with an Open Data Management Case</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>6/2008</td>
<td><p>Patch RG*1*52 makes the following changes in the MPI/PD software:</p>
<ul>
<li><blockquote>
<p>MPI/PD Patient Admin User Menu Removed</p>
</blockquote></li>
</ul>
<blockquote>
<p>The MPI/PD Patient Admin User Menu [RG ADMIN USER MENU] was distributed with patch RG*1.0*49 (released 4/10/08) as obsolete with an Out of Order message. This option is being distributed in this build as DELETE AT SITE in order to remove it from the menu structure. There are other MPI/PD options in the MPIF* and VAFC* namespaces that are also obsolete that will be removed in future MPIF* and DG* patches.</p>
</blockquote>
<ul>
<li><blockquote>
<p>The following Date of Death exceptions in the MPI/PD Exception Handler have been made obsolete:</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>-</strong> <strong>Exception Type:</strong> Death Entry on MPI not in VISTA.<br />
<strong>Description:</strong> MPI had Date of Death field populated. Vista did not have Date of Death.<br />
<strong>Exception number:</strong> 215.</p>
<p><strong>-</strong> <strong>Exception Type:</strong> Death Entry on Vista not in MPI.<br />
<strong>Description:</strong> VISTA had Date of Death field populated. MPI did not have Date of Death.<br />
<strong>Exception number</strong>: 216.</p>
<p><strong>-</strong> <strong>Exception Type:</strong> Death Entries on MPI and Vista DO NOT Match.<br />
<strong>Description:</strong> MPI and VistA had different dates of death for this patient.<br />
<strong>Exception number:</strong> 217.</p>
</blockquote>
<ul>
<li><blockquote>
<p>REMOTE DATE OF DEATH INDICATED Bulletin Made Obsolete:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>The Remote Date of Death Indicated notification message generated from the MPI has been made obsolete. This bulletin indicated that the patient had a date of death entered from the sending site but not at the receiving site.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Obsolete Data Removed from the Unresolved Exception Summary report:</p>
</blockquote></li>
</ul>
<blockquote>
<p>Data referencing the Patient Data Review and CMOR Requests Status has been removed from the Unresolved Exception Summary report. Those issues were made obsolete in earlier patches.</p>
</blockquote></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>4/2008</td>
<td>As of Patch RG*1*49 and DG*5.3*766, the Patient Data Review option has been disabled by placing the MPI/PD Patient Admin User Menu Out of order.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>3/2008</td>
<td><p>As of Patch DG*5.3*756, the ALIAS [#1] multiple in the PATIENT (#2) file will be updated in VistA resulting from the edits made to that information on the MPI by the IMDQ team. The VistA data will be synchronized to match the MPI values. Additionally, when a facility revises their local ALIAS data, the information will be transmitted to the MPI, which in turn will update all treating facilities where the patient is known.</p>
<p>NOTE: Patch DG*5.3*756 was released on September 6, 2007.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>1/2008</td>
<td>A Remote Procedure Call (RPC) sends a request for data to the Master Patient Index (MPI) from VistA for the Primary View Display from MPI [RG PRIMARY VIEW FROM MPI] option, the View PV Rej Detail (PVR) action, and the MPI Primary View (PR) action on the MPI/PD Exception Handling [RG EXCEPTION HANDLING] option. This RPC has been updated in Patch RG*1*53 to allow the query to be re-sent when delays are encountered.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>12/2007</td>
<td>These are the Release Notes for Patch RG*1*50, which reflects Identity Management Data Quality’s (IMDQ) request that the MPI/PD Exception Purge option, [RG EXCEPTION PURGE], be changed to process Primary View Reject exceptions similar to other MPI/PD exception types. Now, the purge job RG EXCEPTION PURGE eliminates duplicate exceptions for the same patient/exception type for <em>all</em> MPI/PD exception types, keeping only the most recent occurrence.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>8/2007</td>
<td><p>Documentation updates for the Patches RG*1*48 and MPIF*1*48, including functionality from Patch DG*5.3*756, which is part of the Master Patient Index (MPI) Changes Project, Iteration 4.</p>
<ul>
<li><blockquote>
<p>VA facilities now have the ability to remotely view Primary View patient identity fields on the Master Patient Index (MPI). This information is available on the MPI in the MPI Patient Data Inquiry [MPI DATA MGT PDAT MPI] option. The report generated by this option displays the current activity scores for individual patient identity fields (i.e., Primary View of the MPI).</p>
</blockquote></li>
<li><blockquote>
<p>In the Primary View of the MPI, the ALIAS multiple (#50) is stored in the MPI VETERAN/CLIENT file (#985). In VistA, the ALIAS multiple (#1) is stored in the PATIENT file (#2). All edits made by Identity Management Data Quality (IMDQ) staff to any of the fields in the ALIAS multiple on the MPI via the Edit PV Alias Values [MPI DATA MGT EDIT PV ALIAS] option, including any pre-existing alias data in that same patient entry that was not edited, is sent to the Primary View of the MPI and now synchronized out to all systems of interest (e.g., VistA treating facilities) for that patient. Site updates to the ALIAS multiple (#1) in the VistA PATIENT file (#2) will be updated in VistA and synchronized to match the MPI values. Additionally, when a VA facility updates their local ALIAS data, the information is sent to the Primary View of the MPI and synchronized back out to all other treating facilities (systems of interest) in which that patient has been seen for care.</p>
</blockquote></li>
<li><blockquote>
<p>The CIRN HL7 EXCEPTION LOG file (#991.1) has been modified to record VA facility personnel who use the MPI/PD Exception Handling option to resolved exceptions and the date/time the resolution occurred. Patch RG*1*48 adds the following new fields to File #991.1:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>DATE/TIME PROCESSED field (#7)</p>
</blockquote></li>
<li><blockquote>
<p>WHO MARKED PROCESSED field (#8)</p>
</blockquote></li>
</ul>
<blockquote>
<p>This data is now being captured and Identity Management Data Quality (IMDQ) staff will have the capability to view this information.</p>
</blockquote>
<ul>
<li><blockquote>
<p>A change has been made in the MPI/PD EXCEPTION HANDLING [RG EXCEPTION HANDLING] option. Upon selecting the MPI/PD Exception Handling option, instead of being prompted to run the exception purge, you are now notified when the last purge took place. The purge process runs automatically if it has not run within the past two hours; however, the MPI/PD EXCEPTION PURGE [RG EXCEPTION PURGE] option should be scheduled to run once an hour via TaskMan. It can take a few minutes to run, but once the job is finished, you can go back to the Message Exception Menu and choose MPI/PD Exception Handling to view the results of the purge process.</p>
</blockquote></li>
<li><blockquote>
<p>A stand-alone option named View VistA Exceptions for Patient [MPI DATA MGT VISTA EXCEPTION] has been implemented on the MPI in Austin for the Identity Management Data Quality (IMDQ) team allowing them to query a VistA site for a selected patient and view all the existing VistA exceptions for a given date range. The VistA side support for this new MPI option came in as part of Patch RG*1*48.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>4/2007</td>
<td><p>As of Patch DG*5.3*707, the following enhancements were made to the Patient MPI/PD Data Inquiry [RG EXCEPTION TF INQUIRY] option:</p>
<ul>
<li><blockquote>
<p>Display SSN Verification and Pseudo SSN Reason.</p>
</blockquote></li>
<li><blockquote>
<p>Remove the call to calculate CMOR score and remove the display of CMOR Score and Subscription Control Number.</p>
</blockquote></li>
<li><blockquote>
<p>Modify format of display.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>3/2007</td>
<td><p>As of Patches MPIF*1*46 and RG*1*44, this documentation has been updated to reflect the following:</p>
<p>Patch MPIF*1*46:</p>
<ul>
<li><blockquote>
<p>Processing to account for the HL7 PID segment message being greater than 245 characters.</p>
</blockquote></li>
<li><blockquote>
<p>Resume correct prompting for identity fields in the first part of PIMS Registration options for new patients.</p>
</blockquote></li>
<li><blockquote>
<p>Updated screening to prevent Primary View Reject exceptions from entering the Potential Matches Returned logic.</p>
</blockquote></li>
<li><blockquote>
<p>Changed exception text for the new Primary View Reject exception.</p>
</blockquote></li>
</ul>
<p>Patch RG*1*44:</p>
<ul>
<li><blockquote>
<p>Functionality incorporated into the MPI/PD Exception Handling RG EXCEPTION HANDLING option to automatically process the "Primary View Reject" exceptions. Name change for exception action that processes reject exceptions "PVR View PV Rej Detail."</p>
</blockquote></li>
<li><blockquote>
<p>MPI/PD Exception Purge process updated. For every date that an exception occurs for a patient, the exception occurs in the Exception Handler for review. However, if more than one active Primary View Reject exception occurs during the same day for the same patient, the purge will remove the duplicate occurrences, leaving only the most recent.</p>
</blockquote></li>
<li><blockquote>
<p>Alias Social Security Numbers included in the HL7 ADT-A31 update message.</p>
</blockquote></li>
<li><blockquote>
<p>Processing to ensure that pending updates to the Primary View waiting in the ADT/HL7 PIVOT file (#391.71) are not lost in IMDQ override process.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>1/2007</td>
<td><p>As of Patches MPIF*1*44 and RG*1*45, this documentation has been updated to reflect the following:</p>
<ul>
<li><p>The concept of a "CMOR facility" is being phased out and will be replaced by the Primary View when Patch MPI*1*40 is installed on the Austin MPI. VistA Patch MPIF*1*44 sets all VistA options related to "CMOR" out of order, rendering them obsolete. The OUT OF ORDER MESSAGE field for these options is marked as "Obsolete with Patch MPIF*1*44."</p></li>
<li><p>As of Patch MPIF*1*44, the Site Parameters Edit for CMOR [MPIF SITE PARAMETER] option, located on the MPI/PD Patient Admin Coordinator Menu, is obsolete and has been placed out of order.</p></li>
<li><p>As of Patch MPIF*1*44, the AUTO CHANGE CMOR NIGHT JOB [MPIF CMOR REQUEST AUTO JOB] option is obsolete. Sites that have this option scheduled to run via TaskMan, should unscheduled it.</p></li>
<li><p>SSN VERIFICATION STATUS field (#.0907) is now synchronized out to Sites when updated by Enrollment System Redesign (ESR) as of Patch RG*1*45.</p></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>4/2006</td>
<td><p>Updated documentation based on VistA Patch DG*5.3*707. Changed the Patient MPI/PD Data Inquiry option display:</p>
<ul>
<li><p>Added SSN Verification and Pseudo SSN Reason</p></li>
<li><p>Remove call to calculate CMOR score and remove display of CMOR Score and SCN</p></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>4/2006</td>
<td>Updates to documentation based on Patches MPIF*1*43 and RG*1*43, which comprise the changes to the MPI/PD software resulting from the Health Eligibility Center (HEC) Enumeration to the Master Patient Index (MPI).</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>4/2005</td>
<td><p>Updated documentation based on Patch MPIF*1*37 as follows:</p>
<ul>
<li><p>Included new "Appendix I: Change To Identity Management Fields, Patch MPIF*1*37"</p></li>
<li><p>Updated all affected screen captures from Patch MPIF*1*37</p></li>
</ul>
<p>Corrected test data for patient name.</p>
<p>Corrected screen captures for misplaced prompts:</p>
<ul>
<li><p>PATIENT SERVICE CONNECTED?</p></li>
<li><p>PATIENT MULTIPLE BIRTH INDICATOR:</p></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>12/2004</td>
<td>Implemented new conventions for displaying TEST data. See Orientation section for details.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>5/2004</td>
<td>MPI/PD VistA Version 1.0 User Manual released in conjunction with patches MPIF*1*33, RG*1*35 and DG*5.3*589 to support the MPI Changes Iteration 2 project.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>12/2003</td>
<td>Updates to documentation based on Patches RG*1*29 and DG*5.3*479.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>6/2003</td>
<td>MPI/PD VistA Version 1.0 User Manual released in conjunction with patches DG*5.3*505, and MPIF*1*28 of the MPI Changes Iteration I project.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>4/1999</td>
<td>Initial MPI/PD and MPI VistA User Manuals were created for release with the MPI/PD V.1.0 software in April 1999.</td>
<td>Master Patient Index team</td>
</tr>
</tbody>
</table>

Patch History

For the current patch history related to this software, please refer to the Patch Module (i.e., Patch User Menu \[A1AE USER\]) on FORUM.

Contents

Figures

Tables

Page intentionally left blank for double-sided print copy.

  
Orientation

How to Use this Manual

This manual uses several methods to highlight different aspects of the material.

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

<span id="_Toc247320306" class="anchor"></span>Table ‑. Documentation Symbol Descriptions

| Symbol                                                                                                     | Description                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/002.png) | NOTE: Used to inform the reader of general information including references to additional reading material |
| ![](mpi-pd-version-1-vista-user-manual/003.png)                                                              | CAUTION: Used to caution the reader to take special notice of critical information                         |

- Descriptive text is presented in a proportional font (as represented by this font).
- "Snapshots" of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts will be boldface type.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter or Return key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/004.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- Uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666."
- Person, patient, and user names will be formatted as follows:

> \[application name\]PERSON,\[fictitious given name\]; \[application name\]PATIENT,\[fictitious given name\]; and \[application name\]USER,\[fictitious given name\] respectively.

> The "fictitious given name" represents a fabricated given name for the patient, person or user. Using a name (rather a number) more clearly represents test data when it’s used in descriptive text in this documentation to convey a concept or comparison. For example: MVIPERSON,SAM; MVIPATIENT,NANCY; MVIUSER,DEBRA, etc.

|                                                                                                                |                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/005.png) | NOTE: The business owner, Healthcare Identity Management (HC IdM), requested we use the following nomenclature to represent test data for HC IdM Caseworkers: “HC IdM CASE WORKER. |

Intended Audience/Assumptions

This manual has been written with many job functions in mind. Personnel responsible for registering persons, data integrity, Patient Information Management System (PIMS) Automated Data Processing Application Coordinators (ADPACs), and IT personnel involved with using all aspects of the Master Veteran Index (MVI) should read this manual. If you need more information, please refer to the OI&T Product Development Web site for a general orientation to VistA:

> VA OIT Product Development Web site

> *NOTE: This is an internal VA Web site and is not available to the public.*Reference Material

Readers who wish to learn more about the Master Patient Index/Patient Demographic (MPI/PD) software should consult the following VA Web sites:

- VA Software Document Library (VDL) Web site:

> [MPI/PD documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=16)

- The MPI/PD product documentation, as found at the link above, includes the following manuals:
- *Master Patient Index/Patient Demographics (MPI/PD) User Manual*
- *Master Patient Index/Patient Demographics (MPI/PD) HL7 Interface Specifications*
- *Master Patient Index/Patient Demographics (MPI/PD) Technical Manual*
- *Master Patient Index/Patient Demographics (MPI/PD) Programmer Manual*
- *Master Patient Index (MPI) Monograph*
- Also see the VistA Duplicate Record Merge manuals listed below, which can be found on the VA Web site:

> [Duplicate Record Merge: Patient Merge documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=2)

- *Duplicate Record Merge: Patient Merge Release Notes for Kernel Toolkit Patch XT\*7.3\*113.*
- *Duplicate Record Merge: Patient Merge User Manual, Version 7.3, Patch XT\*7.3\*113*
- *Duplicate Record Merge: Patient Merge Technical Manual, Version 7.3, Patch XT\*7.3\*113*Installation Information and Procedures

The Master Patient Index VistA and Patient Demographics were distributed and installed together. All installation information and procedures involved with the MPI VistA is included in the *CIRN Patient Demographics (CIRN-PD) Pre-Installation and Implementation Guide v.5* document on the VA Software Document Library Web site:

> [MPI/PD documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=16)

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/006.png) | NOTE: One of the major pre-implementation tasks is the merging of duplicate patient records at a site. The *"Duplicate Record Merge: Patient Merge (Patch XT\*7.3\*23) User Manual"* is required for this task. Patches XT\*7.3\*49, RG\*1\*6, and RG\*1\*10 allow sites with MPI/PD to resolve duplicate records. If you do not have these patches installed, it is recommended that the option to merge patient records be placed out of order. |

Interaction Between MPI/PD and Other Packages

Because of the close interaction between MPI/PD and other packages, you may also find it helpful to review the documentation for the following VistA software:

- *VistA HL7 V. 1.6*
- *PIMS V. 5.3 Admission, Discharge and Transfer (ADT)*

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF).

How to Obtain Technical Information Online

Exported VistA M-based file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/007.png) | NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA M-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in VistA character-based software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A, while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text that may be stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about VistA M-based files and their associated fields is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/008.png) | NOTE: For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Legal DisclaimersSoftware

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. VA software has no patent/copyright/trademark protections and can be distributed freely via the Freedom of Information Act (FOIA). Pursuant to title 17 Section 105 of the United States Code, this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Documentation

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Product Description―What Comprises the Master Patient Index?](#product-descriptionwhat-comprises-the-master-patient-index)
    - [Master Patient Index (Austin)](#master-patient-index-austin)
    - [Master Patient Index/Patient Demographics (VistA)](#master-patient-indexpatient-demographics-vista)
    - [Primary View Replaces Obsolete CMOR View](#primary-view-replaces-obsolete-cmor-view)
    - [Systems of Interest to the MVI—Treating Facilities and Non-VistA Systems](#systems-of-interest-to-the-mvitreating-facilities-and-non-vista-systems)
- [Primary View—How are VistA Sites Affected by this Change to the MVI?](#primary-viewhow-are-vista-sites-affected-by-this-change-to-the-mvi)
    - [Primary View Auto-Updates Person Identity Fields in the VistA Patient File (#2)](#primary-view-auto-updates-person-identity-fields-in-the-vista-patient-file-2)
    - [Primary View Identity Traits](#primary-view-identity-traits)
- [Software Management](#software-management)
    - [Name and Number Spaces](#name-and-number-spaces)
    - [Software Requirements](#software-requirements)
    - [Legal Requirements](#legal-requirements)
    - [HL7 Application Parameters File](#hl7-application-parameters-file)
    - [Bulletin](#bulletin)
    - [MPI/PD Mail Groups](#mpipd-mail-groups)
- [MPI/PD Menus and Options](#mpipd-menus-and-options)
  - [MPI/PD Master Menu](#mpipd-master-menu)
    - [MPI/PD Patient Admin Coordinator Menu](#mpipd-patient-admin-coordinator-menu)
    - [MPI/PD IRM Menu](#mpipd-irm-menu)
    - [Standalone Options](#standalone-options)
- [Background Jobs](#background-jobs)
    - [LOCAL/MISSING ICN RESOLUTION](#localmissing-icn-resolution)
    - [UPDATE BATCH JOB FOR HL7 v2.3](#update-batch-job-for-hl7-v23)
- [PIMS Options](#pims-options)
    - [Overview of PIMS Interaction with the MVI](#overview-of-pims-interaction-with-the-mvi)
    - [PIMS Option: Load/Edit Patient Data](#pims-option-loadedit-patient-data)
    - [PIMS Option: Register a Patient](#pims-option-register-a-patient)
    - [Patient Sensitivity](#patient-sensitivity)
    - [MVI Direct Connection Unavailable: Local ICN Assignments](#mvi-direct-connection-unavailable-local-icn-assignments)
    - [Under What Conditions are Local ICNs Assigned to Patient Records?](#under-what-conditions-are-local-icns-assigned-to-patient-records)
  - [Glossary](#glossary)
  - [Appendix A: VHA DIRECTIVE 1906](#appendix-a-vha-directive-1906)
  - [Appendix B: MPI Glossary of Working Concepts](#appendix-b-mpi-glossary-of-working-concepts)
  - [Appendix C: Why Doesn't a Patient Have a National ICN?](#appendix-c-why-doesnt-a-patient-have-a-national-icn)
  - [Appendix D: Change to Identity Management Fields, Patch MPIF\1\37](#appendix-d-change-to-identity-management-fields-patch-mpif137)
  - [Appendix E: Primary View Identity Traits](#appendix-e-primary-view-identity-traits)
  - [Index](#index)
Overview of Master Veteran Index (MVI)
The Master Veteran Index (MVI) is the authoritative source for *<u>person identity data</u>*. It maintains identity data for persons across VA systems, provides a unique universal identifier for each person, stores identity data as correlations for each system where a person is known, provides a probabilistic matching algorithm, and includes the Master Patient Index (MPI), Person Service Identity Management (PSIM), and Toolkit (TK). It maintains a “gold copy” known as a “Primary View” of the person’s identity data. Broadcasts identity trait updates to systems of interest.
The MPI Austin is the data store of person records and one of the component pieces of the Master Veteran Index. It is a cross-reference or index of persons that includes the person's related identifiers and other patient identifying information. The MVI is used to associate a person's identifiers among multiple ID-assigning entities, possibly including a Health Data Repository, to support the consolidation and sharing of a patient’s health care information across VHA. The MVI is the authoritative source for *<u>patient identity</u>*.
Overview of Master Patient Index/Patient Demographics
This is the documentation for the Master Patient Index/Patient Demographics (MPI/PD) software.
MPI/PD was developed to initialize active persons to the Master Veteran Index (MVI) and to establish the framework for the sharing of person information between sites. During the process of initialization to the Master Veteran Index, each active person received:
- An Integration Control Number (ICN)
- A Coordinating Master of Record (CMOR) – no longer utilized
- A Treating Facility List of sites where the person is also known by this ICN
Each site becomes part of the network of sites that share key demographic data for patients via HL7 messaging. Master Patient Index VistA (MPI) and Patient Demographics (PD) were distributed and installed together. This manual covers the functionality of both packages.
The objectives of the MPI/PD are to:
- Create an index that uniquely identifies each active person treated by the Veterans Administration.
- Identify the sites where a person is receiving care.
This is crucial to the sharing of person information across sites.
Master Patient Index Patch MPI\*1\*40 constituted a change in the business process that updates the person identity fields across VA facilities. As of Patch MPI\*1\*40, the Primary View methodology was introduced, phasing out the use of the facility Coordinating Master of Record (CMOR) concept. Primary View is an enterprise view of the most current data for a person based on authority scoring and the latest data rules.
History
MPI/PD was originally part of the Clinical Information Resource Network (CIRN) project. CIRN was to be a three-phase project consisting of Phase 1: Pre Implementation (site cleanup), Phase 2: Master Patient Index/Patient Demographics (Master Patient Index seeding for VHA-wide patient identification and patient demographics synchronization), and Phase 3: CIRN Clinical Repository. Master Patient Index/Patient Demographics is now a separate, independent package. Due to its beginnings, you will still notice references to CIRN (e.g., shared name and number spaces, file names, package terminology, etc.). The clinical repository is now a separate, independent project called Health Data Repository (HDR).
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/009.png)</td>
<td><p><strong>NOTE:</strong> During the 1980s, the policy for creating persons in the PATIENT file (#2) that were also employees was to enter them as EEE followed by their social security number (SSN). That policy was subsequently revoked but did not include any cleanup of the existing EEE patients. During the implementation phase of the Master Patient Index/Patient Demographics (MPI/PD) application, a report was generated to identify these persons. Some of them were changed to their correct names, but many still had not been resolved. It was possible for these EEE patients to be assigned an ICN, either local or national. Since this data does not assist in the identification or sharing of person data, it was decided that these person should not be assigned an ICN of any kind, nor should an exception be logged that they have been touched. Prior to Patch MPIF*1*33, patients who had both an “EEE” as the first three characters of their last name and an ICN (local or National) were inactivated (following the rules for inactivation) from the MPI during the post initialization for Patch MPIF*1*21. These EEE persons were included in the screen of persons <em>not</em> to be sent to the MVI.</p>
<p>This screen on EEE patients was reviewed again in the MPI Changes 2 project and removed in Patch MPIF*1*33. Patients with last names beginning with “EEE” will no longer be screened from getting a local or national ICN. In addition, no exception message will be logged in the local VistA exception handler when these patient entries are touched.</p></td>
</tr>
</tbody>
</table>
Distinguishing MPI (Austin) from MPI/PD at the VA Facilities
The actual index referred to as the *<u>Master Patient Index (MPI)</u>* is located at the Austin Information Technology Center (AITC). *<u>Master Patient Index/Patient Demographics (MPI/PD)</u>* refers to the software that resides at the VA facilities, which sends patient data to the MPI (Austin). These terms \[i.e., MPI (Austin) and MPI/PD\] are used throughout this manual only when it is not obvious which component of the MPI the documentation is referring. Otherwise, the reader should assume the information is referring to MPI/PD.
MPI Identity Hub for the Healthcare Identity Management (HC IdM) Team
As of the release of MPI/PD Patches MPIF\*1\*52 and RG\*1\*54, the MPI Identity Hub for Healthcare Identity Management (HC IdM) was implemented enabling the change from the current MVI person deterministic lookup to an Identity Hub based probabilistic patient lookup.
Initiate was purchased to be integrated with the MPI and Person Service Identity Management (PSIM) for the purpose of improving the matching of patients and persons across VHA. PSIM will serve as the interface to the commercial Identity Management system and the MPI will interact with PSIM.
The Initiate centralized probabilistic search algorithm will replace the local VistA KERNEL DUPLICATE RECORD MERGE search process for identifying local potential duplicate PATIENT file (#2) records. When the search algorithm identifies potential duplicates, they are automatically added to the VistA DUPLICATE RECORD file (#15).
|                                                                                                                |                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/010.png) | REF: For more information on the VistA DUPLICATE RECORD MERGE release, please refer to Kernel Toolkit Patch XT\*7.3\*113. |
Installation Information
The Master Patient Index VistA and Master Patient Index/Patient Demographics (MPI/PD) were distributed and installed together. All installation information and procedures involved with MPI VistA suite have been referenced in the following MPI/PD documents:
- *CIRN Patient Demographics (CIRN-PD) Pre Installation and Implementation Guide V. 5*
- *Master Patient Index/Patient Demographics (MPI/PD) Installation and Implementation Guide V. 2.*
In October 2002, the three-phase release of patches for the MPI/PD software enhancement began. Phase I consisting of three patches, contains the protocols and routines to execute a new messaging structure. The overall objective of the new messaging is to reduce the amount of facility-to-facility messaging by using the Master Veteran Index (MVI), rather than the CMOR, as the source for update messages.
The second phase of patches updates the necessary routines to call the new trigger events using the updated messaging structure. The trigger events include the following:
- Add new patient to the MVI.
- Link to an existing patient on the MVI.
- Update to non-key fields on an existing MVI entry.
- Update to key fields on an existing MVI entry.
- Update to date last treated.
- Resolution of duplicates at the site where both entries exist on the MVI.
- Resolution of duplicates on the MVI.
- Identification and resolution of a mismatched person.
- Inactivation of existing entry on the MVI.
This phase also includes a data synchronization process to populate new fields in the MPI FACILITY ASSOCIATION file (#985.5) on the MVI for each facility associated with a national integration control number (ICN). Before this is done though, all facilities must install the patches for the second phase.
The third phase of patches contains additional messaging functionality that cannot be implemented until the synchronization process has completed. This final group of patches will clean up obsolete routines, protocols, and options that are no longer used.
Page intentionally left blank for double-sided print copy.

# Product Description―What Comprises the Master Patient Index?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Master Patient Index (Austin)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Master Patient Index (MPI) is located at the Austin Information Technology Center (AITC). It is composed of a unique list of persons and an associated list of VAMCs (Veterans Affairs Medical Centers) and other systems of interest where each person has been seen. This enables the sharing of person data between operationally diverse systems. Each person record (or index entry) on the MVI contains multiple demographic fields which are updated to the Primary View.

When a person is first presented into the MVI for an Integration Control Number (ICN) assignment, that person's identifying information (i.e., name, Social Security Number (SSN), date of birth, gender, mother's maiden name, multiple birth indicator, place of birth city and state) is passed to the MVI.

The MVI checks to see if an exact match on Name (first and last), SSN, date of birth, and gender is found. A check is also made to see if the person's internal entry number (DFN) from the querying site is already known to the MVI. If so, this is also considered an exact match. If an exact match is found, the ICN, and ICN Checksum are returned to the requesting site. The requesting site is added to the list of treating facilities (TF) in which this person has been seen and the updated list is broadcasted to all systems of interest, including VAMCs.

If a match is not found, the MVI returns a message indicating this. The patient entry is then added to the MVI. If a potential match is found, a potential match exception is logged for the HC IdM group to review, the person is still added to the MVI.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/011.png) | NOTE: The term "systems of interest" refers to VA facilities that have seen persons and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a person (e.g., Federal Health Information Exchange \[FHIE\], HomeTeleHealth, Person Service Identity Management \[PSIM\], Health Data Repository \[HDR\], etc.). |

#### Healthcare Identity Management Team is Data Steward for the Master Veteran Index

The Healthcare Identity Management (HC IdM) team is the Data Steward for the Master Veteran Index (MVI). The HC IdM team is comprised of analysts who have considerable experience working with the MVI and person data updates. They have the ability to perform the following functions on the Primary View of the MVI:

- View and/or edit the authority values for the Primary View business rules criterion.
- Override Primary View identity traits for selected identity fields in the MPI VETERAN/CLIENT file (#985) and broadcast the new Primary View out to the systems of interest.
- View the Primary View Reject Report from the data in the MPI REJECTED UPDATE file (#985.65).

### Master Patient Index/Patient Demographics (VistA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Master Patient Index/Patient Demographics (MPI/PD) software resides in VistA enabling sites to:

- Request an ICN assignment
- Resolve a potential duplicate on the MVI.
- Query the MVI for known data.
- Update MVI MPI when changes occur to demographic fields stored on the MVI or of interest to other facilities/systems of interest.

#### Requesting an ICN Assignment

During the initialization of the MVI, each VA Medical Center sent batch HL7 messages to the MVI requesting ICNs for all persons whose records reflected activity in the past three fiscal years (i.e., active patient records).

In day-to-day operations, persons are presented to the MVI via:

- PIMS options:
  - Load/Edit Patient Data \[DG LOAD PATIENT DATA\]
  - Register a Patient \[DG REGISTER PATIENT\]
  - Electronic 10-10EZ Processing \[EAS EZ 1010EZ PROCESSING\]
- Local/Missing ICN Resolution \[MPIF LOC/MIS ICN RES\] background job

When a new patent record is created via the PIMS options, a real-time connection is established to the MVI requesting an ICN assignment. If communication cannot be established or is lost with the MVI before the ICN assignment process has completed, a local ICN is assigned. Otherwise, a national ICN is assigned to the person. The ICN can either be newly created or already on the MMVIPI for that person. The ICN, ICN checksum, and list of facilities, including other systems of interest (e.g., FHIE and HDR), are updated in the site's VistA system.

If an existing person record is edited via the PIMS options, and if this person does not have an ICN (national or local), the same process occurs as was illustrated for a newly created person.

If a person record is edited or created outside of the PIMS options, they are presented to the MVI for ICN assignment via the Local/Missing ICN Resolution background job.

If a match is not found the MVI returns a message indicating this and that the person is being added to the MVI. If potential matches are found, a new ICN is assigned to the person, and an exception is logged for the Health Care Identify Management (HC IdM) group to review and provide the appropriate action.  If the persons are truly the same person, then the records will be linked together with one ICN becoming the primary ICN that all records will be linked under and the other will be deactivated.  The sites that had the deactivated ICN will be updated to the primary ICN.

|                                                                                                                |                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/012.png) | NOTE: As of MPI/PD Patch MPIF\*1\*52, all screens and actions associated with the MPI/PD Exception Handler functionality for resolving Potential Match Exceptions have been removed from MPI/PD. This functionality is now supported in the Identity Management Toolkit. |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/013.png)</td>
<td><p><strong>NOTE</strong>: MPI/PD updates as of VistA Patches MPIF*1*43 and RG*1*43:</p>
<ul>
<li><blockquote>
<p>The only times local ICNs are assigned to person records are when:</p>
</blockquote>
<ul>
<li><blockquote>
<p>The connection to the MVI cannot be established, or has been lost before the ICN assignment was completed.</p>
</blockquote></li>
</ul></li>
</ul>
<blockquote>
<p>This happens regardless of which process is used to present the person to the MVI for ICN assignment (i.e., Register a Patient, Load/Edit Patient Data, Electronic 10-10EZ Processing, and/or the Local/Missing ICN Resolution Background Job).</p>
</blockquote>
<ul>
<li><blockquote>
<p>The site edits an existing person or adds a new person using an option that doesn't directly interact with the MVI (e.g., VistA Lab or VA FileMan). </p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>All existing exceptions that were active in the CIRN HL7 EXCEPTION LOG file (#991.1) of the types listed below, were marked with a status of PROCESSED:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Required field(s) missing for person sent to MVI</p>
</blockquote></li>
<li><blockquote>
<p>SSN Match Failed</p>
</blockquote></li>
<li><blockquote>
<p>Name Doesn't Match</p>
</blockquote></li>
</ul></li>
</ul>
<blockquote>
<p>These three exceptions listed are no longer generated. </p>
</blockquote>
<ul>
<li><blockquote>
<p>As part of RG*1*43, the View Potential Match Patient [RG EXCEPTION POTENTIAL MATCH] option has been removed from the Message Exception Menu [RG EXCEPTION MENU] as it is obsolete.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

The Display Only Query option allows the site to query the MVI to see what the MVI would return if the person was presented for ICN assignment without actually making the request. The person can be an existing person or the user can choose to enter the name, date of birth and SSN (not required) and see what the MVI returns.

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/014.png) | NOTE: More information about the "Potential Duplicate PATIENT records found by MPI" message is available via the installation of VistA Kernel Toolkit Patch XT\*7.3\*113. |

### Primary View Replaces Obsolete CMOR View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As part of the MPI Changes Project, Iteration 4, the concept of a "CMOR facility" is being phased out and will be replaced by the Primary View when Patch MPI\*1\*40 is installed on the Austin MPI. VistA Patch MPIF\*1\*44 sets all VistA options related to "CMOR" out of order, rendering them obsolete. The OUT OF ORDER MESSAGE field for these options is marked as "Obsolete with Patch MPIF\*1\*44." Obsolete options will be removed from the Coordinating Master of Record (CMOR) Request \[MPIF CMOR MGR\] menu at a future date.

### Systems of Interest to the MVI—Treating Facilities and Non-VistA Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The term "systems of interest" refers to VA facilities that have seen persons and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a person (e.g., Federal Health Information Exchange \[FHIE\], HomeTeleHealth, Person Service Identity Management \[PSIM\], Health Data Repository \[HDR\], etc.).

A facility's relationship to a person determines what information it receives and sends. MPI/PD stores this information.

Any facility where a person is identified by the same ICN (regardless of VISN) is placed on the Treating Facility List. The list may contain other systems of interest that are not VAMCs (e.g., FHIE and HDR).

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/015.png) | NOTE: The Treating Facility List is utilized by several other VistA applications, including Inter-facility Consults and Remote Data Views in CPRS. |

# Primary View—How are VistA Sites Affected by this Change to the MVI?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the Primary View?

Patch MPI\*1\*40 constitutes a change in the business process that updates the patient identity fields across VA facilities referred to as the Primary View of the MVI, overview as follows:

- Primary View is an update to the patient identity fields across VA facilities.
- Primary View creates a centralized view of the patient data aka a Primary View
- Primary View has the best data from any combination of sites for the patient
- Synchronizing the patient identity fields becomes centralized under a new set of business rules on the MVI.
- Primary View is a transition from and *disassociated* with the Coordinating Master of Record (CMOR) view of the MPI.
- Primary View allows for:
- VistA sites to continue to edit patient data at their site.
- Patient data is sent to a central system (i.e., the Master Veteran Index) to determine validity and quality

This is an enterprise view of the most current data for a person based on authority scoring and the latest data rules. Edits to patient identity traits (listed below) are evaluated based on the same. The highest score achieves the best quality of data updates to the Primary View. These values are stored in the MPI VETERAN/CLIENT file (#985) on the MVI (*<u>not</u>* a VistA file).

- Name
- Social Security Number
- Date of Birth
- Gender
- Mother's Maiden Name
- Multiple Birth Indicator (Sent and updated to Primary View as of Patch RG\*1\*45. Added to the list of fields auto-updated \[synchronized\] in VistA as of Patch RG\*1\*47.)
- Place of Birth, City and State
- SSN Verification Status (Verified, Invalid Per SSA, and Null) (Added to File \#985 as of Patch MPI\*1\*40. Populated to the Primary View of the MVI and systems of interest to the MVI as of DG\*5.3\*688 \[EVC R2\].)
- Pseudo SSN Reason (Added to File \#985 as of Patch MPI\*1\*40. Populated to the Primary View of the MVI and systems of interest to the MVI as of RG\*1\*47 and DG\*5.3\*653 \[EVC R1\].)

How Does the Primary View Work?

Before Patch MPI\*1\*40, person data reviews were done at the CMOR sites. All VA facilities nation-wide had responsibility to manage and maintain their set of person. With the release of Patch MPI\*1.0\*40, person updates are controlled by centralized business rules and Primary View scoring on the MVI. HC IdM staff have the ability to override the rejection process of any valid edits.

In the transition to Primary View*,* when a patient is new to the NVI or an existing patient is initialized under the latest business rule changes, the CMOR process for resolving Patient Data Reviews no longer exists. Instead, edits are processed against the centralized data rules and Primary View scoring on the MVI. If the data update is rejected, it will not be updated in the Primary View.  If this field is a synchronized field, the Primary View will be sent to that system attempting to make the update to reject the data and changing it to the current Primary View. This took the burden off CMOR sites to review other sites’ edits for acceptance or rejection.

Business Rules for Data Validity and Integrity

The Healthcare Identity Management (HC IdM) team has developed two spreadsheets that dictate business rules for the Primary View:

- "Business Processes That Update Person Identity"—Authority score
- "Primary View Data Rules"—Data rules

Person identity fields in the Primary View of the MVI are evaluated and updated based on scoring and data rules. The Primary View score is evaluated based on criteria captured from person encounters at VA facilities (e.g., active prescriptions, admission or registration in the last year, lab test, or radiology exam in the last year) that are sending the inbound update (i.e., data entered by users or sent from a system of interest) to the MVI. The score is calculated from data updates coming from the site. Data is weighed on a field-by-field basis against any differences on the MVI to determine if the score for the inbound edits is equal to or greater than the score for the existing Primary View*.* Next, the inbound edit is evaluated against Primary View data rules.

Edits to key person identity fields accepted for the update to the Primary View are broadcasted out to all systems of interest that subscribe to updates for that person that do not already have the updated data. Data that does not meet or exceed the current score and pass the data rules will not be updated in the Primary View.  If this field is a synchronized field, the Primary View will be sent to that system attempting to make the update to reject the data and changing it to the current Primary View.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/016.png) | NOTE: The term "systems of interest" refers to VA facilities that have seen persons and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a person (e.g., Federal Health Information Exchange \[FHIE\], HomeTeleHealth, Person Service Identity Management \[PSIM\], Health Data Repository \[HDR\], etc.). |

|                                                                                                                |                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/017.png) | REF: For a list of the patient identity fields that make up the Primary View on the MVI, see the section titled "Appendix E: Primary View Identity Traits" in this documentation. |

|                                                                                                                |                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/018.png) | NOTE: The MPI VETERAN/CLIENT file (#985) comprises the Primary View and is resident on the Austin MPI. |

### Primary View Auto-Updates Person Identity Fields in the VistA Patient File (#2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields, stored in the MPI VETERAN/CLIENT file (#985), are auto-updated from the MVI to the VistA PATIENT file (#2) and broadcast by the MVI to systems of interest:

- Name
- Social Security Number
- Date of Birth
- Gender
- Mother's Maiden Name
- Multiple birth indicator (Sent and updated to Primary View as of Patch RG\*1\*45. Added to the list of fields auto-updated \[synchronized\] in VistA as of Patch RG\*1\*47.)
- SSN Verification Status (Verified, Invalid Per SSA, and null) (Added to File \#985 as of Patch MPI\*1\*40. Populated to the Primary View of the MVI and systems of interest to the MVI as of DG\*5.3\*688 \[EVC R2\].)
- Pseudo SSN Reason (Added to File \#985 as of Patch MPI\*1\*40. Populated to the Primary View of the MVI and systems of interest to the MVI as of RG\*1\*47 and DG\*5.3\*653 \[EVC R1\].)
- Alias (As of Patch DG\*5.3\*756, the ALIAS \[#1\] multiple in the PATIENT (#2) file is updated in VistA resulting from the edits made to that information on the MVI by the HC IdM team. The VistA data is synchronized to match the MPI values. Additionally, when a facility revises their local ALIAS data, the information is transmitted to the MVI, which in turn updates all treating facilities where the patient is known.)

The concept of the Primary View was introduced with Patch MPI\*1\*40*,* which utilizes central business rules and removes the manual review process (Patient Data Review) from the sites. This allows for faster updates and the ability to have the best data from multiple locations. The site-to-HC IdM communication happens when there is a need for an override of a valid edit that the site had rejected do to the centralized business rules.

Site edits to person identity fields *must* pass the Primary View data rules as well as meet or exceed the current authority score value for that field *before* updating the Primary View on the MVI. If local data fails because the authority score has not weighed in high enough, the edit is rejected.

|                                                                                                                |                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/019.png) | NOTE: The term "auto-update" refers to fields that are updated from a central database (i.e., the Master Veteran Index). |

### Primary View Identity Traits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the list of fields that are stored in the Primary View of the MPI.

|                                                                                                                |                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/020.png) | NOTE: Not all Primary View fields are synchronized to the systems of interest. |

<span id="_Ref408226456" class="anchor"></span>Table ‑. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name and Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>INTEGRATION CONTROL NUMBER (ICN) (#.01)</td>
<td><p>Based on ASTM E-1714 format is 16 digits, delimiter character, 6 checksum digits.</p>
<p>When the ICN is displayed in the MVI, it appears as 10 digits followed by the delimiter character (“V”) followed by the 6 checksum digits.</p></td>
</tr>
<tr class="even">
<td>SURNAME (#1)</td>
<td>Family name, also known as last name.</td>
</tr>
<tr class="odd">
<td>FIRST NAME (#2)</td>
<td>Person's first given name.</td>
</tr>
<tr class="even">
<td>MIDDLE NAME (#3)</td>
<td>Person's middle name or middle initial.</td>
</tr>
<tr class="odd">
<td>NAME PREFIX (#4)</td>
<td><p>Commonly, Dr., Ms., Sir, or other appropriate titles.</p>
<p>NOTE: Not currently populated on the MPI.</p></td>
</tr>
<tr class="even">
<td>NAME SUFFIX (#5)</td>
<td>Examples are Jr., Sr., PhD, etc.</td>
</tr>
<tr class="odd">
<td>MOTHERS MAIDEN NAME (#6)</td>
<td>Mother’s Surname at her birth.</td>
</tr>
<tr class="even">
<td>DATE OF BIRTH (#7)</td>
<td>Date of person's birth.</td>
</tr>
<tr class="odd">
<td>PLACE OF BIRTH CITY (#8)</td>
<td><p>Name of the city or town (or nearest) where the person was born.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="even">
<td>PLACE OF BIRTH STATE (#9)</td>
<td><p>If USA, 2 character state abbreviation. If not USA, the country state. Pointer to the STATE file (#5).</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>PLACE OF BIRTH COUNTRY (#9.1)</td>
<td><p>The PLACE OF BIRTH COUNTRY field identifies the Country that was selected from the available COUNTRY CODE list for where the individual was  born.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="even">
<td>PLACE OF BIRTH PROVINCE (#9.2)</td>
<td><p>The PLACE OF BIRTH PROVINCE field identifies the location within certain countries containing additional divisions of where the individual was born.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>DATE OF DEATH (#10)</td>
<td><p>The date of the person's death.</p>
<p>As of Patch MPI*1*90, Increment 7, Date of Death will be on the Primary View when supplied from one of NCA’s systems, BOSS, or AMAS. Date of Death <em><u>will not</u></em> be synched from PV to the correlations for Increment 8.</p></td>
</tr>
<tr class="even">
<td>DEATH VERIFICATION STATUS (#11)</td>
<td><p>One of four criteria must exist to flag this as Verified:</p>
<ul>
<li><blockquote>
<p>Patient death under VA auspices</p>
</blockquote></li>
<li><blockquote>
<p>DoD casualty report</p>
</blockquote></li>
<li><blockquote>
<p>Receipt of certified death certificate</p>
</blockquote></li>
<li><blockquote>
<p>Burial benefits by NCS</p>
</blockquote></li>
</ul>
<p>NOTE: Not currently populated on the MPI.</p></td>
</tr>
<tr class="odd">
<td>GENDER (#12)</td>
<td><ul>
<li><blockquote>
<p>M = MALE</p>
</blockquote></li>
<li><blockquote>
<p>F = FEMALE</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>SOCIAL SECURITY NUMBER (#13)</td>
<td><p>Patient’s Social Security Number (SSN)</p>
<p>NOTE: Pseudo SSNs aren't stored on the MPI.</p></td>
</tr>
<tr class="odd">
<td><p>SSN VERIFICATION STATUS (#14)</p>
<p>NOTE: Added to File #985 as of Patch MPI*1*40. Populated to the Primary View of the MPI and systems of interest to the MPI as of DG*5.3*688 [EVC R2].</p></td>
<td><p>Status of the verification of a person's SSN. This value is stored on the MVI, derived from an update from the ESR application after interaction with SSA (Social Security Administration). Possible values synchronized to sites are:</p>
<ul>
<li><blockquote>
<p>Null</p>
</blockquote></li>
<li><blockquote>
<p>INVALID PER SSA</p>
</blockquote></li>
<li><blockquote>
<p>VERIFIED</p>
</blockquote></li>
</ul>
<p>Possible values used on the MVI for the ESR correlation are:</p>
<ul>
<li><blockquote>
<p>NEW RECORD</p>
</blockquote></li>
<li><blockquote>
<p>IN-PROCESS</p>
</blockquote></li>
<li><blockquote>
<p>INVALID PER SSA</p>
</blockquote></li>
<li><blockquote>
<p>RESEND TO SSA</p>
</blockquote></li>
<li><blockquote>
<p>VERIFIED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><p>PSEUDO SSN REASON (#14.1)</p>
<p>NOTE: Added to File #985 as of Patch MPI*1*40. Populated to the Primary View of the MPI and systems of interest to the MPI as of RG*1*47 and DG*5.3*653 [EVC R1].)</p></td>
<td><p>Used to document the reason an individual was assigned a pseudo SSN. Available reasons are:</p>
<ul>
<li><blockquote>
<p>(R) Refused to Provide—Individual was asked for his/her SSN but refused to provide the number.</p>
</blockquote></li>
<li><blockquote>
<p>(S) SSN Unknown/Follow-up required—Individual is not available to ask/answer the request for SSN. The facility should initiate follow-up activity to obtain the SSN.</p>
</blockquote></li>
<li><blockquote>
<p>(N) No SSN Assigned—Individual has not been assigned an SSN. This generally applies to spouse or dependents of veterans who are not US citizens, and infrequently, non-citizen beneficiaries.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>CLAIM NUMBER (#15)</td>
<td>VBA assigned claim number.  Used to assist confirming ID.</td>
</tr>
<tr class="even">
<td>COORDINATING MASTER OF RECORD (#16)</td>
<td>Pre-Primary View Coordinating Site for patient. POINTER TO INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td>SENSITIVITY (#17)</td>
<td><p>Sensitivity is used to assist in sensitive management audit reports for unusual activity.</p>
<p>NOTE:  This field is not utilized.</p></td>
</tr>
<tr class="even">
<td>PRIMARY ICN (#18)</td>
<td>As of patch MPI*1.0*40, this field will be used as the value of the Primary ICN for a deactivated ICN. The field will only be populated for an entry that has an ID STATE of deactivated. It is basically telling which ICN should be used instead.</td>
</tr>
<tr class="odd">
<td>DATE/TIME OF ORIGINAL CREATION (#19)</td>
<td>Date/time that the person was added to the MPI VETERAN/CLIENT (#985) file.  This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</td>
</tr>
<tr class="even">
<td>FACILITY OF ORIGINAL CREATION (#20)</td>
<td>Facility that originally added the person to the MPI VETERAN/CLIENT (#985) file.  This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</td>
</tr>
<tr class="odd">
<td>CREATED BY (#21)</td>
<td>The CREATED BY field identifies the person at the FACILITY OF ORIGINAL CREATION who added the person to the MPI VETERAN/CLIENT (#985) file. This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</td>
</tr>
<tr class="even">
<td>RESOLUTION JOURNAL CASE NUMBER (#22)</td>
<td>If a case exists in the MPI DATA MGT RESOLUTION JOURNAL file (#985.2) for this ICN it will be stored in this field regardless of the status of the case.  Resolution Journal cases hold the history of any resolution work done by the Healthcare Identity Management (HC IdM) on this ICN.</td>
</tr>
<tr class="odd">
<td>PRIMARY VIEW DATE LAST UPDATED (#23)</td>
<td>The PRIMARY VIEW DATE LAST UPDATED field is the date/time that any of the person's identity element fields were last updated in the MPI VETERAN/CLIENT (#985) file.</td>
</tr>
<tr class="even">
<td>IDENTITY THEFT (#24)</td>
<td>The IDENTITY THEFT field is used to designate that a specific record has been confirmed by Health Care Identity Management (HC IdM) staff to be involved in an identity theft occurrence. Once it has been marked, the IDENTITY THEFT field will prevent good records from being linked or matched to the identify theft record.</td>
</tr>
<tr class="odd">
<td>TEMPORARY ID NUMBER (#25)</td>
<td>The Department of Defense (DoD) Defense Eligibility Enrollment Reporting System (DEERS) uses a Temporary Identification Number for individuals (e.g., babies) who do not have or have not provided a Social Security Number (SSN) when the record is added to DEERS.  It is used for military dependents only. </td>
</tr>
<tr class="even">
<td>FOREIGN ID NUMBER (#26)</td>
<td>The Department of Defense (DoD) Defense Eligibility Enrollment Reporting System (DEERS) uses a Foreign Identification Number for foreign military and foreign nationals when the record is added to DEERS.</td>
</tr>
<tr class="odd">
<td>SELF IDENTIFIED GENDER field (#27)</td>
<td><p>The value of Self Identified Gender specifies the patient’s self-identified gender identity.</p>
<p>NOTE: The PV value will be synched to VHA correlations only. This new field will not be shared to NCA, VBA, DoD or any outside agency/company at this time.</p>
<p>NOTE:As of Patch DG*5.3*902, the menu text display for the field named SELF-IDENTIFIED GENDER was changed to “Self-Identified Gender Identity” in the following MPI/PD options:</p>
<ul>
<li><blockquote>
<p>Patient MPI/PD Data Inquiry</p>
</blockquote></li>
<li><blockquote>
<p>Remote Patient Data Query Menu ...</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>STREET ADDRESS [LINE 1] (#31)</td>
<td><p>First line of person’s residence street address (3-35 characters).</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>STREET ADDRESS [LINE 2] (32#)</td>
<td><p>Second line of person’s residence street address (3-30 characters) if the space provided in "street address" was not sufficient.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td>STREET ADDRESS [LINE 3] (33#)</td>
<td><p>Third line of person’s residence street address (3-30 characters) if the space provided in "street address" and "street address 2" was not sufficient.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>CITY [RESIDENCE] (#34)</td>
<td><p>City in which person resides (3-28 characters).</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td>STATE [RESIDENCE] (#35)</td>
<td><p>State in which person resides.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>ZIP+4 [RESIDENCE] (#36)</td>
<td><p>Five or Nine digit Zip Code.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td>EMAIL ADDRESS (#36.1)</td>
<td>The Email Address (3-50 characters) for receiving electronic correspondence on.</td>
</tr>
<tr class="odd">
<td>PHONE NUMBER [RESIDENCE] (#37)</td>
<td><p>Telephone number (4-23 characters) to person’s place of residence.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td><p>MULTIPLE BIRTH INDICATOR (#39)</p>
<p>NOTE: Added to the list of fields auto-updated in VistA as of Patch RG*1*47.</p></td>
<td><p>The MULTIPLE BIRTH INDICATOR will designate whether or not the person is part of a multiple birth (i.e. to identify twins, etc.). Possible values are:</p>
<ul>
<li><blockquote>
<p>N = NO</p>
</blockquote></li>
<li><blockquote>
<p>Y = MULTIPLE BIRTH</p>
</blockquote></li>
<li><blockquote>
<p>Null (not the same as No)</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>PROVINCE (#40)</td>
<td><p>Enter a PROVINCE if the patient has provided one for his/her foreign address. The entry can be alphanumeric and up to 20 characters in length.</p>
<p>NOTE: As of Patch MPI*1*90, this field was added to the Primary View and is populated from ESR.</p></td>
</tr>
<tr class="even">
<td>POSTAL CODE (#41)</td>
<td><p>Enter the person’s POSTAL CODE if the patient has provided one for his/her foreign address. The entry can be alphanumeric and up to 10 characters in length.  </p>
<p>NOTE: As of Patch MPI*1*90, this field was added to the Primary View and is populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>COUNTRY (#42)</td>
<td><p>Enter the COUNTRY where the person’s permanent address is located.  If entering an Army/Air Force Post Office (APO) or a Fleet Post Office (FPO) address, select United States as the country.</p>
<p>NOTE: As of Patch MPI*1*90, this field was added to the Primary View and is populated from ESR.</p></td>
</tr>
<tr class="even">
<td>ALIAS (#50)</td>
<td>If this person is known by any name other than that entered in the name field enter that/those other name(s) here. (Multiple field)</td>
</tr>
<tr class="odd">
<td>ALIAS SURNAME (#02,.01)</td>
<td><p>Person’s last name (aka family name). If this patient is known by any name other than that entered in the Name field, enter the other name(s) here.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="even">
<td>ALIAS FIRST NAME (#.02,1)</td>
<td><p>Person’s first name.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="odd">
<td>ALIAS MIDDLE NAME (#.02,2)</td>
<td><p>Person’s middle name or middle initial.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="even">
<td>ALIAS PREFIX (#.02,3)</td>
<td><p>Commonly, Dr., Ms., Sir, or other appropriate titles.</p>
<p>NOTE: Not currently populated on the MVI. Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="odd">
<td>ALIAS SUFFIX (#.02,4)</td>
<td><p>Examples are Jr., Sr., PhD, etc.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="even">
<td>ALIAS SSN (#.02,5)</td>
<td><p>If the person was also known under a name other than that listed in the NAME field of the PATIENT file (#2), enter the social security number used if different when the person used this alias. Include any different SSNs used by person even if names are the same.</p>
<p>NOTE: Alias SSNs that are Pseudo SSNs will not be stored on the MVI. Alias SSN is paired with an Alias Name.  There can't be just an alias SSN. Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="odd">
<td>ALIAS DATE LAST UPDATED (#.02,6)</td>
<td>The ALIAS DATE LAST UPDATED field is the date/time that the ALIAS field was last updated in the MPI VETERAN/CLIENT (#985) file.</td>
</tr>
<tr class="even">
<td>RACE INFORMATION (#60)</td>
<td><p>Enter the race that best identifies this person.</p>
<p>NOTE: Not synchronized to the systems of interest. Once in Primary View, will be an aggregated list from all treating facilities. (Multiple field)</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="odd">
<td>RACE INFORMATION (#.03,.01)</td>
<td><p>Enter the races which best identify this patient.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="even">
<td>RACE DATE LAST UPDATED (#.03,1)</td>
<td><p>The RACE DATE LAST UPDATED field is the date/time that the RACE field was last updated in the MPI VETERAN/CLIENT (#985) file.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="odd">
<td>ETHNICITY INFORMATION (#70)</td>
<td><p>Enter the ethnicity that best identifies this person.</p>
<p>NOTE: Not synchronized to the systems of interest. Once in Primary View, will be an aggregated list from all treating facilities. (Multiple field setup but only one value stored)</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="even">
<td>ETHNICITY INFORMATION (#.04,.01)</td>
<td><p>Enter the ethnicity which best identifies this person.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="odd">
<td>ETHNICITY DATE LAST UPDATED (#.04,1)</td>
<td><p>The ETHNICITY DATE LAST UPDATED field is the date/time that the ETHNICITY field was last updated in the MPI VETERAN/CLIENT (#985) file.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="even">
<td>ID STATE (#80)</td>
<td><p>The following ID STATE definitions are from the Object Management Group (OMG) Person Identification Service (PIDS) Specification. ID STATE designates the status of the entry in the MPI VETERAN/CLIENT (#985) file in accordance with business rules and standards. Values for the patient are:</p>
<ul>
<li><p>P = Permanent</p></li>
<li><p>T = Temporary</p></li>
<li><p>D = Deactivated</p></li>
</ul>
<p>PERMANENT: This ID State specifies that all required fields are entered and a national ICN is established. When an ID is created as permanent all mandatory traits <em>must</em> be provided. A permanent ID can be deactivated but <em>cannot</em> be made temporary except for when HC IdM uses the OVR function.</p>
<p>TEMPORARY: This ID State specifies that there are not enough fields to make an entry permanent (as defined further in the business rules). An ID can be created as temporary without indicating any mandatory traits. A common usage is to create an ID that data can be bound to a patient before that patient is identified with an appropriate confidence. A temporary ID can be made permanent or deactivated.</p>
<p>DEACTIVATED: This ID State specifies that the ICN is no longer used. Once an ID is expected not to be needed any more it can be deactivated (merged or deprecated), which keeps it around for historical purposes. A deactivated ID is in its final state and <em>cannot</em> be transitioned to any other state by PIDS operations.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>DATE OF ID STATE (#81)</td>
<td>The DATE OF ID STATE field identifies when the ID STATE field was last updated.</td>
</tr>
<tr class="even">
<td>SURNAME PRIMARY VIEW SCORE (#85)</td>
<td>The SURNAME PRIMARY VIEW SCORE field contains the Primary View Authority Score for the SURNAME (#1) identity element.</td>
</tr>
<tr class="odd">
<td>FIRST NAME PRIMARY VIEW SCORE (#86)</td>
<td>The FIRST NAME PRIMARY VIEW SCORE field contains the Primary View Authority Score for the FIRST NAME (#2) identity element.</td>
</tr>
<tr class="even">
<td>MIDDLE NAME PRIMARY VIEW SCORE (#87)</td>
<td>The MIDDLE NAME PRIMARY VIEW SCORE field contains the Primary View Authority Score for the MIDDLE NAME (#3) identity element.</td>
</tr>
<tr class="odd">
<td>PREFIX PRIMARY VIEW SCORE (#88)</td>
<td>The PREFIX PRIMARY VIEW SCORE field contains the Primary View Authority Score for the NAME PREFIX (#4) identity element. Not currently populated on the MVI.</td>
</tr>
<tr class="even">
<td>SUFFIX PRIMARY VIEW SCORE (#89)</td>
<td>The SUFFIX PRIMARY VIEW SCORE field contains the Primary View Authority Score for the NAME SUFFIX (#5) identity element</td>
</tr>
<tr class="odd">
<td>DOB PRIMARY VIEW SCORE (#90)</td>
<td>The DOB PRIMARY VIEW SCORE field contains the Primary View Authority Score for the DATE OF BIRTH (#7) identity element.</td>
</tr>
<tr class="even">
<td>GENDER PRIMARY VIEW SCORE (#91)</td>
<td>The GENDER PRIMARY VIEW SCORE field contains the Primary View Authority Score for the GENDER (#12) identity element.</td>
</tr>
<tr class="odd">
<td>SSN PRIMARY VIEW SCORE (#92)</td>
<td>The SSN PRIMARY VIEW SCORE field contains the Primary View Authority Score for the SOCIAL SECURITY NUMBER (#13) identity element.</td>
</tr>
<tr class="even">
<td>MMN PRIMARY VIEW SCORE (#95)</td>
<td>The MMN PRIMARY VIEW SCORE field contains the Primary View Authority Score for the MOTHER'S MAIDEN NAME (#6) identity element.</td>
</tr>
<tr class="odd">
<td>MULT BIRTH PRIMARY VIEW SCORE (#96)</td>
<td>The MULT BIRTH PRIMARY VIEW SCORE field contains the Primary View Authority Score for the MULTIPLE BIRTH INDICATOR (#39) identity element.</td>
</tr>
<tr class="even">
<td>POB CITY PRIMARY VIEW SCORE (#97)</td>
<td>The POB CITY PRIMARY VIEW SCORE field contains the Primary View Authority Score for the PLACE OF BIRTH CITY (#8) identity element.</td>
</tr>
<tr class="odd">
<td>POB STATE PRIMARY VIEW SCORE (#98)</td>
<td>The POB STATE PRIMARY VIEW SCORE field contains the Primary View Authority Score for the PLACE OF BIRTH STATE (#9) identity element.</td>
</tr>
<tr class="even">
<td>IDENTITY THEFT ACTIVATION (#102)</td>
<td>The IDENTITY THEFT ACTIVATION field is used to determine when a specific record has been confirmed by the Health Care Identity Management (HC IdM) staff to have been involved in an identity theft occurrence.</td>
</tr>
<tr class="odd">
<td>IDENTITY THEFT DEACTIVATION (#103)</td>
<td>The IDENTITY THEFT DEACTIVATION field is used to determine when a specific record has been removed/cleared by the Health Care Identity Management (HC IdM) staff as having been involved in an identity theft occurrence.</td>
</tr>
<tr class="even">
<td>DEATH ENTERED BY (#104)</td>
<td><p>Name of the individual who entered the DATE OF DEATH.</p>
<p>DEATH ENTERED BY is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="odd">
<td>SOURCE OF NOTIFICATION (#105)</td>
<td><p>Specifies who first notified the VA of the patient’s death.</p>
<p>SOURCE OF NOTIFICATION is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="even">
<td>DATE OF DEATH LAST UPDATED (#106)</td>
<td><p>Date/Time the DATE OF DEATH was last updated for the patient.</p>
<p>DATE OF DEATH LAST UPDATED is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="odd">
<td>DEATH LAST EDITED BY (#107)</td>
<td><p>Name of the individual who last edited the DATE OF DEATH.</p>
<p>DEATH LAST EDITED BY is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="even">
<td>SSA VERIFICATION STATUS (#108)</td>
<td>The SSA VERIFICATION STATUS field identifies the current state of the record.</td>
</tr>
<tr class="odd">
<td>ID INTEROPERABLTY PERSON TYPE (#109)</td>
<td>The ID INTEROPERABLTY PERSON TYPE field identifies the current interoperability person type of the record.</td>
</tr>
<tr class="even">
<td>LEVEL OF ASSURANCE (#110)</td>
<td><p>The LEVEL OF ASSURANCE field identifies the confidence level of the record as determined by the MyHealtheVet (MHV) application.</p>
<p>The LEVEL OF ASSURANCE values refer to the four identity authentication assurance levels for E-Government transactions, described in “E-Authentication Guidance for Federal Agencies” [OMB 04-04]. The four assurance levels are:</p>
<ul>
<li><p>Level1 : Little or no confidence in the asserted identity’s validity.</p></li>
<li><p>Level2 : Some confidence in the asserted identity’s validity.</p></li>
<li><p>Level3 : High confidence in the asserted identity’s validity.</p></li>
<li><p>Level4 : Very high confidence in the asserted identity’s validity.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>DEATH INDICATOR (Y/N)? (#111)</td>
<td><p>The DEATH INDICATOR (Y/N)? field identifies whether or not an individual has been identified as deceased.</p>
<p>Note: Initially this field will only be identified and populated by site 200IVT (Identity Verify Tool), which correlates to the ‘Experian’ integration work.</p></td>
</tr>
<tr class="even">
<td>NOTIFICATION PROVIDER (#113)</td>
<td>The NOTIFICATION PROVIDER field identifies the current Line of Business (LOB) system that correlated a patient’s date of death.</td>
</tr>
<tr class="odd">
<td>SUPPORTING DOCUMENT TYPE (#114)</td>
<td>The SUPPORTING DOCUMENT TYPE field identifies the current document used to inform of a patient’s date of death from the Line of Business (LOB) system.</td>
</tr>
<tr class="even">
<td>DATE OF DEATH OPTION USED (#115)</td>
<td><p>The DATE OF DEATH OPTION USED field specifies the option used on the Line of Business (LOB) system when editing (adding/updating) a patient’s date of death. Option values include the following:</p>
<ul>
<li><p>JRN_OBJ</p></li>
<li><p>JRN_APP</p></li>
<li><p>JRN_STN</p></li>
<li><p>DEATH ENTRY</p></li>
<li><p>DISCHARGE A PATIENT</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>DISCHARGED DATE/TIME (#116)</td>
<td><p>The DISCHARGED DATE/TIME field identifies the date (time is optional) when a patient was last discharged from the Veteran Affairs Medical Center (VAMC).</p>
<p>DISCHARGED DATE/TIME is identified and populated at the VAMC level and updated on the Master Veteran Index (MVI).</p></td>
</tr>
<tr class="even">
<td>DATE OF DEATH OVERRIDE REASON (#117)</td>
<td><p>The DATE OF DEATH OVERRIDE REASON field specifies the reason for making a change to the date of death on a patient’s record. Reason values included the following:</p>
<ul>
<li><p>DECEASED WHILE INPATIENT</p></li>
<li><p>DEATH CERTIFICATE</p></li>
<li><p>NCA</p></li>
<li><p>VERIFIED VIA BIRLS</p></li>
<li><p>VERIFIED VIA SSA</p></li>
<li><p>DATE OF DEATH CORRECTION</p></li>
<li><p>ENTERED IN ERROR</p></li>
<li><p>IDENTITY THEFT</p></li>
</ul>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>DEATH STATUS (#118)</td>
<td><p>The DEATH STATUS field specifies whether the DATE OF DEATH (#20) value in the correlation [MPI FACILITY ASSOCIATION file #985.5] has successfully passed all of the Primary View (PV business rules to get promoted into PV. Status values include the following:</p>
<ul>
<li><p>PENDING</p></li>
<li><p>VERIFIED</p></li>
</ul></td>
</tr>
<tr class="even">
<td>PERSON TYPE (#150)</td>
<td>The person types that this person is identified by. (Multiple field)</td>
</tr>
<tr class="odd">
<td>PERSON TYPE<br />
(#.054, .01)</td>
<td>The Person Type(s) selected from the available list [MPI PERSON TYPES FILE #985.72] that identifies the current person type(s) of the record.</td>
</tr>
<tr class="even">
<td>PREFERRED NAME (#300)</td>
<td>Specifies the name on how the patient would prefer to be referenced by during interactions at the medical facility.</td>
</tr>
</tbody>
</table>

  
Enhanced MPI-to-VistA Synchronization—Additional Patient Identity Fields54BSSN Verification Status Synchronized to Systems of Interest

The SSN Verification Status is populated on the MVI and broadcast to treating facilities and systems of interest. The field values VERIFIED and INVALID PER SSA are triggered as a result of an update from the ESR application and subsequent update to the Primary View.

The SSN Verification Status is an existing field on the MVI with the current values listed below. In order to bring these values in line with the Enrollment VistA Changes (EVC) requirements and Standard Data Services (SDS) tables as well as support the later migration of data into the Administrative Data Repository (ADR), a change is needed to the internal and external value on the MVI. The current values are listed below; however, only the values of Null, Verified and Invalid Per SSA are synchronized with the sites.

- Null
- New Record
- In-Process
- Invalid Per SSA
- Resend to SSA
- Verified

SSN and Pseudo SSN Reason Synchronized to Systems of Interest

When a VistA instance or Enrollment System Redesign (ESR) updates the Pseudo SSN Reason, the MVI updates the MPI FACILITY ASSOCIATION file (#985.5). If the VistA instance is the Primary View, that value is updated in File \#985 and broadcasted out to all sites.

Multiple Birth Indicator Synchronized to Systems of Interest

As of Patch RG\*1\*45, the MULTIPLE BIRTH INDICATOR field is sent and stored on the MVI; however, it is not synchronized to all of the "systems of interest" (i.e., Treating Facilities). As of Patch RG\*1\*47, the MULTIPLE BIRTH INDICATOR is included in the list of patient identity fields that are synchronized from the MPI out to all systems of interest.

If synchronization of the MULTIPLE BIRTH INDICATOR field fails, an exception is logged on the MVI. This functionality is in support of the Patient Safety Office's effort to reduce the number of local duplicate record merges on records that are related to patients with similar trait values to their siblings.

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/021.png) | NOTE: The Duplicate Record Merge: Patient Merge software has already been modified to display the MULTIPLE BIRTH INDICATOR field value if present. |

  
The ALIAS Multiple Stored on MVI and Synchronized to VistA

In the Primary View of the MVI, the ALIAS multiple (#50) is stored in the MPI VETERAN/CLIENT file (#985) as an aggregated list from all the treating facilities associated with that ICN. In VistA, the ALIAS multiple (#1) is stored in the PATIENT file (#2). All edits made by Healthcare Identity Management (HC IdM) staff to the ALIAS multiple on the MVI via the Edit PV Alias Values \[MPI DATA MGT EDIT PV ALIAS\] option are updated in the Primary View on the MVI and synchronized out to all systems of interest (e.g., VistA treating facilities) for that patient. Site edits to the ALIAS multiple (#1) in the VistA PATIENT file (#2) are updated in VistA and sent to the MVI for updates to the Primary View. The updates are then synchronized back out to all other treating facilities (systems of interest) associated with that ICN.

Process Sequence for Inbound Edits

In the process for updating the Primary View of the MVI, the first check is for potential catastrophic edits to person identity, which is defined as an edit to two or more of the following identity traits:

- Name (First, Last)
- Date Of Birth
- Social Security Number (SSN)
- Gender

If the potential catastrophic edit affects two or more identity traits, an exception is generated that becomes a manual HC IdM catastrophic edit review process. HC IdM processes potential catastrophic edits as follows:

- Accept All
- Reject All
- Partial Accept

If there are no catastrophic edits:

- All fields in Primary View are compared to the inbound data sent for that correlation.
- If there are differences, a series of computations begin to "score" the data to determine if it meets the criteria for acceptance. The Primary View score is based on data captured from a patient encounter with a Veterans Affairs facility (e.g., active prescriptions, admission or registration in the last year, lab test, or radiology exam in the last year).
- The score is then calculated from the data update coming from the site.
- Each field is then evaluated against any fields that are different in the current Primary View to see if the score is equal to or greater than the existing Primary View field's score and that the data update meets the business rules for data validity and integrity.
- Any of the fields, all of the fields, or none of the fields may be updated based upon the scoring and the business rules.

|                                                                                                                |                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/022.png) | NOTE: The MPI FACILITY ASSOCIATION file (#985.5) contains the sites' last update. This correlation should be a duplicate of the same data in the PATIENT file (#2) at the sites. |

Primary View Reject

When person identity fields are edited at VA facilities and sent to the MVI, those edits *must* meet or exceed the existing authority score and pass the Primary View Data Rules on a field-by-field basis. If an edit fails to pass both of these tests, the edit to that person identity field is rejected.

If a site determines that the rejected data is a legitimate edit, the only way to get that data updated on the MVI is to contact the Healthcare Identity Management (HC IdM) team and have them make the edit. HC IdM has the ability to overwrite Primary View data.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/023.png)</td>
<td><p><strong>NOTE:</strong> Healthcare Identity Management (HC IdM) has requested the removal/deletion of Primary View Rejects (PVRs) and PVR functionality. As of Patch RG*1.0*62:</p>
<ul>
<li><p>Exception #234 (Primary View Reject) were no longer be logged.</p></li>
<li><p>A post-init process executed and marked all existing unresolved 234 exceptions as Resolved.</p></li>
<li><p>The menu option MPI/PD Exception Handling [RG EXCEPTION HANDLING] was removed, since it is no longer needed.</p></li>
</ul></td>
</tr>
</tbody>
</table>

HC IdM View/Edit Authority Values for Business Rules Criterion

Healthcare Identity Management (HC IdM) staff can view or edit the current authority values for the Primary View business rules criterion. These authority values weigh and score inbound edits to the person entries on the MVI based on person activity at the site.

Page intentionally left blank for double-sided print copy.

# Software Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Master Patient Index/Patient Demographics (MPI/PD) VistA is a Kernel Installation and Distribution System (KIDS) software release.

### Name and Number Spaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPI/PD software is made up of two applications:

- RG Namespace—File range is 990–995 and 997–999.99.
- MPIF Namespace—File range is 994.

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software (fully patched) *must* be installed at the site:

<span id="_Toc247320308" class="anchor"></span>Table ‑. Applications that need to be installed and fully patched for MPI/PD

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Application</strong></th>
<th><strong>Version # and Patches</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CIRN</td>
<td>Version 0.5 fully patched</td>
</tr>
<tr class="even">
<td>Health Level 7 (HL7) VistA</td>
<td><p>Version 1.6 fully patched</p>
<p>NOTE: Place HL*1.6*39 in Production account only.</p></td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td>Version 8 fully patched</td>
</tr>
<tr class="even">
<td>Kernel Toolkit</td>
<td>Version 7.3 fully patched</td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td>Version 8.0 fully patched</td>
</tr>
<tr class="even">
<td>Master Patient Index/Patient Demographics (MPI/PD)</td>
<td><p>RG Version 1.0 fully patched</p>
<p>MPIF Version 1.0 fully patched</p></td>
</tr>
<tr class="odd">
<td>Pharmacy</td>
<td>If running Computerized Patient Record System (CPRS), fully patched version of Outpatient Pharmacy V. 7.0, and Inpatient V. 5.0.</td>
</tr>
<tr class="even">
<td>PIMS</td>
<td>Version 5.3 fully patched</td>
</tr>
<tr class="odd">
<td>Registration</td>
<td>Version 5.3 fully patched</td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td>Version 22 fully patched</td>
</tr>
</tbody>
</table>

|                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/024.png) | CAUTION: DO NOT INSTALL HL\*1.6\*39 IN ANY TEST ACCOUNT! If you install this patch in your test account, you will link your test account to all the other production accounts. Since there are similarities (e.g., patient names/data) in test and production, it would not be good for data from the test account to be transmitted to the production account at another site. |

|                                                                                                                   |                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/025.png) | CAUTION: RG\* and MPIF\* patches should NOT be installed on legacy systems to avoid issues with the legacy systems ending up as Treating Facilities. |

### Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software does not impose any additional legal requirements on the user. All users are reminded that many of the reports generated by this software contain confidential patient information and *must* be treated accordingly.

### HL7 Application Parameters File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check that the correct Station Number is entered in the FACILITY NAME field (#3) of the HL7 APPLICATION PARAMETER file (#771), Figure 4‑2. Local modifications to your INSTITUTION file (#4) may conflict with MPI/PD installation setup.

<span id="_Ref129786464" class="anchor"></span>Figure ‑. HL7 Application Parameter List

HL7 APPLICATION PARAMETER LIST MAR 15,2000 10:45 PAGE 1

NAME FACILITY NAME

MPIF A29 SERVER 679 \<\<This should be YOUR station number\>\>

MPIF A30 SERVER 679

MPIF LOC/MIS 679

MPIF MPI 679

MPIF-STARTUP 679

MPIF TRIGGER \<\<\< SHOULD NOT be populated

RG ADT \<\<\< SHOULD NOT be populated

RG CIRN 679

RG CIRN ADT \<\<\<\<Should NOT be populated

RG SITE MERGE \<\<\<\<Should NOT be populated

RG SUBSCRIPTION 679

VAFC PIMS 679

VAFC TRIGGER \<\<\<\<Should NOT be populated

### Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RG CIRN DEMOGRAPHIC ISSUES bulletin controls the sending of the following patient related bulletin, Table 4‑4.

<span id="_Ref201559348" class="anchor"></span>Table ‑. RG CIRN DEMOGRAPHIC ISSUES bulletin—REMOTE SENSITIVITY INDICATED

|                              |                                                                               |                                     |
|------------------------------|-------------------------------------------------------------------------------|-------------------------------------|
| Patient Related Bulletin | Cause                                                                     | Action to take                  |
| REMOTE SENSITIVITY INDICATED | Patient is marked as sensitive at the sending site but not at receiving site. | No action: message is informational |

### MPI/PD Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc247320310" class="anchor"></span>Table ‑. Mail Groups exported in the MPI/PD package

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Mail Group</strong></th>
<th><strong>Suggested Coordinator</strong></th>
<th><strong>Suggested Members</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>HL7 SITE POC (ON FORUM)</td>
<td>Personnel who monitor MPI/PD HL7 problems.</td>
<td>Personnel who monitor MPI/PD HL7 problems.</td>
<td>This mail group is for personnel who will address HL7 issues.</td>
</tr>
<tr class="even">
<td>MPIF EXCEPTIONS</td>
<td>Messages are sent to the MVI Exception Handler on the MVI. There shouldn’t be any local members in this mail group.</td>
<td>Messages are sent to the remote mail group REDACTED, which is the Exception Handler on the MPI in Austin.</td>
<td>MVI Exception Messages to be addressed are sent to this mail group. These messages are all technical in nature, involving problems with HL7 messages or ICNs not found. There normally isn’t anything the site can do about these, so these messages are sent to a remote mail group. This mail group is used by MVI site point of contacts to send the Healthcare Identity Management (HC IdM) team potential duplicates, questions, issues, etc. This is a local VistA mail group forwarded to the CIRN EXCEPTION MGT mail group on FORUM. If necessary, the remote mail group members will contact the site for assistance.</td>
</tr>
<tr class="odd">
<td>RG CIRN DEMOGRAPHIC ISSUES</td>
<td>Health Administration Service (HAS)/MPI/PD Coordinator</td>
<td><p>Personnel that deal with patient data.</p>
<p>NOTE: IRM personnel will be required to use MailMan utilities to add members to the RG CIRN DEMOGRAPHIC ISSUES.</p></td>
<td><p>This mail group should contain person(s) responsible for ensuring the integrity of the Patient Information Management Systems (PIMS) data. The members of this group will be notified upon login that there are patients awaiting review.</p>
<p>NOTE: Upon logon to the system, members of the RG CIRN DEMOGRAPHIC ISSUES Mail Group now only see the one notification alerting users if there are Primary View Reject exceptions that need to be reviewed (Potential Matches Returned are obsolete).</p></td>
</tr>
<tr class="even">
<td>RG CIRN HL7 PROBLEMS</td>
<td>Personnel who monitor MPI/PD HL7 problems.</td>
<td>Personnel who monitor MPI/PD HL7 problems.</td>
<td>This mail group receives notification of problems that CIRN (MPI/PD) has when interacting with the VistA HL7 package.</td>
</tr>
</tbody>
</table>

Page intentionally left blank for double-sided print copy.

# MPI/PD Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the menus and options comprising the MPI/PD. These options should be made accessible to authorized IRM, Program Application Specialists (PAS), site MPI POCs, and/or Coordinators, etc., and VA facility personnel who will be involved in working with the MPI/PD.

## MPI/PD Master Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPI/PD Master Menu is the primary menu that contains all Master Patient Index/ Patient Demographics (MPI/PD) menus and sub-menus.

|                                                                                                                |                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/026.png) | NOTE: Sub-menus should be assigned to users as appropriate and are described in the *MPI/PD Implementation Guide*. |

<span id="_Toc26665836" class="anchor"></span>Figure ‑. MPI/PD Master Menu

Select OPTION NAME: MPI/PD Master Menu \<Enter\> RGMGR MPI/PD Master Menu

CORD MPI/PD Patient Admin Coordinator Menu ...

IRM MPI/PD IRM Menu ...

Select MPI/PD Master Menu Option:

The following menus comprise the MPI/PD (listed in the order that they appear on the MPI/PD Master Menu):

- MPI/PD Patient Admin Coordinator Menu
- MPI/PD IRM Menu

Each menu and its associated options are described in detail in the topics that follow in this chapter.

  
MPI/PD Patient Admin Coordinator Menu

The MPI/PD Patient Admin Coordinator Menu \[RG ADMIN COORD MENU\] options allow users to monitor and update person data. Figure 5‑2 shows the menus and options that are located on this menu.

<span id="_Ref121908355" class="anchor"></span>Figure ‑. MPI/PD Patient Admin Coordinator Menu

Select MPI/PD Master Menu Option: cord\<Enter\> MPI/PD Patient Admin Coordinator Menu

LOG Patient Audit Log Reports ...

MSG Message Exception Menu ...

RPT Management Reports ...

TK ToolKit POC User Setup

Select MPI/PD Patient Admin Coordinator Menu Option:

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/027.png) | NOTE: The Point of Contact (POC) add/edit functionality for the Add/Edit Point of Contact, \[RG UPDATE POINT OF CONTACT\], menu option was migrated to the ToolKit (TK) graphical user interface (GUI). The VistA process will no longer be accessible to users, as the option will be removed from the MPI/PD Patient Admin Coordinator Menu option, \[RG ADMIN COORD MENU\], and will also be placed out of order with the message: Obsolete with MPIF\*1.0\*59 (the out of order message indicates it’s obsolete in VistA, only.). Complete removal of this functionality from the VistA system will take place at a later date. |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/028.png)</td>
<td><strong>NOTE:</strong> For more information on the MPI/PD Patient Admin Coordinator Menu, please refer to the "<br />
MPI/PD Patient Admin Coordinator Menu" topic in the "MPI/PD Master Menu" section of the documentation.</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/029.png) | NOTE: The active options shown on this menu are described in the topics that follow in this chapter. |

MPI/PD IRM Menu

The MPI/PD IRM Menu provides Information Resource Management (IRM) personnel with the options needed to maintain the Master Patient Index/Patient Demographics (MPI/PD) software. Figure 5‑3 shows the options that are located on this menu.

<span id="_Ref121908686" class="anchor"></span>Figure ‑. MPI/PD IRM Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select MPI/PD Master Menu Option: <strong>IRM</strong> &lt;<strong>Enter&gt;</strong> MPI/PD IRM Menu</p>
<p>Link and Process Status Display</p>
<p>Unresolved Exception Summary</p>
<p>Select MPI/PD IRM Menu Option:</p></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/030.png) | NOTE: For more information on the MPI/PD IRM Menu, please refer to the "MPI/PD IRM Menu" topic in the "MPI/PD Master Menu" section of the documentation. |

### MPI/PD Patient Admin Coordinator Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPI/PD Patient Admin Coordinator Menu \[RG ADMIN COORD MENU\] options allow the monitoring of person data activities.

<span id="_Toc247320247" class="anchor"></span>Figure ‑. MPI/PD Patient Admin Coordinator Menu

Select MPI/PD Master Menu Option: cord\<Enter\> MPI/PD Patient Admin Coordinator Menu

LOG Patient Audit Log Reports ...

MSG Message Exception Menu ...

RPT Management Reports ...

TK ToolKit POC User Setup

Select MPI/PD Patient Admin Coordinator Menu Option:

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/031.png) | NOTE: The Point of Contact (POC) add/edit functionality for the Add/Edit Point of Contact, \[RG UPDATE POINT OF CONTACT\], menu option was migrated to the ToolKit (TK) graphical user interface (GUI). The VistA process will no longer be accessible to users, as the option will be removed from the MPI/PD Patient Admin Coordinator Menu option,\[RG ADMIN COORD MENU\], and will also be placed out of order with the message: Obsolete with MPIF\*1.0\*59 (the out of order message indicates it’s obsolete in VistA, only.). Complete removal of this functionality from the VistA system will take place at a later date. |

|                                |                             |
|--------------------------------|-----------------------------|
| Patient Audit Log Reports… | \[RG TRAN/AUD AUD REP\] |

The Patient Audit Log Reports menu contains two options for reviewing information stored in the AUDIT file (#1.1) for fields being audited in the PATIENT file (#2). Options allow the user to view:

- All audited fields
- Selected fields for a date range
- All audited data on a single patient

<span id="_Toc26665842" class="anchor"></span>Figure ‑. Patient Audit Log Reports Menu

Select MPI/PD Master Menu Option: cord\<Enter\> MPI/PD Patient Admin Coordinator Menu

LOG Patient Audit Log Reports ...

MSG Message Exception Menu ...

RPT Management Reports ...

TK ToolKit POC User Setup

Select MPI/PD Patient Admin Coordinator Menu Option: LOG\<Enter\> Patient Audit Log Reports

Patient Audit File Print

Single Patient Audit File Print

Select Patient Audit Log Reports Option:

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/032.png) | NOTE: The Point of Contact (POC) add/edit functionality for the Add/Edit Point of Contact, \[RG UPDATE POINT OF CONTACT\], menu option is being migrated to the ToolKit (TK) graphical user interface (GUI). The VistA process will no longer be accessible to users, as the option will be removed from the MPI/PD Patient Admin Coordinator Menu option,\[RG ADMIN COORD MENU\], and will also be placed out of order with the message: Obsolete with MPIF\*1.0\*59 (the out of order message indicates it’s obsolete in VistA, only.). Complete removal of this functionality from the VistA system will take place at a later date. |

|                              |                          |
|------------------------------|--------------------------|
| Patient Audit File Print | \[RGMT AUDIT PRINT\] |

This option prints a customized report of information stored in the AUDIT file (#1.1) for fields being audited in the PATIENT file (#2).  For a specified date range, you can view all audited fields or selected fields. You can also opt to print only edits that were done by a specific user.

- If selected fields are viewed, you can choose to see data for all or selected persons.
- If ALL audited fields are viewed, you must choose persons to examine.

If selected fields are viewed, you can choose to see data for all or selected persons. If you only enter one name and there is no audit data on the selected date range, you are told this on the printout. If multiple names are entered, it only prints those that have had an audit in the selected date range. The other names are not displayed on the report (i.e., there is no message indicating there was no audit data).

As of Patch RG\*1.0\*60, changes have been made to the Patient Audit File Print and Single Patient Audit File Print options on the Patient Audit Log Reports menu.  ALIAS data was not displayed on these reports because the process did not handle multiple field values from the AUDIT file (#1.1).  Multiples are stored differently in the AUDIT global.  Modifications have been made to accommodate the AUDIT data for multiple subfields within the PATIENT file (#2), specifically the ALIAS subfield (2.01), ALIAS (.01) and ALIAS SSN (#1) fields.

Print report for ALL audited fields for a single patient

As of Patch RG\*1.0\*60, Alias audits are displayed.

<span id="_Toc510586927" class="anchor"></span>Figure ‑. Patient Audit File Print for all fields

Do you want to see (A)LL or (S)ELECTED audited fields? A// ALL

Select PATIENT: MVIPATIENT,ALLDAT JOE\<Enter\> 7-3-12    666109826     NO     NSC VETERAN     

Select PATIENT: \<Enter\>

Enter date range for data to be included in report.

Beginning Date:  3 1 17\<Enter\> (MAR 01, 2017)

Ending Date:  N\<Enter\> (APR 15, 2017)

Do you want to find only the edits made by a specific user? No// \<Enter\>  NO

The right margin for this report is 80.

PATIENT AUDIT LIST at VAMCSITE on Apr 15, 2017@18:04                      Page: 1

Date Range: Mar 01, 2017 to Apr 15, 2017

Date/Time Edited    Field Edited                   Edited By

                    Old Value / New Value

   Option/Protocol

--------------------------------------------------------------------------------

==\> MVIPATIENT,ALLDAT JOE  (DFN \#100003476)

Mar 01, 2017@15:12  NAME                           MVIUSER,MICHAEL

                    MVIPATIENT,ALLDAT / MVIPATIENT,ALLDAT JOE

   HL TASK RESTART/MPIF ADT-A31 CLIENT

Mar 01, 2017@15:12  TEMPORARY ID NUMBER            MVIUSER,MICHAEL

                    \<no previous value\> / 873092766

   HL TASK RESTART/MPIF ADT-A31 CLIENT

Mar 01, 2017@15:12  FOREIGN ID NUMBER              MVIUSER,MICHAEL

                    \<no previous value\> / 999092767

   HL TASK RESTART/MPIF ADT-A31 CLIENT

Mar 01, 2017@15:12  TEMPORARY ID NUMBER            MVIUSER,MICHAEL

                    873092766 / 873092766

   HL TASK RESTART/MPIF ADT-A31 CLIENT

Mar 01, 2017@15:12  FOREIGN ID NUMBER              MVIUSER,MICHAEL

                    999092767 / 999092767

   HL TASK RESTART/MPIF ADT-A31 CLIENT

Apr 15, 2017@15:17  ALIAS                          MVIUSER,CHRISTINE

                    \<no previous value\> / MVIPATIENT,DATALL

Apr 15, 2017@15:17  ALIAS SSN                      MVIUSER,CHRISTINE

                    \<no previous value\> / 666220000

Print report for specified audited fields for a single patient

As of Patch RG\*1.0\*60, the Alias fields are selectable and Alias audits are displayed.

<span id="_Ref485294458" class="anchor"></span>Figure ‑. Patient Audit File Print for selected fields

Do you want to see (A)LL or (S)ELECTED audited fields? A// SELECTED

Select a LIST NUMBER from the audited field(s) in the PATIENT file:

1\. 2,.01 NAME

2\. 2,.02 SEX

3\. 2,.024 SELF IDENTIFIED GENDER

4\. 2,.03 DATE OF BIRTH

5\. 2,.05 MARITAL STATUS

6\. 2,.08 RELIGIOUS PREFERENCE

7\. 2,.09 SOCIAL SECURITY NUMBER

8\. 2,.0931 PLACE OF BIRTH COUNTRY

9\. 2,.0932 PLACE OF BIRTH PROVINCE

10\. 2,.111 STREET ADDRESS \[LINE 1\]

11\. 2,.1112 ZIP+4

12\. 2,.112 STREET ADDRESS \[LINE 2\]

13\. 2,.113 STREET ADDRESS \[LINE 3\]

14\. 2,.114 CITY

15\. 2,.115 STATE

16\. 2,.117 COUNTY

17\. 2,.1171 PROVINCE

18\. 2,.1172 POSTAL CODE

Type \<Enter\> to continue or '^' to exit:

Select a LIST NUMBER from the audited field(s) in the PATIENT file:

19\. 2,.1173 COUNTRY

20\. 2,.131 PHONE NUMBER \[RESIDENCE\]

21\. 2,.132 PHONE NUMBER \[WORK\]

22\. 2,.1411 CONFIDENTIAL STREET \[LINE 1\]

23\. 2,.211 K-NAME OF PRIMARY NOK

24\. 2,.219 K-PHONE NUMBER

25\. 2,.2403 MOTHER'S MAIDEN NAME

26\. 2,.2405 PREFERRED NAME

27\. 2,.301 SERVICE CONNECTED?

28\. 2,.302 SERVICE CONNECTED PERCENTAGE

29\. 2,.31115 EMPLOYMENT STATUS

30\. 2,.313 CLAIM NUMBER

31\. 2,.323 PERIOD OF SERVICE

32\. 2,.351 DATE OF DEATH

33\. 2,.352 DEATH ENTERED BY

34\. 2,.353 SOURCE OF NOTIFICATION

35\. 2,.354 DATE OF DEATH LAST UPDATED

36\. 2,.355 LAST EDITED BY

Type \<Enter\> to continue or '^' to exit:

Select a LIST NUMBER from the audited field(s) in the PATIENT file:

37\. 2,.357 SUPPORTING DOCUMENT TYPE

38\. 2,.358 DATE OF DEATH OPTION USED

39\. 2,.361 PRIMARY ELIGIBILITY CODE

40\. 2,391 TYPE

41\. 2,991.01 INTEGRATION CONTROL NUMBER

42\. 2,991.02 ICN CHECKSUM

43\. 2,991.03 COORDINATING MASTER OF RECORD

44\. 2,991.04 LOCALLY ASSIGNED ICN

45\. 2,991.05 SUBSCRIPTION CONTROL NUMBER

46\. 2,991.06 CMOR ACTIVITY SCORE

47\. 2,991.07 SCORE CALCULATION DATE

48\. 2,991.08 TEMPORARY ID NUMBER

49\. 2,991.09 FOREIGN ID NUMBER

50\. 2,991.1 FULL ICN

51\. 2,994 MULTIPLE BIRTH INDICATOR

52\. 2,1901 VETERAN (Y/N)?

53\. 2.01,.01 ALIAS

54\. 2.01,1 ALIAS SSN

Type \<Enter\> to continue or '^' to exit:

Select a LIST NUMBER from the audited field(s) in the PATIENT file:

55\. 2.0991,.01 FULL ICN HISTORY

56\. 2.0992,.01 ICN HISTORY

Select list number 1-56: 49 \<Enter\>

Select list number 1-56: 53 \<Enter\>

Select list number 1-56: 54 \<Enter\>

Select list number 1-56: 

Do you want to see audited data for (A)LL or (S)ELECTED patients? S// SELECTED

Select PATIENT: MVIPATIENT,ALLDAT JOE\<Enter\>  7-3-12    666109826     NO     NSC VETERAN     

Select PATIENT:  \<Enter\>

Enter date range for data to be included in report.

Beginning Date: 3 1 13\<Enter\> (MAR 01, 2017)

Ending Date: N\<Enter\> (APR 15, 2017)

Do you want to find only the edits made by a specific user? No// NO

The right margin for this report is 80.

PATIENT AUDIT LIST at VAMCSITE on Apr 15, 2017@18:03                      Page: 1

Date Range: Mar 01, 2017 to Apr 15, 2017

Date/Time Edited    Field Edited                   Edited By

                    Old Value / New Value

   Option/Protocol

--------------------------------------------------------------------------------

==\> MVIPATIENT,ALLDAT JOE  (DFN \#100003476)

Mar 01, 2012@15:12  FOREIGN ID NUMBER              MVIUSER,MICHAEL

                    \<no previous value\> / 999092767

   HL TASK RESTART/MPIF ADT-A31 CLIENT

Mar 01, 2012@15:12  FOREIGN ID NUMBER              MVIUSER,MICHAEL

                    999092767 / 999092767

   HL TASK RESTART/MPIF ADT-A31 CLIENT

May 23, 2012@15:17  ALIAS                          MVIUSER,CHRISTINE

                    \<no previous value\> / MVIPATIENT,DATALL

May 23, 2012@15:17  ALIAS SSN                      MVIUSER,CHRISTINE

                    \<no previous value\> / 666123400

|                                     |                           |
|-------------------------------------|---------------------------|
| Single Patient Audit File Print | \[RGMT AUDIT SINGLE\] |

This option prints information from the AUDIT file (#1.1) for a selected patient and date range.

For the PATIENT file (#2) entry selected, the report prints the following:

- Person name
- DFN
- Date/Time the field was edited
- User name who made the change
- Field edited
- Old field value
- New field value.

The option or protocol (if available) will also be displayed.

<span id="_Toc26665845" class="anchor"></span>Figure ‑. Single Patient Audit File Print report

Select PATIENT: MVIPATIENT,ALEX \<Enter\> MVIPATIENT,ALEX 9-2-01 666437773 YES SC VETERAN

Enter date range for data to be included in report.

Beginning Date: T-45 \<Enter\> (JUN 01, 2017)

Ending Date: T \<Enter\> (JUL 16, 2017)

The right margin for this report is 80.

DEVICE: HOME// \<Enter\>

PATIENT AUDIT LIST at VAMCSITE on Jul 16, 2012@14:15 Page: 1

Patient: MVIPATIENT,ALEX (DFN \#7169700)

Date Range: Jun 01, 2017 to Jul 16, 2017

Date/Time Edited Field Edited Edited By

Old Value / New Value

Option/Protocol

------------------------------------------------------------------------

June 01, 2017@15:12 FOREIGN ID NUMBER MVIUSER,MICHAEL

999000767 / 999000767

HL TASK RESTART/MPIF ADT-A31 CLIENT

June 23, 2017@15:17 ALIAS MVIUSER,CHRISTINE

\<no previous value\> / CML,DATALL

June 23, 2017@15:17 ALIAS SSN MVIUSER,CHRISTINE

\<no previous value\> / 666220000

July 01, 2017@09:49 ALIAS MVIUSER,PAULETTE

\<no previous value\> / MVIPATIENT,JOSEPH

DG LOAD PATIENT DATA

|                            |                           |
|----------------------------|---------------------------|
| Message Exception Menu | \[RG EXCEPTION MENU\] |

This menu provides the options listed in Figure 5‑9, used to process MPI/PD Health Level Seven (HL7) message exceptions logged in the CIRN HL7 EXCEPTION LOG file (#991.1).

<span id="_Ref130013752" class="anchor"></span>Figure ‑. MPI/PD Exception Handling menu

Select MPI/PD Patient Admin Coordinator Menu Option: MSG \<Enter\> Message Exception Menu

Patient MPI/PD Data Inquiry

Remote Patient Data Query Menu ...

Display Only Query

Primary View Display from MPI

Select Message Exception Menu Option:

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/033.png)</td>
<td><p><strong>NOTE:</strong> Healthcare Identity Management (HC IdM) has requested the removal/deletion of Primary View Rejects (PVRs) and PVR functionality. As of Patch RG*1.0*62:</p>
<ul>
<li><p>Exception #234 (Primary View Reject) were no longer be logged.</p></li>
<li><p>A post-init process executed and marked all existing unresolved 234 exceptions as Resolved.</p></li>
<li><p>The menu option MPI/PD Exception Handling [RG EXCEPTION HANDLING] was removed, since it is no longer needed.</p></li>
</ul></td>
</tr>
</tbody>
</table>

  
Primary View Authority Score Criteria and Data Rules for Evaluating Data Quality

When person identity fields are edited at VA facilities and sent to the MVI, they *must* meet or exceed the existing authority score and pass the Primary View business rules on a field-by-field basis. The following are links to two spreadsheets developed by the Healthcare Identity Management (HC IdM) staff for the criteria for computing the Primary View authority scores and the Primary View data rules:

- Scoring of Primary View data is based on criteria captured from person encounters with VA facilities. These are authority score values, the criteria of which are weighted in such a way that the site's edits to the MVI are measured and calculated on a field-by-field basis. The resulting value needs to meet or exceed the current authority score to have enough weight to change the Primary View*.* If the site making the edit has activity with the patient, validated based on authority score calculations and criterion matches proving that the patient is being seen at that site, their score will be high enough to make an edit to that identity trait. These events indicate where the patient is actively seen. This is considered the authoritative site.
- The Primary View Data Rules regulate entering data in specific formats for which users *cannot* violate. The goal of which is to improve the quality of data. These conditions that are different for each identity trait have to be met before a patient identity field can be edited.

|                                                                                                                |                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/034.png) | NOTE: The HC IdM team is also an authoritative source for Primary View data and can override any data on the MVI. |

VA Facilities Can View the Primary View Data on the MVI

VA facilities have the ability to remotely view Primary View patient identity fields on the MVI. The report generated by this option displays the current activity scores for individual patient identity fields (i.e., Primary View of the MVI) and the Primary View data fields. VA facilities send a remote query to the MVI to view the MVI Primary View information. The same capability to examine this data is available in the option named Primary View Display from MPI \[RG PRIMARY VIEW FROM MPI\], located on the Message Exception Menu \[RG EXCEPTION MENU\].

The Primary View Display from MPI option offers VA facilities the ability to send remote queries to the MPI to view patient identity data.

|                                                                                                                |                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/035.png) | NOTE: For information on VA facilities' the ability to send remote queries to the MVI to view person identity data regardless if there is an exception logged for the person, see the documentation for the option "Primary View Display from MPI \[RG PRIMARY VIEW FROM MPI\]" location in this manual. |

Patch RG\*1\*43 Retired the Following Exception Types:

- Potential Match
- Missing Required Fields
- SSN Mismatch or Name Mismatch

Patch RG\*1\*43 also resulted in all local ICNs being sent to the MVI for ICN assignment the next time the Local/Missing ICN Resolution Background Job \[MPIF LOC/MIS ICN RES\] job ran. Any new potential match exceptions logged were a result of the person being presented to the MVI under the new enumeration process.

Patients that had these pending exceptions were sent up to the MVI for ICN assignment under the new business process and were assigned an ICN (either new one or matched to an existing person on the MVI). If a potential match was found, a potential match exception was also logged for review by the local VistA staff.

|                                 |                                 |
|---------------------------------|---------------------------------|
| Patient MPI/PD Data Inquiry | \[RG EXCEPTION TF INQUIRY\] |

This report prints MPI/PD data for a selected person. You can perform the person lookup using the person name, SSN, or ICN. Information displayed includes data pulled from the PATIENT file (#2) and TREATING FACILITY LIST file (#391.91), such as:

- Integration Control Number (ICN)
- Person Identifying Data
- Treating Facility list

The full Integration Control Number (ICN) is displayed, which is comprised of the following data from the PATIENT file (#2):

- INTEGRATION CONTROL NUMBER field (#991.01)
- separated by a "V"
- ICN CHECKSUM field (#991.02)

Example: 1008000002V340972

DG Patch enhancements over the years have added the following fields to the person identifying information displayed in the Local VistA MPI Patient Data Inquiry (PDAT) option:

- PATIENT file (#2)
- SELF IDENTIFIED GENDER (#.024) PATIENT file (#2)
- PERIOD OF SERVICE (#.323) PATIENT file (#2)
- POW STATUS INDICATED? (#.525) PATIENT file (#2)
- RACE INFORMATION (subfile \#2.02) PATIENT file (#2)
- ETHNICITY INFORMATION (subfile \#2.06) PATIENT file (#2)
- MULTIPLE BIRTH INDICATOR (#994) PATIENT file (#2)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/036.png)</td>
<td><p><strong>NOTE:</strong> As of Patch DG*5.3*876, the following fields were added to the Local VistA MPI Patient Data Inquiry (PDAT) option display. These fields are viewable only if they contain a value, i.e., if the value is <em><u>not</u></em> null.</p>
<ul>
<li><p>SELF IDENTIFIED GENDER (#.024)</p></li>
<li><p>PERIOD OF SERVICE (#.323).</p></li>
</ul></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/037.png) | NOTE: Enhancements were added to this option in Patch DG\*5.3\*505 to display the MULTIPLE BIRTH INDICATOR (#994), POW STATUS INDICATED? (#.525), RACE INFORMATION (subfile \#2,.01), and ETHNICITY INFORMATION (#6) subfile (#2.06). These fields have been added in support of the MPI Austin; the Healthcare Identity Management team needs facility information to improve data quality and to resolve differences on the MPI. |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/038.png)</td>
<td><p><strong>NOTE:</strong> The following enhancements were added to this option as of Patch DG*5.3*707:</p>
<ul>
<li><p>Display SSN Verification and Pseudo SSN Reason.</p></li>
<li><p>Remove the call to calculate CMOR score and remove the display of CMOR Score and Subscription Control Number.</p></li>
<li><p>Modify format of display.</p></li>
</ul></td>
</tr>
</tbody>
</table>

  
Print MPI/PD Data for Patient With Self-Identified Gender Identity and Period of Service displayed

<span id="_Ref499742231" class="anchor"></span>Figure ‑. Patient MPI/PD Data Inquiry─Example of inquiry showing patient with Self-Identified Gender Identity and Period of Service displayed

Select OPTION NAME: Patient MPI/PD Data Inquiry \<Enter\> RG EXCEPTION TF INQUIRY Patient MPI/PD Data Inquiry

Patient MPI/PD Data Inquiry

This report prints MPI/PD Data for a selected patient. The

information displayed includes the Integration Control Number

(ICN), patient identity information, and Treating Facility list.

The information is pulled from the Patient (#2) file and the

Treating Facility List (#391.91) file.

Patient lookup can be done by Patient Name/SSN or by ICN.

Select PATIENT: MVIPATIENT,ARRON \<Enter\> ALIAS MVIPATIENT,ERRIN WILLS 7-3-12 666109826 NO NSC VETERAN

DEVICE: HOME// \<Enter\> UCX/TELNET \<Enter\>

MPI/PD Data for: MVIPATIENT,ERRIN WILLS (DFN \#100003476)

Printed May 22, 2014@04:19 at VAMCSITE

===============================================================================

ICN : 1000001953V120008

SSN : 666109826

SSN Verification Status: VERIFIED

Birth Sex : MALE

Claim \# : None

Date of Birth: Jul 03, 1912

Date of Death: FEB 16, 2017@13:41:47

Entered By: MPIUSER,DEBORAH H.

Source of Notification: VAMC INPATIENT DEATH

Last Updated: FEB 16, 2017@13:41:47

Last Edited By: MPIUSER,DEBORAH H.

Supporting Document Type: VAMC EHR INPATIENT DEATH

Option Used: DISCHARGE A PATIENT

Multiple Birth Indicator: NO

DoD Temporary ID Number : 999000766

DoD Foreign ID Number : 999000767

Address:

3456 HALF WAY

ANY TOWN, ALABAMA 12345

Phone \#: 555-555-5555

Self-Identified Gender Identity: Individual chooses not to answer

Treating Facilities: Station: DT Last Treated Event Reason

-------------------- -------- --------------- ------------

VAMCSITE 500 none found none found

Austin Person Service 200PS none found none found

ICN History:

------------

5000002334V680005 - changed JAN 11, 2012@14:02:30

Additional DPT Data for: MVIPATIENT,ERRIN WILLS (DFN \#100003476)

===========================================================

PLACE OF BIRTH \[CITY\] : TAMPA

PLACE OF BIRTH \[STATE\] : FLORIDA

FATHER'S NAME :

MOTHER'S NAME :

MOTHER'S MAIDEN NAME : DERK,

NAME OF PRIMARY NEXT OF KIN :

NEXT OF KIN PHONE NUMBER :

NAME OF DESIGNEE :

EMERGENCY NAME :

MARITAL STATUS : SEPARATED

RELIGIOUS PREFERENCE : CHURCH OF CHRIST

ETHNICITY INFORMATION : NOT HISPANIC OR LATINO

RACE INFORMATION (multiple):

WHITE

PRIMARY ELIGIBILITY CODE : NSC

PATIENT TYPE : NSC VETERAN

VETERAN (Y/N)? : YES

SERVICE CONNECTED PERCENT :

PERIOD OF SERVICE : PERSIAN GULF WAR

POW STATUS INDICATED? :

MILITARY SERVICE (multiple):

Service Branch Service \# Entry DT Separation DT

---------------------------------------------------------

ARMY 999999999 Jan 01, 2000 Jan 01, 2002

ALIAS (multiple):

MVIPATIENT,ARRON ALIAS SSN: 666889999

MVIPATIENT,ERRIN SSN:

PREFERRED NAME : JOHNNIE

DATE ENTERED IN PATIENT FILE : JAN 11, 2012

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/039.png)</td>
<td><blockquote>
<p><strong>NOTE:</strong> As of Patch DG*5.3*902, the menu text display for the field named SELF-IDENTIFIED GENDER was changed to “Self-Identified Gender Identity” in the following MPI/PD options:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Patient MPI/PD Data Inquiry</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Remote Patient Data Query Menu ...</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/040.png) | NOTE: As of Patches DG\*5.3\*902 and RG\*1\*62, the Self-Identified Gender Identity framework is in place; however, a collection point has not yet been established. |

Print MPI/PD Data for Patient With an SSN Verification Status: Verified

<span id="_Ref162766164" class="anchor"></span>Figure ‑. Patient MPI/PD Data Inquiry─Example of inquiry showing patient with an SSN Verification Status: Verified

Select Message Exception Menu Option: Patient MPI/PD Data Inquiry

This report prints MPI/PD Data for a selected patient. The

information displayed includes the Integration Control Number

(ICN), patient identity information, and Treating Facility list.

The information is pulled from the Patient (#2) file and the

Treating Facility List (#391.91) file.

Patient lookup can be done by Patient Name/SSN or by ICN.

Select PATIENT: MVIPATIENT,KENNEDY\<Enter\> 9-16-49 666119999 YES SC VETERAN \*MULTIPLE BIRTH\*

DEVICE: HOME// \<Enter\>

MPI/PD Data for: MVIPATIENT,KENNEDY (DFN \#100000056)

Printed Mar 27, 2007@16:25 at VAMCSITE

===============================================================================

ICN : 1000000440V171717

SSN : 666119999

SSN Verification Status: Verified

Birth Sex : FEMALE

Claim \# : None

Date of Birth: Sep 16, 1949

Multiple Birth Indicator: YES

Address: 1100 MAIN ST

BUTLER, MARYLAND 16001

Treating Facilities: Station: DT Last Treated Event Reason

-------------------- -------- --------------- ------------

VAMCSITE1 553 Sep 17, 2002@13:02 PATIENT ADMISSION

VAMCSITE 500 Sep 17, 2002@12:51 PATIENT DISCHARGE

ICN History:

------------

500000531V909090 - changed SEP 17, 2002@10:58:25

Additional DPT Data for: MVIPATIENT,KENNEDY (DFN \#100000056)

===========================================================

PLACE OF BIRTH \[CITY\] : COLUMBUS

PLACE OF BIRTH \[STATE\] : OHIO

FATHER'S NAME : LAKES,LAND O

MOTHER'S NAME : MVIMOTHER,10

MOTHER'S MAIDEN NAME : MVIMOTHERSMAIDEN,

NAME OF PRIMARY NEXT OF KIN :

NEXT OF KIN PHONE NUMBER :

NAME OF DESIGNEE :

EMERGENCY NAME :

MARITAL STATUS : NEVER MARRIED

RELIGIOUS PREFERENCE : PENTECOSTAL

PRIMARY ELIGIBILITY CODE :

VETERAN (Y/N)? : YES

SERVICE BRANCH \[LAST\] :

SERVICE NUMBER \[LAST\] :

SERVICE CONNECTED PERCENT :

SERVICE ENTRY DATE \[LAST\] :

SERVICE SEPARATION DATE \[LAST\] :

PERIOD OF SERVICE :

POW STATUS INDICATED? :

DATE ENTERED IN PATIENT FILE : SEP 17, 2002

ETHNICITY INFORMATION : HISPANIC OR LATINO

RACE INFORMATION (multiple):

WHITE

Patient lookup can be done by Patient Name/SSN or by ICN.

  
Print MPI/PD Data for Patient With Pseudo SSN

Figure 5‑32 shows an example of only the first portion of the Patient MPI/PD Data Inquiry output shown in Figure 5‑31. In this example, a different person has been entered in VistA with a pseudo SSN. This changes the output of the report in the following ways:

- A trailing "P" appears at the end of the Social Security Number.
- The Pseudo SSN Reason appears only if a pseudo SSN has been entered and the site has entered a value for pseudo SSN reason. Figure 5‑32 shows this value as "REFUSED TO PROVIDE."

Partial example of the Patient MPI/PD Data Inquiry option showing field values in the patient record.

<span id="_Ref132531544" class="anchor"></span>Figure ‑. Patient MPI/PD Data Inquiry—Partial example of inquiry showing patient with pseudo SSN

Select PATIENT: MVIPATIENT,LOGAN \<Enter\> 01-01-42 666032829P YES SC VETERAN (OTHER) \*MULTIPLE BIRTH\*

DEVICE: HOME// \<Enter\>

MPI/PD Data for: MVIPATIENT,LOGAN  (DFN \#100001039)

Printed Mar 27, 2007@15:36 at VAMCSITE

===============================================================================

ICN     : 1000001702V545454

SSN     : 666032829P

         Pseudo SSN Reason: REFUSED TO PROVIDE

Birth Sex    : FEMALE

Claim \# : None

Date of Birth: Jan 1, 1942

Address: 2100 PINE ST

ANYTOWN, MARYLAND 16001

Print MPI/PD Data for Patient With Bad Address Indicator

As of Patch DG\*5.3\*712, the Patient MPI/PD Data Inquiry \[RG EXCEPTION TF INQUIRY\] option has been enhanced to display Bad Address Indicator data, if available. The data is derived from the BAD ADDRESS INDICATOR field (#.121) in the PATIENT file (#2).

<span id="_Ref499742246" class="anchor"></span>Figure ‑. Patient MPI/PD Data Inquiry—Partial example showing Bad Address Indicator data

Select PATIENT: MVIPATIENT,DOMINIQUE \<Enter\> 06-05-34 666005666 NO NSC VETERAN

DEVICE: HOME// \<Enter\>

MPI/PD Data for: MVIPATIENT,DOMINIQUE (DFN \#100001556)

Printed Feb 17, 2009@07:08 at VAMCSITE

===============================================================================

ICN : 1008522692V932932

SSN : 666005666

Birth Sex : MALE

Claim \# : None

Date of Birth: Jun 05, 1934

Multiple Birth Indicator: NO

Address: (Bad Address Indicator: UNDELIVERABLE)

376 HANGOVER LOOP

ANY TOWN, ALABAMA 12345

Phone \#: 205-981-0912

Print MPI/PD Data for Patient Residential Addresses Located in Foreign Countries

As of Patch DG\*5.3\*863, the following foreign address fields from the VistA PATIENT file (#2) are displayed:

- PROVINCE field \#.1171
- POSTAL CODE field \#.1172 (if available)
- COUNTRY field \#.1173

The condition by which these fields are displayed is as follows:

- If the COUNTRY field (#.1173), located in the PATIENT file (#2), is *<u>not</u>* null.
- Or if the CODE field (#.01), in the COUNTRY CODE file (#779.004), is *<u>not</u>* equal to "USA".

The next set of screen captures display the foreign address fields using the options to print a report for MPI/PD data for a selected person at your current facility, Figure 5‑14, and display the data returned from a remote query to a selected treating facility site for MPI/PD data for that same person, Figure 5‑16.

1.  Print MPI/PD Data for Person with Address in Foreign Country

<span id="_Ref360328381" class="anchor"></span>Figure ‑. Patient MPI/PD Data Inquiry—Foreign address fields

Select PATIENT: MVIPATIENT,PAUL \<Enter\>  5-9-64  666879132   NO   NSC VETERAN

DEVICE: HOME// \<Enter\>

MPI/PD Data for: MVIPATIENT,PAUL  (DFN \#100004746)

Printed Jun 27, 2013@07:14 at VAMCSITE

===============================================================================

ICN     : 1008000062V680332

SSN     : 666879132

Birth Sex    : MALE

Claim \# : None

Date of Birth: May 09, 1964

Multiple Birth Indicator: NO

Address:

         67 MAPLE LEAF RD

         APARTMENT D

         ROOM 15

         EAGLETON, ALBERTA (CANADA)  67DT5S

Phone \#: 555-555-5555

Treating Facilities:  Station:  DT Last Treated       Event Reason

--------------------  --------  ---------------       ------------

VAMCSITE                500       none found            none found

Austin Person Servic  200PS     none found            none found

VAMCSITE1               553       none found            none found

ICN History:

------------

5000003543V973280  - changed APR 16, 2013@16:01:25

Additional DPT Data for: MVIPATIENT,PAUL  (DFN \#100004746)

===========================================================

PLACE OF BIRTH \[CITY\]          : TOGUS

PLACE OF BIRTH \[STATE\]         : MAINE

FATHER'S NAME                  :

MOTHER'S NAME                  :

MOTHER'S MAIDEN NAME           : KING,

NAME OF PRIMARY NEXT OF KIN    :

NEXT OF KIN PHONE NUMBER       :

NAME OF DESIGNEE               :

EMERGENCY NAME                 :

MARITAL STATUS                 :

RELIGIOUS PREFERENCE           :

PRIMARY ELIGIBILITY CODE       :

VETERAN (Y/N)?                 : YES

SERVICE CONNECTED PERCENT      :

PERIOD OF SERVICE              :

POW STATUS INDICATED?          :

DATE ENTERED IN PATIENT FILE   : APR 16, 2013

2.  Send remote query to treating facility for MPI/PD patient data

<span id="_Toc510586936" class="anchor"></span>Figure ‑. SEND Remote Query to Treating Facility for MPI/PD Patient Data

Select Message Exception Menu Option: Remote Patient Data Query Menu

Select Remote Patient Data Query Menu Option: SEND \<Enter\> Remote Patient Data Query

This option sends a remote query to selected treating facility site(s) for MPI/PD data for a patient.

Patient lookup can be done by Patient Name, SSN or by ICN.

Select PATIENT: MVIPATIENT,PAUL \<Enter\>   5-9-64    666879132     NO     NS

C VETERAN

Query last sent for this ICN on Jun 27, 2013

Remote patient data queries will be sent to:

1\. (553) VAMCSITE1

Do you want to continue? Yes// \<Enter\> YES

Sending Remote Query to: 553 \<Enter\> VAMCSITE1

3.  Display MPI/PD Data for Patient with Address in Foreign Country

<span id="_Ref360331466" class="anchor"></span>Figure ‑. Display Remote Patient Data Query—Foreign address fields

Select PATIENT:  MVIPATIENT,PAUL \<Enter\>   5-9-64    666879132     NO     NS

C VETERAN     

Display data returned from remote patient data queries.

(Be sure HISTORY is enabled to capture data!)

-\> For ICN 1008000062V680332

     VAMCSITE1  status: (Response Received)

MPI/PD Data for: MVIPATIENT,PAUL  (DFN \#100002979)

Printed Jun 27, 2013@07:17 at VAMCSITE1

===============================================================================

ICN     : 1008000062V680332

SSN    : 666879132

Birth Sex    : MALE

Claim \# : None

Date of Birth: May 09, 1964

Multiple Birth Indicator: NO

Address:

         67 MAPLE LEAF RD

         APARTMENT D

         ROOM 15

         EAGLETON, ALBERTA (CANADA)  67DT5S

Phone \#: 555-555-5555

Treating Facilities:  Station:  DT Last Treated       Event Reason

--------------------  --------  ---------------       ------------

Austin Person Servic  200PS     none found            none found

VAMCSITE1               553       none found            none found

ZZ VAMCSITE             500       none found            none found

Additional DPT Data for: MVIPATIENT,PAUL  (DFN \#100002979)

===========================================================

PLACE OF BIRTH \[CITY\]          : TOGUS

PLACE OF BIRTH \[STATE\]         : MAINE

FATHER'S NAME                  :

MOTHER'S NAME                  :

MOTHER'S MAIDEN NAME           : KING,

NAME OF PRIMARY NEXT OF KIN    :

NEXT OF KIN PHONE NUMBER       :

NAME OF DESIGNEE               :

EMERGENCY NAME                 :

MARITAL STATUS                 :

RELIGIOUS PREFERENCE           :

PRIMARY ELIGIBILITY CODE       :

VETERAN (Y/N)?                 : YES

SERVICE CONNECTED PERCENT      :

PERIOD OF SERVICE              :

POW STATUS INDICATED?          :

DATE ENTERED IN PATIENT FILE   : APR 16, 2013

Date of death bulletin is triggered when a patient is given a Date of Death:

Subj: PATIENT HAS EXPIRED  \[#139445\] 06/27/13@07:23  18 lines

From: MVIUSER, PAULETTE  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

                    NAME: MVIPATIENT,PAUL

                     SSN: 456-87-9132

                     DOB: MAY 9,1964

   CLAIM FOLDER LOCATION: NOT LISTED

            CLAIM NUMBER: NOT LISTED

             LAST EDITED BY: MVIUSER, PAULETTE

    DATE/TIME LAST MODIFIED: JUN 27, 2013@07:23:27

     SOURCE OF NOTIFICATION: DEATH CERTIFICATE ON FILE

      Date/Time of Death: JUN 27, 2013

No Current Primary Care Management Data

#### Support for Department of Defense (DoD) Defense Eligibility Enrollment Reporting System (DEERS)

As of Patch RG\*1\*59, the following two fields were added to the VistA PATIENT file (#2) to support the Defense Eligibility Enrollment Reporting System (DEERS). These fields are Department of Defense (DoD) identifiers used for individuals who do not have a Social Security Number. This data is used by the Master Veteran Index to support the linking of patient records across VA and DoD. The fields are:

- A Temporary ID Number for individuals (e.g., babies) who do not have or have not provided a Social Security Number (SSN) when the record is added to DEERS. It is used for military dependents only. This DoD TEMPORARY ID NUMBER is used by the Master Veteran Index to support the linking of patient records across VA and DoD.
- A Foreign ID Number for foreign military and foreign nationals when the record is added to DEERS. This DoD FOREIGN ID NUMBER is used by the Master Veteran Index to support the linking of patient records without a given Social Security Number (SSN) across VA and DoD.

These fields are displayed *<u>only</u>* when they are populated for the selected person record.

The next set of screen captures display the Temporary ID Number and Foreign ID Number fields using the options to print a report for MPI/PD data for a selected person at your current facility, Figure 5‑17, and display the data returned from a remote query to a selected treating facility site for MPI/PD data for that same patient, Figure 5‑19.

1.  Print MPI/PD data, DoD Identifiers populated in person record display via the Patient MPI/PD Data Inquiry option

<span id="_Ref314705918" class="anchor"></span>Figure ‑. DoD Identifiers Populated for a Patient Display in the Patient MPI/PD Data Inquiry Option

Select Message Exception Menu Option: Patient MPI/PD Data Inquiry

This report prints MPI/PD Data for a selected patient. The

information displayed includes the Integration Control Number

(ICN), patient identity information, and Treating Facility list.

The information is pulled from the Patient (#2) file and the

Treating Facility List (#391.91) file.

Patient lookup can be done by Patient Name/SSN or by ICN.

Select PATIENT: MVIPATIENT,CHARLES \<Enter\> 3-3-52 666546778 NO COLLATERAL

DEVICE: HOME// \<Enter\> UCX/TELNET

MPI/PD Data for: MVIPATIENT,CHARLES (DFN \#19)

Printed Dec 08, 2011@22:30 at VAMCSITE

===============================================================================

ICN : 1000020839V100000

SSN : 666546778

Birth Sex : MALE

Claim \# : 666546778

Date of Birth: Mar 03, 1952

Multiple Birth Indicator: NULL

DoD Temporary ID Number : 999000066

DoD Foreign ID Number : 999000067

Address:

BESTT STREET

VAMCSITE, NEW YORK 12180

Phone \#: 555-2345

Treating Facilities: Station: DT Last Treated Event Reason

-------------------- -------- --------------- ------------

VAMCSITE 500 Jul 18, 2001@16:57 PATIENT ADMISSION

VAMCSITE1 553 May 30, 2001@13:35 PATIENT DISCHARGE

2.  Send remote query to treating facility requesting MPI/PD patient data.

<span id="_Ref360376509" class="anchor"></span>Figure ‑. SEND Remote Query to Treating Facility for MPI/PD Patient Data

Select Message Exception Menu Option: Remote Patient Data Query Menu

Select Remote Patient Data Query Menu Option: SEND \<Enter\> Remote Patient Data Query

This option sends a remote query to selected treating facility site(s) for MPI/PD data for a patient.

Patient lookup can be done by Patient Name, SSN or by ICN.

Select PATIENT: 666546778\<Enter\> MVIPATIENT,CHARLES 3-3-52 666546778 NO COLLATERAL

Query last sent for this ICN on Dec 07, 2011

Remote patient data queries will be sent to:

1\. (500) VAMCSITE

Do you want to continue? Yes// \<Enter\> YES

Sending Remote Query to: 500 VAMCSITE

3.  Display MPI/PD Data, DoD Identifiers, from the remote query sent to selected treating facility.

<span id="_Ref314706247" class="anchor"></span>Figure ‑. DoD Identifiers are Displayed from the Remote Query Sent to Selected Treating Facility

Select Remote Patient Data Query Menu Option: Display Remote Patient Data Query

Patient lookup can be done by Patient Name, SSN or by ICN.

Select PATIENT: MVIPATIENT,CHARLES \<Enter\> 3-3-52 666546778 NO COLLATERAL

Display data returned from remote patient data queries.

(Be sure HISTORY is enabled to capture data!)

-\> For ICN 1000020839V100000

VAMCSITE status: (Response Received)

MPI/PD Data for: MVIPATIENT,CHARLES (DFN \#19)

Printed Dec 07, 2011@22:26 at VAMCSITE

===============================================================================

ICN : 1000020839V100000

SSN : 666546778

Birth Sex : MALE

Claim \# : 666546778

Date of Birth: Mar 03, 1952

Multiple Birth Indicator: NULL

DoD Temporary ID Number : 999000066

DoD Foreign ID Number : 999000067

Address:

BESTT STREET

VAMCSITE, NEW YORK 12180

Phone \#: 555-2345

Treating Facilities: Station: DT Last Treated Event Reason

-------------------- -------- --------------- ------------

VAMCSITE 500 Jul 18, 2001@16:57 PATIENT ADMISSION

VAMCSITE1 553 May 30, 2001@13:35 PATIENT DISCHARGE

Austin Person Service 200PS none found none found

|                                    |                             |
|------------------------------------|-----------------------------|
| Remote Patient Data Query Menu | \[RG REMOTE PDAT MENU\] |

This menu provides options to query any facility at which a selected person has been seen, check the query, and display the remote person data that is returned from that site. The remote data fields retrieved include the Integration Control Number (ICN), MPI/PD Activity Score, Subscription Control Number, and Treating Facility list.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/041.png)</td>
<td><blockquote>
<p><strong>NOTE:</strong> As of Patch DG*5.3*902, the menu text display for the field named SELF-IDENTIFIED GENDER was changed to “Self-Identified Gender Identity” in the following MPI/PD options:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Patient MPI/PD Data Inquiry</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Remote Patient Data Query Menu ...</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc26665868" class="anchor"></span>Figure ‑. Remote Patient Data Query Menu

Select Message Exception Menu Option: Remote \<Enter\> Patient Data Query Menu

Send Remote Patient Data Query

Check Remote Patient Data Query

Display Remote Patient Data Query

Select Remote Patient Data Query Menu Option:

|                                    |                             |
|------------------------------------|-----------------------------|
| Send Remote Patient Data Query | \[RG REMOTE PDAT SEND\] |

This option allows you to send remote person data queries from your facility to any facility at which a selected person has been seen. The remote data fields retrieved are the same as those that are available for local data using the Patient MPI/PD Data Inquiry \[RG EXCEPTION TF INQUIRY\] option.

<span id="_Toc26665869" class="anchor"></span>Figure ‑. Send Remote Patient Data Query

Select Remote Patient Data Query Menu Option: SEND \<Enter\> Remote Patient Data Query

This option sends a remote query to selected treating

facility site(s) for MPI/PD data for a patient.

Patient lookup can be done by Patient Name, SSN or by ICN.

Select PATIENT: MVIPATIENT,ALEX \<Enter\> 9-2-01 666437773 YES SC VETERAN

Remote patient data queries will be sent to:

1\. (662) SAN FRANCISCO

Do you want to continue? Yes// YES

Sending Remote Query to: 662\<Enter\> SAN FRANCISCO

Patient lookup can be done by Patient Name, SSN or by ICN

|                                     |                              |
|-------------------------------------|------------------------------|
| Check Remote Patient Data Query | \[RG REMOTE PDAT CHECK\] |

This option allows you to check the status of a remote patient data query previously sent using the Send Remote Patient Data Query \[RG REMOTE PDAT SEND\] option.

The Check Remote Patient Data Query option displays the full INTEGRATION CONTROL NUMBER (ICN), which includes the following data from the PATIENT file (#2):

- INTEGRATION CONTROL NUMBER field (#991.01)
- a "V" separator character
- ICN CHECKSUM field (#991.02)

Example: 1008000002V340972

<span id="_Ref160855226" class="anchor"></span>Figure ‑. Check Remote Patient Data Query

Select Remote Patient Data Query Menu Option: Check Remote Patient Data Query

This option checks the status of an existing remote patient data query.

Patient lookup can be done by Patient Name, SSN or by ICN.

Select PATIENT: MVIPATIENT,DAKOTA

-\> For ICN 1099999999V987654

Select one or more of the following:

1\. (515) VAMCSITEX

2\. (526) VAMCSITE

3\. (537) VAMCSITE2 HCS

4\. (553) VAMCSITE1

5\. (677) VAMCSITE HCS

6\. (437) VAMCSITE1

7\. (564) VAMCSITE2

8\. (578) VAMCSITEX

9\. (ALL)

Select site(s) 1-8 or 9 for all: 9

VAMCSITEX status: (Response Received)

VAMCSITE status: (Response Received)

VAMCSITE2 HCS status: (Response Received)

VAMCSITE1 status: (Response Received)

VAMCSITE HCS status: (Response Received)

VAMCSITE1 status: (Response Received)

VAMCSITE2 status: (Response Received)

VAMCSITEX status: (Response Received)

Patient lookup can be done by Patient Name, SSN or by ICN.

<span id="_Toc247320311" class="anchor"></span>Table ‑1. Check Remote Patient Data Query status reported back to site

|                                       |                                                                       |                                |
|---------------------------------------|-----------------------------------------------------------------------|--------------------------------|
| Status                            | Description                                                       |                                |
| Error in Process                      | There is a problem with link setup or XTMP global, please log a NOIS. |                                |
| Request Sent                          | The remote query request has been sent.                               |                                |
| Awaiting Response                     | HL7 indicates that the message is being processed.                    |                                |
| Response Received                     | The RPC has completed and the data has returned to the local server.  |                                |
| Display Remote Patient Data Query |                                                                       | \[RG REMOTE PDAT DISPLAY\] |

This option allows you the user to display a patient data query previously sent using the Send Remote Patient Data Query \[RG REMOTE PDAT SEND\] option. This option will display the status of the query and the data returned or an error message.

The Display Remote Patient Data Query option displays the full INTEGRATION CONTROL NUMBER (ICN), which includes the following data from the PATIENT file (#2):

- INTEGRATION CONTROL NUMBER field (#991.01)
- a "V" separator character
- ICN CHECKSUM field (#991.02)

Example: 1008000002V340972

<span id="_Ref132534485" class="anchor"></span>Figure ‑. Display Remote Patient Data Query

Select Remote Patient Data Query Menu Option: Display Remote Patient Data Query

Patient lookup can be done by Patient Name, SSN or by ICN.

Select PATIENT: MVIPATIENT,DAKOTA

-\> For ICN 1099999999V987654

Select one or more of the following:

1\. (515) VAMCSITEX

2\. (526) VAMCSITE

3\. (537) VAMCSITE2 HCS

4\. (553) VAMCSITE1

5\. (677) VAMCSITE HCS

6\. (437) VAMCSITE1

7\. (564) VAMCSITE2

8\. (578) VAMCSITEX

9\. (ALL)

Select site(s) 1-8 or 9 for all: 1

VAMCSITEX status: (Response Received)

MPI/PD Data for: MVIPATIENT,DAKOTA (DFN \#7000377)

Printed Apr 11, 2006@07:39 at VAMCSITEX

===============================================================

ICN : 1099999999V987654

SSN : 666337777

SSN Verification Status: Verified

Birth Sex : MALE

Claim \# : 000337777

Date of Birth: April 04, 1904

Address: 123 COLLEGE TOWN DR

SACRAMENTO, CALIFORNIA 95826

Treating Facilities: Station: DT Last Treated Event Reason

-------------------- -------- --------------- -------------

VAMCSITEX 515 Jun 10, 1999@13:20 PATIENT DISCHARGE

VAMCSITE 526 Aug 13, 1998@9:45 PATIENT DISCHARGE

VAMCSITE2 HCS 537 Sept 11, 1999@13:00 PATIENT DISCHARGE

VAMCSITE1 553 Jun 2, 1999@11:30 PATIENT DISCHARGE

VAMCSITE HCS 677 Jul 12, 1997@16:00 PATIENT DISCHARGE

VAMCSITE1 437 Nov 17, <1998@14:00> PATIENT DISCHARGE

VAMCSITE2 564 Dec 11, <2000@12:30> PATIENT DISCHARGE

VAMCSITEX 578 Dec 12, 2001@13:40 PATIENT DISCHARGE

Additional DPT Data for: MVIPATIENT,DAKOTA N (DFN \#700000)

===========================================================

PLACE OF BIRTH \[CITY\] :

PLACE OF BIRTH \[STATE\] :

FATHER'S NAME :

MOTHER'S NAME :

MOTHER'S MAIDEN NAME :

NAME OF PRIMARY NEXT OF KIN : MPINEXTOFKIN

NEXT OF KIN PHONE NUMBER : 555-555-1212

NAME OF DESIGNEE :

EMERGENCY NAME : MPIEMERGENCY

MARITAL STATUS : DIVORCED

RELIGIOUS PREFERENCE : NO PREFERENCE

RACE :

PRIMARY ELIGIBILITY CODE : NSC

VETERAN (Y/N)? : YES

SERVICE BRANCH \[LAST\] : AIR FORCE

SERVICE NUMBER \[LAST\] : 000337777

SERVICE CONNECTED PERCENT :

SERVICE ENTRY DATE \[LAST\] :

SERVICE SEPARATION DATE \[LAST\] : JAN 24, 1987

PERIOD OF SERVICE : VIETNAM ERA

DATE ENTERED IN PATIENT FILE : DEC 19, 2000

Figure 5‑39 shows an example of only the first portion of the Display Remote Patient Data Query output for the same person shown in Figure 5‑38; however, in this example that same person has been entered in VistA with a pseudo SSN. This changes the output of the report in the following ways:

- A trailing "P" appears at the end of the Social Security Number
- In this instance the verification process has established a status of "Invalid Per SSA"
- The Pseudo SSN Reason appears only if a pseudo SSN has been entered and the site has entered a value for the pseudo SSN reason. Figure 5‑39 shows this value as "SSN UNKNOWN/FOLLOW-UP REQUIRED"

The Display Remote Patient Data Query continues as usual based on the field values in the person record.

<span id="_Ref132534469" class="anchor"></span>Figure ‑. Display Remote Patient Data Query—Partial example query showing person with pseudo SSN

Select PATIENT: MVIPATIENT,DAKOTA

-\> For ICN 1099999999V987654

Select one or more of the following:

1\. (515) VAMCSITEX

2\. (526) VAMCSITE

3\. (537) VAMCSITE2 HCS

4\. (553) VAMCSITE1

5\. (677) VAMCSITE HCS

6\. (437) VAMCSITE1

7\. (564) VAMCSITE2

8\. (578) VAMCSITEX

9\. (ALL)

Select site(s) 1-8 or 9 for all: 1

VAMCSITEX status: (Response Received)

Printed Apr 11, 2006@07:39 at VAMCSITEX

===============================================================

ICN : 1099999999V987654

SSN : 666337777P

SSN Verification Status: Invalid Per SSA

Pseudo SSN Reason : SSN UNKNOWN/FOLLOW-UP REQUIRED

Birth Sex : MALE

Claim \# : 000337777

Date of Birth: April 04, 1904

Address: 123 COLLEGE TOWN DR

SACRAMENTO, CALIFORNIA 95826

Phone \#: 555-555-5555

|                        |                                        |
|------------------------|----------------------------------------|
| Display Only Query | \[MPIF DISPLAY ONLY QUERY TO MPI\] |

This option allows the user to query the MVI for all known data about a person. The person may or may not be currently in the PATIENT file (#2). The MVI will return: Patient Not Known at the MPI, a list of potential matches along with all known data, or an exact match along with all known data. This will be for display purposes only. The VistA Display Only Query accepts upper and/or lower case data entry.

The Display Only Query option, located on the Message Exception Menu displays the full INTEGRATION CONTROL NUMBER (ICN), which includes the following data from the PATIENT file (#2):

- INTEGRATION CONTROL NUMBER field (#991.01)
- a "V" separator character
- ICN CHECKSUM field (#991.02)

Example: 1008000002V340972

Display Only Query—Patient Exists in Patient File

<span id="_Ref499742298" class="anchor"></span>Figure ‑. Display Only Query when person exists in PATIENT File (#2)

Select Master Patient Index Menu Option: Display \<Enter\> Only Query

Is Patient in the PATIENT file ? YES// \<Enter\>

Patient Name: MVIPATIENT,ADRIAN \<Enter\>    4-5-76    666040576P \*\*Pseudo SSN\*\*     NO     NSC VETERAN

Attempting to connect to the Master Patient Index in Austin...

If DOB is inexact or if SSN is not passed or if common name,

this could take some time - please be patient....

Found potential matches

--- All ICNs Below meet the POTENTIAL Match criteria ---

Birth

    ICN               NAME                            SSN        DOB       SEX
1)  1008000002V340972 MVIPATIENT,ADRIAN                      4-5-1976   M

          Treating Facility: VAMCSITE (500)

Birth

    ICN               NAME                            SSN        DOB       SEX
2)  1008000005V340972 MVIPATIENT,ADRIAN JAMES                    4-5-1976   M

          Treating Facility: VAMCSITE1 (553)

Enter the Number to display the details: 1 \<Enter\>

Please wait....

MPI Patient Data Search - For : \<\< 1008590121V175517 \>\>   ID State: PERMANENT

Printed Mar 27, 2013@19:04

================================================================================

              \< PRIMARY VIEW DATA - Updated: Mar 28, 2011@22:56 \>

  ICN      : 1008000002V340972

  Name     : MVIPATIENT,ADRIAN               L\[ -- \]  F\[ -- \]  M\[ -- \]  S\[ -- \]

  SSN      : UNKNOWN                                   \[ -- \]

  DOB      : Apr 05, 1976                              \[ -- \]

  MBI      : NULL                                      \[ -- \]

  Birth Sex: M                                         \[ -- \]

  POB City : NULL                                      \[ -- \]

  POB State: NULL                                      \[ -- \]

  MMN      : NULL                                      \[ -- \]

  Treating Facilities:

  --------------------

    500   - VAMCSITE

    --------------------------------- Correlation Updated: Mar 28, 2011@22:57:41

      Name     : MVIPATIENT,ADRIAN               (DFN \#100002961)

      SSN      : UNKNOWN                         SOURCE ID TYPE: PI

      DOB      : Apr 05, 1976

      MBI      : NULL

      Birth Sex: M

      Site Data Updated: Mar 28, 2011@22:57:35

    200PS - AUSTIN PSIM

    --------------------------------- Correlation Updated: Mar 29, 2011@08:45:20

  Other IDs:

  ----------

  5000001830V352296     Assigning Location: VAMCSITE

  ICN Creation Data:

  ------------------

  Date/Time of Original Creation: Mar 28, 2011@22:56

  Facility of Original Creation : VAMCSITE

  Created by                    : MVIUSER,DEBORHA

If the user answers "No" at the "Is Patient in the PATIENT file?" prompt, see Figure 5‑26, then the person's name and date of birth must be entered. The person's Social Security Number (SSN) is an optional field; however, not supplying the SSN could affect the results of the search.

The ALIAS (multiple), MULTIPLE BIRTH INDICATOR, and POW STATUS INDICATED? fields are returned in the DISPLAY ONLY QUERY option.

  
Display Only Query— Person Doesn’t Exist in PATIENT File (#2)

<span id="_Ref360044877" class="anchor"></span>Figure ‑. Display Only Query when person does not exist in PATIENT file (#2)

Select Master Patient Index Menu Option: DISPLAY \<Enter\> Only Query

Is Patient in the PATIENT file ? YES// n \<Enter\> NO

When the patient is NOT in the local PATIENT file, you will be asked

to provide as much information as possible to facilitate the query.

You will be asked for patient name, date of birth, Social Security Number,

Birth Sex, phone number, and address. Minimally, you must enter patient name

and date of birth.

PATIENT NAME (last,first middle): MVIPATIENT,JEFF

Date of Birth: 4-5-1976 \<Enter\> (APR 05, 1976)

9 Digit SSN (No Dashes): 666040576

Birth Sex: m\<Enter\> MALE

Phone Number: \<Enter\>

Address Line 1: \<Enter\>

Address Line 2: \<Enter\>

Address Line 3: \<Enter\>

City: \<Enter\>

Attempting to connect to the Master Patient Index in Austin...

If DOB is inexact or if SSN is not passed or if common name,

this could take some time - please be patient....

Found potential matches

--- All ICNs Below meet the POTENTIAL Match criteria ---

ICN NAME SSN DOB SEX

1\) 100000007V898989 MVIPATIENT,JEFF 666040576 4-5-1976 M

Treating Facility: VAMCSITE (500)

ICN NAME SSN DOB SEX

2\) 100000008V898989 MVIPATIENT, GEOFF 666040576 4-5-1976 M

Treating Facility: VAMCSITE1 (553)

Enter the Number to display the details: 1

Please wait....

MPI Patient Data Search - For : \<\< 100000007V898989 \>\> ID State: PERMANENT

Printed Jun 27, 2013@00:25

=============================================================================

\< PRIMARY VIEW DATA - Updated: Mar 28, 2011@22:56 \>

ICN : 100000007V898989

Name : MVIPATIENT,JEFF L\[ -- \] F\[ -- \] M\[ -- \] S\[ -- \]

SSN : UNKNOWN \[ -- \]

DOB : Apr 05, 1976 \[ -- \]

MBI : NULL \[ -- \]

Birth Sex: M \[ -- \]

POB City : NULL \[ -- \]

POB State: NULL \[ -- \]

MMN : NULL \[ -- \]

Treating Facilities:

--------------------

500 - VAMCSITE

--------------------------------- Correlation Updated: Mar 28, 2011@22:57:41

Name : MVIPATIENT,JEFF (DFN \#100002961)

SSN : UNKNOWN SOURCE ID TYPE: PI

DOB : Apr 05, 1976

MBI : NULL

Birth Sex: M

Site Data Updated: Mar 28, 2011@22:57:35

200PS - AUSTIN PSIM

--------------------------------- Correlation Updated: Mar 29, 2011@08:45:20

Other IDs:

----------

5000011030V352296 Assigning Location: VAMCSITE

ICN Creation Data:

------------------

Date/Time of Original Creation: Mar 28, 2011@22:56

Facility of Original Creation : VAMCSITE

Created by : MVIUSER,CHRISTINE

  
Display Only Query—Patient with an Open Data Management Case

<span id="_Ref499742307" class="anchor"></span>Figure ‑. Display Only Query with an Open Data Management Case

Select Message Exception Menu Option: Display \<Enter\> Only Query

Is Patient in the PATIENT file ? YES// \<Enter\>

Patient Name: MVIPATIENT,JESSIE \<Enter\> MVIPATIENT,JESSIE 3-23-43 666222333 NO NON-VETERAN (OTHER)

Attempting to connect to the Master Patient Index in Austin...

If DOB is inexact or if SSN is not passed or if common name,

this could take some time - please be patient....

Found One Match

--- All ICNs Below meet the POTENTIAL Match criteria ---

Birth

ICN NAME SSN DOB SEX

1\) 1000001406V377772 MVIPATIENT,JESSIE 666222333 3-23-1943 F

Treating Facility: VAMCSITE (500)

Enter the Number to display the details: 1 \<Enter\>

Please wait....

MPI Patient Data Search - For : \<\< 1000001406 \>\> ID State: PERMANENT

Printed Feb 03, 2013@00:37

================================================================================

\<\<This ICN is actively being worked on - Case \#0902-00001 \>\>

\<\<Case Worker: MPICASEWORKER,EIGHT / / 555-555-5555 \>\>

\< PRIMARY VIEW DATA - Updated: Aug 06, 2012@16:25 \>

ICN : 1000001406V377772

Name : MVIPATIENT,JESSIE L\[ 0\] F\[ 0\] M\[ 0\] S\[ -- \]

SSN : 666222333 \[ 0\]

DOB : Mar 23, 1943 \[ 0\]

MBI : NULL \[ 0\]

Birth Sex: F \[ 0\]

POB City : NULL \[ 0\]

POB State: NULL \[ 0\]

MMN : NULL \[ 0\]

Treating Facilities:

--------------------

500 - VAMCSITE

---------------------------------

Name : MVIPATIENT,JESSIE (DFN \#100000904)

SSN : 666222333

DOB : Mar 23, 1943

MBI : NULL

Birth Sex: F

Site Data Updated: Jul 09, 2012@18:34:02

Other IDs:

----------

None Found

ICN Creation Data:

------------------

Date/Time of Original Creation: Jul 08, 2012@19:02

Facility of Original Creation : VAMCSITE

Created by : MVIUSER,WILLIAM

|                                                                                                                |                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/042.png) | NOTE: Patch MPIF\*1\*21 added several fields to the Display Only Query option. They are: claim number, station number of the treating facility; and if there is an Open Data Management case, the case number, caseworker, telephone number, and NOIS number (if there is one). |

|                                   |                                  |
|-----------------------------------|----------------------------------|
| Primary View Display from MPI | \[RG PRIMARY VIEW FROM MPI\] |

Figure 5‑43 shows the Primary View Display from MPI option, located on the Message Exception Menu \[RG EXCEPTION MENU\]. It is used to remotely view Primary View patient identity fields on the Master Patient Index (MPI). This option offers VA facilities the ability to send remote queries to the MVI to view person identity data regardless if there is an exception logged for the person.

<span id="_Ref175327288" class="anchor"></span>Figure ‑. Primary View Display from MPI \[RG PRIMARY VIEW FROM MPI\] option

Select Message Exception Menu Option: Primary View Display from MPI

This option sends a remote request for data to the Master Patient

Index, using a Remote Procedure Call (RPC). When the RPC returns

the information, you can review Primary View data as it currently

exists on the MPI Patient Data Inquiry (PDAT) report.

Choose the patient for whom Primary View data is to be requested.

The selected patient must have an Integration Control Number (ICN).

You can select by Patient Name, Social Security Number, or ICN.

Select PATIENT: MVIPATIENT,RICK \<Enter\> 12-30-44 000044040 YES SC VETERAN \*MULTIPLE BIRTH\*

A query was last sent for this ICN on Aug 19, 2012@17:12:30

Do you wish to view the existing query data now? YES// No \<Enter\>

Sending a Remote Query to the Master Patient Index.

This will take some time; please be patient.

Query data has returned from the MPI and is available for review.

(Be sure HISTORY is enabled to capture data!)

MPI Patient Data Search - For : \<\< 1000021621V706883 \>\> ID State: PERMANENT

Printed Mar 18, 2012@10:35

================================================================================

\< PRIMARY VIEW DATA - Updated: Mar 18, 2012@14:56:01 \>

ICN : 1000021621V706883

Name : MVIPATIENT,RICK JR L\[ 10\] F\[ 50\] M\[ 10\] S\[ 10\]

SSN : 000044040 (VERIFIED) \[ 100\]

DOB : Dec 30, 1944 \[1000\]

MBI : YES \[ 50\]

Birth Sex: M \[ 250\]

DOD : Mar 12, 2012

POB City : GREENVILLE \[ -- \]

POB State: SOUTH CAROLINA \[ 0\]

MMN : MVIMOTHERSMAIDEN, \[ 100\]

DoD Temporary ID Number: 999000066

DoD Foreign ID Number : 999000067

Address :

STREET 1

STREET 2

STREET 3

ANYTOWN, CALIFORNIA 99999

Phone: (555)555-5555

Alias:

MVIPATIENT,ALIAS

Treating Facilities:

--------------------

500 - VAMCSITE \<\< POTENTIAL CAT EDIT \>\>

200PS - AUSTIN PSIM

553 - VAMCSITE1,MI \<\< POTENTIAL CAT EDIT \>\>

Why VA Facilities Need to Know the Current Activity Scores for Patient Identity Fields

Person identity fields in the Primary View of the MVI are evaluated and updated based on scoring and data rules and displayed at the top of the MPI Patient Data Inquiry \[MPI DATA MGT PDAT MPI\] option.

|                                                                                                                |                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/043.png) | NOTE: For a list of the person identity fields that make up the Primary View on the MVI, see the section titled "Appendix E: Primary View Identity Traits" in this documentation. |

The Primary View score is evaluated based on criteria captured from person encounters at VA facilities (e.g., active prescriptions, admission or registration in the last year, lab test, or radiology exam in the last year) that are sending the inbound update (i.e., data entered by users or sent from a system of interest) to the MVI. The score is calculated from data updates coming from the site. Data is weighed on a field-by-field basis against any differences on the MVI to determine if the score for the inbound edits is equal to or greater than the score for the existing Primary View*.* Next, the inbound edit is evaluated against Primary View data rules.

Edits to key person identity fields accepted for the update to the Primary View are broadcasted out to all systems of interest for that person that do not already have the updated data. Data that does not meet or exceed the current score and pass the data rules will not be updated in the Primary View.  If this field is a synchronized field, the Primary View will be sent to that system attempting to make the update to reject the data and changing it to the current Primary View.

Site edits to person identity data that have existing activity scores equal to 1000 will cause those edits to reject. Access to the MPI Patient Data Inquiry \[MPI DATA MGT PDAT MPI\] option allows sites to see the current activity scores providing an understanding why an edit isn't working and is causing a reject exception.

|                             |                        |
|-----------------------------|------------------------|
| Management Reports. . . | \[RG MGT REPORTS\] |

This menu contains management reports for the MPI/PD Patient Administration Coordinator.

<span id="_Toc26665872" class="anchor"></span>Figure ‑. Management Reports Menu on MPI/PD

Select MPI/PD Patient Admin Coordinator Menu Option: RPT\<Enter\> Management Reports

Pseudo-SSN Report

Link and Process Status Display

Unresolved Exception Summary

Select Management Reports Option:

|                       |                                 |
|-----------------------|---------------------------------|
| Pseudo-SSN Report | \[RGPR PRE-IMP SSN REPORT\] |

The Pseudo SSN Report identifies persons with questionable SSNs. The completed report sorts patients by Patient Activity and then by the patient’s Primary Eligibility Code. The report identifies ALL patients in the database with a missing, pseudo, or potentially false SSN and further identifies patients with inpatient and/or outpatient activity over the past 3 years. The report also identifies entries in the PATIENT file (#2) with a "B" cross-reference and no zero node entry and displays the person record IEN (Internal Entry Number) within the first section of the report. This first section should be provided to your station’s IRM service for their information. The following example shows the output from the report.

<span id="_Toc26665873" class="anchor"></span>Figure ‑. Pseudo-SSN Report

Select Management Reports Option: Pseudo \<Enter\> -SSN Report

This report will provide a list of:

\(1\) any B Cross-references (there is no 'zero' node but a B x-ref)

on the patient file,

\(2\) patients with Pseudo SSNs who have not had activity within the past 3

years,

\(3\) patients with Pseudo SSNs who have had activity within the past 3 years.

The Reports are sorted by Primary Eligibility Code. The report can

be queued if desired.

For MPI/PD purposes, general advice is to concentrate first on

getting correct SSNs for the patients who HAVE had activity within

the past 3 years.

DEVICE: HOME// \<Enter\> Right Margin: 80// \<Enter\>

MPI/PD Report of Pseudo, missing & potentially false SSNs JUL 30, 2002@11:08:23

Bad B Cross References Report

Please contact IRM for assistance with bad B Cross references.

------------------------------------------------------------------------

B Cross Reference with no 0 Node in DPT: DFN= 7169186

B Cross Reference with no 0 Node in DPT: DFN= 7169107

MPI/PD Report of Pseudo, missing & potentially false SSNs JUL 30, 2002@11:08:46

Patient activity within past 3 years = NO

Primary

Elig Code

Elig. Name SSN Home Phone

----------------------------------------------------------------

SERVICE CONNECTED 50% to 100%

1 MVIPATIENT,ADDISON 666101097P 555-555-5555

AID & ATTENDANCE

2 MVIPATIENT,BAILEY 666102357P 555-222-1234

2 MVIPATIENT,TYLER 666102357P 555-222-1234

2 MVIPATIENT,SIDNEY 666020201P 555-222-7890

NSC

5 MVIPATIENT,REESE 666010805P

OTHER FEDERAL AGENCY

6 MVIPATIENT,JAMIE 666032384P

MPI/PD Report of Pseudo, missing & potentially false SSNs JUL 30, <2002@11:09:02>

Patient activity within past 3 years = YES

Primary

Elig Code

Elig. Name SSN Home Phone

----------------------------------------------------------------

SC LESS THAN 50%

3 MVIPATIENT,KASEY 666456799 555-555-9396

3 MVIPATIENT,CARSON 666010101P

NSC

5 MVIPATIENT,QUINN 666081440P

5 MVIPATIENT,RYLEE 66041232P

5 MVIPATIENT,HUNTER 666000999P 555-555-5555

5 MVIPATIENT,ALEX 666000053P 555-555-7890

5 MVIPATIENT,CARSON 666101011P

HOUSEBOUND

15 MVIPATIENT,PEYTON 666101010P

MPI/PD Report of Pseudo, missing & potentially false SSNs JUL 30, <2002@11:11:32>

Patient activity within past 3 years = YES

Primary

Elig Code

Elig. Name SSN Home Phone

----------------------------------------------------------------

HOUSEBOUND

None

MVIPATIENT,PARKER 666000040P

MVIPATIENT,DEVIN 666000041P

MVIPATIENT,REAGAN 666030252P 555-555-2093

MVIPATIENT,SKYLAR 666090708P

MVIPATIENT,AVERY 666050324P

This report should be printed and provided to personnel assigned to update the Social Security Numbers (SSN). These users would contact the person and use the Load/Edit Patient Data option in the Admission, Discharge, Transfer (ADT) Registration menu to update the SSN. It is suggested that sites first clean up those with activity = YES and prioritize the cleanup for person with veteran Primary Eligibility Codes.

|                                     |                                      |
|-------------------------------------|--------------------------------------|
| Link and Process Status Display | \[RG LINKS AND PROCESS DISPLAY\] |

This option is used to monitor the status of MPI/PD related functions and messaging. The monitor displays the following information.

- HL links that currently have messages to be processed on either the inbound or outbound queues and the current STATE of the link
- Status of MPI/PD background jobs
- Current audit status on the NAME field (#.01) in the PATIENT file (#2)
- Current status of the SEND parameters for HL7 messaging
- Local link management information
- Any Logical Links used for MPI/PD Messaging that don’t have an INSTITUTION defined
- Any Logical Links used for MPI/PD messaging that have an incorrect INSTITUTION defined
- Any Non-MPI/PD Links that have an INSTITUTION definition of the local sites

<span id="_Toc26665874" class="anchor"></span>Figure ‑. Link and Process Status Display option

Select MPI/PD IRM Menu Option: Link \<Enter\> and Process Status Display

Logical Link Monitor:

=====================

\<\<Run - Oct 28, 2002@13:39:56\>\>

Outgoing messages:

Incoming messages:

MPI/PD Process Monitor:

=======================

Checking VAFC BATCH UPDATE background job...

(Total DATA UPDATES waiting to be processed = 0)

(Total TREATING FACILITY UPDATES waiting to be processed = 0)

=\> VAFC BATCH UPDATE scheduled to run OCT 28, 2002@13:21.

Checking MPIF LOC/MIS ICN RES background job... (Total Local ICNs = 195)

=\> MPIF LOC/MIS ICN RES is not currently scheduled to run.

=\> Audit on NAME (#.01) field of PATIENT (#2) file set to \<\<YES, ALWAYS\>\>

Checking SEND Parameters for HL7 messaging...

=\> SEND PIMS HL7 V2.3 MESSAGES currently set to \<\< SEND MESSAGES \>\>.

=\> STOP MPI/PD MESSAGING currently set to \<\< SEND MESSAGES \>\>.

Checking SHUTDOWN LLP? field and TCP/IP SERVICE TYPE for VADCRN...

=\> SHUTDOWN LLP? currently set to \<\< NO \>\>.

=\> TCP/IP SERVICE TYPE currently set to \<\< SINGLE LISTENER \>\>.

=\> Logical Link MPIVA currently set to \<\< TCP \>\>.

=\> HL LINK MANAGER is currently \<\< RUNNING \>\>.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/044.png) | NOTE: Patch RG\*1\*20 has added the Link and Process Status Display option to both the MPI/PD IRM Menu and the MPI/PD Patient Admin Coordinator Menu. Once a Class III utility, Link and Process Status Display is used to monitor the status of MPI/PD related functions and messaging. The data provided by this option can also be generated from the Master Patient Index (MPI), via a remote procedure call, for use by the MPI Data Quality Management team. |

|                                  |                           |
|----------------------------------|---------------------------|
| Unresolved Exception Summary | \[RG STATUS DISPLAY\] |

The Unresolved Exception Summary calculates and presents the following data:

- Number of unresolved exceptions in the CIRN HL7 EXCEPTION LOG file (#991.1) for the MPI/PD related entries (e.g., internal entry number 234) in the CIRN HL7 EXCEPTION TYPE file (#991.11) .
- Number of unique patients with exceptions.

The Exception Handler and Patient Data Review numbers indicate how up-to-date a site is in exception resolution. This data can be useful in reducing the number of exceptions.

<span id="_Toc26665875" class="anchor"></span>Figure ‑. Unresolved Exception Summary

Select MPI/PD IRM Menu Option: UNRESOLVED \<Enter\> Exception Summary

Exception Handler Entries:

--------------------------

Primary View Reject 4

Total number of exceptions: 4

Total unique patient exceptions: 0

The MPI/PD Exception Purge process last ran Mar 21, 2010@10:03:27.

Current total number of National ICNs = 357

Current total number of Local ICNs = 195

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/045.png)</td>
<td><p><strong>NOTE:</strong> As of VistA Patch RG*1*43, all existing exceptions that were active in the CIRN HL7 EXCEPTION LOG file (#991.1) of the types listed below, were marked with a status of PROCESSED:</p>
<ul>
<li><p>Required field(s) missing for patient sent to MPI</p></li>
<li><p>SSN Match Failed</p></li>
<li><p>Name Doesn't Match</p></li>
</ul>
<p>These three exceptions listed are no longer generated.</p>
<p>Existing person records that had these exceptions at the time of in installation of RG*1*43 were sent to the MVI again, and under the latest business rules, were assigned ICNs. At this point, if appropriate, these records received a new Potential Matches Returned exception for site personnel to review.</p></td>
</tr>
</tbody>
</table>

|                            |                              |
|----------------------------|------------------------------|
| ToolKit POC User Setup | \[RG TK POC USER SETUP\] |

The ToolKit POC User Setup \[RG TK POC USER SETUP\] option, located on the MPI/PD Patient Admin Coordinator Menu \[RG ADMIN COORD MENU\], sets up Visitor Records on the Master Patient Index (MPI) to support POC (Point of Contact) remote view access. This option calls the MPI TK POC USER SETUP remote procedure (RPC), which accesses the MPI to establish a Visitor Record in the NEW PERSON file (#200). Just calling the RPC will establish the Visitor record if one didn't exist.

The RPC identifies any missing required fields in the NEW PERSON file (#200) and instructs the user to verify the Name, SSN, Network Username and Phone Contact Number fields are populated via the Edit an Existing User option on the User Management menu, noting they should contact their local Information Resource Management (IRM) support for further assistance, if needed.

Once all required fields are populated in the NEW PERSON (#200) file, then:

1.  A Visitor record will be created on the MPI and an Extensible Markup Language (XML) document will be automatically transmitted from MPI to the ToolKit (TK) to update the user's DUZ entry, allowing access to the MPI TK functionality.
2.  The user gets a message back that all is good and to contact Healthcare Identity Management (HC IdM) to verify they have completed this initial step.

|                                                                                                                |                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/046.png) | NOTE: Users *<u>must</u>* already be established in TK before their respective Visitor record can be added to the Master Patient Index (MPI). |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/047.png) | REF: For more information on using the “Edit an Existing User” option, see Kernel Systems Management Guide, Chapter titled: “Signon/Security: System Management,” located on the VA Software Document Library (VDL) at the following link: [Kernel documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=10) Website |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/048.png) | REF: For more information on the MPI TK POC USER SETUP remote procedure call, see the *Master Patient Index/Patient Demographics (MPI/PD) v1.0, Technical Manual, s*ection titled: “Remote Procedure Calls (RPCs),” located in the External Interfaces chapter. The MPI/PD Technical Manual is located on the [VA Software Document Library (VDL) Website](http://www.va.gov/vdl/application.asp?appid=16) |

Figure 5‑33 shows an example display when all required fields for the person are accounted for in the NEW PERSON file (#200):

<span id="_Ref409787324" class="anchor"></span>Figure ‑. ToolKit POC User Setup option—All required fields accounted for in File \#200

Select MPI/PD Master Menu Option: CORD \<Enter\> MPI/PD Patient Admin Coordinator Menu

LOG Patient Audit Log Reports ...

MSG Message Exception Menu ...

RPT Management Reports ...

TK ToolKit POC User Setup

Select MPI/PD Patient Admin Coordinator Menu Option: TK \<Enter\> ToolKit POC User Setup.

This option allows you to create a Visitor Record in the New Person file on

the MPI production account. The purpose of this action is to accomplish the

first step toward establishing your ToolKit POC remote view access. Once this

action is completed successfully you will have the ability to use the new tools.

> **NOTE:** It is important that prior to using this option you be set up correctly

as a user in your local New Person file (#200). You should verify your user

record has the correct Name, SSN, Network Username and Phone Contact Number.

Attempting to establish Visitor Record on MPI...

Your Visitor Record was successfully established,

and your ToolKit user profile updated.

Figure 5‑34 shows an example display if the network username (one of the required fields) is missing for the person in the NEW PERSON file (#200):

<span id="_Ref409787360" class="anchor"></span>Figure ‑. ToolKit POC User Setup option—Required field missing in File \#200

Select MPI/PD Patient Admin Coordinator Menu Option: TK \<Enter\> ToolKit POC User Setup.

This option allows you to create a Visitor Record in the New Person file on

the MPI production account. The purpose of this action is to accomplish the

first step toward establishing your ToolKit POC remote view access. Once this

action is completed successfully you will have the ability to use the new tools.

> **NOTE:** It is important that prior to using this option you be set up correctly

as a user in your local New Person file (#200). You should verify your user

record has the correct Name, SSN, Network Username and Phone Contact Number.

Attempting to establish Visitor Record on MPI...

\<Missing Network Username\> - please populate this field via the User Management

menu as it is required for mapping your VistA account to your ToolKit account.

|                               |                                    |
|-------------------------------|------------------------------------|
| Add/Edit Point of Contact | \[RG UPDATE POINT OF CONTACT\] |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/049.png) | NOTE: The Point of Contact (POC) add/edit functionality for the Add/Edit Point of Contact, \[RG UPDATE POINT OF CONTACT\], menu option is being migrated to the ToolKit (TK) graphical user interface (GUI). The VistA process will no longer be accessible to users, as the option will be removed from the MPI/PD Patient Admin Coordinator Menu option,\[RG ADMIN COORD MENU\], and will also be placed out of order with the message: Obsolete with MPIF\*1.0\*59 (the out of order message indicates it’s obsolete in VistA, only.). Complete removal of this functionality from the VistA system will take place at a later date. |

### MPI/PD IRM Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu provides Information Resource Management (IRM) personnel with the options needed to maintain the Master Patient Index/Patient Demographics (MPI/PD) software.

<span id="_Toc26665895" class="anchor"></span>Figure ‑. MPI/PD IRM Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Select MPI/PD Master Menu Option: <strong>IRM</strong> &lt;<strong>Enter&gt;</strong> MPI/PD IRM Menu</p>
<p>Link and Process Status Display</p>
<p>Unresolved Exception Summary</p>
<p>Select MPI/PD IRM Menu Option:</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="link-and-process-status-display" class="unnumbered"><br />
Link and Process Status Display</h4></td>
<td><strong>[RG LINKS AND PROCESS DISPLAY]</strong></td>
</tr>
</tbody>
</table>

This option is used to monitor the status of MPI/PD related functions and messaging. The monitor displays the following information:

- HL links that currently have messages to be processed on either the inbound or outbound queues and the current STATE of the link.
- Status of MPI/PD background jobs.
- Current audit status on the NAME field (#.01) in the PATIENT file (#2) .
- Current status of the SEND parameters for HL7 messaging.
- Local link management information.

<span id="_Toc26665896" class="anchor"></span>Figure ‑. Link and Process Status Display

Select MPI/PD IRM Menu Option: Link \<Enter\> and Process Status Display

Logical Link Monitor:

=====================

\<\<Run - Oct 28, 2002@13:39:56\>\>

Outgoing messages:

Incoming messages:

MPI/PD Process Monitor:

=======================

Checking VAFC BATCH UPDATE background job...

(Total DATA UPDATES waiting to be processed = 0)

(Total TREATING FACILITY UPDATES waiting to be processed = 0)

=\> VAFC BATCH UPDATE scheduled to run OCT 28, 2002@13:21.

Checking MPIF LOC/MIS ICN RES background job... (Total Local ICNs = 195)

=\> MPIF LOC/MIS ICN RES is scheduled to run JUL 24, 2004@11:50.

=\> MPIF LOC/MIS ICN RES was last run May 11, 2004@14:11:19.

=\> Audit on NAME (#.01) field of PATIENT (#2) file set to \<\<YES, ALWAYS\>\>

Checking SEND Parameters for HL7 messaging...

=\> SEND PIMS HL7 V2.3 MESSAGES currently set to \<\< SEND MESSAGES \>\>.

=\> STOP MPI/PD MESSAGING currently set to \<\< SEND MESSAGES \>\>.

Checking SHUTDOWN LLP? field and TCP/IP SERVICE TYPE for VADCRN...

=\> SHUTDOWN LLP? currently set to \<\< NO \>\>.

=\> TCP/IP SERVICE TYPE currently set to \<\< SINGLE LISTENER \>\>.

=\> Logical Link MPIVA currently set to \<\< TCP \>\>.

=\> HL LINK MANAGER is currently \<\< RUNNING \>\>.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/050.png) | NOTE: Patch RG\*1\*20 has added the Class I option, Link and Process Status Display, to both the MPI/PD IRM Menu and the MPI/PD Patient Admin Coordinator Menu. Once a Class III utility, Link and Process Status Display is used to monitor the status of MPI/PD related functions and messaging. The data provided by this option can also be generated from the Master Patient Index (MPI), via a remote procedure call, for use by the Healthcare Identity Management team. |

|                                  |                           |
|----------------------------------|---------------------------|
| Unresolved Exception Summary | \[RG STATUS DISPLAY\] |

The Unresolved Exception Summary calculates and presents totals for the following data:

- Unresolved exceptions in the CIRN HL7 EXCEPTION LOG file (#991.1) for the MPI/PD related entries (e.g., internal entry number 234) in the CIRN HL7 EXCEPTION TYPE file (#991.11) .
- Unique patients with exceptions.

The Exception Handler numbers indicate how up-to-date a site is in exception resolution. This data can be useful in reducing the number of exceptions.

<span id="_Toc26665897" class="anchor"></span>Figure ‑. Unresolved Exception Summary

Select MPI/PD IRM Menu Option: UNRESOLVED \<Enter\> Exception Summary

Exception Handler Entries:

--------------------------

Primary View Reject 4

Total number of exceptions: 4

Total unique patient exceptions: 0

The MPI/PD Exception Purge process last ran Oct 21, 2002@10:03:27.

Current total number of National ICNs = 357

Current total number of Local ICNs = 195

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/051.png) | NOTE: Patch RG\*1\*20 has revised the MPI/PD Status Display \[RG STATUS DISPLAY\] option. The link and processes information has been removed from this display, as that data is now available on the new Link and Process Status Display \[RG LINKS & PROCESS DISPLAY\] option. The menu text for this option has been changed from MPI/PD Status Display to Unresolved Exception Summary. |

### Standalone Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                   |                               |
|-----------------------------------|-------------------------------|
| MPI/PD HL7 EXCEPTION NOTIFIER | \[RG EXCEPTION NOTIFIER\] |

This option is used to notify members of the RG CIRN DEMOGRAPHIC ISSUES Mail Group that there are exceptions to review. It is not a user option and should *not* be added to user menus.

|                                  |                              |
|----------------------------------|------------------------------|
| LOCAL/MISSING ICN RESOLUTION | \[MPIF LOC/MIS ICN RES\] |

This option will start the background job of resolving local and missing ICNs against the MVI. It should *not* be attached to any menu. It is recommended that this option be scheduled to run via TaskMan every 600 seconds (Patch MPIF\*1\*35).

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/052.png) | NOTE: As of Patch MPI\*1\*38, this background job no longer automatically adds patients to the MPI. Previous to the release of this patch, when the Local/Missing ICN Resolution job was processed on the MVI, if a match wasn't found, the person was added immediately. As of Patch MPI\*1\*38, this functionality has been changed in that if a match for a person isn't found on the MVI, a message is sent back to the site indicating this. On the site's side, this triggers an HL7 A28—Add Patient message, which then adds the person to the MVI. |

|                                                                                                                |                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/053.png) | NOTE: A new field, LOCAL/MISSING DATE LAST RAN (#.04), was created in the CIRN SITE PARAMETER file (#991.8) in patch RG\*1\*23 to hold the last date the Local/Missing ICN Resolution Background job ran. The field will be populated by the routine ^MPIFRES. |

|                                |                       |
|--------------------------------|-----------------------|
| MPI/PD HL7 DIAGNOSTIC MENU | \[RGMT DIAG MGR\] |

This standalone menu contains a diagnostic tool and reports to assist with problem resolution for MPI/PD HL7 messaging. It should *not* be attached to any menu. This diagnostic tool will be used primarily by the MPI/PD development team and EPS.

<span id="_Toc73520866" class="anchor"></span>Figure ‑. MPI/PD HL7 Diagnostic Menu options

Select MPI/PD HL7 Diagnostic Menu Option:

CMP Compile MPI/PD HL7 Data

RPT MPI/PD HL7 Message Status Report

SNG MPI/PD HL7 Activity by Patient/Single Protocol

ALL MPI/PD HL7 Activity by Patient/All Protocols

Select MPI/PD HL7 Diagnostic Menu Option:

|                             |                                    |
|-----------------------------|------------------------------------|
| COMPILE MPI/PD HL7 DATA | \[RGMT DIAG COMPILE HL7 DATA\] |

This utility searches the HL7 MESSAGE TEXT file (#772) for a selected date range. Each HL7 message in the date range is examined. If the RELATED EVENT PROTOCOL field contains the MPI/PD protocols (e.g., "VAF","RG", or "MPI") data is compiled into the ^XTMP("RGMT","HL" array. This option should *not* be attached to any menu.

A cross-reference is built on patient ICN and DFN for faster data retrieval for the associated reports.

|                                      |                                 |
|--------------------------------------|---------------------------------|
| MPI/PD HL7 MESSAGE STATUS REPORT | \[RGMT DIAG STATUS REPORT\] |

This option prints information found during the COMPILE MPI/PD HL7 DATA option. It should *not* be attached to any menu. The MPI/PD HL7 MESSAGE STATUS REPORT is generated from the ^XTMP("RGMT","HL" array. The report is sorted by RELATED EVENT PROTOCOL, date, transmission type, and status.

Either a detailed or summary report can be printed for a selected date range. The summary report displays the total number of messages for each date, transmission type, and status. The right margin for this report is 80.

The detailed report can be printed for a single or all protocols and includes information from each HL7 message. The detailed report displays the related EVENT PROTOCOL, DATE, TRANSMISSION TYPE, STATUS, MESSAGE HEADER DATE, DATE PROCESSED, INTERNAL ENTRY NUMBER (IEN) from the HL7 MESSAGE TEXT file (#772) , message identification number, and whether or not the message has been purged. The right margin for this report is 132.

|                                                    |                                   |
|----------------------------------------------------|-----------------------------------|
| MPI/PD HL7 ACTIVITY BY PATIENT/SINGLE PROTOCOL | \[RGMT DIAG SINGLE PROTOCOL\] |

This option prints information found during the COMPILE MPI/PD HL7 DATA compilation for activity related to a specific protocol. It should *not* be attached to any menu. The ^XTMP("RGMT","HL" array is searched for a user selected protocol, date range, transmission type and patient.

The report prints the patient's name, protocol, date range, transmission type, internal entry number (IEN) from the HL7 MESSAGE TEXT file (#772) , the date and status. The HL7 message data found in the MESSAGE TEXT field is displayed. The right margin for this report is 80.

|                                                  |                                 |
|--------------------------------------------------|---------------------------------|
| MPI/PD HL7 ACTIVITY BY PATIENT/ALL PROTOCOLS | \[RGMT DIAG ALL PROTOCOLS\] |

This option prints information found during the COMPILE MPI/PD HL7 DATA compilation for activity related to ALL protocols. It should *not* be attached to any menu. The ^XTMP("RGMT","HL" array is searched for a user selected patient and date range.

The report prints the patient's name, date range, protocol, transmission type, internal entry number (IEN) from the HL7 MESSAGE TEXT file (#772) , the date and status. The HL7 message data found in the MESSAGE TEXT field is displayed. The right margin for this report is 80.

Page intentionally left blank for double-sided print copy.

# Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### LOCAL/MISSING ICN RESOLUTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Background job: \[MPIF LOC/MIS ICN RES\]

This option starts a background job that assigns ICNs to the following types of person records, which have not been sent to the MVI:

- Person records that have local ICNs
- Person records that have been flagged as being active but do not have an ICN assignment.

It is recommended that this option be scheduled to run via TaskMan every 600 seconds (Patch MPIF\*1\*35).

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/054.png)</td>
<td><p><strong>NOTE:</strong> As of Patch MPI*1*38 (MPI Austin side for the MPIF*1*43 and RG*1*43), this background job no longer automatically adds patients to the MVI.</p>
<p>Previous to the release of this patch, when the Local/Missing ICN Resolution job was processed on the MVI, if a match wasn't found, the patient was added immediately. As of Patch MPI*1*38, this functionality has been changed in that if a match for a person isn't found on the MVI, a message is sent back to the site indicating this. On the site's side, this triggers an HL7 A28—Add Patient message, which then adds the person to the MVI.</p></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/055.png) | NOTE: A new field, LOCAL/MISSING DATE LAST RAN (#.04), was created in the CIRN SITE PARAMETER file (#991.8) to hold the last date the Local/Missing ICN Resolution Background job ran. The field will be populated by the routine ^MPIFRES. |

Local ICNs

ICNs are created for new person locally at the site when the MVI is unavailable or when the connection is lost prior to the assignment an ICN (e.g., the Direct Connect could not be established). A local ICN is also assigned as a placeholder when a person has been sent to the MVI but not yet added. This is to ensure identification of this person as these records await a response from the MPI. Local ICNs look like a national ICN. They contain the same number of digits as a national ICN. The only difference is that the first three digits are the VAMCs station number.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/056.png) | NOTE: It is not recommended that local ICNs be sent to remote databases as they will only be known at the local facility that assigned them. |

Missing ICNs

Missing ICNs result from person records which have been added to the PATIENT file (#2) via other means than through the Patient Information Management System (PIMS) options that establish the real-time connection with the MVI (Load/Edit Patient Data, Register a Patient, and Electronic 10-10EZ Processing). These records are flagged internally for inclusion in the Local/Missing ICN Resolution job.

Resolution of Local/Missing ICNs

The Local/Missing ICN Resolution background job should be scheduled via TaskMan to run every 600 seconds (Patch MPIF\*1\*35). The Local/Missing ICN Resolution job will find either of the following:

- All person entries in the local PATIENT file (#2) with a local ICN
- Person entries that have been flagged as missing an ICN

It then sends these persons to the MVI for a national ICN assignment. These person entries are sent to the MVI requesting an ICN, in batch HL7 messages (maximum of 100 patient entries each). They are processed on the MVI in the same manner as the person entries presented in the real-time connection, only in batch form instead of individual entries.

### UPDATE BATCH JOB FOR HL7 v2.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VAFC BATCH UPDATE\]

The event of updating patient information can take place from several different options within VistA, including VA FileMan. Changes to any of the fields listed in Table 6‑1 are recorded and an entry is created in the ADT/HL7 PIVOT file (#391.71). The entry is then marked as pending transmission. Direct sets to the globals cannot be collected. This background job will periodically collect (via a scheduled job) these marked events and broadcast an ADT-A08 Update Patient Information message. Because it is not possible to determine if the editing of the field is complete, this background job will periodically collect these marked events and broadcast an ADT A08 message (i.e., Update Patient Information). This is a PIMS-generated HL7 message.

<span id="_Ref161148850" class="anchor"></span>Table ‑. Data elements monitored in the PATIENT file (#2) for changes

| Field Number | Field Name                |
|------------------|-------------------------------|
| 2,.01            | NAME                          |
| 2,.02            | SEX                           |
| 2,.024           | SELF IDENTIFIED GENDER        |
| 2,.03            | DATE OF BIRTH                 |
| 2,.05            | MARITAL STATUS                |
| 2,.08            | RELIGIOUS PREFERENCE          |
| 2,.09            | SOCIAL SECURITY NUMBER        |
| 2,.0931          | PLACE OF BIRTH COUNTRY        |
| 2,.0932          | PLACE OF BIRTH PROVINCE       |
| 2,.111           | STREET ADDRESS \[LINE 1\]     |
| 2,.1112          | ZIP+4                         |
| 2,.112           | STREET ADDRESS \[LINE 2\]     |
| 2,.113           | STREET ADDRESS \[LINE 3\]     |
| 2,.114           | CITY                          |
| 2,.115           | STATE                         |
| 2,.116           | ZIP CODE                      |
| 2,.117           | COUNTY                        |
| 2,.1171          | PROVINCE                      |
| 2,.1172          | POSTAL CODE                   |
| 2,.1172          | COUNTRY                       |
| 2,.121           | BAD ADDRESS INDICATOR         |
| 2,.131           | PHONE NUMBER \[RESIDENCE\]    |
| 2,.132           | PHONE NUMBER \[WORK\]         |
| 2,.133           | EMAIL ADDRESS                 |
| 2,.134           | PHONE NUMBER \[CELLULAR\]     |
| 2,.211           | K-NAME OF PRIMARY NOK         |
| 2,.219           | K-PHONE NUMBER                |
| 2,.2403          | MOTHER'S MAIDEN NAME          |
| 2,.2405          | PREFERRED NAME                |
| 2,.301           | SERVICE CONNECTED?            |
| 2,.302           | SERVICE CONNECTED PERCENTAGE  |
| 2,.31115         | EMPLOYMENT STATUS             |
| 2,.313           | CLAIM NUMBER                  |
| 2,.323           | PERIOD OF SERVICE             |
| 2,.351           | DATE OF DEATH                 |
| 2,.352           | DEATH ENTERED BY              |
| 2,.353           | SOURCE OF NOTIFICATION        |
| 2,.354           | DATE OF DEATH LAST UPDATED    |
| 2,.355           | LAST EDITED BY                |
| 2,.357           | SUPPORTING DOCUMENT TYPE      |
| 2,.361           | PRIMARY ELIGIBILITY CODE      |
| 2,.525           | POW STATUS INDICATED?         |
| 2,2              | RACE INFORMATION              |
| 2,6              | ETHNICITY INFORMATION         |
| 2,391            | TYPE                          |
| 2,991.01         | INTEGRATION CONTROL NUMBER    |
| 2,991.02         | ICN CHECKSUM                  |
| 2,991.03         | COORDINATING MASTER OF RECORD |
| 2,991.04         | LOCALLY ASSIGNED ICN          |
| 2,991.05         | SUBSCRIPTION CONTROL NUMBER   |
| 2,991.06         | CMOR ACTIVITY SCORE           |
| 2,991.07         | SCORE CALCULATION DATE        |
| 2,991.08         | TEMPORARY ID NUMBER           |
| 2,991.09         | FOREIGN ID NUMBER             |
| 2,991.1          | FULL ICN                      |
| 2,994            | MULTIPLE BIRTH INDICATOR      |
| 2,1901           | VETERAN (Y/N)?                |
| 2.01,.01         | ALIAS                         |
| 2.01,1           | ALIAS SSN                     |
| 2.0991,.01       | FULL ICN HISTORY              |
| 2.0992,.01       | ICN HISTORY                   |

This background job also sends out Treating Facility "add me" and Treating Facility Update messages.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/057.png)</td>
<td><p><strong>NOTE:</strong> For more information on the ADT A08 Message- Update Patient Information, see the <em>Master Patient Index (MPI) VistA HL7 Interface Specifications</em> on the VA Web site:</p>
<blockquote>
<p><a href="http://www.va.gov/vdl/application.asp?appid=16">MPI/PD documentation on the VA Software Document Library (VDL)</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/058.png) | NOTE: This background job was originally exported in patch DG\*5.3\*91. |

# PIMS Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter documents in detail the daily interaction between the MVI and the following Patient Information Management System (PIMS) options:

- Load/Edit Patient Data \[DG LOAD PATIENT DATA\]
- Register a Patient \[DG REGISTER PATIENT\]
- Electronic 10-10EZ Processing \[EAS EZ 1010EZ PROCESSING\]

Two other PIMS options that do not interact with, but are impacted by the MVI are listed below.

- Patient Inquiry \[DG PATIENT INQUIRY\]
- Preregister a Patient \[DGPRE PRE-REGISTER OPTION\]

### Overview of PIMS Interaction with the MVI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the daily operations of the MVI, a real-time TCP/IP connection (Direct Connect) to the index is established via the Patient Information Management System (PIMS) options Load/Edit Patient Data, Register a Patient, and Electronic 10-10EZ Processing. This takes place when using these PIMS option to add persons to the PATIENT file (#2), or when selecting persons that already exist in the PATIENT file (#2), but do not have an Integration Control Number (ICN)—local ICN or national ICN. This direct connection to the MVI makes it possible for the immediate return of an ICN for a person that does not currently have one assigned in your site’s PATIENT file (#2).

Each time a patient is checked against the MVI via any one of these PIMS options, one of the following scenarios will occur:

1.  Patient is Not Found on the MVI:
- The patient is assigned an ICN and added to the index.

Figure 7‑1 shows the process for adding a new patient to the MVI and getting an ICN assignment.

|                                                                                                                |                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/059.png) | NOTE: The process for adding a new patient to the MVI is the same for each of the three PIMS options listed in this chapter. For the purposes of this example, we are using the PIMS option Register a Patient. |

<span id="_Ref41987873" class="anchor"></span>Figure ‑. No match found, patient is added to MVI

Select Registration Menu Option: REGISTER \<Enter\> a Patient

Select PATIENT NAME: MVIPATIENT,BAILEY

ARE YOU ADDING 'MVIPATIENT,BAILEY' AS A NEW PATIENT (THE 995TH)? No// Y \<Enter\> (Yes)

PATIENT SEX: M \<Enter\> MALE

PATIENT DATE OF BIRTH: 2/2/1952 \<Enter\> (FEB 02, 1952)

PATIENT SOCIAL SECURITY NUMBER: 666376847

PATIENT TYPE: SC \<Enter\> VETERAN

PATIENT VETERAN (Y/N)?: Y \<Enter\> YES

PATIENT SERVICE CONNECTED?: N \<Enter\> YES

PATIENT MULTIPLE BIRTH INDICATOR: N \<Enter\> NO

...searching for potential duplicates

No potential duplicates have been identified.

...adding new patient

Please enter the following additional information:

Patient name components--

FAMILY (LAST) NAME: MVIPATIENT// \<Enter\>

GIVEN (FIRST) NAME: BAILEY// \<Enter\>

MIDDLE NAME: \<Enter\>

PREFIX: \<Enter\>

SUFFIX: \<Enter\>

DEGREE:

Press ENTER to continue

Please verify or update the following information:

MOTHER'S MAIDEN NAME: MPIMAIDENNAME

PLACE OF BIRTH \[CITY\]: BROOKLYN

PLACE OF BIRTH \[STATE\]: NEW YORK

Select ALIAS: \<Enter\>

Attempting to connect to the Master Patient Index in Austin...

If no SSN or inexact DOB or common name, this request

may take some time, please be patient...

Patient was not found in the MPI...

Message sent to MPI requesting Patient to be added.

MVIPATIENT,BAILEY 666-37-6847 FEB 2,1952

=============================================================================

Address: STREET ADDRESS UNKNOWN Temporary: NO TEMPORARY ADDRESS

UNK. CITY/STATE

County: UNSPECIFIED From/To: NOT APPLICABLE

Phone: UNSPECIFIED Phone: NOT APPLICABLE

Office: UNSPECIFIED

Bad Addr:

Confidential Address: Confidential Address Categories:

NO CONFIDENTIAL ADDRESS

From/To: NOT APPLICABLE

Primary Eligibility: UNSPECIFIED

Other Eligibilities:

MVIPATIENT,BAILEY 666-37-6847 FEB 2,1952

=============================================================================

Status : PATIENT HAS NO INPATIENT OR LODGER ACTIVITY IN THE COMPUTER

Future Appointments: NONE

Remarks:

Money Verified: NOT VERIFIED Service Verified: NOT VERIFIED

Do you wish to request a HINQ inquiry ? No// \<Enter\> (No)

Select Admitting Area: ^

Financial query sent ...

Do you want to enter Patient Data? Yes// N \<Enter\> (No)

Checking data for consistency...

===\> 12 inconsistencies found in 0 seconds...

===\> 12 inconsistencies filed in 0 seconds...

MVIPATIENT,BAILEY (666-37-6847) FEB 2,1952

==============================================================================

5 - MARITAL STATUS UNSPECIFIED 6 - RELIGION UNSPECIFIED

8 - ADDRESS DATA INCOMPLETE 12 - SC% UNSPECIFIED FOR SC VET

13 - POS UNSPECIFIED 14 - ELIG CODE UNSPECIFIED

52 - INSURANCE PROMPT UNANSWERED 53 - EMPLOYMENT STATUS UNANSWERED

55 - INCOME DATA MISSING\*\* 61 - MISSING PHONE NUMBER DATA

62 - EMERGENCY CONTACT NAME MISSING 99 - CAN'T PROCESS FURTHER

Inconsistencies followed by two (2) asterisks \[\*\*\] must be corrected by

using the appropriate MAS menu option(s).

All items not followed by an asterisk can be edited at this time. If these

items are not corrected at this time, a bulletin will be sent to the

appropriate hospital personnel.

DO YOU WANT TO UPDATE THESE INCONSISTENCIES NOW? Yes// N \<Enter\> (No)

Initial notification message sent...

Is the patient currently being followed in a clinic for the same condition? N \<Enter\> (No)

Is the patient to be examined in the medical center today? Yes// ^

2.  Record Match Found for Patient on the MVI:
- If the ICN for the person is found, your site is added to the list of treating facilities (correlation list) where the patient has been seen.

Figure 7‑2 shows the MVI process for updating the ICN if a match is found for the person on the index.

|                                                                                                                |                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/060.png) | NOTE: The MVI process for updating the ICN if a match is found is the same for each of the PIMS options listed in this chapter. For the purposes of this example, we are using the PIMS option Register a Patient. |

<span id="_Ref43706819" class="anchor"></span>Figure ‑. Exact Match found on MVI. PATIENT file (#2) updated

Select Registration Menu Option: register \<Enter\> a Patient

Select PATIENT NAME: MVIPATIENT,ASHTON

ARE YOU ADDING 'MVIPATIENT,ASHTON' AS A NEW PATIENT (THE 698TH)? No// Y \<Enter\> (Yes)

PATIENT SEX: M \<Enter\> MALE

PATIENT DATE OF BIRTH: FEB 22,1949 \<Enter\> (FEB 22, 1949)

PATIENT SOCIAL SECURITY NUMBER: 666789899

PATIENT TYPE: SC \<Enter\> VETERAN

PATIENT VETERAN (Y/N)?: Y \<Enter\> YES

PATIENT SERVICE CONNECTED?: Y \<Enter\> YES

PATIENT MULTIPLE BIRTH INDICATOR: N \<Enter\> NO

...searching for potential duplicates

No potential duplicates have been identified.

...adding new patient

Please enter the following additional information:

Patient name components--

FAMILY (LAST) NAME: MVIPATIENT// \<Enter\> MVIPATIENT

GIVEN (FIRST) NAME: ASHTON// \<Enter\> ASHTON

MIDDLE NAME: \<Enter\>

PREFIX: \<Enter\>

SUFFIX: \<Enter\>

DEGREE: \<Enter\>

Press ENTER to continue

Please verify or update the following information:

MOTHER'S MAIDEN NAME: MPIMAIDENNAME

PLACE OF BIRTH \[CITY\]: VAMCSITE

PLACE OF BIRTH \[STATE\]: NEW YORK

Select ALIAS: \<Enter\>

Attempting to connect to the Master Patient Index in Austin...

If no SSN or inexact DOB or common name, this request

may take some time, please be patient...

Found Patient MVIPATIENT,ASHTON in MPI, updating ICN to 1008596062V680332

MVIPATIENT,ASHTON 666-78-9899 FEB 22, 1949

=============================================================================

Address: STREET ADDRESS UNKNOWN Temporary: NO TEMPORARY ADDRESS

UNK. CITY/STATE

County: UNSPECIFIED From/To: NOT APPLICABLE

Phone: UNSPECIFIED Phone: NOT APPLICABLE

Office: UNSPECIFIED

POS: UNSPECIFIED Claim \#: UNSPECIFIED

Relig: UNSPECIFIED Sex: MALE

Primary Eligibility: UNSPECIFIED

Other Eligibilities:

MVIPATIENT,ASHTON 666-78-9899 FEB 22, 1949

=============================================================================

Status : PATIENT HAS NO INPATIENT OR LODGER ACTIVITY IN THE COMPUTER

Future Appointments: NONE

Remarks:

Money Verified: NOT VERIFIED Service Verified: NOT VERIFIED

Do you wish to request a HINQ inquiry ? No// \<Enter\> (No)

Select Admitting Area: ^

3.  MVI has Potential Match(es) to Patient’s Identifying Information:
1.  The person is assigned a new ICN and added to the index.
2.  A potential match exception is logged for HC IdM to review.

|                                                                                                                |                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/061.png) | NOTE: As of MPI/PD Patch MPIF\*1\*52, all screens and actions associated with the MPI/PD Exception Handler functionality for resolving Potential Match Exceptions have been removed from MPI/PD. This functionality is now supported in the Identity Management Toolkit. |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/062.png)</td>
<td><p><strong>NOTE:</strong> As of VistA Patch RG*1*43, all existing exceptions that were active in the CIRN HL7 EXCEPTION LOG file (#991.1) of the types listed below, were marked with a status of PROCESSED:</p>
<ul>
<li><p>Required field(s) missing for person sent to MVI</p></li>
<li><p>SSN Match Failed</p></li>
<li><p>Name Doesn't Match</p></li>
</ul>
<p>These three exceptions listed are no longer generated.</p>
<p>Existing patient records that had these exceptions at the time of in installation of RG*1*43 were sent to the MVI again, and under the latest business rules, were assigned ICNs.</p></td>
</tr>
</tbody>
</table>

### PIMS Option: Load/Edit Patient Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the interaction of the MVI and the Patient Information Management System (PIMS) option Load/Edit Patient Data. The user attempting to do the following:

1.  Add a person to the local PATIENT file (#2) and to the MVI for the first time.
2.  Select a person record for processing that currently exists in the local PATIENT file (#2) and who already has an ICN.

#### Add New Person to MVI for First Time

Figure 7‑3 shows a new person being added to the PATIENT file (#2) using the PIMS option Load/Edit Patient Data. The patient is being added to the MVI for the first time. The MVI will return an ICN for that patient. Boldface text shows that the following procedures are taking place:

- A connection is made to the MVI.
- There is currently no matching patient entry in the MVI for this person.
- The person is added to the MVI.

Once a person has been added to the MVI, the corresponding ICN field in the PATIENT file (#2) is updated.

<span id="_Ref43707028" class="anchor"></span>Figure ‑. Load/Edit Patient Data–Add person to PATIENT file (#2) and MVI for first time

Select Registration Menu Option: LOAD/EDIT \<Enter\> Patient Data

Select PATIENT NAME: MVIPATIENT,CHRISTIAN

ARE YOU ADDING 'MVIPATIENT,CHRISTIAN' AS A NEW PATIENT (THE 971ST)? No// Y\<Enter\> (Yes)

PATIENT SEX: M \<Enter\> MALE

PATIENT DATE OF BIRTH: 2/28/70 \<Enter\> (FEB 28, 1970)

PATIENT SOCIAL SECURITY NUMBER: 666548444

PATIENT TYPE: NSC \<Enter\> VETERAN

PATIENT VETERAN (Y/N)?: Y \<Enter\> (YES)

PATIENT SERVICE CONNECTED?: N \<Enter\> NO

PATIENT MULTIPLE BIRTH INDICATOR: ??

The MULTIPLE BIRTH INDICATOR will designate whether or not

the patient is part of a multiple birth (i.e. to identify

twins, etc.).

Choose from:

N NO

Y \*MULTIPLE BIRTH\*

PATIENT MULTIPLE BIRTH INDICATOR: N \<Enter\> NO

...searching for potential duplicates

No potential duplicates have been identified.

...adding new patient

Please enter the following additional information:

Patient name components--

FAMILY (LAST) NAME: MVIPATIENT// \<Enter\>

GIVEN (FIRST) NAME: CHRISTIAN// \<Enter\>

MIDDLE NAME:

PREFIX: \<Enter\>

SUFFIX: \<Enter\>

DEGREE: \<Enter\>

Press ENTER to continue

Please verify or update the following information:

MOTHER'S MAIDEN NAME: MPIMADENNAME

PLACE OF BIRTH \[CITY\]: \<Enter\>

PLACE OF BIRTH \[STATE\]: NEW YORK

Select ALIAS: \<Enter\>

Attempting to connect to the Master Patient Index in Austin...

If no SSN or inexact DOB or common name, this request

may take some time, please be patient...

Patient was not found in the MPI...

Message sent to MPI requesting Patient to be added.

MVIPATIENT,CHRISTIAN 666-54-8444 FEB 28,1970

=============================================================================

Address: STREET ADDRESS UNKNOWN Temporary: NO TEMPORARY ADDRESS

UNK. CITY/STATE

County: UNSPECIFIED From/To: NOT APPLICABLE

Phone: UNSPECIFIED Phone: NOT APPLICABLE

Office: UNSPECIFIED

Confidential Address: Confidential Address Categories:

NO CONFIDENTIAL ADDRESS

From/To: NOT APPLICABLE

Primary Eligibility: UNSPECIFIED

Other Eligibilities:

MVIPATIENT,CHRISTIAN 666-54-8444 FEB 28,1970

=============================================================================

Status : PATIENT HAS NO INPATIENT OR LODGER ACTIVITY IN THE COMPUTER

Future Appointments: NONE

Remarks:

Money Verified: NOT VERIFIED Service Verified: NOT VERIFIED

Do you wish to request a HINQ inquiry ? No// \<Enter\> (No)

Financial query sent ...

Do you want to enter Patient Data? Yes// N\<Enter\> (No)

Checking data for consistency...

===\> 12 inconsistencies found in 0 seconds...

===\> 12 inconsistencies filed in 0 seconds...

MVIPATIENT,CHRISTIAN (666-54-8444) FEB 28,1970

==============================================================================

5 - MARITAL STATUS UNSPECIFIED 6 - RELIGION UNSPECIFIED

8 - ADDRESS DATA INCOMPLETE 13 - POS UNSPECIFIED

14 - ELIG CODE UNSPECIFIED 52 - INSURANCE PROMPT UNANSWERED

53 - EMPLOYMENT STATUS UNANSWERED 55 - INCOME DATA MISSING\*\*

61 - MISSING PHONE NUMBER DATA 62 - EMERGENCY CONTACT NAME MISSING

64 - POB CITY/STATE MISSING 99 - CAN'T PROCESS FURTHER

Inconsistencies followed by two (2) asterisks \[\*\*\] must be corrected by

using the appropriate MAS menu option(s).

All items not followed by an asterisk can be edited at this time. If these

items are not corrected at this time, a bulletin will be sent to the

appropriate hospital personnel.

DO YOU WANT TO UPDATE THESE INCONSISTENCIES NOW? Yes// N \<Enter\> (No)

Initial notification message sent...

Download VIC data? No// \<Enter\> (No)

#### Process Existing Person Already on MVI

Figure 7‑4 shows that once patients have been added to the MVI, they are assigned an ICN. Anytime the PIMS option Load/Edit Patient Data (or any of the other two PIMS options: Register a Patient, or Electronic 10-10EZ Processing) is used to process an existing person that has an ICN.

<span id="_Ref43707062" class="anchor"></span>Figure ‑. Load/Edit Patient Data—Select patient for processing already having ICN and CMOR

Select Registration Menu Option: LOAD/EDIT \<Enter\> Patient Data

Select PATIENT NAME: MVIPATIENT,ROE \<Enter\> MVIPATIENT,ROE 9-8-42 666678889 NO NSC VETERAN

Please verify or update the following information:

PLACE OF BIRTH \[CITY\]:

PLACE OF BIRTH \[STATE\]:

Select ALIAS:

MVIPATIENT,ROE 666-67-8889 SEP 8,1942

=============================================================================

Address: STREET ADDRESS UNKNOWN Temporary: NO TEMPORARY ADDRESS

UNK. CITY/STATE

County: UNSPECIFIED From/To: NOT APPLICABLE

Phone: UNSPECIFIED Phone: NOT APPLICABLE

Office: UNSPECIFIED

Bad Addr:

Confidential Address: Confidential Address Categories:

NO CONFIDENTIAL ADDRESS

From/To: NOT APPLICABLE

Primary Eligibility: UNSPECIFIED

Other Eligibilities:

### PIMS Option: Register a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This topic describes the interaction between the MPI and the Patient Information Management System (PIMS) option Register a Patient when processing an existing patient. This patient does not have an ICN assignment.

Boldface is used to highlight user responses to online prompts. It is also used to highlight computer dialogue that is new to this PIMS option based on its interaction with the MPI, showing:

1.  A connection being made to the MVI.
2.  That there are currently no matching person entries in the MVI for this person.
3.  The person being added to the MVI.

Once a person has been added to the MVI, the corresponding ICN field in the PATIENT file (#2) is updated.

<span id="_Ref43707394" class="anchor"></span>Figure ‑. Register a Patient- Add new person, and connect to MVI for first time

Select Registration Menu Option: REGISTER \<Enter\> a Patient

Select PATIENT NAME: MVIPATIENT,JOE

ARE YOU ADDING 'MVIPATIENT,JOE' AS A NEW PATIENT (THE 973RD)? No// Y \<Enter\> (Yes)

PATIENT SEX: M \<Enter\> MALE

PATIENT DATE OF BIRTH: 2/29/76 \<Enter\> (FEB 29, 1976)

PATIENT SOCIAL SECURITY NUMBER: 666433245

PATIENT TYPE: NSC \<Enter\> VETERAN

PATIENT VETERAN (Y/N)?: Y \<Enter\> (YES)

PATIENT SERVICE CONNECTED?: Y \<Enter\> YES

PATIENT MULTIPLE BIRTH INDICATOR: N \<Enter\> NO

...searching for potential duplicates

No potential duplicates have been identified.

...adding new patient

Please enter the following additional information:

Patient name components--

FAMILY (LAST) NAME: MVIPATIENT// \<Enter\>

GIVEN (FIRST) NAME: JOE// \<Enter\>

MIDDLE NAME: \<Enter\>

PREFIX: \<Enter\>

SUFFIX: JR

DEGREE: \<Enter\>

Ok to file 'MVIPATIENT,JOE' and its name components? Yes// \<Enter\> (Yes)

Please verify or update the following information:

MOTHER'S MAIDEN NAME: MPIMADENNAME

PLACE OF BIRTH \[CITY\]: \<Enter\>

PLACE OF BIRTH \[STATE\]: NY \<Enter\> NEW YORK

Select ALIAS: \<Enter\>

Attempting to connect to the Master Patient Index in Austin...

If no SSN or inexact DOB or common name, this request

may take some time, please be patient...

Patient was not found in the MPI...

Message sent to MPI requesting Patient to be added.

MVIPATIENT,JOE 666-43-3245 FEB 29,1976

=============================================================================

Address: STREET ADDRESS UNKNOWN Temporary: NO TEMPORARY ADDRESS

UNK. CITY/STATE

County: UNSPECIFIED From/To: NOT APPLICABLE

Phone: UNSPECIFIED Phone: NOT APPLICABLE

Office: UNSPECIFIED

Confidential Address: Confidential Address Categories:

NO CONFIDENTIAL ADDRESS

From/To: NOT APPLICABLE

Primary Eligibility: UNSPECIFIED

Other Eligibilities:

MVIPATIENT,JOE 666-43-3245 FEB 29,1976

=============================================================================

Status : PATIENT HAS NO INPATIENT OR LODGER ACTIVITY IN THE COMPUTER

Future Appointments: NONE

Remarks:

Money Verified: NOT VERIFIED Service Verified: NOT VERIFIED

Do you wish to request a HINQ inquiry ? No// \<Enter\> (No)

Select Admitting Area: ??

Choose from:

VAMCSITE ADMITTING

TROY ADMITTING

Select Admitting Area: VAMCSITE \<Enter\> ADMITTING

PRINT BARCODE LABELS FOR PATIENT'S FOLDERS? YES// \<Enter\>

ISSUE REQUEST FOR RECORDS? NO// \<Enter\>

Financial query sent ...

Do you want to enter Patient Data? Yes// N \<Enter\> (No)

Checking data for consistency...

===\> 12 inconsistencies found in 0 seconds...

===\> 12 inconsistencies filed in 0 seconds...

MVIPATIENT,JOE (666-43-3245) FEB 29,1976

==============================================================================

5 - MARITAL STATUS UNSPECIFIED 6 - RELIGION UNSPECIFIED

8 - ADDRESS DATA INCOMPLETE 13 - POS UNSPECIFIED

14 - ELIG CODE UNSPECIFIED 52 - INSURANCE PROMPT UNANSWERED

53 - EMPLOYMENT STATUS UNANSWERED 55 - INCOME DATA MISSING\*\*

61 - MISSING PHONE NUMBER DATA 62 - EMERGENCY CONTACT NAME MISSING

64 - POB CITY/STATE MISSING 99 - CAN'T PROCESS FURTHER

Inconsistencies followed by two (2) asterisks \[\*\*\] must be corrected by

using the appropriate MAS menu option(s).

All items not followed by an asterisk can be edited at this time. If these

items are not corrected at this time, a bulletin will be sent to the

appropriate hospital personnel.

DO YOU WANT TO UPDATE THESE INCONSISTENCIES NOW? Yes// N \<Enter\> (No)

Initial notification message sent...

Is the patient currently being followed in a clinic for the same condition? N \<Enter\> (No)

Is the patient to be examined in the medical center today? Yes// N \<Enter\> (No)

Registration login date/time: NOW// \<Enter\> (MAY 13,2003@07:47)

TYPE OF BENEFIT APPLIED FOR: 3 \<Enter\> OUTPATIENT MEDICAL

TYPE OF CARE APPLIED FOR: 5 \<Enter\> ALL OTHER

FACILITY APPLYING TO: VAMCSITE// \<Enter\> 500A

REGISTRATION ELIGIBILITY CODE: HUMANITARIAN EMERGENCY

// 6 \<Enter\> 6 NON-VETERAN

Updating eligibility status for this registration...

NEED RELATED TO AN ACCIDENT: N \<Enter\> NO

NEED RELATED TO OCCUPATION: N \<Enter\> NO

Do you wish to enroll in the VA Patient Enrollment System? YES// \<Enter\>

ENROLLMENT APPLICATION DATE: MAY 13, 2003// \<Enter\>

PREFERRED FACILITY: VAMCSITE// \<Enter\>

Application is pending for enrollment in the VA Patient Enrollment System...

Enrollment Date : -none-

Enrollment Application Date : MAY 13, 2003

Enrollment Category : IN PROCESS

Enrollment Status : UNVERIFIED

Enrollment Priority : -none-

Preferred Facility : VAMCSITE

Enrollment Group Threshold : GROUP 8c

PRINT 10/10? Yes// N \<Enter\> (No)

ROUTING SLIP? Yes// N \<Enter\> (No)

Download VIC data? No// \<Enter\> (No)

### Patient Sensitivity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a shared person is flagged as sensitive at one of the treating facility sites, a bulletin is sent to the RG CIRN DEMOGRAPHIC ISSUES mail group at each treating facility telling where, when, and by whom the flag was set. Each site can then review whether the circumstances meet the local criteria for sensitivity flagging.

### MVI Direct Connection Unavailable: Local ICN Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 7‑8 shows the computer dialogue resulting from the MVI unexpectedly becoming unavailable while the direct connection is in use. If this happens, a local ICN is assigned to the patient being processed. This allows the user to continue processing the current patient and flags this patient as needing a national ICN. Patient records having received Local ICN assignment will be resolved through the Local/Missing ICN Resolution Background Job (i.e., MPIF LOC/MIS ICN RES).

The process is the same for each of the three PIMS options listed in this chapter. However, we will use the PIMS option Register a Patient for the purposes of this example, Figure 7‑8.

<span id="_Ref75742040" class="anchor"></span>Figure 7‑6. Computer dialogue displayed if MVI direct connection becomes unavailable

Select OPTION NAME: Register a Patient

Select PATIENT NAME: MVIPATIENT,DOE

ARE YOU ADDING 'MVIPATIENT,DOE' AS A NEW PATIENT (THE 276TH)? No// Y \<Enter\> (Yes)

PATIENT SEX: F \<Enter\> FEMALE

PATIENT DATE OF BIRTH: 090817 \<Enter\> (SEP 08, 1917)

PATIENT SOCIAL SECURITY NUMBER: 666099589

PATIENT TYPE: SC VETERAN

PATIENT VETERAN (Y/N)?: Y \<Enter\> YES

PATIENT SERVICE CONNECTED?: N \<Enter\> NO

PATIENT MULTIPLE BIRTH INDICATOR: ??

The MULTIPLE BIRTH INDICATOR will designate whether or not

the patient is part of a multiple birth (i.e. to identify

twins, etc.).

Choose from:

N NO

Y \*MULTIPLE BIRTH\*

PATIENT MULTIPLE BIRTH INDICATOR: N \<Enter\> NO

...searching for potential duplicates

No potential duplicates have been identified.

...adding new patient

Please enter the following additional information:

Patient name components—

FAMILY (LAST) NAME: DOE//

GIVEN (FIRST) NAME: CHRISTINE//

MIDDLE NAME:

PREFIX:

SUFFIX:

DEGREE:

Press ENTER to continue

Please verify or update the following information:

MOTHER’S MAIDEN NAME: MPIMADENNAME

PLACE OF BIRTH \[CITY\]: BILLINGS

PLACE OF BIRTH \[STATE\]: MONTANA

Select ALIAS:

Attempting to connect to the Master Patient Index in Austin...

If no SSN or inexact DOB or common name, this request

may take some time, please be patient

Could not connect to the MPI or Timed Out, assigning local ICN (if not already

assigned). . .

New page:

MVIPATIENT,DOE 666-09-9589 SEP 8,1917

========================================================================

Address: STREET ADDRESS UNKNOWN Temporary: NO TEMPORARY ADDRESS

UNK. CITY/STATE

County: UNSPECIFIED From/To: NOT APPLICABLE

Phone: UNSPECIFIED Phone: NOT APPLICABLE

Office: UNSPECIFIED

Primary Eligibility: UNSPECIFIED

Other Eligibilities:

Status : PATIENT HAS NO INPATIENT OR LODGER ACTIVITY IN THE COMPUTER

Future Appointments: NONE

Remarks:

*(This option continues as it would normally…)*

### Under What Conditions are Local ICNs Assigned to Patient Records?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are conditions in which local ICNs are assigned to patient records:

- The site's VistA system cannot connect to the MVI.
- The site edits an existing patient or adds a new patient using an option that doesn't directly interact with the MVI (e.g., VistA Laboratory or VA FileMan).
- The site attempts to add a patient; however, something happens to hold up transmission to the MVI causing a delay in national ICN assignment. In this instance, a local ICN is assigned as an interim placeholder to the patient entry until a national ICN is returned. Local ICN assignments made in this situation facilitate these types of patient entries to be easily identifiable.

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>.001 Field</strong></th>
<th colspan="2">A field containing the internal entry number of the record.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>.01 Field</strong></td>
<td colspan="2">The one field that must be present for every file and file entry. It is also called the NAME field. At a file's creation the .01 field is given the label NAME. This label can be changed.</td>
</tr>
<tr class="even">
<td><strong>10-10EZ</strong></td>
<td colspan="2">Form used to apply for health benefits.</td>
</tr>
<tr class="odd">
<td><strong>Abbreviated Response</strong></td>
<td colspan="2">This feature allows you to enter data by typing only the first few characters for the desired response. This feature will not work unless the information is already stored in the computer.</td>
</tr>
<tr class="even">
<td><strong>Accept Agreement</strong></td>
<td colspan="2">Part of the validation and agreement to the privacy regulations associated with Toolkit (IdM TK).</td>
</tr>
<tr class="odd">
<td><strong>Access Code</strong></td>
<td colspan="2">A code that, along with the Verify code, allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than 6 and less than 20 characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator. It is used by the Kernel's Sign-on/Security system to identify the user (see Verify Code).</td>
</tr>
<tr class="even">
<td><strong>Active Patients</strong></td>
<td colspan="2">Persons who have been seen at a site within the past three years.</td>
</tr>
<tr class="odd">
<td><strong>ADPAC</strong></td>
<td colspan="2">Automated Data Processing Application Coordinator.</td>
</tr>
<tr class="even">
<td><strong>ADR</strong></td>
<td colspan="2">The Administrative Data Repository is the authoritative data store within VHA for cross-cutting person administrative information. The Administrative Data Repository contains identification and cross-cutting demographics data as well as other administrative information. Patient Information Management System (PSIM) uploads the identity demographic data to the ADR. May also include subset of the Enrollment database. May also be referred to as ADR-N or ADR-L to designate a national or local instance.</td>
</tr>
<tr class="odd">
<td><strong>ADT</strong></td>
<td colspan="2">Admission Discharge and Transfer- Part of the Patient Information Management System (PIMS).</td>
</tr>
<tr class="even">
<td><strong>ADT/HL7 PIVOT File</strong></td>
<td colspan="2">Changes to any of the fields of person information will be recorded and an entry created in the ADT/HL7 PIVOT file (#391.71). When an update to a person's treating facility occurs, this event is to be added to the ADT/HL7 PIVOT file (#391.71) and marked for transmission. A background job will collect these updates and broadcast the appropriate HL7 message (ADT-A08 Patient Update).</td>
</tr>
<tr class="odd">
<td><strong>AITC</strong></td>
<td colspan="2">The Master Patient Index (MPI) is located at the Austin Information Technology Center (AITC).</td>
</tr>
<tr class="even">
<td><strong>Alerts</strong></td>
<td colspan="2">Brief online notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide interactive notification of pending computing activities, such as the need to reorder supplies or review a patient's clinical test results. Along with the alert message is an indication that the View Alerts common option should be chosen to take further action.</td>
</tr>
<tr class="odd">
<td><strong>Ancillary Reviewer</strong></td>
<td colspan="2">This can be a single person or group of people given the responsibility to conduct reviews of potential duplicate record pairs with data in files other than the PATIENT file (#2). For example, selected personnel in Laboratory, Radiology, and Pharmacy.</td>
</tr>
<tr class="even">
<td><strong>ANSI</strong></td>
<td colspan="2">American National Standards Institute.</td>
</tr>
<tr class="odd">
<td><strong>ANSI M</strong></td>
<td colspan="2">The M (formerly known as MUMPS) programming language is a standard recognized by the American National Standard Institute (ANSI). M stands for Massachusetts Utility Multi-programming System.</td>
</tr>
<tr class="even">
<td><strong>API</strong></td>
<td colspan="2"><p>Program calls provided for use by application programmers. APIs allow programmers to carry out standard computing activities without needing to duplicate utilities in their own software. APIs also further DBA goals of system integration by channeling activities, such as adding new users, through a limited number of callable entry points. VistA APIs fall into the following three categories:</p>
<ul>
<li><p>The first category is "Supported API" These are callable routines, which are supported for general use by all VistA applications.</p></li>
<li><p>The second category is "Controlled Subscription API." These are callable routines for which you must obtain an Integration Agreement (IA - formerly referred to as a DBIA) to use.</p></li>
<li><p>The third category is "Private API," where only a single application is granted permission to use an attribute/function of another VistA package.</p></li>
</ul>
<p>These IAs are granted for special cases, transitional problems between versions, and release coordination.</p></td>
</tr>
<tr class="odd">
<td><strong>application</strong></td>
<td colspan="2">Any software that executes logic or rules which allow people to interface with the computer and programs which collect, manipulate, summarize, and report data and information. .</td>
</tr>
<tr class="even">
<td><strong>Application Coordinator</strong></td>
<td colspan="2">Designated individuals responsible for user-level management and maintenance of an application package such as IFCAP, Lab, Pharmacy, Mental Health, etc.</td>
</tr>
<tr class="odd">
<td><strong>Application Server</strong></td>
<td colspan="2">Software/hardware for handling complex interactions between users, business logic, and databases in transaction-based, multi-tier applications. Application servers, also known as app servers, provide increased availability and higher performance.</td>
</tr>
<tr class="even">
<td><strong>Array</strong></td>
<td colspan="2">An arrangement of elements in one or more dimensions. An M array is a set of nodes referenced by subscripts that share the same variable name.</td>
</tr>
<tr class="odd">
<td><strong>AT-SIGN ("@")</strong></td>
<td colspan="2">A VA FileMan security Access code that gives the user programmer-level access to files and to VA FileMan's developer features. See Programmer Access. Also, the character "@" (i.e., at-sign, Shift-2 key on most keyboards) is used at VA FileMan field prompts to delete data.</td>
</tr>
<tr class="even">
<td><strong>Attribute</strong></td>
<td colspan="2"><p>VHA Definition:</p>
<ul>
<li><p>These are Persons Traits or Meta-Data about the Primary View or the Correlation.</p></li>
</ul>
<p>Identity Hub™ Definition:</p>
<ul>
<li><p>Members have attributes, like Name, Gender, Address, Phone, Birth Date, SSN.</p></li>
<li><p>Attributes are stored in tables according to Segments. Segments are “attribute types” The MEMPHONE segment can hold Home Phone, Cell Phone, and Fax Number information.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Authentication</strong></td>
<td colspan="2">Verifying the identity of the end-user.</td>
</tr>
<tr class="even">
<td><strong>Authorization</strong></td>
<td colspan="2">Granting or denying user access or permission to perform a function.</td>
</tr>
<tr class="odd">
<td><strong>Auto Link Threshold or Threshold, Auto Link</strong></td>
<td colspan="2">The Auto Link Threshold is the level that a Comparison Score must meet or exceed in order for two or more Identity Profiles to be considered the same unique Person Identity.</td>
</tr>
<tr class="even">
<td><strong>Auto-Update</strong></td>
<td colspan="2">The term "auto-update" refers to fields that are updated from a central database (i.e., the Master Veteran Index).</td>
</tr>
<tr class="odd">
<td><strong>Bad Address Indicator (BAI)</strong></td>
<td colspan="2"><p>The Bad Address Indicator field applies to the address at which the person resides. This field should be set as follows (if applicable):</p>
<ul>
<li><p>"UNDELIVERABLE" - Bad Address based on returned mail.</p></li>
<li><p>"HOMELESS" - Patient is known to be homeless.</p></li>
<li><p>"OTHER" - Other Bad Address Reason</p></li>
</ul>
<p>Setting this field will prevent a Bad Address from being shared with HEC and other VAMC facilities. It will also be used to block Means Test Renewal Letters from being sent. Once the Bad Address Indicator is set, incoming “newer" addresses will automatically remove the Bad Address Indicator, and allow the "updated" address to be transmitted to HEC and other VAMC Facilities.</p></td>
</tr>
<tr class="even">
<td><strong>Batch Acknowledgements</strong></td>
<td colspan="2">The format of a HL7 batch acknowledgement message consists entirely of a group of ACK (acknowledgment) messages. In the case of MVI, batch acknowledgements are returned during the initialization process and during the Local/Missing ICN Resolution job. The background job files the ICN, updates the MVI, and then the associated treating facilities and systems. Data returned from this process constitute the acknowledgment of the batch message.</td>
</tr>
<tr class="odd">
<td><strong>Batch Messages</strong></td>
<td colspan="2">There are instances when it is convenient to transfer a batch of HL7 messages. Common examples related to MVI are queries sent to the MVI for an ICN during the initialization process, the resolution of Local or Missing ICNs, and. Such a batch could be sent online using a common file transfer protocol. In the case of the MVI, the HL7 Batch Protocol uses the Batch Header Segment (BHS) and Batch Trailer Segment (BTS) message segments to delineate the batch.</td>
</tr>
<tr class="even">
<td><strong>BHIE</strong></td>
<td colspan="2">Bidirectional Health Information Exchange (Bidirectional Health Information Exchange (BHIE) Web site )</td>
</tr>
<tr class="odd">
<td><strong>Birth Sex</strong></td>
<td>Birth Sex refers to what is recorded on the Veteran’s original birth certificate: male or female. Some people may have changed their birth certificate later. However, the appropriate response for this field is what is recorded on the original birth certificate.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Bulletins</strong></td>
<td colspan="2">Electronic mail messages that are automatically delivered by VistA MailMan under certain conditions. For example, a bulletin can be set up to "fire" when database changes occur, such as adding a new Institution in the INSTITUTION file (#4). Bulletins are fired by bulletin-type cross-references.</td>
</tr>
<tr class="odd">
<td><strong>Business Requirements</strong></td>
<td colspan="2"><ul>
<li><p>Requirements state the customer needs the project output will satisfy. Requirements typically start with phrase “The system shall …” Business requirements refers to how the project will satisfy the business mission of the customer.</p></li>
<li><p>Business requirements refer to business functions of the project, such as project management, financial management, or change management.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Business Rule</strong></td>
<td colspan="2"><ul>
<li><p>A policy imposed by the business, or an external entity, on the system used in the process of conducting that business.</p></li>
<li><p>A special category of a requirement. A business rule is directive, policy, or procedure within an organization that describes the relationship between two or more entities. Business rules may also come from outside sources such as government regulations and membership association guidelines.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Cache</strong></td>
<td colspan="2">Cache memory is a small area of very fast RAM used to speed exchange of data. Also, a file or directory included on your computer's hard drive which automatically stores the text and graphics from a web page you pull up, which, in turn, allows you to go back to that web page, without having to wait for the information to reload.</td>
</tr>
<tr class="even">
<td><strong>CAIP</strong></td>
<td colspan="2">Cross-Application Integration Protocol. A framework which provides both applications and services with support for software procedure calls across systems and applications that rely upon infrastructure and middleware technologies, while simultaneously minimizing the direct dependencies of these same applications and services upon these enabling technologies.</td>
</tr>
<tr class="odd">
<td><strong>Callable Entry Point</strong></td>
<td colspan="2">An authorized programmer call that may be used in any VistA application package. The DBA maintains the list of DBIC-approved entry points.</td>
</tr>
<tr class="even">
<td><strong>CAPRI</strong></td>
<td colspan="2">Compensation &amp; Pension Records Interchange (CAPRI). This Graphical User Interface (GUI) software is used to access veterans’ electronic medical records throughout the VA. The Healthcare Identity Management (HC IdM) Team uses CAPRI as a resource for reviewing patient demographic and clinical data.</td>
</tr>
<tr class="odd">
<td><strong>catastrophic edit</strong></td>
<td colspan="2">Changes that occur to two or more of the specified set of identity traits during an edit of a person's record.</td>
</tr>
<tr class="even">
<td><strong>CHDR</strong></td>
<td colspan="2">Clinical Data Repository (CDR) Health Data Repository</td>
</tr>
<tr class="odd">
<td><strong>Checksum</strong></td>
<td colspan="2">The result of a mathematical computation involving the individual characters of a routine or file.</td>
</tr>
<tr class="even">
<td><strong>Client</strong></td>
<td colspan="2">A single term used interchangeably to refer to the user, the workstation, and the portion of the program that runs on the workstation. In an object-oriented environment, a client is a member of a group that uses the services of an unrelated group. If the client is on a local area network (LAN), it can share resources with another computer (server).</td>
</tr>
<tr class="odd">
<td><strong>Clinical Patient Record System (CPRS)</strong></td>
<td colspan="2">Clinical Patient Record System provides a computer-based person record and organizes and presents all relevant data on a person in a way that directly supports clinical decision-making. CPRS integrates the extensive set of clinical and administrative applications available within VistA.</td>
</tr>
<tr class="even">
<td><strong>Common Menu</strong></td>
<td colspan="2">The Common menu consists of options that are available to all users. Entering two question marks at the menus select prompt displays any secondary menu options available to the signed-on user, along with the common options available to all users.</td>
</tr>
<tr class="odd">
<td><strong>Controlled Subscription Integration Agreement</strong></td>
<td colspan="2">This applies where the IA describes attributes/functions that must be controlled in their use. The decision to restrict the IA is based on the maturity of the custodian package. Typically, these IAs are created by the requesting package based on their independent examination of the custodian package's features. For the IA to be approved, the custodian grants permission to other VistA packages to use the attributes/functions of the IA; permission is granted on a one-by-one basis where each is based on a solicitation by the requesting package. An example is the extension of permission to allow a package (e.g., Spinal Cord Dysfunction) to define and update a component that is supported within the Health Summary package file structures.</td>
</tr>
<tr class="even">
<td><strong>Correlation</strong></td>
<td colspan="2">Comparison of person identity traits for multiple records with the Primary View in the ADR and/or MVI databases.</td>
</tr>
<tr class="odd">
<td><strong>COTS</strong></td>
<td colspan="2">Commercial Off The Shelf applications sold by vendors through public catalogue listings. COTS software is not intended to be customized or enhanced.</td>
</tr>
<tr class="even">
<td><strong>Cross Reference</strong></td>
<td colspan="2">There are several types of cross-references available. Most generally, a VA FileMan cross-reference specifies that some action be performed when the field's value is entered, changed, or deleted. For several types of cross-references, the action consists of putting the value into a list; an index used when looking-up an entry or when sorting. The regular cross-reference is used for sorting and for lookup; you can limit it to sorting only.</td>
</tr>
<tr class="odd">
<td><strong>Data Attribute</strong></td>
<td colspan="2">A characteristic unit of data such as length, value, or method of representation. VA FileMan field definitions specify data attributes.</td>
</tr>
<tr class="even">
<td><strong>Data Dictionary (DD)</strong></td>
<td colspan="2"><p>The Data Dictionary is a global containing a description of the kind of data that is stored in the global corresponding to a particular file. VA FileMan uses the data internally for interpreting and processing files.</p>
<p>It contains the definitions of a file's elements (fields or data attributes), relationships to other files, and structure or design. Users generally review the definitions of a file's elements or data attributes; programmers review the definitions of a file's internal structure.</p></td>
</tr>
<tr class="odd">
<td><strong>Data Dictionary Access</strong></td>
<td colspan="2">A user's authorization to write/update/edit the data definition for a computer file. Also known as DD Access.</td>
</tr>
<tr class="even">
<td><strong>Data Integrity</strong></td>
<td colspan="2">This term refers to the condition of patient records in terms of completeness and correctness. It also refers to the process in which a particular patient’s data is synchronized at all the sites in which that person receives care.</td>
</tr>
<tr class="odd">
<td><strong>Data Type</strong></td>
<td colspan="2">A specific field or type of information, such as Name, Social Security Number, etc.</td>
</tr>
<tr class="even">
<td><strong>Database</strong></td>
<td colspan="2">A set of data, consisting of at least one file, that is sufficient for a given purpose. The VistA database is composed of a number of VA FileMan files. A collection of data about a specific subject, such as the PATIENT file (#2); a data collection has different data fields (e.g. patient name, SSN, Date of Birth, and so on). An organized collection of data about a particular topic.</td>
</tr>
<tr class="odd">
<td><strong>Database Management System (DBMS)</strong></td>
<td colspan="2">A collection of software that handles the storage, retrieval, and updating of records in a database. A Database Management System (DBMS) controls redundancy of records and provides the security, integrity, and data independence of a database.</td>
</tr>
<tr class="even">
<td><strong>Date of Death</strong></td>
<td colspan="2">A person may be entered as deceased at a treating facility. If a shared patient is flagged as deceased, an RG CIRN DEMOGRAPHIC ISSUES bulletin is sent to each treating facility telling where, when, and by whom the deceased date was entered. Each site can then review whether the patient should be marked as deceased at their site.</td>
</tr>
<tr class="odd">
<td><strong>DBA</strong></td>
<td colspan="2">Database Administrator, oversees software development with respect to VistA Standards and Conventions (SAC) such as namespacing. Also, this term refers to the Database Administration function and staff.</td>
</tr>
<tr class="even">
<td><strong>DBIA</strong></td>
<td colspan="2">Database Integration Agreement (see Integration Agreements [IA]).</td>
</tr>
<tr class="odd">
<td><strong>Default</strong></td>
<td colspan="2">Response the computer considers the most probable answer to the prompt being given. It is identified by double slash marks (//) immediately following it. This allows you the option of accepting the default answer or entering your own answer. To accept the default you simply press the Enter (or Return) key. To change the default answer, type in your response.</td>
</tr>
<tr class="even">
<td><strong>Demographic Data</strong></td>
<td colspan="2">Identifying descriptive data about a person, such as: name, sex, date of birth, marital status, religious preference, SSN, address, etc.</td>
</tr>
<tr class="odd">
<td><strong>Demographics</strong></td>
<td colspan="2">Information about a person, such as name, address, service record, next of kin, and so on.</td>
</tr>
<tr class="even">
<td><strong>Department of Veterans Affairs</strong></td>
<td colspan="2">The Department of Veterans Affairs (formerly known as the Veterans Administration.)</td>
</tr>
<tr class="odd">
<td><strong>Device</strong></td>
<td colspan="2">Peripheral connected to the host computer, such as a printer, terminal, disk drive, modem, and other types of hardware and equipment associated with a computer. The host files of underlying operating systems may be treated like devices in that they may be written to (e.g., for spooling).</td>
</tr>
<tr class="even">
<td><strong>DFN</strong></td>
<td colspan="2">Data File Number. This is the patient <a href="http://vaww.vista.med.va.gov/iss/acronyms/i-acronyms.asp#ien">IEN</a> (.001 Field) in the PATIENT file (#2). Additionally, this is a defined variable in VistA that refers to the IEN of the patient currently in memory.</td>
</tr>
<tr class="odd">
<td><strong>DHCP</strong></td>
<td colspan="2">Decentralized Hospital Computer Program (now known as Veterans Health Information Systems and Technology Architecture [VistA]). VistA software, developed by VA, is used to support clinical and administrative functions at VA Medical Centers nationwide. It is written in M and, via the Kernel, runs on all major M implementations regardless of vendor. VistA is composed of packages that undergo a verification process to ensure conformity with namespacing and other VistA standards and conventions.</td>
</tr>
<tr class="even">
<td><strong>Dictionary</strong></td>
<td colspan="2">Database of specifications of data and information processing resources. VA FileMan's database of data dictionaries is stored in the FILE of files (#1).</td>
</tr>
<tr class="odd">
<td><strong>Direct Connect</strong></td>
<td colspan="2"><p>The Direct Connect is a real-time TCP/IP connection to the MPI to allow for an immediate request for an ICN. Direct Connect is activated when using any of the following PIMS options:</p>
<ul>
<li><p>Register A Patient,</p></li>
<li><p>Load/Edit Patient Data,</p></li>
<li><p>Electronic 10-10EZ Processing,</p></li>
</ul>
<p>and when using the:</p>
<ul>
<li><p>Display Only Query</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Direct Mode Utility</strong></td>
<td colspan="2">A programmer call that is made when working in direct programmer mode. A direct mode utility is entered at the MUMPS prompt (e.g., &gt;D ^XUP). Calls that are documented as direct mode utilities cannot be used in application software code.</td>
</tr>
<tr class="odd">
<td><strong>DNS</strong></td>
<td colspan="2">Domain Name Server</td>
</tr>
<tr class="even">
<td><strong>DOB</strong></td>
<td colspan="2">Date of Birth</td>
</tr>
<tr class="odd">
<td><strong>DOD</strong></td>
<td colspan="2">IdM– Date of Death</td>
</tr>
<tr class="even">
<td><strong>DoD</strong></td>
<td colspan="2">Department of Defense.</td>
</tr>
<tr class="odd">
<td><strong>Domain</strong></td>
<td colspan="2">A site for sending and receiving mail.</td>
</tr>
<tr class="even">
<td><strong>Double Quotes ("")</strong></td>
<td colspan="2">Symbol used in front of a Common option's menu text or synonym to select it from the Common menu. For example, the five-character string "TBOX" selects the User's Toolbox Common option.</td>
</tr>
<tr class="odd">
<td><strong>Duplicate Record Merge</strong></td>
<td colspan="2">Patient Merge is a VistA application that provides an automated method to eliminate duplicate patient records within the VistA database (i.e., the VistA PATIENT file [#2]).</td>
</tr>
<tr class="even">
<td><strong>DUZ</strong></td>
<td colspan="2">Locally defined variable in VistA that refers to the IEN of the logged on user (From the New Person file).</td>
</tr>
<tr class="odd">
<td><strong>DUZ(0)</strong></td>
<td colspan="2">Locally defined variable that holds the File Manager Access Code of the signed-on user.</td>
</tr>
<tr class="even">
<td><strong>Electronic Signature Code</strong></td>
<td colspan="2">Secret password that some users may need to establish in order to sign documents via the computer.</td>
</tr>
<tr class="odd">
<td><strong>Eligibility Codes</strong></td>
<td colspan="2">Codes representing the basis of a person's eligibility for care.</td>
</tr>
<tr class="even">
<td><strong>Encryption</strong></td>
<td colspan="2">Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases encryption algorithms are one directional, that is, they only encode and the resulting data cannot be unscrambled (e.g. access/verify codes).</td>
</tr>
<tr class="odd">
<td><strong>Entry</strong></td>
<td colspan="2">VA FileMan record. An internal entry number (IEN, the .001 field) uniquely identifies an entry in a file.</td>
</tr>
<tr class="even">
<td><strong>Error Trap</strong></td>
<td colspan="2">A mechanism to capture system errors and record facts about the computing context such as the local symbol table, last global reference, and routine in use. Operating systems provide tools such as the %ER utility. The Kernel provides a generic error trapping mechanism with use of the ^%ZTER global and ^XTER* routines. Errors can be trapped and, when possible, the user is returned to the menu system.</td>
</tr>
<tr class="odd">
<td><strong>ESR</strong></td>
<td colspan="2">Enrollment Systems Redesign is a centralized and reengineered Enrollment System.</td>
</tr>
<tr class="even">
<td><strong>Exception</strong></td>
<td colspan="2">A task that has encountered an error in personal data. Any Data Quality issue that requires detailed documentation. HC IdM finds an Exception based on business rules.</td>
</tr>
<tr class="odd">
<td><strong>Extrinsic Function</strong></td>
<td colspan="2">Extrinsic function is an expression that accepts parameters as input and returns a value as output that can be directly assigned.</td>
</tr>
<tr class="even">
<td><strong>Facility</strong></td>
<td colspan="2">Geographic location at which VA business is performed.</td>
</tr>
<tr class="odd">
<td><strong>FHIE</strong></td>
<td colspan="2"><p>Federal Health Information Exchange – A Federal IT health care initiative that facilitates the secure electronic one-way exchange of patient medical information between Government health organizations.</p>
<p>The project participants are the Department of Defense (DoD) and the Department of Veterans Affairs (VA). (<a href="http://vaww.va.gov/FHIE-BHIE/">BHIE Intranet Site</a><br />
> **NOTE:** This is an internal VA Web site and is not available to the public.)</p></td>
</tr>
<tr class="even">
<td><strong>Field</strong></td>
<td colspan="2">HL7: An HL7 field is a string of characters defined by one of the HL7 data types.<br />
<br />
VistA: In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file's data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.</td>
</tr>
<tr class="odd">
<td><strong>Field Components</strong></td>
<td colspan="2">A field entry may also have discernible parts or components. For example, the person's name is recorded as last name, first name, and middle initial, each of which is a distinct entity separated by a component delimiter (sub-subfield in ASTM e1238-94).</td>
</tr>
<tr class="even">
<td><strong>File</strong></td>
<td colspan="2">Set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.</td>
</tr>
<tr class="odd">
<td><strong>File Manager (VA FileMan)</strong></td>
<td colspan="2">VistA's Database Management System (DBMS). The central component of Kernel that defines the way standard VistA files are structured and manipulated.</td>
</tr>
<tr class="even">
<td><strong>FIN</strong></td>
<td colspan="2">Foreign ID Number</td>
</tr>
<tr class="odd">
<td><strong>FIPS</strong></td>
<td colspan="2">Standards published by the U.S. National Institute of Standards and Technology, after approval by the Department of Commerce; used as a guideline for federal procurements.</td>
</tr>
<tr class="even">
<td><strong>FOIA</strong></td>
<td colspan="2">Freedom of Information Act</td>
</tr>
<tr class="odd">
<td><strong>FORUM</strong></td>
<td colspan="2">The central E-mail system within VistA. Developers use FORUM to communicate at a national level about programming and other issues. FORUM is located at the OI Field Office—Washington, DC (162-2).</td>
</tr>
<tr class="even">
<td><strong>Free Text</strong></td>
<td colspan="2">A DATA TYPE that can contain any printable characters.</td>
</tr>
<tr class="odd">
<td><strong>FTP</strong></td>
<td colspan="2">File Transfer Protocol</td>
</tr>
<tr class="even">
<td><strong>Function Point Count (FPC)</strong></td>
<td colspan="2">The function point method is used to establish a meaningful unit-of-work measure and can be used to establish baseline costs and performance level monitors. Function point analysis centers on its ability to measure the size of any software deliverable in logical, user-oriented terms. Rather than counting lines of code, function point analysis measures the functionality being delivered to the end user.</td>
</tr>
<tr class="odd">
<td><strong>GAL</strong></td>
<td colspan="2">Global Address List.</td>
</tr>
<tr class="even">
<td><strong>Gender</strong></td>
<td colspan="2"><p>The following are listed in Legacy Vista as Standard Gender values:</p>
<ul>
<li><p>F – Female</p></li>
<li><p>M – Male</p></li>
</ul>
<p>SDS table Values:</p>
<ul>
<li><p>F – Female</p></li>
<li><p>M – Male</p></li>
<li><p>A – Ambiguous</p></li>
<li><p>N – Not Applicable</p></li>
<li><p>O - Other</p></li>
<li><p>U – Unknown</p></li>
<li><p>UN – Undifferentiated</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Global Variable</strong></td>
<td colspan="2">Variable that is stored on disk (M usage).</td>
</tr>
<tr class="even">
<td><strong>GUI</strong></td>
<td colspan="2">Graphical User Interface.</td>
</tr>
<tr class="odd">
<td><strong>HC IdM</strong></td>
<td colspan="2">Healthcare Identity Management</td>
</tr>
<tr class="even">
<td><strong>HDR</strong></td>
<td colspan="2">Health Data Repository – A repository of clinical information normally residing on one or more independent platforms for use by clinicians and other personnel in support of patient-centric care. The data is retrieved from heritage, transaction-oriented systems and is organized in a format to support clinical decision-making in support of patient care. Formerly known as Clinical Data Repository.</td>
</tr>
<tr class="odd">
<td><strong>Health Level 7 (HL7) Batch Protocol</strong></td>
<td colspan="2">Protocol utilized to transmit a batch of HL7 messages. The protocol generally uses FHS, BHS, BTS and FTS segments to delineate the batch. In the case of the MPI, the protocol only uses the BHS and BTS segments.</td>
</tr>
<tr class="even">
<td><strong>Health Level Seven (HL7)</strong></td>
<td colspan="2">National standard for electronic data exchange/messaging protocol. HL7 messages are the dominant standard for peer-to-peer exchange of clinical, text-based information.</td>
</tr>
<tr class="odd">
<td><strong>Health Level Seven (HL7) VistA</strong></td>
<td colspan="2">Messaging system developed as VistA software that follows the HL7 Standard for data exchange.</td>
</tr>
<tr class="even">
<td><strong>Healthcare Identity Management (HC IdM)</strong></td>
<td colspan="2"><p>The Healthcare Identity Management team (formerly the Identity Management Data Quality team)</p>
<ul>
<li><p>Serves as business steward for person identity data for the person's electronic health record (such as name, SSN, date of birth, gender, mother’s maiden name, place of birth) as well as managing the person's longitudinal health record across the enterprise.</p></li>
<li><p>Defines business rules and processes governing healthcare identity management data collection and maintenance.</p></li>
<li><p>Monitors and resolves data integrity issues and conflicts on the MVI and local systems related to the individual’s identity data within their health record, including the resolution of duplicates, mismatches and catastrophic edits to person identity, which affect person care and safety.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>HealtheVet-VistA</strong></td>
<td colspan="2">The next generation of VistA, HealtheVet-VistA, will retain all of the capabilities of legacy VistA but will provide enhanced flexibility for future health care and compliance with the One VA Enterprise Architecture. It will allow seamless data sharing between all parts of VA to benefit veterans and their families.</td>
</tr>
<tr class="even">
<td><strong>HEC</strong></td>
<td colspan="2">Health Eligibility Center.</td>
</tr>
<tr class="odd">
<td><strong>Help Frames</strong></td>
<td colspan="2">Entries in the HELP FRAME file (#9.2) that can be distributed with application packages to provide online documentation. Frames can be linked with other related frames to form a nested structure.</td>
</tr>
<tr class="even">
<td><strong>Help Prompt</strong></td>
<td colspan="2">The brief help that is available at the field level when entering one or more question marks.</td>
</tr>
<tr class="odd">
<td><strong>HINQ</strong></td>
<td colspan="2">Hospital Inquiry- The HINQ module provides the capability to request and obtain veteran eligibility data via the VA national telecommunications network. Individual or group requests are sent from a local computer to a remote Veterans Benefits Administration (VBA) computer where veteran information is stored. The VBA network that supports HINQ is composed of four computer systems located in regional VA payment centers.</td>
</tr>
<tr class="even">
<td><strong>HIPAA</strong></td>
<td colspan="2">Health Insurance Portability and Accountability Act – A law passed by Congress in 1996 that requires the Department of Health and Human Services to implement regulations that will require the use of specific standards related to health care claims, code sets, identifiers (individual, provider, employer, and health plan), and security. Protects the privacy of individually identifiable health information.</td>
</tr>
<tr class="odd">
<td><strong>HL7</strong></td>
<td colspan="2">Health Level 7 – National standard for electronic data exchange/messaging protocol. A standards organization primarily focused on message-oriented middleware for healthcare. HL7 messages are the dominant standard for peer-to-peer exchange of clinical, text-based information.</td>
</tr>
<tr class="even">
<td><strong>HLO</strong></td>
<td colspan="2">HL7 Optimized. VistA HL7 package routines.</td>
</tr>
<tr class="odd">
<td><strong>ICN</strong></td>
<td colspan="2">Persons are assigned a unique identifier, Integration Control Number (ICN), within the process of being added to the MVI database. This number links persons to their records across VHA systems. The Integration Control Number is a unique identifier assigned to patients when they are added to the MVI. The ICN follows the ASTM-E1714-95 standard for a universal health identifier.</td>
</tr>
<tr class="even">
<td><strong>ID State</strong></td>
<td colspan="2"><p>An attribute of the ICN, which describes the state of the record as Permanent, Temporary, or Deactivated. ID State is composed of the following two fields from the MPI VETERAN/CLIENT file (#985):</p>
<ul>
<li><p>ID STATE (#80) is a set of codes: PERMANENT, TEMPORARY, and DEACTIVATED. Auditing is enabled for this field.</p></li>
<li><p>DATE OF ID STATE (#81) identifies when the ID STATE field was last updated.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Identity Services</strong></td>
<td colspan="2">A business and data service that provides a consistent interface for access and maintenance of person identification to trusted client applications and services. It is the authoritative source for person identification in the Veterans Health Administration (VHA) domain.</td>
</tr>
<tr class="even">
<td><strong>IdM</strong></td>
<td colspan="2">Identity Management</td>
</tr>
<tr class="odd">
<td><strong>IdM Toolkit (IdM TK) Administrator</strong></td>
<td colspan="2">An IdM Toolkit Administrator is a user with additional privileges and security beyond the IdM Toolkit User's available functionality in the system.</td>
</tr>
<tr class="even">
<td><strong>IEN</strong></td>
<td colspan="2">Internal Entry Number. The IEN number and Station Number comprise the Source ID of the person targeted for the search. The Source ID is used to uniquely identify a person.</td>
</tr>
<tr class="odd">
<td><p><strong>IMDQ</strong></p>
<p><strong>New name: "Healthcare Identity Management (HC IdM)"</strong></p></td>
<td colspan="2">The Identity Management Data Quality team (renamed the Healthcare Identity Management team) is a group of Data Management Analysts committed to improving and safeguarding the quality and accessibility of person data throughout the VA enterprise. They are involved in many data quality initiatives, but their primary role is to assist VHA facilities in all matters related to the MVI.</td>
</tr>
<tr class="even">
<td><strong>Initiate Identity Hub™</strong></td>
<td colspan="2">The Initiate Identity Hub™ is a third-party proprietary off-the-shelf software package that makes use of a Probabilistic Matching Algorithm.</td>
</tr>
<tr class="odd">
<td><strong>Initiate Identity<br />
Hub</strong></td>
<td colspan="2">Initiate Systems Inc. software that provides a trusted on-demand system of record for multiple organizations or other entities by accurately identifying the relevant duplicate and fragmented records and linking them – within, as well as across, all data sources</td>
</tr>
<tr class="even">
<td><strong>Input Template</strong></td>
<td colspan="2">A pre-defined list of fields that together comprise an editing session.</td>
</tr>
<tr class="odd">
<td><strong>Institution</strong></td>
<td colspan="2">A Department of Veterans Affairs (VA) facility assigned a number by headquarters, as defined by Directive 97-058. An entry in the INSTITUTION file (#4) that represents the Veterans Health Administration (VHA).</td>
</tr>
<tr class="even">
<td><strong>Integration Agreements (IA)</strong></td>
<td colspan="2">Integration Agreements define agreements between two or more VistA software applications to allow access to one development domain by another. VistA software developers are allowed to use internal entry points (APIs) or other software-specific features that are not available to the general programming public. Any software developed for use in the VistA environment is required to adhere to this standard; as such, it applies to vendor products developed within the boundaries of DBA assigned development domains (e.g., MUMPS AudioFax). An IA defines the attributes and functions that specify access. The DBA maintains and records all IAs in the Integration Agreement database on FORUM. Content can be viewed using the DBA menu or the Health Systems Design &amp; Development's Web page.</td>
</tr>
<tr class="odd">
<td><strong>Integration Control Number (ICN)</strong></td>
<td colspan="2">Persons are assigned a unique identifier, known as an Integration Control Number (ICN), within the process of being added to the MVI database. This number links persons to their records across VHA systems. The Integration Control Number is a unique identifier assigned to persons when they are added to the MVI. The ICN follows the ASTM-E1714-95 standard for a universal health identifier.</td>
</tr>
<tr class="even">
<td><strong>Internal Entry Number (IEN)</strong></td>
<td colspan="2">The number used to identify an entry within a file. Every record has a unique internal entry number.</td>
</tr>
<tr class="odd">
<td><strong>IRM</strong></td>
<td colspan="2">Information Resource Management. A service at VA medical centers responsible for computer management and system security.</td>
</tr>
<tr class="even">
<td><strong>ISO</strong></td>
<td colspan="2">Information Security Officer.</td>
</tr>
<tr class="odd">
<td><strong>ISS</strong></td>
<td colspan="2">Infrastructure and Security Services (now known as Common Services Security Program).</td>
</tr>
<tr class="even">
<td><strong>IV&amp;V</strong></td>
<td colspan="2"><p>IV&amp;V is the principal activity that oversees the successful implementation and execution of all internal control processes for financial and interfacing systems.</p>
<p>In order to ensure overall systems integrity, IV&amp;V is accomplished organizationally independent from the elements that acquire, design, develop or maintain the system.</p></td>
</tr>
<tr class="odd">
<td><strong>KERNEL</strong></td>
<td colspan="2">VistA software that functions as an intermediary between the host operating system and other VistA software applications so that VistA software can coexist in a standard operating-system-independent computing environment. Kernel provides a standard and consistent user and programmer interface between software applications and the underlying M implementation.</td>
</tr>
<tr class="even">
<td><strong>LAN</strong></td>
<td colspan="2">Local Area Network.</td>
</tr>
<tr class="odd">
<td><strong>LAYGO Access</strong></td>
<td colspan="2">A user's authorization to create a new entry when editing a computer file. (Learn As You GO allows you the ability to create new file entries.)</td>
</tr>
<tr class="even">
<td><strong>LDAP</strong></td>
<td colspan="2">Lightweight Directory Access Protocol.</td>
</tr>
<tr class="odd">
<td><strong>Lookup</strong></td>
<td colspan="2">To find an entry in a file using a value for one of its fields.</td>
</tr>
<tr class="even">
<td><strong>M (ANSI Standard)</strong></td>
<td colspan="2">Massachusetts General Hospital Utility Multi-Programming System (M, formerly named MUMPS). The Mumps language originated in the mid-60's at the Massachusetts General Hospital. Although most implementations are proprietary, consolidated into the hands of a small number of companies, an open source version of the language has been developed which is distributed freely under the GNU GPL and LGPL licenses.</td>
</tr>
<tr class="odd">
<td><strong>Mail Message</strong></td>
<td colspan="2">An entry in the MESSAGE file (#3.9). The VistA electronic mail system (MailMan) supports local and remote networking of messages.</td>
</tr>
<tr class="even">
<td><strong>Mailman</strong></td>
<td colspan="2">VistA software that provides a mechanism for handling electronic communication, whether it's user-oriented mail messages, automatic firing of bulletins, or initiation of server-handled data transmissions.</td>
</tr>
<tr class="odd">
<td><strong>Manager Account</strong></td>
<td colspan="2">UCI that can be referenced by non-manager accounts such as production accounts. Like a library, the MGR UCI holds percent routines and globals (e.g., ^%ZOSF) for shared use by other UCIs.</td>
</tr>
<tr class="even">
<td><strong>Mandatory Field</strong></td>
<td colspan="2">Field that requires a value. A null response is not valid.</td>
</tr>
<tr class="odd">
<td><strong>Master Files</strong></td>
<td colspan="2">A set of common reference files used by one or more application systems. These common reference files need to be synchronized across the various applications at a given site. The Master Files Notification transactions provide a way of maintaining this synchronization.</td>
</tr>
<tr class="even">
<td><strong>Master Patient Index (Austin) or MPI Austin</strong></td>
<td colspan="2">The MPI is a separate computer system located at the Austin Information Technology Center. It maintains a record for VA patients and stores data such as a unique patient identifier and Treating Facility lists (which tracks the sites where that ICN is known).</td>
</tr>
<tr class="odd">
<td><strong>Master Patient Index or MPI</strong></td>
<td colspan="2">Master Patient Index is a cross-reference or index of patients that includes the patient’s related identifiers and other patient identifying information. It is used to associate a patient’s identifiers among multiple ID-assigning entities, possibly including a Health Data Repository, to support the consolidation and sharing of a patient’s health care information across VHA. The MPI is the authoritative source for patient identity.</td>
</tr>
<tr class="even">
<td><strong>Master Patient Index/Patient Demographics (MPI/PD) VistA or MPI/PD</strong></td>
<td colspan="2">Master Patient Index/Patient Demographics (MPI/PD) software initializes entries in the PATIENT file (#2) with the Master Patient Index, itself. The initialization process assigns an Integration Control Number (ICN), Coordinating Master of Record (CMOR), and creates a Treating Facility list of all sites at which the patient has received care. This information is then updated in the PATIENT file (#2) at all sites where the patient has been treated.</td>
</tr>
<tr class="odd">
<td><strong>Master Veteran Index or MVI</strong></td>
<td colspan="2">The authoritative source for person identity data. Maintains identity data for persons across VA systems. Provides a unique universal identifier for each person. Stores identity data as correlations for each system where a person is known. Provides a probabilistic matching algorithm. (Includes MPI, PSIM, and IdM TK) Maintains a “gold copy” known as a “Primary View” of the person’s identity data. Broadcasts identity trait updates to systems of interest. Maintains a record locator service.</td>
</tr>
<tr class="even">
<td><strong>Match Threshold</strong></td>
<td colspan="2">The Match Threshold is the level at which an Identity Profile must score against a set of identity traits in order to be considered a match. For most enterprise applications the Match Threshold would be set at or near the Auto Link Threshold. Internal Identity Management Systems (MPI/PSIM) may use a lower score, perhaps the Task Threshold, as a Match Threshold for identity management decision processes.</td>
</tr>
<tr class="odd">
<td><strong>Menu System</strong></td>
<td colspan="2">The overall Menu Manager logic as it functions within the Kernel framework.</td>
</tr>
<tr class="even">
<td><strong>Menu Text</strong></td>
<td colspan="2">The descriptive words that appear when a list of option choices is displayed. Specifically, the Menu Text field of the OPTION file (#19). For example, User's Toolbox is the menu text of the XUSERTOOLS option. The option's synonym is TBOX.</td>
</tr>
<tr class="odd">
<td><strong>Menu Text</strong></td>
<td colspan="2">The descriptive words that appear when a list of option choices is displayed. Specifically, the Menu Text field of the OPTION file (#19). For example, User's Toolbox is the menu text of the XUSERTOOLS option. The option's synonym is TBOX.</td>
</tr>
<tr class="even">
<td><strong>Message Segments</strong></td>
<td colspan="2">Each HL7 message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. A [ ] indicates the segment is optional, the { } indicates the segment is repeatable. For each message category, there will be a list of HL7 standard segments and/or "Z" segments used for the message.</td>
</tr>
<tr class="odd">
<td><strong>Mirror Testing</strong></td>
<td colspan="2">Functional testing in a non-production VistA system that is maintained by the VA Medical Center (VAMC) and is normally a mirror (snapshot copy) of their production system as of the date the copy was created. The resultant “mirror” account is normally isolated from external VA systems, is scrambled to protect PHI and PII, and is refreshed (recopied from production) on a periodic basis. Users can modify mirror account data without the changes being transmitted to external systems or affecting the site’s live production database. These qualities enable site testers to execute high-priority test scenario scripts provided by the development team and note the success or failure of each script.</td>
</tr>
<tr class="even">
<td><strong>MMN</strong></td>
<td colspan="2">Mother's Maiden Name: The family name under which the mother was born (i.e., before marriage). It is used to distinguish between patients with the same last name</td>
</tr>
<tr class="odd">
<td><strong>MPI Initialization</strong></td>
<td colspan="2">The process of initializing a site's PATIENT file (#2) with the Master Patient Index (MPI). Initialization synchronizes PATIENT file (#2) information (for active shared patients) with the MPI and identifies facilities where the patient has been treated. This process transfers the Integration Control Number (ICN), and Treating Facility list for each patient to the patient's record in the VistA PATIENT file (#2) at all sites where the patient has been treated. It is also possible to initialize an individual patient to the MPI. This is done through menu options. The initial synchronization of PATIENT file (#2) information (for active, shared patients) with the Master Patient Index and with the patient's treating facilities is an important step in the implementation of the MPI/PD software system.</td>
</tr>
<tr class="even">
<td><strong>Namespace</strong></td>
<td colspan="2">A convention for naming VistA package elements. The Database Administrator (DBA) assigns unique character strings for package developers to use in naming routines, options, and other package elements so that packages may coexist. The DBA also assigns a separate range of file numbers to each package.</td>
</tr>
<tr class="odd">
<td><strong>Namespacing</strong></td>
<td colspan="2">Convention for naming VistA software elements. The DBA assigns unique two to four character string prefix for software developers to use in naming routines, options, and other software elements so that software can coexist. The DBA also assigns a separate range of file numbers to each software application.</td>
</tr>
<tr class="even">
<td><strong>NDBI</strong></td>
<td colspan="2">National Database Integration</td>
</tr>
<tr class="odd">
<td><strong>Node</strong></td>
<td colspan="2">In a tree structure, a point at which subordinate items of data originate. An M array element is characterized by a name and a unique subscript. Thus the terms: node, array element, and subscripted variable are synonymous. In a global array, each node might have specific fields or "pieces" reserved for data attributes such as name.</td>
</tr>
<tr class="even">
<td><strong>NPI</strong></td>
<td colspan="2">National Provider Index</td>
</tr>
<tr class="odd">
<td><strong>Null</strong></td>
<td colspan="2">Empty—A field or variable that has no value associated with it is null.</td>
</tr>
<tr class="even">
<td><strong>Numeric Field</strong></td>
<td colspan="2">Response that is limited to a restricted number of digits. It can be dollar valued or a decimal figure of specified precision.</td>
</tr>
<tr class="odd">
<td><strong>OI</strong></td>
<td colspan="2">Office of Information</td>
</tr>
<tr class="even">
<td><strong>OI&amp;T</strong></td>
<td colspan="2">Office of Information Technology</td>
</tr>
<tr class="odd">
<td><strong>OIFO</strong></td>
<td colspan="2">Office of Information Field Office.</td>
</tr>
<tr class="even">
<td><strong>Option</strong></td>
<td colspan="2">An entry in the OPTION file (#19). As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. Options may also be scheduled to run in the background, non-interactively, by TaskMan.</td>
</tr>
<tr class="odd">
<td><strong>Option Name</strong></td>
<td colspan="2">Name field in the OPTION file (e.g., XUMAINT for the option that has the menu text "Menu Management"). Options are namespaced according to VistA conventions monitored by the DBA.</td>
</tr>
<tr class="even">
<td><strong>Package (Software)</strong></td>
<td colspan="2">The set of programs, files, documentation, help prompts, and installation procedures required for a given application (e.g., Laboratory, Pharmacy, and PIMS). A VistA software environment is composed of elements specified via the PACKAGE file (#9.4). Elements include files, associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, VistA software can be requested through the Freedom of Information Act (FOIA).</td>
</tr>
<tr class="odd">
<td><strong>Person Correlation</strong></td>
<td colspan="2">A profile of an Identity that is maintained by an Associated System and is correlated to only one ICN. (Source - PIDS)</td>
</tr>
<tr class="even">
<td><strong>Person Identification Service</strong></td>
<td colspan="2">The Person Identification Service (PIDS) is an OMG Interface Specification standard responsible for the identification, correlation, and search within and across a specified domain (A domain is a sphere of influence. For instance, a person has an identifier issued by the Social Security Administration [Social Security Number] which is different that their identifier issued by the State Department [Passport Number]. Both the Social Security Administration and State Department could be considered separate domains.) for identifiers based upon a provided set of search criteria traits. Essentially, this service provides for the assignment and reconciliation of multiple identifiers across domains and in supporting multiple implementation topologies. CORBA specification from OMG. (Source - PIDS)</td>
</tr>
<tr class="odd">
<td><strong>PIMS</strong></td>
<td colspan="2">Patient Information Management System- VistA software package that includes Registration and Scheduling packages.</td>
</tr>
<tr class="even">
<td><strong>PKI</strong></td>
<td colspan="2">Public Key Infrastructure</td>
</tr>
<tr class="odd">
<td><strong>POB (Country)</strong></td>
<td>PLACE OF BIRTH COUNTRY: If the person was not born in the USA, this is the country where the individual was born.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>POB (Province)</strong></td>
<td>PLACE OF BIRTH PROVINCE: The location within certain countries that contain additional divisions of where the individual was born.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>POB (City)</strong></td>
<td colspan="2">PLACE OF BIRTH CITY: The city in which this applicant was born (or foreign country if born outside the U.S.).</td>
</tr>
<tr class="even">
<td><strong>POB (State)</strong></td>
<td colspan="2">PLACE OF BIRTH STATE: State in which patient was born.</td>
</tr>
<tr class="odd">
<td><strong>Pointer</strong></td>
<td colspan="2">The address at which a data value is stored in computer memory. A relationship between two VA FileMan files, a pointer is a file entry that references another file (forward or backward). Pointers can be an efficient means for applications to access data by referring to the storage location at which the data exists.</td>
</tr>
<tr class="even">
<td><strong>Potential Match Threshold</strong></td>
<td colspan="2">The level at which an Identity Profile must score against a set of identity traits in order to be considered a Potential Match for HC IdM decision processes.</td>
</tr>
<tr class="odd">
<td><strong>Primary Key</strong></td>
<td colspan="2">A Data Base Management System construct, where one or more fields uniquely define a record (entry) in a file (table). The fields are required to be populated for every record on the file, and are unique, in combination, for every record on the file.</td>
</tr>
<tr class="even">
<td><strong>Primary Menu</strong></td>
<td colspan="2">The list of options presented at sign-on. Each user must have a primary menu in order to sign-on and reach Menu Manager. Users are given primary menus by Information Resource Management (IRM). This menu should include most of the computing activities the user needs.</td>
</tr>
<tr class="odd">
<td><strong>Primary Reviewer</strong></td>
<td colspan="2">This can be a single person or group of people given the overall responsibility to initiate reviews of potential duplicate record pairs. For example, selected personnel in Patient Administration or a task force or group formed to oversee and conduct the effort of reducing or eliminating the occurrence of duplicate records in the site's database.</td>
</tr>
<tr class="even">
<td><strong>Primary View</strong></td>
<td colspan="2">Provides the most accurate, current, and complete identity information for a VA patient. The Primary View from the MVI business rules make determinations about data additions and updates to identity traits (Name, SSN, Date of Birth, Gender, Mother's Maiden Name, Place of Birth, and Multiple Birth Indicator) based on the authoritativeness of the update or edits as they are received by the MVI.</td>
</tr>
<tr class="odd">
<td><strong>Private Integration Agreement</strong></td>
<td colspan="2">Where only a single application is granted permission to use an attribute/function of another VistA package. These IAs are granted for special cases, transitional problems between versions, and release coordination. A Private IA is also created by the requesting package based on their examination of the custodian package's features. Example: one package distributes a patch from another package to ensure smooth installation.</td>
</tr>
<tr class="even">
<td><strong>Probabilistic Comparison Score</strong></td>
<td colspan="2"><p>In a Probabilistic Search, these are the points assigned to an identity to indicate the level of confidence of matching to a given set of traits.</p>
<p>If the Comparison Score is above a certain level called the Match Threshold, then the profile is considered to be a match and the profile would be returned to the calling application.</p></td>
</tr>
<tr class="odd">
<td><strong>Probabilistic Matching Algorithm</strong></td>
<td colspan="2">A method to determine that a person identity profile has been matched in the PS Datastore based on the Comparison Score, which is calculated for each profile compared to the set of traits used for matching.</td>
</tr>
<tr class="even">
<td><strong>Probabilistic Search</strong></td>
<td colspan="2">A search using a matching algorithm to determine that a person's identity profile matches a set of defined traits. The algorithm assigns a comparison score and returns results based on a defined match threshold.</td>
</tr>
<tr class="odd">
<td><strong>Prompt</strong></td>
<td colspan="2">The computer interacts with the user by issuing questions called prompts, to which the user issues a response.</td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td colspan="2">Entry in the PROTOCOL file (#101). Used by the Order Entry/Results Reporting (OE/RR) package to support the ordering of medical tests and other activities.</td>
</tr>
<tr class="odd">
<td><strong>PS</strong></td>
<td colspan="2">Product Support</td>
</tr>
<tr class="even">
<td><strong>Pseudo SSN Reason</strong></td>
<td colspan="2">The reason that a pseudo SSN has been collected for the patient. The PSEUDO SSN REASON value is a set of codes pulled from the PATIENT (#2) file.</td>
</tr>
<tr class="odd">
<td><strong>Pseudo-SSNs</strong></td>
<td colspan="2">False Social Security Numbers that are calculated internally to VistA and cannot be mistaken for valid SSNs because they end in P.</td>
</tr>
<tr class="even">
<td><strong>PSIM</strong></td>
<td colspan="2">Person Service Identity Management (PSIM) enumerates and maintains person identities.</td>
</tr>
<tr class="odd">
<td><strong>Queuing</strong></td>
<td colspan="2">Requesting that a job be processed in the background rather than in the foreground within the current session. Jobs are processed sequentially (first-in, first-out). Kernel's TaskMan module handles the queuing of tasks.</td>
</tr>
<tr class="even">
<td><strong>Queuing Required</strong></td>
<td colspan="2">Option attribute that specifies that the option must be processed by Task Manager (the option can only be queued). The option may be invoked and the job prepared for processing, but the output can only be generated during the specified times.</td>
</tr>
<tr class="odd">
<td><strong>Receiving Site</strong></td>
<td colspan="2">Receiving Site- As it relates to HL7 Messages, it is the site that the message was sent to.</td>
</tr>
<tr class="even">
<td><strong>Record</strong></td>
<td colspan="2">Set of related data treated as a unit. An entry in a VA FileMan file constitutes a record. A collection of data items that refer to a specific entity (e.g., in a name-address-phone number file, each record would contain a collection of data relating to one person).</td>
</tr>
<tr class="odd">
<td><strong>REEME</strong></td>
<td colspan="2">Registration/Eligibility/Enrollment Maintenance and Enhancement</td>
</tr>
<tr class="even">
<td><strong>Registration Process</strong></td>
<td colspan="2"><p>During a registration, the person is checked against the entries in the Master Veteran Index (MVI) to determine if the person is already established or needs to be added. As of Patch DG*5.3*915 “Enterprise Search” replaced Register Once in the registration process to include Department of Defense (DoD) patients in an “extended” patient lookup if no patients are found on the MVI.</p>
<p>Within the Register a Patient [DG REGISTER PATIENT] option, the initial patient lookup search remains unchanged. That is, if a patient lookup performed in the site’s local VistA system returns one or more <em><u>existing</u></em> patients, the Registration user is asked to confirm the patient’s identity. However, if the patient is <em><u>not</u></em> found in the site’s local VistA system, the user is prompted to perform an “Enterprise Search,” which includes searching the DoD system if none found on the MVI. If the user chooses not to do an Enterprise Search, the software returns the user to the Select PATIENT prompt.</p>
<p>As of Patch DG*5.3*915, an Enterprise Search is required to add <em><u>new</u></em> patients to the local VistA system via the Register a Patient [DG REGISTER PATIENT] option.</p>
<p><strong>Using the Enterprise Search functionality:</strong></p>
<p>Upon choosing to do an Enterprise Search, the Registration user is presented with a series of prompts to enter the search criteria. If insufficient search criteria have been entered, the system displays a message requesting the user to enter the search criteria again. Sufficient search criteria entered automatically sends a query to the MVI to attempt to find possible matches. If matches <em><u>are not</u></em> found on the MVI, the query is automatically sent to the DoD system to find matches.</p>
<p>Patient matches that are found are returned grouped as an Auto Link or Potential Match for the registration staff to review. If a patient entry is selected, their data from the MVI (or DoD) is automatically loaded into the new patient's record. If that patient is already enrolled in the VA system, a query is sent to obtain the patient's Enrollment record prior to entering the registration screens. Then the registration process continues as normal.</p>
<p>Other possible results returned from an Enterprise Search:</p>
<ul>
<li><p>If too many matches are returned from the Enterprise Search, then the user is prompted to provide updated (more specific) search criteria to return a more limited search result list from which to select.</p></li>
<li><p>If no patients are found on the MVI or if the connection to the MVI is down, the user will be prompted to add the patient based upon the data previously entered.</p></li>
<li><p>If the matches returned are above the Auto Link threshold, then the user <em>must</em> select one of the patients returned from the query (Auto Link threshold or Potential Match threshold) or hold the security key, DG MVI ADD PT, to override the selection.</p></li>
<li><p>NOTE: Records that are returned from the Enterprise Search of the MVI or DoD systems are displayed in the closest match order based upon score.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Remote Procedure Call (RPC)</strong></td>
<td colspan="2">Remote Procedure Call is a protocol that one program can use to request a service from a program located on another computer network. Essentially M code may take optional parameters to do some work and then return either a single value or an array back to the client application.</td>
</tr>
<tr class="even">
<td><strong>Requesting Site</strong></td>
<td colspan="2">Requesting Site- As is relates to HL7 Messages, it is the site initiating a message to another site requesting some action be taken.</td>
</tr>
<tr class="odd">
<td><strong>Required Field</strong></td>
<td colspan="2">A mandatory field, one that must not be left blank. The prompt for such a field will be repeated until the user enters a valid response.</td>
</tr>
<tr class="even">
<td><strong>Resolution Journal Case Number</strong></td>
<td colspan="2">IDM – Number associated with each Resolution Journal Case. Used by the HealthCare Identity Management (HC IdM) team to document detailed information mostly for duplicate exception resolution but may also be used to denote details for resolving any type of exception.</td>
</tr>
<tr class="odd">
<td><strong>RG CIRN DEMOGRAPHIC ISSUES mail group</strong></td>
<td colspan="2"><p>The RG CIRN DEMOGRAPHIC ISSUES bulletin controls the sending of the following person related bulletin:</p>
<ul>
<li><p>Person Related Bulletin—REMOTE SENSITIVITY INDICATED</p></li>
<li><p>Cause—person is marked as sensitive at the sending site but not at receiving site.</p></li>
<li><p>Action to take—No action: message is informational</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Routine</strong></td>
<td colspan="2">Program or a sequence of instructions called by a program that may have some general or frequent use. M routines are groups of program lines, which are saved, loaded, and called as a single unit via a specific name.</td>
</tr>
<tr class="odd">
<td><strong>SAC</strong></td>
<td colspan="2">Standards and Conventions. Through a process of quality assurance, all VistA software is reviewed with respect to SAC guidelines as set forth by the Standards and Conventions Committee (SACC).</td>
</tr>
<tr class="even">
<td><strong>SACC</strong></td>
<td colspan="2">VistA's Standards and Conventions Committee. This Committee is responsible for maintaining the SAC.</td>
</tr>
<tr class="odd">
<td><strong>Scheduling Options</strong></td>
<td colspan="2">The technique of requesting that Task Manager run an option at a given time, perhaps with a given rescheduling frequency.</td>
</tr>
<tr class="even">
<td><strong>Screen Editor</strong></td>
<td colspan="2">VA FileMan's Screen-oriented text editor. It can be used to enter data into any WORD-PROCESSING field using full-screen editing instead of line-by-line editing.</td>
</tr>
<tr class="odd">
<td><strong>ScreenMan Forms</strong></td>
<td colspan="2">Screen-oriented display of fields, for editing or simply for reading. VA FileMan's Screen Manager is used to create forms that are stored in the FORM file (#.403) and exported with a software application. Forms are composed of blocks (stored in the BLOCK file [#.404]) and can be regular, full screen pages or smaller, "pop-up" pages.</td>
</tr>
<tr class="even">
<td><strong>Screen-Oriented</strong></td>
<td colspan="2">A computer interface in which you see many lines of data at a time and in which you can move your cursor around the display screen using screen navigation commands. Compare to Scrolling Mode.</td>
</tr>
<tr class="odd">
<td><strong>Security Key</strong></td>
<td colspan="2">The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="even">
<td><strong>Self Identified Gender</strong></td>
<td colspan="2"><p>The value of the Self Identified Gender field specifies the patient’s self-identified gender identity. This value will be displayed <em><u>only</u></em> if it is <em><u>not</u></em> null. The field displays as “SELF-IDENTIFIED GENDER IDENTITY.” This field is a SET of codes that specifies the patient's preferred gender:</p>
<ul>
<li><p>M = Male.</p></li>
<li><p>F = Female.</p></li>
<li><p>TM = Transmale/Transman/Female-to-Male.</p></li>
<li><p>TF = Transfemale/Transwoman/Male-to-Female.</p></li>
<li><p>O = Other.</p></li>
<li><p>N = individual chooses not to answer.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Sending Site</strong></td>
<td colspan="2">Sending Site—As it relates to HL7 Messages, it is the site that is transmitting the message to another site.</td>
</tr>
<tr class="even">
<td><strong>Sensitive Patient</strong></td>
<td colspan="2">Person whose record contains certain information, which may be deemed sensitive by a facility, such as political figures, employees, patients with a particular eligibility or medical condition. If a shared patient is flagged as sensitive at one of the treating sites, a bulletin is sent to the DG SENSITIVITY mail group at each subscribing site telling where, when, and by whom the flag was set. Each site can then review whether the circumstances meet the local criteria for sensitivity flagging.</td>
</tr>
<tr class="odd">
<td><strong>Server</strong></td>
<td colspan="2">The computer where the data and the Business Rules reside. It makes resources available to client workstations on the network. In VistA, it is an entry in the OPTION file (#19). An automated mail protocol that is activated by sending a message to a server at another location with the "S.server" syntax. A server's activity is specified in the OPTION file (#19) and can be the running of a routine or the placement of data into a file.</td>
</tr>
<tr class="even">
<td><strong>Set Of Codes</strong></td>
<td colspan="2">Usually a preset code with one or two characters. The computer may require capital letters as a response (e.g., M for male and F for female). If anything other than the acceptable code is entered, the computer rejects the response.</td>
</tr>
<tr class="odd">
<td><strong>Shared Patient</strong></td>
<td colspan="2">A person who has been seen at more than one VistA site. The MVI keeps the Treating Facility list updated every time a new facility is added. The MVI broadcasts out an updates to the treating facility list, including date last treated and event reason.</td>
</tr>
<tr class="even">
<td><strong>Site Manager/IRM Chief</strong></td>
<td colspan="2">At each site, the individual who is responsible for managing computer systems, installing and maintaining new modules, and serving as a liaison to the CIO Field Offices.</td>
</tr>
<tr class="odd">
<td><strong>Software (Package)</strong></td>
<td colspan="2">The set of programs, files, documentation, help prompts, and installation procedures required for a given application (e.g., Laboratory, Pharmacy, and PIMS). A VistA software environment is composed of elements specified via the PACKAGE file (#9.4). Elements include files, associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, VistA software can be requested through the Freedom of Information Act (FOIA).</td>
</tr>
<tr class="even">
<td><strong>Source ID</strong></td>
<td colspan="2"><p>A Source ID is a term used to describe the components that define a unique correlation. There are 4 components of a Source ID in MVI:</p>
<ol type="1">
<li><p>Assigning Authority (ex. USVHA)</p></li>
<li><p>Assigning Location (ex. Station #)</p></li>
<li><p>IDType (e.g. NI, PI, EI)</p></li>
<li><p>Internal Identifier - A code used at the assigning location used to uniquely identify a person.</p></li>
</ol>
<p>The Initiate Identity Hub also uses the term Source ID, but with a slightly different context. The Source ID in the IDHub is the unique identifier of a correlated system.. The fourth Source ID component, IEN, would translate to the Member ID in the ID HUB. Thus, the IDHub uses 2 components to uniquely identify a member: Source ID and Member ID.</p></td>
</tr>
<tr class="odd">
<td><strong>Spacebar Return</strong></td>
<td colspan="2">You can answer a VA FileMan prompt by pressing the spacebar and then the Return key. This indicates to VA FileMan that you would like the last response you were working on at that prompt recalled.</td>
</tr>
<tr class="even">
<td><strong>Special Queuing</strong></td>
<td colspan="2">Option attribute indicating that Task Manager should automatically run the option whenever the system reboots.</td>
</tr>
<tr class="odd">
<td><strong>SSA</strong></td>
<td colspan="2">Social Security Administration</td>
</tr>
<tr class="even">
<td><strong>SSDI</strong></td>
<td colspan="2">Social Security Death Index (SSDI). The SSDI is a database used for genealogical research as well as enabling users to locate a death certificate, find an obituary, and discover cemetery records and track down probate records. The Healthcare Identity Management (HC IdM) Team uses the SSDI (<a href="http://www.genealogybank.com/gbnk/ssdi/">Social Security Death Index Web site</a> ) as a resource for verifying patients’ dates of death.</td>
</tr>
<tr class="odd">
<td><strong>SSN</strong></td>
<td colspan="2">Social Security Number</td>
</tr>
<tr class="even">
<td><strong>SSN Verification Status</strong></td>
<td colspan="2"><p>Possible values of this field used on the MVI for the Enrollment System Redesign (ESR) correlation are:</p>
<ul>
<li><p>NEW RECORD</p></li>
<li><p>IN-PROCESS</p></li>
<li><p>INVALID PER SSA</p></li>
<li><p>RESEND TO SSA</p></li>
<li><p>VERIFIED</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Station Identifier</strong></td>
<td colspan="2">The number assigned to a VAMC facility or a System Association. The station identifier may be three characters in length designating the facility as a parent organization or up to six characters in length designating the facility as a child of a parent organization.</td>
</tr>
<tr class="even">
<td><strong>Subscriber</strong></td>
<td colspan="2">A subscriber is an entity, which receives updates to a patient's descriptive data from other sites. All treating facilities are also made subscribers as part of the MPI/PD processes.</td>
</tr>
<tr class="odd">
<td><strong>Subscript</strong></td>
<td colspan="2">A symbol that is associated with the name of a set to identify a particular subset or element. In M, a numeric or string value that: is enclosed in parentheses, is appended to the name of a local or global variable, and identifies a specific node within an array.</td>
</tr>
<tr class="even">
<td><strong>Supported Reference Integration Agreement</strong></td>
<td colspan="2">This applies where any VistA application may use the attributes/functions defined by the IA (these are also called "Public "). An example is an IA that describes a standard API such as DIE or VADPT. The package that creates/maintains the Supported Reference must ensure it is recorded as a Supported Reference in the IA database. There is no need for other VistA packages to request an IA to use these references; they are open to all by default.</td>
</tr>
<tr class="odd">
<td><strong>Synchronized Patient Data</strong></td>
<td colspan="2">Key descriptive fields in the PATIENT file (#2) that are updated in all the descriptive subscriber's PATIENT files whenever the fields are edited by a subscriber.</td>
</tr>
<tr class="even">
<td><strong>Systems of Interest</strong></td>
<td colspan="2">The term "systems of interest" refers to VA facilities that have seen patients and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a patient (e.g., Federal Health Information Exchange [FHIE], HomeTeleHealth, Person Service Identity Management [PSIM], Health Data Repository [HDR], etc.).</td>
</tr>
<tr class="odd">
<td><strong>Task Manager</strong></td>
<td colspan="2">Kernel module that schedules and processes background tasks (also called TaskMan)</td>
</tr>
<tr class="even">
<td><strong>Task Threshold or Threshold, Task</strong></td>
<td colspan="2"><p>The Task Threshold (also called the Clerical Review Threshold) is a value that is less than the Auto Link Threshold. A Comparison Score above the Task Threshold and below the Auto Link Threshold needs to be reviewed by an Identity Management expert to determine whether the Identity Profile is either a match or not a match for the traits being compared.</p>
<p>The Task Threshold is determined and tuned by Identity Management experts and may change over time as software systems and business processes improve. The ideal goal for automated identity matching is to minimize the difference between the Task Threshold and the Auto Link Threshold.</p></td>
</tr>
<tr class="odd">
<td><strong>TCP/IP</strong></td>
<td colspan="2">Transaction Control Protocol/Internet Protocol. A set of protocols for Layers 3 (Network) and 4 (Transfer) of the OSI network model. TCP/IP has been developed over a period of 15 years under the auspices of the Department of Defense. It is a de facto standard, particularly as higher-level layers over Ethernet. Although it builds upon the OSI model, TCP/IP is not OSI-compliant.</td>
</tr>
<tr class="even">
<td><strong>Template</strong></td>
<td colspan="2">Means of storing report formats, data entry formats, and sorted entry sequences. A template is a permanent place to store selected fields for use at a later time. Edit sequences are stored in the INPUT TEMPLATE file (#.402), print specifications are stored in the PRINT TEMPLATE file (#.4), and search or sort specifications are stored in the SORT TEMPLATE file (#.401).</td>
</tr>
<tr class="odd">
<td><strong>TIN</strong></td>
<td colspan="2">Temporary ID Number</td>
</tr>
<tr class="even">
<td><strong>Toolkit (IdM TK)</strong></td>
<td colspan="2">The User Interface for the HealthCare Identity Management team. The Toolkit provides functionality to allow HC IdM staff to search and view identity and exception information. This includes the ability to view the Primary View record and any associated correlations, correlation data, history, audit trails, and HC IdM Tasks captured by MVI. In addition, functionality is provided to support the re-hosting transition for a side-by-side comparison of ADR and MVI information.</td>
</tr>
<tr class="odd">
<td><strong>Treating Facility</strong></td>
<td colspan="2">Any facility (VAMC) where a person has applied for care, or has been added to the local PATIENT file (#2) (regardless of VISN) and has identified this person to the MVI will be placed in the TREATING FACILITY LIST file (#391.91).</td>
</tr>
<tr class="even">
<td><strong>Treating Facility List</strong></td>
<td colspan="2">Table of institutions at which the person has received care. This list is used to create subscriptions for the delivery of person clinical and demographic information between sites.</td>
</tr>
<tr class="odd">
<td><strong>Trigger</strong></td>
<td colspan="2">A type of VA FileMan cross-reference. Often used to update values in the database given certain conditions (as specified in the trigger logic). For example, whenever an entry is made in a file, a trigger could automatically enter the current date into another field holding the creation date.</td>
</tr>
<tr class="even">
<td><strong>Trigger Event</strong></td>
<td colspan="2">The event that initiates an exchange of messages is called a trigger event. The HL7 Standard is written from the assumption that an event in the real world of health care creates the need for data to flow among systems. The real-world event is called the trigger event. For example, the trigger event "a patient is admitted" may cause the need for data about that patient to be sent to a number of other systems. There is a one-to-many relationship between message types and trigger event codes. The same trigger event code may not be associated with more than one message type.</td>
</tr>
<tr class="odd">
<td><strong>TSPR</strong></td>
<td colspan="2">Technical Services Project Repository</td>
</tr>
<tr class="even">
<td><strong>UAT</strong></td>
<td colspan="2">User Acceptance Testing.</td>
</tr>
<tr class="odd">
<td><strong><u>U</u>nique <u>P</u>atient <u>I</u>dentifier (UPI)</strong></td>
<td colspan="2"><ul>
<li><p><strong>Outward Facing UPI (Social Security Number [SSN]):</strong> Requirements that apply to what the user sees (<u>outward facing</u>) should be what is currently stated in P&amp;LMS policy; currently still the Social Security Number (SSN).</p></li>
<li><p><strong>Inward Facing UPI (Integration Control Number [ICN]):</strong> Any requirements that refer to <u>inward facing</u> functions (internal clinical applications patient lookups) should use the Integration Control Number (ICN).</p></li>
<li><p><strong>Potential replacement for SSN as Outward Facing UPI (EDIPI):</strong> DoD EDIPI may eventually become the outward facing unique patient identifier (UPI), which is why the new VHIC 4.0 cards contain the EDIPI. However, there are some Veterans for whom the DoD has not provided EDIPI’s; therefore, VA has not announced the EDIPI as the official outward facing UPI and will not do so until VA and DoD have closed that gap to ensure all Veterans can be assigned the EDIPI.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>User Access</strong></td>
<td colspan="2"><p>This term is used to refer to a limited level of access, to a computer system, which is sufficient for using/operating a package, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any option, for example, can be locked with the key XUPROGMODE, which means that invoking that option requires programmer access.</p>
<p>The user's access level determines the degree of computer use and the types of computer programs available. The System Manager assigns the user an access level.</p></td>
</tr>
<tr class="odd">
<td><strong>VA</strong></td>
<td colspan="2">Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td><strong>VA Domiciliary</strong></td>
<td colspan="2">Provides comprehensive health and social services in a VA facility for eligible veterans who are ambulatory and do not require the level of care provided in nursing homes.</td>
</tr>
<tr class="odd">
<td><strong>VA FileMan</strong></td>
<td colspan="2">VistA's Database Management System (DBMS). The central component that defines the way standard VistA files are structured and manipulated.</td>
</tr>
<tr class="even">
<td><strong>VA Hospital</strong></td>
<td colspan="2">An institution that is owned, staffed and operated by VA and whose primary function is to provide inpatient services. NOTE: Each division of an integrated medical center is counted as a separate hospital.</td>
</tr>
<tr class="odd">
<td><strong>VA Medical Center (VAMC)</strong></td>
<td colspan="2"><p>A unique VA site of care providing two or more types of services that reside at a single physical site location. The services provided are the primary service as tracked in the VHA Site Tracking (VAST) (i.e., VA Hospital, Nursing Home, Domiciliary, independent outpatient clinic (IOC), hospital-based outpatient clinic (HBOC), and CBOC).</p>
<p>The definition of VA medical center does not include the Vet Centers as an identifying service. NOTE: This definition was established by the Under Secretary for Health.</p></td>
</tr>
<tr class="even">
<td><strong>VA Nursing Home Care Units (NHCU)</strong></td>
<td colspan="2">Provide care to individuals who are not in need of hospital care, but who require nursing care and related medical or psychosocial services in an institutional setting. VA NHCUs are facilities designed to care for patients who require a comprehensive care management system coordinated by an interdisciplinary team. Services provided include nursing, medical, rehabilitative, recreational, dietetic, psychosocial, pharmaceutical, radiological, laboratory, dental and spiritual.</td>
</tr>
<tr class="odd">
<td><strong>Variable</strong></td>
<td colspan="2">Character, or group of characters, that refer(s) to a value. M (previously referred to as MUMPS) recognizes 3 types of variables: local variables, global variables, and special variables. Local variables exist in a partition of main memory and disappear at sign-off. A global variable is stored on disk, potentially available to any user. Global variables usually exist as parts of global arrays. The term "global" may refer either to a global variable or a global array. A special variable is defined by systems operations (e.g., $TEST).</td>
</tr>
<tr class="even">
<td><strong>VBA SHARE</strong></td>
<td colspan="2">This is a VBA application which is utilized by the Regional Offices to access BIRLS, C&amp;P, PIF, PHF, Corporate Database, Social Security and COVERS records. The Healthcare Identity Management (HC IdM) Team uses VBA SHARE as a resource for verifying patient identity data as well as military information.</td>
</tr>
<tr class="odd">
<td><strong>Verify Code</strong></td>
<td colspan="2">The Kernel's Sign-on/Security system uses the Verify code to validate the user's identity. This is an additional security precaution used in conjunction with the Access code. Verify codes shall be at least eight characters in length and contain three of the following four kinds of characters: letters (lower- and uppercase), numbers, and, characters that are neither letters nor numbers (e.g., "#", "@" or "$"). If entered incorrectly, the system does not allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen.</td>
</tr>
<tr class="even">
<td><strong>Vet Center</strong></td>
<td colspan="2">A data source under the direct supervision of the Readjustment Counseling Service (RCS). The Vet Center provides professional readjustment counseling, community education, outreach to special populations, brokering of services with community agencies, and access to important links.</td>
</tr>
<tr class="odd">
<td><strong>VHA</strong></td>
<td colspan="2">Veterans Health Administration.</td>
</tr>
<tr class="even">
<td><strong>VIS</strong></td>
<td colspan="2">Veterans Information Solution (VIS). This intranet-based application is designed to provide a consolidated view of information about veterans and active service members. The HC IdM Team uses VIS as a resource for verifying patient identity data as well as military information.</td>
</tr>
<tr class="odd">
<td><strong>VISN</strong></td>
<td colspan="2">Veterans Integrated Service Network</td>
</tr>
<tr class="even">
<td><strong>VistA</strong></td>
<td colspan="2"><p>Veterans Health Information Systems and Technology Architecture (VistA) of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA). VistA software, developed by the VA, is used to support clinical and administrative functions at VHA sites nationwide. It is both roll-and-scroll- and GUI-based software that undergoes a quality assurance process to ensure conformity with namespacing and other VistA standards and conventions (see <a href="http://vaww.oed.portal.va.gov/communities/app_dev/sac/default.aspx">SAC</a>).</p>
<p>Server-side code is written in M, and, via Kernel, runs on all major M implementations regardless of vendor. Client-side code is written in Java or Borland Delphi and runs on the Microsoft operating system.</p></td>
</tr>
<tr class="odd">
<td><strong>VPID (replaced with ICN.)</strong></td>
<td colspan="2">Veterans Administration Personal Identifier – An enterprise-level identifier uniquely identifying VA „persons‟ across the entire VA domain.</td>
</tr>
<tr class="even">
<td><strong>WAN</strong></td>
<td colspan="2">Wide Area Network.</td>
</tr>
<tr class="odd">
<td><strong>Z segment</strong></td>
<td colspan="2">All message type and trigger event codes beginning with Z are reserved for locally defined messages. No such codes will be defined within the HL7 Standard.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-user-manual/063.png)</td>
<td><p><strong>REF:</strong> For a comprehensive list of commonly used terms and definitions, please visit the VA Web site:</p>
<blockquote>
<p><a href="http://vaww.oed.wss.va.gov/process/Lists/glossary/default.aspx">OI&amp;T Master Glossary Web site</a></p>
<p><em><strong>NOTE:</strong> This is an internal VA Web site and is not available to the public.</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix A: VHA DIRECTIVE 1906

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs VHA DIRECTIVE 1906

> Veterans Health Administration Transmittal Sheet

> Washington, DC 20420 April 29, 2013

> Data Quality Requirements for Healthcare Identity Management and Master Veteran Index Functions

> 1. REASON FOR ISSUE. This Veterans Health Administration (VHA) Directive establishes the business authority for the Healthcare Identity Management (HC IdM) Program and defines HC IdM enterprise and business requirements throughout the information systems lifecycle, including: the Master Veteran Index (MVI) and HC IdM operations at Department of Veterans Affairs (VA) health care facilities.

> 2. SUMMARY OF MAJOR CHANGES. This VHA Directive:

> a\. Changes the system title from Master Patient Index (MPI) to MVI and reflects establishment of MVI as an enterprise system.

> b\. Updates references to reflect involvement in activities such as the Nationwide Health Information Network and current versions of software systems and applications.

> c\. Updates guidance on entry and maintenance of data related to gender consistent with direction provided by Patient Care Services (see Att. A par.4).

> 3. RELATED ISSUES. VHA Handbook 1907.05.

> 4. RESPONSIBLE OFFICE. The Office of Informatics and Analytics (10P2) is responsible for the contents of this Handbook. Questions may be addressed at 202-554-3497.

> 5. RECISSIONS. VHA Directive 2006-036, Data Quality Requirements For Identity

> Management And Master Patient Index Functions, dated June 1, 2006, is rescinded.

> 6. RECERTIFICATION. This VHA Directive is scheduled for recertification on or before the last working day of May 2018.

> REDACTED

> Under Secretary for Health

> DISTRIBUTION: E-mailed to the VHA Publications Distribution List 4/30/2013

> T-1DATA QUALITY REQUIREMENTS FOR HEALTHCARE IDENTITY MANAGEMENT AND MASTER VETERAN INDEX FUNCTIONS

> 1. PURPOSE: This Veterans Health Administration (VHA) Directive establishes the business authority for the Healthcare Identity Management (HC IdM) Program and defines HC IdM enterprise and business requirements throughout the information systems lifecycle, including: the Master Veteran Index (MVI) and HC IdM operations at Department of Veterans Affairs (VA) health care facilities. The MVI is the authoritative identity service within VA maintaining and synchronizing identities for VA clients, Veterans, and beneficiaries (see subpar. 5g).

> AUTHORITY: Title 38 United States Code (U.S.C.) 7301(b).

> 2. BACKGROUND

> a\. In fiscal year (FY) 2000, VHA established a HC IdM Program, now within the Office of Informatics and Analytics, Health Information Governance, Data Quality Program, as the national business owner and data steward for MVI and the services and activities needed to maintain and ensure the integrity of a patient or beneficiary’s longitudinal health record and unique person identity for health care. The MVI and the activities performed by HC IdM are based on national standards (e.g., American Society for Testing and Materials (ASTM)) and link all records about one patient in multiple VHA, VA, Department of Defense (DOD) and other external systems to provide that patient/beneficiary's complete electronic health record (see subpars. 5h and 5i). This ability is essential to seamless care coordination and data sharing and interoperability with health care partners such as DOD, VA lines of business such as the Veterans Benefits Administration (VBA) and National Cemetery Administration (NCA), and any other outside agency/companies. HC IdM information and functionality resident in the MVI are on the critical path for all patient, Veteran, and beneficiary-centered clinical and administrative information technology (IT) applications.

> b\. The MVI contains an entry and unique identifier for all patients who have had an active record in any Veterans Health Information Systems and Technology Architecture (VistA) PATIENT file (#2) since 1996. Today the MVI provides the capability to link a patient’s records through matching of traits such as name, social security number (SSN), date of birth (DOB), gender, address, etc., from multiple VA health care facilities’ national databases and other VA systems that support health care, such as MyHealth*e*Vet (MHV). In FY 2013-2014, VA is expanding this capability to all of VA’s systems legacy and new systems as part of the Veterans Relationship Management (VRM) Major Initiative supported by a mandate from the Assistant Secretary of the Office of Information Technology (OI&T).

> c\. Current HC IdM Program activities include: establishing business policy and rules; overseeing core identity management product implementation; and monitoring, identifying, and resolving record and identity integrity issues and conflicts in the MVI, VA systems such as MHV and local VA health care facilities related to identity data. This includes the resolution of duplicate records, mismatches, and overwrites (catastrophic edits) of patient identity that affect patient care and safety. In FY 2013-2014, the program activities are expanding to other VA lines of business which include the implementation, monitoring, identification and resolution of identity integrity issues and conflicts on the MVI with line-of-business systems.

> d\. Clinical, administrative, billing, and intra-departmental processes within VA, such as eligibility data sharing between VBA and VHA and with external partners, depend on accurate patient health care information and identity management and have implications to patient safety and the provision of health care. In order to ensure that individuals are correctly identified by VA staff during patient selection and entry and to prevent catastrophic edits to identity, extreme care must be exercised when entering and editing identity information. The HC IdM Program supports field efforts relating to the data entry into the patient health record with a team of

> highly-skilled specialists who understand VHA’s health care records and can guide the resolution of duplicate entries, overlaps, overwrites, and other mis-identification of patient identity data that could impact patient care and safety.

> e\. HC IdM is dependent on the correct identification of unique individuals, but it is distinct from Security, and Identity and Access Management (IAM), which involves managing persons seeking access to VA resources based on national security standards (Homeland Security Presidential Directive 12 (HSPD12), Federal Information Security Management Act (FISMA), National Institute of Standards and Technology (NIST), etc. (e.g., authentication, authorization, and access control).

> f\. Definitions

> \(1\) Catastrophic Edit. A Catastrophic Edit means changes have been made to a patient’s electronic health record in a local VistA system that result in the record being changed inappropriately to that of another patient, caused by, but not limited to, edits to patient identity data (such as name, SSN, date of birth, gender) and/or erroneous merging of two or more distinct patient records into a single record within VistA.

> \(a\) These errors can occur as a result of improper due diligence by staff using the Duplicate Record Merge software when two potential duplicate patient records are not properly reviewed and screened. This results in two different patient entries being merged into one.

> \(b\) All types of errors affect the longitudinal patient entry (record) at other facilities that have treated the patient and they specifically affect patient care. These errors are considered a significant patient safety risk.

> \(2\) Enumeration. Enumeration is an assignment of a universal health identifier by the authoritative identity management service to an individual. For VA, this service is provided by the MVI and the identifier is known as the Integration Control Number (ICN) (see subpar. 2f(4)).

> \(3\) Healthcare Identity Management (HC IdM). HC IdM is comprised of the set of business processes and a supporting infrastructure for the creation, maintenance, and use of digital identities within a legal and policy context.

> \(a\) The HC IdM Program is the national business owner or steward for patient identity data within VHA.

> \(b\) The HC IdM Team ensures the integrity of patient identity data within the MVI and the associations to the systems that contain electronic health record information about the patient, which provides the longitudinal health record.

> \(4\) Integration Control Number (ICN). ICN is VA’s enterprise unique person identifier which is based on the conformance standard from ASTM E 1714-00, assigned and maintained by the MVI to each unique patient within the VHA systems and provides the key to linking the patient electronic health record across the enterprise.

> \(5\) Master Veteran Index (MVI). MVI is the authoritative identity service within VA, establishing, maintaining and synchronizing identities for VA clients, Veterans and beneficiaries. The MVI correlates a patient's identity across the enterprise, including all VistA systems and external systems, such as DOD, and the NwHIN. Legacy systems from other VA administrations, e.g., National Cemetery Administration’s (NCA) Burial Operations Support System (BOSS) and Automated Memorial Application System (AMAS) and VBA’s Corporate Database are being integrated with the MVI. The MVI includes authoritative sources for health identity data and contains over 18 million patient entries populated from all VHA facilities nationwide. The MVI facilitates the sharing of health information, resulting in coordinated and integrated health care for Veterans by providing the access point mechanism for linking patient's information to enable an enterprise-wide view of patient information; it uniquely identifies all active patients who have been admitted, treated, or registered in any VHA facility, and assigns a unique identifier to the patient.

> \(6\) Primary View. A Primary View is the VA enterprise profile of an identity indicated by an ICN. An identity is represented by one ICN, and each ICN has one Primary View Profile. The Primary View Profile provides the most authoritative identity traits known about a person’s identity within VA. The Primary View Profile is referenced in VA information systems by an associated ICN.

> 3. POLICY: It is VHA policy that information systems and databases, including the MVI, maintain accurate and complete person-identifying information, and that vital processes related to resolving identity data quality issues be performed.

> 4. RESPONSIBILITIES

> a\. Chief, Office of Informatics and Analytics, Health Information Governance, Data Quality, HC IdM Program, VHA Central Office. The Chief, Office of Informatics and Analytics, Health Information Governance, Data Quality, HC IdM Program, VHA Central Office is responsible for:

> \(1\) Serving as the business owner and data steward to ensure that the correct patient or beneficiary longitudinal, electronic health record is available.

> \(2\) Managing the integrity of health care identities required to provide health care services, treatment and health care operations.

> \(3\) Serving as the business function owner and steward for HC IdM systems such as the MVI and other related HC IdM efforts and/or other applications that require Identity Management (IdM) functionality.

> \(4\) Providing the authoritative business input about and monitoring compliance with HC IdM functions, requirements and policy on behalf of VA to ensure that HC IdM business requirements are provided, understood and addressed within VA information technical efforts throughout product lifecycles.

> \(5\) Promoting HC IdM best practices and developing and disseminating information and training to improve the understanding of HC IdM and related systems.

> \(6\) Resolving patient and other non-patient (e.g., provider) identity issues (e.g., duplicates, mismatches, patient catastrophic edits), working with local facility staff to maintain the integrity of the longitudinal record and ensure that policies and procedures are followed.

> \(7\) Participating in the development of national HC IdM standards.

> \(8\) Ensuring VA information systems adhere to health care identity management requirements as documented in the Identity Management Business Requirements Guidance located on the Data Quality (DQ) homepage: [Data Quality Program Web site](http://vaww.vhadataquality.va.gov/).  
> *NOTE: This is an internal VA Web site and is not available to the public.*

> b\. Facility Director. Each Facility Director is responsible for:

> \(1\) Ensuring that the entry of person identity data into VA applications is accurate and complete.

> \(2\) Ensuring that local duplicate patient records are reviewed and merged in VistA using the Duplicate Record Merge software in an accurate and timely manner.

> \(3\) Designating individuals as points-of-contact (POCs) responsible for processing MVI and Patient Demographic (PD) Exceptions, resolving ICN issues on a daily basis, as well as merging local duplicate patient records and resolving any other data quality issues brought to their attention by the national HC IdM Program staff.

> \(4\) Ensuring that personnel are assigned to resolve, in a timely manner, issues with exceptions, data quality, communication links, infrastructure, and applications that support data communications. This includes assigning staff members to the following roles (including alternates for each of these categories):

> \(a\) Administrative POC, and a Health Information Management (HIM) staff member;

> \(b\) OIT POC; and

> \(c\) Health Level 7 (HL7) POC.

> *NOTE: POC information for Master Veteran Index/Patient Demographics (MVI/PD) is updated using the Add/Edit Point-of-Contact \[RG UPDATE POINT OF CONTACT\] option on the MPI/PD Patient Admin Coordinator Menu \[RG ADMIN COORD MENU\]. A current listing of facility MVI POCs can be found on the Data Quality Web*

> *site:* REDACTED

> \(5\) Ensuring that national HC IdM staff are apprised of staffing changes.

> \(6\) Ensuring that management and staff are made aware of policies and procedures related to catastrophic edits to patient identity. This includes ensuring that all staff members with the ability to enter, edit, and merge patient identity data (such as name, date of birth, SSN and gender) specifically, those individuals who have been given the privilege of being assigned the VistA “DG REGISTER PATIENT,” “DG LOAD EDIT” key or a local equivalent, are required to complete and document the required training module “Preventing Catastrophic Edits to Patient Identity.” *NOTE: The required training, "Preventing Catastrophic Edits to Patient Identity,” can be found at VA Learning University Talent Management System (TMS) under Item Number: VA 7861,* [<u>REDACTED</u>](http://www.tms.va.gov/). This training is required <u>prior</u> to the assignment of the key to these individuals.

> \(7\) Ensuring that the appropriate supervisors are responsible for ensuring this training is successfully completed and documented by the employee, as this is a key competency for patient selection. Any individual who does not demonstrate competency of this skill must re-take the training until core competency is established. Any individual who mis-selects a patient record and generates a catastrophic edit to a patient record must re-take the training and provide evidence of successful completion to the individual’s supervisor and the HC IdM Team.

> \(8\) Ensuring that supervisors monitor employee work quality and ensure that employees achieve and maintain core competency of this skill; failure to achieve competency can lead to patient safety issues.

> \(9\) Ensuring the VistA DG CATASTROPHIC EDIT security key is assigned to the responsible Chief Business Office (CBO) Program Application Specialist (PAS) or Automated Data Processing Application Coordinator (ADPAC), their alternates, and supervisor, so they are recipients of the “Potential Catastrophic Edit of Patient Identifying Data” alerts. Designated staff reviews these alerts on a daily basis to ensure that catastrophic edits are reported and resolved and that any issues with staff performing catastrophic edits are addressed.

> \(10\) Ensuring the VistA DG SUPERVISOR security key is assigned and a daily review of the Report – Patient Catastrophic Edits option is conducted and all potential catastrophic edits listed on the report have been reviewed, and resolved in a timely and accurate manner (see VHA Handbook 1907.05 for detailed procedures and timelines in correcting health and demographic information within the electronic health record and other electronic databases when health or administrative data are erroneously associated with a patient as a result of a catastrophic edit to patient identity).

> \(11\) Ensuring that all facility staff involved in the editing or alteration of the electronic health record exercise care and caution when making changes to identity traits of patients and report any suspected catastrophic edits to the designated facility MVI POC.

> \(12\) Ensuring that staff directly involved with identity data entry into information systems are aware of the guidelines contained within this Directive and are aware of their responsibility for entering complete identity data elements in a consistent and accurate format. This also includes staff at facilities with outpatient clinics and community-based outpatient clinics assigned to their jurisdiction.

> \(13\) Ensuring that each supervisor involved in the activities of entering demographic data follows the guidance on data quality of the non-identity elements provided by the VHA CBO.

> \(14\) Ensuring that staff members responsible for data entry of administrative and demographic information are informed of these requirements mandated by the CBO. *NOTE: Links to up-to-date guidance on data quality are posted on the HC IdM team’s Web site*: [<u>REDACTED</u>](https://www.tms.va.gov/learning/user/login.jsp)

> \(15\) Ensuring that the audit trail of the PATIENT File (#2) for all electronic health records is maintained and <u>never</u> purged as this is critical in the identification and resolution of catastrophic edits to patient identity and other identity integrity issues.

> c\. Facility MVI POC. Each facility MVI POC, who is considered to be the liaison between the facility and HC IdM, is responsible for:

> \(1\) Working with their counterparts and national HC IdM staff in correcting anomalies and addressing issues related to identity data for shared patients.

> \(2\) Processing MVI-PD Exceptions, data quality and other ICN issues in VistA and merging local duplicate patient records, to ensure accuracy and completeness of identity data.

> \(3\) Taking appropriate action to resolve exceptions, data quality and other ICN issues in VistA, and merge local duplicate patient records within <u>5 business days</u>. *NOTE: Specific information regarding these processes can be found in Attachment A of this Directive.*

> \(4\) Responding to requests from HC IdM staff to resolve catastrophic edits that overwrite the original patient entry with another patient. These must be completed within <u>1 business day</u>.

> \(5\) Using electronic mail (i.e., Outlook) to facilitate communications.

> \(6\) Obtaining and maintaining Public Key Infrastructure (PKI) encryption certificates that must be utilized when transmitting and receiving patient identifiable information.

> \(7\) Ensuring that facility contact information maintained by the HC IdM team is current.

> \(8\) Obtaining the necessary VistA access to verify information.

> \(9\) Making appropriate changes to patient data in the respective facility’s VistA system and perform POC functions, such as processing MVI-PD Exception Handling, data quality, and ICN issues.

> d\. Facility OIT and HL7 POCs. Facility OIT and HL7 POCs are responsible for:

> \(1\) Working with their counterparts and OIT Product Development (PD) Product Support (PS) staff to maintain communication links, infrastructure, and applications supporting data communications. Responses to inquiries and requests for assistance must be addressed within <u>1</u> <u>business day</u>;

> \(2\) Ensuring that the audit trail of the PATIENT File(#2) for all electronic health records is maintained and <u>never</u> purged as this is critical in the identification and resolution of catastrophic edits to patient identity and other identity integrity issues; and

> \(3\) Facilitating the resolution of any catastrophic edits to patient identity, which must be completed within the timelines designated in VHA Handbook 1907.05, Repair of Catastrophic Edits to Patient Identity.

> 5. REFERENCES

> a\. VHA Handbook 1601A.02, Eligibility Determination.

> b\. VHA Handbook 1601A.01, Intake Registration.

> c\. VALU TMS Item Number 7861 Preventing Catastrophic Edits to Patient Identity.

> d\. VHA Handbook 1907.05, Repair of Catastrophic Edits to Patient Identity.

> e\. VHA Handbook 1605.1, Privacy and Release of Information.

> f\. Identity Management Business Requirements Guidance, Version 2.5, October 2012 REDACTED

> g\. VA Identity Management Policy Memorandum.

> h\. ASTM. Standard Guide for the Properties of a Universal Healthcare Identifier. E1714-00; E31 reference: [ASTM International Web site](http://www.astm.org/)

> i\. Object Management Group (OMG) Person Identification Service (PIDS) Specification

> Version 1.1, April 2001, [<u>http://www.omg.org/spec/PIDS/1.1/PDF</u>.](http://www.omg.org/spec/PIDS/1.1/PDF)

APPENDIX A

> PROCEDURES FOR DATA ENTRY AND MAINTENANCE RELATED TO HEALTH CARE IDENTITY MANAGEMENT

> It is imperative that staff take the utmost care when entering identity data for patients and other persons. Incomplete or inaccurate data (including typographical errors) are the leading cause of duplicate entries in the Master Veteran Index (MVI) and the failure to link records via the Integration Control Number (ICN). The following guidelines are intended to increase the accuracy and completeness of the essential identity data traits and to clarify practices that need to be followed when data are not available or duplicate entries exist. These guidelines emphasize the intended use of some identity fields within Veterans Health Information Systems and Technology Architecture (VistA). It is important that identity data for patients be reviewed for accuracy and completeness and updated, as necessary, each and every time contact is made with the individual.

> 1. NAME: The NAME field is an important element in the unique identity of a person. Sites need to ensure that the name entered is the complete legal name, and includes a full middle name, when available. Nicknames or ambiguous information are not to be used. Additional guidance for the entry of the name field includes the following procedures:

> a\. All data must be entered using uppercase letters. b. No parenthesis may be used.

> c\. Commas, apostrophes, and hyphens are the only punctuation that may be used.

> d\. Enter full middle names. Do not use only an initial unless an initial is the person’s given middle name. No punctuation will be used if the middle name is only an initial. The middle name will be left blank if one does not exist; NMI (no middle initial) or NMN (no middle name) will not be used.

> e\. Multiple last name components must be separated by spaces. Individuals with hyphenated names are to be entered with the hyphen included.

> f\. When entering a full name, it must contain a comma (i.e., LAST NAME, FIRST NAME). Individuals with a legal name as a single value must be entered with the name followed by a comma.

> g\. Suffixes must be used for junior (JR), senior (SR) and birth positions. Numeric birth position identifiers must be entered in Roman numeral values (i.e., I, II, III, etc.). Suffixes must be entered without punctuation.

> h\. If entering a Prefix, (such as MR, MRS, MS, and MISS), no punctuation must be used.

> i\. The Degree field may be used to denote the degree or profession (such as MD for Doctor of Medicine, PHD for Doctor of Philosophy, REV for Reverend), and must be entered without punctuation.

> j\. Legal Spanish names must be entered with the father’s last name first, a hyphen and then the mother’s maiden name all in the LAST NAME field.

> k\. Alias names must be entered in the ALIAS NAME field for any previously used names (including maiden names). An entry in this field is automatically cross-referenced and the record can be accessed using the alias name.

> l\. To enter another patient record with the same name as an existing person in the file on VistA, use quotes when entering the full name and a new entry will be created (i.e., “LASTNAME,FIRSTNAME MIDDLE”).

> m\. TEST patient records must be designated by the last name being prefixed by ZZ (i.e. ZZLASTNAME, FIRSTNAME MIDDLE).

> n\. A legal name change requires a written request and supporting documentation from the Veteran. Requests to change static administrative data are considered to be a Privacy Act amendment requests and may be made only by the Veteran or by a personal representative of the Veteran as defined in Veterans Health Administration (VHA) Handbook 1605.1. Official supporting documentation for a name change are the following: letter from the Social Security Administration (SSA) stating that all required documentation has been received and they will be issuing the requestor a new SSA card, a State Driver’s License (based on new regulations enforced by the Department of Transportation whereby a name will not be changed until SSA provides the preceding letter or the new SSA card), new SSA card reflecting the name change, an official name change court order, amended birth certificate or passport. Marriage licenses or certificates are no longer sufficient stand-alone documents for a name change, as not all who apply for a marriage license or marry actually change their name. The Privacy Officer must review all documentation supplied by the Veteran to ensure it meets the criteria and to transmit this information to the MVI POC.

> 2. SOCIAL SECURITY NUMBER (SSN): Enter the patient’s official SSN issued by the SSA. No other value will be entered into this field. If a valid SSN is not known, then a "P" must be entered into the field for the calculation of a pseudo SSN. SSNs are not to be created and no other numbers may be entered in this field, including prison-issued numbers or Canadian SSNs. SSNs beginning with five leading zeros are considered TEST patients and are not be used for any other purpose.

> 3. MOTHER’S MAIDEN NAME: Enter the last name only of individual’s mother at the time of her birth. Leave blank if unknown or not provided. Values such as “deceased,” “unknown,” and other inappropriate responses are not to be used.

> 4. GENDER (ADMINISTRATIVE)

> a\. Male or Female must be entered. In case of gender reassignment, a written request and supporting documentation are required from the Veteran and is considered to be a Privacy Act amendment request. One of the following is required as supporting documentation: legal documentation (i.e., amended birth certificate or court order), passport or a signed original statement on office letterhead, from a licensed physician. Sexual reassignment surgery is not a prerequisite for amendment of gender.

> b\. The licensed physician’s statement must include <u>all</u> of the following information:

> \(1\) Physician’s full name.

> \(2\) Medical license or certificate number.

> \(3\) Issuing state of medical license/certificate.

> \(4\) Drug Enforcement Administration (DEA) registration number assigned to the physician or comparable foreign designation, if applicable.

> \(5\) Address and telephone number of the physician.

> \(6\) Language stating that the physician has treated the patient or reviewed and evaluated the medical history of the applicant. Also, the physician has a doctor-patient relationship with the applicant which is evident in having one or more clinical encounters between doctor and patient.

> \(7\) Language stating that the patient has had appropriate clinical treatment for gender transition to the new gender (specifying male or female).

> \(8\) Language stating “I declare under penalty of perjury under the laws of the United States that the foregoing is true and correct.”

> 5. DATE OF BIRTH (DOB): Day, Month, and Year of Birth must be entered, whenever available. Imprecise (month/year or year only) can be entered, but only if the full DOB is not available. If DOB is unknown 1/1/1910 must be entered.

> 6. PLACE OF BIRTH \[CITY\]: Enter the birth city only. For persons born outside of the

> United States, enter the city, province, or other designated area.

> 7. PLACE OF BIRTH \[STATE\]: Enter the birth state only. For persons born outside the

> United States, choose FOREIGN COUNTRY from the list of state options.

> 8. PLACE OF BIRTH \[COUNTRY\] (not yet available): Enter the birth country only (future implementation in VistA). The default country must be the UNITED STATES.

> 9. MULTIPLE BIRTH INDICATOR (Patients only): Enter YES in the Multiple Birth Indicator field <u>only</u> if the patient is part of a multiple birth (i.e., is a twin, triplet, etc.). This field assists in the unique identification of patients who are part of a multiple birth and may have identity traits similar to other patient entries. Leave blank if unknown or not provided.

> 10. DATES OF DEATH: Death certificates are generally required to enter a Date of Death. Dates of Death must not be entered from newspaper obituaries, phone calls, or other unofficial sources. Information from these sources may be used as a mechanism to further research the death information. However, they must not be entered unless they have been verified by an official source. Medical facilities are required to use the following as authoritative sources in order of precedence:

> a\. VHA facility is an authoritative source for date of death if the person died in the VHA facility or while under VA auspices,

> b\. Death Certificate, and

> c\. National Cemetery Administration (NCA) is an authoritative source for the date of death if the Veteran has received NCA benefits.

> 11. MOTHER’S NAME and FATHER’S NAME: The patient’s mother’s and father’s complete legal names need to be entered in the appropriate fields, when known. Values such as “deceased,” “unknown,” and other inappropriate responses in lieu of the name or in addition to the name are not to be used.

> 12. INCAPACITATED, UNIDENTIFIED, OR UNRESPONSIVE PATIENTS (for whatever reason): Records for incapacitated patients must be entered with a pseudo SSN, 1910 for the DOB, and name entered as UU-UNRESPONSIVE, PATIENT. Subsequent patient records must be entered as UU-UNRESPONSIVE, PATIENT A, UU-UNRESPONSIVE, PATIENT B, etc. Records must be completed with appropriate identity data trait fields once the patient has been identified.

> 13. TEST PATIENTS: It is essential that TEST patients who exist in local VistA production systems be designated with a SSN containing five leading zeros (i.e., 000001111) and the last name prefixed by ZZ (i.e., ZZTESTPATIENT, FIRSTNAME MIDDLE). Test entries not to be used for categories of persons outside of patients, or for patients that are other than those used exclusively for testing purposes. Any deviation must be approved by the Healthcare Identity Management (HC IdM) Program Manager.

> 14. RESEARCH PATIENTS: Research patients must have all valid information (i.e., legal name, real SSN, DOB, etc.) collected and entered.

> 15. SSN, DATE OF BIRTH, MOTHER’S MAIDEN NAME, PLACE OF BIRTH \[CITY\], PLACE OF BIRTH \[STATE\] and PLACE OF BIRTH \[COUNTRY\]: The SSN, DATE OF BIRTH, MOTHER’S MAIDEN NAME, PLACE OF BIRTH \[CITY\], PLACE OF BIRTH \[STATE\] and PLACE OF BIRTH \[COUNTRY\] identity trait fields are important and are to be collected for the unique identification of individuals, since these are fields that do not generally change over time. If these fields are inaccurate or incomplete, it is difficult to ensure that duplicates are not being created and that the record is being linked to the correct ICN on the MVI.

> 16. PATIENT RECORDS INVOLVED IN MEDICAL IDENTITY THEFT: Records for a patient that is determined to be an “imposter,” where staff are unable to obtain the true identity of a patient, need to be edited to reflect the NAME field of THEFT, IDENTITY A (where the trailing letter would be incremented for each subsequent entry that exists in the local VistA PATIENT File (#2)). The record needs to be edited to use a pseudo SSN and have the DOB recorded as 1910. Any facility staff suspecting for any reason, that a person may be fraudulently receiving VA health care benefits, must immediately notify their supervisor, the Chief of Health Information Management (HIM) and the Business Office Manager, or equivalent. These individuals are responsible for notifying the HC IdM Team, facility management staff, police, local Information Security Office, local Privacy Officer, appropriate Regional Counsel, and the Office of Inspector General (OIG). Edits to the patient record are not to be made until after the OIG investigation has been completed. Any electronic documentation that is determined not to belong to the real patient (if identified) must be retracted in the same manner that any document found to be erroneously attributed to a patient is removed.

> 17. ALIAS FIELDS: The ALIAS fields are only to be used to enter previously-used names and SSNs. Name changes due to marriage, divorce, etc., are to be entered into the ALIAS field.

> 18. MVI EXCEPTIONS IN VISTA: Exceptions processing must be performed on a daily basis to ensure that inconsistencies are addressed in a timely manner. Failure to resolve data quality issues may result in incorrect operation of the Remote Data View, VistA Web, and Inter- facility Consult functions for facility clinicians. When processing MVI exceptions in VistA, if potential enterprise duplicate records, data quality, or other ICN issues are identified, a request for assistance is to be sent by an e-mail message to the VHA HC IdM Team distribution group on Outlook. PKI encryption must be utilized when transmitting patient identifiable information. A request for national support can also be entered using the OIT national problem management system (Remedy©). When submitting requests for assistance using Remedy©, do not include

> the individual’s identifying information (name, SSN, etc.). The specialist assigned to the request must obtain this information directly from the MVI Point of Contact (POC). *NOTE: Additional information regarding MVI VistA User and Exception Handling manuals can be found on the VistA Documentation Library at:* [<u>MPI/PD documentation on the VA Software Document Library (VDL)</u>](http://www.va.gov/vdl/application.asp?appid=16)*.*

> 19. DUPLICATE PATIENT ENTRIES: Merging of local duplicate patient records in VistA is to be performed in an accurate manner and merge process initiated within <u>5 business days</u> of identification. When more than one record exists for the same patient a treating clinician may not see a complete view of the care provided to a patient and make treatment decisions based on a fragmented record. All proposed merges must be reviewed and approved by the ancillary package experts and the Chief HIM, or equivalent. *NOTE: To merge the data from one record to the other, use the process outlined in the DUPLICATE RECORD MERGE: Patient Merge User Manual located on the VistA Documentation Library at:* [<u>http://www.va.gov/vdl/</u>*.*](http://www.va.gov/vdl/)

> 20. MULTIPLE BIRTHS: Extreme caution must be taken when merging duplicate records to ensure the records are for the same individual. Many identity fields for individuals of multiple birth (e.g., twins) will be the same or similar. Once patients are identified as part of a multiple birth, the Multiple Birth Indicator needs to be set to “Yes” on all applicable records. It is essential that appropriate clinical ancillary staff and Chief HIM or equivalent, review potential duplicate records, to verify whether or not they should be merged.

> 21. ADDITIONAL INFORMATION: Information regarding the HC IdM Program, along with a current staff listing and the VHA facility POC can be found on the HC IdM Web page on the Data Quality Web site at: *REDACTED*

## Appendix B: MPI Glossary of Working Concepts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510586974" class="anchor"></span>Table B-1. MPI Glossary of Working Concepts

| DUPLICATE PATIENTS IN VistA – Not same ICN                 | More than one patient in a single PATIENT file (#2) cannot have the same Integration Control Number (ICN). This is a business rule established by Healthcare Identity Management (HC IdM).  If there is a site duplicate discovered, each patient will have their own unique ICN and a Potential Match Exception will be generated for HC IdM team to review.  If  HC IdM determines the record to be a duplicate, they will link the ICNs together and push down the entry to the Duplicate Record file in that VistA instance for processing via the Duplicate Record Merge application.                                                                                                                                    |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INSTITUTION FILE                                           | A site can be in only one VISN at a time. A record in the INSTITUTION file (#4) cannot have two parents of the same type. A record in the INSTITUTION file (#4) cannot be a child and have children of its own.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| MPI (AUSTIN)                                               | The Master Patient Index (MPI) is located at the Austin Information Technology Center (AITC). It is composed of a unique list of patients and an associated list of VAMCs (Veterans Affairs Medical Centers) and other systems of interest where each patient has been seen. This enables the sharing of patient data between operationally diverse systems. Each patient record (or index entry) on the MPI contains multiple demographic fields which are updated to the Primary View of the MPI.                                                                                                                                                                                                                           |
| PATIENT SENSITIVITY                                        | If a shared patient is flagged as sensitive at one of the treating sites, a bulletin is sent to the RG CIRN DEMOGRAPHIC ISSUES mail group at each subscribing site telling where, when, and by whom the flag was set. Each site can then review whether the circumstances meet the local criteria for sensitivity flagging. If the site chooses to change the patient to a sensitive status, the option to do so would be used and then a bulletin would be sent to the mail group established in the PIMS package for notifying users of a sensitive patient change.                                                                                                                                                         |
| CORRELATIONS (Formally referred to as Treating Facilities) | Systems that know a specific Integration Control Number (ICN) and have registered an interest in that ICN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| POTENTIAL IDENTITY CHANGE                                  | If two or more of the following fields are different than what is currently stored on the MPI (i.e., Name \[first or last name only - only count as 1\], SSN, DOB or Sex), there is no further broadcasting of the update anywhere. If the patient is shared, only that site's Treating Facility entry in the MPI VETERAN/CLIENT file, in Field \#985.5, is updated and an exception is logged on the Toolkit Exception Handler noting that a potential identity change has occurred. If the patient is NOT SHARED, then both the MPI VETERAN/CLIENT file (#985) and the Treating Facility entry (#985.5) is updated and an exception is logged to the MPI Exception Handler noting a potential identity change has occurred. |
| UPDATE MESSAGES                                            | Descriptive data update messages are broadcast by the MPI Austin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

Page intentionally left blank for double-sided print copy.

## Appendix C: Why Doesn't a Patient Have a National ICN?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What Causes a Patient Record Not to Have a National ICN Assignment?Answer:

- If the patient record was not included as part of the initial seeding process to the MPI. When the MPI was first initialized, patient records showing no activity in the last three fiscal years prior to the initialization were not enumerated with an ICN.
- If the patient record has not been edited or has not had clinical activity since approximately 1989, it would not have been sent up to the MPI for an ICN and CMOR assignment during the initial seeding of the index.
- If the patient record has not been processed into the system via any of the following PIMS options: Load/Edit, Register a Patient, or Electronic 10-10EZ Processing since the initial seeding of the index.
- Prior to this patch MPIF\*1\*33, the following criteria were not sent to the Master Patient Index (MPI) for national ICN assignment:
- Patient records with last names beginning with ZZ
- Patient records that have 5 leading zeros for the Social Security Number (SSN)
- Patients records with last names beginning with "EEE"
- Patients records with last names beginning with the word "Merging" (This applies to patients in the process of being merged via the Duplicate Record Merge software.)

> Patient records having met these criteria were either prevented from being sent to the MPI or were removed. Thus, these records currently exist in sites’ PATIENT file (#2) without a national ICN assignment.

- If the patient record had been merged with another.

What Causes a Patient Record to Have Only a Local ICN Assignment?Answer:

- If communication can't be established or is lost with the MPI before the ICN assignment process has completed.
- If the site edits an existing or adds a new patient using an option that doesn't directly interact with the MPI (e.g., VistA Lab or VA FileMan).
- If the patient is being added to the MPI (via the HL7 ADT-A28 message) as a placeholder until a National ICN is assigned. A local ICN is assigned to prevent processing the patient again on the MPI during that interim period.

Page intentionally left blank for double-sided print copy.

## Appendix D: Change to Identity Management Fields, Patch MPIF\*1\*37

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In an earlier patch, MPIF\*1\*28, the user was prompted for selected identifying fields in the PATIENT file (#2) early in the Registration process, so the information would be available for the query to the Master Patient Index (MPI) system. Code was added in routine MPIFAPI to accomplish this. This Application Programmer Interface (API) was called by the Registration options that interact with the MPI to ask for the identifying fields.

Patch MPIF\*1\*37 modifications to the API MPIFAPI affects ONLY those fields that are displayed immediately after the prompt: "Please verify or update the following information:." For identity management fields, listed below, this API only prompts for selected fields if they are blank or imprecise in accordance with the following business rules:

- All fields display if they were previously blank.
- Date of Birth field displays if it contains an imprecise date.
- Social Security Number field displays if it is a pseudo number.
- Mother's Maiden Name and Place of Birth (City, State) fields display if the free text field contains extraneous information (e.g., UNKNOWN, NOT AVAILABLE, NOT GIVEN, NOT KNOWN, UNAVAILABLE, or DECEASED, etc.)

With Patch MPIF\*1\*37, the display of the identity management fields, listed below, is conditional based on the criteria outlined in the MPI business rules, listed above.

- Date of Birth
- Sex
- Social Security Number
- Multiple Birth Indicator
- Mother's Maiden Name
- Place of Birth (City, State)
- Alias

Page intentionally left blank for double-sided print copy.

## Appendix E: Primary View Identity Traits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the list of fields that are stored in the Primary View of the MPI.

|                                                                                                                |                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-user-manual/064.png) | NOTE: Not all Primary View fields are synchronized to the systems of interest. |

<span id="Table_E1" class="anchor"></span>Table E-1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name and Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>INTEGRATION CONTROL NUMBER (ICN) (#.01)</td>
<td><p>Based on ASTM E-1714 format is 16 digits, delimiter character, 6 checksum digits.</p>
<p>When the ICN is displayed in the MPI, it appears as 10 digits followed by the delimiter character (“V”) followed by the 6 checksum digits.</p></td>
</tr>
<tr class="even">
<td>SURNAME (#1)</td>
<td>Family name, also known as last name.</td>
</tr>
<tr class="odd">
<td>FIRST NAME (#2)</td>
<td>Patient’s first given name.</td>
</tr>
<tr class="even">
<td>MIDDLE NAME (#3)</td>
<td>Patient’s middle name or middle initial.</td>
</tr>
<tr class="odd">
<td>NAME PREFIX (#4)</td>
<td><p>Commonly, Dr., Ms., Sir, or other appropriate titles.</p>
<p>NOTE: Not currently populated on the MPI.</p></td>
</tr>
<tr class="even">
<td>NAME SUFFIX (#5)</td>
<td>Examples are Jr., Sr., PhD, etc.</td>
</tr>
<tr class="odd">
<td>MOTHERS MAIDEN NAME (#6)</td>
<td>Mother’s Surname at her birth.</td>
</tr>
<tr class="even">
<td>DATE OF BIRTH (#7)</td>
<td>Date of patient’s birth.</td>
</tr>
<tr class="odd">
<td>PLACE OF BIRTH CITY (#8)</td>
<td><p>Name of the city or town (or nearest) where the patient was born.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="even">
<td>PLACE OF BIRTH STATE (#9)</td>
<td><p>If USA, 2 character state abbreviation. If not USA, the country state. Pointer to the STATE file (#5).</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>PLACE OF BIRTH COUNTRY (#9.1)</td>
<td><p>The PLACE OF BIRTH COUNTRY field identifies the Country that was selected from the available COUNTRY CODE list for where the individual was  born.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="even">
<td>PLACE OF BIRTH PROVINCE (#9.2)</td>
<td><p>The PLACE OF BIRTH PROVINCE field identifies the location within certain countries containing additional divisions of where the individual was born.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>DATE OF DEATH (#10)</td>
<td><p>The date of the person's death.</p>
<p>As of Patch MPI*1*90, Increment 7, Date of Death will be on the Primary View when supplied from one of NCA’s systems, BOSS, or AMAS. Date of Death <em><u>will not</u></em> be synched from PV to the correlations for Increment 8.</p></td>
</tr>
<tr class="even">
<td>DEATH VERIFICATION STATUS (#11)</td>
<td><p>One of four criteria must exist to flag this as Verified:</p>
<ul>
<li><blockquote>
<p>Patient death under VA auspices</p>
</blockquote></li>
<li><blockquote>
<p>DoD casualty report</p>
</blockquote></li>
<li><blockquote>
<p>Receipt of certified death certificate</p>
</blockquote></li>
<li><blockquote>
<p>Burial benefits by NCS</p>
</blockquote></li>
</ul>
<p>NOTE: Not currently populated on the MPI.</p></td>
</tr>
<tr class="odd">
<td>GENDER (#12)</td>
<td><ul>
<li><blockquote>
<p>M = MALE</p>
</blockquote></li>
<li><blockquote>
<p>F = FEMALE</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>SOCIAL SECURITY NUMBER (#13)</td>
<td><p>Patient’s Social Security Number (SSN)</p>
<p>NOTE: Pseudo SSNs aren't stored on the MPI.</p></td>
</tr>
<tr class="odd">
<td><p>SSN VERIFICATION STATUS (#14)</p>
<p>NOTE: Added to File #985 as of Patch MPI*1*40. Populated to the Primary View of the MPI and systems of interest to the MPI as of DG*5.3*688 [EVC R2].</p></td>
<td><p>Status of the verification of a patient's SSN. This value is stored on the MPI, derived from an update from the ESR application after interaction with SSA (Social Security Administration). Possible values synchronized to sites are:</p>
<ul>
<li><blockquote>
<p>Null</p>
</blockquote></li>
<li><blockquote>
<p>INVALID PER SSA</p>
</blockquote></li>
<li><blockquote>
<p>VERIFIED</p>
</blockquote></li>
</ul>
<p>Possible values used on the MPI for the ESR correlation are:</p>
<ul>
<li><blockquote>
<p>NEW RECORD</p>
</blockquote></li>
<li><blockquote>
<p>IN-PROCESS</p>
</blockquote></li>
<li><blockquote>
<p>INVALID PER SSA</p>
</blockquote></li>
<li><blockquote>
<p>RESEND TO SSA</p>
</blockquote></li>
<li><blockquote>
<p>VERIFIED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><p>PSEUDO SSN REASON (#14.1)</p>
<p>NOTE: Added to File #985 as of Patch MPI*1*40. Populated to the Primary View of the MPI and systems of interest to the MPI as of RG*1*47 and DG*5.3*653 [EVC R1].)</p></td>
<td><p>Used to document the reason an individual was assigned a pseudo SSN. Available reasons are:</p>
<ul>
<li><blockquote>
<p>(R) Refused to Provide—Individual was asked for his/her SSN but refused to provide the number.</p>
</blockquote></li>
<li><blockquote>
<p>(S) SSN Unknown/Follow-up required—Individual is not available to ask/answer the request for SSN. The facility should initiate follow-up activity to obtain the SSN.</p>
</blockquote></li>
<li><blockquote>
<p>(N) No SSN Assigned—Individual has not been assigned an SSN. This generally applies to spouse or dependents of veterans who are not US citizens, and infrequently, non-citizen beneficiaries.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>CLAIM NUMBER (#15)</td>
<td>VBA assigned claim number.  Used to assist confirming ID.</td>
</tr>
<tr class="even">
<td>COORDINATING MASTER OF RECORD (#16)</td>
<td>Pre-Primary View Coordinating Site for patient. POINTER TO INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td>SENSITIVITY (#17)</td>
<td><p>Sensitivity is used to assist in sensitive management audit reports for unusual activity.</p>
<p>NOTE:  This field is not utilized.</p></td>
</tr>
<tr class="even">
<td>PRIMARY ICN (#18)</td>
<td>As of patch MPI*1.0*40, this field will be used as the value of the Primary ICN for a deactivated ICN. The field will only be populated for an entry that has an ID STATE of deactivated. It is basically telling which ICN should be used instead.</td>
</tr>
<tr class="odd">
<td>DATE/TIME OF ORIGINAL CREATION (#19)</td>
<td>Date/time that the patient was added to the MPI VETERAN/CLIENT (#985) file.  This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</td>
</tr>
<tr class="even">
<td>FACILITY OF ORIGINAL CREATION (#20)</td>
<td>Facility that originally added the patient to the MPI VETERAN/CLIENT (#985) file.  This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</td>
</tr>
<tr class="odd">
<td>CREATED BY (#21)</td>
<td>The CREATED BY field identifies the person at the FACILITY OF ORIGINAL CREATION who added the patient to the MPI VETERAN/CLIENT (#985) file. This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</td>
</tr>
<tr class="even">
<td>RESOLUTION JOURNAL CASE NUMBER (#22)</td>
<td>If a case exists in the MPI DATA MGT RESOLUTION JOURNAL file (#985.2) for this ICN it will be stored in this field regardless of the status of the case.  Resolution Journal cases hold the history of any resolution work done by the Healthcare Identity Management (HC IdM) on this ICN.</td>
</tr>
<tr class="odd">
<td>PRIMARY VIEW DATE LAST UPDATED (#23)</td>
<td>The PRIMARY VIEW DATE LAST UPDATED field is the date/time that any of the patient's identity element fields were last updated in the MPI VETERAN/CLIENT (#985) file.</td>
</tr>
<tr class="even">
<td>IDENTITY THEFT (#24)</td>
<td>The IDENTITY THEFT field is used to designate that a specific record has been confirmed by Health Care Identity Management (HC IdM) staff to be involved in an identity theft occurrence. Once it has been marked, the IDENTITY THEFT field will prevent good records from being linked or matched to the identify theft record.</td>
</tr>
<tr class="odd">
<td>TEMPORARY ID NUMBER (#25)</td>
<td>The Department of Defense (DoD) Defense Eligibility Enrollment Reporting System (DEERS) uses a Temporary Identification Number for individuals (e.g., babies) who do not have or have not provided a Social Security Number (SSN) when the record is added to DEERS.  It is used for military dependents only. </td>
</tr>
<tr class="even">
<td>FOREIGN ID NUMBER (#26)</td>
<td>The Department of Defense (DoD) Defense Eligibility Enrollment Reporting System (DEERS) uses a Foreign Identification Number for foreign military and foreign nationals when the record is added to DEERS.</td>
</tr>
<tr class="odd">
<td>SELF IDENTIFIED GENDER (#27)</td>
<td><p>The value of Self Identified Gender specifies the patient’s self-identified gender identity.</p>
<p>NOTE: The PV value will NOT be synched out at this time. This new field will not be shared to NCA, VBA, DoD or any outside agency/company at this time.</p>
<p>NOTE: As of Patch DG*5.3*902, the menu text display for the field named SELF-IDENTIFIED GENDER was changed to “Self-Identified Gender Identity” in the following MPI/PD options:</p>
<ul>
<li><blockquote>
<p>Patient MPI/PD Data Inquiry</p>
</blockquote></li>
<li><blockquote>
<p>Remote Patient Data Query Menu ...</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>STREET ADDRESS [LINE 1] (#31)</td>
<td><p>First line of patient's residence street address (3-35 characters).</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>STREET ADDRESS [LINE 2] (32#)</td>
<td><p>Second line of patient's residence street address (3-30 characters) if the space provided in "street address" was not sufficient.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td>STREET ADDRESS [LINE 3] (33#)</td>
<td><p>Third line of patient's residence street address (3-30 characters) if the space provided in "street address" and "street address 2" was not sufficient.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>CITY [RESIDENCE] (#34)</td>
<td><p>City in which patient resides (3-28 characters).</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td>STATE [RESIDENCE] (#35)</td>
<td><p>State in which patient resides.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>ZIP+4 [RESIDENCE] (#36)</td>
<td><p>Five or Nine digit Zip Code.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td>EMAIL ADDRESS (#36.1)</td>
<td>The Email Address (3-50 characters) for receiving electronic correspondence on.</td>
</tr>
<tr class="odd">
<td>PHONE NUMBER [RESIDENCE] (#37)</td>
<td><p>Telephone number (4-23 characters) to patient's place of residence.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td><p>MULTIPLE BIRTH INDICATOR (#39)</p>
<p>NOTE: Added to the list of fields auto-updated in VistA as of Patch RG*1*47.</p></td>
<td><p>The MULTIPLE BIRTH INDICATOR will designate whether or not the patient is part of a multiple birth (i.e. to identify twins, etc.). Possible values are:</p>
<ul>
<li><blockquote>
<p>N = NO</p>
</blockquote></li>
<li><blockquote>
<p>Y = MULTIPLE BIRTH</p>
</blockquote></li>
<li><blockquote>
<p>Null (not the same as No)</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>PROVINCE (#40)</td>
<td><p>Enter a PROVINCE if the patient has provided one for his/her foreign address.      The entry can be alphanumeric and up to 20 characters in length.</p>
<p>NOTE: As of Patch MPI*1*90, this field was added to the Primary View and is populated from ESR.</p></td>
</tr>
<tr class="even">
<td>POSTAL CODE (#41)</td>
<td><p>Enter the patient's POSTAL CODE if the patient has provided one for his/her foreign address. The entry can be alphanumeric and up to 10 characters in length.  </p>
<p>NOTE: As of Patch MPI*1*90, this field was added to the Primary View and is populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>COUNTRY (#42)</td>
<td><p>Enter the COUNTRY where the patient's permanent address is located.  If entering an Army/Air Force Post Office (APO) or a Fleet Post Office (FPO) address, select United States as the country.</p>
<p>NOTE: As of Patch MPI*1*90, this field was added to the Primary View and is populated from ESR.</p></td>
</tr>
<tr class="even">
<td>ALIAS (#50)</td>
<td>If this patient is known by any name other than that entered in the name field enter that/those other name(s) here. (Multiple field)</td>
</tr>
<tr class="odd">
<td>ALIAS SURNAME (#02,.01)</td>
<td><p>Patient's last name (aka family name). If this patient is known by any name other than that entered in the Name field, enter the other name(s) here.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="even">
<td>ALIAS FIRST NAME (#.02,1)</td>
<td><p>Patient’s first name.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="odd">
<td>ALIAS MIDDLE NAME (#.02,2)</td>
<td><p>Patient’s middle name or middle initial.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="even">
<td>ALIAS PREFIX (#.02,3)</td>
<td><p>Commonly, Dr., Ms., Sir, or other appropriate titles.</p>
<p>NOTE: Not currently populated on the MPI. Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="odd">
<td>ALIAS SUFFIX (#.02,4)</td>
<td><p>Examples are Jr., Sr., PhD, etc.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="even">
<td>ALIAS SSN (#.02,5)</td>
<td><p>If the patient was also known under a name other than that listed in the NAME field of the PATIENT file (#2), enter the social security number used if different when the patient used this alias. Include any different SSNs used by person even if names are the same.</p>
<p>NOTE: Alias SSNs that are Pseudo SSNs will not be stored on the MPI. Alias SSN is paired with an Alias Name.  There can't be just an alias SSN. Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="odd">
<td>ALIAS DATE LAST UPDATED (#.02,6)</td>
<td>The ALIAS DATE LAST UPDATED field is the date/time that the ALIAS field was last updated in the MPI VETERAN/CLIENT (#985) file.</td>
</tr>
<tr class="even">
<td>RACE INFORMATION (#60)</td>
<td><p>Enter the race that best identifies this patient.</p>
<p>NOTE: Not synchronized to the systems of interest. Once in Primary View, will be an aggregated list from all treating facilities. (Multiple field)</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="odd">
<td>RACE INFORMATION (#.03,.01)</td>
<td><p>Enter the races which best identify this patient.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="even">
<td>RACE DATE LAST UPDATED (#.03,1)</td>
<td><p>The RACE DATE LAST UPDATED field is the date/time that the RACE field was last updated in the MPI VETERAN/CLIENT (#985) file.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="odd">
<td>ETHNICITY INFORMATION (#70)</td>
<td><p>Enter the ethnicity that best identifies this patient.</p>
<p>NOTE: Not synchronized to the systems of interest. Once in Primary View, will be an aggregated list from all treating facilities. (Multiple field setup but only one value stored)</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="even">
<td>ETHNICITY INFORMATION (#.04,.01)</td>
<td><p>Enter the ethnicity which best identifies this patient.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="odd">
<td>ETHNICITY DATE LAST UPDATED (#.04,1)</td>
<td><p>The ETHNICITY DATE LAST UPDATED field is the date/time that the ETHNICITY field was last updated in the MPI VETERAN/CLIENT (#985) file.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="even">
<td>ID STATE (#80)</td>
<td><p>The following ID STATE definitions are from the Object Management Group (OMG) Person Identification Service (PIDS) Specification. ID STATE designates the status of the entry in the MPI VETERAN/CLIENT (#985) file in accordance with business rules and standards. Values for the patient are:</p>
<ul>
<li><p>P = Permanent</p></li>
<li><p>T = Temporary</p></li>
<li><p>D = Deactivated</p></li>
</ul>
<p>PERMANENT: This ID State specifies that all required fields are entered and a national ICN is established. When an ID is created as permanent all mandatory traits <em>must</em> be provided. A permanent ID can be deactivated but <em>cannot</em> be made temporary except for when HC IdM uses the OVR function.</p>
<p>TEMPORARY: This ID State specifies that there are not enough fields to make an entry permanent (as defined further in the business rules). An ID can be created as temporary without indicating any mandatory traits. A common usage is to create an ID that data can be bound to a patient before that patient is identified with an appropriate confidence. A temporary ID can be made permanent or deactivated.</p>
<p>DEACTIVATED: This ID State specifies that the ICN is no longer used. Once an ID is expected not to be needed any more it can be deactivated (merged or deprecated), which keeps it around for historical purposes. A deactivated ID is in its final state and <em>cannot</em> be transitioned to any other state by PIDS operations.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>DATE OF ID STATE (#81)</td>
<td>The DATE OF ID STATE field identifies when the ID STATE field was last updated.</td>
</tr>
<tr class="even">
<td>SURNAME PRIMARY VIEW SCORE (#85)</td>
<td>The SURNAME PRIMARY VIEW SCORE field contains the Primary View Authority Score for the SURNAME (#1) identity element.</td>
</tr>
<tr class="odd">
<td>FIRST NAME PRIMARY VIEW SCORE (#86)</td>
<td>The FIRST NAME PRIMARY VIEW SCORE field contains the Primary View Authority Score for the FIRST NAME (#2) identity element.</td>
</tr>
<tr class="even">
<td>MIDDLE NAME PRIMARY VIEW SCORE (#87)</td>
<td>The MIDDLE NAME PRIMARY VIEW SCORE field contains the Primary View Authority Score for the MIDDLE NAME (#3) identity element.</td>
</tr>
<tr class="odd">
<td>PREFIX PRIMARY VIEW SCORE (#88)</td>
<td>The PREFIX PRIMARY VIEW SCORE field contains the Primary View Authority Score for the NAME PREFIX (#4) identity element. Not currently populated on the MPI.</td>
</tr>
<tr class="even">
<td>SUFFIX PRIMARY VIEW SCORE (#89)</td>
<td>The SUFFIX PRIMARY VIEW SCORE field contains the Primary View Authority Score for the NAME SUFFIX (#5) identity element</td>
</tr>
<tr class="odd">
<td>DOB PRIMARY VIEW SCORE (#90)</td>
<td>The DOB PRIMARY VIEW SCORE field contains the Primary View Authority Score for the DATE OF BIRTH (#7) identity element.</td>
</tr>
<tr class="even">
<td>GENDER PRIMARY VIEW SCORE (#91)</td>
<td>The GENDER PRIMARY VIEW SCORE field contains the Primary View Authority Score for the GENDER (#12) identity element.</td>
</tr>
<tr class="odd">
<td>SSN PRIMARY VIEW SCORE (#92)</td>
<td>The SSN PRIMARY VIEW SCORE field contains the Primary View Authority Score for the SOCIAL SECURITY NUMBER (#13) identity element.</td>
</tr>
<tr class="even">
<td>MMN PRIMARY VIEW SCORE (#95)</td>
<td>The MMN PRIMARY VIEW SCORE field contains the Primary View Authority Score for the MOTHER'S MAIDEN NAME (#6) identity element.</td>
</tr>
<tr class="odd">
<td>MULT BIRTH PRIMARY VIEW SCORE (#96)</td>
<td>The MULT BIRTH PRIMARY VIEW SCORE field contains the Primary View Authority Score for the MULTIPLE BIRTH INDICATOR (#39) identity element.</td>
</tr>
<tr class="even">
<td>POB CITY PRIMARY VIEW SCORE (#97)</td>
<td>The POB CITY PRIMARY VIEW SCORE field contains the Primary View Authority Score for the PLACE OF BIRTH CITY (#8) identity element.</td>
</tr>
<tr class="odd">
<td>POB STATE PRIMARY VIEW SCORE (#98)</td>
<td>The POB STATE PRIMARY VIEW SCORE field contains the Primary View Authority Score for the PLACE OF BIRTH STATE (#9) identity element.</td>
</tr>
<tr class="even">
<td>IDENTITY THEFT ACTIVATION (#102)</td>
<td>The IDENTITY THEFT ACTIVATION field is used to determine when a specific record has been confirmed by the Health Care Identity Management (HC IdM) staff to have been involved in an identity theft occurrence.</td>
</tr>
<tr class="odd">
<td>IDENTITY THEFT DEACTIVATION (#103)</td>
<td>The IDENTITY THEFT DEACTIVATION field is used to determine when a specific record has been removed/cleared by the Health Care Identity Management (HC IdM) staff as having been involved in an identity theft occurrence.</td>
</tr>
<tr class="even">
<td>DEATH ENTERED BY (#104)</td>
<td><p>Name of the individual who entered the DATE OF DEATH.</p>
<p>DEATH ENTERED BY is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="odd">
<td>SOURCE OF NOTIFICATION (#105)</td>
<td><p>Specifies who first notified the VA of the patient’s death.</p>
<p>SOURCE OF NOTIFICATION is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="even">
<td>DATE OF DEATH LAST UPDATED (#106)</td>
<td><p>Date/Time the DATE OF DEATH was last updated for the patient.</p>
<p>DATE OF DEATH LAST UPDATED is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="odd">
<td>DEATH LAST EDITED BY (#107)</td>
<td><p>Name of the individual who last edited the DATE OF DEATH.</p>
<p>DEATH LAST EDITED BY is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="even">
<td>SSA VERIFICATION STATUS (#108)</td>
<td>The SSA VERIFICATION STATUS field identifies the current state of the record.</td>
</tr>
<tr class="odd">
<td>ID INTEROPERABLTY PERSON TYPE (#109)</td>
<td>The ID INTEROPERABLTY PERSON TYPE field identifies the current interoperability person type of the record.</td>
</tr>
<tr class="even">
<td>LEVEL OF ASSURANCE (#110)</td>
<td><p>The LEVEL OF ASSURANCE field identifies the confidence level of the record as determined by the MyHealtheVet (MHV) application.</p>
<p>The LEVEL OF ASSURANCE values refer to the four identity authentication assurance levels for E-Government transactions, described in “E-Authentication Guidance for Federal Agencies” [OMB 04-04]. The four assurance levels are:</p>
<ul>
<li><p>Level1 : Little or no confidence in the asserted identity’s validity.</p></li>
<li><p>Level2 : Some confidence in the asserted identity’s validity.</p></li>
<li><p>Level3 : High confidence in the asserted identity’s validity.</p></li>
<li><p>Level4 : Very high confidence in the asserted identity’s validity.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>DEATH INDICATOR (Y/N)? (#111)</td>
<td><p>The DEATH INDICATOR (Y/N)? field identifies whether or not an individual has been identified as deceased.</p>
<p>Note: Initially this field will only be identified and populated by site 200IVT (Identity Verify Tool), which correlates to the ‘Experian’ integration work.</p></td>
</tr>
<tr class="even">
<td>NOTIFICATION PROVIDER (#113)</td>
<td>The NOTIFICATION PROVIDER field identifies the current Line of Business (LOB) system that correlated a patient’s date of death.</td>
</tr>
<tr class="odd">
<td>SUPPORTING DOCUMENT TYPE (#114)</td>
<td>The SUPPORTING DOCUMENT TYPE field identifies the current document used to inform of a patient’s date of death from the Line of Business (LOB) system.</td>
</tr>
<tr class="even">
<td>DATE OF DEATH OPTION USED (#115)</td>
<td><p>The DATE OF DEATH OPTION USED field specifies the option used on the Line of Business (LOB) system when editing (adding/updating) a patient’s date of death. Option values include the following:</p>
<ul>
<li><p>JRN_OBJ</p></li>
<li><p>JRN_APP</p></li>
<li><p>JRN_STN</p></li>
<li><p>DEATH ENTRY</p></li>
<li><p>DISCHARGE A PATIENT</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>DISCHARGED DATE/TIME (#116)</td>
<td><p>The DISCHARGED DATE/TIME field identifies the date (time is optional) when a patient was last discharged from the Veteran Affairs Medical Center (VAMC).</p>
<p>DISCHARGED DATE/TIME is identified and populated at the VAMC level and updated on the Master Veteran Index (MVI).</p></td>
</tr>
<tr class="even">
<td>DATE OF DEATH OVERRIDE REASON (#117)</td>
<td><p>The DATE OF DEATH OVERRIDE REASON field specifies the reason for making a change to the date of death on a patient’s record. Reason values included the following:</p>
<ul>
<li><p>DECEASED WHILE INPATIENT</p></li>
<li><p>DEATH CERTIFICATE</p></li>
<li><p>NCA</p></li>
<li><p>VERIFIED VIA BIRLS</p></li>
<li><p>VERIFIED VIA SSA</p></li>
<li><p>DATE OF DEATH CORRECTION</p></li>
<li><p>ENTERED IN ERROR</p></li>
<li><p>IDENTITY THEFT</p></li>
</ul>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>DEATH STATUS (#118)</td>
<td><p>The DEATH STATUS field specifies whether the DATE OF DEATH (#20) value in the correlation [MPI FACILITY ASSOCIATION file #985.5] has successfully passed all of the Primary View (PV business rules to get promoted into PV. Status values include the following:</p>
<ul>
<li><p>PENDING</p></li>
<li><p>VERIFIED</p></li>
</ul></td>
</tr>
<tr class="even">
<td>PERSON TYPE (#150)</td>
<td>The person types that this person is identified by. (Multiple field)</td>
</tr>
<tr class="odd">
<td>PERSON TYPE<br />
(#.054, .01)</td>
<td>The Person Type(s) selected from the available list [MPI PERSON TYPES FILE #985.72] that identifies the current person type(s) of the record.</td>
</tr>
<tr class="even">
<td>PREFERRED NAME (#300)</td>
<td>Specifies the name on how the patient would prefer to be referenced by during interactions at the medical facility.</td>
</tr>
</tbody>
</table>

The ALIAS Multiple Stored on MPI and Synchronized to VistA

In the Primary View of the MPI, the ALIAS multiple (#50) is stored in the MPI VETERAN/CLIENT file (#985) as an aggregated list from all the treating facilities associated with that ICN. In VistA, the ALIAS multiple (#1) is stored in the PATIENT file (#2). All edits made by Healthcare Identity Management (HC IdM) staff to the ALIAS multiple on the MPI via the Edit PV Alias Values \[MPI DATA MGT EDIT PV ALIAS\] option are updated in the Primary View on the MPI and synchronized out to all systems of interest (e.g., VistA treating facilities) for that patient. Site edits to the ALIAS multiple (#1) in the VistA PATIENT file (#2) are updated in VistA and sent to the MPI for updates to the Primary View. The updates are then synchronized back out to all other treating facilities (systems of interest) associated with that ICN.

Edits to the ALIAS Multiple Not Scored in Primary View

The ALIAS identity multiple (#50) has no associated activity score on the MPI. The alias is an aggregated list in the Primary View of all alias information from all the treating facilities and is synchronized with the other treating facilities. If your site adds an alias then everyone will get that alias. If your site deletes an alias entry, then any corresponding entries at the other systems of interest associated with that ICN will remain in Primary View, basically requiring HC IdM to become involved to delete an alias value.

Page intentionally left blank for double-sided print copy.

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A
Add New Patient to MPI, 7-6
Add/Edit Point of Contact, 5-45
Additional Patient Identity Fields, 3-13
ADT/HL7 PIVOT file (#391.71), 6-2
ALIAS multiple
Field \#1 in File \#2, 3-14, 9
Field \#50 in File \#985, 3-14, 9
stored on MVI and synchronized to VistA, 3-14
ALIAS Multiple Stored on MPI and Synchronized to VistA, 9
Appendix A
VHA DIRECTIVE 1906, 1
Appendix B: MPI Glossary of Working Concepts, 1
Appendix C: Why Doesn't a Patient Have a National ICN?, 1
Electronic 10-10EZ Processing, 1
HL7 ADT-A28 message, 1
Load/Edit Patient Data, 1
local ICN, 1
patient record does not have a national ICN?, 1
Register a Patient, 1
Appendix D: Change to Identity Management Fields, Patch
MPIF\*1\*37, 1
Appendix E: Primary View Identity Traits, 1
Authority Score Criteria, 5-12
B
Background Jobs
Local ICNs, 6-1
LOCAL/MISSING ICN RESOLUTION, 6-1
Missing ICNs, 6-1
Resolution of Local/Missing ICNs, 6-2
UPDATE BATCH JOB FOR HL7 v2.3, 6-2
Bulletin, 4-2
Business Processes That Update Person Identity, 3-2
C
Chapter 1: Introduction, 1-1–1-3
Distinguishing MPI (Austin) from MPI/PD (VistA), 1-2
History, 1-2
Installation Information, 1-3
MPI Identity Hub for the HC IdM Team, 1-2
Overview of Master Patient Index/Patient Demographics, 1-1
Overview of Master Veteran Index (MVI), 1-1
Chapter 2: Product Description―What Comprises the Master Patient Index?, 2-1–2-4
HC IdM Team is Data Steward for the Master Veteran Index, 2-1
Master Patient Index/Patient Demographics (VistA), 2-2
Primary View Replaces Obsolete CMOR View, 2-3
Requesting ICN Assignment, 2-2
Systems of Interest to the MVI—Treating Facilities and Non-VistA Systems, 2-3
What Comprises the Master Patient Index Austin, 2-1
Chapter 3: Primary View—How are VistA Sites Affected by this Change to the MVI?, 3-1–3-15
Business Rules for Data Validity and Integrity, 3-2
Enhanced MPI-to-VistA Synchronization—Additional Patient Identity Fields, 3-13
HC IdM View/Edit Authority Values for Business Rules Criterion, 3-15
How Does the Primary View Work?, 3-2
Multiple Birth Indicator Synchronized to Systems of Interest, 3-13
Primary View Auto-Updates Person Identity Fields in the File \#2, 3-3
Primary View Identity Traits, 3-4
Primary View Reject, 3-15
Process Sequence for Inbound Edits, 3-14
SSN and Pseudo SSN Reason Synchronized to Systems of Interest, 3-13
SSN Verification Status Synchronized to Systems of Interest, 3-13
The ALIAS Multiple Stored on MVI and Synchronized to VistA, 3-14
What is the Primary View?, 3-1
Chapter 4: Software Management, 4-1–4-3
HL7 Application Parameters file, 4-2
Legal Requirements, 4-2
Name and Number Spaces, 4-1
Software Requirements, 4-1
Chapter 5: MPI/PD Menus and Options, 5-1–5-51
MPI/PD Master Menu, 5-1
MPI/PD IRM Menu, 5-2, 5-46
MPI/PD Patient Admin Coordinator Menu, 5-2, 5-4
Standalone Options, 5-49
Chapter 6: Background Jobs, 6-1–6-4
Chapter 7: PIMS Options, 7-1–7-14
Check Remote Patient Data Query, 5-27
CIRN HL7 EXCEPTION LOG file (#991.1), 5-42, 5-48
DATE/TIME PROCESSED field (#7), 5-11
CIRN HL7 EXCEPTION TYPE file (#991.11), 5-42, 5-48
CIRN SITE PARAMETER file (#991.8), 5-49, 6-1
CMOR obsolete, 5-1
COMPILE MPI/PD HL7 DATA, 5-50
Contents, xvi
D
data dictionary
Data Dictionary Utilities menu, xxiv
listings, xxiv
data rules, 5-12
DG\*5.3\*505, 5-14
DG\*5.3\*653, 3-3
DG\*5.3\*688, 3-3
DG\*5.3\*707, xiii, xiv, 5-14
DG\*5.3\*712, ix, 5-19
DG\*5.3\*756, xi, xii, 3-3
DG\*5.3\*825, viii
DG\*5.3\*863, vii, 5-20
DG\*5.3\*876, vi
DG\*5.3\*902, iv
Direct Connect, 7-1
becomes unavailable, 7-13
local ICNs, 7-13
Single Patient Initialization to MPI, 7-13
TCP/IP connection, real-time, 7-1, 7-13
Display Only Query, 5-31
Patient Doesn’t Exist in Patient File, 5-33
Patient Exists in Patient File, 5-31
Patient with an Open Data Management Case, 5-35
Display Remote Patient Data Query, 5-28
patient with pseudo SSN, 5-25
Distinguishing MPI (Austin) from MPI/PD (VistA), 1-2
documentation symbols, xxi
E
Edit PV Alias Values \[MPI DATA MGT EDIT PV ALIAS\], 3-14, 9
Electronic 10-10EZ Processing, 2-2, 6-1, 7-1, 1
Enhanced MPI-to-VistA Synchronization, 3-13
Multiple Birth Indicator Synchronized to Systems of Interest, 3-13
SSN and Pseudo SSN Reason Synchronized to Systems of Interest, 3-13
SSN Verification Status Synchronized to Systems of Interest, 3-13
The ALIAS Multiple Stored on MPI and Synchronized to VistA, 3-14
Enterprise Search
Registration Process, 18
Exact Record Match Found for Patient on the MPI, 7-3
F
Figures, xviii
files
ADT/HL7 PIVOT file (#391.71), 6-2
CIRN HL7 EXCEPTION LOG file (#991.1), 5-11, 5-42, 5-48
CIRN HL7 EXCEPTION TYPE file (#991.11), 5-42, 5-48
CIRN SITE PARAMETER file (#991.8), 5-49, 6-1
HL7 MESSAGE TEXT file (#772), 5-50, 5-51
INSTITUTION file (#4), 4-2
MPI VETERAN/CLIENT file (#985), 2-1, 3-3, 3-4
PATIENT file (#2), 3-3, 5-14, 5-19, 5-31, 5-33, 5-39, 5-41, 6-1, 6-4, 7-1, 7-6, 7-9, 1
TREATING FACILITY LIST file (#391.91), 5-14, 5-46
G
Glossary, 1–26
Glossary (Security and Common Services)
Web Address, 26
H
Healthcare Identity Management (HC IdM)
Data Steward for the MPI, 2-1
View/Edit Authority Values for Business Rules Criterion, 3-15
help
at prompts, xxiii
online, xxiii
HL7 Application Parameters file, 4-2
HL7 MESSAGE TEXT file (#772), 5-50, 5-51
HL7 SITE POC mail group (on FORUM), 4-3
Home Pages
Security and Common Services
Glossary Web Address, 26
How Does the Primary View Work?, 3-2
How to
obtain technical information online, xxiii
use this manual, xxi
I
ICN (Integration Control Number)
Direct Connect, 7-1
local ICNs, 7-13
real-time request for, 7-1
ICN assignment
exact match on MPI, 2-1
local, 6-1, 7-14
local ICN, 1
MPI Austin, 2-1
MPI VistA, 2-2
national, 2-1, 2-2, 6-1
patient record does not have a national ICN?, 1
requesting, 2-2
transmission to MPI, 7-14
VistA can't connect, 7-14
Installation Information, 1-3
Installation Information and Procedures, xxiii
INSTITUTION file (#4), 4-2
Intended Audience/Assumptions, xxii
Introduction, 1-1–1-3
Patches MPIF\*1\*52, RG\*1\*54, XT\*7.3\*113, 1-2
L
Legal Disclaimers, xxiv
Legal Requirements, 4-2
Link and Process Status Display, 5-41, 5-46
List File Attributes Option, xxiv
Load/Edit Patient Data, 2-2, 6-1, 7-1, 1
adding new persons to the MPI, 7-9
local ICNs, 7-13, 7-14
assignment, 7-13
Local ICNs, 6-1
LOCAL/MISSING ICN RESOLUTION, 5-49, 6-1
M
mail groups
HL7 SITE POC (on FORUM), 4-3
MPIF EXCEPTIONS, 4-3
RG CIRN DEMOGRAPHIC ISSUES, 4-3
RG CIRN HL7 PROBLEMS, 4-3
management reports, 5-39
Link and Process Status Display, 5-41
Pseudo-SSN Report, 5-39
Unresolved Exception Summary, 5-42
Master Veteran Index
What is the?
Master Patient Index (Austin), 2-1
Master Patient Index/Patient Demographics (VistA), 2-2
Product Description, 2-1
Systems of Interest, 2-3
Treating Facilities, 2-3
Master Veteran Index (MVI), 1-1
menu text
Add/Edit Point of Contact, 5-45
Check Remote Patient Data Query, 5-27
COMPILE MPI/PD HL7 DATA, 5-50
Display Only Query, 5-31
Display Remote Patient Data Query, 5-28
Electronic 10-10EZ Processing, 2-2, 6-1, 7-1, 1
Link and Process Status Display, 5-41, 5-46
List File Attributes, xxiv
Load/Edit Patient Data, 2-2, 6-1, 7-1, 7-6, 1
Local/Missing ICN Resolution, 2-2, 7-1
LOCAL/MISSING ICN RESOLUTION, 5-49
Management Reports. . ., 5-39
Message Exception Menu, 5-11
MPI/PD HL7 ACTIVITY BY PATIENT/ALL PROTOCOLS, 5-51
MPI/PD HL7 ACTIVITY BY PATIENT/SINGLE PROTOCOL, 5-51
MPI/PD HL7 DIAGNOSTIC MENU, 5-50
MPI/PD HL7 EXCEPTION NOTIFIER, 5-49
MPI/PD HL7 MESSAGE STATUS REPORT, 5-50
MPI/PD IRM Menu, 5-2, 5-46
MPI/PD Master Menu, 5-1
MPI/PD Patient Admin Coordinator Menu, 5-2, 5-4
Patient Audit File Print, 5-6
Patient Audit Log Reports…, 5-4
Patient MPI/PD Data Inquiry, 5-14
Primary View Display from MPI, 5-37
Pseudo-SSN Report, 5-39
Register a Patient, 2-2, 6-1, 7-1, 7-9, 1
Remote Patient Data Query Menu, 5-26
Send Remote Patient Data Query, 5-26
Single Patient Audit File Print, 5-10
ToolKit POC User Setup, 5-43
Unresolved Exception Summary, 5-42, 5-48
Message Exception Menu, 5-11
Display Only Query, 5-31
Patient MPI/PD Data Inquiry, 5-14
Primary View Display from MPI, 5-37
Remote Patient Data Query Menu, 5-26
Missing ICNs, 6-1
MPI
Add New Patient, 7-6
Installation Information and Procedures, xxiii
MPI DATA MGT PDAT MPI, 5-38
MPI Direct Connection Unavailable
local ICN assignments, 7-13
MPI Fields Broadcast to Systems of Interest, 3-3
MPI Glossary of Working Concepts, 1
MPI Patient Data Inquiry, 5-38
MPI Primary View Centralized Business Rules
Primary View Identity Traits, 3-4, 1
MPI VETERAN/CLIENT file (#985), 2-1, 3-3, 3-4
ALIAS multiple (#50), 3-14, 9
MPI\*1\*38, 5-49, 6-1
MPI\*1\*40, 1-1, 2-3, 3-3
MPI\*1\*90, 3-4, 3-6, 3-7
MPI\*1\*91, 3-8
MPI/PD HL7 ACTIVITY BY PATIENT/ALL PROTOCOLS, 5-51
MPI/PD HL7 ACTIVITY BY PATIENT/SINGLE PROTOCOL, 5-51
MPI/PD HL7 DIAGNOSTIC MENU, 5-50
MPI/PD HL7 EXCEPTION NOTIFIER, 5-49
MPI/PD HL7 MESSAGE STATUS REPORT, 5-50
MPI/PD IRM Menu, 5-2, 5-46
Link and Process Status Display, 5-46
Unresolved Exception Summary, 5-48
MPI/PD mail groups, 4-3
HL7 SITE POC (on FORUM), 4-3
MPIF EXCEPTIONS, 4-3
RG CIRN DEMOGRAPHIC ISSUES, 4-3
RG CIRN HL7 PROBLEMS, 4-3
MPI/PD Master Menu, 5-1
MPI/PD Patient Admin Coordinator Menu, 5-2
Patient Audit File Print, 5-6
Patient Audit Log Reports…, 5-4
Single Patient Audit File Print, 5-10
MPI/PD Patient Admin Coordinator Menu \[MPIF CMOR MGR\] obsolete, 2-3, 5-1
MPIF DISPLAY ONLY QUERY TO MPI, 5-31
MPIF EXCEPTIONS mail group, 4-3
MPIF LOC/MIS ICN RES, 5-49
MPIF\*1\*21, 1-2, 5-36
MPIF\*1\*28, 1
MPIF\*1\*33, 1-2
MPIF\*1\*35, 5-49, 6-1, 6-2
MPIF\*1\*37, 1
MPIF\*1\*43, 6-1
MPIF\*1\*44, 2-3
MPIF\*1\*52, 1-2, 2-2, 7-6
MPIF\*1.0\*43, xiv
MPIF\*1.0\*44, xiv
MPIF\*1.0\*46, xiii
MPIF\*1.0\*52, ix, x
MPIF\*1.0\*57, vii
Multiple Birth Indicator Synchronized to Systems of Interest, 3-13
Multiple Patient Records Found on the MPI, 7-6
MVI (Master Veteran Index)
new persons added, 7-9
N
Name and Number Spaces, 4-1
O
obsolete
CMOR, 2-3, 5-1
MPI/PD Patient Admin Coordinator Menu \[MPIF CMOR MGR\], 2-3, 5-1
online
Documentation, xxiii
Help Frames, xxiv
technical information, How to obtain, xxiii
options
DG LOAD PATIENT DATA, 2-2, 6-1, 7-1, 1
DG REGISTER PATIENT, 2-2, 6-1, 7-1, 1
EAS EZ 1010EZ PROCESSING, 2-2, 6-1, 7-1, 1
MPI DATA MGT EDIT PV ALIAS, 3-14, 9
MPIF DISPLAY ONLY QUERY TO MPI, 5-31
MPIF LOC/MIS ICN RES, 2-2, 5-49, 7-1
RG ADMIN COORD MENU, 5-2, 5-4
RG EXCEPTION MENU, 5-11
RG EXCEPTION NOTIFIER, 5-49
RG EXCEPTION TF INQUIRY, 5-14
RG IRM MENU, 5-2, 5-46
RG LINKS AND PROCESS DISPLAY, 5-41, 5-46
RG MGT REPORTS, 5-39
RG PRIMARY VIEW FROM MPI, 5-37
RG REMOTE PDAT CHECK, 5-27
RG REMOTE PDAT DISPLAY, 5-28
RG REMOTE PDAT MENU, 5-26
RG REMOTE PDAT SEND, 5-26
RG STATUS DISPLAY, 5-42, 5-48
RG TK POC USER SETUP, 5-43
RG TRAN/AUD AUD REP, 5-4
RG UPDATE POINT OF CONTACT, 5-45
RGMGR, 5-1
RGMT AUDIT PRINT, 5-6
RGMT AUDIT SINGLE, 5-10
RGMT DIAG ALL PROTOCOLS, 5-51
RGMT DIAG COMPILE HL7 DATA, 5-50
RGMT DIAG MGR, 5-50
RGMT DIAG SINGLE PROTOCOL, 5-51
RGMT DIAG STATUS REPORT, 5-50
RGPR PRE-IMP SSN REPORT, 5-39
options, PIMS, 7-1
Load/Edit Patient Data, 7-6
Load/Edit Patient Data \[DG LOAD PATIENT DATA\], 7-7
Register a Patient, 7-9
Register a Patient \[DG REGISTER PATIENT\], 7-2
Orientation, xxi–xxiv
conventions for displaying TEST data, xxi
How to obtain technical information online, xxiii
How to use this manual, xxi
Installation Information and Procedures, xxiii
Intended Audience/Assumptions, xxii
Legal Disclaimers, xxiv
Reference Material, xxii
Overview of PIMS Interaction with the MPI, 7-1
P
Patch
DG\*5.3\*505, 5-14
DG\*5.3\*653, 3-3
DG\*5.3\*688, 3-3
DG\*5.3\*707, xiii, xiv, 5-14
DG\*5.3\*712, ix, 5-19
DG\*5.3\*756, xi, xii, 3-3
DG\*5.3\*825, viii
DG\*5.3\*863, vii, 5-20
DG\*5.3\*876, vi
DG\*5.3\*902, iv
MPI\*1\*38, 5-49, 6-1
MPI\*1\*40, 1-1, 2-3, 3-3
MPI\*1\*90, 3-4, 3-6, 3-7
MPI\*1\*91, 3-8
MPIF\*1\*21, 1-2, 5-36
MPIF\*1\*28, 1
MPIF\*1\*33, 1-2
MPIF\*1\*35, 5-49, 6-1, 6-2
MPIF\*1\*37, 1
MPIF\*1\*43, 6-1
MPIF\*1\*44, 2-3
MPIF\*1\*52, 2-2, 7-6
MPIF\*1.0\*43, xiv
MPIF\*1.0\*44, xiv
MPIF\*1.0\*46, xiii
MPIF\*1.0\*52, ix, x
MPIF\*1.0\*57, vii
RG\*1\*10, xxiii
RG\*1\*20, 5-42, 5-47, 5-48
RG\*1\*23, 5-49
RG\*1\*43, 5-13, 5-42, 6-1, 7-6
RG\*1\*45, 3-3, 3-13
RG\*1\*47, 3-3, 3-13
RG\*1\*59, 5-23
RG\*1\*6, xxiii
RG\*1.0\*43, xiv
RG\*1.0\*44, xiii
RG\*1.0\*45, xiv
RG\*1.0\*48, xii
RG\*1.0\*50, xii
RG\*1.0\*53, xi
RG\*1.0\*54, ix
RG\*1.0\*57, ix
RG\*1.0\*59, viii
RG\*1.0\*60, vii, 5-6, 5-7
RG\*1.0\*61, vi
RG\*1.0\*62, iv, 3-15, 5-11
XT\*7.3\*113, xxii, 2-3
XT\*7.3\*23, xxiii
XT\*7.3\*49, xxiii
Patch History, xv
Patches MPIF\*1\*52, RG\*1\*54, XT\*7.3\*113, 1-2
Patient Audit File Print, 5-6
Patient Audit Log Reports…, 5-4
PATIENT file (#2), 3-3, 5-14, 5-19, 5-31, 5-33, 5-39, 5-41, 6-1, 6-4, 7-1, 7-6, 7-9, 1
ADT/HL7 PIVOT file (#391.71), 6-4
ALIAS multiple (#1), 3-14, 9
Data monitored in the PATIENT file for changes, 6-4
UPDATE BATCH JOB FOR HL7 v2.3, 6-4
Patient is Not Already on the MPI, 7-1
Patient MPI/PD Data Inquiry, 5-14
Partial example of inquiry showing person with pseudo SSN, 5-19
Partial example showing Bad Address Indicator data, 5-19
Patient MPI/PD Data Inquiry─Example of inquiry showing patient with an SSN Verification Status
Verified, 5-17
Patient Sensitivity, 7-13
person & user names
test data, xxi
persons (new) added to MPI, 7-9
PIMS options, 7-1
Load/Edit Patient Data, 7-6
Load/Edit Patient Data \[DG LOAD PATIENT DATA\], 7-7
Register a Patient, 7-9
Register a Patient \[DG REGISTER PATIENT\], 7-2
Primary View
Additional Patient Identity Fields, 3-13
Authority Score Criteria, 5-12
Business Processes That Update Person Identity, 3-2
data rules, 3-2, 5-12
Enhanced MPI-to-VistA Synchronization, 3-13
HC IdM View/Edit Authority Values for Business Rules Criterion, 3-15
How are VistA Sites Affected?, 3-1
How Does the Primary View Work?, 3-2
MPI Fields Broadcast to Systems of Interest, 3-3
Multiple Birth Indicator Synchronized to Systems of Interest, 3-13
Primary View Identity Traits, 3-4, 1
process for updating, 3-14
SSN and Pseudo SSN Reason Synchronized to Systems of Interest, 3-13
SSN Verification Status Synchronized to Systems of Interest, 3-13
The ALIAS Multiple Stored on MPI and Synchronized to VistA, 3-14
Primary View Data Rules, 3-2
Primary View Display from MPI, 5-37
Primary View Identity Traits, 3-4, 1
Process Existing Patient Already on MPI, 7-9
Process for updating the Primary View, 3-14
Product Description
HC IdM is Data Steward for the MPI, 2-1
ICN assignment, 2-1
Master Patient Index/Patient Demographics (VistA), 2-2
Primary View Replaces Obsolete CMOR View, 2-3
Requesting ICN Assignment, 2-2
Systems of Interest to the MPI, 2-3
Treating Facilities and Non-VistA Systems, 2-3
What Comprises the Master Patient Index Austin?, 2-1
Pseudo-SSN Report, 5-39
Q
question mark help,, xxiii
R
real-time TCP/IP connection, 7-1, 7-13
Reference Material, xxii
Register a Patient, 2-2, 6-1, 7-1, 1
Registration Process
Enterprise Search, 18
Remote Patient Data Query Menu, 5-26
Check Remote Patient Data Query, 5-27
Display Remote Patient Data Query, 5-28
Send Remote Patient Data Query, 5-26
Resolution of Local/Missing ICNs, 6-2
Revision History, ii
RG ADMIN COORD MENU, 5-2, 5-4
RG CIRN DEMOGRAPHIC ISSUES mail group, 4-3
RG CIRN HL7 PROBLEMS mail group, 4-3
RG EXCEPTION MENU, 5-11
RG EXCEPTION NOTIFIER, 5-49
RG EXCEPTION TF INQUIRY, 5-14
RG IRM MENU, 5-2, 5-46
RG LINKS AND PROCESS DISPLAY, 5-41, 5-46
RG MGT REPORTS, 5-39
RG PRIMARY VIEW FROM MPI, 5-37
RG REMOTE PDAT CHECK, 5-27
RG REMOTE PDAT DISPLAY, 5-28
RG REMOTE PDAT MENU, 5-26
RG REMOTE PDAT SEND, 5-26
RG STATUS DISPLAY, 5-42, 5-48
RG TRAN/AUD AUD REP, 5-4
RG\*1\*10, xxiii
RG\*1\*20, 5-42, 5-47, 5-48
RG\*1\*23, 5-49
RG\*1\*43, 5-13, 5-42, 6-1, 7-6
RG\*1\*45, 3-3
RG\*1\*45, 3-13
RG\*1\*47, 3-3, 3-13
RG\*1\*54, 1-2
RG\*1\*59, 5-23
RG\*1\*6, xxiii
RG\*1.0\*43, xiv
RG\*1.0\*44, xiii
RG\*1.0\*45, xiv
RG\*1.0\*48, xii
RG\*1.0\*50, xii
RG\*1.0\*53, xi
RG\*1.0\*54, ix
RG\*1.0\*57, ix
RG\*1.0\*59, viii
RG\*1.0\*60, vii, 5-6, 5-7
RG\*1.0\*61, vi
RG\*1.0\*62, iv, 3-15, 5-11
RGMGR, 5-1
RGMT AUDIT PRINT, 5-6
RGMT AUDIT SINGLE, 5-10
RGMT DIAG ALL PROTOCOLS, 5-51
RGMT DIAG COMPILE HL7 DATA, 5-50
RGMT DIAG MGR, 5-50
RGMT DIAG SINGLE PROTOCOL, 5-51
RGMT DIAG STATUS REPORT, 5-50
RGPR PRE-IMP SSN REPORT, 5-39
S
Security and Common Services
Glossary Web Address, 26
Send Remote Patient Data Query, 5-26
Single Patient Audit File Print, 5-10
Social Security Numbers
test data, xxi
Software Management, 4-1
Bulletin, 4-2
HL7 Application Parameters file, 4-2
Legal Requirements, 4-2
MPI/PD mail groups, 4-3
Name and Number Spaces, 4-1
Software Requirements, 4-1
Software Requirements, 4-1
SSN and Pseudo SSN Reason Synchronized to Systems of Interest, 3-13
SSN Verification Status Synchronized to Systems of Interest, 3-13
standalone options
COMPILE MPI/PD HL7 DATA, 5-50
LOCAL/MISSING ICN RESOLUTION, 5-49
MPI/PD HL7 ACTIVITY BY PATIENT/ALL PROTOCOLS, 5-51
MPI/PD HL7 ACTIVITY BY PATIENT/SINGLE PROTOCOL, 5-51
MPI/PD HL7 DIAGNOSTIC MENU, 5-50
MPI/PD HL7 EXCEPTION NOTIFIER, 5-49
MPI/PD HL7 MESSAGE STATUS REPORT, 5-50
Symbols Found in the Documentation, xxi
Systems of Interest
MPI Fields Broadcast to, 3-3
T
TCP/IP connection, real-time, 7-1, 7-13
test data
person & user names, xxi
Social Security Numbers, xxi
ToolKit POC User Setup, 5-43
TREATING FACILITY LIST file (#391.91), 5-14, 5-46
U
Unresolved Exception Summary, 5-42, 5-48
UPDATE BATCH JOB FOR HL7 v2.3, 6-2
URLs
Security and Common Services
Web Address, Glossary, 26
V
VHA Directive 1906
Data Quality Requirements for Healthcare Identity Management and Master Veteran Index Functions, 1
W
Web Pages
Security and Common Services
Glossary Web Address, 26
What is the Master Veteran Index?
Master Patient Index (Austin), 2-1
Master Patient Index/Patient Demographics (VistA), 2-2
Product Description, 2-1
Treating Facilities, 2-3
Who Should Read this Manual?, xxii
Why Doesn't a Patient Have a National ICN?, Appendix C, 1
X
XT\*7.3\*113, xxii, 1-2, 2-3
XT\*7.3\*23, xxiii
XT\*7.3\*49, xxiii
