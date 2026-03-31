---
title: MPI/PD Version 1 VISTA Technical Manual
doc_type: TM
doc_label: Technical Manual
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
  - 391
  - 984
  - 985
  - 991
security_keys: []
menu_options: 32
description: 
audience: 
keywords: 
  - strong
  - colspan
  - patient
  - class
  - blockquote
  - vista
  - table
  - view
  - even
  - identity
page_count: 0
word_count: 41836
section_count: 41
table_count: 76
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: April 1999
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index_(MPI)/rg1_0_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index_(MPI)/rg1_0_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=16"
---

---
title: |
  Master Patient Index  
  Patient Demographics (MPI/PD)

  Version 1.0

  Technical Manual

  ![](mpi-pd-version-1-vista-technical-manual/001.png)
---

April 1999

Office of Information and Technology (OI&T)

Revision History

<span id="_Toc510587935" class="anchor"></span>Table i. Documentation Revision History

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 70%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/2018</td>
<td><p>Documentation updates are listed by patch designation and RTC Story.</p>
<p>Software enhancements for this release comprise Patch MPI*1.0*123/Story #782858 (VETS360).</p>
<p>Field added to “Table 1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)”</p>
<ul>
<li><p>EMAIL ADDRESS (#36.1)</p></li>
</ul></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>4/2018</td>
<td>Corrected references to Self Identified Gender identity in MPI-PD VistA Manuals and HC IdM Manuals based on feedback from the VA Lesbian, Gay, Bisexual, and Transgender (LGBT) Health Program.</td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>10/2017</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story.</p>
<p>Software enhancements for this release comprise companion VistA Patch DG*5.3*944.</p>
<p>RTC <u>Story:557909</u>: “Auditing Place of Birth [City] and Place of Birth [State] in VistA”</p>
<ul>
<li><p>Added the following new fields to “Table 7. Fields that should be turned on for auditing in the PATIENT file (#2) for MPI/PD:”</p></li>
</ul>
<ul>
<li><blockquote>
<p>PLACE OF BIRTH [CITY] (#2,.092)</p>
</blockquote></li>
<li><blockquote>
<p>PLACE OF BIRTH [STATE] (#2,.093)</p>
</blockquote></li>
</ul>
<p>RTC <u>Story 504382</u> (<u>Sub-Story: 513042</u>): “Add new fields (POB Country and POB Province [not Person Type]) to the PATIENT file, Add trigger to the new fields in the PATIENT file, Enable Auditing on fields in PATIENT file (#2) new fields”</p>
<ul>
<li><p>Added the following new fields to “Table 1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file):”</p></li>
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
<li><p>Added the following new fields to “Table 6. Data elements monitored in the PATIENT file (#2) for changes” and “Table 7. Fields that should be turned on for auditing in the PATIENT file (#2) for MPI/PD:”</p></li>
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
<tr class="even">
<td>5/2017</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story.</p>
<p>Software enhancements for this release comprise companion VistA Patches DG*5.3*937, RG*1.0*67 and MPIF*1.0*65.</p>
<p>RTC Story 445457/Sub-Stories:</p>
<ul>
<li><blockquote>
<p>455414: “Add new field to the PATIENT file, Add trigger to the new field in the PATIENT file, Enable Auditing on field in PATIENT file (#2) new field”</p>
</blockquote></li>
</ul>
<blockquote>
<p>The PREFERRED NAME field (#.2405) been added to the PATIENT (#2) file and are utilized by the MPI. (See “Table 6. Data elements monitored in the PATIENT file (#2) for changes”)</p>
<p>The PREFERRED NAME field (#.2405) is enabled for audtiting. (See “AuditingTable 7. Fields that should be turned on for auditing in the PATIENT file (#2) for MPI/PD”)</p>
</blockquote>
<ul>
<li><blockquote>
<p>455445: “Add new field at the Primary View level #985, Enable audit on new field at the Primary View level #985”</p>
</blockquote></li>
</ul>
<blockquote>
<p>The following fields have been added to the Primary View of the MPI (see “Table 1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)”):</p>
</blockquote>
<ul>
<li><blockquote>
<p>DEATH STATUS (#118)</p>
</blockquote></li>
<li><blockquote>
<p>PREFERRED NAME (#300)</p>
</blockquote></li>
</ul></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>12/2016</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story. Software enhancements for this release comprise companion VistA Patches DG*5.3*926, MPIF*1.0*64 and RG*1.0*65.</p>
<p>Patch DG*5.3*926 documentation updates:</p>
<p>RTC Story 323008: Enhance VistA Source of Notification field in the PATIENT file (#2):</p>
<ul>
<li><blockquote>
<p>The following fields was added to the Primary View of the MPI (see “Table 1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file),”) stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file):</p>
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
</ul>
<ul>
<li><blockquote>
<p>The following new field was added to the VistA PATIENT file (#2) and is utilized by the MPI. (See “Table 6. Data elements monitored in the PATIENT file (#2) for changes”):</p>
</blockquote></li>
</ul>
<ul>
<li><p>SUPPORTING DOCUMENT TYPE (#.357)</p></li>
</ul>
<ul>
<li><blockquote>
<p>The following fields were added to the VistA PATIENT file (#2), enabled for auditing.</p>
</blockquote></li>
</ul>
<ul>
<li><p>SUPPORTING DOCUMENT TYPE (#.357)</p></li>
<li><p>DATE OF DEATH OPTION USED (#.358)</p></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>11/2016</td>
<td><p>Patch MPIF*1.0*63 documentation update:</p>
<p>This patch creates the entry “TWO” in the MPI ICN BUILD MANAGEMENT file (#984.8) to determine which communication protocol layer (HTTP or HTTPS) will be utilized when communicating with PSIM.</p>
<p><em>For more information, see the annotation listed with File #984.8 in the Section “Files and Globals.”</em></p></td>
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
<li><blockquote>
<p>Healthcare Identity Management (HC IdM) has requested the removal/deletion of Primary View Rejects (PVRs) and PVR functionality. As of Patch RG*1.0*62:</p>
</blockquote></li>
</ul>
<ul>
<li><p>Exception #234 (Primary View Reject) are no longer being logged.</p></li>
<li><p>A post-init process executed and marked all existing unresolved 234 exceptions as Resolved.</p></li>
<li><p>The menu option MPI/PD Exception Handling [RG EXCEPTION HANDLING] was removed, since it is no longer needed.</p></li>
<li><p>“Appendix A: Exceptions and Bulletins” was removed.</p></li>
</ul>
<ul>
<li><blockquote>
<p>New option and associated RPC:</p>
</blockquote></li>
</ul>
<ul>
<li><p>A new option named ToolKit POC User Setup [RG TK POC USER SETUP] has been created and placed on the MPI/PD Patient Admin Coordinator Menu [RG ADMIN COORD MENU] to set up Visitor Records on the MPI to support POC (Point of Contact) remote view access.</p></li>
<li><p>This new option calls a new RPC named MPI TK POC USER SETUP, which will access the MPI to establish a Visitor Record in the NEW PERSON file (#200).</p></li>
</ul>
<ul>
<li><blockquote>
<p>In support of the new Date of Death (DOD) requirements to the MPI, the following fields from the PATIENT (#2) file will be added to the OBX message segment of the ADT-A08 HL7 message (See “Table 6. Data elements monitored in the PATIENT file (#2) for changes.”):</p>
</blockquote></li>
</ul>
<ul>
<li><p>DEATH ENTERED BY (#.352)</p></li>
<li><p>SOURCE OF NOTIFICATION (#.353)</p></li>
<li><p>DATE OF DEATH LAST UPDATED (#.354)</p></li>
<li><p>LAST EDITED BY (#.355)</p></li>
</ul>
<blockquote>
<p>These fields have been enabled for auditing.</p>
</blockquote>
<p>Patch DG*5.3*902 documentation updates:</p>
<ul>
<li><blockquote>
<p>The following new fields have been added to the PATIENT (#2) file and are utilized by the MPI. (See “Table 6. Data elements monitored in the PATIENT file (#2) for changes”):</p>
</blockquote></li>
</ul>
<ul>
<li><p>FULL ICN (#991.1)</p></li>
<li><p>FULL ICN HISTORY (#991.91)</p></li>
</ul>
<blockquote>
<p>Both fields contain the complete Integration Control Number (ICN) value, which includes the Identifier, Delimiter, Checksum, and optional Encryption Scheme.</p>
</blockquote>
<ul>
<li><blockquote>
<p>The following fields have been added to the Primary View of the MPI (see “Table 1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file).”) and are stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file):</p>
</blockquote></li>
</ul>
<ul>
<li><p>IDENTITY THEFT ACTIVATION (#102)</p></li>
<li><p>IDENTITY THEFT DEACTIVATION (#103)</p></li>
<li><p>DEATH ENTERED BY (#104)</p></li>
<li><p>SOURCE OF NOTIFICATION (#105)</p></li>
<li><p>DATE OF DEATH LAST UPDATED (#106)</p></li>
<li><p>DEATH LAST EDITED BY (#107)</p></li>
</ul>
<ul>
<li><blockquote>
<p>Additional changes for Increment 13:</p>
</blockquote></li>
</ul>
<ul>
<li><p>Updated Glossary.</p></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>10/2014</td>
<td><p>Documentation updates:</p>
<p>Patch DG*5.3*876:</p>
<ul>
<li><blockquote>
<p>The following field was added to the VistA PATIENT file (#2). This field specifies the patient’s self-identified gender identity.</p>
</blockquote></li>
</ul>
<ul>
<li><p>SELF IDENTIFIED GENDER (#.024)</p></li>
</ul>
<blockquote>
<p>Prompt Message:  Select the code that specifies the patient's preferred gender.</p>
<p>NOTE: This field has been turned on for auditing in the PATIENT file (#2) for MPI/PD.</p>
</blockquote>
<ul>
<li><blockquote>
<p>The following VistA PATIENT file (#2) fields were added to the Patient MPI/PD Data Inquiry option [RG EXCEPTION TF INQUIRY] so that if they exist, will be viewable upon execution:</p>
</blockquote></li>
</ul>
<ul>
<li><p>SELF IDENTIFIED GENDER (#.024)</p></li>
<li><p>PERIOD OF SERVICE (#.323).</p></li>
</ul>
<ul>
<li><blockquote>
<p>The following new fields on the MPI: PATIENT TYPE (#391) and VETERAN Y/N (#1901) were already being displayed on the extended data screen on the local Vista PDAT.</p>
</blockquote></li>
</ul>
<ul>
<li><p>TYPE (#391)</p></li>
<li><p>VETERAN (Y/N)? (#1901)</p></li>
</ul>
<ul>
<li><blockquote>
<p>The RPC, VAFC VOA ADD PATIENT, was enhanced to include a new optional parameter, PARAM("MBI"), which represents the MULTIPLE BIRTH INDICATOR (#994) from the PATIENT file (#2). If provided, it will ensure that when an add/update event is sent to the Master Patient Index (MPI), that the MBI value will be placed on the Primary View (PV), the 200 ESR correlation and the preferred facility in the MPI.</p>
</blockquote></li>
</ul>
<p>Patch RG*1.0*61:</p>
<ul>
<li><blockquote>
<p>The Add/Edit Point of Contact [RG UPDATE POINT OF CONTACT] option was removed from the CORD MPI/PD Patient Admin Coordinator Menu [RG ADMIN COORD MENU] and placed out-of-order as part of the MVI Increment 12 release.</p>
</blockquote></li>
</ul>
<p>Additional changes for Increment 12:</p>
<ul>
<li><blockquote>
<p>HC IdM recommended changes to name references: 1) MPI to MVI (where appropriate) and 2) Patient to Person (where appropriate).</p>
</blockquote></li>
</ul>
<ul>
<li><p>The term “Patient” is used when the reference is to VistA PATIENT file (#2). The “MPI” nomenclature is used to display these test data occurrences because the MPI component of the MVI interacts with the PATIENT file (#2). </p></li>
<li><p>All other references are made to “Person” and to the MVI (which overall includes the MPI, PSIM, and TK).</p></li>
</ul>
<ul>
<li><blockquote>
<p>Added a new section excerpt to the Implementation and Maintenance chapter titled “Further Patch Information,” describing a changed to the MVI business rules for DoD DEERS.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>7/2013</td>
<td><p>Patch DG*5.3*863:</p>
<ul>
<li><blockquote>
<p>When a patient's current residential address is located in a foreign country (e.g., for a Department of Defense (DoD) patient) the following foreign address fields, from the VistA PATIENT file (#2), are displayed in the Patient MPI/PD Data Inquiry and Display Remote Patient Data Query options:</p>
</blockquote></li>
</ul>
<ul>
<li><p>PROVINCE field #.1171</p></li>
<li><p>POSTAL CODE field #.1172</p></li>
<li><p>COUNTRY field #.1173</p></li>
</ul>
<p>Patch RG*1.0*60:</p>
<ul>
<li><blockquote>
<p>Include the PATIENT file (#2) ALIAS (#.01) and ALIAS SSN (#1) fields in the list of fields audited for changes by the MPI/PD software.</p>
</blockquote></li>
<li><blockquote>
<p>The obsolete report <em>"National ICN Statistics [RG NATIONAL ICN STATISTICS]"</em> was removed from the Management Reports [RG MGT REPORTS] menu. This report was exported for deletion at the sties with Patch RG*1.0*60.</p>
</blockquote></li>
<li><blockquote>
<p>Organization references and links were updated in this manual to reflect the most current changes in the Dept of Veterans Affairs.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>7/2012</td>
<td><p>Documentation updates <em><u>not</u></em> related to a patch release:</p>
<ul>
<li><blockquote>
<p>Replaced VistA Logo w/VA Seal on title page.</p>
</blockquote></li>
<li><blockquote>
<p>Updated appendix titled: "Data Stored on the MPI in Austin" to reflect current MPI VETERAN/CLIENT file (#985).</p>
</blockquote></li>
<li><blockquote>
<p>Updated appendix and table titled: "Primary View Identity Traits" to reflect Primary View of the MPI.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Glossary based on HC IdM feedback.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>1/2012</td>
<td><p>Documentation updates:</p>
<ul>
<li><blockquote>
<p>As of Patch DG*5.3*837, the following Data Dictionary changes were made to the TREATING FACILITY LIST file (#391.91):</p>
</blockquote></li>
</ul>
<ul>
<li><p>The ASSIGNING AUTHORITY field (#1) was removed and replaced by the ASSIGNING AUTHORITY field (#10).</p></li>
<li><p>The SOURCE ID multiple (#20) containing the SOURCE ID (#.01) and IDENTIFIER STATUS (#1) fields was removed and replaced by identical fields at the file level: SOURCE ID (#11) and IDENTIFIER STATUS (#12).</p></li>
</ul>
<ul>
<li><blockquote>
<p>As of Patch DG*5.3*837, MPI will no longer update the VAFC ASSIGNING AUTHORITY file (#391.92). That data is stored directly into the new ASSIGNING AUTHORITY field (#10) in the TREATING FACILITY LIST file (#391.91). This file is being deleted.</p>
</blockquote></li>
<li><blockquote>
<p>A number of patients at each VA facility that have not been assigned an ICN for a number of reasons. In an effort to support an automated enumeration of these remaining patients, two new Remote Procedures (RPCs) have been created.</p>
</blockquote></li>
</ul>
<ul>
<li><p>MPIF REMOTE FULL ICN STATS</p></li>
<li><p>MPIF REMOTE LOCAL ICN ASSIGN</p></li>
</ul>
<ul>
<li><blockquote>
<p>As of Patch RG*1*59, the following two fields were added to the VistA PATIENT file (#2) in support of the Defense Eligibility Enrollment Reporting System (DEERS). These fields are used by the Master Veteran Index to support the linking of patient records across VA and DoD.</p>
</blockquote></li>
</ul>
<ul>
<li><p>TEMPORARY ID NUMBER (#991.08)</p></li>
<li><p>FOREIGN ID NUMBER (#991.09)</p></li>
</ul>
<blockquote>
<p><strong>NOTE:</strong> Both new fields are turned on for auditing in the PATIENT file (#2) for MPI/PD.</p>
</blockquote></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>12/2010</td>
<td><p>Final updates to formatting for Patch DG*5.3*825 release.</p>
<p>Documented new RPC:</p>
<blockquote>
<p><strong>VAFC AA UPDATE REMOTE PROCEDURE</strong></p>
<p>Routine: PDAT^VAFCRPC</p>
<p>When a new entry is added to the MPI ASSIGNING AUTHORITY (#985.55) file on the MPI, the VAFC AA UPDATE REMOTE PROCEDURE is called.  The RPC triggers an update message to those Treating Facilities where the patient's Integration Control Number (ICN) is known and creates an identical entry in the VistA VAFC ASSIGNING AUTHORITY (#391.92) file.</p>
</blockquote></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>09/2010</td>
<td><p>As of Patch DG*5.3*825 updates as follows:</p>
<ul>
<li><blockquote>
<p>A new file was created named VAFC ASSIGNING AUTHORITY with file number #391.92. File #391.92 expands the capability of VA Identity Management Service (IdM) to support future initiatives, (e.g., National Health Information Network (NHIN) and non-Patient Identity Management, etc.). This file stores information used to assemble fully qualified identifiers used for either the Health Level Seven v2.4 or v3.0 standard.</p>
</blockquote></li>
<li><blockquote>
<p>The following two updates were made to the TREATING FACILITY LIST file (#391.91):</p>
</blockquote></li>
</ul>
<ul>
<li><p>The length of the SOURCE ID field (#.01) in the SOURCE ID multiple (#20) was changed from 40 to 150 characters to accommodate identifiers for National Health Information Network (NHIN) facilities.</p></li>
<li><p>The following new fields were created in the TREATING FACILITY LIST field (#391.91):</p></li>
</ul>
<ul>
<li><p>SOURCE ID TYPE (#.09) defines the data source and comes from the HL7 Table 0203, Identifier Type; set of codes (NI, PI, EI, PN, SS, NPI)</p></li>
<li><p>ASSIGNING AUTHORITY field (#1); pointer to the new VAFC ASSIGNING AUTHORITY file (#391.92). It identifies the entity that established the identification number for the patient.</p></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>07/2010</td>
<td><p>Patch DG*5.3*821 updates support the James A Lovell Joint VA/DOD Medical Center in North Chicago are listed as follows:</p>
<ul>
<li><blockquote>
<p>The SOURCE ID (#20) multiple has been added to the TREATING FACILITY LIST (#391.91) file on VistA.  The SOURCE ID (#.01) and IDENTIFIER STATUS (#1) fields are updated by a Treating Facility update from the Master Patient Index (MPI) and facilitate the addition of the Department of Defense (DoD) as a treating facility correlation.</p>
</blockquote></li>
<li><blockquote>
<p>New Remote Procedure Calls (RPC), which are documented in the RPC section in this manual:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>RPC: VAFC LOCAL GETCORRESPONDINIGIDS returns Treating Facility information.</p>
</blockquote></li>
<li><blockquote>
<p>RPC: VAFC NEW NC TREATING FACILITY adds active Department of Defense Correlations to Treating Facility List file (#391.91).</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>12/2009</td>
<td><p>MPI_CodeCR1841): Create MPI RPC to support the return an array of VAMC correlations with a Date Last Treated</p>
<p>Create MPI RPC to support the return an array of VAMC correlations with a Date Last Treated. This RPC will be called by the PSIM GetCorrespondingIDs WebService calls initiated by the North Chicago Registration UI for the purposes of obtaining and mimicking the Register Once functionality in the new North Chicago Joint Registration UI. Based on performance there might be a need to only return the site with the most recent DLT, however for this release return all entries in 985.5 for a given ICN.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>11/2009</td>
<td>Final updates to documentation implementing feedback from Product Support (PS) for national release.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>8/2009</td>
<td>Remedy Ticket: HD0000000244806 RG QUEUE documentation updated and exported as part of Patch RG*1*54. Included is a new Troubleshooting topic on How to Clear Tasks Waiting in the RG Queue in the Implementation and Maintenance section.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>7/2009</td>
<td>MPI_CodeCR1713: Identity Management Data Quality (IMDQ) name change to Healthcare Identity Management (HC IdM).</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>7/2009</td>
<td><p>Updates via Patch DG*5.3*712:</p>
<ul>
<li><blockquote>
<p>Healthcare Identity Management (HC IdM) requested that BAD ADDRESS INDICATOR field (#.121) be added to the fields monitored and stored on the MPI for use by the matching logic. This VistA field has been added to the existing VistA field trigger mechanism.</p>
</blockquote></li>
<li><blockquote>
<p>The Patient MPI/PD Data Inquiry option has been updated to display a Bad Address Indicator data, if available. This update is being released with Patch DG*5.3*712. The data is derived from the BAD ADDRESS INDICATOR field (#.121) in the PATIENT file (#2).</p>
</blockquote></li>
<li><blockquote>
<p>A new style cross-reference has been added to the following three fields in the VistA PATIENT file (#2) so that when the field is edited, that information is included in the ADT/HL7 PIVOT file (#391.71) in order to update the Master Patient Index:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>BAD ADDRESS INDICATOR (#.121)</p>
</blockquote></li>
<li><blockquote>
<p>EMAIL ADDRESS (#.133)</p>
</blockquote></li>
<li><blockquote>
<p>PHONE NUMBER [CELLULAR] (#.134)</p>
</blockquote></li>
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
<tr class="odd">
<td>2/2009</td>
<td>MPI_CR1499(MPI_CodeCR1527): IMDQ requested that BAD ADDRESS INDICATOR be added to the fields monitored and stored on the MPI for use by the matching logic. In order to support the MPI request, added the BAD ADDRESS INDICATOR VistA field (.121) to the existing VistA field trigger mechanism released with Patch dg*5.3*712.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>1/2009</td>
<td><p>MPI_CR1073 (MPI_CodeCR1429): 3.2.2 - Master Patient Index/Patient Demographics (MPI/PD) VistA Enhancements released with Patch MPIF*1*52:</p>
<ul>
<li><blockquote>
<p>Prevent logging of local exceptions for potential matches.</p>
</blockquote></li>
<li><blockquote>
<p>Auto-resolve existing VistA Potential Match exceptions.</p>
</blockquote></li>
<li><blockquote>
<p>Remove from the MPI/PD Exception Handler the action for resolving a Potential Match Exception and all associated screens and actions. This functionality will be supported by the IMDQ Toolkit.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>6/2008</td>
<td><p>Patch RG*1*52 makes the following changes in the MPI/PD software:</p>
<ul>
<li><blockquote>
<p>MPI/PD Patient Admin User Menu Removed</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>The MPI/PD Patient Admin User Menu [RG ADMIN USER MENU] was distributed with patch RG*1.0*49 (released 4/10/08) as obsolete with an Out of Order message. This option is being distributed in this build as DELETE AT SITE in order to remove it from the menu structure. There are other MPI/PD options in the MPIF* and VAFC* namespaces that are also obsolete that will be removed in future MPIF* and DG* patches.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>The following Date of Death exceptions in the MPI/PD Exception Handler have been made obsolete:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Exception Type: Death Entry on MPI not in VISTA.<br />
Description: MPI had Date of Death field populated. Vista did not have Date of Death.<br />
Exception number: 215.</p>
</blockquote></li>
<li><blockquote>
<p>Exception Type: Death Entry on Vista not in MPI.<br />
Description: VISTA had Date of Death field populated. MPI did not have Date of Death.<br />
Exception number: 216.</p>
</blockquote></li>
<li><blockquote>
<p>Exception Type: Death Entries on MPI and Vista DO NOT Match.<br />
Description: MPI and VistA had different dates of death for this patient.<br />
Exception number: 217.</p>
</blockquote></li>
</ul></li>
<li><blockquote>
<p>REMOTE DATE OF DEATH INDICATED Bulletin Made Obsolete:</p>
</blockquote></li>
</ul>
<ul>
<li><p>The Remote Date of Death Indicated notification message generated from the MPI has been made obsolete. This bulletin indicated that the patient had a date of death entered from the sending site but not at the receiving site.</p></li>
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
<tr class="even">
<td>4/2008</td>
<td>As of Patch RG*1*49 and DG*5.3*766, the Patient Data Review option has been disabled by placing the MPI/PD Patient Admin User Menu Out of order.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>3/2008</td>
<td><p>As of Patch DG*5.3*756, the ALIAS [#1] multiple in the PATIENT (#2) file will be updated in VistA resulting from the edits made to that information on the MPI by the IMDQ team. The VistA data will be synchronized to match the MPI values. Additionally, when a facility revises their local ALIAS data, the information will be transmitted to the MPI, which in turn will update all treating facilities where the patient is known.</p>
<p>NOTE: Patch DG*5.3*756 was released on September 6, 2007.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>12/2007</td>
<td>Identity Management Data Quality’s (IMDQ) request that the MPI/PD Exception Purge option, [RG EXCEPTION PURGE], be changed to process Primary View Reject exceptions similar to other MPI/PD exception types. Now, the purge job RG EXCEPTION PURGE eliminates duplicate exceptions for the same patient/exception type for <em>all</em> MPI/PD exception types, keeping only the most recent occurrence.</td>
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
<li><p>DATE/TIME PROCESSED field (#7)</p></li>
<li><p>WHO MARKED PROCESSED field (#8)</p></li>
</ul>
<blockquote>
<p>This data is now being captured and Identity Management Data Quality (IMDQ) staff will have the capability to view this information.</p>
</blockquote>
<ul>
<li><blockquote>
<p>A change has been made in the MPI/PD EXCEPTION HANDLING [RG EXCEPTION HANDLING] option. Upon selecting the MPI/PD Exception Handling option, instead of being prompted to run the exception purge, you are now notified when the last purge took place. The purge process runs automatically if it has not run within the past two hours; however, the MPI/PD EXCEPTION PURGE [RG EXCEPTION PURGE] option should be scheduled to run once an hour via Taskman. It can take a few minutes to run, but once the job is finished, you can go back to the Message Exception Menu and choose MPI/PD Exception Handling to view the results of the purge process.</p>
</blockquote></li>
<li><blockquote>
<p>A stand-alone option named View VistA Exceptions for Patient [MPI DATA MGT VISTA EXCEPTION] has been implemented on the MPI in Austin for the Identity Management Data Quality (IMDQ) team allowing them to query a VistA site for a selected patient and view all the existing VistA exceptions for a given date range. The VistA side support for this new MPI option came in as part of Patch RG*1*48.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
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
<tr class="odd">
<td>1/2007</td>
<td><p>As of Patches MPIF*1*44 and RG*1*45, this documentation has been updated to reflect the following:</p>
<ul>
<li><blockquote>
<p>The concept of a "CMOR facility" is being phased out and will be replaced by the Primary View when Patch MPI*1*40 is installed on the Austin MPI. VistA Patch MPIF*1*44 sets all VistA options related to "CMOR" out of order, rendering them obsolete. The OUT OF ORDER MESSAGE field for these options is marked as "Obsolete with Patch MPIF*1*44."</p>
</blockquote></li>
<li><blockquote>
<p>As of Patch MPIF*1*44, the Site Parameters Edit for CMOR MPIF SITE PARAMETER option, located on the MPI/PD Patient Admin Coordinator Menu, is obsolete and has been placed out of order.</p>
</blockquote></li>
<li><blockquote>
<p>As of Patch MPIF*1*44, the AUTO CHANGE CMOR NIGHT JOB MPIF CMOR REQUEST AUTO JOB option is obsolete. Sites that have this option scheduled to run via TaskMan, should unschedule it.</p>
</blockquote></li>
<li><blockquote>
<p>SSN VERIFICATION STATUS field (#.0907) is now synchronized out to Sites when updated by Enrollment System Redesign (ESR) as of Patch RG*1*45.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>4/2006</td>
<td>Updates to documentation based on Patches MPIF*1*43 and RG*1*43, which comprise the changes to the MPI/PD software resulting from the Health Eligibility Center (HEC) Enumeration to the Master Patient Index (MPI).</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>6/2005</td>
<td><p>Updated with Patch DG*5.3*648 to include the following fields in the list of fields monitored by the VAFC BATCH UPDATE JOB:</p>
<ul>
<li><blockquote>
<p>POW STATUS INDICATED? (#.525)</p>
</blockquote></li>
<li><blockquote>
<p>ELIGIBILITY (#0361,.01)</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>12/2004</td>
<td>Updated Orientation section to include conventions for displaying TEST data. See <a href="#_Orientation">Orientation</a> section for details.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>8/2004</td>
<td><p>The MPI Data Quality Team has requested to be able to remotely request a PUSH of CMOR. A Remote Procedure Call (RPC) will be added to the local VistA system to support this request. The MPIF CMOR REQUEST file (#984.9) will be updated to include these requests for tracking purposes. Routine MPIFRCMP supports this effort.</p>
<p>New Remote Procedure MPIF CMOR PUSH REMOTE will be added to the REMOTE PROCEDURE file (#8994) as part of this patch.</p></td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>5/2004</td>
<td>MPI/PD VistA Version 1.0 User Manual released in conjunction with patches MPIF*1*33, RG*1*35 and DG*5.3*589 to support the MPI Changes Iteration 2 project</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>06/2003</td>
<td>MPI/PD VistA Version 1.0 User Manual released in conjunction with patches DG*5.3*505, and MPIF*1*28 of the MPI Changes Iteration I project</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>04/1999</td>
<td>Initial MPI/PD and MPI VistA Technical Manuals were created for release with the MPI/PD V.1.0 software in April 1999.</td>
<td>Master Patient Index team</td>
</tr>
</tbody>
</table>

Patch History

For the current patch history related to this software, please refer to the Patch Module (i.e., Patch User Menu A1AE USER) on FORUM.

  
Contents

Figures

Tables

<span id="_Orientation" class="anchor"></span>  
Orientation

How to Use this Manual

This manual uses several methods to highlight different aspects of the material.

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

<span id="_Toc510587936" class="anchor"></span>Table ii. Documentation Symbol Descriptions

| Symbol                                                                                                     | Description                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/002.png) | NOTE: Used to inform the reader of general information including references to additional reading material. |
| ![](mpi-pd-version-1-vista-technical-manual/003.png)                                                              | CAUTION: Used to caution the reader to take special notice of critical information                          |

- Descriptive text is presented in a proportional font (as represented by this font).
- "Snapshots" of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a non-proportional font and enclosed within a box.
- User's responses to online prompts will be boldface type.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter or Return key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/004.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666."
- Person, patient, and user names will be formatted as follows:

> \[application name\]PERSON,\[fictitious given name\]; \[application name\]PATIENT,\[fictitious given name\]; and \[application name\]USER,\[fictitious given name\] respectively.

> The "fictitious given name" represents a fabricated given name for the patient, person or user. Using a name (rather a number) more clearly represents test data when it’s used in descriptive text in this documentation to convey a concept or comparison. For example: MVIPERSON,SAM; MVIPATIENT,NANCY; MVIUSER,DEBRA, etc.

> NOTE: The business owner, Healthcare Identity Management (HC IdM), requested we use the following nomenclature to represent test data for HC IdM Caseworkers: “HC IdM,CASE WORKER.

Intended Audience/Assumptions

This manual is written with the assumption that the reader is familiar with the VistA computing environment. It is written with the assumption that the reader is familiar with the VistA computing environment. No attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere.

Reference Material

Readers who wish to learn more about the Master Patient Index/Patient Demographic (MPI/PD) software should consult the following VA Web sites:

- VA Software Document Library (VDL) Web site:

> [MPI/PD documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=16)

- The MPI/PD product documentation, as found at the link above, includes the following manuals:
- Master Patient Index/Patient Demographics (MPI/PD) VistA User Manual
- Master Patient Index/Patient Demographics (MPI/PD) VistA HL7 Interface Specifications
- Master Patient Index/Patient Demographics (MPI/PD) VistA Technical Manual
- Master Patient Index/Patient Demographics (MPI/PD) VistA Programmer Manual
- Master Patient Index (MPI) VistA Monograph
- Also see the VistA Duplicate Record Merge manuals listed below, which can be found on the VA Web site:

> [Duplicate Record Merge: Patient Merge documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=2)

- *Duplicate Record Merge: Patient Merge Release Notes for Kernel Toolkit Patch XT\*7.3\*113.*
- *Duplicate Record Merge: Patient Merge User Manual, Version 7.3, Patch XT\*7.3\*113*
- *Duplicate Record Merge: Patient Merge Technical Manual, Version 7.3, Patch XT\*7.3\*113*Installation Information and Procedures

The Master Patient Index and Patient Demographics were distributed and installed together. All installation information and procedures involved with the MPI is included in the *CIRN Patient Demographics (CIRN-PD) Pre-Installation and Implementation Guide v.5* document on the VA Software Document Library Web site:

> [MPI/PD documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=16)

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/005.png) | NOTE: One of the major pre-implementation tasks is the merging of duplicate patient records at a site. The *"Duplicate Record Merge: Patient Merge (Patch XT\*7.3\*23) User Manual"* is required for this task. Patches XT\*7.3\*49, RG\*1\*6, and RG\*1\*10 allow sites with MPI/PD to resolve duplicate records. If you do not have these patches installed, it is recommended that the option to merge patient records be placed out of order. |

Interaction Between MPI/PD and Other Packages

Because of the close interaction between MPI/PD and other packages, you may also find it helpful to review the documentation for the following VistA software:

- VistA HL7 V. 1.6
- PIMS V. 5.3 Admission, Discharge and Transfer (ADT)

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF).

How to Obtain Technical Information Online

Exported VistA M-based file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/006.png) | NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA M-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in VistA character-based software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A, while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text that may be stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about VistA M-based files and their associated fields is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/007.png) | REF: For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Legal DisclaimersSoftware

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Documentation

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Product Description―What Comprises the Master Patient Index Austin?](#product-descriptionwhat-comprises-the-master-patient-index-austin)
  - [Master Patient Index (Austin)](#master-patient-index-austin)
    - [HC IdM Team is Data Steward for the Master Veteran Index (MVI)](#hc-idm-team-is-data-steward-for-the-master-veteran-index-mvi)
  - [Master Patient Index/Patient Demographics (VistA)](#master-patient-indexpatient-demographics-vista)
    - [Requesting an ICN Assignment](#requesting-an-icn-assignment)
  - [Primary View Replaces Obsolete CMOR View](#primary-view-replaces-obsolete-cmor-view)
  - [Systems of Interest to the MVI—Treating Facilities and Non-VistA Systems](#systems-of-interest-to-the-mvitreating-facilities-and-non-vista-systems)
- [Primary View—How are VistA Sites Affected by this Change to the MVI?](#primary-viewhow-are-vista-sites-affected-by-this-change-to-the-mvi)
  - [Primary View Auto-Updates Person Identity Fields in the VistA Patient File (#2)](#primary-view-auto-updates-person-identity-fields-in-the-vista-patient-file-2)
  - [Primary View Identity Traits](#primary-view-identity-traits)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Software Requirements](#software-requirements)
  - [Further Patch Information](#further-patch-information)
  - [Name and Number Spaces](#name-and-number-spaces)
  - [Legal Requirements](#legal-requirements)
  - [HL7 Application Parameters File](#hl7-application-parameters-file)
  - [MPI/PD Mail Groups](#mpipd-mail-groups)
  - [Bulletin](#bulletin)
  - [Background Jobs](#background-jobs)
    - [LOCAL/MISSING ICN RESOLUTION](#localmissing-icn-resolution)
    - [UPDATE BATCH JOB FOR HL7 v2.3](#update-batch-job-for-hl7-v23)
  - [Capacity Management and System Diagnostics](#capacity-management-and-system-diagnostics)
  - [Hardware Requirements](#hardware-requirements)
  - [Auditing](#auditing)
  - [Global Information](#global-information)
  - [Global Configuration](#global-configuration)
  - [Journaling](#journaling)
  - [Routine Mapping](#routine-mapping)
  - [HL7 Management](#hl7-management)
  - [Troubleshooting the RG QUEUE Resource Device](#troubleshooting-the-rg-queue-resource-device)
    - [What is the RG QUEUE Resource Device?](#what-is-the-rg-queue-resource-device)
    - [What RG QUEUE Looks Like in the DEVICE File (#3.5)](#what-rg-queue-looks-like-in-the-device-file-35)
    - [Checking on the RG QUEUE Resource Device](#checking-on-the-rg-queue-resource-device)
    - [How to Tell Your Resource Device Slot Isn't Working Anymore](#how-to-tell-your-resource-device-slot-isnt-working-anymore)
- [Routines](#routines)
  - [Routines in the MPIF Namespace](#routines-in-the-mpif-namespace)
  - [Routines in the RG Namespace](#routines-in-the-rg-namespace)
  - [Routines in the VAFC Namespace](#routines-in-the-vafc-namespace)
- [File List](#file-list)
  - [Files and Globals](#files-and-globals)
    - [PATIENT File (#2) Fields Captured During Edits and Included in HL7 Messages Generated by MPI/PD Applications](#patient-file-2-fields-captured-during-edits-and-included-in-hl7-messages-generated-by-mpipd-applications)
  - [Templates](#templates)
    - [List Templates](#list-templates)
    - [Print Templates](#print-templates)
    - [Sort Templates](#sort-templates)
    - [Input Templates](#input-templates)
- [Exported Options](#exported-options)
  - [MPI/PD Menus and Options](#mpipd-menus-and-options)
    - [MPI/PD Master Menu](#mpipd-master-menu)
    - [MPI/PD Patient Admin Coordinator Menu](#mpipd-patient-admin-coordinator-menu)
    - [MPI/PD IRM Menu](#mpipd-irm-menu)
  - [Menu Assignment](#menu-assignment)
  - [Standalone Options](#standalone-options)
  - [Security Keys](#security-keys)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
- [Callable Routines](#callable-routines)
  - [Supported APIs](#supported-apis)
  - [MVI Direct Connect](#mvi-direct-connect)
- [External Interfaces](#external-interfaces)
  - [HL7 Application Parameters](#hl7-application-parameters)
  - [HL Lower Level Protocol Parameters](#hl-lower-level-protocol-parameters)
  - [Protocols](#protocols)
  - [Remote Procedure Calls (RPCs)](#remote-procedure-calls-rpcs)
- [External Relations](#external-relations)
- [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [Software Product Security](#software-product-security)
- [Glossary](#glossary)
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
<td>![](mpi-pd-version-1-vista-technical-manual/008.png)</td>
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
| ![](mpi-pd-version-1-vista-technical-manual/009.png) | REF: For more information on the VistA DUPLICATE RECORD MERGE release, please refer to Kernel Toolkit Patch XT\*7.3\*113. |
Installation Information
The Master Patient Index VistA and Master Patient Index/Patient Demographics (MPI/PD) were distributed and installed together. All installation information and procedures involved with MPI VistA suite have been referenced in the following MPI/PD documents:
- CIRN Patient Demographics (CIRN-PD) Pre Installation and Implementation Guide V. 5
- Master Patient Index/Patient Demographics (MPI/PD) Installation and Implementation Guide V. 2.
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

# Product Description―What Comprises the Master Patient Index Austin?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Master Patient Index (Austin)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Master Patient Index (MPI) is located at the Austin Information Technology Center (AITC). It is composed of a unique list of persons and an associated list of VAMCs (Veterans Affairs Medical Centers) and other systems of interest where each person has been seen. This enables the sharing of person data between operationally diverse systems. Each person record (or index entry) on the MVI contains multiple demographic fields which are updated to the Primary View of the v.

When a person is first presented into the MVI for an Integration Control Number (ICN) assignment, that person's identifying information (i.e., name, Social Security Number (SSN), date of birth, gender, mother's maiden name, multiple birth indicator, place of birth city and state) is passed to the MVI.

The MVI checks to see if an exact match on Name (first and last), SSN, date of birth, and gender is found. A check is also made to see if the person's internal entry number (DFN) from the querying site is already known to the MVI. If so, this is also considered an exact match. If an exact match is found, the ICN, and ICN Checksum are returned to the requesting site. The requesting site is added to the list of treating facilities (TF) in which this person has been seen and the updated list is broadcasted to all systems of interest, including VAMCs.

If a match is not found, the MVI returns a message indicating this. The patient entry is then added to the MVI. If a potential match is found, a potential match exception is logged for the HC IdM group to review, the person is still added to the MVI.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/010.png) | NOTE: The term "systems of interest" refers to VA facilities that have seen persons and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a person (e.g., Federal Health Information Exchange \[FHIE\], HomeTeleHealth, Person Service Identity Management \[PSIM\], Health Data Repository \[HDR\], etc.). |

### HC IdM Team is Data Steward for the Master Veteran Index (MVI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Healthcare Identity Management (HC IdM) team is the Data Steward for the Master Veteran Index (MVI). The HC IdM team is comprised of analysts who have considerable experience working with the MVI and person data updates. They have the ability to perform the following functions on the Primary View of the MVI:

- View and/or edit the authority values for the Primary View business rules criterion.
- Override Primary View identity traits for selected identity fields in the MPI VETERAN/CLIENT file (#985) and broadcast the new Primary View out to the systems of interest.
- View the Primary View Reject Report from the data in the MPI REJECTED UPDATE file (#985.65).

## Master Patient Index/Patient Demographics (VistA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Master Patient Index/Patient Demographics (MPI/PD) software resides in VistA enabling sites to:

- Request an ICN assignment
- Resolve a potential duplicate on the MVI.
- Query the MVI for known data.
- Update MVI MPI when changes occur to demographic fields stored on the MVI or of interest to other facilities/systems of interest.

### Requesting an ICN Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the initialization of the MVI, each VA Medical Center sent batch HL7 messages to the MVI requesting ICNs for all of its persons whose records reflected activity in the past three fiscal years (i.e., active patient records).

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

<table style="width:97%;">
<colgroup>
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">![](mpi-pd-version-1-vista-technical-manual/011.png)</td>
<td><strong>NOTE:</strong> As of MPI/PD Patch MPIF*1*52, all screens and actions associated with the MPI/PD Exception Handler functionality for resolving Potential Match Exceptions have been removed from MPI/PD. This functionality is now supported in the Identity Management Toolkit.</td>
</tr>
<tr class="even">
<td>![](mpi-pd-version-1-vista-technical-manual/012.png)</td>
<td colspan="2"><p><strong>NOTE</strong>: MPI/PD updates as of VistA Patches MPIF*1*43 and RG*1*43:</p>
<ul>
<li><p>The only times local ICNs are assigned to person records are when:</p></li>
</ul>
<ul>
<li><p>The connection to the MVI cannot be established, or has been lost before the ICN assignment was completed.</p></li>
</ul>
<blockquote>
<p>This happens regardless of which process is used to present the person to the MVI for ICN assignment (i.e., Register a Patient, Load/Edit Patient Data, Electronic 10-10EZ Processing, and/or the Local/Missing ICN Resolution Background Job).</p>
</blockquote>
<ul>
<li><p>The site edits an existing person or adds a new person using an option that doesn't directly interact with the MVI (e.g., VistA Lab or VA FileMan). </p></li>
</ul>
<ul>
<li><p>All existing exceptions that were active in the CIRN HL7 EXCEPTION LOG file (#991.1) of the types listed below, were marked with a status of PROCESSED:</p></li>
</ul>
<ul>
<li><p>Required field(s) missing for person sent to MVI</p></li>
<li><p>SSN Match Failed</p></li>
<li><p>Name Doesn't Match</p></li>
</ul>
<blockquote>
<p>These three exceptions listed are no longer generated. </p>
</blockquote>
<ul>
<li><p>As part of RG*1*43, the View Potential Match Patient [RG EXCEPTION POTENTIAL MATCH] option has been removed from the Message Exception Menu [RG EXCEPTION MENU] as it is obsolete.</p></li>
</ul></td>
</tr>
</tbody>
</table>

The Display Only Query option allows the site to query the MVI to see what the MVI would return if the person was presented for ICN assignment without actually making the request. The person can be an existing person or the user can choose to enter the name, date of birth and SSN (not required) and see what the MVI returns.

|                                                                                                                |                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/013.png) | REF: More information about the "Potential Duplicate PATIENT records found by MPI" message is available via the installation of VistA Kernel Toolkit Patch XT\*7.3\*113. |

## Primary View Replaces Obsolete CMOR View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As part of the MPI Changes Project, Iteration 4, the concept of a "CMOR facility" is being phased out and will be replaced by the Primary View when Patch MPI\*1\*40 is installed on the Austin MPI. VistA Patch MPIF\*1\*44 sets all VistA options related to "CMOR" out of order, rendering them obsolete. The OUT OF ORDER MESSAGE field for these options is marked as "Obsolete with Patch MPIF\*1\*44." Obsolete options will be removed from the Coordinating Master of Record (CMOR) Request \[MPIF CMOR MGR\] menu at a future date.

## Systems of Interest to the MVI—Treating Facilities and Non-VistA Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The term "systems of interest" refers to VA facilities that have seen persons and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a person (e.g., Federal Health Information Exchange \[FHIE\], HomeTeleHealth, Person Service Identity Management \[PSIM\], Health Data Repository \[HDR\], etc.).

A facility's relationship to a person determines what information it receives and sends. MPI/PD stores this information.

Any facility where a person is identified by the same ICN (regardless of VISN) is placed on the Treating Facility List. The list may contain other systems of interest that are not VAMCs (e.g., FHIE and HDR).

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/014.png) | NOTE: The Treating Facility List is utilized by several other VistA applications, including Inter-facility Consults and Remote Data Views in CPRS. |

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
- Patient data is sent to a central system (i.e., the Master Patient Index) to determine validity and quality

This is an enterprise view of the most current data for a person based on authority scoring and the latest data rules. Edits to patient identity traits (listed below) are evaluated based on the same. The highest score achieves the best quality of data updates to the Primary View. These values are stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file).

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

|                                                                                                                |     |                                                                                                                                                                                                                                                                                                                                                                          |     |     |
|----------------------------------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| ![](mpi-pd-version-1-vista-technical-manual/015.png) |     | NOTE: The term "systems of interest" refers to VA facilities that have seen persons and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a person (e.g., Federal Health Information Exchange \[FHIE\], HomeTeleHealth, Person Service Identity Management \[PSIM\], Health Data Repository \[HDR\], etc.). |     |     |
| ![](mpi-pd-version-1-vista-technical-manual/016.png) |     | REF: For a list of the patient identity fields that make up the Primary View on the MVI, see the Appendix titled: "Primary View Identity Traits" in the MPI/PD User Manual.                                                                                                                                                                                              |     |     |
| ![](mpi-pd-version-1-vista-technical-manual/017.png) |     | NOTE: The MPI VETERAN/CLIENT file (#985) comprises the Primary View and is resident on the Austin MPI.                                                                                                                                                                                                                                                                   |     |     |

## Primary View Auto-Updates Person Identity Fields in the VistA Patient File (#2)

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
| ![](mpi-pd-version-1-vista-technical-manual/018.png) | NOTE: The term "auto-update" refers to fields that are updated from a central database (i.e., the Master Patient Index). |

## Primary View Identity Traits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the list of fields that are stored in the Primary View of the MPI.

|                                                                                                                |                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/019.png) | NOTE: Not all Primary View fields are synchronized to the systems of interest. |

<span id="_Ref459808401" class="anchor"></span>Table . Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)

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

Enhanced MPI-to-VistA Synchronization—Additional Patient Identity FieldsSSN Verification Status Synchronized to Systems of Interest

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

|                                                                                                                |                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/020.png) | NOTE: The Duplicate Record Merge: Patient Merge software has already been modified to display the MULTIPLE BIRTH INDICATOR field value if present. |

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
| ![](mpi-pd-version-1-vista-technical-manual/021.png) | NOTE: The MPI FACILITY ASSOCIATION file (#985.5) contains the sites' last update. This correlation should be a duplicate of the same data in the PATIENT file (#2) at the sites. |

Primary View Reject

When person identity fields are edited at VA facilities and sent to the MVI, those edits *must* meet or exceed the existing authority score and pass the Primary View Data Rules on a field-by-field basis. If an edit fails to pass both of these tests, the edit to that person identity field is rejected.

If a site determines that the rejected data is a legitimate edit, the only way to get that data updated on the MVI is to contact the Healthcare Identity Management (HC IdM) team and have them make the edit. HC IdM has the ability to overwrite Primary View data.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](mpi-pd-version-1-vista-technical-manual/022.png)</th>
<th><p>NOTE: Healthcare Identity Management (HC IdM) has requested the removal/deletion of Primary View Rejects (PVRs) and PVR functionality. As of Patch RG*1.0*62:</p>
<ul>
<li><p>Exception #234 (Primary View Reject) were no longer be logged.</p></li>
<li><p>A post-init process executed and marked all existing unresolved 234 exceptions as Resolved.</p></li>
<li><p>The menu option MPI/PD Exception Handling [RG EXCEPTION HANDLING] was removed, since it is no longer needed.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

HC IdM View/Edit Authority Values for Business Rules Criterion

Healthcare Identity Management (HC IdM) staff can view or edit the current authority values for the Primary View business rules criterion. These authority values weigh and score inbound edits to the person entries on the MVI based on person activity at the site.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Master Patient Index/Patient Demographics (MPI/PD) VistA is a Kernel Installation and Distribution System (KIDS) software release.

## Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software (fully patched) *must* be installed at the site:

<span id="_Toc510587938" class="anchor"></span>Table . Applications that need to be installed and fully patched for MPI/PD

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Application</th>
<th>Version # and Patches</th>
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

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/023.png) | CAUTION: DO NOT INSTALL HL\*1.6\*39 in any TEST account! If you install this patch in your test account, you will link your test account to all the other production accounts. Since there are similarities (e.g. patient names/data) in test and production, it would not be good for data from the test account to be transmitted to the production account at another site. |                                                                                                                                                          |
| ![](mpi-pd-version-1-vista-technical-manual/024.png) |                                                                                                                                                                                                                                                                                                                                                                                    | CAUTION: RG\* and MPIF\* patches should NOT be installed on legacy systems to avoid issues with the legacy systems ending up as Treating Facilities. |

## Further Patch Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are facilitating adding the TYPE (#391), PERIOD OF SERVICE (#.323) and VETERAN (Y/N)? (#1901) fields from the PATIENT (#2) file to the MVI. One of the reasons for adding these fields is to provide information to the MVI to assist in the Veteran Identification effort.  This effort is ongoing and this is just the first step in providing that identification.  The TYPE (#391) field will also be used by the MVI to add a new filter rule to the business process for correlating MVI records with DoD DEERS.  The new rule is to prevent the records with the TYPE (#391) field equal to EMPLOYEE from correlating with DoD DEERS.  These were all part of the requirements for MVI Increment 12 and further information can be found on the TSPR web site for the MVI project.

## Name and Number Spaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPI/PD software is made up of two applications:

- RG Namespace—File range is 990–995 and 997–999.99.
- MPIF Namespace—File range is 994.

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software does not impose any additional legal requirements on the user. All users are reminded that many of the reports generated by this software contain confidential patient information and *must* be treated accordingly.

## HL7 Application Parameters File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check that the correct Station Number is entered in the FACILITY NAME field (#3) of the HL7 APPLICATION PARAMETER file (#771), Local modifications to your INSTITUTION file (#4) may conflict with MPI/PD installation setup.

<span id="_Toc510587939" class="anchor"></span>Table . HL7 Application Parameter List

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

## MPI/PD Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510587940" class="anchor"></span>Table . Mail Groups exported in the MPI/PD package

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>Mail Group</th>
<th>Suggested Coordinator</th>
<th>Suggested Members</th>
<th>Description</th>
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
<td>Messages are sent to the remote mail group G.CIRN EXCEPTION MGT@FORUM.VA.GOV, which is the Exception Handler on the MPI in Austin.</td>
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

Exception Mail Groups: MPIF EXCEPTIONS and RG CIRN DEMOGRAPHIC ISSUES

The mail groups MPIF EXCEPTIONS and RG CIRN DEMOGRAPHIC ISSUES are specifically used to receive MPI/PD HL7 Exception Messages. It is important to distinguish the difference between them.

1.  Members of the MPIF EXCEPTIONS mail group are automatically notified of technical type problems (e.g., such as data update failures or problems with HL7 messages causing them not to be processed). Messages are sent to the remote mail group G.CIRN EXCEPTION MGT@FORUM.VA.GOV, which is the Exception Handler on the MPI in Austin. There shouldn’t be any local members in this mail group.
2.  The RG CIRN DEMOGRAPHIC ISSUES mail group is exported with MPI/PD. Members of this mail group are automatically notified of problems relating to data.

> It is recommended that PIMS personnel (i.e., ADPACs and/or Coordinators, etc.) be made members of this mail group.

|                                                                                                                |                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/025.png) | REF: For information on assigning members to mail groups, [see the MailMan User Manual V. 8.0. of the VDL](http://www.va.gov/vdl/application.asp?appid=15). |

## Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RG CIRN DEMOGRAPHIC ISSUES bulletin controls the sending of the following patient related bulletin, Table 5.

<span id="_Ref408490888" class="anchor"></span>Table . RG CIRN DEMOGRAPHIC ISSUES bulletin REMOTE SENSITIVITY INDICATED

|                              |                                                                               |                                     |
|------------------------------|-------------------------------------------------------------------------------|-------------------------------------|
| Patient Related Bulletin     | Cause                                                                         | Action to take                      |
| REMOTE SENSITIVITY INDICATED | Patient is marked as sensitive at the sending site but not at receiving site. | No action: message is informational |

## Background Jobs

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
<td>![](mpi-pd-version-1-vista-technical-manual/026.png)</td>
<td><p><strong>NOTE:</strong> As of Patch MPI*1*38 (MPI Austin side for the MPIF*1*43 and RG*1*43), this background job no longer automatically adds patients to the MVI.</p>
<p>Previous to the release of this patch, when the Local/Missing ICN Resolution job was processed on the MVI, if a match wasn't found, the patient was added immediately. As of Patch MPI*1*38, this functionality has been changed in that if a match for a person isn't found on the MVI, a message is sent back to the site indicating this. On the site's side, this triggers an HL7 A28—Add Patient message, which then adds the person to the MVI.</p></td>
</tr>
<tr class="even">
<td>![](mpi-pd-version-1-vista-technical-manual/027.png)</td>
<td><strong>NOTE:</strong> A new field, LOCAL/MISSING DATE LAST RAN (#.04), was created in the CIRN SITE PARAMETER file (#991.8) to hold the last date the Local/Missing ICN Resolution Background job ran. The field will be populated by the routine ^MPIFRES.</td>
</tr>
</tbody>
</table>

Local ICNs

ICNs are created for new person locally at the site when the MVI is unavailable or when the connection is lost prior to the assignment an ICN (e.g., the Direct Connect could not be established). A local ICN is also assigned as a placeholder when a person has been sent to the MVI but not yet added. This is to ensure identification of this person as these records await a response from the MPI. Local ICNs look like a national ICN. They contain the same number of digits as a national ICN. The only difference is that the first three digits are the VAMCs station number.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/028.png) | NOTE: It is not recommended that local ICNs be sent to remote databases as they will only be known at the local facility that assigned them. |

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

The event of updating patient information can take place from several different options within VistA, including VA FileMan. Changes to any of the fields listed in Table 6 are recorded and an entry is created in the ADT/HL7 PIVOT file (#391.71). The entry is then marked as pending transmission. Direct sets to the globals cannot be collected. This background job will periodically collect (via a scheduled job) these marked events and broadcast an ADT-A08 Update Patient Information message. Because it is not possible to determine if the editing of the field is complete, this background job will periodically collect these marked events and broadcast an ADT A08 message (i.e., Update Patient Information). This is a PIMS-generated HL7 message.

<span id="_Ref459808723" class="anchor"></span>Table . Data elements monitored in the PATIENT file (#2) for changes

| Field Number | Field Name                    |
|--------------|-------------------------------|
| 2,.01        | NAME                          |
| 2,.02        | SEX                           |
| 2,.024       | SELF IDENTIFIED GENDER        |
| 2,.03        | DATE OF BIRTH                 |
| 2,.05        | MARITAL STATUS                |
| 2,.08        | RELIGIOUS PREFERENCE          |
| 2,.09        | SOCIAL SECURITY NUMBER        |
| 2,.0931      | PLACE OF BIRTH COUNTRY        |
| 2,.0932      | PLACE OF BIRTH PROVINCE       |
| 2,.111       | STREET ADDRESS \[LINE 1\]     |
| 2,.1112      | ZIP+4                         |
| 2,.112       | STREET ADDRESS \[LINE 2\]     |
| 2,.113       | STREET ADDRESS \[LINE 3\]     |
| 2,.114       | CITY                          |
| 2,.115       | STATE                         |
| 2,.116       | ZIP CODE                      |
| 2,.117       | COUNTY                        |
| 2,.1171      | PROVINCE                      |
| 2,.1172      | POSTAL CODE                   |
| 2,.1172      | COUNTRY                       |
| 2,.121       | BAD ADDRESS INDICATOR         |
| 2,.131       | PHONE NUMBER \[RESIDENCE\]    |
| 2,.132       | PHONE NUMBER \[WORK\]         |
| 2,.133       | EMAIL ADDRESS                 |
| 2,.134       | PHONE NUMBER \[CELLULAR\]     |
| 2,.211       | K-NAME OF PRIMARY NOK         |
| 2,.219       | K-PHONE NUMBER                |
| 2,.2403      | MOTHER'S MAIDEN NAME          |
| 2,.2405      | PREFERRED NAME                |
| 2,.301       | SERVICE CONNECTED?            |
| 2,.302       | SERVICE CONNECTED PERCENTAGE  |
| 2,.31115     | EMPLOYMENT STATUS             |
| 2,.313       | CLAIM NUMBER                  |
| 2,.323       | PERIOD OF SERVICE             |
| 2,.351       | DATE OF DEATH                 |
| 2,.352       | DEATH ENTERED BY              |
| 2,.353       | SOURCE OF NOTIFICATION        |
| 2,.354       | DATE OF DEATH LAST UPDATED    |
| 2,.355       | LAST EDITED BY                |
| 2,.357       | SUPPORTING DOCUMENT TYPE      |
| 2,.361       | PRIMARY ELIGIBILITY CODE      |
| 2,.525       | POW STATUS INDICATED?         |
| 2,2          | RACE INFORMATION              |
| 2,6          | ETHNICITY INFORMATION         |
| 2,391        | TYPE                          |
| 2,991.01     | INTEGRATION CONTROL NUMBER    |
| 2,991.02     | ICN CHECKSUM                  |
| 2,991.03     | COORDINATING MASTER OF RECORD |
| 2,991.04     | LOCALLY ASSIGNED ICN          |
| 2,991.05     | SUBSCRIPTION CONTROL NUMBER   |
| 2,991.06     | CMOR ACTIVITY SCORE           |
| 2,991.07     | SCORE CALCULATION DATE        |
| 2,991.08     | TEMPORARY ID NUMBER           |
| 2,991.09     | FOREIGN ID NUMBER             |
| 2,991.1      | FULL ICN                      |
| 2,994        | MULTIPLE BIRTH INDICATOR      |
| 2,1901       | VETERAN (Y/N)?                |
| 2.01,.01     | ALIAS                         |
| 2.01,1       | ALIAS SSN                     |
| 2.0991,.01   | FULL ICN HISTORY              |
| 2.0992,.01   | ICN HISTORY                   |

This background job also sends out Treating Facility "add me" and Treating Facility Update messages.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-technical-manual/029.png)</td>
<td><p><strong>REF:</strong> For more information on the ADT A08 Message- Update Patient Information, see the <em>Master Patient Index (MPI) VistA HL7 Interface Specifications</em> at the following VA Web site:</p>
<p><a href="http://www.va.gov/vdl/application.asp?appid=16">MPI/PD documentation on the VA Software Documentation Web site</a></p></td>
</tr>
<tr class="even">
<td>![](mpi-pd-version-1-vista-technical-manual/030.png)</td>
<td><strong>NOTE:</strong> This background job was originally exported in patch DG*5.3*91.</td>
</tr>
</tbody>
</table>

## Capacity Management and System Diagnostics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Management team will work closely with sites to determine whether the workload associated with MPI/PD will affect the system negatively. They have also developed a number of tools that monitor the system to provide benchmarking data for further study and process improvement. These may include the following:

- Statistical Analysis of Global Growth (SAGG) - focuses on package-specific impact on data storage, monitors global and file usage.
- Resource Usage Monitor (RUM) - measures resource consumption by package.
- VAX Performance Analyzer (VPM) - monitors system and stores a key subset of data associated with configuration, database activity, response time, central processing unit (CPU), memory, and Input/Output (I/O) utilization.

The following system diagnostics should also be performed:

Transmission Control Protocol/Internet Protocol (TCP/IP) Testing: For the Digital Equipment Corporation (DEC) Alpha sites which were not old 486 sites, test the TCP/IP connection via a "PING" function or other method. This insures that the software and hardware mechanisms associated with this communications protocol are prepared to function. It is also a preventive diagnostic for communications with the MPI Austin.

## Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MPI/PD is designed to run on standard or upgraded Alpha AXP clusters with Virtual Memory System (VMS) or on New Technology (NT) and Open M. TCP/IP setups will have to be in place.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-technical-manual/031.png)</td>
<td><p><strong>NOTE:</strong> See VistA Health Level Seven (HL7) <em>Site Manager and Developer Manual</em> at the VA Web site:</p>
<p><a href="http://www.va.gov/vdl/application.asp?appid=8">HL7 (VistA Messaging) on the VA Software Documentation Web site</a></p></td>
</tr>
</tbody>
</table>

MPI/PD uses TCP/IP as the communications protocol for transmitting and receiving patient information. Use existing system tools for fine-tuning your TCP/IP capabilities.

## Auditing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*149 added new cross references to the PATIENT file (#2) fields to assist MPI/PD in monitoring changes made to the fields listed below. During the normal daily operations of MPI/PD, it is possible that these fields may be updated by HL7 Messaging. Patch DG\*5.3\*231 exported with MPI/PD build, enables auditing for the following fields for monitoring. These fields are the minimal set of fields that should be turned on for auditing in the PATIENT file (#2) for MPI/PD. They are listed numerically by field number.

<span id="_Ref475536823" class="anchor"></span>Table . Fields that should be turned on for auditing in the PATIENT file (#2) for MPI/PD

| Field Number                                                                                                   |     | Field Name                                                                                                                                                                                         |     |     |
|----------------------------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| 2,.01                                                                                                          |     | \*\* NAME                                                                                                                                                                                          |     |     |
| 2,.02                                                                                                          |     | \*\* SEX                                                                                                                                                                                           |     |     |
| 2,.024                                                                                                         |     | SELF IDENTIFIED GENDER                                                                                                                                                                             |     |     |
| 2,.03                                                                                                          |     | \*\* DATE OF BIRTH                                                                                                                                                                                 |     |     |
| 2,.05                                                                                                          |     | MARITAL STATUS                                                                                                                                                                                     |     |     |
| 2,.08                                                                                                          |     | RELIGIOUS PREFERENCE                                                                                                                                                                               |     |     |
| 2,.09                                                                                                          |     | \*\* SOCIAL SECURITY NUMBER                                                                                                                                                                        |     |     |
| 2,.092                                                                                                         |     | PLACE OF BIRTH \[CITY\]                                                                                                                                                                            |     |     |
| 2,.093                                                                                                         |     | PLACE OF BIRTH \[STATE\]                                                                                                                                                                           |     |     |
| 2,.0931                                                                                                        |     | PLACE OF BIRTH COUNTRY                                                                                                                                                                             |     |     |
| 2,.0932                                                                                                        |     | PLACE OF BIRTH PROVINCE                                                                                                                                                                            |     |     |
| 2,.111                                                                                                         |     | STREET ADDRESS \[LINE 1\]                                                                                                                                                                          |     |     |
| 2,.1112                                                                                                        |     | ZIP+4                                                                                                                                                                                              |     |     |
| 2,.112                                                                                                         |     | STREET ADDRESS \[LINE 2\]                                                                                                                                                                          |     |     |
| 2,.113                                                                                                         |     | STREET ADDRESS \[LINE 3\]                                                                                                                                                                          |     |     |
| 2,.114                                                                                                         |     | CITY                                                                                                                                                                                               |     |     |
| 2,.115                                                                                                         |     | STATE                                                                                                                                                                                              |     |     |
| 2,.116                                                                                                         |     | ZIP CODE                                                                                                                                                                                           |     |     |
| 2,.117                                                                                                         |     | COUNTY                                                                                                                                                                                             |     |     |
| 2,.1171                                                                                                        |     | PROVINCE                                                                                                                                                                                           |     |     |
| 2,.1172                                                                                                        |     | POSTAL CODE                                                                                                                                                                                        |     |     |
| 2,.1172                                                                                                        |     | COUNTRY                                                                                                                                                                                            |     |     |
| 2,.121                                                                                                         |     | BAD ADDRESS INDICATOR                                                                                                                                                                              |     |     |
| 2,.131                                                                                                         |     | PHONE NUMBER \[RESIDENCE\]                                                                                                                                                                         |     |     |
| 2,.132                                                                                                         |     | PHONE NUMBER \[WORK\]                                                                                                                                                                              |     |     |
| 2,.133                                                                                                         |     | EMAIL ADDRESS                                                                                                                                                                                      |     |     |
| 2,.134                                                                                                         |     | PHONE NUMBER \[CELLULAR\]                                                                                                                                                                          |     |     |
| 2,.211                                                                                                         |     | K-NAME OF PRIMARY NOK                                                                                                                                                                              |     |     |
| 2,.219                                                                                                         |     | K-PHONE NUMBER                                                                                                                                                                                     |     |     |
| 2,.2403                                                                                                        |     | \*\* MOTHER'S MAIDEN NAME                                                                                                                                                                          |     |     |
| 2,.2405                                                                                                        |     | PREFERRED NAME                                                                                                                                                                                     |     |     |
| 2,.301                                                                                                         |     | SERVICE CONNECTED?                                                                                                                                                                                 |     |     |
| 2,.302                                                                                                         |     | SERVICE CONNECTED PERCENTAGE                                                                                                                                                                       |     |     |
| 2,.31115                                                                                                       |     | EMPLOYMENT STATUS                                                                                                                                                                                  |     |     |
| 2,.313                                                                                                         |     | CLAIM NUMBER                                                                                                                                                                                       |     |     |
| 2,.323                                                                                                         |     | PERIOD OF SERVICE                                                                                                                                                                                  |     |     |
| 2,.351                                                                                                         |     | DATE OF DEATH                                                                                                                                                                                      |     |     |
| 2,.352                                                                                                         |     | DEATH ENTERED BY                                                                                                                                                                                   |     |     |
| 2,.353                                                                                                         |     | SOURCE OF NOTIFICATION                                                                                                                                                                             |     |     |
| 2,.354                                                                                                         |     | DATE OF DEATH LAST UPDATED                                                                                                                                                                         |     |     |
| 2,.355                                                                                                         |     | LAST EDITED BY                                                                                                                                                                                     |     |     |
| 2,.357                                                                                                         |     | SUPPORTING DOCUMENT TYPE                                                                                                                                                                           |     |     |
| 2,.358                                                                                                         |     | DATE OF DEATH OPTION USED                                                                                                                                                                          |     |     |
| 2,.361                                                                                                         |     | PRIMARY ELIGIBILITY CODE                                                                                                                                                                           |     |     |
| 2,.525                                                                                                         |     | POW STATUS INDICATED?                                                                                                                                                                              |     |     |
| 2,2                                                                                                            |     | RACE INFORMATION                                                                                                                                                                                   |     |     |
| 2,6                                                                                                            |     | ETHNICITY INFORMATION                                                                                                                                                                              |     |     |
| 2,391                                                                                                          |     | TYPE                                                                                                                                                                                               |     |     |
| 2,991.01                                                                                                       |     | INTEGRATION CONTROL NUMBER                                                                                                                                                                         |     |     |
| 2,991.02                                                                                                       |     | ICN CHECKSUM                                                                                                                                                                                       |     |     |
| 2,991.03                                                                                                       |     | COORDINATING MASTER OF RECORD                                                                                                                                                                      |     |     |
| 2,991.04                                                                                                       |     | LOCALLY ASSIGNED ICN                                                                                                                                                                               |     |     |
| 2,991.05                                                                                                       |     | SUBSCRIPTION CONTROL NUMBER                                                                                                                                                                        |     |     |
| 2,991.06                                                                                                       |     | CMOR ACTIVITY SCORE                                                                                                                                                                                |     |     |
| 2,991.07                                                                                                       |     | SCORE CALCULATION DATE                                                                                                                                                                             |     |     |
| 2,991.08                                                                                                       |     | TEMPORARY ID NUMBER                                                                                                                                                                                |     |     |
| 2,991.09                                                                                                       |     | FOREIGN ID NUMBER                                                                                                                                                                                  |     |     |
| 2,991.1                                                                                                        |     | FULL ICN                                                                                                                                                                                           |     |     |
| 2,994                                                                                                          |     | MULTIPLE BIRTH INDICATOR                                                                                                                                                                           |     |     |
| 2,1901                                                                                                         |     | VETERAN (Y/N)?                                                                                                                                                                                     |     |     |
| 2.01,.01                                                                                                       |     | ALIAS                                                                                                                                                                                              |     |     |
| 2.01,1                                                                                                         |     | ALIAS SSN                                                                                                                                                                                          |     |     |
| 2.0991,.01                                                                                                     |     | FULL ICN HISTORY                                                                                                                                                                                   |     |     |
| 2.0992,.01                                                                                                     |     | ICN HISTORY                                                                                                                                                                                        |     |     |
| ![](mpi-pd-version-1-vista-technical-manual/032.png) |     | NOTE: The double asterisks (\*\*) denote key fields (in addition to Name and the fields mentioned above) that will be synchronized across sites. This list of key fields is subject to change. |     |     |
| ![](mpi-pd-version-1-vista-technical-manual/033.png) |     | NOTE: The DG SECURITY LOG file (#38.1), Field \#2 Security Level is also monitored for changes to patient sensitivity.                                                                         |     |     |

## Global Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Globals that were included in the installation of MPI/PD are shown in the File List.

The following globals need to be placed on the system:

- ^RG\* (^RGSITE, ^RGHL7 ^RGEQASN, ^RGEQEXC, ^RGSTAT, ^RGEQ) - minimal anticipated growth
- ^MPIF - no anticipated growth

You will need to reboot your system for translations to take effect.

Check disk space for 150 Mb of available space for growth in ^HL Based on Test Site information, projected growth of the ^DIA (audit global) is 400-500Mb over a one year period.

## Global Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open M: Use the GUI Global Utility to add and place the globals. Default global attributes should be used.

<span id="_Toc510587944" class="anchor"></span>Table . Global Configuration of Alpha (DSM) and Open M

|            |              |       |       |              |
|------------|--------------|-------|-------|--------------|
|            | System Owner | World | Group | UCI/USER NET |
| Open M | RWD          | R     | R     | RWD          |

## Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Journaling should be off during the installation but should be enabled afterwards for ^RG\* and ^MPIF\*.

|                                                                                                                |                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/034.png) | NOTE: HL\*1.6\*52 has recommendations for HL7 global journaling that should be reviewed. The MPI/PD heavily uses HL7 messaging. |

## Routine Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several templates associated with the PATIENT file (#2) were compiled during DG\*5.3\*231 portion of the MPI/PD installation. If any of the following routine namespaces are mapped at your site, they should be unmapped prior to starting the installation. If your site cannot map/unmap using the \* wildcard, a complete list of the mapped/unmapped routines can be found in Appendix I of the *Master Patient Index/Patient Demographics (MPI/PD) Installation and Implementation Guide.*

- A1CKC\*
- DGRPTX\*
- DGRPXCR\*
- DVBAXA\*
- DVBHCG\*
- GMRDSTV\*
- IBXSC1\*
- MCARORB\*
- TIUPREL\*
- DGPTX1\*
- DGRPXC\*
- DGRPXX7\*
- DVBHCE\*
- GMRDSTR\*
- IBXBCR2\*
- IBXSC2\*
- SDM1T\*

## HL7 Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MPI/PD makes heavy use of HL7 messaging. The HL7 globals should be checked for sufficient room for growth. In addition, check to see if the HL7 patch, HL\*1.6\*39, properly brought in all of the sites HL LOGICAL LINK file (#870) and set the Queue Size field (#21) to ten. In addition, each site that is running UCX (non-Caché) will need to change their sites (VA\<your site's three-letter abbreviation\> TCP) HL LOWER LEVEL PROTOCOL PARAMETER file (#869.2) entry, field TCP/IP Service Type (#400.03) to M for Multi Listener Server.

|                                                                                                                |                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/035.png) | REF: See Patch HL\*1.6\*19 for further instructions. |

## Troubleshooting the RG QUEUE Resource Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### What is the RG QUEUE Resource Device?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entry RG QUEUE in the DEVICE file (#3.5) was created by the post-installation routine, RGP26PST in patch RG\*1.0\*26.  This device is used to limit the number of background jobs running on the system at any given time. The RG ADT-A08 TRIGGER and RG ADT-A04 TRIGGER HL7 client protocols hang off of the VAFC ADT-A04/A08 SERVER HL7 server protocols and are used to capture patient events and queue up a subsequent HL7 message.  This message follows the new Health Level Seven (HL7) Standard v2.4, which also includes "commit" and "application" level acknowledgements.  Since the potential exists for an unlimited number of patient edits to be queued off at any given time from a backlog in the ADT HL7 PIVOT file (#391.71), this resource device prevents more than 10 jobs from running at any given time.

### What RG QUEUE Looks Like in the DEVICE File (#3.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: RG QUEUE                          \$I: RG QUEUE

  RESOURCE SLOTS: 10                    OPEN COUNT: 858195

  TYPE: RESOURCES

### Checking on the RG QUEUE Resource Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have had a system problem that resulted in an unexpected down time, you might have had entries processing on the RG QUEUE resource device.  To check, use the Monitor Taskman option to see if you have tasks waiting for device.  If you have entries waiting for RG QUEUE, continue to monitor, they shouldn't stay there long.  If they do, you might have a resource device slot with a job that is no longer running.

### How to Tell Your Resource Device Slot Isn't Working Anymore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Get a display of the RESOURCE file (#3.54) for the RG QUEUE device. 

NAME: RG QUEUE                          AVAILABLE SLOTS: 0

SLOT IN USE: 1                          CPU/VOL: ROU

  JOB \#: 543752250                      TASK \#: 2796349

  START TIME: 61598,40492

Up to 10 tasks and job numbers may be listed here.  Use the TaskMan Management utility to List Tasks and determine if any of these jobs still exist and are active.  If they are, then that slot is okay if they aren't active jobs then that slot needs to be cleared.  To clear slots, use the Clear all resources option or Clear one Resource option from the Device Management menu.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](mpi-pd-version-1-vista-technical-manual/036.png)</th>
<th><p><strong>REF:</strong> For more information on the use of these options, refer to the Kernel Systems Management Guide on the VA Web site:</p>
<p><a href="http://www.va.gov/vdl/application.asp?appid=10">Kernel documentation on the VA Software Documentation Web site</a></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines distributed with MPI/PD are broken down according to the namespace of the patch they were released with. The routines for the following namespaces: MPIF, Table 9, RG, Table 10, and VAFC, Table 11 are listed on the following pages.

|                                                                                                                |                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/037.png) | REF: For more information on related DG routines and patches, please refer to the Patch User Menu on FORUM. |

## Routines in the MPIF Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref75591437" class="anchor"></span>Table . VistA routines (MPIF namespace)

| MPIF Routine Name | Description                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------|
| MPIF001           | APIs for ICN, IEN, CMOR Information                                                                                                |
| MPIF002           | APIs for ICN, IEN, CMOR information, continued                                                                                     |
| MPIFA24           | A24 processing routine—Process A24 resulting from A28 add to MPI message or from A40 Merge                                         |
| MPIFA24B          | Build A24 ADD ME Messages                                                                                                          |
| MPIFA28           | Build A28 ADD ME Messages                                                                                                          |
| MPIFA31B          | Build A31 Messages                                                                                                                 |
| MPIFA31I          | Process ADT A31 message from API                                                                                                   |
| MPIFA37           | Utility for processing an ADT-A37 Un-link ID                                                                                       |
| MPIFA40           | BUILD A40 Merge message                                                                                                            |
| MPIFA43           | Utility for processing an ADT-A43 Un-link ID                                                                                       |
| MPIFACHK          | Acknowledgement check                                                                                                              |
| MPIFAPI           | APIs for local ICNs                                                                                                                |
| MPIFAPI1          | APIS for local ICNs, continued                                                                                                     |
| MPIFAREQ          | This routine will automatically process any CMOR Change Request still pending review as approved.                                  |
| MPIFBT1           | Batch query to MPI                                                                                                                 |
| MPIFBT2           | Batch response from MPI                                                                                                            |
| MPIFBT3           | Batch response from MPI                                                                                                            |
| MPIFCMOR          | Set and broadcast CMOR changes                                                                                                     |
| MPIFCMRP          | Push CMOR for patient to another site                                                                                              |
| MPIFD1            | Potential duplicate on the MPI                                                                                                     |
| MPIFDEL           | Delete Patient from MPI.                                                                                                           |
| MPIFDNL           | New Routine as of Patch MPIF\*1\*52, used to add or inactivate an entry on the MPI DO NOT LINK file (#985.28).                     |
| MPIFDUP           | RESOLVE DUP ACTION                                                                                                                 |
| MPIFDUPS          | MPIF RPC APIS                                                                                                                      |
| MPIFEDIT          | Request a CMOR for patient                                                                                                         |
| MPIFEXT           | EXTENDED PDAT - RPC                                                                                                                |
| MPIFEXT2          | EXTENDED PDAT - RPC                                                                                                                |
| MPIFEXT3          | EXTENDED PDAT 3 - RPC                                                                                                              |
| MPIFFULL          | ALLOW ASSIGNMENT OF LOCAL ICNS FOR X PATIENTS                                                                                      |
| MPIFHL7           | Processing incoming HL7 messages                                                                                                   |
| MPIFMER           | Merge patient ICN                                                                                                                  |
| MPIFNEW           | This routine adds a new request for change of CMOR to File \#984.9.                                                                |
| MPIFNQ            | Miscellaneous functions for CMOR                                                                                                   |
| MPIFP48           | POST-INT for MPIF\*1\*48                                                                                                           |
| MPIFP54           | BIRM/CMC-POST INIT FOR MPIF\*1\*54                                                                                                 |
| MPIFP60           | MPI VISTA POST-INIT MPIF\*1\*60                                                                                                    |
| MPIFQ0            | CIRN Query Handler top level                                                                                                       |
| MPIFQ1            | CIRN Query Handler, continued                                                                                                      |
| MPIFQ3            | QUERY List Manager functions                                                                                                       |
| MPIFQED           | Add patient returned in query                                                                                                      |
| MPIFQUE3          | Generate Batch message for comparison of CMOR score                                                                                |
| MPIFQUE4          | Process the CMOR COMPARISON request                                                                                                |
| MPIFQUE5          | Process the RESULT from CMOR COMPARISON request                                                                                    |
| MPIFRCMP          | CMOR push to another site remotely via RPC                                                                                         |
| MPIFREQ           | Process a CMOR request from Event Queue                                                                                            |
| MPIFRES           | Batch processing to the MPI of locally assigned ICNs and patients added to the PATIENT file (#2) by means other than PIMS options. |
| MPIFRESS          | Process approve/disapprove CMOR change requests.                                                                                   |
| MPIFREV           | Review CMOR Request.                                                                                                               |
| MPIFRPC2          | RPC to Single Patient Initialization on patient with SSN                                                                           |
| MPIFRPC3          | RPC to return primary patient record                                                                                               |
| MPIFRTC           | This routine is used during the real-time connection with the MPI to send an HL7 message to add a patient to the MPI.              |
| MPIFSA2           | Stand Alone Query Part 2                                                                                                           |
| MPIFSA3           | Stand Alone Query Part 2                                                                                                           |
| MPIFSAQ           | Stand-alone query                                                                                                                  |
| MPIFSEED          | Seeding of A31s to MPI and sub cleanup                                                                                             |
| MPIFSPC           | This routine computes the checksum for a given ICN.                                                                                |
| MPIFUTL           | CMOR Utilities                                                                                                                     |
| MPIFVTQ           | Build data to query MPI response process (ADDPAT)                                                                                  |

## Routines in the RG Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref75591460" class="anchor"></span>Table . VistA routines (RG namespace)

| RG Routine Name | Description                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------|
| RGACTIV         | MPI/PD patient activity information                                                                        |
| RGADT           | ADT message processing/routing                                                                             |
| RGADT1          | TFL file seeding routine (PD-MPI LOAD)                                                                     |
| RGADT2          | TFL file seeding routine (PD-MPI LOAD)                                                                     |
| RGADTP          | ADT processor to retrigger A08 or A04 messages with AL/AL (Commit/Application) Acknowledgements            |
| RGADTP1         | ADT processor to retrigger A08 or A04 messages with AL/AL (COMMIT/APPLICATION) Acknowledgements, continued |
| RGADTP2         | ADT processor to retrigger A08 or A04 messages with AL/AL (COMMIT/APPLICATION) Acknowledgements, continued |
| RGADTP3         | RGADTP2, continued                                                                                         |
| RGADTPC         | Continuation of RGADTP routine                                                                             |
| RGADTUT         | Utility; determine patient subscriptions (A01/A03)                                                         |
| RGEQDMN         | Dequeue processor                                                                                          |
| RGEQDMN1        | Dequeue processor, continued                                                                               |
| RGEQEXC         | Error processor                                                                                            |
| RGEQSTAT        | Statistics                                                                                                 |
| RGEQSUB         | Dequeue processor                                                                                          |
| RGEVPRG         | Options to purge MPI/PD exceptions                                                                         |
| RGEX01          | List Manager for MPI/PD exceptions                                                                         |
| RGEX03          | List Manager for MPI/PD exceptions                                                                         |
| RGEX04          | List Manager routine for MPI/PD Exception PDAT Query                                                       |
| RGEX05          | List Manager routine for Remote PDAT in Exception Handler                                                  |
| RGEX06          | List Manager routine for remote PMI Primary View PDAT                                                      |
| RGEX07          | List Manager routine for remote Primary View display                                                       |
| RGEXHND1        | MPI/PD Exception Handling utility                                                                          |
| RGFIACK         | Process Application Acknowledgment                                                                         |
| RGFIBM          | Send facility integration message                                                                          |
| RGFICLN         | MPI/PD NDBI site cleanup utility                                                                           |
| RGFIPM          | Process facility integration message                                                                       |
| RGFIPM1         | Process Facility Integration Message                                                                       |
| RGFIRM          | Route Facility Integration Message                                                                         |
| RGFIU           | MPI/PD NDBI Merge Utility, continued                                                                       |
| RGHLLOG         | Log message processing information                                                                         |
| RGHLLOG1        | Send exception to MPI Exception Handler                                                                    |
| RGHLUT          | HL7 message processing utilities                                                                           |
| RGJCREC         | MPI/PD subscription processor                                                                              |
| RGJCSTAT        | CIRN interface receiver of QRY message                                                                     |
| RGJCSUB         | MPI/PD subscription generator                                                                              |
| RGJCTS01        | Subscription Control Startup Utility To CMOR                                                               |
| RGJUSITE        | Routine to hold API for the CIRN PARAMETER file (#991.8)                                                   |
| RGMTAUD         | CIRN Audit file Print for a Specified Patient                                                              |
| RGMTAUDP        | CIRN Audit file Print of Patient Data                                                                      |
| RGMTDPCT        | Count Entries for ^DPT in Dup Record file                                                                  |
| RGMTDPSC        | Count duplicate record entries by CMOR score range                                                         |
| RGMTETOT        | Compile totals for site exceptions                                                                         |
| RGMTHFS         | Build HFS file for capturing report data                                                                   |
| RGMTHL2         | Compile MPI/PD HL7 data for bi-directional TCP                                                             |
| RGMTHLDB        | MPI/PD HL7 ACTIVITY by patient/single protocol                                                             |
| RGMTHLDP        | MPI/PD HL7 ACTIVITY by patient/all protocols                                                               |
| RGMTHLP         | MPI/PD HL7 Message Status Report                                                                           |
| RGMTHLPD        | MPI/PD HL7 Message Status Report (detailed)                                                                |
| RGMTMONT        | MPI/PD Monitor HL7 Messaging/Filers and Setups                                                             |
| RGMTMONX        | MPI/PD Monitor HL7 Messaging/Filers and Setups (CONT)                                                      |
| RGMTRUN         | SCAN TaskMan running HL7 tasks                                                                             |
| RGMTSTAT        | MPI/PD maintenance query                                                                                   |
| RGMTUT01        | MPI/PD Compile and Correct Data Validation Data for Local Sites                                            |
| RGMTUT02        | MPI/PD Compile and Correct Data Validation Data for Local Sites (CON'T)                                    |
| RGMTUT03        | MPI/PD Compile and Correct Data Validation Data for Local Sites (CON'T)                                    |
| RGMTUT98        | Misc. MPI Load COUNTER Utilities                                                                           |
| RGP62PST        | POST-INIT TO RETIRE \#234 EXCEPTIONS                                                                       |
| RGPOC           | ADD/EDIT POINT OF CONTACT OPTION                                                                           |
| RGPOC1          | ADD/EDIT POINT OF CONTACT OPTION - CONTINUED                                                               |
| RGPRSSN         | CIRN Pseudo/Missing SSN Report                                                                             |
| RGPVMPI         | Remote Primary View display from MPI                                                                       |
| RGPVREJ         | Remote Primary View reject (patient)                                                                       |
| RGRAS           | CIRN PRE-SEEDING REPORT FOR TREATING FACILITY UPDATE                                                       |
| RGRPC           | RG RPC API                                                                                                 |
| RGRPDAT         | ROUTINE TO CALL REMOTE PDAT                                                                                |
| RGRSBULL        | RGRSTEXT Bulletin routine                                                                                  |
| RGRSBULL1       | RGRSTEXT BULLETIN ROUTINE (PART 2)                                                                         |
| RGRSDYN         | Build dynamic link list for a patient                                                                      |
| RGRSDYN1        | Build dynamic link list for a TFU                                                                          |
| RGRSDYN2        | Build dynamic link list for sensitivity                                                                    |
| RGRSENS         | Pt sensitivity parser/filer                                                                                |
| RGRSMSH         | Registration message parser for CIRN                                                                       |
| RGRSPAR1        | Registration message parser for CIRN TFU                                                                   |
| RGRSPAR2        | Sensitivity message parser for CIRN                                                                        |
| RGRSPARM        | Edit SEND/STOP/SUSPEND parameter                                                                           |
| RGRSPARS        | Registration message parser for CIRN                                                                       |
| RGRSPT          | High level routine for parsing and filing                                                                  |
| RGRSUTIL        | CIRN Utilities                                                                                             |
| RGRSUTL2        | Utilities for CIRN                                                                                         |
| RGRSZZPT        | Utility for CIRN                                                                                           |
| RGSYSTAT        | MPI/PD status display                                                                                      |
| RGVCCMR1        | CIRN CMOR activity score generator (part 1)                                                                |
| RGVCCMR2        | CIRN CMOR activity score generator (part 2)                                                                |

## Routines in the VAFC Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref130182757" class="anchor"></span>Table . VistA routines (VAFC namespace)

| VAFC Routine Name | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VAFCA04           | Creates the Registration Message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| VAFCAAUT          | ASSIGNING AUTHORITY FILE (#391.92) Utilities                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| VAFCAUD           | MPI/PD AUDIT FILE PRINT FOR A SPECIFIED PATIENT                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VAFCHFS           | BUILD HFS FILE FOR CAPTURING REPORT DATA                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| VAFCHIS           | TESTING CROSS REFERENCE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VAFCLAU           | LIST MANAGER ROUTINE FOR MPI/PD VAFC EXCPT LOCAL AUDIT IN PDR                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| VAFCMG01          | DEMOGRAPHIC MERGE SCREEN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| VAFCMGA           | DEMOGRAPHIC MERGE SCREEN ACTIONS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| VAFCMGA1          | DEMOGRAPHIC MERGE SCREEN ACTIONS, continued                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VAFCMGB           | DEMOGRAPHIC MERGE SCREEN BUILDER                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| VAFCMGB0          | DEMOGRAPHIC MERGE SCREENS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VAFCMGB1          | DEMOGRAPHIC MERGE SCREENS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VAFCMGB2          | DEMOGRAPHIC MERGE SCREENS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VAFCMGB3          | DEMOGRAPHIC MERGE SCREENS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VAFCMGB4          | DEMOGRAPHIC MERGE NOTIFIER                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| VAFCMGU0          | MERGE SCREEN UTILITIES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| VAFCMIS           | MISSING ICN CROSS REFERENCE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VAFCPDAT          | DISPLAY MPI/PD INFORMATION FOR SELECTED PATIENT. Fields added to the Local Vista PDAT option so that they are viewable: SELF IDENTIFIED GENDER (#.024) and PERIOD OF SERVICE (#.323).                                                                                                                                                                                                                                                                                                                           |
| VAFCPDT2          | DISPLAY MPI/PD INFORMATION FOR SELECTED PATIENT                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VAFCPTAD          | Enhanced VAFC VOA ADD PATIENT RPC to include MBI.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| VAFCPTED          | EDIT EXISTING PATIENT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VAFCQRY           | Query for patient demographics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VAFCQRY1          | Query for patient demographics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VAFCQRY2          | Query for patient demographics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VAFCRAU           | LIST MANAGER ROUTINE FOR MPI/PD VAFC EXCPT REMOTE AUDIT IN PDR                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VAFCRAUD          | ROUTINE TO CALL VAFC REMOTE AUDIT (PATIENT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VAFCRPC           | RPC ENTRY POINTS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| VAFCSB            | CONT ADT PROCESSOR TO RETRIGGER A08 or A04 MESSAGES WITH AL/AL (COMMIT/APPLICATION) ACKNOWLEDGEMENTS. Creates entry points that can be used to create OBX and ERR HL7 segments to send to the MPI in ADT-A31, ADT-A08, and ACK-A31 messages. These segments will contain the NAME field (#.01) of the PATIENT File (#2), and the FAMILY (LAST) LAST NAME field (#1), GIVEN (FIRST) NAME field (#2), MIDDLE NAME field (#3), SUFFIX fielMPIFA31Bd (#5), and PREFIX field (#4) of the NAME COMPONENTS File (#20). |
| VAFCTF            | Utility for capturing patient's Date Last Treated and Event Reason                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VAFCTFIN          | TREATING FACILTIY MFU PROCESSING ROUTINE                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| VAFCTFMF          | Broadcast Master File Update for Treating Facility                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VAFCTFPR          | MFU PROCESSING ROUTINE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| VAFCTFU           | UTILITIES FOR THE TREATING FACILITY FILE 391.91                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VAFCTFU1          | Utilities for the Treating Facility file 391.91, continued                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| VAFCTR            | Monitoring fields for MPI/PD via DG field monitoring                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VAFCUTL           | Utility for the ADT/HL7 PIVOT file 391.71, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VAFCUTL1          | UTILITY ROUTINE FOR CIRN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

# File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Files and Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists all the MPI/PD package files with their file numbers, shows their global location, and gives a file description.

391.91 TREATING FACILITY LIST ^DGCN(391.91,  
Data Comes with File: No

This file holds the Treating Facility List, which is a list of institutions where the patient has had treatment.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-technical-manual/038.png)</td>
<td><p><strong>NOTE:</strong> As of Patch DG*5.3*837, the following Data Dictionary changes were made to the TREATING FACILITY LIST file (#391.91):</p>
<ul>
<li><blockquote>
<p>The ASSIGNING AUTHORITY field (#1), which was a pointer to the VAFC ASSIGNING AUTHORITY file (#391.92) was removed. This field was replaced by the ASSIGNING AUTHORITY field (#10). This is a free text field, containing identifier information for either the Health Level Seven v2.4 or v3.0 standard.</p>
</blockquote></li>
<li><blockquote>
<p>The SOURCE ID multiple (#20) containing the SOURCE ID (#.01) and IDENTIFIER STATUS (#1) fields was removed. These fields were replaced by identical fields at the file level: SOURCE ID (#11) and IDENTIFIER STATUS (#12).</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>![](mpi-pd-version-1-vista-technical-manual/039.png)</td>
<td><p><strong>NOTE:</strong> As of Patch DG*5.3*825 the following two updates were made to the TREATING FACILITY LIST file (#391.91):</p>
<ul>
<li><blockquote>
<p>The length of the SOURCE ID field (#.01) in the SOURCE ID multiple (#20) was changed from 40 to 150 characters to accommodate identifiers for National Health Information Network (NHIN) facilities.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>The following new fields were created in the TREATING FACILITY LIST field (#391.91):</p>
</blockquote></li>
</ul>
<ul>
<li><p>SOURCE ID TYPE (#.09) defines the data source and comes from the HL7 Table 0203, Identifier Type. The data type is a Set of Codes (i.e., NI, PI, EI, PN, SS, NPI)</p></li>
<li><p>ASSIGNING AUTHORITY field (#1) is a pointer to the new VAFC ASSIGNING AUTHORITY file (#391.92). It identifies the entity that established the identification number for the patient.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-technical-manual/040.png)</td>
<td><p><strong>NOTE:</strong> As of Patch DG*5.3*821, there are new Treating Facility updates. The SOURCE ID (#20) multiple has been added to the TREATING FACILITY LIST (#391.91) file on VistA.  The SOURCE ID (#.01) and IDENTIFIER STATUS (#1) fields are updated by a Treating Facility update from the Master Patient Index (MPI) and facilitate the addition of the Department of Defense (DoD) as a treating facility correlation.</p>
<p>The SOURCE ID (#.01) field is a unique system assigned identifier for a patient record.  If SOURCE ID is from the Master Patient Index, the value is the Integration Control Number (ICN).  If SOURCE ID is from the Department of Defense (DoD), the value is the Electronic Data Interchange Personal Identifier (EDIPI), which is their equivalent of an ICN. In the future, SOURCE ID may come from other sources due to additional initiatives.</p>
<p>The IDENTIFIER STATUS (#1) field indicates whether the record is active on the identifying system (e.g., VAMC or DoD) or if the record was identified as part of a duplicate pair, has been merged, and is no longer active on the identifying system.</p></td>
</tr>
</tbody>
</table>

391.92 VAFC ASSIGNING AUTHORITY ^DGCN(391.92,  
Data Comes with File: Yes

As of Patch DG\*5.3\*825 the VAFC ASSIGNING AUTHORITY file (#391.92) was created to expand the capability of VA Identity Management Service (IdM) to support future initiatives (e.g., National Health Information Network (NHIN) and non-Patient Identity Management, etc.). File \#391.92 stores information used to assemble fully qualified identifiers used for either the Health Level Seven v2.4 or v3.0 standard. The VAFC ASSIGNING AUTHORITY (#391.92) file is exported with five entries and new data will be added as needed for HL7 messaging.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-technical-manual/041.png)</td>
<td><p><strong>NOTE:</strong> As of Patch DG*5.3*837, MPI will no longer update the VAFC ASSIGNING AUTHORITY file (#391.92). That data is stored directly into the new ASSIGNING AUTHORITY field (#10) in the TREATING FACILITY LIST file (#391.91).</p>
<p>Due to this change in the processing logic in MPI, the VAFC ASSIGNING AUTHORITY file (#391.92) was no longer needed.</p>
<p>NOTE: File #391.92 was distributed by the MPI team via DG*5.3*825 on 1/25/11, has no authorized Integration Agreements, and was deleted with DBA approval.</p></td>
</tr>
</tbody>
</table>

984.1 MASTER PATIENT INDEX (LOCAL NUMBERS) ^MPIF(984.1,  
Data Comes with File: Yes

This file is to be used to generate local ICNs when the MPI is down (unreachable).

984.5 MPI CHECKDIGIT ^MPIF(984.5,  
Data Comes with File: Yes

This file is used to calculate the check digit (check sum) for an ICN.

984.8 MPI ICN BUILD MANAGEMENT ^MPIF(984.8,  
Data Comes with File: Yes

This file is used to track the MPI Initialization process. It is utilized when stopping and restarting the initialization process.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-technical-manual/042.png)</td>
<td><p><strong>NOTE:</strong> As of Patch MPIF*1.0*63, an additional entry “TWO” will be created in file #984.8 to determine which communication protocol layer (HTTP or HTTPS) will be utilized when communicating with PSIM.</p>
<p>If the LAST PATIENT BUILT field (#3) is set to ‘<strong>0’</strong> or is ‘<strong>undefined’</strong>, then the HTTP communication protocol layer will be used. However, if the field is set to <strong>‘1’</strong>, then the HTTPS communication protocol layer will be used instead.</p>
<p>Initially the entry will be set to ‘0’ upon creation, then the MPI will remotely update the value as needed through the remote procedure (RPC) [MPI VISTA HWS CONFIG], turning HTTPS on when the site is properly configured, or reverting back to HTTP while issues/errors are encountered/addressed at the site.</p></td>
</tr>
</tbody>
</table>

984.9 MPIF CMOR REQUEST ^MPIF(984.9,  
Data Comes with File: No

This file holds all requests for change of a patient's Coordinating Master of Record. Requests being sent to remote locations and received from remote locations are stored in this file and updated as new requests are received.

991.1 CIRN HL7 EXCEPTION LOG ^RGHL7(991.1,  
Data Comes with File: No

This file contains exception messages logged during the generation of outbound messages and the processing of inbound messages. Some fields apply only for entries logged by message generation routines, others only to message processing routines, and others to both.

This file should not be edited directly. Instead, use the exception management utilities to manage entries in this file.

991.8 CIRN SITE PARAMETER ^RGSITE(991.8,  
Data Comes with File: No

This file is used to store generic site parameters for the Master Patient Index/Patient Demographic (MPI/PD) VistA package. Only one entry (entry number 1) should exist in this file.

991.11 CIRN HL7 EXCEPTION TYPE ^RGHL7(991.11,  
Data Comes with File: Yes

This file lists the types of exceptions that can be logged and additional information about the exceptions.

You may edit the Action (#2) and Mail Group (#6) fields in this file to suit your needs. No other fields should be modified.

995 CIRN EVENT ASSOCIATION ^RGEQASN(#995,  
Data Comes with File: Yes

This file holds definitions of CIRN events that occur. When an event occurs, an entry is placed into a queue and is associated with an entry in this file. This file will determine how the event is processed (i.e., the routine to call to process the event and related HL7 Protocol).

Since each event type is placed on its own queue, this file also determines characteristics of the queue itself.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-technical-manual/043.png)</td>
<td><p><strong>NOTE: AMPIZZ and ATSSN Cross References Removed From PATIENT File (#2)</strong></p>
<p>As of Patch DG*5.3*589, the AMPIZZ and ATSSN cross-references have been removed from the PATIENT file (#2). These cross-references were used to automatically inactivate patient entries from the MPI if records were found to be ZZ'd and/or if the first five digits of patient Social Security Numbers were replace with zeros.</p></td>
</tr>
</tbody>
</table>

### PATIENT File (#2) Fields Captured During Edits and Included in HL7 Messages Generated by MPI/PD Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/044.png) | REF: For the full list of the fields in the PATIENT file (#2) captured during edits and included in the HL7 messages generated by the MPI/PD applications, see the documentation for the background job titled: “UPDATE BATCH JOB FOR HL7 v2.3” in this manual. |

As of Patch DG\*5.3\*902, the following new fields were added to the PATIENT (#2) file and are utilized by the MPI. (See “Table 6. Data elements monitored in the PATIENT file (#2) for changes”):

- FULL ICN (#991.1)
- FULL ICN HISTORY (#991.91)

Both fields contain the complete Integration Control Number (ICN) value, which includes the Identifier, Delimiter, Checksum, and optional Encryption Scheme.

As of Patch RG\*1.0\*62, in support of the new Date of Death (DOD) requirements to the MPI, the following fields from the PATIENT (#2) file will be added to the OBX message segment of the ADT-A08 HL7 message (See “Table 6. Data elements monitored in the PATIENT file (#2) for changes”):

- DEATH ENTERED BY (#.352)
- SOURCE OF NOTIFICATION (#.353)
- DATE OF DEATH LAST UPDATED (#.354)
- LAST EDITED BY (#.355)

As of Patch DG\*5.3\*837, the following two fields were added to the VistA PATIENT file (#2) to support the Defense Eligibility Enrollment Reporting System (DEERS). These fields are Department of Defense (DoD) identifiers used for individuals who do not have a Social Security Number. This data is used by the Master Veteran Index to support the linking of patient records across VA and DoD.

- Field Name: TEMPORARY ID NUMBER  
  Field Number: \#991.08  
  Description: The Department of Defense (DoD) Defense Eligibility Enrollment Reporting System (DEERS) uses a Temporary Identification Number for individuals (e.g., babies) who do not have or have not provided a Social Security Number (SSN) when the record is added to DEERS. It is used for military dependents only. This DoD TEMPORARY ID NUMBER is used by the Master Veteran Index to support the linking of patient records across VA and DoD.
- Field Name: FOREIGN ID NUMBER  
  Field Number: \#991.09  
  Description: The Department of Defense (DoD) Defense Eligibility Enrollment Reporting System (DEERS) uses a Foreign Identification Number for foreign military and foreign nationals when the record is added to DEERS. This DoD FOREIGN ID NUMBER is used by the Master Veteran Index to support the linking of patient records without a given Social Security Number (SSN) across VA and DoD.

As of Patch DG\*5.3\*863, when a patient's current residential address is located in a foreign country (e.g., for a Department of Defense (DoD) patient) the following foreign address fields, from the VistA PATIENT file (#2), are displayed in the Patient MPI/PD Data Inquiry and Display Remote Patient Data Query options:

- PROVINCE field \#.1171
- POSTAL CODE field \#.1172
- COUNTRY field \#.1173

The condition by which these fields are displayed is as follows:

- If the COUNTRY field (#.1173), located in the PATIENT file (#2), is *<u>not</u>* null.
- Or if the CODE field (#.01), in the COUNTRY CODE file (#779.004), is *<u>not</u>* equal to "USA".

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following is a list of the VA FileMan templates exported with the MPI/PD package. There is a brief description for each template, along with the file name and number that each are located in (if applicable).

### List Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- RG EXCPT ACTION  
  > File: LIST TEMPLATE file (#409.61)  
  > Used to create the List Manager screen for the MPI/PD Exception Handling exception actions for a patient selected.
- RG EXCPT PDAT  
  > File: LIST TEMPLATE file (#409.61)  
  > Used to list Patient Data Query, an activity of MPI/PD Exception Handling.
- RG EXCPT PV REJECT RDISPLAY  
  > File: LIST TEMPLATE file(#409.61)  
  > Used to create MPI Primary View Reject Display screen for the Primary View Reject exception on the MPI/PD Exception Handling option.
- RG EXCPT RPDAT  
  > File: LIST TEMPLATE file (#409.61)  
  > Used to list Remote Patient Data Query, which gets data from shared sites. It is an activity of MPI/PD Exception Handling.
- RG EXCPT SUMMARY  
  > File: LIST TEMPLATE file (#409.61)  
  > Used to create the List Manager screen for MPI/PD Exception Handling.
- RG EXCPT PV MPI PDAT  
  > File: LIST TEMPLATE file (#409.61)  
  > Used to remotely display the MPI Primary View patient identity fields on the Master Patient Index (MPI). The report generated by this option displays the current activity scores for individual patient identity fields (i.e., Primary View of the MPI) and the Primary View data fields.
- VAFC EXCPT LOCAL AUDIT  
  > File: LIST TEMPLATE file (#409.61)  
  > Used to display local patient audit data.
- VAFC EXCPT REMOTE AUDIT  
  > File: LIST TEMPLATE file (#409.61)  
  > Used to return MPI/PD Remote Audit Data.

### Print Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- MPIF OUTSTANDING REQUESTS  
  File: MPIF CMOR REQUEST (#984.9)  
  Allows user to display Pending Approval CMOR Requests.
- MPIF REQUEST VIEW  
  File: MPIF CMOR REQUEST (#984.9)  
  Allows user to display a single CMOR Request.

### Sort Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- MPIF PENDING REQUESTS  
  File: MPIF CMOR REQUEST (#984.9)  
  Sort CMOR requests with STATUS of pending approval, then within that sort by SITE not equal to null.
- MPIF REQUEST SORT  
  > File: MPIF CMOR REQUEST (#984.9)  
  > Sort by SITE number not equal to null, then within that sort by the CMOR request STATUS and chronological order by ENTER DATE.

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- MPIF OPEN REQUEST  
  File: MPIF CMOR REQUEST (#984.9)  
  Gives the user edit access to enter a new record in File \#984.9 for CMOR requests.
- MPIF REQUEST INCOMING  
  File: MPIF CMOR REQUEST (#984.9)  
  Allows user to display the CMOR request.
- MPIF RESULT INCOMING  
  File: MPIF CMOR REQUEST (#984.9)  
  Allows user to approve/disapprove the CMOR request.
- MPIF REVIEW AUTO  
  File: MPIF CMOR REQUEST (#984.9)  
  Automatically approve the CMOR request.
- MPIF REVIEW RESET  
  File: MPIF CMOR REQUEST (#984.9)  
  Reverse the approval process. If the user has not completed the approval process the new data won't be saved. (e.g., through an up-arrow or time out).
- MPIF REVIEW RESULT  
  File: MPIF CMOR REQUEST (#984.9)  
  Automatically saves the approval data to the CMOR request once the user approves request.
- MPIF SITE PARAMETERS  
  File: CIRN SITE PARAMETER (#991.8)  
  Allow automatic processing of CMOR request.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes in detail the menus and options comprising the Master Patient Index/Patient Demographics (MPI/PD) VistA. They should be made accessible to authorized IRM, ADPAC (i.e., most likely PIMS ADPACs and/or Coordinators, etc.), and VAMC personnel who will be involved in working with the MPI/PD.

## MPI/PD Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MPI/PD Master Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510587931" class="anchor"></span>Figure . MPI/PD Master Menu

MPI/PD Master Menu ... RGMGR

CORD MPI/PD Patient Admin Coordinator Menu ... RG ADMIN COORD MENU

IRM MPI/PD IRM Menu ... RG IRM MENU

### MPI/PD Patient Admin Coordinator Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc364074450" class="anchor"></span>Figure . MPI/PD Patient Admin Coordinator Menu

CORD MPI/PD Patient Admin Coordinator Menu ... \[RG ADMIN COORD MENU\]

LOG Patient Audit Log Reports ... \[RG TRAN/AUD AUD REP\]

Patient Audit File Print \[RGMT AUDIT PRINT\]

Single Patient Audit File Print \[RGMT AUDIT SINGLE\]

MSG Message Exception Menu ... \[RG EXCEPTION MENU\]

Patient MPI/PD Data Inquiry \[RG EXCEPTION TF INQUIRY\]

Remote Patient Data Query Menu ... \[RG REMOTE PDAT MENU\]

Send Remote Patient Data Query \[RG REMOTE PDAT SEND\]

Check Remote Patient Data Query \[RG REMOTE PDAT CHECK\]

Display Remote Patient Data Query \[RG REMOTE PDAT DISPLAY\]

Display Only Query \[MPIF DISPLAY ONLY QUERY TO MPI\]

Primary View Display from MPI \[RG PRIMARY VIEW FROM MPI\]

RPT Management Reports ... \[RG MGT REPORTS\]

Pseudo-SSN Report \[RGPR PRE-IMP SSN REPORT\]

Link and Process Status Display\[RG LINKS & PROCESS DISPLAY\]

Unresolved Exception Summary \[RG STATUS DISPLAY\]

ToolKit POC User Setup \[RG TK POC USER SETUP\]

| ![](mpi-pd-version-1-vista-technical-manual/045.png) | NOTE: The Point of Contact (POC) add/edit functionality for the Add/Edit Point of Contact \[RG UPDATE POINT OF CONTACT\] menu option is being migrated to the ToolKit (TK) graphical user interface (GUI). This VistA process will no longer be accessible to users. As of patch release RG\*1\*61, this option was removed from the MPI/PD Patient Admin Coordinator Menu option \[RG ADMIN COORD MENU\]. Complete removal of this functionality from the VistA system will take place at a later date. |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### MPI/PD IRM Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc364074451" class="anchor"></span>Figure . MPI/PD IRM Menu

IRM MPI/PD IRM Menu ... RG IRM MENU

Link and Process Status Display \[RG LINKS & PROCESS DISPLAY\]

Unresolved Exception Summary \[RG STATUS DISPLAY\]

## Menu Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc510587948" class="anchor"></span>Table . MPI/PD Menu Assignment

| Menu                                                      | Assign to:                                      |
|-----------------------------------------------------------|-------------------------------------------------|
| MPI/PD Master Menu RGMGR                                  | Information Resource Management (IRM) personnel |
| MPI/PD Patient Admin Coordinator Menu RG ADMIN COORD MENU | Patient Administration/HAS/MPI/PD Coordinator   |
| MPI/PD IRM Menu RG IRM MENU                               | IRM personnel                                   |

## Standalone Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                   |                           |
|-----------------------------------|---------------------------|
| MPI/PD HL7 EXCEPTION NOTIFIER | RG EXCEPTION NOTIFIER |

This option is used to notify members of the RG CIRN DEMOGRAPHIC ISSUES Mail Group that there are exceptions to review. It is not a user option and should not be added to user menus.

|                                  |                          |
|----------------------------------|--------------------------|
| LOCAL/MISSING ICN RESOLUTION | MPIF LOC/MIS ICN RES |

This option starts a background job that assigns ICNs to the following types of person records, which have not been sent to the MVI:

- Person records that have local ICNs
- Person records that have been flagged as being active but do not have an ICN assignment.

It is recommended that this option be scheduled to run via TaskMan every 600 seconds (Patch MPIF\*1\*35).

|                                                                                                                |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                    |     |     |
|----------------------------------------------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|
| ![](mpi-pd-version-1-vista-technical-manual/046.png) |     | NOTE: As of Patch MPI\*1\*38, this background job no longer automatically adds patients to the MPI. Previous to the release of this patch, when the Local/Missing ICN Resolution job was processed on the MVI, if a match wasn't found, the person was added immediately. As of Patch MPI\*1\*38, this functionality has been changed in that if a match for a person isn't found on the MVI, a message is sent back to the site indicating this. On the site's side, this triggers an HL7 A28—Add Patient message, which then adds the person to the MVI. |                                                                                                                                                                                                                                                                    |     |     |
| ![](mpi-pd-version-1-vista-technical-manual/047.png) |     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | NOTE: A new field, LOCAL/MISSING DATE LAST RAN (#.04), was created in the CIRN SITE PARAMETER file (#991.8) in patch RG\*1\*23 to hold the last date the Local/Missing ICN Resolution Background job ran. The field will be populated by the routine ^MPIFRES. |     |     |
| MPI/PD HL7 DIAGNOSTIC MENU                                                                                 |     | RGMT DIAG MGR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                    |     |     |

This standalone menu contains a diagnostic tool and reports to assist with problem resolution for MPI/PD HL7 messaging. It should not be attached to any menu. This diagnostic tool will be used primarily by the MPI/PD development team and EPS.

<span id="_Toc510587934" class="anchor"></span>Figure . MPI/PD HL7 Diagnostic Menu options

MPI/PD HL7 Diagnostic RGMT DIAG MGR

CMP Compile MPI/PD HL7 Data RGMT DIAG COMPILE HL7 DATA

RPT MPI/PD HL7 Message Status Report RGMT DIAG STATUS REPORT

SNG MPI/PD HL7 Activity by Patient/Single Protocol RGMT DIAG SINGLE PROTOCOL

ALL MPI/PD HL7 Activity by Patient/All Protocols RGMT DIAG ALL PROTOCOLS

|                             |                                |
|-----------------------------|--------------------------------|
| COMPILE MPI/PD HL7 DATA | RGMT DIAG COMPILE HL7 DATA |

This utility searches the HL7 MESSAGE TEXT file (#772) for a selected date range. Each HL7 message in the date range is examined. If the RELATED EVENT PROTOCOL field contains the MPI/PD protocols (e.g., "VAF", "RG", or "MPI") data is compiled into the ^XTMP("RGMT","HL" array.

A cross-reference is built on patient ICN and DFN for faster data retrieval for the associated reports.

|                                      |                             |
|--------------------------------------|-----------------------------|
| MPI/PD HL7 MESSAGE STATUS REPORT | RGMT DIAG STATUS REPORT |

This option prints information found during the COMPILE MPI/PD HL7 DATA option. The MPI/PD HL7 MESSAGE STATUS REPORT is generated from the ^XTMP("RGMT","HL" array. The report is sorted by RELATED EVENT PROTOCOL, date, transmission type, and status.

Either a detailed or summary report can be printed for a selected date range. The summary report displays the total number of messages for each date, transmission type, and status. The right margin for this report is 80.

The detailed report can be printed for a single or all protocols and includes information from each HL7 message. The detailed report displays the related event protocol date, transmission type, status, message header date, date processed, internal entry number (IEN) from the HL7 MESSAGE TEXT file (#772), message identification number, and whether or not the message has been purged. The right margin for this report is 132.

|                                                    |                               |
|----------------------------------------------------|-------------------------------|
| MPI/PD HL7 ACTIVITY BY PATIENT/SINGLE PROTOCOL | RGMT DIAG SINGLE PROTOCOL |

This option allows you to search for activity related to a specific protocol in the HL7 MESSAGE TEXT file (#772) for a patient during a selected period of time. This search is accomplished using data set into a temporary global built by the option "Compile MPI/PD HL7 Data".

The report prints the patient's name, protocol, date range, transmission type, internal entry number (IEN) from the HL7 MESSAGE TEXT file (#772), the date and status. The HL7 message data found in the MESSAGE TEXT field is displayed. The right margin for this report is 80.

|                                                  |                             |
|--------------------------------------------------|-----------------------------|
| MPI/PD HL7 ACTIVITY BY PATIENT/ALL PROTOCOLS | RGMT DIAG ALL PROTOCOLS |

This option allows you to search for ALL activity in the HL7 MESSAGE TEXT file (#772) for a specific patient during a selected period of time. This search is accomplished using data set into a temporary global built by the option "Compile MPI/PD HL7 Data".

The report prints the patient's name, date range, protocol, transmission type, internal entry number (IEN) from the HL7 MESSAGE TEXT file (#772), the date and status. The HL7 message data found in the MESSAGE TEXT field is displayed. The right margin for this report is 80.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no security keys exported with the MPI/PD package.

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no application specific archiving procedures or recommendations for the MPI/PD package.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 and MailMan packages have purging options that should be used to control the large number of HL7 messages that MPI/PD products. Since IRM personnel have the option to use either HL7 or MailMan as the messaging component for sending and receiving data from the MPI, see the associated product documentation, listed below, for purging instructions specific to these packages:

- *VistA Health Level Seven (HL7) Technical Manual*, Version 1.6 and up.
- *VA Electronic Mail System (MailMan)* Technical Manual and Systems Management Guide, Version 7.1 and up.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Supported APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans Health Information Systems and Technology Architecture (VistA) Application Program Interfaces (API) fall into the following three categories:

1.  The first category is "Supported API" These are callable routines, which are supported for general use by all VistA applications.
2.  The second category is "Controlled Subscription API." These are callable routines for which you must obtain an Integration Agreement (IA - formerly referred to as a DBIA) to use.
3.  The third category is "Private API," where only a single application is granted permission to use an attribute/function of another VistA package.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/048.png) | NOTE: All the Supported and Controlled Subscription APIs belonging to the MPI/PD package for retrieving information from the MPI node in the PATIENT file (#2) or MPI /PD related information can be found in the *Master Patient Index/Patient Demographics (MPI/PD) VistA Programmer Manual* and on FORUM. |

The following are instructions for obtaining the current list of Integration Agreements on FORUM in its entirety, to which the Master Patient Index/Patient Demographics (MPI/PD) is a custodian:

1.  Sign on to the FORUM system (forum.va.gov).
2.  Go to the *DBA MENU*.
3.  Select the *INTEGRATION CONTROL REGISTRATIONS* menu.
4.  Select the *Custodial Package* menu.
5.  Choose the *ACTIVE ICRs by Custodial Package* option.
6.  When this option prompts you for a package, enter the name of the VistA software (e.g., Master Patient Index MPIF, Clinical Info Resource Network RG, etc.).

> NOTE: All current IAs for which the VistA package is custodian are listed.

To obtain detailed information on a specific Integration Agreement on FORUM:

1.  Sign on to the FORUM system (forum.va.gov).
3.  Select the *DBA MENU*.
4.  Select the *INTEGRATION CONTROL REGISTRATIONS* menu.
5.  Select the *Inquire to an Integration Control Registration* option.
6.  When prompted for "INTEGRATION REFERENCES", enter the number of the Integration Agreements you want to display.

> NOTE: The option lists the full text of the IAs you requested.

|                                                                                                                |                                                                                                                                                                                                                                                                                                    |     |                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/049.png) |                                                                                                                                                                                                                                                                                                    |     | NOTE: All the Supported and Controlled Subscription APIs belonging to the MPI/PD package for retrieving information from the MPI node in the PATIENT file (#2) or MPI /PD related information can be found in the *Master Patient Index/Patient Demographics (MPI/PD) VistA Programmer Manual* and on FORUM. |
| ![](mpi-pd-version-1-vista-technical-manual/050.png) | NOTE: Due to early and separate beginnings, the now combined MPI/PD, formerly known as CIRN/PD, and MPI VistA software packages, merged into one as MPI/PD, has references to both Clinical Information Resource Network (CIRN) or RG patches, and Master Patient Index VistA or MPIF patches. |     |                                                                                                                                                                                                                                                                                                                  |
| ![](mpi-pd-version-1-vista-technical-manual/051.png) | NOTE: The MPI/PD software (i.e., routines in the MPIF\* and RG\* namespaces) SHOULD NOT reside/run on Legacy systems. Any VistA applications utilizing APIs in the MPIF and RG namespaces on Legacy systems should check the existence of these routine(s) before trying to access them.       |     |                                                                                                                                                                                                                                                                                                                  |

## MVI Direct Connect

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Direct Connect is a real-time Transmission Control Protocol/Internet Protocol (TCP/IP) connection to the Master Veteran Index to allow for an immediate request for an ICN. It is activated during the Register A Patient, Load/Edit Patient Data, and Electronic 10-10EZ Processing processes when a patient doesn't have an ICN (local or national).

The Display Only Query option, used to view the data the MPI knows about a person, also utilizes the TCP/IP direct connect with the MPI.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Master Patient Index/Patient Demographics VistA package makes extensive use of HL7 messaging to ensure synchronization of person records among sites.

|                                                                                                                |                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/052.png) | REF: For more information on MPI HL7 messaging, see the *Master Patient Index/Patient Demographics (MPI/PD) VistA HL7 Interface Specifications* for complete details on message construction. |

Listed below are the HL7 Application Parameters, HL Lower Level Protocol Parameters, and HL7 Protocols, used by MPI/PD for HL7 messaging.

## HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- MPIF A29 SERVER
- MPIF A30 SERVER
- MPIF CMOR CHNG
- MPIF CMOR COMP
- MPIF CMOR RSLT
- MPIF LOC/MIS
- MPIF MPI
- MPIF TRIGGER
- MPIF-STARTUP
- RG ADT
- RG CIRN
- RG CIRN ADT
- RG MPIPD
- RG REPOSITORY
- RG SITE MERGE
- RG SUBSCRIPTION
- RGMT CIRN
- VAFC PIMS
- VAFC TRIGGER

## HL Lower Level Protocol Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- CIRN MAIL
- MPIF RTC PARAMS
- MPIVA MAIL
- MPIVA TCP

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- MPIF ADT-A24 CLIENT
- MPIF ADT-A24 SERVER
- MPIF ADT-A28 CLIENT
- MPIF ADT-A28 SERVER
- MPIF ADT-A29 CLIENT
- MPIF ADT-A29 SERVER
- MPIF ADT-A31 CLIENT
- MPIF ADT-A31 SERVER
- MPIF ADT-A37 CLIENT
- MPIF ADT-A37 SERVER
- MPIF ADT-A40 CLIENT
- MPIF ADT-A40 SERVER
- MPIF ADT-A43 CLIENT
- MPIF ADT-A43 SERVER
- MPIF CMOR APP/DIS
- MPIF CMOR APPROVE/DISAPPROVE
- MPIF CMOR COMPARISON CLIENT
- MPIF CMOR COMPARISON SERVER
- MPIF CMOR REQUEST
- MPIF CMOR RESPONSE
- MPIF CMOR RESULT CLIENT
- MPIF CMOR RESULT SERVER
- MPIF ICN-Q02 SERVER
- MPIF POTENTIAL DUP (CMOR PDAT)
- MPIF POTENTIAL DUP (HELP)
- MPIF POTENTIAL DUP (MPI PDAT)
- MPIF POTENTIAL DUP (SELECT PATIENT)
- MPIF POTENTIAL DUP MENU
- MPIF REAL-TIME QUERY (ADD PATIENT)
- MPIF REAL-TIME QUERY (CMOR PDAT)
- MPIF REAL-TIME QUERY (HELP)
- MPIF REAL-TIME QUERY (MPI PDAT)
- MPIF REAL-TIME QUERY (SELECT PATIENT)
- MPIF REAL-TIME QUERY MENU
- MPIF TEST
- RG ADT-A01 2.4 CLIENT
- RG ADT-A01 2.4 SERVER
- RG ADT-A03 2.4 CLIENT
- RG ADT-A03 2.4 SERVER
- RG ADT-A04 2.4 CLIENT
- RG ADT-A04 2.4 SERVER
- RG ADT-A04 TRIGGER
- RG ADT-A08 2.4 CLIENT
- RG ADT-A08 2.4 SERVER
- RG ADT-A08 TRIGGER
- RG EXCPT ACTION MENU
- RG EXCPT BLANK1
- RG EXCPT DATE SORT
- RG EXCPT DISPLAY ONLY QUERY
- RG EXCPT EDIT NOTE
- RG EXCPT EDIT PATIENT DATA
- RG EXCPT HINQ INQUIRY
- RG EXCPT MAIN MENU
- RG EXCPT MPI/PD DATA
- RG EXCPT PATIENT AUDIT
- RG EXCPT PATIENT INQUIRY
- RG EXCPT PATIENT SORT
- RG EXCPT PDAT MENU
- RG EXCPT POT MATCH
- RG EXCPT PV REJECT
- RG EXCPT RCHK
- RG EXCPT RDISP
- RG EXCPT RSEND
- RG EXCPT SELECT
- RG EXCPT SELECT TYPE
- RG EXCPT SORT
- RG EXCPT UPDATE STATUS
- RG EXCPT TF INQUIRY
- RG EXCPT TYPE SORT
- RG EXCPT UPDATE STATUS
- RG EXPCT PDAT MENU
- RG FACILITY INTEGRATION CLIENT
- RG FACILITY INTEGRATION SERVER
- RG MPI DELETE
- RG PATIENT MERGE

In the Phase III Enhancements project, a new messaging structure was implemented for the MPI/PD. To reduce the amount of facility-to-facility messaging, the MPI Austin is now the source for update messages rather than the CMOR. For those message types that require CMOR action, the CMOR will update the MPI, and the MPI will distribute updates to the appropriate facilities. Changes to messaging include the use of a new generic HL7 2.4 message builder for the ENV, PD1 and PID segments. Additionally, HL7 application acknowledgements are incorporated in all MPI/PD messages. Upon installation of the third phase of patches (DG\*5.3\*474, MPIF\*1\*24, and RG\*1\*27), the necessary routines to call the new trigger events using the updated messaging structure will be in place.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-technical-manual/053.png)</td>
<td><strong>NOTE:</strong> With the implementation MPI Changes Project, Iteration 4 - Primary View (MPI*1*40, MPIF*1*44 and RG*1*45), the CMOR will no longer play a roll, but instead the Primary View business rules will determine what will be updated and send out the update messages to the appropriate facilities.</td>
</tr>
<tr class="even">
<td>![](mpi-pd-version-1-vista-technical-manual/054.png)</td>
<td><p><strong>REF:</strong> For definitions of MPI/PD messages, please refer to the <em>Master Patient Index/Patient Demographics (MPI/PD) VistA HL7 Interface Specification</em> on the VA Web site:</p>
<p><a href="http://www.va.gov/vdl/">VA Software Documentation Web site</a></p></td>
</tr>
</tbody>
</table>

## Remote Procedure Calls (RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists all the supported RPCs belonging to the MPI/PD package sorted alphabetically by RPC name.

<span id="_Toc510587949" class="anchor"></span>Table . MPI/PD Remote Procedure Calls (RPC)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RPC</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MPI GETCORRESPONDINGIDS</strong><br />
Routine: GETIDS^MPIRPC1</td>
<td><p>This RPC is used by PSIM to pull the list of active correlations for a given ICN.  It is intended for use only by consumers like North Chicago that need to get the Date Last Treated information on the correlation which at this time is only stored on MPI. ICN is the name of a return parameter that returns a list of active correlations as the value in the following  format.</p>
<ul>
<li><p>n^SourceID^Station#^DateLastTreated</p></li>
<li><p>n+1^SourceID^Station#^DateLastTreated</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>MPI TK POC USER SETUP<br />
</strong>Routine: TKPOC^MPIRPC12</td>
<td><p>This remote procedure call is invoked when a VistA user uses the option MPIF TK POC USER SETUP to confirm their traits and establish a TK POC record on the MPI in the New Person file (#200).</p>
<p>This RPC is called by the option RG TK POC USER SETUP to access the MPI to establish a Visitor Record in the NEW PERSON file (#200).  Just calling the RPC will establish the Visitor record if one didn't exist. The RPC will identify any missing required fields in the New Person file and instruct the user to check their setup in the New Person file to be sure they have Name, SSN, and Site setup via the Edit an Existing User option on the User Management menu, noting they should contact their local IRM support for further assistance if needed. If they have all the required fields the user will get a message back that all is good and to contact HC IdM to verify they have completed this initial step.  At that point, HC IdM will contact MPI development to find the Visitor Record on MPI production and manually update the POC entry with the SSN, Phone, and DUZ.</p></td>
</tr>
<tr class="odd">
<td><strong>MPIF ACK CHECK<br />
</strong>Routine: EN^MPIFACHK</td>
<td>This RPC will check to see if there are any messages on the sites before date BEFORE that haven’t received the application level ACK back. If so, the message will need to be regenerated to the MPI.</td>
</tr>
<tr class="even">
<td><strong>MPIF DNL ADD UPD</strong><br />
Routine: DNLADD^MPIRPC</td>
<td>This RPC has been established to allow the remote creation of records into the MPI DO NOT LINK (#985.26) file.</td>
</tr>
<tr class="odd">
<td><strong>MPIF EDAT REMOTE</strong><br />
Routine: MPIEDAT^MPIRPC</td>
<td>MPI Extended Patient data inquiry for Display Only Query. ICN needs to be passed in.</td>
</tr>
<tr class="even">
<td><strong>MPIF EXT PDAT REMOTE<br />
</strong>Routine: PATINFO^MPIFEXT2</td>
<td><p>This RPC is the Extended PDAT call remote. ICN or SSN can be passed.</p>
<p>NOTE: With the introduction of the new Race and Ethnicity fields in the PATIENT file (#2), in Patch DG*5.3*415, MPIF EXT PDAT REMOTE was modified to utilize these new fields. Routine MPIFEXT2 was modified to support this change.</p></td>
</tr>
<tr class="odd">
<td><strong>MPIF ICN STATS<br />
</strong>Routine: ICNSTAT^MPIFRPC</td>
<td>This RPC, also known as MPIF ICN STATS, returns an ICN, Exceptions pending, CMOR, CMOR History, ICN History for any given ICN.</td>
</tr>
<tr class="even">
<td><strong>MPIF INACTIVATE<br />
</strong>Routine: INACT^MPIFRPC</td>
<td>This RPC allows the remote inactivation of a patient from the MPI at a specific site.</td>
</tr>
<tr class="odd">
<td><strong>MPIF REMOTE FULL ICN STATS</strong><br />
Routine: STATS^MPIFFULL</td>
<td>This RPC allows the remote MPI user to know when the last run of the MPIF REMOTE LOCAL ICN ASSIGN RPC took place, the total number of patients with national ICNs, local ICNs, merged patients (-9 node in PATIENT (#2) file), and no ICNs.</td>
</tr>
<tr class="even">
<td><strong>MPIF REMOTE ICN UPDATE<br />
</strong>Routine: UPDATE^MPIFRPC2</td>
<td>This RPC allows the remote update of the INTEGRATION CONTROL NUMBER (#991.01), ICN CHECKSUM (#991.02), and COORDINATING MASTER OF RECORD (#991.03) fields in the PATIENT file (#2) at a specified site. The patient is found based upon SSN.</td>
</tr>
<tr class="odd">
<td><strong>MPIF REMOTE LOCAL ICN ASSIGN</strong><br />
Routine: LOCALIA^MPIFFULL RPC</td>
<td>This RPC allows local integration control numbers (ICNs) to be assigned to a number of patient records. This allows them to get a national ICN thru the normal resolution of local ICNs via the MPIF LOCAL/MISSING ICN RESOLUTION background job.</td>
</tr>
<tr class="even">
<td><strong>MPIF REMOTE PRIMARY DFN ICN<br />
</strong>Routine: PRIMARY^MPIFRPC3</td>
<td>This Remote Procedure Call will return the primary system IEN (DFN) in the PATIENT file (#2) along with the Integration Control Number (ICN) if available for a particular legacy system station number and DFN.</td>
</tr>
<tr class="odd">
<td><strong>MPIF REMOTE SPI<br />
</strong>Routine: SPI^MPIFRPC2</td>
<td>This RPC allows the remote sending of a specific patient at a specific site to the MPI for ICN assignment. The patient is found based upon SSN.</td>
</tr>
<tr class="even">
<td><strong>MPIF SSN DUPS<br />
</strong>Routine: TOSITE^MPIFDUPS</td>
<td>This RPC will be used by the MPI Data Quality Management Team’s Statistics Report to search for multiple SSNs with different ICNs from the same site.</td>
</tr>
<tr class="odd">
<td><strong>RG PRIMARY VIEW FROM MPI<br />
</strong>Routine: MPIPV^MPIRPC</td>
<td>This remote procedure call will return the MPI Patient Data Inquiry [MPI DATA MGT PDAT MPI] (PDAT) report for a requested ICN.</td>
</tr>
<tr class="even">
<td><strong>RG PRIMARY VIEW REJECT</strong><br />
Routine: PVREJ^MPIRPC</td>
<td>This RPC will return the Primary View Reject report for a particular station, ICN, and date range. The date range will be from the date of the exception to the current date.</td>
</tr>
<tr class="odd">
<td><strong>RG REM ACTIVITY</strong><br />
Routine: EN^RGACTIV</td>
<td>This RPC returns Health Level Seven (HL7) message information and exception information for a patient. The HL7 data is from the ADT/HL7 PIVOT file (#391.71) and exception date is from the CIRN HL7 EXCEPTION LOG file (#991.1).</td>
</tr>
<tr class="even">
<td><strong>RG REMOTE HL7 TASK<br />
</strong>Routine: TASK^RGMTRUN</td>
<td>This RPC will return the currently running HL7 tasks from a remote site to the Master Patient Index (MPI) Austin.</td>
</tr>
<tr class="odd">
<td><strong>RG VIEW VISTA EXCEPTIONS<br />
</strong>Routine: EN^RGRPC</td>
<td>This RPC will allow the MPI HC IdM staff to view VistA exceptions for a given patient logged during a specific date range.</td>
</tr>
<tr class="even">
<td><strong>VAFC AA UPDATE REMOTE PROCEDURE<br />
</strong>Routine: PDAT^VAFCRPC</td>
<td>When a new entry is added to the MPI ASSIGNING AUTHORITY (#985.55) file on the MPI, the VAFC AA UPDATE REMOTE PROCEDURE is called.  The RPC triggers an update message to those Treating Facilities where the patient's Integration Control Number (ICN) is known and creates an identical entry in the VistA VAFC ASSIGNING AUTHORITY (#391.92) file.</td>
</tr>
<tr class="odd">
<td><strong>VAFC LOCAL GETCORRESPONDINGIDS</strong><br />
Routine: TFL^VAFCTFU2</td>
<td>A new Remote Procedure Call (RPC), VAFC LOCAL GETCORRESPONDINGIDS, has been created. When supplied with a patient DFN, Integration Control Number (ICN), or DoD's Electronic Data Interchange Personal Identifier (EDIPI), the RPC will return specific data. The returned information includes the list of Treating Facilities where the patient has been seen, the station number of that facility, the SOURCE ID and the IDENTIFIER STATUS.</td>
</tr>
<tr class="even">
<td><strong>VAFC NEW NC TREATING FACILITY<br />
</strong>Routine: NEWTF^VAFCTFU2</td>
<td>A new Remote Procedure Call (RPC), VAFC NEW NC TREATING FACILITY, has been created for use by the North Chicago Common Registration User Interface (UI). The RPC allows the UI to add an active Department of Defense correlation to the TREATING FACILITY LIST (#391.91) file if it does not already exist. The RPC then returns the list of Treating Facilities where the patient has been seen, along with the SOURCE ID, INSTITUTION, and IDENTIFIER STATUS.</td>
</tr>
<tr class="odd">
<td><strong>VAFC REMOTE PDAT<br />
</strong>Routine: PDAT^VAFCRPC</td>
<td>This RPC returns the test Patient MPI/PD Data Inquiry report to a remote site.</td>
</tr>
<tr class="even">
<td><strong>VAFC VOA ADD PATIENT<br />
</strong>Routine: ADD^VAFCPTAD</td>
<td>This RPC allows the remote creation of a VistA PATIENT file (#2) record at the Preferred Facility for the Veteran On-Line Application (VOA) project.</td>
</tr>
</tbody>
</table>

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Platform Requirements

The Master Patient Index/Patient Demographics VistA package requires a standard VistA operating environment in order to function correctly. Check your VistA environment for packages and versions installed.

|                                                                                                                |                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-technical-manual/055.png) | REF: For information on the VistA APIs created and used by the MPI/PD package, and for instructions for obtaining the current list of DBA Approvals and Integration Agreements on FORUM, see the section titled: *"Supported APIs"* in the *"Callable Routines"* chapter of this manual. |

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All routines, files, and options within the MPI/PD software can function independently.

Namespace

The Master Patient Index/Patient Demographics (MPI/PD) VistA package uses both MPIF and RG namespaces.

File Numbers

The MPI/PD V.1.0 file numbers and globals are listed below.

<span id="_Toc510587950" class="anchor"></span>Table . MPI/PD v1.0 Files

| File \# | Name                             | Global     |
|-------------|--------------------------------------|----------------|
| 984.1       | MASTER PATIENT INDEX (LOCAL NUMBERS) | ^MPIF(984.1,   |
| 984.5       | MPI CHECKDIGIT                       | ^MPIF(984.5,   |
| 984.8       | MPI ICN BUILD MANAGEMENT             | ^MPIF(984.8,   |
| 984.9       | MPIF CMOR REQUEST                    | ^MPIF(984.9,   |
| 991.1       | CIRN HL7 EXCEPTION LOG               | ^RGHL7(991.1,  |
| 991.8       | CIRN SITE PARAMETER                  | ^RGSITE(991.8  |
| 991.11      | CIRN HL7 EXCEPTION TYPE              | ^RGHL7(991.11, |
| 995         | CIRN EVENT ASSOCIATION DATA SCREEN   | ^RGEQASN(      |

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Master Patient Index/Patient Demographics (MPI/PD) VistA package contains no package-wide variables.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mail Groups

Mail groups exported with the MPI/PD package are documented in the *"Implementation and Maintenance"* section of this manual.

Bulletins

Mail groups exported with the MPI/PD package are documented in the *"Implementation and Maintenance"* section of this manual.

Remote Systems

The MPI Austin, located at the Austin Information Technology Center (AITC), maintains the actual patient index and a current list of facilities where the patient has been seen in order to enable sharing of patient data among operationally diverse systems. The MPI/PD that resides on VistA at the sites, sends data to the MPI Austin. Some patient fields were transmitted to Austin during the initialization process as a result of daily operations at the VAMC. The initialization process started at a VAMC. HL7 messages went to the MPI requesting ICNs for all the patients that had activity in the past three years. This process has been completed and currently the MPI is kept up-to-date via existing VistA options.

The MPI/PD package makes extensive use of HL7 messaging to ensure synchronization of patient records between sites. Please refer to the *Master Patient Index/Patient Demographics (MPI/PD) VistA HL7 InterfaceManual* for complete details on message construction.

Archiving

There are no application-specific archiving procedures or recommendations for the Master Patient Index/Patient Demographics (MPI/PD) VistA package.

The HL7 and MailMan packages have purging options that should be used to control the large number of HL7 messages that MPI/PD products. Since IRM personnel have the option to use either HL7 or MailMan as the messaging component for sending and receiving data from the MPI, see the associated product documentation, listed below, for purging instructions specific to these packages:

*VistA Health Level Seven (HL7) Technical Manual*, Version 1.6 and up.

*VA Electronic Mail System (MailMan) Technical Manual and Systems Management Guide*, Version 7.1 and up.

Contingency Planning

Sites should have a local contingency plan to be used in the event of application problems in a live environment. Field station Information Security Officers (ISOs) can get assistance for the Regional ISO (RISO).

Interfacing

There are no specialized (not VA produced) products (hardware and/or software) embedded within or required by the MPI/PD package.

Electronic Signatures

There are no electronic signatures used in the MPI/PD package.

Menus

There are no options of particular interest to Information Security Officers (ISOs) in the MPI/PD package.

Security Keys

There are no security keys exported with the MPI/PD package.

File Security

<span id="_Ref272183177" class="anchor"></span>Table . Software Product Security: File Access

| File \# | File Name                        | DD | RD | WR | DEL | LAYGO | AUDIT |
|-------------|--------------------------------------|--------|--------|--------|---------|-----------|-----------|
| 984.1       | MASTER PATIENT INDEX (LOCAL NUMBERS) | @      | @      | @      | @       | @         | @         |
| 984.5       | MPI CHECKDIGIT                       | @      | @      | @      | @       | @         | @         |
| 984.8       | MPI ICN BUILD MANAGEMENT             | @      | @      | @      | @       | @         | @         |
| 984.9       | MPIF CMOR REQUEST                    | @      | @      | @      | @       | @         | @         |
| 991.1       | CIRN HL7 EXCEPTION LOG               |        |        |        |         |           |           |
| 991.8       | CIRN SITE PARAMETER                  | @      | @      | @      | @       | @         | @         |
| 991.11      | CIRN HL7 EXCEPTION TYPE              | @      | @      | @      | @       | @         |           |
| \*\*391.91  | TREATING FACILITY LIST               | @      | @      | @      | @       | @         | @         |
| \*\*391.92  | VAFC ASSIGNING AUTHORITY             | @      | @      |        |         |           |           |
| 995         | CIRN EVENT ASSOCIATION               |        |        |        |         |           |           |

\*\* The file numbers listed in Table 15 preceded by two asterisks (\*\*) are not files created in the MPI/PD namespace. They are, however, files that the MPI/PD software interacts with.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 14%" />
<col style="width: 75%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>.001 Field</strong></th>
<th colspan="3">A field containing the internal entry number of the record.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><strong>.01 Field</strong></td>
<td colspan="3">The one field that must be present for every file and file entry. It is also called the NAME field. At a file's creation the .01 field is given the label NAME. This label can be changed.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>10-10EZ</strong></td>
<td colspan="3">Form used to apply for health benefits.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Abbreviated Response</strong></td>
<td colspan="3">This feature allows you to enter data by typing only the first few characters for the desired response. This feature will not work unless the information is already stored in the computer.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Accept Agreement</strong></td>
<td colspan="3">Part of the validation and agreement to the privacy regulations associated with Toolkit (IdM TK).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Access Code</strong></td>
<td colspan="3">A code that, along with the Verify code, allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than 6 and less than 20 characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator. It is used by the Kernel's Sign-on/Security system to identify the user (see Verify Code).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Active Patients</strong></td>
<td colspan="3">Persons who have been seen at a site within the past three years.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>ADPAC</strong></td>
<td colspan="3">Automated Data Processing Application Coordinator.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>ADR</strong></td>
<td colspan="3">The Administrative Data Repository is the authoritative data store within VHA for cross-cutting person administrative information. The Administrative Data Repository contains identification and cross-cutting demographics data as well as other administrative information. Patient Information Management System (PSIM) uploads the identity demographic data to the ADR. May also include subset of the Enrollment database. May also be referred to as ADR-N or ADR-L to designate a national or local instance.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>ADT</strong></td>
<td colspan="3">Admission Discharge and Transfer- Part of the Patient Information Management System (PIMS).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>ADT/HL7 PIVOT File</strong></td>
<td colspan="3">Changes to any of the fields of person information will be recorded and an entry created in the ADT/HL7 PIVOT file (#391.71). When an update to a person's treating facility occurs, this event is to be added to the ADT/HL7 PIVOT file (#391.71) and marked for transmission. A background job will collect these updates and broadcast the appropriate HL7 message (ADT-A08 Patient Update).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>AITC</strong></td>
<td colspan="3">The Master Patient Index (MPI) is located at the Austin Information Technology Center (AITC).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Alerts</strong></td>
<td colspan="3">Brief online notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide interactive notification of pending computing activities, such as the need to reorder supplies or review a patient's clinical test results. Along with the alert message is an indication that the View Alerts common option should be chosen to take further action.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Ancillary Reviewer</strong></td>
<td colspan="3">This can be a single person or group of people given the responsibility to conduct reviews of potential duplicate record pairs with data in files other than the PATIENT file (#2). For example, selected personnel in Laboratory, Radiology, and Pharmacy.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>ANSI</strong></td>
<td colspan="3">American National Standards Institute.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>ANSI M</strong></td>
<td colspan="3">The M (formerly known as MUMPS) programming language is a standard recognized by the American National Standard Institute (ANSI). M stands for Massachusetts Utility Multi-programming System.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>API</strong></td>
<td colspan="3"><p>Program calls provided for use by application programmers. APIs allow programmers to carry out standard computing activities without needing to duplicate utilities in their own software. APIs also further DBA goals of system integration by channeling activities, such as adding new users, through a limited number of callable entry points. VistA APIs fall into the following three categories:</p>
<ul>
<li><p>The first category is "Supported API" These are callable routines, which are supported for general use by all VistA applications.</p></li>
<li><p>The second category is "Controlled Subscription API." These are callable routines for which you must obtain an Integration Agreement (IA - formerly referred to as a DBIA) to use.</p></li>
<li><p>The third category is "Private API," where only a single application is granted permission to use an attribute/function of another VistA package.</p></li>
</ul>
<p>These IAs are granted for special cases, transitional problems between versions, and release coordination.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>application</strong></td>
<td colspan="3">Any software that executes logic or rules which allow people to interface with the computer and programs which collect, manipulate, summarize, and report data and information. .</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Application Coordinator</strong></td>
<td colspan="3">Designated individuals responsible for user-level management and maintenance of an application package such as IFCAP, Lab, Pharmacy, Mental Health, etc.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Application Server</strong></td>
<td colspan="3">Software/hardware for handling complex interactions between users, business logic, and databases in transaction-based, multi-tier applications. Application servers, also known as app servers, provide increased availability and higher performance.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Array</strong></td>
<td colspan="3">An arrangement of elements in one or more dimensions. An M array is a set of nodes referenced by subscripts that share the same variable name.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>AT-SIGN ("@")</strong></td>
<td colspan="3">A VA FileMan security Access code that gives the user programmer-level access to files and to VA FileMan's developer features. See Programmer Access. Also, the character "@" (i.e., at-sign, Shift-2 key on most keyboards) is used at VA FileMan field prompts to delete data.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Attribute</strong></td>
<td colspan="3"><p>VHA Definition:</p>
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
<td colspan="2"><strong>Authentication</strong></td>
<td colspan="3">Verifying the identity of the end-user.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Authorization</strong></td>
<td colspan="3">Granting or denying user access or permission to perform a function.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Auto Link Threshold or Threshold, Auto Link</strong></td>
<td colspan="3">The Auto Link Threshold is the level that a Comparison Score must meet or exceed in order for two or more Identity Profiles to be considered the same unique Person Identity.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Auto-Update</strong></td>
<td colspan="3">The term "auto-update" refers to fields that are updated from a central database (i.e., the Master Veteran Index).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Bad Address Indicator (BAI)</strong></td>
<td colspan="3"><p>The Bad Address Indicator field applies to the address at which the person resides. This field should be set as follows (if applicable):</p>
<ul>
<li><p>"UNDELIVERABLE" - Bad Address based on returned mail.</p></li>
<li><p>"HOMELESS" - Patient is known to be homeless.</p></li>
<li><p>"OTHER" - Other Bad Address Reason</p></li>
</ul>
<p>Setting this field will prevent a Bad Address from being shared with HEC and other VAMC facilities. It will also be used to block Means Test Renewal Letters from being sent. Once the Bad Address Indicator is set, incoming “newer" addresses will automatically remove the Bad Address Indicator, and allow the "updated" address to be transmitted to HEC and other VAMC Facilities.</p></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Batch Acknowledgements</strong></td>
<td colspan="3">The format of a HL7 batch acknowledgement message consists entirely of a group of ACK (acknowledgment) messages. In the case of MVI, batch acknowledgements are returned during the initialization process and during the Local/Missing ICN Resolution job. The background job files the ICN, updates the MVI, and then the associated treating facilities and systems. Data returned from this process constitute the acknowledgment of the batch message.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Batch Messages</strong></td>
<td colspan="3">There are instances when it is convenient to transfer a batch of HL7 messages. Common examples related to MVI are queries sent to the MVI for an ICN during the initialization process, the resolution of Local or Missing ICNs, and. Such a batch could be sent online using a common file transfer protocol. In the case of the MVI, the HL7 Batch Protocol uses the Batch Header Segment (BHS) and Batch Trailer Segment (BTS) message segments to delineate the batch.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>BHIE</strong></td>
<td colspan="3">Bidirectional Health Information Exchange (Bidirectional Health Information Exchange (BHIE) Web site )</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Bulletins</strong></td>
<td colspan="3">Electronic mail messages that are automatically delivered by VistA MailMan under certain conditions. For example, a bulletin can be set up to "fire" when database changes occur, such as adding a new Institution in the INSTITUTION file (#4). Bulletins are fired by bulletin-type cross-references.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Business Requirements</strong></td>
<td colspan="3"><ul>
<li><blockquote>
<p>Requirements state the customer needs the project output will satisfy. Requirements typically start with phrase “The system shall …” Business requirements refers to how the project will satisfy the business mission of the customer.</p>
</blockquote></li>
<li><blockquote>
<p>Business requirements refer to business functions of the project, such as project management, financial management, or change management.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Business Rule</strong></td>
<td colspan="3"><ul>
<li><blockquote>
<p>A policy imposed by the business, or an external entity, on the system used in the process of conducting that business.</p>
</blockquote></li>
<li><blockquote>
<p>A special category of a requirement. A business rule is directive, policy, or procedure within an organization that describes the relationship between two or more entities. Business rules may also come from outside sources such as government regulations and membership association guidelines.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Cache</strong></td>
<td colspan="3">Cache memory is a small area of very fast RAM used to speed exchange of data. Also, a file or directory included on your computer's hard drive which automatically stores the text and graphics from a web page you pull up, which, in turn, allows you to go back to that web page, without having to wait for the information to reload.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>CAIP</strong></td>
<td colspan="3">Cross-Application Integration Protocol. A framework which provides both applications and services with support for software procedure calls across systems and applications that rely upon infrastructure and middleware technologies, while simultaneously minimizing the direct dependencies of these same applications and services upon these enabling technologies.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Callable Entry Point</strong></td>
<td colspan="3">An authorized programmer call that may be used in any VistA application package. The DBA maintains the list of DBIC-approved entry points.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>CAPRI</strong></td>
<td colspan="3">Compensation &amp; Pension Records Interchange (CAPRI). This Graphical User Interface (GUI) software is used to access veterans’ electronic medical records throughout the VA. The Healthcare Identity Management (HC IdM) Team uses CAPRI as a resource for reviewing patient demographic and clinical data.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>catastrophic edit</strong></td>
<td colspan="3">Changes that occur to two or more of the specified set of identity traits during an edit of a person's record.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>CHDR</strong></td>
<td colspan="3">Clinical Data Repository (CDR) Health Data Repository</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Checksum</strong></td>
<td colspan="3">The result of a mathematical computation involving the individual characters of a routine or file.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Client</strong></td>
<td colspan="3">A single term used interchangeably to refer to the user, the workstation, and the portion of the program that runs on the workstation. In an object-oriented environment, a client is a member of a group that uses the services of an unrelated group. If the client is on a local area network (LAN), it can share resources with another computer (server).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Clinical Patient Record System (CPRS)</strong></td>
<td colspan="3">Clinical Patient Record System provides a computer-based person record and organizes and presents all relevant data on a person in a way that directly supports clinical decision-making. CPRS integrates the extensive set of clinical and administrative applications available within VistA.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Common Menu</strong></td>
<td colspan="3">The Common menu consists of options that are available to all users. Entering two question marks at the menus select prompt displays any secondary menu options available to the signed-on user, along with the common options available to all users.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Controlled Subscription Integration Agreement</strong></td>
<td colspan="3">This applies where the IA describes attributes/functions that must be controlled in their use. The decision to restrict the IA is based on the maturity of the custodian package. Typically, these IAs are created by the requesting package based on their independent examination of the custodian package's features. For the IA to be approved, the custodian grants permission to other VistA packages to use the attributes/functions of the IA; permission is granted on a one-by-one basis where each is based on a solicitation by the requesting package. An example is the extension of permission to allow a package (e.g., Spinal Cord Dysfunction) to define and update a component that is supported within the Health Summary package file structures.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Correlation</strong></td>
<td colspan="3">Comparison of person identity traits for multiple records with the Primary View in the ADR and/or MVI databases.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>COTS</strong></td>
<td colspan="3">Commercial Off The Shelf applications sold by vendors through public catalogue listings. COTS software is not intended to be customized or enhanced.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Cross Reference</strong></td>
<td colspan="3">There are several types of cross-references available. Most generally, a VA FileMan cross-reference specifies that some action be performed when the field's value is entered, changed, or deleted. For several types of cross-references, the action consists of putting the value into a list; an index used when looking-up an entry or when sorting. The regular cross-reference is used for sorting and for lookup; you can limit it to sorting only.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Data Attribute</strong></td>
<td colspan="3">A characteristic unit of data such as length, value, or method of representation. VA FileMan field definitions specify data attributes.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Data Dictionary (DD)</strong></td>
<td colspan="3"><p>The Data Dictionary is a global containing a description of the kind of data that is stored in the global corresponding to a particular file. VA FileMan uses the data internally for interpreting and processing files.</p>
<p>It contains the definitions of a file's elements (fields or data attributes), relationships to other files, and structure or design. Users generally review the definitions of a file's elements or data attributes; programmers review the definitions of a file's internal structure.</p></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Data Dictionary Access</strong></td>
<td colspan="3">A user's authorization to write/update/edit the data definition for a computer file. Also known as DD Access.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Data Integrity</strong></td>
<td colspan="3">This term refers to the condition of patient records in terms of completeness and correctness. It also refers to the process in which a particular patient’s data is synchronized at all the sites in which that person receives care.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Data Type</strong></td>
<td colspan="3">A specific field or type of information, such as Name, Social Security Number, etc.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Database</strong></td>
<td colspan="3">A set of data, consisting of at least one file, that is sufficient for a given purpose. The VistA database is composed of a number of VA FileMan files. A collection of data about a specific subject, such as the PATIENT file (#2); a data collection has different data fields (e.g. patient name, SSN, Date of Birth, and so on). An organized collection of data about a particular topic.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Database Management System (DBMS)</strong></td>
<td colspan="3">A collection of software that handles the storage, retrieval, and updating of records in a database. A Database Management System (DBMS) controls redundancy of records and provides the security, integrity, and data independence of a database.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Date of Death</strong></td>
<td colspan="3">A person may be entered as deceased at a treating facility. If a shared patient is flagged as deceased, an RG CIRN DEMOGRAPHIC ISSUES bulletin is sent to each treating facility telling where, when, and by whom the deceased date was entered. Each site can then review whether the patient should be marked as deceased at their site.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>DBA</strong></td>
<td colspan="3">Database Administrator, oversees software development with respect to VistA Standards and Conventions (SAC) such as namespacing. Also, this term refers to the Database Administration function and staff.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>DBIA</strong></td>
<td colspan="3">Database Integration Agreement (see Integration Agreements [IA]).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Default</strong></td>
<td colspan="3">Response the computer considers the most probable answer to the prompt being given. It is identified by double slash marks (//) immediately following it. This allows you the option of accepting the default answer or entering your own answer. To accept the default you simply press the Enter (or Return) key. To change the default answer, type in your response.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Demographic Data</strong></td>
<td colspan="3">Identifying descriptive data about a person, such as: name, sex, date of birth, marital status, religious preference, SSN, address, etc.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Demographics</strong></td>
<td colspan="3">Information about a person, such as name, address, service record, next of kin, and so on.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Department of Veterans Affairs</strong></td>
<td colspan="3">The Department of Veterans Affairs (formerly known as the Veterans Administration.)</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Device</strong></td>
<td colspan="3">Peripheral connected to the host computer, such as a printer, terminal, disk drive, modem, and other types of hardware and equipment associated with a computer. The host files of underlying operating systems may be treated like devices in that they may be written to (e.g., for spooling).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>DFN</strong></td>
<td colspan="3">Data File Number. This is the patient <a href="http://vaww.vista.med.va.gov/iss/acronyms/i-acronyms.asp#ien">IEN</a> (.001 Field) in the PATIENT file (#2). Additionally, this is a defined variable in VistA that refers to the IEN of the patient currently in memory.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>DHCP</strong></td>
<td colspan="3">Decentralized Hospital Computer Program (now known as Veterans Health Information Systems and Technology Architecture [VistA]). VistA software, developed by VA, is used to support clinical and administrative functions at VA Medical Centers nationwide. It is written in M and, via the Kernel, runs on all major M implementations regardless of vendor. VistA is composed of packages that undergo a verification process to ensure conformity with namespacing and other VistA standards and conventions.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Dictionary</strong></td>
<td colspan="3">Database of specifications of data and information processing resources. VA FileMan's database of data dictionaries is stored in the FILE of files (#1).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Direct Connect</strong></td>
<td colspan="3"><p>The Direct Connect is a real-time TCP/IP connection to the MPI to allow for an immediate request for an ICN. Direct Connect is activated when using any of the following PIMS options:</p>
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
<tr class="odd">
<td colspan="2"><strong>Direct Mode Utility</strong></td>
<td colspan="3">A programmer call that is made when working in direct programmer mode. A direct mode utility is entered at the MUMPS prompt (e.g., &gt;D ^XUP). Calls that are documented as direct mode utilities cannot be used in application software code.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>DNS</strong></td>
<td colspan="3">Domain Name Server</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>DOB</strong></td>
<td colspan="3">Date of Birth</td>
</tr>
<tr class="even">
<td colspan="2"><strong>DOD</strong></td>
<td colspan="3">IdM– Date of Death</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>DoD</strong></td>
<td colspan="3">Department of Defense.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Domain</strong></td>
<td colspan="3">A site for sending and receiving mail.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Double Quotes ("")</strong></td>
<td colspan="3">Symbol used in front of a Common option's menu text or synonym to select it from the Common menu. For example, the five-character string "TBOX" selects the User's Toolbox Common option.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Duplicate Record Merge</strong></td>
<td colspan="3">Patient Merge is a VistA application that provides an automated method to eliminate duplicate patient records within the VistA database (i.e., the VistA PATIENT file [#2]).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>DUZ</strong></td>
<td colspan="3">Locally defined variable in VistA that refers to the IEN of the logged on user (From the New Person file).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>DUZ(0)</strong></td>
<td colspan="3">Locally defined variable that holds the File Manager Access Code of the signed-on user.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Electronic Signature Code</strong></td>
<td colspan="3">Secret password that some users may need to establish in order to sign documents via the computer.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Eligibility Codes</strong></td>
<td colspan="3">Codes representing the basis of a person's eligibility for care.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Encryption</strong></td>
<td colspan="3">Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases encryption algorithms are one directional, that is, they only encode and the resulting data cannot be unscrambled (e.g. access/verify codes).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Entry</strong></td>
<td colspan="3">VA FileMan record. An internal entry number (IEN, the .001 field) uniquely identifies an entry in a file.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Error Trap</strong></td>
<td colspan="3">A mechanism to capture system errors and record facts about the computing context such as the local symbol table, last global reference, and routine in use. Operating systems provide tools such as the %ER utility. The Kernel provides a generic error trapping mechanism with use of the ^%ZTER global and ^XTER* routines. Errors can be trapped and, when possible, the user is returned to the menu system.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>ESR</strong></td>
<td colspan="3">Enrollment Systems Redesign is a centralized and reengineered Enrollment System.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Exception</strong></td>
<td colspan="3">A task that has encountered an error in personal data. Any Data Quality issue that requires detailed documentation. HC IdM finds an Exception based on business rules.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Extrinsic Function</strong></td>
<td colspan="3">Extrinsic function is an expression that accepts parameters as input and returns a value as output that can be directly assigned.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Facility</strong></td>
<td colspan="3">Geographic location at which VA business is performed.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>FHIE</strong></td>
<td colspan="3"><p>Federal Health Information Exchange – A Federal IT health care initiative that facilitates the secure electronic one-way exchange of patient medical information between Government health organizations.</p>
<p>The project participants are the Department of Defense (DoD) and the Department of Veterans Affairs (VA). (<a href="http://vaww.va.gov/FHIE-BHIE/">BHIE Intranet Site</a><br />
> **NOTE:** This is an internal VA Web site and is not available to the public.)</p></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Field</strong></td>
<td colspan="3">HL7: An HL7 field is a string of characters defined by one of the HL7 data types.<br />
<br />
VistA: In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file's data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Field Components</strong></td>
<td colspan="3">A field entry may also have discernible parts or components. For example, the person's name is recorded as last name, first name, and middle initial, each of which is a distinct entity separated by a component delimiter (sub-subfield in ASTM e1238-94).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>File</strong></td>
<td colspan="3">Set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>File Manager (VA FileMan)</strong></td>
<td colspan="3">VistA's Database Management System (DBMS). The central component of Kernel that defines the way standard VistA files are structured and manipulated.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>FIN</strong></td>
<td colspan="3">Foreign ID Number</td>
</tr>
<tr class="even">
<td colspan="2"><strong>FIPS</strong></td>
<td colspan="3">Standards published by the U.S. National Institute of Standards and Technology, after approval by the Department of Commerce; used as a guideline for federal procurements.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>FOIA</strong></td>
<td colspan="3">Freedom of Information Act</td>
</tr>
<tr class="even">
<td colspan="2"><strong>FORUM</strong></td>
<td colspan="3">The central E-mail system within VistA. Developers use FORUM to communicate at a national level about programming and other issues. FORUM is located at the OI Field Office—Washington, DC (162-2).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Free Text</strong></td>
<td colspan="3">A DATA TYPE that can contain any printable characters.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>FTP</strong></td>
<td colspan="3">File Transfer Protocol</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Function Point Count (FPC)</strong></td>
<td colspan="3">The function point method is used to establish a meaningful unit-of-work measure and can be used to establish baseline costs and performance level monitors. Function point analysis centers on its ability to measure the size of any software deliverable in logical, user-oriented terms. Rather than counting lines of code, function point analysis measures the functionality being delivered to the end user.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>GAL</strong></td>
<td colspan="3">Global Address List.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Gender</strong></td>
<td colspan="3"><p>The following are listed in Legacy Vista as Standard Gender values:</p>
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
<tr class="even">
<td colspan="2"><strong>Global Variable</strong></td>
<td colspan="3">Variable that is stored on disk (M usage).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>GUI</strong></td>
<td colspan="3">Graphical User Interface.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>HC IdM</strong></td>
<td colspan="3">Healthcare Identity Management</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>HDR</strong></td>
<td colspan="3">Health Data Repository – A repository of clinical information normally residing on one or more independent platforms for use by clinicians and other personnel in support of patient-centric care. The data is retrieved from heritage, transaction-oriented systems and is organized in a format to support clinical decision-making in support of patient care. Formerly known as Clinical Data Repository.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Health Level 7 (HL7) Batch Protocol</strong></td>
<td colspan="3">Protocol utilized to transmit a batch of HL7 messages. The protocol generally uses FHS, BHS, BTS and FTS segments to delineate the batch. In the case of the MPI, the protocol only uses the BHS and BTS segments.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Health Level Seven (HL7)</strong></td>
<td colspan="3">National standard for electronic data exchange/messaging protocol. HL7 messages are the dominant standard for peer-to-peer exchange of clinical, text-based information.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Health Level Seven (HL7) VistA</strong></td>
<td colspan="3">Messaging system developed as VistA software that follows the HL7 Standard for data exchange.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Healthcare Identity Management (HC IdM)</strong></td>
<td colspan="3"><p>The Healthcare Identity Management team (formerly the Identity Management Data Quality team)</p>
<ul>
<li><p>Serves as business steward for person identity data for the person's electronic health record (such as name, SSN, date of birth, gender, mother’s maiden name, place of birth) as well as managing the person's longitudinal health record across the enterprise.</p></li>
<li><p>Defines business rules and processes governing healthcare identity management data collection and maintenance.</p></li>
<li><p>Monitors and resolves data integrity issues and conflicts on the MVI and local systems related to the individual’s identity data within their health record, including the resolution of duplicates, mismatches and catastrophic edits to person identity, which affect person care and safety.</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><strong>HealtheVet-VistA</strong></td>
<td colspan="3">The next generation of VistA, HealtheVet-VistA, will retain all of the capabilities of legacy VistA but will provide enhanced flexibility for future health care and compliance with the One VA Enterprise Architecture. It will allow seamless data sharing between all parts of VA to benefit veterans and their families.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>HEC</strong></td>
<td colspan="3">Health Eligibility Center.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Help Frames</strong></td>
<td colspan="3">Entries in the HELP FRAME file (#9.2) that can be distributed with application packages to provide online documentation. Frames can be linked with other related frames to form a nested structure.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Help Prompt</strong></td>
<td colspan="3">The brief help that is available at the field level when entering one or more question marks.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>HINQ</strong></td>
<td colspan="3">Hospital Inquiry- The HINQ module provides the capability to request and obtain veteran eligibility data via the VA national telecommunications network. Individual or group requests are sent from a local computer to a remote Veterans Benefits Administration (VBA) computer where veteran information is stored. The VBA network that supports HINQ is composed of four computer systems located in regional VA payment centers.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>HIPAA</strong></td>
<td colspan="3">Health Insurance Portability and Accountability Act – A law passed by Congress in 1996 that requires the Department of Health and Human Services to implement regulations that will require the use of specific standards related to health care claims, code sets, identifiers (individual, provider, employer, and health plan), and security. Protects the privacy of individually identifiable health information.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>HL7</strong></td>
<td colspan="3">Health Level 7 – National standard for electronic data exchange/messaging protocol. A standards organization primarily focused on message-oriented middleware for healthcare. HL7 messages are the dominant standard for peer-to-peer exchange of clinical, text-based information.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>HLO</strong></td>
<td colspan="3">HL7 Optimized. VistA HL7 package routines.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>ICN</strong></td>
<td colspan="3">Persons are assigned a unique identifier, Integration Control Number (ICN), within the process of being added to the MVI database. This number links persons to their records across VHA systems. The Integration Control Number is a unique identifier assigned to patients when they are added to the MVI. The ICN follows the ASTM-E1714-95 standard for a universal health identifier.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>ID State</strong></td>
<td colspan="3"><p>An attribute of the ICN, which describes the state of the record as Permanent, Temporary, or Deactivated. ID State is composed of the following two fields from the MPI VETERAN/CLIENT file (#985):</p>
<ul>
<li><p>ID STATE (#80) is a set of codes: PERMANENT, TEMPORARY, and DEACTIVATED. Auditing is enabled for this field.</p></li>
<li><p>DATE OF ID STATE (#81) identifies when the ID STATE field was last updated.</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Identity Services</strong></td>
<td colspan="3">A business and data service that provides a consistent interface for access and maintenance of person identification to trusted client applications and services. It is the authoritative source for person identification in the Veterans Health Administration (VHA) domain.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>IdM</strong></td>
<td colspan="3">Identity Management</td>
</tr>
<tr class="even">
<td colspan="2"><strong>IdM Toolkit (IdM TK) Administrator</strong></td>
<td colspan="3">An IdM Toolkit Administrator is a user with additional privileges and security beyond the IdM Toolkit User's available functionality in the system.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>IEN</strong></td>
<td colspan="3">Internal Entry Number. The IEN number and Station Number comprise the Source ID of the person targeted for the search. The Source ID is used to uniquely identify a person.</td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>IMDQ</strong></p>
<p><strong>New name: "Healthcare Identity Management (HC IdM)"</strong></p></td>
<td colspan="3">The Identity Management Data Quality team (renamed the Healthcare Identity Management team) is a group of Data Management Analysts committed to improving and safeguarding the quality and accessibility of person data throughout the VA enterprise. They are involved in many data quality initiatives, but their primary role is to assist VHA facilities in all matters related to the MVI.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Initiate Identity Hub™</strong></td>
<td colspan="3">The Initiate Identity Hub™ is a third-party proprietary off-the-shelf software package that makes use of a Probabilistic Matching Algorithm.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Initiate Identity<br />
Hub</strong></td>
<td colspan="3">Initiate Systems Inc. software that provides a trusted on-demand system of record for multiple organizations or other entities by accurately identifying the relevant duplicate and fragmented records and linking them – within, as well as across, all data sources</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Input Template</strong></td>
<td colspan="3">A pre-defined list of fields that together comprise an editing session.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Institution</strong></td>
<td colspan="3">A Department of Veterans Affairs (VA) facility assigned a number by headquarters, as defined by Directive 97-058. An entry in the INSTITUTION file (#4) that represents the Veterans Health Administration (VHA).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Integration Agreements (IA)</strong></td>
<td colspan="3">Integration Agreements define agreements between two or more VistA software applications to allow access to one development domain by another. VistA software developers are allowed to use internal entry points (APIs) or other software-specific features that are not available to the general programming public. Any software developed for use in the VistA environment is required to adhere to this standard; as such, it applies to vendor products developed within the boundaries of DBA assigned development domains (e.g., MUMPS AudioFax). An IA defines the attributes and functions that specify access. The DBA maintains and records all IAs in the Integration Agreement database on FORUM. Content can be viewed using the DBA menu or the Health Systems Design &amp; Development's Web page.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Integration Control Number (ICN)</strong></td>
<td colspan="3">Persons are assigned a unique identifier, known as an Integration Control Number (ICN), within the process of being added to the MVI database. This number links persons to their records across VHA systems. The Integration Control Number is a unique identifier assigned to persons when they are added to the MVI. The ICN follows the ASTM-E1714-95 standard for a universal health identifier.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Internal Entry Number (IEN)</strong></td>
<td colspan="3">The number used to identify an entry within a file. Every record has a unique internal entry number.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>IRM</strong></td>
<td colspan="3">Information Resource Management. A service at VA medical centers responsible for computer management and system security.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>ISO</strong></td>
<td colspan="3">Information Security Officer.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>ISS</strong></td>
<td colspan="3">Infrastructure and Security Services (now known as Common Services Security Program).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>IV&amp;V</strong></td>
<td colspan="3"><p>IV&amp;V is the principal activity that oversees the successful implementation and execution of all internal control processes for financial and interfacing systems.</p>
<p>In order to ensure overall systems integrity, IV&amp;V is accomplished organizationally independent from the elements that acquire, design, develop or maintain the system.</p></td>
</tr>
<tr class="even">
<td colspan="2"><strong>KERNEL</strong></td>
<td colspan="3">VistA software that functions as an intermediary between the host operating system and other VistA software applications so that VistA software can coexist in a standard operating-system-independent computing environment. Kernel provides a standard and consistent user and programmer interface between software applications and the underlying M implementation.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>LAN</strong></td>
<td colspan="3">Local Area Network.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>LAYGO Access</strong></td>
<td colspan="3">A user's authorization to create a new entry when editing a computer file. (Learn As You GO allows you the ability to create new file entries.)</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>LDAP</strong></td>
<td colspan="3">Lightweight Directory Access Protocol.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Lookup</strong></td>
<td colspan="3">To find an entry in a file using a value for one of its fields.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>M (ANSI Standard)</strong></td>
<td colspan="3">Massachusetts General Hospital Utility Multi-Programming System (M, formerly named MUMPS). The Mumps language originated in the mid-60's at the Massachusetts General Hospital. Although most implementations are proprietary, consolidated into the hands of a small number of companies, an open source version of the language has been developed which is distributed freely under the GNU GPL and LGPL licenses.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Mail Message</strong></td>
<td colspan="3">An entry in the MESSAGE file (#3.9). The VistA electronic mail system (MailMan) supports local and remote networking of messages.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Mailman</strong></td>
<td colspan="3">VistA software that provides a mechanism for handling electronic communication, whether it's user-oriented mail messages, automatic firing of bulletins, or initiation of server-handled data transmissions.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Manager Account</strong></td>
<td colspan="3">UCI that can be referenced by non-manager accounts such as production accounts. Like a library, the MGR UCI holds percent routines and globals (e.g., ^%ZOSF) for shared use by other UCIs.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Mandatory Field</strong></td>
<td colspan="3">Field that requires a value. A null response is not valid.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Master Files</strong></td>
<td colspan="3">A set of common reference files used by one or more application systems. These common reference files need to be synchronized across the various applications at a given site. The Master Files Notification transactions provide a way of maintaining this synchronization.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Master Patient Index (Austin) or MPI Austin</strong></td>
<td colspan="3">The MPI is a separate computer system located at the Austin Information Technology Center. It maintains a record for VA patients and stores data such as a unique patient identifier and Treating Facility lists (which tracks the sites where that ICN is known).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Master Patient Index or MPI</strong></td>
<td colspan="3">Master Patient Index is a cross-reference or index of patients that includes the patient’s related identifiers and other patient identifying information. It is used to associate a patient’s identifiers among multiple ID-assigning entities, possibly including a Health Data Repository, to support the consolidation and sharing of a patient’s health care information across VHA. The MPI is the authoritative source for patient identity.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Master Patient Index/Patient Demographics (MPI/PD) VistA or MPI/PD</strong></td>
<td colspan="3">Master Patient Index/Patient Demographics (MPI/PD) software initializes entries in the PATIENT file (#2) with the Master Patient Index, itself. The initialization process assigns an Integration Control Number (ICN), Coordinating Master of Record (CMOR), and creates a Treating Facility list of all sites at which the patient has received care. This information is then updated in the PATIENT file (#2) at all sites where the patient has been treated.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Master Veteran Index or MVI</strong></td>
<td colspan="3">The authoritative source for person identity data. Maintains identity data for persons across VA systems. Provides a unique universal identifier for each person. Stores identity data as correlations for each system where a person is known. Provides a probabilistic matching algorithm. (Includes MPI, PSIM, and IdM TK) Maintains a “gold copy” known as a “Primary View” of the person’s identity data. Broadcasts identity trait updates to systems of interest. Maintains a record locator service.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Match Threshold</strong></td>
<td colspan="3">The Match Threshold is the level at which an Identity Profile must score against a set of identity traits in order to be considered a match. For most enterprise applications the Match Threshold would be set at or near the Auto Link Threshold. Internal Identity Management Systems (MPI/PSIM) may use a lower score, perhaps the Task Threshold, as a Match Threshold for identity management decision processes.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Menu System</strong></td>
<td colspan="3">The overall Menu Manager logic as it functions within the Kernel framework.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Menu Text</strong></td>
<td colspan="3">The descriptive words that appear when a list of option choices is displayed. Specifically, the Menu Text field of the OPTION file (#19). For example, User's Toolbox is the menu text of the XUSERTOOLS option. The option's synonym is TBOX.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Menu Text</strong></td>
<td colspan="3">The descriptive words that appear when a list of option choices is displayed. Specifically, the Menu Text field of the OPTION file (#19). For example, User's Toolbox is the menu text of the XUSERTOOLS option. The option's synonym is TBOX.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Message Segments</strong></td>
<td colspan="3">Each HL7 message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. A [ ] indicates the segment is optional, the { } indicates the segment is repeatable. For each message category, there will be a list of HL7 standard segments and/or "Z" segments used for the message.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Mirror Testing</strong></td>
<td colspan="3">Functional testing in a non-production VistA system that is maintained by the VA Medical Center (VAMC) and is normally a mirror (snapshot copy) of their production system as of the date the copy was created. The resultant “mirror” account is normally isolated from external VA systems, is scrambled to protect PHI and PII, and is refreshed (recopied from production) on a periodic basis. Users can modify mirror account data without the changes being transmitted to external systems or affecting the site’s live production database. These qualities enable site testers to execute high-priority test scenario scripts provided by the development team and note the success or failure of each script.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>MMN</strong></td>
<td colspan="3">Mother's Maiden Name: The family name under which the mother was born (i.e., before marriage). It is used to distinguish between patients with the same last name</td>
</tr>
<tr class="even">
<td colspan="2"><strong>MPI Initialization</strong></td>
<td colspan="3">The process of initializing a site's PATIENT file (#2) with the Master Patient Index (MPI). Initialization synchronizes PATIENT file (#2) information (for active shared patients) with the MPI and identifies facilities where the patient has been treated. This process transfers the Integration Control Number (ICN), and Treating Facility list for each patient to the patient's record in the VistA PATIENT file (#2) at all sites where the patient has been treated. It is also possible to initialize an individual patient to the MPI. This is done through menu options. The initial synchronization of PATIENT file (#2) information (for active, shared patients) with the Master Patient Index and with the patient's treating facilities is an important step in the implementation of the MPI/PD software system.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Namespace</strong></td>
<td colspan="3">A convention for naming VistA package elements. The Database Administrator (DBA) assigns unique character strings for package developers to use in naming routines, options, and other package elements so that packages may coexist. The DBA also assigns a separate range of file numbers to each package.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Namespacing</strong></td>
<td colspan="3">Convention for naming VistA software elements. The DBA assigns unique two to four character string prefix for software developers to use in naming routines, options, and other software elements so that software can coexist. The DBA also assigns a separate range of file numbers to each software application.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>NDBI</strong></td>
<td colspan="3">National Database Integration</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Node</strong></td>
<td colspan="3">In a tree structure, a point at which subordinate items of data originate. An M array element is characterized by a name and a unique subscript. Thus the terms: node, array element, and subscripted variable are synonymous. In a global array, each node might have specific fields or "pieces" reserved for data attributes such as name.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>NPI</strong></td>
<td colspan="3">National Provider Index</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Null</strong></td>
<td colspan="3">Empty—A field or variable that has no value associated with it is null.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Numeric Field</strong></td>
<td colspan="3">Response that is limited to a restricted number of digits. It can be dollar valued or a decimal figure of specified precision.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>OI</strong></td>
<td colspan="3">Office of Information</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>OI&amp;T</strong></td>
<td colspan="3">Office of Information Technology</td>
</tr>
<tr class="even">
<td colspan="2"><strong>OIFO</strong></td>
<td colspan="3">Office of Information Field Office.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Option</strong></td>
<td colspan="3">An entry in the OPTION file (#19). As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. Options may also be scheduled to run in the background, non-interactively, by TaskMan.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Option Name</strong></td>
<td colspan="3">Name field in the OPTION file (e.g., XUMAINT for the option that has the menu text "Menu Management"). Options are namespaced according to VistA conventions monitored by the DBA.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Package (Software)</strong></td>
<td colspan="3">The set of programs, files, documentation, help prompts, and installation procedures required for a given application (e.g., Laboratory, Pharmacy, and PIMS). A VistA software environment is composed of elements specified via the PACKAGE file (#9.4). Elements include files, associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, VistA software can be requested through the Freedom of Information Act (FOIA).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Person Correlation</strong></td>
<td colspan="3">A profile of an Identity that is maintained by an Associated System and is correlated to only one ICN. (Source - PIDS)</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Person Identification Service</strong></td>
<td colspan="3">The Person Identification Service (PIDS) is an OMG Interface Specification standard responsible for the identification, correlation, and search within and across a specified domain (A domain is a sphere of influence. For instance, a person has an identifier issued by the Social Security Administration [Social Security Number] which is different that their identifier issued by the State Department [Passport Number]. Both the Social Security Administration and State Department could be considered separate domains.) for identifiers based upon a provided set of search criteria traits. Essentially, this service provides for the assignment and reconciliation of multiple identifiers across domains and in supporting multiple implementation topologies. CORBA specification from OMG. (Source - PIDS)</td>
</tr>
<tr class="even">
<td colspan="2"><strong>PIMS</strong></td>
<td colspan="3">Patient Information Management System- VistA software package that includes Registration and Scheduling packages.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>PKI</strong></td>
<td colspan="3">Public Key Infrastructure</td>
</tr>
<tr class="even">
<td colspan="2"><strong>POB (Country)</strong></td>
<td colspan="2">PLACE OF BIRTH COUNTRY: If the person was not born in the USA, this is the country where the individual was born.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>POB (Province)</strong></td>
<td colspan="2">PLACE OF BIRTH PROVINCE: The location within certain countries that contain additional divisions of where the individual was born.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><strong>POB (City)</strong></td>
<td colspan="2">PLACE OF BIRTH CITY: The city in which this applicant was born (or foreign country if born outside the U.S.).</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>POB (State)</strong></td>
<td colspan="2">PLACE OF BIRTH STATE: State in which patient was born.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Pointer</strong></td>
<td colspan="3">The address at which a data value is stored in computer memory. A relationship between two VA FileMan files, a pointer is a file entry that references another file (forward or backward). Pointers can be an efficient means for applications to access data by referring to the storage location at which the data exists.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Potential Match Threshold</strong></td>
<td colspan="3">The level at which an Identity Profile must score against a set of identity traits in order to be considered a Potential Match for HC IdM decision processes.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Primary Key</strong></td>
<td colspan="3">A Data Base Management System construct, where one or more fields uniquely define a record (entry) in a file (table). The fields are required to be populated for every record on the file, and are unique, in combination, for every record on the file.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Primary Menu</strong></td>
<td colspan="3">The list of options presented at sign-on. Each user must have a primary menu in order to sign-on and reach Menu Manager. Users are given primary menus by Information Resource Management (IRM). This menu should include most of the computing activities the user needs.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Primary Reviewer</strong></td>
<td colspan="3">This can be a single person or group of people given the overall responsibility to initiate reviews of potential duplicate record pairs. For example, selected personnel in Patient Administration or a task force or group formed to oversee and conduct the effort of reducing or eliminating the occurrence of duplicate records in the site's database.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Primary View</strong></td>
<td colspan="3">Provides the most accurate, current, and complete identity information for a VA patient. The Primary View from the MVI business rules make determinations about data additions and updates to identity traits (Name, SSN, Date of Birth, Gender, Mother's Maiden Name, Place of Birth, and Multiple Birth Indicator) based on the authoritativeness of the update or edits as they are received by the MVI.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Private Integration Agreement</strong></td>
<td colspan="3">Where only a single application is granted permission to use an attribute/function of another VistA package. These IAs are granted for special cases, transitional problems between versions, and release coordination. A Private IA is also created by the requesting package based on their examination of the custodian package's features. Example: one package distributes a patch from another package to ensure smooth installation.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Probabilistic Comparison Score</strong></td>
<td colspan="3"><p>In a Probabilistic Search, these are the points assigned to an identity to indicate the level of confidence of matching to a given set of traits.</p>
<p>If the Comparison Score is above a certain level called the Match Threshold, then the profile is considered to be a match and the profile would be returned to the calling application.</p></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Probabilistic Matching Algorithm</strong></td>
<td colspan="3">A method to determine that a person identity profile has been matched in the PS Datastore based on the Comparison Score, which is calculated for each profile compared to the set of traits used for matching.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Probabilistic Search</strong></td>
<td colspan="3">A search using a matching algorithm to determine that a person's identity profile matches a set of defined traits. The algorithm assigns a comparison score and returns results based on a defined match threshold.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Prompt</strong></td>
<td colspan="3">The computer interacts with the user by issuing questions called prompts, to which the user issues a response.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Protocol</strong></td>
<td colspan="3">Entry in the PROTOCOL file (#101). Used by the Order Entry/Results Reporting (OE/RR) package to support the ordering of medical tests and other activities.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>PS</strong></td>
<td colspan="3">Product Support</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Pseudo SSN Reason</strong></td>
<td colspan="3">The reason that a pseudo SSN has been collected for the patient. The PSEUDO SSN REASON value is a set of codes pulled from the PATIENT (#2) file.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Pseudo-SSNs</strong></td>
<td colspan="3">False Social Security Numbers that are calculated internally to VistA and cannot be mistaken for valid SSNs because they end in P.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>PSIM</strong></td>
<td colspan="3">Person Service Identity Management (PSIM) enumerates and maintains person identities.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Queuing</strong></td>
<td colspan="3">Requesting that a job be processed in the background rather than in the foreground within the current session. Jobs are processed sequentially (first-in, first-out). Kernel's TaskMan module handles the queuing of tasks.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Queuing Required</strong></td>
<td colspan="3">Option attribute that specifies that the option must be processed by Task Manager (the option can only be queued). The option may be invoked and the job prepared for processing, but the output can only be generated during the specified times.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Receiving Site</strong></td>
<td colspan="3">Receiving Site- As it relates to HL7 Messages, it is the site that the message was sent to.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Record</strong></td>
<td colspan="3">Set of related data treated as a unit. An entry in a VA FileMan file constitutes a record. A collection of data items that refer to a specific entity (e.g., in a name-address-phone number file, each record would contain a collection of data relating to one person).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>REEME</strong></td>
<td colspan="3">Registration/Eligibility/Enrollment Maintenance and Enhancement</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Registration Process</strong></td>
<td colspan="3"><p>During a registration, the person is checked against the entries in the Master Veteran Index (MVI) to determine if the person is already established or needs to be added. As of Patch DG*5.3*915 “Enterprise Search” replaced Register Once in the registration process to include Department of Defense (DoD) patients in an “extended” patient lookup if no patients are found on the MVI.</p>
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
<tr class="even">
<td colspan="2"><strong>Remote Procedure Call (RPC)</strong></td>
<td colspan="3">Remote Procedure Call is a protocol that one program can use to request a service from a program located on another computer network. Essentially M code may take optional parameters to do some work and then return either a single value or an array back to the client application.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Requesting Site</strong></td>
<td colspan="3">Requesting Site- As is relates to HL7 Messages, it is the site initiating a message to another site requesting some action be taken.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Required Field</strong></td>
<td colspan="3">A mandatory field, one that must not be left blank. The prompt for such a field will be repeated until the user enters a valid response.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Resolution Journal Case Number</strong></td>
<td colspan="3">IDM – Number associated with each Resolution Journal Case. Used by the HealthCare Identity Management (HC IdM) team to document detailed information mostly for duplicate exception resolution but may also be used to denote details for resolving any type of exception.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>RG CIRN DEMOGRAPHIC ISSUES mail group</strong></td>
<td colspan="3"><p>The RG CIRN DEMOGRAPHIC ISSUES bulletin controls the sending of the following person related bulletin:</p>
<ul>
<li><p>Person Related Bulletin—REMOTE SENSITIVITY INDICATED</p></li>
<li><p>Cause—person is marked as sensitive at the sending site but not at receiving site.</p></li>
<li><p>Action to take—No action: message is informational</p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Routine</strong></td>
<td colspan="3">Program or a sequence of instructions called by a program that may have some general or frequent use. M routines are groups of program lines, which are saved, loaded, and called as a single unit via a specific name.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>SAC</strong></td>
<td colspan="3">Standards and Conventions. Through a process of quality assurance, all VistA software is reviewed with respect to SAC guidelines as set forth by the Standards and Conventions Committee (SACC).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>SACC</strong></td>
<td colspan="3">VistA's Standards and Conventions Committee. This Committee is responsible for maintaining the SAC.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Scheduling Options</strong></td>
<td colspan="3">The technique of requesting that Task Manager run an option at a given time, perhaps with a given rescheduling frequency.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Screen Editor</strong></td>
<td colspan="3">VA FileMan's Screen-oriented text editor. It can be used to enter data into any WORD-PROCESSING field using full-screen editing instead of line-by-line editing.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>ScreenMan Forms</strong></td>
<td colspan="3">Screen-oriented display of fields, for editing or simply for reading. VA FileMan's Screen Manager is used to create forms that are stored in the FORM file (#.403) and exported with a software application. Forms are composed of blocks (stored in the BLOCK file [#.404]) and can be regular, full screen pages or smaller, "pop-up" pages.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Screen-Oriented</strong></td>
<td colspan="3">A computer interface in which you see many lines of data at a time and in which you can move your cursor around the display screen using screen navigation commands. Compare to Scrolling Mode.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Security Key</strong></td>
<td colspan="3">The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Self Identified Gender</strong></td>
<td colspan="3"><p>The value of the Self Identified Gender field specifies the patient’s self-identified gender identity. This value will be displayed <em><u>only</u></em> if it is <em><u>not</u></em> null. The field displays as “SELF-IDENTIFIED GENDER IDENTITY.” This field is a SET of codes that specifies the patient's preferred gender:</p>
<ul>
<li><p>M = Male.</p></li>
<li><p>F = Female.</p></li>
<li><p>TM = Transmale/Transman/Female-to-Male.</p></li>
<li><p>TF = Transfemale/Transwoman/Male-to-Female.</p></li>
<li><p>O = Other.</p></li>
<li><p>N = individual chooses not to answer.</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Sending Site</strong></td>
<td colspan="3">Sending Site—As it relates to HL7 Messages, it is the site that is transmitting the message to another site.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Sensitive Patient</strong></td>
<td colspan="3">Person whose record contains certain information, which may be deemed sensitive by a facility, such as political figures, employees, patients with a particular eligibility or medical condition. If a shared patient is flagged as sensitive at one of the treating sites, a bulletin is sent to the DG SENSITIVITY mail group at each subscribing site telling where, when, and by whom the flag was set. Each site can then review whether the circumstances meet the local criteria for sensitivity flagging.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Server</strong></td>
<td colspan="3">The computer where the data and the Business Rules reside. It makes resources available to client workstations on the network. In VistA, it is an entry in the OPTION file (#19). An automated mail protocol that is activated by sending a message to a server at another location with the "S.server" syntax. A server's activity is specified in the OPTION file (#19) and can be the running of a routine or the placement of data into a file.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Set Of Codes</strong></td>
<td colspan="3">Usually a preset code with one or two characters. The computer may require capital letters as a response (e.g., M for male and F for female). If anything other than the acceptable code is entered, the computer rejects the response.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Shared Patient</strong></td>
<td colspan="3">A person who has been seen at more than one VistA site. The MVI keeps the Treating Facility list updated every time a new facility is added. The MVI broadcasts out an updates to the treating facility list, including date last treated and event reason.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Site Manager/IRM Chief</strong></td>
<td colspan="3">At each site, the individual who is responsible for managing computer systems, installing and maintaining new modules, and serving as a liaison to the CIO Field Offices.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Software (Package)</strong></td>
<td colspan="3">The set of programs, files, documentation, help prompts, and installation procedures required for a given application (e.g., Laboratory, Pharmacy, and PIMS). A VistA software environment is composed of elements specified via the PACKAGE file (#9.4). Elements include files, associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, VistA software can be requested through the Freedom of Information Act (FOIA).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Source ID</strong></td>
<td colspan="3"><p>A Source ID is a term used to describe the components that define a unique correlation. There are 4 components of a Source ID in MVI:</p>
<ol type="1">
<li><p>Assigning Authority (ex. USVHA)</p></li>
<li><p>Assigning Location (ex. Station #)</p></li>
<li><p>IDType (e.g. NI, PI, EI)</p></li>
<li><p>Internal Identifier - A code used at the assigning location used to uniquely identify a person.</p></li>
</ol>
<p>The Initiate Identity Hub also uses the term Source ID, but with a slightly different context. The Source ID in the IDHub is the unique identifier of a correlated system.. The fourth Source ID component, IEN, would translate to the Member ID in the ID HUB. Thus, the IDHub uses 2 components to uniquely identify a member: Source ID and Member ID.</p></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Spacebar Return</strong></td>
<td colspan="3">You can answer a VA FileMan prompt by pressing the spacebar and then the Return key. This indicates to VA FileMan that you would like the last response you were working on at that prompt recalled.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Special Queuing</strong></td>
<td colspan="3">Option attribute indicating that Task Manager should automatically run the option whenever the system reboots.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>SSA</strong></td>
<td colspan="3">Social Security Administration</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>SSDI</strong></td>
<td colspan="3">Social Security Death Index (SSDI). The SSDI is a database used for genealogical research as well as enabling users to locate a death certificate, find an obituary, and discover cemetery records and track down probate records. The Healthcare Identity Management (HC IdM) Team uses the SSDI (<a href="http://www.genealogybank.com/gbnk/ssdi/">Social Security Death Index Web site</a> ) as a resource for verifying patients’ dates of death.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>SSN</strong></td>
<td colspan="3">Social Security Number</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>SSN Verification Status</strong></td>
<td colspan="3"><p>Possible values of this field used on the MVI for the Enrollment System Redesign (ESR) correlation are:</p>
<ul>
<li><p>NEW RECORD</p></li>
<li><p>IN-PROCESS</p></li>
<li><p>INVALID PER SSA</p></li>
<li><p>RESEND TO SSA</p></li>
<li><p>VERIFIED</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Station Identifier</strong></td>
<td colspan="3">The number assigned to a VAMC facility or a System Association. The station identifier may be three characters in length designating the facility as a parent organization or up to six characters in length designating the facility as a child of a parent organization.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Subscriber</strong></td>
<td colspan="3">A subscriber is an entity, which receives updates to a patient's descriptive data from other sites. All treating facilities are also made subscribers as part of the MPI/PD processes.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Subscript</strong></td>
<td colspan="3">A symbol that is associated with the name of a set to identify a particular subset or element. In M, a numeric or string value that: is enclosed in parentheses, is appended to the name of a local or global variable, and identifies a specific node within an array.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Supported Reference Integration Agreement</strong></td>
<td colspan="3">This applies where any VistA application may use the attributes/functions defined by the IA (these are also called "Public "). An example is an IA that describes a standard API such as DIE or VADPT. The package that creates/maintains the Supported Reference must ensure it is recorded as a Supported Reference in the IA database. There is no need for other VistA packages to request an IA to use these references; they are open to all by default.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Synchronized Patient Data</strong></td>
<td colspan="3">Key descriptive fields in the PATIENT file (#2) that are updated in all the descriptive subscriber's PATIENT files whenever the fields are edited by a subscriber.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Systems of Interest</strong></td>
<td colspan="3">The term "systems of interest" refers to VA facilities that have seen patients and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a patient (e.g., Federal Health Information Exchange [FHIE], HomeTeleHealth, Person Service Identity Management [PSIM], Health Data Repository [HDR], etc).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Task Manager</strong></td>
<td colspan="3">Kernel module that schedules and processes background tasks (also called TaskMan)</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Task Threshold or Threshold, Task</strong></td>
<td colspan="3"><p>The Task Threshold (also called the Clerical Review Threshold) is a value that is less than the Auto Link Threshold. A Comparison Score above the Task Threshold and below the Auto Link Threshold needs to be reviewed by an Identity Management expert to determine whether the Identity Profile is either a match or not a match for the traits being compared.</p>
<p>The Task Threshold is determined and tuned by Identity Management experts and may change over time as software systems and business processes improve. The ideal goal for automated identity matching is to minimize the difference between the Task Threshold and the Auto Link Threshold.</p></td>
</tr>
<tr class="even">
<td colspan="2"><strong>TCP/IP</strong></td>
<td colspan="3">Transaction Control Protocol/Internet Protocol. A set of protocols for Layers 3 (Network) and 4 (Transfer) of the OSI network model. TCP/IP has been developed over a period of 15 years under the auspices of the Department of Defense. It is a de facto standard, particularly as higher-level layers over Ethernet. Although it builds upon the OSI model, TCP/IP is not OSI-compliant.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Template</strong></td>
<td colspan="3">Means of storing report formats, data entry formats, and sorted entry sequences. A template is a permanent place to store selected fields for use at a later time. Edit sequences are stored in the INPUT TEMPLATE file (#.402), print specifications are stored in the PRINT TEMPLATE file (#.4), and search or sort specifications are stored in the SORT TEMPLATE file (#.401).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>TIN</strong></td>
<td colspan="3">Temporary ID Number</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Toolkit (IdM TK)</strong></td>
<td colspan="3">The User Interface for the HealthCare Identity Management team. The Toolkit provides functionality to allow HC IdM staff to search and view identity and exception information. This includes the ability to view the Primary View record and any associated correlations, correlation data, history, audit trails, and HC IdM Tasks captured by MVI. In addition, functionality is provided to support the re-hosting transition for a side-by-side comparison of ADR and MVI information.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Treating Facility</strong></td>
<td colspan="3">Any facility (VAMC) where a person has applied for care, or has been added to the local PATIENT file (#2) (regardless of VISN) and has identified this person to the MVI will be placed in the TREATING FACILITY LIST file (#391.91).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Treating Facility List</strong></td>
<td colspan="3">Table of institutions at which the person has received care. This list is used to create subscriptions for the delivery of person clinical and demographic information between sites.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Trigger</strong></td>
<td colspan="3">A type of VA FileMan cross-reference. Often used to update values in the database given certain conditions (as specified in the trigger logic). For example, whenever an entry is made in a file, a trigger could automatically enter the current date into another field holding the creation date.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Trigger Event</strong></td>
<td colspan="3">The event that initiates an exchange of messages is called a trigger event. The HL7 Standard is written from the assumption that an event in the real world of health care creates the need for data to flow among systems. The real-world event is called the trigger event. For example, the trigger event "a patient is admitted" may cause the need for data about that patient to be sent to a number of other systems. There is a one-to-many relationship between message types and trigger event codes. The same trigger event code may not be associated with more than one message type.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>TSPR</strong></td>
<td colspan="3">Technical Services Project Repository</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>UAT</strong></td>
<td colspan="3">User Acceptance Testing.</td>
</tr>
<tr class="even">
<td colspan="2"><strong><u>U</u>nique <u>P</u>atient <u>I</u>dentifier (UPI)</strong></td>
<td colspan="3"><ul>
<li><p><strong>Outward Facing UPI (Social Security Number [SSN]):</strong> Requirements that apply to what the user sees (<u>outward facing</u>) should be what is currently stated in P&amp;LMS policy; currently still the Social Security Number (SSN).</p></li>
<li><p><strong>Inward Facing UPI (Integration Control Number [ICN]):</strong> Any requirements that refer to <u>inward facing</u> functions (internal clinical applications patient lookups) should use the Integration Control Number (ICN).</p></li>
<li><p><strong>Potential replacement for SSN as Outward Facing UPI (EDIPI):</strong> DoD EDIPI may eventually become the outward facing unique patient identifier (UPI), which is why the new VHIC 4.0 cards contain the EDIPI. However, there are some Veterans for whom the DoD has not provided EDIPI’s; therefore, VA has not announced the EDIPI as the official outward facing UPI and will not do so until VA and DoD have closed that gap to ensure all Veterans can be assigned the EDIPI.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>User Access</strong></td>
<td colspan="3"><p>This term is used to refer to a limited level of access, to a computer system, which is sufficient for using/operating a package, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any option, for example, can be locked with the key XUPROGMODE, which means that invoking that option requires programmer access.</p>
<p>The user's access level determines the degree of computer use and the types of computer programs available. The System Manager assigns the user an access level.</p></td>
</tr>
<tr class="even">
<td colspan="2"><strong>VA</strong></td>
<td colspan="3">Department of Veterans Affairs</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>VA Domiciliary</strong></td>
<td colspan="3">Provides comprehensive health and social services in a VA facility for eligible veterans who are ambulatory and do not require the level of care provided in nursing homes.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>VA FileMan</strong></td>
<td colspan="3">VistA's Database Management System (DBMS). The central component that defines the way standard VistA files are structured and manipulated.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>VA Hospital</strong></td>
<td colspan="3">An institution that is owned, staffed and operated by VA and whose primary function is to provide inpatient services. NOTE: Each division of an integrated medical center is counted as a separate hospital.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>VA Medical Center (VAMC)</strong></td>
<td colspan="3"><p>A unique VA site of care providing two or more types of services that reside at a single physical site location. The services provided are the primary service as tracked in the VHA Site Tracking (VAST) (i.e., VA Hospital, Nursing Home, Domiciliary, independent outpatient clinic (IOC), hospital-based outpatient clinic (HBOC), and CBOC).</p>
<p>The definition of VA medical center does not include the Vet Centers as an identifying service. NOTE: This definition was established by the Under Secretary for Health.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>VA Nursing Home Care Units (NHCU)</strong></td>
<td colspan="3">Provide care to individuals who are not in need of hospital care, but who require nursing care and related medical or psychosocial services in an institutional setting. VA NHCUs are facilities designed to care for patients who require a comprehensive care management system coordinated by an interdisciplinary team. Services provided include nursing, medical, rehabilitative, recreational, dietetic, psychosocial, pharmaceutical, radiological, laboratory, dental and spiritual.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Variable</strong></td>
<td colspan="3">Character, or group of characters, that refer(s) to a value. M (previously referred to as MUMPS) recognizes 3 types of variables: local variables, global variables, and special variables. Local variables exist in a partition of main memory and disappear at sign-off. A global variable is stored on disk, potentially available to any user. Global variables usually exist as parts of global arrays. The term "global" may refer either to a global variable or a global array. A special variable is defined by systems operations (e.g., $TEST).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>VBA SHARE</strong></td>
<td colspan="3">This is a VBA application which is utilized by the Regional Offices to access BIRLS, C&amp;P, PIF, PHF, Corporate Database, Social Security and COVERS records. The Healthcare Identity Management (HC IdM) Team uses VBA SHARE as a resource for verifying patient identity data as well as military information.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Verify Code</strong></td>
<td colspan="3">The Kernel's Sign-on/Security system uses the Verify code to validate the user's identity. This is an additional security precaution used in conjunction with the Access code. Verify codes shall be at least eight characters in length and contain three of the following four kinds of characters: letters (lower- and uppercase), numbers, and, characters that are neither letters nor numbers (e.g., "#", "@" or "$"). If entered incorrectly, the system does not allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Vet Center</strong></td>
<td colspan="3">A data source under the direct supervision of the Readjustment Counseling Service (RCS). The Vet Center provides professional readjustment counseling, community education, outreach to special populations, brokering of services with community agencies, and access to important links.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>VHA</strong></td>
<td colspan="3">Veterans Health Administration.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>VIS</strong></td>
<td colspan="3">Veterans Information Solution (VIS). This intranet-based application is designed to provide a consolidated view of information about veterans and active service members. The HC IdM Team uses VIS as a resource for verifying patient identity data as well as military information.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>VISN</strong></td>
<td colspan="3">Veterans Integrated Service Network</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>VistA</strong></td>
<td colspan="3"><p>Veterans Health Information Systems and Technology Architecture (VistA) of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA). VistA software, developed by the VA, is used to support clinical and administrative functions at VHA sites nationwide. It is both roll-and-scroll- and GUI-based software that undergoes a quality assurance process to ensure conformity with namespacing and other VistA standards and conventions (see <a href="http://vaww.oed.portal.va.gov/communities/app_dev/sac/default.aspx">SAC</a>).</p>
<p>Server-side code is written in M, and, via Kernel, runs on all major M implementations regardless of vendor. Client-side code is written in Java or Borland Delphi and runs on the Microsoft operating system.</p></td>
</tr>
<tr class="even">
<td colspan="2"><strong>VPID (replaced with ICN.)</strong></td>
<td colspan="3">Veterans Administration Personal Identifier – An enterprise-level identifier uniquely identifying VA „persons‟ across the entire VA domain.</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>WAN</strong></td>
<td colspan="3">Wide Area Network.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Z segment</strong></td>
<td colspan="3">All message type and trigger event codes beginning with Z are reserved for locally defined messages. No such codes will be defined within the HL7 Standard.</td>
</tr>
<tr class="odd">
<td colspan="2">![](mpi-pd-version-1-vista-technical-manual/056.png)</td>
<td colspan="2"><p><strong>REF:</strong> For a comprehensive list of commonly used terms and definitions, please visit the VA Web site:</p>
<p><a href="http://vaww.oed.wss.va.gov/process/Lists/glossary/default.aspx">OI&amp;T Master Glossary Web site</a></p>
<p><em><strong>NOTE:</strong> This is an internal VA Web site and is not available to the public.</em></p></td>
<td></td>
</tr>
</tbody>
</table>
