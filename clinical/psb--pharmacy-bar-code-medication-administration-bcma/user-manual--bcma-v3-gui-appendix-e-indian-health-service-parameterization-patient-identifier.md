---
title: BCMA Version 3 GUI User Manual - Appendix E (Indian Health Service Parameterization Patient Identifier)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: GUI  - Appendix E (Indian Health Service Parameterization Patient Identifier)
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 0
description: "- [Appendix E: IHS - Parameterization](#appendix-e-ihs-parameterization) - [Appendix E: IHS - Parameterization](#appendix-e-ihs-parameterization-1) - [Appendix E: IHS - Parameterization](#appendix-e-ihs-parameterization-2) - [Appendix E: IHS - Parameterization](#appendix-e-ihs-parameterization-3) - "
audience: 
keywords: 
  - patient
  - bcma
  - strong
  - parameterization
  - table
  - appendix
  - label
  - style
  - width
  - rpms
page_count: 0
word_count: 2074
section_count: 1
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_um_appendixe_ihs_par_pt_id_r0111.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_um_appendixe_ihs_par_pt_id_r0111.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

# Appendix E: IHS - Parameterization


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Appendix E: IHS - Parameterization](#appendix-e-ihs-parameterization)
- [Appendix E: IHS - Parameterization](#appendix-e-ihs-parameterization-1)
- [Appendix E: IHS - Parameterization](#appendix-e-ihs-parameterization-2)
- [Appendix E: IHS - Parameterization](#appendix-e-ihs-parameterization-3)
- [Appendix E: IHS - Parameterization](#appendix-e-ihs-parameterization-4)
- [Appendix E IHS - Parameterization](#appendix-e-ihs-parameterization-5)
- [Appendix E IHS - Parameterization](#appendix-e-ihs-parameterization-6)
<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 66%" />
<col style="width: 1%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h2 id="what-is-ihs---parameterization-of-bcma-patient-identifier">What Is IHS - Parameterization of BCMA Patient Identifier?</h2>
<h2 id="section"></h2></th>
<th colspan="3"><p>BCMA has been modified to recognize whether it is operating in the Indian Health Service (IHS) environment or the Veterans Health Administration (VHA) environment and to display the appropriate patient identifier. This enables a single version of BCMA to be maintained by VHA and yet be installed and operate in a “plug and play” fashion in an IHS or Tribal facility running Resource and Patient Management System (RPMS).</p>
<p>The IHS has adapted the current version (3.0) of BCMA to operate in the RPMS environment. The principal interactions of BCMA are with the Patient Information Management System (PIMS), Inpatient Pharmacy, and Order Entry/Results Reporting (OE/RR) packages. Each of these has a native VistA version and a modified RPMS version maintained by IHS. This enhancement requires and enables BCMA to work seamlessly alongside these packages regardless of the operating environment. In addition, the BCMA Graphical User Interface (GUI) displays vital measurements from the Veterans Administration (VA) VITALS/MEASUREMENTS package or the PCC V MEASUREMENT files, if operating in an RPMS system.</p></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="6"></td>
</tr>
<tr class="even">
<td colspan="2"><h2 id="scope">Scope</h2></td>
<td><p>The IHS Electronic Health Record GUI is implemented widely throughout the Indian Health Care System. A critical element of full Electronic Health Record (EHR) implementation in the hospital setting is the VistA BCMA application. BCMA supports the five rights of medication administration, and documents the administration of the right dose of the right medication in the right route to the right patient at the right time.</p>
<p>Under the current IHS-VHA sharing agreement, VHA has incorporated IHS requirements in VistA applications so that these applications correctly function in the RPMS environment, rather than requiring IHS modifications and management of a separate IHS version. BCMA installations recognize the local environment (RPMS or VistA) and operate appropriately.</p></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix E: IHS - Parameterization 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 67%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th><h2 id="definitions-used-in-ihs---parameterization-of-bcma-patient-identifier">Definitions Used in IHS - Parameterization of BCMA Patient Identifier </h2></th>
<th><p>The following definitions are used in the IHS – Parameterization of BCMA Patient Identifier:</p>
<ul>
<li><p><strong>ASUFAC</strong> — Area, Service Unit, Facility – 6 digit code uniquely identifying IHS and Tribal health care facilities</p></li>
<li><p><strong>BCMA</strong> — Bar Code Medication Administration</p></li>
<li><p><strong>EHR or RPMS EHR</strong> — Electronic Health Record – graphical user interface application to RPMS, analogous to CPRS</p></li>
<li><p><strong>GUI</strong> — Graphical User Interface</p></li>
<li><p><strong>HL7</strong> — Health Level 7</p></li>
<li><p><strong>HRN</strong> — Health Record Number – 6 digit patient identifier in IHS/Tribal facilities</p></li>
<li><p><strong>IHS</strong> — Indian Health Service</p></li>
<li><p><strong>OE/RR</strong> — Order Entry/Results Reporting</p></li>
<li><p><strong>PCC</strong> — Patient Care Component – RPMS application storing visit-related patient care data</p></li>
<li><p><strong>PIMS</strong> — Patient Information Management System application</p></li>
<li><p><strong>RPC</strong> — Remote Procedure Call</p></li>
<li><p><strong>RPMS</strong> — Resource and Patient Management System – health information system for IHS, analogous to VistA</p></li>
<li><p><strong>TCP</strong> — Transmission Control Protocol</p></li>
<li><p><strong>VDL</strong> — Virtual Due List</p></li>
<li><p><strong>VistA</strong> — Veterans Health Information Systems and Technology Architecture</p></li>
</ul></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"></td>
</tr>
</tbody>
</table>

|     |
|-----|

# Appendix E: IHS - Parameterization 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 28%" />
<col style="width: 0%" />
<col style="width: 68%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><h2 id="design-constraints-specifications">Design Constraints Specifications </h2></th>
<th colspan="2"><p>The existing BCMA workflow, functionality, and display are not changed.</p>
<p>The variable identifying the operational environment (the agency variable DUZ ("AG")) must be present. The RPMS PIMS was modified to produce the IHS patient identifier and cause it to print correctly on the patient wristband. This ability was delivered in RPMS PIMS*5.3*1004, December 2005.</p>
<p>.</p></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"></td>
</tr>
<tr class="even">
<td colspan="2"><h2 id="user-characteristics"><br />
<br />
<br />
<br />
User Characteristics</h2></td>
<td><p>This application is for clinicians who are responsible for administering active medication orders to “inpatients” at IHS and Tribal health care facilities and who have the following knowledge or skills:</p>
<ul>
<li><p>Experienced using and navigating around a PC or a Laptop computer</p></li>
<li><p>Experienced using a keyboard, mouse, touch screen, or touch pen</p></li>
<li><p>Experienced using Windows-based software</p></li>
<li><p>Understand how to open menus and choose commands, close dialog boxes and windows, minimize and maximize windows, and print from a software program</p></li>
<li><p>Understand the medication administration process</p></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix E: IHS - Parameterization 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="how-it-works-in-bcma"><br />
<br />
<br />
<br />
How It Works in BCMA</h2></td>
<td><p>BCMA recognizes the RPMS Health Record Number (HRN), instead of the VA’s Social Security Number (SSN) as a patient identifier, and reads vital measurement information from the RPMS Patient Care Component (instead of the VA VITALS/MEASUREMENTS package). BCMA then displays the IHS HRN, instead of the VA’s SSN on screens and reports.</p>
<h6 id="bar-code-recognition">Bar Code Recognition</h6>
<p>With this feature, the user may scan a bar-coded wristband that contains a facility code and HRN specific to the patient. In the RPMS system, the PIMS application (PIMS*5.3*1004) prints a wristband displaying a bar code that consists of a 12-digit string. The first six digits are the Area, Service Unit, Facility (ASUFAC) code which uniquely identifies the IHS, Tribal, or Urban health care facility. This code is part of the IHS standard code table. The second six digits are the HRN for the patient at that facility. If the HRN is shorter than six digits, leading zeros are inserted.</p>
<h6 id="detection-of-vital-signs-application">Detection of Vital Signs Application</h6>
<p>This feature allows BCMA to determine which vital signs application is in use at the facility (VA VITALS/MEASUREMENTS or PCC V MEASUREMENTS) and allows the user to retrieve, display, and file vitals measurement data in the appropriate locations.</p>
<h6 id="provide-ihs-output-device-support">Provide IHS Output Device Support</h6>
<p>If BCMA recognizes the RPMS operating environment, it adds the output device of OTH “OTHER” to support printing of reports in the IHS AIX operating system.</p>
<h6 id="set-system-level-patient-id-label-default">Set System Level Patient ID label default</h6>
<p>Upon installation of the server package, the System level “IHS Patient ID label” variable default value must be set. The variable is identified as PSB PATIENT ID LABEL.</p></td>
</tr>
</tbody>
</table>

# Appendix E: IHS - Parameterization 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="how-it-works-in-bcma-continued" class="H2-Continued"><br />
<br />
<br />
<br />
How It Works in BCMA (Continued)</h2></td>
<td><h6 id="bcma-site-parameters-application-additions">BCMA Site Parameters Application Additions</h6>
<p>IHS users may customize the patient identifier label used in their environment by selecting from the parameter options in the BCMA Parameters application. IHS user parameter selections are stored at the Division level and override System level values.</p>
<h6 id="add-tab-to-bcma-site-parameters-application">Add Tab to BCMA Site Parameters Application</h6>
<p>If the operating environment is RPMS, the tab entitled “IHS” is added to the Parameters application.</p>
<h6 id="add-field-to-bcma-site-parameters-application">Add Field to BCMA Site Parameters Application</h6>
<p>If the operating environment is RPMS, the field entitled “IHS Patient ID Label” is added to the “IHS” tab. This text entry field allows the user to enter a patient ID textual label of up to 5 characters. The contents of this field are displayed throughout in BCMA GUI forms and reports.</p>
<h6 id="display-patient-id-label">Display Patient ID Label</h6>
<p>If the operating environment is RPMS, and the Division level “IHS Patient ID Label” variable has no value, the program displays the System level “IHS Patient ID Label” variable value in the “IHS Patient ID Label” field.</p>
<p>If the Division level “IHS Patient ID Label” variable has a value assigned to it, the program displays the Division level “IHS Patient ID Label” variable value in the “IHS Patient ID Label” field.</p>
<p>If the operating environment is RPMS, and both Division and System level “IHS Patient ID Label” variables have no value, the program displays the “IHS Patient ID Label” field as blank and BCMA displays “PtID” as the default value for “IHS Patient ID Label.”</p>
<h6 id="when-to-set-division-level-patient-id-label-to-null">When to Set Division Level Patient ID Label to Null </h6>
<p>If the operating environment is RPMS, and the user entry for “IHS Patient ID Label” is the same as the System level value, the program sets the Division level “IHS Patient ID Label” variable to null.</p>
<h6 id="store-user-selected-patient-id-label-to-division">Store User selected Patient ID label to Division </h6>
<p>If the operating environment is RPMS, and the user entry for “IHS Patient ID Label” differs from the System level value, the program stores the user entry to the Division level variable.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix E IHS - Parameterization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="what-you-will-see"><br />
<br />
<br />
<br />
What You Will See</h2>
<h2 id="section-1"></h2></td>
<td><p>The following BCMA GUI screen examples illustrate the inclusion of the HRN patient iden<strong>tifier.</strong></p>
<p>Example: Patient Select</p>
<p>![](bcma-version-3-gui-user-manual-appendix-e-indian-health-service-parameterization/001.png)</p>
<p>Example: Patient Confirmation</p>
<h6 id="section-2">![](bcma-version-3-gui-user-manual-appendix-e-indian-health-service-parameterization/002.png)</h6>
<p>Example: Virtual Due List</p>
<p>![](bcma-version-3-gui-user-manual-appendix-e-indian-health-service-parameterization/003.png)</p></td>
</tr>
</tbody>
</table>

# Appendix E IHS - Parameterization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="what-you-will-see-continued" class="H2-Continued"><br />
<br />
<br />
<br />
What You Will See (Continued) </h2></td>
<td><p>Example: Edit Med log Administration Selection</p>
<p>![](bcma-version-3-gui-user-manual-appendix-e-indian-health-service-parameterization/004.png)</p></td>
</tr>
<tr class="even">
<td></td>
<td><p>Example: Edit Med Log</p>
<p>![](bcma-version-3-gui-user-manual-appendix-e-indian-health-service-parameterization/005.png)</p></td>
</tr>
</tbody>
</table>