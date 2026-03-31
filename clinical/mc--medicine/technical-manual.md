---
title: Medicine Version 2.3 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: MC
app_name: Medicine
section: CLI
app_status: active
pkg_ns: MC
patch_ver: 2.3
patch_id: MC*2.3
group_key: "MC:MC:2.3"
file_numbers: []
security_keys: []
menu_options: 16
description: 
audience: 
keywords: 
  - blockquote
  - class
  - style
  - width
  - even
  - table
  - contents
  - colspan
  - strong
  - colgroup
page_count: 0
word_count: 11098
section_count: 13
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: September 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Medicine/mc_2_3tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Medicine/mc_2_3tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=77"
---

Medicine

Technical MANUAL

![](medicine-version-2-3-technical-manual/001.png)

September 1996

(Revised July 2014)

Office of Information and Technology

Product Development

Revision History

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 43%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>July 2014</td>
<td>MC*2.3*43 MC*2.3*44</td>
<td><p>Converted PDF to Word document.</p>
<p>Updates for ICD-10 Patch MC*2.3*43 and Patch MC*2.3*44 as follows:</p>
<ul>
<li><blockquote>
<p>Rheumatology Line Enter/Edit Menu [MCRHMENULIN] marked UNAVAILABLE was placed out of order (p. <a href="#p43_44_37">37</a>)</p>
</blockquote></li>
<li><blockquote>
<p>Added ICR #5747 (p. <a href="#p43_44_44">44</a>)</p>
</blockquote></li>
<li><blockquote>
<p>Documentation updated to change ICD9 to ICD (p. <a href="#p43_44_82">82</a>)</p>
</blockquote></li>
<li><blockquote>
<p>Technical Edit</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>September 1996</td>
<td></td>
<td>Initial creation of document (PDF)</td>
<td></td>
</tr>
</tbody>
</table>

> Preface

> This document is provided to help the Information Resource Management technical staff maintain this release of the Medicine software.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Functional Description](#functional-description)
  - [Related Manuals](#related-manuals)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Implementation](#implementation)
  - [Maintenance](#maintenance)
    - [Name/Number Spacing](#namenumber-spacing)
    - [Journaling](#journaling)
    - [Routines](#routines)
    - [Screen Handler Files](#screen-handler-files)
    - [Reindexing](#reindexing)
- [Security](#security)
  - [File Security](#file-security)
  - [Menu Option Assignment](#menu-option-assignment)
  - [Electronic Signatures](#electronic-signatures)
  - [Security (Release Control) Keys](#security-release-control-keys)
  - [Release Control](#release-control)
  - [Release Control Options](#release-control-options)
- [Routine List](#routine-list)
- [File List](#file-list)
- [Exported Options](#exported-options)
- [Archiving and Purging](#archiving-and-purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
  - [DBI Agreements by Subscriber](#dbi-agreements-by-subscriber)
  - [Medicine Custodial DBI Agreements](#medicine-custodial-dbi-agreements)
- [Internal Relations](#internal-relations)
- [Package-wide Variables](#package-wide-variables)
- [How to Generate On-line Documentation](#how-to-generate-on-line-documentation)
- [Appendix A - Patch MC\2.3\24](#appendix-a-patch-mc2324)
- [Glossary](#glossary)
- [Index](#index)

## Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Medicine package is a VA FileMan M based computer program to serve the needs of the Department of Veterans Affairs' Medicine Service. Medical test results are organized in a manner which enable the physician to manage patient data with greater ease, as well as furnish reports for use by others in the facility, and furnish management data on a timely basis. It is an important

> part of the Decentralized Hospital Computer Program (DHCP), making maximum use of the hospital data base.

> The Medicine package is designed for entry, edit, and display of data from a large number of medical tests or procedures. Printed reports are available for all procedures.

> The modules currently included are Cardiology, Pulmonary, Gastrointestinal (GI), Hematology, Rheumatology, Pacemaker, and Generalized Procedure. Each module has a menu designed for entering, editing, and printing reports for various procedures/tests associated with that subspecialty.

> The last option on each subspecialty menu is a management menu which allows local control for the subspecialty over various files such as medications, instruments, release control, view marked for deletion, and superseded records.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Refer to the Medicine User Manual for using screen oriented entry/edit in this package. The Medicine User Manual contains information relative to using the various options of the Medicine system modules. If services are to receive only the documentation pertaining to

> their module, it is important to also include the Introduction, Summary of Patient Procedures, Problem Oriented Consult, and Index sections.

> 2\. The DHCP Lab, Order Entry/Results Reporting, Pharmacy, National Drug File, Consult/Request Tracking, Health Summary, and Adverse Reaction Tracking User Manuals may be of assistance as they contain information relative to the Medicine package.

> 3\. The Installation Guide provides instructions for installing and implementing this version of

> Medicine.

> 4\. A chapter on package security is provided in this manual for the ISO.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ❒ Insure that the following fields of the Terminal Type file (#3.2) are defined for each terminal type at your site that is being used with the Medicine package. This is necessary to provide support for the screen edit driver routines.

> XY CRT

> Erase to End of Page

> High Intensity

> Low Intensity

> ❒ The installation killed all the Data Dictionaries for the package, so if you made any local changes to the DDs, you may want to add those changes to the DDs.

> ❒ Make sure all provider users of the medicine package have an electronic signature.

> ❒ Assign security keys to the appropriate users. (See Security Keys under the Security chapter in this manual.

> ❒ Assign menu options to the appropriate users. (See Menu Option Assignment under the

> Security chapter in this manual.

> ❒ When a procedure for a patient is completed (results entered into the Medicine package) and the procedure has been signed and released, the Medicine package will send a message to a mail group and/or report to a device that contains the Patient ID, Provider ID, Patient SSN, Procedure Name, and Date/Time. If your users want this capability, within the Workload Reporting Management \[MCWKLDM\] menu do the following:

> ❒ Turn on the workload reporting toggle using the option Workload Reporting ON/OFF Toggle \[MCWKLDT\] option.

> Workload Reporting ON/OFF Toggle

> WORKLOAD REPORTING: NO// Y YES

> ❒ Set up a list of devices for the users via the Workload Reporting Device \[MCWKLDD\] option. It provides a mechanism for the user to select a printing device or devices to receive message transmissions (Patient ID, Provider ID, Patient SSN, Procedure Name, and Date/Time).

> and/or

> ❒ Make sure to define a mail group for them before using the Workload Reporting Mailgroup Selection \[MCWKLDG\] option. It provides a mechanism for the user to select a mail group to receive message transmissions (Patient ID, Provider ID, Patient SSN, Procedure Name, and Date/Time).

> Select WORKLOAD MAIL GROUP: CARDIOLOGY// Pulmonary

> Are you adding 'PULMONARY' as a new WORKLOAD MAIL GROUP (the 2ND

> for this MEDICINE PACKAGE PARAMETERS)? Y (YES)

> Select WORKLOAD MAIL GROUP: \<RET\>

> ❒ If your site is using OE/RR, turn on OE/RR using the option Enable/Disable OE/RR \[MCORHOOK\].

> Select Medicine Menu Option: Enable/Disable OE/RR

> Do you want to enable Order Entry/Results Reporting? y YES OE/RR enabled!

> ❒ The rest of set-up can be done by the users who are holding the MCMANAGER key.

> These are generally the department or assistant department heads for each subspecialty. There are specific options within each subspecialty and/or within each procedure in a subspecialty that should be used to build the data in files for that specific subspecialty or procedure.

> Release Control Options menu is found under: Cardiology Menu

> Cath Lab menu ECG Menu Echo Lab Menu EP Lab Menu

> Holter Lab menu

> Exercise Tolerance Test (ETT) Menu

> GI Menu

> GI Management Menu

> Pulmonary Menu

> Endoscopy Menu

> Pulmonary Function Test Menu

> Hematology Menu

> ❒ For those sites that want to activate Release Control and Electronic Signature, use the option Turn On Release Control/Elec. Signature. This is done for each subspecialty/procedure listed above. See Electronic Signature and Release Control in the Security chapter of this manual for more complete information. This functionality protects patient procedural data from being seen before it is completed and signed. Once it is turned on for the subspecialty or procedure, it cannot be turned off.

> Select Release Control Options (Pulmonary) Option: Turn On Release

> Control/Elec. Signature

> Electronic Signature is now turned on!

> ❒ Once you have activated Release Control and Electronic Signature, turn on the view of superseded reports using the option Allow Printing of Superseded Reports for each subspecialty and procedure above making sure the response includes "turned on". If it states "turned off", select the option again.

> Select Release Control Options (Pulmonary) Option: Allow Printing of Superseded Reports

> Superseded View (by non-manager) <u>turned on</u>

> ❒ For all but the Endoscopy Menu under Pulmonary Menu above, the users may convert old records that do not have a release status and assign them the status of Released Not Verified. It allows the non-key holders to view the old records but not to edit them.

> Select Release Control Options (CATH) Option: Convert Old Records to Released Not Verified

> Convert all records prior to: ?

> All records on or prior to this date will be converted. Any records after this date will be left as is.

> Enter an exact date less than or equal to today. Convert all records prior to: T (MAY 15, 1996)

> In order to do the conversion, you must select a provider that has the key to ELECTROPHYSIOLOGY

> Please select a Provider with a ELECTROPHYSIOLOGY key: PROVIDER,MISTER// \<RET\>

> MP 162-4 CARDIOLOGIST

> Your records are being converted. Please wait!

> A mail message will be sent to you with records that are

> converted.

> A dot is equal to 5 records..

> This is an example of the mail message following the conversion:

> Subj: Procedure File Change \[#6370\] 15 May 96 11:02 7 Lines

> From: \<Installer of Medicine\> in 'IN' basket. Page 1 \*\*NEW\*\*

> ----------------------------------------------------------------------- PROVIDER,MISTER has been

> assigned the responsibility for releasing

> the procedure results that were released not verified for the ELECTROPHYSIOLOGY procedure file.

> Only procedures on or prior to May 15, 1996 have been updated.

> The following is a list of records that has been assigned a status:

> 1 MAY 12, 1996@14:42 -Draft

> Records that have been assigned a draft status: 1

> Select MESSAGE Action: IGNORE (in IN basket)//

> Cardiology Management Menu \[MCARMGR\]

> ❒ To build a selection list of drugs for use when editing a cardiology procedure, use the option Cardiology Medication File Update.

> ❒ To build a selection list of EP interventions to be used when entering Atrial and Ventricular study data, use the option EP Intervention File Update. The interventions must be between 3 - 50 characters in length.

> GI Management Menu \[MCARGIMGR\]

> ❒ To build a selection list of drugs for use when editing a GI procedure, use the option GI Medication File Update.

> ❒ To build a selection list of endoscopic instruments, use the option Endoscopic

> Instrument Enter/Edit.

> ❒ To build a selection list of sphincterotomes, use the option Sphincterotome

> Enter/Edit.

> ❒ To build a selection list of stents, use the option Stent Enter/Edit.

> ❒ To build a selection list of gastrostomy tubes, use the option Gastrostomy Tube

> Enter/Edit.

> ❒ To build a selection list of jejunostomy tubes, use the option Jejunostomy Tube

> Enter/Edit.

> Pulmonary Management Menu

> ❒ To build a selection list of drugs for use when editing a pulmonary procedure, use the option Pulmonary Medication Update.

> ❒ To build a selection list of instruments, use the option Pulmonary Instrument

> Enter/Edit.

> ❒ To edit the PFT predicted value formulas and associate male or female to the formula, use the options Edit Predicted Value Formulas and Associate Predicted Value Formulas under the PFT Predicted Values Formulas menu. The managers may want to review the formulas that are already available before editing.

> Generalized Procedure Menu

> ❒ To build a selection list of local procedures/subspecialties for use at the GENERALIZED PROCEDURE/CONSULT SUBSPECIALTY prompt when entering a generalized procedure, use the option Procedures/Subspecialties Definition Enter/Edit under the Generalized Procedure Management menu.

## Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Besides the above implementation instructions that may be used to update and maintain the package files, the following information may be helpful for continued maintenance of the package.

### Name/Number Spacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The namespace assigned to the Medicine package is MC. All routines, globals, options, edit and print templates start with these characters. All routines generated from templates have the namespace MCARO, MCOB, MCOE, or MCOP. All files use the ^MCAR global namespace.

> The Medicine package number space is 690 through 704. The package currently uses 690 through 701. Number spaces 702 through 704 are reserved for future growth.

### Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is highly recommended that the ^MCAR global be journaled.

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The compiled print routines occupy approximately 300 K bytes and the package routines occupy approximately 447 K bytes.

### Screen Handler Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The routines MCARD\* are modified VA FileMan routines that run Screen Handler for the Medicine package. (The \* indicates all routines beginning with the given letters.)

> The Medicine screens themselves are saved in File 697.3 Medicine Screen (User). Through VA FileMan, IRM can find the following information:

> 1\) Name of the Screen

> 2\) Lines allowed in the screen: This is always 15, to allow the bottom half of the screen to be used for Commands, Help, etc. Note that at any time ^C can be typed to reprint the Command menu.

> 3\) Previous screen: This might be the parent of a sub-screen, or if you are in Screen 2 of

> 2, it might be Screen 1 of 2.

> 4\) Right-linked screen: This might be a sub-screen, or if you are in Screen 1 of 2, Screen

> 2 of 2 would be right-linked.

> 5\) DD number

> 6\) Label

> These are the fields from the file:

> A\) Starting XY coordinates of the label of the field

> B\) Field Length

> C\) Ending XY coordinates of the label of the field

> D\) Attribute \#: This is the number on the screen to the left of the label.

> E\) Type Similar to the descriptor in the DD: It allows the screen management system to decide whether the data is a set of codes, free text, pointer file, etc. An example would be: 691.18PM.

> F\) Post- and Pre-Action Code: This is similar to entry and exit actions on options.

> There are many places where the package sets fields dependent on the type of procedure.

> The following example of a Pre-action code is taken from

> MCGENDO100:

> S DJBLO=\$S(MCARGNAM="COL":"5,8,9", MCARGNAM="LAP":"1,2,3,4,8,9",MCARGNAM="ERC": "1,2,3,4,5",1:"1,2,3,4,5,8,9") D ^MCARDBL

> In the example shown, MCARGNAM is the name of the procedure and DJBLO is the variable set to show which fields should be asterisked out. If the procedure is "COL" (colonoscopy), the user will not have to enter fields 5, 8, and 9. They show as \*\*\*\*\*\*\*\*\*.

> G\) Multiple screen name

> All multiples have a separate screen name, however NOT all multiples have a sub-screen. If only the .01 field of the multiple is asked for, the user WILL NOT be moved to a sub-screen, however, if more than one field is required, a sub- screen will be provided.

> There are a few other fields that have not been previously mentioned. They include Security, Description, File Level, Highest \# used, Rd (only), and Default Value. The MCARD\* routines and the 697.3 files SHOULD NOT BE MODIFIED!

### Reindexing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A post-init killed all the cross references and rebuilt them in all the files.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 23%" />
<col style="width: 22%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 8%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>#</strong></p>
<p>690</p>
</blockquote></td>
<td><blockquote>
<p><strong>File Name</strong></p>
<p>Medical Patient</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>DD</strong></p>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p><strong>RD</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>WR</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DEL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>LAYGO</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>AUDIT</strong></p>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>690.1</p>
</blockquote></td>
<td><blockquote>
<p>Medicine Package</p>
</blockquote></td>
<td><blockquote>
<p>Parameters</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>690.2</p>
</blockquote></td>
<td><blockquote>
<p>Medicine View</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>690.5</p>
</blockquote></td>
<td><blockquote>
<p>ASTM</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>690.97</p>
</blockquote></td>
<td><blockquote>
<p>MCQ Polling</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>690.99</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>*New Person Conversion</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ECHO</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>691.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Cardiac Catheterization</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Electrocardiogram (EKG)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>691.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Holter</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Exercise Tolerance Test</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>691.8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Electrophysiology (EP)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691.9</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Atrial Study</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>692</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Ventricular Study</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>693</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Medical Description</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>693.2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Interpretation</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>693.3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ECG Interpretation</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>693.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Recording Site</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>593.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EP Intervention</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>694</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Hematology</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>694.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Indication</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>694.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Cardiac Surgery Risk Assessment</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>694.8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Procedure Term</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Medication</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Regional Wall Motion</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695.3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Cath Procedure</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Past History and Risk Factor</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Symptom</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Heart Catheter</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695.8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Reason (Medicine)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.9</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Normality of Coronary Vessel</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Segment of Coronary Arteries</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>696.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Percentage Lesion</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696.2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Lesion Morphology</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>696.3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Morphology of Distal Vessel</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Bypass Graft Segment</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>696.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Left Ventriculography</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Mitral Regurg on LV Gram</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>696.9</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Complication</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>697</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Anatomy</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>697.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Referring Physician/Agency</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>697.2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Procedure/Subspecialty</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>697.3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Medicine Screen (User)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>697.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Medical Diagnosis/ICD Codes</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>698</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Generator Implant</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>V Lead Implant</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>698.2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>A Lead Implant</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 13%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 8%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>#</strong></p>
<p>698.3</p>
</blockquote></td>
<td><blockquote>
<p><strong>File Name</strong></p>
<p>Pacemaker</p>
</blockquote></td>
<td><blockquote>
<p>Surveillance</p>
</blockquote></td>
<td><p><strong>DD</strong></p>
<p>@</p></td>
<td><blockquote>
<p><strong>RD</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>WR</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DEL</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>LAYGO</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>AUDIT</strong></p>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698.4</p>
</blockquote></td>
<td><blockquote>
<p>Pacemaker</p>
</blockquote></td>
<td><blockquote>
<p>Equipment</p>
</blockquote></td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>698.6</p>
</blockquote></td>
<td><blockquote>
<p>Pacemaker</p>
</blockquote></td>
<td><blockquote>
<p>Manufacturer</p>
</blockquote></td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698.9</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Non-Magnet ECG Rhythm</p>
</blockquote></td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Endoscopy/Consult</p>
</blockquote></td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.48</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Instrument</p>
</blockquote></td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 699.5 Generalized Procedure/Consult @ @

> 699.55 Gross @ @

> 699.57 Modifier @ @

> 699.6 Diag/Therap Intervent @ @

> 699.7 Endoscopic Device @ @

> 699.81 Results @ @

> 699.82 Consultation @ @

> 699.83 Location of Pain/Pneumonias @ @

> 699.84 Disease Evaluation @ @

> 699.85 Followup Device/Therapy @ @

> 699.86 Surveillance @ @

> 699.88 Non-Endoscopic Procedure @ @

> 700 Pulmonary Function Tests @ @

> 700.1 PFT Predicted Values @ @

> 700.2 PFT Formula @ @

> 700.5 Medicine Auto Instrument @ @ Interface Summary

> 701 Rheumatology @ @

## Menu Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The overall menu for use by IRM is the Medicine Menu \[MCMEDICINE SITE MGR MENU\].

> It contains all the user menus plus the Enable/Disable OE/RR \[MCORHOOK\] option, Summary of Patient Procedures \[MCARSUMMARY\] option, and the Workload Reporting Management \[MCWKLDM\] menu.

> The Summary of Patient Procedures \[MCARSUMMARY\] option is also exported under each subspecialty user menu. Only users with the MCMANAGER key for the subspecialty will see the management and release control menus. Users must have the key that goes with the subspecialty (See Security Keys below). The user menus should be assigned according to specialty as

> follows:

> Cardiology: MCARUSER GI: MCARGIUSER Pulmonary: MCARPULMUSER Pacemaker: MCARPACEUSER Hematology: MCARHEMUSER Rheumatology: MCRHUSER Generalized Procedure: MCGENERIC

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Electronic signatures are used to maintain the integrity of reported procedure results. The provider uses an electronic signature to authorize the release of the information to other users of the package. Editing of a record prior to release is controlled by limiting access to the record. Once released, the record cannot be edited. Make sure all physician users have an electronic signature.

## Security (Release Control) Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Security keys for each module in the Medicine package allow the user to view, release, and sign draft procedures within that module. A key is not needed to edit procedures in the draft mode. The MCMANAGER key allows the department head or assistant department head to view procedures that are Draft, Superseded, or that have been marked for deletion.

> Assign the following security keys:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 35%" />
<col style="width: 42%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><u>Module</u></p>
</blockquote></td>
<td><blockquote>
<p><u>User Keys</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Dept./Assist. Dept. Heads</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cardiology</p>
</blockquote></td>
<td><blockquote>
<p>MCKEYCARD</p>
</blockquote></td>
<td><blockquote>
<p>MCMANAGER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GI</p>
</blockquote></td>
<td><blockquote>
<p>MCKEYGI</p>
</blockquote></td>
<td><blockquote>
<p>MCMANAGER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pulmonary</p>
</blockquote></td>
<td><blockquote>
<p>MCKEYPULM</p>
</blockquote></td>
<td><blockquote>
<p>MCMANAGER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PFT</p>
</blockquote></td>
<td><blockquote>
<p>MCKEYPFT</p>
</blockquote></td>
<td><blockquote>
<p>MCMANAGER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hematology</p>
</blockquote></td>
<td><blockquote>
<p>MCKEYHEM</p>
</blockquote></td>
<td><blockquote>
<p>MCMANAGER</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Release Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Release control and electronic signatures allow the users of the Medicine package to have medical procedure records with a status of Draft, Problem Draft, Released Not Verified, Released Off-line Verified, Released On-line Verified or Superseded.

> Draft: Unless designated otherwise, all records have draft status once they are entered. A record with Draft status may be edited or deleted. An audit trail is kept of the last person to have edited the record. It is not released to non-key holders for viewing or printing in report form.

> Problem Draft: A record may be designated as Problem Draft if the information is incomplete or inaccurate. This label should alert the provider that there is some problem with the information that needs to be resolved. The record may be edited or deleted. An audit trail is kept of the last person to have edited the record. It is not released to non-key holders

> for viewing or printing in report form.

> Released Not Verified: This option is used when a record may need to be released before the information has been verified or when an authorized signature is not available. A record that has been released not verified can be marked for deletion, printed, or verified either on- or off-line at another time. An internal record is made of the person releasing the record.

> Released Off-line Verified: This option is used when the provider authorizes release of the record by signing a printed copy of the report rather than the on-line version. Another key holder is designated to make the electronic release. Both persons are recorded in the release record.

> Released On-line Verified: After reviewing a record on screen, the provider may choose to release it immediately. When this option is chosen, the provider must enter a pre- designated, unique code known as an electronic signature to authorize the release of the record. Once released, the record can no longer be edited or deleted and is available to all users in report form.

> Superseded: Occasionally, information in a verified record may need to be modified. A copy of the original record must be made using the Superseded option. The new copy is considered a draft which can be edited prior to release. The original record remains unchanged in the file. The manager controls availability of superseded records through an option on the Manager's menu. After superseding a record, the user is automatically put into Enter/Edit mode for the new record. The new record must be released either on-line or off-line at this time or it will be deleted and the old record will remain unchanged.

> The status of a record and the key that a user holds will determine the functions the user will be able to perform.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 27%" />
<col style="width: 27%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>When the record status is...</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>The holder of...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>No keys can...</p>
</blockquote></td>
<td><blockquote>
<p>Subspecialty</p>
<p>Provider Key can...</p>
</blockquote></td>
<td><blockquote>
<p>Both the Manager Key and the Subspecialty Key can...</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DRAFT</p>
</blockquote></td>
<td><blockquote>
<p>Edit* Delete*</p>
</blockquote></td>
<td><blockquote>
<p>Edit Delete View/Print</p>
<p>Assign New Status</p>
</blockquote></td>
<td><blockquote>
<p>Edit Delete View/Print</p>
<p>Assign New Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PROBLEM DRAFT</p>
</blockquote></td>
<td><blockquote>
<p>Edit* Delete*</p>
</blockquote></td>
<td><blockquote>
<p>Edit Delete View/Print</p>
<p>Assign New Status</p>
</blockquote></td>
<td><blockquote>
<p>Edit Delete View/Print</p>
<p>Assign New Status</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RELEASED NOT VERIFIED</p>
<p>(Optional)</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
</blockquote></td>
<td><blockquote>
<p>Mark for Deletion</p>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
<td><blockquote>
<p>Mark for Deletion</p>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RELEASED OFF-LINE VERIFIED</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RELEASED ON-LINE VERIFIED</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
<td><blockquote>
<p>View/Print</p>
<p>Assign New Status</p>
<p>Supersede</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SUPERSEDED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>View/Print</p>
<p>Allow View/Print</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \*Preventing non-key holders from editing and deleting records should be handled by excluding edit and delete menu options from non-key holders.

## Release Control Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The options require that the user hold the Manager's key \[MCMANAGER\] and the specific module key.

> Turn On Release Control/Elec. Signature

> This is a one-time option that turns on release control/electronic signature. This option should only be used by the manager of the department. Once this option is executed, there is no way to turn it off. Once it is turned on, the non-key holders will not be able to print a record until it is released.

> Convert Old Records to Released Not Verified

> This option converts old records or records that do not have a release status to Released Not Verified. It allows the non-key holders to view the old records but not to edit them. Before executing this option, turn on release control/electronic signature. All records upgraded using this option are assigned a status of Released Not Verified. If mass updating of records is not desirable, individual records may be updated by using the Enter/Edit option to assign them a Draft Status. Records that already have a release control status will not be affected. The responsibility for upgrading old records should be assigned to only one person.

> Print Superseded Reports

> This option allows you to display or print a superseded report.

> Allow Printing of Superseded reports

> This option is a switch that allows or disallows the non-managers to view superseded records from the print options. By switching this option to on, superseded records can be viewed from the print option. By switching this option to off, superseded records will be removed from the print option.

> Print Reports that are Marked for Deletion

> This option allows the manager to display or print reports that are marked for deletion.

> Status Report

> This option provides the manager with a report of all procedure statuses. It allows the user to select a range of dates and allows either Release statuses, Draft statuses or both.

> The release control previously used by Hematology and Pulmonary is now obsolete. Records which were given a status of Released in Medicine V. 2.0 will be assigned Released Not Verified status. Records that had Non-Released status will be assigned Draft status.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>In this Module…</p>
</blockquote></td>
<td><blockquote>
<p>Release Control options are found on this menu…</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cardiology</p>
</blockquote></td>
<td><blockquote>
<p>Cath Lab Menu ECG Menu Echo Menu</p>
<p>EP Menu</p>
<p>Holter Lab Menu</p>
<p>Exercise Tolerance Test menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Gastrointestinal</p>
</blockquote></td>
<td><blockquote>
<p>GI Management Menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Pulmonary</p>
</blockquote></td>
<td><blockquote>
<p>Endoscopy Menu</p>
<p>Pulmonary Function Menu</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hematology</p>
</blockquote></td>
<td><blockquote>
<p>Hematology Menu</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MCARAM MUSE AUTO INSTRUMENT DATA LOAD INTO DHCP MCARAM0 MUSE AUTO INSTRUMENT REINITIALIZE MCARAM0A MUSE AUTO INSTRUMENT REINIT-EXT DATE

> MCARAM0B MUSE AUTO INSTRUMENT REINIT-TRAN CORRES EKG MCARAM0C MUSE AUTO INSTRUMENT REINIT-NO DIAG

> MCARAM0D MUSE AUTO INSTRUMENT REINIT-NONDHCP NAME MCARAM0E MUSE AUTO INSTRUMENT REINIT-NOTED REC IN ERR MCARAM0F MUSE AUTO INSTRUMENT REINIT-MISS TRAN REC MCARAM0G MUSE AUTO INSTRUMENT REINIT-MISS EKG REC

> MCARAM0H MUSE AUTO INSTRUMENT REINIT-REMOVE RELEASE STATUS, ADD CONFIRMATION STATUS

> MCARAM1 MUSE TRANSFER LAB DATA TO LOCAL MCARAM2 MUSE TRANSFER LAB DATA TO LOCAL MCARAM3 MUSE TRANSFER LAB DATA TO LOCAL MCARAM4 MUSE TRANSFER LAB DATA TO LOCAL MCARAM5 MUSE TRANSFER LOCAL DATA INTO DHCP MCARAM6 MUSE LOOKUP IN DHCP

> MCARAM7 MUSE SUMMARY LOOKUP AND FILE IN DHCP MCARAML MUSE AUTO INSTRUMENT RETRANSMISSION LIST MCARAMLA MUSE AUTO RETRANSMISSION-TRAN INCOMP

> MCARAMLB MUSE AUTO INSTRUMENT RETRANSMISSION-TRAN DATE MCARAMLC MUSE AUTO INSTRUMENT RETRANSMISSION NO TRAN MCARAMLD MUSE AUTO INSTRUMENT RETRANSMISSION-NO EKG DIAG MCARAMLE MUSE AUTO INSTRUMENT RETRANSMISSION-TRAN ERRORS MCARAMLF MUSE AUTO INSTRUMENT RETRANSMISSION-NODHCP NAME MCARAMLG MUSE AUTO INSTRUMENT RETRANSMISSION-EKG CORR MCARAMLH MUSE AUTO INSTRUMENT RETRANSMISSION-CONVERT MCARAP MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY PRINT MCARAP1 MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY PRINT MCARAP2 MEDICINE AUTO INSTRUMENT INTERFACE SUMMARY PRINT

> MCARASE MEDICINE AUTO INSTRUMENT SETUP VAR FOR DATA COLLECTION MCARATVE ENTER/EDIT CARDIAC PROCEDURES

> MCARBSA COMPUTE BODY SURFACE AREA .001\*71.84\*((WT/2.2)\*\*.425\* (HT\*2.5)\*\*.725)

> MCARCNV0 CONSULT CONVERSION 699 \>\>\>===\> 699.5

> MCARCNV1 CONSULT CONVERSION 699 \>\>\>===\> 699.5

> MCARCNV2 CONSULT CONVERSION 699 \>\>\>===\> 699.5 Deleted

> MCARD SCREEN HANDLER

> MCARD1 FILL V() AFTER SELECTION

> MCARDBL UTILITY TO ASTERIK OUT ENTRIES ON SCREEN AND FUNCTIONS

> MCARDC MODIFIED DIC ROUTINE FOR MEDICINE SCREENS

> MCARDC1 READ X, SET UP ID'S, ASK OK

> MCARDCM MODIFIED DICM ROUTINE FOR MEDICINE SCREENS

> MCARDCM1 MODIFIED DICM1 ROUTINE FOR MEDICINE SCREENS

> MCARDCM2 MODIFIED DICM2 ROUTINE FOR MEDICINE SCREENS

> MCARDCM3 MODIFIED DICM3 ROUTINE FOR MEDICINE SCREEN

> MCARDCN MODIFIED DICN ROUTINE FOR MEDICINE SCREENS

> MCARDCN1 MODIFIED DICN1 ROUTINE FOR MEDICINE SCREENS

> MCARDCQ MODIFIED DICQ ROUTINE FOR MEDICINE SCREENS

> MCARDCQ1 HELP FROM DIC (MODIFIED FOR MEDICINE SCREENS)

> MCARDHLP HELP FOR SCREEN INPUT

> MCARDML MULTIPLE STACK DRIVER

> MCARDNJ INPUT TO SCREEN

> MCARDNJ1 INSERT AND LOOK UP MCARDNJ2 FUNCTION FOR DISPLAY ONLY MCARDNK SCREEN INPUT - KILLS (@) MCARDNQ SCREEN INPUT - QUESTIONMARKS

> MCARDNQ2 SCREEN INPUT - QUESTIONMARKS (PART 2) MCARDPAR INITIATE SCREEN VARIABLES

> MCARDPL DISPLAY SCREEN

> MCARDSE MEDICINE SCREEN HANDLER-PROCESS FIELD

> MCARDSS DECISION SUPPORT INTERFACE

> MCARE EDIT ROUTINES

> MCARE1 MAKES ENTRIES IN MCQ POLLING FILE

> MCARED ENTER/EDIT CARDIAC PROCEDURES-PROCESS A NEW PROCEDURE DATE

> MCAREH ENTER/EDIT CARDIAC PROCEDURES-HELP

> MCARENV MEDICINE PACKAGE INSTALLATION-ENVIRONMENT CHECK ROUTINE \#1

> MCARENV1 MEDICINE PACKAGE INSTALLATION-ENVIRONMENT CHECK ROUTINE \#2

> MCAREO ENTER/EDIT CARDIAC PROCEDURES-ORDER ENTRY HOOKS

> MCARFX22 DELETE REMARKS (A-FIB) FIELD

> MCARFXDA FIX DATA Deleted at site

> MCARGD DIAGNOSIS FILTER MCARGE GI ENTER/EDIT

> MCARGEA GI ENTER/EDIT-DISPLAY ALLERGY INFO MCARGEO GI ENTER/EDIT-ORDER ENTRY/IMAGING HOOKS

> MCARGES SCREEN ENTER/EDIT-ENDOSCOPY,HEMATOLOGY,PACEMAKER MCARGP ENDOSCOPY REPORTS

> MCARGPA PRINT ALLERGY INFO ON 'MCAROGH' PRINT TEMPLATE MCARGS SPECIAL CODE FOR PRINT TEMPLATES

> MCARHP PRINT HEMATOLOGY REPORTS

> MCARINS Installation routine for Medicine Deleted at site

> MCARLV MEDICINE PACKAGE ECHO LVINDEX MCARP PRINT ROUTINES

> MCARP1 PRINT ROUTINES TWO

> MCARPAC PRINT ROUTINES FOR PACEMAKER

> MCARPACE COMBINED GENERATOR,LEAD ENTER/EDIT

> MCARPAL PACEMAKER ACTIVE PATIENT LIST

> MCARPCE ENTER/EDIT ROUTINE FOR PACEMAKER SURVEILLANCE

> MCARPCS AUTO TRANSMIT PACEMAKER REPORT-QUEUE

> MCARPCS1 AUTO TRANSMIT PACEMAKER REPORT-LOAD

> MCARPCS2 AUTO TRANSMIT PACEMAKER REPORT-LOAD

> MCARPCS3 AUTO TRANSMIT PACEMAKER REPORT LOAD

> MCARPCS4 AUTO TRANSMIT PACEMAKER REPORT LOAD

> MCARPOS1 MEDICINE PACKAGE INSTALLATION FIRE OFF MESSAGE TO DEVELOPERS MCARPOST POST INIT Deleted at site MCARPRE MEDICINE PACKAGE INSTALLATION PREINIT AFTER USER COMMIT

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 47%" />
<col style="width: 14%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MCARPROC</p>
<p>MCARPS</p>
<p>MCARPS1</p>
<p>MCARSRE</p>
<p>MCARSRP</p>
<p>MCARSRR</p>
<p>MCARSUP</p>
<p>MCARVCHK</p>
</blockquote></td>
<td><blockquote>
<p>STORE PROCEDURES IN MEDICINE PATIENT</p>
<p>PROCEDURE SUMMARY REPORTS</p>
<p>SUMMARY OF PATIENT PROCEDURES (2)</p>
<p>CATH SURGICAL RISK ENTER/EDIT</p>
<p>CATH SURGICAL RISK REPORT</p>
<p>CATH SURGERY RISK COMPUTATION</p>
<p>MEDICINE PACKAGE MANAGEMENT OPTIONS</p>
<p>MEDICINE VIEW FILE SANITY CHECK</p>
</blockquote></td>
<td><blockquote>
<p>FILE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCBLD</p>
</blockquote></td>
<td><blockquote>
<p>TERM: SUBSPECIALTY ALLIGNER</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>Deleted</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCBLD1</p>
</blockquote></td>
<td><blockquote>
<p>MEDICINE VIEW FILE UPDATE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>at</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCBLD2</p>
</blockquote></td>
<td><blockquote>
<p>ASTM FILE UPDATE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>site</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCBPFTP1</p>
<p>MCBPFTP2</p>
<p>MCBPFTP3</p>
<p>MCBPFTP4</p>
<p>MCBPFTP5</p>
</blockquote></td>
<td><blockquote>
<p>PFT BRIEF REPORT-DEMO INFO</p>
<p>PFT BRIEF REPORT-VOLUMES</p>
<p>PFT BRIEF REPORT-FLOWS</p>
<p>PFT BRIEF REPORT-ABGS</p>
<p>PFT BRIEF REPORT-SPECIAL STUDIES (PT</p>
</blockquote></td>
<td><blockquote>
<p>1)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> MCBPFTP6 PREDICTED VALUES FOR SPECIAL STUDIES MCBPFTP7 PFT BRIEF REPORT-SPECIAL STUDIES (PT 2) MCDBELM save and load util.

> MCDBSAVE save and load util. MCDIE001 KILL ALL VARIABLES MCDIE002 KILL ALL VARIABLES MCDIE003 KILL ALL VARIABLES MCDIEDIE KILL ALL VARIABLES

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 63%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MCDUP1</p>
</blockquote></td>
<td><blockquote>
<p>Repoints the pointed to file and removes the dup</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCDUPE</p>
</blockquote></td>
<td><blockquote>
<p>Executed routine for dupr.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCDUPM</p>
</blockquote></td>
<td><blockquote>
<p>DUPLICATION FINDER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCDUPP</p>
</blockquote></td>
<td><blockquote>
<p>Post process for the Duplication</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCDUPR</p>
</blockquote></td>
<td><blockquote>
<p>Reporting of the duplicates</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCEF</p>
</blockquote></td>
<td><blockquote>
<p>FILEMAN ENTER/EDIT OF MED PROCS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCENDIQ1</p>
</blockquote></td>
<td><blockquote>
<p>GET EXTERNAL FIELD VALUE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCENV00</p>
</blockquote></td>
<td><blockquote>
<p>ENVIRONMENT CHECK ROUTINE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCENVCHK</p>
</blockquote></td>
<td><blockquote>
<p>ENVIROMENT CHECK ROUTINE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCEO</p>
</blockquote></td>
<td><blockquote>
<p>MED PROC EDIT, OE INTERFACE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCEPROC</p>
</blockquote></td>
<td><blockquote>
<p>Printer driver</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCESCON3</p>
</blockquote></td>
<td><blockquote>
<p>CONVERT RELEASE CODES TO NEW CODES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCESCONV</p>
</blockquote></td>
<td><blockquote>
<p>Convert PFTs to Electronic Signature</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCESEDT</p>
</blockquote></td>
<td><blockquote>
<p>ELECTRONIC SIGNATURE PART 1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCESEDT2</p>
</blockquote></td>
<td><blockquote>
<p>ELECTRONIC SIGNATURE EDITS PART 2</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCESHLP</p>
</blockquote></td>
<td><blockquote>
<p>Release Control Help</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCESLIST</p>
</blockquote></td>
<td><blockquote>
<p>This routine will list reports by release status</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCESMFDV</p>
</blockquote></td>
<td><blockquote>
<p>Manager Options for Mark for Deletion</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCESPRT</p>
</blockquote></td>
<td><blockquote>
<p>ELECTRONIC SIGNATURE PRINT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCESSCR</p>
</blockquote></td>
<td><blockquote>
<p>Sets up the screening for Electronic Signature</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCFIXOEP</p>
</blockquote></td>
<td><blockquote>
<p>PROTOCOL DELETION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCFSIZE</p>
</blockquote></td>
<td><blockquote>
<p>SIZE PROCEDURE FILES</p>
</blockquote></td>
<td><blockquote>
<p><strong>Deleted at site</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> MCFX005 RECOMPILE ALL OF THE MEDICINE PRINT TEMPLATES

> MCGBL PROGRAM TO DETERMINE BLANK FIELDS FOR GI

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 45%" />
<col style="width: 14%" />
<col style="width: 27%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MCL MCL610</p>
<p>MCL611</p>
<p>MCL613</p>
</blockquote></td>
<td><blockquote>
<p>POPULATE LAB FILES</p>
<p>TOPOGRAPHY FIELD FILE (#61) DATA</p>
<p>MORPHOLOGY FIELD FILE (#61.1) DATA FUNCTION FIELD FILE (#61.3) DATA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Deleted at site</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCL615</p>
</blockquote></td>
<td><blockquote>
<p>PROCEDURE FIELD FILE (#61.5) DATA</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCLPOST</p>
</blockquote></td>
<td><blockquote>
<p>CHECK THE LAB INIT</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCLPOST1</p>
</blockquote></td>
<td><blockquote>
<p>Corrects and Updates lab file</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCMAG</p>
</blockquote></td>
<td><blockquote>
<p>IMAGING LINK</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCMAGDSP</p>
</blockquote></td>
<td><blockquote>
<p>IMAGING INTERFACE</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCMENUDE</p>
</blockquote></td>
<td><blockquote>
<p>Check new person file for dangling</p>
</blockquote></td>
<td><blockquote>
<p>pointers</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> MCNMDUP Duplicate "NM" node routine for Medicine

> MCNP MEDICINE NEW PERSON CONVERSION REPORT

> MCNP0 CONVERT MEDICINE FILE PTRS FROM 3,6,16 TO 200 Deleted

> MCNP1 CONVERT MEDICINE FILE PTRS FROM 3,6,16 TO 200 at site

> MCNP2 CONVERT MEDICINE FILE PTRS FROM 3,6,16 TO 200

> MCNP2CHK UNIQUE PROVIDER NAME PRINT MCNP2X NEW PERSON CONVERSION FILE XREF

> MCNP3 CONVERT MEDICINE FILE PTRS FROM 3,6,16 TO 200

> MCNP4 MEDICINE NEW PERSON CONVERSION RPT, OPTION 1 (SUMMARY) Deleted

> MCNP5 CONVERT MEDICINE FILE PTRS TO NEW PERSON FILE - PROCESS at site

> MCNPSET MAKE AN ENTRY IN ^MCNP("CV")

> MCNPT NEW PERSON CONVERSION-ALLOW TASKING WITHOUT PRINTING

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MCNTEG</p>
</blockquote></td>
<td><blockquote>
<p>PACKAGE</p>
</blockquote></td>
<td><blockquote>
<p>CHECKSUM</p>
</blockquote></td>
<td><blockquote>
<p>CHECKER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCNTEG0</p>
</blockquote></td>
<td><blockquote>
<p>PACKAGE</p>
</blockquote></td>
<td><blockquote>
<p>CHECKSUM</p>
</blockquote></td>
<td><blockquote>
<p>CHECKER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCNTEG1</p>
<p>MCNTEG2</p>
<p>MCNTEG3</p>
</blockquote></td>
<td><blockquote>
<p>PACKAGE PACKAGE PACKAGE</p>
</blockquote></td>
<td><blockquote>
<p>CHECKSUM CHECKSUM CHECKSUM</p>
</blockquote></td>
<td><blockquote>
<p>CHECKER CHECKER CHECKER</p>
</blockquote></td>
<td><blockquote>
<p><strong>Deleted at site</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> MCNTEG4 PACKAGE CHECKSUM CHECKER MCNTEG5 PACKAGE CHECKSUM CHECKER

> MCOR OERR/MEDICINE PACKAGE LINKS

> MCOR1 OERR/MEDICINE PACKAGE LINKS (PART 2)

> MCOREX OERR/MEDICINE DATA EXTRACT UTILITY

> MCORMN Front-end for Health Summary

> MCORMN0 HL7 MESSAGE BUILDER

> MCORMN01 HL7 MESSAGE BUILDER PART 2

> MCORMN1 BUILD INTERMEDIATE DATA SET

> MCORMN2 NON-INTERACTIVE INQUIRY

> MCPARAM CHECK FOR MEDICINE PARAMETERS

> MCPFTE PULMONARY FUNCTION TEST ENTER/EDIT

> MCPFTI PFT INTERPRETATION ENTRY

> MCPFTIC COMPUTER GENERATED PFT INTERPRETATION

> MCPFTP PULMONARY FUNCTION TEST PRINT

> MCPFTP1 PFT REPORT-DEMO INFO

> MCPFTP1A PFT Report Demo Info Exit Routine

> MCPFTP2 PFT REPORT-VOLUMES

> MCPFTP2A PFT REPORT-FLOWS

> MCPFTP3 PFT REPORT-ABGS

> MCPFTP4 PFT REPORT-SPECIAL STUDIES (PT 1)

> MCPFTP4A PREDICTED VALUES FOR SPECIAL STUDIES

> MCPFTP5 PFT REPORT-SPECIAL STUDIES (PT 2)

> MCPFTR RELEASE A PFT REPORT

> MCPFTSS PFT SPECIAL STUDIES ANCILLARY

> MCPMV Medicine View file data

> MCPMVA ASTM sub-file data

> MCPOS00 POST INSTALLATION DRIVER

> MCPOS01 SEARCH AND DELETE

> MCPOS01A Kill all cross reference in a file

> MCPOS01B Kill all cross reference in a file

> MCPOS01C Kill all cross reference in a file

> MCPOS01D Kill all cross reference in a file

> MCPOS01E Kill all cross reference in a file

> MCPOS01F Kill all cross reference in a file

> MCPOS01G Kill all cross reference in a file

> MCPOS02 NEW PERSON CONVERSION

> MCPOS02A NEW PERSON CONVERSION EXCEPTION REPORT

> MCPOS03 INSTRUMENT FLAT--\>MULT CONVERSION FILE \#699

> MCPOS04 CONSULT CONVERSION 699 \>\>\>===\> 699.5

> MCPOS04A CONSULT CONVERSION 699 \>\>\>===\> 699.5

> MCPOS05 MAIL GROUP CREATION

> MCPOS06 FIX SUB DD NUMBER IN DATA NODES

> MCPOS07 UPDATE POINTERS TO LAB FILES

> MCPOS08 PUT CARDIOLOGY CODE INTO MULT IN 695

> MCPOS09 MOVE MICRO DESC REMARKS INTO WP FIELD

> MCPOS0A TERM:SUBSPECIALTY ALLIGNER

> MCPOS0B Medicine View file update

> MCPOS0C ASTM file update

> MCPOS0D UPDATE FILE SECURITY

> MCPOS0E RESTORE LOCALLY DEFINED PROCEDURES TO THE MED VIEW FILE

> MCPOS0Z CLEAN-UP XTMP

> MCPOST POST INIT9.9 TO 699 Deleted MCPOST0 VERIFIED THAT THE INITS RAN at site MCPOST1 POST INIT TO CLEAN UP STATIC FILE SPELLING ERRORS

> MCPRE00 PRE INSTALLATION DRIVER MCPRE01 PROTOCOL DELETION

> MCPRE02 FIX DATA IN PROCEDURE/SUBSPECIALTY FILE

> MCPRE03 REMOVE 'M' FROM APPLICATION PACKAGES' USE FIELD (50,63)

> MCPRE04 MCNP GLOBAL CLEANUP

> MCPRE05 CLEAN UP DATA IN INDICATION FILE (#694.1)

> MCPRE06 ICD CODE MULTIPLE CLEANUP IN MEDICAL DIAGNOSIS/ICD CODES FILE

> (#697.5)

> MCPRE07 KILL RECORDS WITH NO ZERO NODES

> MCPRE08 PFT PREDICTED VALUES FILE (700.1) CLEANUP

> MCPRE0Z DD CLEAN UP

> MCPRE1 Process which removes archaic Medicine Options - Deleted at site

> MCPREDT ENTER/EDIT PROCEDURE/SUBSPECIALTY

> MCPREDUP MEDICINE PACKAGE PRE INIT TO RUN DUPLICATE CLEAN UP

> MCPRESU1 DELETES NATIONAL FIELDS ONLY Deleted MCPRESU2 MOVE A FIELD TO A MULTIPLE at site MCPRESUB CONVERT SUBFILE HEADER NODE

> MCPSOP PHARMACY PATIENT PROFILE (MEDICINE VERS) MCPTF Medicine Term File Data

> MCRH1 RHEUMATOLOGY PATIENT HISTORY EDIT

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 37%" />
<col style="width: 5%" />
<col style="width: 19%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MCRH2</p>
</blockquote></td>
<td><blockquote>
<p>RHEUMATOLOGY ICD CODE UPDATE</p>
</blockquote></td>
<td><blockquote>
<p>FOR</p>
</blockquote></td>
<td><blockquote>
<p>QMAN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MCRINDEX</p>
</blockquote></td>
<td><blockquote>
<p>Reindex the Medicine Package</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p><strong>Deleted at site</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MCU</p>
<p>MCWORKLD</p>
<p>MCXCATH</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL UTILITY FOR MEDICINE</p>
<p>Workload reporting</p>
<p>This is a quit statement for</p>
</blockquote></td>
<td><blockquote>
<p>del</p>
</blockquote></td>
<td><blockquote>
<p>nodes of Echo</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

# File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 51%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>690</p>
</blockquote></td>
<td><blockquote>
<p>Medical Patient</p>
</blockquote></td>
<td><blockquote>
<p>This file stores Medicine patients' DINUM to the Patient file and also keeps a cross reference of procedures done on a patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>690.1</p>
</blockquote></td>
<td><blockquote>
<p>Medicine Package Parameters</p>
</blockquote></td>
<td><blockquote>
<p>This file contains information on the existence of related DHCP packages (OE/RR, PCC, Imaging) at this site.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>690.2</p>
</blockquote></td>
<td><blockquote>
<p>Medicine View</p>
</blockquote></td>
<td><blockquote>
<p>This file allows Order Entry and Health Summary to pick-up the fields within the Medicine Data base.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>690.5</p>
</blockquote></td>
<td><blockquote>
<p>ASTM</p>
</blockquote></td>
<td><blockquote>
<p>This file contains ASTM codes for the HL7 messaging builder for Medicine.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>690.97</p>
</blockquote></td>
<td><blockquote>
<p>MCQ POLLING</p>
</blockquote></td>
<td><blockquote>
<p>This file supports the loading of Patient Care Component (PCC) visit related procedure information for sites running QueryMan.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>690.99</p>
</blockquote></td>
<td><blockquote>
<p>*New Person Conversion</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the list of entries that were converted.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691</p>
</blockquote></td>
<td><blockquote>
<p>ECHO</p>
</blockquote></td>
<td><blockquote>
<p>This file stores data on Echo procedures done on a patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>691.1</p>
</blockquote></td>
<td><blockquote>
<p>Cardiac Catheterization</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the data on Catheterizations done on patients.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691.5</p>
</blockquote></td>
<td><blockquote>
<p>Electrocardiogram (EKG)</p>
</blockquote></td>
<td><blockquote>
<p>This file stores data on EKGs done on a patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>691.6</p>
</blockquote></td>
<td><blockquote>
<p>Holter</p>
</blockquote></td>
<td><blockquote>
<p>This file stores data for Holter tests done on a patient.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691.7</p>
</blockquote></td>
<td><blockquote>
<p>Exercise Tolerance Test</p>
</blockquote></td>
<td><blockquote>
<p>This file stores data on Exercise Tolerance</p>
<p>Tests done on a patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>691.8</p>
</blockquote></td>
<td><blockquote>
<p>Electrophysiology (EP)</p>
</blockquote></td>
<td><blockquote>
<p>This file stores (along with Atrial Study and Ventricular Study files) data on Electrophysiologies done on a patient.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 41%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>691.9</p>
</blockquote></td>
<td><blockquote>
<p>Atrial Study</p>
</blockquote></td>
<td><blockquote>
<p>This file stores data for Atrial studies done for a particular EP procedure. Data is entered into this file through EP options.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>692</p>
</blockquote></td>
<td><blockquote>
<p>Ventricular Study</p>
</blockquote></td>
<td><blockquote>
<p>This file stores data for Ventricular studies associated with a particular EP. Data to this file is entered through the EP options.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>693</p>
</blockquote></td>
<td><blockquote>
<p>Medical Description</p>
</blockquote></td>
<td><blockquote>
<p>This file stores a list of allowable Echo conclusions for use in the Echo option and of Hematology Bone Marrow descriptions.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>693.2</p>
</blockquote></td>
<td><blockquote>
<p>Interpretation</p>
</blockquote></td>
<td><blockquote>
<p>This file holds interpretations for Cardiac</p>
<p>Catheterization and PFT studies.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>693.3</p>
</blockquote></td>
<td><blockquote>
<p>ECG Interpretation</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the interpretations for ECG</p>
<p>procedures.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>693.5</p>
</blockquote></td>
<td><blockquote>
<p>Recording Site</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the placement sites for use in cardiac catheterization.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>693.6</p>
</blockquote></td>
<td><blockquote>
<p>EP Intervention</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the allowable interventions for EP procedures.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>694</p>
</blockquote></td>
<td><blockquote>
<p>Hematology</p>
</blockquote></td>
<td><blockquote>
<p>This file stores results of Bone Marrow</p>
<p>Aspirates and Bone Marrow Biopsies.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>694.1</p>
</blockquote></td>
<td><blockquote>
<p>Indication</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the indication for procedures for the various medical procedures.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>694.5</p>
</blockquote></td>
<td><blockquote>
<p>Cardiac Surgery Risk Assessment</p>
</blockquote></td>
<td><blockquote>
<p>This file holds data for use on the Surgical</p>
<p>Risk Assessment form.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>694.8</p>
</blockquote></td>
<td><blockquote>
<p>Procedure Term</p>
</blockquote></td>
<td><blockquote>
<p>This file provides linkage between Medicine procedures and various standard coding schemes. It also allows procedures to be called by the term of the users choice.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695</p>
</blockquote></td>
<td><blockquote>
<p>Medicine</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the medications used in the various Medicine procedures.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.1</p>
</blockquote></td>
<td><blockquote>
<p>Regional Wall Motion</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the regional wall motions associated with ECHO procedures.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 39%" />
<col style="width: 51%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>695.3</p>
</blockquote></td>
<td><blockquote>
<p>Cath Procedure</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the various procedure types of cardiac catheterization.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695.4</p>
</blockquote></td>
<td><blockquote>
<p>Past History and Risk Factor</p>
</blockquote></td>
<td><blockquote>
<p>File holds the various types of risk factors that can affect a procedure.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.5</p>
</blockquote></td>
<td><blockquote>
<p>Symptom</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the various symptoms associated with the various medical procedures.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695.6</p>
</blockquote></td>
<td><blockquote>
<p>Heart Catheter</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the various types of catheters used in catheterization.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.8</p>
</blockquote></td>
<td><blockquote>
<p>Reason (Medicine)</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the various reasons for stopping of Exercise Tolerance Tests, the reason for Generator/Lead changes for Pacemaker, and the reason for transmitting a Pacemaker report to the National Center.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695.9</p>
</blockquote></td>
<td><blockquote>
<p>Normality of Coronary Vessel</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the normality of the cardiac vessels for use by the CATHETERIZATION file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>696</p>
</blockquote></td>
<td><blockquote>
<p>Segment of Coronary Arteries</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the coronary artery segments for use by the CATHETERIZATION file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696.1</p>
</blockquote></td>
<td><blockquote>
<p>Percentage Lesion</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the lesion percentage for various segments of the Cardiac Catheterization procedures.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>696.2</p>
</blockquote></td>
<td><blockquote>
<p>Lesion Morphology</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the various morphologies pointed to by the Morphology sub-fields of the Cardiac Catheterization file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696.3</p>
</blockquote></td>
<td><blockquote>
<p>Morphology of Distal Vessel</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the allowable morphologies for distal vessels. It is pointed to by the Cardiac Catheterization file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>696.4</p>
</blockquote></td>
<td><blockquote>
<p>Bypass Graft Segment</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the various locations for the bypass graft segment. It is pointed to by the Cardiac Catheterization file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696.5</p>
</blockquote></td>
<td><blockquote>
<p>Left Ventriculography</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the left ventricular segments for use by the Cardiac Catheterization procedure.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 39%" />
<col style="width: 51%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>696.7</p>
</blockquote></td>
<td><blockquote>
<p>Mitral Regurg on LV Gram</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the types of mitral regurgitation used by the Cardiac Catheterization procedure.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696.9</p>
</blockquote></td>
<td><blockquote>
<p>Complication</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the complications associated with medical procedures.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>697</p>
</blockquote></td>
<td><blockquote>
<p>Anatomy</p>
</blockquote></td>
<td><blockquote>
<p>This file holds anatomical entries used in the</p>
<p>Medicine package.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>697.1</p>
</blockquote></td>
<td><blockquote>
<p>Referring Physician/Agency</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the various referring physicians and agencies that have made referrals for cardiac catheterizations.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>697.2</p>
</blockquote></td>
<td><blockquote>
<p>Procedure/Subspecialty</p>
</blockquote></td>
<td><blockquote>
<p>This file stores various File Manager and Screen Handler parameters associated with medical procedures, including global locations, names of File Manager full and brief input templates, and names of Screen Handler enter/edit screens.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>697.3</p>
</blockquote></td>
<td><blockquote>
<p>Medicine Screen (User)</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the screen characteristics of the medicine screen to be displayed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>697.5</p>
</blockquote></td>
<td><blockquote>
<p>Medical Diagnosis/ICD Codes</p>
</blockquote></td>
<td><blockquote>
<p>This file contains various Medical diagnoses with a screen to differentiate the area of Medicine associated with it. It also stores</p>
<p>the various ICD codes associated with each diagnosis.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698</p>
</blockquote></td>
<td><blockquote>
<p>Generator Implant</p>
</blockquote></td>
<td><blockquote>
<p>This file is used to hold the Generator Implant/Explant data for the Pacemaker portion of the Medicine package.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>698.1</p>
</blockquote></td>
<td><blockquote>
<p>V Lead Implant</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the V Lead Implant/Explant information for Pacemaker.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698.2</p>
</blockquote></td>
<td><blockquote>
<p>A Lead Implant</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the A Lead Implant/Explant information for Pacemaker.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>698.3</p>
</blockquote></td>
<td><blockquote>
<p>Pacemaker Surveillance</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the telephone/clinic follow- up data for Pacemaker.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 39%" />
<col style="width: 51%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>698.4</p>
</blockquote></td>
<td><blockquote>
<p>Pacemaker Equipment</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the various Generators, Leads, PSA Analyzers and telephone transmitters used in the Pacemaker module.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698.6</p>
</blockquote></td>
<td><blockquote>
<p>Pacemaker Manufacturer</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the manufacturer's name for the various equipment (Generators, A Leads, V Leads, PSAs, and telephone transmitters) used by Pacemaker.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>698.9</p>
</blockquote></td>
<td><blockquote>
<p>Non-Magnet ECG Rhythm</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the rhythms for use by the Basic Rhythm field of the Pacemaker Surveillance file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699</p>
</blockquote></td>
<td><blockquote>
<p>Endoscopy/Consult</p>
</blockquote></td>
<td><blockquote>
<p>This file holds all Endoscopic procedures as well as GI Non-endoscopic procedures.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.48</p>
</blockquote></td>
<td><blockquote>
<p>Instrument</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the various instruments used in medical procedures with a screen to differentiate the area of medicine.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.5</p>
</blockquote></td>
<td><blockquote>
<p>Generalized Procedure/Consult</p>
</blockquote></td>
<td><blockquote>
<p>This file stores basic information on procedures in subspecialties for which separate files do not currently exist in the Medicine package.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.55</p>
</blockquote></td>
<td><blockquote>
<p>Gross</p>
</blockquote></td>
<td><blockquote>
<p>This file holds grosses used for Endoscopic procedures with a screen to differentiate the type of sub-procedure(s) the gross is related to.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.57</p>
</blockquote></td>
<td><blockquote>
<p>Modifier</p>
</blockquote></td>
<td><blockquote>
<p>This file holds modifiers used for Endoscopic Procedures with a screen to differentiate the type of sub-procedure(s) the modifier is related to.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.6</p>
</blockquote></td>
<td><blockquote>
<p>Diag/Therap Intervent</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the techniques used in medical procedures with a screen to differentiate the type of sub-procedure(s) the technique is related to.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.7</p>
</blockquote></td>
<td><blockquote>
<p>Endoscopic Device</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the various stents, sphincterotomes, tubes, etc. used in Endoscopic procedures.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 51%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>699.81</p>
</blockquote></td>
<td><blockquote>
<p>Results</p>
</blockquote></td>
<td><blockquote>
<p>This file holds results for Endoscopic procedures.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.82</p>
</blockquote></td>
<td><blockquote>
<p>Consultation Type</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the consultation types for use in the Consult enter/edits.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.83</p>
</blockquote></td>
<td><blockquote>
<p>Location of Pain/Pneumonias</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the location of pain for GI Endoscopies and location of pneumonia for Pulmonary Endoscopy with a screen to differentiate them.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.84</p>
</blockquote></td>
<td><blockquote>
<p>Disease Evaluation</p>
</blockquote></td>
<td><blockquote>
<p>This file holds disease evaluations for use with GI/Pulmonary.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.85</p>
</blockquote></td>
<td><blockquote>
<p>Followup Device/Therapy</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the various types of follow- up devices and therapies for use with GI/Pulmonary modules.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.86</p>
</blockquote></td>
<td><blockquote>
<p>Surveillance</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the type of surveillance for use by GI/Pulmonary modules.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.88</p>
</blockquote></td>
<td><blockquote>
<p>Non-Endoscopic Procedure</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the types of Non-endoscopic procedures for use with GI module.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>700</p>
</blockquote></td>
<td><blockquote>
<p>Pulmonary Function Tests</p>
</blockquote></td>
<td><blockquote>
<p>This file stores the data on Pulmonary</p>
<p>Function Tests performed on the patient.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>700.1</p>
</blockquote></td>
<td><blockquote>
<p>PFT Predicted Values</p>
</blockquote></td>
<td><blockquote>
<p>This file holds the set of Predicted Value and Correction formulas for use by the PFT report. The formulas are selected from the PFT Formula file (700.2). There are 2 sets present (Male and Female). The Male and Female sets can be changed through the Pulmonary Managers' menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>700.2</p>
</blockquote></td>
<td><blockquote>
<p>PFT Formula</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the master list of predicted value and correction formulas for use in Pulmonary Function Tests.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 700.5 Medicine Auto Instrument Interface Summary

> This file contains one entry for each record transmitted from an auto instrument to DHCP. This file is used to print the Auto- Instrument Summary report.

> 701 Rheumatology This file stores data on Rheumatology visits.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Menu Option: Medicine Menu \[MCMEDICINE SITE MGR MENU\] Cardiology Menu \[MCARUSER\]

> \| Cath Lab Menu \[MCARCATH\]

> \| \| Enter/Edit Cath (Screen) \[MCFSCATH\]

> \| \| Cath Test Results \[MCFPCATH\]

> \| \| Line Entry/Edit of Cath Record \[MCFLCATH\]

> \| \| Image Capture \[MCARCATHIMAGE\]

> \| \| Brief Line Entry/Edit of Cath Record \[MCBLCATH\]

> \| \| Brief Enter/Edit Cath (Screen) \[MCBSCATH\]

> \| \| Brief Cath Report \[MCBPCATH\]

> \| \| Release Control Options (CATH) \[MCARCATHMANAGER\]

> \| \| \| Turn On Release Control/Elec. Signature \[MCESTONCATH\]

> \| \| \| Convert Old Records to Released Not Verified \[MCARCATHCONV\]

> \| \| \| Allow Printing of Superseded Reports \[MCESSUPONCATH\]

> \| \| \| Print Superseded Reports \[MCESSUPCATH\]

> \| \| \| Print Reports that are Marked for Deletion \[MCARCATHMFD\]

> \| \| \| Status Report \[MCESSTATUSCATH\]

> \| ECG Menu \[MCARECG\]

> \| \| Enter/Edit ECG (Screen) \[MCFSECG\]

> \| \| ECG Test Results \[MCFPECG\]

> \| \| Line ECG Entry/Edit \[MCFLECG\]

> \| \| Summary of Automated Records Transferred \[MCARECGAUTOSUM\]

> \| \| Brief Line ECG Entry/Edit \[MCBLECG\]

> \| \| Brief Enter/Edit ECG (Screen) \[MCBSECG\]

> \| \| Brief ECG Report \[MCBPECG\]

> \| \| Release Control Options (ECG) \[MCARECGMANGER\]

> \| \| \| Turn On Release Control/Elec. Signature \[MCESTONECG\]

> \| \| \| Convert Old Records to Released Not Verified \[MCARECGCONV\]

> \| \| \| Allow Printing of Superseded Reports \[MCESSUPONECG\]

> \| \| \| Print Superseded Reports \[MCESSUPECG\]

> \| \| \| Print Reports that are Marked for Deletion \[MCARECGMFD\]

> \| \| \| Status Report \[MCESSTATUSECG\]

> \| Echo Lab Menu \[MCARECHO\]

> \| \| Enter/Edit Echo (Screen) \[MCFSECHO\]

> \| \| Echo Test Results \[MCFPECHO\]

> \| \| Line Entry/Edit of ECHO test \[MCFLECHO\]

> \| \| Image Capture \[MCARECHOIMAGE\]

> \| \| Brief Line Echo Entry/Edit \[MCBLECHO\]

> \| \| Brief Enter/Edit Echo (Screen) \[MCBSECHO\]

> \| \| Brief Echo Report \[MCBPECHO\]

> \| \| Release Control Options (ECHO) \[MCARECHOMANAGER\]

> \| \| \| Turn On Release Control/Elec. Signature \[MCESTONECHO\]

> \| \| \| Convert Old Records to Released Not Verified \[MCARECHOCONV\]

> \| \| \| Print Superseded Reports \[MCESSUPECHO\]

> \| \| \| Allow Printing of Superseded Reports \[MCESSUPONECHO\]

> \| \| \| Print Reports that are Marked for Deletion \[MCARECHOMFD\]

> \| \| \| Status Report \[MCESSTATUSECHO\]

> \| EP Lab Menu \[MCAREP\]

> \| \| Enter/Edit Ep (Screen) \[MCFSEP\]

> \| \| Results of EP Tests \[MCFPEP\]

> \| \| EP Line Entry/Edit \[MCFLEP\]

> \| \| Brief EP Line Entry/Edit \[MCBLEP\]

> l MCESTONEP\]

l ed

\[MCAREPCONV\]

> Allow Printing of Superseded Reports \[MCESSUPONEP\] Print Superseded Reports \[MCESSUPEP\]

> Print Reports that are Marked for Deletion \[MCAREPMFD\] Status Report \[MCESSTATUSEP\]

> \| Holter Lab Menu \[MCARHOLTER\]

> \| \| Enter/Edit Holter (Screen) \[MCFSHOLTER\]

> \| \| Holter Test Results \[MCFPHOLTER\]

> \| \| Line Entry/Edit of Holter \[MCFLHOLTER\]

> \| \| Summary of Automated Records Transferred \[MCARHOLTAUTOSUM\]

> \| \| Brief Line Entry/Edit of Holter \[MCBLHOLTER\]

> \| \| Brief Enter/Edit Holter (Screen) \[MCBSHOLTER\]

> \| \| Brief Holter Report \[MCBPHOLTER\]

> \| \| Release Control Options (Holter) \[MCARHOLTERMANAGER\]

> \| \| \| Turn On Release Control/Elec. Signature \[MCESTONHOLTER\]

> \| \| \| Convert Old Records to Released Not Verified \[MCARHOLTERCONV\]

> \| \| \| Allow Printing of Superseded Reports \[MCESSUPONHOLTER\]

> \| \| \| Print Superseded Reports \[MCESSUPHOLTER\]

> \| \| \| Print Reports that are Marked for Deletion \[MCARHOLTERMFD\]

> \| \| \| Status Report \[MCESSTATUSHOLTER\]

> \| Exercise Tolerance Test (ETT) Menu \[MCARETT\]

> \| \| Enter/Edit ETT (Screen) \[MCFSETT\]

> \| \| ETT Results \[MCFPETT\]

> \| \| Line Entry/Edit of ETT Test \[MCFLETT\]

> \| \| Brief Line Entry/Edit of ETT \[MCBLETT\]

> \| \| Brief Enter/Edit ETT (Screen) \[MCBSETT\]

> \| \| Brief ETT Report \[MCBPETT\]

> \| \| Release Control Options (ETT) \[MCARETTMANAGER\]

> \| \| \| Turn On Release Control/Elec. Signature \[MCESTONETT\]

> \| \| \| Convert Old Records to Released Not Verified \[MCARETTCONV\]

> \| \| \| Allow Printing of Superseded Reports \[MCESSUPONETT\]

> \| \| \| Print Superseded Reports \[MCESSUPETT\]

> \| \| \| Print Reports that are Marked for Deletion \[MCARETTMFD\]

> \| \| \| Status Report \[MCESSTATUSETT\]

> \| Surgical Risk Analysis Menu \[MCARSURISKMENU\]

> \| \| Pre-Surgery Risk Analysis Enter/Edit \[MCARCATHSRAPRE\]

> \| \| Post-Surgery Risk Analysis Enter/Edit \[MCARCATHSRAPOST\]

> \| \| Pre-Surgery Risk Analysis Enter/Edit(Screen) \[MCARSRAPRE\]

> \| \| Post-Surgery Risk Analysis Enter/Edit(Screen) \[MCARSRAPOST\]

> \| \| Surgical Risk Analysis Report \[MCARCATHSRAPRINT\]

> ICONSULTEDIT\] \[MCCONSULTSCREEN\]

SULTPRINT\]

lt \[MCARGICONSULTBRIEF\]

> \| \| Brief Consult Enter/Edit (Screen) \[MCCONSULTBRSCR\]

> \| \| Brief Consult Report \[MCCONSULTBRREPORT\]

> \| Cardiology Management Menu \[MCARMGR\]

> \| \| Cardiology Medication File Update \[MCARMED\]

> \| \| EP Intervention File Update \[MCARINTUPDATE\]

> GI Menu \[MCARGIUSER\]

> \| Endoscopic Procedure Menu \[MCGIENDOSCOPIC MENU\]

> \| \| Enter/Edit GI Procedure (Line) \[MCFLGI\]

> \| \| Procedure Enter/Edit (Screen) \[MCFSGI\]

> \| \| Endoscopic Report \[MCFPGI\]

> \| \| \[MCDUMMY\]

> \| \| Diagnosis Review/Revision \[MCARGIDIAG\]

> \| \| Recall List \[MCARGIRECALLIST\]

> \| \| Image Capture \[MCARGIMAGE\]

> \| \| \[MCDUMMY\]

> \| \| Brief Enter/Edit GI Procedure \[MCBLGI\]

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 58%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Brief Procedure Enter/Edit (Screen)</p>
</blockquote></td>
<td><blockquote>
<p>[MCBSGI]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Brief Endoscopic Report [MCBPGI]</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>| Non-Endoscopic Procedures [MCGINONENDOSOPIC MENU]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Enter/Edit Non-Endoscopic Exams (Line) [MCFLNONENDO]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Enter/Edit Non-Endoscopic Exams (Screen) [MCFSNONENDO]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Non-Endoscopic Report [MCFPNONENDO]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>[MCDUMMY]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \| \| Brief Enter/Edit of Non-Endo GI Procedure \[MCBLNONENDO\]

> \| \| Brief Non-Endo Enter/Edit (Screen) \[MCBSNONENDO\]

> \| \| Brief Non-Endoscopic Report \[MCBPNONENDO\]

> ICONSULTEDIT\] \[MCCONSULTSCREEN\]

SULTPRINT\]

lt \[MCARGICONSULTBRIEF\]

> \| \| Brief Consult Enter/Edit (Screen) \[MCCONSULTBRSCR\]

> \| \| Brief Consult Report \[MCCONSULTBRREPORT\]

> \| GI Management Menu \[MCARGIMGR\]

\]

\]

MCESTONGIENDO\]

d \[MCARGICONV\]

SSUPONGI\]

> \[MCARGIMFD\] \[MCARGIMFDED\]

rt \[MCARGIMFDNON\]

> Pulmonary Menu \[MCARPULMUSER\]

> \| Endoscopy Menu \[MCPULMENDOMENU\]

> \| \| Endoscopy Enter/Edit \[MCFLPULM\]

> \| \| Endoscopy Enter/Edit (Screen) \[MCFSPULM\]

> \| \| Endoscopic Report \[MCFPPULM\]

> \| \| Diagnosis Review/Revision \[MCARPULMDIAG\]

> \| \| Recall List \[MCARPULMRECALLIST\]

> \| \| Image Capture \[MCARPULMIMAGE\]

> \| \| Brief Endoscopy Enter/Edit \[MCBLPULM\]

> \| \| Brief Endoscopy Enter/Edit (Screen) \[MCBSPULM\]

> \| \| Brief Endoscopy Report \[MCBPPULM\]

> \| \| Release Control Options (Pulmonary) \[MCARPULMENDMANG\]

> \| \| \| Turn On Release Control/Elec. Signature \[MCESTONPULM\]

> \| \| \| Allow Printing of Superseded Reports \[MCESSUPONPULM\]

> \| \| \| Print Superseded Reports \[MCESSUPPULM\]

> \| \| \| Print Reports that are Marked for Deletion \[MCARPULMENDOMFD\]

> \| \| \| Status Report \[MCESSTATUSPULM\]

> \| Pulmonary Function Test Menu \[MCARPULMPFT\]

> FT\]

> \| \| Release Control Options (PFT) \[MCPFTMANAGER\]

> \| \| \| Turn On Release Control/Elec. Signature \[MCESTONPFT\]

fied

\[MCARPFTCONV\]

MCESSUPONPFT\]

on \[MCARPFTMFD\]

> ICONSULTEDIT\] \[MCCONSULTSCREEN\]

SULTPRINT\]

lt \[MCARGICONSULTBRIEF\]

> \| \| Brief Consult Enter/Edit (Screen) \[MCCONSULTBRSCR\]

> \| \| Brief Consult Report \[MCCONSULTBRREPORT\]

> \| Pulmonary Management Menu \[MCARPULMGR\]

> \| \| Pulmonary Medication Update \[MCARMEDPULM\]

> \| \| Pulmonary Instrument Enter/Edit \[MCARPULMINST\]

> \| \| PFT Predicted Values Formulas \[MCPFTPREDVALUES\]

> \| \| \| Edit Predicted Value Formulas \[MCPFTPVFEDT\]

> \| \| \| Associate Predicted Value Formulas \[MCPFTPVFASS\]

> Hematology Menu \[MCARHEMUSER\]

> \| Enter/Edit Hematology Procedures \[MCFLHEM\]

> \| Enter/Edit Hematology Procedures (Screen) \[MCFSHEM\]

> \| Hematology Report \[MCFPHEM\]

> \| Summary of Patient Procedures \[MCARSUMMARY\]

> \| Problem Oriented Consult Menu \[MCCONSULT MENU\]

> \| \| Problem Oriented Consult Enter/Edit \[MCARGICONSULTEDIT\]

> \| \| Problem Oriented Consult Enter/Edit (Screen) \[MCCONSULTSCREEN\]

> \| \| Problem Oriented Consult Report \[MCARGICONSULTPRINT\]

> \| \| Brief Enter/Edit of a Problem Oriented Consult \[MCARGICONSULTBRIEF\]

> \| \| Brief Consult Enter/Edit (Screen) \[MCCONSULTBRSCR\]

> \| \| Brief Consult Report \[MCCONSULTBRREPORT\]

> \| Image Capture \[MCARHEMIMAGE\]

> \| Brief Enter/Edit of Hematology Procedures \[MCBLHEM\]

> \| Brief Hematology Enter/Edit (Screen) \[MCBSHEM\]

> \| Brief Hematology Report \[MCBPHEM\]

> \| Release Control Options (Hematology) \[MCARHEMGR\]

> \| \| Turn On Release Control/Elec. Signature \[MCESTONHEM\]

> \| \| Convert Old Records to Released Not Verified \[MCARHEMCONV\]

> \| \| Allow Printing of Superseded Reports \[MCESSUPONHEM\]

> \| \| Print Superseded Reports \[MCESSUPHEM\]

> \| \| Print Reports that are Marked for Deletion \[MCARHEMMFD\]

> \| \| Status Report \[MCESSTATUSHEM\]

> Pacemaker Menu \[MCARPACEUSER\]

> \| Enter/Edit Menu (Line Entry) \[MCARPACEDITLINE\]

> \| \| Combined Implant/Leads Enter/Edit \[MCARPACEMULTEDIT\]

> \| \| Generator Implant/Explant Enter/Edit \[MCARPACEGENIMP\]

> \| \| A-Lead Implant/Explant Enter/Edit \[MCFLALEAD\]

> \| \| V-Lead Implant/Explant Enter/Edit \[MCFLVLEAD\]

> \| \| Surveillance Enter/Edit \[MCFLSURV\]

> \| \| Demographic Data Enter/Edit \[MCARPACEDIT\]

> \| \| Brief Generator Implant/Explant Enter/Edit \[MCBLGENE\]

> \| \| Brief A-Lead Implant/Explant Entry/Edit \[MCBLALEAD\]

> \| \| Brief V-Lead Implant/Explant Enter/Edit \[MCBLVLEAD\]

> \| \| Brief Surveillance Enter/Edit \[MCBLSURV\]

> \| Enter/Edit Menu (Screen Entry) \[MCARPACESCREENMENU\]

> \| \| Combined Implant/Leads Enter/Edit \[MCFSMULTI\]

> \| \| Generator Implant/Explant Enter/Edit \[MCFSGEN.IMPL.\]

> \| \| A-Lead Implant/Explant Enter/Edit \[MCFSALEAD\]

> \| \| V-Lead Implant/Explant Enter/Edit \[MCFSVLEAD\]

> \| \| Surveillance Enter/Edit \[MCARPACESCREENSURV\]

> \| \| Demographic Data Enter/Edit \[MCARPACESCREENDEMO\]

> BSGENI\] \[MCBSALEAD\] \[MCBSVLEAD\]

> MCPACSURVBRSCR\]

enter

\]

\[MCARPACETRANS\]

> \| Pacemaker Management Menu \[MCARPACEMGR\]

> \| \| Equipment Update \[MCARPACEQUIP\]

EPORT\]

> \| \| Manufacturer's List Update \[MCARPACEMANUF\] Rheumatology Menu \[MCRHUSER\]

> \| Diagnosis Edit \[MCRHDIAGF\]

> \| Add NEW visit/display Patient Background Info. \[MCRHBACKF\]

> \| History Narrative Edit \[MCRHNARRF\]

> \| Display Serial Laboratory Info. \[MCRHLABF\]

> \| Display/Print Drug Treatment Program \[MCRHTREAT\]

> \| Health Assessment (HAQ) Edit \[MCRHHAQF\]

> \| Health/Physical History Edit \[MCRHPATHISTF\]

> \| Physical Examination Edit \[MCRHPHYSF\]

> \| Death Admin Edit \[MCRHDEATHF\]

> \| Print Menu \[MCRHMENUPRT\]

> \| \| Diagnosis Print \[MCRHDIAGP\]

> \| \| Background Information Print \[MCRHBACKP\]

> \| \| History Narrative Print \[MCRHNARRP\]

> \| \| Serial Laboratory Info. Print \[MCRHLABP\]

> \| \| Health Assessment (HAQ) Print \[MCRHHAQP\]

> \| \| Health/Physical History Print \[MCRHPATHISTP\]

> \| \| Physical Examination Print \[MCRHPHYSP\]

> \| \| Death Admin Print \[MCRHDEATHP\]

> \| \| Print All Report \[MCRHALLP\]

> \| \| Brief Rheumatology Report \[MCBPRHEUM\]

> \| Line Enter/Edit Menu \[MCRHMENULIN\] <span id="p43_44_37" class="anchor"></span>\*\*UNAVAILABLE\*\*

> \| \| Diagnosis Line Edit \[MCRHDIAGL\]

> \| \| History Narrative Line Edit \[MCRHNARRL\]

> \| \| Health Assessment (HAQ) Line Edit \[MCRHHAQL\]

> \| \| Health/Physical History Line Edit \[MCRHPATHISTL\]

> \| \| Physical Examination Line Edit \[MCRHPHYSL\]

> \| \| Death Admin Line Edit \[MCRHDEATHL\]

> \| \| Brief Diagnosis Line Edit \[MCRHBRIEF\]

> \| Problem Oriented Consult Menu \[MCCONSULT MENU\]

> \| \| Problem Oriented Consult Enter/Edit \[MCARGICONSULTEDIT\]

> \| \| Problem Oriented Consult Enter/Edit (Screen) \[MCCONSULTSCREEN\]

> \| \| Problem Oriented Consult Report \[MCARGICONSULTPRINT\]

> \| \| Brief Enter/Edit of a Problem Oriented Consult \[MCARGICONSULTBRIEF\]

> \| \| Brief Consult Enter/Edit (Screen) \[MCCONSULTBRSCR\]

> \| \| Brief Consult Report \[MCCONSULTBRREPORT\]

> \| Image Capture \[MCRHIMAGE\]

> \| Summary of Patient Procedures \[MCARSUMMARY\]

> \| Rheumatology Management Menu \[MCRHMENUMGR\]

> \| \| Rheumatology Medication File Update \[MCRHMED\]

> \| \| Delete Rheumatology Visit \[MCRHDELVISIT\]

> Generalized Procedure Menu \[MCGENERIC MEDICINE MENU\]

> \| Generalized Procedure Enter/Edit \[MCFLGEN\]

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 23%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 39%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>Generalized Procedure Enter/Edit (Screen) Generalized Procedure Report [MCFPGEN]</p>
</blockquote></td>
<td><blockquote>
<p>[MCFSGEN]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Summary of Patient Procedures</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>[MCARSUMMARY]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Problem Oriented Consult Menu</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>[MCCONSULT MENU]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Problem Oriented</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Consult Enter/Edit [MCARGICONSULTEDIT]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Problem Oriented</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Consult Enter/Edit (Screen) [MCCONSULTSCREEN]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Problem Oriented</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Consult Report [MCARGICONSULTPRINT]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>Brief Enter/Edit</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>of a Problem Oriented Consult [MCARGICONSULTBRIEF]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \| \| Brief Consult Enter/Edit (Screen) \[MCCONSULTBRSCR\]

> \| \| Brief Consult Report \[MCCONSULTBRREPORT\]

> \| Image Capture \[MCGENERICIMAGE\]

> \| Brief Generalized Procedure Enter/Edit \[MCBLGEN\]

> \| Brief Generalized Procedure Enter/Edit (Screen) \[MCBSGEN\]

> \| Brief Generalized Procedure Report \[MCBPGEN\]

> \| Generalized Procedure Management \[MCGENERICMGR\]

> \| \| Procedures/Subspecialties Definition Enter/Edit \[MCGENERICPREDT\]

> Summary of Patient Procedures \[MCARSUMMARY\]

> Enable/Disable OE/RR \[MCORHOOK\]

> Workload Reporting Management \[MCWKLDM\]

> \| Workload Reporting ON/OFF Toggle \[MCWKLDT\]

> \| Workload Reporting Mailgroup Selection \[MCWKLDG\]

> \| Workload Reporting Device Selection \[MCWKLDD\]

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At present, the only archiving or purging capability for the Medicine package is for Automated

> Instrument Interface.

> The user can enter the Cardiology menu and then select Cardiology Management Menu.

> \#3 is ECG Transfer Record Delete.

> \#4 is Holter Transfer Record Delete.

> Upon choosing one of the above options, the user will be asked for the number of days of reports they wish to retain. There is a 30-day minimum, which means one must keep at least the last 30- days’ worth of records.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The MCORMNO routine is called from the Order/Entry Health Summary package and is a black box. It checks that the variables GMRCSR and GMRCPRUM are defined. If these variables are not defined, the routine asks for the print template or record number using VA FileMan routines.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This package was created using Kernel V. 8.0 and VA FileMan V. 21.0 and requires the following external files:

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 59%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"></td>
<td><blockquote>
<p>Minimum</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><u>File #</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Package Name</u></p>
</blockquote></td>
<td><blockquote>
<p><u>Required Version</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>PIMS</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT PHARMACY</p>
</blockquote></td>
<td><blockquote>
<p>2.2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>55</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT PHARMACY</p>
</blockquote></td>
<td><blockquote>
<p>2.2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>61</p>
</blockquote></td>
<td><blockquote>
<p>LAB SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>5.1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>61.1</p>
</blockquote></td>
<td><blockquote>
<p>LAB SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>5.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>61.3</p>
</blockquote></td>
<td><blockquote>
<p>LAB SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>5.1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>61.5</p>
</blockquote></td>
<td><blockquote>
<p>LAB SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>5.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>DRG GROUPER</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>100</p>
</blockquote></td>
<td><blockquote>
<p>OE/RR</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>101</p>
</blockquote></td>
<td><blockquote>
<p>OE/RR</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>120.8</p>
</blockquote></td>
<td><blockquote>
<p>ADVERSE REACTION TRACKING</p>
</blockquote></td>
<td><blockquote>
<p>2.2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>123</p>
</blockquote></td>
<td><blockquote>
<p>CONSULT/REQUEST TRACKING</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Health Summary V. 2.7 AND HL7 V. 1.5 need not be installed for Medicine to run, however any components that use Health Summary will not be available. Therefore, it is suggested that both Health Summary and HL7 be installed.

> Installation of Imaging is optional at this time.

> SACC Exemptions

> 1 STANDARD SECTION: 2D2 \* & \# READs

> DATE GRANTED: FEB 13,1990

> The Medicine package may use \#-read in the screen-handler routines.

## DBI Agreements by Subscriber

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="p43_44_44" class="anchor"></span>5747     NAME: ICD Data Extraction

  CUSTODIAL PACKAGE: DRG GROUPER                               

SUBSCRIBING PACKAGE: LEXICON UTILITY                           

The LEXICON UTILITY has access to all APIs listed in this ICR as if it were the Custodial Package. 

CLINICAL PROCEDURES (MD) will use the following APIs:

- \$\$ICDDX^ICDEX to return data about an ICD Diagnosis code.
- \$\$CSI^ICDEX to return the coding system for an Internal Entry Number (IEN) to filter searches by coding system
- \$\$IMP^ICDEX to return the implementation date of a coding system.
- \$\$SINFO^ICDEX to return basic information about the active coding system based on a Date of Service.

> 1568 NAME: Set File Security for Medicine Files

> CUSTODIAL PACKAGE: VA FILEMAN San Francisco

> SUBSCRIBING PACKAGE: MEDICINE Chicago

> USAGE: Private APPROVED: Approved

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 1 ROOT: DIC(

> DESCRIPTION: TYPE: File

> The Medicine package uses the KIDS utility to export the package software.

> Medicine exports file level security codes for its data dictionaries.

> Currently, KIDS will not change the file level security codes on the

> target system if they already exist. This DBIA allows Medicine to check

> the file level security nodes on the package's data dictionaries and

> change the target system's file level security to match the ones being

> exported.

> The nodes changed are:

> ^DIC(File,0,"DD")="@" and ^DIC(File,0,"AUDIT")="@" Where 'File' has the following values:

<table style="width:100%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>690</p>
</blockquote></td>
<td><blockquote>
<p>690.1</p>
</blockquote></td>
<td><blockquote>
<p>690.2</p>
</blockquote></td>
<td><blockquote>
<p>690.5</p>
</blockquote></td>
<td><blockquote>
<p>690.97</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>690.99</p>
</blockquote></td>
<td><blockquote>
<p>691</p>
</blockquote></td>
<td><blockquote>
<p>691.1</p>
</blockquote></td>
<td><blockquote>
<p>691.5</p>
</blockquote></td>
<td><blockquote>
<p>691.6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>691.7</p>
</blockquote></td>
<td><blockquote>
<p>691.8</p>
</blockquote></td>
<td><blockquote>
<p>691.9</p>
</blockquote></td>
<td><blockquote>
<p>692</p>
</blockquote></td>
<td><blockquote>
<p>693</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>693.2</p>
</blockquote></td>
<td><blockquote>
<p>693.3</p>
</blockquote></td>
<td><blockquote>
<p>693.5</p>
</blockquote></td>
<td><blockquote>
<p>693.6</p>
</blockquote></td>
<td><blockquote>
<p>694</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>694.1</p>
</blockquote></td>
<td><blockquote>
<p>694.5</p>
</blockquote></td>
<td><blockquote>
<p>694.8</p>
</blockquote></td>
<td><blockquote>
<p>695</p>
</blockquote></td>
<td><blockquote>
<p>695.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>695.3</p>
</blockquote></td>
<td><blockquote>
<p>695.4</p>
</blockquote></td>
<td><blockquote>
<p>695.5</p>
</blockquote></td>
<td><blockquote>
<p>695.6</p>
</blockquote></td>
<td><blockquote>
<p>695.8</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>695.9</p>
</blockquote></td>
<td><blockquote>
<p>696</p>
</blockquote></td>
<td><blockquote>
<p>696.1</p>
</blockquote></td>
<td><blockquote>
<p>696.2</p>
</blockquote></td>
<td><blockquote>
<p>696.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>696.4</p>
</blockquote></td>
<td><blockquote>
<p>696.5</p>
</blockquote></td>
<td><blockquote>
<p>696.7</p>
</blockquote></td>
<td><blockquote>
<p>696.9</p>
</blockquote></td>
<td><blockquote>
<p>697</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>697.1</p>
</blockquote></td>
<td><blockquote>
<p>697.2</p>
</blockquote></td>
<td><blockquote>
<p>697.3</p>
</blockquote></td>
<td><blockquote>
<p>697.5</p>
</blockquote></td>
<td><blockquote>
<p>698</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>698.1</p>
</blockquote></td>
<td><blockquote>
<p>698.2</p>
</blockquote></td>
<td><blockquote>
<p>698.3</p>
</blockquote></td>
<td><blockquote>
<p>698.4</p>
</blockquote></td>
<td><blockquote>
<p>698.6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>698.9</p>
</blockquote></td>
<td><blockquote>
<p>699</p>
</blockquote></td>
<td><blockquote>
<p>699.48</p>
</blockquote></td>
<td><blockquote>
<p>699.5</p>
</blockquote></td>
<td><blockquote>
<p>699.55</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>699.57</p>
</blockquote></td>
<td><blockquote>
<p>699.6</p>
</blockquote></td>
<td><blockquote>
<p>699.7</p>
</blockquote></td>
<td><blockquote>
<p>699.81</p>
</blockquote></td>
<td><blockquote>
<p>699.82</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>699.83</p>
</blockquote></td>
<td><blockquote>
<p>699.84</p>
</blockquote></td>
<td><blockquote>
<p>699.85</p>
</blockquote></td>
<td><blockquote>
<p>699.86</p>
</blockquote></td>
<td><blockquote>
<p>699.88</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>700</p>
</blockquote></td>
<td><blockquote>
<p>700.1</p>
</blockquote></td>
<td><blockquote>
<p>700.2</p>
</blockquote></td>
<td><blockquote>
<p>700.5</p>
</blockquote></td>
<td><blockquote>
<p>701</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> -------------------------------------------------------------------------------

> 1090 NAME: DBIA1090

> CUSTODIAL PACKAGE: CONSULT/REQUEST TR Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Other

> The Medicine developers and the Consult/Request Tracking developers have

> agreed to remove the GMRCACT NEW PATIENT protocol (child) as an item from

> the GMRCACTM MEDICINE PKG MENU protocol (parent) in the Consult/

> Request Tracking package. The functionality provided in the GMRCACT NEW

> PATIENT protocol as an item in the GMRCACTM MED PKG MENU is not

> appropriate within the defined context of the Medicine package and removing this

> item will ensure that users are not prompted twice for selecting a patient.

> The routine MCFIXOEP, has been developed and will be included in the

> pre-installation process for Medicine V2.2 which will remove the protocol

> item. The Consult/Request Tracking developers will remove the GMRCACT NEW

> PATIENT protocol item from future versions of Consults.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 190 NAME: DBIA190-A

> CUSTODIAL PACKAGE: GEN. MED. REC. - A Chicago

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> The Medicine package has the permission of the Allergy Tracking System developers to use the following items from ATS V2.2.

> EN2^GMRAPEM0: This entry point is to be used by the Medicine package to enter data into the Allergy Tracking System. The input variable

> is DFN (pointer to file 2).

> ROUTINE: GMRAPEM0

> COMPONENT: EN2

> VARIABLES:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 672 NAME: DBIA190-B

> CUSTODIAL PACKAGE: GEN. MED. REC. - A Chicago

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 120.8 ROOT: GMR(120.8,

> DESCRIPTION: TYPE: File

> The Medicine package also needs to reference the following data

> elements:

> Patient Allergies (120.8) file:

> REACTION:REACTION (10,.01) and REACTION:OTHER REACTION (10,1)

> which is located in \$P(^GMR(120.8,D0,10,D1,0),U,1,2).

> -D0 would be obtained from a call to ^GMRADPT, and D1 would be

> obtained by looping through the multiple.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 673 NAME: DBIA190-C

> CUSTODIAL PACKAGE: GEN. MED. REC. - A Chicago

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 120.83 ROOT: GMRD(120.83,

> DESCRIPTION: TYPE: File

> The Medicine package has the permission of the Allergy Tracking System developers to use the following items from ATS V2.2.

> GMR Reactions (120.83) file:

> NAME (.01) which is located in \$P(^GMRD(120.83,D0,0),U).

> -D0 is obtained as the first piece from the first piece of

> ^GMR(120.8,D0,10,D1,0) as described above.

> "B" xref on NAME (.01) field which is located in ^GMRD(120.83,"B")

> -This is used to determine if an entry in the REACTIONS

> multiple, described above, points to the entry "OTHER REACTION".

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 466 NAME: DBIA466

> CUSTODIAL PACKAGE: IMAGING Washington

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> The Medicine package has been given permission by the Imaging package to

> do the following:

> Make calls to the ^MAGMIM routine through the ^MCMAG routine.

> ROUTINE: MAGMIM

> COMPONENT: MAGMIM

> VARIABLES: MCFILE Input

This is the file number of the procedure.

> ^MAGMIM routine allows the set-up of the variables necessary for image capture. The routine is used during the Image Capture option of the various Medicine modules. This option allows the imaging package to associate images with the various Medicine procedures.

> COMPONENT: EN1

> VARIABLES: MCFILE Input

> This is the file number for the current procedure.

> EN1^MAGMIM entry-point is the same as MAGMIM with the expectation that it happens after the editing of a Medicine procedure.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 467 NAME: DBIA467

> CUSTODIAL PACKAGE: IMAGING Washington

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> The Medicine package has been given permission by the Imaging package to

> do the following:

> Make calls to the ^MAGDISP routine through the ^MCMAG routine.

> ROUTINE: MAGDISP COMPONENT: MAGDISP

> VARIABLES: MCFILE Input

This is the file number for the current procedure.

> ^MAGDISP routine allows the display of images with a

> Medicine procedure during the printing of that procedure.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 468 NAME: DBIA468

> CUSTODIAL PACKAGE: IMAGING Washington

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> The Medicine package has been given permission by the Imaging package to the following:

> Make calls to the ^MAGSUM routine through the ^MCMAG routine.

> ROUTINE: MAGSUM COMPONENT: MAGSUM

> VARIABLES: MCFILE Input

This is the file number for the current procedure.

> ^MAGSUM routine displays a series of patient images. This routine is used during the Summary of Patient Procedures options.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 469 NAME: DBIA469

> CUSTODIAL PACKAGE: IMAGING Washington

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Other

> The Medicine package has permission by the Imaging package to Kill the

> ^TMP("MAG",\$J,"COL") and ^TMP("MAG",\$J,"ROW") globals within the

> Medicine package upon exiting the Summary of Patient Procedures options.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 470 NAME: DBIA470

> CUSTODIAL PACKAGE: IMAGING Washington

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 2005 ROOT: MAG(2005

> DESCRIPTION: TYPE: File

> The Medicine package has been given permission by the Imaging package to

> do the following:

> Point to the Imaging File (#2005) to reference each Medicine Procedure that has images.

> ^MAG(2005,

> The Medicine package is pointing to File 2005 to reference each

> Medicine Procedure that has images.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 895 NAME: PSGIU

> CUSTODIAL PACKAGE: INPATIENT MEDICATI Birmingham

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT: DESCRIPTION: TYPE: Routine

> Gives the ability to mark entries in the Drug file (50) for use with various packages.

> ROUTINE: PSGIU COMPONENT: EN

> VARIABLES: PSIUDA Input

> PSIUX Input

Internal entry number of the drug in the Drug file (50). The variable is not killed by this entry point.

Package information =\> package code^package name where:

Package code. The code used to mark the entry. This code is provided by the Birmingham ISC.

Package name. The name of the package for which the item will be used.

> The variable is not killed by this entry point.

> Prompts users to mark or unmark drug entries for use by their package.

> COMPONENT: ENS

> VARIABLES: PSIUDA Input

> PSIUX Input

Internal entry number of the drug in the Drug file (50). The variable is not killed by this entry point.

Package information =\> package code^package name where:

Package code. The code used to mark the entry. This code is provided by the Birmingham ISC.

Package name. The name of the package for which the item will be used.

> The variable is not killed by this entry point.

> Automatically marks drug entry for use with the package without any user interaction.

> COMPONENT: END

> VARIABLES: PSIUDA Input

> PSIUX Input

Internal entry number of the drug in the Drug file (50). The variable is not killed by this entry point.

Package information =\> package code^package name where:

Package code. The code used to mark the entry. This code is provided by the Birmingham ISC.

Package name. The name of the package for which the item will be used. The package name is not required for the END entry point.

This variable is not killed by this entry point.

> Automatically unmarks drug entry for use with package with no user interaction.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 38 NAME: DBIA38

> CUSTODIAL PACKAGE: LAB SERVICE Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Other

> Cardiology package exports Lab Codes for Cardiology.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 196 NAME: DBIA196-A

> CUSTODIAL PACKAGE: LAB SERVICE Dallas

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 62.5 ROOT: LAB(62.4,

> DESCRIPTION: TYPE: File

> The Medicine Package has permission from the Lab developers for read and

> write access to the ^LA node for the purpose of LSI autoinstrument

> interfacing.

> The Medicine Package has permission from the Lab developers for creating entries in the Autoinstrument file for the purpose of LSI autoinstrument interfacing.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 680 NAME: DBIA196-B

> CUSTODIAL PACKAGE: LAB SERVICE Dallas

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 61.5 ROOT: LAB(61.5,

> DESCRIPTION: TYPE: File

> The Medicine package has permission from the Lab developers to correct the

> double entry (CARDIOASSIST, AORTIC BALLOON PUMP) in the Lab SNOMED

> file.

> The Medicine package has permission from the Lab developers to create pointer values to the Lab SNOMED code file entries.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 681 NAME: DBIA196-C

> CUSTODIAL PACKAGE: LAB SERVICE Dallas

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 63 ROOT: LR(

> DESCRIPTION: TYPE: File

> The Medicine package has permission from the Lab developers to use the following root for FileMan access to Lab chemistry values: ^LR(DFN,""CH"", (for display only) .

> ^LR(D0,'CH', ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 861 NAME: OR

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ROUTINE: OR COMPONENT: EN

> VARIABLES: X Input

Variable pointer of the protocol.

> OE/RR Processor. This is the main entry point to run the OE/RR program. It is called with X set as a variable pointer to the initial protocol.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 862 NAME: ORUHDR

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ROUTINE: ORUHDR COMPONENT: EXT

> VARIABLES: ORIFN Both

> ORAGE Output

> ORIO Output ORANSI Output ORDOB Output

> ORFT Output ORHI Output ORNP Output

Internal number in file 100 of the order to display.

Patient age.

Patient Date of Birth

Pointer to file 200 for Current

Agent/Provider

> ORL Output

> ORPD Output

> ORPNM Output

> ORPV Output

> ORSEQ Output

> ORSEX Output

Variable pointer to the variable pointer.

Patient name

Pointer to Provider file for the person requesting the order.

Patient sex.

> ORSSN Output ORTIT Output ORTS Output

> ORVP Output

> ORWARD Output

Patient SSN Title

Pointer to Treating Specialty associated with the order.

Variable pointer toe object of an order. Inpatient Ward location

> Displays a standard header for detailed order displays. If

> calling this from within OE/RR, it is not necessary to

> kill the returned variables. OE/RR will kill them.

> COMPONENT: PGBRK

> VARIABLES: DIROUT Output

> OREND Output

User entered a '^^'

User entered a '^'

> Displays 'Press return to continue or "^" to escape' at page breaks.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 863 NAME: ORUPREF2

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ROUTINE: ORUPREF2

> COMPONENT: EN3

> VARIABLES: ORPKG Input

> ORDEF Input

Package pointer.

> ORFL Input

> ORDANM Input

> ORDA Input OREA Input ORTXT Input

Default protocol for setting up protocols.

File link - variable pointer for procedure file.

Optional name of the protocol.

Internal number of an existing protocol to be updated.

Action used in lieu of default defined in

OROEF.

Name of protocol; if not defined, the .01 filed of the procedure referenced is

used.

> Utility for 'on-the-fly' protocol creation. See OE/RR Developers guide.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 864 NAME: ORUTL

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT: DESCRIPTION: TYPE: Routine

> ROUTINE: ORUTL COMPONENT: READ VARIABLES:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 865 NAME: ORVOM

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ROUTINE: ORVOM

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 866 NAME: ORX

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ROUTINE: ORX COMPONENT: FILE

> VARIABLES: OREPDUZ Input ORL Input ORPCL Input

> ORNP Input

> ORVP Input

> ORCOST Input

> OREVENT Input

> ORIT Input ORLOG Input ORPK Input

> ORPURG Input ORSTOP Input ORSTRT Input

DUZ of the person entering the order. Variable pointer to the variable pointer. Variable pointer to the protocol that

created the order.

Pointer to file 200 for Current

Agent/Provider

Variable pointer to the object of an order.

Cost of the order

Two piece variable delimited by a semicolon. The first piece is the time at which an event should occur. The second piece is a character that has meaning to a package.

Variable pointer to the item ordered. Time the order is entered.

Package reference defined by the package when an order is created.

Grace days before an order is purged. Order Stop Date

Order start date

> ORSTS Input

> ORTO Input

Order status

> ORTS Input

> ORTX(i) Input

> ORIFN Output

> COMPONENT: RETURN

> VARIABLES: ORIFN Input

> ORETURN(OR Input

> ORETURN(OR Input

> ORETURN(OR Input ORETURN(OR Input ORETURN(OR Input ORETURN(OR Input

> ORETURN(OR Input ORETURN(OR Input ORETURN(OR Input ORETURN(OR Input

> COMPONENT: ST

> VARIABLES: ORIFN Input

> ORSTS Input

Pointer to Display Group file. Identifies the service receiving the order.

Pointer to Treating Specialty associated with the order.

Order Text.

Internal entry number of order in file

100

Internal entry number of order. Cost of the order.

Two piece variable delimited by a semicolon. The first piece is the time at which an event should occur. The second piece is a character that has meaning to a package.

Variable pointer to the item ordered. Free text, package defined reference. Grace period before purging order. Pointer to file 200 for Current

Agent/Provider

Stop Date

Start Date

Pointer to Order Status

Order Text

Internal entry number of the order. Order Status

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 867 NAME: ORX2

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ROUTINE: ORX2

> COMPONENT: LK

> VARIABLES: X Input

> Y Output

Variable pointer of patient.

Y=1 if lock is successful, 0 if failed.

> Used when updating orders for a patient to check that someone else is not also updating orders at the same time for the same patient. This will attempt to set a software lock on the patient. Applications using this entry point must also call the entry point ULK^ORX2 to unlock the patient when the updating process is finished.

> COMPONENT: ULK

> VARIABLES: X Input

> Variable pointer to the patient.

> Used in conjunction with the entry point LK^ORX2 to unlock

> a patient during the process of adding orders. Do not call

> this entry point unless you have already successfully

> locked the patient.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 868 NAME: ORX3

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ROUTINE: ORX3

> COMPONENT: NOTE

> VARIABLES: ORNOTE(i) Input

> ORVP Input

> ORIFN Input

i=internal \# of the notification Variable pointer to the patient. Order number that you want this

notification to linked to.

> This is an entry point that creates a notification for a package.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 869 NAME: ORX5

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ROUTINE: ORX5

> COMPONENT: DC

> VARIABLES: ORIFN Input

Pointer to the order.

> This entry is called when a package needs to create a DC

> order.

> COMPONENT: HOLD

> VARIABLES: ORIFN Input

> Pointer to the order.

> This entry is called when a package needs to place a HOLD

> on an ordered item.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 870 NAME: ORX7

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ROUTINE: ORX7

> COMPONENT: DC

> VARIABLES: ORIFN Input

> ORNATR Input

Pointer to the order.

Identifies the Nature of Order.

> This entry point is provided for orders that are discontinued by the service. This creates a DC order for the order identified by ORIFN.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 871 NAME: ORX8

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ROUTINE: ORX8

> COMPONENT: EN(ORIFN)

> VARIABLES: ORIFN Input

> ORUPCHUK(' Output ORUPCHUK(' Output ORUPCHUK(' Output ORUPCHUK(' Output ORUPCHUK(' Output ORUPCHUK(' Output ORUPCHUK(' Output ORUPCHUK(' Output ORUPCHUK(' Output ORUPCHUK(' Output ORUPCHUK(' Output ORUPCHUK(' Output

Pointer to the order.

=WHO ENTERED^External Format

=PATIENT LOCATION

=CURRENT AGENT/PROVIDER^External format

=WHEN ENTERED

=PROTOCOL

=CURRENT AGENT/PROVIDER^External Format

=STOP DATE

=CURRENT START DATE

=STATUS^External format

=TO (display group)^External Format

=ORDER TEXT (Multiple)

=OBJECT OF ORDER

> This entry point returns data from the Order file (100) for a particular order.

> COMPONENT: NOTIF(ORIFN,ORNOTE) VARIABLES: ORIFN Input

> ORNOTE Input

Pointer to the order

Pointer to the notification

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 872 NAME: File 101

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 101 ROOT: ORD(101,

> DESCRIPTION: TYPE: File

> This file may be referenced by packages to maintain protocols within their

> namespace. This file may also be pointed to.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 873 NAME: File 100.98

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 100.98 ROOT: ORD(100.98,

> DESCRIPTION: TYPE: File

> This file may be referenced to determine an appropriate Display Group for

> an order in the manner:

> S ORTO=\$O(^ORD(100.98,'B','OTHER HOSPITAL SERVICES',0))

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 874 NAME: File 100.99

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 100.99 ROOT: ORD(100.99,

> DESCRIPTION: TYPE: File

> This file may be referenced by packages interfacing with OE/RR to see if

> OE/RR has been installed in the manner:

> I \$D(^ORD(100.99)) ...

> Packages may also setup entries in the Package Parameters portion of this file.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 875 NAME: File 100.01

> CUSTODIAL PACKAGE: ORDER ENTRY/RESULT Salt Lake City

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Controlled Subscri APPROVED: APPROVED

> STATUS: Active EXPIRES: DURATION: Till Otherwise Agr VERSION:

> FILE: 100.01 ROOT: ORD(100.01, DESCRIPTION: TYPE: File

> This file may be pointed to.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 674 NAME: DBIA191-B

> CUSTODIAL PACKAGE: PHARMACY Birmingham

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> ^PSODEM: This is Pharmacy's MAS patient demographic

> function which is used in conjunction with the Pharmacy

> Patient profile. The input variable is DA and is the

> internal entry number of the VA Patient file and is

> equivalent to the DFN.

> ROUTINE: PSODEM

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 675 NAME: DBIA191-C

> CUSTODIAL PACKAGE: PHARMACY Birmingham

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> STAT^PSOFUNC: This is the Pharmacy treatment status

> function and is used in the Pharmacy patient profile.

> The required variables are RX0, RX2, and J.

> ROUTINE: PSOFUNC COMPONENT: STAT VARIABLES:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 676 NAME: DBIA191-D

> CUSTODIAL PACKAGE: PHARMACY Birmingham

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION: FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> DOIT^PSOP: This is the Pharmacy queue report entry point.

> ROUTINE: PSOP COMPONENT: DOIT VARIABLES:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 677 NAME: DBIA191-E

> CUSTODIAL PACKAGE: PHARMACY Birmingham

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 55 ROOT: PS(55,

> DESCRIPTION: TYPE: File

> ^PS(55,DA,"P") and ^PS(55,DA,"ARC") in order to screen the

> file for relevant data.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 678 NAME: DBIA191-F

> CUSTODIAL PACKAGE: PHARMACY Birmingham

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 52 ROOT: PSRX(

> DESCRIPTION: TYPE: File

> ^PSRX(DA, for prescription data.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 679 NAME: DBIA191-G

> CUSTODIAL PACKAGE: PHARMACY Birmingham

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 50 ROOT: PSDRUG(

> DESCRIPTION: TYPE: File

> ^PSDRUG(DA, for drug data.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> 934 NAME: DBIA934

> CUSTODIAL PACKAGE: PHARMACY Birmingham

> SUBSCRIBING PACKAGE: MEDICINE Washington

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> This is for Pharmacy 6.0 and greater.

> ROUTINE: PSOP COMPONENT: PSOP

> VARIABLES: PLS Input

> DFN Input

Internal Entry Number of the patient.

> This entry point(and re-entry point) is the functional Pharmacy Patient profile. This tool is used for acquisition of display only data for use in Rheumatology reports.

> This supersedes DBIA191-A \#191.

## Medicine Custodial DBI Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: DBIA147-A ENTRY: 147

> CUSTODIAL PACKAGE: MEDICINE Washington

> SUBSCRIBING PACKAGE: CONSULT/REQUEST TR Salt Lake City

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Other

> 1\. The REQUEST/CONSULTATION file, 123, has a variable pointer field

> called "Results" which points to the following fields.

> 691 Echo

> 691.1 Cardiac Catheterization

> 691.5 Electrocardiogram (EKG/ECG)

> 691.6 Holter

> 691.7 Exercise Tolerance Test

> 691.8 Electrophysiology (EP)

> 694 Hematology

> 698 Generator Implant

> 698V1 V Lead Implant

> 698.2 A Lead Implant

> 698.3 Pacemaker Surveillance

> 699 Endoscopy/Consult

> 700 Pulmonary Function Tests

> 701 Rheumatology

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NAME: DBIA147-B ENTRY: 615

> CUSTODIAL PACKAGE: MEDICINE Washington

> SUBSCRIBING PACKAGE: CONSULT/REQUEST TR Salt Lake City

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: ROOT:

> DESCRIPTION: TYPE: Routine

> 2\. This results pointer is updated via calls from the Medicine options

> which enter/edit results to EN^GMRCR and RESULT^GMRCR, which are

> documented in the Consult/Request Tracking package.

> Once the results variable pointer is defined, the Medicine Package has

> provided Consult/Request Tracking with an entry point PRINT^MCOR which

> extracts results information and stores them in an ^TMP array for display

> purposes in OE/RR and Consult/Request Tracking.

> In order to call PRINT^MCOR the Consult/Request Tracking package must

> define the following variables.

> ORACTION=8

> GMRCSR=variable pointer to results file

> GMRCPRNM=Name of procedure type, which should equal one of the

> Procedure Types in File 697.2, the eighth piece.

> ROUTINE: MCOR COMPONENT: PRINT VARIABLES:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NAME: DBIA147-C ENTRY: 616

> CUSTODIAL PACKAGE: MEDICINE Washington

> SUBSCRIBING PACKAGE: CONSULT/REQUEST TR Salt Lake City

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 697.2 ROOT: MCAR(697.2,

> DESCRIPTION: TYPE: File

> 3\. In addition to the interface the Medicine Package has provided, an

> alternative method for the Medicine Package Users is provided in a stand

> alone option provided by the Consult/Request Tracking Package. This

> option functions as follows:

> \- The user selects the Medicine Procedure Type from a Protocol Menu

> \- The service related to the Procedure Type defined in the FILE LINK

> field in Protocol File is determined

> \- The patient is selected.

> \- Consults/Request for the Service and Patient are displayed.

> \- At the Select Action: prompt, the user may select "AR" for

> associate results

> \- File 697.2 (new agreement) is used to determine the appropriate

> file of results to use, based on the Procedure Type.

> \- The user is allowed to select from the list of Results in this

> results file for the Patient. (Using Medicine "C" cross-ref.)

> \- Once a result entry is selected, it may be viewed using the

> PRINT^MCOR, to verify these are the correct results to associate with the

> request.

> \- The user is asked if the order status should be updated to

> 'Completed' (default is yes, if no, ORSTS is incomplete)

> \- The user is asked to enter the name of the clinician responsible

> for the results.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NAME: DBIA80-A ENTRY: 80

> CUSTODIAL PACKAGE: MEDICINE Washington

> SUBSCRIBING PACKAGE: HEALTH SUMMARY Salt Lake City

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 690 ROOT: MCAR(690,

> DESCRIPTION: TYPE: File

> The Health Summary exports and calls the routine GMTSMCPS, which generates

> the output for the Health Summary Medicine component. The following

> fields and cross references are being referenced:

> ^MCAR(690, Medical Patient File

> Uses "AC" cross reference

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NAME: DBIA80-B ENTRY: 540

> CUSTODIAL PACKAGE: MEDICINE Washington

> SUBSCRIBING PACKAGE: HEALTH SUMMARY Salt Lake City

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 699 ROOT: MCAR(699,

> DESCRIPTION: TYPE: File

> The Health Summary exports and calls the routine GMTSMCPS, which generates

> the output for the Health Summary Medicine component. The following

> fields and cross references are being referenced:

> ^MCAR(699, Endoscopy File

> Fields: 1 Procedure

> 20 Summary

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NAME: DBIA80-C ENTRY: 541

> CUSTODIAL PACKAGE: MEDICINE Washington

> SUBSCRIBING PACKAGE: HEALTH SUMMARY Salt Lake City

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 694 ROOT: MCAR(694,

> DESCRIPTION: TYPE: File

> The Health Summary exports and calls the routine GMTSMCPS, which generates

> the output for the Health Summary Medicine component. The following

> fields and cross references are being referenced:

> ^MCAR(694, Hematology File

> Fields: 2 Procedure

> 1.5 Summary

> ROUTINE:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> NAME: DBIA80-D ENTRY: 542

> CUSTODIAL PACKAGE: MEDICINE Washington

> SUBSCRIBING PACKAGE: HEALTH SUMMARY Salt Lake City

> USAGE: Private APPROVED: APPROVED

> STATUS: Active EXPIRES:

> DURATION: Till Otherwise Agr VERSION:

> FILE: 697.2 ROOT: MCAR(697.2,

> DESCRIPTION: TYPE: File

> The Health Summary exports and calls the routine GMTSMCPS, which generates

> the output for the Health Summary Medicine component. The following

> fields and cross references are being referenced:

> ^MCAR(697.2, Procedure Location File

> Fields: .01 Name

> 1 Global Location

> Uses "C" cross reference on Global Location field.

> The "C" cross reference could result in pointing

> to global locations in the Global Location field which

> currently contains global roots for the range on files

> from ^MCAR(691, through ^MCAR(699,.

> ROUTINE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> NAME: DBIA1189-A ENTRY: 1189

> CUSTODIAL PACKAGE: MEDICINE Washington

> SUBSCRIBING PACKAGE: IMAGING Washington

> USAGE: Private APPROVED:

> STATUS: Pending EXPIRES:

> DURATION: Till otherwise agreed

> FILE: ROOT:

> DESCRIPTION: TYPE: File

> The purpose of this agreement is to provide access to the Medicine

> package (custodian) by the Imaging package (subscriber) for the purpose of

> creating a new Medicine package entry (stub:Pt ID, Date/time) as a holder

> of an Imaging pointer or set of Imaging pointers. The Imaging pointers

> are set in the Field 2005, as descendants of the 0 subscript of node 2005

> in each of the following files: Echo(691), Cardiac Cath(691.1),

> EKG(691.5), Hematology(694), Endoscopy(699), Generalized Procedure(699.5),

> and Rheumatology(701).

> The Imaging routines which perform this function are as follows: MAGMCPT\* and MAGUFILR

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> NAME: DBIA1189-B ENTRY: 1190

> CUSTODIAL PACKAGE: MEDICINE Washington

> SUBSCRIBING PACKAGE: IMAGING Washington

> USAGE: Private APPROVED:

> STATUS: Pending EXPIRES:

> DURATION: Till otherwise agreed

> FILE: ROOT:

> DESCRIPTION: TYPE: File

> The purpose of this agreement is to provide access to the Medicine

> package (custodian) by the Imaging package (subscriber) for the purpose of

> editing (including deletion of) Medicine package Image entries.

> The Imaging pointers are set in the Field 2005, as descendants of the 0

> subscript of node 2005 on each of the following files: Echo(691), Cardiac

> Cath(691.1), EKG(691.5), Hematology(694), Endoscopy(699), Generalized

> Procedure(699.5), and Rheumatology(701).

> The Imaging routines which perform this function are as follows: MAGMCPT\*, MAGUDEL\* and MAGUFILR.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> NAME: DBIA1189-C ENTRY: 1191

> CUSTODIAL PACKAGE: MEDICINE Washington

> SUBSCRIBING PACKAGE: IMAGING Washington

> USAGE: Private APPROVED:

> STATUS: Pending EXPIRES:

> DURATION: Till otherwise agreed

> FILE: ROOT:

> DESCRIPTION: TYPE: File

> The purpose of this agreement is to provide access to the Medicine

> package (custodian) by the Imaging package (subscriber) for the purpose of

> displaying Medicine package Summary fields associated with Images.

> The Imaging functions require direct global read access to the Procedure/Subspecialty file (697.2), the Image multiple of each of the Medicine Procedure files listed below, and the Summary field of each of the files Listed below.

> Medicine Procedure files: Echo(691), Cardiac Cath(691.1),

> EKG(691.5), Hematology(694), Endoscopy(699), Generalized Procedure(699.5),

> and Rheumatology(701).

> The Imaging routines which perform this function are as follows: MAGDISP, MAGMIM, MAGSUM, and MAGABLP.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All menus and menu options are independent of each other.

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no package-wide variables associated with the Medicine package.

> Variables which users should be aware of are MCARDIE and MCOB\*, which are used by routine MCARPROC to set the Medical Patient file cross reference whenever a procedure is performed. MCARDIE is the global reference in VA FileMan DIC format and is set by the various procedure dictionaries.

# How to Generate On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is recommended that you print the Medicine package V. 2.3 Data Dictionaries immediately after you load the software. This is done using the VA FileMan List File Attributes option. The Medicine files currently use numbers 690 through 701. You may specify a Standard or Brief Data Dictionary as your needs require.

> The first part of each Data Dictionary (in a Standard listing) is a list of other files that point to Medicine file fields. The second part is a listing of all of the cross-references for that file and a brief description of what the cross-reference is for.

> To learn more about the options for the Medicine package, one may either print a more detailed option list (including things such as entry/exit actions, menu type, etc.) or D ^XUP, select XUMAINT, and then select a specific option.

> Utilizing on-line documentation is the best way to obtain the most current information available. Further information for generating On-line documentation is provided in the Kernel and VA FileMan documentation. This can be obtained either from your IRM or your local ISC.

> %Index can be used as a cross-reference listing of all local and global variable usage as well as other information of invaluable assistance in de-bugging. Running %INDEX V. 7.3 on this version of the Medicine package will produce the following Errors and Warnings:

> S - Routine exceeds SACC maximum size of 5000 The new SACC standards now allow routine sizes of up to 10000.

> S - Star or pound READ used. The Medicine package has a

SACC exemption.

> F - Invalid or wrong number of arguments to a function. This is a 2 argument \$ORDER or \$GET which is now allowed.

> F - Reference to routine '…'. That isn't in this UCI. Depending on the status of the Imaging package, these routines may or may not be present. The Medicine package checks for the existence of these routines before trying to use them.

# Appendix A - Patch MC\*2.3\*24

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Clinical Instrument Interface Specifications

> I. Purpose

> This document specifies an interface between clinical instrumentation and the VA Medicine software package.

> II\. Overview

> The Office of Information Field Office at Hines (Hines OIFO) has developed plans to implement an interface for exchange of data between clinical instrumentation and the Medicine package.

> III\. Installation and Configuration

> Refer to Medicine Patch 24 Installation Guide for instructions on installing patch 24. Configuration instructions (first installation and new devices):

> 1\. Use the Start/Stop Link option in the Filer and Link Management Options menu of the HL7 package (HL Main Menu) to inactivate or activate the MCAR INST link as needed.

> Select OPTION NAME: hl main menu HL7 Main Menu

> Systems Link Monitor

> Filer and Link Management Options ...

> Message Management Options ...

> Interface Developer Options ...

> Site Parameter Edit

> Select HL7 Main Menu Option: filer and link management options

> SM Systems Link Monitor

> FM Monitor, Start, Stop Filers

> LM TCP Link Manager Start/Stop

> SA Stop All Messaging Background Processes

> RA Restart/Start All Links and Filers

> DF Default Filers Startup

> SL Start/Stop Links

> PI Ping (TCP Only)

> ED Link Edit

> ER Link Errors ...

> 1 Patch MC\*2.3\*24 December 2000 This entire appendix is new material.

> Select Filer and Link Management Options Option: sl Start/Stop Links

> This option is used to launch the lower level protocol for the appropriate device. Please select the node with which you want to communicate

> Select HL LOGICAL LINK NODE: MCAR INST

> The LLP was last started on OCT 26, 2000 09:47:45.

> Inactivate the Link.

> Okay to shut down this job? y YES

> The job for the MCAR INST Lower Level Protocol will be shut down.

> SM Systems Link Monitor

> FM Monitor, Start, Stop Filers

> LM TCP Link Manager Start/Stop

> SA Stop All Messaging Background Processes

> RA Restart/Start All Links and Filers

> DF Default Filers Startup

> SL Start/Stop Links

> PI Ping (TCP Only)

> ED Link Edit

> ER Link Errors ...

> Select Filer and Link Management Options Option: sl Start/Stop Links

> This option is used to launch the lower level protocol for the appropriate device. Please select the node with which you want to communicate

> Select HL LOGICAL LINK NODE: MCAR INST

> Activate the Link.

> The LLP was last shutdown on NOV 06, 2000 16:03:47.

> This LLP will start on node DEV:ISC4A2 if it is run in the Background.

> Select one of the following: F FOREGROUND

> B BACKGROUND

> Q QUIT

> Method for running the receiver: B// \<RET\> ACKGROUND Job was queued as 266473.

> 2\. Through FileMan edit the Instrument HL7 Coding (#690.7) file for the instrument you are using. Create or use the name of an existing mailgroup that is responsible for processing the errors from the instrument.

> DMGR\>D P^DI

> VA FileMan 22.0

> Select OPTION: enter OR EDIT FILE ENTRIES

> INPUT TO WHAT FILE: HL7 APPLICATION PARAMETER// 690.7 Instrument HL7 Coding

> (8 entries)

> EDIT WHICH FIELD: ALL// \<RET\>

> Select Instrument HL7 Coding NAME: cmore

> NAME: CMore// \<RET\>

> PROCESSING ROUTINE: MCAR7E// \<RET\>

> MAIL GROUP FOR ERRORS: HL7 ERRORS// \<RET\>

> IV\. Summary of Interface and Data Requirements

> Patch MC\*2.3\*24 is a clinical device interface system. The interface allows the clinical devices listed in Table 1 to send data to the Medicine Package using Transport Communication Protocol/ Internet Protocol (TCP/IP) and Health Level Seven (HL7) data format.

> Table 1

> -----------------------------

> Device Device Instrument

> Vendor Type Code

> ----------------- ------------- ------------- Sensormedics Pulmonary SMC Medgraphics Pulmonary Medgraph Medgraphics Pulmonary \* D.I. cMore Endoscope cMore

> Olympus Endoscope OLYMPUS Pentax Endoscope PENTAX DelMar Holter CCF Marquette EKG/ECG Muse ECG

> \* For Medgraphics devices that use the Data Innovations (D.I.) interface, the Sending Facility (4th

> piece of the message header (MSH) segment, delimited by a vertical bar “\|”) will contain the string “Instrument Manager”. The 25th piece of the observation request (OBR) segment will then contain the Instrument Code for that device. The MSH and OBR segments will take the following format:

> MSH\|^~\\\|INST-MCAR\|Instrument Manager\|MCAR-INST\|VISTA OBR\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\[Instrument Code\]

> ^^^^^^

> 25th Piece of OBR String

> The MSH for all other devices will take the following format:

> MSH\|^~\\\|INST-MCAR\|\[Instrument Code\]\|MCAR-INST\|VISTA

> V. File Settings

> The following are the parameter settings for the HL7 Application Parameter file, HL Logical Link file, and the Protocol file that are automatically set by the KIDS build (MC\*2.3\*24). They are listed here for your reference. Bolded fields must be set as they appear below.

> HL7 Application Parameter (#771) file:

> This file contains a list of VISTA applications that are capable of sending and receiving HL7 transmissions.

> NAME: MCAR-INST ACTIVE/INACTIVE: ACTIVE FACILITY NAME: VISTA MAIL GROUP: POSTMASTER

> COUNTRY CODE: US HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> NAME: INST-MCAR ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: US HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

> HL Logical Link (#870) file:

> This file stores parameters that govern the behavior of the Logical Links, and also stores information that drives the SYSTEMS LINK MONITOR display option.

> NODE: MCAR INST LLP TYPE: TCP

> QUEUE SIZE: 100 RE-TRANSMISSION ATTEMPTS: 3

> ACK TIMEOUT: 60 EXCEED RE-TRANSMIT ACTION: ignore

> TCP/IP PORT: 1026 TCP/IP SERVICE TYPE: SINGLE LISTENER

> PERSISTENT: NO

> Protocol (#101) file:

> This file contains the methods (protocols) for processing the HL7 messages.

> NAME: MCAR Device Client ITEM TEXT: Instrument Device Client

> TYPE: subscriber CREATOR: LUSHENE,ROBERT E

> PACKAGE: MEDICINE

> DESCRIPTION: Subscriber protocol for sending data to VISTA from clinical instruments.

> TIMESTAMP: 57540,31165 RECEIVING APPLICATION: MCAR-INST

> TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

> PROCESSING ID: P LOGICAL LINK: MCAR INST

> \* VERSION ID: 2.3 RESPONSE MESSAGE TYPE: ACK

> PROCESSING ROUTINE: D ^MCAR7A SENDING FACILITY REQUIRED?: NO

> RECEIVING FACILITY REQUIRED?: NO

> NAME: MCAR Device Server ITEM TEXT: Instrument HL7 Event Driver

> TYPE: event driver CREATOR: LUSHENE,ROBERT E

> PACKAGE: MEDICINE

> DESCRIPTION: This protocol is used by the HL7 package to send results to

> VISTA from various clinical instrumentation.

> TIMESTAMP: 57631,55707 SENDING APPLICATION: INST-MCAR

> TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

> PROCESSING ID: P \* VERSION ID: 2.3

> SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

> SUBSCRIBERS: MCAR Device Client

> \* NOTE: Version ID should match what the instrument is sending.

> VI\. Technical Issues

> 1\. For all sites:

> a\. Kernel Patch XU\*8.0\*146 has been released and must be installed prior to this installation to prevent the Medicine patch (MC\*2.3\*24) from over-writing any existing HL Logical Links.

> b\. To avoid error messages because of a missing or invalid 'Event Protocol', 'Invalid Processing Code', 'Invalid Application Code', etc., make sure that all settings (except TCP/IP PORT and TCP/IP ADDRESS, in the HL Logical Link (#870) file, which are site specific) are the same as the file settings listed earlier. Be sure that the VERSION ID parameters in the Protocol (#101) file are set to the same HL7 Version that is being sent by the vendor instrument. The ITEM and SUBSCRIBERS fields in the Device Server entry in the Protocol (#101) file MUST be the same as the Device Client name.

> 2\. For Sensormedics interfaces only:

> Because the VISTA HL7 package returns a 2 part acknowledgement (ACK) to the instrument, the following solution will allow the Sensormedics device to process the ACK directly.

> Solution:

> • In the Vmax software Reports option, select NETLINK/IS.

> • Then on the Transmission Setup pull-down menu, select Configuration.

> • If the "Wait for Host Acknowledgement Messages" box is not checked, check it.

> • Change the entry in the "Number of ACK messages" box from 1 to 2.

> • Press the F3 key to store changes and exit the software.

> There are also several special VA files that Sensormedics has set up. You will need to acquire a copy of the SensorMedics NetLink/IS software for each Vmax system that will be sending patient data to VISTA. This software will be installed on the Vmax pulmonary system(s) using the Software Installation routine found in the Setup menu of the Vmax main screen. The following 3 files should be extracted into the C:\VISION

> directory on the Vmax pulmonary system(s) that will be interfaced to VISTA, overwriting any file of the same name that may be there:

> a\. XMITHDFT.DBF - This is a file containing the special header and footer lines that comply with the patch requirements in VISTA.

> b\. SMVADEF.DBF - This is the VA definition file for the SensorMedics NetLink/IS software. It contains definitions of all of the OBX segments that can be sent using the HL7 NetLink/IS engine.

> c\. REPLACE. - This is a 'housekeeping' file that causes the NetLink/IS software to replace any HL7 control character entered from the keyboard with a space.

> 3\. For Olympus interfaces only:

> Verify that the following keys in the \[HL7 Parameters\] section of the OLYHLUPL.INI file appear as below. If the keys do not appear as below, call your Olympus representative.

> a\. Sending_Application=INST-MCAR

> b\. Sending_Facility=OLYMPUS

> c\. Receiving_Application=MCAR-INST

> d\. Receiving_Facility=VISTA

> (these correspond to the MSH fields described earlier)

> VII\. Problem Solving

> Join the mailgroup on FORUM called “ER, MEDICINE” for discussion on this patch. Use this mail group to discuss problems and issues with any Medicine device interfaces. For help on joining a mailgroup, refer to Mailman help on FORUM.

> VIII\. Interfacing with New Devices

> 1\. Determine whether your site is willing to test the device.

> 2\. Contact the vendor and find out if they use HL7 through TCP/IP.

> 3\. Get the name, address, and phone number of a contact person for the vendor.

> 4\. Send all necessary information to the Hines OI Field Office.

> IX\. HL7 Data Formats

> A. Rationale:

> The function of the HL7 coding scheme is to define a data stream that will pass coded, addressed clinical data across a distributed network.

> B. Methodology:

> A complete collection of data, a complete procedure, or a complete report is transferred between systems by a single message. This message is comprised of a group of segments in a defined sequence.

> A segment is defined by its first three characters, which identify segment type, and is terminated by a carriage return. The subcomponents of segments are data fields that are in a fixed order, of variable length, and are delimited by a field separator for which the default specified by HL7 is the vertical bar (\|).

> The message type used by these interfaces is an “ORU^R01”, Observation Result Unsolicited (unsolicited transmission of requested observation). The first segment is the message header (MSH). Other segments in the message include the patient identification (PID), the observation request (OBR), and observation (OBX).

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NOTE:

> Only MSH, PID, OBR and OBX segments are required, any other segments will be ignored.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The first character found after the “MSH” defines the field separator for the remainder of the message. In practice, the vertical bar has been generally accepted. The next four characters, the second field in the MSH segment, define the component separator, the repetition separator, the escape character, and the subcomponent separator. The characters generally used to portray these are “^~\\” (circumflex, tilde, backslash, ampersand).

> C. Sample Clinical Scenario for Vendor-Initiated Messaging:

> The physician uses the vendor equipment to enter findings in a report and performs whatever action is necessary to trigger the vendor software to create and send to VISTA an HL7 ORU message containing the report. VISTA accepts and files the report and sends a positive acknowledgement (ACK) message, or rejects the report and sends an HL7 response (ACK) indicating why it was rejected.

> D. Data tables:

> The following HL7 messages are used to support the exchange of Medicine data: ACK General Acknowledgement

> ORU Observational Results Unsolicited

> The following HL7 segments are used to support the exchange of Medicine data: MSA Message Acknowledgement

> MSH Message Header

> PID Patient Identification OBR Observational Request OBX Result

> Following is a list of Data Types: ST string

> TS timestamp

> PN person name

> ID coded value

> CK composite with check digit CN composite number and name CE coded element

> Following are the various data record fields in tabular form, along with their definitions. The columns shown are sequence number, M (MUMPS) piece - delimited by field separator, maximum length, data type, whether the element is Required or Optional, the element name, and the values that the element may have.

> MSH table

e=variable)

> FIELD SEPARATOR: Character used to separate fields in message segments. The default is the ASCII decimal 124 (vertical bar).

> ENCODING CHARACTERS: Characters used as component separator, repetition separator, escape character and subcomponent separator respectively. The defaults are ASCII decimals

> 94, 126, 92, 38 (circumflex, tilde, backslash, ampersand).

> SENDING APPLICATION: Application parameter (file \#771) used by instrument. SENDING FACILITY: Instrument Code used by vendor (i.e., SMC, Muse ECG). RECEIVING APPLICATION: Application parameter used by VISTA. RECEIVING FACILITY: System receiving the information.

> DATE/TIME OF MSG: Date/time stamp when message was sent by instrument. MESSAGE TYPE: Type of message being sent by instrument.

> MESSAGE CONTROL ID: Unique alphanumeric identifier for the message.

> VERSION ID: Version of HL7 messages that the instrument will be sending to VISTA.

> PID table

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 28%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Seq</p>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
<p>piece</p>
</blockquote></td>
<td><blockquote>
<p>Len</p>
</blockquote></td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>R/O</p>
</blockquote></td>
<td><blockquote>
<p>Element Name</p>
</blockquote></td>
<td><blockquote>
<p>Values (lower case=variable)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>CK</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ID</p>
</blockquote></td>
<td><blockquote>
<p>Patient ID – (social security #)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td>6</td>
<td><blockquote>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>PN</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT NAME</p>
</blockquote></td>
<td><blockquote>
<p>Last^First^Middle initial</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>CK</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT SSN</p>
</blockquote></td>
<td><blockquote>
<p>Social security number</p>
</blockquote></td>
</tr>
</tbody>
</table>

> PATIENT ID: This is the patient ID number, usually social security number. Format can include hyphens.

> PATIENT NAME: This is a three component field – Last name^First name^Middle initial. PATIENT SSN: This is the patient’s social security number, because some systems use

> sequence \#3 for another type of patient ID.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NOTE:

> Either sequence \#3 OR sequence \#19 OR both MUST be present.

> OBR table

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Seq</p>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
<p>piece</p>
</blockquote></td>
<td><blockquote>
<p>Len</p>
</blockquote></td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>R/O</p>
</blockquote></td>
<td><blockquote>
<p>Element Name</p>
</blockquote></td>
<td><blockquote>
<p>Values (lower case=variable)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>5</td>
<td><blockquote>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>UNIVERSAL SERVICE ID</p>
</blockquote></td>
<td><blockquote>
<p>Code^text^code type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td>8</td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>TS</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>OBSERVATION DATE/TIME</p>
</blockquote></td>
<td><blockquote>
<p>Yyyymmddhhmmss</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>RESULT STATUS</p>
</blockquote></td>
<td><blockquote>
<p>F or C</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td><blockquote>
<p>32</p>
</blockquote></td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>REASON FOR STUDY</p>
</blockquote></td>
<td><blockquote>
<p>ICD code</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>32</p>
</blockquote></td>
<td><blockquote>
<p>33</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>CN</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>RESULT INTERPRETER</p>
</blockquote></td>
<td><blockquote>
<p>Last name^First name^MI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>34</p>
</blockquote></td>
<td><blockquote>
<p>35</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>CN</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>TECHNICIAN</p>
</blockquote></td>
<td><blockquote>
<p>Last name^First name^MI</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="p43_44_82" class="anchor"></span>

> UNIVERSAL SERVICE ID: This is a 3-component field. The first component is the synonym for the procedure (i.e. COL, ENDO, 93005). The second component is a free text identifier for the procedure (i.e. Colonoscopy, Endoscopy, Holter). The third component is optional, and can identify the type of synonym in the first component (i.e. CPT4 for a CPT code in the first component).

> OBSERVATION DATE/TIME: Date/time stamp of when the result was generated. RESULT STATUS: Status code for result – F = Final, C = Correction.

> REASON FOR STUDY: ICD code that prompted the procedure to be performed.

> RESULT INTERPRETER: Name of interpreting physician – Last name^First name^Middle initial.

> TECHNICIAN: Name of technician giving test – Last name^First name^Middle initial.

> OBX table

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 26%" />
<col style="width: 39%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Seq</p>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
<p>piece</p>
</blockquote></td>
<td><blockquote>
<p>Len</p>
</blockquote></td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>R/O</p>
</blockquote></td>
<td><blockquote>
<p>Element Name</p>
</blockquote></td>
<td><blockquote>
<p>Values (lower case=variable)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>3</td>
<td>2</td>
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>VALUE TYPE</p>
</blockquote></td>
<td><blockquote>
<p>Type of data contained in result</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>CE</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>OBSERVATION ID</p>
</blockquote></td>
<td><blockquote>
<p>Identifier for result data</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td>6</td>
<td><blockquote>
<p>65536</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>RESULT</p>
</blockquote></td>
<td><blockquote>
<p>Data</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td>7</td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>UNITS</p>
</blockquote></td>
<td><blockquote>
<p>Unit of measure for result</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VALUE TYPE: Allowable result data types include: CD = Channel definition, CE = Coded entry, ED = Encapsulated data, FT = Formatted text, MA = Multiplexed array, NA = Numeric array, NM = Numeric data, RP = Reference pointer, ST = String data, TS = Timestamp, TX = Text.

> OBSERVATION ID: Identifiers can be text (i.e. “Height”, “Weight”), or codes that are pointers to an observation identifier global.

> RESULT: Data field that holds the result value for the identifier in observation ID. UNITS: Unit of measure used in conjunction with value and observation ID above.

> MSA table

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 29%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Seq</p>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>M</p>
<p>piece</p>
</blockquote></td>
<td><blockquote>
<p>Len</p>
</blockquote></td>
<td><blockquote>
<p>DT</p>
</blockquote></td>
<td><blockquote>
<p>R/O</p>
</blockquote></td>
<td><blockquote>
<p>Element Name</p>
</blockquote></td>
<td><blockquote>
<p>Values (lower case=variable)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
<p>3</p>
</blockquote></td>
<td><p>2</p>
<p>20</p></td>
<td><blockquote>
<p>ID</p>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>R</p>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>ACKNOWLEDGEMENT CODE</p>
<p>MESSAGE CONTROL ID</p>
</blockquote></td>
<td><blockquote>
<p>AA or AR</p>
<p>Message identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>TEXT MESSAGE</p>
</blockquote></td>
<td><blockquote>
<p>Reason report was rejected</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ACKNOWLEDGEMENT CODE: Code signifying that a message has been accepted (AA), or rejected (AR) by VISTA.

> MESSAGE CONTROL ID: Unique alphanumeric identifier sent by the instrument in the

> MSH segment and returned in the acknowledgement segment. TEXT MESSAGE: The reason why a report was rejected.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Atrial A term for the left and right upper chamber of the heart.
> Clinical Instrument An instrument (device) that generates reports and other data dealing with a specific type of test for the patient.
> Clinical Instrument An interface designed to support the exchange of data between a clinical
> Interface instrument and the Medicine package.
> Device Type The type of test performed and reported on by a specific clinical instrument (e.g., pulmonary, endoscope).
> Device Vendor The company that designs clinical instruments (devices) that generate reports and other data dealing with a specific type of test (e.g., Sensormedics, Medgraphics).
> HL7 Health Level Seven. A messaging standard that forms the basis for the exchange of health care information between VISTA systems and non- VISTA systems that generate results information in the form of reports and impressions.
> HL7 Messages A unit of data transferred between systems that is comprised of a group of segments in a defined sequence.
> HL7 Segments A logical grouping of data fields contained in an HL7 message. Instrument Code The identifying code transmitted by the clinical instrument.
> Mitral The cardiac valve located between the left atrium and left ventricle. Morphology The shape or form of a P, QRS, or T wave.
> Pulmonary A reference to the part of circulation supplied by the pulmonary artery. Systemic A reference to the part of circulation supplied by the aorta.
> TCP/IP Transport Communication Protocol/ Internet Protocol. The leading standard of communication between computers in a networked environment.
> Ventricular A term for the left or right lower chamber of the heart.
> 1 Patch MC\*2.3\*24 December 2000 This entire glossary has been changed.
> VISTA Veterans Health Information Systems and Technology Architecture.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A
> archiving, 39
> Archiving and Purging, 39
> Automated Instrument Interface, 39
> C
> Callable Routines, 41
> Cardiology Management Menu, 6
> Cardiology menu, 39
> Clinical Instrument Interface Specifications, 67 cMore, 70
> D
> DBI Agreements by Subscriber, 44
> DelMar, 70
> DRAFT, 15
> E
> ECG Transfer Record Delete., 39
> Electronic Signatures, 13
> Exported Options, 33
> External Relations, 43
> F
> File List, 25
> File Security, 11
> Functional Description, 1
> G
> Generalized Procedure Menu, 7
> GI Management Menu, 6
> 1 Patch MC\*2.3\*24 December 2000 This entire index is new material.
> H
> HL Logical Link file, 71
> HL7 Application Parameter file, 71
> HL7 Data Formats, 75
> Holter Transfer Record Delete, 39
> How to Generate On-line Documentation, 67
> I
> Implementation, 3
> Implementation and Maintenance, 3
> Interfacing with New Devices, 74
> Internal Relations, 63
> J
> Journaling, 7
> M
> Maintenance, 7
> Marquette, 70
> MCORMNO routine, 41
> Medgraphics, 70
> Medicine Custodial DBI Agreements, 58
> Menu Option Assignment, 12
> MSA table, 81
> MSH table, 77
> N
> Name/Number Spacing, 7
> O
> OBR table, 79
> OBX table, 80
> Olympus, 70
Index
> P
> Package-wide Variables, 65
> Patch MC\*2.3\*24, 67
> PID table, 78
> PROBLEM DRAFT, 15
> Protocol file, 72
> Pulmonary Management Menu, 6 purging, 39
> R
> Reindexing, 9
> Related Manuals, 1
> Release Control, 13
> Release Control Options, 4, 15
> RELEASED NOT VERIFIED, 15
> RELEASED OFF-LINE VERIFIED, 15
> RELEASED ON-LINE VERIFIED, 15
> Routine List, 19
> Routines, 7
> S
> SACC Exemptions, 43 screen edit driver, 3
> Screen Handler Files, 8
> Security, 11
> Security (Release Control) Keys, 13
> Sensormedics, 70
> Subspecialty, 15
> SUPERSEDED, 15
> T
> Terminal Type file, 3
